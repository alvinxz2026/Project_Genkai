# GS2 — 应用层方案（分阶段 · 收敛自 brainstrom 批注）

> **这份文档现在是什么**：brainstorm 一轮 + 你逐条批注后，我把它收敛成一条**分阶段路线**
> （Phase 1 quick win → 2 → 3 → 远期）+ 一轮**可行性讨论**。原始的想法编号（A1…G1）保留在
> §5 决策表里，连同你批注的要点，方便回溯。**下一步是讨论可行性、再定具体方案**，不是马上动手。
> 配套：数据现状 [`gs2_plan.md`](gs2_plan.md)（§5 backlog = 本文档 §6 会重排的对象）、
> 数据形状 [`gs2_er_sketch.md`](gs2_er_sketch.md)。
>
> 上一版（纯 brainstorm + 你的批注全文）在 git 历史里（commit 前一版）。

---

## 1. 从你的批注收敛出的几条定调

1. **受众**：先给你自己边打边用；跑顺了再考虑放给 GS2 社区。→ Phase 1–2 不为"公开"过度打磨。
2. **不强求"一个 app"**：可以是**几个共享同一份数据的交付物**——一个单机 HTML、一个
   NotebookLM/Project 形态的问答、一份中文攻略，彼此不冲突。这是本方案的架构基调（§2）。
3. **AI 层（F）走"丢进 NotebookLM / ChatGPT/Claude Project"路线**，不自建 RAG 引擎、不付运行时钱。
4. **从 quick win 起步**，先有个能用的东西，再往上 layer。
5. **中文**：应用 UI 的翻译靠后；但你**前期就想要一份中文 walkthrough**（只翻散文、名词留英文）
   方便阅读——这条被**提前**到 Phase 1 的并行交付。
6. **gs1 / 跨 game**：先不做，但**留数据接口**（实体页能挂两套数据即可）；而且 gs1 不一定要塞进同一个 app。

---

## 2. 架构：不是一个 app，是 3 个共享数据的交付物

你那句"这些不冲突、可以同时有好几个"是对的，工程上也更省。把它们拆开，各自用最省力的形态：

| 交付物 | 形态 | 解决什么 | 运行时成本 |
|---|---|---|---|
| **① The Codex**（主应用） | **单文件 HTML，数据内嵌**（沿用 gs1 codex 路线） | 边打边查：wiki / boss 卡 / 图鉴 / 锻造 / 进度追踪 | 0（纯前端，离线可用，可分享） |
| **② The Oracle**（问答） | 把 JSON + walkthrough md **丢进 NotebookLM 或一个 Claude/ChatGPT Project** | 自然语言问答，零自建 | 0（用你已有的订阅） |
| **③ 中文 Walkthrough** | `walkthrough_zh/` 一批 md（Gemini bulk 翻译，散文译、名词留英文） | 你自己看着舒服 | 0（一次性生成） |

**它们共享同一份 `data/gs2/*.json` + `walkthrough/*.md` 作 SSoT**——这正是前面所有数据工作的回报：
一份干净数据，喂三种消费方式。**主线工程量集中在 ①**；② ③ 基本是"导出/喂料"，几乎不写代码。

### 关于"单文件 HTML 装得下吗"（你的 Q4）
装得下。现在 `data/gs2` 全部 JSON ≈ **1.5 MB**，walkthrough 散文 ≈ 0.23 MB，合计 ~1.7 MB；
gs1 的 `gs1_codex.html` 已经内嵌数据、单文件 582 KB 跑得很顺。GS2 版大概 **2–3 MB 单文件**，
浏览器无压力（离线、双击即开、能直接发给别人）。**天花板**：等 gs1 也并进来、或散文再翻倍，
单文件会变笨重——那时再退一步改成"一个极小的本地静态站 + 按需加载 JSON"。**现在单文件是对的。**
（唯一坑：`file://` 下 `fetch` 会被 CORS 挡，所以数据必须**内嵌**而非 fetch——gs1 已经这么做了，照搬。）

---

## 3. 分阶段路线

> 原则：每个 Phase 结束都有**能用的东西**；后一个 Phase 在前一个的壳上 layer，不推倒重来。

### Phase 1 — 「The Codex」静态参考（quick win，1 个能用的单文件）
**目标**：打开就能查的 GS2 百科 + build，**零新数据**（现状数据已够）。

