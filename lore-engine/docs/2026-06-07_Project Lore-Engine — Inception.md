
---
title: "2026-06-07_Project Lore-Engine Inception"
doc_type: project
source_type: llm_chat
version: v1.0
status: active
created: 2026-06-07
updated: 2026-06-07
source: Claude - Miku
model_mode:
  - Claude Sonnet 4.6
tags:
  - meta-system
  - knowledge
  - llm
  - meta-system
  - life
privacy: cloud mirror
summary: "Inception document for Project Lore-Engine — a reusable pipeline for converting unstructured text (FAQs, documents, SOPs) into structured, queryable knowledge bases. Started with Golden Sun GameFAQs as the prototype corpus; designed to generalize to work and other domains."
---

# 2026-06-07_Project Lore-Engine Inception

## Meta
- **Doc type**: project
- **Source type**: llm_chat
- **Status**: active
- **Scope**: Project index and inception record for Lore-Engine
- **Context**:
  - Started from playing Golden Sun on Switch 2 via NSO — found rich but inaccessible GameFAQs text archives
  - Core insight: the real skill being built is not a game wiki, but a reusable pipeline for turning unstructured text into structured, queryable knowledge
  - Same pipeline applies to work scenarios: internal SOPs, meeting notes, unstructured documentation
  - Lives in GitHub under `genkai` repo as a subproject; may be extracted to its own repo later
  - **Trigger**: Brainstorm session in Claude Evergarden, June 2026
- **Summary**: Inception document for Project Lore-Engine — a reusable pipeline for converting unstructured text into structured, queryable knowledge bases. Prototype corpus is Golden Sun GameFAQs; architecture is designed to generalize.

---

## 1. Project Identity

| Field | Value |
|---|---|
| **Name** | Project Lore-Engine |
| **Repo** | `genkai/lore-engine` (subfolder) or standalone later |
| **Status** | Inception — Phase 0 not yet started |
| **Prototype corpus** | Golden Sun (GBA) — GameFAQs FAQ collection |
| **Generalization target** | Any domain with unstructured text sources (game wikis, work SOPs, research notes) |

---

## 2. Core Concept

**The problem**: Rich knowledge exists in unstructured long-form text (GameFAQs FAQs, internal docs, old SOPs). It is hard to query, cross-reference, or maintain.

**The pipeline**:
```
Raw text sources → Extract → Structure → Knowledge base → Applications
```

**What makes this reusable**: The pipeline is domain-agnostic. Swap the input corpus and schema, and the same tooling works for Golden Sun 2, a different game, or an internal company knowledge base.

---

## 3. Phases

### Phase 1 — Data Acquisition
Get raw text into the pipeline.

- **Prototype approach**: Manual copy-paste of 2–3 key GameFAQs pages into `/raw/*.txt`
- **Scale-up**: Python scraper (via Claude Code) to fetch pages programmatically
- **Output**: `/raw/` folder of plain `.txt` files, one per source

### Phase 2 — Extraction + Structuring
Convert raw text into structured data matching the schema.

- **Tool**: Claude (via Claude Code) — prompt-driven extraction
- **Input**: `/raw/*.txt`
- **Output**: `/data/*.json` or `/data/*.md` — one file per entity type (djinn, bosses, locations, classes...)
- **Key challenge**: Multiple sources may conflict — flag discrepancies, don't silently merge
- **Reusable skill**: Using AI to convert unstructured text → structured data at scale

### Phase 3 — Pipeline
Connect Phase 1 and Phase 2 into a repeatable, maintainable flow.

- Adding a new source = drop file in `/raw/`, rerun script
- Schema versioned alongside data
- **Reusable skill**: Designing a maintainable data pipeline

### Phase 4 — Applications (open-ended)
What gets built on top of the knowledge base. Not the focus — the KB is.

- NotebookLM Q&A layer
- Static webpage (wiki-style, with cross-links)
- Obsidian import
- Claude context injection
- Work scenario adaptation

---

## 4. Folder Structure

```
lore-engine/
├── README.md
├── raw/                  # Original source text, unmodified
│   └── gs1/             # Golden Sun 1 sources
├── data/                 # Structured output — source of truth
│   └── gs1/
│       ├── djinn.json
│       ├── bosses.json
│       ├── locations.json
│       ├── classes.json
│       └── items.json
├── scripts/              # Extraction and pipeline scripts
│   ├── extract.py
│   └── scraper.py
├── schema/               # Data structure definitions
│   └── gs1_schema.md
└── docs/                 # Project documentation (this file lives here)
    └── 2026-06-07_Project Lore-Engine Inception.md
```

---

## 5. Design Principles

1. **Data and presentation are separate** — `/raw` and `/data` are the source of truth; applications read from `/data` only
2. **Schema first, filling second** — define what a Djinn/Boss/Location looks like before extracting
3. **Flag conflicts, don't merge silently** — when sources disagree, surface it; don't pick a winner automatically
4. **Rerunnable** — the pipeline should be safe to rerun; outputs are reproducible from inputs
5. **Generalizable** — every design decision should ask: would this work for a different corpus?

---

## 6. Tools

| Tool | Role |
|---|---|
| Claude / Claude Code | Extraction, structuring, script generation |
| Python | Scraper, pipeline scripts |
| GitHub (`genkai`) | Version control, single source of truth |
| NotebookLM | Q&A application layer (Phase 4) |
| VSCode | Local editing environment |

---

## 7. Open Questions (to resolve during build)

- Schema design: what fields does each entity type need? (resolve during Phase 1–2)
- Conflict handling: auto-flag only, or also auto-resolve with confidence scoring?
- GS2 extension: same schema or parallel schema with cross-references?
- Work generalization: what's the first non-game corpus to test this on?

---

## 8. Status Log

| Date | Entry |
|---|---|
| 2026-06-07 | Project conceived in brainstorm session. Inception doc created. Repo setup pending. |
| 2026-06-17 | **GS1 prototype complete.** 11 FK-linked + audited entities in `data/gs1/`; unified explorer `tools/gs1_codex.html` (graph wiki + build planner). Pipeline validated end-to-end on the gs1 corpus. Wrapped up (cleanup, archived one-shots, READMEs); GS2 next — see `docs/gs1_wrapup_gs2_kickoff_plan.md`. |

---
