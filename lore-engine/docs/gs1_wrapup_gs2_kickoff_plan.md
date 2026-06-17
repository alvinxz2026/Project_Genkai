# GS1 收尾 + GS2 启动 — 计划（待你 review / annotate）

> 回应 `docs/scratch.md`。结构：先把你问的几个**核心决策**给出我的推荐（你来拍板），
> 再展开 GS1 收尾、GS2 启动两块的**具体动作**，最后给一个**执行顺序**。
> 每个需要你拍板的地方都标了 **【待拍板】**，方便你直接在下面批注。

---

## Part 0 — 先回答你 scratch 里的三个核心问题

### Q1. GS2 在同一个 folder 里做，还是新开 folder？
**推荐：就在 `lore-engine/` 里继续，按 `{game}` 分目录。** 不新开 repo / folder。

理由：lore-engine 从 inception 起就是**「换语料 + 换 schema，同一套管线」**的设计，目录早就按
`raw/{game}/`、`data/{game}/`、`schema/{game}_schema.md` 命名空间分好了。GS2 = 加一个 `gs2`
命名空间，正好是对「这套管线可泛化」这个论点的第一次真实验证（也就是 application_ideas 里的 **F 元目标**）。
新开 folder 反而割裂了「同一管线两套语料」的证据。

→ GS2 落点：`raw/gs2/`、`data/gs2/`、`schema/gs2_schema.md`、`tools/gs2_*.html`。

**【待拍板】** 同意「同 folder + gs2 命名空间」？还是你想把 lore-engine 抽成独立 repo 再说？

> 嗯同folder, 你后面去gs2的那些folder建好。那么现存gs1这些是不是也要额外建folder？

---

### Q2. 有哪些东西能直接 port over？（这是我实际查过代码后的结论，不是乐观估计）

我把 `scripts/` 分成三类：

| 类别 | 脚本 | port 现状 |
|---|---|---|
| **真·通用（已参数化）** | `extract.py` | ✅ 直接可用。`--game gs2` 就跑，零改动。它读 schema、token-match raw 文件名，全是数据驱动的。 |
| **半通用（逻辑通用但 gs1 写死）** | `links_normalize.py`、`links_audit.py`、`locations_refs.py`、`build_codex.py` | ⚠️ 这些都硬编码了 `DATA = ROOT/"data"/"gs1"`，而且内含 gs1 专属逻辑（djinn 元素别名表、`reachable_in_gs1`、codex 的实体渲染 JS）。**不能裸 port**，要么参数化、要么 fork 一份改。 |
| **gs1 一次性脚本（已完成使命）** | `*_supplement.py`、`*_apply.py`（8 个）、`monsters_extract.py`、`shops_extract.py`、`build_terence_class_reqs.py`、`build_planner.py`（已被 codex 取代）、`scraper.py`（空壳） | 🗄️ 不 port。它们是 gs1 建数据时的一次性迁移/补洞脚本，价值是「记录数据怎么来的」，应归档，不带进 gs2。 |

**由此引出一个真正的架构决策 ——【待拍板】**：半通用脚本，走哪条路？
- **(A) 参数化**：把 `DATA = .../gs1` 改成 `--game` 参数，gs1/gs2 共用一份脚本。
  好处：真正「一套管线」；坏处：得把 gs1 专属逻辑（元素别名、reachable 规则）抽成每个 game 的配置。
- **(B) fork**：`links_normalize.py` → 复制成 gs2 版各自改。
  好处：快、互不干扰；坏处：背离「可泛化管线」的项目论点，逻辑改一处要改两处。
- **我的倾向：extract.py 已经是 (A) 的样板，半通用脚本也走 (A)**，但**不要现在就抽**——
  等 gs2 schema 定了、知道 gs2 实体长什么样，再「按需参数化」（先量化再改源的同款心法）。
  也就是：gs2 启动初期可以先 fork 跑通，跑通后再回头把两边合并成参数化版。

> 这个我听你的。比较technical我不懂。主要是也不知道gs2的那些长什么样，还不确定是不是真的通用。

---

