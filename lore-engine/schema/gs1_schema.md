# Golden Sun 1 — Data Schema Definitions

File: `gs1_schema.md`
Lore-Engine | `schema/gs1/`
Last updated: 2026-06-15
Status: v1.3

---

## Table of Contents

- [General Rules](#general-rules)
- [Schema: `djinn`](#schema-djinn)
  - [Damage Format](#damage-format)
  - [Source IDs](#source-ids)
  - [Example Entry: Flint](#example-entry-flint)
  - [Example Entry: with conflict flag](#example-entry-with-conflict-flag)
  - [Notes for CC (Extraction Instructions)](#notes-for-cc-extraction-instructions)
- [Schema: `bosses`](#schema-bosses)
  - [Damage Power vs. LinkTheValiant Descriptions](#damage-power-vs-linkthevaliant-descriptions)
  - [Source IDs (bosses-relevant)](#source-ids-bosses-relevant)
  - [Example Entry: Tret](#example-entry-tret-single-encounter-wiki-detail-page-available)
  - [Example Entry: Saturos](#example-entry-saturos-three-encounters)
  - [Notes for CC (Extraction Instructions)](#notes-for-cc-extraction-instructions-1)
- [Schema: `equipment`](#schema-equipment)
  - [Type Enums](#type-enums)
  - [Equippable-By Reference](#equippable-by-reference)
  - [Example Entry: Gaia Blade (weapon)](#example-entry-gaia-blade-weapon)
  - [Example Entry: Spirit Armlet (armor)](#example-entry-spirit-armlet-armor)
  - [Notes for CC (Extraction Instructions)](#notes-for-cc-extraction-instructions-2)
- [Schema: `classes`](#schema-classes)
  - [Class ID Disambiguation](#class-id-disambiguation)
  - [Example Entry: Lord](#example-entry-lord)
  - [Example Entry: Water Shaman](#example-entry-water-shaman)
  - [Notes for CC (Extraction Instructions)](#notes-for-cc-extraction-instructions-3)
- [Schema: `psynergy`](#schema-psynergy)
  - [Range Notation Mapping](#range-notation-mapping)
  - [Category Enum](#category-enum)
  - [Example Entry: Ragnarok](#example-entry-ragnarok)
  - [Example Entry: Wish (party heal)](#example-entry-wish-party-heal)
  - [Example Entry: Force (item-granted utility)](#example-entry-force-item-granted-utility)
  - [Notes for CC (Extraction Instructions)](#notes-for-cc-extraction-instructions-4)
- [Schema: `items`](#schema-items)
  - [Item Type Enum](#item-type-enum)
  - [Example Entry: Herb (consumable)](#example-entry-herb-consumable)
  - [Example Entry: Apple (stat boost)](#example-entry-apple-stat-boost)
  - [Example Entry: Black Orb (key item)](#example-entry-black-orb-key-item)
  - [Notes for CC (Extraction Instructions)](#notes-for-cc-extraction-instructions-5)
- [Schema: `summons`](#schema-summons)
  - [Example Entry: Judgment](#example-entry-judgment)
  - [Notes for CC (Extraction Instructions)](#notes-for-cc-extraction-instructions-6)
- [Schema: `shops`](#schema-shops)
  - [Example Entry: Vale](#example-entry-vale)
  - [Notes for CC (Extraction Instructions)](#notes-for-cc-extraction-instructions-7)
- [Schema: `monsters`](#schema-monsters)
  - [Example Entry: Vermin](#example-entry-vermin)
  - [Notes for CC (Extraction Instructions)](#notes-for-cc-extraction-instructions-8)

---

## General Rules

- All field names use `snake_case`.
- String values use `lowercase` unless the value is a proper noun (e.g. `"Flint"`, `"Vale"`).
- Use `0` when a stat bonus is confirmed to be zero. Use `null` only when data is missing or unconfirmed from all sources.
- `sources` lists every FAQ or reference that contributed data to this entry. Add a source whenever a new document is ingested.

### Conflict Resolution Policy

When sources disagree on a field, do NOT silently drop the disagreement. Resolve
to the single best value when the evidence allows, and keep an audit trail in
`conflicts`. Precedence:

1. **Majority** — if more sources agree on one value than any other, take the
   majority value (an outlier is almost always a transcription error).
2. **Authority** — when there is no clear majority (or a tie), defer to the most
   authoritative source for that field's domain (see Source Authority Ranking).
3. **Unresolved** — if neither majority nor authority can decide (e.g. the same
   thing named two ways, or a genuine ambiguity), keep the best available value
   and mark the conflict `unresolved` with a reason.

The field always holds the **resolved value**; `conflicts[]` records who said
what and how it was resolved. The conflict object shape (used by every schema):

```
conflicts[].field       string   Dot-notation path. e.g. "location.area", "stat_bonus.hp"
conflicts[].values      object   Map of source_id → that source's value.
conflicts[].resolution  string   "majority" | "authority" | "unresolved"  (optional;
                                 omit on legacy 2-source flags that predate this policy)
conflicts[].note        string   Rationale. e.g. "4/6 incl. fandom-wiki", "terence authoritative".
```

### Source Authority Ranking

Used for the **authority** tiebreak above. Authority is per-domain:

| Field domain | Most authoritative | Then |
|---|---|---|
| numeric stats / battle mechanics | `terence` (data-mined mechanics FAQ) | `fandom-wiki` / `golden-sun-wiki` |
| locations | `plz2bstfu` (dedicated location list), `fandom-wiki` / `golden-sun-wiki` | others |
| boss attacks / encounters | dedicated fandom single-boss pages (`fandom-tret`, …), `linkt` | others |

All other compilation sources (`telago`, `bfgamer`, `shotgunnova`,
`electrospecter`, `super-slash`, `torrent-load`) rank below the above; they are
strong for **corroboration / majority** but lose authority tiebreaks.

### Master Source IDs

This table lists every source ID used across all schemas in this file.

| ID | Document |
|---|---|
| `plz2bstfu` | Djinn Location List by plz2bstfu (GameFAQs, 2001) |
| `terence` | Djinn/Class Mechanics FAQ by Terence Fergusson (GameFAQs, 2002) |
| `golden-sun-wiki` | Golden Sun Wiki (community wiki, fetched 2026) |
| `linkt` | Boss Guide by LinkTheValiant (GameFAQs, 2006) |
| `fandom-wiki` | Golden Sun Fandom Wiki (fetched 2026-06-07) |
| `fandom-tret` | Golden Sun Fandom Wiki — Tret page (fetched 2026) |
| `fandom-saturos` | Golden Sun Fandom Wiki — Saturos page (fetched 2026) |
| `fandom-deadbeard` | Golden Sun Fandom Wiki — Deadbeard page (fetched 2026) |
| `dnextreme88` | Equipment Capabilities FAQ by dnextreme88 (GameFAQs, date unknown) |
| `fandom-equipment` | Golden Sun Fandom Wiki — GBA Equipment Comparison Charts (fetched 2026) |
| `rockettrekkie` | Golden Sun Artifacts Guide by RocketTrekkieEvoli (GameFAQs, date unknown) |
| `plz2bstfu-class` | Class Change FAQ by plz2bstfu / 'spoon' (GameFAQs, 2001). Same author as `plz2bstfu`, different document. |
| `aku-chi` | Class Setup Guide v1.50 by Christopher Goss / aku chi (GameFAQs, 2005) |
| `tetzcatlipoca` | Psynergy Guide v3.11 by Tetzcatlipoca (GameFAQs, 2004; raw file named "Psynergy Guide - nintendos_own.txt") |
| `jiggyhunter` | Psynergy List v1.1 by Jiggyhunter (GameFAQs, 2002) |
| `strawhat` | Psynergy/Class Guide v1.01 by strawhat (GameFAQs, 2005) |
| `super-slash` | Various data FAQ by Super Slash (GameFAQs; item/weapon/armor/djinn/class/psynergy/enemy/shop lists) |
| `telago` | Djinn/Class/Items/Psynergy appendix by Telago (GameFAQs; "Djinn Class Items Phynergy") |
| `bfgamer` | Djinn/Items/Psynergy guide by BFGamer (GameFAQs) |
| `shotgunnova` | Various data FAQ by Shotgunnova (GameFAQs; psynergy/class/djinn/shop/equipment lists) |
| `torrent-load` | Comprehensive Enemy List v1.52 by Torrent Lord (GameFAQs, 2005; full bestiary with regen, abilities, drop rates) |
| `electrospecter` | Classes/Djinn/Weapons/Armor/Equipment guide by ElectroSpecter (GameFAQs) |

Add new rows here when new sources are ingested.

---

## Schema: `djinn`

One entry per Djinni. File: `data/gs1/djinn.json`

```
Field               Type              Required   Notes
---------------------------------------------------------------------------
id                  string            YES        Lowercase name, no spaces. e.g. "flint"
name                string            YES        Display name. e.g. "Flint"
element             string            YES        One of: "earth" | "fire" | "wind" | "water"
game                string            YES        First game this Djinni appears in.
                                                 One of: "gs1" | "gs2"
                                                 For GS1 Djinn carried into GS2 via transfer,
                                                 this is still "gs1".

stat_bonus          object            YES        Stat changes when this Djinni is set on a character.
  .hp               integer | null    YES        HP bonus. 0 if confirmed none. null if unknown.
  .pp               integer | null    YES        PP bonus.
  .atk              integer | null    YES        Attack bonus.
  .def              integer | null    YES        Defense bonus.
  .agi              integer | null    YES        Agility bonus.
  .lck              integer | null    YES        Luck bonus.

battle_effect       object            YES        What happens when this Djinni is unleashed in battle.
  .damage           string | null     YES        Damage formula code. See Damage Format below.
                                                 null if the ability deals no damage.
  .range            integer | string  YES        Number of targets. Use integer (1, 3, 5, 7)
                                                 or "all" for party/enemy-wide effects.
  .special          string | null     YES        Plain English description of any special effect.
                                                 null if none.

location            object            YES        Where to find this Djinni in GS1.
  .area             string            YES        Location name as it appears in-game. e.g. "Kolima"
  .description      string            YES        Primary acquisition method in plain English.
  .notes            string | null     NO         Alternative routes, extra conditions, or
                                                 caveats. null if none.
  .source           string            YES        Which source this location description came from.

must_fight          boolean           YES        true if you must battle the Djinni to obtain it.
                                                 Derived from the §XIII bestiary: a Djinni that
                                                 appears as an "X Djinni" enemy must be fought.
                                                 false for Djinn that join automatically or via a
                                                 puzzle with no battle.

sources             array of string   YES        All FAQs/references that contributed data.
                                                 Use short identifiers (see Source IDs below).

conflicts           array of object   NO         Resolved disagreements (see Conflict Resolution
                                                 Policy). Omit entirely if no conflicts exist.
  [].field          string            YES        Which field the conflict is on. e.g. "location.area"
  [].values         object            YES        Map of source_id → that source's value.
  [].resolution     string            NO         "majority" | "authority" | "unresolved".
  [].note           string | null     NO         Rationale for the resolution.
```

### Damage Format

The `battle_effect.damage` field uses the following codes, inherited from Terence's FAQ:

| Code | Meaning |
|---|---|
| `"mXXX%"` | Elemental physical attack. Mult Mod = XXX / 100. Add Mod = 0. e.g. `"m160%"` = 1.6× normal attack. |
| `"aXX"` | Elemental physical attack. Mult Mod = 1. Add Mod = XX flat damage added. e.g. `"a50"` = normal attack + 50. |
| `null` | No damage. Effect only (buff, debuff, heal, status). |

Both `m` and `a` types use Relative Attack (User Attack − Target Defense) as base, with a 50%–150% elemental modifier applied.

### Source IDs

See Master Source IDs table above.

### Example Entry: Flint

```json
{
  "id": "flint",
  "name": "Flint",
  "element": "earth",
  "game": "gs1",
  "stat_bonus": {
    "hp": 8,
    "pp": 4,
    "atk": 3,
    "def": 0,
    "agi": 0,
    "lck": 0
  },
  "battle_effect": {
    "damage": "m160%",
    "range": 1,
    "special": null
  },
  "location": {
    "area": "World Map (near Vale)",
    "description": "Automatically acquired upon leaving Vale and entering the overworld for the first time.",
    "notes": null,
    "source": "golden-sun-wiki"
  },
  "must_fight": false,
  "sources": ["plz2bstfu", "terence", "golden-sun-wiki", "telago", "bfgamer", "shotgunnova", "electrospecter", "super-slash"]
}
```

### Example Entry: with conflict flag

```json
{
  "id": "granite",
  "name": "Granite",
  "element": "earth",
  "game": "gs1",
  "stat_bonus": {
    "hp": 9,
    "pp": 0,
    "atk": 0,
    "def": 2,
    "agi": 2,
    "lck": 1
  },
  "battle_effect": {
    "damage": null,
    "range": "all",
    "special": "Reduces all damage taken by party members by 50% for the current turn. Acts with increased priority."
  },
  "location": {
    "area": "Kolima",
    "description": "In a fenced-in area reached by entering a secret back door behind the treehouse to its left, traversing a short underground path.",
    "notes": null,
    "source": "golden-sun-wiki"
  },
  "sources": ["plz2bstfu", "golden-sun-wiki"],
  "conflicts": [
    {
      "field": "location.area",
      "values": {
        "plz2bstfu": "Kolima (fenced area with secret tunnel)",
        "golden-sun-wiki": "Kolima"
      },
      "note": "plz2bstfu entry #04 describes the Kolima fenced area but the description matches Granite. Entry #15 (Vine) may have been transposed. Verify in-game."
    }
  ]
}
```

### Notes for CC (Extraction Instructions)

When extracting Djinn data from raw source files:

1. **One JSON object per Djinni.** All 28 GS1 Djinn should produce 28 entries.
2. **Use `0` for confirmed-zero stat bonuses**, not `null`. Terence's table uses `--` to mean 0 — translate these to `0`.
3. **Preserve original location prose** in `location.description`. Do not paraphrase or summarise — keep it close to the source wording.
4. **Resolve conflicts** per the Conflict Resolution Policy (majority → authority
   → unresolved) and record them in `conflicts` with `resolution` + `note`.
   For stat disagreements `terence` is authoritative; for location names use
   majority across the location sources.
5. **Add the source ID** to `sources` for every field you populate from that document.
6. **`must_fight`**: derive from the §XIII bestiary (`monsters.json`) — a Djinni
   listed as an "X Djinni" enemy must be fought. BFGamer's "Fight: Y/N" column
   corroborates (but only covers the first few Djinn).
7. **Do not invent data.** If a field cannot be determined from available sources, use `null` and do not guess.

---

## Schema: `bosses`

One entry per boss character. Bosses that appear multiple times (e.g. Saturos)
use the `encounters` array with one object per fight instance. All other bosses
have exactly one object in `encounters`.

File: `data/gs1/bosses.json`

```
Field                   Type              Required   Notes
---------------------------------------------------------------------------
id                      string            YES        Lowercase, hyphens only. e.g. "saturos",
                                                     "killer-ape", "fusion-dragon"
name                    string            YES        Display name as it appears in-game.
game                    string            YES        Always "gs1" for this file.
is_optional             boolean           YES        true if the fight can be skipped entirely.
is_superboss            boolean           YES        true for Deadbeard only. false for all others.
encounters              array of object   YES        One object per fight instance.
                                                     Most bosses have exactly one.
                                                     Saturos has three (prologue, Mercury, Venus).

--- Per encounter object ---

  encounter_id          string            YES        Unique identifier for this instance.
                                                     Format: "{boss_id}-{location_slug}"
                                                     e.g. "saturos-mercury", "tret-kolima"
                                                     Single-encounter bosses: same as boss id.
  location              string            YES        Location name as it appears in-game.
  is_winnable           boolean           YES        false for scripted-loss encounters (prologue).
  stats                 object            YES        Boss stats for this encounter.
    .hp                 integer | null    YES        Hit Points.
    .pp                 integer | null    YES        Psynergy Points. null if boss has no PP.
    .atk                integer | null    YES        Attack.
    .def                integer | null    YES        Defense.
    .agi                integer | null    YES        Agility.
    .lck                integer | null    YES        Luck.
  elemental_power       array of object   YES        Elements the boss attacks with.
                                                     Empty array [] if none known.
    [].element          string            YES        One of: "earth" | "fire" | "wind" | "water"
    [].power            integer           YES        Power rating (e.g. 110).
  resistance            array of object   YES        Elemental resistance ratings.
                                                     Empty array [] if none known.
    [].element          string            YES        One of: "earth" | "fire" | "wind" | "water"
    [].value            integer           YES        Resistance value (e.g. 175).
  attacks               array of object   YES        All known attacks and abilities.
                                                     Includes both offensive and self-buff moves.
    [].name             string            YES        Ability name. e.g. "Heat Flash", "Inferno"
    [].type             string            YES        One of:
                                                     "psynergy" — costs PP, uses psynergy system
                                                     "physical" — physical attack, no PP cost
                                                     "monster_skill" — special monster ability
    [].target           string            YES        One of:
                                                     "enemy" — targets player party
                                                     "self" — targets the boss itself (buff)
                                                     "ally" — targets boss's ally (multi-boss fights)
    [].element          string | null     YES        Element of the attack.
                                                     null for non-elemental physical attacks.
    [].damage_power     integer | null    YES        Base damage power rating.
                                                     null for non-damaging effects.
    [].range            integer | null    YES        Number of targets. Use integer (1, 3, 5, 7).
                                                     null if non-damaging with no meaningful range.
    [].pp_cost          integer | null    YES        PP cost. null for physical/monster_skill.
    [].special          string | null     YES        Status effect, condition, or mechanic.
                                                     null if none.
    [].use_frequency    string | null     YES        How often this move is selected.
                                                     Format: "X/Y" e.g. "2/8", "53/256".
                                                     null if unknown (most bosses without a
                                                     dedicated fandom wiki page).
    [].source           string            YES        Source ID for this attack's data.
  special_mechanics     array of string   YES        Notable battle mechanics not captured above.
                                                     e.g. "acts twice per turn",
                                                     "immune to status ailments",
                                                     "regenerates 80 HP per turn"
                                                     Empty array [] if none.
  rewards               object | null     YES        Rewards for winning. null if unwinnable.
    .exp                integer | null    YES        Experience points awarded.
    .coins              integer | null    YES        Coins awarded.
    .items              array of string   YES        Guaranteed item drops. Empty array [] if none.
    .notes              string | null     NO         Conditional reward info.
                                                     e.g. "bonus EXP if felled by Venus Djinni"
  special_notes         string | null     NO         Per-encounter note not captured elsewhere.
                                                     e.g. "Mia regenerates 4 PP per turn"

--- Back to top-level boss fields ---

weakness                array of string   YES        Elemental weaknesses. e.g. ["fire"]
                                                     Empty array [] if none confirmed.
recommended_level       integer | null    NO         Suggested level from LinkTheValiant.
                                                     null if not provided.
strategy                string | null     NO         Prose strategy notes from LinkTheValiant.
                                                     Preserved close to original wording.
                                                     null if not provided.
sources                 array of string   YES        All source IDs that contributed data.
conflicts               array of object   NO         Only present if sources disagree on a field.
                                                     Omit entirely if no conflicts exist.
  [].field              string            YES        Dot-notation path. e.g. "encounters[0].stats.hp"
  [].values             object            YES        Map of source_id to conflicting value.
  [].note               string | null     NO         Optional human note.
```

### Damage Power vs. LinkTheValiant Descriptions

Damage power ratings come from Terence's FAQ and the Fandom Wiki.
LinkTheValiant describes attacks in plain English without power numbers.
Where both sources cover the same attack, the power number takes precedence
for `damage_power`; LinkTheValiant's description informs `special` and `type`.

### Source IDs (bosses-relevant)

See Master Source IDs table above.

### Example Entry: Tret (single encounter, wiki detail page available)

```json
{
  "id": "tret",
  "name": "Tret",
  "game": "gs1",
  "is_optional": false,
  "is_superboss": false,
  "encounters": [
    {
      "encounter_id": "tret-kolima",
      "location": "Kolima Forest (Tret Tree)",
      "is_winnable": true,
      "stats": {
        "hp": 710,
        "pp": 36,
        "atk": 89,
        "def": 27,
        "agi": 30,
        "lck": 28
      },
      "elemental_power": [
        { "element": "earth", "power": 105 }
      ],
      "resistance": [
        { "element": "water", "value": 175 },
        { "element": "wind",  "value": 100 },
        { "element": "earth", "value": 72 },
        { "element": "fire",  "value": 25 }
      ],
      "attacks": [
        {
          "name": "Attack",
          "type": "physical",
          "target": "enemy",
          "element": null,
          "damage_power": null,
          "range": 1,
          "pp_cost": null,
          "special": null,
          "use_frequency": "2/8",
          "source": "fandom-tret"
        },
        {
          "name": "Sleep Star",
          "type": "monster_skill",
          "target": "enemy",
          "element": null,
          "damage_power": null,
          "range": 3,
          "pp_cost": null,
          "special": "May inflict Sleep on each target.",
          "use_frequency": "2/8",
          "source": "fandom-tret"
        },
        {
          "name": "Thorn",
          "type": "psynergy",
          "target": "enemy",
          "element": "earth",
          "damage_power": 35,
          "range": 3,
          "pp_cost": 6,
          "special": null,
          "use_frequency": "2/8",
          "source": "fandom-tret"
        },
        {
          "name": "Growth",
          "type": "psynergy",
          "target": "enemy",
          "element": "earth",
          "damage_power": 25,
          "range": 1,
          "pp_cost": 4,
          "special": null,
          "use_frequency": "1/8",
          "source": "fandom-tret"
        },
        {
          "name": "Quake",
          "type": "psynergy",
          "target": "enemy",
          "element": "earth",
          "damage_power": 12,
          "range": 3,
          "pp_cost": 4,
          "special": null,
          "use_frequency": "1/8",
          "source": "fandom-tret"
        }
      ],
      "special_mechanics": [],
      "rewards": {
        "exp": 226,
        "coins": 700,
        "items": ["Potion"],
        "notes": "Rewards increase to 290 EXP and 900 coins if felled by an offensive Mars Djinni."
      },
      "special_notes": null
    }
  ],
  "weakness": ["fire"],
  "recommended_level": 7,
  "strategy": "Have Isaac and Garet start the battle with their Djinn on standby so that they can summon right off. After this, have all characters use psynergy on Tret. If you wish, you can attack with Isaac and Garet's Djinn again, and then summon. Tret will go down easily in the first few turns.",
  "sources": ["linkt", "fandom-wiki", "fandom-tret"]
}
```

### Example Entry: Saturos (three encounters)

```json
{
  "id": "saturos",
  "name": "Saturos",
  "game": "gs1",
  "is_optional": false,
  "is_superboss": false,
  "encounters": [
    {
      "encounter_id": "saturos-prologue",
      "location": "Vale",
      "is_winnable": false,
      "stats": {
        "hp": 3000,
        "pp": 260,
        "atk": 63,
        "def": 22,
        "agi": 9,
        "lck": 40
      },
      "elemental_power": [
        { "element": "fire", "power": 110 }
      ],
      "resistance": [
        { "element": "fire",  "value": 175 },
        { "element": "wind",  "value": 127 },
        { "element": "earth", "value": 100 },
        { "element": "water", "value": 72 }
      ],
      "attacks": [
        {
          "name": "Attack",
          "type": "physical",
          "target": "enemy",
          "element": null,
          "damage_power": null,
          "range": 1,
          "pp_cost": null,
          "special": null,
          "use_frequency": "2/8",
          "source": "fandom-saturos"
        },
        {
          "name": "Heat Flash",
          "type": "monster_skill",
          "target": "enemy",
          "element": "fire",
          "damage_power": 20,
          "range": 1,
          "pp_cost": null,
          "special": "May inflict Delusion. Damage equals normal attack + 20.",
          "use_frequency": "2/8",
          "source": "fandom-saturos"
        },
        {
          "name": "Fireball",
          "type": "psynergy",
          "target": "enemy",
          "element": "fire",
          "damage_power": 65,
          "range": 5,
          "pp_cost": 12,
          "special": null,
          "use_frequency": "2/8",
          "source": "fandom-saturos"
        },
        {
          "name": "Eruption",
          "type": "psynergy",
          "target": "enemy",
          "element": "fire",
          "damage_power": 90,
          "range": 3,
          "pp_cost": 14,
          "special": null,
          "use_frequency": "2/8",
          "source": "fandom-saturos"
        }
      ],
      "special_mechanics": [
        "Scripted loss — party is expected to be defeated.",
        "Fought as 'Mystery Man' alongside 'Mystery Woman' (Menardi)."
      ],
      "rewards": null,
      "special_notes": "Unwinnable under normal circumstances. Stats identical to Venus Lighthouse encounter."
    },
    {
      "encounter_id": "saturos-mercury",
      "location": "Mercury Lighthouse",
      "is_winnable": true,
      "stats": {
        "hp": 1200,
        "pp": 160,
        "atk": 113,
        "def": 35,
        "agi": 51,
        "lck": 40
      },
      "elemental_power": [
        { "element": "fire", "power": 110 }
      ],
      "resistance": [
        { "element": "fire",  "value": 175 },
        { "element": "wind",  "value": 127 },
        { "element": "earth", "value": 100 },
        { "element": "water", "value": 72 }
      ],
      "attacks": [
        {
          "name": "Attack",
          "type": "physical",
          "target": "enemy",
          "element": null,
          "damage_power": null,
          "range": 1,
          "pp_cost": null,
          "special": null,
          "use_frequency": null,
          "source": "fandom-saturos"
        },
        {
          "name": "Heat Flash",
          "type": "monster_skill",
          "target": "enemy",
          "element": "fire",
          "damage_power": 20,
          "range": 1,
          "pp_cost": null,
          "special": "May inflict Delusion. Damage equals normal attack + 20.",
          "use_frequency": null,
          "source": "fandom-saturos"
        },
        {
          "name": "Fireball",
          "type": "psynergy",
          "target": "enemy",
          "element": "fire",
          "damage_power": 65,
          "range": 5,
          "pp_cost": 12,
          "special": null,
          "use_frequency": null,
          "source": "fandom-saturos"
        },
        {
          "name": "Eruption",
          "type": "psynergy",
          "target": "enemy",
          "element": "fire",
          "damage_power": 90,
          "range": 3,
          "pp_cost": 14,
          "special": null,
          "use_frequency": null,
          "source": "fandom-saturos"
        }
      ],
      "special_mechanics": [
        "Mars powers weakened by the Mercury Beacon.",
        "Mia regenerates 4 PP per turn during this battle.",
        "Fixed attack pattern: Attack - Heat Flash - Fireball - Attack - Fireball - Heat Flash - Attack - Eruption"
      ],
      "rewards": {
        "exp": 331,
        "coins": 800,
        "items": ["Psy Crystal"],
        "notes": null
      },
      "special_notes": null
    },
    {
      "encounter_id": "saturos-venus",
      "location": "Venus Lighthouse",
      "is_winnable": true,
      "stats": {
        "hp": 3000,
        "pp": 260,
        "atk": 409,
        "def": 140,
        "agi": 160,
        "lck": 50
      },
      "elemental_power": [
        { "element": "fire", "power": 110 }
      ],
      "resistance": [
        { "element": "fire",  "value": 175 },
        { "element": "wind",  "value": 127 },
        { "element": "earth", "value": 100 },
        { "element": "water", "value": 72 }
      ],
      "attacks": [
        {
          "name": "Heat Flash",
          "type": "monster_skill",
          "target": "enemy",
          "element": "fire",
          "damage_power": 20,
          "range": 1,
          "pp_cost": null,
          "special": "May inflict Delusion.",
          "use_frequency": "53/256",
          "source": "fandom-saturos"
        },
        {
          "name": "Inferno",
          "type": "psynergy",
          "target": "enemy",
          "element": "fire",
          "damage_power": 140,
          "range": 5,
          "pp_cost": 23,
          "special": null,
          "use_frequency": "47/256",
          "source": "fandom-saturos"
        },
        {
          "name": "Break",
          "type": "psynergy",
          "target": "enemy",
          "element": null,
          "damage_power": null,
          "range": null,
          "pp_cost": 5,
          "special": "Removes all stat buffs from the player party.",
          "use_frequency": "41/256",
          "source": "fandom-saturos"
        },
        {
          "name": "Attack",
          "type": "physical",
          "target": "enemy",
          "element": null,
          "damage_power": null,
          "range": 1,
          "pp_cost": null,
          "special": null,
          "use_frequency": "35/256",
          "source": "fandom-saturos"
        },
        {
          "name": "Pyroclasm",
          "type": "psynergy",
          "target": "enemy",
          "element": "fire",
          "damage_power": 180,
          "range": 3,
          "pp_cost": 29,
          "special": null,
          "use_frequency": "29/256",
          "source": "fandom-saturos"
        },
        {
          "name": "Protect",
          "type": "psynergy",
          "target": "self",
          "element": null,
          "damage_power": null,
          "range": null,
          "pp_cost": 5,
          "special": "Increases Defense of Saturos and Menardi by 12.5%.",
          "use_frequency": "23/256",
          "source": "fandom-saturos"
        },
        {
          "name": "Haunt",
          "type": "psynergy",
          "target": "enemy",
          "element": null,
          "damage_power": null,
          "range": 3,
          "pp_cost": 5,
          "special": "May inflict Haunt status on each target.",
          "use_frequency": "17/256",
          "source": "fandom-saturos"
        },
        {
          "name": "Potent Cure",
          "type": "psynergy",
          "target": "ally",
          "element": "earth",
          "damage_power": null,
          "range": 1,
          "pp_cost": 16,
          "special": "Restores approximately 300 HP to Saturos or Menardi.",
          "use_frequency": "11/256",
          "source": "fandom-saturos"
        }
      ],
      "special_mechanics": [
        "Fought alongside Menardi.",
        "Isaac regenerates 4 PP per turn during this battle.",
        "Immune to status ailments except Psynergy Seal.",
        "Leads directly into Fusion Dragon fight with no rest."
      ],
      "rewards": {
        "exp": 3000,
        "coins": 3600,
        "items": [],
        "notes": "Rewards combined with Menardi's share: 6000 EXP and 7800 coins total."
      },
      "special_notes": null
    }
  ],
  "weakness": ["water"],
  "recommended_level": 32,
  "strategy": "Begin with all djinn set. Isaac unleashes Flint, Garet unleashes Fever, Ivan casts Impact on Isaac or Garet, and Mia unleashes Sleet. Isaac continues to unleash attackers, then unleashes Vine to slow Saturos and Menardi. Garet unleashes his attackers and then summons. Ivan unleashes Squall, Smog, and Breeze, then summons. Mia summons at her first opportunity and thereafter heals. All summons are focused on Menardi. After the summons, have each character attack Menardi if she is not already down. Once she is down, have the men attack Saturos until he goes down.",
  "sources": ["linkt", "fandom-wiki", "fandom-saturos"]
}
```

### Notes for CC (Extraction Instructions)

When extracting boss data from raw source files:

1. **One JSON object per boss character**, not per encounter. Saturos is one
   entry with three objects in `encounters`. All other bosses have one.
2. **encounter_id format**: `{boss-id}-{location-slug}` for multi-encounter
   bosses. For single-encounter bosses, `encounter_id` equals the boss id.
3. **attacks array**: include ALL moves — offensive, defensive, and self-buff.
   Use `target: "self"` for buffs the boss casts on itself.
4. **use_frequency**: only populate from fandom single-boss wiki pages
   (Tret, Saturos, Deadbeard). Leave `null` for all others.
5. **strategy field**: populate from LinkTheValiant. Preserve original wording;
   do not summarise heavily.
6. **rewards: null** for unwinnable encounters (prologue fights).
7. **is_optional**: true for Deadbeard, Storm Lizard, Tempest Lizard,
   Toadonpa. false for all mandatory story bosses.
8. **HP discrepancies**: LinkTheValiant gives approximate HP (~figures).
   Prefer fandom-wiki exact values. This is NOT a conflict — note it in
   `special_notes` only if the difference is large.
9. **GS2 bosses**: the fandom-wiki Boss page includes Lost Age bosses.
   Extract GS1 entries only. Stop at and include Deadbeard. Do not extract
   any Lost Age entries.
10. **Do not invent data.** If a field cannot be confirmed, use `null`.

---

## Schema: `equipment`

One entry per named equipment piece. Covers weapons, armor, and usable/artifact items.
Weapons, armor, and items share a single schema; use `category` + `type` to discriminate.

File: `data/gs1/equipment.json`

```
Field               Type              Required   Notes
---------------------------------------------------------------------------
id                  string            YES        Lowercase, hyphens only.
                                                 e.g. "gaia-blade", "demon-mail", "spirit-armlet"
name                string            YES        Display name as it appears in-game.
                                                 e.g. "Gaia Blade", "Demon Mail"
game                string            YES        Always "gs1" for this file.
category            string            YES        One of: "weapon" | "armor" | "item"
type                string            YES        See Type Enums below.
is_cursed           boolean           YES        true if equipping the item curses the character.
                                                 false for all non-cursed items.
is_artifact         boolean           YES        true if the item cannot be repurchased after
                                                 selling (one-time acquisition only).
                                                 false for ordinary shop items.
equippable_by       array of string   YES        Characters who can equip this item.
                                                 e.g. ["Isaac", "Garet"] or
                                                 ["Isaac", "Garet", "Ivan", "Mia"]
                                                 See Equippable-By Reference below.

stat_bonus          object            YES        Flat numeric stat changes when equipped.
  .atk              integer | null    YES        Attack bonus. 0 if confirmed none. null if unknown.
  .def              integer | null    YES        Defense bonus.
  .hp               integer | null    YES        Max HP bonus.
  .pp               integer | null    YES        Max PP bonus.
  .agi              integer | null    YES        Agility bonus.
  .lck              integer | null    YES        Luck bonus.
  .hp_regen         integer | null    YES        Passive HP restored per turn when equipped.
                                                 0 if confirmed none. null if unknown.
  .pp_regen         integer | null    YES        Passive PP restored per turn when equipped.

stat_multiplier     object | null     NO         Only present when a source explicitly states a
                                                 multiplicative modifier (e.g. "Agility x1.5").
                                                 null if the item has no multiplicative stats.
  .pp               float | null      NO         PP multiplier. e.g. 1.2 for "Max PP x1.2".
  .agi              float | null      NO         Agility multiplier. e.g. 1.5 for "Agility x1.5".

increases_critical  boolean | null    YES        true if the item increases the wearer's
                                                 critical hit rate. false if confirmed no effect.
                                                 null if unknown.

elemental_power     object            YES        Elemental attack power bonuses when equipped.
                                                 Use 0 for confirmed none.
  .earth            integer           YES
  .fire             integer           YES
  .wind             integer           YES
  .water            integer           YES

elemental_resistance object           YES        Elemental resistance bonuses when equipped.
                                                 Use 0 for confirmed none. Negative values are
                                                 valid (e.g. Demon Mail: Wind Resist −10).
  .earth            integer           YES
  .fire             integer           YES
  .wind             integer           YES
  .water            integer           YES

unleash             object | null     YES        Weapon unleash data. null for armor, items,
                                                 or weapons that have no unleash (e.g. Blessed Mace
                                                 has a use effect but no unleash).
  .name             string            YES        Unleash ability name. e.g. "Titan Blade"
  .element          string | null     YES        Element of the unleash.
                                                 One of: "earth" | "fire" | "wind" | "water" | null
                                                 null for non-elemental unleashes.
  .rate             string            YES        How often the unleash triggers on a normal attack.
                                                 One of: "low" | "medium" | "high"
  .power_level      string            YES        Relative damage power of the unleash.
                                                 One of: "low" | "medium" | "high"
  .effects          array of string   YES        Secondary status/damage effects in plain English.
                                                 e.g. ["may poison foe", "may drop foe's defense"]
                                                 Empty array [] if no secondary effects.
  .notes            string | null     NO         Extra context. Use for "2 different unleashes;
                                                 second unnamed in source" cases. null if none.

use_effect          object | null     YES        In-battle use effect when item is selected from
                                                 the menu. null if the item cannot be used.
  .description      string            YES        Plain English description of the effect.
                                                 e.g. "Restores 150 HP to one ally"
  .may_break        boolean           YES        true if using the item may permanently destroy it.

acquisition         object            YES        Primary acquisition method.
  .method           string            YES        One of:
                                                 "shop"         — purchasable at a weapon/armor dealer
                                                 "chest"        — found in a treasure chest
                                                 "lucky_wheels" — prize from Lucky Medal (Tolbi Springs)
                                                 "drop"         — monster drop (RNG)
                                                 "event"        — story/event reward (e.g. Colosso)
                                                 "unobtainable" — cannot be obtained without hacking
  .location         string | null     YES        Town, dungeon, or monster source.
                                                 null only for "unobtainable" method.
  .price            integer | null    YES        Purchase price in coins. null if not sold in shops.
  .notes            string | null     NO         Extra acquisition conditions or caveats.
                                                 e.g. "employ RNG strategy", "sells for X coins"

sources             array of string   YES        All source IDs that contributed data to this entry.
conflicts           array of object   NO         Only present if two sources disagree on a field.
                                                 Omit this field entirely if no conflicts exist.
  [].field          string            YES        Dot-notation path. e.g. "stat_bonus.def"
  [].values         object            YES        Map of source_id → conflicting value.
  [].note           string | null     NO         Optional human note explaining the discrepancy.
```

### Type Enums

```
category = "weapon"
  type: "axe" | "light_blade" | "long_sword" | "mace" | "staff"

category = "armor"
  type: "armor" | "robe" | "clothing" | "shield" | "gloves" | "bracelet" |
        "helm" | "crown" | "hat" | "circlet" | "shirt" | "boots"

category = "item"
  type: "item"
```

### Equippable-By Reference

Derived from the character equipment table at the top of dnextreme88's FAQ.

```
Armor types:
  armor, shield, helm, crown, hat, gloves, clothing
    → Isaac, Garet can equip (and NOT Ivan, Mia)
  robe, circlet, bracelet
    → Ivan, Mia can equip (and NOT Isaac, Garet)
  hat, clothing, gloves, crown
    → all four characters can equip
  (hats/crowns: all four; circlets: Ivan+Mia only; helms: Isaac+Garet only)

Full breakdown (from FAQ table):
  armor     → ["Isaac", "Garet"]
  robe      → ["Ivan", "Mia"]
  clothing  → ["Isaac", "Garet", "Ivan", "Mia"]
  shield    → ["Isaac", "Garet"]
  gloves    → ["Isaac", "Garet", "Ivan", "Mia"]
  bracelet  → ["Ivan", "Mia"]
  helm      → ["Isaac", "Garet"]
  crown     → ["Isaac", "Garet", "Ivan", "Mia"]
  hat       → ["Isaac", "Garet", "Ivan", "Mia"]
  circlet   → ["Ivan", "Mia"]
  shirt     → ["Isaac", "Garet", "Ivan", "Mia"]
  boots     → ["Isaac", "Garet", "Ivan", "Mia"]

Weapon types:
  axe        → ["Isaac", "Garet"]
  long_sword → ["Isaac", "Garet"]
  light_blade → ["Isaac", "Garet", "Ivan"]
  mace       → ["Isaac", "Garet", "Mia"]
  staff      → ["Ivan", "Mia"]

Items:
  item       → ["Isaac", "Garet", "Ivan", "Mia"]
```

Note: individual items may have further restrictions noted in source text
(e.g. "Females only"). Override the type-based default when a source
explicitly restricts or expands equippability.

### Example Entry: Gaia Blade (weapon)

```json
{
  "id": "gaia-blade",
  "name": "Gaia Blade",
  "game": "gs1",
  "category": "weapon",
  "type": "long_sword",
  "is_cursed": false,
  "is_artifact": true,
  "equippable_by": ["Isaac", "Garet"],
  "stat_bonus": {
    "atk": 135,
    "def": 0,
    "hp": 0,
    "pp": 0,
    "agi": 0,
    "lck": 0,
    "hp_regen": 0,
    "pp_regen": 0
  },
  "stat_multiplier": null,
  "increases_critical": false,
  "elemental_power": { "earth": 20, "fire": 0, "wind": 0, "water": 0 },
  "elemental_resistance": { "earth": 20, "fire": 0, "wind": 0, "water": 0 },
  "unleash": {
    "name": "Titan Blade",
    "element": "earth",
    "rate": "high",
    "power_level": "high",
    "effects": [],
    "notes": null
  },
  "use_effect": null,
  "acquisition": {
    "method": "chest",
    "location": "Venus Lighthouse",
    "price": null,
    "notes": null
  },
  "sources": ["dnextreme88", "rockettrekkie"]
}
```

### Example Entry: Spirit Armlet (armor)

```json
{
  "id": "spirit-armlet",
  "name": "Spirit Armlet",
  "game": "gs1",
  "category": "armor",
  "type": "bracelet",
  "is_cursed": false,
  "is_artifact": false,
  "equippable_by": ["Ivan", "Mia"],
  "stat_bonus": {
    "atk": 0,
    "def": 38,
    "hp": 0,
    "pp": 0,
    "agi": 0,
    "lck": 0,
    "hp_regen": 0,
    "pp_regen": 0
  },
  "stat_multiplier": null,
  "increases_critical": false,
  "elemental_power": { "earth": 10, "fire": 0, "wind": 0, "water": 10 },
  "elemental_resistance": { "earth": 0, "fire": 0, "wind": 0, "water": 0 },
  "unleash": null,
  "use_effect": {
    "description": "Cures status ailments on one ally.",
    "may_break": false
  },
  "acquisition": {
    "method": "shop",
    "location": "Lalivero",
    "price": 9000,
    "notes": null
  },
  "sources": ["dnextreme88"]
}
```

### Notes for CC (Extraction Instructions)

When extracting equipment data from the three raw source files:

1. **One JSON object per named equipment piece.** Items that share a name but
   differ in stats (e.g. Dragon Scales appears as both a Shield and an Armor)
   get separate entries with distinct IDs (e.g. `"dragon-scales-shield"` and
   `"dragon-scales-armor"`).

2. **Primary source for stats**: dnextreme88's FAQ is the most complete source
   for GS1 equipment stats. Use it as the base. Supplement with rockettrekkie
   (artifact context, element field, additional stat details) and fandom-equipment
   (obtainable method classification, price confirmation).

3. **`equippable_by`**: derive from equipment type using the Equippable-By
   Reference table above. Override only when a source explicitly states a
   character or gender restriction (e.g. "Females only", "Only Mia can equip").

4. **`is_artifact`**: set to true when rockettrekkie lists the item in the
   Artifacts Guide AND the item has no regular shop price, or when fandom-equipment
   marks the item's obtainable column as "Artifact". Set to false for all
   ordinary shop items.

5. **`unleash`**: Only weapons have unleash effects. Extract name from the
   "Unleashes X (Element)" text in the EFFECT column. Extract rate and
   power_level from the UNLEASH CAPABILITIES column ("Low/Medium/High Unleash
   rate, Low/Medium/High Unleash power"). Lowercase all enum values.
   For items with "2 Different Unleashes" where the second is unnamed, set
   `notes: "2 different unleashes; second unnamed in source"`.

6. **`use_effect`**: Set for any item whose EFFECT column says "Use to …" or
   "Replenishes …" or similar action-in-battle language. Set `may_break: true`
   when the source says "may break if used."

7. **`elemental_power` / `elemental_resistance`**: populate from STATS GIVEN
   column entries like "Earth Power +10" and "Wind Resist +20". Use 0 for all
   elements not mentioned. Negative resistance values are valid (e.g. Demon Mail
   "Wind Resist -10" → `elemental_resistance.wind: -10`).

8. **`stat_multiplier`**: only populate when the source uses "x N" notation
   (e.g. "Agility x1.5", "Max PP x1.2"). Do not attempt to convert these to
   flat values. Items with a multiplier still need all `stat_bonus` fields set
   (use 0 for the multiplied stat in `stat_bonus`).

9. **`increases_critical`**: set to true when the STATS GIVEN column says
   "Critical Hits increase" or similar. false for all others.

10. **`acquisition.method`**: Use `"lucky_wheels"` for "A prize from throwing
    a Lucky Medal into Tolbi Springs." Use `"drop"` for any "Dropped from …"
    or "employ RNG strategy" entries. Use `"event"` for Colosso prizes or
    story-reward items. Use `"unobtainable"` only when a source explicitly
    states the item cannot be obtained without hacking.

11. **`acquisition.price`**: populate from the coins figure in "Buy from X's
    weapon/armor dealer (N coins)." null for non-shop items. For artifact items
    where rockettrekkie lists a "Sells for X coins" figure, that is the sell
    price — do NOT use it as `price`; note it in `acquisition.notes` instead.

12. **Conflict handling**: flag conflicts with the `conflicts` array when
    sources disagree on a numeric stat, element, or acquisition method.
    Do NOT silently pick a winner. Common conflicts to watch for:
    - dnextreme88 vs. rockettrekkie on stat values
    - fandom-equipment method classification vs. FAQ description

13. **Do not invent data.** If a field cannot be determined from available
    sources, use `null` (or `0` for elemental fields confirmed to be zero).
    Do not guess at missing stat values.

---

## Schema: `classes`

One entry per distinct class. A "class" here is a unique combination of
display name + element context: the game reuses display names (e.g. "Shaman")
for mechanically different classes reached via different djinn mixes, and the
FAQ sources disambiguate these with parenthesised qualifiers ("(Water) Shaman").
Each such qualified variant is its own entry. Tier chains (Squire → Knight →
Gallant → Lord) are separate entries linked by `class_line`.

File: `data/gs1/classes.json`

```
Field                   Type              Required   Notes
---------------------------------------------------------------------------
id                      string            YES        Lowercase, hyphens only. Element qualifier
                                                     prefix when sources use one.
                                                     e.g. "lord", "water-shaman", "chaos-lord"
                                                     See Class ID Disambiguation below.
name                    string            YES        In-game display name. e.g. "Shaman", "Lord"
qualified_name          string | null     YES        Disambiguated name as used by sources,
                                                     e.g. "(Water) Shaman". null when the display
                                                     name is already unique.
game                    string            YES        Always "gs1" for this file.
class_line              string            YES        `id` of the lowest tier in this class's
                                                     psynergy family (classes that share base
                                                     psynergy and upgrade into each other).
                                                     Standalone classes use their own id.
                                                     e.g. "squire" for Squire/Knight/Gallant/
                                                     Lord/Slayer; "ninja" for Ninja;
                                                     "water-shaman" for (Water) Shaman.
reachable_in_gs1        boolean           YES        false for classes requiring 8 djinn of one
                                                     element (Slayer, Chaos Lord, War Adept) —
                                                     GS1 caps at 7 set djinn per character.
                                                     true for everything else.

available_to            array of object   YES        One object per character who can take this
                                                     class. Jenna's Flame User lists Jenna.
  [].character          string            YES        "Isaac" | "Garet" | "Ivan" | "Mia" | "Jenna"
  [].djinn_requirements array of object   YES        Djinn setups per source. Sources express
                                                     requirements differently (ranges relative to
                                                     the character's base element vs. concrete
                                                     7-djinn examples); keep each as stated.
    [].requirement      string            YES        Verbatim-ish requirement prose.
                                                     e.g. "0-1 Earth Djinn", "3 Mars, 4 Jupiter"
    [].source           string            YES        Source ID this requirement came from.
  [].acr                number | null     YES        aku-chi's Combat efficiency Rank (out of 10)
                                                     for this character in this class.
                                                     null if aku-chi does not rate it.

stat_multiplier         object | null     YES        Class stat bonuses as percentages, from
                                                     aku-chi (originally Terence's data). The
                                                     class multiplies (base + djinn + equip)
                                                     stats by these values. null when no source
                                                     provides them.
  .hp                   integer           YES        e.g. 170 for "170%".
  .pp                   integer           YES
  .atk                  integer           YES
  .def                  integer           YES
  .agi                  integer           YES
  .lck                  integer           YES

psynergy                array of object   YES        Psynergy learnable in this class. Union of
                                                     all sources' lists, with attribution.
                                                     Empty array [] only if no source lists any
                                                     (should not happen).
  [].name               string            YES        Psynergy display name, matching `name` in
                                                     psynergy.json. e.g. "Mother Gaia"
  [].sources            array of string   YES        Source IDs that list this psynergy for this
                                                     class.
notes                   string | null     NO         Caveats: tier-snapshot limitations of a
                                                     source list, source typos corrected, etc.
sources                 array of string   YES        All source IDs that contributed data.
conflicts               array of object   NO         Only present if sources disagree on a field.
                                                     Same shape as in other schemas.
  [].field              string            YES        Dot-notation path.
  [].values             object            YES        Map of source_id → conflicting value.
  [].note               string | null     NO         Optional human note.
```

### Class ID Disambiguation

The same display name can belong to several distinct classes. Two
disambiguation mechanisms apply, in this order:

1. **Source element qualifier**: when sources write "(Water) Shaman",
   "(Earth) Cavalier" etc., the qualifier becomes an id prefix:
   `water-shaman`, `earth-cavalier`.
2. **Character suffix**: when the same unqualified display name on two
   characters carries DIFFERENT psynergy lists (because the underlying
   element mix differs), split into per-character entries suffixed with the
   character name: `swordsman-isaac` vs `swordsman-garet`.

A class shared by two characters with IDENTICAL psynergy lists stays a single
entry with multiple `available_to` objects (Brute line, Ninja, Samurai,
Dragoon, Hermit/Elder/Scholar/Savant/Sage, Medium, Ranger, White Mage).

```
Display name   Distinct classes (id)
-----------------------------------------------------------------
Shaman         "water-shaman" (Isaac, 6-7 water)
               "wind-shaman"  (Isaac, 6-7 wind)
               "shaman-ivan"  (Ivan, Seer-line tier 3: Bolt series)
               "shaman-mia"   (Mia, Seer-line tier 3: Froth series)
Seer           "wind-seer"  (Ivan base class)
               "water-seer" (Mia base class)
               "seer-ivan"  (Ivan, 1 earth: Bolt series)
               "seer-mia"   (Mia, 1 earth: Froth series)
Diviner        "diviner-ivan" / "diviner-mia" (tier 2 of the Seer lines)
Druid          "druid-ivan" / "druid-mia"     (tier 4 of the Seer lines)
Ascetic        "water-ascetic" (Garet, 6-7 water)
               "wind-ascetic"  (Garet, 6-7 wind)
               "ascetic-ivan"  (Ivan, Pilgrim-line: Slash series)
               "ascetic-mia"   (Mia, Pilgrim-line: Douse/Prism series)
Cavalier       "cavalier-isaac" / "cavalier-garet" (water-line tier 3)
               "earth-cavalier" (Mia, 6-7 earth)
               "fire-cavalier"  (Mia, 6-7 fire)
Enchanter      "enchanter-isaac" / "enchanter-garet" (wind-line tier 3)
               "earth-enchanter" (Ivan, 6-7 earth)
               "fire-enchanter"  (Ivan, 6-7 fire)
Swordsman      "swordsman-isaac" (Thorn series + Revive)
               "swordsman-garet" (Mad Blast series + Guard/Protect)
Defender       "defender-isaac" / "defender-garet"
Illusionist    "illusionist-isaac" (Apprentice line)
               "illusionist-garet" (Page line)
Conjurer       "conjurer-isaac" / "conjurer-garet"
Pilgrim        "pilgrim-ivan" (Slash/Plasma) / "pilgrim-mia" (Douse/Prism)
Wanderer       "wanderer-ivan" / "wanderer-mia"
```

Note: "Guardian" the class (Isaac, 1 earth + 6 water) and "Guardian" the
psynergy (Samurai defense buff) are unrelated; they live in different files
so no disambiguation is needed.

### Example Entry: Lord

```json
{
  "id": "lord",
  "name": "Lord",
  "qualified_name": null,
  "game": "gs1",
  "class_line": "squire",
  "reachable_in_gs1": true,
  "available_to": [
    {
      "character": "Isaac",
      "djinn_requirements": [
        { "requirement": "6-7 Earth Djinn", "source": "plz2bstfu-class" },
        { "requirement": "6 earth", "source": "aku-chi" },
        { "requirement": "4-8 Venus Djinn (Gallant/Lord/Slayer tier group)", "source": "strawhat" }
      ],
      "acr": 9
    }
  ],
  "stat_multiplier": {
    "hp": 170,
    "pp": 110,
    "atk": 140,
    "def": 130,
    "agi": 140,
    "lck": 100
  },
  "psynergy": [
    { "name": "Ragnarok", "sources": ["plz2bstfu-class", "strawhat"] },
    { "name": "Quake", "sources": ["plz2bstfu-class", "strawhat"] },
    { "name": "Gaia", "sources": ["plz2bstfu-class", "strawhat"] },
    { "name": "Grand Gaia", "sources": ["strawhat"] },
    { "name": "Revive", "sources": ["plz2bstfu-class"] }
  ],
  "notes": "plz2bstfu's spell list is a level-30 snapshot and omits psynergy learned above level 30 (e.g. Grand Gaia).",
  "sources": ["plz2bstfu-class", "aku-chi", "strawhat"]
}
```

(Example abbreviated — real entries list the full psynergy union.)

### Example Entry: Water Shaman

```json
{
  "id": "water-shaman",
  "name": "Shaman",
  "qualified_name": "(Water) Shaman",
  "game": "gs1",
  "class_line": "water-shaman",
  "reachable_in_gs1": true,
  "available_to": [
    {
      "character": "Isaac",
      "djinn_requirements": [
        { "requirement": "6-7 Water Djinn", "source": "plz2bstfu-class" },
        { "requirement": "7 Mercury", "source": "strawhat" }
      ],
      "acr": null
    }
  ],
  "stat_multiplier": null,
  "psynergy": [
    { "name": "Froth", "sources": ["plz2bstfu-class", "strawhat"] },
    { "name": "Froth Spiral", "sources": ["strawhat"] },
    { "name": "Wish", "sources": ["plz2bstfu-class", "strawhat"] }
  ],
  "notes": null,
  "sources": ["plz2bstfu-class", "strawhat"]
}
```

(Example abbreviated.)

### Notes for CC (Extraction Instructions)

When extracting class data from raw source files:

1. **One JSON object per distinct class** per the Class ID Disambiguation
   table. A class shared by two characters is ONE entry with multiple
   `available_to` objects ONLY when both characters' psynergy lists are
   identical in the sources (Brute line, Ninja, Samurai, Dragoon,
   Hermit/Elder/Scholar/Savant/Sage, Medium, Ranger, White Mage). When the
   lists differ (Swordsman, Seer, Pilgrim lines...), split per character.
2. **Tier groups**: strawhat groups tiers ("Squire/Knight", "Gallant/Lord/
   Slayer") and gives one psynergy list per group; plz2bstfu lists each tier
   with "Same as X, with these additions". Expand both into per-tier entries.
   A strawhat group list applies to every tier in the group.
3. **plz2bstfu psynergy lists are level-29/30 snapshots** — they omit
   psynergy learned at higher levels. A spell present in strawhat but absent
   in plz2bstfu is NOT a conflict. A spell present in plz2bstfu but absent
   from strawhat's class list (e.g. Revive on Gallant/Lord) should be
   included with plz2bstfu attribution and noted in `notes` if it looks like
   a strawhat omission.
4. **djinn_requirements**: keep each source's phrasing. plz2bstfu states
   counts of non-base elements relative to the character ("1 Fire Djinni");
   strawhat gives example 7-8 djinn setups ("3 Venus, 3 Mars"); aku-chi
   gives top-tier setups ("1 earth, 6 wind"). These describe the same class
   from different angles — record all, flag only direct contradictions.
5. **stat_multiplier / acr**: only aku-chi provides these, and only for the
   classes it discusses. stat_multiplier is class-level; acr is per
   character + class (lives in `available_to`).
6. **8-djinn classes** (Slayer, Chaos Lord, War Adept — mentioned only in
   strawhat's tier headers): create entries with `reachable_in_gs1: false`
   and a note. Do not invent psynergy beyond the tier-group list.
7. **Jenna's Flame User** (strawhat section 2.5): one entry, `available_to`
   Jenna, psynergy Flare / Flare Wall / Flare Storm, note that her class
   cannot be changed.
8. **strawhat's "(Earth) Shaman" header for Ivan** is a typo: its content
   matches plz2bstfu's "(Earth) Enchanter". Extract as `earth-enchanter`
   and flag in `conflicts` or `notes`.
9. **Normalize element words**: sources mix Venus/Mars/Jupiter/Mercury with
   earth/fire/wind/water. Keep requirement strings close to source wording
   but the rest of the entry uses earth/fire/wind/water.
10. **Do not invent data.** Missing stat multipliers stay null; do not
    derive them from Terence's GS2 guide or memory.

---

## Schema: `psynergy`

One entry per distinct psynergy ability. Abilities sharing a display name but
mechanically distinct (the two "Blast" lines) get separate entries with
distinct ids. Upgrades (Cure → Cure Well → Potent Cure) are separate entries
linked by `series` + `tier`.

File: `data/gs1/psynergy.json`

```
Field                   Type              Required   Notes
---------------------------------------------------------------------------
id                      string            YES        Lowercase, hyphens only. e.g. "ragnarok",
                                                     "mother-gaia". For the two "Blast" lines:
                                                     "blast-nova" (7pp, Nova series) and
                                                     "blast-mad" (5pp, Mad Blast series).
name                    string            YES        Display name. e.g. "Mother Gaia", "Blast"
game                    string            YES        Always "gs1" for this file.
element                 string | null     YES        One of: "earth" | "fire" | "wind" | "water".
                                                     null for non-elemental utility psynergy
                                                     (Move, Retreat, Catch, Avoid, ...).
category                string            YES        Primary effect. See Category Enum below.
pp_cost                 integer | null    YES        PP cost. null only if no source states it.
range                   integer | string  YES        Number of targets: 1, 3, 5, 7, or "all"
                        | null                       for party-wide effects. null for field-only
                                                     utility psynergy. See Range Notation Mapping.
target                  string            YES        "enemy" | "ally" | "none".
                                                     "ally" covers self/single-ally/party
                                                     beneficial psynergy (disambiguated by range).
                                                     "none" for field utility.
battle_usable           boolean           YES        false for field-only psynergy (Move,
                                                     Retreat, Mind Read, Catch, ...). Avoid is
                                                     field-only → false.
level_learned           integer | null    YES        Level learned, from strawhat. When strawhat
                                                     lists different levels per class, use the
                                                     LOWEST and put the rest in
                                                     level_learned_variants. null if not given
                                                     (item-granted or default psynergy).
level_learned_variants  string | null     NO         Per-class level variations, condensed from
                                                     strawhat. e.g. "20 (Apprentice line) / 24
                                                     (Brute line)". Omit or null if none.
series                  string | null     YES        `id` of the series' first tier. e.g.
                                                     "growth" for Growth/Mad Growth/Wild Growth;
                                                     "blast-nova" vs "blast-mad" keeps the two
                                                     Blast lines distinct. null for standalone
                                                     psynergy.
tier                    integer | null    YES        1-based position within the series.
                                                     null when series is null.
description             string | null     YES        In-game description text from sources.
                                                     e.g. "Attack with the earth's might."
effect_notes            string | null     YES        Mechanics beyond the description: healing
                                                     amounts, status chances, instant-kill
                                                     attempts, source commentary worth keeping.
                                                     null if nothing to add.
field_effect            string | null     NO         Out-of-battle use of a battle psynergy
                                                     (e.g. Frost freezes puddles, Gale/Whirlwind
                                                     clear vines). null/omit if none.
available_to            array of string   YES        Characters who can access this psynergy via
                                                     any class or item, per sources.
                                                     Subset of ["Isaac","Garet","Ivan","Mia",
                                                     "Jenna"].
acquired_via_item       object | null     YES        For psynergy granted by equipping an item.
                                                     null for class-learned psynergy.
  .item                 string            YES        Item name. e.g. "Catch Beads"
  .location             string | null     YES        Where the item is obtained, prose from
                                                     source. null if not stated.
  .source               string            YES        Source ID for the item/location info.
sources                 array of string   YES        All source IDs that contributed data.
conflicts               array of object   NO         Only present if sources disagree on a field.
                                                     Same shape as in other schemas.
  [].field              string            YES        e.g. "pp_cost", "range", "element"
  [].values             object            YES        Map of source_id → conflicting value.
  [].note               string | null     NO         Optional human note.
```

Note: the class → psynergy mapping lives in `classes.json` (`psynergy`
arrays). It is NOT duplicated here; psynergy entries only carry the coarser
`available_to` character list.

### Range Notation Mapping

Sources draw target counts as bar/tally diagrams. Map as follows:

| Source | Notation | Meaning |
|---|---|---|
| jiggyhunter | `I`, `III`, `IIIII`, `IIIIIII`, `IIIIIIIII` | 1, 3, 5, 7, all |
| tetzcatlipoca | `\|`, `\|\|\|`, `\|\|\|\|\|`, `\|\|\|\|\|\|\|`, `\|\|\|\|\|\|\|\|\|` | 1, 3, 5, 7, all |
| strawhat | `\|`, `;\|;`, `,;\|;,` or `.;\|;.`, `.,;\|;,.` or `,,;\|;,,` | 1, 3, 5, 7 |
| strawhat | 7+ plain bars on a beneficial effect | all |

Nine-or-more-bar tallies map to `"all"` on either side: party-wide
beneficial effects (descriptions saying "party's", "whole party", "entire
party") AND all-enemy effects (Break). Sources are inconsistent about drawing
7, 8, 9, or 10 bars for these — descriptions take precedence over bar count.
Offensive *damage* psynergy caps at 7 targets; only non-damaging
all-enemy effects use `"all"` with `target: "enemy"`.

### Category Enum

```
category = "attack"   — deals damage (incl. elemental physical attacks and
                        damage+status moves like Annihilation, Helm Splitter)
           "healing"  — restores HP or revives (Cure/Ply/Wish lines, Revive)
           "buff"     — raises allies' stats (Impact, Guard, Ward, Demon
                        Spear, Magic Shell lines)
           "debuff"   — lowers enemy stats or removes bonuses (Impair,
                        Weaken, Dull lines, Break)
           "status"   — inflicts or cures status conditions without damage
                        (Delude, Sleep, Bind, Mist, Haunt, Curse, Condemn,
                        Cure Poison, Restore)
           "drain"    — absorbs HP/PP (Drain, Psy Drain)
           "utility"  — field/non-combat (Move, Retreat, Mind Read, Reveal,
                        Catch, Force, Lift, Carry, Halt, Cloak, Avoid)
```

### Example Entry: Ragnarok

```json
{
  "id": "ragnarok",
  "name": "Ragnarok",
  "game": "gs1",
  "element": "earth",
  "category": "attack",
  "pp_cost": 7,
  "range": 1,
  "target": "enemy",
  "battle_usable": true,
  "level_learned": 13,
  "series": null,
  "tier": null,
  "description": "Strike with a massive sword.",
  "effect_notes": "One of the most powerful attacks available early in the game (strawhat).",
  "available_to": ["Isaac"],
  "acquired_via_item": null,
  "sources": ["jiggyhunter", "tetzcatlipoca", "strawhat", "plz2bstfu-class"]
}
```

### Example Entry: Wish (party heal)

```json
{
  "id": "wish",
  "name": "Wish",
  "game": "gs1",
  "element": "water",
  "category": "healing",
  "pp_cost": 9,
  "range": "all",
  "target": "ally",
  "battle_usable": true,
  "level_learned": 5,
  "level_learned_variants": "5 (Isaac water classes) / 8 (Garet, Mia most classes) / 12 (Ivan, Mia wind classes)",
  "series": "wish",
  "tier": 1,
  "description": "Restore 80 HP to the whole party.",
  "effect_notes": null,
  "available_to": ["Isaac", "Garet", "Ivan", "Mia"],
  "acquired_via_item": null,
  "sources": ["jiggyhunter", "tetzcatlipoca", "strawhat", "plz2bstfu-class"]
}
```

### Example Entry: Force (item-granted utility)

```json
{
  "id": "force",
  "name": "Force",
  "game": "gs1",
  "element": null,
  "category": "utility",
  "pp_cost": 2,
  "range": null,
  "target": "none",
  "battle_usable": false,
  "level_learned": null,
  "series": null,
  "tier": null,
  "description": "Strike a distant object.",
  "effect_notes": "Not needed to complete the game (tetzcatlipoca).",
  "available_to": ["Isaac", "Garet", "Ivan", "Mia"],
  "acquired_via_item": {
    "item": "Orb of Force",
    "location": "Complete the puzzles in Fuchin Falls Cave.",
    "source": "tetzcatlipoca"
  },
  "sources": ["tetzcatlipoca", "strawhat"],
  "conflicts": [
    {
      "field": "acquired_via_item.item",
      "values": {
        "tetzcatlipoca": "Orb of Force",
        "strawhat": "Force Gem"
      },
      "note": null
    }
  ]
}
```

### Notes for CC (Extraction Instructions)

When extracting psynergy data from raw source files:

1. **One entry per distinct ability.** The two "Blast" abilities (Nova series
   7pp Mars vs. Mad Blast series 5pp Mars) are separate entries (`blast-nova`,
   `blast-mad`). Series upgrades are separate entries linked via
   `series`/`tier`.
2. **Series membership** is established by shared in-game description text
   and escalating PP within a source's grouping (e.g. all three Growth tiers
   read "Attack with ... plants"), and by aku-chi's explicit "the X series"
   references. Do not group on name similarity alone.
3. **strawhat transcription errors** — do not import these as separate
   abilities; map to the real ability and flag in `conflicts`/`effect_notes`
   when values differ:
   - second "Thunderbolt" (lv 50) = Thunderstorm
   - second "Clay Spire" (22pp, lv 42) = Stone Spire
   - second "Storm Ray" (21pp, lv 36) = Destruct Ray
   - second "Rockslide" (30pp, lv 54) / "Avanlanche" = Avalanche
   - the 13-PP Mars "Haunt" with description "Attack with a massive
     explosion" is a corrupted duplicate; the real Haunt is 5pp Venus
   - Sleep and Bind carry the description "Boost Resistance" (copy-paste);
     use jiggyhunter/tetzcatlipoca descriptions instead
   - "Ice Missle", "High Impace", "Sonich Slash", "Asceti" etc. are typos
4. **PP and range conflicts**: where sources disagree (Curse 6 vs 5, Bind 4
   vs 7, Wild Growth 19 vs 15, Grand Gaia 32 vs 17, Ply 4 vs 3, Thorn 6 vs 4,
   Spire range 1 vs 3, Stone Spire range 5 vs 3, Typhoon range 5 vs 3, Fire
   Bomb range 3 vs 5, Hurricane range 7 vs 5, Dull element wind vs water...)
   set the field to the MAJORITY value when 2+ sources agree, otherwise the
   tetzcatlipoca value, and always record the disagreement in `conflicts`.
5. **level_learned comes from strawhat only.** Other sources don't track it.
   Lowest value into `level_learned`, the rest into `level_learned_variants`.
6. **Item-granted psynergy** (Catch, Force, Lift, Carry, Halt, Cloak +
   Douse/Frost which are also class psynergy): populate `acquired_via_item`
   from tetzcatlipoca's "Everyone" section (richer location prose), flag
   item-name disagreements with strawhat (Orb of Force vs Force Gem, Carry
   Stone vs Carry Gem).
7. **available_to**: union of the characters under whose section the
   psynergy appears in tetzcatlipoca/strawhat, plus all four for item-granted
   psynergy, plus Jenna for her Flame User moves. The djinn-trade bracket
   codes ([M], [J(4)]...) in tetzcatlipoca encode class requirements already
   captured in classes.json — do not model them here.
8. **Healing amounts** ("Restore 70 HP") stay in `description`; source
   caveats ("restores AROUND 300 HP") go to `effect_notes`.
9. **Do not invent data.** Jiggyhunter's "Description Needed" entries
   contribute PP/range only. If no source states a value, use null.

---

## Schema: `items`

One entry per non-equippable item: consumables, stat-boost items, and key items.
Equippable gear (weapons, armor, rings/accessories) lives in `equipment.json`, NOT here.

File: `data/gs1/items.json`

```
Field               Type              Required   Notes
---------------------------------------------------------------------------
id                  string            YES        Lowercase, hyphens only. e.g. "herb",
                                                 "water-of-life", "black-orb"
name                string            YES        Display name as it appears in-game.
game                string            YES        Always "gs1" for this file.
item_type           string            YES        One of: "consumable" | "stat_boost" | "key"
                                                 See Item Type Enum below.

effect              object            YES        What the item does.
  .description      string            YES        Plain English. Preserve source wording.
  .target          string | null     YES        Who/what it affects when used.
                                                 One of: "ally" | "party" | "enemy" | "self" | null
                                                 null for key items with no battle/menu use.
  .stat_boosted    string | null     YES        For stat_boost items only: which stat is
                                                 permanently raised. One of:
                                                 "atk" | "def" | "hp" | "pp" | "agi" | "lck".
                                                 null for non-stat_boost items.

usable_in_battle    boolean           YES        true if the item can be selected/thrown in
                                                 battle (heals, revives, status, thrown damage).
                                                 false for field-only and key items.

buy_price           integer | null    YES        Shop purchase price in coins.
                                                 null if not sold in shops ("N/A" in source).
sell_price          integer | null    YES        Sell value in coins. null if unsellable/unknown.

acquisition         object | null     NO         Where/how to obtain, beyond ordinary shops.
                                                 null when the item is only shop-bought or its
                                                 source gives no acquisition detail.
  .method           string            YES        "shop" | "chest" | "lucky_wheels" | "drop" |
                                                 "event" | "field" | "unobtainable"
  .location         string | null     YES        Town/dungeon/monster source. null if unknown.
  .notes            string | null     NO         Extra conditions or caveats.

sources             array of string   YES        All source IDs that contributed data.
conflicts           array of object   NO         Only present if sources disagree on a field.
                                                 Same shape as in other schemas.
  [].field          string            YES        Dot-notation path. e.g. "sell_price"
  [].values         object            YES        Map of source_id → conflicting value.
  [].note           string | null     NO         Optional human note.
```

### Item Type Enum

Derived from Super Slash's "Item List" sub-headings:

| item_type | Meaning | Examples |
|---|---|---|
| `consumable` | Used up on use: heals, status cures, thrown battle items, special tokens | Herb, Potion, Antidote, Smoke Bomb, Game Ticket |
| `stat_boost` | Permanently raises one stat of a party member | Apple, Cookie, Power Bread |
| `key` | Story/progression items; no HP/PP/battle effect | Black Orb, Mars Star, Cell Key |

Thrown battle items (Crystal Powder, Sleep Bomb, Smoke Bomb, Weasel's Claw) are
`consumable` with `usable_in_battle: true` and `effect.target: "enemy"`.

### Example Entry: Herb (consumable)

```json
{
  "id": "herb",
  "name": "Herb",
  "game": "gs1",
  "item_type": "consumable",
  "effect": {
    "description": "Replenishes 50 HP.",
    "target": "ally",
    "stat_boosted": null
  },
  "usable_in_battle": true,
  "buy_price": 10,
  "sell_price": 7,
  "acquisition": null,
  "sources": ["super-slash"]
}
```

### Example Entry: Apple (stat boost)

```json
{
  "id": "apple",
  "name": "Apple",
  "game": "gs1",
  "item_type": "stat_boost",
  "effect": {
    "description": "Permanently boosts a party member's Attack.",
    "target": "ally",
    "stat_boosted": "atk"
  },
  "usable_in_battle": false,
  "buy_price": null,
  "sell_price": 375,
  "acquisition": null,
  "sources": ["super-slash"]
}
```

### Example Entry: Black Orb (key item)

```json
{
  "id": "black-orb",
  "name": "Black Orb",
  "game": "gs1",
  "item_type": "key",
  "effect": {
    "description": "A mysterious orb that gets Babi's ship sailing.",
    "target": null,
    "stat_boosted": null
  },
  "usable_in_battle": false,
  "buy_price": null,
  "sell_price": null,
  "acquisition": null,
  "sources": ["super-slash"]
}
```

### Notes for CC (Extraction Instructions)

When extracting item data:

1. **Scope**: consumables, stat-boost items, key items ONLY. Do NOT include
   weapons, armor, or rings/accessories — those stay in `equipment.json`.
2. **Primary source**: Super Slash §VI "Item List" (full list with Buy/Sell
   prices and descriptions, grouped into Consumable / Stat-Increasing / Key).
   Map each sub-heading to `item_type`.
3. **buy_price / sell_price**: from Super Slash "Buy Price" / "Sells For".
   Translate "N/A" to `null`. Do NOT invent a buy price for items Super Slash
   marks N/A, even if another source lists a nominal value — note that in
   `acquisition.notes` or `conflicts` instead.
4. **acquisition**: populate from rockettrekkie (Artifacts Guide) for the items
   it covers (Potion, Psy Crystal, Water of Life, Hermes' Water, Empty Bottle,
   Game Ticket, Lucky Medal, Cell Key). null when no source gives detail.
5. **Migrated entries**: Potion, Psy Crystal, Water of Life, Hermes' Water,
   Empty Bottle, Game Ticket, Lucky Medal, Cell Key were previously misfiled in
   `equipment.json` (category "item"). They now live here; their rockettrekkie
   acquisition/use data is preserved. The 6 rings stay in `equipment.json`.
6. **usable_in_battle**: true for HP/PP restore, revive, status cure, and thrown
   damage/status items. false for stat_boost, field-only (Sacred Feather), and
   key items.
7. **Do not invent data.** Use `null` for any field no source confirms.

---

## Schema: `summons`

One entry per summon spirit. GS1 has 16 summons: 4 per element, unlocked by
having that many Djinn of the element on Standby in battle.

File: `data/gs1/summons.json`

```
Field               Type              Required   Notes
---------------------------------------------------------------------------
id                  string            YES        Lowercase, hyphens only. e.g. "judgment",
                                                 "ramses". Base elemental summons share their
                                                 element's name: "venus", "mars", "jupiter",
                                                 "mercury".
name                string            YES        Display name. Use in-game GS1 spelling
                                                 (e.g. "Judgment", not "Judgement").
element             string            YES        One of: "earth" | "fire" | "wind" | "water"
game                string            YES        Always "gs1" for this file.
djinn_required      integer           YES        Number of Standby Djinn of `element` needed to
                                                 summon (1-4). Also functions as the summon's
                                                 tier within its element (1 = weakest).
damage_power        integer | null    YES        Base summon power. null when no ingested source
                                                 provides a number (current sources do not).
effect              string | null     YES        Special/secondary effect text. null if none/unknown.
sources             array of string   YES        All source IDs that contributed data.
conflicts           array of object   NO         Only if sources disagree. Same shape as elsewhere.
```

### Example Entry: Judgment

```json
{
  "id": "judgment",
  "name": "Judgment",
  "element": "earth",
  "game": "gs1",
  "djinn_required": 4,
  "damage_power": null,
  "effect": null,
  "sources": ["telago", "bfgamer"]
}
```

### Notes for CC (Extraction Instructions)

When extracting summon data:

1. **16 entries total**: 4 per element × 4 elements. Map the Djinn-count →
   spirit name from Telago §2 "Summons Table" and BFGamer §6.2.
2. **element ↔ Djinn type**: Venus = earth, Mars = fire, Jupiter = wind,
   Mercury = water.
3. **djinn_required** = the standby-Djinn count beside the spirit name (1-4).
4. **Spelling**: prefer in-game GS1 spelling. "Judgment" (Telago), not
   "Judgement" (BFGamer) — a spelling variant, not a data conflict.
5. **damage_power / effect**: current ingested sources (Telago, BFGamer,
   Super Slash) only list names; leave these `null`. Populate later if a
   source with summon power numbers is ingested.
6. **Do not invent data.**

---

## Schema: `shops`

One entry per town that has shops. Each entry lists the town's combined stock
(weapons, armor, items) with buy price. Stock names reference `equipment.json`
and `items.json` entries by display name.

File: `data/gs1/shops.json`

```
Field               Type              Required   Notes
---------------------------------------------------------------------------
id                  string            YES        Town slug. e.g. "vale", "lalivero"
name                string            YES        Town display name. e.g. "Vale"
game                string            YES        Always "gs1" for this file.
availability_notes  string | null     YES        Conditions on when the shop opens, if any.
                                                 e.g. "Shops are closed until Tret's curse is
                                                 lifted." null when unconditional.

stock               array of object   YES        Everything the town sells.
  [].name           string            YES        Display name (matches equipment.json/items.json).
  [].category       string            YES        One of: "weapon" | "armor" | "item"
  [].price          integer           YES        Buy price in coins.
  [].is_artifact    boolean           YES        true if sold as an artifact (Shotgunnova marks
                                                 these with "*"; they appear in shops only after
                                                 being sold once, or are stocked specially).

sources             array of string   YES        All source IDs that contributed data.
conflicts           array of object   NO         Only if sources disagree. Same shape as elsewhere.
  [].field          string            YES        e.g. "stock[Wooden Stick].price"
  [].values         object            YES        Map of source_id → conflicting value.
  [].note           string | null     NO
```

### Example Entry: Vale

```json
{
  "id": "vale",
  "name": "Vale",
  "game": "gs1",
  "availability_notes": null,
  "stock": [
    { "name": "Herb", "category": "item", "price": 10, "is_artifact": false },
    { "name": "Short Sword", "category": "weapon", "price": 120, "is_artifact": false },
    { "name": "Travel Vest", "category": "armor", "price": 50, "is_artifact": false }
  ],
  "sources": ["shotgunnova", "super-slash"],
  "conflicts": [
    {
      "field": "stock[Wooden Stick].price",
      "values": { "shotgunnova": 60, "super-slash": 40 },
      "note": null
    }
  ]
}
```

### Notes for CC (Extraction Instructions)

When extracting shop data:

1. **One entry per town.** GS1 has 12 shop towns: Vale, Vault, Bilibin, Imil,
   Kolima, Xian, Altin, Kalay, Tolbi, Lunpa, Suhalla, Lalivero.
2. **Primary source**: Shotgunnova [SHPL] — one combined table per town with a
   COST column and "*" artifact markers. Derive `category` from which stat
   column is filled: DEF → armor (incl. gloves like War Gloves), else ATK →
   weapon, else (consumable) → item.
3. **is_artifact**: true when the Shotgunnova row begins with "*".
4. **Cross-check** against Super Slash §XIV (which splits Weapon/Armor/Item
   shops per town but OMITS artifacts). Flag price disagreements in `conflicts`
   (e.g. Wooden Stick 60 vs 40, Circlet 130 vs 120, Battle Rapier 2800 vs 2900).
   Super Slash's omission of artifacts is NOT a conflict.
5. **availability_notes**: capture Shotgunnova's bracketed notes (Imil, Kolima,
   Lunpa).
6. **Do not invent data.**

---

## Schema: `monsters`

One entry per enemy stat-line in the GS1 bestiary. Covers regular enemies,
fightable Djinn, and boss stat-entries. Bosses also have a richer entry in
`bosses.json` (attacks, encounters, strategy); here they appear as a flat
stat-line cross-linked via `boss_id`. Use `is_boss` to filter them out.

File: `data/gs1/monsters.json`

```
Field                 Type              Required   Notes
---------------------------------------------------------------------------
id                    string            YES        Lowercase, hyphens. Includes variant suffix.
                                                   e.g. "vermin-1", "mimic-3", "mars-djinni-forge"
name                  string            YES        Base display name without variant number.
                                                   e.g. "Vermin", "Mimic", "Saturos"
game                  string            YES        Always "gs1".
variant               integer | null    YES        Variant number from Super Slash "(n)" suffix.
                                                   null when the enemy has no variant.
is_boss               boolean           YES        true if this stat-line is a boss (links bosses.json).
boss_id               string | null     YES        bosses.json id when is_boss, else null.
is_djinn_enemy        boolean           YES        true for fightable Djinn ("X Djinni (Name)").
djinn_id              string | null     YES        djinn.json id when is_djinn_enemy, else null.
                                                   null for the secret/unknown Venus Djinni.

found                 array of string   YES        Locations where encountered. Union of sources.
stats                 object            YES
  .hp                 integer | null    YES
  .pp                 integer | null    YES
  .hp_regen           integer | null    YES        HP regen/turn (Torrent only; null if unknown).
  .pp_regen           integer | null    YES        PP regen/turn (Torrent only).
  .atk                integer | null    YES
  .def                integer | null    YES
  .agi                integer | null    YES
  .lck                integer | null    YES
  .turns              integer | null    YES        Actions per turn.

elemental_power       object            YES        Attack power per element. Map by element NAME,
                                                   not column order (sources differ).
  .earth/.fire/.wind/.water  integer    YES        Venus=earth, Mars=fire, Jupiter=wind, Mercury=water.
elemental_resistance  object            YES        Same shape as elemental_power.

abilities             array of string   YES        Move names (Torrent ::Abilities::). May include
                                                   "Attack"/"Defend". [] if none listed.
drops                 object            YES
  .exp                integer | null    YES
  .coins              integer | null    YES
  .items              array of object   YES        [] if no item drop.
    [].name           string            YES        Item name (matches items.json/equipment.json).
    [].icc            integer | null    YES        Torrent "Item Class Chance" (drop-rate class).
                                                   null if only Super Slash lists the item.

sources               array of string   YES
conflicts             array of object   NO         Cross-source stat disagreements. Same shape as elsewhere.
```

### Example Entry: Vermin

```json
{
  "id": "vermin-1",
  "name": "Vermin",
  "game": "gs1",
  "variant": 1,
  "is_boss": false,
  "boss_id": null,
  "is_djinn_enemy": false,
  "djinn_id": null,
  "found": ["Vale", "Sol Sanctum"],
  "stats": { "hp": 20, "pp": 0, "hp_regen": 0, "pp_regen": 0, "atk": 23, "def": 7, "agi": 7, "lck": 2, "turns": 1 },
  "elemental_power": { "earth": 100, "fire": 70, "wind": 80, "water": 80 },
  "elemental_resistance": { "earth": 48, "fire": 25, "wind": 72, "water": 48 },
  "abilities": ["Attack", "Defend"],
  "drops": { "exp": 2, "coins": 2, "items": [ { "name": "Herb", "icc": 5 } ] },
  "sources": ["super-slash", "torrent-load"]
}
```

### Notes for CC (Extraction Instructions)

When extracting monster data (preferably via `scripts/monsters_extract.py`):

1. **Two aligned sources**: Super Slash §XIII and Torrent Load complete list
   each contain the SAME 152 enemies in the SAME order — match by index.
2. **Element mapping is by NAME, not column**: Super Slash lists Venus/Mars/
   Jupiter/Mercury; Torrent lists Ven/Mrc/Mar/Jup. Map Venus=earth, Mars=fire,
   Jupiter=wind, Mercury=water in both.
3. **regen + abilities + drop ICC**: Torrent only. Super Slash has no regen,
   no ability list, and no drop rates.
4. **variant**: from Super Slash "(n)" suffix (Vermin (1) → variant 1). The
   parenthetical in "Mars Djinni (Forge)" is the Djinn name, not a variant.
5. **is_boss / boss_id**: map boss stat-lines to `bosses.json`. Mystery Woman →
   menardi, Mystery Man → saturos (prologue forms). Saturos/Menardi appear more
   than once (different encounters) — all link to the same boss_id.
6. **is_djinn_enemy / djinn_id**: "X Djinni (Name)" → link djinn.json by the
   inner name. The secret "Venus Djinni (???)" / "Unknown Venus Djinni" has
   djinn_id null.
7. **conflicts**: flag any stat/elemental/drop disagreement between the two
   sources. Do not silently pick a winner (Super Slash is the default value).
8. **Do not invent data.**
