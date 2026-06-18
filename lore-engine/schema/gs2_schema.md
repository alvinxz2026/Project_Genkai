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
| `mr-unorigino-item` | `raw/gs2/In-Depth Guides/Item List by Mr_UnOrigino.md` | Mr_UnOrigino | equipment, items |
| `link-kirby-boss` | `raw/gs2/In-Depth Guides/Boss Guide by Link_Kirby.md` | Link_Kirby | bosses |

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

---

## Schema: `equipment`

One entry per named piece of TLA equipment: weapons, armor, wearable artifacts
(rings/shirts/boots), rusty weapons, and class-change items. Mirrors the gs1
`equipment` split (gear in `equipment.json`, consumables/materials in `items.json`).

File: `data/gs2/equipment.json`

Primary source — `mr-unorigino-item` (`Item List by Mr_UnOrigino`), a clean
debug-room-ordered table cross-listing GS1 **and** TLA items. **Only the TLA
sections (`2A`–`2U`)** feed gs2; GS1-numbered sections are gs1's truth source
("two independent truth sources, no import"). The source gives stats, elements,
the localized unleash *name*, cursed flag, use-effect text, and buy/sell prices —
but **not** equippability, unleash element/rate/power, or acquisition; those are
deferred (left null/empty) for a later source or `links_normalize`.

```
Field                Type              Required   Notes
---------------------------------------------------------------------------
id                   string            YES        Lowercase, hyphens, from GS-US name.
                                                  Collisions get a "-n" suffix (rusty weapons).
name                 string            YES        GS-US English name (canonical). e.g. "Huge Sword"
name_literal         string            YES        Mr_UnOrigino's literal English column (alt name).
                                                  e.g. "Darkside Sword" for Darksword. The 4th-column
                                                  Japanese is mojibake under this file's encoding -> dropped.
game                 string            YES        Always "gs2".
category             string            YES        "weapon" | "armor" | "item" (class-change items).
type                 string            YES        See Type Enums (gs1 set + "special", "ring", "rusty",
                                                  "class_item").
is_cursed            boolean           YES        From an "It's cursed" line.
is_rusty             boolean           YES        gs2-specific: true for section 2Q rusty weapons
                                                  (forge into real weapons; see forged_from on the result).
is_artifact          boolean | null    YES        Deferred — this source doesn't mark artifacts -> null.
forged_from          array of string   YES        gs2 forging edge: item ids of materials. Deferred ([] now);
                                                  filled later from aspartate-forge by links_normalize.
equippable_by        array of string   YES        Characters who can equip. Deferred ([] now; no equip
                                                  table in this source).
stat_bonus           object            YES        Flat bonuses when equipped; 0 = confirmed none.
  .atk/.def/.hp/.pp/.agi/.lck/.hp_regen/.pp_regen  integer   From "Attack/Defense/Maximum HP/Maximum PP/
                                                  Agility/Luck +N" and "HP/PP recovery +N".
elemental_power      object            YES        Map by element NAME. 0 = confirmed none.
  .earth/.fire/.wind/.water  integer    YES        "Venus/Mars/Jupiter/Mercury Power +N" ->
                                                  Venus=earth, Mercury=water, Mars=fire, Jupiter=wind.
elemental_resistance object            YES        Same shape/mapping (negatives valid, e.g. cursed gear).
increases_critical   boolean           YES        From "Rate of Criticals rise."
unleash              object | null     YES        null for armor/items or weapons with no unleash.
  .name              string            YES        GS-US unleash name (from "US - Unleashes 'X'").
  .name_literal      string | null     YES        Literal English in parens on the JP unleash line.
  .element           string | null     YES        Deferred (null) — not in this source.
  .rate              string | null     YES        Deferred (null).
  .power_level       string | null     YES        Deferred (null).
use_effect           object | null     YES        In-battle/menu use effect (mainly rings & some armor).
  .description       string | null     YES        Joined effect text. null if only a "may break" line.
  .may_break         boolean           YES        From "(It) might/may break if used in battle".
effects              array of string   YES        Raw descriptive lines preserved losslessly (use
                                                  effects, "Rate of Criticals rise.", etc.). [] if none.
buy_price            integer | null    YES        From "Buy: N coins". null if not sold.
sell_price           integer | null    YES        From "Sell: N coins". null if unsellable.
can_trade            boolean           YES        false for "Cannot be sold or bought." (quest gear).
debug_no             integer           YES        Mr_UnOrigino debug-room number (provenance; not unique —
                                                  the source reuses 328 for Trident and Planet Armor).
sources              array of string   YES        ["mr-unorigino-item"].
conflicts            array of object   NO         When a 2nd aligned source is merged. Same shape as gs1.
```

