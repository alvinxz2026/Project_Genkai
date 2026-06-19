"""Extract GS2 shop stock into data/gs2/shops.json + harvest shared consumables
into data/gs2/items.json.

Source: `shotgunnova-shop` (Shop List) — one boxed fixed-width table per town:
  [SHnn] - TOWN [optional note]
   | ITEM | USE? | ATK | DEF | AGL | LCK | UNLEASH/EFFECT | COST |
A leading '*' on a row marks an artifact.

Two outputs:
  1. shops.json — per-town stock [{name, category, price, is_artifact}]. The
     stock name -> equipment|item ref is resolved later by links_normalize_gs2.
  2. items.json — MERGE the shop's consumables (rows with no ATK/DEF: Herb,
     Antidote, Elixir, ...). These are gs1<->gs2 shared consumables that the
     TLA-only equipment/items extraction deliberately deferred; the shop is the
     sanctioned gs2 source to backfill them. Idempotent merge keyed by id.

NOTE (deferred, by decision): the ~73 shared *basic gear* rows (Long Sword,
Battle Axe, ...) are NOT harvested into equipment.json this pass — they need
name->type inference the shop doesn't provide. They remain expected-gap shop
refs until a later focused pass.

Rerunnable / deterministic; no manual data embedded.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "raw" / "gs2" / "In-Depth Guides" / "Shop List by Shotgunnova.md"
DATA = ROOT / "data" / "gs2"

HEADER = re.compile(r"^\[SH\d+\]\s*-\s*(.+)$")


def slug(s):
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", s.lower())).strip("-")


def has_num(s):
    return bool(re.search(r"\d", s))


def categorize(atk, dfn):
    if has_num(dfn):
        return "armor"        # gloves with atk+def land here too (gs1 convention)
    if has_num(atk):
        return "weapon"
    return "item"             # consumable (no atk/def)


def parse_shops():
    lines = RAW.read_text(encoding="utf-8").splitlines()
    # body starts after the TOC fence
    try:
        start = next(i for i, l in enumerate(lines)
                     if l.strip() == "END OF TABLE OF CONTENTS")
    except StopIteration:
        start = 0
    shops = []
    cur = None
    for raw in lines[start:]:
        stripped = raw.strip()
        m = HEADER.match(stripped)
        if m:
            head = m.group(1).strip()
            note = None
            nm = re.search(r"\[(.+)\]", head)
            if nm:
                note = nm.group(1).strip()
            name = head.split("[")[0].strip().title()
            cur = {"id": slug(name), "name": name, "game": "gs2",
                   "location": name, "availability_notes": note, "stock": [],
                   "sources": ["shotgunnova-shop"]}
            shops.append(cur)
            continue
        # stock row: "*| Magic Rod | ... |" or " | Herb | ... |"
        body = stripped.lstrip("*").strip()
        if not body.startswith("|") or body.count("|") < 8:
            continue
        parts = [p.strip() for p in body.split("|")][1:-1]
        if len(parts) < 8:
            continue
        name, use, atk, dfn, agi, lck, effect, cost = parts[:8]
        if not re.search(r"[A-Za-z]", name) or name.upper() == "ITEM":
            continue
        if not has_num(cost):
            continue
        if cur is None:
            continue
        cur["stock"].append({
            "name": name,
            "category": categorize(atk, dfn),
            "price": int(re.search(r"\d+", cost).group()),
            "is_artifact": stripped.startswith("*"),
            "use": use if re.search(r"[A-Za-z]", use) else None,
            "effect": effect.strip("- ").strip() or None,
        })
    return shops


def harvest_consumables(shops):
    """Distinct shop rows categorized 'item' (no atk/def) -> item dicts."""
    seen = {}
    for s in shops:
        for st in s["stock"]:
            if st["category"] != "item":
                continue
            key = slug(st["name"])
            if key not in seen:
                seen[key] = {
                    "id": key,
                    "name": st["name"],
                    "game": "gs2",
                    "name_literal": st["name"],
                    "item_type": "consumable",
                    "effect": {"description": (st["effect"] or "").lower() or None,
                               "target": None, "stat_boosted": None},
                    "usable_in_battle": None,
                    "debug_no": None,
                    "buy_price": st["price"],
                    "sell_price": None,
                    "can_trade": True,
                    "sources": ["shotgunnova-shop"],
                }
    # drop the per-shop helper fields from stock (use/effect not stored in shops.json)
    for s in shops:
        for st in s["stock"]:
            st.pop("use", None)
            st.pop("effect", None)
    return list(seen.values())


def merge_items(consumables):
    items = json.loads((DATA / "items.json").read_text(encoding="utf-8"))
    by_id = {i["id"]: idx for idx, i in enumerate(items)}
    by_name = {re.sub(r"[^a-z0-9]", "", i["name"].lower()) for i in items}
    added = []
    for c in consumables:
        nkey = re.sub(r"[^a-z0-9]", "", c["name"].lower())
        if c["id"] in by_id:
            items[by_id[c["id"]]] = c       # idempotent refresh of shop-sourced row
        elif nkey in by_name:
            continue                         # already present under another id
        else:
            items.append(c)
            added.append(c["name"])
    (DATA / "items.json").write_text(json.dumps(items, ensure_ascii=False, indent=2) + "\n",
                                     encoding="utf-8")
    return items, added


def main():
    shops = parse_shops()
    consumables = harvest_consumables(shops)
    (DATA / "shops.json").write_text(json.dumps(shops, ensure_ascii=False, indent=2) + "\n",
                                     encoding="utf-8")
    items, added = merge_items(consumables)

    print(f"wrote shops.json: {len(shops)} towns, "
          f"{sum(len(s['stock']) for s in shops)} stock rows")
    for s in shops:
        arts = sum(x["is_artifact"] for x in s["stock"])
        print(f"  {s['name']:16} stock={len(s['stock']):2}  artifacts={arts}")
    print(f"\nitems.json now {len(items)} entries; "
          f"harvested {len(added)} shared consumables: {added}")


if __name__ == "__main__":
    main()
