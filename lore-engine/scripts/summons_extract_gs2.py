"""Extract GS2 summons into data/gs2/summons.json.

Deterministic parser (no LLM/API), mirroring scripts/monsters_extract_gs2.py.

Primary source: `Summons FAQ by cooldude345`, which carries two clean tables that
must be merged by summon name:
  - Section VII "Summons Stats" (sourced from Terence Fergusson's Battle
    Mechanics): per summon -> damage element, Base damage, HP% modifier, range,
    special effect.
  - Section V "Summons": per summon -> djinn requirement. Standard summons need
    N djinn of one element (djinn_required + raises_power). The 13 multi-element
    "combo" summons (from tablets) need a cross-element recipe (djinn_recipe) and
    list a Found-At location.

This matches the ER sketch's gs2 increment: base 16 summons keep a simple
`djinn_required`; combo summons (Zagan/Charon/Iris/...) get `djinn_recipe`
[{element,count}] + `acquisition`.

Element mapping: E=earth, W=water, F=fire, A(ir)=wind; in recipes Venus=earth,
Mercury=water, Mars=fire, Jupiter=wind.

Deferred: `acquisition.location` clean name (cooldude gives prose Found-At; note
cooldude calls Valukar "Bullrog"); dbfire is an optional 2nd source for tablets.

Rerunnable: parses raw text only; no stats embedded.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "raw" / "gs2" / "In-Depth Guides" / "Summons FAQ by cooldude345.md"
OUT = ROOT / "data" / "gs2" / "summons.json"

ELM_CODE = {"E": "earth", "W": "water", "F": "fire", "A": "wind"}
DJINN_ELM = {"Venus": "earth", "Mercury": "water", "Mars": "fire", "Jupiter": "wind"}


def slug(s):
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", s.lower())).strip("-")


def section(lines, start_sub, end_sub):
    # The guide has two tables of contents; only the *real* section headers are
    # immediately followed by an "====" underline (TOC entries are not).
    def header(sub):
        # startswith (not `in`) so "V.)" doesn't match "IV.)"; the "====" underline
        # rules out the table-of-contents copies.
        return next(i for i, l in enumerate(lines)
                    if l.strip().startswith(sub) and i + 1 < len(lines)
                    and lines[i + 1].strip() and set(lines[i + 1].strip()) == {"="})
    start = header(start_sub)
    end = header(end_sub)
    return lines[start:end]


def parse_range(tok):
    if "A" in tok:
        return "all"
    m = re.search(r"\d", tok)
    return int(m.group()) if m else None


def parse_stats(lines):
    """Section VII -> {name: {element, damage_power, damage_hp_mod, range, effect}}."""
    out = {}
    for raw in lines:
        s = raw.strip()
        if not s or s.startswith(("EARTH", "WATER", "FIRE", "WIND", "Elm", "=", "*")):
            continue
        if s.startswith("<"):           # <Missile> is Daedalus' sub-attack, not a summon
            continue
        t = s.split()
        if len(t) < 5 or t[1] not in ELM_CODE:
            continue
        name, elm = t[0], ELM_CODE[t[1]]
        # find the range token (the |||| / ==== bar) -> stats are between elm and it
        ri = next((i for i, x in enumerate(t) if set(x) <= set("|=A0123456789") and ("|" in x or "=" in x)), None)
        if ri is None:
            continue
        mid = t[2:ri]                   # Base, HP% (Coatlicue: 'c', '60', '---')
        curative = mid and mid[0] == "c"
        nums = [x for x in mid if re.fullmatch(r"-?\d+", x)]
        out[name] = {
            "element": elm,
            "damage_power": None if curative else (int(nums[0]) if nums else None),
            "damage_hp_mod": None if curative else (round(int(nums[1]) / 100, 2) if len(nums) > 1 else None),
            "range": parse_range(t[ri]),
            "effect": " ".join(t[ri + 1:]).strip() or None,
        }
    return out


def parse_reqs(lines):
    """Section V -> {name: {djinn_required|djinn_recipe, raises_power, found_at}}."""
    out = {}
    in_multi = False
    cur = None
    last_word = None                    # most recent lone-word line (a summon name)
    for raw in lines:
        s = raw.strip()
        if not s:
            continue
        if s == "Multi-Elemental":      # the section header, not the word in the intro prose
            in_multi = True
            continue
        if not in_multi:
            m = re.match(r"^(\w+)\s+(\d+)\s+(Venus|Mars|Mercury|Jupiter)$", s)
            if m:
                cur = m.group(1)
                out[cur] = {"djinn_required": int(m.group(2)), "djinn_recipe": None,
                            "raises_power": None, "found_at": None}
                continue
            rm = re.match(r"Raises Elemental Power By:\s*(\d+)", s)
            if rm and cur:
                out[cur]["raises_power"] = int(rm.group(1))
        else:
            # The name sits alone between two "####" fences; track the last lone word
            # ("Djinn Used:" / "Found At:" etc. are never lone words, so they're safe).
            if re.fullmatch(r"[A-Z][a-z]+", s):
                last_word = s
                continue
            dm = re.match(r"Djinn Used:\s*(.+)", s)
            if dm and last_word:
                cur = last_word
                pairs = re.findall(r"(\d+)\s+(Venus|Mars|Mercury|Jupiter)", dm.group(1))
                out[cur] = {"djinn_required": None, "raises_power": None, "found_at": None,
                            "djinn_recipe": [{"element": DJINN_ELM[e], "count": int(n)} for n, e in pairs]}
                continue
            fm = re.match(r"Found At:\s*(.+)", s)
            if fm and cur:
                out[cur]["found_at"] = fm.group(1).strip()
    return out


def main():
    lines = SRC.read_text(encoding="utf-8", errors="replace").splitlines()
    stats = parse_stats(section(lines, "VII.)", "VIII.)"))
    reqs = parse_reqs(section(lines, "V.)", "VI.)"))

    summons = []
    for name, st in stats.items():
        r = reqs.get(name, {})
        is_combo = bool(r.get("djinn_recipe"))
        acquisition = {"location": None, "found_at": r["found_at"], "source": "cooldude345"} \
            if r.get("found_at") else None
        summons.append({
            "id": slug(name), "name": name, "element": st["element"], "game": "gs2",
            "is_combo": is_combo,
            "djinn_required": r.get("djinn_required"),
            "djinn_recipe": r.get("djinn_recipe") if is_combo else None,
            "raises_power": r.get("raises_power"),
            "damage_power": st["damage_power"], "damage_hp_mod": st["damage_hp_mod"],
            "range": st["range"], "effect": st["effect"],
            "acquisition": acquisition,
            "sources": ["cooldude345"],
        })

    summons.sort(key=lambda d: (d["is_combo"], d["element"], d["damage_power"] or 0))
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(summons, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    ids = [d["id"] for d in summons]
    dupes = sorted({x for x in ids if ids.count(x) > 1})
    nostat = [d["name"] for d in summons if d["damage_power"] is None and not d["is_combo"]]
    print(f"wrote {OUT.relative_to(ROOT)} : {len(summons)} summons")
    print(f"  standard / combo     : {sum(not d['is_combo'] for d in summons)} / {sum(d['is_combo'] for d in summons)}")
    print(f"  combo with recipe    : {sum(bool(d['djinn_recipe']) for d in summons)}")
    print(f"  combo with found_at  : {sum(bool(d['acquisition']) for d in summons)}")
    print(f"  id collisions        : {dupes if dupes else 'none'}")
    print(f"  reqs not matched     : {[n for n in reqs if n not in stats] or 'none'}")


if __name__ == "__main__":
    main()
