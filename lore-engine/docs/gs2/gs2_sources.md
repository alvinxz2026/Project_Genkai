# GS2 源索引（raw 收集清单 / source map 原料）

> 把 `raw/gs2/` 下所有源链在一起的总览。收一个登记一个。
> 这里的短 `source_id` + `covers` 最终会誊进 `schema/gs2_schema.md` 的
> **Master Source IDs** 表（`extract.py` 靠它把 source-id token-match 到 raw 文件名）。
>
> 标注分工：收集时手填 `source_id/author/url/type/quality`；`covers` + `summary`
> 读完 TOC 后补（见每篇 frontmatter）。词表与约定见 `docs/gs2/gs2_plan.md §3`。
>
> 版本/大小/年份取自 GameFAQs 目录页
> [`faq-index`](../../raw/gs2/Golden%20Sun%20The%20Lost%20Age%20–%20Guides%20and%20FAQs.md)。

---

## 已收集 — Full Game Guides（10 篇，均 `type: general`）

| source_id | 作者 | 版本/年份/大小 | quality | covers | 一句话 |
|---|---|---|---|---|---|
| [`telago`](../../raw/gs2/Guide%20and%20Walkthrough/Guide%20and%20Walkthrough%20by%20Telago.md) ⭐ | Telago | v1.95 / 2013 / 568KB | high | walkthrough · djinn · summons · classes · psynergy · equipment · items · monsters · bosses · locations · characters · transfer | **首选主源**：最全最新。全走法 + 附录A(djinn/原始+石板召唤/按元素职业&psynergy) + 附录B 全图表 + 4 副本 + Battle Arena + GS1 linkage。 |
| [`super-slash`](../../raw/gs2/Guide%20and%20Walkthrough/Guide%20and%20Walkthrough%20by%20Super_Slash.md) | Super_Slash | v1.0 / 2008 / 608KB | default | walkthrough · items · equipment · djinn · classes · psynergy · monsters · forging · mechanics · characters | 最长(22k 行)覆盖最全：完整 item/weapon/armor/accessory 表 + djinn + 职业 + forging + psynergy + enemy list。逐项数据最丰富。 |
| [`autocon`](../../raw/gs2/Guide%20and%20Walkthrough/Guide%20and%20Walkthrough%20by%20Autocon.md) | Autocon | v4.3.7 / 2007 / 536KB | default | walkthrough · djinn · summons · classes · psynergy · equipment · bosses · monsters · transfer · forging · locations · characters | 极全面：完整 djinn/summon(含新组合召唤) + 25 职业+psynergy + 终极装备与配装建议 + Sunshine 锻造 + 6 transfer 事件 + 18 boss + bestiary。 |
| [`shotgunnova`](../../raw/gs2/Guide%20and%20Walkthrough/Guide%20and%20Walkthrough%20by%20Shotgunnova.md) | Shotgunnova | 2009 / 389KB | default | walkthrough · mechanics · djinn · summons · psynergy · classes · equipment · shops · forging · transfer | 结构清晰、spoiler-free：附录 shop/equipment/djinn/psynergy/class 表 + forging/minigames + send option(transfer)。附录表很适合喂提取。 |
| [`cloud-blazer`](../../raw/gs2/Guide%20and%20Walkthrough/Guide%20and%20Walkthrough%20by%20Cloud_Blazer.md) | Cloud_Blazer | v4.0 / 2004 / 548KB | default | walkthrough · mechanics · characters · items · locations | 走法为主，区域覆盖极细(含大量 revisit)；basics 讲战斗/djinn 机制。实体数据表少。 |
| [`darthmarth`](../../raw/gs2/Guide%20and%20Walkthrough/Guide%20and%20Walkthrough%20by%20DarthMarth.md) | DarthMarth | v1.0 / 2006 / 419KB | default | walkthrough · characters · items · djinn · psynergy · classes · monsters | 完整走法 + Indexes：character、items/djinn/psynergy/class 表、bestiary。TOC 走法只列到 high-level。 |
| [`strawhat`](../../raw/gs2/Guide%20and%20Walkthrough/Guide%20and%20Walkthrough%20by%20strawhat.md) | strawhat | v1.0 / 2006 / 260KB | default | walkthrough · mechanics · characters · djinn · summons · psynergy · classes · items · equipment · forging · transfer | 中等体量覆盖全：走法 23 区 + sidequests(含 transfer) + djinn/summons/psynergy/classes + items/weapons/armor + forged items。 |
| [`ikillkenny`](../../raw/gs2/Guide%20and%20Walkthrough/Guide%20and%20Walkthrough%20by%20Ikillkenny.md) | Ikillkenny | v1.8 / 2003 / 324KB | default | walkthrough · bosses · mechanics | 走法完整(66 节到 Mars) + 12 boss + game basics。末尾 "English Section Ends Here"，疑似后段语言混排。无实体数据表。 |
| [`darkslime`](../../raw/gs2/Guide%20and%20Walkthrough/Guide%20and%20Walkthrough%20by%20Darkslime.md) | Darkslime | v0.2 / 2003 / 186KB | partial | walkthrough · characters · items · djinn · psynergy · classes · monsters | 未完成：走法只到 Osenia/Gondowan 开头；但 Indexes 有各表与 bestiary 起步。 |
| [`killerfusion`](../../raw/gs2/Guide%20and%20Walkthrough/Guide%20and%20Walkthrough%20by%20KillerFusion.md) | KillerFusion | v0.35 / 2003 / 118KB | partial | walkthrough · bosses · characters · djinn · items · equipment | 未完成：走法到 Apojii；boss 仅 4 个；有 djinn 列表/位置、item 与 artifact 装备表起步。 |

