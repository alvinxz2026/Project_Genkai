"""Extract GS2 (TLA) equipment + gs2-specific items from mr-unorigino's Item List.

Deterministic parser (no LLM/API), mirroring scripts/monsters_extract_gs2.py.

Primary source: `Item List by Mr_UnOrigino` — a single clean data table that
cross-lists **GS1 and TLA** items in debug-room order. Each entry is:

    <debug_no> / <Japanese> / <English-literal> / <GS-US English name>
    <attribute lines...>
    Buy: N coins      (optional)
    Sell: N coins      (optional)

Only the **TLA sections (2A-2U)** are parsed — the GS1-numbered sections are
gs1 data (extracted separately; "two independent truth sources, no import").
This means TLA-exclusive equipment + gs2-only items (forging materials, trident
pieces, TLA "other" items) are captured here; consumables shared with GS1
(Herb / Potion / Psy Crystal / stat-boost foods) live only in the GS1-numbered
sections and are DEFERRED to a later pass against a TLA-complete appendix source.

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
}

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
SECTION_RE = re.compile(r"^-?(2[A-U]\d?)\.\s+(.+)$")
ENTRY_RE = re.compile(r"^(\d+)\s*/\s*(.+?)\s*/\s*(.+?)\s*/\s*(.+?)$")
BUY_RE = re.compile(r"^Buy:\s*(\d+)\s*coins?$", re.I)
SELL_RE = re.compile(r"^Sell:\s*(\d+)\s*coins?$", re.I)
# Greedy to the LAST quote so apostrophes inside the name survive
# (e.g. "Acheron's Grief" must not truncate at "Acheron").
UNLEASH_US_RE = re.compile(r"^US\s*-\s*Unleashe?s? '(.+)'\s*$", re.I)
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


def new_record(debug_no, jp, en_literal, us_name):
    # `jp` (4th-column katakana) is mojibake under this file's encoding -> dropped.
    # `en_literal` is clean ASCII (a useful alternate name) -> kept.
    return {
        "debug_no": int(debug_no),
        "name": us_name.strip(),
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
    start = next(i for i, l in enumerate(lines) if l.strip().startswith("-2A."))
    end = next(i for i, l in enumerate(lines[start:], start)
               if l.strip().startswith("4. Planned Updates"))
    records = []          # list of (section_code, record)
    cur = None
    section_code = None
    for raw in lines[start:end]:
        s = raw.strip()
        if not s or set(s) <= {"-", "="}:
            continue
        sm = SECTION_RE.match(s)
        if sm and sm.group(1) in SECTION:
            section_code = sm.group(1)
            cur = None
            continue
        em = ENTRY_RE.match(s)
        if em and section_code:
            cur = new_record(*em.groups())
            records.append((section_code, cur))
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
    return {
        "name": rec["unleash_name"], "name_literal": rec["unleash_name_literal"],
        "element": None, "rate": None, "power_level": None,
    }


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
        eid = slug(r["name"])
        if eid in seen:
            seen[eid] += 1
            eid = f"{eid}-{seen[eid]}"
        else:
            seen[eid] = 1
        if entity == "equipment":
            category, etype = a, b
            if code == "2Q":
                etype = rusty_type(r["name"])
            equipment.append({
                "id": eid, "name": r["name"], "game": "gs2",
                "name_literal": r["name_literal"],
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
                "can_trade": r["can_trade"], "sources": [SOURCE_ID],
            })
        else:
            item_type = a if a != "other" else other_item_type(r["name"])
            desc = "; ".join(r["effects"]) if r["effects"] else None
            items.append({
                "id": eid, "name": r["name"], "game": "gs2",
                "name_literal": r["name_literal"],
                "item_type": item_type,
                "effect": {"description": desc, "target": None, "stat_boosted": None},
                "usable_in_battle": None,      # source doesn't state; deferred
                "debug_no": r["debug_no"],
                "buy_price": r["buy_price"], "sell_price": r["sell_price"],
                "can_trade": r["can_trade"], "sources": [SOURCE_ID],
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
