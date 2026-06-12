# Classes & Psynergy Extraction — Progress Tracker

Goal: design schemas for `classes` and `psynergy` in `schema/gs1_schema.md`,
then extract into `data/gs1/classes.json` and `data/gs1/psynergy.json`.

## Source files (raw/gs1/)

- [x] Class Change FAQ - plz2bstfu.txt (686 lines) — class lists per character, djinn reqs, lvl 29/30 spell lists w/ PP
- [x] Class Setup Guide - aku_chi.txt (827 lines) — stat multipliers (%), ACR ranks, djinn setups, strategy
- [x] Psynergy Guide - nintendos_own.txt (527 lines) — by Tetzcatlipoca; per-character psynergy w/ PP, range bars, djinn-trade keys
- [x] Psynergy List - _Jiggyhunter_.txt (209 lines) — attack psynergy by element, PP + target count
- [x] Psynergy Class FAQ - strawhat.txt (4411 lines) — PP, level learned, range, element, learned-by, class lists. MANY typos.

## Steps

- [x] Read all five sources
- [x] Design `classes` schema (append to gs1_schema.md)
- [x] Design `psynergy` schema (append to gs1_schema.md)
- [x] Self-review schemas; fixed: class_line now uses ids (was colliding display names); range "all" extended to all-enemy non-damaging effects (Break)
- [x] Extract psynergy → data/gs1/psynergy.json — DONE: 141 entries (32 earth, 30 fire, 45 wind, 25 water, 9 utility), validated
- [x] Extract classes → data/gs1/classes.json — DONE: 76 entries (25 Isaac+shared, 14 Garet, 22 Ivan+Ivan/Mia-shared, 15 Mia+Jenna), validated
- [x] Schema correction during extraction: same-name classes on different characters have DIFFERENT psynergy (Swordsman, Seer, Pilgrim, Illusionist, Cavalier, Enchanter, Ascetic, Shaman, Druid, Diviner, Wanderer, Defender, Conjurer lines) → split with character suffix (swordsman-isaac / swordsman-garet). Disambiguation table rewritten.
- [x] Final validation — both files parse; psynergy ids unique (141); class ids unique (76); every class `psynergy[].name` resolves to a psynergy.json entry; every `class_line` resolves to a class id; enums (category/element/range/target) checked; series/tier consistency checked; temp fragment files deleted

## Status: COMPLETE (2026-06-11)

Final numbers:
- schema/gs1_schema.md → v1.1: +5 source IDs, +`classes` schema, +`psynergy` schema
- data/gs1/psynergy.json → 141 entries (32 earth, 30 fire, 45 wind, 25 water, 9 utility)
- data/gs1/classes.json → 76 entries; 15 with aku-chi stat multipliers, 18 ACR ratings;
  3 flagged unreachable in GS1 (slayer, chaos-lord, war-adept — 8-djinn classes)
- Conflicts flagged (not silently resolved): PP (Curse, Bind, Wild Growth, Grand Gaia,
  Ply, Thorn, Thunderstorm), range (Spire, Stone Spire, Typhoon, Fire Bomb, Hurricane),
  element (Dull), item names (Force, Carry), class name ((Earth) Shaman/Enchanter),
  djinn requirements (Medium-Mia, White Mage-Mia)

## Notes

- New source IDs to register: `plz2bstfu-class`, `aku-chi`, `tetzcatlipoca`, `jiggyhunter`, `strawhat`.
- Name collisions: Shaman (water/wind/earth-line), Ascetic, Cavalier, Enchanter, Seer → IDs need element qualifiers.
- Two distinct "Blast" psynergies: Nova series (7pp) vs Mad Blast series (5pp).
- strawhat known errors to flag, not fix silently: dup "Thunderbolt" (=Thunderstorm), dup "Clay Spire" (=Stone Spire), dup "Storm Ray" (=Destruct Ray), "Rockslide 30pp lv54" (=Avalanche), Mars 13-PP "Haunt" (corrupted Nova copy), Sleep/Bind descriptions say "Boost Resistance", Dull element "Mercury" + learned-by "Jupiter", "(Earth) Shaman" header for Ivan (= (Earth) Enchanter content), "Avanlanche", "Quire", "Berserket", "Asceti", "Shman", "SCribe", "Ice Missle", "High Impace", "Sonich Slash".
- PP conflicts spotted: Curse 6 vs 5, Bind 4 vs 7, Wild Growth 19 vs 15, Grand Gaia 32 vs 17, Ply 4 vs 3, Thorn 6 vs 4, Nettle 23 vs 11 (strawhat internal).
- Range conflicts: Spire 1 vs 3, Stone Spire 5 vs 3 vs 3, Typhoon 5 vs 3, Fire Bomb 3 vs 5, Hurricane 7 vs 5.
- Item-name conflicts: Orb of Force vs Force Gem; Carry Stone vs Carry Gem.
- Range mapping: 1/3/5/7 bars → integers; party-wide (9-bar / "whole party"/"party's") → "all".
- Expected counts: ~60 class entries (incl. Jenna's Flame User, 8-djinn classes Slayer/Chaos Lord/War Adept), ~110 psynergy entries.
