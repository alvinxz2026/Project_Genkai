# GS2 — 项目计划 & 进度追踪（meta，living doc）

> **这是一份会持续迭代的元文档**，不是一次性计划。一开始故意只写到 high-level；
> 做着做着有了新想法、或执行方法变了，就回来改这里。它的作用是给 gs2 一个
> idea → design → plan → execution 的主线 + 一个能随时看「做到哪了」的地方。
> 细节（schema、脚本怎么复用、怎么提取）**留到真正动手那一步再展开**。
>
> 配套：收尾 + 启动的来龙去脉见 `docs/gs1_wrapup_gs2_kickoff_plan.md`。

---

## 0. 一句话定位

把 lore-engine 这套**「schema 先行 → 提取 → 冲突标记 → FK 连图 → audit」**管线，
第二次跑在一份真实语料上（Golden Sun 2），验证它**可泛化**——同时产出一份 gs2 的
结构化知识库，目标是「**我可以一边打 gs2 一边用**」。

GS2 和 GS1 共用同一套管线、同一个仓库，按 `gs2` 命名空间分目录：
`raw/gs2/`、`data/gs2/`、`schema/gs2_schema.md`、`docs/gs2/`、`tools/gs2_*.html`。

---

## 1. 起点 / 继承自 GS1

- **管线现成**：`scripts/extract.py` 直接 `--game gs2` 可用；其余脚本是否复用见 §4 待定。
- **数据可播种**：gs2 在机制上继承 gs1（4 名 gs1 Adept 后期回归、Djinn 体系延续、
  部分 item/equipment 复现），所以 djinn / classes / 部分 equipment 可拿 gs1 当种子草稿再 diff。
  原则：**gs1 与 gs2 是两份独立真相源，不互相 import**。（细节 §4 待定。）
- **约定现成**：snake_case / `0` vs `null` / 每条带 `sources` / 冲突标记不静默合并
  （见 `schema/gs1_schema.md` General Rules，gs2 沿用）。

---

## 2. 阶段主线（high-level，状态随做随更）

| 阶段 | 内容 | 状态 |
|---|---|---|
| **0. Kickoff** | 建 gs2 命名空间脚手架 + 这份 meta plan | ✅ 完成 2026-06-17 |
| **1. Idea / 范围** | 想清楚 gs2 要覆盖哪些实体、做成什么应用（可参考 gs1 的 11 实体起步） | ⬜ 待 review |
| **2. Raw 收集 + 标注** | 收齐 GameFAQs 源到 `raw/gs2/`，每篇加 frontmatter（见 §3）；建源清单/索引 | 🔄 近完成：10 篇 walkthrough + 32 篇 In-Depth + 目录页均已收+标注，索引 `gs2_sources.md` 已建（含 tracker）；目录页专项源已悉数到位，仅余 Maps 暂不收 |
| **3. Design — schema** | 先有 ER 草图钉 id/FK，再以 `gs1_schema.md` 为模板写 `gs2_schema.md`（含 Master Source IDs 表） | 🔄 ER 草图 `gs2_er_sketch.md` ✅ + `gs2_schema.md` monsters 段 ✅；其余实体段未写 |
| **3.5 Extraction plan** | 按实体讨论怎么提取、每个实体/源用 Gemini 还是 Claude Code（见 §4 已定 + 待定） | 🔄 已起草 draft：`docs/gs2/gs2_extraction_plan.md`（实体×源覆盖矩阵 + 初步分工），待 refine |
| **4. 提取 + 连图** | 逐实体提（**规整 data-table 走确定性解析器**，见竖切结论；agent/extract.py 为退路）；播种继承数据；跑 normalize→audit（纯 Python，免费） | 🔄 monsters ✅（203 条，竖切验证）；其余未开始 |
| **5. 应用层** | 复用/扩展 codex 等（gs2 版或合并版） | ⬜ 远期 |

> 勾选用 ⬜/🔄/✅。每推进一块就回来改这张表 + §5 日志。

---

## 3. Raw 收集 + 标注规范（你的主战场）

目标：收集阶段就把「作者 / 这份强在哪 / 能喂给哪个实体」标清楚，让 gs2 比 gs1 更 organized。
这些标注最终会誊进 `gs2_schema.md` 的 Master Source IDs 表，作为提取的源映射（agent 或 extract.py 都按它定位源文件，见 §4）。

**工作分工**：frontmatter **你收集时先手动加最小集**（id/author/url/type），
其余（`covers` 打标、`summary`）**我后面可代你补全**——我可以读完每篇后回填 `covers` 和一句话 `summary`。

