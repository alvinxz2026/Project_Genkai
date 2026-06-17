"""C4: regenerate equipment.json — add the ~54 basic weapons/armor that shops
reference but the (artifact-biased) equipment.json lacked, and cross-check the
existing entries' ATK/DEF against the new sources.

Data sources (all GS1-clean), parsed in equipment_supplement.py:
  shotgunnova    [EQPT] table: equip flags, ATK/DEF/AGL/LCK, unleash, cost,
                 artifact '*' / cursed '|C|'.
  super-slash    §VII-IX blocks: Found / Buy Price / Stats / Effect (explicit
                 elemental & PP/HP bonuses, regen, multipliers).
  electrospecter §8/§10 per-type tables: authoritative `type`, ATK/DEF, price, location.

The three sources AGREE on every ATK/DEF for the 54 new basics (no stat conflicts);
they disagree on 3 prices (Wooden Stick / Circlet / Battle Rapier) where Shotgunnova
is the lone outlier -> majority wins, conflict recorded.

`type` is taken from a curated map (cross-validated against the FandomWiki chart and
ElectroSpecter type tables) because the source type buckets are individually
incomplete/ambiguous (e.g. crown vs hat). equippable_by comes from Shotgunnova's
explicit IGIM flags, falling back to the type default for items it omits.

Rerunnable: new entries are rebuilt from source each run; existing entries only get
new source IDs + atk/def conflict records appended (curated values never overwritten).
"""
import json
import re
from collections import Counter
from pathlib import Path

import equipment_supplement as sup

ROOT = Path(__file__).resolve().parent.parent
EJ = ROOT / "data/gs1/equipment.json"
norm = sup.norm

# curated type map for the 54 missing basics (validated vs FandomWiki chart +
# ElectroSpecter type tables; caps -> hat, Jerkin/One-Piece Dress -> robe per wiki).
TYPE = {
    # weapons
    "Long Sword": "long_sword", "Broad Sword": "long_sword", "Claymore": "long_sword",
    "Great Sword": "long_sword",
    "Short Sword": "light_blade", "Hunter's Sword": "light_blade", "Battle Rapier": "light_blade",
    "Master Rapier": "light_blade", "Ninja Sword": "light_blade",
    "Battle Axe": "axe", "Broad Axe": "axe", "Great Axe": "axe",
    "Mace": "mace", "Heavy Mace": "mace", "Battle Mace": "mace", "War Mace": "mace",
    "Wooden Stick": "staff",
    # body armor
    "Leather Armor": "armor", "Chain Mail": "armor", "Plate Mail": "armor",
    "Steel Armor": "armor", "Armored Shell": "armor",
    "Travel Robe": "robe", "Silk Robe": "robe", "Jerkin": "robe", "One-Piece Dress": "robe",
    "Travel Vest": "clothing", "Adept's Clothes": "clothing", "Silver Vest": "clothing",
    "Cotton Shirt": "clothing",
    # headgear
    "Open Helm": "helm", "Bronze Helm": "helm", "Iron Helm": "helm", "Steel Helm": "helm",
    "Silver Helm": "helm", "Knight's Helm": "helm",
    "Leather Cap": "hat", "Wooden Cap": "hat", "Mail Cap": "hat",
    "Circlet": "circlet", "Silver Circlet": "circlet", "Guardian Circlet": "circlet",
    "Platinum Circlet": "circlet",
    # hand armor
    "Wooden Shield": "shield", "Bronze Shield": "shield", "Iron Shield": "shield",
    "Knight's Shield": "shield",
    "Padded Gloves": "gloves", "Leather Gloves": "gloves", "Gauntlets": "gloves",
    "Armlet": "bracelet", "Leather Armlet": "bracelet", "Heavy Armlet": "bracelet",
    "Silver Armlet": "bracelet",
}

