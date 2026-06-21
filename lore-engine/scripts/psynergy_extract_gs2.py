"""Extract the GS2 (Lost Age) psynergy master list into data/gs2/psynergy.json.

Deterministic parser (no LLM/API). Primary source `yoyoyoshi` (Psynergy FAQ),
section "11 > ALL PSYNERGIES" — a clean fixed-width alphabetical table:

    Name            PP  <I-bar>  Short description.            Type

  * Name  : display name (single-spaced words)
  * PP    : pp cost
  * I-bar : targeting range as a run of "I"s -> 1/3/5/7 targets, or 8 = "all"
  * desc  : in-game short description
  * Type  : element (Venus=earth, Mars=fire, Mercury=water, Jupiter=wind, Neutral)

`mr-unorigino-psy` is a secondary completeness cross-check only: its kana columns
are mojibake (encoding loss) but its 4th "/"-field is the clean US-English name.
We diff its names against yoyoyoshi's set and corroborate `sources` on matches;
its "None Yet" rows are dummied/untranslated puzzle psynergy with no US name.

Deferred (null/[]; not cleanly/deterministically in this source):
  - series / tier — yoyoyoshi's element sections group psynergy inconsistently
    (true progressions mixed with thematic clusters), so series is left for a
    curated/links pass.
  - level_learned / available_to — these are *derivable from classes.json*
    (classes[].psynergy[] carries name+level per class) and belong to the gs2
    links_normalize reverse-index step, not this extractor.
  - category / target / battle_usable / acquired_via_item / effect_notes — later.

Rerunnable: parses raw text only.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
YOYO = ROOT / "raw" / "gs2" / "In-Depth Guides" / "Psynergy FAQ by YoyoYoshi.md"
UNOR = ROOT / "raw" / "gs2" / "In-Depth Guides" / "Psynergy List by Mr_UnOrigino.md"
OUT = ROOT / "data" / "gs2" / "psynergy.json"

ELEM = {"Venus": "earth", "Mars": "fire", "Mercury": "water", "Jupiter": "wind",
        "Neutral": "neutral"}
ROW = re.compile(
    r"^(?P<name>\S(?:.*\S)?)\s{2,}(?P<pp>\d+)\s+(?P<range>I+)\s+"
    r"(?P<desc>.+?)\s+(?P<elem>Venus|Mars|Mercury|Jupiter|Neutral)\s*$")


def slug(s):
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", s.lower())).strip("-")


def section(lines, start_marker, end_marker):
    start = next(i for i, l in enumerate(lines) if start_marker in l)
    end = next(i for i, l in enumerate(lines[start + 1:], start + 1) if end_marker in l)
    return lines[start:end]


def parse_yoyo():
    lines = YOYO.read_text(encoding="utf-8", errors="replace").splitlines()
    rows = []
    for l in section(lines, "11 > ALL PSYNERGIES", "12 > OUT-OF-BATTLE"):
        m = ROW.match(l)
        if not m:
            continue
        rng = len(m.group("range"))
        rows.append({
            "name": m.group("name").strip(),
            "pp_cost": int(m.group("pp")),
            "range": "all" if rng == 8 else rng,
            "description": m.group("desc").strip(),
            "element": ELEM[m.group("elem")],
        })
    return rows


def parse_unorigino_names():
    """US-English names (4th '/'-field), skipping mojibake + 'None Yet'."""
    names = set()
    for l in UNOR.read_text(encoding="utf-8", errors="replace").splitlines():
        if l.count("/") >= 3:
            us = l.split("/")[-1].strip()
            if us and us.lower() not in ("none yet", "none", "n/a"):
                names.add(us.lower())
    return names


def main():
    rows = parse_yoyo()

    # validate range domain
    for r in rows:
        assert r["range"] in (1, 3, 5, 7, "all"), f"bad range for {r['name']}: {r['range']}"

    # assign ids; disambiguate duplicate display names by pp suffix
    name_counts = {}
    for r in rows:
        name_counts[r["name"]] = name_counts.get(r["name"], 0) + 1
    out = []
    for r in rows:
        base = slug(r["name"])
        cid = base if name_counts[r["name"]] == 1 else f"{base}-{r['pp_cost']}pp"
        out.append({
            "id": cid, "name": r["name"], "game": "gs2", "element": r["element"],
            "pp_cost": r["pp_cost"], "range": r["range"], "description": r["description"],
            "series": None, "tier": None,
            "sources": ["yoyoyoshi"],
        })

    ids = [e["id"] for e in out]
    assert len(ids) == len(set(ids)), f"dup ids: {[i for i in ids if ids.count(i) > 1]}"

    # flag entries that share a display name — links_normalize treats them as
    # ambiguous (expected-gap); document this explicitly in the data
    dup_names = {r["name"] for r in out if name_counts.get(r["name"], 0) > 1}
    for e in out:
        if e["name"] in dup_names:
            e["conflicts"] = [{"field": "name", "value": e["name"], "source": "all",
                               "note": "Two distinct psynergy share this display name "
                                       f"(differentiated by id suffix -{e['pp_cost']}pp); "
                                       "class refs by name alone are unresolvable — "
                                       "classified as expected-gap in links_normalize"}]

    # completeness cross-check vs mr-unorigino (corroborate sources on name match)
    unor = parse_unorigino_names()
    yoyo_names = {e["name"].lower() for e in out}
    for e in out:
        if e["name"].lower() in unor:
            e["sources"].append("mr-unorigino-psy")
    only_unor = sorted(unor - yoyo_names)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    from collections import Counter
    print(f"wrote {len(out)} psynergy -> {OUT.relative_to(ROOT)}")
    print("  by element:", dict(Counter(e["element"] for e in out)))
    print(f"  corroborated by mr-unorigino: {sum('mr-unorigino-psy' in e['sources'] for e in out)}")
    print(f"  in mr-unorigino but not yoyoyoshi ({len(only_unor)}): {only_unor}")


if __name__ == "__main__":
    main()
