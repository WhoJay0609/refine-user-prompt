# Refactoring Examples

Use these examples to calibrate semantic preservation, proportional structure, and the mandatory "show the refined prompt before acting" rule. Do not copy their domain details into unrelated requests.

## Short answer after refinement

Raw input:

```text
帮我把这篇文章总结一下，要短一点，重点说结论和限制。
```

Response shape:

```markdown
### 重构后的提示词

建议：执行模式：`refine_then_answer`；模型：`gpt-5.6-luna`；思考强度：`low`；理由：任务目标明确、输出短且不需要复杂工具或副作用。

总结这篇文章。先给核心结论，再说明关键限制；保留理解结论所必需的证据，省略背景铺垫、重复解释和次要细节。

[then provide the summary]
```

Why this shape works: the refined prompt is visible, then the agent answers directly because no side effect is needed.

## Ordinary execution after refinement

Raw input:

```text
看看这个登录 bug，先看看代码，找原因，然后修一下。别改接口，也别碰支付。
```

Response shape:

```markdown
### 重构后的提示词

建议：执行模式：`refine_then_execute`；模型：`gpt-5.6-terra`；思考强度：`medium`；理由：需要代码诊断、范围控制和测试验证，但停止条件明确且不需要持久 Goal。

目标：端到端诊断并修复登录故障。

成功标准：
- 找到并解释根因；
- 实施范围内的最小修复；
- 保持现有公开接口不变；
- 运行最相关的测试，或说明无法运行的原因。

约束与授权：
- 只检查和修改登录相关代码；
- 不要修改支付代码；
- 外部写入、破坏性操作或实质性扩大范围前必须确认。

输出：
先给结果，再概述根因、修改文件、验证结果和剩余风险。

[then inspect files, edit only authorized files, and validate]
```

Why this shape works: the task authorizes ordinary local execution but preserves exclusions and confirmation gates.

## Goal creation explicitly authorized

Raw input:

```text
把这个研究项目从方案设计、数据准备、实验执行、结果分析一直做到论文初稿。实验可能跑几天，中断后要能继续；每个阶段通过验收后再进入下一阶段，失败的实验要记录并重试。润色后如果你判断需要目标，就创建 Goal 开始做。
```

Response shape:

```markdown
### 重构后的提示词

建议：执行模式：`refine_then_create_goal`；模型：`gpt-5.6-sol`；思考强度：`high`；理由：任务包含多阶段验收、长时间实验、中断恢复和失败重试，且用户已明确授权在需要时创建 Goal。

目标：
完成研究方案设计、数据准备、实验执行、结果分析和论文初稿，并保持阶段之间的证据与决策连续性。

背景与输入：
使用当前项目资料、数据、实验配置、运行日志和已有研究上下文；开始前先确认缺失的关键项目路径、数据入口或实验约束。

成功标准：
- 每个阶段都有明确交付物和验收条件；
- 只有当前阶段通过验收后才进入下一阶段；
- 实验运行状态、失败原因、重试记录和有效结果可恢复；
- 论文初稿中的结论与已验收实验结果一致。

约束与授权：
- 不要跳过数据和实验完整性检查；
- 不要把失败或未验证结果写成论文结论；
- 可直接执行项目范围内的读取、分析、实验准备、实验运行和本地验证；
- 外部发布、付费资源或实质性改变研究目标前必须确认。

工具与验证：
查阅项目文件、实验配置、数据说明和运行日志；按阶段运行必要检查或实验；记录失败、重试、有效结果和不能运行的验证原因。

输出：
使用中文。按阶段给出交付物、关键决策、验证结果、剩余风险和论文初稿。

停止规则：
论文初稿、实验依据和阶段验收记录均完成后停止；遇到会改变研究目标、验收标准、授权范围或资源成本的阻塞时请求确认。

[then call create_goal with a compact objective derived from the refined prompt]
```

Why this shape works: Goal creation is allowed because durable state is useful and the user explicitly authorized it.

## Paper revision proactively creates Goal

Raw input:

```text
帮我把这篇论文按审稿意见改好，检查实验结论和引用，最后编译 PDF，改完直接给我结果。
```

Response shape:

