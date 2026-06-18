这个文档是用来Draft Prompt用的，不是工作区。


---

给 Antigravity 的 prompt（带 /goal）
模型设 Gemini 3.5 Flash (High)。/goal 设一次，然后每个源贴一遍 per-source prompt（换 <id>）。两段都存进 docs/gs2/walkthrough_chapters.md 了。

① /goal（开一次）


/goal Run the gs2 walkthrough chapter pipeline in the lore-engine repo: for each
Guide-and-Walkthrough source, deterministically split it into per-chapter files
under raw/gs2/_chapters/<id>/ and tag each chapter's semantic frontmatter
(kind/covers/region). Follow docs/gs2/walkthrough_chapters.md exactly. HARD RULES:
never edit the raw sources under "raw/gs2/Guide and Walkthrough/" (immutable);
chapter bodies are byte-exact slices — never reword/reformat them; split ONLY via
scripts/walkthrough_split.py (deterministic), never by hand; every split must print
"verify: byte-exact reconstruction OK"; tagging sets only kind/covers/region and
nothing else; do not invent data.
② 每个源跑一轮（换 <id>）


Do source_id = <id> through both stages (read docs/gs2/walkthrough_chapters.md
and the finished raw/gs2/_chapters/cloud-blazer/ first to match the pattern).

STAGE 1 — split (deterministic; no LLM):
- Run: python scripts/walkthrough_split.py --source <id> --verify
- It MUST print "verify: byte-exact reconstruction OK".
- For each "!! entries NOT located": open the raw file in
  "raw/gs2/Guide and Walkthrough/", find the header the author actually used, and
  add an override in scripts/walkthrough_split.py:
  ALIASES["<id>"]["<toc_path>"] = ("<enum>", "<title>")   # add a 3rd "<CODE>" for a [CODE] guide
  then re-run. "container" info lines are fine — ignore. If a section is truly
  absent (unfinished guide), leave it and note it in the tracker.
- Once you start Stage 2, do NOT re-run split (it deletes+rewrites the files and
  wipes tags); use --dry-run to re-verify.

STAGE 2 — tag (your judgment):
- For each file in raw/gs2/_chapters/<id>/, set kind / covers / region IN PLACE
  per the vocab in the runbook. Touch ONLY those three keys — never the body or the
  mechanical fields (source_id/parent/chapter_no/toc_path/title/source_lines). Don't
  reformat anything. Judge from what's actually in the body; don't invent coverage.

FINALLY: update the progress-tracker row for <id> in
docs/gs2/walkthrough_chapters.md, and print one line per chapter: file / kind /
covers / region.

---

/goal Run the gs2 walkthrough chapter pipeline in the lore-engine repo: for each
Guide-and-Walkthrough source, deterministically split it into per-chapter files
under raw/gs2/_chapters/<id>/ and tag each chapter's semantic frontmatter
(kind/covers/region). Follow docs/gs2/walkthrough_chapters.md exactly. HARD RULES:
never edit the raw sources under "raw/gs2/Guide and Walkthrough/" (immutable);
chapter bodies are byte-exact slices — never reword/reformat them; split ONLY via
scripts/walkthrough_split.py (deterministic), never by hand; every split must print
"verify: byte-exact reconstruction OK"; tagging sets only kind/covers/region and
nothing else; do not invent data.

Do source_id = <id> through both stages (read docs/gs2/walkthrough_chapters.md
and the finished raw/gs2/_chapters/cloud-blazer/ first to match the pattern).

STAGE 1 — split (deterministic; no LLM):
- Run: python scripts/walkthrough_split.py --source <id> --verify
- It MUST print "verify: byte-exact reconstruction OK".
- For each "!! entries NOT located": open the raw file in
  "raw/gs2/Guide and Walkthrough/", find the header the author actually used, and
  add an override in scripts/walkthrough_split.py:
  ALIASES["<id>"]["<toc_path>"] = ("<enum>", "<title>")   # add a 3rd "<CODE>" for a [CODE] guide
  then re-run. "container" info lines are fine — ignore. If a section is truly
  absent (unfinished guide), leave it and note it in the tracker.
- Once you start Stage 2, do NOT re-run split (it deletes+rewrites the files and
  wipes tags); use --dry-run to re-verify.

STAGE 2 — tag (your judgment):
- For each file in raw/gs2/_chapters/<id>/, set kind / covers / region IN PLACE
  per the vocab in the runbook. Touch ONLY those three keys — never the body or the
  mechanical fields (source_id/parent/chapter_no/toc_path/title/source_lines). Don't
  reformat anything. Judge from what's actually in the body; don't invent coverage.

FINALLY: update the progress-tracker row for <id> in
docs/gs2/walkthrough_chapters.md, and print one line per chapter: file / kind /
covers / region.