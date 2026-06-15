"""C2: regenerate psynergy.json — add new sources, resolve pp_cost/range conflicts.

Resolution (per Conflict Resolution Policy): majority of all source votes;
ties broken by authority (tetzcatlipoca = psynergy numeric authority).
Existing numeric sources back the json value (or the recorded conflict.values);
new sources (super-slash, shotgunnova; bfgamer for pp only) add votes.

element/item-name conflicts (dull, force, carry) are hand-adjudicated below.
Rerunnable.
"""
import json
import re
from collections import Counter
from pathlib import Path

import psynergy_supplement as sup

ROOT = Path(__file__).resolve().parent.parent
PJ = ROOT / "data/gs1/psynergy.json"

NUMERIC_EXISTING = ["jiggyhunter", "tetzcatlipoca", "strawhat", "plz2bstfu-class"]
# authority order for numeric tie-breaks (highest first)
AUTH = ["tetzcatlipoca", "jiggyhunter", "plz2bstfu-class", "strawhat",
        "super-slash", "shotgunnova", "bfgamer"]

# hand-adjudicated non-numeric conflicts (element / item names)
SPECIAL = {
    "dull": {
        "field": "element",
        "values": {"jiggyhunter": "wind", "strawhat": "water"},
        "resolution": "authority",
        "note": "GS1 Dull is a Jupiter (wind) psynergy; jiggyhunter says wind, strawhat's 'water' is a known element typo.",
        "set": ("element", "wind"),
    },
    "force": {
        "field": "acquired_via_item.item",
        "values": {"tetzcatlipoca": "Orb of Force", "strawhat": "Force Gem"},
        "resolution": "unresolved",
        "note": "Same item named two ways; verify in-game.",
    },
    "carry": {
        "field": "acquired_via_item.item",
        "values": {"tetzcatlipoca": "Carry Stone", "strawhat": "Carry Gem"},
        "resolution": "unresolved",
        "note": "Same item named two ways; verify in-game.",
    },
}


def resolve(votes):
    """votes: {source: value} -> (resolved_value, resolution_label)."""
    counts = Counter(votes.values())
    maxc = max(counts.values())
    winners = [v for v, c in counts.items() if c == maxc]
    if len(winners) == 1:
        return winners[0], "majority"
    # tie -> highest-authority source among tied values
    for a in AUTH:
        if a in votes and votes[a] in winners:
            return votes[a], "authority"
    return winners[0], "majority"


def build_votes(p, field, new):
    """assemble {source: value} for a numeric field across existing + new sources."""
    votes = {}
    existing_conf = next((c for c in p.get("conflicts", []) if c["field"] == field), None)
    if existing_conf:
        votes.update(existing_conf["values"])
    else:
        jv = p[{"pp_cost": "pp_cost", "range": "range"}[field]]
        for s in NUMERIC_EXISTING:
            if s in p["sources"]:
                votes[s] = jv
    votes.update(new)  # new source votes (override only if same source — none overlap)
    return votes


def main():
    P = json.load(open(PJ, encoding="utf-8"))
    by_name = {}
    for p in P:
        by_name.setdefault(sup.norm(p["name"]), []).append(p)

    # gather new-source votes per psynergy id (reuse supplement parsers + matcher)
    nv = {p["id"]: {"pp_cost": {}, "range": {}} for p in P}
    srcmap = [("super-slash", sup.parse_superslash()),
              ("shotgunnova", sup.parse_shotgunnova()),
              ("bfgamer", sup.parse_bfgamer())]
    for srcname, data in srcmap:
        for nm, recs in data.items():
            recs = recs if isinstance(recs, list) else [recs]
            for rec in recs:
                e = sup.match(nm, by_name, rec.get("pp"))
                if not e:
                    continue
                if rec.get("pp") is not None:
                    nv[e["id"]]["pp_cost"][srcname] = rec["pp"]
                if rec.get("range") is not None and srcname != "bfgamer":
                    nv[e["id"]]["range"][srcname] = rec["range"]

    changed = []
    resolved_log = []
    for p in P:
        conflicts = []
        # numeric fields
        for field, key in (("pp_cost", "pp_cost"), ("range", "range")):
            votes = build_votes(p, field, nv[p["id"]][field])
            if len(set(votes.values())) <= 1:
                continue  # all agree, no conflict
            val, label = resolve(votes)
            if p[key] != val:
                changed.append((p["id"], field, p[key], val))
            p[key] = val
            conflicts.append({"field": field, "values": votes,
                              "resolution": label,
                              "note": f"{label}: " + "/".join(f"{v}×{c}" for v, c in Counter(votes.values()).most_common())})
            resolved_log.append((p["id"], field, val, label, dict(Counter(votes.values()))))
        # special (element / item) conflicts
        sp = SPECIAL.get(p["id"])
        if sp:
            c = {"field": sp["field"], "values": sp["values"],
                 "resolution": sp["resolution"], "note": sp["note"]}
            conflicts.append(c)
            if "set" in sp:
                f, v = sp["set"]
                p[f] = v
        # preserve any pre-existing non-numeric, non-special conflict we didn't touch
        for c in p.get("conflicts", []):
            if c["field"] not in ("pp_cost", "range") and p["id"] not in SPECIAL:
                c.setdefault("resolution", "unresolved")
                conflicts.append(c)

        # merge sources actually contributing a vote
        contributing = set()
        for field in ("pp_cost", "range"):
            contributing |= set(nv[p["id"]][field].keys())
        for s in ("super-slash", "shotgunnova", "bfgamer"):
            if s in contributing and s not in p["sources"]:
                p["sources"].append(s)

        if conflicts:
            p["conflicts"] = conflicts
        elif "conflicts" in p:
            del p["conflicts"]

    json.dump(P, open(PJ, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    open(PJ, "a", encoding="utf-8").write("\n")

    print(f"psynergy.json: {len(P)} entries")
    print(f"  with conflicts: {sum('conflicts' in p for p in P)}")
    print(f"  field values changed by re-resolution: {len(changed)}")
    for cid, f, old, new in changed:
        print(f"    {cid:16} {f}: {old} -> {new}")
    print("\n  all resolved numeric conflicts:")
    for cid, f, val, lab, tally in resolved_log:
        print(f"    {cid:16} {f:8} = {str(val):4} [{lab:9}] votes={tally}")


if __name__ == "__main__":
    main()
