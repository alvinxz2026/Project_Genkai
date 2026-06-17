# Plan — Walkthrough→Data 链接 + location 升级为真 FK

> 计划文档，待执行。承接 `gs1_linkage_normalization_plan.md`（Phase E 已完成）。
> Resume 时先读本文件。

## Context（为什么做）

两个相关问题，答案收敛到同一处：

1. **能否把攻略（`data/gs1/gs1_walkthrough.md`）和 data JSON 连起来？** —— 能。攻略是模板结构化
   文档（Chapter → Location 块，含 **Enemies/Items/Djinn/Shop/Boss** 子块 + Djinn 速查表），
   每个实体在 data 侧都有规范 id 和 `aliases` 受控词表。项目里**已有现成的实体解析器**
   （`scripts/locations_refs.py` 的 `build_resolver`/`resolve`）和 FK 回填范式
   （`scripts/links_normalize.py`），把攻略里的实体提及解析成 id 完全可行。

2. **data JSON 有无优化空间？** —— 选定方向：**把各实体的自由文本 location 升级成真 location_id
   外键**。这是 `data_management_notes.md` 第 6 节里**有意推迟**的那一步（“理想是外键，先量化
   再改源”）。量化已完成（`locations_refs.py` 报告 0 未匹配），可以做。

**收敛点**：location FK 给出的就是攻略链接器要解析的**同一套地点 id**。所以先做 location FK
（Part A，也是被选中的优化），它顺带把地点词表打通；再做攻略链接层（Part B），复用同一解析器。

遵循项目铁律：**source/derived 分离**、保留可读 `name` 旁加权威 id、派生物化视图脚本生成不手改、
幂等可重跑、改实体后重跑 `links_normalize`→`links_audit`。

> 备注：summons 的 `damage_power`/`effect` 数据洞由 owner 另行补（与本计划独立，不阻塞）。

---

## Part A — location 升级为真 FK（先做）

### A1. 抽出共享解析器
把 `scripts/locations_refs.py` 里的 `normalize` / `strip_parens` / `build_resolver` /
`resolve` / `IGNORE` 抽到新模块 **`scripts/location_resolve.py`**，由 `locations_refs.py`、
`links_normalize.py`、`walkthrough_links.py` 共同 import。解析逻辑从此**只有一处**，杜绝漂移。
`locations_refs.py` 改为 `from location_resolve import ...`，行为不变。

### A2. 在 links_normalize.py 增加 location FK 回填边
沿用既有 `reinsert(entry, after_key, {...})` 幂等 in-place 插入（id 紧跟在自由文本之后）。
按实体基数选单值/多值：

| 实体 | 源自由文本字段 | 新增 FK 字段 | 基数 |
|---|---|---|---|
| djinn | `location.area` | `location.area_id` | 单值 |
| bosses | `encounters[].location` | `encounters[].location_id` | 单值（每 encounter）|
| shops | `name`（=地点）| `location_id`（顶层）| 单值 |
| equipment | `acquisition.location` | `acquisition.location_ids`（sorted 数组）| 多值（如 “Babi Lighthouse / Tunnel Ruins / Venus Lighthouse (Chimera Mage)”）|
| items | `acquisition.location` | `acquisition.location_ids` | 多值 |
| monsters | `found[]` | `found_ids`（sorted 数组）| 多值 |

规则：
- 自由文本为 `null`/缺失 → id 为 `null`/空数组，不算错。
- 命中 `IGNORE`（`b2`/`b3`/`various shops / mimics` 等）→ 不报 unresolved（沿用现有语义）。
- 单值实体若 `resolve()` 返回 >1，说明源数据异常 → 进 unresolved 报告（非静默吞掉）。
- 任何**非 IGNORE 且解析失败**的串 → unresolved，`main()` 退出非零（与现有边一致）。
  目标：0 unresolved（locations_refs 当前已 0 未匹配，应平移成立）。

### A3. locations_refs.py 改为从 FK 派生（可选但推荐）
回填后 `location_refs.json` 本质就是这些 `*_id(s)` 的 group-by。建议把 `locations_refs.py`
改成**读回填好的 id 直接反转**（不再自己 resolve），解析只留在 `links_normalize`。
**护栏**：改造后输出须与现状 **md5 一致**（已验证当前 0 未匹配，等价）。若想零风险，也可
让 locations_refs 仍走共享解析器、行为完全不变——二选一，推荐前者（单一解析路径）。
注意由此产生顺序依赖：`locations_refs.py` 须在 `links_normalize.py` 之后跑（符合“FK 回填是
最后一道 enrichment”）。

### A4. links_audit.py 增加 location FK 校验
仿现有 6 类 FK 检查：每个 `area_id`/`location_id`/`location_ids[]`/`found_ids[]` 必须存在于
`locations.json`；且自由文本 `resolve()` 结果与回填 id 一致（name↔id 一致性）。0 errors / exit 0；
做一次负向测试（改坏一个 id → 应报 dangling、exit 1）。

