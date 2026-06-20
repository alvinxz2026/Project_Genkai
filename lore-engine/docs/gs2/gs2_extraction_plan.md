# GS2 — Extraction Plan（实体×源底料 + 缺口收尾轮）

> **状态：提取主体完成，进入数据缺口收尾。** 本文原是标注 32 篇 In-Depth + 10 篇
> walkthrough 时沉淀的「每个实体从哪些源提、谁主谁辅、用 Claude Code 还是 Gemini」底料。
> 11 实体已全部提取（§1 矩阵），telago 附录 + cross-check + SSoT 闭环已过。**现行动焦点 =
> §5「数据缺口收尾轮」**（2026-06-20，Tier1+Tier2）。配套：源清单见
> [`gs2_sources.md`](gs2_sources.md)，活跃主线/backlog 见 [`gs2_plan.md`](gs2_plan.md)（§5），
> 逐刀历史见 git log + 各 `scripts/*_gs2.py` docstring + memory `gs2-extraction.md`。

提取路线已定（见 `gs2_plan.md §4`）：**走 subscription/agent（Claude Code 和/或 Gemini），
不依赖 `extract.py`(API，更贵)**；`gs2_schema.md` 仍是核心 spec，下游 `links_normalize→audit→
build_codex` 是纯 Python、零 LLM 成本。沿用 gs1 巨型 walkthrough 的「子代理批量提取」先例。

---

## 0. 竖切验证结论（monsters，2026-06-17 完成）✅

第一刀切 `monsters`，已跑通并验证。**核心结论（直接影响后续所有实体）**：

> **对干净的 data-table 源，「中间层」= 确定性 Python 解析器，不是 LLM 蒸馏。**
> 既免费、又精确、又可重跑，完全契合「走 subscription 不走 API」。LLM 只留给散文类源。

- **怎么做的**：`scripts/monsters_extract_gs2.py`（镜像 gs1 的 `monsters_extract.py`）确定性解析
  `torrentlord` 的 Division A「Complete List」：按 `HP n (Regen m)` 锚定每块、`Ven Mrc Mar Jup`
  按名映射元素、`-Location- (n)` 用顶部图例解析地名。**零 LLM 调用**。
- **中间层物化**：per-source 规范化产物写到 `data/gs2/intermediate/monsters__torrentlord.json`（可单独
  inspect），再 enrich/merge 成 `data/gs2/monsters.json`。merge 里的 `pick()` 冲突标记框架已就位，
  加第 2 源即用——单源 torrentlord 已足够产出完整高质量数据。
- **产出**：**203 个 monsters**（含 23 个 boss stat-line、27 个可战 djinn），每条 9 项 stats + 四元素
  power/resist + abilities + drops(含 ICC) + found(地名) 全齐；0 校验错误、id 唯一、location 全解析。
- **踩坑（已修，沉淀给后续 data-table 解析）**：① 地点索引有 `(10a)` 内部/后段后缀；② boss 多形态
  HP 是斜杠分隔 `5000 / 4200 / 4000`（取首值）——曾导致 Karst/Agatio/Doom Dragon 漏解析并污染前一条；
  ③ ICC 可能是 `?`（未知→null）。**教训：data-table 源要先扫"非常规行"再定锚，并用「块数 vs 锚数」对账。**
- **FK 暂缓（如计划）**：`boss_id`/`djinn_id`/drop `ref_id` 全 null，待 gs2 的 bosses/djinn/items/
  equipment 实体齐了再由 `links_normalize` 阶段补。`is_boss` 用 curated 名单（boss guide 提取），待
  `bosses.json` 存在后细化。

**对中间层假设的回答**：值得，但形态是**确定性解析器 + 物化中间产物**，不是泛化的「LLM 预处理文件」。
下面矩阵里标 `data-table` 的源（torrentlord/mr-unorigino-item/ultimalink/shotgunnova-shop/demooni/
mr-unorigino-psy）都走这条路；散文/多源软合并的才考虑 LLM。

