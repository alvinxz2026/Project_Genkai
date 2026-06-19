"""Merge forging data from `aspartate-forge` into data/gs2/equipment.json.

Per the ER sketch, forging is NOT a separate entity — it enriches equipment:
each forgeable item gets `forged_from` = [source material]. Rusty weapons forge
from a found "Rusty <Type>"; raw-material items forge from the material block
they sit under (Orihalcon, Dark Matter, ...).

Source structure (section IV "GS:TLA Forged Items Guide"):
  [Material]                         <- material block header (or [Rusty Weapons])
  ItemName
  ------------
  <EquipType>: for <chars>
  Worth N coins
  Attack +N / Defense +N / ...
  Unleashes X                        (optional)
  Found as Rusty <Type> (...)        (rusty section only)

This pass writes `forged_from` (idempotent: cleared then re-set for matched
items) and prints a corroboration report (Worth vs buy_price, Unleashes vs
unleash.name). equippable_by is intentionally left to links_normalize_gs2's
type->can_equip derivation; the forge "for <chars>" line is parsed only for the
cross-check report, not written here.

Rerunnable / deterministic; no manual data embedded.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "raw" / "gs2" / "In-Depth Guides" / "Forged Items Guide by aspartate.md"
DATA = ROOT / "data" / "gs2"

CHARS = ["Isaac", "Garet", "Ivan", "Mia", "Felix", "Jenna", "Sheba", "Piers"]

# forge-guide spelling -> equipment.json canonical name (same item, source variance).
# "appolo's axe" is an equipment.json typo (mr-unorigino) the forge guide spells
# correctly; aliased so forged_from resolves, and reported below.
FORGE_ALIASES = {
    "cosmo shield": "Cosmos Shield",
    "psychic circlet": "Psychic Circle",
    "astral circlet": "Astral Circle",
    "spirits ring": "Spirit Ring",
    "apollo's axe": "Appolo's Axe",
}


def norm(s):
    return re.sub(r"[^a-z0-9]", "", s.lower())


def parse_for_chars(text):
    """'for Ivan, Mia, Jenna, and Sheba' / 'for everyone' /
    'for everyone except Ivan and Jenna' -> [char ids]."""
    t = text.strip()
    names = lambda blob: [c.lower() for c in CHARS if re.search(rf"\b{c}\b", blob)]
    if "everyone" in t.lower():
        m = re.search(r"except (.+)", t, re.I)
        excl = set(names(m.group(1))) if m else set()
        return [c.lower() for c in CHARS if c.lower() not in excl]
    return names(t)


def parse_forge():
    lines = RAW.read_text(encoding="utf-8").splitlines()
    # section IV body .. section V
    start = next(i for i, l in enumerate(lines)
                 if l.strip() == "GS:TLA Forged Items Guide" and i > 80)
    end = next(i for i, l in enumerate(lines)
               if l.strip() == "Monsters that drop raw materials")
    body = lines[start:end]

    items = []
    material = None
    i = 0
    while i < len(body):
        s = body[i].strip()
        mh = re.fullmatch(r"\[(.+)\]", s)
        if mh:
            material = mh.group(1).strip()
            i += 1
            continue
        # item block: name line followed by a dashes line
        if i + 1 < len(body) and re.fullmatch(r"-{3,}", body[i + 1].strip()) and s:
            name = s
            attrs = {"name": name, "material": material, "for_chars": [],
                     "worth": None, "unleash": None, "rusty": None}
            j = i + 2
            while j < len(body) and body[j].strip() != "" and \
                    not re.fullmatch(r"-{3,}", body[j].strip()) and \
                    not re.fullmatch(r"\[(.+)\]", body[j].strip()):
                a = body[j].strip()
                m = re.match(r"^[\w' ]+:\s*for\s+(.+)$", a)
                if m:
                    attrs["for_chars"] = parse_for_chars(m.group(1))
                elif re.match(r"^Worth\s+(\d+)\s+coins", a):
                    attrs["worth"] = int(re.search(r"\d+", a).group())
                elif a.startswith("Unleashes "):
                    attrs["unleash"] = a[len("Unleashes "):].strip().split("(")[0].strip()
                elif a.startswith("Found as Rusty"):
                    rm = re.match(r"Found as (Rusty [\w ]+?)\s*\(", a)
                    if rm:
                        attrs["rusty"] = rm.group(1).strip()
                j += 1
            # a dashes line means the prev line was the next item's name; back up
            if j < len(body) and re.fullmatch(r"-{3,}", body[j].strip()):
                j -= 1
            items.append(attrs)
            i = j
            continue
        i += 1
    return items


def main():
    forged = parse_forge()
    equipment = json.loads((DATA / "equipment.json").read_text(encoding="utf-8"))
    eq_by_name = {norm(e["name"]): e for e in equipment}

    # reset forged_from (idempotent), then re-apply
    for e in equipment:
        e["forged_from"] = []

    matched, unmatched, conflicts = 0, [], []
    for f in forged:
        canon = FORGE_ALIASES.get(f["name"].lower(), f["name"])
        e = eq_by_name.get(norm(canon))
        if e is None:
            unmatched.append(f["name"])
            continue
        matched += 1
        src = f["rusty"] if f["rusty"] else f["material"]
        e["forged_from"] = [src] if src else []
        if "aspartate-forge" not in e["sources"]:
            e["sources"].append("aspartate-forge")
        # corroboration (flag, do not silently change). forge "Worth" == sell price.
        if f["worth"] is not None and e.get("sell_price") not in (None, f["worth"]):
            conflicts.append(f"{f['name']}: worth {f['worth']} vs sell_price {e['sell_price']}")
        if f["unleash"] and e.get("unleash", {}).get("name") and \
                norm(f["unleash"]) != norm(e["unleash"]["name"]):
            conflicts.append(f"{f['name']}: unleash {f['unleash']!r} vs equipment {e['unleash']['name']!r}")

    (DATA / "equipment.json").write_text(json.dumps(equipment, ensure_ascii=False, indent=2) + "\n",
                                         encoding="utf-8")

    print(f"forging_extract_gs2 — parsed {len(forged)} forged items, matched {matched} to equipment")
    print(f"  forged_from set on {sum(1 for e in equipment if e['forged_from'])} equipment rows")
    if unmatched:
        print(f"  unmatched forged names ({len(unmatched)}): {unmatched}")
    if conflicts:
        print(f"  corroboration conflicts ({len(conflicts)}):")
        for c in conflicts:
            print(f"    {c}")
    else:
        print("  corroboration: 0 conflicts (worth/unleash agree with equipment.json)")


if __name__ == "__main__":
    main()
