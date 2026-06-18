"""Deterministically split a gs2 Guide-and-Walkthrough into per-chapter files.

NO LLM. The raw walkthroughs are immutable; this writes a *derived* layer under
`raw/gs2/_chapters/<source_id>/NN-<slug>.md`, each chapter = a **byte-exact**
slice of the original with a YAML frontmatter header prepended (body unchanged).

How it splits: every walkthrough carries a standardized
`## TABLE OF CONTENTS ... END OF TABLE OF CONTENTS` block. We parse its entries
and locate each entry's header in the body. The matcher is **source-agnostic** and
auto-detects two TOC styles (`code_mode` = majority of entries carry a `[CODE]`):
  * plain `enum. Title` (darkslime etc.) — after stripping leading decoration the
    header line starts with the entry's enumerator + title; anchored on
    ``^<enum>[.)] <title-words-as-subsequence>`` (the enumerator prefix avoids
    prose false-positives), matched sequentially in TOC order (disambiguates
    repeated titles like "Madra").
  * GameFAQs `Title ..... [CODE]` Ctrl+F guides (cloud-blazer etc.) — anchored on
    the unique `[CODE]` tag in the body, searched globally and sorted by body
    position (so a TOC ordered differently from the body still works).

Two expected mismatch classes are handled, not silently dropped:
  * **container entries** — a TOC grouping (e.g. "2. CONTINENT OF INDRA") that has
    no body header of its own; its located children cover the text. Reported as
    info, not a failure.
  * **author drift** — body renumbers/retitles a section vs the TOC (e.g. TOC
    "VI > 6 Legal info and Credits" but body "5. Legal Stuff and Credits"). Fixed
    by a per-source `ALIASES` override: toc_path -> `(enum, title)`, or
    `(enum, title, code)` for a code guide. Genuinely-absent sections (unfinished
    guides) are left as known gaps.

`--dry-run` computes + `--verify`s without writing any files — use it to re-check a
source that has already been tag-edited (a normal run deletes+rewrites its
chapters, which would wipe the Stage-2 tags).

Frontmatter written per chapter (mechanical layer only; semantic layer left blank
for a later Gemini tagging pass):
    source_id, parent, chapter_no, toc_path, title, source_lines (1-based,
    inclusive, into the ORIGINAL file — the provenance bridge back to raw),
    kind: "", covers: [], region: "".

  python scripts/walkthrough_split.py --source darkslime          # split one
  python scripts/walkthrough_split.py --source darkslime --verify # + check
  python scripts/walkthrough_split.py --list                      # known sources

`--verify` reconstructs the original body from the chapter slices and asserts it
is byte-identical, and reports any TOC entry whose header was not found.
"""
import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = ROOT / "raw" / "gs2" / "Guide and Walkthrough"
OUT_ROOT = ROOT / "raw" / "gs2" / "_chapters"

# source_id -> filename (all 10 gs2 Guide-and-Walkthrough sources).
SOURCES = {
    "autocon": "Guide and Walkthrough by Autocon.md",
    "cloud-blazer": "Guide and Walkthrough by Cloud_Blazer.md",
    "darkslime": "Guide and Walkthrough by Darkslime.md",
    "darthmarth": "Guide and Walkthrough by DarthMarth.md",
    "ikillkenny": "Guide and Walkthrough by Ikillkenny.md",
    "killerfusion": "Guide and Walkthrough by KillerFusion.md",
    "shotgunnova": "Guide and Walkthrough by Shotgunnova.md",
    "super-slash": "Guide and Walkthrough by Super_Slash.md",
    "telago": "Guide and Walkthrough by Telago.md",
    "strawhat": "Guide and Walkthrough by strawhat.md",
}

