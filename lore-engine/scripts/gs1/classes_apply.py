"""C3: fill/cross-check class stat_multiplier from ElectroSpecter §7 + Shotgunnova [CLSS].

Per-stat resolution across {electrospecter, shotgunnova, aku-chi(existing json)}:
majority wins; electro/shotgun 1v1 ties (no 3rd source) -> keep electrospecter,
resolution=unresolved. Fills the 57 classes that lacked stat_multiplier; the 4
unreachable classes (no source) stay null.

Rerunnable.
"""
import json
from collections import Counter
from pathlib import Path

import classes_supplement as sup

ROOT = Path(__file__).resolve().parent.parent
CJ = ROOT / "data/gs1/classes.json"
STATK = sup.STATK

# authority order for stat ties (highest first): only aku-chi (Terence data-mined)
# and fandom-wiki (wiki, data-derived) are real numeric authorities. The two
# compilations (electrospecter, shotgunnova) are equal-rank, so a pure
# electro-vs-shotgun tie has no authority -> unresolved (keep electrospecter).
AUTH = ["aku-chi", "fandom-wiki"]


def resolve(votes):
    """votes: {source: value} -> (resolved_value, label). Majority; tie -> highest
    authority among the tied values; if no authority source present, unresolved."""
    counts = Counter(votes.values())
    top = counts.most_common()
    if len(top) == 1:
        return top[0][0], None  # unanimous
    if top[0][1] > top[1][1]:
        return top[0][0], "majority"
    winners = {v for v, c in counts.items() if c == top[0][1]}
    for a in AUTH:
        if a in votes and votes[a] in winners:
            return votes[a], "authority"
    return votes.get("electrospecter", top[0][0]), "unresolved"


def main():
    C = json.load(open(CJ, encoding="utf-8"))
    idx = sup.build_index(C)
    got = {c["id"]: {} for c in C}
    for src, rows in (("electrospecter", sup.parse_electrospecter()),
                      ("shotgunnova", sup.parse_shotgunnova())):
        for r in rows:
            m = sup.match(r, idx)
            if m:
                got[m["id"]][src] = r["stats"]
    # FandomWiki generic table: name-keyed, applies to every entry sharing the name.
    fw = sup.parse_fandomwiki()
    for c in C:
        nk = sup.norm(c["name"])
        if nk in fw:
            got[c["id"]]["fandom-wiki"] = fw[nk]

    filled = 0
    conflict_log = []
    for c in C:
        g = got[c["id"]]
        cur = c.get("stat_multiplier")
        # Recover the ORIGINAL aku-chi vote (the json may already hold a resolved
        # value from a prior run). aku-chi voted iff it's in sources; per stat its
        # original value is the one recorded in that stat's conflict (where it was
        # overruled), else the current value (no conflict -> aku-chi agreed).
        akuchi = None
        if "aku-chi" in c.get("sources", []) and cur:
            prev = {cf["field"]: cf for cf in c.get("conflicts", [])}
            akuchi = {}
            for k in STATK:
                cf = prev.get(f"stat_multiplier.{k}")
                akuchi[k] = cf["values"].get("aku-chi", cur[k]) if cf else cur[k]
        if not g and not akuchi:
            continue  # unreachable class, no source -> stays null
        had = cur is not None  # already had stats before this run
        resolved = {}
        conflicts = []
        for k in STATK:
            votes = {}
            if "electrospecter" in g: votes["electrospecter"] = g["electrospecter"][k]
            if "shotgunnova" in g: votes["shotgunnova"] = g["shotgunnova"][k]
            if "fandom-wiki" in g: votes["fandom-wiki"] = g["fandom-wiki"][k]
            if akuchi: votes["aku-chi"] = akuchi[k]
            if not votes:
                resolved[k] = akuchi[k] if akuchi else None
                continue
            val, label = resolve(votes)
            resolved[k] = val
            if label is None:  # unanimous, no conflict to record
                continue
            counts = Counter(votes.values())
            conflicts.append({"field": f"stat_multiplier.{k}", "values": dict(votes),
                              "resolution": label,
                              "note": f"{label}: " + "/".join(f"{v}×{n}" for v, n in counts.most_common())})
            conflict_log.append((c["id"], k, val, label, dict(votes)))

        c["stat_multiplier"] = resolved
        if not had:
            filled += 1
        # sources
        for s in ("electrospecter", "shotgunnova", "fandom-wiki"):
            if s in g and s not in c["sources"]:
                c["sources"].append(s)
        # merge with any pre-existing non-stat conflicts
        existing = [cf for cf in c.get("conflicts", []) if not cf["field"].startswith("stat_multiplier")]
        for cf in existing:
            cf.setdefault("resolution", "unresolved")
        allc = existing + conflicts
        if allc:
            c["conflicts"] = allc
        elif "conflicts" in c:
            del c["conflicts"]

    json.dump(C, open(CJ, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    open(CJ, "a", encoding="utf-8").write("\n")

    print(f"classes.json: {len(C)} entries")
    print(f"  now have stat_multiplier: {sum(c.get('stat_multiplier') is not None for c in C)} (filled {filled} new)")
    print(f"  still null (unreachable): {[c['id'] for c in C if c.get('stat_multiplier') is None]}")
    print(f"  stat conflicts recorded: {len(conflict_log)}")
    for cid, k, val, label, votes in conflict_log:
        print(f"    {cid:18} {k}: {votes} -> {val} [{label}]")


if __name__ == "__main__":
    main()
