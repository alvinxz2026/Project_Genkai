# GS2 — Entity-Relationship Sketch（建模草图）

> **这是什么**：一张轻量的实体关系图，钉死 ① 有哪些实体 ② 每个实体的 `id` 方案
> ③ 谁引用谁、FK 放哪、怎么解析 ④ gs2 相对 gs1 的增量。**目的是防返工**——把 id 方案和
> 引用字段提前定好，这样可以任意顺序、独立提取每个实体，绝不会"做完一个又得回头改"。
>
> **为什么不用先把游戏 mechanics 全摸一遍**：gs1 的架构已经把「连接」和「提取」解耦了——
> 每个实体只存**自然键（名字）**，最后由 `links_normalize.py`（idempotent、最后跑的一层）
> 把 `name → id` 的 FK 回填上，`links_audit.py` 保证引用完整性。所以**字段完整性靠"源够多"，
> 关联设计靠这张图**，两件事分开。本图大部分直接继承 gs1 的成熟图（已跑通 0 error），只标 gs2 增量。
>
> 配套：[`gs2_extraction_plan.md`](gs2_extraction_plan.md)（实体×源 + 怎么提）、
> [`gs2_sources.md`](gs2_sources.md)（源清单）、`schema/gs1_schema.md`（字段细节母版）。

---

## 1. 实体清单（沿用 gs1 的 11 个 + gs2 增量）

| 实体 | 角色 | `id` 方案 | gs2 状态 |
|---|---|---|---|
| `characters` | **维度表**（被引用，不引用别人） | 小写名，如 `felix` | ⚠️ 4→**8**（Felix/Jenna/Sheba/Piers + 回归 Isaac/Garet/Ivan/Mia） |
| `locations` | **枢纽**（万物的位置反向索引→`location_refs.json`） | 小写连字符，如 `mars-lighthouse` | 增量：新大陆/副本/islet/Anemos |
| `djinn` | 事实表 | 小写名，如 `flint` | 增量：新 djinn；transfer 带入的 gs1 djinn 其 `game` 仍为 `gs1` |
| `summons` | 事实表 | 小写连字符，如 `judgment` | ⚠️ 新增**组合/石板召唤**（Daedalus/Catastrophe/Charon/Iris）破坏"每元素 4 个按数量"模型 |
| `classes` | 事实表（含自引用链） | 小写连字符 + 元素前缀，如 `water-shaman` | 增量：8 角色的职业；`terence` 仍是职业需求权威源 |
| `psynergy` | 事实表（含自引用系列） | 小写连字符，如 `mother-gaia` | 增量：新 psynergy |
| `equipment` | 事实表 | 小写连字符，如 `gaia-blade` | ⚠️ 新增**锻造件/锈蚀武器/三叉戟碎片** |
| `items` | 事实表 | 小写连字符，如 `herb` | 增量：**锻造原材料** |
| `shops` | 事实表（连 location↔货品） | 小写城镇名 | 主源 `shotgunnova-shop`（15 城镇） |
| `monsters` | 事实表 | 小写连字符 + `#n`→`-n` 变体，如 `mimic-1` | ✅ **已提取，203 条**（`scripts/monsters_extract_gs2.py`） |
| `bosses` | 事实表（比 monsters 多 encounters/attacks/strategy） | 小写连字符 | 未开始；monsters 里已有 boss stat-line 待 cross-link |

> **`game` 字段语义**：标"首次出现的游戏"而非"文件归属"。gs2 文件里多数实体 = `"gs2"`，
> 但 transfer 从 gs1 带入的 djinn 仍记 `"gs1"`（沿用 gs1 djinn schema 约定）。

---

## 2. 关系图（边 = 谁引用谁）

**两个被引用的核心节点**：`characters`（维度）和 `locations`（枢纽）。其余事实表挂上去。

