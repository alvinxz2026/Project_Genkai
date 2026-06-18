"""Extract the GS2 bestiary into data/gs2/monsters.json.

Deterministic parser (no LLM/API), mirroring scripts/monsters_extract.py for gs1.

Primary source: torrentlord "Enemy and Boss List" (same author as gs1's Torrent
Load; different layout). Only **Division A "Complete List"** is parsed — Divisions
B/C/D… are re-sorted views of the same data. Each enemy block is anchored on its
`HP n (Regen m)` line; the name is the nonblank line just above it.

Element columns "Ven Mrc Mar Jup" are mapped by NAME:
  Venus=earth, Mercury=water, Mars=fire, Jupiter=wind.

`-Location- (n)` index refs are resolved against the legend under "Section III".

The per-source normalized records are materialized to
data/gs2/intermediate/monsters__torrentlord.json (the inspectable "intermediate
layer"); monsters.json is the merged/enriched output. With a single source there
are no cross-source conflicts; a second aligned source would merge here via a
conflict-flagging pick() (see the gs1 script).

Deferred (no gs2 djinn/bosses/items/equipment yet): boss_id, djinn_id, and drop
ref_type/ref_id stay null. is_boss uses a curated name set.

Rerunnable: parses raw text only; no manual stat data embedded.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "raw" / "gs2" / "In-Depth Guides" / "Enemy and Boss List by torrentlord.md"
OUT = ROOT / "data" / "gs2" / "monsters.json"
INTER = ROOT / "data" / "gs2" / "intermediate" / "monsters__torrentlord.json"

# Ven Mrc Mar Jup  ->  earth water fire wind
ELEM_COLS = ["earth", "water", "fire", "wind"]

# Curated boss / mini-boss base names (from the GS2 boss guides). is_boss is a
# heuristic flag until a real bosses.json exists to cross-link via boss_id.
BOSS_NAMES = {
    "chestbeater", "chestbeaters", "king scorpion", "briggs", "sea fighter",
    "aqua hydra", "serpent", "avimander", "poseidon", "moapa", "knight",
    "agatio", "karst", "flame dragon", "blaze dragon", "doom dragon",
    "star magician", "sentinel", "valukar", "dullahan", "kraken",
}

# HP/PP value may be slash-separated for multi-form bosses (e.g. "3240/3186",
# "5000 / 4200 / 4000") -> take the first value.
HP_RE = re.compile(r"^HP\s+([\d/ ]+?)\s*\(Regen\s*([0-9 /]*)\)")
PP_RE = re.compile(r"^PP\s+([\d/ ]+?)\s*\(Regen\s*([0-9 /]*)\)")
STAT_RE = re.compile(r"^(Attack|Defense|Agility|Luck|Turns)\s+([-\d/ ]+)$")
PR_RE = re.compile(r"^(Power|Resist)\s+([\d\s]+)$")
STAT_KEY = {"Attack": "atk", "Defense": "def", "Agility": "agi", "Luck": "lck", "Turns": "turns"}


def slug(s):
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", s.lower())).strip("-")


def first_int(s):
    m = re.search(r"-?\d+", s or "")
    return int(m.group()) if m else None


def find_anchor(lines, code):
    """First line index whose stripped text starts with the section code (e.g. 'dpt ')."""
    pat = re.compile(rf"^{code}\b")
    return next(i for i, l in enumerate(lines) if pat.match(l.strip()))


def parse_legend(lines):
    """{index: place name} from the '(n) - Place' table under Section III."""
    start = find_anchor(lines, "enm")
    end = find_anchor(lines, "dpt")
    legend = {}
    for l in lines[start:end]:
        m = re.match(r"^\((\d+)\)\s*-\s*(.+)$", l.strip())
        if m:
            legend[int(m.group(1))] = m.group(2).strip()
    return legend


def new_record(name_raw):
    vm = re.match(r"^(.*?)\s*#(\d+)$", name_raw)
    name = (vm.group(1) if vm else name_raw).strip()
    variant = int(vm.group(2)) if vm else None
    return {
        "name": name, "raw_name": name_raw, "variant": variant,
        "found_idx": [], "power": {}, "resist": {}, "abilities": [], "items": [],
        "hp": None, "pp": None, "hp_regen": None, "pp_regen": None,
        "atk": None, "def": None, "agi": None, "lck": None, "turns": None,
        "exp": None, "coins": None,
    }


def parse_reward(rec, text):
    t = text.strip()
    if not t:
        return
    em = re.match(r"^(\d+)\s+EXP$", t)
    cm = re.match(r"^(\d+)\s+Coins?$", t)
    im = re.match(r"^(.+?)\s+\(ICC\s+(\d+|\?)\)$", t)   # ICC may be "?" (unknown)
    if em:
        rec["exp"] = int(em.group(1))
    elif cm:
        rec["coins"] = int(cm.group(1))
    elif im:
        icc = int(im.group(2)) if im.group(2).isdigit() else None
        rec["items"].append({"name": im.group(1).strip(), "icc": icc})
    elif t.lower() in ("no item", "nothing", "none", "-"):
        pass
    else:
        rec["items"].append({"name": t, "icc": None})


def parse_enemies(lines):
    """Parse Division A 'Complete List' into normalized per-source records."""
    start = find_anchor(lines, "dpt")
    end = find_anchor(lines, "dbl")
    records = []
    cur = None
    section = None
    last_nonblank = None
    for raw in lines[start:end]:
        s = raw.strip()

        m = HP_RE.match(s)
        if m:
            cur = new_record(last_nonblank or "???")
            cur["hp"] = first_int(m.group(1))
            cur["hp_regen"] = first_int(m.group(2))
            section = "stats"
            records.append(cur)
            last_nonblank = s
            continue

        if cur is not None:
            pm = PP_RE.match(s)
            if pm:
                cur["pp"] = first_int(pm.group(1))
                cur["pp_regen"] = first_int(pm.group(2))
                last_nonblank = s
                continue
            if s.startswith("-Abilities-"):
                section = "abilities"
                last_nonblank = s
                continue
            if s.startswith("-Reward-"):
                section = "reward"
                parse_reward(cur, s[len("-Reward-"):])
                last_nonblank = s
                continue
            if s.startswith("-Location-"):
                section = "location"
                cur["found_idx"] += [int(n) for n in re.findall(r"\((\d+)[a-z]?\)", s)]
                last_nonblank = s
                continue

            if section == "stats":
                if re.match(r"^Ven\s+Mrc\s+Mar\s+Jup", s):
                    last_nonblank = s
                    continue
                pr = PR_RE.match(s)
                if pr:
                    vals = [int(x) for x in pr.group(2).split()]
                    tgt = cur["power"] if pr.group(1) == "Power" else cur["resist"]
                    for col, v in zip(ELEM_COLS, vals):
                        tgt[col] = v
                    last_nonblank = s
                    continue
                st = STAT_RE.match(s)
                if st:
                    cur[STAT_KEY[st.group(1)]] = first_int(st.group(2))
                    last_nonblank = s
                    continue
                # else: junk ([N LIGHTS], 'Regen X HP, 3 Turns.', etc.) -> skip
            elif section == "abilities":
                am = re.match(r"^\*\s*(.+)$", s)
                if am:
                    cur["abilities"].append(am.group(1).strip())
            elif section == "reward":
                parse_reward(cur, s)
            elif section == "location":
                cur["found_idx"] += [int(n) for n in re.findall(r"\((\d+)[a-z]?\)", s)]

        if s:
            last_nonblank = s
    return records


def normalize(records, legend):
    """Resolve locations + element dicts; the on-disk intermediate-layer shape."""
    out = []
    unresolved = set()
    for r in records:
        found = []
        for i in r["found_idx"]:
            if i in legend:
                if legend[i] not in found:   # dedupe (e.g. "(10) (10a)" -> same area)
                    found.append(legend[i])
            else:
                unresolved.add(i)
        out.append({
            "name": r["name"], "raw_name": r["raw_name"], "variant": r["variant"],
            "found": found,
            "stats": {k: r[k] for k in ("hp", "pp", "hp_regen", "pp_regen", "atk", "def", "agi", "lck", "turns")},
            "elemental_power": {e: r["power"].get(e) for e in ELEM_COLS},
            "elemental_resistance": {e: r["resist"].get(e) for e in ELEM_COLS},
            "abilities": r["abilities"],
            "drops": {"exp": r["exp"], "coins": r["coins"], "items": r["items"]},
        })
    return out, unresolved


def enrich(normalized):
    """Single-source merge: add id / game / flags / sources. (pick()-merge would
    go here when a 2nd aligned source is added.)"""
    monsters = []
    seen = {}
    for n in normalized:
        base = slug(n["name"])
        mid = base if n["variant"] is None else f"{base}-{n['variant']}"
        if mid in seen:
            seen[mid] += 1
            mid = f"{mid}-dup{seen[mid]}"
        else:
            seen[mid] = 1
        is_djinn = "djinni" in n["name"].lower()
        name_l = n["name"].lower()
        # exact match, or "Boss Name (form)" multi-form variants (e.g. "Flame Dragon (Big)")
        is_boss = name_l in BOSS_NAMES or any(name_l.startswith(b + " (") for b in BOSS_NAMES)
        monsters.append({
            "id": mid, "name": n["name"], "game": "gs2", "variant": n["variant"],
            "is_boss": is_boss, "boss_id": None,
            "is_djinn_enemy": is_djinn, "djinn_id": None,
            "found": n["found"], "stats": n["stats"],
            "elemental_power": n["elemental_power"],
            "elemental_resistance": n["elemental_resistance"],
            "abilities": n["abilities"], "drops": n["drops"],
            "sources": ["torrentlord"],
        })
    return monsters


def main():
    lines = SRC.read_text(encoding="utf-8", errors="replace").splitlines()
    legend = parse_legend(lines)
    records = parse_enemies(lines)
    normalized, unresolved = normalize(records, legend)

    INTER.parent.mkdir(parents=True, exist_ok=True)
    INTER.write_text(json.dumps(normalized, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    monsters = enrich(normalized)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(monsters, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    n_missing_hp = sum(m["stats"]["hp"] is None for m in monsters)
    n_no_loc = sum(not m["found"] for m in monsters)
    print(f"legend places         : {len(legend)}")
    print(f"wrote {OUT.relative_to(ROOT)} : {len(monsters)} monsters")
    print(f"  intermediate         : {INTER.relative_to(ROOT)}")
    print(f"  bosses (flagged)     : {sum(m['is_boss'] for m in monsters)}")
    print(f"  djinn enemies        : {sum(m['is_djinn_enemy'] for m in monsters)}")
    print(f"  id collisions (-dup) : {sum(v > 1 for v in seen_counts(monsters))}")
    print(f"  missing HP           : {n_missing_hp}")
    print(f"  no location resolved : {n_no_loc}")
    if unresolved:
        print(f"  WARNING unresolved location idx: {sorted(unresolved)}")


def seen_counts(monsters):
    c = {}
    for m in monsters:
        base = re.sub(r"-dup\d+$", "", m["id"])
        c[base] = c.get(base, 0) + 1
    return c.values()


if __name__ == "__main__":
    main()
