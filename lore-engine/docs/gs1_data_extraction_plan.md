# Lore-Engine — GS1 数据提取计划 & Progress Tracker

> 这个文件既是计划也是**进度追踪器**：每批完成后勾掉 `[ ]→[x]`，并在「进度日志」追加一行。

## Context（为什么做这个）

GS1 原型已把 djinn / bosses / equipment / classes / psynergy 五类 schema + 数据直出完成。
现又确定了一批 raw 文本（已找全，见下），含**现有 JSON 未覆盖的实体类型**与对现有实体的**补充/交叉校验源**。
目标：按 lore-engine 既定流水线（schema 先行、冲突标记不静默合并、可重复运行）增量并入 `data/gs1/`。
**约束：数据量大，必须分批，避免单次 usage / context window 爆掉。**

## 已锁定的方法论决策

1. **按实体类型切轴**提取（不是按文档）——同一实体多源并置才能做冲突标记。
2. **中间 markdown 清洗层 = 选择性**——规整源直出 JSON；杂乱源（locations）才先切片。
3. **控 context 的关键**：每批只读相关 section 的**行号区间**，绝不整文件读。下表已列定位。

## 源文件 × 实体 覆盖矩阵（已找全，7 个新源 + 既有源）

| 源文件（raw/gs1/） | 行数 | 覆盖实体（section 定位） |
|---|---|---|
| `Various data - Super Slash.txt` | 9546 | items §VI@2 / weapons §VII@223 / armor §VIII@634 / accessories §IX@1376 / djinn §X@1524 / classes §XI@1903 / psynergy §XII@3424 / **monsters §XIII@5087-9048** / shops §XIV@9049 |
| `Comprehensive Enemy List - Torrent Load.txt` | 7292 | **monsters**（§IV/1 Complete List = 主用；IV/2~IV/13 为排序视图，**忽略冗余**） |
| `Djinn Class Items Phynergy - Telago.txt` | 2474 | djinn §1@5 / **summons §2@86** / class&psynergy §3@118 |
| `Djinn Items Psynergy - BFGamer.txt` | 2126 | djinn loc §6.1@10 / summons §6.2@63 / setups §6.3@93 / items §7@730（game items §7.4@1741）/ psynergy §8@1748 |
| `Various data - Shotgunnova.txt` | 1565 | psynergy [PSNR]@2 / classes [CLSS]@212 / djinn [DJNN]@944 / **shops [SHPL]@1028** / equipment [EQPT]@1309 |
| `Classes Djinn Weapons Armor Equipment - ElectroSpecter.txt` | 1507 | classes §7@2（stat% + djinn 需求）/ weapons / armor / equipment / djinn |
| `Various data - strawhat.txt` | 564 | psynergy {6.0}@2（字母序，⚠**含部分 GS2 条目，需过滤只留 GS1**）|

既有源（已在五类 JSON 中）：dnextreme88 / Jiggyhunter / plz2bstfu / Terence / aku-chi / LinkTheValiant / RocketTrekkie / nintendos_own / strawhat(psynergy FAQ) / 各 FandomWiki。

## 分批执行计划（按批勾选）

> 每批的标准 5 步：①定/审 schema → ②凑源(行号区间) → ③提取(规整直出/杂乱先清洗) → ④冲突标记 → ⑤计数+抽样校验。
> 估算：S=小(1 session)、M=中、L=大(需再切片)。每批结束更新「进度日志」。

### Phase A — 新类型 · 规整 · 快赢（先做这批）
- [x] **A1 items** （S）→ `data/gs1/items.json`（**28 条**：16 consumable / 6 stat_boost / 6 key）✅
  - 源：Super Slash §VI@2-222（主，27 项含 buy/sell 价+描述）；rockettrekkie（8 个迁移项的 acquisition）
  - schema：已加 `items` 段（v1.2）+ source `super-slash`
  - **迁移**：8 个误置在 equipment.json 的消耗品/关键道具移入 items.json；equipment.json 95→87（保留 7 戒指）
  - 冲突：Hermes' Water 效果描述（super-slash「restore Tret」vs rockettrekkie「restores HP」）已标记
  - 注：BFGamer §7.4 game items 实为空段，无数据