# Per-source overrides for entries the author renumbered/retitled in the body.
# toc_path -> (body_enum, body_title, body_code [optional]) to anchor on instead of the TOC's.
ALIASES = {
    "darkslime": {
        "VI > 5": ("4", "Conclusion"),
        "VI > 6": ("5", "Legal Stuff and Credits"),
    },
    "cloud-blazer": {
        "VII > OSC2": ("", "Osenia Cliffs/ Madra Drawbridge Revisited", "OCMD"),
        "VII > TRSL": ("", "Treasure Isle", "TRSLI"),
    },
    "autocon": {},
    "ikillkenny": {
        "chapter-4 > 5": ("5", "Kandorean Temple"),
        "chapter-4 > 34": ("34", "Djinn in Apojii Island and Gabomba Catacombs"),
        "chapter-4 > 44": ("44", "Taopo Swamp"),
        "chapter-4 > 46": ("46", "The Sea of Time"),
        "chapter-5 > 5": ("5", "Aqua Hydra"),
        "chapter-5 > 9": ("9", "Moapa"),
    },
    "killerfusion": {
        "9": ("9", "Credits", "GS090")
    },
    "shotgunnova": {
        "III > 03": ("03", "Shrine of the Sea God", ""),
        "III > 35": ("35", "The Western Sea", "")
    },
    "telago": {
        "4.1": ("4A", "Trapping a scorpion in the desert"),
        "4.2": ("4B", "The pirates' hideout in Alhafra"),
        "5": {
            "Revealing lycanthropy of the wind tribe": ("5", "Revealing Lycanthropy of Wind Tribe")
        },
        "16": ("16", "Mars Lighthouse behind the northern reaches"),
        "17": ("", "Mars Lighthouse"),
        "2": {
            "About the Summon": ("2", "About the Summons")
        },
        "7": {
            "Psynergy Spells": ("8", "I Psynergy Spells - Field")
        },
        "8": {
            "Weapon Unleash Attacks": ("9", "Weapon Unleash Attacks")
        },
        "9": {
            "Monster Compendium": ("10", "Monster Compendium")
        }
    }
}

# Programmatic autocon aliases
ALIASES["autocon"].update({
    "1 > 1.7 > 1.7f": ("1.7f", "Djinn Run"),
    "2 > 2.7 > 2.7f": ("2.7f", "Djinn Run"),
    "4 > 4.1": ("4.1", "Squire"),
    "3 > 3.5 > 3.5b": ("3.5c", "Mars Djinn"),
    "3 > 3.5 > 3.5c": ("3.5d", "Jupiter Djinn"),
    "3 > 3.5 > 3.5d": ("3.5b", "Mercury Djinn"),
})
for c, title in zip("abcdefghijk", ["Cannon", "Spark", "Kindle", "Char", "Coal", "Reflux", "Core", "Tinder", "Shine", "Fury", "Fugue"]):
    ALIASES["autocon"][f"3 > 3.2 > 3.2{c}"] = (f"3.3{c}", title)
for c, title in zip("abcdefghijk", ["Breath", "Blitz", "Ether", "Waft", "Haze", "Wheeze", "Aroma", "Whorl", "Gasp", "Lull", "Gale"]):
    ALIASES["autocon"][f"3 > 3.3 > 3.3{c}"] = (f"3.4{c}", title)
for c, title in zip("abcdefghijk", ["Fog", "Sour", "Spring", "Shade", "Chill", "Steam", "Rime", "Gel", "Eddy", "Balm", "Serac"]):
    ALIASES["autocon"][f"3 > 3.4 > 3.4{c}"] = (f"3.2{c}", title)
for i in range(1, 9):
    c = chr(ord('a') + i - 1)
    ALIASES["autocon"][f"7 > 7.6 > 7.6{c}"] = (f"7.6{c}", f"Char {i}")
for c, title in zip("abcdefghijk", [
    "Earth Adept 1", "Earth Adept 2", "Earth Adept 3",
    "Fire Adept 1", "Fire Adept 2", "Fire Adept 3",
    "Wind Adept 1", "Wind Adept 2",
    "Water Adept 1", "Water Adept 2", "Water Adept 3"
]):
    ALIASES["autocon"][f"7 > 7.7 > 7.7{c}"] = (f"7.7{c}", title)

ENUM_RE = re.compile(r"^(?:(\d+(?:\.\d+[a-z]?)?)[.)\s]\s*|([A-Za-z]|[IVXLC]+)(?:[.)]\s+|\.+))(.*)$")


def words(s):
    return re.sub(r"[^a-z0-9]+", " ", s.lower()).split()


def is_subseq(small, big):
    it = iter(big)
    return all(w in it for w in small)


def strip_decoration(line):
    return re.sub(r"^[^A-Za-z0-9]+", "", line)


def split_frontmatter(lines):
    """Return index of first body line after a leading --- ... --- block (or 0)."""
    if lines and lines[0].strip() == "---":
        for i in range(1, len(lines)):
            if lines[i].strip() == "---":
                return i + 1
    return 0


