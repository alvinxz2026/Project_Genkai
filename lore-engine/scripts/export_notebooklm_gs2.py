#!/usr/bin/env python3
"""Render gs2 SSoT JSON into NotebookLM-friendly prose markdown.

NotebookLM is a RAG over naively-chunked text: JSON gets split mid-object and
loses the entity<->value binding, so raw JSON ingests badly. This script turns
each JSON entry into a self-contained prose paragraph under a `## Name` heading,
so every retrieved chunk still names the entity it describes.

Output: export/gs2_notebooklm/
  - one <entity>.md per JSON entity (prose, SSoT — deduped/conflict-aware)
  - walkthrough_en.md / walkthrough_zh.md (concatenated chapter prose)
  - README.md (what to drop into NotebookLM)

Run from the lore-engine root:  python scripts/export_notebooklm_gs2.py
Deterministic, no API calls.
"""
import json
import os
import glob

DATA = "data/gs2"
OUT = "export/gs2_notebooklm"

ELEM = {"earth": "Earth", "fire": "Fire", "wind": "Wind", "water": "Water",
        "mars": "Mars", "venus": "Venus", "jupiter": "Jupiter", "mercury": "Mercury"}


def load(name):
    return json.load(open(f"{DATA}/{name}.json", encoding="utf-8"))


def cap(s):
    return ELEM.get(s, s.capitalize() if isinstance(s, str) else s)


def art(word):
    """'a' / 'an' for the following word."""
    return "an" if word[:1].lower() in "aeiou" else "a"


def nonzero_stats(d, keys=None):
    """Return 'atk +108, def +6' for nonzero numeric entries; '' if all zero/null."""
    if not d:
        return ""
    keys = keys or list(d.keys())
    parts = []
    for k in keys:
        v = d.get(k)
        if isinstance(v, (int, float)) and v:
            sign = "+" if v > 0 else ""
            parts.append(f"{k} {sign}{v}")
    return ", ".join(parts)


def elem_line(d, label):
    """Render an elemental power/resistance dict, only nonzero."""
    if not d:
        return ""
    parts = [f"{cap(k)} {v}" for k, v in d.items() if isinstance(v, (int, float)) and v]
    return f"{label}: {', '.join(parts)}." if parts else ""


def src(entry):
    s = entry.get("sources") or []
    return f" _(sources: {', '.join(s)})_" if s else ""


def write(fname, title, lead, blocks):
    os.makedirs(OUT, exist_ok=True)
    body = [f"# {title}", "", lead, ""]
    body += [b for b in blocks if b]
    txt = "\n".join(body).rstrip() + "\n"
    open(f"{OUT}/{fname}", "w", encoding="utf-8").write(txt)
    return len([b for b in blocks if b])


# ---------- per-entity renderers ----------

def r_characters():
    data = load("characters")
    blocks = []
    for c in data:
        L = [f"## {c['name']}"]
        line = f"{c['name']}"
        if c.get("jp_name"):
            line += f" (JP: {c['jp_name']})"
        el = cap(c.get('element', ''))
        line += f" is {art(el)} {el}-element Adept"
        if c.get("hometown"):
            line += f" from {c['hometown']}"
        line += "."
        if c.get("is_starter"):
            line += " A starting party member."
        if c.get("from_gs1"):
            line += " Returns from Golden Sun 1."
        L.append(line)
        if c.get("join"):
            L.append(f"Joins: {c['join']}")
        if c.get("can_equip"):
            L.append(f"Can equip: {', '.join(c['can_equip'])}.")
        L.append("" + src(c))
        blocks.append("\n".join(L) + "\n")
    return write("characters.md", "Golden Sun 2 — Characters",
                 "The eight playable Adepts.", blocks)


