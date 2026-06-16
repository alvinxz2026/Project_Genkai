"""Read-only integrity gate for the GS1 cross-entity link graph.

Validates everything links_normalize.py produced (plus the pre-existing
djinn_id FK and the character natural keys). Writes nothing. Exits non-zero if
any problem is found, so it can serve as a regression check after data edits.

Checks:
  1. id uniqueness within every data file.
  2. FK referential integrity + name<->id consistency:
       classes.psynergy[].id              -> psynergy
       shops.stock[].ref_id (+ref_type)   -> equipment | item
       monsters.drops.items[].ref_id      -> equipment | item
       psynergy.acquired_via_item.item_id -> item
       classes.available_to[].character_id-> character
       monsters.djinn_id                  -> djinn
  3. Character natural keys exist in characters.json:
       equipment.equippable_by[], psynergy.available_to[],
       classes.available_to[].character
  4. djinn_requirements parsed sanity (element enum, min<=max).

Usage: python scripts/links_audit.py
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "gs1"
ELEMENTS = {"earth", "fire", "wind", "water"}


def load(name):
    return json.loads((DATA / name).read_text(encoding="utf-8"))


def norm(s):
    return re.sub(r"[^a-z0-9]", "", s.lower())


def main():
    files = ["djinn", "summons", "classes", "psynergy", "equipment", "items",
             "shops", "monsters", "bosses", "locations", "characters"]
    data = {f: load(f + ".json") for f in files}
    errors = []

    def err(category, ctx, detail):
        errors.append((category, ctx, detail))

    # --- 1. id uniqueness ---
    for f, rows in data.items():
        ids = [r["id"] for r in rows]
        if len(ids) != len(set(ids)):
            dup = sorted({i for i in ids if ids.count(i) > 1})
            err("id-uniqueness", f, f"duplicate ids: {dup}")

    # by-id name lookups
    name_by_id = {f: {r["id"]: r["name"] for r in data[f]} for f in files}
    char_names = {r["name"] for r in data["characters"]}

    def check_fk(category, ctx, ref_id, table, ref_name):
        """ref_id must exist in `table` and its canonical name must match ref_name."""
        if ref_id is None:
            err(category, ctx, f"unresolved (null id) for {ref_name!r}")
            return
        if ref_id not in name_by_id[table]:
            err(category, ctx, f"dangling {table} id {ref_id!r}")
            return
        if norm(name_by_id[table][ref_id]) != norm(ref_name):
            err(category, ctx, f"name/id mismatch: {ref_name!r} -> {ref_id!r} "
                               f"({name_by_id[table][ref_id]!r})")

    # --- 2. FK integrity + name consistency ---
    for c in data["classes"]:
        for p in c["psynergy"]:
            check_fk("classes.psynergy", c["id"], p.get("id"), "psynergy", p["name"])
        for a in c["available_to"]:
            if a.get("character"):
                check_fk("classes.available_to", c["id"], a.get("character_id"),
                         "characters", a["character"])
            for r in a.get("djinn_requirements", []):
                for pr in r.get("parsed", []):
                    if pr["element"] not in ELEMENTS:
                        err("djinn_req.parsed", c["id"], f"bad element {pr['element']!r}")
                    if pr["min"] > pr["max"]:
                        err("djinn_req.parsed", c["id"], f"min>max in {r['requirement']!r}")

    for s in data["shops"]:
        for st in s["stock"]:
            table = "equipment" if st.get("ref_type") == "equipment" else "items"
            if st.get("ref_type") not in ("equipment", "item"):
                err("shops.stock", s["id"], f"bad ref_type {st.get('ref_type')!r} for {st['name']!r}")
            check_fk("shops.stock", s["id"], st.get("ref_id"), table, st["name"])

    for m in data["monsters"]:
        for d in m["drops"].get("items", []):
            table = "equipment" if d.get("ref_type") == "equipment" else "items"
            if d.get("ref_type") not in ("equipment", "item"):
                err("monsters.drops", m["id"], f"bad ref_type {d.get('ref_type')!r} for {d['name']!r}")
            check_fk("monsters.drops", m["id"], d.get("ref_id"), table, d["name"])
        if m.get("djinn_id") is not None and m["djinn_id"] not in name_by_id["djinn"]:
            err("monsters.djinn_id", m["id"], f"dangling djinn id {m['djinn_id']!r}")

    for p in data["psynergy"]:
        acq = p.get("acquired_via_item")
        if acq and acq.get("item"):
            check_fk("psynergy.acquired_via_item", p["id"], acq.get("item_id"),
                     "items", acq["item"])
        for ch in p.get("available_to", []):
            if ch not in char_names:
                err("psynergy.available_to", p["id"], f"unknown character {ch!r}")

    # --- 3. character natural keys ---
    for e in data["equipment"]:
        for ch in (e.get("equippable_by") or []):
            if ch not in char_names:
                err("equipment.equippable_by", e["id"], f"unknown character {ch!r}")

    # --- report ---
    print(f"links_audit — checked {sum(len(v) for v in data.values())} rows across {len(files)} files")
    if not errors:
        print("  OK — 0 errors. All FKs resolve, names consistent, ids unique.")
        return 0
    print(f"  {len(errors)} ERROR(S):")
    for cat, ctx, detail in errors:
        print(f"    [{cat}] {ctx}: {detail}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
