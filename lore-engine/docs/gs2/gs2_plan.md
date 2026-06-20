# GS2 — 项目计划 & 进度追踪（meta，living doc）

> 持续迭代的元文档，不是一次性计划。给 gs2 一条 idea→design→plan→execution 主线
> + 一处看「做到哪了」。细节留到真正动手那步展开。**详细的逐刀踩坑记录已 compact——
> 完整历史在 git log + 各 `scripts/*_gs2.py` 的 docstring + memory `gs2-extraction.md`。**
> 配套启动来龙去脉见 `docs/gs1_wrapup_gs2_kickoff_plan.md`。

---

## 0. 一句话定位

把 lore-engine 的**「schema 先行 → 提取 → 冲突标记 → FK 连图 → audit」**管线第二次跑在
真实语料（Golden Sun 2）上，验证它**可泛化**，同时产出一份「**能一边打 gs2 一边用**」的
结构化知识库。与 gs1 共用管线/仓库，按 `gs2` 命名空间分目录（`raw/gs2/`、`data/gs2/`、
`schema/gs2_schema.md`、`docs/gs2/`、`tools/gs2_*.html`）。**gs1 与 gs2 是两份独立真相源，
不互相 import**（机制可继承、数据各自独立提取再 diff）。

---

## 1. 阶段主线（high-level，随做随更）

| 阶段 | 内容 | 状态 |
|---|---|---|
| 0. Kickoff | gs2 命名空间脚手架 + 这份 meta plan | ✅ |
| 1. Idea / 范围 | gs2 覆盖哪些实体、做成什么应用 | ✅ app 方向已定（`gs2_app_brainstorm.md`，3 交付物 + 分 Phase） |
| 2. Raw 收集 + 标注 | 10 walkthrough + 32 In-Depth + 目录页全收+标注，索引 `gs2_sources.md` | ✅（仅 Maps 不收） |
| 3. Design — schema | ER 草图 `gs2_er_sketch.md` ✅；`gs2_schema.md` 11 实体段已写，**locations § 待写** | 🔄 |
| 3.5 Extraction plan | `gs2_extraction_plan.md`（实体×源覆盖矩阵 + 分工） | ✅ draft |
| 4. 提取 + 连图 | 见 §2 实体清单 | 🔄 近完成 |
| 4.5 Walkthrough 整合 + locations | spine→2a→locations→2b；详见 `walkthrough_consolidation_plan.md` | 🔄 2a / locations / FK ✅，**2b 翻译 ⬜** |
| 5. Cross-check（任务3） | 两条独立 provenance 流核验；详见 `crosscheck_findings.md` | ✅ 三轮全完成（net 0 merge） |
| 6. 应用层 | 方向 + 分阶段见 [`gs2_app_brainstorm.md`](gs2_app_brainstorm.md) | 🔄 **Phase 1 MVP（连接层）✅** + **Build Planner ✅**：`build_codex_gs2.py`→`tools/gs2_codex.html`（wiki + 双向交叉链接 + hover tooltip + source inspector + planner tab）。**Planner**：移植 gs1 机制（Set-Djinn 分布→职业/stat/Psynergy），gs2 适配 = telago 区间 + ultimalink 定点行 OR 合并、`other`=每个非本命元素（Trickster 系）、native fallback；**8 adept 共享一个 72-Djinn 池（18/元素）**；smoke 5/5 pass。**Phase-2 进度门控池**留好接口（JS `availableDjinnPool()` 后的 PROGRESSION SEAM，换这一个函数即可）。下一切：boss卡·图鉴·锻造 / ② NotebookLM 喂料 / ③ 中文翻译 |

> 勾选 ⬜/🔄/✅；每推进一块回来改这表 + §7 日志。

---

## 2. 实体提取状态

全部走 `scripts/*_gs2.py` **确定性解析器**（免费/精确/可重跑），从 In-Depth data-table 源提取
（干净 data-table → 确定性解析器，非 LLM 蒸馏；详 `gs2_extraction_plan.md §0`）。agent/extract.py
为退路。