- [x] **A2 summons** （S）→ `data/gs1/summons.json`（**16 个**，4 元素 × tier 1-4）✅
  - 源：Telago §2@86-114 + BFGamer §6.2（仅 name/element/djinn数）
  - schema：已加 `summons` 段 + source `telago`/`bfgamer`
  - ⚠ 当前源**无召唤伤害数值**，`damage_power`/`effect` 暂为 null，待后续源补；拼写用游戏内正名 Judgment
- [x] **A3 shops** （M）→ `data/gs1/shops.json`（**12 城镇 / 202 stock 行**）✅
  - 源：Shotgunnova [SHPL]（主，含 artifact 星标+营业备注）∪ Super Slash §XIV（补 Bilibin/Kolima/Altin 漏项）
  - schema：已加 `shops` 段 + source `shotgunnova`
  - **脚本**：`scripts/shops_extract.py`（可重复运行，从 raw 解析+自动跑价格交叉校验）
  - 冲突：6 个价格分歧已标记（Wooden Stick 60/40、Circlet 130/120、Battle Rapier 2800/2900）；Platinum Circlet 拼写归一化
  - 连带修 items.json：Potion/Psy Crystal/Water of Life 确认可买(1000/1500/3000)，buy_price 补全+冲突标记
  - **⚠ Phase C 输入**：shops 引用的 **54 个基础武器/防具 equipment.json 里没有**（旧 equipment 偏 artifact）→ C4 要补

### Phase B — 新类型 · monsters（脚本一次性完成，未走手动切片）
- [x] **B monsters**（L）→ `data/gs1/monsters.json`（**137 条** = 152 − 15 boss）✅
  - **两源完全同序 152 条**（Super Slash §XIII ↔ Torrent Load complete list）→ 按索引 1:1 匹配，绕开变体匹配难题
  - schema：已加 `monsters` 段 + source `torrent-load`
  - **脚本**：`scripts/monsters_extract.py`（可重复，双源解析+按元素名映射+索引合并+自动冲突标记）
  - **boss 排除**：15 条 boss stat-line（Saturos×2/Menardi/Tret/Deadbeard…）按决策排除，bosses.json 为 boss 唯一真相源
  - djinn 敌人 14 个（13 链 djinn.json，秘密 Venus Djinni ??? 留 null）；Torrent 提供 regen/abilities/掉落 ICC
  - 冲突：27 条真实源分歧已标记（如 `orc` exp/coins 两源对调、多处元素 power 80/90）
  - ⚠ **遗留**：被排除的 15 条 boss stat-line 可作**交叉校验 bosses.json** 的输入（脚本会打印它们）

### Phase C — 补充现有 JSON（加 source + 冲突标记，互相独立可乱序）
- [x] **C1 djinn 补充** → `data/gs1/djinn.json`（28 条）✅
  - 新源：Telago §1 / BFGamer §6.1 / Super Slash §X / Shotgunnova [DJNN] / ElectroSpecter（+ torrent-load 佐证 must_fight）
  - **冲突裁决策略升级（全局）**：schema v1.3 加 Conflict Resolution Policy（majority→authority→unresolved）+ Source Authority Ranking；冲突对象加 `resolution`
  - 新字段 `must_fight`（13 个要打，从 §XIII bestiary 派生）
  - 裁决：3 stat 冲突(Fever/Kite/Tonic)→terence 权威；4 location 冲突(Zephyr→Fuchin Falls Cave / Luff→Babi Lighthouse / Tonic→Lunpa Fortress / Hail 保留)→majority
  - 脚本：`scripts/djinn_supplement.py`（diff 报告）+ `scripts/djinn_apply.py`（重生成）
