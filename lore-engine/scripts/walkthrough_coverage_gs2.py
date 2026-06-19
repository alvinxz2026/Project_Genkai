#!/usr/bin/env python3
"""Coverage / QA gate for the gs2 walkthrough consolidation (2a).

2a is the only GENERATIVE step in the gs2 pipeline (split + the data parsers are
deterministic & verifiable; merging prose from 10 sources is not). This is the
lightweight gate that keeps it honest. Two layers:

  PRE-2a  (mapping integrity, always):
    - every prose chapter is assigned to >=1 spine node (no orphans)
    - no spine node is empty (every node has source material)

  POST-2a (output completeness, when data/gs2/walkthrough/ has files):
    - every expected node (main/side/postgame) has a consolidated file
    - each file's frontmatter `region_id` is a real spine node
    - each file's `sources:` is a SUBSET of that node's mapped chapters
      (provenance integrity — no source pulled in that wasn't mapped here)

  python scripts/walkthrough_coverage_gs2.py            # full report; exit 1 on FATAL

Run region_spine_gs2.py first (this reads its output).
"""
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SPINE_JSON = REPO / "data" / "gs2" / "intermediate" / "region_spine.json"
OUT_DIR = REPO / "data" / "gs2" / "walkthrough"

# node kinds that MUST get a consolidated file in 2a (overworld/reference are
# cross-cutting buckets, distributed into other files, so not required to stand alone)
REQUIRED_KINDS = {"main", "side", "postgame"}


def parse_fm(text):
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    end = next((i for i in range(1, len(lines)) if lines[i].strip() == "---"), None)
    if end is None:
        return {}
    fm, key = {}, None
    for ln in lines[1:end]:
        m = re.match(r"^([a-z_]+):\s*(.*)$", ln)
        if m:
            key, val = m.group(1), m.group(2).strip()
            if val.startswith("[") and val.endswith("]"):
                inner = val[1:-1].strip()
                fm[key] = [t.strip().strip('"') for t in inner.split(",") if t.strip()]
            elif val == "":
                fm[key] = []  # block list follows
            else:
                fm[key] = val.strip('"')
        else:
            m2 = re.match(r"^\s*-\s*(.+)$", ln)
            if m2 and key and isinstance(fm.get(key), list):
                fm[key].append(m2.group(1).strip().strip('"'))
    return fm


def main():
    if not SPINE_JSON.exists():
        print("FATAL: run scripts/region_spine_gs2.py first")
        sys.exit(1)
    data = json.load(open(SPINE_JSON, encoding="utf-8"))
    spine = data["spine"]
    by_id = {n["id"]: n for n in spine}
    fatal, warn = [], []

    # ---- PRE-2a: mapping integrity ----
    if data["unmatched"]:
        fatal.append(f"{len(data['unmatched'])} prose chapters unmatched (orphans)")
    empty = [n["id"] for n in spine if not n["chapters"]]
    if empty:
        fatal.append(f"empty spine nodes: {', '.join(empty)}")

    print(f"PRE-2a mapping: {data['stats']['assigned']}/{data['stats']['prose_chapters']} "
          f"prose chapters assigned, {len(spine)} nodes, "
          f"{len(empty)} empty, {len(data['unmatched'])} unmatched")

    # ---- POST-2a: output completeness ----
    out_files = sorted(OUT_DIR.glob("*.md")) if OUT_DIR.exists() else []
    if not out_files:
        print("POST-2a output: none yet (data/gs2/walkthrough/ empty) — pre-2a only")
    else:
        seen = {}
        for f in out_files:
            fm = parse_fm(f.read_text(encoding="utf-8"))
            rid = fm.get("region_id")
            if rid not in by_id:
                fatal.append(f"{f.name}: region_id {rid!r} not a spine node")
                continue
            seen[rid] = f.name
            mapped = {c["file"] for c in by_id[rid]["chapters"]}
            for s in fm.get("sources", []):
                if s not in mapped:
                    fatal.append(f"{f.name}: source {s!r} not mapped to node {rid}")
        required = [n["id"] for n in spine if n["kind"] in REQUIRED_KINDS]
        missing = [r for r in required if r not in seen]
        if missing:
            warn.append(f"{len(missing)} required nodes have no file yet: "
                        + ", ".join(missing))
        print(f"POST-2a output: {len(out_files)} files, "
              f"{len(seen)}/{len(required)} required nodes covered")

    print()
    for w in warn:
        print("WARN : " + w)
    for e in fatal:
        print("FATAL: " + e)
    if fatal:
        print(f"\n{len(fatal)} FATAL — gate FAILED")
        sys.exit(1)
    print("\ngate OK" + (f" ({len(warn)} warnings)" if warn else ""))


if __name__ == "__main__":
    main()
