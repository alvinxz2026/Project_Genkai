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
| `demooni` | `raw/gs2/In-Depth Guides/Djinni Stat Boosts Guide by Demooni.md` | Demooni | djinn, locations |
| `cooldude345` | `raw/gs2/In-Depth Guides/Summons FAQ by cooldude345.md` | cooldude345 | summons, djinn |
| `darkslime` | `raw/gs2/Guide and Walkthrough/Guide and Walkthrough by Darkslime.md` | Darkslime | walkthrough, characters, items, djinn, psynergy, classes, monsters (general) |
| `darthmarth` | `raw/gs2/Guide and Walkthrough/Guide and Walkthrough by DarthMarth.md` | DarthMarth | walkthrough, characters (general) |
| `terence` | `raw/gs2/In-Depth Guides/Battle Mechanics by Terence.md` | Terence | classes (bonuses+reqs, authoritative), mechanics, djinn, psynergy |
| `ultimalink` | `raw/gs2/In-Depth Guides/Character Class Guide by UltimaLink.md` | UltimaLink | classes (per-character chains, psynergy learnsets, available_to) |
| `yoyoyoshi` | `raw/gs2/In-Depth Guides/Psynergy FAQ by YoyoYoshi.md` | YoyoYoshi | psynergy (master list: pp/range/description/element), mechanics |
| `mr-unorigino-psy` | `raw/gs2/In-Depth Guides/Psynergy List by Mr_UnOrigino.md` | Mr_UnOrigino | psynergy (completeness cross-check; kana columns mojibake) |
| `shotgunnova-shop` | `raw/gs2/In-Depth Guides/Shop List by Shotgunnova.md` | Shotgunnova | shops (per-town stock + price), equipment, items, locations |
| `aspartate-forge` | `raw/gs2/In-Depth Guides/Forged Items Guide by aspartate.md` | aspartate | forging (forged_from), equipment, items, monsters |

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

---

## Schema: `djinn`

One entry per Djinni available in GS2 — all **72** (4 elements x 18). Per the ER
sketch's transfer convention, a Djinni's `game` is where it *first* appeared:
each element has 11 TLA djinn (`game: "gs2"`) and 7 GS1 djinn (`game: "gs1"`,
brought in via transfer / re-found), so gs2's `djinn.json` legitimately includes
the GS1 ones — they are re-extracted from a gs2 source (demooni), not imported
from `data/gs1`.

File: `data/gs2/djinn.json`

Primary source — `demooni` (`Djinni Stat Boosts Guide`), a single clean source
giving element + stat boosts + acquisition. Extracted deterministically by
`scripts/djinn_extract_gs2.py`. The `---` split in demooni's section 2 is exactly
the TLA/GS1 (gs2/gs1) boundary. Element mapping: Venus=earth, Mercury=water,
Mars=fire, Jupiter=wind.

```
Field               Type              Required   Notes
---------------------------------------------------------------------------
id                  string            YES        Lowercase name. e.g. "flint", "echo"
name                string            YES        Display name. e.g. "Flint"
element             string            YES        "earth" | "fire" | "wind" | "water"
game                string            YES        "gs2" (TLA-native) | "gs1" (transferred).
                                                 From demooni's `---` group split.
stat_bonus          object            YES        Permanent boosts when set. demooni columns
                                                 "HP PP STR DEF AGL LCK" (STR->atk); "---" -> 0.
  .hp/.pp/.atk/.def/.agi/.lck  integer YES        0 = confirmed none (table is exhaustive).
battle_effect       object | null     YES        Unleash effect (damage/range/special). Deferred
                                                 (null) — not in demooni; from a mechanics source later.
location            object | null     YES        Acquisition. null for the 28 GS1 djinn (no TLA
                                                 location in demooni).
  .area             string | null     YES        Clean location name for the locations FK. Deferred
                                                 (null) — demooni gives prose only.
  .description      string            YES        demooni's acquisition prose (verbatim).
  .source           string            YES        "demooni".
must_fight          boolean | null    YES        true if won in battle (demooni "*FIGHT*" tag).
                                                 null for GS1 djinn (no location entry).
sources             array of string   YES        ["demooni"].
conflicts           array of object   NO         Cross-source disagreements. Same shape as gs1.
```

### Notes for CC (Extraction Instructions)

1. **Single clean source**: demooni alone covers element + boosts + location +
   must_fight. `aspartate-djinn` / `android50` are optional cross-validation /
   `location.area` enrichment for later (deferred), not needed for this slice.
