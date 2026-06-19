"""Backfill resolved foreign-key ids onto cross-entity references (GS2).

GS2 analog of links_normalize.py. Same contract: the human-readable `name` stays
the source of truth; this adds an authoritative resolved id next to it. In-place +
idempotent (resolves from name and rewrites the id each run), so it is safe to
re-run after any entity (re)generation -- it must run AFTER, as a final
enrichment pass.

GS2 edges:
  A. classes.psynergy[]          += id                 -> psynergy.json
  B. monsters.drops.items[]      += ref_type, ref_id   -> equipment.json | items.json
  C. monsters.djinn_id           (top-level)           -> djinn.json
  D. monsters.boss_id            (top-level)           -> bosses.json
  E. classes.available_to[].character_id (re)validated -> characters.json
  F. equipment.equippable_by[]   (derived)             -> characters (by can_equip)
  G. shops.stock[]               += ref_type, ref_id   -> equipment.json | items.json

Key GS2 difference from GS1: psynergy.json is a deliberately CLEAN canonical set
(yoyoyoshi, 157 entries). It is NOT exhaustive -- ~35 class-only psynergy (card
tricks, Magma Storm, Hurricane, Thorn, ...) have no canonical entry, and a few
ultimalink spellings are typos. So an unresolved classes.psynergy ref is
*expected* unless the name is actually present in canonical. We therefore split
the report into FATAL (only-real-bugs) vs EXPECTED (known gaps), and exit
non-zero only on FATAL. The rule is policy, not a hand-maintained name list:
  - name in canonical (unique, after ALIASES) but unresolved -> FATAL (a bug)
  - name absent from canonical                               -> EXPECTED gap
  - name ambiguous in canonical (e.g. "Blast")               -> EXPECTED (can't
    disambiguate by name alone; left null + flagged)
Likewise monster drops absent from gs2 gear are EXPECTED (shared gs1 consumables
& gear live in the deferred GS1-numbered source segment).

Usage: python scripts/links_normalize_gs2.py
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "gs2"

# ultimalink misspellings that map cleanly onto a unique canonical psynergy.
# (Verified against data/gs2/psynergy.json names.) "Megacool" is intentionally
# NOT here -- it conflicts with canonical "Supercool" and is flagged, not merged.
ALIASES = {
    "frezze prism": "freeze prism",
    "flare strom": "flare storm",
    "strom ray": "storm ray",
    "high imapct": "high impact",
    "drian": "drain",
}

# equipment.type -> the characters.can_equip category gating it. Clean 1:1 for
# weapons + body armor; `ring` is a universal accessory (all characters). The
# remaining types (hat/class_item/special) have no clean category mapping
# (hat mixes caps/crowns/masks) and are left to equippable_by = [].
TYPE2CAT = {
    "long_sword": "long swords", "light_blade": "light blades", "axe": "axes",
    "mace": "maces", "staff": "staves", "armor": "armor", "clothing": "clothing",
    "robe": "robes", "shield": "shields", "gloves": "gloves", "boots": "boots",
    "shirt": "shirts", "helm": "helms", "circlet": "circlets", "bracelet": "armlets",
}


def load(name):
    return json.loads((DATA / name).read_text(encoding="utf-8"))


def save(name, obj):
    (DATA / name).write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n",
                             encoding="utf-8")


def norm(s):
    return re.sub(r"[^a-z0-9]", "", s.lower())


def reinsert(entry, after_key, new_fields):
    """Return a new dict with new_fields placed right after after_key.
    Drops any pre-existing copies of those keys first (idempotent re-run)."""
    out = {}
    for k, v in entry.items():
        if k in new_fields:
            continue  # will be re-added in the right place
        out[k] = v
        if k == after_key:
            for nk, nv in new_fields.items():
                out[nk] = nv
    return out


def main():
    psynergy = load("psynergy.json")
    equipment = load("equipment.json")
    items = load("items.json")
    classes = load("classes.json")
    monsters = load("monsters.json")
    characters = load("characters.json")
    djinn = load("djinn.json")
    bosses = load("bosses.json")
    shops = load("shops.json")

    # --- resolver tables ---
    char_by_name = {norm(c["name"]): c["id"] for c in characters}
    djinn_by_name = {norm(d["name"]): d["id"] for d in djinn}
    # psynergy: name -> [entries] (one name can map to >1, e.g. "Blast")
    ps_by_name = {}
    for p in psynergy:
        ps_by_name.setdefault(norm(p["name"]), []).append(p)
    # name_variants resolve too (telago/ultimalink alt spellings folded onto a
    # canonical entry, e.g. "Thunderhead"->Thunderstorm); canonical names always
    # win, and a variant only fills a gap (never adds ambiguity).
    for p in psynergy:
        for v in p.get("name_variants", []):
            ps_by_name.setdefault(norm(v), [p])
    # gear: name -> (ref_type, id). equipment and items names are disjoint.
    # Also index name_variants so renamed items (90Kirsdarke canonical names) and
    # singular/plural variants still resolve from a ref that uses the old/alt name.
    gear = {}
    for e in equipment:
        gear[norm(e["name"])] = ("equipment", e["id"])
    for i in items:
        gear[norm(i["name"])] = ("item", i["id"])
    # lower-priority aliases (setdefault: canonical names always win): name_variants
    # (90Kirsdarke renames, GS annotations) + the English-literal column (handles
    # singular/plural like drop "Oil Drop" -> item "Oil Drops").
    for e in equipment:
        for v in e.get("name_variants", []) + [e.get("name_literal")]:
            if v:
                gear.setdefault(norm(v), ("equipment", e["id"]))
    for i in items:
        for v in i.get("name_variants", []) + [i.get("name_literal")]:
            if v:
                gear.setdefault(norm(v), ("item", i["id"]))
    # bosses: resolve by id, name, or any encounter form_id
    boss_lookup = {}
    for b in bosses:
        boss_lookup[norm(b["id"])] = b["id"]
        boss_lookup[norm(b["name"])] = b["id"]
        for e in b.get("encounters", []):
            if e.get("form_id"):
                boss_lookup[norm(e["form_id"])] = b["id"]

    fatal = []     # (edge, ctx, name, reason) -> exit non-zero
    expected = []  # (edge, ctx, name, reason) -> reported, not fatal

    # --- edge A: classes.psynergy[] -> psynergy id ---
    n_ps = n_ps_resolved = 0
    for c in classes:
        new_list = []
        for p in c["psynergy"]:
            n_ps += 1
            key = norm(p["name"])
            if key in ps_by_name:
                cands = ps_by_name[key]
            elif p["name"].lower() in ALIASES:
                cands = ps_by_name.get(norm(ALIASES[p["name"].lower()]), [])
            else:
                cands = []
            pid = None
            if len(cands) == 1:
                pid = cands[0]["id"]
                n_ps_resolved += 1
            elif len(cands) > 1:
                expected.append(("classes.psynergy", c["id"], p["name"],
                                 f"ambiguous ({[x['id'] for x in cands]})"))
            else:
                # absent from canonical -> expected gap (class-only psynergy)
                expected.append(("classes.psynergy", c["id"], p["name"],
                                 "class-only (not in canonical)"))
            new_list.append(reinsert(p, "name", {"id": pid}))
        c["psynergy"] = new_list

    # --- edge B: monsters.drops.items[] -> equipment|item ---
    n_drop = n_drop_resolved = 0
    for m in monsters:
        new_items = []
        for d in m["drops"].get("items", []):
            n_drop += 1
            hit = gear.get(norm(d["name"]))
            if hit is None:
                # shared gs1 consumables / gear in deferred source segment
                expected.append(("monsters.drops", m["id"], d["name"],
                                 "not in gs2 gear (shared/deferred)"))
                rt, rid = None, None
            else:
                rt, rid = hit
                n_drop_resolved += 1
            new_items.append(reinsert(d, "name", {"ref_type": rt, "ref_id": rid}))
        m["drops"]["items"] = new_items

    # --- edge C: monsters.djinn_id -> djinn ; edge D: monsters.boss_id -> bosses ---
    n_dje = n_dje_resolved = n_bm = n_bm_resolved = 0
    for m in monsters:
        if m.get("is_djinn_enemy"):
            n_dje += 1
            # enemy name embeds the djinn name in parens: "Mercury Djinni (Fog)"
            inner = re.search(r"\(([^)]+)\)", m["name"])
            did = djinn_by_name.get(norm(inner.group(1))) if inner else None
            if did is None:
                fatal.append(("monsters.djinn_id", m["id"], m["name"], "no djinn match"))
            else:
                n_dje_resolved += 1
            m["djinn_id"] = did
        if m.get("is_boss"):
            n_bm += 1
            # strip party-config variant suffix: "Karst (vs All)" -> "Karst"
            base = re.sub(r"\s*\(vs[^)]*\)", "", m["name"]).strip()
            bid = boss_lookup.get(norm(base)) or boss_lookup.get(norm(m["name"]))
            if bid is None:
                fatal.append(("monsters.boss_id", m["id"], m["name"], "no boss match"))
            else:
                n_bm_resolved += 1
            m["boss_id"] = bid

    # --- edge E: classes.available_to[].character_id (re)validate ---
    n_av = 0
    for c in classes:
        new_av = []
        for a in c["available_to"]:
            n_av += 1
            cid = char_by_name.get(norm(a["character"])) if a.get("character") else None
            if a.get("character") and cid is None:
                fatal.append(("classes.available_to", c["id"], a["character"], "no character match"))
            elif a.get("character_id") and a.get("character_id") != cid:
                fatal.append(("classes.available_to", c["id"], a["character"],
                              f"character_id drift {a['character_id']!r} != {cid!r}"))
            new_av.append(reinsert(a, "character", {"character_id": cid}))
        c["available_to"] = new_av

    # --- edge F: equipment.equippable_by[] derived from type -> can_equip ---
    # forged_from and other equipment fields are owned by their extractors; here
    # we only (re)derive equippable_by deterministically.
    n_eq_filled = 0
    for e in equipment:
        cat = TYPE2CAT.get(e.get("type"))
        if cat:
            who = [c["name"] for c in characters if cat in c.get("can_equip", [])]
        elif e.get("type") == "ring":
            who = [c["name"] for c in characters]   # universal accessory
        else:
            who = []                                 # hat / class_item / special
        e["equippable_by"] = who
        if who:
            n_eq_filled += 1

    # --- edge G: shops.stock[] -> equipment|item ---
    n_shop = n_shop_resolved = 0
    for s in shops:
        new_stock = []
        for st in s["stock"]:
            n_shop += 1
            hit = gear.get(norm(st["name"]))
            if hit is None:
                expected.append(("shops.stock", s["id"], st["name"],
                                 "not in gs2 gear (shared basic gear deferred)"))
                rt, rid = None, None
            else:
                rt, rid = hit
                n_shop_resolved += 1
            new_stock.append(reinsert(st, "name", {"ref_type": rt, "ref_id": rid}))
        s["stock"] = new_stock

    save("classes.json", classes)
    save("monsters.json", monsters)
    save("equipment.json", equipment)
    save("shops.json", shops)

    # --- report ---
    print("links_normalize_gs2 — wrote classes.json, monsters.json, equipment.json, shops.json")
    print(f"  classes.psynergy refs      : {n_ps_resolved}/{n_ps} resolved")
    print(f"  monsters.drops refs        : {n_drop_resolved}/{n_drop} resolved")
    print(f"  monsters.djinn_id          : {n_dje_resolved}/{n_dje} resolved")
    print(f"  monsters.boss_id           : {n_bm_resolved}/{n_bm} resolved")
    print(f"  classes.available_to       : {n_av} validated")
    print(f"  equipment.equippable_by    : {n_eq_filled}/{len(equipment)} derived")
    print(f"  shops.stock refs           : {n_shop_resolved}/{n_shop} resolved")
    print(f"  FATAL unresolved           : {len(fatal)}")
    for edge, ctx, name, reason in fatal:
        print(f"    [{edge}] {ctx}: {name!r} ({reason})")
    # expected gaps: collapse by (edge, reason, name) with counts for readability
    if expected:
        from collections import Counter
        by_name = Counter((edge, name, reason) for edge, ctx, name, reason in expected)
        print(f"  expected gaps (non-fatal)  : {len(expected)} refs, {len(by_name)} distinct names")
        for (edge, name, reason), cnt in sorted(by_name.items()):
            print(f"    [{edge}] {name!r} x{cnt} ({reason})")

    return 1 if fatal else 0


if __name__ == "__main__":
    sys.exit(main())
