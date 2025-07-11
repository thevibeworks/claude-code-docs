# Scripts

## fetchccdocs.sh

Fetches Claude Code docs from Anthropic sources.

```bash
./scripts/fetchccdocs.sh
./scripts/fetchccdocs.sh --out /path/to/output
```

Output: `content/claude-code-docs/` (includes release-notes), `content/anthropic-blog/`

## check-changes.sh

Checks if git changes are meaningful enough for commit/PR.

```bash
./scripts/check-changes.sh        # quiet
./scripts/check-changes.sh -v     # verbose
```

**Meaningful**: Major/minor version changes, CHANGELOG features, substantial docs (>100 lines)  
**Ignored**: Patch versions, minor docs, metadata-only changes

Returns 0 if meaningful, 1 if not (auto-resets staged changes).