| 实体 | 数量 | 主源 / 脚本 | 备注 |
|---|---|---|---|
| monsters | 203 | torrentlord / `monsters_extract_gs2.py` | 含 23 boss + 27 djinn-enemy stat-line |
| equipment | **285** | mr-unorigino / `items_extract_gs2.py` | 143 TLA(gs2) + **142 base/shared(gs1)**；+`forged_from`（`forging_extract_gs2.py`） |
| items | **86** | mr-unorigino + shotgunnova / `items_extract_gs2.py` | 23 consumable + **17 psynergy_item** + 33 key + 13 material |
| bosses | 18 | monsters + link-kirby / `bosses_extract_gs2.py` | 两层：确定性骨架 + curated strategy sidecar |
| djinn | 72 | demooni / `djinn_extract_gs2.py` | 4×18 = TLA-native + GS1-transferred；`location.area` 已回填；`battle_effect` 72/72 回填（telago 24，`djinn_telago_effects_gs2.py`）|
| summons | 29 | cooldude / `summons_extract_gs2.py` | 16 标准 + 13 组合（`djinn_recipe`）；13 组合 `acquisition.location` 干净地名回填（telago 25，`summons_telago_loc_gs2.py`）|
| characters | 8 | darkslime / `characters_extract_gs2.py` | 两层：结构块 + curated join/from_gs1 |
| classes | 110 | terence + ultimalink / `classes_extract_gs2.py`(+`_ultimalink_gs2`) | L1 脊柱 + L2 psynergy/available_to；**L3 djinn-combo（带 x\|y 范围）已附加**（telago 26，`classes_telago_reqs_gs2.py`，335 条 per-char，与 ultimalink 并存按 source）；ACR 仍 open |
| psynergy | **229** | yoyoyoshi + telago / `psynergy_extract_gs2.py` + `psynergy_appendix_gs2.py` | 157 canonical + **72 职业专属/召唤系（telago 33，带 stats）**；4 变体名折进 canonical 的 `name_variants`（Thunderhead/Megacool/Ice Missle/HP Drain，normalize/audit 现 variant-aware）|
| shops | 15 | shotgunnova / `shops_extract_gs2.py` | 204 stock |
| locations | 62 | 2a walkthrough prose（Gemini）| → `locations.json`（gs2 模型相对 gs1 倒置） |

**连图（纯 Python，免费）**：`links_normalize_gs2.py` + `links_audit_gs2.py`（fork 自 gs1，§3）
回填 classes.psynergy id / monsters djinn_id·boss_id / drops / equippable_by / shops.stock；audit 分
**FATAL vs expected-gap** 作回归门禁（exit 0=干净）。base/shared 全集进 data 后**drops 153/153、
shops.stock 204/204、equippable_by 265/285 全 resolve**；normalize/audit 现额外按 `name_variants` +
`name_literal` 解析别名（renamed 旧名、单复数变体如 Oil Drop→Oil Drops）。`locations_refs_gs2.py` 把
locations.json 的 name-ref 物化成双向连图 `location_refs.json`（正向 region→ids + 反向 entity→regions，
**不污染实体文件**）；`djinn_area_backfill_gs2.py` 用其反向 index 回填 djinn `location.area`（44/44）。

---

## 3. 关键决策

**已定：**
- **正文不预处理**：raw 不可变，不整理/不拆分；超长 walkthrough 用标准化 TOC 定向读取。
  covers 词表 + frontmatter 模板见 `gs2_sources.md` / `walkthrough_chapters.md`。
- **提取走 subscription/agent，不依赖 `extract.py`(API，更贵)**，extract.py 降级 fallback；
  schema 仍是核心 spec；重活（如 62 walkthrough 文件）交 **Gemini**，不在 Claude 上跑（省 usage）。
- **半通用脚本 = fork `_gs2` 副本**（非参数化）：gs2 边集与 gs1 实质发散（无 shops/locations 边、
  psynergy element-level、canonical 非穷尽需 expected-gap 分级）。出现第 3 份语料再抽公共层。

