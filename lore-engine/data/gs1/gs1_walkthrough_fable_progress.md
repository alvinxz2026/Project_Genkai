# Progress Tracker — gs1_walkthrough_fable.md

Goal: Distill a full Golden Sun 1 walkthrough from the four source FAQs in raw/gs1/:
- Guide and Walkthrough - Telago.txt (Iron Knuckle, v2.1 2023) — PRIMARY spine, walkthrough at lines 1424–4750
- Guide and Walkthrough - ElectroSpecter.txt — cross-reference, walkthrough section [wkth]
- Guide and Walkthrough - Ikillkenny.txt — cross-reference, walkthrough at lines ~1313–3400
- Guide and Walkthrough - BF_Gamer.txt — backup cross-reference, walkthrough sections 5.01–5.13

Output: data/gs1/gs1_walkthrough_fable.md (incremental appends, chapter by chapter)

## Chapter status

| # | Chapter | Telago lines | Status |
|---|---------|--------------|--------|
| 0 | Header + intro + how-to-use | — | DONE |
| 1 | Prologue: The Storm at Mt. Aleph | 1424–1521 | DONE |
| 2 | Sol Sanctum & the Elemental Stars | 1522–1709 | DONE (as "Chapter 1") |
| 3 | Vault & the Bandits | 1710–1865 | DONE (as "Chapter 2") |
| 4 | Bilibin, Kolima & the Cursed Forest | 1866–2108 | DONE (as "Chapter 3 / 3A") |
| 5 | Imil & Mercury Lighthouse | 2109–2391 | DONE (as "Chapter 4") |
| 6 | Fuchin Temple (Optional) | 2392–2486 | DONE (as "Chapter 5") |
| 7 | Mogall Forest | 2487–2573 | DONE (as "Chapter 6") |
| 8 | Xian, Alpine Crossing & Altin | 2574–2805 | DONE (as "Chapter 7") |
| 9 | Lama Temple, Lamakan Desert & Kalay | 2806–3024 | DONE (as "Chapter 8") |
| 10 | Optional Backtracking (Vale/Vault caves, Lunpa hoard, Bilibin cave) | 3025–3208 | DONE (as "Chapter 9") |
| 11 | Kalay to Tolbi | 3209–3424 | DONE (as "Chapter 10") |
| 12 | Tolbi, mini-games, Altmiller Cave & Babi | 3425–3736 | DONE (as "Chapter 11") |
| 13 | Colosso | 3737–3995 | DONE (as "Chapter 12") |
| 14 | Rescuing Master Hammet (Optional) | 3996–4134 | DONE (as "Chapter 13") |
| 15 | Suhalla Desert & Gate | 4135–4259 | DONE (as "Chapter 14") |
| 16 | Venus Lighthouse (Dead End) & Lalivero & Babi's Tower | 4260–4494 | DONE (as "Chapter 15") |
| 17 | Venus Lighthouse Revisited & Final Battle | 4495–4697 | DONE (as "Chapter 16") |
| 18 | Epilogue | 4698–4765 | DONE (as "Epilogue") |
| 19 | Crossbone Isle (Optional superdungeon) | Appendix C (7271–7650) | DONE (as "Chapter 17") |
| 20 | Final pass: ToC, Djinn quick-reference table, Battle Arena/linkage appendix | — | DONE |

## Status: COMPLETE (2026-06-10)

Final output: 1679 lines / ~17k words. Structure: How to Use → ToC → Djinn quick reference
(all 28) → Prologue → Chapters 1–16 → Epilogue → Chapter 17 (Crossbone Isle) → Appendix
(Battle Arena, Lost Age linkage). Per-chapter checklists for items/Djinn, boss callouts with
HP/weakness/strategy cross-checked between Telago and ElectroSpecter (plus BF_Gamer for the
Arctic Blade location and Ikillkenny for structure).

## Notes
- Do NOT touch data/gs1/gs1_walkthrough.md (reference only, not even needed).
- Style: clean markdown, per-chapter Items/Djinn/Boss callouts, no ASCII art.
- Djinn names/locations cross-checked against at least two sources when they appear.