WEAPON_TYPES = {"long_sword", "light_blade", "axe", "mace", "staff"}
EQUIP_DEFAULT = {
    "long_sword": ["Isaac", "Garet"], "axe": ["Isaac", "Garet"],
    "light_blade": ["Isaac", "Garet", "Ivan"], "mace": ["Isaac", "Garet", "Mia"],
    "staff": ["Ivan", "Mia"],
    "armor": ["Isaac", "Garet"], "shield": ["Isaac", "Garet"], "helm": ["Isaac", "Garet"],
    "robe": ["Ivan", "Mia"], "bracelet": ["Ivan", "Mia"], "circlet": ["Ivan", "Mia"],
    "clothing": ["Isaac", "Garet", "Ivan", "Mia"], "gloves": ["Isaac", "Garet", "Ivan", "Mia"],
    "hat": ["Isaac", "Garet", "Ivan", "Mia"], "crown": ["Isaac", "Garet", "Ivan", "Mia"],
    "shirt": ["Isaac", "Garet", "Ivan", "Mia"], "boots": ["Isaac", "Garet", "Ivan", "Mia"],
}
ELEM = {"earth": "earth", "fire": "fire", "wind": "wind", "water": "water",
        "venus": "earth", "mars": "fire", "jupiter": "wind", "mercury": "water"}


def slug(name):
    # drop apostrophes first so "Knight's Helm" -> "knights-helm" (matches existing ids)
    return re.sub(r"[^a-z0-9]+", "-", name.lower().replace("'", "")).strip("-")


def zero_stats():
    return {"atk": 0, "def": 0, "hp": 0, "pp": 0, "agi": 0, "lck": 0, "hp_regen": 0, "pp_regen": 0}


def zero_elem():
    return {"earth": 0, "fire": 0, "wind": 0, "water": 0}


def parse_ss_stats(stat_lines, effect):
    """super-slash 'Stats:' lines + 'Effect:' text -> (stat_bonus, power, resist,
    multiplier, increases_critical, use_effect, unleash_name, cursed)."""
    sb, power, resist = zero_stats(), zero_elem(), zero_elem()
    mult, crit, cursed = None, False, False
    for s in stat_lines or []:
        s = s.strip()
        m = re.match(r"^([+-]\d+)\s+Attack", s)
        if m: sb["atk"] = int(m.group(1)); continue
        m = re.match(r"^([+-]\d+)\s+Defense", s)
        if m: sb["def"] = int(m.group(1)); continue
        m = re.match(r"^([+-]\d+)\s+Maximum HP", s)
        if m: sb["hp"] = int(m.group(1)); continue
        m = re.match(r"^([+-]\d+)\s+Maximum PP", s)
        if m: sb["pp"] = int(m.group(1)); continue
        m = re.match(r"^([+-]\d+)\s+Agility", s)
        if m: sb["agi"] = int(m.group(1)); continue
        m = re.match(r"^([+-]\d+)\s+Luck", s)
        if m: sb["lck"] = int(m.group(1)); continue
        m = re.match(r"^([+-]\d+)\s+(\w+)\s+Resistance", s)
        if m and m.group(2).lower() in ELEM:
            resist[ELEM[m.group(2).lower()]] = int(m.group(1)); continue
        m = re.match(r"^([+-]\d+)\s+(\w+)\s+Power", s)
        if m and m.group(2).lower() in ELEM:
            power[ELEM[m.group(2).lower()]] = int(m.group(1)); continue
        m = re.match(r"^Agility x([\d.]+)", s)
        if m: mult = {"agi": float(m.group(1))}; continue
    use_effect, unleash_name = None, None
    if effect and effect not in ("N/A", "-"):
        e = effect.strip()
        m = re.match(r'^Randomly casts "?([A-Za-z \'-]+?)"?\.?$', e)
        if m:
            unleash_name = m.group(1).strip()
        if re.search(r"[Cc]ursed", e):
            cursed = True
        m = re.search(r"Heals (\d+) HP every turn", e)
        if m: sb["hp_regen"] = int(m.group(1))
        if re.search(r"when used as an item|Use to|Restores", e):
            use_effect = {"description": e, "may_break": bool(re.search(r"may break", e, re.I))}
        if re.search(r"[Cc]ritical", e):
            crit = True
    return sb, power, resist, mult, crit, use_effect, unleash_name, cursed