def r_djinn():
    data = load("djinn")
    blocks = []
    for d in data:
        L = [f"## {d['name']} (Djinn)"]
        el = cap(d.get('element', ''))
        line = f"{d['name']} is {art(el)} {el} Djinni."
        if d.get("battle_effect"):
            line += f" Battle effect: {d['battle_effect']}."
        L.append(line)
        st = nonzero_stats(d.get("stat_bonus"))
        if st:
            L.append(f"Set bonus when Set: {st}.")
        if d.get("location"):
            loc = d["location"]
            if isinstance(loc, dict):
                loc = loc.get("area") or loc.get("found_at") or json.dumps(loc, ensure_ascii=False)
            L.append(f"Found: {loc}.")
        if d.get("must_fight"):
            L.append("Must be fought to obtain.")
        L.append("" + src(d))
        blocks.append("\n".join(L) + "\n")
    return write("djinn.md", "Golden Sun 2 — Djinn",
                 "All 72 Djinn across the four elements (shared 8-Adept pool).", blocks)


def r_summons():
    data = load("summons")
    blocks = []
    for s in data:
        L = [f"## {s['name']} (Summon)"]
        el = cap(s.get('element', ''))
        line = f"{s['name']} is {art(el)} {el} summon."
        if s.get("is_combo"):
            recipe = s.get("djinn_recipe") or []
            req = ", ".join(f"{r['count']} {cap(r['element'])}" for r in recipe)
            line += f" A combination summon requiring {req} Djinn Set."
        elif s.get("djinn_required"):
            line += f" Requires {s['djinn_required']} Djinn of its element."
        L.append(line)
        dmg = []
        if s.get("damage_power") is not None:
            dmg.append(f"base power {s['damage_power']}")
        if s.get("damage_hp_mod"):
            dmg.append(f"+{int(s['damage_hp_mod']*100)}% of target max HP")
        if s.get("range") is not None:
            dmg.append(f"range {s['range']}")
        if dmg:
            L.append("Damage: " + ", ".join(dmg) + ".")
        if s.get("effect"):
            L.append(f"Effect: {s['effect']}.")
        acq = s.get("acquisition") or {}
        if acq.get("location") or acq.get("found_at"):
            L.append(f"Obtained: {acq.get('found_at') or acq.get('location')}.")
        L.append("" + src(s))
        blocks.append("\n".join(L) + "\n")
    return write("summons.md", "Golden Sun 2 — Summons",
                 "Standard and combination summons.", blocks)


def r_psynergy():
    data = load("psynergy")
    blocks = []
    for p in data:
        L = [f"## {p['name']} (Psynergy)"]
        el = cap(p.get('element') or '')
        if el:
            line = f"{p['name']} is {art(el)} {el} Psynergy"
        else:
            line = f"{p['name']} is a Psynergy ability"
        if p.get("pp_cost") is not None:
            line += f" costing {p['pp_cost']} PP"
        line += "."
        if p.get("range"):
            line += f" Range: {p['range']}."
        L.append(line)
        if p.get("description"):
            L.append(p["description"])
        L.append("" + src(p))
        blocks.append("\n".join(L) + "\n")
    return write("psynergy.md", "Golden Sun 2 — Psynergy",
                 "Battle and utility Psynergy (canonical + class-specific).", blocks)


def r_equipment():
    data = load("equipment")
    blocks = []
    for e in data:
        L = [f"## {e['name']}"]
        cat = e.get("type") or e.get("category") or "equipment"
        cat = cat.replace("_", " ")
        line = f"{e['name']} is a {cat}"
        tags = []
        if e.get("is_artifact"):
            tags.append("artifact")
        if e.get("is_cursed"):
            tags.append("cursed")
        if e.get("is_rusty"):
            tags.append("rusty (forgeable)")
        if tags:
            line += f" ({', '.join(tags)})"
        line += "."
        L.append(line)
        st = nonzero_stats(e.get("stat_bonus"))
        if st:
            L.append(f"Stats: {st}.")
        ep = elem_line(e.get("elemental_power"), "Elemental power")
        if ep:
            L.append(ep)
        er = elem_line(e.get("elemental_resistance"), "Elemental resistance")
        if er:
            L.append(er)
        if e.get("increases_critical"):
            L.append("Increases critical-hit rate.")
        un = e.get("unleash") or {}
        if un.get("name"):
            L.append(f"Unleash: {un['name']}.")
        if e.get("use_effect"):
            L.append(f"Use effect: {e['use_effect']}.")
        if e.get("equippable_by"):
            L.append(f"Equippable by: {', '.join(e['equippable_by'])}.")
        if e.get("forged_from"):
            L.append(f"Forged from: {', '.join(e['forged_from'])}.")
        price = []
        if e.get("buy_price"):
            price.append(f"buy {e['buy_price']}")
        if e.get("sell_price"):
            price.append(f"sell {e['sell_price']}")
        if price:
            L.append("Price: " + ", ".join(price) + " coins.")
        L.append("" + src(e))
        blocks.append("\n".join(L) + "\n")
    return write("equipment.md", "Golden Sun 2 — Equipment",
                 "Weapons, armor, and accessories (TLA + shared base items).", blocks)


