# Golden Sun 1 — Distilled Walkthrough Template

File: `gs1_walkthrough_template.md`
Lore-Engine | `schema/gs1/`
Last updated: 2026-06-09
Status: v1.0 — Template (not filled)

---

## Purpose

This file defines the structure of `gs1_walkthrough.md` — a distilled,
human-readable walkthrough synthesised from multiple FAQ sources. It serves
two roles simultaneously:

1. **Readable document** — navigable by a person playing the game
2. **Structured data layer** — consistent enough to be parsed or converted
   to JSON in a later pipeline phase

---

## General Rules

- **Two-level hierarchy**: Chapter (narrative arc) → Location (place entity).
  A chapter can contain multiple locations. A location can appear in multiple
  chapters (e.g. Vault revisited).
- **Optional fields**: Only include a section if data exists. Do not write
  empty headers or blank lists.
- **Conflict footnotes**: When sources disagree, keep the most commonly
  attested version in the main text and add a `[^note]` footnote. See format
  below.
- **Source attribution**: Each chapter footer lists which sources contributed
  to that chapter.
- **Prose in Narrative**: Write in second person ("Head north…"), synthesising
  across sources. Do not copy verbatim from any single FAQ.

---

## Source IDs

| ID               | Document                                                        |
|------------------|-----------------------------------------------------------------|
| `telago`         | FAQ/Walkthrough by Iron Knuckle / Telago (GameFAQs, v2.1)      |
| `electrospecter` | FAQ/Walkthrough by ElectroSpecter (GameFAQs, Final Version)     |
| `bf-gamer`       | Walkthrough/FAQ by BF_Gamer (GameFAQs, v1.0)                   |
| `ikillkenny`     | Comprehensive FAQ/Walkthrough by Ikillkenny (GameFAQs, v2.0a)  |

Add new rows here when new sources are ingested.

---

## Conflict Footnote Format

Use inline footnote markers `[^N]` directly after the contested value.
Define footnotes at the bottom of each chapter section (not the whole file).
Reset numbering per chapter.

**Example — inline marker:**
```
- Hail[^1] — random encounter west of Tolbi
```

**Example — footnote definition:**
```
[^1]: **Source conflict** — `telago`: random encounter on world map west of
Tolbi near the bridges; `electrospecter`: fixed spawn on Gondowan Cliffs
plateau. Most sources favour the world map west of Tolbi.
```

---

## File-Level Template

```markdown
# Golden Sun 1 — Distilled Walkthrough

> Synthesised from: telago, electrospecter, bf-gamer, ikillkenny
> Game: Golden Sun (GBA, 2001)
> Pipeline: Project Lore-Engine

---

[Chapter entries follow — see Chapter Template below]
```

---

## Chapter Template

````markdown
## Chapter N — [Narrative Title]

> **Objective**: One-sentence summary of what this chapter accomplishes
> in the main story.

[One or more Location blocks — see Location Template below]

---
*Sources for this chapter: `telago`, `electrospecter`*

[Footnotes for this chapter]
[^1]: **Source conflict** — ...
````

---

## Location Template

````markdown
### [Location Name]

**Enemies**
- Enemy Name
- Enemy Name

**Items**
- Item Name — where to find it (e.g. chest in northwest corner)
- Item Name — hidden in barrel near inn entrance

**Djinn**
- Element — Djinn Name — brief acquisition note (e.g. "battle on world map")

**Shop**
| Item | Price |
|------|-------|
| Herb | 10    |
| Long Sword | 200 |

**Boss: [Boss Name]**
- HP / ATK / DEF / AGL / LCK
- Weak: [element] — Strong: [element]
- Special: [notable attacks or mechanics]
- Strategy: [1–2 sentence synthesis]

**Narrative**
Head [direction] to reach… [step-by-step prose, second person, synthesised
from sources]. Notable: [any tip or mechanic worth flagging].
````

**Field rules:**

| Field | Required | Notes |
|-------|----------|-------|
| Enemies | Optional | Omit if no new enemies in this location |
| Items | Optional | Omit if no obtainable items |
| Djinn | Optional | Only include Djinn first obtainable here |
| Shop | Optional | Include only if shop inventory is relevant |
| Boss | Optional | Include only if a boss/mini-boss fight occurs here |
| Narrative | Required | Always present; minimum 1 paragraph |

---

## Worked Example

The following is a filled example using Vault (Chapter 2) to illustrate
correct usage of all fields. CC should use this as a reference during
extraction.

````markdown
## Chapter 2 — Solving the Burglaries in Vault

> **Objective**: Recover Master Hammet's stolen rod, recruit Ivan, and
> defeat the Lunpa bandits hiding in the Inn.

### World Map — Vale to Vault

**Djinn**
- Earth — Flint — joins automatically on first step outside Vale; cannot
  be declined

**Narrative**
On leaving Vale, Flint approaches immediately and joins the party,
demonstrating the Djinn system. Cross the bridge east and head south to
reach Vault. Hammet's caravan is stalled near the bridge to Kalay; they
will head north toward Lunpa instead.

---

### Vault

**Enemies**
*(none — no random encounters inside town)*

