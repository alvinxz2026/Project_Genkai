"""Backfill resolved foreign-key ids onto cross-entity references.

The source of truth stays the human-readable `name`; this adds an authoritative
resolved id next to it (id = link of record, name = readable, kept in sync).
In-place + idempotent: resolves from name and rewrites the id each run, so it is
safe to re-run after any entity (re)generation (it must run AFTER, as a final
enrichment pass).

E2a edges:
  classes.psynergy[]              += id                 -> psynergy.json
                                                          ("Blast" disambiguated by series-mates)
  shops.stock[]                   += ref_type, ref_id   -> equipment.json | items.json
  monsters.drops.items[]          += ref_type, ref_id   -> equipment.json | items.json

E2b edges:
  psynergy.acquired_via_item      += item_id            -> items.json
  classes.available_to[]          += character_id       -> characters.json
  classes.available_to[].djinn_requirements[] += parsed -> [{element, min, max}]

Character references in equipment.equippable_by / psynergy.available_to are left as
names (natural keys); links_audit.py validates them against characters.json.

Prints an unresolved report; exits non-zero if any FK fails to resolve.
Usage: python scripts/links_normalize.py
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "gs1"


def load(name):
    return json.loads((DATA / name).read_text(encoding="utf-8"))


def save(name, obj):
    (DATA / name).write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n",
                             encoding="utf-8")


def norm(s):
    return re.sub(r"[^a-z0-9]", "", s.lower())


# Djinn element names appear as either the element (Earth/Fire/Wind/Water) or the
# Djinn type (Venus/Mars/Jupiter/Mercury); normalize both to the element.
ELEM_ALIAS = {
    "earth": "earth", "venus": "earth", "fire": "fire", "mars": "fire",
    "wind": "wind", "jupiter": "wind", "air": "wind", "water": "water",
    "mercury": "water",
}


def parse_djinn_req(text):
    """'1 Earth, 6 Fire Djinn' -> [{element:earth,min:1,max:1},
    {element:fire,min:6,max:6}]. '0-1 Venus Djinn' -> [{earth,0,1}].
    Strips '(... tier group)' notes. [] if nothing element-shaped is found."""
    t = re.sub(r"\([^)]*\)", "", text)
    out = []
    for m in re.finditer(
            r"(\d+)(?:\s*-\s*(\d+))?\s+(earth|fire|wind|water|air|venus|mars|jupiter|mercury)",
            t, re.I):
        lo = int(m.group(1))
        hi = int(m.group(2)) if m.group(2) else lo
        out.append({"element": ELEM_ALIAS[m.group(3).lower()], "min": lo, "max": hi})
    return out


def reinsert(entry, after_key, new_fields):
    """Return a new dict with new_fields placed right after after_key.
    Drops any pre-existing copies of those keys first (idempotent re-run)."""
    out = {}
    for k, v in entry.items():
        if k in new_fields:
            continue  # will be re-added in the right place
        out[k] = v
        if k == after_key:
            for nk, nv in new_fields.items():
                out[nk] = nv
    return out


def main():
    psynergy = load("psynergy.json")
    equipment = load("equipment.json")
    items = load("items.json")
    classes = load("classes.json")
    shops = load("shops.json")
    monsters = load("monsters.json")
    characters = load("characters.json")

    # --- resolver tables ---
    item_by_name = {norm(i["name"]): i["id"] for i in items}
    char_by_name = {norm(c["name"]): c["id"] for c in characters}
    # psynergy: name -> [entries] (one name can map to >1, e.g. "Blast")
    ps_by_name = {}
    for p in psynergy:
        ps_by_name.setdefault(norm(p["name"]), []).append(p)
    # series -> set of member normalized-names (for disambiguation)
    series_members = {}
    for p in psynergy:
        if p.get("series"):
            series_members.setdefault(p["series"], set()).add(norm(p["name"]))

    # gear: name -> (ref_type, id). equipment and items names are disjoint (verified).
    gear = {}
    for e in equipment:
        gear[norm(e["name"])] = ("equipment", e["id"])
    for i in items:
        gear[norm(i["name"])] = ("item", i["id"])

    unresolved = []  # (edge, context, raw_name, reason)  -> exit non-zero
    warnings = []    # (kind, context, text)               -> printed, not fatal

    # --- edge 1: classes.psynergy[] -> psynergy id ---
    for c in classes:
        class_pnames = {norm(p["name"]) for p in c["psynergy"]}
        new_list = []
        for p in c["psynergy"]:
            cands = ps_by_name.get(norm(p["name"]), [])
            pid = None
            if len(cands) == 1:
                pid = cands[0]["id"]
            elif len(cands) > 1:
                # disambiguate: pick the candidate whose series has another
                # member also listed in this class.
                matches = []
                for cand in cands:
                    sibs = series_members.get(cand.get("series"), set()) - {norm(p["name"])}
                    if sibs & class_pnames:
                        matches.append(cand)
                if len(matches) == 1:
                    pid = matches[0]["id"]
            if pid is None:
                unresolved.append(("classes.psynergy", c["id"], p["name"],
                                   "no match" if not cands else "ambiguous"))
            new_list.append(reinsert(p, "name", {"id": pid}))
        c["psynergy"] = new_list

    # --- edge 2: shops.stock[] -> equipment|item ---
    for s in shops:
        new_stock = []
        for st in s["stock"]:
            hit = gear.get(norm(st["name"]))
            if hit is None:
                unresolved.append(("shops.stock", s["id"], st["name"], "no match"))
                rt, rid = None, None
            else:
                rt, rid = hit
            new_stock.append(reinsert(st, "name", {"ref_type": rt, "ref_id": rid}))
        s["stock"] = new_stock

    # --- edge 3: monsters.drops.items[] -> equipment|item ---
    for m in monsters:
        new_items = []
        for d in m["drops"].get("items", []):
            hit = gear.get(norm(d["name"]))
            if hit is None:
                unresolved.append(("monsters.drops", m["id"], d["name"], "no match"))
                rt, rid = None, None
            else:
                rt, rid = hit
            new_items.append(reinsert(d, "name", {"ref_type": rt, "ref_id": rid}))
        m["drops"]["items"] = new_items

    # --- edge 4: psynergy.acquired_via_item -> item id ---
    for p in psynergy:
        acq = p.get("acquired_via_item")
        if not acq or not acq.get("item"):
            continue
        iid = item_by_name.get(norm(acq["item"]))
        if iid is None:
            unresolved.append(("psynergy.acquired_via_item", p["id"], acq["item"], "no match"))
        p["acquired_via_item"] = reinsert(acq, "item", {"item_id": iid})

    # --- edge 5: classes.available_to character_id + djinn_requirements parsing ---
    n_req = n_req_empty = 0
    for c in classes:
        new_av = []
        for a in c["available_to"]:
            cid = char_by_name.get(norm(a["character"])) if a.get("character") else None
            if a.get("character") and cid is None:
                unresolved.append(("classes.available_to", c["id"], a["character"], "no match"))
            new_reqs = []
            for r in a.get("djinn_requirements", []):
                n_req += 1
                # terence rows carry authoritative full 4-element `parsed`
                # (written by build_terence_class_reqs.py); the prose parser is
                # lossy for "Earth 0-2, ..." form, so keep them verbatim.
                if r.get("source") == "terence" and r.get("parsed"):
                    new_reqs.append(r)
                    continue
                parsed = parse_djinn_req(r["requirement"])
                if not parsed:
                    n_req_empty += 1
                    warnings.append(("djinn_requirement", c["id"], r["requirement"]))
                new_reqs.append(reinsert(r, "requirement", {"parsed": parsed}))
            a = dict(a)
            a["djinn_requirements"] = new_reqs
            new_av.append(reinsert(a, "character", {"character_id": cid}))
        c["available_to"] = new_av

    save("classes.json", classes)
    save("shops.json", shops)
    save("monsters.json", monsters)
    save("psynergy.json", psynergy)

    # --- report ---
    n_ps = sum(len(c["psynergy"]) for c in classes)
    n_shop = sum(len(s["stock"]) for s in shops)
    n_drop = sum(len(m["drops"].get("items", [])) for m in monsters)
    n_acq = sum(1 for p in psynergy if p.get("acquired_via_item"))
    n_av = sum(len(c["available_to"]) for c in classes)
    print("links_normalize — wrote classes.json, shops.json, monsters.json, psynergy.json")
    print(f"  classes.psynergy refs      : {n_ps}")
    print(f"  shops.stock refs           : {n_shop}")
    print(f"  monsters.drops refs        : {n_drop}")
    print(f"  psynergy.acquired_via_item : {n_acq}")
    print(f"  classes.available_to       : {n_av}")
    print(f"  djinn_requirements parsed  : {n_req - n_req_empty}/{n_req}")
    print(f"  unresolved                 : {len(unresolved)}")
    for edge, ctx, name, reason in unresolved:
        print(f"    [{edge}] {ctx}: {name!r} ({reason})")
    if warnings:
        print(f"  warnings (non-fatal)       : {len(warnings)}")
        for kind, ctx, text in warnings:
            print(f"    [{kind}] {ctx}: {text!r}")

    return 1 if unresolved else 0


if __name__ == "__main__":
    sys.exit(main())
