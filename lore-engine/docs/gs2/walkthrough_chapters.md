# GS2 — Walkthrough Chapter Pipeline (split + tag)

> Turn the 10 giant `raw/gs2/Guide and Walkthrough/*.md` (each thousands of lines)
> into a **derived** per-chapter layer: `raw/gs2/_chapters/<source_id>/NN-<slug>.md`,
> each chapter a **byte-exact slice** of the original with a YAML frontmatter
> header prepended. Serves three downstream uses: targeted **extraction**
> (locations / flow / cross-check), walkthrough **consolidation**, and
> **translation**. Most of this is meant to run in **Antigravity CLI (Gemini)** to
> save Claude usage; the split step is a free deterministic script.

## Immutability rule (unchanged)

`raw/gs2/.../*.md` are **immutable sources** — never edited. This `_chapters/`
tree is *derived*: bodies are copied verbatim (the `source_lines` frontmatter is
the exact 1-based line range back into the original, so any chapter is provably
`raw[a:b]`). The split script `--verify`s byte-exact reconstruction. Nothing here
replaces raw; it's a convenience/index layer.

## Folder layout

```
raw/gs2/_chapters/
  README.md
  <source_id>/
    00-front.md            # title banner + TOC + preamble (kind: meta)
    01-<slug>.md … NN-<slug>.md
```

## Frontmatter (two layers)

```yaml
---
# --- mechanical layer: filled by scripts/walkthrough_split.py (deterministic) ---
source_id: darkslime
parent: Guide and Walkthrough by Darkslime.md
chapter_no: 8
toc_path: "IV > 2 > A"          # nested TOC position (provenance / region mapping)
title: "Daili"
source_lines: 399-444           # 1-based inclusive range into the ORIGINAL file
# --- semantic layer: filled by the Gemini tagging pass (judgment) ---
kind:        # prose-walkthrough | data-table | story | meta
covers: []   # entities the chapter has usable data for (see vocab below)
region:      # in-game area/location this chapter covers (free text for now)
---
<body — verbatim slice, never edited>
```

## Pipeline — two stages **per source** (one Antigravity round each, ~per file)

### Stage 1 — split (deterministic, free; no LLM)

```bash
python scripts/walkthrough_split.py --list                       # show sources
python scripts/walkthrough_split.py --source <id> --verify       # split + check
```
Steps (Antigravity, agentic):
1. Ensure `<id>` is in `SOURCES` (all 10 are pre-filled).
2. Run with `--verify`. It must print **`verify: byte-exact reconstruction OK`**.
3. Resolve any `!! entries NOT located`:
   - **container** misses are auto-downgraded (info line) — fine, ignore.
   - a **true miss** = the author renumbered/retitled vs the TOC. Open the body,
     find the real header, add a `ALIASES["<id>"]["<toc_path>"] = ("<enum>",
     "<title>")` override, re-run. If a section is genuinely absent (unfinished
     guide), leave it — note it in the tracker.
4. Done when `--verify` is OK and remaining misses are only known gaps.

> The matcher strips leading decoration and anchors on `^<enum>[.)] <title>`
> (title matched as a word-subsequence), so it is format-agnostic across authors.

### Stage 2 — tag (Gemini; the reusable LLM task)

Fill the **semantic** frontmatter (`kind`, `covers`, `region`) of each chapter in
`_chapters/<id>/`. Edit only those three keys — **never touch the body or the
mechanical fields**. Prompt + vocab below.

**`kind`** (exactly one):
- `prose-walkthrough` — step-by-step area/dungeon walkthrough prose.
- `data-table` — tables/lists (bestiary, item/djinn/psynergy/class indexes, shops).
- `story` — plot recap / dialogue / character bios (no extractable game data).
- `meta` — intro, version history, controls, legal, FAQ, credits, TOC/front.

**`covers`** (zero or more; only when the chapter genuinely carries that data):
`locations, monsters, bosses, items, equipment, djinn, summons, psynergy,
classes, characters, shops, forging, transfer, walkthrough`.
(`walkthrough` = the flow itself, for the consolidation use.)

