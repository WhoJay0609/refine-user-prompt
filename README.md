# refine-user-prompt

`refine-user-prompt` is an explicitly invoked Codex prompt compiler. It restructures a raw request into one lean, outcome-first prompt, displays that prompt exactly once, and stops before answering, using target-task tools, executing the task, or creating a Goal. Host-required Skill loading and one concise activation announcement remain allowed.

It follows the principles in OpenAI's [Prompting guidance for GPT-5.6](https://developers.openai.com/api/docs/guides/prompt-guidance-gpt-5p6): define the outcome and completion bar, remove repeated instructions, preserve true constraints, and leave room for the model to choose an efficient path.

## Quick start

Install the package (documented command; file-copy smoke tested in a temporary directory), start a new Codex task, and invoke it explicitly (documented first-use example; Codex host execution is not run in this checkout):

```bash
git clone --depth 1 https://github.com/WhoJay0609/refine-user-prompt.git
mkdir -p ~/.codex/skills/refine-user-prompt
cp -R refine-user-prompt/skills/refine-user-prompt/. ~/.codex/skills/refine-user-prompt/
```

```text
$refine-user-prompt

Please restructure this request without changing its intent:
[raw request]
```

The skill returns the compiled prompt once and stops. It does not answer, call target-task tools, create a Goal, or execute the task during the refinement turn. Send a later message such as `继续` or `按上面执行` (without invoking `$refine-user-prompt` again) to start execution in a separate user turn.

## What it does

- Preserves explicit facts, values, exclusions, permissions, and requested output.
- Removes repetition, irrelevant process narration, and contradictory scaffolding.
- Keeps simple requests short and adds structure only when it changes behavior.
- Preserves the smallest question needed to resolve a material ambiguity and instructs the future executor to ask it before acting.
- Recommends one explicit GPT-5.6 model variant and reasoning effort from task difficulty, risk, verification burden, latency, and cost priorities.
- Runs only when explicitly invoked as `$refine-user-prompt`; ordinary tasks never trigger it implicitly.
- Preserves requested execution as future work while keeping prompt compilation and task execution in separate user turns.
- Never uses target-task tools, creates a Goal, or executes the refined task in the refinement turn; only host-required Skill-resource reads are allowed.
- Adds an execution-continuity rule to tool-using prompts so a later executor advances after results or recovery without repeating the prompt or startup message.

## Model guidance

The skill follows OpenAI's current [GPT-5.6 model guide](https://developers.openai.com/api/docs/guides/latest-model):

- `gpt-5.6-luna` for efficient, routine, high-volume work;
- `gpt-5.6-terra` as the balanced everyday default;
- `gpt-5.6-sol` for flagship-quality complex or high-consequence work.

It recommends `medium` as the balanced reasoning baseline, uses `low` for latency-sensitive work, reserves `high` or `xhigh` for tasks that benefit from deeper reasoning, and uses `max` only for the hardest quality-first workloads. Recommendations are advisory and never change the active model automatically.

## Repository layout

```text
skills/refine-user-prompt/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   └── examples.md
└── scripts/
    └── validate_anti_loop.py
```

The installable skill is kept under `skills/refine-user-prompt/`; repository documentation and licensing remain outside the skill package.

## Install details

The installable package is `skills/refine-user-prompt/`; the repository README and license stay outside that package. After copying it, start a new Codex task so the skill catalog is refreshed.

## Use

Invoke the skill explicitly:

```text
$refine-user-prompt

Please restructure the following request without changing its intent:
[raw request]
```

For Chinese input:

```text
$refine-user-prompt

请重新梳理下面的用户输入，保留原意和授权边界：
[原始输入]
```

The skill returns the compiled prompt and stops. Send a later message such as `继续` or `按上面执行` to start the task without invoking the skill again.

### Input → output (illustrative)

The wording below is an output shape, not a transcript or a measured result. The skill fills the details from the request it receives:

```text
Input:
$refine-user-prompt

Rewrite the README for clarity, keep all numbers and citations, and do not strengthen the conclusion.

Output shape:
### Refined prompt

Recommendation: model: `[advisory GPT-5.6 variant]`; reasoning effort: `[advisory level]`; reason: [one concise reason]

Rewrite the README for clarity while preserving every number, citation, and the original conclusion strength.
```

The skill stops immediately after emitting the compiled prompt; no target-task tools are called and no files are changed in the refinement turn. If the raw request asks to execute a tool-using task, the compiled prompt preserves that execution scope and appends the execution-continuity rule for a later user turn. It does not invent evidence, token savings, model compatibility, or a Goal.

## Validate

Run the anti-loop contract validator and the generic Codex skill validator against the installable package:

```bash
python3 skills/refine-user-prompt/scripts/validate_anti_loop.py
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/refine-user-prompt
```

## Compatibility

| Harness / surface | Status | Evidence |
| --- | --- | --- |
| Codex local Skill package | documented; anti-loop validator, package validator, and temporary-directory copy smoke passed | [`skills/refine-user-prompt/SKILL.md`](skills/refine-user-prompt/SKILL.md), [`skills/refine-user-prompt/scripts/validate_anti_loop.py`](skills/refine-user-prompt/scripts/validate_anti_loop.py) |
| Other harnesses | unknown | This checkout contains no runtime adapter or plugin manifest |

## Scope, support, and provenance

- This repository ships prompt instructions, examples, and a contract validator; it does not contain a runtime wrapper, model weights, or an automatic model switch.
- Model and reasoning recommendations are advisory. The active Codex configuration remains unchanged unless the user changes it separately.
- The skill cannot grant permissions or override host/system instructions; it never calls `create_goal` or target-task tools in the refinement turn.
- For help, include the raw request and the observed output with credentials, session identifiers, and local paths removed.
- Contributions should edit the installable skill and its examples together, then run the validators above. Keep the non-reentrant refine-only contract, explicit-only trigger, turn separation, and Goal prohibition intact.
- The skill's behavior is defined by [`skills/refine-user-prompt/SKILL.md`](skills/refine-user-prompt/SKILL.md); [`skills/refine-user-prompt/references/examples.md`](skills/refine-user-prompt/references/examples.md) is illustrative guidance, not execution evidence.

## License

MIT