```markdown
### 重构后的提示词

建议：执行模式：`refine_then_create_goal`；模型：`gpt-5.6-sol`；思考强度：`high`；理由：用户已授权实际修改论文，任务涉及审稿意见、全文一致性、实验结论、引用和 PDF 编译，适合用 Goal 保留阶段状态与验收记录。

目标：
按审稿意见完成论文修订，确保实验结论、引用、正文、图表和最终 PDF 一致，并交付可检查的修改结果。

背景与输入：
使用当前论文源文件、审稿意见、实验结果、引用库、图表和构建配置；开始前确认论文主文件、审稿意见位置和编译命令。

成功标准：
- 审稿意见中的实质问题均有对应修改或解释；
- 实验结论、数值、引用、图表和正文表述一致；
- 论文能够完成指定编译或明确说明无法编译的原因；
- 输出修改摘要、验证结果和剩余风险。

约束与授权：
- 不要夸大实验结论或添加无依据声明；
- 不要改动无关项目文件；
- 可直接修改论文相关本地文件并运行本地验证；
- 外部提交、远程推送、付费资源或大规模实验前必须确认。

工具与验证：
查阅论文源文件、审稿意见、引用库、图表和实验结果；运行相关文本/引用/编译检查；记录无法运行的检查及替代验证。

输出：
使用中文。先给完成结果，再列修改摘要、关键证据、编译/验证结果和待用户确认的剩余事项。

停止规则：
审稿意见处理、论文修订、验证和结果汇总完成后停止；缺少审稿意见、主文件、实验依据或授权边界时先询问。

[then call create_goal with a compact objective derived from the refined prompt]
```

Why this shape works: even without the word `Goal`, the user authorized execution and the paper task has durable multi-stage revision, evidence, and build gates.

## Bounded paragraph edit stays ordinary

Raw input:

```text
帮我润色这段论文，写得更专业一点，但不要改实验数字，也别把结论吹大。
```

Response shape:

```markdown
### 重构后的提示词

建议：执行模式：`refine_then_answer`；模型：`gpt-5.6-luna`；思考强度：`low`；理由：这是边界明确的短文本改写，不需要持久状态或 Goal。

润色给定论文段落，提高表达清晰度、连贯性、准确性和专业性。

优先保留原有实验数字、事实性陈述、结论强度、段落功能和引用关系。不要添加新证据、强化结论、使用宣传性措辞或增加新章节。

只返回使用原文语言改写后的段落。

[then provide the revised paragraph]
```

Why this shape works: paper domain alone is not enough; the work is a bounded paragraph edit.

## Goal useful but not authorized

Raw input:

```text
持续推进这个实验，失败要重试，中断后继续，最后给我完整报告。
```

Response shape:

```markdown
### 重构后的提示词

建议：执行模式：`refine_only`；模型：`gpt-5.6-sol`；思考强度：`high`；理由：任务适合 Goal，但用户尚未明确授权创建 Goal。

目标：
持续推进实验直到完成，并保留中断恢复、失败重试和最终报告所需的状态与证据。

背景与输入：
[当前实验项目、配置、数据、日志和运行环境。若缺少路径或实验入口，先询问。]

成功标准：
- 实验完成或达到用户定义的停止条件；
- 失败原因、重试记录和有效结果可追踪；
- 最终报告中的结论有运行证据支持。

约束与授权：
- 不要伪造或扩大实验结论；
- 不要执行高成本、外部发布、删除或远程写入操作，除非另有确认；
- 创建 Goal 前必须得到明确授权。

工具与验证：
检查实验配置、运行日志、状态文件和验证脚本；记录无法运行的验证原因。

输出：
使用中文，按阶段报告进展、证据、失败、重试和最终结论。

停止规则：
完成最终报告后停止；缺少实验入口、资源授权或 Goal 创建授权时先询问。

### 待确认项

- 这个任务适合创建 Goal。是否授权我基于上述提示词创建 Goal 并开始执行？
```

Why this shape works: the skill may recommend a Goal, but without explicit authorization it must stop before `create_goal`.

## No execution requested

Raw input:

```text
把这个项目整理好然后发出去，先给计划，不要动文件。
```

Response shape:

```markdown
### 重构后的提示词

建议：执行模式：`refine_only`；模型：`gpt-5.6-terra`；思考强度：`medium`；理由：用户明确要求先给计划且不要动文件。

目标：制定项目整理与发布前准备计划，不修改文件、不执行发布。

成功标准：
- 明确“整理好”和“发出去”可能包含的工作项；
- 标出需要用户确认的发布目标、范围和授权；
- 给出可执行但尚未执行的分阶段计划。

约束与授权：
- 不要修改文件；
- 不要发布、推送、部署或发送给外部对象；
- 等用户确认发布目标和执行授权后再动手。

输出：
使用中文，先给计划，再列待确认项。
```

Why this shape works: explicit no-execution wording overrides execution or Goal creation.

## Material ambiguity

Raw input:

```text
把这个项目整理好然后发出去。
```

Required response before refinement:

```markdown
### 待确认项

- “发出去”具体指推送代码、发布软件包、部署服务，还是发送给某个人？目标不同会改变授权和验收范围。
```

Why this shape works: guessing would authorize a materially different external action.