### Type Enums

```
category = "weapon"  -> "long_sword" | "light_blade" | "axe" | "mace" | "staff" |
                        "special" (Trident) | "rusty" (fallback when name lacks a class keyword)
category = "armor"   -> "armor" | "clothing" | "robe" | "shield" | "gloves" |
                        "bracelet" | "helm" | "hat" | "circlet" | "shirt" | "boots" | "ring"
category = "item"    -> "class_item" (Mysterious Card, Trainer's Whip, Tomegathericon)
```

### Notes for CC (Extraction Instructions)

Extracted by `scripts/items_extract_gs2.py` — a **deterministic parser** (no
LLM/API), mirroring `scripts/monsters_extract_gs2.py`. Not produced by `extract.py`.

1. **Parse only the TLA sections `2A`–`2U`** of `mr-unorigino-item`; skip the
   GS1-numbered sections (`A`–`R3`) — those are gs1's truth source.
2. Entry header is `debug_no / Japanese / English-literal / GS-US name`; the
   **4th field (GS-US name) is canonical**; the Japanese column is mojibake -> drop it.
3. Section header (`-2A. TLA Long Swords`) sets `category`/`type` for following entries.
4. Element mapping is **by name** (Venus=earth, Mercury=water, Mars=fire, Jupiter=wind).
5. **Unleash name capture must be greedy to the last quote** so apostrophes survive
   (e.g. "Acheron's Grief", not "Acheron").
6. **Deferred** (null/[]): `is_artifact`, `forged_from`, `equippable_by`, unleash
   `element`/`rate`/`power_level`. Filled later by aspartate sources / `links_normalize`.
7. Unrecognized attribute lines go to `effects[]` (lossless); never drop data.

---

## Schema: `items`

One entry per non-equippable TLA item that is **gs2-specific**: forging materials
(blacksmith items), trident pieces (key), and TLA "Other Items". Equippable gear
lives in `equipment.json`.

File: `data/gs2/items.json`

> **Scope caveat (deferred):** consumables shared with GS1 (Herb / Potion / Psy
> Crystal / stat-boost foods) are NOT in `mr-unorigino-item`'s TLA sections — the
> source lists them once under GS1 numbering. They are deferred to a later pass
> against a TLA-complete appendix source (e.g. `super-slash`). `items.json` is
> therefore intentionally partial for now (materials + key + misc only), the same
> way monsters deferred its FKs.

```
Field               Type              Required   Notes
---------------------------------------------------------------------------
id                  string            YES        Lowercase, hyphens, from GS-US name.
name                string            YES        GS-US English name. e.g. "Tear Stone"
name_literal        string            YES        Mr_UnOrigino literal English column (alt name).
game                string            YES        Always "gs2".
item_type           string            YES        "material" (forging) | "key" | "consumable".
                                                 2R blacksmith -> material; 2S trident -> key;
                                                 2U "Other" -> curated map (else key).
effect              object            YES
  .description      string | null     YES        Source effect text if any; else null.
  .target           string | null     YES        Deferred (null) — not stated in this source.
  .stat_boosted     string | null     YES        Deferred (null).
usable_in_battle    boolean | null    YES        Deferred (null) — not stated in this source.
buy_price           integer | null    YES        From "Buy: N coins".
sell_price          integer | null    YES        From "Sell: N coins".
can_trade           boolean           YES        false for "Cannot be sold or bought." (trident pieces).
debug_no            integer           YES        Provenance (see equipment note).
sources             array of string   YES        ["mr-unorigino-item"].
conflicts           array of object   NO         Same shape as gs1.
```

### Notes for CC (Extraction Instructions)

Extracted by `scripts/items_extract_gs2.py` (same parser as `equipment`; the run
splits records into `equipment.json` vs `items.json` by section). Sections `2R`
(blacksmith → `material`), `2S` (trident → `key`), `2U` (Other → curated
`consumable`/`material`/`key`) become items; all other TLA sections become
equipment. Do not invent data.

---

## Schema: `bosses`

