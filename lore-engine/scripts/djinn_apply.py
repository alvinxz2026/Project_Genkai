"""C1: regenerate djinn.json with new sources, must_fight, and resolved conflicts.

- must_fight: derived from the §XIII bestiary (monsters.json) — a Djinni listed
  as an "X Djinni" enemy must be fought.
- sources: append the new corroborating sources that cover every Djinni
  (telago/shotgunnova/electrospecter/super-slash); bfgamer for the 5 it lists;
  torrent-load for the fought Djinn.
- conflicts: re-adjudicated per the Conflict Resolution Policy. Resolutions are
  encoded here (they are human adjudication, kept with the data for an audit
  trail). Stat disagreements -> terence authority; location names -> majority.

Rerunnable.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DJ = ROOT / "data/gs1/djinn.json"

BF5 = {"Flint", "Forge", "Gust", "Granite", "Breeze"}  # djinn BFGamer §6.1 lists

# resolved conflicts (and area overrides where the resolved value differs from current)
RESOLUTIONS = {
    "zephyr": {
        "area": "Fuchin Falls Cave",
        "conflicts": [{
            "field": "location.area",
            "values": {"plz2bstfu": "Fuchin Temple", "telago": "Fuchin Temple",
                       "fandom-wiki": "Fuchin Falls Cave", "shotgunnova": "Fuchin Falls Cave",
                       "electrospecter": "Fuchin Falls Cave", "super-slash": "Fuchin Falls Cave"},
            "resolution": "majority",
            "note": "4 of 6 sources (incl. fandom-wiki) say 'Fuchin Falls Cave'; 'Fuchin Temple' is the broader area name.",
        }],
    },
    "luff": {
        "area": "Babi Lighthouse",
        "conflicts": [{
            "field": "location.area",
            "values": {"plz2bstfu": "Babi Tower", "telago": "Babi's Tower",
                       "fandom-wiki": "Babi Lighthouse", "shotgunnova": "Babi Lighthouse",
                       "electrospecter": "Babi Lighthouse", "super-slash": "Babi Lighthouse Entrance"},
            "resolution": "majority",
            "note": "4 of 6 sources (incl. fandom-wiki) say 'Babi Lighthouse'; plz2bstfu/Telago call the same structure 'Babi('s) Tower'.",
        }],
    },
    "hail": {
        "area": "World Map (west/northwest of Tolbi)",
        "conflicts": [{
            "field": "location.area",
            "values": {"plz2bstfu": "World Map (west/northwest of Tolbi)",
                       "telago": "World Map (west of Tolbi)",
                       "shotgunnova": "World Map (NW of Tolbi, by bridge)",
                       "electrospecter": "World Map (NW of Tolbi, across two bridges)",
                       "super-slash": "World Map",
                       "fandom-wiki": "Gondowan (forested area SW of Altmiller Cave)"},
            "resolution": "majority",
            "note": "5 sources place it on the world map NW/W of Tolbi; fandom-wiki frames the same spot as Gondowan SW of Altmiller Cave (different reference point).",
        }],
    },
    "tonic": {
        "area": "Lunpa Fortress",
        "conflicts": [
            {
                "field": "location.area",
                "values": {"plz2bstfu": "Dononpa's Fortress", "fandom-wiki": "Lunpa Fortress",
                           "telago": "Lunpa Fortress", "shotgunnova": "Lunpa Fortress",
                           "electrospecter": "Lunpa Fortress", "super-slash": "Lunpa Fortress"},
                "resolution": "majority",
                "note": "5 of 6 sources say 'Lunpa Fortress' (standard name); plz2bstfu uses 'Dononpa's Fortress' (after the boss).",
            },
            {
                "field": "stat_bonus.hp",
                "values": {"terence": 8, "telago": 10},
                "resolution": "authority",
                "note": "terence (data-mined mechanics FAQ) authoritative for stats; Telago lists hp 10.",
            },
        ],
    },
    "fever": {
        "conflicts": [
            {"field": "stat_bonus.hp", "values": {"terence": 8, "telago": 12},
             "resolution": "authority", "note": "terence authoritative; Telago lists hp 12."},
            {"field": "stat_bonus.agi", "values": {"terence": 2, "telago": 1},
             "resolution": "authority", "note": "terence authoritative; Telago lists agi 1."},
        ],
    },
    "kite": {
        "conflicts": [
            {"field": "stat_bonus.pp", "values": {"terence": 4, "telago": 3},
             "resolution": "authority", "note": "terence authoritative; Telago lists pp 3."},
        ],
    },
}


def main():
    D = json.load(open(DJ, encoding="utf-8"))
    M = json.load(open(ROOT / "data/gs1/monsters.json", encoding="utf-8"))
    fought = {m["djinn_id"] for m in M if m["is_djinn_enemy"] and m["djinn_id"]}

    out = []
    for d in D:
        # sources: existing + corroborating new ones
        srcs = list(d["sources"])
        for s in ("telago", "shotgunnova", "electrospecter", "super-slash"):
            if s not in srcs:
                srcs.append(s)
        if d["name"] in BF5 and "bfgamer" not in srcs:
            srcs.append("bfgamer")
        if d["id"] in fought and "torrent-load" not in srcs:
            srcs.append("torrent-load")

        loc = dict(d["location"])
        res = RESOLUTIONS.get(d["id"])
        if res and "area" in res:
            loc["area"] = res["area"]

        entry = {
            "id": d["id"], "name": d["name"], "element": d["element"], "game": d["game"],
            "stat_bonus": d["stat_bonus"], "battle_effect": d["battle_effect"],
            "location": loc, "must_fight": d["id"] in fought, "sources": srcs,
        }
        if res:
            entry["conflicts"] = res["conflicts"]
        out.append(entry)

    json.dump(out, open(DJ, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    open(DJ, "a", encoding="utf-8").write("\n")

    print(f"djinn.json: {len(out)} entries")
    print(f"  must_fight=true: {sum(e['must_fight'] for e in out)}")
    print(f"  with conflicts : {sum('conflicts' in e for e in out)} -> {[e['id'] for e in out if 'conflicts' in e]}")
    print(f"  Flint sources  : {out[0]['sources']}")


if __name__ == "__main__":
    main()
