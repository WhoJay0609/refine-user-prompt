# Refactoring Examples

Use these examples to calibrate semantic preservation and proportional structure. Do not copy their domain details into unrelated requests.

## Short request

Raw input:

```text
帮我把这篇文章总结一下，要短一点，重点说结论和限制。
```

Refined prompt:

```text
总结这篇文章。先给核心结论，再说明关键限制；保留理解结论所必需的证据，省略背景铺垫、重复解释和次要细节。
```

```markdown
### 模型配置建议

- 任务难度：低
- 模型：`gpt-5.6-luna`
- 思考强度：`low`
- 原因：任务目标明确、输出短且不需要复杂工具或多源判断。

该配置仅为建议，不会自动切换模型或思考强度。
```

Why this shape works: the request is already clear, so a large template would add noise.

## Repository change

Raw input:

```text
看看这个登录 bug，先看看代码，找原因，然后修一下。别改接口，也别碰支付。
```

Refined prompt:

```text
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
```

```markdown
### 模型配置建议

- 任务难度：中等
- 模型：`gpt-5.6-terra`
- 思考强度：`medium`
- 原因：需要代码诊断、边界保持和测试验证，但当前范围仍然明确且有限。
- 升级条件：如果根因涉及认证安全、跨服务状态或高影响回归，升级为 `gpt-5.6-sol` + `high`。

该配置仅为建议，不会自动切换模型或思考强度。
```

Why this shape works: it preserves the two explicit exclusions and turns generic process narration into completion criteria.

## Grounded research

Raw input:

```text
查一下最近有哪些多模态剪枝的方法，最好都列出来，要有引用，不确定的别瞎说。
```

Refined prompt:

```text
目标：形成一份当前且有证据支持的多模态模型剪枝方法综述。

成功标准：
- 覆盖主要方法类别及代表性工作；
- 区分来源直接支持的事实与推断；
- 说明检索范围和重要覆盖限制；
- 按剪枝对象、粒度、校准数据、训练需求和评测设置等统一维度比较方法。

证据与检索：
- 重要结论使用当前的一手来源；
- 引用紧跟其支持的结论；
- 明确说明来源冲突；
- 不要把缺少证据表述成事实上的“不存在”；
- 如果无法证明穷尽性，将“所有方法”收窄为实际检索范围内有证据支持的方法。

输出：
使用中文。先给出简洁分类，再提供比较表和主要证据缺口。

停止规则：
主要类别和代表性一手来源均有支持后停止。只有缺少必需的比较字段或重要的新近方法类别时才继续检索。
```

```markdown
### 模型配置建议

- 任务难度：高
- 模型：`gpt-5.6-sol`
- 思考强度：`high`
- 原因：任务需要当前检索、多源证据核对、统一分类和对穷尽性边界的审慎判断。
- 升级条件：只有在评测表明遗漏关键类别或证据冲突仍无法解决时，才比较 `xhigh`。

该配置仅为建议，不会自动切换模型或思考强度。
```

Why this shape works: it converts an unsafe exhaustive claim into an explicit coverage contract without weakening the user's research goal.

## Editing with preservation

Raw input:

```text
帮我润色这段论文，写得更专业一点，但不要改实验数字，也别把结论吹大。
```

Refined prompt:

```text
润色给定论文段落，提高表达清晰度、连贯性、准确性和专业性。

优先保留原有实验数字、事实性陈述、结论强度、段落功能和引用关系。不要添加新证据、强化结论、使用宣传性措辞或增加新章节。

只返回使用原文语言改写后的段落。
```

```markdown
### 模型配置建议

- 任务难度：低
- 模型：`gpt-5.6-luna`
- 思考强度：`low`
- 原因：这是边界明确的文本改写，关键要求是保持事实和结论强度。

该配置仅为建议，不会自动切换模型或思考强度。
```

Why this shape works: preservation priorities matter more than a generic “professional” persona.

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

## Goal mode recommended

Raw input:

```text
把这个研究项目从方案设计、数据准备、实验执行、结果分析一直做到论文初稿。实验可能跑几天，中断后要能继续；每个阶段通过验收后再进入下一阶段，失败的实验要记录并重试。
```

Refined prompt:

```text
目标：完成研究方案设计、数据准备、实验执行、结果分析和论文初稿，并保持阶段之间的证据与决策连续性。

成功标准：
- 每个阶段有明确交付物和验收条件；
- 只有当前阶段通过验收后才进入下一阶段；
- 实验运行状态、失败原因、重试记录和有效结果可恢复；
- 论文初稿中的结论与已验收实验结果一致。

约束与授权：
- 不要跳过数据和实验完整性检查；
- 不要把失败或未验证结果写成论文结论；
- 外部发布、付费资源或实质性改变研究目标前必须确认。

停止规则：
论文初稿、实验依据和阶段验收记录均完成后停止；遇到会改变研究目标或验收标准的阻塞时请求确认。
```

```markdown
### 模型配置建议

- 任务难度：高
- 模型：`gpt-5.6-sol`
- 思考强度：`high`
- 原因：任务包含研究设计、实验判断、证据约束和论文结论一致性，错误会跨阶段传播。
- 升级条件：只有最关键的实验解释或论文结论审查仍存在重大冲突时，才比较 `xhigh`。

该配置仅为建议，不会自动切换模型或思考强度。
```

Execution-mode recommendation:

```markdown
### 执行模式建议

建议使用目标模式。

原因：
- 任务包含多个相互依赖且需要逐阶段验收的阶段；
- 实验可能长时间运行，并要求中断恢复、失败记录和重试；
- 最终论文结论依赖持久保存的实验状态与证据。

建议目标：端到端完成该研究项目的方案、数据、实验、分析和论文初稿，并以阶段验收和可恢复实验状态保证证据连续性。

该提示仅为建议，不会自动创建或执行目标。如需启用，请明确要求创建目标。
```

Why this shape works: Goal mode provides material value through durable state, dependent milestones, recovery, and acceptance gates.

## Goal mode omitted

Raw input:

```text
检查这个函数为什么在空列表时报错，修复后运行对应单元测试，不要改公开接口。
```

Refined prompt:

```text
诊断并修复该函数处理空列表时的错误。保留现有公开接口，实施范围内的最小修改，并运行对应单元测试；如果测试无法运行，说明原因和下一项最有效的验证。
```

```markdown
### 模型配置建议

- 任务难度：中等
- 模型：`gpt-5.6-terra`
- 思考强度：`medium`
- 原因：需要理解代码、实施修复和验证，但范围小、停止条件明确且不需要持久状态。

该配置仅为建议，不会自动切换模型或思考强度。
```

Why this shape works: this is a bounded change with a clear validation path. Omit the execution-mode section because Goal mode would add overhead without durable orchestration value.
