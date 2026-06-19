#!/usr/bin/env python3
"""Canonical region spine + cross-source chapter mapping for gs2 walkthrough.

THE KEYSTONE of the consolidation pipeline (docs/gs2/walkthrough_consolidation_plan.md).

The 10 walkthroughs were each split by their own TOC, so granularity / spelling /
boundaries differ per author. This script reconciles them onto ONE canonical,
ordered progression of in-game regions (the "spine") and maps every prose
chapter onto the node(s) it covers. That mapping is:
  - the work queue for 2a (consolidation): per node, the set of source chapters to merge.
  - the skeleton for locations.json (each node ~ one location record).

Design:
  - SPINE: ordered canonical nodes, hand-authored from cloud-blazer's clean
    area-level chapter order (the structural reference) + GS2 game knowledge.
    Each node: id, name, kind (main|side|postgame|overworld), aliases.
  - cloud-blazer = STRUCTURAL reference (ordering/granularity).
    telago      = CONTENT authority for 2a (most-recommended guide; primary
                  narrative voice, conflict tie-breaker) — but its chapters are
                  coarse quest-arcs, so they map one-to-many via COARSE_MAP.
  - Matching: normalize a chapter's `region` tag (lowercase, drop
    revisit/again/part-N decoration, strip punctuation) -> alias index -> node.
    Multi-area / quest-arc tags resolve via COARSE_MAP or comma/"and" splitting.

  python scripts/region_spine_gs2.py            # build mapping + report
  python scripts/region_spine_gs2.py --unmatched  # just list unmatched chapters

Output: data/gs2/intermediate/region_spine.json
"""
import argparse
import json
import re
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
INDEX = REPO / "data" / "gs2" / "intermediate" / "walkthrough_chapter_index.json"
OUT = REPO / "data" / "gs2" / "intermediate" / "region_spine.json"