- [x] **C2 psynergy 补充** → `data/gs1/psynergy.json`（141 条）✅
  - 新源：Shotgunnova [PSNR] / Super Slash §XII / BFGamer §8（**跳过 Various-strawhat** 避 GS2）
  - pp/range 现在最多 7 源 → **多数表决真正生效**；15 现有冲突全部重判 + 新源加票
  - 结果：22 冲突全带 resolution（18 majority/2 authority/2 unresolved）；**0 值改变**（新源印证 json 本就在多数值上）
  - 亮点：grand-gaia pp 32（5 源印证，strawhat 17 离群）；hurricane 平局→tetz 权威保 7；dull→wind（strawhat water 是已知元素 typo）；force/carry 同物异名→unresolved
  - 脚本：`scripts/psynergy_supplement.py`（diff 报告）+ `scripts/psynergy_apply.py`（重生成）
  - 修了 2 个解析 bug：「One Ally」含子串 all、Shotgunnova 用 R=9 表「全体」
- [x] **C3 classes 补充** → `data/gs1/classes.json`（76 条）✅
  - 核心价值：**stat_multiplier 从 15→72**（填了 57 个之前缺 % 的 class）
  - 源：**ElectroSpecter §7 + Shotgunnova [CLSS] + FandomWiki 通用职业表**（`Class - FandomWiki`，20 行高阶双元素职业，无角色维度，按名匹配）+ aku-chi 四源交叉；**放弃 Telago §3**（元素-角色共享段 + `x|y` 含管道，解析不可靠）；Super Slash §XI 只有 spell 列表无 %（本次未用）
  - 匹配：角色 + class 名 + Djinn 元素消歧（Shaman(1) 6 Jupiter→wind-shaman 等）；FandomWiki 按 class 名直接套到所有同名条目（Conjurer/Druid 双变体 stat 相同，无歧义）
  - 裁决：逐 stat majority；平局走权威 **aku-chi → fandom-wiki**（皆 data-derived）；纯 electro-vs-shotgun 1v1 无权威→ unresolved（留 electro）
  - **2026-06-15 加 FandomWiki 复核（用户查 wiki 发现 champion pp 是 110 不是 120）**：13→10 stat 冲突；**champion pp 120→110**（electro/shotgun 120 vs aku-chi/fandom-wiki 110，2-2 平局→权威→110，唯一被改值）；medium agi/lck 由 unresolved 升 majority（FandomWiki 站 electro）；berserker pp/atk、magister atk 得 FandomWiki 佐证确认 Shotgunnova swap 为离群；脚本可重入（从 conflict 还原原始 aku-chi 票，避免用已裁决值重投）
  - 当前 10 冲突 resolution：8 majority / 1 authority(champion pp) / 1 unresolved(cavalier-isaac agi)；另 3 旧非 stat 冲突补 unresolved → 全表 13 冲突全带 resolution
  - 4 个不可达类（slayer/war-adept/chaos-lord/flame-user）无源，stat% 留 null
  - 脚本：`scripts/classes_supplement.py` + `scripts/classes_apply.py`
  - ⚠ 遗留：Shotgunnova 有 7 个 Ivan 异名 class（Water Seer/Scribe/Cleric/Paragon…）未匹配 json，可能 json 缺这些 Ivan 变体——待查