def resolve_price(votes):
    """votes {src:price} -> (value, conflict|None). majority; tie keeps lowest (shop floor)."""
    vals = [v for v in votes.values() if v is not None]
    if not vals:
        return None, None
    counts = Counter(vals)
    top = counts.most_common()
    if len(top) == 1:
        return top[0][0], None
    if top[0][1] > top[1][1]:
        val, label = top[0][0], "majority"
    else:
        val, label = min(v for v, c in counts.items() if c == top[0][1]), "tie-min"
    conflict = {"field": "acquisition.price", "values": dict(votes), "resolution": label,
                "note": f"{label}: " + "/".join(f"{v}×{c}" for v, c in counts.most_common())}
    return val, conflict


def build_entry(name, sh, ss, es, shop_price, shop_artifact):
    nk = norm(name)
    typ = TYPE[name]
    cat = "weapon" if typ in WEAPON_TYPES else "armor"
    sg, us, e = sh.get(nk), ss.get(nk), es.get(nk)

    sb, power, resist, mult, crit, use_effect, unleash_name, cursed = \
        parse_ss_stats(us["stats"] if us else None, us["effect"] if us else None)

    # primary stat: super-slash parsed -> shotgunnova column -> electrospecter
    if typ in WEAPON_TYPES:
        if sb["atk"] == 0:
            sb["atk"] = (sg and sg["atk"]) or (e and e["atk"]) or 0
    else:
        if sb["def"] == 0:
            sb["def"] = (sg and sg["def"]) or (e and e["def"]) or 0

    # cursed / artifact from shotgunnova markers (+ shops artifact flag)
    if sg and sg["is_cursed"]:
        cursed = True
    is_artifact = bool((sg and sg["is_artifact"]) or shop_artifact)

    # equippable_by: use the type default (matches how the existing 87 were built);
    # override to females-only [Mia] when Shotgunnova flags ---M (e.g. One-Piece Dress).
    # (Shotgunnova's IG-- on Leather/Wooden Cap is an outlier vs ElectroSpecter "used by
    # all" + the existing all-four hats, so the hat default wins.)
    equip = EQUIP_DEFAULT[typ]
    if sg and sg["equippable_by"] == ["Mia"]:
        equip = ["Mia"]

    # unleash: from shotgunnova UNLEASH column (weapons) or super-slash "Randomly casts"
    unleash = None
    if typ in WEAPON_TYPES:
        un = unleash_name
        if not un and sg and sg["effect"] and sg["effect"].strip("-"):
            un = sg["effect"].strip()
        if un:
            unleash = {"name": un, "element": None, "rate": None, "power_level": None,
                       "effects": [], "notes": "source gives unleash name only; "
                       "rate/power/element unconfirmed"}

    # price: majority of the 3 equipment sources (shops price derives from shotgunnova,
    # so it is NOT an independent vote)
    votes = {}
    if sg and sg["cost"] is not None: votes["shotgunnova"] = sg["cost"]
    if us and us["price"] is not None: votes["super-slash"] = us["price"]
    if e and e["price"] is not None: votes["electrospecter"] = e["price"]
    price, price_conflict = resolve_price(votes)
    if price is None:
        price = shop_price

    # location: electrospecter "X Weapon/Armor Shop" -> town; else super-slash Found
    loc = None
    if e and e["location"]:
        loc = re.sub(r"\s+(Weapon|Armor)\s+Shop$", "", e["location"]).strip() or None
    if not loc and us and us["location"]:
        loc = us["location"]

    sources = sorted({s for s, v in (("shotgunnova", sg), ("super-slash", us),
                                     ("electrospecter", e)) if v})
    entry = {
        "id": slug(name), "name": name, "game": "gs1", "category": cat, "type": typ,
        "is_cursed": cursed, "is_artifact": is_artifact, "equippable_by": equip,
        "stat_bonus": sb, "stat_multiplier": mult, "increases_critical": crit,
        "elemental_power": power, "elemental_resistance": resist,
        "unleash": unleash, "use_effect": use_effect,
        "acquisition": {"method": "shop", "location": loc, "price": price, "notes": None},
        "sources": sources,
    }
    if price_conflict:
        entry["conflicts"] = [price_conflict]
    return entry


# entries carrying one of these sources are hand-curated; everything else in the
# file is a basic this script generated (rebuilt from source each run -> rerunnable).
CURATED = {"dnextreme88", "rockettrekkie", "fandom-equipment"}