---

## 1. 实体 × 源 覆盖矩阵（提取的核心底料）

每行一个目标实体，列出**主源（干净数据，优先喂）/ 辅源（补全 & 交叉校验）/ 冲突注意**。
源 id 见 `gs2_sources.md`。综合 walkthrough（telago/super-slash/autocon/shotgunnova… 均 `type:
general`）几乎对每个实体都有附录表，作为通用辅源/兜底，不再每行重复列——下面只点出**专项主源**。

| 实体 | 主源（专项，优先） | 辅源 / 校验 | 备注 |
|---|---|---|---|
| **monsters** ✅ | `torrentlord`（全 stat block + 掉落 + location）→ **已提取，203 条** | walkthrough bestiary（autocon/darthmarth/super-slash）；`aspartate-forge`（产材料怪） | **竖切完成**（见 §0）。确定性解析器 `scripts/monsters_extract_gs2.py`，单源 torrentlord。第 2 源做交叉校验是后续可选项。 |
| **bosses** ✅ | `torrentlord`（boss 数值，已在 monsters）；`link-kirby-boss`（打法/弱点/等级）→ **已提取，18 条** | `goldmario-boss`、`rena-chan-hardboss`（Hard Mode）、walkthrough boss 段、`ikillkenny` 待并入 sidecar | **第三刀完成**：两层=确定性骨架(`bosses_extract_gs2.py` 从 monsters 拉数值/合并多形态) + curated strategy sidecar(`intermediate/bosses_strategy.json`，从 link-kirby 提 weakness/level/strategy/mechanics)。数值以 torrentlord 为准不静默改。monsters.boss_id 回填待 gs2 links_normalize。 |
| **classes** ✅ | `terence`+`ultimalink`+`telago`(L3)+`aku-chi`(ACR)+`autocon`(Tamer)→ **110 条，全层完成** | `aku-chi`(ACR)；`autocon`(Tamer learn-list)；`telago`(L3 djinn-combo) | **Layer1+2+3+4 完成**：`classes_extract`+`_ultimalink`+`_telago_reqs`(335 条 djinn-combo 带 x\|y)+`_acr`(aku-chi→`available_to[].acr` 37 条+`acr_config`)+`_tamer_psynergy`(autocon→4 子职 +48 psynergy)。gs2=Element-Level+Dominance。`djinn_requirements` telago+ultimalink 双源满。**判冗余跳过**=terence「Prm Aff Wek Neu」matcher。**剩 expected-gap**=classes.psynergy `Blast`(2 同名歧义)；ACR stat% 交叉校验可选。 |
| **psynergy** ✅ | `yoyoyoshi` m11「ALL PSYNERGIES」(pp/range/desc/element)→ **231 条**（157 canonical + 72 telago + 2 name-only） | `telago` 33 附录(职业专属带 stats)；`mr-unorigino-psy`（completeness）；classes 学法表；`terence` | **第九刀 + telago 附录 + 缺口收尾完成**：`psynergy_extract`(157)+`psynergy_appendix`(telago 33→+72；6 变体折进 name_variants 含 Fairy/Minotaurus；**NAME_ONLY** +2=Splash[water]/Siren[null] name-only+conflicts flag)。classes.psynergy expected-gap **37→3→1**：仅 `Blast`(2 同名按名不可消歧)；Splash 补、`Quake Strike→Quick Strike` 走 ALIASES。 |
| **djinn** ✅ | `demooni`（element + stat boosts + 位置 + *FIGHT*，单源全覆盖）→ **已提取，72 条**（44 gs2 + 28 gs1） | `aspartate-djinn`/`android50`（location.area 补全）；`cooldude345`/`terence`（battle_effect 机制）；walkthrough 附录A(telago) | **第四刀完成**：确定性解析器 `djinn_extract_gs2.py`。demooni 的 `---` 分隔正好是 TLA(gs2)/GS1(gs1) 分界，每元素 11+7=18。deferred：battle_effect、location.area、monsters.djinn_id 回填（monsters 27 djinn-enemy vs demooni 26 *FIGHT*，连图时核对）。 |
| **summons** ✅ | `cooldude345`（VII 数值[引 Terence Fergusson] + V 配方/获取，双段 merge）→ **已提取，29 条**（16 标准 + 13 组合） | `dbfire`（石板获取 + 支线，可选 2 源）；walkthrough（telago 附录A / autocon §3.6） | **第五刀完成**：确定性解析器 `summons_extract_gs2.py`。组合召唤 `djinn_recipe`[{element,count}] + `acquisition`。Coatlicue 治疗特判。cooldude 把 Valukar 写作 Bullrog、Sentinel→Sentinal，连图时核对。 |
| **equipment** ✅ | `mr-unorigino-item`（TLA 段 2A–2U + **base 段 -A.‥-R3.**）→ **已提取，285 条**（143 TLA + 142 base/shared） | `aspartate-item`；`shotgunnova-shop`（售价/售点）；`aspartate-forge`（锻造 forged_from）；`90kirsdarke-hack`(命名校验) | **第二刀 + SSoT full extract 完成**：`scripts/items_extract_gs2.py`(2026-06-19 反转「只取 TLA」→full extract base 段,game="gs1")。`forged_from` 由 `forging_extract_gs2.py` 回填、`equippable_by` 由 type→can_equip 派生(265/285)。6 处采纳 90Kirsdarke 真名(NAME_FIXES+name_variants)。**本轮小修(§5)**：Levatine unleash `Radient`→`Radiant`、Dragon Armor 锻造别名。 |
| **items** ✅ | `mr-unorigino-item`（TLA 段 + base 段）+`shotgunnova`→ **已提取，86 条**（23 consumable + 17 psynergy_item + 33 key + 13 material） | `aspartate-item`；`bbbbrain2000`；walkthrough item 附录 | 与 equipment 同源同解析器。**2026-06-19 full extract**：base 段并入(17 Psynergy 道具 + key item Red/Blue Key/Stars/Black Orb + base 武防/Ring/Boots/消耗品)。 |
| **shops** ✅ | `shotgunnova-shop`（15 城镇清单，link location↔item） | walkthrough shop 段（shotgunnova general） | `shops_extract_gs2.py`→15 城镇 204 stock，全 resolve。**残留**：Mikasalla/Naribwe 有 `shop:true` 但 shotgunnova 没收、2a 散文也无清单（§5 判不可恢复）。 |
| **forging** ✅ | `aspartate-forge`（材料→装备 + 锈蚀 + 产材料怪） | `aspartate-item` mini guide；walkthrough forging 段 | `forging_extract_gs2.py`→回填 `equipment.forged_from` 56/57（并入 equipment，非独立实体）。**本轮小修(§5)**：Dragon Armor 无匹配（aspartate 别名→我方某甲）。 |
| **locations** ✅ | 2a walkthrough prose（Gemini，cloud-blazer spine） | `shotgunnova-shop`；djinn/物品位置源 | → `locations.json` 62 条（gs2 模型相对 gs1 倒置：locations 自带 forward ref，反向图物化在 `location_refs.json`，不污染实体文件）。`locations_refs_gs2.py` + `djinn_area_backfill_gs2.py`。 |
| **characters** ✅ | `darkslime`「Character Guide」结构块（element/hometown/can_equip）→ **已提取，8 条** | `ultimalink`（确认 8 花名册）；`darthmarth`（join 校验）；剧本源（story，仅背景） | **第六刀完成**：`characters_extract_gs2.py` 两层=darkslime 结构块(带 `Can Equip:` 行=可玩判据) + curated `is_starter`/`from_gs1`/`join`(ER §4.1 拆 gs1 的 is_permanent)。源缺陷：Sheba hometown 折行带入 "Caps"，literal 保留待连图核对。 |
| **transfer**（机制） | `dbfire`（4 事件）；`mr-unorigino-pw`（password 对照） | walkthrough transfer 段（autocon 6 事件 / telago linkage） | gs2 专有；归机制/事件，不一定独立实体。 |

