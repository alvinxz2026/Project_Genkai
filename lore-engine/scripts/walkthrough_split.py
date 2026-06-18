"""Deterministically split a gs2 Guide-and-Walkthrough into per-chapter files.

NO LLM. The raw walkthroughs are immutable; this writes a *derived* layer under
`raw/gs2/_chapters/<source_id>/NN-<slug>.md`, each chapter = a **byte-exact**
slice of the original with a YAML frontmatter header prepended (body unchanged).

How it splits: every walkthrough carries a standardized
`## TABLE OF CONTENTS ... END OF TABLE OF CONTENTS` block. We parse its entries
(roman / number / letter enumerated), then locate each entry's header in the
body. Header styles vary per author (decorated ``---|I. Introduction |-O``, bare
``A. Venus Lighthouse``, ``/\\ 1. The Character Guide /\\``), but in every case,
after stripping leading decoration, the line **starts with the entry's enumerator
+ title**. Matching on ``^<enum>[.)] <title-words-as-subsequence>`` is precise
(the enumerator prefix avoids prose false-positives) and format-agnostic.

Two expected mismatch classes are handled, not silently dropped:
  * **container entries** — a TOC grouping (e.g. "2. CONTINENT OF INDRA") that has
    no body header of its own; its located children cover the text. Reported as
    info, not a failure.
  * **author drift** — body renumbers/retitles a section vs the TOC (e.g. TOC
    "VI > 6 Legal info and Credits" but body "5. Legal Stuff and Credits"). Fixed
    by a per-source `ALIASES` override (toc_path -> the enum/title actually in the
    body). Genuinely-absent sections (unfinished guides) are left as known gaps.

Frontmatter written per chapter (mechanical layer only; semantic layer left blank
for a later Gemini tagging pass):
    source_id, parent, chapter_no, toc_path, title, source_lines (1-based,
    inclusive, into the ORIGINAL file — the provenance bridge back to raw),
    kind: "", covers: [], region: "".

  python scripts/walkthrough_split.py --source darkslime          # split one
  python scripts/walkthrough_split.py --source darkslime --verify # + check
  python scripts/walkthrough_split.py --list                      # known sources

`--verify` reconstructs the original body from the chapter slices and asserts it
is byte-identical, and reports any TOC entry whose header was not found.
"""
import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = ROOT / "raw" / "gs2" / "Guide and Walkthrough"
OUT_ROOT = ROOT / "raw" / "gs2" / "_chapters"

# source_id -> filename (all 10 gs2 Guide-and-Walkthrough sources).
SOURCES = {
    "autocon": "Guide and Walkthrough by Autocon.md",
    "cloud-blazer": "Guide and Walkthrough by Cloud_Blazer.md",
    "darkslime": "Guide and Walkthrough by Darkslime.md",
    "darthmarth": "Guide and Walkthrough by DarthMarth.md",
    "ikillkenny": "Guide and Walkthrough by Ikillkenny.md",
    "killerfusion": "Guide and Walkthrough by KillerFusion.md",
    "shotgunnova": "Guide and Walkthrough by Shotgunnova.md",
    "super-slash": "Guide and Walkthrough by Super_Slash.md",
    "telago": "Guide and Walkthrough by Telago.md",
    "strawhat": "Guide and Walkthrough by strawhat.md",
}

# Per-source overrides for entries the author renumbered/retitled in the body.
# toc_path -> (body_enum, body_title) to anchor on instead of the TOC's.
ALIASES = {
    "darkslime": {
        "VI > 5": ("4", "Conclusion"),
        "VI > 6": ("5", "Legal Stuff and Credits"),
    },
}

ENUM = r"(?:[IVXLC]+|[A-Z]|\d+)"
TOC_ENTRY = re.compile(rf"^(?P<indent>\s*)(?P<enum>{ENUM})[.)]\s+(?P<title>.+?)"
                       r"(?:\s*\(m?\w+\))?\s*$")


def words(s):
    return re.sub(r"[^a-z0-9]+", " ", s.lower()).split()


def is_subseq(small, big):
    it = iter(big)
    return all(w in it for w in small)


def strip_decoration(line):
    return re.sub(r"^[^A-Za-z0-9]+", "", line)


def split_frontmatter(lines):
    """Return index of first body line after a leading --- ... --- block (or 0)."""
    if lines and lines[0].strip() == "---":
        for i in range(1, len(lines)):
            if lines[i].strip() == "---":
                return i + 1
    return 0