- [x] **C4 equipment 补充** → `data/gs1/equipment.json`（**141 条** = 87 + **54 新基础装备**）✅
  - 核心价值：补全 A3 发现的 shops 引用但 equipment.json（偏 artifact）缺失的 54 基础武器/防具 → **shops stock 现 0 缺口**
  - 新源（3 个结构化表，均 GS1 干净）：**Shotgunnova [EQPT]**（一张定宽表覆盖全部类别：IGIM 装备位/ATK/DEF/AGL/LCK/unleash/cost/artifact `*`/cursed `|C|`；但不全，缺 Battle Axe、Hunter's Sword）∪ **Super Slash §VII-IX**（Found/Buy Price/Stats/Effect，含元素与 PP/HP 加成、regen、倍率）∪ **ElectroSpecter §8/§10**（按 type 分表 → 权威 type 桶 + ATK/DEF + price/location）
  - 54 新：17 武器（4 long_sword / 5 light_blade / 3 axe / 4 mace / 1 staff）+ 37 防具；**三源 ATK/DEF 全一致（无数值冲突）**
  - `type` 用人工 map（按 FandomWiki 装备图表 + ElectroSpecter type 表交叉验证：caps→hat、Jerkin/One-Piece Dress→robe、Cotton Shirt→clothing）；`equippable_by` 用 type 默认 + females-only 覆盖（Shotgunnova `---M`→[Mia]，如 One-Piece Dress）；Shotgunnova 给 Leather/Wooden Cap 的 `IG--` 是离群（ElectroSpecter「used by all」+ 既有 hat 全四人）→ 忽略
  - 裁决：`acquisition.price` 取三源**多数票**（shops 价格派生自 Shotgunnova，非独立票）→ Wooden Stick 40 / Circlet 120 / Battle Rapier 2900（Shotgunnova 每次都是离群），冲突已记
  - 交叉校验既有 87：新源印证处加进 `sources`（shotgunnova 124 / super-slash 114 / electrospecter 121 条引用）；真分歧标 `resolution:"authority"` 保 dnextreme88 值（grievous-mace atk 88 vs 101、storm-gear def 42 vs 36、war-gloves def 32 vs 35、battle-gloves atk 8 vs 5）；回填 A 阶段旧冲突 resolution
  - 当前 20 冲突全带 resolution（10 majority / 4 authority / 6 unresolved）
  - 脚本：`scripts/equipment_supplement.py`（覆盖+冲突报告）+ `scripts/equipment_apply.py`（重生成，从 curated 87 基底每次重建 54，可重入、字节级幂等）
  - 修了 1 个解析 bug：「One-Piece Dress」含连字符未被识别为新块 → 数据漏进上一条（Cocktail Dress）；id slug 去撇号匹配既有命名（knights-helm 而非 knight-s-helm）

### Phase D — locations（做成 gazetteer / hub 节点，不做复杂结构；最后做）

**设计决定（关键 = 简化）**：`locations.json` 只做**规范地名注册表 + hub 节点**，**不**做房间/连接/坐标/逐格道具这类复杂结构。
理由：① 复杂结构化 location 收益低、维护贵；② 地图已在 `data/gs1/gs1_maps.md`（含 ASCII 图 + 道具 + 敌人 + 图例），攻略散文已在 `data/gs1/gs1_walkthrough.md`，再 JSON 化只是重复。
locations.json 的真正价值 = ①一份**规范地名清单**（type + 章节 + 一句话）；②把现有各 JSON 里散落的 location 字符串（`djinn.location.area` / `equipment.acquisition.location` / `monsters.found[]` / `bosses.location` / shops 镇名 / `items.location` / `psynergy.acquisition.location`）**反向索引**聚到一个节点。

**源（全是已清洗的二手层，本批不必再读 raw）**：
- `gs1_maps.md` 的三个分类标题块（World Map / Towns & Villages / Dungeons & Caves / Other）→ 直接给 `type` 分类 + `has_map`。其 `_(暂无 ASCII 地图)_` 占位 = `has_map:false`。
- `gs1_walkthrough.md` 的 `### {地点}` 标题序（按 chapter 组织）→ 给 `chapter_first_seen` + 截 narrative 首句做 `summary`。

**schema（最小字段，新增 `locations` 段；TOC + Master Source IDs 同步）**：
- `id`(slug)、`name`(游戏内名)、`type`(enum: `town` | `dungeon` | `world_map` | `other`)、`region`(string|null)、`chapter_first_seen`(string)、`summary`(1 句，取自 walkthrough narrative，不臆造)、`has_map`(bool，true 时即指向 `gs1_maps.md` 同名条目)、`aliases`(array：攻略里出现的异名 / revisit / 拆屏变体，**供反向索引匹配用**)
- **反向索引（refs）= 派生的物化视图，不嵌在 locations.json**，单独落 `data/gs1/location_refs.json`（脚本生成、勿手改）。locations.json 保持纯手写 dimension/词表。设计依据：源/派生分层、先量化数据质量再决定是否清源（data management 规范，详见 `docs/data_management_notes.md`）。
- **无冲突标记环节**：注册表是地名枚举，无多源数值分歧；故不套 conflicts/resolution 机制。

