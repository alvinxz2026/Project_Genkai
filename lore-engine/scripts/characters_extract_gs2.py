"""Extract the 8 GS2 (Lost Age) playable characters into data/gs2/characters.json.

Deterministic parser (no LLM/API), mirroring scripts/djinn_extract_gs2.py et al.
`characters` is a small **dimension table** (the node that equipment.equippable_by /
psynergy.available_to / classes.available_to[].character resolve against). Two layers,
like bosses:

  1. Structured layer — `darkslime`'s "1. The Character Guide" section lists every
     character in a clean block: `Name/JPName` header, prose, then `Hair:`,
     `Alignment:`, `Can Equip:` (may wrap a line), `Hometown:`. The **8 playables are
     exactly the blocks that carry a `Can Equip:` line** (villains have none). From
     each we take name / jp_name / element (Alignment clan) / hometown / can_equip.

  2. Curated layer — `is_starter` / `from_gs1` / `join` are prose/judgment (when &
     how each joins the TLA party, and whether they are a returning GS1 Adept).
     GS1's `characters` used `is_permanent`; per the ER sketch (§4.1) the TLA roster
     splits instead into TLA-native starters/early joiners vs the 4 returning GS1
     Adepts who rejoin late-game. Kept small (8 rows), sourced to the walkthroughs.

Element mapping (same as the other gs2 parsers): Venus=earth, Mercury=water,
Mars=fire, Jupiter=wind.

Rerunnable: parses raw text for the structured fields; only the 8-row judgment map
is embedded.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "raw" / "gs2" / "Guide and Walkthrough" / "Guide and Walkthrough by Darkslime.md"
OUT = ROOT / "data" / "gs2" / "characters.json"

CLAN_ELEMENT = {"Venus": "earth", "Mars": "fire", "Jupiter": "wind", "Mercury": "water"}

# Curated judgment layer (darkslime/darthmarth walkthroughs). Order = roster order.
# is_starter: in the party at the opening (Idejima). from_gs1: returning GS1 Adept.
CURATED = {
    "felix":  {"is_starter": True,  "from_gs1": False, "join": "party leader; available from the start on Idejima."},
    "jenna":  {"is_starter": True,  "from_gs1": False, "join": "available from the start on Idejima (Felix's sister)."},
    "sheba":  {"is_starter": True,  "from_gs1": False, "join": "available from the start (fell to Idejima with Felix)."},
    "piers":  {"is_starter": False, "from_gs1": False, "join": "joins at Kibombo, after the party helps recover his ship."},
    "isaac":  {"is_starter": False, "from_gs1": True,  "join": "returning GS1 Adept; joins the playable party in the late game once the two parties reunite (Contigo)."},
    "garet":  {"is_starter": False, "from_gs1": True,  "join": "returning GS1 Adept; joins the playable party in the late game once the two parties reunite (Contigo)."},
    "ivan":   {"is_starter": False, "from_gs1": True,  "join": "returning GS1 Adept; joins the playable party in the late game once the two parties reunite (Contigo)."},
    "mia":    {"is_starter": False, "from_gs1": True,  "join": "returning GS1 Adept; joins the playable party in the late game once the two parties reunite (Contigo)."},
}

LABELS = ("Hair:", "Alignment:", "Can Equip:", "Hometown:")


def section_lines(text):
    """The block between the '1. The Character Guide' banner and '2. Tables and Lists'."""
    lines = text.splitlines()
    start = next(i for i, l in enumerate(lines) if "1. The Character Guide" in l)
    end = next(i for i, l in enumerate(lines[start + 1:], start + 1) if "2. Tables and Lists" in l)
    return lines[start + 1:end]


def split_blocks(lines):
    """Split on blank-line boundaries; each block = one character's entry."""
    blocks, cur = [], []
    for l in lines:
        if l.strip() == "":
            if cur:
                blocks.append(cur)
                cur = []
        else:
            cur.append(l)
    if cur:
        blocks.append(cur)
    return blocks


def field(block, label):
    """Value of a 'Label:' line, joining wrapped continuation lines (indented, no
    other label) that follow it within the block."""
    for i, l in enumerate(block):
        if l.lstrip().startswith(label):
            parts = [l.split(label, 1)[1].strip()]
            for nxt in block[i + 1:]:
                if any(nxt.lstrip().startswith(x) for x in LABELS):
                    break
                if nxt[:1] in (" ", "\t"):  # wrapped continuation is indented
                    parts.append(nxt.strip())
                else:
                    break
            return " ".join(p for p in parts if p).strip()
    return None


def parse(text):
    out = []
    for block in split_blocks(section_lines(text)):
        equip_raw = field(block, "Can Equip:")
        if not equip_raw:
            continue  # villains / non-playables have no 'Can Equip:'
        header = block[0].strip()
        name, _, jp = header.partition("/")
        name, jp = name.strip(), jp.strip()
        cid = name.lower()

        clan = (field(block, "Alignment:") or "").split()[0]  # "Venus Clan" -> "Venus"
        element = CLAN_ELEMENT.get(clan)

        can_equip = [t.strip().lower() for t in equip_raw.split(",") if t.strip()]
        hometown = field(block, "Hometown:") or None

        cur = CURATED.get(cid, {})
        out.append({
            "id": cid,
            "name": name,
            "jp_name": jp or None,
            "game": "gs2",
            "element": element,
            "is_starter": cur.get("is_starter"),
            "from_gs1": cur.get("from_gs1"),
            "join": cur.get("join"),
            "hometown": hometown,
            "can_equip": can_equip,
            "sources": ["darkslime"] + (["darthmarth"] if cur.get("join") else []),
        })
    return out


def main():
    text = SRC.read_text(encoding="utf-8", errors="replace")
    rows = parse(text)

    # Validation / accounting.
    ids = [r["id"] for r in rows]
    assert len(ids) == len(set(ids)), f"duplicate ids: {ids}"
    expected = set(CURATED)
    got = set(ids)
    assert got == expected, f"roster mismatch: missing {expected - got}, extra {got - expected}"
    for r in rows:
        assert r["element"] in ("earth", "fire", "wind", "water"), f"bad element: {r}"
        assert r["can_equip"], f"empty can_equip: {r['id']}"

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(rows, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"wrote {len(rows)} characters -> {OUT.relative_to(ROOT)}")
    for r in rows:
        flag = "starter" if r["is_starter"] else ("gs1-return" if r["from_gs1"] else "joins")
        print(f"  {r['id']:8} {r['element']:6} [{flag}] equip={len(r['can_equip'])} hometown={r['hometown']!r}")


if __name__ == "__main__":
    main()
