# Golden Sun 1 — Data Schema Definitions

File: `gs1_schema.md`
Lore-Engine | `schema/gs1/`
Last updated: 2026-06-08
Status: v1.0

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

---

## General Rules

- All field names use `snake_case`.
- String values use `lowercase` unless the value is a proper noun (e.g. `"Flint"`, `"Vale"`).
- Use `0` when a stat bonus is confirmed to be zero. Use `null` only when data is missing or unconfirmed from all sources.
- `sources` lists every FAQ or reference that contributed data to this entry. Add a source whenever a new document is ingested.
- When two sources conflict on the same field, do NOT silently pick a winner. Flag it using `conflicts` (see field definition below).

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

sources             array of string   YES        All FAQs/references that contributed data.
                                                 Use short identifiers (see Source IDs below).

conflicts           array of object   NO         Only present if two sources disagree on a field.
                                                 Omit this field entirely if no conflicts exist.
  [].field          string            YES        Which field the conflict is on. e.g. "location.area"
  [].values         object            YES        Map of source_id → conflicting value.
  [].note           string | null     NO         Optional human note explaining the discrepancy.
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
  "sources": ["plz2bstfu", "terence", "golden-sun-wiki"]
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
4. **Flag conflicts explicitly** using the `conflicts` field. Do not silently pick one source over another.
5. **Add the source ID** to `sources` for every field you populate from that document.
6. **Do not invent data.** If a field cannot be determined from available sources, use `null` and do not guess.

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
