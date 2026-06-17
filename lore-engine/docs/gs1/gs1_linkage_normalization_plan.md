# Lore-Engine — GS1 跨实体 FK 规范化 计划 & Progress Tracker

> 这个文件既是计划也是**进度追踪器**：每阶段完成后勾掉 `[ ]→[x]`，并在「进度日志」追加一行。
> 多 session 推进，**每个 session 只做一个 Stage**，避免单次 usage 爆掉。Resume 时先读本文件。

## Context（为什么做）

GS1 九个实体表（djinn/summons/classes/psynergy/equipment/items/shops/monsters/bosses）+ locations 已建好，
但彼此**只靠 name 字符串 / 元素+数量隐式相连**，真正的外键只有 `monsters.djinn_id` / `monsters.boss_id` 两个。
没有可直接查询、可强校验的关系层——回答「Ninja 给哪些 psynergy」「哪些怪掉 Long Sword」每次都要现跑 name-join。

一轮跨文件审计还查出 3 类数据 bug（见 E0a/E0b）。目标：给各实体加真正的 `*_id` FK + 建 `characters.json`，
把 djinn→summon→class→psynergy→shop→equipment、equipment→角色 变成 **id 连通、双向可查、可强校验的图**。

## 已锁定的方法论决策（承接 `docs/data_management_notes.md`）

1. **FK 表示 = 保留可读 `name` + 旁加权威 `*_id`**（id 是链接 of record，name 是冗余便读，audit 保持同步）。
2. **角色引用用 `characters.json` 作自然键校验**（角色名干净、1:1 对 id），不在每条加 id 数组。
3. **id 回填全由脚本完成、in-place 幂等**；绝不手改上千条引用条目。
4. **先修脏数据，再建 FK**（脏数据会让 FK 解析失败）。
5. **FK 回填是各实体（重）生成后的最后一道 enrichment pass**；若日后重跑某实体的 `*_apply.py`/`*_extract.py`，
   需再跑一次 `links_normalize.py`（幂等，安全）。

## 当前链接现状（审计结论，2026-06-16）

| 关系 | 现在怎么连 | 状态 |
|---|---|---|
| class → psynergy | `classes.psynergy[].name` | ✅ 1026 refs 100% 可解析（待加 id）|
| shop → items/equipment | `shops.stock[].name` | ✅ 202 refs 100% 可解析（待加 id）|
| monster → 掉落 | `monsters.drops.items[].name` | ⚠ 126 refs，3 类 bug（E0a/E0b 修）|
| psynergy → 道具 | `acquired_via_item.item`（name）| ⚠ 8 个引用的道具 items.json 里没有（E0a 补）|
| djinn 组合 → class | `available_to[].djinn_requirements`（文本）| 隐式文本，待结构化（E2b）|
| equipment/psynergy → 角色 | 角色名数组 | 待 characters.json 校验（E1）|
| djinn → summon | summon 的 element+djinn_required | 隐式语义（不物化，查询时按 element 连）|
| monster → djinn/boss | `djinn_id`/`boss_id` | ✅ 既有真 FK |

## 分阶段执行计划（每阶段≈1 session，按序勾选）

- [x] **E0a items 补缺**（M）→ items.json **28→38** ✅
  - 战斗投掷（consumable）：Oil Drop（fire power 30）、Bramble Seed（earth power 50）—— 源 telago（power+element）/ strawhat / shotgunnova
  - field-psynergy 关键道具（key，8 条）：Catch Beads / Carry Stone / Cloak Ball / Douse Drop / Frost Jewel / Halt Gem / Lifting Gem / Orb of Force —— 源 super-slash（Found+effect "Equip to learn X spell"）/ tetzcatlipoca（acquisition 位置）
  - 校验：items=38、id 唯一；**psynergy.acquired_via_item 8 个引用 100% 可解析**；monsters.drops 除 E0b hobgoblin 损坏外 0 未解析；与 equipment.json 0 重名
- [x] **E0b 修脏数据**（S–M）✅
  - monsters：根因修 `scripts/monsters_extract.py`——Torrent 的 section 识别改成通用正则 `^::(.+?)::$`，未知 section（`::Carries::`，全文件仅 Hobgoblin 有）不再漏进 drops。重生成 monsters.json（137 条不变）；**diff 完全隔离**：仅 `hobgoblin` 去掉 4 条 `(1) X` 碎片 + `::Carries::`，并消掉一条因损坏产生的伪 drops 冲突。hobgoblin drops 现 = Lucky Medal(ICC1)（其真实掉落；Carries 是它「携带/可偷」的道具，非战利品，按设计不计入 drops——4 个道具本就都在 items.json）
  - psynergy：`blast-nova` vs `blast-mad` **不是重复 bug**——是 GS1 两条真·不同法术线共用 tier1 名 "Blast"：blast-nova(7)→Nova(13)→Supernova(31)、blast-mad(5)→Mad Blast(9)→Fiery Blast(19)。**不改数据**。仅需 E2a 解析 "Blast" 时按同类法术消歧（有 Nova/Supernova→blast-nova，有 Mad Blast/Fiery Blast→blast-mad）；已验证 12 个含 Blast 的 class **全部可确定解析、0 歧义**
- [x] **E1 characters.json + schema**（S）✅
  - 5 条：isaac(earth)/garet(fire)/ivan(wind)/mia(water)/jenna(fire，is_permanent=false)；字段 id/name/game/element/is_permanent/notes/sources
  - schema 加 `characters` 段（dimension table，说明 equippable_by/available_to/available_to.character 用 name 作自然键）+ TOC
  - 校验：5 id 唯一；**各文件引用的 5 个角色名 100% 被覆盖**（0 dangling）
