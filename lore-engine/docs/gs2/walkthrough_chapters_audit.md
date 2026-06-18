# Walkthrough Chapters Audit Report

**Date:** 2026-06-18
**Auditor Model:** Gemini 3.1 Pro (High)
**Commit Hash:** fce52e9
**Overall Verdict:** FAIL (due to pervasive tagging inconsistencies and overclaims)

## Summary Table

| Source | Chapters | Verify OK | Body Integrity | Tagging Verdict | # Findings |
|---|---|---|---|---|---|
| autocon | 325 | ✅ | ✅ | FAIL | 3 |
| cloud-blazer | 95 | ✅ | ✅ | PASS-WITH-NOTES | 1 |
| darkslime | 42 | ✅ | ✅ | PASS-WITH-NOTES | 2 |
| darthmarth | 39 | ✅ | ✅ | PASS-WITH-NOTES | 2 |
| ikillkenny | 88 | ✅ | ✅ | FAIL | 3 |
| killerfusion | 83 | ✅ | ✅ | FAIL | 3 |
| shotgunnova | 69 | ✅ | ✅ | FAIL | 2 |
| strawhat | 54 | ✅ | ✅ | FAIL | 3 |
| super-slash | 20 | ✅ | ✅ | FAIL | 2 |
| telago | 40 | ✅ | ✅ | FAIL | 2 |

## Critical Issues

*   **Raw Immutability:** PASS. `git status --short` confirms no files in `raw/gs2/Guide and Walkthrough/` were modified.
*   **Body Integrity:** PASS. A strict byte-exact assertion script verified all 855 chapter bodies equal the exact raw slice named by their `source_lines`. 0 body mismatches.

## Quality Findings

### Tagging Quality
The semantic frontmatter tagging (`kind`, `covers`, `region`) suffers from severe inconsistency across the 10 sources. The primary issue is a lack of a clear threshold for `covers`: some sources tag an entity only if there is extractable data, while others tag it if the entity is merely mentioned in passing. 

#### Source Details:
*   **autocon:** 
    *   *Over-tagging on Meta:* `00-front.md`, `309-transfer-questions.md`, and `323-thanks.md` have massive `covers` lists (e.g., `[bosses, characters, classes, djinn, equipment, ...]`) despite containing no extractable data.
    *   *Misclassified Section Headers:* Chapters like `02-prologue.md` are tagged as `prose-walkthrough` but only contain a 2-line section header. These should be `meta`.
*   **cloud-blazer & darkslime:**
    *   Generally accurate, but inconsistent with each other. Cloud-blazer under-tags `djinn` and `psynergy` in walkthroughs where they are obtained (e.g., `16-kandorean-temple.md`), while darkslime uses extremely sparse covers (only `[locations, walkthrough]`) even when boss fights and items are described.
*   **darthmarth:**
    *   *Under-tagging:* Walkthroughs routinely miss `equipment` when discussing equippable gear pickups (e.g., `08-air-s-rock.md` misses `equipment` despite mentioning Storm Brand and Fujin Shield).
    *   *Multi-location regions:* Chapters cover multiple areas but only tag the primary one in `region`.
*   **ikillkenny & killerfusion:**
    *   *Kind Misclassification:* Boss strategy chapters (e.g., ikillkenny `85-doom-dragon.md`, killerfusion `59-king-scorpion.md`) are incorrectly tagged as `data-table`. They are primarily prose boss walkthroughs and should be `prose-walkthrough`.
    *   *Covers Overclaim:* These same boss chapters wildly overclaim covers like `summons`, `psynergy`, `equipment`, and `characters` simply because they are mentioned as tactics to use.
    *   *Killerfusion Index Overclaim:* `64-dijnn-list.md` tags `characters`, `equipment`, and `items` despite being a pure djinn list.
*   **shotgunnova & strawhat:**
    *   *Severe Covers Inflation:* Almost every chapter is over-tagged. Strawhat's `41-djinn.md` tags `[characters, classes, djinn, equipment, items, monsters, psynergy, summons, transfer]`. Shotgunnova's `61-djinn-list.md` does the same. This renders the `covers` field useless for filtering.
    *   Both sources also incorrectly populate the `covers` array on `00-front.md` chapters.
*   **super-slash:**
    *   *Severe Covers Underclaim:* The monolithic 5000-line `04-walkthrough.md` chapter omits `psynergy`, `characters`, `transfer`, and `summons` despite thoroughly covering the entire game. Reference tables like `11-character-classes.md` miss `psynergy` despite listing all class psynergies.

### Splitter Code Health
`scripts/walkthrough_split.py` correctly reconstructs all sources byte-for-byte, but has accreted a few code health issues:
1.  **Dead Code:** The `ENUM` regex variable at line 147 is unused (only `ENUM_RE` is used).
2.  **Duplicated Docstring:** Lines 20-21 are an exact duplicate ("Two expected mismatch classes are handled, not silently dropped:").
3.  **Source-Specific Branches:** There are 7 source-specific `if source_id == "..."` branches inside the parser logic. While they successfully handle parser weaknesses (e.g., shotgunnova's empty string codes, strawhat's bracketed enums), they contradict the "source-agnostic" design goal and could misfire if used on new texts.

### Tracker Accuracy
PASS. The progress tracker chapter counts match reality perfectly. For `autocon`, the 9 true misses (`2.8b Magma Rock` through `2.8j The End`) were investigated. They are genuinely absent from the raw file (the author stopped writing at 2.8a, leaving a "(coming soon)" note).

## Recommendations

1.  **[re-tag]** Establish a firm `covers` standard: does it mean "entity has structured/extractable data" or "entity is mentioned"? Apply this strictly across all 10 sources to fix the wild inconsistencies (shotgunnova/strawhat overclaims vs super-slash/darthmarth underclaims).
2.  **[re-tag]** Fix boss strategy chapters in `ikillkenny` and `killerfusion` (e.g., `85-doom-dragon.md`) which are currently tagged as `data-table`. They should be `prose-walkthrough`.
3.  **[re-tag]** Fix the `00-front.md` chapters in `autocon`, `strawhat`, `telago`, and `shotgunnova` which have massive `covers` lists. Frontmatter should be `covers: []`.
4.  **[re-tag]** Fix empty section headers in `autocon` (e.g., `02-prologue.md`) currently tagged as `prose-walkthrough`; they should be `meta`.
5.  **[deterministic-script fix]** Remove the dead code `ENUM` variable at line 147 of `scripts/walkthrough_split.py`.
6.  **[deterministic-script fix]** Remove the duplicated docstring on lines 20-21 in `scripts/walkthrough_split.py`.
7.  **[doc update]** Update the progress tracker in `docs/gs2/walkthrough_chapters.md` to note the 9 known gaps for `autocon` (sections 2.8b through 2.8j are unfinished).
