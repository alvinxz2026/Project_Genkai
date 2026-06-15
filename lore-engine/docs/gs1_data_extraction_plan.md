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
- [ ] **C3 classes 补充** → `data/gs1/classes.json`
  - 新源：Telago §3 / Super Slash §XI / Shotgunnova [CLSS] / ElectroSpecter §7
- [ ] **C4 equipment 补充** → `data/gs1/equipment.json`
  - 新源：Super Slash §VII-IX / Shotgunnova [EQPT] / ElectroSpecter
  - **已知缺口**：A3 发现 shops 引用的 ~54 个基础武器/防具（Long Sword、Leather Armor 等）equipment.json 里没有，需补全（含 stats）

### Phase D — locations（最难，单列，需清洗层）
- [ ] **D1 locations**（L）→ `data/gs1/locations.json`（现为空）
  - 散落在各攻略，无规整源 → 先按地区切中间 markdown（staging），人工 review 后再出 JSON
  - 建议**最后做**，或独立成另一个 plan

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
