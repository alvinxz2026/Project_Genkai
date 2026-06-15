"""Extract GS1 shop stock into data/gs1/shops.json.

Primary source: Shotgunnova [SHPL] (combined per-town table with COST + "*" artifacts).
Cross-check: Super Slash XIV (Weapon/Armor/Item split per town, no artifacts) -> price conflicts.

Rerunnable: parses raw/gs1 text files; no manual data embedded.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "raw" / "gs1"
OUT = ROOT / "data" / "gs1" / "shops.json"

TOWNS = ["Vale", "Vault", "Bilibin", "Imil", "Kolima", "Xian",
         "Altin", "Kalay", "Tolbi", "Lunpa", "Suhalla", "Lalivero"]
TOWN_UPPER = {t.upper(): t for t in TOWNS}
SLUG = {t: t.lower() for t in TOWNS}


def categorize(atk, dfn):
    has = lambda s: bool(re.search(r"\d", s))
    if has(dfn):
        return "armor"            # incl. gloves (War Gloves has atk+def)
    if has(atk):
        return "weapon"
    return "item"


def parse_shotgunnova():
    text = (RAW / "Various data - Shotgunnova.txt").read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()
    # isolate the SHPL section
    start = next(i for i, l in enumerate(lines) if l.startswith("SHOP LIST"))
    end = next(i for i, l in enumerate(lines) if l.startswith("EQUIPMENT LIST"))
    towns = {}
    cur = None
    for raw in lines[start:end]:
        line = raw.rstrip()
        stripped = line.strip()
        # town header: e.g. "VALE", "IMIL   [NOTE...]"
        head = stripped.split("[")[0].strip()
        if head in TOWN_UPPER:
            name = TOWN_UPPER[head]
            note = None
            m = re.search(r"\[(.*)\]", stripped)
            if m:
                note = m.group(1).strip()
            cur = {"id": SLUG[name], "name": name, "game": "gs1",
                   "availability_notes": note, "stock": [],
                   "sources": ["shotgunnova", "super-slash"]}
            towns[name] = cur
            continue
        # stock row
        body = stripped.lstrip("*").strip()
        if not body.startswith("|") or body.count("|") < 8:
            continue
        artifact = stripped.startswith("*")
        parts = [p.strip() for p in body.split("|")][1:-1]
        if len(parts) < 8:
            continue
        name, use, atk, dfn, agi, lck, effect, cost = parts[:8]
        if not re.search(r"[A-Za-z]", name) or name.upper() == "WEAPON":
            continue
        if not re.search(r"\d", cost):
            continue
        cur["stock"].append({
            "name": name,
            "category": categorize(atk, dfn),
            "price": int(re.search(r"\d+", cost).group()),
            "is_artifact": artifact,
        })
    return towns


# Known Super Slash spelling typos -> canonical (Shotgunnova) name
SS_TYPO = {"plantinum circlet": "platinum circlet"}


def norm(name):
    n = name.strip().lower()
    return SS_TYPO.get(n, n)


def parse_super_slash():
    text = (RAW / "Various data - Super Slash.txt").read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()
    start = next(i for i, l in enumerate(lines) if l.strip() == "XIV. Shops")
    stock = {t: {} for t in TOWNS}   # town -> norm_name -> (display, price, category)
    cur = None
    cat = None
    for raw in lines[start:]:
        s = raw.strip()
        if s in TOWNS:
            cur = s; cat = None; continue
        if s.startswith("Weapon Shop"):
            cat = "weapon"; continue
        if s.startswith("Armor Shop"):
            cat = "armor"; continue
        if s.startswith("Item Shop"):
            cat = "item"; continue
        m = re.match(r"^(.+?) - (\d+) Coins$", s)
        if m and cur:
            disp = SS_TYPO.get(m.group(1).strip().lower(), m.group(1).strip())
            stock[cur][norm(m.group(1))] = (disp, int(m.group(2)), cat)
    return stock


def main():
    towns = parse_shotgunnova()
    ss = parse_super_slash()
    added = []
    for name in TOWNS:
        t = towns[name]
        ss_town = ss.get(name, {})
        conflicts = []
        seen = {norm(item["name"]) for item in t["stock"]}
        for item in t["stock"]:
            entry = ss_town.get(norm(item["name"]))
            if entry is not None and entry[1] != item["price"]:
                conflicts.append({
                    "field": f"stock[{item['name']}].price",
                    "values": {"shotgunnova": item["price"], "super-slash": entry[1]},
                    "note": None,
                })
        # union: add real Super-Slash-only items (Shotgunnova omitted them)
        for key, (disp, price, cat) in ss_town.items():
            if key not in seen:
                t["stock"].append({
                    "name": disp, "category": cat, "price": price, "is_artifact": False,
                })
                added.append(f"  {name}: +{disp} ({cat}, {price})")
        if conflicts:
            t["conflicts"] = conflicts
    data = [towns[name] for name in TOWNS]
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    # summary
    print(f"wrote {OUT.relative_to(ROOT)} : {len(data)} towns")
    for name in TOWNS:
        t = towns[name]
        nc = len(t.get("conflicts", []))
        print(f"  {name:9} stock={len(t['stock']):2}  artifacts={sum(s['is_artifact'] for s in t['stock'])}  price_conflicts={nc}")
    print("\nPrice conflicts:")
    for name in TOWNS:
        for c in towns[name].get("conflicts", []):
            print(f"  {name}: {c['field']} {c['values']}")
    if added:
        print("\nUnion additions (Super-Slash-only items merged in):")
        print("\n".join(added))


if __name__ == "__main__":
    main()
