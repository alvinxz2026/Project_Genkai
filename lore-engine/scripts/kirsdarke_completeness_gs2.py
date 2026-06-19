"""Completeness cross-check: 90Kirsdarke item-code table vs our equipment+items.

`90Kirsdarke` (Item Djinn Hacking Guide) carries the game's COMPLETE item table
as `HH - Name` hex-code rows in two banks (Items+00 = base/shared set, Items+01 =
TLA-native set), grouped by section banner (Weapons / Armor / Minor Items /
Psyenergy Items / Key Items / Class Items / Forge / Trident). That makes it a
deterministic completeness backstop: diff its full name list against our
equipment.json + items.json by normalized name to surface
  - THEIRS-NOT-OURS = coverage gaps (the deferred shared set, plus any gs2 item
    we genuinely missed — e.g. the Psynergy/key items absent from items.json);
  - OURS-NOT-THEIRS = our names with no code-table match (possible over-extraction
    or a spelling drift on either side).

NOTE the hex codes are NOT a usable canonical id for us: our `debug_no`
(mr-unorigino) uses a different numbering, so we diff by NAME only. The djinn
section of this source is memory-address hacking, not a djinn name list, so djinn
completeness is out of scope here (use demooni, already the djinn authority).

We do NOT silently fix names; the author has many misspellings ("Psyenergy",
"Festive Coat", "Saftey Boots", "Beserker Band"). `THEIRS_ALIASES` maps a few of
his consistent typos onto our canonical names so they don't show as false gaps;
everything else is reported for a human look. Report-only; writes a materialized
parse to intermediate/ for inspection.

Usage: python scripts/kirsdarke_completeness_gs2.py
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "gs2"
SRC = ROOT / "raw" / "gs2" / "In-Depth Guides" / "Item Djinn Hacking Guide by 90Kirsdarke.md"
OUT = DATA / "intermediate" / "kirsdarke_item_codes.json"

# section banners that head the columned code blocks
SECTIONS = {
    "Weapons", "Armor", "Minor Items", "Psyenergy Items", "Key Items",
    "Class Items", "Forge Weapons", "Forge Materials", "Trident",
    "Key Items (cont)",
}

# 90Kirsdarke's consistent misspellings -> our canonical name (verified by eye).
# Only obvious 1:1 author typos; keeps them from showing as false coverage gaps.
THEIRS_ALIASES = {
    "psyenergy rod": "psynergy rod",
    "psyenergy armor": "psynergy armor",
    "festive coat": "festival coat",
}

# one `HH - Name` cell; names can hold ' . ( ) and digits
CELL_RE = re.compile(r"\b([0-9A-Fa-f]{2})\s+-\s+([A-Za-z][A-Za-z0-9'.()/ +]*?)\s*(?=$|[0-9A-Fa-f]{2}\s+-\s)")


def norm(s):
    return re.sub(r"[^a-z0-9]", "", s.lower())


def parse_source():
    """Walk the Item Values tables, return list of {bank, section, code, name}."""
    lines = SRC.read_text(encoding="utf-8").splitlines()
    out = []
    bank = None
    section = None
    in_items = False
    for ln in lines:
        s = ln.strip()
        m = re.match(r"Items \+ (\d\d)", s)
        if m:
            bank, in_items = m.group(1), True
            continue
        if s.startswith("1.1 Djinn") or s.startswith("1.11"):
            in_items = False  # leave the item tables
        if not in_items:
            continue
        if s in SECTIONS:
            section = s
            continue
        for code, name in CELL_RE.findall(ln):
            name = name.strip()
            if name:
                out.append({"bank": bank, "section": section,
                            "code": code.upper(), "name": name})
    return out


def main():
    rows = parse_source()
    # de-dupe by (bank, code) keeping name; rusty variants share a name legitimately
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(json.dumps(rows, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    equipment = json.loads((DATA / "equipment.json").read_text(encoding="utf-8"))
    items = json.loads((DATA / "items.json").read_text(encoding="utf-8"))
    ours = {}
    for e in equipment:
        ours[norm(e["name"])] = ("equipment", e["name"])
    for i in items:
        ours[norm(i["name"])] = ("item", i["name"])

    theirs = {}  # norm name -> row (first seen)
    for r in rows:
        key = norm(THEIRS_ALIASES.get(r["name"].lower(), r["name"]))
        theirs.setdefault(key, r)

    theirs_not_ours = [r for k, r in theirs.items() if k not in ours]
    ours_keys = set(ours)
    matched = sum(1 for k in theirs if k in ours_keys)
    ours_not_theirs = [(ours[k][0], ours[k][1]) for k in ours_keys if k not in theirs]

    print(f"parsed {len(rows)} code rows -> {len(theirs)} distinct names "
          f"(wrote {OUT.relative_to(ROOT)})")
    print(f"ours: {len(ours)} (equipment {len(equipment)} + items {len(items)})")
    print(f"matched (theirs ∩ ours): {matched}/{len(theirs)}\n")

    # THEIRS-NOT-OURS, grouped by section so the gap is structured/actionable
    print(f"=== THEIRS-NOT-OURS — completeness gaps: {len(theirs_not_ours)} ===")
    by_sec = {}
    for r in theirs_not_ours:
        by_sec.setdefault((r["bank"], r["section"]), []).append(r["name"])
    for (bank, sec), names in sorted(by_sec.items(), key=lambda x: (x[0][0] or "", x[0][1] or "")):
        print(f"  [+{bank} / {sec}] {len(names)}: {', '.join(sorted(names))}")

    # OURS-NOT-THEIRS, with a near-match hint (likely author typo vs real)
    print(f"\n=== OURS-NOT-THEIRS — our names with no code-table match: {len(ours_not_theirs)} ===")
    their_norms = list(theirs)
    for rt, name in sorted(ours_not_theirs):
        n = norm(name)
        near = [theirs[k]["name"] for k in their_norms
                if (n[:6] in k or k[:6] in n) and abs(len(k) - len(n)) <= 3][:3]
        hint = f"  ~near: {near}" if near else ""
        print(f"  [{rt}] {name!r}{hint}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
