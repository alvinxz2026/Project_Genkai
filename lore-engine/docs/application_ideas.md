# Lore-Engine GS1 — 应用层想法草稿（待讨论）

> 草稿，给明天讨论用。不是计划、不是承诺，是把可能性摊开。
> 现在 `data/gs1/` 已经是一份**结构化 + FK 连通 + 可校验**的知识库，可以在它上面搭"应用层"了。

---

## 我们手里到底有什么（决定了能做什么）

- **10 张实体表 + 1 张关系视图**：djinn(28) / summons(16) / classes(76) / psynergy(141) /
  equipment(141) / items(38) / shops(12) / monsters(137) / bosses(13) / locations(38) /
  characters(5)，外加 `location_refs.json`（地点反向索引）。
- **整张图已连起来**（id 外键）：
  - class ←→ psynergy（哪个职业给哪些法术，双向）
  - djinn 配置 → class（`classes.available_to[].djinn_requirements[].parsed{element,min,max}`，**已结构化**）
  - class → stat_multiplier（职业属性倍率）
  - shop / monster-drop → equipment / items（哪里买、哪个怪掉）
  - psynergy → 角色 / 授予道具；equipment → 可装角色
  - location → 该地点的一切（djinn/装备/怪/boss/商店/道具）
- **校验脚本**：`links_audit.py` 保证图永远自洽；`links_normalize.py` 改数据后重生成。

**一句话**：这不再是一堆静态表，而是一张**可双向查询的游戏知识图**。这正是下面这些应用的地基。

### 已知的数据洞
- ~~`summons` 的 `damage_power` / `effect` 全空~~ —— **已补**（2026-06-16，源 Terence `raw/gs1/Summon.md`）：
  伤害 = `damage_power`(Base Mod) + `damage_hp_mod`(Max HP Mod) × 目标 Max HP，仅随 tier(djinn_required) 变，
  另加 user-Power buff（effect）。目前无其它已知数据洞。

### 一条不变的原则（来自项目本身）
> **data 与 presentation 分离**。`data/gs1/` 是真相源，应用层只是它的"读视图"。
> 所以理想情况下，应用应该是**纯读 JSON 的展示层**，不把逻辑/数据塞回去。

---

## 应用想法（按"这套数据独有的价值"排序）

### ⭐ A. 职业 / 配队规划器（Build Planner / Class Calculator）— ✅ 已实现 MVP（2026-06-16）

> 产出：`tools/gs1_build_planner.html`（自包含静态页，内嵌 JSON，file:// 可用）；
> 生成脚本 `scripts/build_planner.py`（纯读 data/gs1，数据改了重跑即可）。
> 匹配模型：以 `plz2bstfu-class` 为权威单一模型（每职业是 djinn 分布空间里一块互斥区域：
> 本命元素数定基础线 tier，副元素数定混合线；未命名的副元素须为 0、本命未命名则不限）。
> 覆盖四名常驻 Adept 全部 GS1-reachable 职业（Ivan 的 White Mage 唯一回退 strawhat，确定且与 aku-chi 一致）；
> 8-djinn 职业 reachable_in_gs1=false 已排除。正向（djinn→职业+stat_multiplier+psynergy）+
> 反向（下拉选目标职业→回填所需 djinn）。边界处少量真实重叠（如 Garet savage 4-5 / barbarian 5-7 earth
> 在源数据里共享 earth=5）按"最具体优先"选主、其余列为 also valid。
> **副产物修了一个真 bug**：`links_normalize.py` 的 `parse_djinn_req` 缺 "Air"→wind 别名，
> 导致 Mia 的 Sage "1 Water, 6 Air" 漏解析成只剩 water1；已补别名、重跑 normalize→audit（0 err）、
> djinn_requirements parsed 215/216（剩 1 为 Jenna 固定职业备注，合理）。


**做什么**：输入四个角色身上各自的 Djinn 分布（按元素数量）→ 实时算出每人**当前职业** +
解锁的 **psynergy 列表** + **stat_multiplier**。反向也行："我想让 Ivan 当 X 职业，需要怎样的 Djinn 配置？"

**为什么是它**：这个应用**独一无二地吃到我们刚做的东西**——`djinn_requirements.parsed` 的
`{element,min,max}` 结构 + class→psynergy 的 FK + stat_multiplier。换别的数据集做不出来。
对真实玩家也**真有用**（Djinn 配队是 GS 的核心策略）。范围可控。

**靠哪些数据**：classes（available_to.parsed / psynergy / stat_multiplier）、djinn、characters。
**工作量**：MVP 小-中（纯前端读 JSON + 一点匹配逻辑）。

### ⭐ B. 自然语言问答（LLM over the Knowledge Base）— 最点题
**做什么**：用 Claude 把这份 JSON 当**结构化工具/检索后端**，回答自由问题：
"Ivan 配 3 火 Djinn 最佳职业是什么""Frost 在哪拿""哪些怪掉 Long Sword""Imil 有什么"。

**为什么**：直接呼应 lore-engine 的初衷——*把非结构化文本变成可查询知识库*。
而且现在数据干净、连通、id 化，正是 LLM 最容易准确检索的形态（tool use / 结构化 RAG，
比纯文本 RAG 准得多）。是最能"讲清楚我们为什么做这件事"的 demo。

