"""C1: compare djinn data across all sources -> diff report (read-only).

Does NOT write djinn.json. Prints a per-djinn comparison so conflicts can be
resolved by the policy (majority -> authority -> unresolved) by hand.

Sources parsed:
  terence (current djinn.json) - numeric stats authority
  Telago  - numeric stats + location + ability
  BFGamer - location prose + Fight (Y/N)  -> must_fight
  Shotgunnova - location + in-battle function
  ElectroSpecter - effect + location prose
  Super Slash  - Found + Effect prose
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "raw" / "gs1"


def read(name):
    return (RAW / name).read_text(encoding="utf-8", errors="replace").splitlines()


def stat_list(vals):
    return {k: (0 if set(v.strip()) <= {"-"} else int(v)) for k, v in
            zip(["hp", "pp", "atk", "def", "agi", "lck"], vals)}


def parse_telago():
    lines = read("Djinn Class Items Phynergy - Telago.txt")
    start = next(i for i, l in enumerate(lines) if "1. Djinn Descriptions" in l)
    end = next(i for i, l in enumerate(lines) if "2. About the Summons" in l)
    out = {}
    for l in lines[start:end]:
        m = re.match(r"^(\S+)\s+([\d-]+)\s+([\d-]+)\s+([\d-]+)\s+([\d-]+)\s+([\d-]+)\s+([\d-]+)\s+(.*)$", l)
        if not m:
            continue
        name = m.group(1)
        if name.lower() == "name" or set(name) <= {"-"}:
            continue
        rest = re.split(r"\s{2,}", m.group(8).strip())
        loc = rest[0] if rest else ""
        ability = rest[1] if len(rest) > 1 else ""
        out[name] = {"stats": stat_list(m.groups()[1:7]), "location": loc, "ability": ability}
    return out


def parse_bfgamer():
    lines = read("Djinn Items Psynergy - BFGamer.txt")
    start = next(i for i, l in enumerate(lines) if "6.1 Djinn Locations" in l)
    end = next(i for i, l in enumerate(lines) if "6.2 Djinn Summons" in l)
    out = {}
    cur = None
    field = None
    for l in lines[start:end]:
        m = re.match(r"^Name:\s*(.+)$", l)
        if m:
            cur = m.group(1).strip()
            out[cur] = {"location": "", "fight": None}
            field = None
            continue
        if cur is None:
            continue
        lm = re.match(r"^Location:\s*(.*)$", l)
        fm = re.match(r"^Fight:\s*(Yes|No)\s*$", l)
        if lm:
            out[cur]["location"] = lm.group(1).strip()
            field = "loc"
        elif fm:
            out[cur]["fight"] = (fm.group(1) == "Yes")
            field = None
        elif field == "loc" and l.strip() and not l.startswith("Name:"):
            out[cur]["location"] += " " + l.strip()
    return out


def parse_shotgunnova():
    lines = read("Various data - Shotgunnova.txt")
    start = next(i for i, l in enumerate(lines) if l.startswith("DJINN LIST"))
    end = next(i for i, l in enumerate(lines) if i > start and l.startswith("SHOP LIST"))
    out = {}
    for l in lines[start:end]:
        if not l.strip().startswith("|"):
            continue
        parts = [p.strip() for p in l.strip().split("|")][1:-1]
        if len(parts) < 5 or not re.match(r"\d", parts[0]):
            continue
        _, name, typ, loc, func = parts[:5]
        out[name] = {"location": loc, "function": func}
    return out


def parse_electrospecter():
    lines = read("Classes Djinn Weapons Armor Equipment - ElectroSpecter.txt")
    start = next(i for i, l in enumerate(lines) if "8. Djinn" in l)
    # ends at the next "\ N. <title> /" section header
    end = next((i for i, l in enumerate(lines) if i > start and re.match(r"^\\ \d+\.", l)), len(lines))
    out = {}
    in_loc = False
    for l in lines[start:end]:
        s = l.strip()
        if s.startswith("Locations"):
            in_loc = True
            continue
        if s.startswith("|"):
            in_loc = False
            parts = [p.strip() for p in s.split("|")][1:-1]
            if len(parts) >= 3 and parts[0] not in ("Djinni", "Name", "") and "Effect" not in parts[1]:
                out.setdefault(parts[0], {})["effect"] = parts[1]
            continue
        lm = re.match(r"^(\w+)\s+-\s+(.+)$", s)
        if in_loc and lm:
            out.setdefault(lm.group(1), {})["location"] = lm.group(2).strip()
    return out


def parse_superslash():
    lines = read("Various data - Super Slash.txt")
    start = next(i for i, l in enumerate(lines) if l.strip() == "X. Djinn")
    end = next(i for i, l in enumerate(lines) if l.strip() == "XI. Character Classes")
    out = {}
    cur = None
    known = None
    block = lines[start:end]
    for i, l in enumerate(block):
        s = l.strip()
        fm = re.match(r"^Found:\s*(.+)$", s)
        em = re.match(r"^Effect:\s*(.+)$", s)
        if fm and cur:
            out[cur]["found"] = fm.group(1).strip()
        elif em and cur:
            out[cur]["effect"] = em.group(1).strip()
        elif s and not s.startswith(("-", "=", "Found", "Effect", "How To Find", "Venus", "Mars", "Jupiter", "Mercury")) and re.match(r"^[A-Z][a-z]+$", s):
            # a bare capitalized single word on its own line = djinn name header
            cur = s
            out[cur] = {"found": "", "effect": ""}
    return out


def main():
    D = json.load(open(ROOT / "data/gs1/djinn.json", encoding="utf-8"))
    tel = parse_telago()
    bf = parse_bfgamer()
    sh = parse_shotgunnova()
    el = parse_electrospecter()
    ss = parse_superslash()
    # must_fight: a djinn appears as an "X Djinni" enemy in the bestiary <=> you fight it
    M = json.load(open(ROOT / "data/gs1/monsters.json", encoding="utf-8"))
    must_fight = {m["djinn_id"] for m in M if m["is_djinn_enemy"] and m["djinn_id"]}

    print("source coverage counts (expect 28):")
    for nm, d in [("telago", tel), ("bfgamer", bf), ("shotgunnova", sh),
                  ("electrospecter", el), ("super-slash", ss)]:
        print(f"  {nm:15} {len(d)}")
    print()

    stat_conflicts = []
    for d in D:
        name = d["name"]
        t = tel.get(name, {})
        if t.get("stats") and t["stats"] != d["stat_bonus"]:
            diffs = {k: (d["stat_bonus"][k], t["stats"][k]) for k in d["stat_bonus"]
                     if d["stat_bonus"][k] != t["stats"].get(k)}
            stat_conflicts.append((name, diffs))

    print(f"=== STAT conflicts (terence-json vs Telago): {len(stat_conflicts)} -> terence authority ===")
    for name, diffs in stat_conflicts:
        print(f"  {name:9} " + ", ".join(f"{k}: terence={a} telago={b}" for k, (a, b) in diffs.items()))

    print(f"\n=== must_fight (derived from §XIII bestiary, {len(must_fight)} fought) ===")
    for d in D:
        mf = d["id"] in must_fight
        bfv = bf.get(d["name"], {}).get("fight")
        flag = ""
        if bfv is not None and bfv != mf:
            flag = f"  <-- BFGamer says fight={bfv}"
        print(f"  {d['name']:9} must_fight={mf}{flag}")

    print("\n=== per-djinn location strings (eyeball majority) ===")
    for d in D:
        name = d["name"]
        locs = {
            "json": d["location"]["area"],
            "telago": tel.get(name, {}).get("location", ""),
            "bfgamer-fight": bf.get(name, {}).get("fight"),
            "shotgun": sh.get(name, {}).get("location", ""),
            "electro": el.get(name, {}).get("location", ""),
            "superslash": ss.get(name, {}).get("found", ""),
        }
        print(f"\n  {name} (cur conflicts: {len(d.get('conflicts',[]))})")
        for k, v in locs.items():
            print(f"     {k:12} {v}")


if __name__ == "__main__":
    main()