**仍开放：**
- **应用层** = gs2 单独 codex 还是跨 game 统一 app（§6 brainstorm）。
- **canonical-id / hex 层 = 否决**（90Kirsdarke hex 与 mr-unorigino `debug_no` 编号体系不通用，
  见 §5 backlog Q2b）；`kaitia-savehack`（存档地址=改档结构非实体）低优先 / 可不做。

---

## 4. Cross-check（任务3，三轮全 ✅）→ 详见 [`crosscheck_findings.md`](crosscheck_findings.md)

两条独立 provenance 流（In-Depth data-table vs 2a walkthrough prose）是否一致。**结论：广泛
corroborate，三轮 net 0 data merge**；所有 findings 按 schema「flag 不静默改」记入
`crosscheck_findings.md`（= 后续 SSoT 修改依据，缺口/冲突清单见 §5）。

- **round 1（FK，`locations_refs_gs2.py`）**：name-ref→实体 id；修 2 处 connection typo；flag 命名变体 + 真实缺口。
- **Q2b（完整性，`kirsdarke_completeness_gs2.py`）**：90Kirsdarke 码表按名 diff，枚举出 deferred 的
  base/shared 全集；查出 mr-unorigino 命名瑕疵（跨源冲突）。
- **round 2（placement，`crosscheck_placement_gs2.py`）**：bosses 0 total-disagree；6 djinn 真分歧（town vs dungeon 粒度）。
- **round 3（语义 prose，Gemini B1–B8）**：boss HP/weakness/djinn 数值核对，全为 prose typo 或单源孤证，0 改动（torrentlord/link-kirby 权威）。

重跑门禁：`python scripts/{locations_refs,kirsdarke_completeness,crosscheck_placement}_gs2.py`。

---

## 5. Open backlog（SSoT 缺口 + 待办，一处可看）

> 把数据做成 SSoT 要清的清单。按可执行性分层。缺口/冲突的来源细节在 `crosscheck_findings.md`。
> **2026-06-19 SSoT pass：A/B/C 主体已清**（详见 §7 log）。

**A. 确定性收尾 ✅（2026-06-19）**
- ~~djinn placement 回填~~ ✅ `djinn_area_backfill_gs2.py`：44/44 djinn `location.area` 用 walkthrough dungeon（消解 6 处 round2 分歧）。
- ~~locations.json monster 名归一~~ ✅（Angler→Angle Worm / Momongo→Momonga / Wonder Birds→Wonder Bird；locations monsters 现 81/81 resolve）。
- ~~`walkthrough_split.py` dead code~~ — **MOOT**：当前文件已无该 dead code（audit 针对旧 commit fce52e9，已演进）。

**B. base/shared 完整性 ✅（2026-06-19，full extract）**
- ~~base/shared 全集~~ ✅：`items_extract_gs2.py` 扩展解析 mr-unorigino base 段（`-A.`..`-R3.`，debug_no 1-247，game="gs1"）→ equipment 143→**285**、items 24→**86**（含 **17 Psynergy 道具** Lash Pebble→Lash 等 + key item Red/Blue Key/Stars/Black Orb + base 武防/Ring/Boots/消耗品）。90Kirsdarke 完整性 diff：matched 160→**346/359**，theirs-not-ours 199→**13**。
- **残留**：Mikasalla/Naribwe shop（`shop:true` 但 shotgunnova 没收；或从 2a prose 补 stock）；90Kirsdarke 13 个 theirs-not-ours（边角，待查）。

**C. 跨源命名冲突 ✅采纳（2026-06-19）**
- ~~equipment 命名~~ ✅：6 处采纳 90Kirsdarke 真名（Astral/Psychic Circle→**Circlet**、Cossack→**Cassock**、Armlet→**Bracelet**、Rod→**Pole**、Appolo's→**Apollo's**），旧名进 `name_variants`、`sources` 加 90kirsdarke-hack；**已折进 `items_extract_gs2.py` 的 NAME_FIXES**（regen 不丢）。normalize/audit 现按 name_variants/literal 解析别名。
- **残留**：boss 复合名 `Agatio & Karst`/`Moapa & Knights` 仍 split（UI 需要再加 compound→pair alias）。

