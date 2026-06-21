#!/usr/bin/env python3
"""Lore-Engine extraction pipeline.

Reads the entity-relevant section of the data schema plus the raw source files
listed in the schema's Master Source IDs table, sends them to Claude, and writes
the extracted entries to data/{game}/{entity}.json.

Usage:
    python scripts/extract.py --entity bosses
    python scripts/extract.py --entity djinn --game gs1
    python scripts/extract.py --entity bosses --dry-run   # no API call

Requires: anthropic, python-dotenv  (pip install anthropic python-dotenv)
An ANTHROPIC_API_KEY must be present in <repo-root>/.env (or the environment).
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path

import anthropic
from dotenv import load_dotenv

# The user specified this model. It is the exact, complete model ID — do not
# append a date suffix. Sonnet 4.6 supports adaptive thinking and streaming.
MODEL = "claude-sonnet-4-6"
MAX_TOKENS = 64000  # Sonnet 4.6 streaming ceiling; JSON output can be large.

# Repo root is the parent of the scripts/ directory (contains schema/, raw/, data/).
REPO_ROOT = Path(__file__).resolve().parent.parent


def log(msg: str) -> None:
    """Print a status line to stderr so stdout stays clean."""
    print(msg, file=sys.stderr)


def extract_schema_section(schema_text: str, entity: str) -> str:
    r"""Return the ``## Schema: `{entity}` `` section, up to the next H2 heading.

    H3 subsections (field defs, Damage Format, examples, Notes for CC) nested
    under the entity's H2 are included; the next `## ` heading ends the section.
    """
    lines = schema_text.splitlines()
    heading = re.compile(r"^##\s+Schema:\s+`?" + re.escape(entity) + r"`?\s*$", re.IGNORECASE)
    start = next((i for i, ln in enumerate(lines) if heading.match(ln)), None)
    if start is None:
        raise ValueError(
            f"No '## Schema: {entity}' section found in the schema file. "
            f"Check the --entity value."
        )
    end = next(
        (i for i in range(start + 1, len(lines)) if re.match(r"^##\s+", lines[i])),
        len(lines),
    )
    return "\n".join(lines[start:end]).strip()


def parse_master_source_ids(schema_text: str) -> list[str]:
    """Return the source IDs from the Master Source IDs table (backticked first cell)."""
    ids: list[str] = []
    in_table = False
    for ln in schema_text.splitlines():
        if re.match(r"^###\s+Master Source IDs", ln, re.IGNORECASE):
            in_table = True
            continue
        if in_table:
            if ln.startswith("## ") or ln.startswith("### "):
                break  # left the section
            m = re.match(r"^\|\s*`([^`]+)`\s*\|", ln)
            if m:
                ids.append(m.group(1))
    return ids


def resolve_source_files(source_ids: list[str], raw_dir: Path) -> tuple[list[Path], list[str]]:
    """Map each source ID to at most one raw file by token matching against filenames.

    The source ID is split on hyphens/underscores into tokens; a file is a
    candidate only when *every* token appears as a substring of its normalized
    stem (a full match). Among candidates, the most specific match wins:

      1. highest specificity score (number of source-ID tokens present), then
      2. shortest normalized stem (the more general file), then
      3. alphabetical normalized stem (deterministic final tie-break).

    e.g. "fandom-tret" -> {fandom, tret} -> "FandomWiki - Tret.txt"; "fandom-wiki"
    -> {fandom, wiki} matches every FandomWiki file, so the shortest stem wins
    ("FandomWiki - Boss.txt"). Source IDs with no candidate are returned as
    unmatched. Returns the de-duplicated union of matched files and the unmatched IDs.

    LEGACY / FLAT-LAYOUT ONLY: the glob below is non-recursive, so this resolves
    sources only when raw files sit directly in `raw/{game}/` (the gs1 layout).
    The gs2 corpus is nested under `raw/gs2/Guide and Walkthrough/` and
    `raw/gs2/In-Depth Guides/`, so `extract.py --game gs2` resolves *zero* files
    and is effectively dead. That is intentional and not maintained: gs2 was
    extracted with the dedicated, per-entity `scripts/*_extract_gs2.py` scripts
    (which read the subfolders directly), and that is the path to use for gs2.
    If the generic path is ever revived for nested corpora, switch to `rglob`.
    """
    files = sorted(p for p in raw_dir.glob("*.txt")) + sorted(p for p in raw_dir.glob("*.md"))
    norm = {f: re.sub(r"[^a-z0-9]", "", f.stem.lower()) for f in files}

    matched: dict[Path, None] = {}  # ordered set
    unmatched_ids: list[str] = []
    for sid in source_ids:
        tokens = [t for t in re.split(r"[-_]", sid.lower()) if t]
        candidates = [f for f in files if all(t in norm[f] for t in tokens)]
        if not candidates:
            unmatched_ids.append(sid)
            continue
        best = min(
            candidates,
            key=lambda f: (-sum(t in norm[f] for t in tokens), len(norm[f]), norm[f]),
        )
        matched[best] = None
    return list(matched.keys()), unmatched_ids


def build_prompt(entity: str, schema_section: str, raw_files: list[tuple[str, str]]) -> str:
    """Assemble the focused extraction prompt: schema + raw content + JSON-only instruction."""
    parts = [
        f"You are extracting structured `{entity}` data for the Lore-Engine project.",
        "",
        "## Schema",
        "",
        "Follow this schema exactly — field names, types, rules, and examples:",
        "",
        schema_section,
        "",
        "## Raw source files",
        "",
    ]
    for filename, content in raw_files:
        parts += [f"### Source file: {filename}", "", content, ""]
    parts += [
        "## Task",
        "",
        f"Extract ALL `{entity}` entries from the raw source files, following the schema "
        "above. Return ONLY valid JSON — a single JSON array of entry objects. "
        "Do not include any prose, explanation, or markdown code fences.",
    ]
    return "\n".join(parts)


def strip_code_fences(text: str) -> str:
    """Defensively remove a leading/trailing ```json ... ``` fence if present."""
    t = text.strip()
    if t.startswith("```"):
        t = re.sub(r"^```[a-zA-Z0-9]*\s*", "", t)
        t = re.sub(r"\s*```$", "", t)
    return t.strip()


def call_claude(prompt: str) -> str:
    """Stream a completion from Claude and return the concatenated text output."""
    client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY from the environment
    text_parts: list[str] = []
    with client.messages.stream(
        model=MODEL,
        max_tokens=MAX_TOKENS,
        messages=[{"role": "user", "content": prompt}],
    ) as stream:
        message = stream.get_final_message()
    for block in message.content:
        if block.type == "text":
            text_parts.append(block.text)
    return "".join(text_parts)


def main() -> int:
    ap = argparse.ArgumentParser(description="Lore-Engine extraction pipeline.")
    ap.add_argument("--entity", required=True, help='e.g. "djinn" or "bosses"')
    ap.add_argument("--game", default="gs1", help='e.g. "gs1" (default: "gs1")')
    ap.add_argument(
        "--dry-run",
        action="store_true",
        help="Resolve schema and raw files and report, but do not call the API.",
    )
    args = ap.parse_args()
    entity, game = args.entity, args.game

    # 1. Load ANTHROPIC_API_KEY from .env in the repo root.
    env_path = REPO_ROOT / ".env"
    load_dotenv(env_path)
    if env_path.exists():
        log(f"Loaded environment from {env_path}")
    else:
        log(f"WARNING: no .env file at {env_path}")
    have_key = bool(os.environ.get("ANTHROPIC_API_KEY"))

    # 2. Read the schema and extract the entity-relevant section.
    schema_path = REPO_ROOT / "schema" / f"{game}_schema.md"
    if not schema_path.exists():
        log(f"ERROR: schema file not found: {schema_path}")
        return 1
    schema_text = schema_path.read_text(encoding="utf-8")
    try:
        schema_section = extract_schema_section(schema_text, entity)
    except ValueError as e:
        log(f"ERROR: {e}")
        return 1
    log(f"Extracted schema section for '{entity}' ({len(schema_section)} chars)")

    # 3. Read the raw source files listed in the Master Source IDs table.
    source_ids = parse_master_source_ids(schema_text)
    if not source_ids:
        log("ERROR: no Master Source IDs table found in the schema.")
        return 1
    log(f"Master Source IDs: {', '.join(source_ids)}")

    raw_dir = REPO_ROOT / "raw" / game
    if not raw_dir.is_dir():
        log(f"ERROR: raw directory not found: {raw_dir}")
        return 1
    files, unmatched = resolve_source_files(source_ids, raw_dir)
    for sid in unmatched:
        log(f"WARNING: source ID '{sid}' matched no file on disk — skipping.")
    if not files:
        log("ERROR: no source files resolved from the Master Source IDs table.")
        return 1

    raw_files: list[tuple[str, str]] = []
    for f in files:
        raw_files.append((f.name, f.read_text(encoding="utf-8", errors="replace")))
        log(f"Read raw source file: {f.name}")

    prompt = build_prompt(entity, schema_section, raw_files)
    log(f"Built prompt ({len(prompt)} chars) from {len(raw_files)} source file(s).")

    out_dir = REPO_ROOT / "data" / game
    out_path = out_dir / f"{entity}.json"

    if args.dry_run:
        log("--dry-run: skipping API call.")
        log(f"Would call model '{MODEL}' and write to {out_path}")
        if not have_key:
            log("Note: ANTHROPIC_API_KEY is not set — a real run would fail.")
        return 0

    if not have_key:
        log("ERROR: ANTHROPIC_API_KEY is not set (checked .env and environment).")
        return 1

    # 4. Call Claude.
    try:
        raw_response = call_claude(prompt)
    except anthropic.APIError as e:
        log(f"ERROR: Claude API call failed: {e}")
        return 1
    except Exception as e:  # network, timeout, etc.
        log(f"ERROR: extraction request failed: {e}")
        return 1

    # 5. Parse the JSON response and write it out.
    out_dir.mkdir(parents=True, exist_ok=True)
    cleaned = strip_code_fences(raw_response)
    try:
        data = json.loads(cleaned)
    except json.JSONDecodeError as e:
        debug_path = out_dir / f"{entity}_raw_response.txt"
        debug_path.write_text(raw_response, encoding="utf-8")
        log(f"ERROR: response was not valid JSON: {e}")
        log(f"Raw response saved to {debug_path} for debugging.")
        return 1

    out_path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    # 6. Print a summary.
    count = len(data) if isinstance(data, list) else 1
    print(f"Wrote {count} entr{'y' if count == 1 else 'ies'} to {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
