# GS2 — Walkthrough Consolidation + Locations Plan (2a / 1 / 2b)

> **Detailed execution plan** for the next walkthrough work line. The previous
> doc [`walkthrough_chapters.md`](walkthrough_chapters.md) covered **split + tag**
> (all 10 sources → 855 derived per-chapter files, tagged kind/covers/region).
> This doc covers what comes after: **consolidate (2a) → extract locations (1) →
> translate (2b)**, plus a placeholder for **cross-check (3)**.
>
> Most heavy work hands off to **Antigravity (Gemini)** to save Claude usage; the
> backbone (index, spine, mapping, QA gate) is deterministic Python, already built.

---

## 0. The shape (locked with user 2026-06-18)

```
_chapters/ (split+tagged)  →  region spine + mapping  →  2a consolidate  →  1 locations  →  2b translate
   855 chapters               (THE KEYSTONE)            per-region prose    locations.json   zh from en
                              deterministic, built       (Gemini Pro)        (from 2a output)  (Gemini Flash)
```

Four decisions, locked:
1. **Order = spine → 2a → locations.** Locations rides on 2a's clean merged prose
   (much easier/higher-quality than re-reading 10 raw sources). Not parallel.
2. **2a and locations are two separate passes** (not one dual-output task) — keeps
   each Gemini handoff prompt simple and each output faithful.
3. **2a output is chunked per region** (`data/gs2/walkthrough/NN-<slug>.md`), one
   file per spine node — directly matches the eventual HTML chapter structure.
4. **Sources are NOT equal weight. Telago is the most-recommended guide** → it is
   the **primary narrative voice / conflict tie-breaker** in 2a (see §3).

**Why a spine at all:** the 10 guides each split by their own TOC — different
granularity, spelling (Daili/Dalia/Diala), boundaries, and main/side framing. The
spine reconciles them onto ONE canonical ordered progression so 2a/locations have
a stable backbone. cloud-blazer (clean area-level, in-order, whole game ch12–92)
is the **structural reference** for ordering/granularity; telago is the **content**
authority. Two different roles, both hold.

---

## 1. Keystone artifacts (built, deterministic, re-runnable — free)

| script | output | what it does |
|---|---|---|
| `scripts/walkthrough_index_gs2.py` | `data/gs2/intermediate/walkthrough_chapter_index.json` (+ `.md`) | dumps all 855 chapters' frontmatter + sizes. 494 are `prose-walkthrough` = the 2a corpus. |
| `scripts/region_spine_gs2.py` | `data/gs2/intermediate/region_spine.json` | **the keystone.** Canonical ordered spine (62 areas + overworld + boss-strategies buckets) + maps every prose chapter to node(s). Coarse/quest-arc tags resolve via `COARSE_MAP`; spelling variants via per-node `aliases`. **494/494 assigned, 0 unmatched, 0 empty nodes.** |
| `scripts/walkthrough_coverage_gs2.py` | (report; exit 1 on FATAL) | QA gate. PRE-2a: no orphan chapters / no empty nodes. POST-2a: every required node has an output file + each file's `sources:` ⊆ its mapped chapters (provenance integrity). |

