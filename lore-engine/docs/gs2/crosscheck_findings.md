# GS2 — Cross-Check Findings (task 2/3)

> **This doc is the basis for later corrections.** It consolidates every
> cross-check finding so far into one place, classifies each as **FIXED /
> DECIDE / EXPECTED**, and queues the remaining (heavy, prose-level) semantic
> pass as a Gemini handoff. Per the schema General Rules we **flag cross-source
> conflicts, never silently pick a winner** — so most rows here are recorded for
> a human/decision pass, not auto-edited.
>
> Cross-check = do our **two independent provenance streams** agree?
> **In-Depth Guides** (data-table sources: torrentlord bestiary, demooni djinn,
> cooldude summons, mr-unorigino items, shotgunnova shops) vs the **consolidated
> 2a walkthrough** (`data/gs2/walkthrough/`, prose from the 10 Guide&Walkthrough
> sources). All findings below are reproducible by re-running the scripts in §3.

---

## 1. Status

| round | what | how | status |
|---|---|---|---|
| 1 | locations FK + structural resolution | `locations_refs_gs2.py` (deterministic) | ✅ 2026-06-19 |
| Q2b | item completeness vs 90Kirsdarke code table | `kirsdarke_completeness_gs2.py` (deterministic) | ✅ 2026-06-19 |
| 2 | In-Depth vs walkthrough **placement** (where things are) | `crosscheck_placement_gs2.py` (deterministic) | ✅ 2026-06-19 |
| 3 | **semantic** per-region prose vs entity JSON (boss numbers, fight reqs, drop/treasure detail) | Gemini 3.1 Pro per-region (B1–B8) | ✅ 2026-06-19 (boss/djinn-bearing focus) |

**Headline:** the two streams **broadly corroborate** across all three rounds.
Bosses agree on placement with 0 total-disagreements; monsters 59 agree; djinn 27
agree; summons agreements are mostly masked by landmark-vs-dungeon naming. **No
crisp auto-fixes surfaced in rounds 2–3** — and round 3 (semantic prose, verified
against JSON below) produced **0 changes to our data**: every §2E finding is a
prose-side error, semantic phrasing, or a single-source claim our chosen authority
doesn't back. Our entity data holds up against the independent walkthrough stream.

---

## 2. Findings

### 2A. FIXED (unambiguous, already applied)

| where | fix | why safe |
|---|---|---|
| `locations.json` connections | `n-osenia-islet` → `north-osenia-islet` | target node id exists, internal typo, no ambiguity |
| `locations.json` connections | `anemos-inner-sanctum` → `anemos-sanctum` | same |

### 2B. DECIDE — cross-source naming conflicts → **RESOLVED 2026-06-19**

> **Applied (user decision: adopt 90Kirsdarke canonical names).** The 6 equipment
> renames below are now in the data (`name` updated, old name in `name_variants`,
> `90kirsdarke-hack` credited in `sources`), folded into `items_extract_gs2.py`'s
> `NAME_FIXES` so they survive regeneration. `links_normalize`/`links_audit` now
> resolve refs via `name_variants` + `name_literal`, so any ref using an old name
> still links. Monster name variants normalized in `locations.json` (Tier A). The
> boss compound-name rows stay as designed (split entities). Original table kept
> below for provenance.

Our data is **faithful to its source**; these are cases where the source name
differs from another stream. Recommendation column = which looks like the real
game name.

| field | our value (source) | other stream | recommend |
|---|---|---|---|
| equipment | `Astral Circle`, `Psychic Circle` (mr-unorigino) | `…Circlet` (90Kirsdarke) | adopt **Circlet** (our other 5 circlets are "Circlet") |
| equipment | `Aeolian Cossack` (mr-unorigino) | `Aeolian Cassock` (90Kirsdarke) | adopt **Cassock** |
| equipment | `Leda's Armlet` (mr-unorigino) | `Leda's Bracelet` (90Kirsdarke) | adopt **Bracelet** |
| equipment | `Fireman's Rod` (mr-unorigino) | `Fireman's Pole` (90Kirsdarke) | adopt **Pole** |
| equipment | `Appolo's Axe` (mr-unorigino) | `Apollo's Axe` (90Kirsdarke) | adopt **Apollo's** |
| equipment | `Pirate's Sword` vs `Pirate's Sabre` | both exist in both | confirm two distinct items, keep both |
| monster | `Angle Worm` (torrentlord) | `Angler Worm` (walkthrough) | keep torrentlord (data-table authority); fix walkthrough mention |
| monster | `Momonga` (torrentlord) | `Momongo` (walkthrough) | keep **Momonga** |
| monster | `Wonder Bird` (torrentlord) | `Wonder Birds` (walkthrough) | keep **Wonder Bird** (singular) |
| boss | `Agatio`+`Karst`, `Moapa`+`Knight` (separate) | `Agatio & Karst`, `Moapa & Knights` (walkthrough compound) | model keeps split; add a compound→pair alias if a UI needs it |

> Note: 90Kirsdarke itself has author typos where **our value is correct**
> (`Beserker`→our `Berserker`, `Cosair`→our `Corsair`, `Saftey`→our `Safety`) —
> no action.