**Items**
- Sleep Bomb — barrel in right section of Item Shop
- Nut — box just outside Mayor's house
- 7 Coins — jar inside house near lower village entrance
- 4 Coins — barrel in centre house
- Mint — box on main floor of Inn
- Bone — speak to lady in Inn after defeating the bandits[^1]

**Djinn**
- Earth — Sap — not accessible yet; requires Reveal (obtainable only after
  Lamakan Desert)

**Shop**
| Item | Price |
|------|-------|
| Herb | 10 |
| Antidote | 20 |
| Long Sword | 200 |
| Short Sword | 120 |
| Mace | 80 |

**Boss: Bandit + Thief ×2**
- Bandit: HP 260 / ATK 46 / DEF 8 / AGL 20 / LCK 3 — Weak: All
- Thief: HP 110 / ATK 42 / DEF 5 / AGL 9 / LCK 1 — Weak: All
- Special: Bandit uses Herb, Smoke Bomb, Glower; Thief uses Herb, Intimidate,
  Defend
- Strategy: Focus all attacks on the Bandit first. Ivan and Garet Psynergy
  work well; human enemies are weak to all elements.

**Narrative**
Talk to the townspeople to learn about recent thefts. Find Ivan in the
northwest house upstairs; he joins the party and requests help locating
Hammet's rod. Use Mind Read (Ivan's Psynergy) on the suspicious guests at
the Inn: trap one in the upper-left corner using Garet and Isaac to block
the exits. After reading their minds, exit the Inn and climb the now-
unguarded ladder to the roof. Move the crate with Move Psynergy and enter
the storeroom to find the stolen goods and a captive woman. The Lunpa
bandits arrive immediately — Boss Fight. After winning, speak to the
Mayor for the Water of Life reward. Ivan retrieves the Shaman's Rod and
joins permanently.

---

### Goma Cave Entrance

**Narrative**
Jump the river and push the two movable pillars to continue. The third
pillar is blocked by foliage — Ivan reappears, demonstrates Whirlwind,
and joins permanently. Use Whirlwind on the foliage to open the cave
entrance. Optional: backtrack to Vale and use Whirlwind to open the
hidden cavern behind the shop for a Power Bread chest.

---

### Goma Cave

**Enemies**
- Ghost
- Skeleton
- Slime
- Will Head
- Zombie

**Items**
- Lucky Medal — chest on right side of upper area

**Djinn**
- Fire — Forge — defeat in battle; set up by moving bottom pillar so you
  can jump to the ledge above the man

**Boss: Forge (Djinn Battle)**
- HP 172 / ATK 45 / DEF 9 / AGL 22 / LCK 6 — Weak: Water — Strong: Fire
- Special: Flare, Blast, Escape
- Strategy: Hit with Water-element attacks or Mia's Psynergy if available.
  If Forge attempts to flee, re-enter the area to respawn the encounter.

**Narrative**
The route is mostly linear. Head south, down the stairs, and far right to
place a pillar and speak to the NPC if desired. Return left, jump the
lower water stream, then move the tall pillar on the right to create a
jump point. Push the small fat pillar off the edge into the water below to
form a bridge. Collect the Lucky Medal from the chest. Use the new bridge
path to reach Forge. After obtaining Forge, continue east to exit.

---
*Sources for this chapter: `telago`, `electrospecter`, `ikillkenny`*

[^1]: **Item note** — The Bone item received from the Inn lady after the
bandit fight has no use except giving it to the dog in the village. `telago`
notes it explicitly; `electrospecter` and `bf-gamer` omit it. Safe to
include as a low-priority item.
````

---

## Notes for CC (Extraction Instructions)

When extracting from the four source files to produce `gs1_walkthrough.md`:

1. **Chapter boundaries**: Use Telago's chapter titles as the primary
   chapter structure — they map most cleanly to narrative arcs.

2. **Location names**: Normalise to the most common spelling across sources.
   When sources differ (e.g. "Lunpa" vs "Lupna"), use the majority spelling
   and add a footnote only if the discrepancy is significant.

3. **Items**: Telago is the primary source for hidden items (most complete,
   has cumulative count tracking). ElectroSpecter is the primary source for
   shop lists. Cross-check with other sources where available.

4. **Enemies**: ElectroSpecter and Telago both have enemy lists per location.
   Use the union of both — if one source has an enemy the other doesn't,
   include it.

5. **Djinn**: Use Telago as primary (inline with walkthrough). Cross-check
   location details against existing `djinn.json` entries.

6. **Boss blocks**: Telago has the most complete stat blocks. Use Telago
   stats as primary; note discrepancies from other sources in footnotes.

7. **Narrative**: Synthesise — do not copy verbatim from any single source.
   Prefer second person ("Head north…"). Favour concision over completeness;
   the goal is a usable reference, not a transcript of all four FAQs.

8. **Conflicts**: Any field where two sources give materially different
   information (different location, different item, different stat) should
   be footnoted. Minor wording differences do not need footnotes.

9. **Optional fields**: If a location has no shop, no boss, no Djinn —
   simply omit those headers entirely. Do not write `**Shop**: none`.

10. **One file**: The output is a single `gs1_walkthrough.md` file covering
    the full game, chapter by chapter.