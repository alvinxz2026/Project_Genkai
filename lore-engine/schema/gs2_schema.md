# GS2 Schema (skeleton — to be filled during Design stage)

> Mirror `schema/gs1_schema.md` structure. This file is the **control plane**:
> `scripts/extract.py --game gs2` reads the `### Master Source IDs` table (to find
> raw files) and each `## Schema: {entity}` section (sent to Claude verbatim as the
> extraction spec). Nothing here drives anything until the tables below are filled.
>
> Plan / tracking: `docs/gs2/gs2_plan.md`.

## General Rules

GS2 follows the same conventions as GS1 (see `schema/gs1_schema.md` → "General
Rules"): `snake_case` fields; string values `lowercase` except proper nouns; `0`
= confirmed-zero vs `null` = missing/unconfirmed; every entry carries a `sources`
array; cross-source conflicts are **flagged** (`conflicts` field), never silently
merged. Restate or amend here once gs2-specific rules emerge.

### Master Source IDs

> Add one row per ingested file in `raw/gs2/`. The backticked first cell is the
> source ID `extract.py` token-matches against filenames. Populate as raw sources
> are collected + annotated (each raw file's `source_id` frontmatter → a row here).

| Source ID | Document | Author | Covers |
|---|---|---|---|
| _(tbd)_ | | | |

---

## Schema: entities (tbd)

> One `## Schema: {entity}` section per entity, copied from `gs1_schema.md` and
> adjusted for gs2. Likely starting set (mirror gs1's 11): djinn, summons, classes,
> psynergy, equipment, items, shops, monsters, bosses, locations, characters —
> plus gs2-new concepts (party transfer, new party members). Decide scope in the
> Idea stage before filling these.
