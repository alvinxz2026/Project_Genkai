# gs1_schema.md
# Golden Sun 1 — Data Schema Definitions
# Lore-Engine | schema/gs1/

Last updated: 2026-06-07
Status: v1.0

---

## General Rules

- All field names use `snake_case`.
- String values use `lowercase` unless the value is a proper noun (e.g. `"Flint"`, `"Vale"`).
- Use `0` when a stat bonus is confirmed to be zero. Use `null` only when data is missing or unconfirmed from all sources.
- `sources` lists every FAQ or reference that contributed data to this entry. Add a source whenever a new document is ingested.
- When two sources conflict on the same field, do NOT silently pick a winner. Flag it using `conflicts` (see field definition below).

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

---

## Damage Format

The `battle_effect.damage` field uses the following codes, inherited from Terence's FAQ:

| Code | Meaning |
|---|---|
| `"mXXX%"` | Elemental physical attack. Mult Mod = XXX / 100. Add Mod = 0. e.g. `"m160%"` = 1.6× normal attack. |
| `"aXX"` | Elemental physical attack. Mult Mod = 1. Add Mod = XX flat damage added. e.g. `"a50"` = normal attack + 50. |
| `null` | No damage. Effect only (buff, debuff, heal, status). |

Both `m` and `a` types use Relative Attack (User Attack − Target Defense) as base, with a 50%–150% elemental modifier applied.

---

## Source IDs

| ID | Document |
|---|---|
| `plz2bstfu` | Djinn Location List by plz2bstfu (GameFAQs, 2001) |
| `terence` | Djinn/Class Mechanics FAQ by Terence Fergusson (GameFAQs, 2002) |
| `golden-sun-wiki` | Golden Sun Wiki (community wiki, fetched 2026) |
| `linkt` | Boss Guide by LinkTheValiant (GameFAQs, 2006) |
| `fandom-wiki` | Golden Sun Fandom Wiki (fetched 2026-06-07) |

Add new rows here when new sources are ingested.

---

## Example Entry: Flint

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

---

## Example Entry: with conflict flag

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

---

## Notes for CC (Extraction Instructions)

When extracting Djinn data from raw source files:

1. **One JSON object per Djinni.** All 28 GS1 Djinn should produce 28 entries.
2. **Use `0` for confirmed-zero stat bonuses**, not `null`. Terence's table uses `--` to mean 0 — translate these to `0`.
3. **Preserve original location prose** in `location.description`. Do not paraphrase or summarise — keep it close to the source wording.
4. **Flag conflicts explicitly** using the `conflicts` field. Do not silently pick one source over another.
5. **Add the source ID** to `sources` for every field you populate from that document.
6. **Do not invent data.** If a field cannot be determined from available sources, use `null` and do not guess.