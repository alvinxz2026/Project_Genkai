"""Extract GS2 (TLA) equipment + gs2-specific items from mr-unorigino's Item List.

Deterministic parser (no LLM/API), mirroring scripts/monsters_extract_gs2.py.

Primary source: `Item List by Mr_UnOrigino` — a single clean data table that
cross-lists **GS1 and TLA** items in debug-room order. Each entry is:

    <debug_no> / <Japanese> / <English-literal> / <GS-US English name>
    <attribute lines...>
    Buy: N coins      (optional)
    Sell: N coins      (optional)

BOTH segments are parsed (SSoT completeness pass, 2026-06-19; user opted for full
extraction so the gs2 item data is a complete single-source-of-truth):
  * base/shared sections `-A.`..`-R3.` (debug_no 1-247) — base weapons/armor,
    consumables (Herb/Potion/Psy Crystal/stat-boost foods), Psynergy items
    (Lash Pebble teaches Lash, ...), key items (Red/Blue Key, Venus/Mars Stars,
    Black Crystal=Black Orb, ...). mr-unorigino cross-lists GS1's numbering first,
    so these are tagged game="gs1" (origin) — but they ARE present/obtainable in
    TLA (90Kirsdarke confirms them in the base/shared item bank).
  * TLA-native sections `-2A.`..`-2U.` — TLA-exclusive equipment + gs2-only items
    (forging materials, trident pieces, TLA "other"), tagged game="gs2".
(Earlier passes parsed only the TLA segment under a "two independent truth sources"
reading and deferred the base set; that deferral was scope, not principle — the base
segment of a TLA guide is legitimate gs2 extraction. gs1's own JSON is still never
imported.)

A few mr-unorigino US-name-column quirks are corrected to 90Kirsdarke's real-game
names inline (NAME_FIXES; cross-check Q2b) with the old name kept in name_variants.

Output is split by entity, mirroring the gs1 equipment/items schema split:
  - data/gs2/equipment.json  (weapons, armor, artifacts, rusty weapons, class items)
  - data/gs2/items.json      (forging materials, trident pieces, misc "other" items)

Per-source normalized records are materialized to data/gs2/intermediate/ for
inspection, then enriched (id / game / flags) into the final files.

Deferred fields (source doesn't provide; left null/empty for links_normalize or a
2nd source to fill later, exactly as monsters deferred its FKs):
  - equippable_by []        (no character-equip table in this source)
  - is_artifact null         (source doesn't mark artifacts)
  - forged_from []           (gs2 forging edge; from aspartate-forge later)
  - unleash element/rate/power_level null (source gives only the unleash name)
  - acquisition              (handled by locations/shops/walkthrough sources)

Element mapping (same as monsters): Venus=earth, Mercury=water, Mars=fire,
Jupiter=wind.

Rerunnable: parses raw text only; no manual stat data embedded.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "raw" / "gs2" / "In-Depth Guides" / "Item List by Mr_UnOrigino.md"
EQUIP_OUT = ROOT / "data" / "gs2" / "equipment.json"
ITEMS_OUT = ROOT / "data" / "gs2" / "items.json"
INTER_DIR = ROOT / "data" / "gs2" / "intermediate"
SOURCE_ID = "mr-unorigino-item"

# Section code -> (entity, category/item_type, weapon-armor type | None).
# entity "equipment": (entity, category, type). entity "items": (entity, item_type, None).
SECTION = {
    "2A": ("equipment", "weapon", "long_sword"),
    "2B": ("equipment", "weapon", "light_blade"),
    "2C": ("equipment", "weapon", "axe"),
    "2D": ("equipment", "weapon", "mace"),
    "2E": ("equipment", "weapon", "staff"),
    "2F": ("equipment", "weapon", "special"),
    "2G": ("equipment", "armor", "armor"),
    "2H": ("equipment", "armor", "clothing"),
    "2I": ("equipment", "armor", "robe"),
    "2J": ("equipment", "armor", "shield"),
    "2K": ("equipment", "armor", "gloves"),
    "2L": ("equipment", "armor", "bracelet"),
    "2M": ("equipment", "armor", "helm"),
    "2N": ("equipment", "armor", "hat"),
    "2O": ("equipment", "armor", "circlet"),
    "2P1": ("equipment", "armor", "shirt"),
    "2P2": ("equipment", "armor", "boots"),
    "2P3": ("equipment", "armor", "ring"),
    "2Q": ("equipment", "weapon", "rusty"),   # is_rusty; refined type by name below
    "2R": ("items", "material", None),
    "2S": ("items", "key", None),
    "2T": ("equipment", "item", "class_item"),
    "2U": ("items", "other", None),           # sub-classified by name below
    # --- base/shared segment (single-letter codes, debug_no 1-247, game="gs1") ---
    "A": ("equipment", "weapon", "long_sword"),
    "B": ("equipment", "weapon", "light_blade"),
    "C": ("equipment", "weapon", "axe"),
    "D": ("equipment", "weapon", "mace"),
    "E": ("equipment", "weapon", "staff"),
    "F": ("equipment", "armor", "armor"),
    "G": ("equipment", "armor", "clothing"),
    "H": ("equipment", "armor", "robe"),
    "I": ("equipment", "armor", "shield"),
    "J": ("equipment", "armor", "gloves"),
    "K": ("equipment", "armor", "bracelet"),
    "L": ("equipment", "armor", "helm"),
    "M": ("equipment", "armor", "hat"),
    "N": ("equipment", "armor", "circlet"),
    "O": ("items", "consumable", None),
    "P": ("items", "psynergy_item", None),
    "Q": ("items", "key", None),              # Other Items: stars, key/quest items
    "R1": ("equipment", "armor", "shirt"),
    "R2": ("equipment", "armor", "boots"),
    "R3": ("equipment", "armor", "ring"),
}

# mr-unorigino US-name-column quirks -> 90Kirsdarke real-game name (Q2b; user
# decision 2026-06-19). Old name preserved in name_variants; 90kirsdarke credited.
NAME_FIXES = {
    "Astral Circle": "Astral Circlet",
    "Psychic Circle": "Psychic Circlet",
    "Aeolian Cossack": "Aeolian Cassock",
    "Leda's Armlet": "Leda's Bracelet",
    "Fireman's Rod": "Fireman's Pole",
    "Appolo's Axe": "Apollo's Axe",
}
# mr-unorigino unleash-name typos -> correct spelling (corroborated by aspartate-
# forge). Old spelling kept in unleash.name_variants for provenance.
UNLEASH_FIXES = {
    "Radient Fire": "Radiant Fire",  # Levatine; aspartate-forge spells it "Radiant"
}
KIRS_SRC = "90kirsdarke-hack"

ELEM = {"Venus": "earth", "Mercury": "water", "Mars": "fire", "Jupiter": "wind"}

STAT_PATTERNS = [
    (re.compile(r"^Attack \+(\d+)$"), "atk"),
    (re.compile(r"^Defense \+(\d+)$"), "def"),
    (re.compile(r"^Maximum HP \+(\d+)$"), "hp"),
    (re.compile(r"^Maximum PP \+(\d+)$"), "pp"),
    (re.compile(r"^Agility \+(\d+)$"), "agi"),
    (re.compile(r"^Luck \+(\d+)$"), "lck"),
    (re.compile(r"^HP recovery \+(\d+)$"), "hp_regen"),
    (re.compile(r"^PP recovery \+(\d+)$"), "pp_regen"),
]
ELEM_RE = re.compile(r"^(Venus|Mercury|Mars|Jupiter) (Power|Resist) ([+-]\d+)$")
# Real section headers carry a leading '-' ("-A. Long Blades", "-2O. TLA Circlets");
# the table-of-contents lists them WITHOUT the dash, so the dash is mandatory here.
SECTION_RE = re.compile(r"^-(2?[A-U]\d?)\.\s+(.+)$")
ENTRY_RE = re.compile(r"^(\d+)\s*/\s*(.+?)\s*/\s*(.+?)\s*/\s*(.+?)$")
BUY_RE = re.compile(r"^Buy:\s*(\d+)\s*coins?$", re.I)
SELL_RE = re.compile(r"^Sell:\s*(\d+)\s*coins?$", re.I)
# Greedy to the LAST quote so apostrophes inside the name survive
# (e.g. "Acheron's Grief" must not truncate at "Acheron").
UNLEASH_US_RE = re.compile(r"^US\s*-\s*Unleashe?s? '(.+)'(?:\s*\(.*)?$", re.I)
# JP source line: Unleashes '<katakana>' (<english literal>) -> capture the literal.
UNLEASH_LIT_RE = re.compile(r"^Unleashe?s? '.+' \((.+)\)\s*$")
CRIT_RE = re.compile(r"^Rate of Criticals rise\.?$", re.I)
BREAK_RE = re.compile(r"break if used in battle", re.I)
CURSED_RE = re.compile(r"^It's cursed\.?$", re.I)
NOTRADE_RE = re.compile(r"^Cannot be (sold or bought|bought or sold)\.?$", re.I)

# 2U "Other Items" item_type by GS-US name (small curated set; the rest -> key).
OTHER_CONSUMABLE = {
    "healing fungus", "laughing fungus", "milk", "large bread", "li'l turtle",
}
OTHER_MATERIAL = {
    "dancing idol", "pretty stone", "red cloth", "sea god's tear",
}


def slug(s):
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", s.lower())).strip("-")


def section_code(s):
    """Return the SECTION code if `s` is a known section header, else None."""
    m = SECTION_RE.match(s)
    return m.group(1) if (m and m.group(1) in SECTION) else None


def new_record(debug_no, jp, en_literal, us_name):
    # `jp` (4th-column katakana) is mojibake under this file's encoding -> dropped.
    # `en_literal` is clean ASCII (a useful alternate name) -> kept.
    # A few base-segment US names carry a trailing parenthetical GS annotation
    # ("Black Crystal (Black Orb in GS)", "Jupiter Star (listed as 222 in GS)").
    # No real item name uses '(', so strip from the first " (" and keep the full
    # original in name_variants (lossless; keeps e.g. "Black Orb" searchable).
    us = us_name.strip()
    m = re.match(r"^(.*?)\s*\(.*$", us)
    clean = m.group(1).strip() if m else us
    return {
        "debug_no": int(debug_no),
        "name": clean,
        "name_annotation": us if clean != us else None,
        "name_literal": en_literal.strip(),
        "stat_bonus": {k: 0 for k in ("atk", "def", "hp", "pp", "agi", "lck", "hp_regen", "pp_regen")},
        "elemental_power": {e: 0 for e in ("earth", "fire", "wind", "water")},
        "elemental_resistance": {e: 0 for e in ("earth", "fire", "wind", "water")},
        "unleash_name": None, "unleash_name_literal": None,
        "is_cursed": False, "may_break": False, "increases_critical": False,
        "can_trade": True, "effects": [],
        "buy_price": None, "sell_price": None,
    }


def parse_attribute(rec, s):
    """Apply one attribute line to a record. Unrecognized -> effects[] (lossless)."""
    # base segment's dual "GS-value / US - US-value" lines -> keep the US (gs2) value.
    if " / US - " in s:
        s = s.split(" / US - ", 1)[1]
    # GS1 unleash-annotation spillover line (Sol Blade/Masamune/Fire Brand) -> noise.
    if "dummy weapon" in s:
        return
    for pat, key in STAT_PATTERNS:
        m = pat.match(s)
        if m:
            rec["stat_bonus"][key] = int(m.group(1))
            return
    em = ELEM_RE.match(s)
    if em:
        elem = ELEM[em.group(1)]
        tgt = rec["elemental_power"] if em.group(2) == "Power" else rec["elemental_resistance"]
        tgt[elem] = int(em.group(3))
        return
    mu = UNLEASH_US_RE.match(s)
    if mu:
        rec["unleash_name"] = mu.group(1).strip()
        return
    mj = UNLEASH_LIT_RE.match(s)
    if mj:
        rec["unleash_name_literal"] = mj.group(1).strip()
        return
    if CURSED_RE.match(s):
        rec["is_cursed"] = True
        return
    if BREAK_RE.search(s):
        rec["may_break"] = True
        return
    if CRIT_RE.match(s):
        rec["increases_critical"] = True
        rec["effects"].append(s)
        return
    if NOTRADE_RE.match(s):
        rec["can_trade"] = False
        return
    bm = BUY_RE.match(s)
    if bm:
        rec["buy_price"] = int(bm.group(1))
        return
    sm = SELL_RE.match(s)
    if sm:
        rec["sell_price"] = int(sm.group(1))
        return
    # everything else = descriptive effect line (use-effects on rings/armor, etc.)
    rec["effects"].append(s)


def parse(lines):
    """Walk the TLA sections; return per-section normalized records."""
    # span both segments: from the first real section header ("-A. Long Blades")
    # through to "4. Planned Updates" (covers base -A..-R3 then TLA -2A..-2U).
    start = next(i for i, l in enumerate(lines) if section_code(l.strip()))
    end = next(i for i, l in enumerate(lines[start:], start)
               if l.strip().startswith("4. Planned Updates"))
    records = []          # list of (section code, record)
    cur = None
    code = None
    for raw in lines[start:end]:
        s = raw.strip()
        if not s or set(s) <= {"-", "="}:
            continue
        sc = section_code(s)
        if sc:
            code = sc
            cur = None
            continue
        em = ENTRY_RE.match(s)
        if em and code:
            cur = new_record(*em.groups())
            records.append((code, cur))
            continue
        if cur is not None:
            parse_attribute(cur, s)
    return records


def rusty_type(name):
    n = name.lower()
    for kw, t in (("sword", "long_sword"), ("axe", "axe"), ("mace", "mace"),
                  ("staff", "staff"), ("stick", "staff")):
        if kw in n:
            return t
    return "rusty"


def other_item_type(name):
    n = name.lower()
    if n in OTHER_CONSUMABLE:
        return "consumable"
    if n in OTHER_MATERIAL:
        return "material"
    return "key"


def build_unleash(rec):
    if not rec["unleash_name"]:
        return None
    name = rec["unleash_name"]
    out = {
        "name": name, "name_literal": rec["unleash_name_literal"],
        "element": None, "rate": None, "power_level": None,
    }
    if name in UNLEASH_FIXES:
        out["name"] = UNLEASH_FIXES[name]
        out["name_variants"] = [name]
    return out


def build_use_effect(rec):
    descs = [e for e in rec["effects"] if not CRIT_RE.match(e)]
    if rec["may_break"] or descs:
        return {"description": "; ".join(descs) if descs else None,
                "may_break": rec["may_break"]}
    return None


def enrich(records):
    equipment, items = [], []
    seen = {}
    for code, r in records:
        entity, a, b = SECTION[code]
        # base/shared segment uses single-letter codes (no "2" prefix) -> game gs1
        game = "gs2" if code.startswith("2") else "gs1"
        # canonical-name correction (90Kirsdarke real-game name over US-column quirk)
        orig_name = r["name"]
        canon = NAME_FIXES.get(orig_name)
        name = canon or orig_name
        name_variants = []
        if r.get("name_annotation"):
            name_variants.append(r["name_annotation"])
        if canon:
            name_variants.append(orig_name)
        sources = [SOURCE_ID] + ([KIRS_SRC] if canon else [])
        eid = slug(name)
        if eid in seen:
            seen[eid] += 1
            eid = f"{eid}-{seen[eid]}"
        else:
            seen[eid] = 1
        if entity == "equipment":
            category, etype = a, b
            if code == "2Q":
                etype = rusty_type(name)
            equipment.append({
                "id": eid, "name": name, "game": game,
                "name_literal": r["name_literal"],
                "name_variants": name_variants,
                "category": category, "type": etype,
                "is_cursed": r["is_cursed"],
                "is_rusty": code == "2Q",
                "is_artifact": None,           # deferred (source doesn't mark)
                "forged_from": [],             # gs2 forging edge — deferred
                "equippable_by": [],           # deferred (no equip table here)
                "stat_bonus": r["stat_bonus"],
                "elemental_power": r["elemental_power"],
                "elemental_resistance": r["elemental_resistance"],
                "increases_critical": r["increases_critical"],
                "unleash": build_unleash(r),
                "use_effect": build_use_effect(r),
                "effects": r["effects"],
                "debug_no": r["debug_no"],
                "buy_price": r["buy_price"], "sell_price": r["sell_price"],
                "can_trade": r["can_trade"], "sources": sources,
            })
        else:
            item_type = a if a != "other" else other_item_type(name)
            desc = "; ".join(r["effects"]) if r["effects"] else None
            items.append({
                "id": eid, "name": name, "game": game,
                "name_literal": r["name_literal"],
                "name_variants": name_variants,
                "item_type": item_type,
                "effect": {"description": desc, "target": None, "stat_boosted": None},
                "usable_in_battle": None,      # source doesn't state; deferred
                "debug_no": r["debug_no"],
                "buy_price": r["buy_price"], "sell_price": r["sell_price"],
                "can_trade": r["can_trade"], "sources": sources,
            })
    return equipment, items


def main():
    lines = SRC.read_text(encoding="utf-8", errors="replace").splitlines()
    records = parse(lines)
    equipment, items = enrich(records)

    INTER_DIR.mkdir(parents=True, exist_ok=True)
    inter = INTER_DIR / "equipment_items__mr-unorigino.json"
    inter.write_text(json.dumps([{"section": c, **r} for c, r in records],
                                ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    for out, data in ((EQUIP_OUT, equipment), (ITEMS_OUT, items)):
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    ids = [e["id"] for e in equipment] + [i["id"] for i in items]
    dupes = sorted({x for x in ids if ids.count(x) > 1})
    print(f"parsed entries        : {len(records)}")
    print(f"wrote {EQUIP_OUT.relative_to(ROOT)} : {len(equipment)} equipment")
    print(f"  weapons             : {sum(e['category'] == 'weapon' for e in equipment)}")
    print(f"  armor               : {sum(e['category'] == 'armor' for e in equipment)}")
    print(f"  cursed / rusty      : {sum(e['is_cursed'] for e in equipment)} / {sum(e['is_rusty'] for e in equipment)}")
    print(f"  with unleash        : {sum(e['unleash'] is not None for e in equipment)}")
    print(f"wrote {ITEMS_OUT.relative_to(ROOT)} : {len(items)} items")
    for t in ("material", "key", "consumable"):
        print(f"  {t:18}: {sum(i['item_type'] == t for i in items)}")
    print(f"  intermediate         : {inter.relative_to(ROOT)}")
    print(f"  id collisions (dup)  : {dupes if dupes else 'none'}")


if __name__ == "__main__":
    main()
