---
name: refine-user-prompt
description: Refine a user's raw request into a lean, outcome-first execution prompt, show the refined prompt before acting, then either answer/execute from that prompt or create a Codex Goal when authorized or strongly warranted by an authorized long-horizon task. Preserve intent, facts, scope, language, authorization, evidence requirements, and output needs; recommend a GPT-5.6 model variant and reasoning effort. Use when the user asks to 梳理、整理、优化、重写或改写提示词, convert an informal request into a GPT-5.6-ready prompt, refine then execute, proactively decide whether to create a Goal, or clarify success criteria and stop rules.
---

# Refine User Prompt

## Contract

Transform the request into a refined execution prompt, show that prompt to the user, then follow the authorized execution mode.

Use one of four modes:

- `refine_only`: show the refined prompt and stop when the user asks only for rewriting, planning, or no execution.
- `refine_then_answer`: show the refined prompt, then answer directly for bounded non-mutating work.
- `refine_then_execute`: show the refined prompt, then execute ordinary authorized work while preserving all confirmation gates.
- `refine_then_create_goal`: show the refined prompt, then create a Codex Goal when Goal creation is explicitly authorized or when the user has authorized execution and the task is clearly durable-goal-shaped.

Never hide the refined prompt. Never treat vague complexity as permission to create a Goal. Never create a Goal, mutate files, call external services, push, delete, install, spend money, or run high-cost jobs unless the original user request or a later confirmation authorizes that class of action.

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

### 6. Decide execution mode and Goal creation

Evaluate the underlying task after refining its contract. Use `refine_then_create_goal` when either path applies:

1. **Explicit Goal path:** Goal mode is materially useful and the user explicitly authorizes creating a Goal, such as `润色后如果需要就创建 Goal`, `自动创建目标`, `创建 Goal 后执行`, or equivalent wording.
2. **Proactive Goal path:** the user authorizes execution or says to directly use the refined prompt, and the task is clearly durable-goal-shaped. In this path, Goal creation does not need the word `Goal`, but it still must preserve all operation-level confirmation gates.

Goal mode is materially useful especially when the task has one or more of these properties:

- several dependent phases or milestones whose accepted results constrain later work;
- work expected to span multiple turns or long-running operations and resume after interruption;
- repeated monitoring, experiments, evaluations, retries, or recovery that must preserve state;
- multiple dependent deliverables with explicit acceptance and closeout gates;
- an explicit terminal condition that requires durable progress tracking rather than a single bounded response.

Treat paper, thesis, manuscript, rebuttal, grant, patent, or long-form technical-document revision as durable-goal-shaped when the request asks to actually revise or finish the artifact and includes any of these signals:

- cross-section or cross-file consistency, references, figures, tables, experiments, claims, rebuttal points, supplement, or compilation must stay synchronized;
- multiple passes are expected, such as review, rewrite, verify, compile, polish, and closeout;
- quality gates matter, such as submission readiness, reviewer response, evidence/claim boundaries, citation checks, LaTeX/PDF/DOCX build, or final artifact delivery;
- the work is likely to span many edits or multiple turns and needs resumable state.

For these paper-like tasks, prefer `refine_then_create_goal` over `refine_then_execute` when execution is authorized, even if the user phrased it as “改论文”, “润色全文”, “把论文改好”, “按意见修改”, or “推进到可投稿”. Keep simple paragraph editing, short abstract rewriting, grammar polishing, or a single bounded section edit as `refine_then_answer` or `refine_then_execute`.

Use `refine_then_execute` for ordinary authorized implementation, debugging, review fixes, document generation, or local validation that can proceed in the current task without durable Goal state.

Use `refine_then_answer` for bounded answers, explanations, diagnoses, reviews, summaries, and rewrites that do not require file edits or side effects.

Use `refine_only` when the user says `先给计划`, `不要执行`, `只润色`, `只分析`, `先不要动文件`, or equivalent wording.

Do not recommend or create Goal mode merely because the task is long, technically difficult, contains several steps, or is being rewritten by this skill. For bounded questions, reviews, plans, diagnoses, single changes, or tasks that can reasonably finish in the current task with ordinary validation, choose `refine_then_answer` or `refine_then_execute`.

Use judgment from the task shape rather than keyword matching. If a missing fact materially determines suitability, ask the smallest question instead of making a speculative recommendation.