**非提取源（不进任何实体，仅参考/校验/背景）**：
- `90kirsdarke-hack` / `kaitia-savehack` — hex/内存码 → 见 §4「master-data / canonical id」想法。
- `sintaku-script` / `mtkennerly-script` / `thehomeland-dialogue` — 剧本/对白（story），仅角色背景参考。
- `barbarossa89-music`（music）、`barbarianbob-glitch`（glitch）、`link-kirby-rng`（RNG 刷取）— 杂项，跳过。
- `josher1212` — 未完成且无 TOC，**待补 TOC 后再评估**（见 §4）。

---

## 2. 每实体执行分工（Claude Code vs Gemini）— **初步，待定**

原则（沿用 gs1 经验 + `gs2_plan.md §4`；**已被 §0 竖切修正**）：
- **规整 data-table 源**（torrentlord/mr-unorigino-item/ultimalink/shotgunnova-shop/demooni/
  mr-unorigino-psy…）：**优先写确定性 Python 解析器**（§0 已验证：免费/精确/可重跑），**不用 LLM**。
  只有当某源格式太乱、解析器性价比低时才退回 LLM。
- **需要细 judgment / 跨源合并 / 冲突标记**（djinn 位置+数值合并、classes 多源交叉）：
  倾向 **Claude Code**（指令遵循 + 冲突处理更稳）。
