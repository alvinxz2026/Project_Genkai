"""C4: parse the 3 structured equipment sources -> read-only coverage/conflict report.

Goal of C4: fill the ~54 basic weapons/armor that shops.json references but
equipment.json (artifact-biased) lacks, AND cross-check the existing 87 entries'
ATK/DEF against the new sources.

New structured sources (all GS1-clean tables):
  shotgunnova    [EQPT] one fixed-width table covering every category: USE flags
                 (IGIM), ATK/DEF/AGL/LCK, UNLEASH/EFFECT, COST, artifact '*',
                 cursed '|C|', plus element footnotes. NOT 100% complete
                 (missing e.g. Battle Axe, Hunter's Sword).
  super-slash    §VII Weapons / §VIII Armor / §IX Accessories: per-item block
                 Found / Buy Price / Stats(+N Attack, +N Fire Resistance, ...) / Effect.
  electrospecter §8 Weapons / §10 Armor: per-TYPE tables (LONG SWORDS / AXES / ...
                 HELMS / ROBE / SHIELD / ...) -> authoritative `type` buckets;
                 Name | ATK|DEF | Price | Location/Notes.

This module only parses + reports; equipment_apply.py builds the JSON.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "raw" / "gs1"


def read(name):
    return (RAW / name).read_text(encoding="utf-8", errors="replace").splitlines()


def norm(s):
    return re.sub(r"[^a-z0-9]", "", s.lower())


# character equip-flag positions in Shotgunnova's "USE?" column (IGIM)
FLAG_CHARS = ["Isaac", "Garet", "Ivan", "Mia"]


def parse_flags(f):
    """'IG--' -> ['Isaac','Garet']; pos0=Isaac pos1=Garet pos2=Ivan pos3=Mia."""
    f = f.strip()
    out = []
    for i, want in enumerate(("I", "G", "I", "M")):
        if i < len(f) and f[i] == want:
            out.append(FLAG_CHARS[i])
    return out


def cell_num(c):
    """stat cell: '---'->0, 'x.5'/'x1.5'->('mult', float), number->int."""
    c = c.strip()
    if c in ("---", "--", "", "-"):
        return 0
    m = re.match(r"^x([\d.]+)$", c)
    if m:
        return ("mult", float(m.group(1)) if m.group(1)[0] != "." else float("0" + m.group(1)))
    if c.isdigit():
        return int(c)
    return 0


# ---------- Shotgunnova [EQPT] ----------
SHOT_WEAPON_CATS = {"WEAPON"}
SHOT_ARMOR_CATS = {"ARMOR", "HEADGEAR", "ACCESSORIES", "SHIRTS", "BOOTS"}


def parse_shotgunnova():
    lines = read("Various data - Shotgunnova.txt")
    start = next(i for i, l in enumerate(lines) if l.startswith("EQUIPMENT LIST"))
    end = next(i for i, l in enumerate(lines) if i > start and l.strip().startswith("____") and i > start + 5 and "RINGS" not in l)
    out = {}
    cat = None
    for l in lines[start:]:
        hm = re.match(r"^\s*\|\s*([A-Z]{4,})\s*\|\s*USE\?", l)
        if hm:
            cat = hm.group(1)
            if cat in ("RINGS", "ITEMS"):  # rings already in equipment.json; items elsewhere
                cat = cat  # keep parsing rings for cross-check but skip ITEMS adds
            continue
        if cat is None or "|" not in l:
            continue
        artifact = l.lstrip().startswith("*")
        cursed = bool(re.search(r"\|C\|", l)) or l.rstrip().endswith("|C")
        cells = [c.strip() for c in l.split("|")]
        # leading cell is '' or '*'; expect name,flags,atk,def,agl,lck,effect,cost
        cells = [c for c in cells]
        # find the name cell: first cell after the (possibly '*') marker
        try:
            idx = 1  # cells[0] is '' or '*'
            name = cells[idx]
            flags = cells[idx + 1]
            atk, dfn, agl, lck = cells[idx + 2:idx + 6]
            effect = cells[idx + 6]
            cost = cells[idx + 7]
        except (ValueError, IndexError):
            continue
        if not re.match(r"^[A-Za-z]", name) or not re.match(r"^[IGM\-]{4}$", flags):
            continue
        out[norm(name)] = {
            "name": name, "category": cat, "is_artifact": artifact, "is_cursed": cursed,
            "equippable_by": parse_flags(flags),
            "atk": cell_num(atk), "def": cell_num(dfn), "agl": cell_num(agl), "lck": cell_num(lck),
            "effect": effect, "cost": (int(cost) if cost.isdigit() else None),
            "raw": l.strip(),
        }
        if cat == "ITEMS":
            del out[norm(name)]  # don't add consumables here
    return out


# ---------- Super Slash §VII-IX ----------
def parse_superslash():
    lines = read("Various data - Super Slash.txt")
    start = next(i for i, l in enumerate(lines) if re.match(r"^VII\. Weapons", l))
    end = next(i for i, l in enumerate(lines) if re.match(r"^X\. Djinn", l))
    region = lines[start:end]
    out = {}
    cur = None
    collecting_stats = False
    for j, l in enumerate(region):
        s = l.strip()
        if re.match(r"^Found:", s):
            if cur:
                out[cur]["location"] = re.sub(r"^Found:\s*", "", s)
            collecting_stats = False
        elif re.match(r"^Buy Price:", s):
            if cur:
                v = re.sub(r"^Buy Price:\s*", "", s)
                m = re.search(r"([\d,]+)", v)
                out[cur]["price"] = int(m.group(1).replace(",", "")) if m else None
            collecting_stats = False
        elif re.match(r"^Stats:", s):
            if cur:
                first = re.sub(r"^Stats:\s*", "", s)
                if first and first != "N/A":
                    out[cur]["stats"].append(first)
            collecting_stats = True
        elif re.match(r"^Effect:", s):
            if cur:
                out[cur]["effect"] = re.sub(r"^Effect:\s*", "", s)
            collecting_stats = False
        elif collecting_stats and re.match(r"^[+\-]?\d|^Agility x|^Max", s):
            if cur:
                out[cur]["stats"].append(s)
        elif re.match(r"^[A-Z][A-Za-z'.\- ]+$", s) and len(s) < 24:
            # potential item name: only if next non-blank line is Found:
            nxt = next((region[k].strip() for k in range(j + 1, min(j + 4, len(region))) if region[k].strip()), "")
            if nxt.startswith("Found:"):
                cur = norm(s)
                out[cur] = {"name": s, "location": None, "price": None, "stats": [], "effect": None}
            collecting_stats = False
    return out


# ---------- ElectroSpecter §8 / §10 ----------
ES_TYPE = {
    "LONG SWORDS": "long_sword", "LIGHT SWORDS": "light_blade", "AXES": "axe",
    "MACES": "mace", "STAVES": "staff",
    "HELMS": "helm", "ROBE": "robe", "SHIELD": "shield", "GLOVES": "gloves",
    "BRACELETS": "bracelet", "CIRCLETS": "circlet", "CLOTHING": "clothing",
    "ARMOR": "armor",  # "HATS AND CROWNS" handled separately (-> hat default)
}
ES_WEAPON_TYPES = {"long_sword", "light_blade", "axe", "mace", "staff"}


def parse_electrospecter():
    lines = read("Classes Djinn Weapons Armor Equipment - ElectroSpecter.txt")
    out = {}
    cur_type = None
    last = None
    for l in lines:
        # a section header is a single-cell boxed title row: "| TITLE (Used by ...) |"
        hm = re.match(r"^\|\s*([A-Z][A-Z'&. ]+?)\s*(?:\([^)]*\))?\s*\|\s*$", l)
        if hm:
            head = hm.group(1).strip()
            cur_type = ES_TYPE.get(head, "hat" if "HAT" in head else None)
            last = None
            continue
        if cur_type is None or "|" not in l:
            continue
        cells = [c.strip() for c in l.split("|")]
        if len(cells) < 5:
            continue
        name, statc, price, notes = cells[1], cells[2], cells[3], cells[4]
        if name in ("Weapon", "Armor", "") and not statc:
            # continuation line (name blank): attach notes to last
            if last and notes:
                out[last]["notes"].append(notes)
            continue
        if name in ("Weapon", "Armor") or not re.match(r"^[A-Za-z]", name):
            if last and notes and not name:
                out[last]["notes"].append(notes)
            continue
        stat = int(statc) if statc.isdigit() else None
        pr = int(price.replace(",", "")) if price.replace(",", "").isdigit() else None
        rec = {"type": cur_type, "price": pr, "location": notes, "notes": [],
               "atk": stat if cur_type in ES_WEAPON_TYPES else None,
               "def": stat if cur_type not in ES_WEAPON_TYPES else None}
        out[norm(name)] = rec
        last = norm(name)
    return out


def missing_set():
    E = json.load(open(ROOT / "data/gs1/equipment.json", encoding="utf-8"))
    I = json.load(open(ROOT / "data/gs1/items.json", encoding="utf-8"))
    S = json.load(open(ROOT / "data/gs1/shops.json", encoding="utf-8"))
    have = {norm(e["name"]) for e in E} | {norm(i["name"]) for i in I}
    stock = {}
    for sh in S:
        for st in sh.get("stock", []):
            stock.setdefault(norm(st["name"]), st["name"])
    return {k: v for k, v in stock.items() if k not in have}, E


def main():
    sh = parse_shotgunnova()
    ss = parse_superslash()
    es = parse_electrospecter()
    print(f"parsed: shotgunnova={len(sh)} super-slash={len(ss)} electrospecter={len(es)}")

    missing, E = missing_set()
    print(f"\n=== {len(missing)} missing basics: source coverage ===")
    notfound = []
    for nk, name in sorted(missing.items(), key=lambda x: x[1]):
        s, u, e = sh.get(nk), ss.get(nk), es.get(nk)
        srcs = "".join(c if v else "-" for c, v in (("S", s), ("U", u), ("E", e)))
        if not (s or u or e):
            notfound.append(name)
        atk = {k: v for k, v in (("S", s and s["atk"]), ("U", None), ("E", e and e["atk"])) if v}
        dfn = {k: v for k, v in (("S", s and s["def"]), ("E", e and e["def"])) if v}
        typ = e["type"] if e else "?"
        print(f"  [{srcs}] {name:18} type={typ:11} atk={atk} def={dfn}")
    if notfound:
        print(f"  !! NOT FOUND in any source: {notfound}")

    # cross-check existing 87 ATK/DEF vs new sources
    print("\n=== existing-entry ATK/DEF conflicts vs new sources ===")
    n = 0
    for ent in E:
        nk = norm(ent["name"])
        cur_atk = ent["stat_bonus"]["atk"]
        cur_def = ent["stat_bonus"]["def"]
        for src, rec in (("shotgunnova", sh.get(nk)), ("electrospecter", es.get(nk))):
            if not rec:
                continue
            if rec.get("atk") not in (None, 0) and rec["atk"] != cur_atk:
                print(f"  {ent['id']:20} atk json={cur_atk} {src}={rec['atk']}"); n += 1
            if rec.get("def") not in (None, 0) and rec["def"] != cur_def:
                print(f"  {ent['id']:20} def json={cur_def} {src}={rec['def']}"); n += 1
    print(f"  ({n} potential conflicts on existing entries)")


if __name__ == "__main__":
    main()