def parse_toc(lines):
    """-> (entries, toc_end_line_index). entries: [{enum,title,depth,toc_path}]."""
    start = next(i for i, l in enumerate(lines) if "TABLE OF CONTENTS" in l)
    end = next(i for i, l in enumerate(lines[start:], start) if "END OF TABLE OF CONTENTS" in l)
    entries = []
    stack = []  # (indent, label) for toc_path
    for l in lines[start + 1:end]:
        m = TOC_ENTRY.match(l)
        if not m:
            continue
        indent = len(m.group("indent").expandtabs())
        enum, title = m.group("enum"), m.group("title").strip()
        while stack and stack[-1][0] >= indent:
            stack.pop()
        path = [s[1] for s in stack] + [enum]
        stack.append((indent, enum))
        entries.append({"enum": enum, "title": title, "depth": len(path),
                        "toc_path": " > ".join(path)})
    return entries, end


def find_anchor(body, start, enum, title):
    tw = words(title)
    pat = re.compile(rf"^{re.escape(enum)}[.)]\s+(.*)", re.I)
    for i in range(start, len(body)):
        m = pat.match(strip_decoration(body[i]))
        if m and is_subseq(tw, words(m.group(1))):
            return i
    return None


def slug(s):
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", s.lower())).strip("-")[:50]


def split_source(source_id, verify=False):
    path = RAW_DIR / SOURCES[source_id]
    text = path.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines(keepends=True)

    entries, toc_end = parse_toc(lines)
    body_start = toc_end + 1
    aliases = ALIASES.get(source_id, {})

    # mark container entries (a deeper entry immediately follows)
    for i, e in enumerate(entries):
        e["container"] = i + 1 < len(entries) and entries[i + 1]["depth"] > e["depth"]

    # locate each TOC entry's header line (in order, advancing the cursor)
    cursor = body_start
    missed = []
    for e in entries:
        enum, title = aliases.get(e["toc_path"], (e["enum"], e["title"]))
        idx = find_anchor(lines, cursor, enum, title)
        if idx is None:
            missed.append(e)
            e["line"] = None
        else:
            e["line"] = idx
            cursor = idx + 1

    located = [e for e in entries if e["line"] is not None]
    # chunk boundaries: [front preamble] + each located entry up to the next one
    bounds = [(0, located[0]["line"] if located else len(lines), None)]
    for k, e in enumerate(located):
        nxt = located[k + 1]["line"] if k + 1 < len(located) else len(lines)
        bounds[0] = (0, located[0]["line"], None) if k == 0 else bounds[0]
        bounds.append((e["line"], nxt, e))

    out_dir = OUT_ROOT / source_id
    out_dir.mkdir(parents=True, exist_ok=True)
    for f in out_dir.glob("*.md"):
        f.unlink()

    written = []
    for n, (a, b, e) in enumerate(bounds):
        body = "".join(lines[a:b])
        if e is None:
            title, toc_path, name = "(front matter)", "", "00-front"
        else:
            title, toc_path = e["title"], e["toc_path"]
            name = f"{n:02d}-{slug(title) or 'untitled'}"
        fm = (
            "---\n"
            f"source_id: {source_id}\n"
            f"parent: {SOURCES[source_id]}\n"
            f"chapter_no: {n}\n"
            f'toc_path: "{toc_path}"\n'
            f'title: "{title}"\n'
            f"source_lines: {a + 1}-{b}\n"
            "kind:        # prose-walkthrough | data-table | story | meta\n"
            "covers: []   # entities: locations | monsters | items | ...\n"
            "region:      # canonical game-progression region (fill at consolidation)\n"
            "---\n"
        )
        (out_dir / f"{name}.md").write_text(fm + body, encoding="utf-8")
        written.append((name, a + 1, b, title))

    print(f"[{source_id}] {len(entries)} TOC entries, {len(located)} located, "
          f"{len(written)} chapters -> {out_dir.relative_to(ROOT)}")
    containers = [e for e in missed if e["container"]]
    true_missed = [e for e in missed if not e["container"]]
    if containers:
        print(f"  i  {len(containers)} container entries (no own body header; "
              f"covered by children): {[e['toc_path'] for e in containers]}")
    if true_missed:
        print(f"  !! {len(true_missed)} entries NOT located (add ALIASES / known gap):")
        for e in true_missed:
            print(f"     - {e['toc_path']:18} {e['title']!r}")

    if verify:
        recon = "".join(
            "".join(lines[a:b]) for a, b, _ in bounds)
        assert recon == text, "RECONSTRUCTION MISMATCH — chapters are not byte-exact!"
        print("  verify: byte-exact reconstruction OK")
    return written, missed


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--source")
    ap.add_argument("--verify", action="store_true")
    ap.add_argument("--list", action="store_true")
    args = ap.parse_args()
    if args.list:
        for sid, fn in SOURCES.items():
            print(f"  {sid:14} {fn}")
        return
    if not args.source:
        ap.error("pass --source <id> (or --list)")
    split_source(args.source, verify=args.verify)


if __name__ == "__main__":
    main()
