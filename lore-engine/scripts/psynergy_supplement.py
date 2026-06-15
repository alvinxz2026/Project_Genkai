"""C2: cross-check psynergy.json against 3 new GS1-clean sources -> diff report.

Read-only. Tallies pp_cost / range votes per psynergy across all sources so
conflicts can be resolved by majority (tetzcatlipoca = numeric authority on ties).

New sources:
  super-slash §XII   per-character: Name / PP Cost / Range / Description
  shotgunnova [PSNR] Field/Attack/Status/Medicinal tables: name | PP | R | EFFECT
  bfgamer §8         per-character: Name *NPP |bars Description [djinn-trade code]
                     (the [V]/[M]/[J]/[Me] brackets are djinn-trade codes, NOT element)

Skipped: Various-strawhat (GS2-contaminated, redundant with existing `strawhat`).
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "raw" / "gs1"


def read(name):
    return (RAW / name).read_text(encoding="utf-8", errors="replace").splitlines()


def norm(name):
    return re.sub(r"[^a-z0-9]", "", name.lower())


# known source name variants/typos -> canonical (json) name
TYPO = {"annihalation": "annihilation", "punjipit": "punjitrap", "hpdrain": "drain"}


def norm_range(s):
    s = s.strip().lower()
    if s in ("-", "n/a", "na", "none", "", "--"):
        return None
    # number words first ("One Ally" contains the substring "all" — check words before "all")
    for w, n in {"one": 1, "three": 3, "five": 5, "seven": 7}.items():
        if w in s:
            return n
    m = re.search(r"\d+", s)
    if m:
        return int(m.group())
    if "all" in s:
        return "all"
    return None


# ---------- Super Slash §XII ----------
def parse_superslash():
    lines = read("Various data - Super Slash.txt")
    start = next(i for i, l in enumerate(lines) if l.strip() == "XII. Psynergy")
    end = next(i for i, l in enumerate(lines) if l.strip() == "XIII. Enemies")
    out = {}
    cur = None
    for l in lines[start:end]:
        s = l.strip()
        pm = re.match(r"^PP Cost:\s*(\d+)", s)
        rm = re.match(r"^Range:\s*(.+)$", s)
        if pm and cur:
            out[cur]["pp"] = int(pm.group(1))
        elif rm and cur:
            out[cur]["range"] = norm_range(rm.group(1))
        elif s and not s.startswith(("PP Cost", "Range", "Description", "+", "-", "=")) and re.match(r"^[A-Z][A-Za-z' ]+$", s):
            cur = s
            out.setdefault(cur, {"pp": None, "range": None})
    return out


# ---------- Shotgunnova [PSNR] ----------
def parse_shotgunnova():
    lines = read("Various data - Shotgunnova.txt")
    start = next(i for i, l in enumerate(lines) if l.startswith("PSYNERGY LIST"))
    end = next(i for i, l in enumerate(lines) if i > start and l.startswith("CLASS OVERVIEW"))
    out = {}
    cell = re.compile(r"([A-Za-z][A-Za-z '-]+?)\s*\|\s*(\d{1,2})\s*\|\s*([\d-]+)\s*\|\s*([A-Za-z][A-Za-z ]*?)\s*\|")
    for l in lines[start:end]:
        if "|" not in l:
            continue
        for name, pp, r, eff in cell.findall(l):
            name = name.strip()
            if name.upper() in ("PSYNERGY", "SERIES"):
                continue
            elem = None
            em = re.match(r"(Earth|Fire|Wind|Water) DMG", eff.strip())
            if em:
                elem = {"earth": "earth", "fire": "fire", "wind": "wind", "water": "water"}[em.group(1).lower()]
            rng = norm_range(r)
            if rng == 9:           # Shotgunnova encodes whole-party/all AOE as R=9
                rng = "all"
            out.setdefault(name, []).append({"pp": int(pp), "range": rng, "element": elem})
    return out


# ---------- BFGamer §8 ----------
def parse_bfgamer():
    lines = read("Djinn Items Psynergy - BFGamer.txt")
    start = next(i for i, l in enumerate(lines) if re.search(r"VIII\.\s*Psynergy", l))
    out = {}
    # compact rows: "Name * NPP |bars Description [code]"
    row = re.compile(r"^([A-Za-z][A-Za-z' ]+?)\s+\*?\s*(\d+)PP\s+(\|*)\s+\S")
    # verbose (Everyone): Name / PP: N / Affected: N/A
    cur = None
    for l in lines[start:]:
        s = l.strip()
        m = row.match(s)
        if m:
            name = m.group(1).strip()
            pp = int(m.group(2))
            bars = m.group(3)
            rng = len(bars) if bars else None
            out.setdefault(name, []).append({"pp": pp, "range": rng})
            continue
        # verbose block
        nm = re.match(r"^([A-Z][A-Za-z' ]+)$", s)
        ppm = re.match(r"^PP:\s*(\d+)", s)
        afm = re.match(r"^Affected:\s*(.+)$", s)
        if nm and len(s) < 20:
            cur = s
        elif ppm and cur:
            out.setdefault(cur, []).append({"pp": int(ppm.group(1)), "range": None})
        elif afm and cur and out.get(cur):
            out[cur][-1]["range"] = norm_range(afm.group(1))
    return out


def match(name, by_name, pp_hint=None):
    """match a source name to a json entry, disambiguating dup names by pp."""
    k = TYPO.get(norm(name), norm(name))
    cands = by_name.get(k)
    if not cands:
        return None
    if len(cands) == 1:
        return cands[0]
    if pp_hint is not None:
        return min(cands, key=lambda e: abs((e.get("pp_cost") or 0) - pp_hint))
    return cands[0]


def main():
    P = json.load(open(ROOT / "data/gs1/psynergy.json", encoding="utf-8"))
    by_name = {}
    for p in P:
        by_name.setdefault(norm(p["name"]), []).append(p)

    ss = parse_superslash()
    sh = parse_shotgunnova()
    bf = parse_bfgamer()
    print("source psynergy counts:", {"super-slash": len(ss), "shotgunnova": len(sh), "bfgamer": len(bf)})

    # collect new-source votes onto json entries (by id)
    votes = {p["id"]: {"pp": {}, "range": {}} for p in P}
    unmatched = {"super-slash": [], "shotgunnova": [], "bfgamer": []}

    def add(srcname, entries):
        for nm, recs in entries.items():
            recs = recs if isinstance(recs, list) else [recs]
            for rec in recs:
                e = match(nm, by_name, rec.get("pp"))
                if not e:
                    unmatched[srcname].append(nm)
                    continue
                if rec.get("pp") is not None:
                    votes[e["id"]]["pp"][srcname] = rec["pp"]
                # BFGamer range comes from |bars, which are stylistic for AOE -> not a reliable range vote
                if rec.get("range") is not None and srcname != "bfgamer":
                    votes[e["id"]]["range"][srcname] = rec["range"]

    add("super-slash", ss)
    add("shotgunnova", sh)
    add("bfgamer", bf)

    # report: psynergy where new sources disagree with json, OR existing conflicts
    print("\n=== pp_cost: new-source disagreements with json ===")
    for p in P:
        v = votes[p["id"]]["pp"]
        diff = {s: val for s, val in v.items() if val != p["pp_cost"]}
        if diff:
            print(f"  {p['id']:16} json={p['pp_cost']}  new={diff}  (existing conflict: {'yes' if any(c['field']=='pp_cost' for c in p.get('conflicts',[])) else 'no'})")

    print("\n=== range: new-source disagreements with json ===")
    for p in P:
        v = votes[p["id"]]["range"]
        diff = {s: val for s, val in v.items() if val != p["range"]}
        if diff:
            print(f"  {p['id']:16} json={p['range']}  new={diff}  (existing conflict: {'yes' if any(c['field']=='range' for c in p.get('conflicts',[])) else 'no'})")

    print(f"\n=== unmatched new-source names (GS2/typos, NOT added) ===")
    for s, names in unmatched.items():
        uniq = sorted(set(names))
        print(f"  {s} ({len(uniq)}): {uniq}")


if __name__ == "__main__":
    main()
