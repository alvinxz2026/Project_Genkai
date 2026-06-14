#!/usr/bin/env python3
"""Extract a Shotgunnova-style map: separate the ASCII art from the numbered
item table that sits beside it. Throwaway helper for the maps cleanup.

Usage:
    python map_extract.py <start> <end> [--table left|right] [--ltrim]

  start/end : 1-indexed inclusive line range (the code-block body) in raw/gs1/maps.md
  --table   : which side the | NN | Item | table is on (default: right)
  --ltrim   : strip common leading whitespace from the map (use for --table left)

Prints the cleaned MAP block, then the parsed ITEMS list.
The map is everything on the OTHER side of the table; trailing whitespace stripped.
"""
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
RAW = Path(__file__).resolve().parent.parent / "raw" / "gs1" / "maps.md"

# table data row, e.g. "| 01 | Lucky Medal     |"
ROW = re.compile(r"\|\s*(\d+)\s*\|\s*([^|]*?)\s*\|")


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    side = "right"
    if "--table" in sys.argv:
        side = sys.argv[sys.argv.index("--table") + 1]
    ltrim = "--ltrim" in sys.argv

    start, end = int(args[0]), int(args[1])
    lines = RAW.read_text(encoding="utf-8").splitlines()[start - 1:end]

    # collect every table-like match, but the REAL table is a vertical stack
    # aligned at one column. Map cells like "| 1 |" are scattered, so the
    # table's leading-'|' column is the modal start column.
    from collections import Counter
    matches = []
    for ln in lines:
        for m in ROW.finditer(ln):
            if re.search(r"[A-Za-z]", m.group(2)):  # item text has a letter
                matches.append(m)
    if not matches:
        print("!! no table rows found", file=sys.stderr)
        cut_l = cut_r = None
        rows = []
    else:
        cut_l = Counter(m.start() for m in matches).most_common(1)[0][0]
        rows = [m for m in matches if m.start() == cut_l]
        cut_r = max(m.end() for m in rows)
    items = [(m.group(1), m.group(2)) for m in rows]

    # blank only the table rectangle (its row span + one border row each side),
    # so map content that wraps above/below a corner table is preserved.
    tlines = [i for i, ln in enumerate(lines) if ROW.search(ln) and ROW.search(ln).start() == cut_l] if cut_l is not None else []
    lo, hi = (min(tlines) - 1, max(tlines) + 1) if tlines else (None, None)
    art = []
    for i, ln in enumerate(lines):
        if lo is not None and lo <= i <= hi:
            if side == "right":
                # blank only the table's column span; keep any map to its right
                ln = ln[:cut_l] + " " * (cut_r - cut_l) + ln[cut_r:]
            else:
                ln = ln[cut_r:]
        elif side == "left" and cut_r is not None:
            ln = ln[cut_r:]
        art.append(ln.rstrip())
    if side == "left" or ltrim:
        ne = [a for a in art if a.strip()]
        pad = min((len(a) - len(a.lstrip()) for a in ne), default=0)
        art = [a[pad:] for a in art]

    print("--- MAP ---")
    print("\n".join(art))
    print("--- ITEMS ---")
    for num, txt in items:
        print(f"| {num} | {txt} |")


if __name__ == "__main__":
    main()
