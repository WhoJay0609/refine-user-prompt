---
name: refine-user-prompt
description: Restructure a user's raw request into a lean, outcome-first prompt while preserving intent, facts, scope, language, authorization, evidence requirements, and output needs, and recommend Codex Goal mode when durable orchestration would materially help. Use when the user asks to 梳理、整理、优化、重写或改写提示词, convert an informal request into a GPT-5.6-ready prompt, remove repetition or contradictions from an instruction stack, clarify success criteria and stop rules, or assess whether the underlying task merits Goal mode without executing it or creating a Goal.
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

Keep a simple request to one sentence or a short list. For a complex request, select only the useful sections from this order:

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

Omit empty or behavior-neutral sections. Describe the destination before the method and leave room for the model to choose an efficient path.

### 5. Recommend Goal mode only when it materially helps

Evaluate the underlying task after refining its contract. Recommend Codex Goal mode when durable orchestration is materially useful, especially when the task has one or more of these properties:

- several dependent phases or milestones whose accepted results constrain later work;
- work expected to span multiple turns or long-running operations and resume after interruption;
- repeated monitoring, experiments, evaluations, retries, or recovery that must preserve state;
- multiple dependent deliverables with explicit acceptance and closeout gates;
- an explicit terminal condition that requires durable progress tracking rather than a single bounded response.

Do not recommend Goal mode merely because the task is long, technically difficult, contains several steps, or is being rewritten by this skill. Omit the recommendation for bounded questions, reviews, plans, diagnoses, single changes, or tasks that can reasonably finish in the current task with ordinary validation.

Use judgment from the task shape rather than keyword matching. If a missing fact materially determines suitability, ask the smallest question instead of making a speculative recommendation.

Keep recommendation separate from authorization. Never create a Goal, invoke `goal-entry`, update Goal state, or begin executing the refined task unless the user explicitly requests that separate action.

### 6. Preserve domain-specific boundaries

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

[ready-to-use prompt]
```

Preserve the source request's language, including headings, unless the user requests another language. Add a localized `待确认项` / `Open questions` section only when material information remains unresolved. For a Chinese request, use:

```markdown
### 待确认项

- [the smallest question or unresolved conflict]
```

When Goal mode is recommended, add a localized execution-mode section after the refined prompt. For a Chinese request, use:

```markdown
### 执行模式建议

建议使用目标模式。

原因：
- [one to three concrete reasons from the task shape]

建议目标：[one-sentence objective derived from the refined prompt]

该提示仅为建议，不会自动创建或执行目标。如需启用，请明确要求创建目标。
```

Omit this section when Goal mode would add no material value. Do not add a negative “不需要目标模式” notice unless the user explicitly asks for a mode assessment.

Do not add a change log, rationale, score, or prompt-engineering lecture unless requested. If the user asks for both a refined prompt and an explanation, place the ready-to-use prompt first.

## Final Check

Before responding, verify:

- the refined prompt is semantically equivalent to the user's request;
- no explicit fact, value, exclusion, or approval boundary was lost;
- no fact, authority, deliverable, or tool was invented;
- duplicate or contradictory instructions were removed or surfaced;
- success and stopping conditions are sufficient for the task;
- the structure is no more elaborate than the task requires;
- any Goal-mode recommendation is justified by durable orchestration needs rather than complexity alone;
- no Goal was created, invoked, or executed from the recommendation;
- the output can be copied and used directly.

For representative coding, research, rewriting, Goal-mode, and short-input transformations, read [references/examples.md](references/examples.md) only when an example is needed.