**`region`**: the in-game area/location the chapter is about, free text from the
title/content (e.g. `Idejima`, `Daila`, `Kandorean Temple`). Blank for
`meta`/`story`/index chapters. (A canonical region taxonomy is a later,
consolidation-time pass — don't force it now.)

#### Gemini tagging prompt (copy-paste, run per source folder)

```
You are tagging derived walkthrough chapter files for a Golden Sun: The Lost Age
knowledge base. For every .md file in raw/gs2/_chapters/<id>/:

1. Read the YAML frontmatter and the body.
2. Set exactly these three frontmatter keys, IN PLACE:
   - kind:   one of prose-walkthrough | data-table | story | meta
   - covers: a YAML list of entities the body has usable data for, from:
       [locations, monsters, bosses, items, equipment, djinn, summons,
        psynergy, classes, characters, shops, forging, transfer, walkthrough]
   - region: the in-game area/location this chapter is about (free text), or
             leave blank for meta/story/index chapters.
3. DO NOT modify the body, or any other frontmatter field (source_id, parent,
   chapter_no, toc_path, title, source_lines). DO NOT reword or reformat anything.
4. Judge from what is actually present — do not invent coverage. If unsure
   between data-table and prose-walkthrough, pick by what dominates the body.

Output = the edited files only. Then print a one-line summary per file:
  <filename>  kind=<..> covers=[..] region=<..>
```

After Gemini runs, Claude (me) spot-audits a few files per source.

## Model recommendation (your Antigravity options)

| Task | Model | Why |
|---|---|---|
| **Split** | — (none) | deterministic Python; no model. |
| **Tag** (kind/covers/region) | **Gemini 3.5 Flash (High)** | cheap, fast; classification is easy, High for reliability. |
| **Extract** prose → schema JSON (later) | **Gemini 3.1 Pro (High)** or **Claude Sonnet 4.6 (Thinking)** | needs reasoning + faithfulness; Sonnet if you want max fidelity. |
| **Translate** (later) | **Gemini 3.5 Flash (High)** (bulk) / Pro for polish | translation is Flash-friendly; Pro for literary quality. |

Avoid `Low` tiers for anything touching data faithfulness. Reserve the Claude
models in Antigravity for extraction/conflict-heavy work, not bulk tagging.

## Progress tracker

| source_id | split | verify | tagged | chapters | notes |
|---|---|---|---|---|---|
| darkslime | ✅ | ✅ | ⬜ | 42 | **reference run.** 5 containers; 1 known gap (IV>2>E Indran Easternland Beach absent — guide is v0.2 unfinished). |
| autocon | ⬜ | ⬜ | ⬜ | — | |
| cloud-blazer | ⬜ | ⬜ | ⬜ | — | locations source (most detailed regions). |
| darthmarth | ⬜ | ⬜ | ⬜ | — | |
| ikillkenny | ⬜ | ⬜ | ⬜ | — | boss strategy. |
| killerfusion | ⬜ | ⬜ | ⬜ | — | |
| shotgunnova | ⬜ | ⬜ | ⬜ | — | shops/items appendices. |
| super-slash | ⬜ | ⬜ | ⬜ | — | |
| telago | ⬜ | ⬜ | ⬜ | — | djinn/summon appendices. |
| strawhat | ⬜ | ⬜ | ⬜ | — | |

> Update this table per Antigravity round. `split`/`verify` = Stage 1 clean;
> `tagged` = Stage 2 done + Claude spot-audit passed.

## Notes / gotchas (sediment as sources are processed)

- darkslime: author renumbers VI in the body (TOC "5. Conclusion / 6. Legal info"
  → body "4. Conclusion / 5. Legal **Stuff**"); handled via `ALIASES["darkslime"]`.
  Expect similar TOC-vs-body drift on other authors → resolve with `ALIASES`.
- Chapter granularity = the finest TOC level the author actually headers in the
  body (darkslime → area level: Daila, Kandorean Temple, …). Good for locations.
- Walkthrough data chapters (bestiary/item/djinn appendices) largely **overlap**
  the In-Depth Guides we already extracted deterministically — so for *new*
  extraction the high-value chapters are `kind: prose-walkthrough` (locations +
  flow). Tagging makes that routing trivial.