- **A1 Wiki**：每个实体有自己的页面；同类可共享一个列表页（"All Mace"式按类聚合）。
- **A1 交叉链接 / hover**：散文或卡片里提到某武器/Djinn/Psynergy，**鼠标悬停看属性 tooltip，点击进入该（类）页面**。这是贯穿全 app 的连接层。
- **build planner**：移植 gs1 的 `build_codex.py` → `build_codex_gs2.py`，喂 gs2 的职业/djinn。
- **D1 Boss 备战卡**：数值 + 弱点 + 推荐等级 + **现成的 strategy prose**（不自造判断层，直接用从源里提取的）。
- **D2 图鉴/掉落**：monsters + drops + `found[]` 反向索引。
- **C3 锻造规划**：材料 → 锻造件 → 哪里掉（数据现成，最简单）。
- **E1 Source Inspector**：每条数值旁小角标，点开看"哪些源贡献了它 / 有无 conflict"。贯穿所有 view，几乎零数据成本。
- **A2 预留接口**：实体页的数据结构留一个"可挂第二套数据（gs1）"的位，但 Phase 1 不填。

**Codex polish backlog（已交付连接层后的小优化，记一笔、后面再做、不急）**：
- **列表列 + 排序**：现在左侧列表只有名字。给「长列表型」实体在列表里直接带**关键列**并可**排序**——
  例：summons 列出 `djinn_required`（含 combo 配方）、equipment 列出关键数值（ATK/DEF/buy 等）。
  让你在不点开 detail 的情况下就能横向比较 + 按数值排序。（已有 facet 过滤；这是过滤之上的"列+排序"层。）
- 候选延伸：列表按 facet 值**分组**显示子标题；detail 里数值表也可排序。

**并行 quick win（不占主线、可同时做）**：
- **② Oracle 起步**：把 `data/gs2/*.json` + `walkthrough/*.md` 丢进 NotebookLM / 一个 Project，立刻能问答。先验证够不够用，再决定要不要做 F2 门控。
- **③ 中文 walkthrough**：Gemini bulk 翻 `walkthrough/` 散文（名词留英文）→ `walkthrough_zh/`。
- **F3 离线生成卡片**（可选）：每 region 一张 TL;DR、boss 策略浓缩，一次性生成、烘进 ①。

### Phase 2 — 「The Companion」进度感（挂上 62-region 脊柱）
**目标**：把 ① 从"静态百科"升级成"随你推进而变化的伴随物"。差异化最强的一层。

- **B1 攻略阅读器**：电子书式，左 62-region 目录、右散文，正文实体名全是活链接接回 ① 的 wiki。
  **加可选的 spoiler 门控**："我打到第 N 区"→ 后面默认折叠防剧透。
- **B2 Missable / 收集追踪器** ← **杀手锏**：每区 front-matter 已结构化"这里有什么可拿"。
  做成 **collection checklist + localStorage 持久化**（类似 BotW/TotK 的 tracker），关键是**离场提醒**：
  "你要离开 Yampi Desert 了，Sand djinn / 某支线还没做——回不来了，确认？"
- **C2 "我现在能变成什么"**：在 region N、按正典顺序你大概有哪些 djinn → 列出**此刻可达**的职业/召唤。
  **只给可能性、不给最优解**（所以不难，见 §4）。

### Phase 3 — 深化 / 半公开
- **E2 冲突仪表盘 + resolution 回收**：把 cross-check findings 做成可浏览视图；页面底部一个评论框，
  点一下**导出/复制成 txt**（单文件 HTML 不能静默写盘，用"下载 txt / 复制到剪贴板"实现），
  你按游戏真实数据 resolve、把 txt 汇总给我，我回去更新 SSoT。
- **A2 跨 game 数据槽落地**：实体页真正挂上 gs1 的第二套数据（接口 Phase 1 已留）。
- **C4 伤害/对战计算器**：boss 的 elemental_power/resistance × 你的 psynergy/summon。
- 若要放给社区：UI 打磨 + 移动端。

### 远期（看情况，不承诺）
- **C1 Djinn 全局最优求解器**：暂缓——见 §4 的可行性判断（你也质疑了，我同意）。
- **B3 完美通关路线规划**：需要把散文里的**前置条件**结构化；现在**顺带**能提的先提（§6），算法靠后。
- **F1/F2 自建 RAG / 门控 AI**：只有当 NotebookLM 路线明显不够用时才考虑。
- **G1 通用多 game 壳 / infra 收敛**：gs1≈gs2 高度相似，等真有第三套语料再抽公共层。

