# refine-user-prompt

`refine-user-prompt` is a Codex skill that restructures raw user requests into lean, outcome-first prompts while preserving intent, facts, scope, authorization, evidence requirements, and output constraints.

It follows the principles in OpenAI's [Prompting guidance for GPT-5.6](https://developers.openai.com/api/docs/guides/prompt-guidance-gpt-5p6): define the outcome and completion bar, remove repeated instructions, preserve true constraints, and leave room for the model to choose an efficient path.

## What it does

- Preserves explicit facts, values, exclusions, permissions, and requested output.
- Removes repetition, irrelevant process narration, and contradictory scaffolding.
- Keeps simple requests short and adds structure only when it changes behavior.
- Asks only the smallest question needed to resolve a material ambiguity.
- Recommends Codex Goal mode when durable state, dependent milestones, recovery, or repeated monitoring materially justify it.
- Never creates a Goal or executes the refined task unless the user explicitly requests that separate action.

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

## Install

Clone the repository and copy the skill directory into your Codex skills directory:

```bash
git clone https://github.com/WhoJay0609/refine-user-prompt.git
cp -R refine-user-prompt/skills/refine-user-prompt ~/.codex/skills/
```

Start a new Codex task after installation so the skill catalog is refreshed.

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

## Validate

Run the generic Codex skill validator against the installable package:

```bash
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/refine-user-prompt
```

## License

MIT
