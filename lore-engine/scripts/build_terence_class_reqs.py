"""Extract the authoritative full 4-element class requirement table from
`raw/gs1/Djinn Class Mechanics FAQ - Terence.txt` and merge it into
`data/gs1/classes.json` as a new `terence` requirement source.

Why: the other sources (plz2bstfu-class / strawhat / aku-chi) record each class
as a *single* off-element range and implicitly force the other off-elements to 0,
so the planner can't resolve any Djinn mix that touches a second off-element.
Terence's table gives every class's range on ALL FOUR elements at once (with
alternative OR-rows), which is what the game actually uses.

Each Terence OR-row becomes one `djinn_requirements` entry with source "terence"
whose `parsed` lists all four elements ({element,min,max}); the matcher
OR-combines all terence rows for a (class, character). Token semantics:
  "0-2" -> min0 max2 | "3" -> 3..3 | "---" -> 0..0 | "5,7" -> disjoint -> 2 rows.

Idempotent: drops any pre-existing source=="terence" rows before re-adding.
Run after editing the raw table; then re-run links_normalize.py + links_audit.py.

    python scripts/build_terence_class_reqs.py
"""
import json
import re
from itertools import product
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "raw" / "gs1" / "Djinn Class Mechanics FAQ - Terence.txt"
CLASSES = ROOT / "data" / "gs1" / "classes.json"

# Terence's table columns are: Eth Fre Wnd Wtr
ELEM_ORDER = ["earth", "fire", "wind", "water"]
ELEM_LABEL = {"earth": "Earth", "fire": "Fire", "wind": "Wind", "water": "Water"}
CHARS = ["ISAAC", "GARET", "IVAN", "MIA"]

# (character, name-as-printed-in-table) -> classes.json id.
# Qualifier letters in the table: A=Air/Wind, W=Water, F=Fire, E=Earth.
NAME2ID = {
    "ISAAC": {
        "Squire": "squire", "Knight": "knight", "Gallant": "gallant", "Lord": "lord",
        "Brute": "brute", "Ruffian": "ruffian", "Savage": "savage",
        "Barbarian": "barbarian", "Berserker": "berserker",
        "Apprentice": "apprentice", "Illusionist": "illusionist-isaac",
        "Enchanter": "enchanter-isaac", "Conjurer": "conjurer-isaac",
        "Shaman(A)": "wind-shaman", "Shaman(W)": "water-shaman",
        "Swordsman": "swordsman-isaac", "Defender": "defender-isaac",
        "Cavalier": "cavalier-isaac", "Guardian": "guardian",
        "Dragoon": "dragoon", "Ninja": "ninja", "Samurai": "samurai",
    },
    "GARET": {
        "Guard": "guard", "Soldier": "soldier", "Warrior": "warrior", "Champion": "champion",
        "Brute": "brute", "Ruffian": "ruffian", "Savage": "savage",
        "Barbarian": "barbarian", "Berserker": "berserker",
        "Swordsman": "swordsman-garet", "Defender": "defender-garet",
        "Cavalier": "cavalier-garet", "Luminier": "luminier", "Ascetic(W)": "water-ascetic",
        "Page": "page", "Illusionist": "illusionist-garet", "Enchanter": "enchanter-garet",
        "Conjurer": "conjurer-garet", "Ascetic(A)": "wind-ascetic",
        "Dragoon": "dragoon", "Ninja": "ninja", "Samurai": "samurai",
    },
    "IVAN": {
        "Wind Seer": "wind-seer", "Magician": "magician", "Mage": "mage", "Magister": "magister",
        "Hermit": "hermit", "Elder": "elder", "Scholar": "scholar", "Savant": "savant", "Sage": "sage",
        "Seer": "seer-ivan", "Diviner": "diviner-ivan", "Shaman": "shaman-ivan", "Druid": "druid-ivan",
        "Enchanter(E)": "earth-enchanter", "Enchanter(F)": "fire-enchanter",
        "Pilgrim": "pilgrim-ivan", "Wanderer": "wanderer-ivan", "Ascetic": "ascetic-ivan",
        "Fire Monk": "fire-monk", "Ranger": "ranger", "Medium": "medium", "White Mage": "white-mage",
    },
    "MIA": {
        "Water Seer": "water-seer", "Scribe": "scribe", "Cleric": "cleric", "Paragon": "paragon",
        "Hermit": "hermit", "Elder": "elder", "Scholar": "scholar", "Savant": "savant", "Sage": "sage",
        "Pilgrim": "pilgrim-mia", "Wanderer": "wanderer-mia", "Ascetic": "ascetic-mia",
        "Water Monk": "water-monk", "Cavalier(F)": "fire-cavalier",
        "Seer": "seer-mia", "Diviner": "diviner-mia", "Shaman": "shaman-mia", "Druid": "druid-mia",
        "Cavalier(E)": "earth-cavalier", "Ranger": "ranger", "Medium": "medium", "White Mage": "white-mage",
    },
}
CHAR_NAME = {"ISAAC": "Isaac", "GARET": "Garet", "IVAN": "Ivan", "MIA": "Mia"}

