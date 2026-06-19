"""Backfill djinn.location.area from the walkthrough-authoritative placement.

SSoT pass (task 4): djinn.json carries demooni's acquisition PROSE in
`location.description`, but `location.area` (the clean locations-FK field) was left
null/deferred. The consolidated 2a walkthrough is our authority for *placement*
(round-2 cross-check found 6 djinn where demooni names the nearest TOWN while the
walkthrough names the precise DUNGEON — the walkthrough is more precise). So this
fills `location.area` from `location_refs.json`'s resolved djinn index (the
walkthrough's `djinn_here` placements), leaving `description` (demooni) untouched.

`area` becomes a sorted list of region_ids (FK into locations.json). 3 djinn
(coal/crystal/serac) genuinely span two adjacent regions -> 2 ids; the rest get 1.

Deterministic + idempotent: recomputed from location_refs every run, byte-stable.
Run AFTER locations_refs_gs2.py (which produces location_refs.json).

Usage: python scripts/djinn_area_backfill_gs2.py
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "gs2"


def main():
    djinn = json.loads((DATA / "djinn.json").read_text(encoding="utf-8"))
    refs = json.loads((DATA / "location_refs.json").read_text(encoding="utf-8"))
    didx = refs["index"]["djinn"]  # djinn_id -> [region_id]

    filled = missing = 0
    for d in djinn:
        loc = d.get("location")
        if not loc:
            continue  # the 28 GS1-transferred djinn have no demooni location entry
        regions = didx.get(d["id"])
        if regions:
            loc["area"] = sorted(regions)
            filled += 1
        else:
            missing += 1
            print(f"  no walkthrough placement for djinn {d['id']!r} (area left as-is)")

    (DATA / "djinn.json").write_text(
        json.dumps(djinn, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"djinn.location.area backfilled: {filled} filled, {missing} unresolved "
          f"(of {sum(1 for d in djinn if d.get('location'))} with a location)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
