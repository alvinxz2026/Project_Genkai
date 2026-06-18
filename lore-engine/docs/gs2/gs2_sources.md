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

## 已收集 — In-Depth Guides（32 篇）

专项指南，全部存于 `raw/gs2/In-Depth Guides/`。frontmatter 已补全（短 `source_id` /
`type` / `covers` / `quality` / `summary`）。按**提取价值**分四组，便于写 schema 与
extraction plan。`covers` 词表在 gs1 11 实体 + walkthrough/transfer/forging/mechanics
基础上，本批新增 4 个 tag：`story`（剧本/对白）、`music`、`glitch`、`ids`（hex/内存码，可做
canonical id 与完整性校验）。

### A. 数据型 / 提取主源（写 schema + 提取的首选原料）
| source_id | 作者 | type | quality | covers | 一句话 |
|---|---|---|---|---|---|
| [`torrentlord`](../../raw/gs2/In-Depth%20Guides/Enemy%20and%20Boss%20List%20by%20torrentlord.md) ⭐ | torrentlord | data-table | high | monsters · bosses · locations · items | Highest Rated 敌人数据库：每只 HP/PP/Att/Def/Agil/Luck/turns + 四元素 power&resist + abilities + reward(掉落含 ICC) + location。monsters/bosses 首选。 |
| [`mr-unorigino-item`](../../raw/gs2/In-Depth%20Guides/Item%20List%20by%20Mr_UnOrigino.md) | Mr_UnOrigino | data-table | high | equipment · items | 极整齐全 item 表，GS1 与 TLA 分列（武器/防具/饰品/artifact/rusty/blacksmith/class items）。equipment/items 主源之一。 |
| [`ultimalink`](../../raw/gs2/In-Depth%20Guides/Character%20Class%20Guide%20by%20UltimaLink.md) | UltimaLink | data-table | high | classes · psynergy | 按 8 角色列各职业链 HP/PP/ATK/DEF/AGL/LUCK 增减% + 所需 djinn 数 + psynergy 习得等级。classes 干净主源。 |
| [`shotgunnova-shop`](../../raw/gs2/In-Depth%20Guides/Shop%20List%20by%20Shotgunnova.md) | Shotgunnova | data-table | high | shops · equipment · items · locations | 15 城镇商店清单，把 location 与 equipment/item 链起来。shops 主源。 |
| [`yoyoyoshi`](../../raw/gs2/In-Depth%20Guides/Psynergy%20FAQ%20by%20YoyoYoshi.md) | YoyoYoshi | faq | high | psynergy · classes · djinn · mechanics | 近期更新、覆盖全：psynergy 机制 + 职业关系 + 分类/最佳 + 全列表（按元素）。psynergy 主源。 |
| [`terence`](../../raw/gs2/In-Depth%20Guides/Battle%20Mechanics%20by%20Terence.md) ⭐ | Terence | mechanics | high | mechanics · classes · psynergy · djinn · summons · equipment · forging | Highest Rated 战斗机制权威源（职业需求/加成、伤害公式、解放、djinn/summon 机制）。偏机制非数值。gs1 同作者。 |
| [`dbfire`](../../raw/gs2/In-Depth%20Guides/Summon%20Tablet%20and%20Sidequest%20Guide%20by%20DBFire.md) | DBFire | faq | high | summons · locations · transfer · walkthrough | 召唤石板获取 + 8 大支线 + 4 transfer 事件。石板召唤获取核心源，惜全文本。 |
| [`mr-unorigino-psy`](../../raw/gs2/In-Depth%20Guides/Psynergy%20List%20by%20Mr_UnOrigino.md) | Mr_UnOrigino | data-table | default | psynergy | 全 psynergy 列表（按元素 + puzzle/dummied）。日文乱码；适合 completeness 校验。 |
| [`demooni`](../../raw/gs2/In-Depth%20Guides/Djinni%20Stat%20Boosts%20Guide%20by%20Demooni.md) | Demooni | data-table | default | djinn · locations | 每颗 djinn 属性加成 + 获取位置。djinn 数值辅源。 |
| [`cooldude345`](../../raw/gs2/In-Depth%20Guides/Summons%20FAQ%20by%20cooldude345.md) | cooldude345 | faq | default | summons · djinn | Anemos Sanctum 找法 + summons 用法 + summon 数值（引自 Terrence Fergusson）。summons 辅源。 |
| [`aspartate-item`](../../raw/gs2/In-Depth%20Guides/Item%20Guide%20by%20aspartate.md) | aspartate | faq | default | equipment · items · forging | 武器/防具/饰品/道具分类讲解（数据+定性）+ 最佳/锻造/稀有掉落 mini guide。 |
| [`aspartate-djinn`](../../raw/gs2/In-Depth%20Guides/Djinn%20Guide%20by%20aspartate.md) | aspartate | faq | default | djinn · locations · transfer | djinn 获取（按顺序 + 按元素），标出不靠 transfer 即可拿的。比 Android50 详细。 |
| [`aspartate-forge`](../../raw/gs2/In-Depth%20Guides/Forged%20Items%20Guide%20by%20aspartate.md) | aspartate | faq | default | forging · equipment · items · monsters | Sunshine 锻造：各材料可锻装备、锈蚀武器、产材料的怪。forging 辅源。 |
| [`android50`](../../raw/gs2/In-Depth%20Guides/Djinn%20Guide%20by%20Android50.md) | Android50 | faq | default | djinn · locations | 按元素列 djinn 获取位置（本质 location 列表），无数值。 |
| [`aku-chi`](../../raw/gs2/In-Depth%20Guides/Class%20Setup%20Guide%20by%20aku_chi.md) | aku_chi | faq | default | classes · psynergy · bosses · mechanics | 职业系统 + 各组合配装策略 + link battle + 重要 boss；含 psynergy board。gs1 同作者。 |
| [`bbbbrain2000`](../../raw/gs2/In-Depth%20Guides/Hidden%20Item%20%26%20Best%20Item%20Guide%20by%20bbbbrain2000.md) | bbbbrain2000 | walkthrough | default | items · equipment · locations | 按地点列隐藏/最佳物品获取。items/equipment 的 location 辅源。 |

