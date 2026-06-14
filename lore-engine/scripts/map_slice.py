#!/usr/bin/env python3
"""Throwaway helper for the maps cleanup: print a line/column slice of raw maps.md
so ASCII art can be transcribed faithfully into data/gs1/gs1_maps.md.

Usage:
    python map_slice.py <start> <end> [colstart] [colend] [--rstrip] [--ltrim]

  start/end : 1-indexed inclusive line numbers in raw/gs1/maps.md
  colstart  : 0-indexed column to start each line (default 0)
  colend    : 0-indexed column to end each line, exclusive (default end of line)
  --rstrip  : strip trailing whitespace from each emitted line
  --ltrim   : remove the common leading whitespace across all emitted lines
"""
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

RAW = Path(__file__).resolve().parent.parent / "raw" / "gs1" / "maps.md"

def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    flags = {a for a in sys.argv[1:] if a.startswith("--")}
    start = int(args[0]); end = int(args[1])
    colstart = int(args[2]) if len(args) > 2 else 0
    colend = int(args[3]) if len(args) > 3 else None

    lines = RAW.read_text(encoding="utf-8").splitlines()
    chunk = lines[start - 1:end]
    sliced = [ln[colstart:colend] if colend is not None else ln[colstart:] for ln in chunk]
    if "--rstrip" in flags:
        sliced = [ln.rstrip() for ln in sliced]
    if "--ltrim" in flags:
        nonempty = [ln for ln in sliced if ln.strip()]
        pad = min((len(ln) - len(ln.lstrip()) for ln in nonempty), default=0)
        sliced = [ln[pad:] for ln in sliced]
    sys.stdout.write("\n".join(sliced) + "\n")

if __name__ == "__main__":
    main()
