"""Extract all 72 GS2-available Djinn into data/gs2/djinn.json.

Deterministic parser (no LLM/API), mirroring scripts/monsters_extract_gs2.py.

Primary source: `Djinni Stat Boosts Guide by Demooni` — a single clean source
that covers, for every Djinni: element, stat boosts, acquisition (TLA djinn),
and the *FIGHT* flag. Section 2 ("The Boosts") lists stat boosts per element in
two `---`-separated groups; the **`---` split is exactly TLA-native vs GS1**:
each element has 11 TLA djinn (game "gs2") then 7 GS1 djinn (game "gs1"),
11+7 = 18 per element, x4 = 72 total (per the ER sketch's transfer convention:
GS1 djinn keep game "gs1"). Section 3 ("The Locations") gives acquisition prose
for the 44 TLA djinn only; the 28 GS1 djinn have no TLA location here.

Boost columns are fixed "HP PP STR DEF AGL LCK" (STR -> atk); "---" means no
boost (0, since the table is exhaustive per djinn).

Element mapping (same as the other gs2 parsers): Venus=earth, Mercury=water,
Mars=fire, Jupiter=wind.

Deferred (not in this source; left null for a 2nd source / links_normalize):
  - battle_effect (damage/range/special) — from aspartate/cooldude/terence later.
  - location.area — demooni gives prose only; the clean area name (for the
    locations FK) is deferred. The prose is kept in location.description.
  - monsters.djinn_id back-fill stays the future gs2 links_normalize's job.

Rerunnable: parses raw text only; no boost/location data embedded.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "raw" / "gs2" / "In-Depth Guides" / "Djinni Stat Boosts Guide by Demooni.md"
OUT = ROOT / "data" / "gs2" / "djinn.json"

ELEMENTS = {"Venus": "earth", "Mercury": "water", "Mars": "fire", "Jupiter": "wind"}
# Fixed boost column order in section 2.
STAT_KEYS = ["hp", "pp", "atk", "def", "agi", "lck"]


def slug(s):
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", s.lower())).strip("-")


def section_bounds(lines, start_marker, end_marker):
    start = next(i for i, l in enumerate(lines) if start_marker in l)
    end = next(i for i, l in enumerate(lines[start + 1:], start + 1) if end_marker in l)
    return start, end


def parse_boosts(lines):
    """Section 2 -> {name: {element, game, stat_bonus}}. `---` flips game gs2->gs1."""
    start, end = section_bounds(lines, "2. THE BOOSTS", "3. THE LOCATIONS")
    out = {}
    element = None
    game = "gs2"
    last = None
    for raw in lines[start:end]:
        s = raw.strip()
        if s in ELEMENTS:
            element = ELEMENTS[s]
            game = "gs2"                 # each element starts with the TLA group
            last = None
            continue
        if s == "---":                   # TLA -> GS1 split (exactly 3 dashes)
            game = "gs1"
            last = None
            continue
        if s.startswith("+") and last and element:
            vals = s[1:].split()         # 6 positional values, "---" -> 0
            if len(vals) >= 6:
                name = last.split()[0]
                bonus = {k: (0 if v == "---" else int(v)) for k, v in zip(STAT_KEYS, vals)}
                out[name] = {"element": element, "game": game, "stat_bonus": bonus}
            last = None
            continue
        if s:
            last = s
    return out


def parse_locations(lines):
    """Section 3 -> {name: {description, must_fight}} for the TLA djinn."""
    start, end = section_bounds(lines, "3. THE LOCATIONS", "4. CREDITS")
    out = {}
    cur = None
    for raw in lines[start:end]:
        s = raw.strip()
        if s in ELEMENTS or not s or set(s) <= {"=", "-"}:
            continue
        m = re.match(r"^([A-Z][a-z]+)\s*-\s+(.*)$", s)
        if m:
            name, desc = m.group(1), m.group(2).strip()
            must_fight = "*FIGHT*" in desc
            desc = desc.replace("*FIGHT*", "").strip()
            cur = {"description": desc, "must_fight": must_fight}
            out[name] = cur
        elif cur is not None:            # continuation line
            cur["description"] = (cur["description"] + " " + s).strip()
    return out


def main():
    lines = SRC.read_text(encoding="utf-8", errors="replace").splitlines()
    boosts = parse_boosts(lines)
    locs = parse_locations(lines)

    djinn = []
    for name, b in boosts.items():
        loc = locs.get(name)
        location = None
        if loc:
            location = {"area": None,           # deferred (prose only); clean name later
                        "description": loc["description"], "source": "demooni"}
        djinn.append({
            "id": slug(name), "name": name, "element": b["element"], "game": b["game"],
            "stat_bonus": b["stat_bonus"],
            "battle_effect": None,              # deferred (not in demooni)
            "location": location,
            "must_fight": loc["must_fight"] if loc else None,
            "sources": ["demooni"],
        })

    djinn.sort(key=lambda d: (d["element"], d["game"], d["name"]))
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(djinn, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    ids = [d["id"] for d in djinn]
    dupes = sorted({x for x in ids if ids.count(x) > 1})
    by_el = {e: sum(d["element"] == e for d in djinn) for e in ("earth", "fire", "wind", "water")}
    print(f"wrote {OUT.relative_to(ROOT)} : {len(djinn)} djinn")
    print(f"  by game (gs2/gs1)    : {sum(d['game']=='gs2' for d in djinn)} / {sum(d['game']=='gs1' for d in djinn)}")
    print(f"  by element           : {by_el}")
    print(f"  with location        : {sum(d['location'] is not None for d in djinn)}")
    print(f"  must_fight (TLA)     : {sum(d['must_fight'] is True for d in djinn)}")
    print(f"  id collisions        : {dupes if dupes else 'none'}")


if __name__ == "__main__":
    main()