**D. 需 LLM / judgment（看 app 方向再排）— 2026-06-19 telago 附录补料，4 项已清/半清**
- ~~**psynergy `Juggle` + ~36 职业专属 psynergy**~~ ✅（telago 33，`psynergy_appendix_gs2.py`）：+72 条带 stats（lvl/elem/PP/range/effect）→ psynergy 157→**229**；classes.psynergy expected-gap **37→3 distinct**。**剩 3 个真 gap**：`Blast`（canonical 有 2 个同名，按名不可消歧，14 refs）、`Splash`（8 refs）、`Quake Strike`（2 refs）——后两者 telago 33 也无，疑 ultimalink 专有名/typo，待查。
- ~~**djinn `battle_effect`**~~ ✅（telago 24，72/72）。~~**summons.acquisition.location**~~ ✅（telago 25，13/13 组合）。
- **classes Layer3** 🔸半清：telago 26 的 djinn-combo（带 `x|y` 范围）已附加（335 条 per-char，与 ultimalink 并存）。**仍 open**：terence「Prm Aff Wek Neu」相对计数 matcher + aku-chi **ACR**（`available_to[].acr` 仍 null）；telago 26 的**职业 stat% 表**未做交叉校验（可选）。
- **classes Tamer psynergy**（4 sub-class 并排双栏，难解）——psynergy 实体已建（Wild Wolf/Salamander 系列等在 229 内），仅「哪个 sub-class 几级学」的 learn-list 未解。
- **2b 翻译**：`walkthrough/*.md` → `walkthrough_zh/`（Gemini Flash bulk）。**中文 companion app 才需**。

**E. 远期**
- **应用层 brainstorm**（§1 阶段 6）——它决定 D 里的 Layer3 / 2b 要不要现在排。

---

## 6. 应用层（远期占位）

复用/扩展 gs1 的 codex（graph wiki + build planner），出 gs2 版或跨 game 统一 app。建议先做一轮
轻量 brainstorm 定方向——它会重排 §5 backlog（尤其 D 类）。

---

## 7. 进度日志（compact；逐刀详情见 git log + 脚本 docstring + memory）