### 2C. djinn placement disagreements (round 2) → **RESOLVED 2026-06-19**

> **Applied:** `djinn.location.area` backfilled from the walkthrough-authoritative
> placement (`location_refs.json`) for all 44 located djinn via
> `djinn_area_backfill_gs2.py` — the 6 below now carry the precise dungeon region.
> `location.description` (demooni prose) is kept untouched.

6 djinn where the demooni description and the walkthrough resolve to **different
regions**. Caveat: the In-Depth side is a *substring match on demooni's prose*,
which often grabs the nearest **town** as a landmark, while the walkthrough names
the precise **dungeon**. Likely the walkthrough is more precise; worth a glance.
(`djinn.location.area` is currently null — these could be backfilled from
`location_refs.json` if we decide the walkthrough is authoritative for placement.)

| djinn | walkthrough | demooni-prose | likely |
|---|---|---|---|
| iron | indra-cavern | madra | check |
| meld | sea-of-time-islet | islet-cave | check |
| mud | gabomba-catacombs | kibombo | walkthrough (dungeon vs town) |
| steel | gabomba-statue | kibombo | walkthrough (dungeon vs town) |
| chill | gondowan-cliffs | naribwe | walkthrough (dungeon vs town) |
| sour | osenia-cavern | mikasalla | walkthrough (dungeon vs town) |

### 2D. EXPECTED — explained, **not** errors (recorded so they aren't re-litigated)

- **Recurring / ambush monsters** (round 2): `Mimic` (bestiary `found`=treasure-isle)
  and `Mad Plant` (=jupiter-lighthouse) appear in many walkthrough regions as
  chest-mimics / respawns. 16 of 19 monster "extras" are this or single-`found`
  monsters. Not a data error — the bestiary lists one canonical spot.
