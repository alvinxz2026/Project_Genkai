"""Extract the authoritative GS2 (Lost Age) class roster into data/gs2/classes.json.

Deterministic parser (no LLM/API). **Layer 1 — the Terence spine.**

Source `terence` (Battle Mechanics) section "== CLASS BONUSES AND REQS ==" holds
the game-accurate class tables: each class row is

    Name [(qual)]   HP% PP% Att% Def% Agi% Lck%      Eth Wtr Fre Wnd

i.e. 6 stat-multiplier columns then 4 element-LEVEL requirement columns (order
**Eth Wtr Fre Wnd** = earth/water/fire/wind; `-` = not applicable). Rows are
grouped into alignment tables (Basic / Lost Age New / Water-/Wind-/Earth-/Fire-
aligned / Earth-Fire / Water-Wind / Item-required), and within a table `-----`
rules separate tier chains (Squire->Knight->...->Slayer is one chain).

GS2's class system is Element-Levels + Dominance (base Element Level 5 in the
primary element, +1 per equipped Djinni), NOT GS1's raw djinn-count table — so
this `element_requirements` block is element LEVELS, not djinn counts. The
relative per-djinn-count matcher table (terence "Prm Aff Wek Neu") is the GS2
analog of GS1's build_terence_class_reqs and is a **deferred** later layer.

Same-name classes are disambiguated by Terence's qualifier letters, appended as
an id **suffix** (suffix not prefix so they never collide with the leading-element
compound base names, e.g. "Water Seer"->water-seer vs "Seer (W)"->seer-water):
  (E)=Earth (W)=Water (F)=Fire (A)=Wind  -> -earth/-water/-fire/-wind (swordsman-earth)
  (D)=Medium-upgrade-only               -> -medium (conjurer-medium)
  (I)=Item-class-only                   -> -item   (dark-mage-item)

Deferred to later layers (left null/[] here):
  - available_to[]  — which characters reach the class (ultimalink per-character
    chains + Dominance rules).  - psynergy[] — learnset (ultimalink).
  - djinn_requirements / acr — the relative-count matcher (terence 2nd table) +
    aku-chi ratings.

Rerunnable: parses raw text only.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "raw" / "gs2" / "In-Depth Guides" / "Battle Mechanics by Terence.md"
OUT = ROOT / "data" / "gs2" / "classes.json"

ELEM_ORDER = ["earth", "water", "fire", "wind"]  # table column order: Eth Wtr Fre Wnd
STAT_KEYS = ["hp", "pp", "atk", "def", "agi", "lck"]
# All qualifiers become an id suffix (see module docstring).
QUAL_SUFFIX = {"E": "earth", "W": "water", "F": "fire", "A": "wind",
               "D": "medium", "I": "item"}

GROUPS = {
    "BASIC ELEMENT CLASSES": "basic",
    "LOST AGE NEW CLASSES": "lost-age-new",
    "WATER ALIGNED CLASSES": "water-aligned",
    "WIND ALIGNED CLASSES": "wind-aligned",
    "EARTH ALIGNED CLASSES": "earth-aligned",
    "FIRE ALIGNED CLASSES": "fire-aligned",
    "EARTH/FIRE ALIGNED CLASSES": "earth-fire-aligned",
    "WATER/WIND ALIGNED CLASSES": "water-wind-aligned",
    "ITEM REQUIRED CLASSES": "item-required",
}

PCT = re.compile(r"^\d+%$")
ELEM_TOK = re.compile(r"^(?:\d+|-)$")
QUAL = re.compile(r"\(([EWFADI])\)$")


def slug(s):
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", s.lower())).strip("-")


def make_id(name, qual):
    base = slug(name)
    if qual in QUAL_SUFFIX:
        return f"{base}-{QUAL_SUFFIX[qual]}"
    return base


def section_lines(text):
    lines = text.splitlines()
    start = next(i for i, l in enumerate(lines) if "BASIC ELEMENT CLASSES" in l)
    end = next(i for i, l in enumerate(lines[start:], start) if "Now for Dominance" in l)
    return lines[start:end]


def parse_row(line):
    """A data row -> dict, or None if not a class row."""
    toks = line.split()
    pct_idx = next((i for i, t in enumerate(toks) if PCT.match(t)), None)
    if pct_idx is None or pct_idx == 0:
        return None
    stats = toks[pct_idx:pct_idx + 6]
    elems = toks[pct_idx + 6:pct_idx + 10]
    if len(stats) != 6 or not all(PCT.match(s) for s in stats):
        return None
    if len(elems) != 4 or not all(ELEM_TOK.match(e) for e in elems):
        return None
    name_part = " ".join(toks[:pct_idx]).strip()
    m = QUAL.search(name_part)
    qual = m.group(1) if m else None
    name = QUAL.sub("", name_part).strip() if m else name_part
    return {
        "id": make_id(name, qual),
        "name": name,
        "qualified_name": name_part if qual else None,
        "qualifier": qual,
        "stat_multiplier": {k: int(s.rstrip("%")) for k, s in zip(STAT_KEYS, stats)},
        "element_requirements": {ELEM_ORDER[i]: (None if e == "-" else int(e))
                                 for i, e in enumerate(elems)},
    }


def parse(text):
    rows = []
    group = None
    line_root = None  # id of current tier-chain root (reset on '----' rule)
    for raw in section_lines(text):
        s = raw.strip()
        if not s:
            continue
        core = s.strip("= ").strip()    # "== EARTH/FIRE ALIGNED CLASSES ==" -> core
        if core in GROUPS:
            group = GROUPS[core]
            line_root = None
            continue
        if set(s) <= set("="):          # group fence
            continue
        if set(s) <= set("-"):          # tier-chain separator within a group
            line_root = None
            continue
        row = parse_row(s)
        if row is None:
            continue                    # header row ("HP PP Att..."), prose, etc.
        if line_root is None:
            line_root = row["id"]       # first row of the sub-block is the chain root
        row["dominance_group"] = group
        row["class_line"] = line_root
        rows.append(row)
    return rows


def to_entry(r):
    """Shape the final classes.json record (deferred fields null/[])."""
    return {
        "id": r["id"],
        "name": r["name"],
        "qualified_name": r["qualified_name"],
        "game": "gs2",
        "class_line": r["class_line"],
        "dominance_group": r["dominance_group"],
        "stat_multiplier": r["stat_multiplier"],
        "element_requirements": r["element_requirements"],
        "available_to": [],     # deferred: ultimalink per-character chains
        "psynergy": [],         # deferred: ultimalink learnsets
        "sources": ["terence"],
    }


def main():
    text = SRC.read_text(encoding="utf-8", errors="replace")
    rows = parse(text)

    ids = [r["id"] for r in rows]
    dupes = {i for i in ids if ids.count(i) > 1}
    assert not dupes, f"duplicate ids: {sorted(dupes)}"
    for r in rows:
        assert r["class_line"], f"no class_line: {r['id']}"
        assert all(0 <= v <= 999 for v in r["stat_multiplier"].values()), r

    out = [to_entry(r) for r in rows]
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(f"wrote {len(out)} classes -> {OUT.relative_to(ROOT)}")
    from collections import Counter
    for g, n in Counter(r["dominance_group"] for r in rows).items():
        print(f"  {g:20} {n}")
    print(f"  distinct class_lines: {len(set(r['class_line'] for r in rows))}")


if __name__ == "__main__":
    main()
