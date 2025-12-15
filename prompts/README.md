# Prompts

Meta prompts and patterns derived from Anthropic's official documentation.

## Contents

| File | Description |
|------|-------------|
| `prompt-optimizer.md` | Meta prompt for improving user prompts |
| `agent-patterns.md` | Patterns for building agentic workflows |

## Documentation Sources

All prompts derived from official docs (append `.md` for raw markdown):

```
# Prompt Engineering
https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview.md
https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompt-improver.md
https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/be-clear-and-direct.md
https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/use-xml-tags.md
https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/chain-of-thought.md
https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/system-prompts.md
https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/multishot-prompting.md
https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prefill-claudes-response.md
https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-4-best-practices.md

# Agent Building
https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview.md
https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices.md

# Prompt Library (65+ examples)
https://platform.claude.com/docs/en/resources/prompt-library/library.md
```

## Fetching Updates

Anthropic docs support direct `.md` access. Use the fetcher:

```bash
# Fetch specific URL(s) - appends .md automatically
uv run scripts/fetcher.py https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

# Multiple URLs
uv run scripts/fetcher.py URL1 URL2 URL3

# Fetch all prompt engineering docs
uv run scripts/fetcher.py --section api

# Show available structure
uv run scripts/fetcher.py --tree

# See all options
uv run scripts/fetcher.py --help
```