def r_items():
    data = load("items")
    blocks = []
    for it in data:
        L = [f"## {it['name']}"]
        typ = (it.get("item_type") or "item").replace("_", " ")
        line = f"{it['name']} is a {typ}."
        eff = it.get("effect")
        if isinstance(eff, dict):
            eff = eff.get("description")
        if eff:
            line += f" {eff[0].upper()+eff[1:]}."
        L.append(line)
        if it.get("usable_in_battle"):
            L.append("Usable in battle.")
        price = []
        if it.get("buy_price"):
            price.append(f"buy {it['buy_price']}")
        if it.get("sell_price"):
            price.append(f"sell {it['sell_price']}")
        if price:
            L.append("Price: " + ", ".join(price) + " coins.")
        L.append("" + src(it))
        blocks.append("\n".join(L) + "\n")
    return write("items.md", "Golden Sun 2 — Items",
                 "Consumables, Psynergy items, key items, and forge materials.", blocks)


def r_monsters():
    data = load("monsters")
    blocks = []
    for m in data:
        if m.get("is_boss"):
            continue  # bosses get their own richer file
        L = [f"## {m['name']}"]
        line = f"{m['name']} is an enemy"
        if m.get("variant"):
            line += f" ({m['variant']} variant)"
        if m.get("found"):
            line += f" found in {', '.join(m['found'])}"
        line += "."
        L.append(line)
        st = m.get("stats") or {}
        statline = nonzero_stats(st, ["hp", "pp", "atk", "def", "agi", "lck"])
        if statline:
            L.append(f"Stats: {statline}.")
        er = elem_line(m.get("elemental_resistance"), "Elemental resistance")
        if er:
            L.append(er)
        if m.get("abilities"):
            L.append(f"Abilities: {', '.join(m['abilities'])}.")
        drops = m.get("drops") or {}
        d = []
        if drops.get("exp") is not None:
            d.append(f"{drops['exp']} EXP")
        if drops.get("coins") is not None:
            d.append(f"{drops['coins']} coins")
        for itm in drops.get("items") or []:
            nm = itm.get("name") if isinstance(itm, dict) else itm
            icc = itm.get("icc") if isinstance(itm, dict) else None
            d.append(f"{nm}" + (f" (drop chance 1/{icc})" if icc else ""))
        if d:
            L.append("Drops: " + ", ".join(d) + ".")
        L.append("" + src(m))
        blocks.append("\n".join(L) + "\n")
    return write("monsters.md", "Golden Sun 2 — Monsters",
                 "Regular enemies (bosses are in bosses.md).", blocks)