# ---------------------------------------------------------------------------
# Canonical spine — ordered. kind: main (storyline path) | side (optional area)
# | postgame (superboss / endgame optional) | overworld (navigation interlude).
# aliases are extra region-tag spellings/variants seen across the 10 sources.
# ---------------------------------------------------------------------------
SPINE = [
    ("venus-lighthouse",       "Venus Lighthouse",        "main",     ["venus lighthouse and suhalla gate", "venus lighthouse and suhulla gate"]),
    ("suhalla-gate",           "Suhalla Gate",            "main",     ["suhulla gate"]),
    ("idejima",                "Idejima",                 "main",     []),
    ("daila",                  "Daila",                   "main",     ["daili", "dalia", "diala", "daila and kandorean temple"]),
    ("kandorean-temple",       "Kandorean Temple",        "main",     ["kanorean temple", "kandorean temple's cave", "to kandorean temple", "the trial temple"]),
    ("shrine-of-the-sea-god",  "Shrine of the Sea God",   "main",     ["shrine of the sea god and dehkan plateau"]),
    ("dehkan-plateau",         "Dehkan Plateau",          "main",     ["dehkan plateu"]),
    ("indra-cavern",           "Indra Cavern",            "main",     ["indra", "east indra shore", "indra cavern, madra, mikasalla, and garoh"]),
    ("madra",                  "Madra",                   "main",     ["back to madra"]),
    ("madra-catacombs",        "Madra Catacombs",         "main",     ["kibombo statue and madra catacombs"]),
    ("madra-drawbridge",       "Madra Drawbridge",        "main",     []),
    ("osenia-cliffs",          "Osenia Cliffs",           "main",     []),
    ("yampi-desert",           "Yampi Desert",            "main",     ["back through yampi desert", "trapping a scorpion in the desert"]),
    ("alhafra",                "Alhafra",                 "main",     ["alhafra and briggs", "the pirates' hideout in alhafra"]),
    ("garoh",                  "Garoh",                   "main",     []),
    ("airs-rock",              "Air's Rock",              "main",     ["air's rock interior", "air's rock exterior", "air's rock (inside)", "air's rock (outside)", "to air's rock"]),
    ("osenia-cavern",          "Osenia Cavern",           "main",     []),
    ("mikasalla",              "Mikasalla",               "main",     []),
    ("gondowan-cliffs",        "Gondowan Cliffs",         "main",     ["to gondowan"]),
    ("naribwe",                "Naribwe",                 "main",     ["naribwe village"]),
    ("kibombo-mountains",      "Kibombo Mountains",       "main",     ["kibombo mountain"]),
    ("kibombo",                "Kibombo",                 "main",     ["kibombo and gabomba statue"]),
    ("gabomba-statue",         "Gabomba Statue",          "main",     ["great gabomba", "kibombo statue"]),
    ("gabomba-catacombs",      "Gabomba Catacombs",       "main",     []),
    ("lemurian-ship",          "Lemurian Ship",           "main",     []),
    ("north-osenia-islet",     "North Osenia Islet",      "side",     ["n osenia islet"]),
    ("apojii-islands",         "Apojii Islands",          "main",     []),
    ("aqua-rock",              "Aqua Rock",               "main",     ["aqua rock interior"]),
    ("sea-of-time-islet",      "Sea of Time Islet",       "main",     ["sea of time islet cave"]),
    ("izumo",                  "Izumo",                   "main",     []),
    ("gaia-rock",              "Gaia Rock",               "main",     []),
    ("izumo-ruins",            "Izumo Ruins",             "side",     []),
    ("champa",                 "Champa",                  "main",     []),
    ("ankohl-ruins",           "Ankohl Ruins",            "main",     ["ankohl swamp"]),
    ("east-tundaria-islet",    "East Tundaria Islet",     "side",     ["e tundaria islet"]),
    ("se-angara-islet",        "SE Angara Islet",         "side",     []),
    ("west-indra-islet",       "West Indra Islet",        "side",     []),
    ("yallam",                 "Yallam",                  "main",     []),
    ("taopo-swamp",            "Taopo Swamp",             "side",     []),
    ("islet-cave",             "Islet Cave",              "side",     ["item change/islet cave"]),
    ("tundaria-tower",         "Tundaria Tower",          "main",     ["tundaria"]),
    ("alhafran-cavern",        "Alhafran Cavern",         "side",     ["alhafran cave"]),
    ("sea-of-time",            "Sea of Time",             "main",     ["route through the sea of time"]),
    ("lemuria",                "Lemuria",                 "main",     ["reaching lemuria", "finding lemuria", "going to lemuria", "lemuria at last"]),
    ("hesperia-settlement",    "Hesperia Settlement",     "main",     ["hesperia"]),
    ("shaman-village-cave",    "Shaman Village Cave",     "main",     []),
    ("shaman-village",         "Shaman Village",          "main",     []),
    ("trial-road",             "Trial Road",              "main",     []),
    ("sw-atteka-islet",        "SW Atteka Islet",         "main",     ["atteka inlet", "atteka", "atteka islet"]),
    ("contigo",                "Contigo",                 "main",     []),
    ("jupiter-lighthouse",     "Jupiter Lighthouse",      "main",     ["jupiter lighthouse - reunion"]),
    ("atteka-cavern",          "Atteka Cavern",           "side",     ["angara cavern"]),
    ("magma-rock",             "Magma Rock",              "main",     []),
    ("gondowan-settlement",    "Gondowan Settlement",     "main",     []),
    ("loho",                   "Loho",                    "main",     []),
    ("northern-reaches",       "Northern Reaches",        "main",     []),
    ("prox",                   "Prox",                    "main",     []),
    ("mars-lighthouse",        "Mars Lighthouse",         "main",     ["mars lighthouse and ending", "the mars lighthouse", "ending", "the end"]),
    # --- optional / superboss / postgame ---
    ("kalt-island",            "Kalt Island",             "side",     []),
    ("treasure-isle",          "Treasure Isle",           "postgame", ["treasure island"]),
    ("yampi-desert-cave",      "Yampi Desert Cave",       "postgame", []),
    ("anemos-sanctum",         "Anemos Inner Sanctum",    "postgame", ["anemos sanctum", "anemos inner sanctum"]),
    # --- overworld / navigation interludes (not a fixed area) ---
    ("overworld",              "Overworld / Navigation",  "overworld",
        ["world map", "weyard", "world tour", "getting your ship", "your ship",
         "moving on", "new continent", "to the next continent", "to the next continent",
         "sailing north", "sailing south", "sailing west", "sailing", "out to the open sea",
         "eastern sea", "western sea", "djinni run", "gathering", "more gathering",
         "finding some djinn", "more djinn", "djinn hunting on the western hemisphere",
         "trading sequence", "trident prong", "creating a trident", "collect the trident parts",
         "forge the trident of the ankohl", "transfer events", "walkthrough", "sidequests"]),
    # --- reference bucket: boss/event strategy appendix chapters (blank region,
    #     title = a boss/event name). Overlaps bosses.json + bosses_strategy.json;
    #     during 2a these enrich the boss encounter in their fight's region. ---
    ("boss-strategies",        "Boss Strategies (appendix)", "reference", []),
]

