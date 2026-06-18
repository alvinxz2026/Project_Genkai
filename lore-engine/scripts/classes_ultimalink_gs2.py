"""Layer 2 for data/gs2/classes.json: back-fill `psynergy[]` learnsets and
`available_to[]` from `ultimalink` (Character Class Guide). Run after Layer 1
(`classes_extract_gs2.py`). Deterministic, no LLM. Idempotent (recomputes both
fields from scratch each run).

ultimalink is organized per character; each character section has class *blocks*:
a title, tier rows (name + 6 stat% + a djinn requirement like "Venus x2", or
"N/A" when that tier is unreachable for the character), then a per-chain
"Psynergy / Level" table. Findings that make this deterministic:

  * Same-element characters share identical chains + psynergy (Felix == Isaac).
    => psynergy is a property of the class-LINE; assign the block's learnset to
       every terence class on that line.
  * A block's tier sequence aligns 1:1, in order, with a terence class-line
    (chain). The block TITLE maps consistently to a class-line root (BLOCK2LINE);
    e.g. "Swordsman" -> swordsman-earth for both earth and water characters,
    "Luminier" -> swordsman-fire. So: map title -> root, take the terence chain
    (classes.json rows with that class_line, already in tier order), and zip.
  * `available_to` = the characters whose tier row is reachable (not N/A), each
    carrying ultimalink's character-relative djinn counts.

Deferred: the Tamer item-class has per-sub-class psynergy in side-by-side columns
(not one chain table); its psynergy is left [] here (note in schema). aku-chi ACR
+ the relative djinn-count matcher are Layer 3.
"""
import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "raw" / "gs2" / "In-Depth Guides" / "Character Class Guide by UltimaLink.md"
CLASSES = ROOT / "data" / "gs2" / "classes.json"

CHARS = {
    "Felix": ("Felix", "earth"), "Isaac": ("Isaac", "earth"),
    "Jenna": ("Jenna", "fire"), "Garret": ("Garet", "fire"),
    "Sheba": ("Sheba", "wind"), "Ivan": ("Ivan", "wind"),
    "Piers": ("Piers", "water"), "Mia": ("Mia", "water"),
}
ELEM_DJINN = {"Venus": "earth", "Mercury": "water", "Mars": "fire", "Jupiter": "wind"}
DJINN_RE = re.compile(r"(Venus|Mercury|Mars|Jupiter)\s+x?(\d+)", re.I)
PSY_ROW = re.compile(r"^(.+?)\**\s*(\d+)\s*$")

# Block title (parenthetical stripped) -> terence class-line root id. Consistent
# across the characters that can reach the line (verified from the full dump).
BLOCK2LINE = {
    # basic element chains (element-distinct titles)
    "Squire": "squire", "Fighter": "guard", "Flame User": "flame-user",
    "Magician": "wind-seer", "Priest": "water-seer", "Mariner": "mariner",
    # dual / dip chains
    "Swordsman": "swordsman-earth", "Luminier": "swordsman-fire",
    "Apprentice": "apprentice", "Page": "page",
    "Brute": "brute", "Samurai": "samurai",
    "Water Seer": "seer-water", "Wind Seer": "seer-wind",
    "Sage": "hermit", "White Mage": "white-mage",
    "Medium": "medium", "Ranger": "ranger",
    "Pilgrim A": "pilgrim-water", "Pilgrim B": "pilgrim-wind",
    "Dragoon": "dragoon", "Ninja": "ninja",
    # item classes
    "Pierrot": "pierrot", "Tamer": "tamer", "Dark Mage": "dark-mage-item",
}
DEFER_PSYNERGY = {"tamer"}  # per-sub-class side-by-side columns; defer


def slug(s):
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", s.lower())).strip("-")


def char_sections(lines):
    heads = [(i, m.group(1)) for i, l in enumerate(lines)
             if (m := re.match(r"Chapter [IVX]+ - (\w+)(?:'s)? Classes", l.strip()))]
    out = []
    for k, (i, name) in enumerate(heads):
        end = heads[k + 1][0] if k + 1 < len(heads) else len(lines)
        out.append((name, lines[i + 1:end]))
    return out


def is_tier_row(line):
    if not line[:1].strip():
        return False
    return ("\t" in line or "  " in line) and ("%" in line or "N/A" in line)