def r_bosses():
    data = load("bosses")
    blocks = []
    for b in data:
        L = [f"## {b['name']} (Boss)"]
        tags = []
        if b.get("is_optional"):
            tags.append("optional")
        if b.get("is_superboss"):
            tags.append("superboss")
        line = f"{b['name']} is a boss"
        if tags:
            line += f" ({', '.join(tags)})"
        if b.get("recommended_level"):
            line += f"; recommended level {b['recommended_level']}"
        line += "."
        if b.get("weakness"):
            line += f" Weak to: {', '.join(cap(w) for w in b['weakness'])}."
        L.append(line)
        for enc in b.get("encounters") or []:
            where = enc.get("location", "")
            st = nonzero_stats(enc.get("stats") or {}, ["hp", "pp", "atk", "def", "agi", "lck"])
            seg = f"Encounter ({where}): {st}." if st else f"Encounter: {where}."
            atks = [a.get("name") if isinstance(a, dict) else a for a in enc.get("attacks") or []]
            if atks:
                seg += f" Attacks: {', '.join(atks)}."
            rew = enc.get("rewards") or {}
            rparts = []
            if rew.get("exp") is not None:
                rparts.append(f"{rew['exp']} EXP")
            if rew.get("coins") is not None:
                rparts.append(f"{rew['coins']} coins")
            if rew.get("items"):
                rparts.append(", ".join(rew["items"]))
            if rparts:
                seg += f" Rewards: {', '.join(rparts)}."
            L.append(seg)
        if b.get("strategy"):
            L.append(f"Strategy: {b['strategy']}")
        if b.get("special_mechanics"):
            L.append("Mechanics: " + "; ".join(b["special_mechanics"]) + ".")
        if b.get("special_notes"):
            L.append(b["special_notes"])
        L.append("" + src(b))
        blocks.append("\n".join(L) + "\n")
    return write("bosses.md", "Golden Sun 2 — Bosses",
                 "Story and optional bosses with stats and strategy.", blocks)


def r_classes():
    data = load("classes")
    blocks = []
    for c in data:
        L = [f"## {c['name']} (Class)"]
        line = f"{c['name']} is a class"
        if c.get("class_line"):
            line += f" in the {c['class_line']} line"
        line += "."
        L.append(line)
        sm = c.get("stat_multiplier") or {}
        smline = ", ".join(f"{k} {v}%" for k, v in sm.items() if v is not None)
        if smline:
            L.append(f"Stat multipliers: {smline}.")
        er = c.get("element_requirements") or {}
        erp = [f"{cap(k)} {v}" for k, v in er.items() if v]
        if erp:
            L.append(f"Element requirements: {', '.join(erp)}.")
        # who can be it + djinn reqs (use the requirement strings, keep concise)
        whos = []
        for a in c.get("available_to") or []:
            reqs = a.get("djinn_requirements") or []
            rs = "; ".join(f"{r['requirement']} ({r['source']})" for r in reqs) if reqs else "no extra Djinn"
            whos.append(f"{a['character']}: {rs}")
        if whos:
            L.append("Available to — " + " | ".join(whos) + ".")
        psy = c.get("psynergy") or []
        if psy:
            psline = ", ".join(f"{p['name']} (Lv{p['level']})" for p in psy if p.get("level") is not None)
            L.append(f"Learns: {psline}.")
        L.append("" + src(c))
        blocks.append("\n".join(L) + "\n")
    return write("classes.md", "Golden Sun 2 — Classes",
                 "Class lines with stat multipliers, Djinn requirements, and learned Psynergy.", blocks)


def r_locations():
    data = load("locations")
    blocks = []
    for loc in sorted(data, key=lambda x: x.get("order", 0)):
        L = [f"## {loc['name']}"]
        line = f"{loc['name']} is a {loc.get('kind','')} location".replace("a main location", "a main story location")
        if loc.get("connections"):
            line += f", connected to {', '.join(loc['connections'])}"
        line += "."
        L.append(line)
        for label, key in [("Pickups", "pickups"), ("Djinn", "djinn_here"),
                           ("Psynergy obtained", "psynergy_here"), ("Summons", "summons_here"),
                           ("Monsters", "monsters_here"), ("Bosses", "bosses_here"),
                           ("Forging", "forging")]:
            v = loc.get(key)
            if v:
                L.append(f"{label}: {', '.join(str(x) for x in v)}.")
        if loc.get("shop"):
            L.append("Has a shop.")
        L.append("" + src(loc))
        blocks.append("\n".join(L) + "\n")
    return write("locations.md", "Golden Sun 2 — Locations",
                 "Areas in walkthrough order with pickups, Djinn, and encounters.", blocks)