def parse_toc(lines, source_id=None):
    """Parse the standardized TOC into ordered entries: [{enum,title,code,depth,
    toc_path}]. Source-agnostic — handles plain `enum. Title` guides AND GameFAQs
    `Title ........ [CODE]` Ctrl+F-anchored guides (and mixes). `enum`/`code` may
    be "" / None per entry; `toc_path` keys on enum, else code, else slug."""
    start = next(i for i, l in enumerate(lines) if "TABLE OF CONTENTS" in l)
    end = next(i for i, l in enumerate(lines[start:], start) if "END OF TABLE OF CONTENTS" in l)
    
    # Preprocess lines to join wrapped lines
    toc_lines = lines[start + 1:end]
    joined_lines = []
    i = 0
    while i < len(toc_lines):
        curr_line = toc_lines[i].rstrip()
        has_enum = bool(re.match(rf"^\s*(?:[IVXLC]+|[A-Za-z]|\d+)[.)]", curr_line))
        has_code = bool(re.search(r"(?:\[|-)[A-Za-z0-9]+(?:\]|-)\s*$", curr_line))
        if has_enum and not has_code and i + 1 < len(toc_lines):
            next_line = toc_lines[i + 1].strip()
            next_has_enum = bool(re.match(rf"^\s*(?:[IVXLC]+|[A-Za-z]|\d+)[.)]", next_line))
            next_has_code = bool(re.search(r"(?:\[|-)[A-Za-z0-9]+(?:\]|-)\s*$", next_line))
            if next_has_code and not next_has_enum:
                curr_line = curr_line + " " + next_line
                i += 1
        joined_lines.append((toc_lines[i], curr_line))
        i += 1
        
    entries = []
    stack = []  # (indent, key)
    for raw_l, l in joined_lines:
        indent = len(re.match(r"[ \t]*", raw_l).group().expandtabs())
        cm = re.search(r"\[([A-Za-z0-9]+)\]\s*$", l)           # trailing [CODE]
        if not cm:
            cm = re.search(r"-([A-Za-z0-9]+)-\s*$", l)          # trailing -CODE-
        if not cm and source_id == "shotgunnova":
            cm = re.search(r"\b([A-Z0-9]{4})\s*$", l)           # trailing 4-char code
        code = cm.group(1) if cm else None
        label = (l[:cm.start()] if cm else l)
        label = re.sub(r"[\s.]+$", "", label)                  # drop trailing dots and spaces
        core = re.sub(r"^-+\s*", "", re.sub(r"^[\s*]+", "", label)).strip()
        m = ENUM_RE.match(core)
        enum, title = (m.group(1) or m.group(2), m.group(3).strip()) if m else ("", core)
        
        # Special handling for Chapter headers in ikillkenny
        if not enum and not code and source_id == "ikillkenny":
            ch_match = re.match(r"^=?Chapter\s+(\d+):?\s*(.*)$", core, re.I)
            if ch_match:
                enum = "chapter-" + ch_match.group(1)
                title = ch_match.group(2).strip()

        # Special handling for strawhat
        if source_id == "strawhat":
            m_straw = re.match(r"^[{[]([0-9.]+)[}\]]\s*(.*)$", core)
            if m_straw:
                enum = m_straw.group(1)
                title = m_straw.group(2).strip()

        if not re.search(r"[A-Za-z0-9]", title):                # legend / rule line
            continue
        if "table of contents" in title.lower():                # skip TOC helper/note lines
            continue
        if not enum and not code:                               # skip non-entry explanation lines
            continue
        key = enum or code or slug(title)
        while stack and stack[-1][0] >= indent:
            stack.pop()
        path = [s[1] for s in stack] + [key]
        stack.append((indent, key))
        entries.append({"enum": enum, "title": title, "code": code,
                        "depth": len(path), "toc_path": " > ".join(path)})
    return entries, end


def find_anchor(body, start, enum, title, code=None, source_id=None):
    """Body line index of an entry's header, or None. `code` -> the unique
    `[CODE]` or `(CODE)` tag (anywhere on the line); else the entry's enumerator + title as a
    word-subsequence, after stripping leading decoration. Empty enum -> title only."""
    if code:
        pat = re.compile(rf"\b{re.escape(code)}\b", re.I)
        for i in range(start, len(body)):
            if pat.search(body[i]):
                return i
        return None
    tw = words(title)
    if not tw:
        return None
    if enum:
        if source_id == "ikillkenny":
            pat = re.compile(rf"^{re.escape(enum)}[.):\s]\s*", re.I)
        elif source_id == "strawhat":
            pat = re.compile(rf"^{re.escape(enum)}[.)\]}}\s]\s*", re.I)
        elif re.search(r"\d", enum):
            pat = re.compile(rf"^{re.escape(enum)}[.)\s]\s*", re.I)
        else:
            pat = re.compile(rf"^{re.escape(enum)}[.)]\s*", re.I)
    else:
        pat = None
    for i in range(start, len(body)):
        s = strip_decoration(body[i])
        if source_id == "ikillkenny":
            s = re.sub(r"^Section\s+", "", s, flags=re.I)
        if pat:
            m = pat.match(s)
            if m and is_subseq(tw, words(s[m.end():])):
                return i
        elif words(s)[:len(tw)] == tw:                 # no enum: title at line start
            return i
    return None


def slug(s):
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", s.lower())).strip("-")[:50]


