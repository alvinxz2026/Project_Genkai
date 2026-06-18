"""Build data/gs2/bosses.json: deterministic stat skeleton + curated strategy.

Two layers, mirroring the project pattern (deterministic where the data is clean,
curated/prose only where it must be):

  Layer 1 (this script, deterministic & free): the boss *numbers* are already
  parsed into data/gs2/monsters.json (the 23 `is_boss` stat-lines from
  torrentlord). We do NOT re-extract them; we pull stats / elements / abilities /
  rewards / location straight from monsters.json via a small curated boss map
  (which collapses party-config stat variants and multi-form dragons into one
  boss each — see BOSSES below).

  Layer 2 (curated prose, optional sidecar): strategy / weakness /
  recommended_level / special_mechanics come from the prose boss guides
  (link-kirby-boss, goldmario-boss) and live in
  data/gs2/intermediate/bosses_strategy.json (hand-authored from those sources,
  the LLM/judgment half). If that file is absent the skeleton is still emitted
  with those fields null/[] (deferred), exactly as monsters deferred its FKs.

Element shape note: gs2 keeps elemental_power/resistance as the {earth,fire,wind,
water} dict used by gs2 monsters (NOT gs1's array-of-objects) so the two gs2
fact tables stay consistent.

Cross-link: monsters.boss_id back-fill is the job of the (future) gs2
links_normalize, not this script — it stays null in monsters.json for now.

Rerunnable: reads monsters.json + the strategy sidecar only; no stats embedded.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MONSTERS = ROOT / "data" / "gs2" / "monsters.json"
STRATEGY = ROOT / "data" / "gs2" / "intermediate" / "bosses_strategy.json"
OUT = ROOT / "data" / "gs2" / "bosses.json"

# Curated boss map. Each boss pulls its stat-line(s) from monsters.json.
#   monster  : primary monster id (canonical stats)
#   variants : party-config stat variants (collapsed; noted, not separate fights)
#   forms    : distinct simultaneous/sequential forms (extra encounters)
#   optional / superboss : the 4 summon-tablet guardians (link-kirby groups them
#              separately from "Required Bosses").
BOSSES = [
    {"id": "chestbeater", "name": "Chestbeater", "monster": "chestbeater",
     "note": "Fought as three Chestbeaters at once (x3)."},
    {"id": "king-scorpion", "name": "King Scorpion", "monster": "king-scorpion"},
    {"id": "briggs", "name": "Briggs", "monster": "briggs",
     "note": "Fought alongside two Sea Fighters."},
    {"id": "sea-fighter", "name": "Sea Fighter", "monster": "sea-fighter",
     "note": "Two appear as Briggs' escorts."},
    {"id": "aqua-hydra", "name": "Aqua Hydra", "monster": "aqua-hydra"},
    {"id": "serpent", "name": "Serpent", "monster": "serpent"},
    {"id": "avimander", "name": "Avimander", "monster": "avimander"},
    {"id": "poseidon", "name": "Poseidon", "monster": "poseidon"},
    {"id": "moapa", "name": "Moapa", "monster": "moapa",
     "note": "Fought alongside two Knights."},
    {"id": "knight", "name": "Knight", "monster": "knight",
     "note": "Two appear as Moapa's escorts."},
    {"id": "agatio", "name": "Agatio", "monster": "agatio",
     "variants": ["agatio-vs-all", "agatio-vs-2-3"],
     "note": "Fought together with Karst at Jupiter Lighthouse."},
    {"id": "karst", "name": "Karst", "monster": "karst",
     "variants": ["karst-vs-all", "karst-vs-2-3"],
     "note": "Fought together with Agatio at Jupiter Lighthouse."},
    {"id": "flame-dragon", "name": "Flame Dragon", "monster": "flame-dragon-big",
     "forms": ["flame-dragon-small", "flame-dragon-big"],
     "note": "Two Flame Dragons (Agatio & Karst transformed) at Mars Lighthouse."},
    {"id": "doom-dragon", "name": "Doom Dragon", "monster": "doom-dragon",
     "note": "Final boss; three heads / multiple HP phases (5000 / 4200 / 4000)."},
    {"id": "valukar", "name": "Valukar", "monster": "valukar", "optional": True, "superboss": True},
    {"id": "star-magician", "name": "Star Magician", "monster": "star-magician", "optional": True, "superboss": True},
    {"id": "sentinel", "name": "Sentinel", "monster": "sentinel", "optional": True, "superboss": True},
    {"id": "dullahan", "name": "Dullahan", "monster": "dullahan", "optional": True, "superboss": True},
]


def encounter_from_monster(m, mid):
    """Build one encounter object from a monsters.json boss stat-line."""
    return {
        "form_id": mid,
        "location": m["found"][0] if m["found"] else None,
        "stats": m["stats"],
        "elemental_power": m["elemental_power"],
        "elemental_resistance": m["elemental_resistance"],
        "attacks": [{"name": a, "source": "torrentlord"} for a in m["abilities"]],
        "rewards": {
            "exp": m["drops"]["exp"], "coins": m["drops"]["coins"],
            "items": [d["name"] for d in m["drops"]["items"]],
        },
    }


def variant_note(monsters, ids):
    """Summarize party-config stat variants (HP/Atk differ by transfer count)."""
    bits = []
    for vid in ids:
        v = monsters.get(vid)
        if v:
            bits.append(f"{vid}: HP {v['stats']['hp']}, Atk {v['stats']['atk']}")
    return ("Stats vary by GS1-transfer party size — " + "; ".join(bits) + ".") if bits else None


def main():
    monsters = {x["id"]: x for x in json.loads(MONSTERS.read_text(encoding="utf-8"))}
    strategy = {}
    if STRATEGY.exists():
        strategy = {s["id"]: s for s in json.loads(STRATEGY.read_text(encoding="utf-8"))}

    bosses = []
    missing = []
    for b in BOSSES:
        prim = monsters.get(b["monster"])
        if not prim:
            missing.append(b["monster"])
            continue
        encounters = [encounter_from_monster(prim, b["monster"])]
        for fid in b.get("forms", []):
            if fid != b["monster"] and fid in monsters:
                encounters.append(encounter_from_monster(monsters[fid], fid))

        notes = [n for n in (b.get("note"), variant_note(monsters, b.get("variants", []))) if n]
        st = strategy.get(b["id"], {})
        bosses.append({
            "id": b["id"], "name": b["name"], "game": "gs2",
            "is_optional": b.get("optional", False),
            "is_superboss": b.get("superboss", False),
            "encounters": encounters,
            "weakness": st.get("weakness", []),
            "recommended_level": st.get("recommended_level"),
            "strategy": st.get("strategy"),
            "special_mechanics": st.get("special_mechanics", []),
            "special_notes": " ".join(notes) if notes else None,
            "sources": sorted(set(["torrentlord"] + st.get("sources", []))),
        })

    OUT.write_text(json.dumps(bosses, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    n_strat = sum(b["strategy"] is not None for b in bosses)
    print(f"wrote {OUT.relative_to(ROOT)} : {len(bosses)} bosses")
    print(f"  superbosses / optional : {sum(b['is_superboss'] for b in bosses)} / {sum(b['is_optional'] for b in bosses)}")
    print(f"  multi-form encounters  : {sum(len(b['encounters']) > 1 for b in bosses)}")
    print(f"  with curated strategy  : {n_strat}/{len(bosses)}"
          + ("" if STRATEGY.exists() else f"  (no sidecar at {STRATEGY.relative_to(ROOT)} yet)"))
    if missing:
        print(f"  WARNING missing monster stat-lines: {missing}")


if __name__ == "__main__":
    main()
