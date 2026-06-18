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
python scripts/walkthrough_split.py --list                          # show sources
python scripts/walkthrough_split.py --source <id> --verify          # split + check
python scripts/walkthrough_split.py --source <id> --dry-run --verify # check, NO write
```
Steps (Antigravity, agentic):
1. Ensure `<id>` is in `SOURCES` (all 10 are pre-filled).
2. Run with `--verify`. It must print **`verify: byte-exact reconstruction OK`**.
3. Resolve any `!! entries NOT located`:
   - **container** misses are auto-downgraded (info line) — fine, ignore.
   - a **true miss** = the author renumbered/retitled vs the TOC. Open the body,
     find the real header, add a `ALIASES["<id>"]["<toc_path>"] = ("<enum>",
     "<title>")` override (or `("<enum>", "<title>", "<CODE>")` for a code guide),
     re-run. If a section is genuinely absent (unfinished guide), leave it — note
     it in the tracker.
4. Done when `--verify` is OK and remaining misses are only known gaps.

> The matcher is **source-agnostic** and auto-detects two TOC styles:
> - plain `enum. Title` → anchors on `^<enum>[.)] <title>` (title as a word
>   subsequence, after stripping leading decoration), sequential in TOC order.
> - GameFAQs `Title ..... [CODE]` (Ctrl+F tags) → anchors on the unique `[CODE]`
>   in the body; codes searched globally + sorted by body position (handles a TOC
>   whose order differs from the body, e.g. cloud-blazer's FAQs/Side-Quests swap).
>
> ⚠️ **Re-running split deletes+rewrites a source's chapter files** — it would wipe
> the Stage-2 tags. So never re-split a source after it's tagged. To re-verify a
> tagged source non-destructively, use `--dry-run` (computes + verifies, writes
> nothing).

### Stage 2 — tag (Gemini; the reusable LLM task)

Fill the **semantic** frontmatter (`kind`, `covers`, `region`) of each chapter in
`_chapters/<id>/`. Edit only those three keys — **never touch the body or the
mechanical fields**. Prompt + vocab below.

**`kind`** (exactly one):
- `prose-walkthrough` — area/dungeon/boss walkthrough written as prose. **Boss-fight
  strategy in prose is `prose-walkthrough`, NOT `data-table`.**
- `data-table` — the body is *dominated by a table or list* (bestiary, item / djinn /
  psynergy / class index, shop stock). A prose section that merely contains a small
  stat line is not `data-table`.
- `story` — plot recap / dialogue / character bios; no extractable structured data.
- `meta` — intro, version history, controls, **mechanics overviews (battle / djinn /
  menu basics)**, legal, FAQ, credits, contact, TOC/front, AND any chapter that is
  only a 1–3 line section header/banner.

**`covers`** — the threshold is **extractable-data, NOT mention**. Include an entity
only if this chapter is a place you'd actually go to *extract or learn* that entity's
data: it has a list/table/stat-block for it, the entity is **obtained/learned here**,
or an **encounter is described** with real detail. Do **not** include an entity that
is merely name-dropped (e.g. "use Ragnarok" ≠ `psynergy`; "a Summon helps here" ≠
`summons`; a Djinn list naming each character/element ≠ `characters`/`classes`).
> Test per entity X: *would an X-extractor want to read this chapter?* Yes → include.
> Just mentioned in passing → exclude.

Vocab: `locations, monsters, bosses, items, equipment, djinn, summons, psynergy,
classes, characters, shops, forging, transfer, walkthrough` (`walkthrough` = the
flow itself, for consolidation).

**Hard rules** (these are exactly where the first tagging pass went wrong):
- `meta` and `story` chapters → **`covers: []`** (almost always). `00-front` and all
  intro/version/controls/mechanics/legal/FAQ/credits/contact → `kind: meta`,
  `covers: []`, `region:` blank. **Always.**
- A **pure index/list** chapter → `data-table`, and `covers` = **only the one entity
  it lists** (a "Djinn List" → `[djinn]`, not `[characters, classes, items, …]` just
  because those appear as column values).
- A **walkthrough area** chapter → `locations` + `walkthrough` almost always; then add
  only entities with real content *here*: `items` (pickups listed), `monsters`/`bosses`
  (encounters described), `djinn` (a Djinni is obtained here), `psynergy`/`summons`
  (learned/obtained here), `shops` (stock given), `forging` (described), `equipment`
  (named equippable pickups), `characters` (a member joins here), `transfer` (GS1
  linkage/password here).

**`region`**: the primary in-game area (one), free text (e.g. `Idejima`, `Daila`).
Blank for `meta`/`story`/index. If a chapter spans several areas, use the main/first.
(A canonical region taxonomy is a later consolidation pass — don't force it now.)

#### Gemini tagging prompt (copy-paste, run per source folder)

```
You are tagging derived walkthrough chapter files for a Golden Sun: The Lost Age
knowledge base. For every .md file in raw/gs2/_chapters/<id>/, set exactly three
frontmatter keys IN PLACE — kind, covers, region — and change NOTHING else (not the
body, not source_id/parent/chapter_no/toc_path/title/source_lines). Don't reformat.

