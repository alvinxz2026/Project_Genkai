"""Backfill classes.available_to[].acr from aku-chi's Class Setup Guide (Layer 4).

ACR = "Aku chi's Combat efficiency Rank (out of ten)" — a per-(character, class)
combat rating. The guide gives it in two kinds of fixed-width tables that share
one row shape:

    <Character> - <Class> (<djinn config>)  HP%  PP%  Att% Def% Agi% Lck%  ACR
    e.g.  Isaac - Master    (4 fire, 5 wind)   200% 160% 170% 140% 190%  80%  10

  (a) the seven full-party SETUP tables (#1..#7, ranked by setup ACR), and
  (b) the LINK BATTLE STRATEGY per-class tables (Warrior/Intermediary/Spell).

The same (character, class) appears across multiple setups with DIFFERENT ACRs
because ACR depends on the djinn configuration. The schema field is a single
value, so (user decision) we record the MAX ACR seen for that (character, class)
plus `acr_config` = the djinn config string that achieved it.

Config strings may use per-section footnotes (`*`, `**`, ...), e.g.
    Isaac - Necromage (3 fire, *)   ...
    *  - 3 wind, 3 water, Tomegathericon
We resolve those within each `==SECTION==` so `acr_config` is self-contained.

Matching (mirrors classes_telago_reqs_gs2.py): class name -> candidate classes,
filtered to those listing the character in available_to. If >1 remains (class
names are not unique — split by element path), disambiguate by the config's
element set vs the class's non-null element_requirements keys. Only the matching
available_to[] entry (character == row char) gets acr/acr_config.

aku-chi rates only top-tier builds, so most of the 110 classes keep acr=null —
that is expected, not a gap.

Idempotent: clears every acr/acr_config first. Run anytime (independent of
links_normalize). Usage: python scripts/classes_acr_gs2.py
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "gs2"
SRC = ROOT / "raw" / "gs2" / "In-Depth Guides" / "Class Setup Guide by aku_chi.md"

ELEMS = ("earth", "fire", "wind", "water")
# aku-chi misspells Piers as "Peirs"; normalize to roster name.
CHAR_FIX = {"peirs": "Piers"}

# <Char> -|– <Class> (<config>)  six "NN%"  then ACR (int or x.y)
ROW = re.compile(
    r"^([A-Za-z]+)\s*[-–]\s*([A-Za-z][A-Za-z ]*?)\s+\(([^)]*)\)\s+"
    r"((?:\d+%\s+){6})(\d+(?:\.\d+)?)\s*$"
)
FOOT = re.compile(r"^(\*+)\s*[-–]\s*(.+)$")
SECTION = re.compile(r"^==.*==")


def norm(s):
    return re.sub(r"[^a-z0-9]", "", s.lower())


def canon_char(name):
    return CHAR_FIX.get(name.lower(), name.capitalize())


def resolve_config(config, footnotes):
    """Expand footnote refs (`*`, `**`) inside a config string using the
    current section's footnote map; return the self-contained config text."""
    out = []
    for tok in (t.strip() for t in config.split(",")):
        m = re.fullmatch(r"\*+", tok)
        if m and m.group(0) in footnotes:
            out.append(footnotes[m.group(0)])
        elif tok:
            out.append(tok)
    return ", ".join(out)


def config_elems(config):
    return {e for e in ELEMS if re.search(rf"\b{e}\b", config.lower())}


def parse_acr_rows():
    """Return [{char, cls, config, acr}] for every ACR table row in the guide.

    Footnote definitions (`*  - 3 earth, ...`) appear AFTER the rows that cite
    them within a section, so we buffer each `==SECTION==` block and resolve its
    rows against the section's footnotes once the block is complete."""
    rows = []
    raw_rows, footnotes = [], {}

    def flush():
        for char, cls, config, acr in raw_rows:
            rows.append({"char": char, "cls": cls,
                         "config": resolve_config(config, footnotes), "acr": acr})

    for raw in SRC.read_text(encoding="utf-8").splitlines():
        line = raw.rstrip()
        if SECTION.match(line):
            flush()
            raw_rows, footnotes = [], {}
            continue
        fm = FOOT.match(line)
        if fm:
            footnotes[fm.group(1)] = fm.group(2).strip()
            continue
        m = ROW.match(line)
        if m:
            raw_rows.append((canon_char(m.group(1)), m.group(2).strip(),
                             m.group(3).strip(), float(m.group(5))))
    flush()
    return rows


def main():
    classes = json.loads((DATA / "classes.json").read_text(encoding="utf-8"))
    by_name = {}
    for c in classes:
        by_name.setdefault(norm(c["name"]), []).append(c)

    # idempotency: clear all acr / acr_config
    for c in classes:
        for a in c["available_to"]:
            a["acr"] = None
            a.pop("acr_config", None)

    rows = parse_acr_rows()

    # collapse to best (max) ACR per (char, class-name)
    best = {}  # (char, norm cls) -> (acr, config)
    for r in rows:
        key = (r["char"], norm(r["cls"]))
        if key not in best or r["acr"] > best[key][0]:
            best[key] = (r["acr"], r["config"])

    filled, unmatched, ambiguous = 0, [], []
    for (char, ncls), (acr, config) in best.items():
        cands = [c for c in by_name.get(ncls, [])
                 if any(a["character"] == char for a in c["available_to"])]
        if not cands:
            unmatched.append((char, ncls)); continue
        if len(cands) == 1:
            cls = cands[0]
        else:
            sig = config_elems(config)
            exact = [c for c in cands
                     if {k for k, v in c["element_requirements"].items() if v} == sig]
            if len(exact) != 1:
                ambiguous.append((char, ncls, sig, [c["id"] for c in cands])); continue
            cls = exact[0]
        for a in cls["available_to"]:
            if a["character"] == char:
                a["acr"] = acr
                a["acr_config"] = config
                filled += 1

    (DATA / "classes.json").write_text(
        json.dumps(classes, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    total_at = sum(len(c["available_to"]) for c in classes)
    print(f"classes_acr_gs2 — parsed {len(rows)} ACR rows -> {len(best)} distinct "
          f"(char,class); filled {filled} available_to[].acr (of {total_at}; rest "
          f"expected null = not top-tier-rated)")
    if unmatched:
        print(f"  UNMATCHED ({len(unmatched)}): {unmatched}")
    if ambiguous:
        print(f"  AMBIGUOUS ({len(ambiguous)}):")
        for char, ncls, sig, ids in ambiguous:
            print(f"    {char} {ncls} cfg-elems={sig} -> {ids}")
    return 1 if (unmatched or ambiguous) else 0


if __name__ == "__main__":
    sys.exit(main())
