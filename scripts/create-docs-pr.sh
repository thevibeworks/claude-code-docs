#!/bin/bash
set -euo pipefail

if [ $# -lt 3 ]; then
    echo "Usage: $0 <title> <description> <version>"
    echo "Example: $0 'SDK improvements' 'Request cancellation support' '1.0.83'"
    exit 1
fi

TITLE="$1"
DESCRIPTION="$2"
VERSION="$3"

if git diff --quiet && git diff --cached --quiet; then
    echo "No changes to commit"
    exit 0
fi

CURRENT_BRANCH=$(git branch --show-current)
if [[ "$CURRENT_BRANCH" != "main" ]]; then
    echo "Error: Must be on main branch. Current: $CURRENT_BRANCH"
    exit 1
fi

TIMESTAMP=$(date +%Y%m%d-%H%M)
BRANCH_NAME="docs/claude-code-v${VERSION}-${TIMESTAMP}"

git checkout -b "$BRANCH_NAME" || exit 1

git add .
git commit -m "docs: Claude Code v${VERSION} - ${TITLE}

🤖 Generated with [Claude Code](https://claude.ai/code)

Co-Authored-By: Claude <noreply@anthropic.com>"

git push -u origin HEAD || exit 1

PR_URL=$(gh pr create \
  --title "docs: Claude Code v${VERSION} - ${TITLE}" \
  --body "## Night shift report

WHY THIS MATTERS: ${DESCRIPTION}

WHAT CHANGED: Version bump to v${VERSION}

HIGHLIGHTS:
- ${DESCRIPTION}

---
*Created by night-shift claude-yolo*
*After Anthropic engineers went home*
*Day-shift claude-yolo will review and merge this in the morning*")

echo "$PR_URL"