### Q3. raw 先收集好 + 做轻量标注（frontmatter）再开做 —— 这个思路对吗？
**完全对，而且正好接上现有管线的一个真实接口。** 你直觉里的「作者 / 内容大概相关什么」这些标注，
其实就是 schema 里 **`### Master Source IDs` 表**要的东西 —— `extract.py` 靠它把 source-id
token-match 到 raw 文件名。你把标注前置到 raw 文件里，等于**提前把这张表的原料准备好了**，
到时候誊进 schema 即可。这会让 gs2 比 gs1 更 organized（gs1 是边做边补这张表的）。

我建议的 raw 标注规范（每个源文件顶部加 frontmatter；纯文本 .txt 不好带 frontmatter，
所以**统一存成 `.md`**，extract.py 已经同时认 `.txt`/`.md`）：

```markdown
---
source_id: telago            # 短 id，将誊进 schema 的 Master Source IDs；用 -/_ 分词以便文件名匹配
author: Telago
url: https://gamefaqs.gamespot.com/...
type: walkthrough | faq | data-table | mechanics   # 大类
covers: [djinn, classes, psynergy]                 # 这个源对哪些实体有用（指导 extract 该喂给谁）
quality: high | medium | partial                   # 主观可信度
gs1_counterpart: "Djinn Class Items Phynergy - Telago.txt"  # 若同作者也写过 gs1，标一下，方便对照
notes: 一句话：这份强在哪、坑在哪
---

<原文照抄，不改正文>
```

好处：① 收集阶段就逼自己想清楚每个源「能喂给哪个实体」；② 给你想要的
**idea→design→plan→execution** 仪式感一个落点 —— 见 Part 2.4。

**【待拍板】** 这个 frontmatter 字段集合够用吗？要加/减字段吗？

> 大致可以。按你建议。  
> Frontmatter想说的是type里面，有些source文档，里面啥都有，需要个catch-all的类型。这种我可能会拆可能不会拆。  
> 然后quality，我可能也不知道是high还是medium，可以给个default之类的。  
> 我觉得我raw收集完之后，可以先让你做个大的目录文件或者index之类的，这样这些markdown文档就被link在一起，目录里面你是不是还可以直接link到这些文档之类的。  
> Cover也是，我可以手动tag，但是如果后面很多，可能也会让你来tag。可以和下面这一步一起。  
> gs2里面我想要个project-level的plan+tracking的文档，这样每做一些，也可以去里面更新。文档本身的plan也可以根据实际的进展来iterate/adjust, 一开始很high-level就行不需要很细，能明白我意思么，因为有些东西做着做着可能又会有新的想法，有些执行层面的东西做着做着会改变方法之类的。但还是想要个meta的东西来track。  
> 就是这个frontmatter我先手动加，然后你后面可能可以来完善。甚至可以读了一个文档加个summary在frontmatter里面，这会是个好主意么？  


---

## Part 1 — GS1 收尾

> 目标：把 gs1 留成一个**干净、可复述、可当 gs2 样板**的里程碑，然后打一个 commit 封存。

### 1A. 清理临时 / 调试文件
我实际扫过，**好消息是脏东西不多**：
- ✅ `_raw_response.txt`、`_batch_*.md` —— 没有残留（已清干净）。
- ✅ `scripts/__pycache__/` —— 已被 `.gitignore` 忽略，没进版本库；本地删不删都行。
- ⚠️ **进度追踪文件**（已 commit 进库）：`data/gs1/classes_psynergy_progress.md`、
  `data/gs1/gs1_maps_progress.md`。这俩是建数据时的临时 todo，数据做完后是死文档。
  **【待拍板】** 删掉？还是挪进 `docs/` 当历史记录留存？
> 留着吧当个记录。
- ⚠️ `data/gs1/scratch.md` 不存在，但 `docs/scratch.md`（就是你写想法这份）已被 track。
  收尾时这份内容会被本计划替代 —— **【待拍板】** scratch.md 留着当草稿区，还是清空/删除？
> 这个放草稿区，经常用的。
- ⚠️ `scripts/scraper.py` —— 0 字节空壳，从没用过（raw 是手工收集的）。建议删，或留作 gs2 的占位。
> ok。

