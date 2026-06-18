## CONTEXT

你可以先看下：
- lore-engine/README.MD
- lore-engine/docs/gs1_wrapup_gs2_kickoff_plan.md
- lore-engine/docs/gs2/gs2_plan.md

这几个是Context最相关的。

## MY PROGRESS

我现在刚开始收集raw：
- 目前我copy过来了1+10个，都在raw/gs2下面
    - `Golden Sun The Lost Age – Guides and FAQs` 这个是网站的目录页，我觉得你的目录也可以build based on this.
    - 另外有10个`Guide and Walkthrough by xxx`, 放在raw/gs2/里面一个我新建的子文件夹了

### GUIDE AND WALKTHROUGH

我最开始有尝试简单的update一下formatting，比如Telago那篇，但实在是不简单。
- 都太长了。
- 而且里面本身就有各种符号，比如`=======`, `-------`, `####`这些markdown的格式符号。
- 所以这个很不好弄。

然后我就放弃了，但有个好消息，就是这10篇都是comprehensive的，里面都有table of contents。
- 所以我决定把table of contents起码我update一下format，这样方便llm阅读里面有些啥。
- 这些都在前100或者几百行，很容易阅读到。

并且，我把所有的table of contents统一了一下。

我在开始的地方加了：
```
## TABLE OF CONTENTS
```

我在结尾处加了：
```
---

END OF TABLE OF CONTENTS

---
```

这样起码llm阅读的时候会容易知道table of contents在哪？

## NEXT STEP

我现在的想法是：
1. 先试试让LLM读这些，populate一下frontmatter，这个应该比较容易。
2. LLM是否能对这些很raw的txt进行一些格式上的整理？稍微整理成markdown格式？

我不知道如果是做这两个的话，token usage需要的量如何？因为都是几千几万行的，LLM会要全部读吗？还是是会选择性的读？

如果量特别大的话，我不太想用Claude的Usage
- 起码10篇特别特别长的不用。
- 我怕我Proplan的usage兜不住太多，like 5-hours和weekly的usage会比较快的用完。

我有Gemini的Pro Plan Subscription。这个任务，是不是也可以交给Gemini解决？我应该是可以在VSCode里面用Gemini的CLI的。

还有一个想问的，就是这10篇，我们需不需要用LLM把这些先按topics拆碎？这样就不是里面啥都有，比如某一篇里面，有12个topics，那么我就拆成12篇小的。

你怎么看？