# GS2 Appendix Triage Report

## 评估结论概述
基于对各大语料库的附录（Appendices）和数据表的评估，**我们完全可以补齐目前缺失的 4 个数据缺口**。其中，`telago` 和 `super-slash` 的附录部分数据最为完备，是填补这 4 个缺口的最佳选择。

## 各语料库评测详情

| 数据源 (Guide) | 评估章节 / 模块 | 1. 职业专属 Psynergy | 2. Classes Layer3 (Djinn配比) | 3. Djinn 战斗效果 | 4. Summons 获取地点 | 综合结论与建议 |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **telago** | `24-djinn-descriptions.md` 到 `33-psynergy-spells.md` | ✅ **包含** | ✅ **包含** | ✅ **包含** | ✅ **包含** | **最佳提取源**。33章节包含了非常完整的Psynergy字典（含 PP, Range, Element, Effect），而26章节详尽列出了所有职业的Djinn需求及按等级习得的专属法术。24和25章节也完美覆盖了Djinn效果和召唤兽位置。 |
| **super-slash** | `06-item-list.md` 到 `14-enemy-list.md` | ✅ **包含** | ✅ **包含** | ✅ **包含** | ❌ 缺失 | **次佳提取源（可作为交叉验证）**。13章节包含了带描述的Psynergy字典，11章节包含了Classes需求的Djinn以及习得列表，10章节包含Djinn描述。但该作者没有专门的Summons附录。 |
| **strawhat** | `41-djinn.md` 到 `44-classes.md` | ⚠️ **部分** | ✅ **包含** | ✅ **包含** | ✅ **包含** | **可用作补充**。43章节的Psynergy列表自带完整属性（PP/Range/Element/Effect），但44章节作者明确表示“嫌麻烦”没有列出各职业所学法术。可用于补全Djinn和Summons数据。 |
| **autocon** | `129` 到 `322` 散落的独立文件 | ❌ 缺失 | ✅ **包含** | ✅ **包含** | ✅ **包含** | **不推荐**。文件过度碎片化，且缺乏集中的Psynergy字典（只有各职业零散的习得列表，没有PP/Range/Effect等关键数值）。 |
| **darthmarth**| `30-djinn-guide.md` 到 `36-psynergy-guide.md` | ❌ 缺失 | ⚠️ **不全** | ✅ **包含** | ✅ **包含** | **不推荐**。`36-psynergy-guide.md` 是空章节，且 `35-class-guide.md` 只编写了基础职业便太监了。 |

## 针对 4 个缺口的后续提取建议
1. **缺口 1 (职业专属 Psynergy)**：使用 `telago` 提取。通过交叉匹配 `33-psynergy-spells.md`（查属性）和 `26-class-psynergy-effects.md`（查从属），完美获取这36+条专属法术的完整数据。
2. **缺口 2 (Classes Layer3 需求)**：使用 `telago` 或 `strawhat` 提取。两者都有格式工整的Djinn组合配比数据（如 Venus x2, Jupiter x4）。
3. **缺口 3 (Djinn `battle_effect`)**：四个数据源均有良好覆盖，可使用 `telago/24-djinn-descriptions.md` 或 `strawhat/41-djinn.md`。
4. **缺口 4 (Summons `acquisition.location`)**：推荐使用 `strawhat/42-summons.md` 或 `telago/25-about-the-summon.md`，两者提取起来都很直观。
