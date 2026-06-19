# GS2 — Walkthrough Consolidation + Locations Plan (2a / 1 / 2b)

> Execution plan for the walkthrough work line **after** split+tag
> ([`walkthrough_chapters.md`](walkthrough_chapters.md)). Covers **consolidate (2a) →
> extract locations (1) → translate (2b)**. **2a + locations + FK are done
> (2026-06-18/19); only 2b (translate) remains.** Heavy work hands off to
> **Antigravity (Gemini)** to save Claude usage; the backbone (index, spine, gate)
> is deterministic Python.

---

## 0. The shape (locked with user 2026-06-18)

```
_chapters/ (split+tagged)  →  region spine + mapping  →  2a consolidate  →  1 locations  →  2b translate
   855 chapters               (THE KEYSTONE, ✅)          per-region prose ✅  locations.json ✅  zh from en ⬜
                              deterministic Python        (Gemini Pro)        (from 2a output)  (Gemini Flash)
```

Four locked decisions:
1. **Order = spine → 2a → locations.** Locations rides on 2a's clean merged prose
   (easier/higher-quality than re-reading 10 raw sources). Not parallel.
2. **2a and locations are two separate passes** — keeps each Gemini handoff simple.
3. **2a output chunked per region** (`data/gs2/walkthrough/NN-<slug>.md`), one file
   per spine node — matches the eventual HTML chapter structure.
4. **Sources are NOT equal weight. Telago is the primary narrative voice / conflict
   tie-breaker** in 2a; cloud-blazer is the structural reference for ordering only.

**Why a spine:** the 10 guides each split by their own TOC (different granularity,
spelling, boundaries). The spine reconciles them onto ONE canonical ordered
progression so 2a/locations have a stable backbone.

---

## 1. Keystone artifacts (built, deterministic, re-runnable — free)

| script | output | what it does |
|---|---|---|
| `scripts/walkthrough_index_gs2.py` | `intermediate/walkthrough_chapter_index.json` (+`.md`) | dumps all 855 chapters' frontmatter + sizes. 494 are `prose-walkthrough` = the 2a corpus. |
| `scripts/region_spine_gs2.py` | `intermediate/region_spine.json` | **the keystone + work queue.** Canonical ordered spine (62 areas + overworld + boss-strategies buckets) + maps every prose chapter to node(s) via `COARSE_MAP` / per-node `aliases`. **494/494 assigned, 0 unmatched, 0 empty.** |
| `scripts/walkthrough_coverage_gs2.py` | (report; exit 1 on FATAL) | QA gate. PRE-2a: no orphan/empty. POST-2a: every required node has an output file + each file's `sources:` ⊆ its mapped chapters. |

`region_spine.json` is the work queue: each node's `chapters[]` lists exactly which
source files to merge. Re-run `region_spine_gs2.py` if any chapter's `region` tag
changes; patch misses via `SPINE` aliases / `COARSE_MAP`.

---

## 2. Stage 2a — consolidate ✅ (done 2026-06-18, Gemini 3.1 Pro, 62/62 nodes, gate clean)