```
  characters ◄─ name ──┬─ equipment.equippable_by[]
  [维度,叶子]          ├─ psynergy.available_to[]
                       └─ classes.available_to[].character (+ .character_id 解析)

  locations  ◄─ name ──┬─ djinn.location.area · equipment.acquisition.location
  [枢纽; 反向索引       ├─ items.acquisition.location · bosses.location · shops.location
   = location_refs]    ├─ monsters.found[]
                       └─ summons.acquisition.location        ← gs2 NEW (石板召唤)

  psynergy   ◄─ id ──── classes.psynergy[] (+id)              · psynergy.series → 自引用
  items      ◄─ id ──┬─ shops.stock[] · monsters.drops.items[] · psynergy.acquired_via_item
                     └─ equipment.forged_from[]               ← gs2 NEW (锻造)
  equipment  ◄─ id ──── shops.stock[] · monsters.drops.items[]   (stock/drop 用 ref_type 区分 item|equipment)
  djinn      ◄─ id ──── monsters.djinn_id  (is_djinn_enemy 时)
  bosses     ◄─ id ──── monsters.boss_id   (is_boss 时)
  classes    ◄─ id ──── classes.class_line (自引用：职业链最低 tier)
```

**元素软连接（不是 FK，是按元素+数量的关系）**：
`classes.available_to[].djinn_requirements`（每元素 djinn 数）、`summons.djinn_required`（同元素 djinn 数）
都通过 `element` + 数量与 djinn 关联，**不指向具体 djinn id**。所有 djinn/summons/psynergy/
characters/classes 都带 `element`，作软 join 键。

---

## 3. 连接原则（继承 gs1，已验证）——这就是"不会返工"的保证

1. **每个实体只存自然键（名字 / area 字符串）**；不在提取时手解析 FK。
2. **最后跑一遍 `links_normalize`（gs2 版）**：`name → id` 回填 FK，idempotent，任何实体重生成后重跑即可。
   gs1 边清单见 `scripts/links_normalize.py` docstring（直接照搬，改 `data/gs1`→`data/gs2`）。
3. **`links_audit`（gs2 版）**保证引用完整性（0 悬空引用）。`characters`/`locations` 多以名字校验，不一定加 id。
4. **推论**：实体可**任意顺序、独立提取**。monsters 先做、`djinn_id`/`boss_id`/drop `ref_id` 先留 null，
   等被引用实体齐了再回填——**已在 monsters 那一刀验证**。

> 实务上的提取顺序建议（非强制）：先做**被引用方**（locations / characters / items / equipment /
> djinn / bosses）再做**引用方**（shops / classes / monsters✅），这样 audit 能更早跑通——但因为是
> 最后统一连图，顺序错了也只是 audit 晚一点绿，不需重提。

---

## 4. gs2 增量的建模决策（倾向已给，标 TBD 的待写 schema 时定）

1. **characters 4→8**：加 Felix/Jenna/Sheba/Piers + 回归 4 人。`is_permanent`（gs1 用来标 Jenna 仅序章）
   语义变化 → 倾向换成 `join`/`availability` 描述（何时入队、是否后期回归）。**[倾向]** 仍是维度表，字段微调。
2. **forging（新边 equipment←items）**：**[倾向]** 不另立实体；在 `equipment` 上加
   `forged_from: [item_id]` + `is_forged` / `is_rusty` 标志，把"原材料(items)→锻造件(equipment)"建成一条边。
   主源 `aspartate-forge` / `aspartate-item`。
3. **组合/石板召唤（summons 新形态）**：单一 `djinn_required`(单元素数量)不够。**[倾向]** 给 summons 加
   `djinn_recipe: [{element, count}]`（跨元素配方）+ `acquisition`（石板→location）。基础 16 召唤继续用简单数量，
   组合召唤用 recipe。主源 `cooldude345` / `dbfire`（石板获取）。
4. **transfer（不是实体）**：**[倾向]** 建成**标志/小事件表**，不建 JSON 实体。在受影响的 djinn/item 上加
   `via_transfer` 之类布尔；4–6 个 transfer 触发事件归 walkthrough/locations，或一张极小的 `transfer_events`
   参考表。主源 `dbfire`(事件) / `mr-unorigino-pw`(password)。**[TBD]**

---

## 5. 这张图怎么用

- 写 `gs2_schema.md` 各实体段时，**引用字段按本图的边来定**（哪些存 name、哪个最后加 `*_id`/`ref_id`）。
- 增量项（forging / 组合召唤 / 8 角色 / transfer）在写到对应实体时落实 §4 的决策。
- 提取完几个实体后，照搬 gs1 的 `links_normalize`/`links_audit` 改 gs2 版跑连图。
- 本图是 living：写 schema 时若发现新边/改决策，回来更新。