### A5. schema 更新
`schema/gs1_schema.md` 的 “Cross-Entity Links（foreign keys）” 总表加一行 location FK；
djinn/bosses/shops/equipment/items/monsters 各段字段表补 `*_id(s)` 字段（标注 links_normalize 生成）。

---

## Part B — 攻略链接层 walkthrough_links.json（后做）

新脚本 **`scripts/walkthrough_links.py`**，仿 `locations_refs.py` 的物化视图范式
（脚本生成、不手改、幂等 sorted、产出数据质量报告）。

### B1. 解析 gs1_walkthrough.md
按 `## Chapter N — Title`（含 Prologue/Epilogue/Appendix）切章，按 `### Location` 切地点块，
块内解析模板子块 **Enemies / Items / Djinn / Shop / Boss**（template 定义的固定结构）。

### B2. 实体解析（全部复用既有解析器/词表）
- 地点标题 → `location_id`：用 A1 的 `location_resolve`（同一套 `aliases` 词表）。
- **Djinn**（“Element — Name — note”）→ djinn id：按 djinn name 解析。
- **Items** → equipment|items id：复用 `links_normalize` 的 `gear` 解析器（equipment∪items 名字不重叠，已验证）。
- **Boss** → boss id；并按 boss+地点匹配出 `encounter_id`（多 encounter 如 Saturos）。
- **Enemies** → monsters id。
- **Shop** → 该地点的 shop id。
- 消歧沿用既有约定（boss 多 encounter；psynergy “Blast” 系列消歧已在 links_normalize 里）。

### B3. 产出
`data/gs1/walkthrough_links.json`：
```
{ "generated_by": "scripts/walkthrough_links.py",
  "note": "DERIVED ... 不手改", "source": "gs1_walkthrough.md",
  "chapters": [ { "chapter": "...", "locations": [
      { "location_id": "vault", "heading": "Vault",
        "djinn": [...], "items": [...], "equipment": [...],
        "monsters": [...], "bosses": [...], "shops": [...] } ] } ] }
```
+ **unmatched 报告**（解析不到的实体提及全部列出，逼着逐条理解——同 locations_refs 心法）。

### B4. 交叉校验（高价值副产物）
对每个地点，比对 `walkthrough_links[loc]` 与 `location_refs[loc]` 的实体集合，列出差异
（攻略提到但反向索引没有，或反之）。这是**免费的数据质量审计**（类似 fizz/Imil 那种洞察），
同时验证两层一致。差异进报告，不视为 fatal（攻略叙事粒度与实体源粒度本就可能不同）。

### B5. audit
在 `links_audit.py` 增一段（或脚本内）：walkthrough_links.json 里所有 id 必须存在于对应实体文件。

---

## 关键复用点（不要新造）

- `scripts/locations_refs.py`：`build_resolver` / `resolve` / `normalize` / `strip_parens` / `IGNORE`
  → 抽到 `scripts/location_resolve.py`。
- `scripts/links_normalize.py`：`reinsert`（幂等 in-place 插 id）、`norm`、`gear`（equipment∪items 解析）、
  unresolved-报告 + exit-code 范式。
- `scripts/links_audit.py`：只读质量门，扩展。

## 范围外（本次不做）
- `gs1_walkthrough_fable.md` / `_cn` 变体：只链 `gs1_walkthrough.md`。结构相同的话日后可复用同一 parser。
- token 精简派生视图、prose 内嵌 markdown 链接：均未选，不做。
- summons 数据洞：owner 另补，独立于本计划。

---

## 验证

**Part A**
1. `python scripts/links_normalize.py` → 0 unresolved、exit 0；连跑两次相关 JSON md5 稳定（幂等）。
2. `python scripts/locations_refs.py` → 若按 A3 改造，输出与改造前 md5 一致。
3. `python scripts/links_audit.py` → 0 errors、exit 0；负向测试：改坏一个 location id → 报 dangling、exit 1，恢复后回 0。
4. 抽样：`gaia-blade.acquisition.location_ids` 含 `venus-lighthouse`；某多地点 equipment 落到多个 id；djinn `granite.location.area_id` = `kolima`。

**Part B**
5. `python scripts/walkthrough_links.py` → 写出 walkthrough_links.json；unmatched 报告逐条可解释（目标趋近 0，残留须能说清）。
6. 章节数与 gs1_walkthrough.md 一致（18 章）；连跑两次 md5 稳定。
7. 交叉校验报告：抽查 Mercury Lighthouse —— 攻略侧 djinn 应与 `location_refs.json` 的 `mercury-lighthouse` 大体吻合，差异有解释。
8. 抽样图查询：由 walkthrough_links “Chapter 2 / Vault” → bandit boss id + 该地点 djinn/items id，能跳回各实体文件。

---

## 执行顺序建议
Part A（A1→A2→A3→A4→A5）一个 session 跑完并通过审计 → 再做 Part B（B1→B5）。
两部分都满足：改实体后重跑 `links_normalize.py` → `locations_refs.py` → `links_audit.py`。