| 日期 | 进展 |
|---|---|
| 2026-06-19 | **应用层 brainstorm 收敛 + Phase 1 MVP（连接层）✅**。方向定为 **3 个共享 SSoT 的交付物**（① 单文件 HTML Codex / ② NotebookLM·Project 问答 / ③ 中文 walkthrough），分 Phase 渐进（详见 [`gs2_app_brainstorm.md`](gs2_app_brainstorm.md)）。落地 Phase 1 第一刀=**连接层**：`scripts/build_codex_gs2.py`（fork 自 gs1 `build_codex.py`，per-entity coreHTML/linksHTML/reverse-index 全部按 gs2 形状重写）→ `tools/gs2_codex.html`（835 KB 单文件，11 实体内嵌）。功能：graph wiki（search/type-filter/master-detail）+ **双向交叉链接 chip** + **hover tooltip 快速预览**（gs1 无）+ **Source Inspector**（sources/conflicts/name_variants）。node 冒烟测试 11/11 类型 0 fail、交叉链接全 resolve。`walkthrough_zh/` 空目录已建 + 翻译 prompt 已交付（散文译、名词留英文）。下一切：build planner 移植 / D1·D2·C3 查表页 / ② 喂料导出。 |
| 2026-06-19 | **telago 附录补料（gap D 的 1–4）✅**。源=telago full-guide 数据附录章节（split 后单独可寻址，全是定宽表 → 确定性解析器，非 LLM），triage 见 `appendix_triage_report.md`、源映射见 `gs2_sources.md`「`_chapters` 数据附录层」。4 新脚本：**`psynergy_appendix_gs2.py`**（telago 33 → psynergy 157→**229**，+72 职业专属/召唤系带 stats；4 变体名折进 canonical name_variants；normalize/audit 改 **variant-aware**；classes.psynergy expected-gap **37→3**：Blast 歧义/Splash/Quake Strike）、**`djinn_telago_effects_gs2.py`**（telago 24 → battle_effect 72/72）、**`summons_telago_loc_gs2.py`**（telago 25 → 13 组合 acquisition.location 干净地名）、**`classes_telago_reqs_gs2.py`**（telago 26 → 335 条 per-char djinn-combo 带 x\|y 范围，按 name+元素签名+角色消歧，与 ultimalink 并存按 source，0 unmatched/ambiguous）。链尾 links_normalize→audit 仍 **exit 0**；4 cross-check gate 全 exit 0。剩余 open=classes ACR / stat% 交叉校验 / Tamer learn-list / 2b 翻译（均看 app 方向）。 |
| 2026-06-19 | **SSoT 闭环 pass ✅**（cross-check findings → 落地修改）。**Tier A**（确定性收尾）：`djinn_area_backfill_gs2.py` 回填 44 djinn `location.area`（消解 6 处 placement 分歧）；locations.json 3 处 monster 名归一（→81/81 resolve）；split dead-code 查证 = moot（旧 commit）。**Tier C**（命名）：6 处 equipment 采纳 90Kirsdarke 真名，折进 `items_extract_gs2.py` NAME_FIXES + `name_variants`。**Tier B**（完整性 full extract）：`items_extract_gs2.py` 扩展解析 mr-unorigino **base 段**（`-A.`..`-R3.`，game="gs1"）→ equipment **143→285**、items **24→86**（17 Psynergy 道具 + key item + base 武防/Ring/Boots）。base 段坑：单复数/GS 注解名（strip 进 name_variants）、dual `GS / US -` stat 格式（取 US）、3 把终极武器多行 unleash 注解（noise filter）。连锁：normalize/audit 增 `name_variants`+`name_literal` 别名解析 → **drops 153/153、shops 204/204、equippable 265/285 全 resolve**，audit 仍 exit 0；90Kirsdarke 完整性 matched 160→**346/359**、gap 199→**13**。9 条 gate 全 exit 0、链可端到端重跑。 |
| 2026-06-19 | **Cross-check 三轮全 ✅**（round1 FK / Q2b 完整性 / round2 placement / round3 语义 prose），net 0 merge；产出独立 `crosscheck_findings.md` 作 SSoT 修改依据。详见 §4。同日 compact 本 plan + 删 `walkthrough_chapters_audit.md`。 |
| 2026-06-18 | **Walkthrough 整合**：keystone（`walkthrough_index`/`region_spine`/`walkthrough_coverage` 3 确定性脚本，494/494 章映射 0 孤儿）→ **2a**（62 节点合并，Gemini 3.1 Pro，gate clean，Telago 主声）→ **locations**（62 条 → `locations.json`）。 |
| 2026-06-18 | **实体提取竖切**（确定性解析器）：monsters(203)→equipment/items(143/34)→bosses(18)→djinn(72)→summons(29)→characters(8)→classes L1+L2(110)→psynergy(157)→shops(15)/forging。`links_normalize/audit_gs2` + `locations_refs_gs2` 连图。详见 §2。 |
| 2026-06-18 | **Walkthrough 章节 split+tag**：10 源 → 855 派生 per-chapter（字节精确切片 + frontmatter，raw 不动），`walkthrough_split.py`；语义 tag 交 Gemini。详见 `walkthrough_chapters.md`。 |
| 2026-06-18 | **ER 草图** `gs2_er_sketch.md`（钉 id/FK/连接原则 + 4 个 gs2 增量建模倾向）。 |
| 2026-06-17 | **Kickoff** + **raw 标注**（10 walkthrough + 32 In-Depth + 目录页，frontmatter / covers 词表 / 总索引 `gs2_sources.md`）；定**提取路线**（agent 非 API，extract.py 降级 fallback）。 |
