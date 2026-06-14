# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository layout

`Project_Genkai` is a monorepo of "boundary experiments." Each subfolder is an
independent project. The only active subproject today is **`lore-engine/`**.

Note the two sibling directories on disk: `Project_Genkai` (underscore) is the
git repository and holds all code; `Project Genkai` (space) holds only local
`.claude/` settings and is not version-controlled. Work in the underscore one.

## lore-engine

A schema-driven pipeline that turns unstructured long-form text (GameFAQs FAQs,
and eventually work SOPs / docs) into structured, queryable JSON knowledge
bases. The prototype corpus is Golden Sun 1 (`gs1`); the design generalizes to
any `{game}`/domain by swapping the raw corpus and schema.

### Pipeline architecture

```
raw/{game}/*.txt   →   schema/{game}_schema.md   →   scripts/extract.py   →   data/{game}/{entity}.json   →   tools/*.html
(source FAQs)          (field defs + source map)     (Claude API call)        (structured output)             (single-file explorers)
```

The **schema file is the control plane** — `extract.py` reads it, not hardcoded
config. Two parts of `schema/{game}_schema.md` drive everything:

- **`### Master Source IDs` table** — maps short source IDs (e.g. `telago`,
  `fandom-tret`) to documents. `extract.py` parses the backticked first cell of
  each row, then token-matches each ID against filenames in `raw/{game}/` (split
  ID on `-`/`_`; a file matches only if *every* token is a substring of its
  normalized stem; most-specific/shortest wins). Add a row here whenever a new
  source file is ingested.
- **`## Schema: {entity}` sections** — one per entity (`djinn`, `bosses`,
  `equipment`, `classes`, `psynergy`). Everything from that `## ` heading to the
  next `## ` (field table, enums, examples, "Notes for CC") is sent to Claude
  verbatim as the extraction spec for that entity.

`extract.py` then builds a prompt (schema section + matched raw files + a
JSON-only instruction), streams from `claude-sonnet-4-6`, and writes a JSON
array to `data/{game}/{entity}.json`. On a JSON parse failure it dumps the raw
model output to `data/{game}/{entity}_raw_response.txt` for debugging — these
`_raw_response.txt` files are debug artifacts, not pipeline output.

### Running the extractor

```bash
# from inside lore-engine/  (REPO_ROOT = the lore-engine folder, the scripts/ parent)
pip install anthropic python-dotenv          # no requirements.txt; these two deps
python scripts/extract.py --entity bosses --game gs1
python scripts/extract.py --entity djinn     # --game defaults to gs1
python scripts/extract.py --entity bosses --dry-run   # resolve schema + files, no API call
```

`ANTHROPIC_API_KEY` must be in `lore-engine/.env` (loaded via python-dotenv) or
the environment. Use `--dry-run` first when changing schema sections or source
files to confirm the right raw files resolve before spending an API call.

### The walkthrough sub-pipeline (separate from extract.py)

`data/gs1/gs1_walkthrough.md` is NOT produced by `extract.py`. The four source
walkthroughs total ~1.3 MB and exceed a single context window, so the
walkthrough is built by a manual, multi-agent batching process: chapter-range
batches extracted by parallel subagents against
`schema/gs1_walkthrough_template.md`, each agent reading ≤~150 KB of raw text at
a time. See `docs/gs1_walkthrough_extraction_plan.md` for the batch strategy and
progress. `_batch_*.md` files in `data/gs1/` are intermediate batch artifacts.

### The HTML explorers

`tools/*.html` are standalone single-file apps. Data is **embedded** in
`<script type="application/json" id="data-...">` blocks and read via
`JSON.parse(...)` — they do not `fetch` the JSON files. Consequence: after
regenerating a `data/{game}/*.json`, the corresponding embedded block in the
explorer must be re-pasted by hand; the tool will not pick up changes
automatically.

## Schema/data conventions

These rules (from `schema/gs1_schema.md` → "General Rules") apply to all
extracted JSON and any hand-edits:

- Field names are `snake_case`; string values are `lowercase` except proper
  nouns (`"Flint"`, `"Vale"`).
- `0` means a confirmed-zero stat; `null` means missing/unconfirmed across all
  sources. They are not interchangeable.
- Every entry carries a `sources` array of source IDs that contributed to it.
- On a cross-source conflict, do **not** silently pick a winner — flag it with
  the `conflicts` field (JSON) or a `[^note]` footnote (walkthrough markdown).