### 1B. 归档 gs1 一次性脚本
把 Part 0/Q2 第三类（8 个 `*_supplement/_apply` + `monsters_extract`、`shops_extract`、
`build_terence_class_reqs`、`build_planner`）**移到 `scripts/gs1/`**（或 `scripts/archive/gs1/`）。
通用 + 半通用脚本留在 `scripts/` 顶层。这样「哪些是管线、哪些是 gs1 一次性活」一眼分明，
也直接回答了「gs2 该 port 什么」。
**注意**：移动后要同步改 CLAUDE.md 里的脚本路径引用。
**【待拍板】** 用 `scripts/gs1/` 还是 `scripts/archive/`？
> 听你的。

### 1C. 被取代的旧工具
application_ideas 里已写明：统一 app `gs1_codex.html` 取代了三个旧工具
（`gs1_class_explorer.html`、`gs1_equipment_explorer.html`、`gs1_build_planner.html`）+ `build_planner.py`，
「旧文件保留待确认后删」。**现在就是那个确认点。**
**【待拍板】** 删这 3 个旧 html + `build_planner.py`？（codex 已完全覆盖其功能。）
> 旧的留着吧，archive之类的，留个记录？

### 1D. 文档更新
- **`lore-engine/README.md` 当前是 0 字节空文件。** 这是收尾最该补的一块。建议内容（精简）：
  项目一句话定位 → 管线图（inception 里那张）→ 目录说明 → 怎么跑 extract → gs1 现状
  （11 实体 + FK 连图 + codex app，给个数字快照）→ 指向 docs/ 里的深入文档。
- **根 `README.md`**（123 字节）：补一句 monorepo 说明 + 指向 lore-engine。
- **`CLAUDE.md`**：基本准确，但收尾后要同步：① 若 1B 移动了脚本，改路径；
  ② 补一句 codex app 取代旧 explorer；③ 若确立 gs2 命名空间约定，写进去。
- **inception 文档的 Status Log**：补一行「gs1 prototype 完成」的里程碑，日期 2026-06-17。
> 听你的。

### 1E. （可选）docs 分层
现在 `docs/` 把项目级文档（inception、data_management_notes、application_ideas）和
gs1 专属计划（各种 `gs1_*_plan.md`）混在一起。gs2 一来会更乱。
**建议**：`docs/gs1/` 收 gs1 专属计划，`docs/` 顶层只留项目级 + 跨 game 的。
**【待拍板】** 现在就分，还是等 gs2 真开始再分？（我倾向现在分，趁文件还少。）
> 可以现在就分。这个和Q1里面的有关系么？folder那些？

### 1F. 封存 commit
以上做完，打一个 commit：`chore(gs1): wrap up gs1 prototype — cleanup, archive one-shots, README`。
gs1 成为一个干净的 baseline。
> ok。到这里停下来，我commit一轮。

---

## Part 2 — GS2 启动

顺序原则：**先搭脚手架和约定 → 你收集+标注 raw → 写 schema → 跑提取**。
即 idea→design→plan→execution。raw 收集是你的活，其余我可以代劳。

> 我上面frontmatter那里提到了一些，你整合一下。

### 2.1 建命名空间脚手架
`raw/gs2/`、`data/gs2/`、`schema/gs2_schema.md`（先放空/骨架）、docs 里建 gs2 计划文档。
> 参考上面的。文件夹你可以先建起来，然后放那个meta的plan。我后面再去review/annotate一下。gs2先不讨论细节了，感觉可以后面再讨论？

### 2.2 决定半通用脚本走 (A) 还是 (B)（见 Q2）—— 这步是 design，不是马上写码。

### 2.3 从 gs1「播种」继承数据
GS2 在剧情/机制上继承 gs1：四名 gs1 Adept（Isaac/Garet/Ivan/Mia）在 gs2 后期回归、
Djinn 体系延续、不少 item/equipment 复现。所以**不是「共享同一张表」，而是「拿 gs1 版当种子草稿，再 diff 扩展」**：
- 可播种：`djinn`（gs2 新增大量，但 gs1 的 28 个机制相同）、`classes`、部分 `items/equipment`。
- 全新：gs2 自己的队伍（Felix/Jenna/Sheba/Piers）、传输（transfer）机制、新地点/boss/summon。
- 做法：`cp data/gs1/djinn.json data/gs2/djinn.json` 当起点，标注哪些是继承、哪些待改。
  **守住原则**：gs1 和 gs2 是**两份独立真相源**，不要让 gs2 去 import gs1（版本会打架）。