2. **The `---` split = game**: each element lists 11 TLA (gs2) djinn, then `---`,
   then 7 GS1 (gs1) djinn. Reset to gs2 at each element header.
3. **Deferred**: `battle_effect`, `location.area`, and the `monsters.djinn_id`
   back-fill (the future gs2 `links_normalize`'s job — note: monsters lists 27
   djinn-enemies vs demooni's 26 `*FIGHT*` tags; reconcile at link time).
4. Do not invent data.

---

## Schema: `summons`

One entry per summon — **29** total: the 16 standard summons (4 per element,
needing N same-element djinn) plus 13 multi-element **combo** summons from tablets
(per the ER sketch's gs2 increment: combos get a cross-element `djinn_recipe` +
`acquisition`).

File: `data/gs2/summons.json`

Primary source — `cooldude345` (`Summons FAQ`). Extracted deterministically by
`scripts/summons_extract_gs2.py`, which merges two of its tables by summon name:
section VII "Summons Stats" (from Terence Fergusson: damage element, Base, HP%,
range, special) and section V "Summons" (djinn requirement / combo recipe /
Found-At). Element codes: E=earth, W=water, F=fire, A=wind; recipe element names
Venus/Mercury/Mars/Jupiter map the same way.

```
Field            Type               Required   Notes
---------------------------------------------------------------------------
id               string             YES        Lowercase name. e.g. "judgement", "charon"
name             string             YES        Source spelling. e.g. "Judgement"
element          string             YES        Damage element (VII "Elm" column).
game             string             YES        Always "gs2".
is_combo         boolean            YES        true for the 13 multi-element tablet summons.
djinn_required   integer | null     YES        Standard summons: N same-element djinn (1-4).
                                               null for combos.
djinn_recipe     array | null       YES        Combos: [{element, count}] cross-element recipe.
                                               null for standard summons.
  [].element     string             YES        "earth" | "fire" | "wind" | "water"
  [].count       integer            YES        Djinn of that element required.
raises_power     integer | null     YES        Elemental Power boost after summoning (standard
                                               only, from section V). null for combos.
damage_power     integer | null     YES        VII "Base" damage. null for Coatlicue (curative).
damage_hp_mod    float | null       YES        VII "HP%" / 100 (e.g. 12 -> 0.12). null if curative.
range            integer | string   YES        VII range: radius int (6) or "all".
effect           string | null      YES        VII "Special" (status/buff/curative text). null if "---".
acquisition      object | null      YES        Combos only (standard are available from the start).
  .location      string | null      YES        Clean location name (locations FK). Deferred (null).
  .found_at      string             YES        cooldude's Found-At prose (verbatim).
  .source        string             YES        "cooldude345".
sources          array of string    YES        ["cooldude345"] (stats via Terence Fergusson).
conflicts        array of object    NO         Same shape as gs1.
```

### Notes for CC (Extraction Instructions)

1. **Merge VII + V by name**: VII has the numbers (damage element/Base/HP%/range/
   special), V has the djinn requirement (standard) or recipe + Found-At (combo).
2. **Combo damage element vs recipe**: VII lists each combo under its *damage*
   element (e.g. Charon under EARTH) while its `djinn_recipe` is cross-element
   (8 Venus + 2 Jupiter). Keep both — `element` = damage element.
3. **Coatlicue** is curative (VII Base code "c"): `damage_power`/`damage_hp_mod`
   null, effect notes the heal/Regen. `<Missile>` is Daedalus' sub-attack, not a
   summon — skip it.
4. **Deferred / cross-source**: `acquisition.location` clean name (prose only);
   note cooldude calls Valukar "Bullrog" and Sentinel "Sentinal" — reconcile with
   `bosses` at link time. `dbfire` is an optional 2nd source for tablet sidequests.
5. Do not invent data.

---

## Schema: `characters`

One entry per **playable** GS2 (Lost Age) party member. This is the small
**dimension table** the scattered character references resolve against
(`equipment.equippable_by`, `psynergy.available_to`,
`classes.available_to[].character`). GS2 has **8** playables: the four TLA-native
Adepts (Felix, Jenna, Sheba, Piers) plus the four returning GS1 Adepts (Isaac,
Garet, Ivan, Mia) who rejoin in the late game. Mirrors GS1's `characters` but,
per the ER sketch (§4.1), replaces GS1's single `is_permanent` with
`is_starter` + `from_gs1` + a prose `join` (the GS1 "permanent vs Prologue-only"
split does not map onto the TLA roster).

File: `data/gs2/characters.json`

```
Field           Type              Required   Notes
---------------------------------------------------------------------------
id              string            YES        Lowercase. e.g. "felix", "piers".
name            string            YES        In-game display name. Matches the strings used
                                             in equippable_by / available_to (natural key).
jp_name         string | null     YES        Alt/JP romanized name from darkslime's
                                             "Name/JPName" header (e.g. Piers -> "Picard").
game            string            YES        Always "gs2".
element         string            YES        Innate element from darkslime "Alignment: <clan>":
                                             Venus->earth | Mars->fire | Jupiter->wind |
                                             Mercury->water.
is_starter      boolean           YES        true if in the party at the opening (Idejima):
                                             Felix/Jenna/Sheba. (curated)
from_gs1        boolean           YES        true for a returning GS1 Adept (Isaac/Garet/Ivan/
                                             Mia), who rejoins late-game. (curated)
join            string            YES        Short factual note: when/how they join the TLA
                                             party. (curated — judgment, walkthrough-sourced)
hometown        string | null     YES        From darkslime "Hometown:". Proper noun, literal.
can_equip       array of string   YES        Equip-type categories from darkslime "Can Equip:"
                                             (lowercased), e.g. ["long swords","axes",...].
                                             The reverse of equipment.equippable_by.
sources         array of string   YES        Source IDs.
```

### Example Entry: Piers

```json
{
  "id": "piers",
  "name": "Piers",
  "jp_name": "Picard",
  "game": "gs2",
  "element": "water",
  "is_starter": false,
  "from_gs1": false,
  "join": "joins at Kibombo, after the party helps recover his ship.",
  "hometown": "Lemuria",
  "can_equip": ["long swords", "light blades", "axes", "maces", "armor",
    "clothing", "shields", "gloves", "helms", "crowns", "boots", "shirts", "masks"],
  "sources": ["darkslime", "darthmarth"]
}
```

### Notes for CC (Extraction Instructions)

Produced by the deterministic parser `scripts/characters_extract_gs2.py` (no LLM).

1. **Two layers**: structured fields (name/jp_name/element/hometown/can_equip) are
   parsed from `darkslime`'s "1. The Character Guide" blocks; the **8 playables are
   exactly the blocks carrying a `Can Equip:` line** (villains have none). The
   judgment fields (`is_starter`/`from_gs1`/`join`) are a curated 8-row map.
2. **Natural keys**: `name` is the key that `equipment.equippable_by` /
   `psynergy.available_to` / `classes.available_to[].character` reference; the gs2
   `links_audit` validates them against this table (no `*_id` added at those sites).
3. **Known source artifact**: darkslime's Sheba block line-wraps a stray equip type
   "Caps" onto the `Hometown:` line, so her `hometown` reads
   "Unknown, fell from the sky into Tolbi, Caps" and her `can_equip` omits "caps".
   Left literal (faithful to source, not silently fixed); reconcile at link time.
4. Do not invent data.

---

## Schema: `classes`

One entry per distinct GS2 class. **GS2's class system is Element-Levels +
Dominance, not GS1's raw djinn-count table**: each character has a base Element
Level of 5 in their primary element and +1 per equipped Djinni of an element; the
class you get is decided by your two Dominant elements (see `terence` "Dominance")
and the Element-Level thresholds. The game reuses display names across element
contexts (e.g. "Seer", "Conjurer", "Dark Mage"); `terence`'s qualifier letters
disambiguate them.

Built in **layers** (like `bosses`); this file has **Layers 1+2 done**:

- **Layer 1 — Terence spine** (`scripts/classes_extract_gs2.py`, done): the
  authoritative roster — `stat_multiplier` + `element_requirements` + grouping,
  from `terence`'s "Class Bonuses And Reqs" tables. 110 classes.
- **Layer 2 — ultimalink** (`scripts/classes_ultimalink_gs2.py`, done): fills
  `available_to[]` (which of the 8 characters reach each class, with that
  character's djinn counts) + `psynergy[]` learnsets (per class-line, by level).
  GS1 had to split classes per character (swordsman-isaac vs -garet) for diverging
  psynergy; the Layer-1 element-context ids **pre-resolve** that, so psynergy is a
  property of the class-LINE shared across same-element characters. 106/110 have
  psynergy (Tamer's per-sub-class psynergy is deferred — side-by-side columns).
- **Layer 3 — matcher / ratings** (deferred): the relative per-djinn-count rows
  (`terence` "Prm Aff Wek Neu" table — the GS2 analog of GS1's
  `build_terence_class_reqs`) + `aku-chi` ACR ratings (`available_to[].acr`).

File: `data/gs2/classes.json`

```
Field                   Type              Required   Notes
---------------------------------------------------------------------------
id                      string            YES        Lowercase, hyphens. Qualifier -> suffix:
                                                     (E)/(W)/(F)/(A) -> -earth/-water/-fire/-wind,
                                                     (D) -> -medium, (I) -> -item. Suffix (not
                                                     prefix) so it never collides with leading-
                                                     element compound base names, e.g. "Water Seer"
                                                     -> water-seer vs "Seer (W)" -> seer-water.
name                    string            YES        In-game display name. e.g. "Seer", "Swordsman".
qualified_name          string | null     YES        Name as printed with qualifier, e.g.
                                                     "Seer (W)", "Dark Mage (I)". null if unqualified.
game                    string            YES        Always "gs2".
class_line              string            YES        id of the top (root) class of this tier chain,
                                                     i.e. the first row of the `----`-delimited
                                                     sub-block in terence's table. Standalone chains
                                                     use their own id. e.g. "squire" for the
                                                     Squire->Knight->...->Slayer chain.
dominance_group         string            YES        terence table the class is from:
                                                     basic | lost-age-new | water-aligned |
                                                     wind-aligned | earth-aligned | fire-aligned |
                                                     earth-fire-aligned | water-wind-aligned |
                                                     item-required.
stat_multiplier         object            YES        Class stat bonus as a percent (110 = 110%).
  .hp .pp .atk .def .agi .lck  integer    YES
element_requirements    object            YES        Min Element LEVEL per element from terence
                                                     (order Eth Wtr Fre Wnd). 5 = base primary level;
                                                     int value | null when the column is "-".
  .earth .water .fire .wind   integer|null YES
available_to            array of object   YES        One per character (of 8) who can reach this
                                                     class (ultimalink). [] if no source lists it.
  [].character          string            YES        Display name, natural key -> characters.json.
  [].character_id       string            YES        Lowercased name (FK -> characters.id).
  [].djinn_requirements array of object   YES        ultimalink's character-relative djinn counts.
    [].requirement      string            YES        e.g. "water x6, earth x1" | "none".
    [].parsed           array of object   YES        [{element, count}]; [] for "none".
    [].source           string            YES        "ultimalink".
  [].acr                number | null     YES        aku-chi Combat Rank — null (Layer 3).
psynergy                array of object   YES        Class-line learnset (ultimalink), sorted by
                                                     level. [] if deferred (Tamer) / no source.
  [].name               string            YES        Display name (footnote * stripped). FK ->
                                                     psynergy.json (by name).
  [].id                 string | null     YES        null until gs2 links_normalize fills it.
  [].level              integer           YES        Level learned (ultimalink).
  [].sources            array of string   YES        ["ultimalink"].
sources                 array of string   YES        Source IDs, e.g. ["terence", "ultimalink"].
```

### Example Entry: Cavalier (E)

```json
{
  "id": "cavalier-earth",
  "name": "Cavalier",
  "qualified_name": "Cavalier (E)",
  "game": "gs2",
  "class_line": "swordsman-earth",
  "dominance_group": "water-aligned",
  "stat_multiplier": {"hp": 140, "pp": 110, "atk": 130, "def": 130, "agi": 110, "lck": 120},
  "element_requirements": {"earth": 5, "water": 4, "fire": null, "wind": null},
  "available_to": [
    {"character": "Felix", "character_id": "felix",
     "djinn_requirements": [{"requirement": "water x4", "parsed": [{"element": "water", "count": 4}], "source": "ultimalink"}],
     "acr": null}
  ],
  "psynergy": [{"name": "Ply", "id": null, "level": 1, "sources": ["ultimalink"]}],
  "sources": ["terence", "ultimalink"]
}
```

### Notes for CC (Extraction Instructions)

Layers produced by deterministic parsers (no LLM): `scripts/classes_extract_gs2.py`
(Layer 1) then `scripts/classes_ultimalink_gs2.py` (Layer 2). Rerun in that order.

1. **Spine = terence**: parse "== CLASS BONUSES AND REQS ==" tables only. Each
   group banner (`== <NAME> ==`, exact match) sets `dominance_group`; `----` rules
   within a group separate tier chains (first row = `class_line` root); a data row
   is any line whose tokens are `name… N% N% N% N% N% N% E E E E` (find the first
   `%` token to split name from stats). Element column order is **Eth Wtr Fre Wnd**.
2. **`element_requirements` is Element LEVELS, not djinn counts** — GS2 differs from
   GS1 here. 5 = base primary; the relative djinn-count matcher is Layer 3.
3. **Layer 2 = ultimalink** maps each per-character class block to a terence
   class-line (BLOCK2LINE, by block title), then **positionally zips** the block's
   tier rows to the line's classes (in tier order) — the block title→line mapping is
   globally consistent and every block's tier-count matches its chain length. A
   non-N/A tier => that character is `available_to` that class (with its djinn
   counts); the block's psynergy table is assigned to the whole class-line (shared
   across same-element characters, verified). `character_id` is the lowercased name;
   psynergy `id` stays null until gs2 `links_normalize`.
4. **Deferred**: Tamer per-sub-class psynergy (side-by-side columns) -> psynergy [];
   Layer 3 = `acr` (aku-chi) + the relative djinn-count matcher (terence 2nd table).
5. Do not invent data.

---

## Schema: `psynergy`

One entry per distinct psynergy ability. Abilities sharing a display name but
mechanically distinct (the two "Blast" lines) get separate ids. The clean master
source is `yoyoyoshi`'s section "11 > ALL PSYNERGIES" — an alphabetical
fixed-width table giving, per ability: pp / targeting range / short description /
element. This file is the **canonical psynergy reference** that
`classes[].psynergy[]` resolves against (by name).

File: `data/gs2/psynergy.json`

```
Field         Type              Required   Notes
---------------------------------------------------------------------------
id            string            YES        Lowercase, hyphens. Duplicate display names get a
                                           "-<pp>pp" suffix: "blast-5pp" (explosive) /
                                           "blast-7pp" (massive explosion).
name          string            YES        Display name. e.g. "Angel Spear", "Cure".
game          string            YES        Always "gs2".
element       string            YES        From the Type column: Venus->earth | Mars->fire |
                                           Mercury->water | Jupiter->wind | "neutral".
pp_cost       integer           YES        PP cost.
range         integer | string  YES        Targets from the "I"-bar: 1 | 3 | 5 | 7, or "all"
                                           (the 8-wide bar = whole party / all enemies).
description   string            YES        In-game short description.
series        string | null     YES        null — deferred (yoyoyoshi's element-section groupings
                                           mix true progressions with thematic clusters).
tier          integer | null    YES        null — deferred (with series).
sources       array of string   YES        ["yoyoyoshi"] (+ "mr-unorigino-psy" when its US-English
                                           name corroborates).
```

### Example Entry

```json
{
  "id": "angel-spear", "name": "Angel Spear", "game": "gs2", "element": "wind",
  "pp_cost": 12, "range": "all", "description": "Boost attack with a heavenly blade.",
  "series": null, "tier": null, "sources": ["yoyoyoshi", "mr-unorigino-psy"]
}
```

### Coverage & deferred

- **157 psynergy** (battle + field/utility), produced by deterministic parser
  `scripts/psynergy_extract_gs2.py` (no LLM). `mr-unorigino-psy` corroborates 126
  (its kana columns are mojibake; only its ASCII US-English name is used).
- **Known gap (-> gs2 `links_normalize`)**: yoyoyoshi's "ALL PSYNERGIES" is *not*
  exhaustive of class-learnable psynergy. `classes[].psynergy[]` (from ultimalink)
  references ~37 abilities absent here — Pierrot **Card** skills (Sword Card,
  Saber Dance…), high-tier attacks (Magma Storm, Hurricane, Quake Strike,
  Thunderhead), and Thorn/Nettle/Guardian/Protector — plus ~7 ultimalink
  misspellings (`Frezze Prism`->Freeze Prism, `Flare Strom`->Flare Storm,
  `Strom Ray`->Storm Ray, `High Imapct`, `Drian`->Drain, `Wind slash`, a
  `Cluster\tBomb` tab) and a name conflict (ultimalink "Megacool" vs yoyoyoshi
  "Supercool"). Resolving `classes.psynergy` name->id (fix typos, add the missing,
  flag the conflict) is the gs2 `links_normalize` job — `classes[].psynergy[].id`
  is null until then; this canonical list is intentionally not padded with
  typo-prone, stat-less names.
- **Deferred fields**: `series`/`tier`; and `level_learned` / `available_to` /
  `category` / `target` / `acquired_via_item` (level_learned + available_to are
  **derivable from `classes.json`** — the reverse-index belongs to links_normalize).

---

## Schema: `shops`

One entry per town shop in the `shotgunnova-shop` Shop List. Each town is a single
combined vendor table (`[SHnn] - TOWN`) with a `USE?`/`ATK`/`DEF`/.../`COST` grid;
a leading `*` marks an artifact. Deterministic parser `scripts/shops_extract_gs2.py`
(mirrors gs1 `shops_extract.py`).

File: `data/gs2/shops.json`

```
Field               Type              Required   Notes
---------------------------------------------------------------------------
id                  string            YES        Town slug. e.g. "daila", "apojii-islands"
name                string            YES        Town display name. e.g. "Daila"
game                string            YES        Always "gs2".
location            string            YES        Town name (natural key; resolves to a
                                                 locations entry once that layer exists).
availability_notes  string | null     YES        Bracketed shop note, e.g. "Shops are closed
                                                 until post-Trial Road"; null if none.
stock[]             array             YES        One per item row sold in the town:
  .name             string            YES        Item/gear display name. e.g. "Long Sword"
  .category         string            YES        "weapon" | "armor" | "item" (by ATK/DEF presence)
  .price            int               YES        Buy price in coins.
  .is_artifact      boolean           YES        True if the source row was '*'-prefixed.
  .ref_type         string | null     links      "equipment" | "item" (links_normalize_gs2).
  .ref_id           string | null     links      Resolved id, or null (see gap below).
sources             [string]          YES        ["shotgunnova-shop"].
```

- **Consumables harvested**: `shops_extract_gs2.py` also merges the shop's
  consumable rows (no ATK/DEF: Herb/Antidote/Elixir/Nut/Vial/Potion/Psy Crystal/
  Water of Life/Sacred Feather/Mist Potion) into `items.json` as `item_type:
  consumable` — these gs1↔gs2 shared consumables were deferred by the TLA-only
  item extraction; the shop is the sanctioned gs2 source. Idempotent by id.
- **Known gap (deferred)**: ~73 shared *basic gear* rows (Long Sword, Battle Axe,
  Magic Rod, ...) are gs1↔gs2-shared equipment that `mr-unorigino`'s TLA-only
  segment excluded, so they are absent from `equipment.json`. Their `stock` refs
  stay null and `links_audit_gs2` reports them as **expected gaps**. A later focused
  pass can backfill them from the shop source (needs name→type inference).

---

## Forging (equipment enrichment, not a separate entity)

Per the ER sketch, forging is modeled as fields on `equipment`, not its own entity.
`scripts/forging_extract_gs2.py` parses the `aspartate-forge` guide (section IV:
material blocks `[Orihalcon]`… + `[Rusty Weapons]`) and backfills:

```
equipment.forged_from   [string]   The source material(s). Material blocks ->
                                   ["Orihalcon"] etc.; rusty weapons -> ["Rusty Staff"] etc.
                                   [] for non-forgeable gear.
```

- **Corroboration (flag, don't merge)**: the parser cross-checks the guide's
  `Worth N coins` against `equipment.sell_price` (forge "Worth" == sell price =
  0.75×buy) and `Unleashes X` against `unleash.name`. Mismatches are reported, not
  silently applied. Found: two guide rounding typos (Nebula Wand, Pure Circlet) and
  one equipment typo (`Radient Fire` → guide's `Radiant Fire` on Levatine).
- **Name variants** (`FORGE_ALIASES`): the guide spells a few items differently
  (Cosmo→Cosmos Shield, Psychic/Astral Circlet→Circle, Spirits→Spirit Ring, and the
  equipment typo Apollo's→Appolo's Axe); aliased so `forged_from` resolves. `Dragon
  Armor` has no equipment match (reported unmatched).
- **`equippable_by`** is NOT set here — it is derived in `links_normalize_gs2` from
  `equipment.type` → `characters.can_equip`; the guide's `for <chars>` lines serve
  as an independent cross-check (55/56 forged items agree exactly).

---

## Equipment enrichment by links_normalize_gs2: `equippable_by`

`equipment.equippable_by[]` (character names) is **derived deterministically** from
`equipment.type` via `TYPE2CAT` → the `characters.can_equip` category that gates it
(e.g. `long_sword`→"long swords", `circlet`→"circlets", `bracelet`→"armlets"); `ring`
is a universal accessory (all 8). Types with no clean category mapping —
`hat` (mixes caps/crowns/masks), `class_item`, `special` — are left `[]` (11 items).
Validated against the forge guide's explicit lists (see above).
