#!/bin/bash
set -euo pipefail

if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

# Copy UI UX Pro Max skill to global ~/.claude/skills/ so it's available every session
mkdir -p ~/.claude/skills
cp -r "$CLAUDE_PROJECT_DIR/.claude/skills/ui-ux-pro-max" ~/.claude/skills/