> ⭐ = 目录页 Most Recommended。

---

## 候选 / 未收集（来自目录页，按需补齐）

这些是 GameFAQs 上 GS2 的专项源。收哪个就把它移到上表，建 `raw/gs2/` 文件 + frontmatter。
**优先级建议**：写 schema 前，专项数据源往往比综合走法更干净、更适合做实体提取的主源。

### In-Depth Guides（专项，提取友好）
| 候选 source_id | 标题 / 作者 | 大概 covers |
|---|---|---|
| `terence` | Battle Mechanics by Terence (Highest Rated, 2003) | mechanics · classes · psynergy（gs1 同作者是职业需求权威源） |
| `torrentlord` | Enemy/Boss List by torrentlord (Highest Rated, 2022) | monsters · bosses |
| `ultimalink` | Character Class Guide by UltimaLink | classes |
| `aku-chi` | Class Setup Guide by aku_chi | classes |
| `android50` / `aspartate-djinn` | Djinn Guide by Android50 / aspartate | djinn |
| `demooni` | Djinni Stat Boosts Guide by Demooni | djinn |
| `aspartate-item` | Item Guide by aspartate | items · equipment |
| `mr-unorigino-item` | Item List by Mr_UnOrigino | items · equipment |
| `aspartate-forge` | Forged Items Guide by aspartate | forging · equipment |
| `bbbbrain2000` | Hidden Item & Best Item Guide by bbbbrain2000 | items · equipment |
| `yoyoyoshi` | Psynergy FAQ by YoyoYoshi | psynergy |
| `mr-unorigino-psy` | Psynergy List by Mr_UnOrigino | psynergy |
| `shotgunnova-shop` | Shop List by Shotgunnova | shops |
| `dbfire` | Summon Tablet/Sidequest Guide by DBFire | summons · locations（石板召唤获取） |
| `cooldude345` | Summons FAQ by cooldude345 | summons |
| `josher1212` | Reference Guide by josher1212 | mechanics（综合参考） |

### Maps and Charts
目录页有 ~60 张地图（多为 Alex_GER 2024 + Krac6 内部图等），偏视觉、`extract.py` 不易吃。
**暂不收**；若日后做 locations/地图层再单独评估。

---

## 关于"组合召唤 / 石板召唤"
GS2 新增的 stone-tablet / 组合召唤（Daedalus、Catastrophe、Charon、Iris 等）：
**数值**归 `summons` 实体；**石板/支线获取**归 `locations`/`walkthrough`。
主源参考：Telago 附录A "Additional Stone Tablet Summons"、Autocon §3.6、DBFire 的
Summon Tablet/Sidequest Guide（候选）。