TOK = re.compile(r"^(---|\d+|\d+-\d+|\d+(?:,\d+)+)$")


def parse_token(t):
    """Return list of (min,max) alternatives for one djinn-column token."""
    if t == "---":
        return [(0, 0)]
    if "," in t:                      # disjoint set, e.g. "5,7"
        return [(int(x), int(x)) for x in t.split(",")]
    if "-" in t:
        a, b = t.split("-")
        return [(int(a), int(b))]
    n = int(t)
    return [(n, n)]


def parse_table(text):
    """-> { (CHAR, terence_name): [ row, ... ] } where row = [(min,max)]*4."""
    out = {}
    cur_char = None
    cur_key = None
    for raw in text.splitlines():
        line = raw.rstrip()
        s = line.strip()
        if not s:
            continue
        head = s.split()[0]
        if head in CHARS and "HP" in s:          # character section header
            cur_char = head
            cur_key = None
            continue
        if cur_char is None:
            continue
        if s.startswith("==") or "CLASS ABILITIES" in s:
            break
        if set(s) <= set("-"):                    # separator rule
            continue
        toks = s.split()
        if len(toks) < 4:
            continue
        djinn = toks[-4:]
        if not all(TOK.match(t) for t in djinn):  # not a data row
            continue
        is_cont = len(toks) == 4 and TOK.match(toks[0])
        if is_cont:
            if cur_key is None:
                continue
        else:
            name = " ".join(toks[:-10]).strip()    # 6 stat cols + 4 djinn = 10 trailing
            cid = NAME2ID.get(cur_char, {}).get(name)
            if cid is None:
                raise SystemExit(f"Unmapped Terence class: {cur_char} {name!r} | {line!r}")
            cur_key = (cur_char, name, cid)
            out.setdefault(cur_key, [])
        # expand disjoint tokens into concrete OR-rows
        alts = [parse_token(t) for t in djinn]
        for combo in product(*alts):
            out[cur_key].append(list(combo))
    return out


def req_prose(row):
    return ", ".join(
        f"{ELEM_LABEL[ELEM_ORDER[i]]} {lo}" if lo == hi else f"{ELEM_LABEL[ELEM_ORDER[i]]} {lo}-{hi}"
        for i, (lo, hi) in enumerate(row)
    )


def to_entry(row):
    return {
        "requirement": req_prose(row),
        "parsed": [{"element": ELEM_ORDER[i], "min": lo, "max": hi}
                   for i, (lo, hi) in enumerate(row)],
        "source": "terence",
    }


def main():
    table = parse_table(RAW.read_text(encoding="utf-8"))
    classes = json.loads(CLASSES.read_text(encoding="utf-8"))
    by_id = {c["id"]: c for c in classes}

    n_rows = 0
    n_av = 0
    for (char_up, name, cid), rows in table.items():
        cls = by_id.get(cid)
        if cls is None:
            raise SystemExit(f"id not in classes.json: {cid}")
        char = CHAR_NAME[char_up]
        av = next((a for a in cls.get("available_to", []) if a["character"] == char), None)
        if av is None:
            raise SystemExit(f"{cid} has no available_to for {char}")
        reqs = av.get("djinn_requirements", [])
        reqs = [r for r in reqs if r.get("source") != "terence"]   # idempotent
        reqs.extend(to_entry(r) for r in rows)
        av["djinn_requirements"] = reqs
        n_av += 1
        n_rows += len(rows)

    CLASSES.write_text(json.dumps(classes, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"merged terence reqs: {n_av} (class,character) entries, {n_rows} OR-rows")
    print(f"wrote {CLASSES.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
