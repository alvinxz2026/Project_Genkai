"""C3: cross-check / fill class stat_multiplier from Telago §3 + ElectroSpecter §7.

Read-only diff report. Both sources give the full 6-stat % per class (per
character, with Djinn requirement for element disambiguation). Only 15 of 76
json classes currently have stat_multiplier (from aku-chi); the rest can be
filled from these two corroborating sources.

Match key: (character, class display name) + element disambiguation (from the
source's Djinn requirement) when several json entries share a name.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "raw" / "gs1"

ELEM = {"venus": "earth", "mars": "fire", "jupiter": "wind", "mercury": "water"}
CHARS = {"issac": "Isaac", "isaac": "Isaac", "garet": "Garet", "ivan": "Ivan",
         "mia": "Mia", "jenna": "Jenna"}
STATK = ["hp", "pp", "atk", "def", "agi", "lck"]


def read(name):
    return (RAW / name).read_text(encoding="utf-8", errors="replace").splitlines()


def norm(s):
    return re.sub(r"[^a-z0-9]", "", s.lower())


def pct(v):
    v = v.strip().replace("%", "")
    if v in ("-", ""):
        return 100
    return int(v)


def dominant_element(djinn_text):
    """element of the class from its Djinn requirement text."""
    t = djinn_text.lower()
    # prefer the element with the largest count; ties -> first mentioned
    best, bestn = None, -1
    for word, el in ELEM.items():
        for m in re.finditer(rf"(\d+)\s*{word}", t):
            n = int(m.group(1))
            if n > bestn:
                best, bestn = el, n
    # Telago column form "Ven Mar Jup Mer" handled separately
    return best


# ---------- ElectroSpecter §7 ----------
def parse_electrospecter():
    lines = read("Classes Djinn Weapons Armor Equipment - ElectroSpecter.txt")
    start = next(i for i, l in enumerate(lines) if re.search(r"7\. Classes", l))
    end = next(i for i, l in enumerate(lines) if i > start and re.match(r"^\\ \d+\.", l))
    out = []
    char = None
    for l in lines[start:end]:
        s = l.strip()
        hm = re.match(r"^\|\s*([A-Z]{3,})\s*\|$", s)
        if hm and norm(hm.group(1)) in CHARS:
            char = CHARS[norm(hm.group(1))]
            continue
        # data row: | Class | h% | p% | a% | d% | g% | l% | Djinn |
        cells = [c.strip() for c in s.split("|")][1:-1]
        if len(cells) == 8 and char and re.search(r"%", s) and re.match(r"^[A-Za-z]", cells[0]):
            name = re.sub(r"\s*\(\d+\)$", "", cells[0]).strip()  # "Shaman (1)" -> "Shaman"
            stats = {k: pct(cells[i + 1]) for i, k in enumerate(STATK)}
            out.append({"char": char, "name": name, "element": dominant_element(cells[7]),
                        "djinn": cells[7], "stats": stats})
    return out


# ---------- Shotgunnova [CLSS] ----------
def parse_shotgunnova():
    lines = read("Various data - Shotgunnova.txt")
    start = next(i for i, l in enumerate(lines) if l.startswith("CLASS OVERVIEW"))
    end = next(i for i, l in enumerate(lines) if i > start and l.startswith("DJINN LIST"))
    out = []
    char = None
    for l in lines[start:end]:
        s = l.strip()
        hm = re.search(r"\|\s*([A-Z]{3,})\s+CLASS\s*\|", s)
        if hm and norm(hm.group(1)) in CHARS:
            char = CHARS[norm(hm.group(1))]
            continue
        cells = [c.strip() for c in s.split("|")][1:-1]
        # | name | ERT FIR WIN WAT | HP% PP% ATK% DEF% AGL% LCK% |
        if len(cells) == 3 and char and "%" in s and re.match(r"^[A-Za-z]", cells[0]):
            name = cells[0].strip()
            dj = cells[1].split()  # ERT FIR WIN WAT, "---" = 0
            counts = [int(x) if x.isdigit() else 0 for x in dj[:4]]
            order = ["earth", "fire", "wind", "water"]
            el = order[counts.index(max(counts))] if max(counts) > 0 else None
            pcts = re.findall(r"(\d+)%", cells[2])
            if len(pcts) != 6:
                continue
            stats = {k: int(pcts[i]) for i, k in enumerate(STATK)}
            out.append({"char": char, "name": name, "element": el, "djinn": cells[1], "stats": stats})
    return out


# ---------- FandomWiki class table ----------
def parse_fandomwiki():
    """The Golden Sun Wiki generic high-tier class table (20 rows -> 18 distinct
    names). No character axis: each row's stat% applies to every json entry that
    shares the class name. Conjurer (Venus/Mars) and Druid (Jupiter/Mercury)
    variants carry identical stats, so a name->stats map is unambiguous.
    Authoritative (wiki, data-derived); returns {norm(name): stats}.
    """
    lines = read("Class - FandomWiki")
    out = {}
    for l in lines[2:]:  # skip "Golden Sun" + header row
        cells = [c.strip() for c in l.split("\t")]
        if len(cells) < 7 or not re.match(r"^[A-Za-z]", cells[0]):
            continue
        name = re.sub(r"\s*\(.*\)$", "", cells[0]).strip()  # drop "(Venus Adept)"
        out[norm(name)] = {k: pct(cells[i + 1]) for i, k in enumerate(STATK)}
    return out


# ---------- Telago §3 ----------
def parse_telago():
    lines = read("Djinn Class Items Phynergy - Telago.txt")
    start = next(i for i, l in enumerate(lines) if "3. Class & Psynergy Effects" in l)
    end = next((i for i, l in enumerate(lines) if i > start + 5 and "Appendix" in l), len(lines))
    out = []
    char = None
    for l in lines[start:end]:
        s = l.strip()
        hm = re.match(r"^(Isaac|Garet|Ivan|Mia|Jenna)\s+-\s+", s)
        if hm:
            char = hm.group(1)
            continue
        # row: Class | Ven Mar Jup Mer | HP | PP | Att | Def | Agl | Lck |
        if "|" not in s or char is None:
            continue
        parts = [p.strip() for p in s.split("|")]
        if len(parts) < 8 or not re.match(r"^[A-Za-z]", parts[0]):
            continue
        name = re.sub(r"\*$", "", parts[0]).strip()
        if name.lower() in ("class", ""):
            continue
        djc = parts[1].split()  # Ven Mar Jup Mer counts
        stat_cells = parts[2:8]
        if len(stat_cells) != 6 or not all(re.match(r"^[\d%-]+$", c.replace("%", "") or "-") for c in stat_cells):
            continue
        # element from nonzero djinn column
        el = None
        try:
            counts = [int(re.sub(r"\D", "", x) or 0) for x in djc[:4]]
            order = ["earth", "fire", "wind", "water"]
            el = order[counts.index(max(counts))] if max(counts) > 0 else None
        except Exception:
            pass
        out.append({"char": char, "name": name, "element": el,
                    "djinn": parts[1], "stats": {k: pct(stat_cells[i]) for i, k in enumerate(STATK)}})
    return out


def build_index(C):
    idx = {}
    for c in C:
        for a in c["available_to"]:
            idx.setdefault((a["character"], norm(c["name"])), []).append(c)
    return idx


def entry_element(c):
    m = re.match(r"^(earth|fire|wind|water)-", c["id"])
    if m:
        return m.group(1)
    if c.get("qualified_name"):
        qm = re.search(r"\((Earth|Fire|Wind|Water)\)", c["qualified_name"])
        if qm:
            return qm.group(1).lower()
    return None


def match(rec, idx):
    cands = idx.get((rec["char"], norm(rec["name"])), [])
    if len(cands) <= 1:
        return cands[0] if cands else None
    for c in cands:
        if entry_element(c) == rec["element"]:
            return c
    return None  # ambiguous


def main():
    C = json.load(open(ROOT / "data/gs1/classes.json", encoding="utf-8"))
    idx = build_index(C)
    el = parse_electrospecter()
    sh = parse_shotgunnova()
    # Telago §3 dropped: element-adept shared sections + "x|y" pipes make it unreliable.
    print(f"parsed: electrospecter={len(el)} rows, shotgunnova={len(sh)} rows")

    got = {c["id"]: {"electrospecter": None, "shotgunnova": None} for c in C}
    unmatched = {"electrospecter": [], "shotgunnova": []}
    for src, rows in (("electrospecter", el), ("shotgunnova", sh)):
        for r in rows:
            m = match(r, idx)
            if m:
                got[m["id"]][src] = r["stats"]
            else:
                unmatched[src].append((r["char"], r["name"], r["element"]))

    have_json = {c["id"]: c.get("stat_multiplier") for c in C}
    fillable = covered = 0
    mism_list = []
    for c in C:
        g = got[c["id"]]
        any_new = g["electrospecter"] or g["shotgunnova"]
        if any_new:
            covered += 1
        if any_new and not have_json[c["id"]]:
            fillable += 1
        vals = {"electrospecter": g["electrospecter"], "shotgunnova": g["shotgunnova"],
                "aku-chi": have_json[c["id"]]}
        present = {k: v for k, v in vals.items() if v}
        if len(present) >= 2 and any(v != list(present.values())[0] for v in present.values()):
            mism_list.append((c["id"], present))

    print(f"\njson classes: {len(C)} | currently have stat%: {sum(bool(v) for v in have_json.values())}")
    print(f"covered by new sources: {covered} | newly fillable (had none): {fillable}")
    still = [c["id"] for c in C if not have_json[c["id"]] and not (got[c["id"]]["electrospecter"] or got[c["id"]]["shotgunnova"])]
    print(f"json entries STILL without stat% after fill: {len(still)} -> {still}")

    print(f"\ncross-check disagreements (per stat, with majority): {len(mism_list)}")
    for cid, present in mism_list:
        for k in STATK:
            vs = {n: d[k] for n, d in present.items()}
            if len(set(vs.values())) > 1:
                from collections import Counter
                maj = Counter(vs.values()).most_common(1)[0]
                print(f"  {cid:18} {k}: {vs}  -> majority {maj[0]} (×{maj[1]})")

    print(f"\nunmatched source rows: " + ", ".join(f"{s}={len(u)}" for s, u in unmatched.items()))
    for s, u in unmatched.items():
        for x in u[:15]:
            print(f"  [{s}] {x}")


if __name__ == "__main__":
    main()
