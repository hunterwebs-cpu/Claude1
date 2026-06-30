#!/bin/bash
set -euo pipefail

if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

# Copy all project skills to ~/.claude/skills/ so they're available session-wide
mkdir -p ~/.claude/skills
for skill_dir in "$CLAUDE_PROJECT_DIR/.claude/skills"/*/; do
  cp -r "$skill_dir" ~/.claude/skills/
done
