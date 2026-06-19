"""Resolve gs2 locations.json name-refs to entity ids + materialize the cross-index.

GS2 inverts gs1's locations model. In gs1 each entity carried its own location
string and `locations_refs.py` built the reverse map. In gs2 `locations.json`
(extracted from the consolidated 2a walkthrough) already holds the FORWARD refs
per region -- djinn_here / monsters_here / bosses_here / summons_here /
psynergy_here / pickups / forging / shop / connections -- as human-readable
NAMES, while the entities' own `location` fields were deferred. So here we:

  1. resolve every name in every region's ref-lists to its entity id
     (deterministic, by normalized name -- no LLM);
  2. materialize data/gs2/location_refs.json with BOTH directions:
       regions: region_id -> resolved id lists (forward, cleaned)
       index:   entity_id -> [region_id] per category (the inverse, so
                djinn/boss/summon/monster/shop "where is X" queries resolve
                without mutating the entity files);
  3. print a CROSS-CHECK report. Because locations names come from prose and the
     entity tables come from data-table sources, every unresolved name is a real
     discrepancy worth a human look (typo, plural, missing entity, unmodeled
     overworld region). We deliberately do NOT alias typos away -- the misses
     ARE the finding (this is the first pass of task-3 cross-check).

Resolution is format-only normalization (case / punctuation / whitespace). Known
non-entity ref shapes are bucketed as EXPECTED, not silently dropped:
  - pickups that are coin drops ("315 Coins", "16 gold coins")     -> EXPECTED
  - bosses_here that are djinni encounters ("Mercury Djinni (Fog)") -> EXPECTED
    (these live in monsters.json as djinn-enemies, not bosses.json)

pickups / forging follow the SAME policy as links_normalize_gs2's drops & shop
stock: a name absent from gs2 gear is an EXPECTED gap (shared gs1 consumables &
the deferred GS1-numbered gear segment), so it is reported as a distilled
distinct-name list for the focused backlog rather than as a per-region finding.
The hard FINDINGS bucket is reserved for ref categories that SHOULD fully resolve
against our tables (connections / djinn / monsters / bosses / summons / psynergy
/ shops) -- a miss there is a genuine discrepancy (typo, plural, missing entity,
naming-convention gap) worth a human look.

locations.json and the entity files are NOT mutated; this only writes the
derived view. Rerunnable + byte-stable.

Usage: python scripts/locations_refs_gs2.py
"""
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "gs2"
OUT = DATA / "location_refs.json"


def load(name):
    return json.loads((DATA / name).read_text(encoding="utf-8"))


def norm(s):
    return re.sub(r"[^a-z0-9]", "", s.lower())


# ref shapes that are intentionally not entities -> EXPECTED, never a finding
COIN_RE = re.compile(r"\bcoins?\b", re.I)            # "315 Coins", "16 gold coins"
DJINNI_ENCOUNTER_RE = re.compile(r"\bdjinn?i\b", re.I)  # "Mercury Djinni (Fog)" etc.


