# Golden Sun 2 — NotebookLM 投喂包

本目录由 `scripts/export_notebooklm_gs2.py` 从 SSoT JSON 渲染而成。
全部是 **prose markdown**（每个实体一个 `## 名称` 段落），专为 NotebookLM 的
分块检索优化——直接丢 JSON 会被切坏，这里不会。

## 丢哪些进 NotebookLM

把下面这些文件作为 source 上传（**不要**再额外丢 `data/gs2/*.json` 原始文件，
否则会把已裁决的 conflict 又请回来）：

- `characters.md` — 8 条
- `djinn.md` — 72 条
- `summons.md` — 29 条
- `psynergy.md` — 229 条
- `classes.md` — 110 条
- `equipment.md` — 285 条
- `items.md` — 86 条
- `monsters.md` — 180 条
- `bosses.md` — 18 条
- `locations.md` — 62 条
- `shops.md` — 15 条
- `walkthrough_en.md` — 62 章英文流程（合并）
- `walkthrough_zh.md` — 62 章中文流程（合并）

共 13 个 source，远低于 NotebookLM 的 50 source 上限。

## 可选：也丢 raw 原始攻略

若想要原汁原味的叙述细节，可再把 `raw/gs2/` 里的 prose 攻略一并丢进去。
但注意 raw 是多源、未裁决的，回答可能出现 SSoT 已解决的矛盾。
**图准 → 只用本目录；图全 → 本目录 + raw（择一为主，别混着当权威）。**
