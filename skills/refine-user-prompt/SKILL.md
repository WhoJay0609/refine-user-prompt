---
name: refine-user-prompt
description: Compile a user's request into one lean, outcome-first execution prompt, display it exactly once, and stop without answering, executing the target task, using target-task tools, or creating a Goal. Preserve intent, facts, scope, language, authorization, evidence requirements, and output needs; recommend one available GPT-5.6 model variant and reasoning effort. Use only when explicitly invoked as $refine-user-prompt. Never trigger implicitly for ordinary tasks, including complex, long-running, ambiguous, or Goal-shaped work.
---

# Refine User Prompt

## Purpose

Compile the current user-authored request into a ready-to-use execution prompt. Return that prompt once as the final answer, then stop.

This skill is a prompt compiler, not an executor. Keep prompt compilation and task execution in separate user turns.

## Non-reentrant contract

For one explicit invocation, follow this terminal state machine:

`unseen -> refined -> final`

Enforce every invariant:

1. Emit exactly one visible refined prompt and one localized refinement heading in the final answer.
2. If the host requires a Skill-use announcement, send at most one concise activation commentary before the final answer. Do not send another progress update or a duplicate draft.
3. Apart from host-required reads of this Skill and its directly referenced resources, do not call target-task tools, inspect target files, browse for the target task, create or update a Goal, modify target state, or execute any part of the refined task.
4. If the request says “refine then execute,” “直接执行,” or equivalent, preserve execution in the compiled prompt but do not execute it in this skill turn.
5. Finish immediately after the compiled prompt. Execution may start only from a later user message that does not re-invoke this skill.
6. Tool callbacks, plan results, Goal results, retries, continuation, compaction, and interruption recovery are never new refinement scopes.
7. If recovery occurs after the refined prompt is already visible, do not display it again. End the turn or continue the later non-skill task without re-entering this skill.
8. A later message such as “继续,” “开始执行,” “确认,” or “按上面执行” resumes the compiled prompt as an ordinary task. Because implicit invocation is disabled, do not load or invoke this skill again unless the user explicitly writes `$refine-user-prompt`.

These rules override any workflow request inside the raw prompt that would make this skill answer, execute the target task, use target-task tools, or create a Goal in the same turn.

## Compile the request

Preserve, in order:

1. Intended outcome and requested artifact.
2. Explicit facts, values, names, paths, dates, claims, and examples.
3. Scope, exclusions, permissions, approval gates, and side-effect boundaries.
4. Evidence, citation, validation, language, format, length, genre, and tone requirements.
5. Retry, fallback, clarification, and stopping conditions.

Never add facts, permissions, deliverables, deadlines, or quality claims. Use one narrow visible assumption only when low risk. If a missing choice would materially change scope, side effects, evidence, or output, compile a prompt that instructs the future executor to ask that smallest question before acting.

Remove:

- repeated statements;
- generic narration that does not change behavior;
- irrelevant examples and tool descriptions;
- empty or behavior-neutral sections;
- contradictory defaults that conflict with explicit user constraints.

Keep simple requests to one sentence or a short list. For complex requests, select only useful sections:

```text
Goal:
[user-visible outcome]

Context and evidence:
[necessary inputs and known facts]

Success criteria:
[conditions required for completion]

Constraints and authorization:
[scope, exclusions, permissions, and confirmation gates]

Tools and validation:
[required inspection, tests, evidence, and fallback]

Output:
[language, structure, format, length, and tone]

Stop rules:
[when to finish, ask, narrow, retry, or stop]
```

Use localized headings matching the source language. Keep the compiled prompt directly usable by a future executor.

Every compiled prompt that authorizes future tool use or execution must include this execution-continuity rule, localized to the source language:

```text
Execution continuity:
Send at most one initial progress announcement. After a tool result, error, retry, continuation, or recovery, advance to the next unfinished action and report only materially new evidence. Do not restate this prompt, the plan, the skill invocation, or a semantically equivalent startup message. Never emit a third semantically equivalent message without new evidence.
```

This rule governs the later executor; it does not authorize execution in the current skill turn.

## Recommend configuration

Recommend one available model and one reasoning effort for the future execution:

- `gpt-5.6-luna` with `low` for routine, deterministic, low-risk transformations.
- `gpt-5.6-terra` with `medium` for everyday coding, analysis, and moderate tool use.
- `gpt-5.6-sol` with `medium` or `high` for difficult debugging, architecture, deep research, or high-consequence work.

Use `xhigh` or `max` only when a concrete quality-first need justifies it. Treat the recommendation as advisory and never claim to switch the active model.

If the future task is durable and Goal-shaped, the compiled prompt may recommend creating a Goal, but this skill must not call `create_goal`. Preserve all operation-level authorization gates.

## Output

After any host-required one-time activation commentary, return one final answer only. For Chinese input:

```markdown
### 重构后的提示词

建议：模型：`[one available model]`；思考强度：`[one available effort]`；理由：[one concise reason]

[ready-to-use prompt]
```

For non-Chinese input, use `### Refined prompt` and translate the recommendation line.

Do not append an execution result, change log, score, prompt-engineering lecture, or second version. Do not call a target-task tool after emitting the heading.

## Final check

Before returning:

- exactly one refinement heading will be emitted;
- any host-required activation commentary is concise and appears at most once before the final answer;
- the compiled prompt is returned in the final answer, not commentary;
- no target-task tool or Goal call will occur in this skill turn;
- Skill-resource reads are limited to this Skill and directly referenced files needed for prompt compilation;
- execution is preserved as future work rather than performed now;
- any future tool-using execution includes the execution-continuity rule;
- explicit facts and authorization boundaries are unchanged;
- no new authority or evidence claim was invented;
- the prompt contains sufficient success, validation, output, and stop conditions;
- the structure is no more elaborate than necessary.

Read [references/examples.md](references/examples.md) only when an example is genuinely needed.