**步骤（轻量，2 步）**：
- [x] **D1 清单 + schema**（S–M）→ `locations.json` 骨架（**38 条**：12 town / 22 dungeon / 3 other / 1 world_map；26 条 has_map）✅
  - 合并两文件标题 + 各 JSON 实际 location 字符串 → **去重归一**：`Imil Ice Sliding`/`(Post-Lighthouse)` → imil；`Crossbone Isle #1..#10`/`Ghost Ship` → crossbone-isle；`World Map (near Vale)`/`World Map 1..9` 等 → 单个 world-map；`Colosso`/`Babi's Palace`/`Battle Arena` → tolbi（`Vale Cave`/`Vault Cave`/`Kalay Tunnel` 保留独立）。
  - `type` 照 maps.md 分类；`aliases` 已**预填各 JSON 里的真实写法含 typo**（`Bibilin Cave`/`Atmiller Cave`/`Tolbi-bound Boat`/`Crossbones Isle`）以拉高 D2 命中率。
  - schema 已加 `locations` 段（含 Type Enum + 示例 + CC 注记）；TOC 同步；Master Source IDs 加 `gs1-walkthrough` / `gs1-maps` 两个清洗层源。
  - chapter 用 `gs1_walkthrough.md`（非 fable）编号；refs 外迁 D2。校验：38 id 唯一、0 alias 冲突、JSON 合法。
- [x] **D2 反向索引（物化视图）**（S）→ `scripts/locations_refs.py` + `data/gs1/location_refs.json`（可重入、字节级幂等）✅
  - 读 djinn / equipment / monsters / bosses / shops / items 的 location 字段，按 `aliases` 解析到 location id，物化反向索引到**独立文件** `location_refs.json`（不回写 locations.json，不动源实体）。
  - 解析器：整串精确 → 拆复合串（` / ;,` 切片 + 剥 `(...)` 括注）→ 词边界子串兜底；多匹配（一条装备可同属 3 个灯塔）。
  - **未匹配从 10 → 0**：白名单掉 `B2/B3`（floor 碎片，母条目已含 Altin Peak）、`Various shops / Mimics`（game-ticket 非定点）、`[Not In Game]`。
  - psynergy/summons 无 location 字段，未纳入。零-ref 地点 2 个（idejima 片尾场景 / lama-temple 纯剧情）合理为空。
  - 校验：双向引用完整性（location id + 实体 id 均真实）；重跑 md5 一致；抽样 mercury-lighthouse→saturos、kolima-forest→tret/breeze、tolbi→springs items 均正确。
  - schema 改：locations 段删 `refs` 字段、加「Derived view」小节；TOC 同步。
- [x] **D3 教学文档**（S）✅ → `docs/data_management_notes.md`：用本项目实例讲 data management（源/派生、物化视图、受控词表/实体解析、引用完整性、measure-before-mutate）。

估算：整体 S–M，**比 A/B/C 都轻**（无 raw 切片、无冲突裁决）。D1+D2 已收尾；D3 为用户额外要求的科普文档。

### Phase E — 跨实体 FK 规范化（已完成，独立 tracker）
A–D 完成后，把「各实体只靠 name 字符串隐式相连」升级成 **id 连通、可强校验的图**：补 10 个缺失 item、建 `characters.json`、给 classes/shops/monsters/psynergy 回填 FK（`scripts/links_normalize.py`）、加只读质量门（`scripts/links_audit.py`）。详见独立 tracker **`docs/gs1_linkage_normalization_plan.md`**。

### 每批通用：新增 source 时
- 把新 source ID 加进 `schema/gs1_schema.md` 的 **Master Source IDs** 表。

