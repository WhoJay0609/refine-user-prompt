# refine-user-prompt

`refine-user-prompt` is a Codex skill that restructures raw user requests into lean, outcome-first prompts while preserving intent, facts, scope, authorization, evidence requirements, and output constraints.

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

The skill shows the refined prompt first. It then answers, executes, or recommends Goal mode according to the request's authorization; a recommendation alone never grants permission to act, and host/system rules still govern Goal creation.

## What it does

- Preserves explicit facts, values, exclusions, permissions, and requested output.
- Removes repetition, irrelevant process narration, and contradictory scaffolding.
- Keeps simple requests short and adds structure only when it changes behavior.
- Asks only the smallest question needed to resolve a material ambiguity.
- Recommends one explicit GPT-5.6 model variant and reasoning effort from task difficulty, risk, verification burden, latency, and cost priorities.
- Recommends Codex Goal mode when durable state, dependent milestones, recovery, or repeated monitoring materially justify it.
- Does not create a Goal or execute the refined task from a recommendation alone; it follows an explicitly authorized mode, including a clearly durable task whose execution was authorized.

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
└── references/
    └── examples.md
```

The installable skill is kept under `skills/refine-user-prompt/`; repository documentation and licensing remain outside the skill package.

## Install details

The installable package is `skills/refine-user-prompt/`; the repository README, license, and reference examples stay outside that package. After copying it, start a new Codex task so the skill catalog is refreshed.

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

### Input → output (illustrative)

The wording below is an output shape, not a transcript or a measured result. The skill fills the details from the request it receives:

```text
Input:
Please refine this request only; do not edit files: rewrite the README for clarity,
keep all numbers and citations, and do not strengthen the conclusion.

Output shape:
Recommendation: mode=refine_only; model=[advisory GPT-5.6 variant]; reasoning effort=[advisory level]
Refined prompt: Rewrite the README for clarity while preserving every number,
citation, and the original conclusion strength.
Mode: refine_only
Action: show the refined prompt, then stop; no files are changed.
```

For an authorized execution request, the output keeps the same constraints and states the checks it will run. It does not invent evidence, token savings, model compatibility, or a Goal.

## Validate

Run the generic Codex skill validator against the installable package:

```bash
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/refine-user-prompt
```

## Compatibility

| Harness / surface | Status | Evidence |
| --- | --- | --- |
| Codex local Skill package | documented; package validator and temporary-directory copy smoke passed (2026-09-12) | [`skills/refine-user-prompt/SKILL.md`](skills/refine-user-prompt/SKILL.md), command above |
| Other harnesses | unknown | This checkout contains no runtime adapter or plugin manifest |

## Scope, support, and provenance

- This repository ships prompt instructions and examples; it does not contain a runtime wrapper, model weights, or an automatic model switch.
- Model and reasoning recommendations are advisory. The active Codex configuration remains unchanged unless the user changes it separately.
- The skill cannot grant permissions or override host/system instructions; if the active environment requires explicit Goal wording, that rule wins.
- For help, include the raw request, the selected mode, and the observed output with credentials, session identifiers, and local paths removed.
- Contributions should edit the installable skill and its examples together, then run the validator above. Keep the `refine_only` stop rule and the Goal-authorization boundary intact.
- The skill's behavior is defined by [`skills/refine-user-prompt/SKILL.md`](skills/refine-user-prompt/SKILL.md); [`references/examples.md`](skills/refine-user-prompt/references/examples.md) is illustrative guidance, not execution evidence.

## License

MIT