def backfill_resolution(conf):
    """give a pre-existing conflict a resolution if it lacks one: clear modal value
    -> majority, else unresolved."""
    if conf.get("resolution"):
        return conf
    counts = Counter(conf.get("values", {}).values())
    top = counts.most_common()
    conf["resolution"] = "majority" if len(top) == 1 or top[0][1] > top[1][1] else "unresolved"
    return conf


def main():
    allE = json.load(open(EJ, encoding="utf-8"))
    E = [e for e in allE if set(e["sources"]) & CURATED]  # curated base only
    sh, ss, es = sup.parse_shotgunnova(), sup.parse_superslash(), sup.parse_electrospecter()
    I = json.load(open(ROOT / "data/gs1/items.json", encoding="utf-8"))
    S = json.load(open(ROOT / "data/gs1/shops.json", encoding="utf-8"))
    have = {norm(e["name"]) for e in E} | {norm(i["name"]) for i in I}
    shop_meta = {}
    missing = {}
    for shp in S:
        for st in shp.get("stock", []):
            nk = norm(st["name"])
            shop_meta.setdefault(nk, st)
            if nk not in have:
                missing.setdefault(nk, st["name"])

    existing_ids = {e["id"] for e in E}
    added = []
    for nk, name in missing.items():
        if name not in TYPE:
            print(f"  !! no TYPE mapping for {name!r}; skipped"); continue
        st = shop_meta.get(nk, {})
        ent = build_entry(name, sh, ss, es, st.get("price"), st.get("is_artifact"))
        if ent["id"] in existing_ids:
            print(f"  !! id collision {ent['id']} for {name!r}; skipped"); continue
        added.append(ent)

    # --- cross-check existing entries: add new source IDs + atk/def conflicts ---
    xcheck = 0
    for ent in E:
        nk = norm(ent["name"])
        sb = ent["stat_bonus"]
        # keep non-atk/def conflicts; recompute the cross-check ones each run
        ent_conf = [backfill_resolution(c) for c in ent.get("conflicts", [])
                    if c["field"] not in ("stat_bonus.atk", "stat_bonus.def")]
        for src, rec in (("shotgunnova", sh.get(nk)), ("electrospecter", es.get(nk)),
                         ("super-slash", ss.get(nk))):
            if not rec:
                continue
            sa = rec.get("atk"); sd = rec.get("def")
            if src == "super-slash":  # super-slash record stores raw stat lines
                psb = parse_ss_stats(rec["stats"], rec["effect"])[0]
                sa, sd = psb["atk"], psb["def"]
            corroborates = False
            if sa not in (None, 0):
                if sa == sb["atk"]:
                    corroborates = True
                else:
                    ent_conf.append({"field": "stat_bonus.atk",
                                     "values": {"dnextreme88": sb["atk"], src: sa},
                                     "resolution": "authority",
                                     "note": "authority: dnextreme88 is the equipment-stat authority"})
                    xcheck += 1
            if sd not in (None, 0):
                if sd == sb["def"]:
                    corroborates = True
                else:
                    ent_conf.append({"field": "stat_bonus.def",
                                     "values": {"dnextreme88": sb["def"], src: sd},
                                     "resolution": "authority",
                                     "note": "authority: dnextreme88 is the equipment-stat authority"})
                    xcheck += 1
            if (corroborates or sa not in (None, 0) or sd not in (None, 0)) and src not in ent["sources"]:
                ent["sources"].append(src)
        if ent_conf:
            ent["conflicts"] = ent_conf
        elif "conflicts" in ent:
            del ent["conflicts"]

    out = E + added
    json.dump(out, open(EJ, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    open(EJ, "a", encoding="utf-8").write("\n")

    from collections import Counter as C
    print(f"equipment.json: {len(out)} entries ({len(E)} existing + {len(added)} new)")
    print(f"  new by category: {dict(C(e['category'] for e in added))}")
    print(f"  new by type: {dict(C(e['type'] for e in added))}")
    print(f"  new with price conflict: {[e['id'] for e in added if 'conflicts' in e]}")
    print(f"  existing-entry stat conflicts flagged: {xcheck}")
    print(f"  new entries missing primary stat (atk/def all 0): "
          f"{[e['id'] for e in added if e['stat_bonus']['atk']==0 and e['stat_bonus']['def']==0]}")


if __name__ == "__main__":
    main()
