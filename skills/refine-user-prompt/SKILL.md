---
name: refine-user-prompt
description: Restructure a user's raw request into a lean, outcome-first prompt while preserving intent, facts, scope, language, authorization, evidence requirements, and output needs; recommend a GPT-5.6 model variant and reasoning effort from task difficulty; and recommend Codex Goal mode when durable orchestration would materially help. Use when the user asks to 梳理、整理、优化、重写或改写提示词, convert an informal request into a GPT-5.6-ready prompt, remove repetition or contradictions, clarify success and stop rules, or assess model, reasoning, or Goal-mode fit without executing the task, switching models, or creating a Goal.
---

# Refine User Prompt

## Contract

Transform the request; do not execute the transformed task unless the user explicitly asks for both refinement and execution.

Preserve, in this priority order:

1. The user's intended outcome and requested artifact.
2. Explicit facts, values, names, paths, dates, claims, and examples.
3. Scope, exclusions, permissions, approval gates, and side-effect boundaries.
4. Evidence, citation, validation, language, format, length, genre, and tone requirements.

Never silently add facts, permissions, deliverables, tools, deadlines, or quality claims. Label a bounded assumption when it is useful and low risk. Ask for the smallest missing fact when an ambiguity would materially change the outcome, scope, side effects, evidence standard, or output contract.

## Workflow

### 1. Extract the prompt contract

Identify only fields that affect behavior:

- user-visible goal;
- necessary context and available evidence;
- success criteria and completion bar;
- constraints, exclusions, and authorization boundaries;
- tool, retrieval, or validation requirements;
- required output shape, language, length, and tone;
- retry, fallback, clarification, and stopping conditions.

Keep explicit user values verbatim unless the user asks to normalize them.

### 2. Resolve ambiguity proportionally

Distinguish three cases:

- **Complete enough:** refine immediately.
- **Low-risk omission:** use a narrow, visible assumption only when needed.
- **Material ambiguity or contradiction:** ask one smallest useful question before producing a misleading prompt.

Do not ask merely because an optional section is empty. Do not replace an unresolved user decision with a universal default or keyword rule.

### 3. Simplify before adding structure

Remove:

- repeated statements of the same rule;
- generic process narration that does not change behavior;
- examples that add no unique constraint;
- irrelevant tools and tool descriptions;
- broad style labels that are already expressed by concrete writing choices.

Keep true invariants. Use absolute words such as `must`, `never`, `only`, `必须`, and `禁止` only for genuine invariants. Convert judgment calls into compact decision rules, but preserve a mandatory sequence when the sequence itself is part of the requirement.

### 4. Structure to the task's complexity

Keep a simple request to one sentence or a short list. The refined prompt must be directly usable whether or not Goal mode is recommended.

For complex non-Goal requests, select only the useful sections from this order:

```text
Role: [include only when role or domain context changes behavior]

Personality and collaboration: [include only when requested]

Goal: [user-visible outcome]

Context and evidence: [necessary inputs, sources, files, or known facts]

Success criteria: [conditions that must hold before completion]

Constraints and authorization: [scope, safety, permissions, side effects]

Tools and validation: [routing, prerequisites, checks, fallbacks]

Output: [format, language, structure, length, tone]

Stop rules: [when to answer, retry, ask, narrow, abstain, or stop]
```

When Goal mode is recommended, use this fixed template for the refined prompt. Keep the Chinese headings exactly for Chinese requests; translate them only when the source request is not Chinese.

```text
目标：
[最终希望获得什么结果]

背景与输入：
[必要的项目、数据、文件和上下文]

成功标准：
- [完成后必须成立的条件]
- [必须覆盖的内容]
- [必须通过的验证]

约束与授权：
- [不能改变什么]
- [哪些操作可以直接执行]
- [哪些操作必须先征得我同意]

工具与验证：
[需要查阅什么、运行什么测试、如何检查结果]

输出：
[语言、结构、长度和格式]

停止规则：
[什么时候可以结束；缺什么信息时再问我]
```

Omit empty or behavior-neutral sections. Describe the destination before the method and leave room for the model to choose an efficient path.

### 5. Recommend a model and reasoning effort

Assess the underlying task after refining its contract. Base difficulty on the combination of:

- ambiguity and semantic judgment;
- dependency depth and number of interacting constraints;
- tool orchestration, retrieval, and verification burden;
- context volume and cross-file or cross-source synthesis;
- consequence of error, reversibility, and evidence requirements;
- latency, throughput, and cost priorities stated by the user.

Do not infer difficulty from prompt length, number of listed steps, or domain labels alone. Before increasing reasoning effort, check whether the refined prompt is missing a success criterion, dependency rule, tool route, or verification loop.

Preserve an explicitly requested model or deployment constraint. Otherwise, when the current surface exposes the GPT-5.6 family, use this compact default rubric:

- **`gpt-5.6-luna`:** choose for well-specified, routine, high-volume, or latency-sensitive transformations such as formatting, extraction, classification, short summaries, and small low-risk edits. Prefer the lowest available effort, normally `low`; use `none` only when the active API surface supports it and the task is deterministic.
- **`gpt-5.6-terra`:** choose as the balanced default for everyday coding, analysis, research assistance, and moderate tool use with several constraints. Start at `medium`; use `low` when latency matters and quality remains sufficient.
- **`gpt-5.6-sol`:** choose for flagship-quality work involving deep ambiguity, difficult debugging, architecture, complex optimization, high-value review, deep research, or high consequences of error. Start at `medium` or `high`; use `xhigh` only when the extra reasoning has a clear expected benefit.

