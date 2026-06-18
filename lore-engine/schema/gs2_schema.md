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
| `torrentlord` | `raw/gs2/In-Depth Guides/Enemy and Boss List by torrentlord.md` | torrentlord | monsters, bosses, locations, items |
| `super-slash` | `raw/gs2/Guide and Walkthrough/Guide and Walkthrough by Super_Slash.md` | Super_Slash | walkthrough, monsters, items, equipment, … (general) |

> More rows are added per entity as extraction proceeds. The full per-source map
> lives in `docs/gs2/gs2_sources.md`; only rows for entities being extracted need
> to be mirrored here. `monsters` (below) is the first extracted entity.

---

## Schema: `monsters`

One entry per enemy stat-line in the GS2 bestiary. The primary source —
`torrentlord` "Enemy and Boss List" (same author as GS1's Torrent Load) — lists
regular enemies **and** bosses in one "Complete List". Bosses appear here as flat
stat-lines (`is_boss: true`); a richer `bosses.json` entry (encounters, attacks,
strategy) is a *later* entity and will cross-link via `boss_id`.

File: `data/gs2/monsters.json`

```
Field                 Type              Required   Notes
---------------------------------------------------------------------------
id                    string            YES        Lowercase, hyphens. Variant suffix from "#n".
                                                   e.g. "ruffian", "mimic-1"
name                  string            YES        Base display name without variant. e.g. "Mimic"
game                  string            YES        Always "gs2".
variant               integer | null    YES        From torrentlord "#n" suffix (Mimic #1 -> 1).
                                                   null when no variant suffix.
is_boss               boolean           YES        true if this stat-line is a boss/mini-boss
                                                   (curated name set; refine when bosses.json exists).
boss_id               string | null     YES        bosses.json id — null until bosses.json exists.
is_djinn_enemy        boolean           YES        true if name contains "Djinni".
djinn_id              string | null     YES        djinn.json id — null until djinn.json exists.

found                 array of string   YES        Location names. torrentlord lists "-Location- (n)"
                                                   index refs; resolve each (n) against the legend at
                                                   the top of Section III. [] if none.
stats                 object            YES
  .hp                 integer | null    YES
  .pp                 integer | null    YES
  .hp_regen           integer | null    YES        From "HP n (Regen m)". Multi-value boss regen
                                                   (e.g. "Regen 2430 / 810 / …") -> first value.
  .pp_regen           integer | null    YES        From "PP n (Regen m)".
  .atk                integer | null    YES
  .def                integer | null    YES
  .agi                integer | null    YES
  .lck                integer | null    YES
  .turns              integer | null    YES        Multi-value (e.g. "3 / 2") -> first value.

elemental_power       object            YES        Map by element NAME, not column order.
  .earth/.fire/.wind/.water  integer    YES        torrentlord cols "Ven Mrc Mar Jup" ->
                                                   Venus=earth, Mercury=water, Mars=fire, Jupiter=wind.
elemental_resistance  object            YES        Same shape / same mapping.

abilities             array of string   YES        From "-Abilities-" "* X" lines. [] if none.
drops                 object            YES
  .exp                integer | null    YES        From "-Reward- n EXP".
  .coins              integer | null    YES        From "n Coins".
  .items              array of object   YES        [] for "No Item"/"Nothing".
    [].name           string            YES        Item name (will match items/equipment later).
    [].ref_type       string | null     NO         "equipment" | "item". Filled by links_normalize
                                                   once items.json/equipment.json exist (deferred).
    [].ref_id         string | null     NO         FK — deferred (null for now).
    [].icc            integer | null    YES        torrentlord "Item Class Chance" drop-rate class.

sources               array of string   YES        e.g. ["torrentlord"].
conflicts             array of object   NO         Cross-source disagreements (when a 2nd aligned
                                                   source is merged). Same shape as gs1.
```

### Example Entry: Ruffian

```json
{
  "id": "ruffian",
  "name": "Ruffian",
  "game": "gs2",
  "variant": null,
  "is_boss": false,
  "boss_id": null,
  "is_djinn_enemy": false,
  "djinn_id": null,
  "found": ["Venus Lighthouse Entry", "Suhalla Gate"],
  "stats": { "hp": 29, "pp": 0, "hp_regen": 0, "pp_regen": 0, "atk": 24, "def": 6, "agi": 11, "lck": 3, "turns": 1 },
  "elemental_power": { "earth": 100, "water": 100, "fire": 100, "wind": 100 },
  "elemental_resistance": { "earth": 100, "water": 100, "fire": 100, "wind": 100 },
  "abilities": ["Attack"],
  "drops": { "exp": 5, "coins": 5, "items": [ { "name": "Herb", "icc": 1 } ] },
  "sources": ["torrentlord"]
}
```

### Notes for CC (Extraction Instructions)

Extracted by `scripts/monsters_extract_gs2.py` — a **deterministic parser** (no
LLM/API), mirroring `scripts/monsters_extract.py` for gs1. Not produced by
`extract.py`.

1. **Parse only Division A ("Complete List", `dpt`)** of the torrentlord enemy
   list; Divisions B/C/D… are re-sorted views of the same data — skip them.
2. **Location legend**: the `(n) - Place Name` table sits under "Section III"
   *before* Division A. Build the index map first, then resolve each enemy's
   `-Location- (n)` refs to place names.
3. **New-enemy anchor**: each block's `HP n (Regen m)` line; the enemy name is
   the nonblank line immediately above it. `#n` suffix -> `variant`.
4. **Element mapping is by NAME**: `Ven Mrc Mar Jup` -> earth/water/fire/wind.
5. **Boss blocks** (Serpent, Poseidon, Doom Dragon, Dullahan, …) are *in* the
   Complete List with extra `[N LIGHTS]`/multi-value regen lines — ignore those
   junk lines (strict stat patterns won't match them); take the first value for
   multi-value `hp_regen`/`turns`. Flag `is_boss` from the curated boss-name set.
6. **Deferred FKs**: `boss_id`, `djinn_id`, and drop `ref_type`/`ref_id` stay
   null until gs2's bosses/djinn/items/equipment entities exist (then
   `links_normalize` fills drop refs). This slice produces monsters in isolation.
7. **Do not invent data.**
