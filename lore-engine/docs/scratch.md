# 下一组 Opening Prompt — gs2 提取：characters → classes → psynergy

> 复制下面这段作为新 session 的开场即可。

---

继续 lore-engine 的 **gs2（Golden Sun: The Lost Age）结构化提取**。先读
`lore-engine/docs/gs2/gs2_plan.md`（进度追踪，§2 阶段表 + §5 日志）、
`gs2_extraction_plan.md`（§1 实体×源覆盖矩阵）、`gs2_er_sketch.md`（id/FK 图）
和记忆 `gs2-extraction.md` 把上下文捡起来，然后我们做下一组实体。

**已完成 6 个实体**（都在 `data/gs2/`）：monsters(203) / equipment(143) /
items(24) / bosses(18) / djinn(72) / summons(29)。

**核心范式（沿用）**：
- 干净 data-table 源 → 写**确定性 Python 解析器**（`scripts/{entity}_extract_gs2.py`，
  镜像已有几个），**零 LLM / 零 extract.py API**，免费可重跑。
- 散文/judgment 部分 → curated sidecar 或 defer（见 bosses 的两层做法）。
- 单源够干净就单源；缺的字段留 null/[] 标 deferred，别杜撰。
- 守「gs1/gs2 两份独立真相源，不互相 import」——只从 gs2 源提取。
- `schema/gs2_schema.md` 是控制平面：每做一个实体，写它的 `## Schema:` 段 +
  在 Master Source IDs 表加源行。
- **每刀收尾**：更新 `gs2_plan.md`(§2 表 + §5 日志) + `gs2_extraction_plan.md`(§1 矩阵)
  + 记忆 `gs2-extraction.md`。commit 由我（用户）来发起，按「开分支→ff merge→push」，
  排除 `docs/scratch.md`。

**这一组要做的（按顺序，关联紧密）**：
1. **characters**（先做，维度表/被引用方）。主源 `ultimalink`（8 角色职业表覆盖
   Felix/Jenna/Sheba/Piers + 回归的 Isaac/Garet/Ivan/Mia）+ walkthrough 角色索引
   (darthmarth/darkslime)。ER 增量见 `gs2_er_sketch.md §4.1`：4→8 角色，`is_permanent`
   语义变化倾向换 `join`/`availability`。参考 gs1 `schema/gs1_schema.md` 的 characters 段。
2. **classes**。主源 `ultimalink`（per-角色职业链 stat% + djinn 数 + psynergy 等级表）
   + `terence`（职业需求/加成**权威源**，同 gs1）+ `aku-chi`（配装）。注意 gs1 的教训：
   职业匹配要靠 terence 的完整四元素 djinn_requirements（见记忆
   `lore-engine-data-extraction` 里 Build Planner 修复那条）。
3. **psynergy**。主源 `yoyoyoshi`（全列表+机制，较新）+ `mr-unorigino-psy`（completeness
   校验，注意日文乱码——参考 djinn/equipment 的乱码处理：丢弃乱码列）。

关联：classes 引用 characters(available_to) + psynergy；psynergy 引用 characters
(available_to)；这些 FK 存自然键(name)，最后由 gs2 版 links_normalize 回填。

**遗留 TODO（不在这一组、记着）**：建 gs2 版 `links_normalize`/`audit`（六+实体已就绪，
boss_id / djinn_id / drop ref / summons↔djinn 软连待回填）；补 gs1↔gs2 共享消耗品进 items；
boss strategy sidecar 并入 goldmario/rena-chan/ikillkenny；josher1212 补 TOC；hex master-data 层。

先从 **characters** 起。先 explore 源格式定确定性 vs LLM，再动手。
