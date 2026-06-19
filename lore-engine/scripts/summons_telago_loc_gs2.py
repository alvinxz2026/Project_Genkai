"""Backfill summons.acquisition.location (clean place name) from telago ch. 25.

cooldude345 (the summon stat source) records acquisition.found_at as free prose
("Yampi Desert Cave, Defeat Bullrog") and leaves the clean `location` field null.
Telago's appendix chapter 25 (`raw/gs2/_chapters/telago/25-about-the-summon.md`)
"New Tablet Summons" table has a dedicated Location column (Zagan -> Indra Cavern,
Megaera -> Osenia Cave, ...). This deterministic parser reads it and fills the
13 combo (stone-tablet) summons' `location`. Base summons (1-4 of a single
element, no tablet) have no location and are left as-is.

Idempotent: re-derives location from telago each run. Run anytime.

Usage: python scripts/summons_telago_loc_gs2.py
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "gs2"
SRC = ROOT / "raw" / "gs2" / "_chapters" / "telago" / "25-about-the-summon.md"

# telago spelling -> summons.json spelling
ALIAS = {"haurus": "haures"}


def norm(s):
    return re.sub(r"[^a-z0-9]", "", s.lower())


def parse_locations():
    """spirit(norm) -> clean location, from the 'New Tablet Summons' table."""
    out = {}
    active = False
    for raw in SRC.read_text(encoding="utf-8").splitlines():
        line = raw.rstrip()
        if "New Tablet Summons" in line:
            active = True; continue
        if not active or not line.strip():
            continue
        # spirit | "N Type + N Type" | Element(Fire/Water/Wind/Earth) | Location
        m = re.match(r"^(?P<spirit>[A-Z]\S+)\s+\d.*?\s+"
                     r"(?P<elem>Fire|Water|Wind|Earth)\s+(?P<loc>\S.*)$", line)
        if m:
            key = norm(m["spirit"])
            out[ALIAS.get(key, key)] = m["loc"].strip()
    return out


def main():
    summons = json.loads((DATA / "summons.json").read_text(encoding="utf-8"))
    locs = parse_locations()

    filled, matched = 0, set()
    for s in summons:
        loc = locs.get(norm(s["name"]))
        if not loc:
            continue
        matched.add(norm(s["name"]))
        acq = s.get("acquisition") or {}
        acq["location"] = loc
        if acq.get("source") and "telago" not in acq.get("source", ""):
            acq["source"] = f"{acq['source']} + telago"
        elif not acq.get("source"):
            acq["source"] = "telago"
        s["acquisition"] = acq
        if "telago" not in s["sources"]:
            s["sources"].append("telago")
        filled += 1
    unmatched = sorted(k for k in locs if k not in matched)

    (DATA / "summons.json").write_text(json.dumps(summons, ensure_ascii=False, indent=2) + "\n",
                                       encoding="utf-8")
    print(f"summons_telago_loc_gs2 — location filled {filled}/{len(summons)} summons")
    print(f"  telago tablet locations parsed: {len(locs)}")
    if unmatched:
        print(f"  telago spirits not matched ({len(unmatched)}): {unmatched}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
