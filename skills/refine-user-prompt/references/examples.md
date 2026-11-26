# Refine-only examples

## Bounded rewrite

Raw request:

```text
帮我把这篇文章总结一下，要短一点，重点说结论和限制。
```

Final response:

```markdown
### 重构后的提示词

建议：模型：`gpt-5.6-luna`；思考强度：`low`；理由：任务边界清晰且不需要复杂工具。

总结给定文章。先给核心结论，再说明关键限制；保留理解结论所必需的证据，省略背景铺垫和重复解释。使用中文，控制在 200 字以内。
```

Stop here. Do not summarize the article in the same turn.

## Tool-using future task

Raw request:

```text
润色后直接检查这个任务的状态，再运行测试并给我结论。
```

Final response:

```markdown
### 重构后的提示词

建议：模型：`gpt-5.6-terra`；思考强度：`medium`；理由：后续执行需要状态读取、测试和证据归纳。

检查指定任务的当前状态，读取其最终输出和错误信息；随后运行最相关的测试。根据直接证据说明任务是否完成、测试是否通过及仍存风险。不要修改无关文件；无法运行测试时说明原因和替代验证。

执行连续性：
最多发送一次启动说明。工具结果、错误、重试、续写或恢复后，直接推进到下一项未完成动作，只报告实质性新证据。不要重复本提示词、计划、skill 调用或语义相同的启动说明；没有新证据时，禁止第三次输出语义相同的消息。
```

Stop here even though the raw request says to execute. A later ordinary user message may start execution.