---

## 4. 可行性讨论（逐条，含我对你几个疑问的判断）

| 特性 | 难度 | 数据就绪 | 我的判断 |
|---|---|---|---|
| A1 wiki + hover/click | 低–中 | ✅ | 标准前端活；tooltip 直接读内嵌 JSON。**核心连接层，值得先打好。** |
| build planner 移植 | 中 | ✅ | gs1 已有壳，主要成本是 gs2 数据形状对接（classes 结构有差异）。 |
| D1 boss 卡 | 低 | ✅ | strategy 已在 `bosses.json`。**同意你**：用现成 prose，不自造判断层。 |
| D2 图鉴 / C3 锻造 | 低 | ✅ | 都是查表 + 反向索引，最快出活。 |
| E1 source inspector | 低 | ✅ | `sources[]` 每条都在，纯展示。 |
| B1 阅读器 + 门控 | 中 | ✅ | 门控 = 一个"当前进度"选择器过滤 region + 折叠后文，`order` 字段现成。 |
| **B2 tracker** | 中 | ✅(基本) | front-matter 的 items/chests/djinn 已结构化够做 checklist；**"支线/不可逆提醒"有一部分埋在散文里、未完全结构化**——需要一轮轻量 missable 标注（§6）。 |
| C2 "能变成什么" | 中 | 🔸 | **可行，且不难**——正如你说，只枚举**可能性**不求最优：给定按区可得的 djinn 数（按元素），过滤出满足 `element_requirements` 的职业即可。需要一张"djinn→可得区"映射（可从 `location.area` + region order 物化）。 |
| **C1 全局最优求解** | 高 | 🔸 | **同意你的质疑，建议远期/不做**。难点不在算法，在**目标没法定义**：summon 流 vs 物理流 vs 辅助流，最优解不同；djinn 全队共享是约束满足，但"最优"是多目标且主观。做成"求解器"会假装客观、实则误导。**正确形态是 C2 的扩展**——"给我所有让 Felix 上 X 职业的合法 djinn 分配"（枚举可行解，不排名），把"哪个更好"留给你判断。 |
| C4 伤害计算 | 中 | ✅ | 数据够；Phase 3，不急。 |
| E2 仪表盘 + resolution | 中 | 🔸 | findings 需先结构化成可浏览数据；resolution 回收用"下载 txt/复制"绕开单文件写盘限制——**完全可行，且很轻**。 |
| ② NotebookLM 问答 | **极低** | ✅ | **强烈推荐先试**。把 JSON + walkthrough md 当 source 丢进去就能用、免费、零代码。回答你的 Q3：这条路成立，够用就不必自建 F1。**唯一注意**：NotebookLM 对结构化 JSON 的"推理"弱于对散文的检索，所以**问答体验主要吃 walkthrough 散文 + boss strategy**；纯数值类查询（"这把武器攻击多少"）还是 ① 的 wiki 更准。两者互补。 |
| ③ 中文翻译 | 低 | ✅ | Gemini bulk，散文译、名词留英文；一次性。可提前。 |
| F3 离线生成卡 | 低 | ✅ | 一次性 LLM pass → 烘进 ①，零运行时。 |
| A2 跨 game 数据槽 | 低(留口)/中(落地) | ✅ | Phase 1 只留结构位很便宜；真正挂两套数据放 Phase 3。 |

**一句话可行性结论**：Phase 1 全部是"数据已就绪的查表/展示活"，无技术风险，**quick win 成立**。
Phase 2 的 B2 是最有价值也最值得投入的一块，唯一需要补的是一轮轻量 missable 标注。C1 是唯一
我建议主动砍/降级的——它看着酷但目标不可定义，C2 才是对的形态。

---

## 5. 想法决策表（保留原编号 + 你的批注要点）