def parse_blocks(seclines):
    blocks = []
    i, n = 0, len(seclines)
    prev = None
    while i < n:
        line = seclines[i].rstrip()
        if is_tier_row(line):
            title = re.sub(r"\s*\(.*?\)\s*$", "", prev or "").strip()
            tiers, psy = [], []
            while i < n:  # tier rows + djinn continuations
                l = seclines[i].rstrip()
                if not l.strip():
                    i += 1
                    if i < n and (seclines[i].strip().startswith("Psynergy")
                                  or is_tier_row(seclines[i].rstrip())):
                        continue
                    break
                if is_tier_row(l):
                    name = re.split(r"\t+|\s{2,}", l.strip())[0].strip()
                    djinn = [(ELEM_DJINN[e.capitalize()], int(c)) for e, c in DJINN_RE.findall(l)]
                    tiers.append({"name": name, "reachable": "N/A" not in l, "djinn": djinn})
                elif DJINN_RE.search(l) and not l[:1].strip() and tiers:
                    tiers[-1]["djinn"] += [(ELEM_DJINN[e.capitalize()], int(c))
                                           for e, c in DJINN_RE.findall(l)]
                else:
                    break
                i += 1
            multi_col = title in ("Tamer",)
            while i < n:  # psynergy table(s) until footnotes
                l = seclines[i].rstrip()
                s = l.strip()
                if not s:
                    i += 1
                    continue
                if s.startswith(("Psynergy", "Tamer", "Trainer", "Beastkeeper", "Beast Lord")):
                    i += 1
                    continue
                if s.startswith(("*", "(", "Note")):
                    break
                if is_tier_row(l):
                    break
                m = PSY_ROW.match(s)
                if m:
                    if not multi_col:
                        psy.append((m.group(1).strip(" *\t"), int(m.group(2))))
                    i += 1
                    continue
                break  # non-row line = next block's title; leave it for the main loop
            blocks.append({"title": title, "tiers": tiers, "psynergy": psy})
        else:
            if line.strip():
                prev = line.strip()
            i += 1
    return blocks


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--inspect", action="store_true")
    args = ap.parse_args()

    lines = SRC.read_text(encoding="utf-8", errors="replace").splitlines()
    classes = json.loads(CLASSES.read_text(encoding="utf-8"))
    by_id = {c["id"]: c for c in classes}
    # terence chains in tier order (= file order within a class_line).
    chains = {}
    for c in classes:
        chains.setdefault(c["class_line"], []).append(c["id"])

    # accumulators keyed by class id
    psy_by_line = {}                       # root -> {name: level}
    avail = {cid: {} for cid in by_id}     # cid -> {char_name: djinn list}

    unmapped = set()
    for printed, seclines in char_sections(lines):
        disp, elem = CHARS[printed]
        for b in parse_blocks(seclines):
            root = BLOCK2LINE.get(b["title"])
            if root is None:
                unmapped.add((printed, b["title"]))
                continue
            chain = chains[root]
            if len(chain) != len(b["tiers"]):
                raise SystemExit(f"chain/tier mismatch {disp} [{b['title']}] -> {root}: "
                                 f"{len(b['tiers'])} tiers vs chain {len(chain)} {chain}")
            for cid, tier in zip(chain, b["tiers"]):
                # alignment guard: tier name should relate to the class id
                if tier["reachable"] and slug(tier["name"]) not in cid and cid not in slug(tier["name"]):
                    # exception: item/medium upgrade ids keep base name (ok)
                    if slug(tier["name"].split()[0]) not in cid:
                        raise SystemExit(f"misalign {disp} [{b['title']}] {tier['name']!r} vs {cid}")
                if tier["reachable"]:
                    avail[cid][disp] = tier["djinn"]
            if root not in DEFER_PSYNERGY:
                d = psy_by_line.setdefault(root, {})
                for name, lvl in b["psynergy"]:
                    d.setdefault(name, lvl)        # first level wins; chains agree

    if args.inspect:
        for printed, title in sorted(unmapped):
            print(f"UNMAPPED: {printed} [{title}]")
        print(f"lines with psynergy: {len(psy_by_line)}; "
              f"classes with available_to: {sum(1 for v in avail.values() if v)}")
        return

    if unmapped:
        raise SystemExit(f"unmapped blocks: {sorted(unmapped)}")

    # write back
    n_psy = n_av = 0
    for c in classes:
        cid, root = c["id"], c["class_line"]
        learn = psy_by_line.get(root, {})
        c["psynergy"] = [{"name": nm, "id": None, "level": lv, "sources": ["ultimalink"]}
                         for nm, lv in sorted(learn.items(), key=lambda kv: (kv[1], kv[0]))]
        av = []
        for char_name, djinn in avail[cid].items():
            parsed = [{"element": e, "count": n} for e, n in djinn]
            req = ", ".join(f"{e} x{n}" for e, n in djinn) or "none"
            av.append({"character": char_name, "character_id": char_name.lower(),
                       "djinn_requirements": [{"requirement": req, "parsed": parsed,
                                               "source": "ultimalink"}], "acr": None})
        c["available_to"] = av
        if c["psynergy"]:
            n_psy += 1
        if av:
            n_av += 1
        if "ultimalink" not in c["sources"] and (c["psynergy"] or av):
            c["sources"].append("ultimalink")

    CLASSES.write_text(json.dumps(classes, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"updated {CLASSES.relative_to(ROOT)}")
    print(f"  classes with psynergy:     {n_psy}/{len(classes)}")
    print(f"  classes with available_to: {n_av}/{len(classes)}")
    empty = [c["id"] for c in classes if not c["available_to"]]
    print(f"  no available_to ({len(empty)}): {empty}")


if __name__ == "__main__":
    main()
