# lore-engine

A schema-driven pipeline that turns unstructured long-form text (GameFAQs FAQs,
and eventually work SOPs / docs) into structured, queryable JSON knowledge bases.
The prototype corpus is **Golden Sun 1 (`gs1`)**; the design generalizes to any
`{game}` / domain by swapping the raw corpus and schema.

```
raw/{game}/*.{txt,md}  →  schema/{game}_schema.md  →  scripts/extract.py  →  data/{game}/{entity}.json  →  tools/{game}_*.html
(source FAQs)             (field defs + source map)    (Claude API call)       (structured source of truth)   (single-file apps)
```

The **schema file is the control plane**: `extract.py` reads the entity's schema
section + the raw files listed in its `Master Source IDs` table, sends them to
Claude, and writes a JSON array. Nothing is hardcoded per entity.

## Layout

| Path | What |
|---|---|
| `raw/{game}/` | Original source text, unmodified (one file per source) |
| `data/{game}/` | Structured output — **the source of truth** |
| `schema/{game}_schema.md` | Field defs, enums, source map; drives extraction |
| `scripts/` | Cross-cutting pipeline + active rebuild chain |
| `scripts/gs1/` | Applied gs1 one-shot scripts (provenance; not rerun) |
| `tools/{game}_*.html` | Standalone apps with embedded JSON (active app: `gs1_codex.html`) |
| `tools/archive/` | Superseded explorers |
| `docs/` | Project-level docs; `docs/{game}/` holds per-corpus build plans |

## Running the extractor

```bash
# from inside lore-engine/
pip install anthropic python-dotenv          # the only two deps; no requirements.txt
python scripts/extract.py --entity bosses --game gs1
python scripts/extract.py --entity djinn               # --game defaults to gs1
python scripts/extract.py --entity bosses --dry-run    # resolve schema + files, no API call
```

`ANTHROPIC_API_KEY` must be in `lore-engine/.env` or the environment. Use
`--dry-run` first after changing schema sections or raw files to confirm the
right files resolve before spending an API call.

## Conventions (from `schema/gs1_schema.md` → "General Rules")

- Field names `snake_case`; string values `lowercase` except proper nouns.
- `0` = confirmed-zero stat; `null` = missing/unconfirmed. Not interchangeable.
- Every entry carries a `sources` array of contributing source IDs.
- On a cross-source conflict, **flag it** (`conflicts` field / `[^note]`
  footnote) — never silently pick a winner.

## GS1 status (prototype complete, 2026-06-17)

A structured, FK-linked, audited knowledge base of **11 entities**:
djinn (28) · summons (16) · classes (76) · psynergy (141) · equipment (141) ·
items (38) · shops (12) · monsters (137) · bosses (13) · locations (38) ·
characters (5), plus `location_refs.json` (a materialized reverse-index view).

The whole graph is cross-linked by id (class↔psynergy, djinn→class requirements,
shop/drop→equipment/items, location→everything). `links_normalize.py` regenerates
the FK layer and `links_audit.py` guarantees referential integrity (0 errors).
The unified explorer is `tools/gs1_codex.html`.

See `docs/` for the inception record, the data-management write-up, application
ideas, and `docs/gs1/` for the per-stage build plans.