- **Summons landmark-vs-dungeon naming** (round 2): cooldude `found_at` uses a
  landmark ("Cave NW of Loho", "Cave SW of Contigo", "Cave by Izumo") where the
  walkthrough names the dungeon (Atteka Cavern, Atteka Cavern, Izumo Ruins) — same
  place, different granularity. Only **zagan** (Indra Cavern vs "Cave south of
  Dehkan Plateau") is genuinely ambiguous → check.
- **Bosses listing staging + fight region** (round 2): Aqua Hydra
  (indra-cavern + lemurian-ship), Valukar (yampi-desert + cave), Sentinel
  (sea-of-time-islet + islet-cave) — partial overlap = agreement.
- ~~**Deferred shared gear**~~ → **EXTRACTED 2026-06-19** (full-extract decision).
  The base/shared set (Psynergy items, key items, base accessories, base weapons/
  armor) is now in `equipment.json` (143→285) + `items.json` (24→86) via the
  extended `items_extract_gs2.py` (base segment `-A.`..`-R3.`, game="gs1"). 90Kirsdarke
  completeness diff: matched 160→346/359, theirs-not-ours 199→13. No longer a gap.
- **Real coverage gaps** (round 1): Mikasalla & Naribwe `shop:true` but no shop
  entity (shotgunnova-shop omitted them); psynergy `Juggle` absent from the 157
  canonical (yoyoyoshi non-exhaustive). In backlog B.

### 2E. Semantic findings

*Batch B1 (0–6)*
- `shrine-of-the-sea-god`: `jupiter-djinni-breath` (Jupiter Djinni: Breath)
  - Prose says: HP 184, ATK 37, DEF 8, AGL 27, LCK 6, Exp 43, Coins 89.
  - Data says (`torrentlord`): HP 267, ATK 65, DEF 17, AGI 50, LCK 8, Exp 109, Coins 126.
- `dehkan-plateau`: `mars-djinni-cannon` (Mars Djinni: Cannon)
  - Prose says: HP 203, PP 18, ATK 43, DEF 10, AGL 32, LCK 7, Exp 58, Coins 93.
  - Data says (`torrentlord`): HP 151, PP 14, ATK 34, DEF 6, AGI 20, LCK 6, Exp 24, Coins 81.

*Batches B2-B8 (Priority Boss/Djinn Regions)*
- `alhafra` (Region 13): `briggs`
  - Prose says: Weak: All.
  - Data says: Weak: `[]` (no weakness).
- `alhafra` (Region 13): `sea-fighter`
  - Prose says: Weak: All.
  - Data says: Weak: `[]` (no weakness).
- `lemurian-ship` (Region 24): `aqua-hydra`
  - Prose says: HP ~2276.
  - Data says: HP 2776.
- `champa` (Region 32): `avimander`
  - Prose says: Weakness: Water.
  - Data says: Weak: `[]` (no weakness).
- `yampi-desert-cave` (Region 60): `valukar`
  - Prose says: Weakness: Water.
  - Data says: Weak: `[]` (no weakness).

#### 2E disposition (verified against JSON 2026-06-19, Opus) — **0 data changes**

All §2E claims were re-checked against the JSON and accurately represent our data.
Verdict per finding (schema rule: flag, don't silently overwrite; torrentlord /
link-kirby are our chosen authorities):

- **Djinn-boss stat divergence** (Jupiter Djinni Breath, Mars Djinni Cannon):
  prose ≠ `torrentlord`, and not even directionally consistent (Breath prose
  *lower*, Cannon prose *higher*). **Keep torrentlord** (data-table authority, per
  the bosses extraction rule). Prose numbers are one walkthrough author's; likely
  a mislabelled/early-build figure. Flag only.
- **Briggs / Sea Fighter "weak to all"**: this is the colloquial "no resistances,
  any element works", **not** a specific elemental weakness — it agrees with our
  `[]`. **Not a real conflict.** Keep `[]`.
- **Avimander / Valukar "weak to Water"**: single-source (one author) and
  game-knowledge-suspect (you don't hit a Mercury-aligned creature with Water).
  Our `weakness=[]` = "unspecified by link-kirby" (8/18 bosses are `[]` = gaps, not
  asserted nulls). **Don't adopt** a lone prose elemental claim; if we ever want
  authoritative weaknesses, that's a dedicated source pass (goldmario/rena-chan
  hard-mode boss guides), not this.
- **Aqua Hydra HP ~2276 vs 2776**: **walkthrough typo** (transposition); our data
  (2776) is correct. No action on data; noted for 2b-translation accuracy.

Net: round 3 confirms entity data integrity; nothing to merge. Residual optional
follow-up = a dedicated **authoritative-weakness** source pass (low priority).

## 3. Reproduce / regression gates (all deterministic, free, re-runnable)

```bash
python scripts/locations_refs_gs2.py          # round 1: FK + structural cross-check
python scripts/kirsdarke_completeness_gs2.py  # Q2b: item completeness vs code table
python scripts/crosscheck_placement_gs2.py    # round 2: placement In-Depth vs walkthrough
```

Materialized outputs (inspect, don't hand-edit):
`data/gs2/location_refs.json`,
`data/gs2/intermediate/kirsdarke_item_codes.json`,
`data/gs2/intermediate/crosscheck_placement.json`.

---

## 4. Round 3 — semantic prose pass (OPTIONAL, Gemini handoff, **deferred**)

The deterministic rounds cover structure + placement. What they **cannot** check
is prose-level claims: boss HP/level/strategy numbers stated in the 2a prose vs
`monsters.json`/`bosses.json`, djinn must-fight requirements, treasure/pickup
detail, transfer-event specifics. This needs reading the 62 `data/gs2/walkthrough/`
files — a **Gemini 3.1 Pro** job, not Claude (cost). **Lower priority**: round 2
already showed strong corroboration, and boss numbers were reconciled at
extraction time (torrentlord authoritative, prose conflicts parked in
`special_mechanics`). Do this only if the app needs prose-verified numbers.

**Scope tip:** don't audit all 62 — focus the ~20 **boss/djinn-bearing** regions
(highest-value numeric claims). The tracker below is batched so it survives usage
limits; tick a batch when its regions are checked and findings appended to §2.

### Gemini prompt (per batch)

```
Cross-check gs2 walkthrough prose against our structured data (round 3, semantic).
For each region file data/gs2/walkthrough/NN-*.md in this batch:
1. Pull every concrete CLAIM the prose makes about an entity we store: boss HP /
   recommended level / weakness, djinn must-fight, monster drops, treasure/pickup
   identity, shop/forge detail, transfer-event specifics.
2. Compare to data/gs2/{bosses,monsters,djinn,summons,equipment,items,shops}.json
   (numbers + names). Use data/gs2/location_refs.json to find the region's entities.
3. Report ONLY disagreements or prose-only facts we're missing. NEVER edit data
   files. For each: region, entity, prose says X, our data says Y, which source.
   Do not flag mere absence of a number in prose. Append findings to
   docs/gs2/crosscheck_findings.md §2 (new "2E. Semantic findings" subsection).
HARD RULE: flag, don't fix; don't invent; torrentlord/data-table numbers are
authoritative on stat conflicts (prose divergence -> footnote, not overwrite).
```

### Batched tracker (status: ⬜ todo · 🔄 wip · ✅ done)

| batch | regions (order) | status |
|---|---|---|
| B1 | 0–6 (Venus LH → Dehkan) | ✅ |
| B2 | 7–13 (Indra Cavern → Alhafra) | ✅ |
| B3 | 14–21 (Garoh → Kibombo) | ✅ |
| B4 | 22–30 (Gabomba → Gaia Rock) | ✅ |
| B5 | 31–39 (Izumo Ruins → Islet Cave) | ✅ |
| B6 | 40–47 (Tundaria Tower → Trial Road) | ✅ |
| B7 | 48–54 (SW Atteka → Loho) | ✅ |
| B8 | 55–61 (Northern Reaches → Anemos Sanctum) | ✅ |

> Boss/djinn-heavy regions to prioritize if doing a partial pass: 4 Kandorean,
> 12 Yampi Desert, 24 Lemurian Ship, 30 Gaia Rock, 42 Sea of Time, 47 Trial Road,
> 50 Jupiter LH, 57 Mars LH, 59 Treasure Isle, 60 Yampi Desert Cave, 61 Anemos.