**存放**：每个源存成 `raw/gs2/<描述性文件名>.md`（统一 `.md` 以便带 frontmatter；
extract.py 同时认 `.txt`/`.md`）。文件名建议 `<内容> - <作者>.md`，沿用 gs1 习惯。

**正文处理铁律（2026-06-17 定）**：raw 正文**不整理、不重排、不物理拆分**——raw 是
不可变源，结构在提取阶段才按 schema 赋予。超长 walkthrough 靠**标准化 TOC 做定向读取**
（每篇用 `## TABLE OF CONTENTS` … `END OF TABLE OF CONTENTS` 包裹），提取时按 TOC 章节
锚点只把相关段落喂给对应实体，省 token 又保持 raw 不可变。

**covers 词表（gs2 版）**：沿用 gs1 的 11 实体 + `walkthrough`，新增 3 个 gs2 机制 tag：
`transfer`（GS1→GS2 linkage/password/transfer events）、`forging`（Sunshine 铁匠/锈蚀武器/
稀有材料锻造）、`mechanics`（战斗系统/djinn 用法/属性/RNG 等 basics）。石板/组合召唤归
`summons`(数值) + `locations`/`walkthrough`(获取)。词表非封闭，写 schema 时可再加。
> **2026-06-17 标注 In-Depth 时新增 4 个 tag**：`story`（剧本/对白 dump，非实体提取）、
> `music`、`glitch`（杂项 FAQ，非提取）、`ids`（hex/内存码源，价值在 canonical id + 完整性校验）。
> 这些主要用于把「非实体提取源」与真正的数据源区分开。

**frontmatter 模板**（已纳入你的反馈：catch-all type、quality 默认、summary 可后补）：

```markdown
---
source_id: telago            # 短 id；用 -/_ 分词便于文件名 token 匹配；最终进 schema 的 Master Source IDs
author: Telago
url: https://gamefaqs.gamespot.com/...
type: general                # walkthrough | faq | data-table | mechanics | general
                             #   general = catch-all：一篇里啥都有的综合源（可不拆）
covers: []                   # 这份对哪些实体有用，如 [djinn, classes]；收集时可留空，我后面帮你 tag
quality: unknown             # unknown(默认) | high | medium | partial —— 拿不准就留 unknown
summary:                     # 留空即可；我读完可代填一句话
gs1_counterpart:             # 若同作者也写过 gs1，标一下 gs1 文件名，便于对照继承
notes:                       # 可选，一句话：强在哪 / 坑在哪
---

<原文照抄，不改正文>
```

**总索引**：[`docs/gs2/gs2_sources.md`](gs2_sources.md) 已建——把已收的 10 篇 walkthrough +
目录页链在一起（source_id / 作者 / 版本年份 / quality / covers / 链接 / summary），
并附"候选 / 未收集"区列出目录页里的专项 In-Depth Guides（Terence、torrentlord 等），便于按需补齐。
新收一个源就登记进去。

---

## 4. 待定决策（动手前再拍板，先不展开）

> **已定（2026-06-17）**：
> - raw 是否预处理 → **不预处理**（正文不整理/不拆分，见 §3 铁律）；covers 词表见 §3。
> - **提取走 subscription / agent，不依赖 `extract.py`(API)**：走 API 按 token 计费，比已付的
>   subscription plan 更贵。所以 raw→JSON 提取由 agent 跑（Claude Code 和/或 Gemini CLI，
>   按源大小分工），沿用 gs1 巨型 walkthrough 的"子代理批量提取"先例（见
>   `docs/gs1/gs1_walkthrough_extraction_plan.md`）。`extract.py` **降级为可选 fallback**
>   （某个小实体懒得开 agent 时用，API 成本几分钱）。
>   - 推论：`gs2_schema.md` 仍是核心 spec（无论谁执行都按它产出，字段/0-vs-null/`sources[]`/
>     冲突标记不变）；下游 `links_normalize→audit→build_codex` 是纯 Python、零 LLM 成本不受影响；
>     extract.py 不扫子文件夹这点也不再绑文件夹结构。
>   - **待定**：每个实体/源具体用 Gemini 还是 Claude Code → 下一轮 frontmatter 补全后，
>     专门做一份 **extraction plan** 讨论（见 §2 阶段 3.5）。


