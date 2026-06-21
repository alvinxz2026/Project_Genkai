"""Build data/gs2/access_gates.json — the per-region ACCESS-GATE / missable layer (B2).

WHY THIS IS CURATED (not a deterministic parse): whether a collectible is reachable
on first visit or needs a return trip is *judgment over walkthrough prose* — the prose
flags it with phrases like "return later once you have Frost", "* = reachable after
Piers joins", "cannot be obtained until ...", "only accessible during your first visit".
A regex can surface candidate sentences (see git log for the extraction pass) but cannot
reliably bind "which item, gated by what". So the GATES table below is hand-curated from
the 62 consolidated walkthrough nodes, and this script's job is to VALIDATE + materialize
it: every region_id must exist in locations.json, and every named item must resolve to a
pickup / djinn / summon / psynergy actually listed at that region. Unresolved -> FATAL.

KEY FINDING (documented, not a gap): GS2/TLA has effectively NO permanently-missable
collectibles. Once the ship opens the world, every gated item stays reachable on a return
trip. So `missable` is false throughout; the real, trackable payload is `access` =
`return_required` (come back with Psynergy/after an event) vs `first_visit_only` (the easy
access method closes, though the content usually has an alt route) vs `transfer_only`
(only if carried over from GS1). B2's "leaving-area" reminder is built on `return_required`.

Sidecar pattern (does NOT pollute locations.json), mirroring location_refs.json. Rerun:

    python scripts/access_gates_gs2.py

Schema per gate entry:
    region_id        str   — FK to locations.json
    item             str|null — pickup/djinn/summon/psynergy name at that region
                               (null when prose names a gated chest but not its contents)
    kind             str   — item | djinn | summon | psynergy
    access           str   — return_required | first_visit_only | transfer_only
    requires_psynergy [str] — Psynergy NOT held on first visit that unlocks it
    requires_event   str|null — non-Psynergy gate (story event / GS1 transfer / key item)
    missable         bool  — permanently lost if not taken (false for all of GS2)
    note             str   — human-readable provenance from the walkthrough
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "gs2"
OUT = DATA / "access_gates.json"

# region_id -> [gate, ...].  Each gate: (item|None, kind, access, [psy], event|None, note)
RR = "return_required"
FV = "first_visit_only"
TO = "transfer_only"

GATES = {
    "daila": [
        ("Sea God's Tear", "item", RR, ["Frost"], None,
         "Daila Revisited: return with Frost, freeze the Sanctum puddles. Key item used later at Shrine of the Sea God."),
    ],
    "shrine-of-the-sea-god": [
        ("Rusty Staff", "item", RR, [], "Piers joins party",
         "Marked '* reachable after Piers joins'; grabbed on the Second Visit downriver."),
        ("Right Prong", "item", RR, [], "Piers joins party",
         "Marked '* reachable after Piers joins'."),
    ],
    "indra-cavern": [
        ("Cookie", "item", RR, ["Frost"], "Piers joins + Black Crystal",
         "East Indra Shore / Piers' Ship section — relevant only after Piers and the Black Crystal."),
        ("Elixir", "item", RR, ["Frost"], "Piers joins + Black Crystal",
         "Piers' Ship cabin, after the locked door opens."),
        ("Potion", "item", RR, ["Frost"], "Piers joins + Black Crystal",
         "Piers' Ship below deck, Aqua-Jelly Frost puzzle."),
        ("Antidote", "item", RR, ["Frost"], "Piers joins + Black Crystal",
         "Piers' Ship below deck, Aqua-Jelly Frost puzzle."),
    ],
    "madra": [
        ("Char", "djinn", RR, ["Frost"], "trade Healing Fungus",
         "Traded by the townsman for the Healing Fungus (which itself needs Frost at Gondowan Cliffs)."),
    ],
    "madra-catacombs": [
        ("Apple", "item", RR, ["Frost", "Reveal"], None,
         "Return Visit (needs Frost + Reveal); Frost the puddle to reach the chest."),
        ("Lucky Medal", "item", RR, ["Frost", "Reveal"], None,
         "Return Visit (needs Frost + Reveal)."),
        # graveyard-entrance items below are first-visit-easy but NOT missable (alt route via Reveal)
        ("Tremor Bit", "item", FV, [], None,
         "Graveyard entrance is first-visit-only; if you return the cave is blocked and you must use the main ladder + Reveal. Content still reachable, so not missable."),
    ],
    "yampi-desert": [
        # the optional Yampi Desert Cave (also surfaced as region yampi-desert-cave)
        ("Water of Life", "item", RR, ["Sand"], None, "Optional Yampi Desert Cave, accessible much later with Sand."),
        ("Mythril Silver", "item", RR, ["Sand"], None, "Optional Yampi Desert Cave (Sand)."),
        ("Dark Matter", "item", RR, ["Sand"], None, "Optional Yampi Desert Cave (Sand)."),
        ("Orihalcon", "item", RR, ["Sand", "Burst"], None, "Optional Yampi Desert Cave; Burst the crumbling pillar."),
        ("Crystal", "djinn", RR, ["Sand", "Scoop"], None, "Optional Yampi Desert Cave; time Scoop to unearth it."),
        ("Daedalus", "summon", RR, ["Sand"], None, "Optional Yampi Desert Cave."),
    ],
    "garoh": [
        ("Hypnos' Sword", "item", RR, ["Reveal"], None,
         "Revisit: Reveal the six cavern platforms to open the path to the chest."),
    ],
    "airs-rock": [
        ("Vial", "item", RR, ["Frost"], None,
         "Exterior chest marked '* reachable after learning Frost'."),
    ],
    "gondowan-cliffs": [
        ("Healing Fungus", "item", RR, ["Frost"], None,
         "Flagged 'requires Frost, cannot be collected yet'. Feeds the Madra trade for Char."),
    ],
    "kibombo-mountains": [
        ("Waft", "djinn", RR, ["Frost", "Growth"], None,
         "Footnote: 'must return later with Frost and Growth to reach it'."),
    ],
    "lemurian-ship": [
        (None, "item", RR, ["Parch"], None,
         "After the boss the room floods; one chest is unreachable until Parch (contents unnamed in prose)."),
    ],
    "alhafran-cavern": [
        ("777 Coins", "item", RR, ["Frost"], "Briggs escapes",
         "After Briggs' escape removes the pillar; Frost the puddle for the three deeper chests."),
        ("Potion", "item", RR, ["Frost"], "Briggs escapes", "Deeper Frost-gated chest after Briggs escapes."),
        ("Psy Crystal", "item", RR, ["Frost"], "Briggs escapes", "Deeper Frost-gated chest after Briggs escapes."),
    ],
    "islet-cave": [
        ("Tisiphone Edge", "item", RR, ["Teleport"], None,
         "Second stretch of the Islet Cave opens only after Teleport; dropped by the Cruel Dragons."),
    ],
    "shaman-village-cave": [
        ("Eddy", "djinn", RR, ["Lift"], None,
         "Middle path Mercury Djinni unreachable without Lift; return on the Second Visit."),
    ],
    "trial-road": [
        ("Gasp", "djinn", RR, ["Lift", "Reveal"], None,
         "Second Visit after Hover Jade + joining Isaac's party (Lift + Reveal)."),
    ],
    "sw-atteka-islet": [
        ("Petra", "djinn", RR, ["Hover", "Lift"], None, "Islet only reachable after Hover (ship wings)."),
        ("Core", "djinn", RR, ["Hover"], None, "Islet only reachable after Hover."),
        ("Geode", "djinn", RR, ["Hover", "Lift", "Cyclone"], None, "Lift the boulder, Cyclone the weeds."),
        ("Vial", "item", RR, ["Hover"], None, "Islet only reachable after Hover."),
        ("Orihalcon", "item", RR, ["Hover"], None, "Islet only reachable after Hover."),
        ("Dragon Skin", "item", RR, ["Hover"], None, "Islet only reachable after Hover."),
    ],
    "contigo": [
        ("Shine", "djinn", TO, ["Force"], "Force Orb (GS1 transfer)",
         "Only if data transferred from GS1 (Force Orb); Force the stump on the Contigo revisit after Jupiter Lighthouse."),
    ],
    "atteka-cavern": [
        ("Coatlicue", "summon", RR, ["Hover", "Carry"], None,
         "Cavern only reachable once the ship has wings (Hover); inner puzzle needs Carry."),
        ("Haures", "summon", RR, ["Hover", "Carry"], None,
         "Cavern only reachable once the ship has wings (Hover); inner puzzle needs Carry."),
    ],
    "treasure-isle": [
        ("Jester's Armlet", "item", RR, ["Grind"], None,
         "Dungeon reachable early but only fully cleared with Grind + Lift."),
        ("Gale", "djinn", RR, ["Lift"], None, "Lift the center boulder to reach the Jupiter Djinni."),
        ("Iris Robe", "item", RR, ["Grind", "Lift"], None, "Deep Treasure Isle (Grind + Lift)."),
        ("Fire Brand", "item", RR, ["Grind", "Lift"], None, "Deep Treasure Isle (Grind + Lift)."),
        ("Azul", "summon", RR, ["Grind", "Lift"], None, "Deep Treasure Isle (Grind + Lift)."),
    ],
    "yampi-desert-cave": [
        ("Water of Life", "item", RR, ["Sand"], None, "Optional cave, accessible much later with Sand."),
        ("Mythril Silver", "item", RR, ["Sand", "Scoop"], None, "Scoop the sparkling ground."),
        ("Dark Matter", "item", RR, ["Sand"], None, "Optional cave (Sand)."),
        ("Orihalcon", "item", RR, ["Sand", "Burst"], None, "Burst the broken pillar."),
        ("Crystal", "djinn", RR, ["Sand", "Scoop"], None, "Time Scoop (or Halt then Scoop) to unearth it."),
        ("Daedalus", "summon", RR, ["Sand"], None, "Optional cave (Sand)."),
    ],
    "anemos-sanctum": [
        ("Dragon Skin", "item", RR, ["Reveal"], None, "Reveal at the main entrance for the chest."),
        ("Dark Matter", "item", RR, ["Teleport"], "all 72 Djinn collected",
         "Inner Sanctum needs all 72 Djinn + Teleport (Teleport the Contigo circle)."),
        ("Orihalcon", "item", RR, ["Teleport"], "all 72 Djinn collected", "Inner Sanctum (all 72 Djinn + Teleport)."),
        ("Charon", "summon", RR, ["Teleport"], "all 72 Djinn collected", "Inner Sanctum (all 72 Djinn + Teleport)."),
        ("Iris", "summon", RR, ["Teleport"], "all 72 Djinn collected", "Inner Sanctum (all 72 Djinn + Teleport)."),
    ],
}


def load(name):
    return json.loads((DATA / f"{name}.json").read_text(encoding="utf-8"))


def main():
    locs = load("locations")
    by_region = {l["region_id"]: l for l in locs}

    fatals = []
    out = []
    for region_id, gates in GATES.items():
        loc = by_region.get(region_id)
        if loc is None:
            fatals.append(f"unknown region_id: {region_id}")
            continue
        # the set of collectible names actually present at this region (for validation)
        present = set()
        for f in ("pickups", "djinn_here", "psynergy_here", "summons_here"):
            present.update(loc.get(f) or [])

        entries = []
        for item, kind, access, psy, event, note in gates:
            if item is not None and item not in present:
                fatals.append(f"[{region_id}] item not listed at region: {item!r} "
                              f"(present: {sorted(present)})")
            entries.append({
                "item": item,
                "kind": kind,
                "access": access,
                "requires_psynergy": psy,
                "requires_event": event,
                "missable": False,
                "note": note,
            })
        out.append({
            "region_id": region_id,
            "order": loc["order"],
            "name": loc["name"],
            "point_of_no_return": False,  # GS2 open world: no hard permanent missables
            "gates": entries,
        })

    out.sort(key=lambda r: r["order"])

    if fatals:
        print("FATAL — curated GATES table does not validate against locations.json:")
        for f in fatals:
            print("  -", f)
        sys.exit(1)

    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    n_gates = sum(len(r["gates"]) for r in out)
    print(f"wrote {OUT.relative_to(ROOT)}  ({len(out)} regions, {n_gates} gated collectibles)")
    # quick breakdown
    from collections import Counter
    acc = Counter(g["access"] for r in out for g in r["gates"])
    psy = Counter(p for r in out for g in r["gates"] for p in g["requires_psynergy"])
    print("  access:", dict(acc))
    print("  top gate psynergy:", dict(psy.most_common(8)))


if __name__ == "__main__":
    main()