def split_source(source_id, verify=False, dry_run=False):
    path = RAW_DIR / SOURCES[source_id]
    text = path.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines(keepends=True)

    entries, toc_end = parse_toc(lines, source_id=source_id)
    body_start = toc_end + 1
    aliases = ALIASES.get(source_id, {})

    # mark container entries (a deeper entry immediately follows)
    for i, e in enumerate(entries):
        e["container"] = i + 1 < len(entries) and entries[i + 1]["depth"] > e["depth"]

    # Code-anchored guides (GameFAQs [CODE] Ctrl+F tags): codes are unique, so
    # search the whole body and sort by position (TOC order may differ from body
    # order). Plain guides: sequential cursor in TOC order (disambiguates repeated
    # titles like "Madra" appearing twice).
    code_mode = sum(1 for e in entries if e["code"]) >= max(1, len(entries)) / 2
    search_from_start = code_mode or source_id == "autocon"
    cursor = body_start
    missed = []
    for e in entries:
        alias_val = aliases.get(e["toc_path"])
        if isinstance(alias_val, dict):
            alias_val = alias_val.get(e["title"])
        if alias_val:
            enum, title, code = alias_val if len(alias_val) == 3 else (*alias_val, e["code"])
        else:
            enum, title, code = e["enum"], e["title"], e["code"]
        idx = find_anchor(lines, body_start if search_from_start else cursor, enum, title,
                          code=code if code_mode else None, source_id=source_id)
        e["line"] = idx
        if idx is None:
            missed.append(e)
        elif not search_from_start:
            cursor = idx + 1

    located = sorted((e for e in entries if e["line"] is not None), key=lambda e: e["line"])

    # chunk boundaries: [front preamble] + each located entry up to the next one
    bounds = [(0, located[0]["line"] if located else len(lines), None)]
    for k, e in enumerate(located):
        nxt = located[k + 1]["line"] if k + 1 < len(located) else len(lines)
        bounds[0] = (0, located[0]["line"], None) if k == 0 else bounds[0]
        bounds.append((e["line"], nxt, e))

    out_dir = OUT_ROOT / source_id
    written = []
    for n, (a, b, e) in enumerate(bounds):
        body = "".join(lines[a:b])
        if e is None:
            title, toc_path, name = "(front matter)", "", "00-front"
        else:
            title, toc_path = e["title"], e["toc_path"]
            name = f"{n:02d}-{slug(title) or 'untitled'}"
        fm = (
            "---\n"
            f"source_id: {source_id}\n"
            f"parent: {SOURCES[source_id]}\n"
            f"chapter_no: {n}\n"
            f'toc_path: "{toc_path}"\n'
            f'title: "{title}"\n'
            f"source_lines: {a + 1}-{b}\n"
            "kind:        # prose-walkthrough | data-table | story | meta\n"
            "covers: []   # entities: locations | monsters | items | ...\n"
            "region:      # canonical game-progression region (fill at consolidation)\n"
            "---\n"
        )
        written.append((name, a + 1, b, title, fm + body))

    if not dry_run:
        out_dir.mkdir(parents=True, exist_ok=True)
        for f in out_dir.glob("*.md"):
            f.unlink()
        for name, _, _, _, content in written:
            (out_dir / f"{name}.md").write_text(content, encoding="utf-8")

    tag = "DRY-RUN " if dry_run else ""
    print(f"[{source_id}] {tag}{len(entries)} TOC entries, {len(located)} located, "
          f"{len(written)} chapters -> {out_dir.relative_to(ROOT)}")
    containers = [e for e in missed if e["container"]]
    true_missed = [e for e in missed if not e["container"]]
    if containers:
        print(f"  i  {len(containers)} container entries (no own body header; "
              f"covered by children): {[e['toc_path'] for e in containers]}")
    if true_missed:
        print(f"  !! {len(true_missed)} entries NOT located (add ALIASES / known gap):")
        for e in true_missed:
            print(f"     - {e['toc_path']:18} {e['title']!r}")

    if verify:
        recon = "".join(
            "".join(lines[a:b]) for a, b, _ in bounds)
        assert recon == text, "RECONSTRUCTION MISMATCH — chapters are not byte-exact!"
        print("  verify: byte-exact reconstruction OK")
    return written, missed


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--source")
    ap.add_argument("--verify", action="store_true")
    ap.add_argument("--dry-run", action="store_true",
                    help="compute + verify without writing files (won't clobber tags)")
    ap.add_argument("--list", action="store_true")
    args = ap.parse_args()
    if args.list:
        for sid, fn in SOURCES.items():
            print(f"  {sid:14} {fn}")
        return
    if not args.source:
        ap.error("pass --source <id> (or --list)")
    split_source(args.source, verify=args.verify, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
