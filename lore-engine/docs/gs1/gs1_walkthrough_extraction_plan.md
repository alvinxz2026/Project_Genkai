# Plan: Generate data/gs1/gs1_walkthrough.md

## Context

User wants to distill four large GameFAQs walkthroughs into one structured
`gs1_walkthrough.md` following the schema defined in
`lore-engine/schema/gs1_walkthrough_template.md`. The template specifies a
two-level hierarchy (Chapter → Location), field rules, conflict footnote
format, and source priorities per field type. Telago is the chapter backbone;
ElectroSpecter is primary for shops; Telago is primary for items, djinn, and
boss stats.

---

## The Context-Length Problem

| Source          | Size    | Role                              |
|-----------------|---------|-----------------------------------|
| Telago          | 411 KB  | Primary (chapter structure, items, djinn, bosses) |
| ElectroSpecter  | 306 KB  | Secondary (shops, enemy lists)    |
| BF_Gamer        | 295 KB  | Tertiary (cross-check)            |
| Ikillkenny      | 275 KB  | Tertiary (cross-check)            |
| **Total**       | **~1.3 MB** | —                             |

Loading all four files simultaneously would exceed practical context limits
and produce noisy, hard-to-control extraction. The strategy is to never load
more than ~150 KB of raw source text into a single agent context at once.

---

## Proposed Approach

### Phase -1 — Persist plan doc to repo
Before any extraction, write this plan as
`lore-engine/docs/gs1_walkthrough_extraction_plan.md`
(creating `docs/` if needed). The file should be identical to this plan
including the Progress section below.

### Phase 0 — Map structure (1 targeted read)
Read Telago's Table of Contents section only (first ~200 lines) to extract:
- All chapter headings and their approximate line numbers
- Section marker codes used in the file (e.g. `{~CH2}`)

This gives a precise offset map for targeted reads in later phases.
**Batch boundaries will be finalised from Telago's actual TOC — the arcs
listed below are approximate placeholders only.**

Do the same quick structural read for ElectroSpecter and Ikillkenny so we
know where each chapter starts in those files too.

### Phase 1 — Batch extraction (4 parallel agents)
Divide GS1's narrative into 4 chapter batches based on the TOC extracted in
Phase 0. Approximate arcs (subject to correction from actual TOC):

| Batch | Approx. arc                                      |
|-------|--------------------------------------------------|
| A     | Vale → Vault → Bilibin → Mercury Lighthouse      |
| B     | Kolima → Mogall Forest → Xian → Altin            |
| C     | Kalay → Tolbi → Altmiller Cave → Lunpa           |
| D     | Suhalla → Lalivero → Jupiter Lighthouse → finale |

*(Exact chapter ranges assigned after Phase 0 TOC read.)*

Each agent receives:
- The exact line range in Telago covering its batch (from Phase 0 offsets)
- The matching line ranges in ElectroSpecter (for shops + enemy lists)
- The matching line ranges in Ikillkenny (for cross-check, esp. djinn)
- The full template (316 lines) as formatting reference
- The worked example (Chapter 2 / Vault) as a style anchor

Each agent outputs properly formatted chapter blocks following the template.

### Phase 2 — Assembly
Concatenate the four batches into the final
`lore-engine/data/gs1/gs1_walkthrough.md`,
prepending the file-level header:

```markdown
# Golden Sun 1 — Distilled Walkthrough

> Synthesised from: telago, electrospecter, bf-gamer, ikillkenny
> Game: Golden Sun (GBA, 2001)
> Pipeline: Project Lore-Engine
```

BF_Gamer is used opportunistically: if Phase 1 agents find a stat or item
that conflicts between Telago/ElectroSpecter/Ikillkenny, they pull the
matching BF_Gamer section to break the tie. It is NOT read wholesale.

---

## Field Source Priority (from template)

| Field     | Primary        | Secondary           |
|-----------|----------------|---------------------|
| Chapter structure | Telago | —               |
| Items     | Telago         | cross-check others  |
| Shops     | ElectroSpecter | Telago              |
| Enemies   | Telago + ElectroSpecter (union) | — |
| Djinn     | Telago         | djinn.json (existing) |
| Boss stats | Telago        | footnote conflicts  |
| Narrative | Synthesised    | second person, concise |

---

## Output Path

`lore-engine/data/gs1/gs1_walkthrough.md`

---

## Progress

| Step | Status | Notes |
|------|--------|-------|
| Phase -1: Write plan doc to repo | ✓ | |
| Phase 0: Telago TOC map | ✓ | |
| Phase 0: ElectroSpecter TOC map | ✓ | |
| Phase 0: Ikillkenny TOC map | ✓ | |
| Phase 1 Batch A | ✓ | 667 lines |
| Phase 1 Batch B | ✓ | 698 lines |
| Phase 1 Batch C | ✓ | 913 lines |
| Phase 1 Batch D | ✓ | 778 lines |
| Phase 2: Assembly | ✓ | gs1_walkthrough.md — 3066 lines, 18 chapters |

---

## Verification

After assembly:
1. Check chapter count matches Telago's chapter structure
2. Verify each chapter has at least one Location block with a Narrative field
3. Spot-check known boss stat blocks (e.g. Saturos at Mercury Lighthouse) against Telago source
4. Confirm conflict footnotes are present for any known stat discrepancies
5. Check no empty headers were written (e.g. `**Shop**` with nothing below)
