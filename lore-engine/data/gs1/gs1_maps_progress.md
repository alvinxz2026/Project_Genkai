# gs1_maps.md — Cleanup Progress Tracker

Tracks the conversion of `raw/gs1/maps.md` → `data/gs1/gs1_maps.md`.
Resume work by reading this file first. `raw/gs1/maps.md` must stay unmodified.

**Status: COMPLETE** — all 35 location entries / 41 maps done (2026-06-14).
The format conventions actually used are documented at the top of `gs1_maps.md`.

Last updated: 2026-06-14

---

## Unified template (per map entry)

```markdown
#### {Location} - {Source}

​```
{pure ASCII map only — side/below prose and item-table columns removed}
​```

**Enemies:** A, B, C            ← only if the source has a clean enemy list
**Items:**
| # | Item |
|---|------|
| 01 | ... |
**Legend:** `$` = Chest · `O` = Log    ← only if the map uses symbol markers
```

Rules:
- Code block holds **only the map art**. Item tables, `[1 - X / 2 - Y]` brackets,
  `>>>Items<<<` / `>>>Legend<<<` / `ENEMIES` blocks → move into the info block below.
- **All walkthrough prose is deleted.**
- Preserve every map character verbatim (`¯ ¥ \ / ~ #`, borders). Use `scripts/map_slice.py`
  to extract exact column slices.
- Source label normalized in heading; add `- Shotgunnova` to Babi Lighthouse & Tunnel Ruin.
- Type A = Shotgunnova art+prose(+embedded table); B = art already has legend below;
  C = Crossbone structured `>>>...<<<`.

---

## Status

Status values: `todo` · `done` · `n/a` (empty placeholder, no map in source)

### World Map
| Location | Source | Type | Status |
|---|---|---|---|
| World Map | — | — | n/a |

### Towns & Villages
| Location | Source | Type | Status |
|---|---|---|---|
| Vale | Shotgunnova | A | done |
| Vale Cave | Shotgunnova | A | done |
| Vault | Shotgunnova | A | done |
| Bilibin | Shotgunnova | A | done |
| Kolima | Shotgunnova | A | done |
| Imil | Shotgunnova | A | done |
| Imil Ice Sliding | Shotgunnova | B | done |
| Xian | — | — | n/a |
| Altin | — | — | n/a |
| Kalay | Shotgunnova | A | done |
| Tolbi | Shotgunnova | A | done |
| Lunpa | Shotgunnova | A | done |
| Lalivero | Shotgunnova | A | done |

### Dungeons & Caves
| Location | Source | Type | Status |
|---|---|---|---|
| Sol Sanctum | Shotgunnova | A | done |
| Goma Cave | Shotgunnova | A | done |
| Kolima Forest / Tret Tree | Shotgunnova | A (multi: First Screen / Log / Tret Tree) | done |
| Bilibin Cave | Shotgunnova | A | done |
| Mercury Lighthouse | Shotgunnova | A | done |
| Fuchin Falls Cave | Shotgunnova | A | done |
| Mogall Forest | Shotgunnova | A | done |
| Altin Peak | Shotgunnova | A | done |
| Lama Temple | — | — | n/a |
| Lamakan Desert | Shotgunnova | A | done |
| Lamakan Desert (Hude Desert) | ElectroSpecter | B | done |
| Lamakan Desert (Hude Desert) | Telago | B | done |
| Altmiller Cave | Shotgunnova | A | done |
| Lunpa Fortress | Shotgunnova | A | done |
| Suhalla Desert | Shotgunnova | A | done |
| Suhalla Gate | — | — | n/a |
| Babi Lighthouse | Shotgunnova | A | done |
| Tunnel Ruin | Shotgunnova | A | done |
| Venus Lighthouse Part I | Shotgunnova | A | done |
| Venus Lighthouse Part II Upper | Shotgunnova | A | done |
| Crossbone Isle — Level 1 | BFGamer | C | done |
| Crossbone Isle — Level 2 | BFGamer | C | done |
| Crossbone Isle — Level 3 | BFGamer | C | done |
| Crossbone Isle — Level 4 | BFGamer | C | done |
| Crossbone Isle — Level 5 | BFGamer | C | done |
| Crossbone Isle — Level 6 | BFGamer | C | done |
| Crossbone Isle — Level 7 | BFGamer | C | done |
| Crossbone Isle — Level 8 | BFGamer | C | done |
| Crossbone Isle — Level 9 | BFGamer | C | done |
| Crossbone Isle — Ghost Ship | BFGamer | C (no map) | done |

### Other
| Location | Source | Type | Status |
|---|---|---|---|
| The Battle Arena | Telago | B | done |

---

## Helper scripts (kept for future map additions)

Both live in `lore-engine/scripts/` and read `raw/gs1/maps.md`. Output forced to UTF-8.

- `map_slice.py <start> <end> [colstart] [colend] [--rstrip] [--ltrim]`
  Print a line/column slice of the raw file. Use to lift a map at a known column cut.
- `map_extract.py <start> <end> [--table left|right] [--ltrim]`
  Auto-detect the `| NN | Item |` table by its modal column, blank only the table
  rectangle (keeps map content that wraps above/right of a corner table), and print
  the cleaned MAP plus the parsed ITEMS.

Caveats learned while using them:
- Leading-space differences between rows make hand-counted column cuts off-by-one — always
  eyeball the output and adjust the cut ±1–2.
- `map_extract` item parsing drops a row when a map digit (e.g. `|9|`, `|567|`) sits on the
  same line as a table row; cross-check the ITEMS list against the raw table.
- Maps where prose/labels share columns with the art (Vale, Mogall, Tunnel Ruin) need
  per-region cuts or manual cleanup, not a single column slice.

## Decisions & caveats

- **Walkthrough prose dropped entirely** (per request). `[REDUCTED]` markers were just
  truncated-prose markers and disappeared with the prose.
- **Enemies lists kept** as `**Enemies:**` (Crossbone / Fuchin / Mogall / Suhalla) — they are
  clean lists, not prose. Easy to drop later if undesired.
- **Vale**: source fused the village map with past/present narrative on the same lines; the
  map shown is the reconstructed **present-Vale** overview (prose stripped via a 3+-space rule).
- **Tunnel Ruin**: no item table in source; `Asura Armor` / `Oracle Robe` were transcribed
  from on-map room labels (`ASURA/ARMOR`, `ORACL/ROBE`) — verify against in-game names.
- **Empty stubs** (World Map, Xian, Altin, Lama Temple, Suhalla Gate, Ghost Ship) kept as
  `_(暂无 ASCII 地图)_` placeholders — source has no ASCII map for these.
- Multi-source locations (Lamakan Desert: Shotgunnova / ElectroSpecter / Telago) stacked as
  separate `#### ` subsections.
