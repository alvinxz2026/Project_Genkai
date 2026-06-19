#!/usr/bin/env python3
"""Deterministic chapter index for the gs2 walkthrough consolidation pipeline.

Reads the *derived* per-chapter layer produced by walkthrough_split.py
(raw/gs2/_chapters/<source>/NN-slug.md) and dumps every chapter's frontmatter
(plus body size) into one queryable index. No LLM, free, re-runnable.

This is step 0 of the consolidation pipeline (see
docs/gs2/walkthrough_consolidation_plan.md): the index is the raw material the
region spine + mapping (region_spine_gs2.py) is built on.

  python scripts/walkthrough_index_gs2.py            # write JSON + md table
  python scripts/walkthrough_index_gs2.py --prose     # only prose-walkthrough rows to stdout

Outputs:
  data/gs2/intermediate/walkthrough_chapter_index.json
  data/gs2/intermediate/walkthrough_chapter_index.md   (human-readable table)
"""
import argparse
import json
import re
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
CHAPTERS = REPO / "raw" / "gs2" / "_chapters"
OUT_DIR = REPO / "data" / "gs2" / "intermediate"

# scalar frontmatter keys we lift verbatim
SCALARS = ("source_id", "parent", "chapter_no", "toc_path", "title",
           "source_lines", "kind", "region")


def parse_frontmatter(text):
    """Return (frontmatter dict, body_line_count). Frontmatter is the block
    between the first two '---' lines. Minimal parser: scalars + the one flow
    list we use (covers: [a, b])."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, len(lines)
    end = next((i for i in range(1, len(lines)) if lines[i].strip() == "---"), None)
    if end is None:
        return {}, len(lines)
    fm = {}
    for ln in lines[1:end]:
        m = re.match(r"^([a-z_]+):\s*(.*)$", ln)
        if not m:
            continue
        key, val = m.group(1), m.group(2).strip()
        if key == "covers":
            inner = val.strip().lstrip("[").rstrip("]").strip()
            fm["covers"] = [t.strip() for t in inner.split(",") if t.strip()] if inner else []
        else:
            fm[key] = val.strip().strip('"')
    body_lines = len(lines[end + 1:])
    return fm, body_lines


def collect():
    rows = []
    for src_dir in sorted(p for p in CHAPTERS.iterdir() if p.is_dir()):
        for f in sorted(src_dir.glob("*.md")):
            fm, body_lines = parse_frontmatter(f.read_text(encoding="utf-8"))
            # source_lines "1426-1520" -> raw line span
            span = None
            if fm.get("source_lines") and "-" in fm["source_lines"]:
                a, b = fm["source_lines"].split("-", 1)
                if a.isdigit() and b.isdigit():
                    span = int(b) - int(a) + 1
            row = {k: fm.get(k) for k in SCALARS}
            row["covers"] = fm.get("covers", [])
            row["file"] = str(f.relative_to(REPO)).replace("\\", "/")
            row["raw_lines"] = span
            row["body_lines"] = body_lines
            if row["chapter_no"] and row["chapter_no"].isdigit():
                row["chapter_no"] = int(row["chapter_no"])
            rows.append(row)
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--prose", action="store_true",
                    help="print only prose-walkthrough rows to stdout, no write")
    args = ap.parse_args()

    rows = collect()

    if args.prose:
        for r in rows:
            if r["kind"] == "prose-walkthrough":
                print(f'{r["source_id"]:>14}  {r["chapter_no"]:>3}  '
                      f'{(r["region"] or ""):<26}  {r["title"]}')
        return

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "walkthrough_chapter_index.json").write_text(
        json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")

    # summary + markdown table
    by_src, by_kind = {}, {}
    for r in rows:
        by_src.setdefault(r["source_id"], {"total": 0, "prose": 0})
        by_src[r["source_id"]]["total"] += 1
        if r["kind"] == "prose-walkthrough":
            by_src[r["source_id"]]["prose"] += 1
        by_kind[r["kind"]] = by_kind.get(r["kind"], 0) + 1

    md = ["# gs2 walkthrough chapter index (generated)\n",
          f"Total chapters: **{len(rows)}** across {len(by_src)} sources.\n",
          "kind: " + ", ".join(f"{k}={v}" for k, v in sorted(by_kind.items())) + "\n",
          "| source | chapters | prose-walkthrough |", "|---|---|---|"]
    for s in sorted(by_src):
        md.append(f"| {s} | {by_src[s]['total']} | {by_src[s]['prose']} |")
    md.append("\n## prose-walkthrough chapters (the 2a / locations corpus)\n")
    md.append("| source | ch | region | title | raw_lines |")
    md.append("|---|---|---|---|---|")
    for r in rows:
        if r["kind"] == "prose-walkthrough":
            md.append(f'| {r["source_id"]} | {r["chapter_no"]} | '
                      f'{r["region"] or ""} | {r["title"]} | {r["raw_lines"]} |')
    (OUT_DIR / "walkthrough_chapter_index.md").write_text("\n".join(md) + "\n",
                                                          encoding="utf-8")

    print(f"wrote {len(rows)} chapters -> {OUT_DIR/'walkthrough_chapter_index.json'}")
    print("by source:")
    for s in sorted(by_src):
        print(f"  {s:>14}  {by_src[s]['total']:>3} total  "
              f"{by_src[s]['prose']:>3} prose")
    print("by kind: " + ", ".join(f"{k}={v}" for k, v in sorted(by_kind.items())))


if __name__ == "__main__":
    main()
