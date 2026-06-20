"""Backfill the Tamer-family classes' psynergy learn-lists from autocon.

The four Trainer's-Whip item classes — Tamer -> Trainer -> Beastkeeper ->
Beast Lord — learn DIFFERENT psynergy per sub-class, laid out in autocon as a
single fixed-width level matrix (one column per sub-class). classes_ultimalink_gs2
explicitly defers this (`DEFER_PSYNERGY = {"tamer"}`) because ultimalink's
side-by-side pair tables are messy; autocon's 4-column matrix is clean:

    Lvl Psynergy
       Tamer          Trainer        Beastkeeper    Beast Lord
    --+-----------    -----------    -----------    -----------
     1|Wild Wolf      Orc            Dinox          Troll
     5|Cure Poison    Cure Poison    Cure Poison    Cure Poison
    10|Salamander     Cerberus       Chimera        Macetail
    ...
    45|Roc            Grand Golem    Living Armor   Ghost Soldier

Cells are `\\s{2,}`-separated (psynergy names contain single spaces, e.g.
"Cure Poison", "Ghost Soldier"); `-----` = not learned at that level. We write
{name, level, sources:["autocon"]} into each class's psynergy[]; `id` is left for
links_normalize_gs2 to resolve by name (the psynergy entities already exist —
added via psynergy_appendix_gs2). Format matches the ultimalink-sourced rows on
other classes.

Idempotent: drops prior source=="autocon" psynergy on the four classes first.
Run before links_normalize. Usage: python scripts/classes_tamer_psynergy_gs2.py
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "gs2"
SRC = ROOT / "raw" / "gs2" / "_chapters" / "autocon" / "218-tamer.md"

# column order in the matrix -> class id
COL_IDS = ["tamer", "trainer", "beastkeeper", "beast-lord"]
ROW = re.compile(r"^\s*(\d+)\|(.+)$")


def parse_matrix():
    """Return {class_id: [(name, level), ...]} from the autocon Learns matrix."""
    learned = {cid: [] for cid in COL_IDS}
    in_matrix = False
    for raw in SRC.read_text(encoding="utf-8").splitlines():
        line = raw.rstrip()
        if line.startswith("Learns:"):
            in_matrix = True
            continue
        if not in_matrix:
            continue
        if line.startswith("="):  # trailing "=====" ends the block
            break
        m = ROW.match(line)
        if not m:
            continue
        level = int(m.group(1))
        cells = re.split(r"\s{2,}", m.group(2).strip())
        if len(cells) != len(COL_IDS):
            print(f"  WARN: row L{level} has {len(cells)} cols (expected "
                  f"{len(COL_IDS)}): {cells}", file=sys.stderr)
            continue
        for cid, cell in zip(COL_IDS, cells):
            name = cell.strip()
            if name and set(name) != {"-"}:  # "-----" = not learned
                learned[cid].append((name, level))
    return learned


def main():
    classes = json.loads((DATA / "classes.json").read_text(encoding="utf-8"))
    by_id = {c["id"]: c for c in classes}

    missing = [cid for cid in COL_IDS if cid not in by_id]
    if missing:
        print(f"ERROR: class ids not found: {missing}", file=sys.stderr)
        return 1

    learned = parse_matrix()
    added = 0
    for cid in COL_IDS:
        cls = by_id[cid]
        # idempotency: drop prior autocon-sourced psynergy
        cls["psynergy"] = [p for p in cls.get("psynergy", [])
                           if "autocon" not in p.get("sources", [])]
        for name, level in learned[cid]:
            cls["psynergy"].append({"name": name, "id": None, "level": level,
                                    "sources": ["autocon"]})
            added += 1
        cls["psynergy"].sort(key=lambda p: (p.get("level") or 0, p["name"]))

    (DATA / "classes.json").write_text(
        json.dumps(classes, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    counts = {cid: len(learned[cid]) for cid in COL_IDS}
    print(f"classes_tamer_psynergy_gs2 — added {added} psynergy across "
          f"{len(COL_IDS)} Tamer classes: {counts}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