- **超长 walkthrough**（>250KB，locations/characters）：沿用 gs1 **子代理按 TOC 章节批量**先例。
- `extract.py`(API) 仅作懒人 fallback（某小实体几分钱）。

> 这张分工表等 `gs2_schema.md` 字段定下来、并对重点源再抽读后再拍板。先留占位。

---

## 3. gs2 实体范围草记（discovery，喂给 `gs2_plan.md §4` 待定 2/3）

> 已升级为正式建模草图：[`gs2_er_sketch.md`](gs2_er_sketch.md)（实体清单 + id 方案 + FK 边 +
> 连接原则 + 4 个 gs2 增量的建模倾向）。下面是最初的 discovery 笔记，保留备查。

标注时观察到、与 gs1 的差异（**待 schema 阶段细化，先记不展开**）：
- **characters**：`ultimalink` 的职业表覆盖 8 个角色（Felix / Isaac / Jenna / Garet / Sheba /
  Ivan / Piers / Mia）——gs2 比 gs1 多，且含新角色 Felix/Jenna/Sheba/Piers + 后期回归的 4 名
  gs1 Adept。characters/classes 实体规模比 gs1 大。
- **新增/扩展机制实体**：`transfer`（GS1→GS2 联动事件 + password）、`forging`（Sunshine 锻造）、
  **组合/石板召唤**（Daedalus/Catastrophe/Charon/Iris…）。是否各立实体、还是并入现有实体
  （forging→equipment？transfer→事件附录？），schema 阶段定。
- **可播种继承**：djinn 体系、部分 equipment/item 与 gs1 重叠（mr-unorigino-item 直接 GS1+TLA
  并列），可考虑拿 gs1 数据当草稿再 diff——但遵守「gs1/gs2 两份独立真相源，不互相 import」。

---

## 4. 遗留 TODO / 待单独处理（用户指定，本轮不做）

1. **`josher1212`（Reference Guide）补 TOC**：原文无 TOC 且未完成，但内容有价值。需**单独一轮
   通读**后给它加标准化 TOC（`## TABLE OF CONTENTS` … `END OF TABLE OF CONTENTS`），再评估提取价值。