def main():
    locations = load("locations.json")
    djinn = load("djinn.json")
    monsters = load("monsters.json")
    bosses = load("bosses.json")
    summons = load("summons.json")
    psynergy = load("psynergy.json")
    equipment = load("equipment.json")
    items = load("items.json")
    shops = load("shops.json")

    region_ids = {l["region_id"] for l in locations}

    # --- resolver tables (normalized name -> id) ---
    djinn_by = {norm(d["name"]): d["id"] for d in djinn}
    mon_by = {norm(m["name"]): m["id"] for m in monsters}
    sum_by = {norm(s["name"]): s["id"] for s in summons}
    ps_by = {norm(p["name"]): p["id"] for p in psynergy}
    shop_by = {norm(s["name"]): s["id"] for s in shops}
    # gear: equipment + items names are disjoint -> (ref_type, id)
    gear = {}
    for e in equipment:
        gear[norm(e["name"])] = ("equipment", e["id"])
    for i in items:
        gear[norm(i["name"])] = ("item", i["id"])
    # bosses: id, name, or any encounter form_id
    boss_by = {}
    for b in bosses:
        boss_by[norm(b["id"])] = b["id"]
        boss_by[norm(b["name"])] = b["id"]
        for enc in b.get("encounters", []):
            if enc.get("form_id"):
                boss_by[norm(enc["form_id"])] = b["id"]

    # accumulators
    regions = {}
    index = {c: defaultdict(list) for c in
             ("djinn", "monsters", "bosses", "summons", "shops")}
    findings = defaultdict(list)   # category -> [(region_id, raw)]
    expected = defaultdict(list)   # category -> [(region_id, raw)]
    counts = defaultdict(lambda: [0, 0])  # category -> [resolved, total]

    def simple(cat, names, table, lookup):
        """Resolve a flat name list against one id table; record findings."""
        out = []
        for raw in names:
            counts[cat][1] += 1
            hit = table.get(norm(raw))
            if hit is not None:
                out.append(hit)
                counts[cat][0] += 1
            else:
                findings[cat].append((rid, raw))
        return out

    for loc in locations:
        rid = loc["region_id"]

        # connections -> validate against the region_id vocabulary
        conn_ok, conn_bad = [], []
        for c in loc.get("connections", []):
            counts["connections"][1] += 1
            if c in region_ids:
                conn_ok.append(c)
                counts["connections"][0] += 1
            else:
                conn_bad.append(c)
                findings["connections"].append((rid, c))

        dj = simple("djinn", loc.get("djinn_here", []), djinn_by, None)
        mon = simple("monsters", loc.get("monsters_here", []), mon_by, None)
        sm = simple("summons", loc.get("summons_here", []), sum_by, None)
        ps = simple("psynergy", loc.get("psynergy_here", []), ps_by, None)

        # bosses: djinni-encounters are EXPECTED (they're monster djinn-enemies)
        bo = []
        for raw in loc.get("bosses_here", []):
            counts["bosses"][1] += 1
            hit = boss_by.get(norm(raw))
            # strip "(vs All)" / "(Fog)" style suffixes as a second try
            if hit is None:
                base = re.sub(r"\s*\([^)]*\)", "", raw).strip()
                hit = boss_by.get(norm(base))
            if hit is not None:
                bo.append(hit)
                counts["bosses"][0] += 1
            elif DJINNI_ENCOUNTER_RE.search(raw):
                expected["bosses"].append((rid, raw))
            else:
                findings["bosses"].append((rid, raw))

        # pickups / forging -> gear; coins are EXPECTED non-entities
        def gearlist(cat, names):
            out = []
            for raw in names:
                counts[cat][1] += 1
                hit = gear.get(norm(raw))
                if hit is not None:
                    out.append({"name": raw, "ref_type": hit[0], "ref_id": hit[1]})
                    counts[cat][0] += 1
                else:
                    # absent from gs2 gear -> EXPECTED gap (coins / shared
                    # consumables / deferred GS1-numbered gear), same policy as
                    # links_normalize_gs2 drops & shop stock.
                    out.append({"name": raw, "ref_type": None, "ref_id": None})
                    expected[cat].append((rid, raw))
            return out

        pickups = gearlist("pickups", loc.get("pickups", []))
        forging = gearlist("forging", loc.get("forging", []))

        # shop boolean -> resolve a shop id by region name when present
        shop_id = None
        if loc.get("shop"):
            counts["shops"][1] += 1
            shop_id = shop_by.get(norm(loc["name"]))
            if shop_id is not None:
                counts["shops"][0] += 1
            else:
                findings["shops"].append((rid, loc["name"]))

        regions[rid] = {
            "name": loc["name"],
            "order": loc["order"],
            "kind": loc["kind"],
            "connections": conn_ok,
            "connections_unresolved": conn_bad,
            "djinn": dj,
            "monsters": mon,
            "bosses": bo,
            "summons": sm,
            "psynergy": ps,
            "pickups": pickups,
            "forging": forging,
            "shop": shop_id,
        }

        # inverse index (resolved ids only)
        for did in dj:
            index["djinn"][did].append(rid)
        for mid in mon:
            index["monsters"][mid].append(rid)
        for bid in bo:
            index["bosses"][bid].append(rid)
        for sid in sm:
            index["summons"][sid].append(rid)
        if shop_id:
            index["shops"][shop_id].append(rid)

    materialized = {
        "generated_by": "scripts/locations_refs_gs2.py",
        "note": "DERIVED view. Do not hand-edit. Rebuild: python scripts/locations_refs_gs2.py",
        "source_files": ["locations.json", "djinn.json", "monsters.json", "bosses.json",
                         "summons.json", "psynergy.json", "equipment.json", "items.json",
                         "shops.json"],
        "regions": {rid: regions[rid] for rid in sorted(regions)},
        "index": {c: {k: sorted(set(v)) for k, v in sorted(index[c].items())}
                  for c in index},
    }
    OUT.write_text(json.dumps(materialized, ensure_ascii=False, indent=2) + "\n",
                   encoding="utf-8")

    # --- report ---
    print(f"wrote {OUT.relative_to(ROOT)} : {len(regions)} regions\n")
    print("resolved / total per ref category:")
    order = ["connections", "djinn", "monsters", "bosses", "summons",
             "psynergy", "pickups", "forging", "shops"]
    for cat in order:
        r, t = counts[cat]
        print(f"  {cat:14} {r:>3}/{t:<3}")

    n_exp = sum(len(v) for v in expected.values())
    print(f"\nexpected gaps (coins / shared consumables / deferred GS1 gear): {n_exp}")
    for cat in sorted(expected):
        names = sorted({raw for _, raw in expected[cat] if not COIN_RE.search(raw)})
        n_coin = sum(1 for _, raw in expected[cat] if COIN_RE.search(raw))
        print(f"  {cat}: {len(expected[cat])} refs "
              f"({len(names)} distinct non-coin + {n_coin} coin drops)")
        # distilled distinct non-coin names -> these feed the focused gear backlog
        if names:
            print("    " + ", ".join(names))

    n_find = sum(len(v) for v in findings.values())
    print(f"\n=== CROSS-CHECK FINDINGS (unresolved names — review): {n_find} ===")
    for cat in order:
        if findings[cat]:
            print(f"\n[{cat}] {len(findings[cat])}:")
            for rid, raw in findings[cat]:
                print(f"    {rid:24} {raw!r}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