| 编号 | 想法 | 决定 | 你批注的要点 |
|---|---|---|---|
| A1 | Wiki + build_codex + hover/click | **Phase 1 核心** | 每个东西有独立页（同类可共享如 All Mace）；要 hover 看属性、点击进页 |
| A2 | 跨 game 合并 | **Phase 1 留接口 / Phase 3 落地** | 优先级不高；只要实体页能挂两套数据即可 |
| B1 | 进度门控攻略阅读器 | **Phase 2** | 本想要电子书式；门控想法有趣，愿意试 |
| B2 | Missable / 收集追踪 | **Phase 2 杀手锏** | 一定要有；要"提醒"+ collection checklist（仿 BotW/TotK tracker） |
| B3 | 完美通关路线规划 | **远期**（现在顺带提前置数据） | 优先低；可提取的前置信息顺带提 |
| C1 | Djinn 全局最优求解 | **降级/远期** | 你质疑组合太多、目标不一；我同意 → 改成 C2 形态 |
| C2 | "现在能变成什么" | **Phase 2** | 只给可能性不求最优 → 可行 |
| C3 | 锻造规划 | **Phase 1** | 应该很简单 |
| C4 | 伤害/对战计算 | **Phase 3** | 不放 Phase 1 |
| D1 | Boss 备战卡 | **Phase 1** | 用现成 prose，不自造判断层 |
| D2 | 图鉴/掉落 | **Phase 1**（基础） | 基础功能 |
| E1 | Source Inspector | **Phase 1**（贯穿层） | 想要 |
| E2 | 冲突仪表盘 + resolution 回收 | **Phase 3** | 要能 submit resolution（评论框→存 txt→汇总给你更新） |
| F1 | 自建可溯源 RAG | **远期/可能不做** | 倾向丢 NotebookLM/Project 就好 |
| F2 | 进度门控 AI 伴随 | **远期** | 非刚需，玩过这游戏 |
| F3 | 离线生成内容 | **Phase 1 quick win** | 当 quick win |
| G1 | 通用多 game 壳 | **远期** | gs1≈gs2 很像；后面收敛出 infra |
| ②  | NotebookLM/Project 问答 | **Phase 1 并行** | 丢进去就能用、不额外花钱 |
| ③  | 中文 walkthrough | **Phase 1 并行（提前）** | 前期就想要，散文译、名词留英文 |

---

## 6. 对数据 backlog 的影响（重排 [`gs2_plan.md`](gs2_plan.md) §5 D 类）

选了"Phase 1 静态 + Phase 2 进度感、C1 降级"之后，D 类的排期变清楚了：

- **提前做（Phase 1 并行）**：
  - **2b 中文翻译**（散文译、名词留英文）——你前期阅读刚需，从"看 app 方向"升级为**现在排**。
- **Phase 2 之前做（轻量新提取）**：
  - **Missable / 不可逆事件标注**：扫 walkthrough 散文，把"离开前必须拿/做"的点结构化进每个 region
    （front-matter 已覆盖 items/chests/djinn，缺的是**支线 & 时序不可逆**标记）。B2 需要，B3 也复用。
- **可继续推迟（这些方向都没进近期 Phase）**：
  - **classes ACR / djinn-combo 范围补全**：只有 **C1 求解器**才真需要，而 C1 已降级 → **可继续 defer**。
  - C2 只需"djinn→可得区"映射，从现有 `location.area` 物化即可，不需 ACR。
- **可选增益**：
  - 多提一些 **strategy prose**（你提到还有很多没提）→ 同时喂肥 D1 boss 卡 和 ② NotebookLM 的问答质量。

> 净结论：近期数据活只有两件——**中文翻译**（提前）+ **missable 标注**（Phase 2 前）；
> ACR 那类重活继续躺 backlog。

---

## 7. 还想跟你确认的（讨论用，不阻塞）

1. **Phase 1 的 MVP 切片**：是先把 wiki+交叉链接+source inspector 这条"连接层"打通（最能体现差异化），
   还是先把 boss 卡/图鉴/锻造这些"独立查表页"快速铺满给你即时可用？（我倾向先连接层，但听你的。）
2. **build planner**：直接照搬 gs1 的视觉/交互，还是借这次重做一版？（照搬最快。）
3. **② NotebookLM**：要不要我**现在就先把喂料整理好**（一个 `export/` 把 JSON + walkthrough 拼成
   适合丢进去的格式），让你这两天就能先用上问答？这是真正的零成本最快 quick win。
4. **③ 中文翻译**：现在就开 Gemini bulk 跑 `walkthrough_zh/`？（独立、不阻塞 app。）

> **下一步**：你看这版分阶段 + 可行性，回我上面 4 个确认点（或直接改本文档）→ 我们锁 Phase 1 的
> MVP 切片 → 我开始落地。