## 进度日志（每批完成追加一行）
| 日期 | 批次 | 产出 | 备注 |
|---|---|---|---|
| 2026-06-14 | 计划 | 本 tracker | 源已找全，方法论锁定，待按 A→B→C→D 推进 |
| 2026-06-14 | A1 items | items.json(28) + schema v1.2 + equipment.json 去重(95→87) | 8 个道具从 equipment 迁入；Hermes' Water 冲突已标记 |
| 2026-06-14 | A2 summons | summons.json(16) + schema summons 段 | 仅 name/element/djinn数；伤害数值待补 |
| 2026-06-14 | A3 shops | shops.json(12镇/202行) + schema shops 段 + scripts/shops_extract.py | 6 价格冲突；items.json 修 3 项 buy_price；发现 equipment 缺 54 基础装备(→C4) |
| 2026-06-15 | B monsters | monsters.json(137) + schema monsters 段 + scripts/monsters_extract.py | 双源同序索引合并；排除15 boss；27 真实冲突；boss stat 可后续校验 bosses.json |
| 2026-06-15 | 自检 A+B | 修 monsters 1 个真 bug（末条吸入 IV/2 榜单）+ 过滤 SS found "N/A" | 验证双源对齐(仅3处错位且无害)；Orc exp/coins 确为真源对调；全 JSON 合法、id 唯一、计数核对通过 |
| 2026-06-15 | C1 djinn | djinn.json(28) +must_fight +6 裁决冲突；schema v1.3 冲突裁决策略+权威排序 | stat→terence权威；location→majority(Zephyr/Luff/Tonic 改名)；djinn_supplement+djinn_apply 脚本 |
| 2026-06-15 | C2 psynergy | psynergy.json(141) 22 冲突全裁决(18maj/2auth/2unres)；跳过 GS2 源 | pp/range 多数表决；0 值改变(新源印证)；psynergy_supplement+apply 脚本 |
| 2026-06-15 | C3 classes | classes.json(76) stat% 15→72(填57)；electro+shotgun+aku-chi 三源；13 冲突 | 放弃 Telago(难解析)；champion pp 多数120 压过 aku-chi 110；classes_supplement+apply 脚本 |
| 2026-06-15 | C3 复核 | 加第4源 FandomWiki 通用职业表(20行)；20 条引用 fandom-wiki；脚本可重入 | 用户查 wiki 纠正：**champion pp 120→110**(2-2平局→权威 aku-chi/fandom-wiki)；medium agi/lck 升 majority；权威只认 aku-chi/fandom-wiki，electro≠shotgun 1v1 留 unresolved |
| 2026-06-15 | C4 equipment | equipment.json(141=87+54)；3 结构化源(shotgunnova/super-slash/electrospecter)；equipment_supplement+apply 脚本 | 补全 shops 全部 54 基础装备(stock 0 缺口)；价格多数票(Wooden Stick 40/Circlet 120/Battle Rapier 2900)；4 既有 stat 冲突 authority 保 dnextreme88；20 冲突全裁决；修 One-Piece Dress 连字符解析 bug |
| 2026-06-16 | D1 locations | locations.json(38: 12town/22dungeon/3other/1world_map) + schema locations 段 + TOC + 2 源(gs1-walkthrough/gs1-maps) | gazetteer/hub 设计；折叠 Crossbone 9 层/World Map/Imil 子区到 aliases；aliases 预填各 JSON 真实写法+typo；refs 全空待 D2；38 id 唯一/0 alias 冲突 |
| 2026-06-16 | D2 location_refs | scripts/locations_refs.py + data/gs1/location_refs.json(物化视图) ；locations.json 删 refs 字段；schema 加 Derived view 小节 | 反向索引外迁独立文件(源/派生分层)；解析器 精确+拆复合+子串兜底+多匹配；未匹配 10→0(白名单 B2/B3·Various shops·[Not In Game])；双向引用完整性+md5 幂等校验通过；2 零-ref 地点(idejima/lama-temple)合理 |

## 验证方式（落地后）
- 计数核对：djinn=28、summons=16、monsters≈全敌人数等已知总数
- 抽样把 JSON 字段回比源文本
- JSON 合法性 / 必填字段检查
- 现有 `tools/*.html` explorer 可扩展用于人工浏览新数据

## 仍待你确认（review 时定）
- [ ] Phase A 内部顺序 / 是否同意 A 先于 C
- [ ] monsters 每片粒度（默认 ~25-30 个/片）是否合适
- [ ] locations(D) 是否本轮纳入，还是另起 plan
- [ ] 脚本化程度：手工 CC 提取 vs 扩展 `scripts/extract.py` 自动化