`region_spine.json` is the **work queue**: for each node, `chapters[]` lists exactly
which source files to merge. Re-run `region_spine_gs2.py` if any chapter's `region`
tag changes; patch misses by editing `SPINE` aliases / `COARSE_MAP` (same
philosophy as `walkthrough_split.py`'s `ALIASES`).

---

## 2. Stage 2a — consolidate (the heavy Gemini line)

**Goal:** for each spine node, merge all mapped source chapters into ONE detailed,
faithful walkthrough section. **Detailed-first** (use all sources well); distill/
concise later if needed.

**Input per node:** the `chapters[]` for that node in `region_spine.json` (read the
listed `_chapters/<src>/*.md` files — bodies are byte-exact raw slices).

**Output:** `data/gs2/walkthrough/NN-<region-slug>.md`, where `NN` = spine `order`
(zero-padded), one file per node. Frontmatter:

```yaml
---
region_id: daila              # spine node id (must match region_spine.json)
region: Daila
order: 3
kind: main                    # main | side | postgame
sources:                      # the source chapter files actually merged (⊆ node's mapped chapters)
  - raw/gs2/_chapters/cloud-blazer/15-daila.md
  - raw/gs2/_chapters/telago/04-...
  - raw/gs2/_chapters/...
---
<consolidated detailed walkthrough prose for this region>
```

The coverage gate checks `region_id` is real and `sources` ⊆ the node's mapped set.

**Model: Gemini 3.1 Pro (High).** This is reasoning + faithfulness heavy (merging
up to 9 sources, resolving conflicts). Do **not** use Flash here — it loses fidelity.

**Batching:** work the spine in `order`. One Gemini round = a handful of nodes.
Update the tracker (§6) per round. ~58 required nodes (main/side/postgame); overworld
+ boss-strategies are buckets, not standalone files (see §4).

### Faithfulness rules (this is the only generative, non-verifiable step — bind it tightly)

- **Telago is primary** (most-recommended guide). Use Telago's account as the
  narrative backbone; layer the other sources on for extra detail/pickups/coverage
  Telago omits. **On a material conflict, default to Telago** unless several other
  sources clearly agree against it.
- **Never silently pick a winner on conflicts.** Where sources materially disagree
  (different item location, different boss HP/strategy), keep the divergence as a
  footnote (`[^src]`) — same rule as gs1's walkthrough and the schema General Rules.
- **Provenance:** list every merged source in `sources:`. Don't invent content not
  in the sources. Don't reword raw chapter bodies into the file as-is — synthesize.
- **Scope:** consolidate the *walkthrough flow* (route, puzzles, pickups, encounters,
  djinn/psynergy obtained here, shops, forging, transfer events). Structured entity
  data (full stat tables) already lives in `data/gs2/*.json` — reference, don't dump.

---

## 3. Stage 1 — locations (after 2a)

**Goal:** structured `data/gs2/locations.json` — one record per spine node (the
spine IS the locations skeleton). Extract from the **consolidated 2a prose**
(`data/gs2/walkthrough/`), not the raw sources — the merge work is already done.

Per record (final schema TBD when we write `gs2_schema.md` locations §; sketch):
`name`, `region_id`, `order`, `kind` (main/side/postgame), `connections` (adjacent
regions), `pickups` (items/equipment found), `djinn_here`, `psynergy_here`,
`summons_here`, `monsters_here`, `bosses_here`, `shop` (ref), `forging`, `transfer`,
`sources`. FK refs (to monsters/djinn/items/bosses) are **deferred to gs2
`links_normalize`** — store names, normalize later. Then build a gs2
`locations_refs` materialized reverse index (mirror gs1's `locations_refs.py`):
`shops.location` / `djinn.location` / `summons.acquisition` / `bosses.location`
all resolve against it.

**Model:** Gemini 3.1 Pro (High), or Claude (smaller, ~58 records from clean prose).

---

## 4. Coarse / monolithic / bucket source handling (the granularity難点, resolved)

The "each author splits differently" problem is handled by the spine mapping
(many-to-many). Specific cases:

- **Telago coarse quest-arcs** ("Out to the open sea" = whole Eastern Sea; "Osenia"
  = Garoh+Air's Rock+Mikasalla+Osenia Cavern) → mapped to *multiple* spine nodes via
  `COARSE_MAP`. So a Telago arc chapter appears in several nodes' `sources`; the 2a
  prompt tells Gemini to use only the slice of that chapter relevant to the node.
- **Monolithic sources** (strawhat "Walkthrough", super-slash 2 prose chapters):
  whole-game in one chapter, can't be sliced by the spine. Currently routed to the
  `overworld` bucket. During 2a, Gemini should `Ctrl+F` the region name inside these
  to pull the relevant passage. Flagged here so they're not silently dropped.
- **`overworld` bucket** (node 62, 40 ch): navigation/djinn-collection interludes
  (World Map, Sailing, trading sequence, trident parts). Not a standalone output
  file — its content gets distributed into the relevant area files during 2a, or a
  small "between-regions / overworld" file if useful.
- **`boss-strategies` bucket** (node 63, 42 ch): per-boss strategy appendix chapters
  (blank region, title = boss name) from autocon/ikillkenny/killerfusion/darthmarth.
  Overlaps `bosses.json` + `bosses_strategy.json` (already extracted). During 2a these
  **enrich the boss encounter in its fight's region** — not a standalone file.
- **Thin nodes** (SE Angara Islet, West Indra Islet = 1 source each): real but only
  autocon covers them. Fine — single-source is allowed, just less to cross-check.

---

## 5. Stage 2b — translate (after 2a is done)

Translate the consolidated English `data/gs2/walkthrough/*.md` → Chinese, chunk for
chunk (preserve frontmatter + footnotes + structure). **Model: Gemini 3.5 Flash
(High)** for bulk, Pro for literary polish. Output: `data/gs2/walkthrough_zh/` (same
filenames). Do not re-translate from raw — translate the consolidated English so EN
and ZH stay structurally aligned.

---

## 6. Tracker

`region_spine.json` is the source of truth for the queue; this table tracks 2a output.
Status: ⬜ not started · 🔄 in progress · ✅ done + gate-clean.

| stage | status | notes |
|---|---|---|
| index + spine + gate (keystone) | ✅ | 494/494 mapped, 0 unmatched/empty; gate OK |
| 2a consolidate | ⬜ | 58 required nodes (main/side/postgame); Gemini Pro, by spine order |
| 1 locations | ⬜ | after 2a; from consolidated prose; needs `gs2_schema.md` locations § + gs2 `locations_refs` |
| 2b translate | ⬜ | after 2a; Gemini Flash bulk |
| 3 cross-check | ⬜ | far; see gs2_plan.md §4 |

### 2a per-node work queue (from `region_spine.json`; T = Telago covers it)

| # | region | kind | #ch | #src | T | 2a |
|---|---|---|---|---|---|---|
| 0 | Venus Lighthouse | main | 7 | 7 |  | ✅ |
| 1 | Suhalla Gate | main | 8 | 6 |  | ✅ |
| 2 | Idejima | main | 5 | 5 |  | ✅ |
| 3 | Daila | main | 10 | 7 |  | ✅ |
| 4 | Kandorean Temple | main | 12 | 9 | T | ✅ |
| 5 | Shrine of the Sea God | main | 14 | 9 | T | ✅ |
| 6 | Dehkan Plateau | main | 10 | 9 | T | ✅ |
| 7 | Indra Cavern | main | 11 | 6 |  | ✅ |
| 8 | Madra | main | 16 | 8 | T | ✅ |
| 9 | Madra Catacombs | main | 7 | 5 |  | ✅ |
| 10 | Madra Drawbridge | main | 3 | 3 |  | ✅ |
| 11 | Osenia Cliffs | main | 3 | 3 |  | ✅ |
| 12 | Yampi Desert | main | 14 | 9 | T | ✅ |
| 13 | Alhafra | main | 17 | 9 | T | ✅ |
| 14 | Garoh | main | 19 | 9 | T | ✅ |
| 15 | Air's Rock | main | 17 | 9 | T | ✅ |
| 16 | Osenia Cavern | main | 8 | 6 | T | ✅ |
| 17 | Mikasalla | main | 13 | 8 | T | ✅ |
| 18 | Gondowan Cliffs | main | 14 | 9 | T | ✅ |
| 19 | Naribwe | main | 8 | 7 | T | ✅ |
| 20 | Kibombo Mountains | main | 10 | 7 | T | ✅ |
| 21 | Kibombo | main | 9 | 7 | T | ✅ |
| 22 | Gabomba Statue | main | 9 | 7 | T | ✅ |
| 23 | Gabomba Catacombs | main | 5 | 5 |  | ✅ |
| 24 | Lemurian Ship | main | 3 | 3 |  | ✅ |
| 25 | North Osenia Islet | side | 5 | 4 |  | ✅ |
| 26 | Apojii Islands | main | 10 | 5 |  | ✅ |
| 27 | Aqua Rock | main | 9 | 6 |  | ✅ |
| 28 | Sea of Time Islet | main | 7 | 5 |  | ✅ |
| 29 | Izumo | main | 9 | 5 |  | ✅ |
| 30 | Gaia Rock | main | 7 | 6 |  | ✅ |
| 31 | Izumo Ruins | side | 2 | 2 |  | ✅ |
| 32 | Champa | main | 9 | 7 |  | ✅ |
| 33 | Ankohl Ruins | main | 8 | 6 |  | ✅ |
| 34 | East Tundaria Islet | side | 4 | 3 |  | ✅ |
| 35 | SE Angara Islet | side | 2 | 1 |  | ✅ |
| 36 | West Indra Islet | side | 2 | 1 |  | ✅ |
| 37 | Yallam | main | 8 | 6 | T | ✅ |
| 38 | Taopo Swamp | side | 6 | 5 |  | ✅ |
| 39 | Islet Cave | side | 3 | 3 | T | ✅ |
| 40 | Tundaria Tower | main | 7 | 6 |  | ✅ |
| 41 | Alhafran Cavern | side | 2 | 2 |  | ✅ |
| 42 | Sea of Time | main | 8 | 6 | T | ✅ |
| 43 | Lemuria | main | 10 | 6 | T | ✅ |
| 44 | Hesperia Settlement | main | 3 | 3 |  | ✅ |
| 45 | Shaman Village Cave | main | 3 | 2 |  | ✅ |
| 46 | Shaman Village | main | 8 | 5 |  | ✅ |
| 47 | Trial Road | main | 4 | 4 | T | ✅ |
| 48 | SW Atteka Islet | main | 6 | 5 | T | ✅ |
| 49 | Contigo | main | 9 | 5 | T | ✅ |
| 50 | Jupiter Lighthouse | main | 8 | 7 | T | ✅ |
| 51 | Atteka Cavern | side | 3 | 2 |  | ✅ |
| 52 | Magma Rock | main | 7 | 7 | T | ✅ |
| 53 | Gondowan Settlement | main | 5 | 4 |  | ✅ |
| 54 | Loho | main | 6 | 5 |  | ✅ |
| 55 | Northern Reaches | main | 2 | 2 | T | ✅ |
| 56 | Prox | main | 5 | 5 |  | ✅ |
| 57 | Mars Lighthouse | main | 9 | 7 | T | ✅ |
| 58 | Kalt Island | side | 2 | 2 |  | ✅ |
| 59 | Treasure Isle | postgame | 6 | 6 | T | ✅ |
| 60 | Yampi Desert Cave | postgame | 5 | 5 | T | ✅ |
| 61 | Anemos Inner Sanctum | postgame | 5 | 5 | T | ✅ |
| 62 | Overworld / Navigation | overworld | 40 | 8 | T | — (bucket, §4) |
| 63 | Boss Strategies (appendix) | reference | 42 | 4 |  | — (bucket, §4) |

---

## 7. Antigravity (Gemini) handoff

Set model to **Gemini 3.1 Pro (High)** for 2a/locations. `/goal` once, then a simple
per-batch prompt.

### `/goal` (set once)

```
/goal Consolidate the gs2 walkthrough in the lore-engine repo. Read
docs/gs2/walkthrough_consolidation_plan.md first. The work queue + exact source
chapters per region are in data/gs2/intermediate/region_spine.json. For each spine
node, merge its mapped source chapters into one detailed, faithful walkthrough file
at data/gs2/walkthrough/NN-<slug>.md with the frontmatter in §2. HARD RULES: never
edit raw or _chapters files; Telago is the primary voice + conflict tie-breaker;
never silently resolve a conflict — footnote it; list every merged source in
sources:; don't invent content; after each batch run
python scripts/walkthrough_coverage_gs2.py and it must not print FATAL.
```

### Per-batch 2a prompt (swap the node ids)

```
Consolidate spine nodes <id1>, <id2>, <id3> (2a). For each:
1. In data/gs2/intermediate/region_spine.json, find the node; read every file in
   its chapters[] (they're byte-exact raw slices under raw/gs2/_chapters/).
2. Merge into ONE detailed walkthrough for that region. Telago is the backbone;
   add detail/pickups/coverage from the others. On a material conflict default to
   Telago and footnote the divergence [^src]. Don't invent; don't dump stat tables
   (those live in data/gs2/*.json — reference them).
3. Write data/gs2/walkthrough/<order>-<slug>.md with frontmatter:
   region_id / region / order / kind / sources: (only the chapters you actually used).
4. For Telago coarse arc chapters and monolithic sources (strawhat/super-slash),
   use only the slice relevant to this region.
Then run: python scripts/walkthrough_coverage_gs2.py  (must not print FATAL)
and update the per-node 2a status in docs/gs2/walkthrough_consolidation_plan.md.
```

### Model picks

| task | model | why |
|---|---|---|
| index / spine / gate | — (Python) | deterministic, done |
| **2a consolidate** | **Gemini 3.1 Pro (High)** | multi-source faithful merge + conflict handling |
| **1 locations** | Gemini 3.1 Pro (High) or Claude | structured extract from clean prose |
| **2b translate** | Gemini 3.5 Flash (High) bulk / Pro polish | translation is Flash-friendly |