Reserve `max` for the hardest quality-first workloads that need extensive exploration and verification; never recommend it globally. The `gpt-5.6` alias routes to `gpt-5.6-sol`, but prefer an explicit variant in recommendations. Recommend only models and effort levels available on the active surface. If availability is unknown, state the assumption instead of inventing support, pricing, or latency.

For a mixed workflow, recommend one default configuration and at most one escalation condition. Keep model choice, reasoning effort, and Goal-mode suitability separate: durability does not imply cognitive difficulty, and difficulty does not imply a need for durable state.

Treat the configuration as advisory. Never claim to switch the active model or reasoning effort from this recommendation.

### 6. Recommend Goal mode only when it materially helps

Evaluate the underlying task after refining its contract. Recommend Codex Goal mode when durable orchestration is materially useful, especially when the task has one or more of these properties:

- several dependent phases or milestones whose accepted results constrain later work;
- work expected to span multiple turns or long-running operations and resume after interruption;
- repeated monitoring, experiments, evaluations, retries, or recovery that must preserve state;
- multiple dependent deliverables with explicit acceptance and closeout gates;
- an explicit terminal condition that requires durable progress tracking rather than a single bounded response.

Do not recommend Goal mode merely because the task is long, technically difficult, contains several steps, or is being rewritten by this skill. Omit the recommendation for bounded questions, reviews, plans, diagnoses, single changes, or tasks that can reasonably finish in the current task with ordinary validation.

Use judgment from the task shape rather than keyword matching. If a missing fact materially determines suitability, ask the smallest question instead of making a speculative recommendation.

Keep recommendation separate from authorization. Never create a Goal, invoke `goal-entry`, update Goal state, or begin executing the refined task unless the user explicitly requests that separate action.

### 7. Preserve domain-specific boundaries

Apply these rules only when relevant:

- For grounded work, require support for material claims, place citations near supported claims, label inference, expose source conflicts, and narrow unsupported conclusions instead of guessing.
- For coding or artifact creation, name the most relevant validation and require an explanation when it cannot run.
- For answer, explanation, review, diagnosis, or planning requests, do not imply implementation authority.
- For change, build, or fix requests, preserve authorized in-scope local actions and explicit confirmation gates for external, destructive, costly, or scope-expanding actions.
- For editing or rewriting, preserve the requested artifact, factual claims, genre, length, and structure before improving clarity.
- For tool-heavy work, expose only relevant tools. Use decision rules for retrieval, fallback, parallel reads, and stopping instead of requesting tool use for its own sake.

## Output

By default, return only the ready-to-use prompt under a short heading in the source request's language. For a Chinese request, use:

```markdown
### 重构后的提示词

建议：目标模式：[建议使用 / 普通对话即可]；模型：`[one explicit available model]`；思考强度：`[one available reasoning effort]`；理由：[one concise task-specific reason]

[ready-to-use prompt]
```

Put the recommendation first and keep it to one line. Always recommend one default model configuration for sufficiently specified tasks. Include Goal-mode suitability in that same line; do not add a separate model or execution-mode section.

Use `普通对话即可` when Goal mode would add no material value. Use `建议使用` only when durable orchestration materially helps. The recommendation is advisory: it does not create a Goal, switch models, or change reasoning effort.

When Goal mode is recommended, the prompt after the first line must use the fixed Goal-mode template from the workflow and must remain directly usable by the user. When Goal mode is not recommended, the prompt after the first line can remain a compact sentence or proportional sectioned prompt.

Preserve the source request's language, including headings, unless the user requests another language. Add a localized `待确认项` / `Open questions` section only when material information remains unresolved. For a Chinese request, use:

```markdown
### 待确认项

- [the smallest question or unresolved conflict]
```

Choose one default, not a menu. If one concrete escalation condition would materially help, incorporate it briefly in the ready-to-use prompt's `工具与验证` or `停止规则` section instead of adding a separate recommendation block. If a material ambiguity prevents a responsible difficulty or Goal-mode assessment, ask the smallest question first and defer the recommendation.

Do not add a change log, rationale, score, or prompt-engineering lecture unless requested. If the user asks for both a refined prompt and an explanation, place the ready-to-use prompt first.

## Final Check

Before responding, verify:

- the refined prompt is semantically equivalent to the user's request;
- no explicit fact, value, exclusion, or approval boundary was lost;
- no fact, authority, deliverable, or tool was invented;
- duplicate or contradictory instructions were removed or surfaced;
- success and stopping conditions are sufficient for the task;
- the structure is no more elaborate than the task requires;
- the first line states Goal-mode suitability, model, reasoning effort, and one concise reason;
- the model and effort recommendation matches task difficulty, risk, latency, cost, and current availability;
- `max` is reserved for a concrete hardest-quality-first reason rather than used as a default;
- no model or reasoning setting was claimed to be changed automatically;
- any Goal-mode recommendation is justified by durable orchestration needs rather than complexity alone;
- any Goal-mode prompt uses the fixed template and remains directly usable;
- no Goal was created, invoked, or executed from the recommendation;
- the output can be copied and used directly.

For representative coding, research, rewriting, model-selection, Goal-mode, and short-input transformations, read [references/examples.md](references/examples.md) only when an example is needed.
