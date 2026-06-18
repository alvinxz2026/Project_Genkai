# GS2 — Extraction Plan（阶段 3.5，**DRAFT**）

> **状态：draft / discovery。** 本文在标注 32 篇 In-Depth + 10 篇 walkthrough 的
> frontmatter 时顺手沉淀，用来回答「每个实体从哪些源提、谁主谁辅、用 Claude Code 还是
> Gemini」。**先不 finalize**——等 `gs2_schema.md` 起草、源再抽读细化后再 refine，然后才
> 往 execution 走。配套：源清单见 [`gs2_sources.md`](gs2_sources.md)，主线见 [`gs2_plan.md`](gs2_plan.md)。

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
| **classes** 🔄 | `terence`(脊柱:stat_multiplier+element_requirements+group)+`ultimalink`(psynergy 习得+available_to)→ **Layer1+2 已提取，110 条** | `aku-chi`（ACR/配装，Layer3）；walkthrough class 段；`yoyoyoshi`（djinn↔class） | **第七+八刀 Layer1+2 完成**：`classes_extract_gs2.py`(terence 9 张表)+`classes_ultimalink_gs2.py`(block title→class_line 映射+tier 位置 zip)。gs2=Element-Level+Dominance(非 gs1 djinn 计数)。Layer1 id 用 qualifier 后缀避让(seer-water vs water-seer)。Layer2：106/110 有 psynergy(Tamer 缓)、110/110 available_to；元素上下文 id 预消解 per-角色 psynergy 分歧。**Layer3 待**=terence「Prm Aff Wek Neu」相对计数 matcher(gs2 版 build_terence_class_reqs)+aku-chi ACR。 |
| **psynergy** ✅ | `yoyoyoshi` m11「ALL PSYNERGIES」(pp/range/desc/element)→ **已提取，157 条 canonical** | `mr-unorigino-psy`（completeness 校验，乱码只用 US 名，corroborate 126）；classes 学法表(补漏~37 个)；walkthrough；`terence` | **第九刀完成**：`psynergy_extract_gs2.py` 确定性解析 yoyoyoshi 定宽表。Blast 按 pp 消歧。**yoyoyoshi 非穷尽**：classes.psynergy 有~37 个职业技(Pierrot 卡牌/高阶攻击/Thorn/Nettle 等)不在此+ultimalink ~7 拼写+1 冲突(Megacool/Supercool)→交 gs2 links_normalize 核对补漏(classes.psynergy.id 待回填)。deferred：series/tier、level_learned/available_to(可从 classes 反查)。 |
| **djinn** ✅ | `demooni`（element + stat boosts + 位置 + *FIGHT*，单源全覆盖）→ **已提取，72 条**（44 gs2 + 28 gs1） | `aspartate-djinn`/`android50`（location.area 补全）；`cooldude345`/`terence`（battle_effect 机制）；walkthrough 附录A(telago) | **第四刀完成**：确定性解析器 `djinn_extract_gs2.py`。demooni 的 `---` 分隔正好是 TLA(gs2)/GS1(gs1) 分界，每元素 11+7=18。deferred：battle_effect、location.area、monsters.djinn_id 回填（monsters 27 djinn-enemy vs demooni 26 *FIGHT*，连图时核对）。 |
| **summons** ✅ | `cooldude345`（VII 数值[引 Terence Fergusson] + V 配方/获取，双段 merge）→ **已提取，29 条**（16 标准 + 13 组合） | `dbfire`（石板获取 + 支线，可选 2 源）；walkthrough（telago 附录A / autocon §3.6） | **第五刀完成**：确定性解析器 `summons_extract_gs2.py`。组合召唤 `djinn_recipe`[{element,count}] + `acquisition`。Coatlicue 治疗特判。cooldude 把 Valukar 写作 Bullrog、Sentinel→Sentinal，连图时核对。 |
| **equipment** ✅ | `mr-unorigino-item`（TLA 段 2A–2U）→ **已提取，143 条** | `aspartate-item`（数据+定性）；`shotgunnova-shop`（售价/售点）；`bbbbrain2000`（隐藏）；`aspartate-forge`（锻造） | **第二刀完成**：确定性解析器 `scripts/items_extract_gs2.py`，单源 mr-unorigino TLA 段。deferred：equippable_by/is_artifact/forged_from/unleash 元素·rate·power。forging 单列见下。 |
| **items** ✅(部分) | `mr-unorigino-item`（TLA 段：2R 材料 / 2S trident / 2U other）→ **已提取，24 条** | `aspartate-item`；`bbbbrain2000`；walkthrough item 附录 | 与 equipment 同源同解析器。**只取 gs2 专属**；gs1↔gs2 共享消耗品（Herb/Potion/Psy Crystal/补品）源里仅在 GS1 编号段，**deferred** 待下轮用 super-slash/shotgunnova 附录补。 |
| **shops** | `shotgunnova-shop`（15 城镇清单，link location↔item） | walkthrough shop 段（shotgunnova general） | gs1 同作者（`Various data - Shotgunnova.txt`）。 |
| **forging** | `aspartate-forge`（材料→装备 + 锈蚀 + 产材料怪） | `aspartate-item` mini guide；walkthrough forging 段 | gs2 专有机制；可单列实体或并入 equipment（schema 再定）。 |
| **locations** | walkthrough（cloud-blazer 区域最细）；`shotgunnova-shop`（城镇）；`dbfire`（支线区域） | `gamecubeguy49-islet`、djinn/物品位置源 | locations 仍靠 walkthrough 为主；专项源补点。 |
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
2. **hex / master-data 层**（`90kirsdarke-hack` item/djinn 码 + `kaitia-savehack` 全存档地址）：
   评估能否用这些内存码给我方每条数据挂一个 **canonical id / code**，做一个跨实体的
   master-data / 完整性校验层。用户提议，单独一轮处理。
3. **分工表拍板**：§2 的 Claude/Gemini 分工待 schema 定稿后确认。
