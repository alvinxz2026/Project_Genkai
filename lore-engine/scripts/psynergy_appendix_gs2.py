"""Gap-fill psynergy.json with the class-exclusive spells the canonical set omits.

GS2's psynergy.json is the yoyoyoshi "clean canonical" set (157) — deliberately
non-exhaustive. ~37 distinct spells that ultimalink's class learn-lists reference
(card tricks, Magma Storm, Hurricane, Thorn/Nettle, the Tamer summon-psynergy,
Searing Beam, Froth Spiral, ...) have no canonical entry, so their
classes.psynergy[].id never resolves (the audit's "expected gap" pile).

Telago's appendix chapter 33 (`raw/gs2/_chapters/telago/33-psynergy-spells.md`)
is a complete fixed-width psynergy table WITH stats (lvl / element / PP / range /
effect). This deterministic parser reads its battle sections (II Healing&Status,
III Attack), and ADDS every spell whose name is not already in canonical — closing
the gap so the class refs resolve. Field psynergy (section I) all already exist in
canonical, so nothing is added from there.

Naming reconciliation (telago spelling vs the consumer/class-ref spelling):
  - CANON_NAME: rename a telago entry to the standard consumer spelling, keeping
    telago's spelling in name_variants (e.g. "Sabre Dance" -> "Saber Dance").
  - VARIANT_OF: a telago/class name that is the SAME spell as an existing canonical
    entry under a different name is folded into that entry's name_variants (not a
    duplicate row): ultimalink "Thunderhead" -> canonical "Thunderstorm"; telago
    "Megacool" -> canonical "Extremecool" (a real cross-source conflict, also
    recorded in `conflicts`). Resolution is variant-aware in links_normalize_gs2 /
    links_audit_gs2, so these resolve without a second row.

Idempotent: drops any prior telago-sourced rows + telago-added name_variants first,
then re-derives. Run BEFORE links_normalize_gs2.py (which resolves the new ids).

Usage: python scripts/psynergy_appendix_gs2.py
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "gs2"
SRC = ROOT / "raw" / "gs2" / "_chapters" / "telago" / "33-psynergy-spells.md"

ELEM = {"Wind": "wind", "Fire": "fire", "Earth": "earth", "Water": "water", "-": "neutral"}

# telago spelling -> standard consumer spelling (class refs use the value); the
# telago spelling is preserved in name_variants.
CANON_NAME = {"Sabre Dance": "Saber Dance"}

# name (telago- or class-spelled) -> existing canonical entry it is the SAME spell
# as. Folded into that entry's name_variants instead of creating a duplicate row.
# value 'conflict' marks a genuine cross-source naming disagreement (flagged).
VARIANT_OF = {
    "Thunderhead": ("Thunderstorm", "ultimalink-variant"),
    "Megacool": ("Extremecool", "conflict"),  # telago vs yoyoyoshi
    "Ice Missle": ("Ice Missile", "telago-typo"),   # telago drops an 'i'
    "HP Drain": ("Drain", "telago-variant"),         # canonical "Drain" == telago "HP Drain"
}


def norm(s):
    return re.sub(r"[^a-z0-9]", "", s.lower())


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def parse_telago33():
    """Yield (name, element, pp, range, effect) for battle-section spells."""
    mode = None  # 'field' (Item col) | 'battle' (Ran col)
    seen = {}
    for raw in SRC.read_text(encoding="utf-8").splitlines():
        line = raw.rstrip()
        if "PP Item" in line:
            mode = "field"; continue
        if "PP Ran" in line:
            mode = "battle"; continue
        if mode != "battle" or not line.strip():
            continue
        # data row: name (up to 2+ spaces) | lvl | elem | pp(int) | ran | effect?
        m = re.match(r"^(?P<name>\S.*?)\s{2,}(?P<lvl>\S+)\s+(?P<elem>\S+)\s+"
                     r"(?P<pp>\d+)\s+(?P<ran>\S+)(?:\s+(?P<eff>.*))?$", line)
        if not m or m["elem"] not in ELEM:
            continue
        name = re.sub(r"\s*\(.*\)", "", m["name"]).strip()  # "Force (Ki)" -> "Force"
        ran = m["ran"]
        rng = ran.lower() if ran in {"1", "3", "5", "7"} else ("all" if ran == "All" else None)
        eff = (m["eff"] or "").strip()
        if name and norm(name) not in seen:
            seen[name] = (name, ELEM[m["elem"]], int(m["pp"]), rng, eff)
    return list(seen.values())


def main():
    psy = json.loads((DATA / "psynergy.json").read_text(encoding="utf-8"))

    # --- idempotency: strip prior telago additions + telago-added variants ---
    psy = [p for p in psy if "telago" not in p.get("sources", []) or p.get("sources") != ["telago"]]
    by_name = {norm(p["name"]): p for p in psy}
    for canon, _ in VARIANT_OF.values():
        e = by_name.get(norm(canon))
        if e:
            e["name_variants"] = [v for v in e.get("name_variants", [])
                                  if norm(v) not in {norm(k) for k in VARIANT_OF}]
            if not e["name_variants"]:
                e.pop("name_variants", None)
            e.pop("conflicts", None)

    canon_names = {norm(p["name"]) for p in psy}
    added, folded = [], []

    # --- fold VARIANT_OF names into existing canonical entries ---
    for variant, (canon, kind) in VARIANT_OF.items():
        e = by_name.get(norm(canon))
        if not e:
            continue
        e.setdefault("name_variants", [])
        if norm(variant) not in {norm(v) for v in e["name_variants"]}:
            e["name_variants"].append(variant)
        if kind == "conflict":
            e["conflicts"] = [{"field": "name", "value": variant, "source": "telago",
                               "note": f"telago calls this {variant!r}; canonical (yoyoyoshi) {e['name']!r}"}]
            if "telago" not in e["sources"]:
                e["sources"].append("telago")
        folded.append(f"{variant} -> {canon} ({kind})")

    # --- add telago battle spells absent from canonical ---
    for name, elem, pp, rng, eff in parse_telago33():
        disp = CANON_NAME.get(name, name)
        if norm(disp) in canon_names or norm(name) in {norm(v) for v in VARIANT_OF}:
            continue
        sm = re.search(r"^(.*?)\s+Series\b", eff)
        series = re.sub(r"\(\d\)", "", sm.group(1)).strip().lower() if sm else None
        desc = None if (sm and sm.start() == 0) else (eff or None)
        entry = {
            "id": slug(disp), "name": disp, "game": "gs2", "element": elem,
            "pp_cost": pp, "range": rng, "description": desc,
            "series": series or None, "tier": None, "sources": ["telago"],
        }
        if disp != name:
            entry["name_variants"] = [name]
        added.append(entry)
        canon_names.add(norm(disp))

    # guard: no id collisions
    ids = [p["id"] for p in psy] + [e["id"] for e in added]
    assert len(ids) == len(set(ids)), f"id collision: {[i for i in ids if ids.count(i) > 1]}"

    psy.extend(added)
    (DATA / "psynergy.json").write_text(json.dumps(psy, ensure_ascii=False, indent=2) + "\n",
                                        encoding="utf-8")

    print(f"psynergy_appendix_gs2 — psynergy.json now {len(psy)} entries (+{len(added)} added)")
    print(f"  folded as variants ({len(folded)}): {', '.join(folded)}")
    print(f"  added ({len(added)}):")
    for e in sorted(added, key=lambda x: x["name"]):
        print(f"    {e['name']:16} {e['element']:7} pp={e['pp_cost']:<3} range={e['range']} "
              f"series={e['series']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