def r_shops():
    data = load("shops")
    blocks = []
    for s in data:
        L = [f"## {s['name']} Shop"]
        line = f"The shop in {s.get('location', s['name'])}"
        if s.get("availability_notes"):
            line += f" ({s['availability_notes']})"
        line += " stocks:"
        L.append(line)
        for it in s.get("stock") or []:
            tag = " [artifact]" if it.get("is_artifact") else ""
            L.append(f"- {it['name']} — {it.get('price','?')} coins ({it.get('category','')}){tag}")
        L.append("" + src(s))
        blocks.append("\n".join(L) + "\n")
    return write("shops.md", "Golden Sun 2 — Shops",
                 "Shop inventories by town.", blocks)


# ---------- walkthrough concatenation ----------

def concat_walkthrough(srcdir, fname, title):
    files = sorted(glob.glob(f"{DATA}/{srcdir}/*.md"))
    if not files:
        return 0
    body = [f"# {title}", ""]
    for f in files:
        body.append(open(f, encoding="utf-8").read().rstrip())
        body.append("\n---\n")
    os.makedirs(OUT, exist_ok=True)
    open(f"{OUT}/{fname}", "w", encoding="utf-8").write("\n".join(body).rstrip() + "\n")
    return len(files)


def main():
    os.makedirs(OUT, exist_ok=True)
    counts = {}
    for fn in [r_characters, r_djinn, r_summons, r_psynergy, r_equipment,
               r_items, r_monsters, r_bosses, r_classes, r_locations, r_shops]:
        name = fn.__name__[2:]
        counts[name] = fn()
    counts["walkthrough_en"] = concat_walkthrough("walkthrough", "walkthrough_en.md",
                                                  "Golden Sun 2 — Walkthrough (English)")
    counts["walkthrough_zh"] = concat_walkthrough("walkthrough_zh", "walkthrough_zh.md",
                                                  "黄金太阳2 — 流程攻略（中文）")

    # README
    lines = [
        "# Golden Sun 2 — NotebookLM 投喂包", "",
        "本目录由 `scripts/export_notebooklm_gs2.py` 从 SSoT JSON 渲染而成。",
        "全部是 **prose markdown**（每个实体一个 `## 名称` 段落），专为 NotebookLM 的",
        "分块检索优化——直接丢 JSON 会被切坏，这里不会。", "",
        "## 丢哪些进 NotebookLM", "",
        "把下面这些文件作为 source 上传（**不要**再额外丢 `data/gs2/*.json` 原始文件，",
        "否则会把已裁决的 conflict 又请回来）：", "",
    ]
    order = ["characters", "djinn", "summons", "psynergy", "classes",
             "equipment", "items", "monsters", "bosses", "locations", "shops"]
    for k in order:
        lines.append(f"- `{k}.md` — {counts.get(k,0)} 条")
    lines += [
        f"- `walkthrough_en.md` — {counts['walkthrough_en']} 章英文流程（合并）",
        f"- `walkthrough_zh.md` — {counts['walkthrough_zh']} 章中文流程（合并）",
        "",
        "共 13 个 source，远低于 NotebookLM 的 50 source 上限。", "",
        "## 可选：也丢 raw 原始攻略", "",
        "若想要原汁原味的叙述细节，可再把 `raw/gs2/` 里的 prose 攻略一并丢进去。",
        "但注意 raw 是多源、未裁决的，回答可能出现 SSoT 已解决的矛盾。",
        "**图准 → 只用本目录；图全 → 本目录 + raw（择一为主，别混着当权威）。**",
    ]
    open(f"{OUT}/README.md", "w", encoding="utf-8").write("\n".join(lines) + "\n")

    print("Rendered to", OUT)
    for k, v in counts.items():
        print(f"  {k:16} {v}")


if __name__ == "__main__":
    main()
