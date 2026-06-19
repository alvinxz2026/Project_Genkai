"""Read-only integrity gate for the GS2 cross-entity link graph.

GS2 analog of links_audit.py. Validates everything links_normalize_gs2.py
produced. Writes nothing. Exits non-zero on any ERROR, so it can serve as a
regression check after data edits.

Unlike GS1 (where any unresolved FK is an error), GS2's psynergy.json is a
deliberately non-exhaustive canonical set and items.json omits shared/deferred
consumables. So a NULL id whose name is legitimately absent from the target
table is EXPECTED (a known gap), reported as a warning, not an error. A null id
whose name IS present in the target (i.e. should have resolved) is an error.

Checks:
  1. id uniqueness within every data file.
  2. FK referential integrity + name<->id consistency:
       classes.psynergy[].id            -> psynergy (null OK iff name absent)
       monsters.drops.items[].ref_id     -> equipment | item (null OK iff absent)
       monsters.djinn_id                 -> djinn (must resolve for djinn enemies)
       monsters.boss_id                  -> bosses (must resolve for bosses)
       classes.available_to[].character_id -> characters
  3. Character natural keys exist in characters.json:
       equipment.equippable_by[], psynergy.available_to[] (if present),
       classes.available_to[].character

Usage: python scripts/links_audit_gs2.py
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "gs2"


def load(name):
    return json.loads((DATA / name).read_text(encoding="utf-8"))


def norm(s):
    return re.sub(r"[^a-z0-9]", "", s.lower())


# Must mirror links_normalize_gs2.ALIASES: ultimalink typos that resolve onto a
# unique canonical psynergy. The classes.psynergy[].name stays the source typo
# while .id is the corrected resolution, so the audit applies the alias before
# comparing name<->id.
ALIASES = {
    "frezze prism": "freeze prism",
    "flare strom": "flare storm",
    "strom ray": "storm ray",
    "high imapct": "high impact",
    "drian": "drain",
}


def main():
    files = ["monsters", "equipment", "items", "bosses", "djinn", "summons",
             "characters", "classes", "psynergy", "shops"]
    data = {f: load(f + ".json") for f in files}
    errors = []
    warnings = []

    def err(category, ctx, detail):
        errors.append((category, ctx, detail))

    def warn(category, ctx, detail):
        warnings.append((category, ctx, detail))

    # --- 1. id uniqueness ---
    for f, rows in data.items():
        ids = [r["id"] for r in rows]
        if len(ids) != len(set(ids)):
            dup = sorted({i for i in ids if ids.count(i) > 1})
            err("id-uniqueness", f, f"duplicate ids: {dup}")

    name_by_id = {f: {r["id"]: r["name"] for r in data[f]} for f in files}
    char_names = {r["name"] for r in data["characters"]}
    # normalized name presence in each target table (to judge expected vs error)
    has_name = {f: {norm(r["name"]) for r in data[f]} for f in files}
    # psynergy: normalized name -> [ids] (one name can map to >1, e.g. "Blast")
    ps_by_name = {}
    for p in data["psynergy"]:
        ps_by_name.setdefault(norm(p["name"]), []).append(p["id"])

    def check_psynergy(ctx, ref_id, ref_name):
        """classes.psynergy edge: alias- and ambiguity-aware.
        null id is expected (warning) when the name is absent or ambiguous in
        canonical; an error only when exactly one canonical match should have
        resolved. A resolved id is validated against the (aliased) target name."""
        target = norm(ALIASES.get(ref_name.lower(), ref_name))
        cands = ps_by_name.get(target, [])
        if ref_id is None:
            if len(cands) == 1:
                err("classes.psynergy", ctx, f"unresolved but psynergy has {ref_name!r}")
            elif len(cands) > 1:
                warn("classes.psynergy", ctx, f"{ref_name!r} ambiguous in psynergy (expected)")
            else:
                warn("classes.psynergy", ctx, f"{ref_name!r} class-only, not in canonical (expected)")
            return
        if ref_id not in name_by_id["psynergy"]:
            err("classes.psynergy", ctx, f"dangling psynergy id {ref_id!r}")
        elif norm(name_by_id["psynergy"][ref_id]) != target:
            err("classes.psynergy", ctx,
                f"name/id mismatch: {ref_name!r} -> {ref_id!r} ({name_by_id['psynergy'][ref_id]!r})")

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
            check_psynergy(c["id"], p.get("id"), p["name"])
        for a in c["available_to"]:
            if a.get("character"):
                check_fk("classes.available_to", c["id"], a.get("character_id"),
                         "characters", a["character"])

    for m in data["monsters"]:
        for d in m["drops"].get("items", []):
            table = "equipment" if d.get("ref_type") == "equipment" else "items"
            if d.get("ref_id") is not None and d.get("ref_type") not in ("equipment", "item"):
                err("monsters.drops", m["id"], f"bad ref_type {d.get('ref_type')!r} for {d['name']!r}")
            # drop resolves to equipment OR item; lenient against whichever table
            # the (possibly null) ref points at, but expected-gap test must allow
            # absence from BOTH tables.
            if d.get("ref_id") is None:
                if norm(d["name"]) in has_name["equipment"] or norm(d["name"]) in has_name["items"]:
                    err("monsters.drops", m["id"], f"unresolved but gear has {d['name']!r}")
                else:
                    warn("monsters.drops", m["id"], f"{d['name']!r} absent from gs2 gear (shared/deferred)")
            else:
                check_fk("monsters.drops", m["id"], d["ref_id"], table, d["name"])
        if m.get("is_djinn_enemy"):
            if m.get("djinn_id") is None or m["djinn_id"] not in name_by_id["djinn"]:
                err("monsters.djinn_id", m["id"], f"djinn enemy unresolved/dangling: {m.get('djinn_id')!r}")
        if m.get("is_boss"):
            if m.get("boss_id") is None or m["boss_id"] not in name_by_id["bosses"]:
                err("monsters.boss_id", m["id"], f"boss unresolved/dangling: {m.get('boss_id')!r}")

    for s in data["shops"]:
        for st in s["stock"]:
            table = "equipment" if st.get("ref_type") == "equipment" else "items"
            if st.get("ref_id") is not None and st.get("ref_type") not in ("equipment", "item"):
                err("shops.stock", s["id"], f"bad ref_type {st.get('ref_type')!r} for {st['name']!r}")
            if st.get("ref_id") is None:
                if norm(st["name"]) in has_name["equipment"] or norm(st["name"]) in has_name["items"]:
                    err("shops.stock", s["id"], f"unresolved but gear has {st['name']!r}")
                else:
                    warn("shops.stock", s["id"], f"{st['name']!r} absent from gs2 gear (shared basic gear deferred)")
            else:
                check_fk("shops.stock", s["id"], st["ref_id"], table, st["name"])

    # --- 3. character natural keys ---
    for e in data["equipment"]:
        for ch in (e.get("equippable_by") or []):
            if ch not in char_names:
                err("equipment.equippable_by", e["id"], f"unknown character {ch!r}")
    for p in data["psynergy"]:
        for ch in p.get("available_to", []) or []:
            if isinstance(ch, str) and ch not in char_names:
                err("psynergy.available_to", p["id"], f"unknown character {ch!r}")

    # --- report ---
    print(f"links_audit_gs2 — checked {sum(len(v) for v in data.values())} rows across {len(files)} files")
    if warnings:
        from collections import Counter
        by = Counter((cat, detail) for cat, ctx, detail in warnings)
        print(f"  expected gaps (warnings)   : {len(warnings)} refs, {len(by)} distinct")
    if not errors:
        print("  OK — 0 errors. All required FKs resolve, names consistent, ids unique.")
        return 0
    print(f"  {len(errors)} ERROR(S):")
    for cat, ctx, detail in errors:
        print(f"    [{cat}] {ctx}: {detail}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
