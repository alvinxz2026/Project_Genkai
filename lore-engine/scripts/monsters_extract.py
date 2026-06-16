"""Extract the GS1 bestiary into data/gs1/monsters.json.

Two aligned sources, SAME 152 enemies in the SAME order -> matched by index:
  - Super Slash XIII  (clean key:value stats; primary stat values)
  - Torrent Load complete list (adds regen, abilities, drop ICC rates)

Element columns differ between sources, so they are mapped by NAME:
  Venus=earth, Mars=fire, Jupiter=wind, Mercury=water.

Cross-source stat disagreements are flagged in `conflicts` (Super Slash wins
the value slot). Boss stat-lines link to bosses.json via boss_id; fightable
Djinn link to djinn.json via djinn_id.

Rerunnable: parses raw/gs1 text; no manual stat data embedded.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "raw" / "gs1"
OUT = ROOT / "data" / "gs1" / "monsters.json"

ELEM = {"venus": "earth", "mars": "fire", "jupiter": "wind", "mercury": "water"}

# Boss stat-lines (by Super Slash name) -> bosses.json id
BOSS_MAP = {
    "Mystery Woman": "menardi", "Mystery Man": "saturos",
    "Tret": "tret", "Saturos": "saturos", "Killer Ape": "killer-ape",
    "Hydros Statue": "hydros-statue", "Manticore": "manticore", "Kraken": "kraken",
    "Toadonpa": "toadonpa", "Storm Lizard": "storm-lizard",
    "Tempest Lizard": "tempest-lizard", "Menardi": "menardi",
    "Fusion Dragon": "fusion-dragon", "Deadbeard": "deadbeard",
}


def slug(s):
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", s.lower())).strip("-")


def num(s):
    m = re.search(r"-?\d+", s)
    return int(m.group()) if m else None


# ---------------- Super Slash ----------------
def parse_super_slash():
    lines = (RAW / "Various data - Super Slash.txt").read_text(encoding="utf-8", errors="replace").splitlines()
    start = next(i for i, l in enumerate(lines) if l.strip() == "XIII. Enemies")
    end = next(i for i, l in enumerate(lines) if l.strip() == "XIV. Shops")
    out = []
    cur = None
    for l in lines[start:end]:
        m = re.match(r"^(\d{3})\. (.+)$", l.strip())
        if m:
            raw_name = m.group(2).strip()
            vm = re.match(r"^(.*?) \((\d+)\)$", raw_name)
            name = vm.group(1).strip() if vm else raw_name
            variant = int(vm.group(2)) if vm else None
            cur = {"name": name, "raw_name": raw_name, "variant": variant,
                   "found": [], "power": {}, "resist": {}, "items": [],
                   "hp": None, "pp": None, "atk": None, "def": None,
                   "agi": None, "lck": None, "turns": None, "exp": None, "coins": None}
            out.append(cur)
            continue
        if cur is None:
            continue
        s = l.strip()
        if s.startswith("Found:"):
            cur["found"] = [x.strip() for x in s[6:].split(",")
                            if x.strip() and x.strip().lower() not in ("n/a", "none", "nothing", "-")]
        elif s.startswith("HP:"): cur["hp"] = num(s)
        elif s.startswith("PP:"): cur["pp"] = num(s)
        elif s.startswith("Attack:"): cur["atk"] = num(s)
        elif s.startswith("Defense:"): cur["def"] = num(s)
        elif s.startswith("Agility:"): cur["agi"] = num(s)
        elif s.startswith("Luck:"): cur["lck"] = num(s)
        elif s.startswith("Turns:"): cur["turns"] = num(s)
        elif s.startswith("EXP Gained:"): cur["exp"] = num(s)
        elif s.startswith("Power ("):
            e = re.search(r"Power \((\w+)\):", s).group(1).lower()
            cur["power"][ELEM[e]] = num(s.split(":", 1)[1])
        elif s.startswith("Resist ("):
            e = re.search(r"Resist \((\w+)\):", s).group(1).lower()
            cur["resist"][ELEM[e]] = num(s.split(":", 1)[1])
        elif s.startswith("Items Obtained:"):
            body = s.split(":", 1)[1].strip()
            for part in [p.strip() for p in body.split(",") if p.strip()]:
                cm = re.match(r"^(\d+)\s+Coins?$", part)
                if cm:
                    cur["coins"] = int(cm.group(1))
                elif part.lower() not in ("nothing", "n/a", "none", "-", ""):
                    cur["items"].append(part)
    return out


# ---------------- Torrent Load ----------------
def parse_torrent():
    lines = (RAW / "Comprehensive Enemy List - Torrent Load.txt").read_text(encoding="utf-8", errors="replace").splitlines()
    start = next(i for i, l in enumerate(lines) if "IV/1 - Complete List" in l)
    # the complete list is IV/1 only; it ends where IV/2 (Sort By HP) begins
    end = next(i for i, l in enumerate(lines) if i > start and "IV/2" in l and "Sort" in l)
    out = []
    cur = None
    section = None
    pending_regen = None  # 'hp' or 'pp' -> next Regen belongs to it
    elem_cols = None
    for l in lines[start:end]:
        hm = re.match(r"^~~~ (.+?) ~~~$", l.strip())
        if hm:
            name = hm.group(1).strip()
            if "IV/" in name or "Complete List" in name:
                continue
            cur = {"name": name, "found": [], "power": {}, "resist": {},
                   "abilities": [], "items": [], "hp": None, "pp": None,
                   "hp_regen": None, "pp_regen": None, "atk": None, "def": None,
                   "agi": None, "lck": None, "turns": None, "exp": None, "coins": None}
            out.append(cur)
            section = None
            pending_regen = None
            elem_cols = None
            continue
        if cur is None:
            continue
        s = l.strip()
        sm = re.match(r"^::(.+?)::$", s)
        if sm:
            # Recognize ANY ::Section:: marker. Known ones (stats/abilities/drops/
            # location) are parsed below; unknown ones (e.g. ::Carries:: on the
            # Hobgoblin) set a section with no handler, so their lines are skipped
            # rather than leaking into the previous section's data.
            section = sm.group(1).strip().lower()
            continue
        if not s or set(s) <= {"~"}:   # skip blanks and block-border tildes
            continue
        if section == "stats":
            if s.startswith("Ven"):
                elem_cols = [ELEM[w.lower()] for w in
                             ["Venus", "Mercury", "Mars", "Jupiter"]]  # Ven Mrc Mar Jup
                continue
            mp = re.match(r"^(Power|Resist)\s+(.+)$", s)
            if mp and elem_cols:
                vals = [int(x) for x in re.findall(r"-?\d+", mp.group(2))]
                tgt = cur["power"] if mp.group(1) == "Power" else cur["resist"]
                for col, v in zip(elem_cols, vals):
                    tgt[col] = v
                continue
            lm = re.match(r"^(HP|PP|Regen|Attack|Defense|Agility|Luck|Turns)\s+(-?\d+)$", s)
            if lm:
                lab, val = lm.group(1), int(lm.group(2))
                if lab == "HP": cur["hp"] = val; pending_regen = "hp"
                elif lab == "PP": cur["pp"] = val; pending_regen = "pp"
                elif lab == "Regen":
                    if pending_regen == "hp": cur["hp_regen"] = val
                    elif pending_regen == "pp": cur["pp_regen"] = val
                    pending_regen = None
                elif lab == "Attack": cur["atk"] = val
                elif lab == "Defense": cur["def"] = val
                elif lab == "Agility": cur["agi"] = val
                elif lab == "Luck": cur["lck"] = val
                elif lab == "Turns": cur["turns"] = val
        elif section == "abilities":
            am = re.match(r"^\*\s*(.+)$", s)
            if am:
                cur["abilities"].append(am.group(1).strip())
        elif section == "drops":
            em = re.match(r"^(\d+)\s+EXP$", s)
            gm = re.match(r"^(\d+)\s+Gold$", s)
            im = re.match(r"^(.+?)\s+\(ICC\s+(\d+)\)$", s)
            if em: cur["exp"] = int(em.group(1))
            elif gm: cur["coins"] = int(gm.group(1))
            elif im: cur["items"].append({"name": im.group(1).strip(), "icc": int(im.group(2))})
            elif s.lower() != "nothing":
                cur["items"].append({"name": s, "icc": None})
        elif section == "location":
            cur["found"].append(s)
    return out


# ---------------- Merge ----------------
def main():
    ss = parse_super_slash()
    tl = parse_torrent()
    assert len(ss) == 152, len(ss)
    assert len(tl) == 152, len(tl)

    djinn_ids = {e["id"] for e in json.load(open(ROOT / "data/gs1/djinn.json", encoding="utf-8"))}
    boss_ids = {e["id"] for e in json.load(open(ROOT / "data/gs1/bosses.json", encoding="utf-8"))}

    monsters = []
    excluded_bosses = []
    total_conf = 0
    for a, b in zip(ss, tl):
        name = a["name"]
        variant = a["variant"]
        mid = slug(a["raw_name"]) if variant is None else f"{slug(name)}-{variant}"

        # Bosses live in bosses.json (richer: encounters/attacks/strategy).
        # Exclude their stat-lines here; keep the parsed stats only for the
        # exclusion report (future cross-validation of bosses.json).
        boss_id = BOSS_MAP.get(name)
        if boss_id and boss_id in boss_ids:
            excluded_bosses.append((a["raw_name"], boss_id, b["found"]))
            continue

        is_djinn = "Djinni" in name
        djinn_id = None
        if is_djinn:
            inner = re.search(r"\((\w+)\)", a["raw_name"])
            if inner and inner.group(1).lower() in djinn_ids:
                djinn_id = inner.group(1).lower()

        found = list(dict.fromkeys(a["found"] + b["found"]))

        conflicts = []
        def pick(key, av, bv):
            nonlocal conflicts
            if av is not None and bv is not None and av != bv:
                conflicts.append({"field": key,
                                  "values": {"super-slash": av, "torrent-load": bv},
                                  "note": None})
            return av if av is not None else bv

        stats = {
            "hp": pick("stats.hp", a["hp"], b["hp"]),
            "pp": pick("stats.pp", a["pp"], b["pp"]),
            "hp_regen": b["hp_regen"],
            "pp_regen": b["pp_regen"],
            "atk": pick("stats.atk", a["atk"], b["atk"]),
            "def": pick("stats.def", a["def"], b["def"]),
            "agi": pick("stats.agi", a["agi"], b["agi"]),
            "lck": pick("stats.lck", a["lck"], b["lck"]),
            "turns": pick("stats.turns", a["turns"], b["turns"]),
        }
        epow = {e: pick(f"elemental_power.{e}", a["power"].get(e), b["power"].get(e))
                for e in ("earth", "fire", "wind", "water")}
        eres = {e: pick(f"elemental_resistance.{e}", a["resist"].get(e), b["resist"].get(e))
                for e in ("earth", "fire", "wind", "water")}

        exp = pick("drops.exp", a["exp"], b["exp"])
        coins = pick("drops.coins", a["coins"], b["coins"])

        # items: Torrent (with ICC) is primary; flag if SS lists a different set
        items = b["items"]
        ss_set = {i.lower() for i in a["items"]}
        tl_set = {i["name"].lower() for i in items}
        if ss_set and ss_set != tl_set:
            conflicts.append({"field": "drops.items",
                              "values": {"super-slash": sorted(ss_set), "torrent-load": sorted(tl_set)},
                              "note": None})
            # include SS-only items (no ICC)
            for nm in a["items"]:
                if nm.lower() not in tl_set:
                    items = items + [{"name": nm, "icc": None}]

        total_conf += len(conflicts)
        m = {
            "id": mid, "name": name, "game": "gs1", "variant": variant,
            "is_djinn_enemy": is_djinn, "djinn_id": djinn_id,
            "found": found, "stats": stats,
            "elemental_power": epow, "elemental_resistance": eres,
            "abilities": b["abilities"],
            "drops": {"exp": exp, "coins": coins, "items": items},
            "sources": ["super-slash", "torrent-load"],
        }
        if conflicts:
            m["conflicts"] = conflicts
        monsters.append(m)

    # unique ids
    seen = {}
    for m in monsters:
        if m["id"] in seen:
            seen[m["id"]] += 1
            m["id"] = f"{m['id']}-dup{seen[m['id']]}"
        else:
            seen[m["id"]] = 1

    OUT.write_text(json.dumps(monsters, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)} : {len(monsters)} monsters (152 - {len(excluded_bosses)} bosses)")
    print(f"  djinn enemies   : {sum(m['is_djinn_enemy'] for m in monsters)}")
    print(f"  with conflicts  : {sum('conflicts' in m for m in monsters)}  (total {total_conf})")
    print(f"  id collisions    : {sum(v>1 for v in seen.values())}")
    print(f"  excluded bosses ({len(excluded_bosses)}, -> bosses.json):")
    for raw, bid, loc in excluded_bosses:
        print(f"    {raw:22} -> {bid:14} {loc}")


if __name__ == "__main__":
    main()