### B. 策略 / 攻略向（应用层素材，非一手数值）
| source_id | 作者 | type | quality | covers | 一句话 |
|---|---|---|---|---|---|
| [`link-kirby-boss`](../../raw/gs2/In-Depth%20Guides/Boss%20Guide%20by%20Link_Kirby.md) | Link_Kirby | walkthrough | default | bosses | 全 required boss + 4 石板守护者打法；含锻 Excalibur 法、无召唤策略。纯文本。 |
| [`goldmario-boss`](../../raw/gs2/In-Depth%20Guides/Boss%20Guide%20by%20goldmario.md) | goldmario | walkthrough | default | bosses | boss 打法（主线 + 4 石板 boss），偏文字、不算详细。 |
| [`rena-chan-hardboss`](../../raw/gs2/In-Depth%20Guides/Hard%20Mode%20Boss%20Guide%20by%20Rena_Chan.md) | Rena_Chan | faq | default | bosses · djinn | Hard Mode boss 打法 + 各元素 djinn 分析。偏应用层（基础数据后叠加）。 |
| [`astralfire`](../../raw/gs2/In-Depth%20Guides/Competitive%20Battling%20Guide%20by%20AstralFire.md) | AstralFire | faq | default | classes · equipment · djinn · summons · mechanics | PvP/对战向：选职业、装备、djinn、召唤、clause、样板队伍。 |
| [`gamecubeguy49-islet`](../../raw/gs2/In-Depth%20Guides/Islet%20Cave%20Guide%20by%20GameCubeGuy49.md) | GameCubeGuy49 | walkthrough | default | locations · equipment · walkthrough | Islet Cave 支线（到达/传送区/练级/Tisiphone Edge）。单点 location 攻略。 |
| [`monet-ship`](../../raw/gs2/In-Depth%20Guides/Ship%20%26%20Sailing%20FAQ%20by%20Monet_Vanilla.md) | Monet_Vanilla | faq | default | mechanics · locations | 船与航海 FAQ + 船只列表/船主。机制/支线向。 |

### C. id / hex 参考（非提取源，价值在校验 + master-data/canonical id）
| source_id | 作者 | type | quality | covers | 一句话 |
|---|---|---|---|---|---|
| [`90kirsdarke-hack`](../../raw/gs2/In-Depth%20Guides/Item%20Djinn%20Hacking%20Guide%20by%2090Kirsdarke.md) | 90Kirsdarke | data-table | default | items · equipment · djinn · ids | item/djinn 内存地址与取值码（hex）。可做 canonical id / 完整性校验。 |
| [`kaitia-savehack`](../../raw/gs2/In-Depth%20Guides/Save%20Game%20Hacking%20Guide%20by%20kaitia.md) | kaitia | data-table | default | items · djinn · summons · psynergy · classes · characters · ids | 存档 hex 地址（属性/状态/psynergy/djinn/summon/item/arena）。canonical id / master-data 来源。 |