- [x] **E2a links_normalize.py（清晰边）**（M）✅ → 回填 100% 可解析的 FK
  - `scripts/links_normalize.py`：`classes.psynergy[]` += `id`（1026）；`shops.stock[]` += `ref_type`+`ref_id`（202）；`monsters.drops.items[]` += `ref_type`+`ref_id`（121，E0b 后从 126 降）
  - **"Blast" 消歧**：按 series 成员通用消歧（候选法术的 series 在该 class 还有别的成员则命中）→ 实跑 blast-nova/blast-mad 各 6 个 class，0 歧义
  - equipment/items 名字全局不重叠（已验），故 ref_type 由命中文件唯一确定
  - **0 未解析、exit 0、连跑 md5 幂等、diff 仅新增 ref 字段**；id/ref_id 插在 name 之后便于读
- [x] **E2b links_normalize.py（复杂边）**（M）✅
  - `psynergy.acquired_via_item` += `item_id`（8 条，依赖 E0a；全解析）
  - `classes.available_to[]` += `character_id`（92 条，全解析）；`djinn_requirements[]` += `parsed:[{element,min,max}]`（元素别名归一 Venus→earth 等 + `a-b` 区间 + 多元素复合 "4 Venus, 3 Jupiter"→2 条）
  - djinn_requirements 解析 **215/216**；唯一未解析是 flame-user 的 "Fixed class; Jenna's class…cannot be changed"（非元素备注，parsed=[] 合理，非 fatal warning）
  - `equipment.equippable_by` / `psynergy.available_to` 角色名保留自然键，校验放 E3 audit
  - **0 未解析、exit 0、连跑 md5 幂等、diff 仅加字段**
- [x] **E3 links_audit.py**（S）✅ → 只读质量门
  - `scripts/links_audit.py`：校验 11 文件 645 行——id 唯一 / 6 类 FK 解析+name↔id 一致 / monsters.djinn_id / 角色自然键(equippable_by·available_to·available_to.character) / djinn_requirements parsed 合法
  - 跑通 **0 errors、exit 0**；**负向测试**：故意改坏一个 ref_id → 正确报 dangling、exit 1，恢复后再 0（确认非空过）
- [x] **E4 schema 更新**（S）✅：classes（psynergy.id / available_to.character_id / djinn_requirements.parsed）、shops（stock.ref_type+ref_id）、monsters（drops.ref_type+ref_id）、psynergy（acquired_via_item.item_id）字段表全补；General Rules 加「Cross-Entity Links」总表
- [x] **E5 收尾**（S）✅：本 tracker 勾完；`gs1_data_extraction_plan.md` 加 Phase E 引用；项目记忆更新「实体已 FK 连图」

## 进度日志（每阶段完成追加一行）

| 日期 | 阶段 | 产出 | 备注 |
|---|---|---|---|
| 2026-06-16 | 计划 | 本 tracker | 审计完成：3 类 bug 定位、链接现状摸清、方法论锁定（改源 FK 方案）|
| 2026-06-16 | E0a items | items.json 28→38（2 throwable + 8 psynergy-grant key items）| 数据均来自 raw（telago/super-slash/tetzcatlipoca），未臆造；psynergy.acquired_via_item 引用全解；与 equipment 0 重名 |
| 2026-06-16 | E0b 修脏 | monsters_extract.py 通用化 section 识别 → 重生成 monsters.json（hobgoblin drops 干净，diff 仅此一处）；psynergy "Blast" 查实非 bug（两条真法术线），不改数据 | Blast 同名碰撞由 E2a 按同系法术消歧，12/12 class 0 歧义；monsters 仍 137、id 唯一 |
| 2026-06-16 | E1 characters | characters.json(5) + schema characters 段 + TOC | isaac/garet/ivan/mia/jenna；各文件引用的角色名 100% 覆盖、0 dangling；角色名作自然键（E3 校验） |
| 2026-06-16 | E2a 回填FK | scripts/links_normalize.py；classes.psynergy+id(1026)/shops.stock+ref(202)/monsters.drops+ref(121) | 0 未解析；Blast 按 series 消歧 6/6；幂等、diff 仅加字段；equipment∪items 名字不重叠 |
| 2026-06-16 | E2b 回填FK | links_normalize.py 扩展；psynergy.acquired_via_item+item_id(8)/classes.available_to+character_id(92)+djinn_requirements parsed(215/216) | 0 未解析；元素别名归一+多元素+区间；唯一未解析是 Jenna 固定职业备注(合理)；幂等 |
| 2026-06-16 | E3 audit | scripts/links_audit.py（只读质量门）| 645 行 0 errors、exit 0；6 类 FK+name↔id+id 唯一+角色自然键全过；负向测试确认能抓 dangling |
| 2026-06-16 | E4 schema | schema 4 段补 FK 字段 + General Rules「Cross-Entity Links」总表 | classes/shops/monsters/psynergy；字段标注 links_normalize 生成 |
| 2026-06-16 | E5 收尾 | Phase E 完成；gs1_data_extraction_plan.md 加引用；项目记忆更新 | 终检：normalize exit0 / audit 0err / 全 JSON 合法（items38·chars5）|

## 验证方式

- **幂等**：`links_normalize.py` 连跑两次 → 相关 JSON 的 md5 稳定
- **完整性**：`links_audit.py` 报告 0 未解析 / 0 悬空 / 0 name-id 不一致 / 全 id 唯一
- **图查询抽样**（证双向连通）：
  - class `ninja` → 经 psynergy id 列出法术
  - `long-sword` equipment id → 反查哪些 shop 卖、哪些 monster 掉、哪些角色可装
  - summon `judgment` → 经 element 反查可供养的 djinn
  - psynergy `catch` → 经 `item_id` 找到 Catch Beads
- **计数**：characters=5、items=38；全 JSON 合法、id 唯一