One entry per boss (18). Richer than a `monsters` stat-line: adds strategy,
weakness, recommended level, special mechanics, and an `encounters` array
(multiple objects only for multi-form bosses). The boss **numbers** already live
in `monsters.json` (the 23 `is_boss` stat-lines); this entity does not
re-extract them.

File: `data/gs2/bosses.json`

Built by **two layers** (see `scripts/bosses_extract_gs2.py`):
- **Deterministic skeleton** — stats / elements / abilities / rewards / location
  are pulled straight from `data/gs2/monsters.json` via a curated boss map that
  collapses party-config stat variants (Karst/Agatio "vs-all"/"vs-2-3") and
  multi-form dragons into one boss each.
- **Curated strategy sidecar** — `data/gs2/intermediate/bosses_strategy.json`
  (hand-authored from the prose boss guides, currently `link-kirby-boss`) supplies
  `weakness` / `recommended_level` / `strategy` / `special_mechanics`. The prose
  half is the LLM/judgment layer; the stats half stays deterministic.

> **Element shape**: gs2 keeps `elemental_power`/`elemental_resistance` as the
> `{earth,fire,wind,water}` dict used by gs2 `monsters` — NOT gs1 bosses'
> array-of-objects — so the two gs2 fact tables stay consistent.

```
Field                Type              Required   Notes
---------------------------------------------------------------------------
id                   string            YES        Lowercase, hyphens. e.g. "doom-dragon"
name                 string            YES        Display name. e.g. "Doom Dragon"
game                 string            YES        Always "gs2".
is_optional          boolean           YES        true for the 4 summon-tablet guardians
                                                  (link-kirby groups them apart from required bosses).
is_superboss         boolean           YES        true for Star Magician / Sentinel / Valukar / Dullahan.
encounters           array of object   YES        One object per fight form. >1 only for multi-form
                                                  bosses (Flame Dragon: big + small).
  .form_id           string            YES        Source monsters.json id for this form. e.g. "flame-dragon-big"
  .location          string | null     YES        From the monster stat-line's found[0].
  .stats             object            YES        Same shape as monsters.stats (hp/pp/regen/atk/def/agi/lck/turns).
  .elemental_power   object            YES        {earth,fire,wind,water} (from torrentlord).
  .elemental_resistance object         YES        Same shape.
  .attacks           array of object   YES        Seeded from the monster's abilities.
    [].name          string            YES        Ability name.
    [].source        string            YES        "torrentlord".
  .rewards           object            YES        {exp, coins, items[]} from the monster's drops.
weakness             array of string   YES        Elemental weaknesses from the boss guide. [] if not stated.
recommended_level    integer | null    NO         From the boss guide's recommended party level.
strategy             string | null     NO         Condensed prose strategy (preserves key tactics).
special_mechanics    array of string   YES        Notable battle mechanics (regen, instakills, Djinn
                                                  Storm, summon-ball behavior, etc.). [] if none.
special_notes        string | null     NO         Skeleton-side note: "fought alongside X",
                                                  party-config stat variants, multi-head phases.
sources              array of string   YES        e.g. ["link-kirby-boss", "torrentlord"].
conflicts            array of object   NO         Cross-source disagreements. Same shape as gs1.
```

### Notes for CC (Extraction Instructions)

1. **Do not re-extract boss stats** — pull them from `monsters.json` (torrentlord
   is the stat authority). Boss-guide HP/coins figures are approximate/secondary;
   where they disagree (e.g. King Scorpion 1054 vs 1064; Doom Dragon's 14,400
   *total* vs torrentlord's per-head HP) keep torrentlord and put the prose figure
   in `special_mechanics`/`special_notes`, never silently overwrite.
2. **Multi-form / paired bosses**: collapse party-config stat variants into the
   primary boss (note them in `special_notes`); give genuinely distinct forms
   (Flame Dragon big/small) separate `encounters`. Paired bosses fought together
   (Agatio+Karst, Moapa+Knight, Briggs+Sea Fighter) stay as separate entries that
   cross-reference each other in `special_notes`.
3. **Deferred**: `monsters.boss_id` back-fill (monster → boss FK) is the future
   gs2 `links_normalize`'s job; it stays null in monsters.json for now.
4. The strategy sidecar is the only hand-authored input; everything else is
   deterministic. Add more boss guides (goldmario-boss, rena-chan-hardboss) by
   merging into the sidecar + appending to `sources`. Do not invent data.
