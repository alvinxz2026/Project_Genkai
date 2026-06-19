"""Backfill djinn.battle_effect from telago's Djinn Descriptions appendix.

demooni (the djinn stat source) gives per-djinn stat boosts + location but no
battle ability text, so djinn.json ships with battle_effect: null. Telago's
appendix chapter 24 (`raw/gs2/_chapters/telago/24-djinn-descriptions.md`) is a
fixed-width table whose last column is the in-battle Ability (e.g. Flint -> "Swift
Strike", Granite -> "Reduce Damage"). This deterministic parser slices that column
by its header position and writes it onto the matching djinn.

Idempotent: re-derives battle_effect from telago each run; adds "telago" to
sources only on djinn it fills. Run anytime; independent of links_normalize.

Usage: python scripts/djinn_telago_effects_gs2.py
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "gs2"
SRC = ROOT / "raw" / "gs2" / "_chapters" / "telago" / "24-djinn-descriptions.md"


def norm(s):
    return re.sub(r"[^a-z0-9]", "", s.lower())


def parse_effects():
    """name(norm) -> battle ability. Column-sliced by the header's 'Ability' pos."""
    out = {}
    col_loc = col_abil = None
    for raw in SRC.read_text(encoding="utf-8").splitlines():
        line = raw.rstrip("\n")
        if "Location" in line and "Ability" in line:        # section header row
            col_loc, col_abil = line.index("Location"), line.index("Ability")
            continue
        if col_abil is None or not line.strip():
            continue
        if line[:1] == " " or line.lstrip().startswith("("):  # notes / "(WM) ="
            continue
        name = line.split()[0]
        ability = line[col_abil:].strip()
        if name and ability:
            out[norm(name)] = ability
    return out


def main():
    djinn = json.loads((DATA / "djinn.json").read_text(encoding="utf-8"))
    effects = parse_effects()

    filled, unmatched = 0, []
    for d in djinn:
        eff = effects.get(norm(d["name"]))
        if eff:
            d["battle_effect"] = eff
            if "telago" not in d["sources"]:
                d["sources"].append("telago")
            filled += 1
    matched_names = {norm(d["name"]) for d in djinn}
    unmatched = sorted(n for n in effects if n not in matched_names)

    (DATA / "djinn.json").write_text(json.dumps(djinn, ensure_ascii=False, indent=2) + "\n",
                                     encoding="utf-8")
    print(f"djinn_telago_effects_gs2 — battle_effect filled {filled}/{len(djinn)} djinn")
    print(f"  telago abilities parsed     : {len(effects)}")
    if unmatched:
        print(f"  telago names not in djinn.json ({len(unmatched)}): {unmatched}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