2. ~~**hex / master-data 层**~~ **已评估并部分落地（2026-06-19）**：
   - `90kirsdarke-hack` **item 完整性 cross-check 完成** = `scripts/kirsdarke_completeness_gs2.py`
     （解析两段码表 359 distinct name，按名 diff equipment+items；matched 160/359、theirs-not-ours
     199=完整枚举 deferred 共享段、ours-not-theirs 10=查出 mr-unorigino 命名瑕疵）。可重跑当门禁。
   - **canonical-id / code 层提案 → 否决**：90Kirsdarke hex 码与我方 `debug_no`(mr-unorigino) 编号
     体系不同（非线性、不可换算），挂不上统一 code；只能按名做完整性兜底。
   - **djinn 不在覆盖**：该源 djinn 段是改档内存地址，非 djinn 名单（仅 8 Venus 名作 binary 示例），
     djinn 完整性仍以 demooni 为准。
   - `kaitia-savehack`（全存档地址 = 改档结构，非实体数据）**低优先 / 可不做**。
   详见 `gs2_plan.md §5 日志(2026-06-19) + §6 backlog`。
3. **分工表拍板**：§2 的 Claude/Gemini 分工待 schema 定稿后确认。

---

## 5. 数据缺口收尾轮（2026-06-20，Tier1+Tier2）✅ 全完成

**Context**：11 实体已全提取 + telago 附录补料 + cross-check 三轮 + SSoT 闭环全过（详见 `gs2_plan.md §5/§7`），三应用交付物各有第一版。剩余多是 expected-gap。这轮（用户拍板 **Tier1+Tier2**）把可确定性恢复的缺口清掉，啃完 classes 这块最后的硬骨头；不可恢复/噪声项文档化为 expected-gap。**全部走确定性解析器（免费/可重跑），无 API 成本。**

> 缺口来源细节见 `crosscheck_findings.md`；本节是 execution 清单，进度回标 ⬜/🔄/✅。
> **结果（2026-06-20）**：6 项全 ✅。`available_to[].acr` 37 条回填；4 Tamer 子职 +48 psynergy；
> **classes.psynergy expected-gap 3 distinct → 1**（仅 `Blast` 歧义 x14 留 expected-gap）；forging
> **53→57/57**；locations_refs **bosses 17→19/24**（2 复合名解析）。链尾 `links_audit` + kirsdarke +
> placement **全 exit 0**，codex 已 regen（psynergy 231）。

### Tier 1 — classes 完整性（新确定性解析器）

| # | 项 | 脚本（新） | 源 / 格式 | 落点 + 建模 | 状态 |
|---|---|---|---|---|---|
| 1 | **ACR** | `scripts/classes_acr_gs2.py` | `aku-chi`「Class Setup Guide」#1–#7 setup 表，per-row `[Char] - [Class] ([config]) [stat%×6] [ACR]`（定宽，行尾单 decimal） | 回填 `available_to[].acr`。**建模(用户拍板)**=每 (角色,职业) 取跨 setup **最高 ACR** + 新增 `acr_config` 记达成配置（如 "8 wind"）。消歧=character+class name → available_to 条目（仿 `classes_telago_reqs_gs2.py` 签名匹配）。 | ✅ `classes_acr_gs2.py`：70 行→37 distinct，回填 37，footnote 展开，0 unmatched |
| 2 | **Tamer learn-list** | `scripts/classes_tamer_psynergy_gs2.py` | `autocon` `raw/gs2/_chapters/autocon/218-tamer.md` 的 `Learns:` 定宽 4 列矩阵（`Lvl \| Tamer \| Trainer \| Beastkeeper \| Beast Lord`，`-----`=该级不学） | 回填 4 子职（tamer/trainer/beastkeeper/beast-lord）的 `classes.psynergy`（写 `{name, level, sources:["autocon"]}`，`id` 交 links_normalize 回填，格式同 squire）。 | ✅ `classes_tamer_psynergy_gs2.py`：+48 psynergy（9/11/13/15）。Fairy→Faery、Minotaurus→Minotaur 折为 name_variants（psynergy_appendix VARIANT_OF）；Siren 见下 |

