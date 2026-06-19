"""Attach telago's per-character djinn-requirement combos onto classes (Layer 3).

classes.json already carries ultimalink-derived element_requirements (a flattened
per-class djinn count) and available_to[].djinn_requirements. Telago's appendix
chapter 26 (`raw/gs2/_chapters/telago/26-class-psynergy-effects.md`) gives an
INDEPENDENT, richer view: per base-element adept, the exact djinn combo to reach
each class WITH ranges (the "x|y" notation, e.g. Knight needs 2|3 Venus). That
range granularity is lost in ultimalink's single number, and it is a second
provenance stream for the same fact.

This deterministic parser reads telago's four adept stat-tables (Venus/Mars/
Jupiter/Mercury Adepts) + the Book Classes table, and appends a telago-sourced
entry to the matching classes.available_to[].djinn_requirements. It does NOT
overwrite ultimalink's — both coexist, each tagged by source (schema rule: flag,
don't silently pick a winner). Semantics differ on purpose: telago lists the
*non-native* djinn to add (a Venus adept shows 0 Venus), ultimalink lists totals;
we store telago's literal combo verbatim.

Disambiguation (class names are not unique — Shaman/Cavalier/... split by element
path): a row is matched to the class entry whose name matches AND whose
element_requirements key-set == {telago's non-zero req elements} ∪ {adept native},
AND that lists the table's character(s) in available_to. The combo attaches only
to those table characters actually in that class.

Idempotent: drops prior source=="telago" djinn_requirements first. Run anytime
(independent of links_normalize).

Usage: python scripts/classes_telago_reqs_gs2.py
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "gs2"
SRC = ROOT / "raw" / "gs2" / "_chapters" / "telago" / "26-class-psynergy-effects.md"

# djinn type column order in telago's "Ven Mar Jup Mer" req cell -> element.
REQ_ELEMS = ["earth", "fire", "wind", "water"]
ADEPT_NATIVE = {"Venus": "earth", "Mars": "fire", "Jupiter": "wind", "Mercury": "water"}


def norm(s):
    return re.sub(r"[^a-z0-9]", "", s.lower())


def parse_val(tok):
    """'0'->None ; '4'->(4,4) ; '2|3'->(2,3)."""
    if tok == "0":
        return None
    if "|" in tok:
        a, b = tok.split("|")
        return int(a), int(b)
    return int(tok), int(tok)


def fmt(parsed):
    out = []
    for p in parsed:
        rng = f"{p['count_min']}|{p['count_max']}" if p["count_min"] != p["count_max"] else f"x{p['count_min']}"
        out.append(f"{p['element']} {rng}")
    return " + ".join(out)


def parse_telago26():
    """Yield dicts: {class, chars, native, parsed, is_book}."""
    rows = []
    chars, native, is_book = None, None, False
    for raw in SRC.read_text(encoding="utf-8").splitlines():
        line = raw.rstrip()
        h = re.match(r"^(Venus|Mars|Jupiter|Mercury) Adepts - (.+?) \(Base Class:", line)
        if h:
            native = ADEPT_NATIVE[h.group(1)]
            chars = [c.strip() for c in re.split(r"[&,]", h.group(2))]
            is_book = False
            continue
        if "All Adepts - Book Classes" in line:
            chars = ["Felix", "Isaac", "Jenna", "Garet", "Sheba", "Ivan", "Piers", "Mia"]
            native, is_book = None, True
            continue
        if chars is None or " | " not in line and "|" not in line:
            continue
        parts = re.split(r"\s+\|\s+", line.strip().rstrip("|").strip())
        if len(parts) < 2 or not re.match(r"^[A-Za-z][A-Za-z' ]*$", parts[0]):
            continue
        cls = parts[0].strip()
        if cls in ("Class",):
            continue
        parsed = []
        if is_book:
            # "<name> | <own> | <o o o> | stats..."  -> N of each non-native element
            if len(parts) < 3:
                continue
            others = re.split(r"\s{2,}", parts[2].strip())
            n = parse_val(others[0]) if others and others[0].isdigit() else None
            if n:
                parsed.append({"element": "other", "count_min": n[0], "count_max": n[1]})
        else:
            # "<name> | Ven Mar Jup Mer | stats..."
            cells = re.split(r"\s{2,}", parts[1].strip())
            if len(cells) != 4:
                continue
            for elem, tok in zip(REQ_ELEMS, cells):
                v = parse_val(tok)
                if v:
                    parsed.append({"element": elem, "count_min": v[0], "count_max": v[1]})
        if parsed or is_book:
            rows.append({"class": cls, "chars": list(chars), "native": native,
                         "parsed": parsed, "is_book": is_book})
    return rows


def main():
    classes = json.loads((DATA / "classes.json").read_text(encoding="utf-8"))
    by_name = {}
    for c in classes:
        by_name.setdefault(norm(c["name"]), []).append(c)

    # idempotency: strip prior telago reqs
    for c in classes:
        for a in c["available_to"]:
            a["djinn_requirements"] = [d for d in a.get("djinn_requirements", [])
                                       if d.get("source") != "telago"]

    rows = parse_telago26()
    attached, unmatched, ambiguous = 0, [], []

    for r in rows:
        cands = [c for c in by_name.get(norm(r["class"]), [])
                 if any(a["character"] in r["chars"] for a in c["available_to"])]
        if not cands:
            unmatched.append((r["class"], r["chars"])); continue
        if len(cands) == 1:
            cls = cands[0]
        else:
            sig = {p["element"] for p in r["parsed"]} | ({r["native"]} if r["native"] else set())
            exact = [c for c in cands
                     if {k for k, v in c["element_requirements"].items() if v} == sig]
            if len(exact) != 1:
                ambiguous.append((r["class"], r["chars"], sig, [c["id"] for c in exact or cands]))
                continue
            cls = exact[0]
        req = {"requirement": fmt(r["parsed"]) + (" (each non-native)" if r["is_book"] and r["parsed"] else "")
               or "base", "parsed": r["parsed"], "source": "telago"}
        for a in cls["available_to"]:
            if a["character"] in r["chars"]:
                a["djinn_requirements"].append(dict(req))
                attached += 1

    (DATA / "classes.json").write_text(json.dumps(classes, ensure_ascii=False, indent=2) + "\n",
                                       encoding="utf-8")
    print(f"classes_telago_reqs_gs2 — parsed {len(rows)} telago rows; attached {attached} "
          f"per-character djinn_requirements")
    if unmatched:
        print(f"  UNMATCHED rows ({len(unmatched)}): {unmatched}")
    if ambiguous:
        print(f"  AMBIGUOUS rows ({len(ambiguous)}):")
        for cls, chars, sig, ids in ambiguous:
            print(f"    {cls} {chars} sig={sig} -> {ids}")
    return 1 if (unmatched or ambiguous) else 0


if __name__ == "__main__":
    sys.exit(main())