### D. 非提取源（剧本 / 音乐 / 密码 / glitch / RNG / 未完成）
| source_id | 作者 | type | quality | covers | 一句话 |
|---|---|---|---|---|---|
| [`josher1212`](../../raw/gs2/In-Depth%20Guides/Reference%20Guide%20by%20josher1212.md) | josher1212 | general | partial | mechanics · classes · djinn · psynergy · summons | 综合参考，内容好但**未完成且原文无 TOC**。**待单独一轮通读补 TOC** 再评估提取价值。 |
| [`sintaku-script`](../../raw/gs2/In-Depth%20Guides/Game%20Script%20by%20Sintaku.md) | Sintaku | general | default | story | 全游戏剧本 dump（含 djinn/summon、transfer 事件、可选 boss 附录）。非提取源。 |
| [`mtkennerly-script`](../../raw/gs2/In-Depth%20Guides/Game%20Script%20by%20mtkennerly.md) | mtkennerly | general | default | story | 全游戏剧本 dump + GS1 故事回顾。非提取源。 |
| [`thehomeland-dialogue`](../../raw/gs2/In-Depth%20Guides/Dialogue%20FAQ%20by%20thehomeland.md) | thehomeland | faq | partial | story | 仅开场与结局过场对白。非提取源。 |
| [`barbarossa89-music`](../../raw/gs2/In-Depth%20Guides/Music%20FAQ%20by%20Barbarossa89.md) | Barbarossa89 | faq | default | music | 各曲目及出现场景。非提取源。 |
| [`mr-unorigino-pw`](../../raw/gs2/In-Depth%20Guides/Password%20Conversion%20Guide%20by%20Mr_UnOrigino.md) | Mr_UnOrigino | faq | default | transfer | GS1→GS2 password 字符替换对照。transfer 参考；非提取源。 |
| [`barbarianbob-glitch`](../../raw/gs2/In-Depth%20Guides/Glitch%20Debug%20Room%20FAQ%20by%20barbarianbob.md) | barbarianbob | faq | default | glitch | 各种 glitch + 4 debug room。非提取源。 |
| [`link-kirby-rng`](../../raw/gs2/In-Depth%20Guides/Random%20Number%20Generator%20FAQ%20by%20Link_Kirby.md) | Link_Kirby | mechanics | default | mechanics · items | RNG 机制与掉落/锻造刷取（ICC、RN 值）。机制向，非提取源。 |

---

## 候选 / 未收集（来自目录页，按需补齐）

这些是 GameFAQs 上 GS2 的专项源。收哪个就把它移到上表，建 `raw/gs2/` 文件 + frontmatter。

> **In-Depth Guides 已全部收集**（见上「已收集 — In-Depth Guides（32 篇）」），目录页上
> 此前候选的专项源现已悉数到位。剩余未收集的只有下方「Maps and Charts」。

### Maps and Charts
目录页有 ~60 张地图（多为 Alex_GER 2024 + Krac6 内部图等），偏视觉、`extract.py` 不易吃。
**暂不收**；若日后做 locations/地图层再单独评估。

---

## 关于"组合召唤 / 石板召唤"
GS2 新增的 stone-tablet / 组合召唤（Daedalus、Catastrophe、Charon、Iris 等）：
**数值**归 `summons` 实体；**石板/支线获取**归 `locations`/`walkthrough`。
主源参考：Telago 附录A "Additional Stone Tablet Summons"、Autocon §3.6、DBFire 的
Summon Tablet/Sidequest Guide（[`dbfire`](../../raw/gs2/In-Depth%20Guides/Summon%20Tablet%20and%20Sidequest%20Guide%20by%20DBFire.md)）。

---

## 标注进度 tracker（可中断续做）

> 一个源标完（短 `source_id` + `type` + `covers` + `quality` + `summary`）就勾上。
> 仅追踪 frontmatter 标注状态，不含正文处理。

**Full Game Guides（10）** — 全部 ✅（上一轮完成）。

**In-Depth Guides（32）** — 本轮全部 ✅：

- [x] terence
- [x] torrentlord
- [x] ultimalink
- [x] aku-chi
- [x] android50
- [x] aspartate-djinn
- [x] demooni
- [x] aspartate-item
- [x] mr-unorigino-item
- [x] aspartate-forge
- [x] bbbbrain2000
- [x] yoyoyoshi
- [x] mr-unorigino-psy
- [x] shotgunnova-shop
- [x] dbfire
- [x] cooldude345
- [x] josher1212
- [x] link-kirby-boss
- [x] goldmario-boss
- [x] rena-chan-hardboss
- [x] astralfire
- [x] gamecubeguy49-islet
- [x] monet-ship
- [x] 90kirsdarke-hack
- [x] kaitia-savehack
- [x] sintaku-script
- [x] mtkennerly-script
- [x] thehomeland-dialogue
- [x] barbarossa89-music
- [x] mr-unorigino-pw
- [x] barbarianbob-glitch
- [x] link-kirby-rng

**遗留 TODO（下一轮）**：
- `josher1212`（Reference Guide）原文无 TOC 且未完成 → 单独一轮**通读后补 TOC**，再评估提取价值（用户指定）。
- `90kirsdarke-hack` / `kaitia-savehack` 的 hex 码 → 单独一轮评估是否做 **canonical id / master-data 层**（用户提议）。
