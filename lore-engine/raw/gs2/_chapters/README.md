# `_chapters/` — derived walkthrough chapters (NOT source)

This tree is **generated**, not authored. Each `<source_id>/NN-<slug>.md` is a
**byte-exact slice** of the matching `raw/gs2/Guide and Walkthrough/*.md`, with a
YAML frontmatter header prepended (the body is copied verbatim, never edited).
The `source_lines` field is the exact 1-based line range back into the original.

- The real, immutable sources are in `raw/gs2/Guide and Walkthrough/`. Edit those
  never; regenerate these instead.
- Generator: `scripts/walkthrough_split.py --source <id> --verify` (deterministic,
  no LLM; `--verify` asserts byte-exact reconstruction).
- Full pipeline, frontmatter spec, tagging prompt, model choices, and progress
  tracker: [`docs/gs2/walkthrough_chapters.md`](../../../docs/gs2/walkthrough_chapters.md).

The `_` prefix marks this as a derived layer so it doesn't get mistaken for raw.
