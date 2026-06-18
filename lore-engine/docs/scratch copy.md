这个文档是用来Draft Prompt用的，不是工作区。

---

RE-TAG pass for the gs2 walkthrough chapters. The chapter files are already split
and body-verified — DO NOT run the splitter, DO NOT touch any body or mechanical
frontmatter field. You are ONLY rewriting the three semantic keys (kind, covers,
region) of every chapter, applying a tightened spec that fixes a prior inconsistent
tagging pass.

First read the "Stage 2 — tag" section of docs/gs2/walkthrough_chapters.md and
follow its kind rules, the covers threshold (EXTRACTABLE-DATA, not mention), and the
HARD RULES exactly.

Then, for source_id = telago, for every file in raw/gs2/_chapters/telago/, OVERWRITE
kind/covers/region per that spec. In particular fix these recurring first-pass errors:
- 00-front and all meta/story chapters -> kind correct + covers: [] + region blank.
- boss-fight strategy written as prose -> kind: prose-walkthrough (NOT data-table).
- a pure index/list chapter (e.g. a Djinn List) -> covers is ONLY that one entity,
  not every entity named in a column.
- walkthrough area chapters -> covers only entities with real content here; drop
  entities merely mentioned as a tactic.
- 1-3 line section-header-only chapters -> kind: meta, covers: [].

Touch nothing but those 3 keys. Print one line per file: file / kind / covers /
region. Then set this source's `tagged` cell to ✅ in docs/gs2/walkthrough_chapters.md.