"""Round-2 cross-check: In-Depth data-table/guide placement vs walkthrough placement.

The original cross-check question (user task 2/3): our entity data came from the
In-Depth Guides (torrentlord bestiary, demooni djinn, cooldude summons), and the
consolidated 2a walkthrough is an *independent* provenance stream. Do the two
agree on WHERE things are? This compares, per entity, the In-Depth location claim
against the walkthrough's `locations.json` placement (via `location_refs.json`'s
resolved inverse index), entirely deterministically (no LLM, free, re-runnable).

Streams compared (In-Depth source  vs  walkthrough):
  bosses    monsters.json boss stat-line `found`   vs  locations.bosses_here
  djinn     djinn.json    location.description prose vs  locations.djinn_here
  summons   summons.json  acquisition.found_at prose vs  locations.summons_here
  monsters  monsters.json `found`                   vs  locations.monsters_here

Output buckets per entity:
  AGREE            : In-Depth and walkthrough share >=1 region   (corroboration)
  WALKTHROUGH-ONLY : walkthrough places it in a region In-Depth omits -> a FINDING
                     (possible walkthrough error, or In-Depth incompleteness)
  INDEPTH-ONLY     : In-Depth places it where walkthrough doesn't mention it
                     -> mostly EXPECTED (walkthrough prose is curated/incomplete)

IMPORTANT — this is SOFT signal, not crisp bugs. Two big confounders are labelled,
not silently dropped: (1) recurring/ambush monsters (Mimic, Mad Plant) whose
single bestiary `found` can't cover every chest/respawn the walkthrough notes;
(2) adjacency (a monster listed in the neighbouring region). Both inflate
WALKTHROUGH-ONLY without being errors. The crisp, worth-a-look findings are in
bosses/djinn/summons where a thing is placed in an ENTIRELY different region by
the two streams (total disagreement, 0 region overlap).

Names are resolved format-only (no typo aliasing); unresolved walkthrough names
were already reported by locations_refs_gs2.py round 1 and are skipped here.
Overworld pseudo-locations (World Map *, East/West Sea, Gateway Cave) are not
spine regions -> dropped. Report-only; materializes the comparison for inspection.

Usage: python scripts/crosscheck_placement_gs2.py
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "gs2"
OUT = DATA / "intermediate" / "crosscheck_placement.json"

# free-text In-Depth location strings -> spine region_id (paren-strip handles
# "Trial Road (Top)"; these are the residue that don't match a region name).
ALIASES = {
    "venus lighthouse entry": "venus-lighthouse",
    "eastern alhafra": "alhafra",
    "outside of madra": "madra",
    "alhafran cave": "alhafran-cavern",
    "apojii island caves": "apojii-islands",
    "anemos inner sanctum": "anemos-sanctum",
    "sea of time": "sea-of-time",
}
# overworld / sea pseudo-locations: real, but not spine nodes -> not comparable.
OVERWORLD = re.compile(r"^world map\b|\bsea\b|^gateway cave$", re.I)


def norm(s):
    return re.sub(r"[^a-z0-9]", "", s.lower())


def strip_paren(s):
    return re.sub(r"\s*\([^)]*\)", "", s).strip()


def main():
    locations = json.loads((DATA / "locations.json").read_text(encoding="utf-8"))
    refs = json.loads((DATA / "location_refs.json").read_text(encoding="utf-8"))
    monsters = json.loads((DATA / "monsters.json").read_text(encoding="utf-8"))
    djinn = json.loads((DATA / "djinn.json").read_text(encoding="utf-8"))
    summons = json.loads((DATA / "summons.json").read_text(encoding="utf-8"))

    # --- region resolver (exact name/alias + substring phrases for prose) ---
    exact = {}
    phrases = []  # (normalized region name, region_id), longest first
    for l in locations:
        exact[norm(l["name"])] = l["region_id"]
        phrases.append((norm(l["name"]), l["region_id"]))
    for k, v in ALIASES.items():
        exact[norm(k)] = v
    phrases.sort(key=lambda p: len(p[0]), reverse=True)

    def resolve_strict(s):
        """For clean location labels (bestiary found): exact, then paren-strip/alias."""
        if not s or OVERWORLD.match(s.strip()):
            return None
        for cand in (s, strip_paren(s)):
            k = norm(cand)
            if k in exact:
                return exact[k]
        return ALIASES.get(strip_paren(s).lower()) or ALIASES.get(s.lower())

    def resolve_prose(text):
        """For prose (djinn desc / summon found_at): substring-scan region names."""
        if not text:
            return set()
        n = norm(text)
        hits = set()
        for k, rid in phrases:
            if len(k) >= 4 and k in n:   # avoid 1-2 char false hits
                hits.add(rid)
        return hits

    # --- inverse index from walkthrough (already resolved in round 1) ---
    idx = refs["index"]  # category -> {entity_id: [region_ids]}
    wk = {c: {k: set(v) for k, v in idx[c].items()} for c in idx}

    # name -> entity_id maps
    boss_region_indepth = {}   # boss display name handled via monsters found below
    report = {"bosses": [], "djinn": [], "summons": [], "monsters": []}
    summary = {}

    # ============ BOSSES ============
    # In-Depth: each boss's monster stat-lines `found`; walkthrough: wk['bosses']
    # map boss_id -> indepth regions via monsters that are is_boss + boss_id
    bi = {}
    for m in monsters:
        if m.get("is_boss") and m.get("boss_id"):
            for f in (m.get("found") or []):
                r = resolve_strict(f)
                if r:
                    bi.setdefault(m["boss_id"], set()).add(r)
    bosses = json.loads((DATA / "bosses.json").read_text(encoding="utf-8"))
    agree = wonly = ionly = 0
    for b in bosses:
        ind = bi.get(b["id"], set())
        wlk = wk["bosses"].get(b["id"], set())
        if not ind and not wlk:
            continue
        overlap = ind & wlk
        if overlap:
            agree += 1
        w_only = wlk - ind
        i_only = ind - wlk
        if w_only or (wlk and ind and not overlap):
            report["bosses"].append({"id": b["id"], "indepth": sorted(ind),
                                     "walkthrough": sorted(wlk),
                                     "disagree": not overlap and bool(wlk and ind)})
            wonly += bool(w_only)
        ionly += bool(i_only)
    summary["bosses"] = {"agree": agree, "walkthrough_extra": wonly, "indepth_extra": ionly}

    # ============ SUMMONS ============
    agree = wonly = ionly = 0
    for s in summons:
        acq = s.get("acquisition") or {}
        fa = acq.get("found_at") or acq.get("location")
        ind = resolve_prose(fa)
        wlk = wk["summons"].get(s["id"], set())
        if not ind and not wlk:
            continue
        overlap = ind & wlk
        agree += bool(overlap)
        if (wlk - ind) or (wlk and ind and not overlap):
            report["summons"].append({"id": s["id"], "found_at": fa,
                                      "indepth": sorted(ind), "walkthrough": sorted(wlk),
                                      "disagree": not overlap and bool(wlk and ind)})
            wonly += bool(wlk - ind)
        ionly += bool(ind - wlk)
    summary["summons"] = {"agree": agree, "walkthrough_extra": wonly, "indepth_extra": ionly}

    # ============ DJINN ============
    agree = wonly = ionly = 0
    for d in djinn:
        desc = (d.get("location") or {}).get("description")
        ind = resolve_prose(desc)
        wlk = wk["djinn"].get(d["id"], set())
        if not ind and not wlk:
            continue
        overlap = ind & wlk
        agree += bool(overlap)
        if (wlk - ind) or (wlk and ind and not overlap):
            report["djinn"].append({"id": d["id"], "desc": desc,
                                    "indepth": sorted(ind), "walkthrough": sorted(wlk),
                                    "disagree": not overlap and bool(wlk and ind)})
            wonly += bool(wlk - ind)
        ionly += bool(ind - wlk)
    summary["djinn"] = {"agree": agree, "walkthrough_extra": wonly, "indepth_extra": ionly}

    # ============ MONSTERS (soft: recurring/adjacency) ============
    RECURRING = {"mimic", "madplant"}
    mon_found = {}
    for m in monsters:
        if m.get("is_boss") or m.get("is_djinn_enemy"):
            continue
        rs = set()
        for f in (m.get("found") or []):
            r = resolve_strict(f)
            if r:
                rs.add(r)
        mon_found[norm(m["name"])] = rs
    # walkthrough monster placements (resolved monster id -> regions)
    mon_id_by_norm = {norm(m["name"]): m["id"] for m in monsters}
    agree = wonly = 0
    for l in locations:
        for mn in l.get("monsters_here", []):
            k = norm(mn)
            if k not in mon_found:
                continue  # unresolved name -> round 1 already flagged it
            ind = mon_found[k]
            if l["region_id"] in ind:
                agree += 1
            else:
                report["monsters"].append({
                    "monster": mn, "walkthrough_region": l["region_id"],
                    "indepth": sorted(ind),
                    "recurring": k in RECURRING or (len(ind) <= 1)})
                wonly += 1
    summary["monsters"] = {"agree": agree, "walkthrough_extra": wonly,
                           "recurring_or_singlefound": sum(1 for r in report["monsters"] if r["recurring"])}

    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(json.dumps({"summary": summary, "findings": report},
                              ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    # ---- report ----
    print(f"wrote {OUT.relative_to(ROOT)}\n")
    for cat in ("bosses", "djinn", "summons", "monsters"):
        print(f"=== {cat} === {summary[cat]}")
        for f in report[cat]:
            tag = " <-- TOTAL DISAGREE" if f.get("disagree") else ""
            if cat == "monsters":
                soft = " (recurring/single-found)" if f["recurring"] else ""
                print(f"    {f['walkthrough_region']:20} {f['monster']!r} "
                      f"indepth={f['indepth']}{soft}")
            else:
                print(f"    {f['id']:18} walkthrough={f['walkthrough']} "
                      f"indepth={f['indepth']}{tag}")
        print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