1. **半通用脚本怎么复用**：`links_normalize` / `links_audit` / `locations_refs` / `build_codex`
   现在 gs1 写死。走 (A) 参数化共用 还是 (B) fork 一份？倾向 A 但「等 gs2 实体定了再抽」。
2. **继承数据怎么播种**：哪些实体从 gs1 拷草稿（djinn/classes/equipment？），怎么标「继承 vs 待改」。
   → discovery 草记见 [`gs2_extraction_plan.md §3`](gs2_extraction_plan.md)（mr-unorigino-item 直接 GS1+TLA 并列等）。
3. **schema 差异**：gs2 新增（队伍 Felix/Jenna/Sheba/Piers、transfer 机制、新 summon/地点/boss），
   哪些实体直接沿用 gs1 段、哪些要改。→ 实体范围草记见 [`gs2_extraction_plan.md §3`](gs2_extraction_plan.md)
   （characters 8 角色、forging/transfer/组合召唤 是否独立实体）。
4. **应用层**：gs2 单独出 codex，还是做成跨 game 的统一 app。
5. **master-data / canonical id 层（新）**：用 hex 源（`90kirsdarke-hack` / `kaitia-savehack`）给
   每条数据挂 code/id + 做完整性校验？用户提议，待单独一轮（见 `gs2_extraction_plan.md §4`）。

---

## 5. 进度日志

| 日期 | 进展 |
|---|---|
| 2026-06-17 | Kickoff：建 `raw/gs2` `data/gs2` `docs/gs2` 脚手架 + `schema/gs2_schema.md` 骨架 + 这份 meta plan。待用户 review/annotate。 |
| 2026-06-17 | Raw 标注：收 10 篇 walkthrough + 目录页；补全 frontmatter(短 source_id/covers/summary)；定"正文不整理/不拆分、用 TOC 定向读"铁律 + gs2 covers 词表(新增 transfer/forging/mechanics)；建总索引 `gs2_sources.md`(含候选专项源)。正文零改动。 |
| 2026-06-17 | 定提取路线：**走 subscription/agent(Claude Code 和/或 Gemini)，不依赖 extract.py(API，更贵)**，extract.py 降级 fallback；schema 仍是核心 spec，下游 Python 连图免费。加阶段 3.5「Extraction plan」——下一轮补全专项源 frontmatter 后专门讨论各类数据怎么提取、每实体用谁。 |
| 2026-06-17 | 收 32 篇 In-Depth Guides（含补回的 `bbbbrain2000`）+ 补全 frontmatter（短 `source_id` 规范化 / `type` / `covers` / `quality` / `summary`）；新增 4 个 covers tag（`story`/`music`/`glitch`/`ids`）。`gs2_sources.md` 加四组「已收集 In-Depth」表 + 标注进度 tracker；候选区只剩 Maps。起草 `gs2_extraction_plan.md`（实体×源覆盖矩阵 + 初步 Claude/Gemini 分工，draft）。正文零改动。遗留：`josher1212` 待补 TOC、hex 源（`90kirsdarke-hack`/`kaitia-savehack`）待评估做 master-data/canonical id 层。 |
| 2026-06-17 | **第一刀竖切：monsters ✅**。写 `gs2_schema.md` monsters 段 + Master Source IDs 起头；写确定性解析器 `scripts/monsters_extract_gs2.py`（镜像 gs1 `monsters_extract.py`）解析 torrentlord Division A → 物化中间层 `data/gs2/intermediate/monsters__torrentlord.json` → `data/gs2/monsters.json`：**203 条**（23 boss + 27 djinn-enemy），全字段齐、0 错、零 LLM。**结论：干净 data-table 源的「中间层」= 确定性解析器（免费/精确/可重跑），非 LLM 蒸馏**（详见 `gs2_extraction_plan.md §0`）。FK（boss_id/djinn_id/drop ref）按计划暂缓。 |
| 2026-06-18 | **ER 草图 `gs2_er_sketch.md` ✅**。把 gs1 已跑通的实体关系图（11 实体 + characters 维度 / locations 枢纽 + 各 FK 边）整理成 gs2 版，钉死 id 方案 + 引用字段 + 连接原则（存 name、最后 `links_normalize` 回填 id、idempotent → 实体可任意顺序独立提取，不返工）；标出 4 个 gs2 增量及建模倾向（8 角色、forging=equipment.forged_from、组合召唤=djinn_recipe、transfer=标志/小事件表）。回答了「中间层直觉」：字段完整性靠源够多、关联设计靠这张图，两者分开；无需先做 mechanics 预处理。 |
