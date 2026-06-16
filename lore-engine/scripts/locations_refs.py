"""Build the locations reverse-index materialized view: data/gs1/location_refs.json.

DERIVED data. The source of truth is each entity's own location field
(djinn.location.area, equipment.acquisition.location, monsters.found[],
bosses.encounters[].location, shops.name, items.acquisition.location). This
script resolves those (often dirty) location strings to canonical location ids
using locations.json's `aliases` controlled vocabulary, then materializes the
reverse map location_id -> {djinn, equipment, monsters, bosses, shops, items}.

Rerunnable + byte-stable: no manual data embedded; reads data/gs1/*.json only.
Prints a data-quality report (unmatched strings + zero-ref locations) to stdout.

Usage: python scripts/locations_refs.py
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "gs1"
LOCATIONS = DATA / "locations.json"
OUT = DATA / "location_refs.json"

CATEGORIES = ["djinn", "equipment", "monsters", "bosses", "shops", "items"]

# Raw strings that are intentionally NOT locations -> never report as unmatched.
#   b2/b3        bare floor sub-labels; these monsters already carry "Altin Peak"
#   various ...  game tickets drop from any shop purchase, not a single place
IGNORE = {"[not in game]", "b2", "b3", "various shops / mimics"}


def load(name):
    return json.loads((DATA / name).read_text(encoding="utf-8"))


def normalize(s):
    """lowercase, collapse whitespace, strip trailing punctuation."""
    s = s.strip().lower()
    s = re.sub(r"\s+", " ", s)
    s = s.strip(" .,:;")
    return s


def strip_parens(s):
    """Remove (parenthetical) notes -- they hold monster/shop names, not places."""
    return re.sub(r"\s*\([^)]*\)", "", s).strip()


# --- build resolver from locations.json -------------------------------------

def build_resolver(locations):
    """normalized string -> location id (exact table) + (norm, id) list for
    substring fallback, longest-first so 'Vale Cave' beats 'Vale'."""
    exact = {}
    phrases = []  # (normalized, id)
    for loc in locations:
        lid = loc["id"]
        for label in [loc["name"], *loc.get("aliases", [])]:
            n = normalize(label)
            if n:
                exact.setdefault(n, lid)
                phrases.append((n, lid))
    phrases.sort(key=lambda p: len(p[0]), reverse=True)
    return exact, phrases


def resolve(raw, exact, phrases):
    """Return set of location ids for one raw location string (multi-match)."""
    full = normalize(raw)
    if not full or full in IGNORE:
        return set()
    ids = set()
    # 1) whole-string exact (catches parenthetical aliases like 'world map (near vale)')
    if full in exact:
        ids.add(exact[full])
    # 2) split compound strings, try each piece with and without parentheticals
    pieces = re.split(r"\s*[/;,]\s*|\s+and\s+", raw)
    for piece in pieces:
        for variant in (normalize(piece), normalize(strip_parens(piece))):
            if variant and variant in exact:
                ids.add(exact[variant])
    # 3) substring fallback (word-boundary), only if nothing matched yet
    if not ids:
        for n, lid in phrases:
            if re.search(r"\b" + re.escape(n) + r"\b", full):
                ids.add(lid)
    return ids


# --- collect (entity_id, [location strings]) per source ---------------------

def collect():
    """source category -> list of (entity_id, [raw location strings])."""
    out = {c: [] for c in CATEGORIES}

    for d in load("djinn.json"):
        loc = (d.get("location") or {}).get("area")
        out["djinn"].append((d["id"], [loc] if loc else []))

    for e in load("equipment.json"):
        acq = e.get("acquisition") or {}
        loc = acq.get("location") if isinstance(acq, dict) else None
        out["equipment"].append((e["id"], [loc] if loc else []))

    for m in load("monsters.json"):
        out["monsters"].append((m["id"], list(m.get("found") or [])))

    for b in load("bosses.json"):
        locs = []
        if b.get("location"):
            locs.append(b["location"])
        for enc in b.get("encounters") or []:
            if enc.get("location"):
                locs.append(enc["location"])
        out["bosses"].append((b["id"], locs))

    for s in load("shops.json"):
        out["shops"].append((s["id"], [s["name"]]))

    for it in load("items.json"):
        acq = it.get("acquisition")
        loc = acq.get("location") if isinstance(acq, dict) else None
        out["items"].append((it["id"], [loc] if loc else []))

    return out


def main():
    locations = load("locations.json")
    loc_ids = [loc["id"] for loc in locations]
    exact, phrases = build_resolver(locations)

    refs = {lid: {c: set() for c in CATEGORIES} for lid in loc_ids}
    unmatched = {c: [] for c in CATEGORIES}  # (entity_id, raw_string)
    entities = collect()

    for cat, rows in entities.items():
        for ent_id, raws in rows:
            for raw in raws:
                ids = resolve(raw, exact, phrases)
                if ids:
                    for lid in ids:
                        refs[lid][cat].add(ent_id)
                elif normalize(raw) and normalize(raw) not in IGNORE:
                    unmatched[cat].append((ent_id, raw))

    # materialize (sorted everything for byte-stability)
    materialized = {
        "generated_by": "scripts/locations_refs.py",
        "note": "DERIVED materialized view. Do not hand-edit. Rebuild: python scripts/locations_refs.py",
        "source_files": [f"{c}.json" for c in CATEGORIES],
        "locations": {
            lid: {c: sorted(refs[lid][c]) for c in CATEGORIES}
            for lid in sorted(loc_ids)
        },
    }
    OUT.write_text(json.dumps(materialized, ensure_ascii=False, indent=2) + "\n",
                   encoding="utf-8")

    # --- report ---
    total_unmatched = sum(len(v) for v in unmatched.values())
    print(f"wrote {OUT.relative_to(ROOT)} : {len(loc_ids)} locations")
    print(f"unmatched location strings: {total_unmatched}\n")

    print("ref counts per location:")
    for lid in sorted(loc_ids):
        counts = " ".join(f"{c[:3]}={len(refs[lid][c])}" for c in CATEGORIES)
        print(f"  {lid:20} {counts}")

    zero = [lid for lid in sorted(loc_ids)
            if all(not refs[lid][c] for c in CATEGORIES)]
    print(f"\nzero-ref locations ({len(zero)}): {', '.join(zero) or '-'}")

    if total_unmatched:
        print("\nUNMATCHED (add aliases to locations.json, then rerun):")
        for cat in CATEGORIES:
            for ent_id, raw in unmatched[cat]:
                print(f"  [{cat}] {ent_id}: {raw!r}")


if __name__ == "__main__":
    main()