### Tier 2 — 小修（data-edit / 别名）

| # | 项 | 改哪 | 说明 | 状态 |
|---|---|---|---|---|
| 3 | **Splash psynergy** | `psynergy.json`（经解析器/补丁） | 8 个 classes ref 无对应 canonical。**注**：autocon 类表只给名+级、无 stat 行；执行先查 telago 33 / yoyoyoshi 有无 stat 源——有则带 stat 补，无则最小条目 + flag（element 按上下文 water）。 | ✅ Splash(water)+Siren(null) 加 name-only+conflicts flag（psynergy_appendix NAME_ONLY，231 条）；**Quake Strike→Quick Strike** 走 ALIASES（双脚本）；Blast 留 expected-gap |
| 4 | **Levatine unleash typo** | `items_extract_gs2.py` 的 NAME/unleash fix 表 | unleash `Radient Fire`→`Radiant Fire`（mr-unorigino vs aspartate 跨源冲突，采 aspartate 正确拼写；旧拼写留 flag）。折进 extractor 保 regen 不丢。 | ✅ `items_extract` UNLEASH_FIXES：unleash `Radient Fire`→`Radiant Fire`，旧拼写入 unleash.name_variants |
| 5 | **Dragon Armor 锻造别名** | `forging_extract_gs2.py` FORGE_ALIASES | aspartate「Dragon Armor」(Def+44) 在 forge 无匹配。**注**：Def+44 同时撞 Dragon Scales / Dragon Mail，执行时按 aspartate forged_from/equip 上下文消歧到正确那件。 | ✅ `Dragon Armor`→**Dragon Mail**（抗 15/15、worth 7275=sell 吻合）。顺手删 NAME_FIXES 后失效的 3 个 stale alias→forging **57/57** |
| 6 | **boss 复合名别名** | `links_normalize_gs2.py` + `bosses.json` | `Agatio & Karst` / `Moapa & Knights` 加 compound→pair 解析层（如 bosses.json 加 `compound_names` + normalize 解析），供 codex/walkthrough ref。数据 split 存储本身正确（cross-check 已确认）。 | ✅ bosses_extract 加 `compound_names`（COMPOUND_NAMES），locations_refs 数据驱动 `compound_by` 展开→bosses 17→19/24 |

### 链尾（每次改 data 后必跑）

`links_normalize_gs2 → links_audit_gs2`（exit 0=干净）+ 4 个 cross-check gate；数据稳后 `build_codex_gs2.py` regen `tools/gs2_codex.html`（数据内嵌，不自动刷新）。

### 本轮不做 → 文档化为 expected-gap

- **terence「Prm Aff Wek Neu」matcher**：`available_to[].djinn_requirements` 已 telago(区间)+ultimalink(定点)双源填满，Build Planner 已基于此工作；terence 第三源冗余，**跳过**（留作可选三源交叉校验）。
- **Mikasalla/Naribwe shop stock**：2a 散文仅「buy armor here」无清单，无 stock 源 → **不可恢复**，留 expected-gap。
- **90Kirsdarke 13 theirs-not-ours**：多为对方 typo（Beserker/Cosair/Psyenergy/Saftey…）= 噪声；可选给 `kirsdarke_completeness_gs2.py` THEIRS_ALIASES 补几条，非必须。
- **Quake Strike**（无任何源）/ **Blast**（2 个 fire canonical 同名、按名不可消歧）psynergy → 留 expected-gap。
- classes **stat% 表交叉校验**（telago 26）、**ACR 全 config sidecar** → 可选，本轮取最高值即可。