**靠哪些数据**：全部（尤其 FK 图让多跳问题可答）+ Claude API（tool use / function calling）。
**工作量**：中（定义几个查询工具函数 + 接 Claude）。

### B'. 浏览器 / 交互式 Wiki（Graph-aware Explorer）— ✅ 已实现（2026-06-16，与 A 合并）

> 产出：统一 app `tools/gs1_codex.html`（自包含静态页，内嵌全 11 实体 + location_refs，543 KB，file:// 可用）；
> 生成器 `scripts/build_codex.py`（纯读 data/gs1，改数据重跑）。两个 tab：**Wiki(B')** + **Build Planner(A)**。
> Wiki 把全部 FK 边建了正反双向反向索引（覆盖 schema "Cross-Entity Links" 全表 + location_refs 反演），
> 任意实体详情把出/入向链接列成可点 chip，可顺图遍历；location 直接当中枢读 location_refs。
> 反向索引计数与 `links_audit.py` 完全吻合（class.psynergy 1026 / shop.stock 202 / monster.drops 121 / acquired_via_item 8）。
> Planner 的职业/psynergy 名可点跳进 Wiki——B' 与 A 真正"做到一起"。
> **统一 app 取代**原 3 个工具（`gs1_class_explorer.html` / `gs1_equipment_explorer.html` / `gs1_build_planner.html` +
> `build_planner.py`）——旧文件保留待确认后删。**E（图谱可视化）本轮未做**，但 Wiki 的反向索引层即 E 的数据底座。

**原始设想**：扩展现有 `tools/*.html`，做成点一个实体就能顺着 FK 跳的浏览器——
点 class 看它的 psynergy、点 psynergy 看哪些 class 给它、点 location 看这里的一切。最低门槛把"连图"价值可视化。

### C. 攻略路线伴侣（Route / Checklist Companion）
**做什么**：按 location + chapter 顺序，列出每个地点的 Djinn / 道具 / 装备 / boss
（用 location_refs + chapter_first_seen），做成可勾选清单；按章节做**剧透分级**。
**为什么**：把 locations(D 阶段) + 反向索引直接变成玩家用得上的"通关不漏拿"工具。
**靠**：locations / location_refs / bosses。**工作量**：小-中。

### D. Boss 备战顾问
**做什么**：给定章节/队伍，按 boss 的 weakness + 你能拿到的 equipment/psynergy，推荐打法。
**为什么**：组合 bosses.weakness + equipment.elemental_power + 当前可达资源。
**靠**：bosses / equipment / psynergy / locations（章节门控）。**工作量**：中（要点策略逻辑）。

### E. 图谱可视化（Knowledge Graph Viz）
**做什么**：把实体图渲染出来（locations 当 hub，class↔psynergy 网络等），可交互探索。
**为什么**：好看、直观体现"连图"成果；偏 demo/展示价值。**工作量**：中。

### F. 管线泛化（元目标，不止 GS1）
**做什么**：把"schema 先行 → 提取 → 冲突标记 → FK 连图 → audit"这套**复用到 GS2 / 或非游戏域**
（如工作 SOP），证明 lore-engine 是个**可泛化的管线**而不是一次性脚本集。
**为什么**：这才是项目的终极价值主张。但偏"平台/方法论"，不是面向用户的 app。
**工作量**：大（取决于新域）。

---

## 一张对比表

| 想法 | 独特性(吃到连图?) | 对用户价值 | 工作量 | 性质 |
|---|---|---|---|---|
| A 配队规划器 | 极高（parsed 需求专属）| 高（玩家核心策略）| 小-中 | 工具 |
| B NL 问答 | 高（多跳检索）| 高 | 中 | demo+工具，最点题 |
| B' 浏览器 | 中 | 中 | 小-中 | 底座 |
| C 路线伴侣 | 中-高 | 中-高 | 小-中 | 工具 |
| D Boss 顾问 | 中 | 中 | 中 | 工具 |
| E 图谱可视化 | 中 | 低-中 | 中 | 展示 |
| F 管线泛化 | —（元层）| —（对开发者）| 大 | 平台 |

---

## 我的倾向（供拍砖）

- **想要"最能体现这套数据/项目价值"的一个东西** → 选 **B（NL 问答）**：它把"非结构化→可查询知识库 + 给 LLM 用"的论点直接演示出来。
- **想要"对玩家最实在、范围最可控、且独占我们刚做的 parsed 结构"** → 选 **A（配队规划器）**。
- **最省事的起步/底座** → **B'（浏览器）**，顺便给 A/B 当调试视图。

可以考虑：先做 **B'** 当地基（半天到一天），再叠 **A** 或 **B**。

---

## 待你拍板的开放问题（明天讨论）

1. **受众**：给玩家用的工具？给 LLM 用的知识后端 demo？还是给开发者看的"管线泛化"证明？
2. **技术栈**：纯静态前端（直接读 JSON，零后端，好部署）vs 带后端 / 接 Claude API（B/D 需要）？
3. **要不要先补 summons 伤害洞**？（只有做"输出/伤害"类功能才卡这个。）
4. **只服务 GS1**，还是从一开始就为 GS2 / 泛化预留接口？
5. 有没有你自己更想做、上面没列到的方向？
