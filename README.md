# Plain Korean

Make technical answers, status reports, and diagnoses easy to understand in natural Korean without hiding evidence, uncertainty, or risk.

Plain Korean ships as an agent skill and as a Claude Code custom output style. It does not call an API or require a separate model.

English | [한국어](README.ko.md)

## What it changes

- Leads with the result instead of the work log
- Uses one idea per sentence and explains necessary technical terms
- Separates verified facts, inference, and unknowns
- Preserves failures, partial success, and safety limits
- Scales detail to the decision instead of forcing every answer to be tiny

## Install the agent skill

```sh
git clone https://github.com/beamonic/plain-korean.git
cd plain-korean
mkdir -p ~/.agents/skills
cp -R skills/plain-korean ~/.agents/skills/
```

Restart the agent if the skill does not appear immediately.

## Install the Claude Code output style

```sh
mkdir -p ~/.claude/output-styles
cp skills/plain-korean/assets/claude-output-style.md ~/.claude/output-styles/plain-korean.md
```

In Claude Code, run `/config`, choose **Output style**, and select **Plain Korean**. Start a new session or run `/clear` for the change to take effect.

## Use

```text
$plain-korean Explain this failed deployment so a non-developer can decide the next action.
```

```text
$plain-korean Rewrite this status update in clear Korean without hiding what is still unverified.
```

## Verify

```sh
python3 -m unittest -v tests/test_skill.py
python3 /path/to/skill-creator/scripts/quick_validate.py skills/plain-korean
```

## License

MIT. Copyright (c) 2026 Beamonic.