# Coarse / quest-arc / multi-area region tags -> explicit list of node ids.
# (used when one chapter clearly spans several spine nodes; the 2a prompt tells
# the model to use only the slice relevant to each node.)
COARSE_MAP = {
    "Osenia":                     ["garoh", "airs-rock", "osenia-cavern", "mikasalla"],
    "Osenia Continent":           ["garoh", "airs-rock", "osenia-cavern", "mikasalla"],
    "Gondowan":                   ["gondowan-cliffs", "naribwe", "kibombo-mountains", "kibombo", "gabomba-statue"],
    "Atteka":                     ["trial-road", "sw-atteka-islet", "contigo"],
    "Champa, Ankohl Ruins, and Champa Revisited": ["champa", "ankohl-ruins"],
    "Gondowan Cliffs, Naribwe, Kibombo Mountains, and Kibombo": ["gondowan-cliffs", "naribwe", "kibombo-mountains", "kibombo"],
    "Tundaria Tower and Izumo":   ["tundaria-tower", "izumo"],
    "Lemurian Ship, Gabomba Catacombs, and Shrine of the Sea God": ["lemurian-ship", "gabomba-catacombs", "shrine-of-the-sea-god"],
    "Gaia Rock, Izumo Ruins, N Osenia Islet, West Indra Islet, Sea of Time Islet, and Alhafra Revisited": ["gaia-rock", "izumo-ruins", "north-osenia-islet", "sea-of-time-islet", "alhafra"],
    "East Tundaria Islet, SE Angara Islet, Yallam, Taopo Swamp, and Apojii Islands": ["east-tundaria-islet", "yallam", "taopo-swamp", "apojii-islands"],
    "Garoh revisited, Yampi Desert, Alhafra, and Osenia Cavern": ["garoh", "yampi-desert", "alhafra", "osenia-cavern"],
    "Shaman Village Cave, Trial Road, and Contigo": ["shaman-village-cave", "trial-road", "contigo"],
    "Sea of Time, Lemuria, and Hesperia Settlement": ["sea-of-time", "lemuria", "hesperia-settlement"],
    "Loho Angara Cavern, and Prox": ["loho", "atteka-cavern", "prox"],
    "Mars Lighthouse and Ending": ["mars-lighthouse"],
    "Contigo Revisited, Atteka Islet, SW Atteka Islet, SW Atteka Cave, Shaman Village Cave Revisited, and Gondowan Settlement": ["contigo", "sw-atteka-islet", "shaman-village-cave", "gondowan-settlement"],
    "Djinn in Apojii Islands and Gabomba": ["apojii-islands", "gabomba-statue"],
    "Kibombo and Gabomba Statue": ["kibombo", "gabomba-statue"],
    "Venus Lighthouse and Suhalla Gate": ["venus-lighthouse", "suhalla-gate"],
    "Venus Lighthouse and Suhulla Gate": ["venus-lighthouse", "suhalla-gate"],
    "Daila and Kandorean Temple": ["daila", "kandorean-temple"],
    "Shrine of the Sea God and Dehkan Plateau": ["shrine-of-the-sea-god", "dehkan-plateau"],
    "Indra Cavern, Madra, Mikasalla, and Garoh": ["indra-cavern", "madra", "mikasalla", "garoh"],
    "Gondowan Settlement and More": ["gondowan-settlement", "loho"],
    "The Jupiter Djinni in The Shrine of the Sea God": ["shrine-of-the-sea-god"],
    "Cave": ["suhalla-gate"],  # killerfusion 4.113: intro cave between Suhalla Gate & Idejima
}