kind (one): prose-walkthrough | data-table | story | meta
  - boss-fight strategy in prose = prose-walkthrough (NOT data-table)
  - data-table only when the body is dominated by a table/list
  - meta = intro/version/controls/mechanics-overview/legal/FAQ/credits/contact/front,
    or any chapter that is just a 1-3 line header/banner

covers (list; threshold = EXTRACTABLE DATA, not mention): include an entity only if
the chapter is somewhere you'd go to extract/learn it — it has a list/table/stat-block
for it, the entity is obtained/learned here, or an encounter is described in detail.
Do NOT add an entity merely name-dropped as a tactic/aside. Vocab: [locations,
monsters, bosses, items, equipment, djinn, summons, psynergy, classes, characters,
shops, forging, transfer, walkthrough].
  HARD RULES:
  - meta/story chapters -> covers: []  (00-front is ALWAYS meta + covers: [])
  - a pure index/list -> covers is ONLY the one entity it lists
  - a walkthrough area -> usually [locations, walkthrough] + only the entities with
    real content here (items if pickups listed, monsters/bosses if encounters
    described, djinn if obtained here, etc.)

region: the primary in-game area (free text); blank for meta/story/index.

Print one line per file: <filename>  kind=<..> covers=[..] region=<..>
```

After a tagging pass, Claude (me) spot-audits per source (see the audit report
`walkthrough_chapters_audit.md`).

## Antigravity kickoff (per-source rounds)

Set the model to **Gemini 3.5 Flash (High)**. Set the `/goal` **once** per session,
then paste the per-source prompt for each source (swap `<id>`).

### `/goal` (set once)

```
/goal Run the gs2 walkthrough chapter pipeline in the lore-engine repo: for each
Guide-and-Walkthrough source, deterministically split it into per-chapter files
under raw/gs2/_chapters/<id>/ and tag each chapter's semantic frontmatter
(kind/covers/region). Follow docs/gs2/walkthrough_chapters.md exactly. HARD RULES:
never edit the raw sources under "raw/gs2/Guide and Walkthrough/" (immutable);
chapter bodies are byte-exact slices — never reword/reformat them; split ONLY via
scripts/walkthrough_split.py (deterministic), never by hand; every split must print
"verify: byte-exact reconstruction OK"; tagging sets only kind/covers/region and
nothing else; do not invent data.
```

### Per-source prompt (one round each)

```
Do source_id = <id> through both stages (read docs/gs2/walkthrough_chapters.md
and the finished raw/gs2/_chapters/cloud-blazer/ first to match the pattern).

STAGE 1 — split (deterministic; no LLM):
- Run: python scripts/walkthrough_split.py --source <id> --verify
- It MUST print "verify: byte-exact reconstruction OK".
- For each "!! entries NOT located": open the raw file in
  "raw/gs2/Guide and Walkthrough/", find the header the author actually used, and
  add an override in scripts/walkthrough_split.py:
  ALIASES["<id>"]["<toc_path>"] = ("<enum>", "<title>")   # add a 3rd "<CODE>" for a [CODE] guide
  then re-run. "container" info lines are fine — ignore. If a section is truly
  absent (unfinished guide), leave it and note it in the tracker.
- Once you start Stage 2, do NOT re-run split (it deletes+rewrites the files and
  wipes tags); use --dry-run to re-verify.

STAGE 2 — tag (your judgment):
- For each file in raw/gs2/_chapters/<id>/, set kind / covers / region IN PLACE
  per the vocab in the runbook. Touch ONLY those three keys — never the body or the
  mechanical fields (source_id/parent/chapter_no/toc_path/title/source_lines). Don't
  reformat anything. Judge from what's actually in the body; don't invent coverage.