**【待拍板】** 同意「播种 + diff」而非「共享表」？

### 2.4 raw 收集 + 标注（你的主战场 → 给你 idea-design-plan-execution 的仪式感）
这一步正好满足你「想要更 formal、像个 project」的诉求。我建议把它做成一份**清单驱动**的过程：
1. 在 `docs/gs2/gs2_sources.md` 建一张**收集清单**：列出打算收哪些 GameFAQs 源（作者、链接、覆盖实体），
   收一个勾一个 —— 这就是 gs2 的「design / plan」可见产物。
2. 每个源落到 `raw/gs2/<描述性文件名>.md`，顶部按 Q3 的 frontmatter 标注。
3. 收齐后，把每个 `source_id` 誊进 `schema/gs2_schema.md` 的 Master Source IDs 表。

### 2.5 写 gs2 schema
以 `gs1_schema.md` 为模板，逐实体改。这步决定 extract 提什么。可以先 `--dry-run` 验证
源文件解析正确，再花 API 钱。

### 2.6 跑提取
`python scripts/extract.py --entity <e> --game gs2`，逐实体提，沿用 gs1 的「冲突标记不静默合并」铁律。
之后视 2.2 的决定，跑（或先 fork 出）links_normalize → links_audit → build_codex。

> 2.3-2.6是不是可以后面再讨论？

---

## Part 3 — 推荐执行顺序（一条线）

**先全部收尾 gs1，再碰 gs2** —— 别在脏状态上分叉。

```
【GS1 收尾】
 1. 清理临时文件 + 决定 progress/scratch 去留        (1A)
 2. 归档 gs1 一次性脚本到 scripts/gs1/               (1B)  ← 同步改 CLAUDE.md
 3. 删被取代的旧 html + build_planner.py             (1C)
 4. （可选）docs 分层 docs/gs1/                       (1E)
 5. 写 README（lore-engine + 根）+ 更新 CLAUDE.md     (1D)
 6. commit 封存 gs1 baseline                          (1F)
────────────────────────────────────────────────
【GS2 启动】
 7. 建 gs2 命名空间脚手架                              (2.1)
 8. 定半通用脚本 (A)参数化 / (B)fork                   (2.2 / Q2)
 9. 播种继承数据 cp gs1→gs2 草稿                       (2.3)
10. 【你】建 gs2_sources 清单 → 收集 raw → 加 frontmatter (2.4)
11. 写 gs2_schema.md（含 Master Source IDs 表）         (2.5)
12. dry-run 验证 → 逐实体 extract → normalize→audit→codex (2.6)
─── 然后你就可以一边打 gs2 一边用了 ───
```

我能代劳的：1–9、11、12 的脚本面。**第 10 步（收集 + 标注 raw）是你的核心手工活**，
也是你最想要的「formal project」体验所在。

> 这一步，你可以把7也做了吗？加上那个全局的project plan文档，以及一个markdown template，带frontmatter的，这样我的raw我直接复制template，然后简单填frontmatter，然后正文贴下面（我到时候看是我自己来简单加正文格式，还是也交给你来做）

---

## 给你拍板的开放问题汇总（可直接在此批注）

1. **Q1** 同 folder + gs2 命名空间？还是抽独立 repo？
2. **Q2** 半通用脚本走 (A) 参数化 还是 (B) fork？（我倾向 A，但晚点抽）
3. **Q3** raw frontmatter 字段集合够用吗？
4. **1A** `*_progress.md` 删还是挪 docs？`scratch.md` / `scraper.py` 去留？
5. **1B** 归档目录叫 `scripts/gs1/` 还是 `scripts/archive/`？
6. **1C** 现在删 3 个旧 html + `build_planner.py`？
7. **1E** docs 现在分层还是等 gs2？
8. **2.3** 继承数据用「播种 + diff」？
9. 还有没有我没覆盖到的收尾项 / 你更想先做的？
10. **walkthrough 变体**：`data/gs1/` 有 4 份走法（EN/CN × 普通/fable），gs2 也要全做吗？还是先做一份？
> 这部分直接看我上面回答吧。