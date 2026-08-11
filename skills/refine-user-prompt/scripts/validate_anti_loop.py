#!/usr/bin/env python3
"""Validate the non-reentrant contract of refine-user-prompt."""

from pathlib import Path
import sys


target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
SKILL = target / "SKILL.md" if target.is_dir() else target
text = SKILL.read_text(encoding="utf-8")

required = {
    "terminal state machine": "`unseen -> refined -> final`",
    "single visible refinement": "Emit exactly one visible refined prompt",
    "target-task tool prohibition": "do not call target-task tools",
    "host announcement allowance": "If the host requires a Skill-use announcement",
    "skill resource allowance": "host-required reads of this Skill and its directly referenced resources",
    "goal prohibition": "must not call `create_goal`",
    "turn separation": "Keep prompt compilation and task execution in separate user turns",
    "continuation exclusion": "A later message such as “继续,” “开始执行,” “确认,” or “按上面执行”",
    "recovery guard": "after the refined prompt is already visible, do not display it again",
    "future executor guard": "Every compiled prompt that authorizes future tool use or execution must include this execution-continuity rule",
    "third-repeat fuse": "Never emit a third semantically equivalent message without new evidence",
    "explicit-only trigger": "Use only when explicitly invoked as $refine-user-prompt",
}

missing = [name for name, marker in required.items() if marker not in text]
if missing:
    raise SystemExit("missing anti-loop safeguards: " + ", ".join(missing))

if "Never trigger implicitly for ordinary tasks" not in text:
    raise SystemExit("trigger remains too broad")

if "Do not call tools" in text:
    raise SystemExit("tool prohibition incorrectly blocks host-required Skill loading")

print("anti-loop contract: PASS")