Keep recommendation separate from authorization. If Goal mode is useful but neither explicit Goal authorization nor authorized durable execution is present, show the refined prompt, state that Goal creation needs confirmation, and stop before calling `create_goal`.

When `refine_then_create_goal` is selected, create the Goal with the displayed refined prompt body as the `objective` by default. Do not re-summarize it into a numbered task list merely for neatness. The Goal objective is the durable execution contract, so preserve the refined prompt's headings, success criteria, authorization boundaries, validation requirements, output contract, and stop rules.

If the displayed refined prompt body would exceed the Goal objective length limit, compress it only enough to fit. Compression must preserve, in order:

1. Explicit prohibitions, approval gates, and authorization boundaries.
2. Stop rules, terminal states, and decision criteria.
3. Success criteria and required validation/evidence.
4. Required outputs and reporting language/format.
5. Essential background, inputs, paths, names, dates, and frozen facts.

Do not compress away conditions such as `only proceed if`, `must confirm before`, `do not modify`, `STOP`, `GO`, `NARROW`, `PIVOT_REQUIRED`, evidence hashes, compile/test gates, or external-service restrictions. After Goal creation, do not start external, destructive, costly, or scope-expanding work unless separately authorized.

### 7. Preserve domain-specific boundaries

Apply these rules only when relevant:

- For grounded work, require support for material claims, place citations near supported claims, label inference, expose source conflicts, and narrow unsupported conclusions instead of guessing.
- For coding or artifact creation, name the most relevant validation and require an explanation when it cannot run.
- For answer, explanation, review, diagnosis, or planning requests, do not imply implementation authority.
- For change, build, or fix requests, preserve authorized in-scope local actions and explicit confirmation gates for external, destructive, costly, or scope-expanding actions.
- For editing or rewriting, preserve the requested artifact, factual claims, genre, length, and structure before improving clarity.
- For tool-heavy work, expose only relevant tools. Use decision rules for retrieval, fallback, parallel reads, and stopping instead of requesting tool use for its own sake.

## Output

By default, first return the refined prompt under a short heading in the source request's language. For a Chinese request, use:

```markdown
### 重构后的提示词

建议：执行模式：`[refine_only / refine_then_answer / refine_then_execute / refine_then_create_goal]`；模型：`[one explicit available model]`；思考强度：`[one available reasoning effort]`；理由：[one concise task-specific reason]

[ready-to-use prompt]
```

Put the recommendation first and keep it to one line. Always recommend one default model configuration for sufficiently specified tasks. Include the execution mode in that same line; do not add a separate model or execution-mode section.

Use `refine_then_create_goal` when Goal creation is explicitly authorized or when authorized execution is clearly durable-goal-shaped. Use `refine_then_execute` for ordinary authorized work, `refine_then_answer` for bounded non-mutating work, and `refine_only` when execution is not authorized. The model and effort recommendation is advisory: it does not switch models or reasoning effort.

When `refine_then_create_goal` is selected, the prompt after the first line must use the fixed Goal-mode template from the workflow and must remain directly usable by the user. When Goal creation is not selected, the prompt after the first line can remain a compact sentence or proportional sectioned prompt.

After showing the refined prompt:

- For `refine_only`, stop after any required `待确认项`.
- For `refine_then_answer`, answer from the refined prompt in the same response.
- For `refine_then_execute`, proceed with the ordinary task after the prompt, respecting confirmation gates.
- For `refine_then_create_goal`, call `create_goal` only after displaying the refined prompt and only when explicit Goal authorization is present or the user has authorized execution of a clearly durable-goal-shaped task. Use the displayed refined prompt body itself as the Goal `objective` unless length forces boundary-preserving compression. Then continue according to the created Goal's lifecycle and the user's authorization boundaries.

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
- the first line states execution mode, model, reasoning effort, and one concise reason;
- the model and effort recommendation matches task difficulty, risk, latency, cost, and current availability;
- `max` is reserved for a concrete hardest-quality-first reason rather than used as a default;
- no model or reasoning setting was claimed to be changed automatically;
- any Goal creation is justified by durable orchestration needs and explicit authorization rather than complexity alone;
- any Goal creation prompt uses the fixed template and remains directly usable;
- the Goal objective is the displayed refined prompt body by default, not a lossy summary;
- no Goal was created from recommendation alone;
- the output can be copied and used directly.

For representative coding, research, rewriting, model-selection, Goal-mode, and short-input transformations, read [references/examples.md](references/examples.md) only when an example is needed.