For each spine node, merge all mapped source chapters into ONE detailed faithful
walkthrough section → `data/gs2/walkthrough/NN-<region-slug>.md`. Frontmatter:
`region_id / region / order / kind (main|side|postgame) / sources:` (the chapter
files actually merged, ⊆ node's mapped set). The coverage gate verifies both.

**Faithfulness rules (the one generative step — bound tightly):**
- **Telago is primary** (narrative backbone); layer others for extra detail/pickups.
  On a material conflict default to Telago unless several sources clearly agree against it.
- **Never silently pick a winner** — keep divergences as `[^src]` footnotes (schema General Rules).
- **Provenance:** list every merged source in `sources:`; don't invent; synthesize, don't dump raw bodies.
- **Scope:** consolidate *walkthrough flow* (route/puzzles/pickups/encounters/djinn/
  psynergy/shops/forging/transfer). Full stat tables already live in `data/gs2/*.json` — reference, don't dump.

**Bucket handling (granularity 難点, resolved by many-to-many spine mapping):**
Telago coarse quest-arcs → multiple nodes via `COARSE_MAP`; monolithic sources
(strawhat/super-slash) → `overworld` bucket (Ctrl+F region name); `boss-strategies`
bucket (42 ch) enriches each boss in its fight region; thin nodes (1 source) are fine.

---

## 3. Stage 1 — locations ✅ (done 2026-06-18; FK done 2026-06-19)

Structured `data/gs2/locations.json` — one record per spine node, extracted from the
**consolidated 2a prose** (not raw sources). Per record: `name`, `region_id`, `order`,
`kind`, `connections`, `pickups`, `djinn_here`, `psynergy_here`, `summons_here`,
`monsters_here`, `bosses_here`, `shop`, `forging`, `transfer`, `sources`. FK refs
stored as **names**.

**FK resolution — `scripts/locations_refs_gs2.py`** (not links_normalize). gs2 inverts
gs1's model: locations.json already holds forward refs as names, so resolution + the
reverse index both live in one derived view. Resolves every name → entity id,
materializes `data/gs2/location_refs.json` (BOTH directions: `regions` forward id
lists + `index` inverse `entity_id → [region_id]`), and prints a cross-check report
where **every unresolved name is a finding** (= first pass of task-3 cross-check; see
`gs2_plan.md` §4 + §5 backlog). Entity files NOT mutated (only 2 unambiguous
connection id typos fixed). Re-runnable + byte-stable.

---

## 4. Stage 2b — translate (⬜ remaining)

Translate consolidated English `data/gs2/walkthrough/*.md` → Chinese, chunk for chunk
(preserve frontmatter + footnotes + structure). Output `data/gs2/walkthrough_zh/`
(same filenames). Do **not** re-translate from raw — translate the consolidated
English so EN and ZH stay structurally aligned. **Model: Gemini 3.5 Flash (High)** for
bulk, Pro for literary polish. Scheduled by app direction (a ZH companion app needs it).

---

## 5. Antigravity (Gemini) handoff (reusable for 2b / any future re-run)

Set model to **Gemini 3.1 Pro (High)** for 2a/locations, **Flash (High)** for 2b.
`/goal` once, then a simple per-batch prompt.

```
/goal Consolidate the gs2 walkthrough in the lore-engine repo. Read
docs/gs2/walkthrough_consolidation_plan.md first. The work queue + exact source
chapters per region are in data/gs2/intermediate/region_spine.json. For each spine
node, merge its mapped source chapters into one detailed faithful walkthrough file at
data/gs2/walkthrough/NN-<slug>.md with the frontmatter in §2. HARD RULES: never edit
raw or _chapters files; Telago is the primary voice + conflict tie-breaker; never
silently resolve a conflict — footnote it; list every merged source in sources:;
don't invent; after each batch run python scripts/walkthrough_coverage_gs2.py and it
must not print FATAL.
```

Per-batch 2a prompt: "Consolidate spine nodes <ids> (2a). For each: read every file in
its `chapters[]` in region_spine.json (byte-exact raw slices); merge into ONE detailed
walkthrough (Telago backbone, footnote conflicts, don't dump stat tables); write
`data/gs2/walkthrough/<order>-<slug>.md` with frontmatter; for Telago coarse arcs +
monolithic sources use only the relevant slice. Then run the coverage gate."

| task | model | why |
|---|---|---|
| index / spine / gate | — (Python) | deterministic, done |
| 2a consolidate ✅ | Gemini 3.1 Pro (High) | multi-source faithful merge + conflict handling |
| 1 locations ✅ | Gemini 3.1 Pro (High) or Claude | structured extract from clean prose |
| **2b translate ⬜** | Gemini 3.5 Flash (High) bulk / Pro polish | translation is Flash-friendly |