FINALLY: update the progress-tracker row for <id> in
docs/gs2/walkthrough_chapters.md, and print one line per chapter: file / kind /
covers / region.
```

Remaining sources: **darkslime** needs Stage 2 only (already split). Then
`autocon, darthmarth, ikillkenny, killerfusion, shotgunnova, super-slash, telago,
strawhat` need both stages. (`cloud-blazer` is done.)

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

`tagged`: ✅ = first pass done **and** audited clean; 🔄 = first pass done but a
re-tag with the tightened spec is pending (see audit below).

| source_id | split | verify | tagged | chapters | notes |
|---|---|---|---|---|---|
| darkslime | ✅ | ✅ | ✅ | 42 | **reference run.** 5 containers; 1 known gap (IV>2>E Indran Easternland Beach absent — guide is v0.2 unfinished). audit: PASS-with-notes. |
| autocon | ✅ | ✅ | ✅ | 325 | 9 known gaps (2.8b–2.8j, author stopped at 2.8a "coming soon"). audit: covers over-claim on meta/front. |
| cloud-blazer | ✅ | ✅ | ✅ | 95 | locations source (most detailed regions). audit: PASS-with-notes (under-tags djinn/psynergy). |
| darthmarth | ✅ | ✅ | ✅ | 39 | audit: under-tags equipment. |
| ikillkenny | ✅ | ✅ | ✅ | 88 | boss strategy. audit: boss chapters mis-tagged data-table + covers over-claim. |
| killerfusion | ✅ | ✅ | ✅ | 83 | audit: boss chapters mis-tagged data-table; index over-claim. |
| shotgunnova | ✅ | ✅ | ✅ | 69 | shops/items appendices. audit: severe covers inflation. |
| super-slash | ✅ | ✅ | ✅ | 20 | audit: severe covers UNDER-claim (monolithic walkthrough chapter). |
| telago | ✅ | ✅ | ✅ | 40 | djinn/summon appendices. audit: covers over-claim. |
| strawhat | ✅ | ✅ | ✅ | 54 | audit: severe covers inflation. |

> Update this table per Antigravity round. `split`/`verify` = Stage 1 clean;
> `tagged ✅` = Stage 2 done + audited clean.

### Audit 2026-06-18 (`walkthrough_chapters_audit.md`)

Independent audit of all 10 sources (855 chapters). **Objective layer all PASS**:
raw immutability (no source edited), split reproducibility (every source byte-exact),
and on-disk body integrity (all 855 chapter bodies == their `source_lines` raw slice,
**0 mismatches**). **Verdict FAIL was solely Stage-2 tagging consistency** — the first
pass lacked a firm `covers` threshold, so sources swung between over-claim
(shotgunnova/strawhat tag every entity that's mentioned) and under-claim
(super-slash/darthmarth). The Stage-2 spec above has been tightened accordingly; a
single re-tag pass over all 10 (below) resolves it.

## Notes / gotchas (sediment as sources are processed)

- darkslime: author renumbers VI in the body (TOC "5. Conclusion / 6. Legal info"
  → body "4. Conclusion / 5. Legal **Stuff**"); handled via `ALIASES["darkslime"]`.
  Expect similar TOC-vs-body drift on other authors → resolve with `ALIASES`.
- cloud-blazer: GameFAQs `[CODE]` Ctrl+F guide (auto-detected). Its TOC lists
  FAQs before Side-Quests but the body has them swapped — handled automatically
  (code anchors sorted by body position). Two codes the author changed between
  TOC and body fixed via `ALIASES["cloud-blazer"]` (OSC2→OCMD, TRSL→TRSLI).
- Chapter granularity = the finest TOC level the author actually headers in the
  body (darkslime → area level: Daila, Kandorean Temple, …). Good for locations.
- Walkthrough data chapters (bestiary/item/djinn appendices) largely **overlap**
  the In-Depth Guides we already extracted deterministically — so for *new*
  extraction the high-value chapters are `kind: prose-walkthrough` (locations +
  flow). Tagging makes that routing trivial.
- darthmarth: GameFAQs `-CODE-` / `(CODE)` guide (auto-detected). Its TOC contains multi-line wrapped entries (j, m, r) which are preprocessed and joined automatically in `parse_toc`. Lowercase letter enums supported.
