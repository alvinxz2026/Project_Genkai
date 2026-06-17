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
| **2. Raw 收集 + 标注** | 收齐 GameFAQs 源到 `raw/gs2/`，每篇加 frontmatter（见 §3）；建源清单/索引 | ⬜ 你主导，未开始 |
| **3. Design — schema** | 以 `gs1_schema.md` 为模板写 `gs2_schema.md`（含 Master Source IDs 表） | ⬜ 未开始 |
| **4. 提取 + 连图** | `extract.py --game gs2` 逐实体提；播种继承数据；跑 normalize→audit | ⬜ 未开始 |
| **5. 应用层** | 复用/扩展 codex 等（gs2 版或合并版） | ⬜ 远期 |

> 勾选用 ⬜/🔄/✅。每推进一块就回来改这张表 + §5 日志。

---

## 3. Raw 收集 + 标注规范（你的主战场）

目标：收集阶段就把「作者 / 这份强在哪 / 能喂给哪个实体」标清楚，让 gs2 比 gs1 更 organized。
这些标注最终会誊进 `gs2_schema.md` 的 Master Source IDs 表，是 `extract.py` 的输入。

**工作分工**：frontmatter **你收集时先手动加最小集**（id/author/url/type），
其余（`covers` 打标、`summary`）**我后面可代你补全**——我可以读完每篇后回填 `covers` 和一句话 `summary`。

**存放**：每个源存成 `raw/gs2/<描述性文件名>.md`（统一 `.md` 以便带 frontmatter；
extract.py 同时认 `.txt`/`.md`）。文件名建议 `<内容> - <作者>.md`，沿用 gs1 习惯。

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

**收齐后**：我会建一份 `docs/gs2/gs2_sources.md` 作总索引——把所有 raw 文件链在一起
（作者 / type / covers / 链接 / 指回相关 docs），给你一个一览 + 「formal project」的目录感。
（清单的空表头我先放在那个文件里，你可以边收边填。）

---

## 4. 待定决策（动手前再拍板，先不展开）

1. **半通用脚本怎么复用**：`links_normalize` / `links_audit` / `locations_refs` / `build_codex`
   现在 gs1 写死。走 (A) 参数化共用 还是 (B) fork 一份？倾向 A 但「等 gs2 实体定了再抽」。
2. **继承数据怎么播种**：哪些实体从 gs1 拷草稿（djinn/classes/equipment？），怎么标「继承 vs 待改」。
3. **schema 差异**：gs2 新增（队伍 Felix/Jenna/Sheba/Piers、transfer 机制、新 summon/地点/boss），
   哪些实体直接沿用 gs1 段、哪些要改。
4. **应用层**：gs2 单独出 codex，还是做成跨 game 的统一 app。

---

## 5. 进度日志

| 日期 | 进展 |
|---|---|
| 2026-06-17 | Kickoff：建 `raw/gs2` `data/gs2` `docs/gs2` 脚手架 + `schema/gs2_schema.md` 骨架 + 这份 meta plan。待用户 review/annotate。 |