DECOR = re.compile(
    r"\b(revisited|revisit|revisted|again|reunion|part\s*\d+|part\s*two)\b", re.I)


def norm(s):
    if not s:
        return ""
    s = s.lower()
    s = re.sub(r"\((inside|outside)\)", "", s)
    s = DECOR.sub("", s)
    s = s.replace("'", "").replace('"', "")
    s = re.sub(r"[^a-z0-9 ]", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


def build_alias_index():
    idx = {}
    for nid, name, _kind, aliases in SPINE:
        for key in [name] + aliases:
            idx[norm(key)] = nid
    return idx


def assign(region, alias_idx):
    """Return list of node ids this region tag maps to (possibly empty).

    A blank region on a prose chapter, by inspection of all 10 sources, only
    occurs on boss/event strategy appendix chapters (title = a boss/event name)
    -> route to the boss-strategies reference bucket so nothing is lost."""
    if not region:
        return ["boss-strategies"]
    if region in COARSE_MAP:
        return COARSE_MAP[region]
    n = norm(region)
    if n in alias_idx:
        return [alias_idx[n]]
    # try splitting multi-area "A, B, and C"
    parts = re.split(r",| and ", region)
    hits = []
    for p in parts:
        pn = norm(p)
        if pn and pn in alias_idx and alias_idx[pn] not in hits:
            hits.append(alias_idx[pn])
    return hits


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--unmatched", action="store_true")
    args = ap.parse_args()

    rows = json.load(open(INDEX, encoding="utf-8"))
    prose = [r for r in rows if r["kind"] == "prose-walkthrough"]
    alias_idx = build_alias_index()

    nodes = {nid: {"id": nid, "name": name, "kind": kind, "order": i,
                   "chapters": []}
             for i, (nid, name, kind, _a) in enumerate(SPINE)}
    unmatched = []
    for r in prose:
        ids = assign(r["region"], alias_idx)
        if not ids:
            unmatched.append(r)
            continue
        for nid in ids:
            nodes[nid]["chapters"].append({
                "source_id": r["source_id"], "file": r["file"],
                "title": r["title"], "region": r["region"],
                "covers": r["covers"], "raw_lines": r["raw_lines"],
            })

    if args.unmatched:
        print(f"{len(unmatched)} unmatched prose chapters:\n")
        for r in unmatched:
            print(f'  {r["source_id"]:>14}  region={r["region"]!r:<30}  {r["title"]}')
        return

    out = {"spine": list(nodes.values()),
           "unmatched": unmatched,
           "stats": {
               "prose_chapters": len(prose),
               "assigned": len(prose) - len(unmatched),
               "unmatched": len(unmatched),
               "nodes": len(nodes),
               "empty_nodes": [n["id"] for n in nodes.values() if not n["chapters"]],
           }}
    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"spine nodes: {len(nodes)}  |  prose chapters: {len(prose)}  |  "
          f"assigned: {out['stats']['assigned']}  |  unmatched: {len(unmatched)}")
    if out["stats"]["empty_nodes"]:
        print("EMPTY nodes (no source chapter mapped):")
        for e in out["stats"]["empty_nodes"]:
            print(f"  - {e}")
    print(f"\nper-node source coverage (sources -> #chapters):")
    for n in nodes.values():
        srcs = {}
        for c in n["chapters"]:
            srcs[c["source_id"]] = srcs.get(c["source_id"], 0) + 1
        flag = "  <-- EMPTY" if not n["chapters"] else ""
        print(f'  {n["order"]:>2} {n["kind"]:<9} {n["name"]:<26} '
              f'{len(n["chapters"]):>2} ch / {len(srcs)} src{flag}')
    print(f"\nwrote {OUT}")
    if unmatched:
        print(f"\n{len(unmatched)} unmatched (run --unmatched to list)")


if __name__ == "__main__":
    main()
