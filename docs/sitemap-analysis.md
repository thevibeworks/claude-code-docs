# Sitemap Structure Analysis & Improvement Proposals

**Analysis Date:** 2025-11-05
**Sitemap:** https://docs.claude.com/sitemap.xml
**Total URLs:** 269 (all /en/ paths)

## Sitemap Structure Tree

```
docs.claude.com/en/ (269 total)
│
├─ api/ (84 URLs - 31%)
│  ├─ admin-api/ (25)
│  │  ├─ apikeys/
│  │  ├─ claude-code/
│  │  ├─ invites/
│  │  ├─ organization/
│  │  ├─ usage-cost/
│  │  ├─ users/
│  │  ├─ workspaces/
│  │  └─ workspace_members/
│  ├─ agent-sdk/ (16)
│  │  ├─ cost-tracking/
│  │  ├─ custom-tools/
│  │  ├─ hosting/
│  │  ├─ mcp/
│  │  ├─ modifying-system-prompts/
│  │  ├─ permissions/
│  │  ├─ sessions/
│  │  ├─ slash-commands/
│  │  ├─ streaming-vs-single-mode/
│  │  ├─ subagents/
│  │  └─ todo-tracking/
│  ├─ skills/ (9)
│  │  ├─ create-skill/
│  │  ├─ create-skill-version/
│  │  ├─ delete-skill/
│  │  ├─ delete-skill-version/
│  │  ├─ get-skill/
│  │  ├─ get-skill-version/
│  │  ├─ list-skills/
│  │  └─ list-skill-versions/
│  └─ [+34 other endpoints]
│     - messages, models, files-*, errors
│     - rate-limits, versioning, batch operations
│     - client-sdks, openai-sdk
│     - claude-on-amazon-bedrock, claude-on-vertex-ai
│     - prompt-tools-*, supported-regions, service-tiers
│
├─ docs/ (116 URLs - 43%)
│  ├─ about-claude/ (12)
│  │  ├─ models/ (choosing, model-comparison)
│  │  ├─ use-case-guides/ (content-moderation, customer-support-chat, etc)
│  │  ├─ glossary/
│  │  ├─ model-deprecations/
│  │  └─ pricing/
│  ├─ agents-and-tools/ (17)
│  │  ├─ agent-skills/ (overview, quickstart, best-practices)
│  │  ├─ tool-use/ (11 docs: overview, implement, bash, computer-use, etc)
│  │  ├─ claude-for-sheets/
│  │  ├─ mcp-connector/
│  │  └─ remote-mcp-servers/
│  ├─ build-with-claude/ (30)
│  │  ├─ prompt-engineering/ (15 docs)
│  │  │  ├─ overview/
│  │  │  ├─ be-clear-and-direct/
│  │  │  ├─ chain-of-thought/
│  │  │  ├─ chain-prompts/
│  │  │  ├─ claude-4-best-practices/
│  │  │  ├─ multishot-prompting/
│  │  │  ├─ prefill-claudes-response/
│  │  │  ├─ system-prompts/
│  │  │  ├─ use-xml-tags/
│  │  │  ├─ long-context-tips/
│  │  │  ├─ extended-thinking-tips/
│  │  │  ├─ prompt-generator/
│  │  │  ├─ prompt-improver/
│  │  │  └─ prompt-templates-and-variables/
│  │  └─ [features: batch, citations, context, embeddings, etc]
│  ├─ claude-code/ (44)
│  │  ├─ setup, quickstart, settings, common-workflows
│  │  ├─ memory, interactive-mode, slash-commands
│  │  ├─ hooks, troubleshooting, cli-reference
│  │  ├─ ide-integrations, mcp, github-actions
│  │  ├─ security, iam, monitoring-usage
│  │  ├─ amazon-bedrock, google-vertex-ai
│  │  ├─ network-config, terminal-config
│  │  ├─ checkpointing, headless, plugins
│  │  └─ sub-agents, skills
│  ├─ test-and-evaluate/ (10)
│  │  ├─ define-success/
│  │  ├─ develop-tests/
│  │  ├─ eval-tool/
│  │  └─ strengthen-guardrails/ (7 docs)
│  ├─ get-started/ (1)
│  ├─ intro/ (1)
│  └─ mcp/ (1)
│
├─ resources/ (66 URLs - 24%)
│  ├─ overview/ (1)
│  └─ prompt-library/ (65)
│     - 65 curated prompt templates
│
├─ release-notes/ (2 URLs - 1%)
│  ├─ overview/
│  └─ system-prompts/
│
└─ home/ (1 URL)
```

## Current Coverage Analysis

| Script Section  | URLs | Sitemap Match              | Coverage | Output Dir                        |
|-----------------|------|----------------------------|----------|-----------------------------------|
| build           | 30   | docs/build-with-claude/    | ✓ 100%   | build-with-claude/                |
| agents          | 17   | docs/agents-and-tools/     | ✓ 100%   | agents-and-tools/                 |
| claude-code     | 44   | docs/claude-code/          | ✓ 100%   | claude-code-docs/                 |
| agent-sdk       | 16   | api/agent-sdk/             | ✓ 100%   | claude-code-docs/api/api/agent-sdk/ |
| api-skills      | 9    | api/skills/                | ✓ 100%   | claude-code-docs/api/api/skills/  |
| admin-api       | 25   | api/admin-api/             | ✓ 100%   | claude-code-docs/api/api/admin-api/ |
| api-reference   | ~20  | api/* (partial)            | ✗ ~24%   | claude-code-docs/api/             |
| about-claude    | 12   | docs/about-claude/         | ✓ 100%   | about-claude/                     |
| test-eval       | 10   | docs/test-and-evaluate/    | ✓ 100%   | test-and-evaluate/                |
| get-started     | 2    | docs/(get-started\|intro)  | ✗ ~67%   | get-started/                      |
| release-notes   | 2    | release-notes/*            | ✓ 100%   | release-notes/                    |
| resources       | 66   | resources/*                | ✓ 100%   | resources/                        |
| blog            | ~10  | anthropic.com/*/claude-code| ✓ 100%   | anthropic-blog/                   |
| **TOTAL**       | ~263 |                            | **~98%** |                                   |

### Missing URLs (~6)
- `api/administration-api/` (1)
- `api/beta-headers/` (1)
- `api/overview/` (1)
- `api/usage-cost-api/` (1)
- `api/claude-code-analytics-api/` (1)
- `home/` (1)

### Issues Identified

#### 1. Inconsistent Output Structure
Current mapping is convoluted:
- `api/agent-sdk` → `claude-code-docs/api/api/agent-sdk/` (triple nesting)
- `api/skills` → `claude-code-docs/api/api/skills/` (confusing)
- `docs/claude-code` → `claude-code-docs/` (loses context)

#### 2. Pattern Matching is Fragile
- Hardcoded patterns in two places (`_matches_pattern()` + `patterns` dict)
- Easy to miss new sections
- No validation against sitemap structure

#### 3. Section Naming Mismatch
- Script: `agents` vs Sitemap: `agents-and-tools`
- Script: `test-eval` vs Sitemap: `test-and-evaluate`
- Script: `api-skills` vs Sitemap: `skills`

#### 4. Missing API Coverage
`api-reference` pattern catches only ~20/84 API URLs (24%)

Missing endpoints:
- beta-headers, overview, usage-cost-api
- client-sdks, openai-sdk
- prompt-tools-* (generate, improve, templatize)
- All batch operations (creating, listing, retrieving, canceling, deleting)
- migration guides, ip-addresses, service-tiers

## Improvement Proposals

### 1. Simplified Directory Structure

**Current (Messy):**
```
content/
├── claude-code-docs/          # docs/claude-code
│   └── api/api/               # api/* (why nested?)
├── build-with-claude/         # docs/build-with-claude
├── agents-and-tools/          # docs/agents-and-tools
├── about-claude/              # docs/about-claude
├── test-and-evaluate/         # docs/test-and-evaluate
├── resources/                 # resources/*
└── release-notes/             # release-notes/*
```

**Proposed (Clean):**
```
content/
├── docs/                      # 1:1 sitemap mirror
│   ├── about-claude/
│   ├── agents-and-tools/
│   ├── build-with-claude/
│   ├── claude-code/
│   ├── get-started/
│   ├── intro/
│   ├─� mcp/
│   └── test-and-evaluate/
├── api/                       # 1:1 sitemap mirror
│   ├── admin-api/
│   ├── agent-sdk/
│   ├── skills/
│   ├── messages/
│   ├── models/
│   └── [all 84 api endpoints]
├── resources/
│   ├── overview/
│   └── prompt-library/
├── release-notes/
├── blog/
├── claude-code-manifest.json
└── .metadata.json
```

**Benefits:**
- 1:1 mapping: `/en/docs/foo` → `content/docs/foo/`
- Predictable and maintainable
- New sections auto-work
- No special cases

### 2. Simplified URL Extraction

**Current:** 50+ lines of hardcoded patterns

**Proposed:** Auto-discover from sitemap
```python
async def extract_urls_v2(self, session):
    """Auto-extract URLs by sitemap structure"""
    sitemap_xml = await self.fetch_sitemap(session, self.sitemap_url)

    urls_by_section = defaultdict(list)
    for line in sitemap_xml.split('\n'):
        if '<loc>' in line:
            url = line.split('<loc>')[1].split('</loc>')[0]
            if '/en/' not in url:
                continue

            # /en/{section}/* → group by section
            path = url.replace('https://docs.claude.com/en/', '')
            section = path.split('/')[0]
            urls_by_section[section].append(url)

    return urls_by_section
```

**Benefits:**
- Zero hardcoding
- Auto-discovers new sections
- Future-proof

### 3. Simplified Path Mapping

**Current:** 50+ lines of if/elif spaghetti

**Proposed:** 3 lines
```python
def get_output_path(self, url):
    """Direct mapping: /en/docs/foo/bar → content/docs/foo/bar.md"""
    path = url.replace('https://docs.claude.com/en/', '')
    return self.output_dir / f"{path}.{self.format}"
```

### 4. Migration Plan

**Phase 1:** Add `--output-style` flag
```bash
uv run fetchccdocs.py --output-style mirror   # New structure
uv run fetchccdocs.py --output-style legacy   # Current (default)
```

**Phase 2:** Update CLAUDE.md references
- `@./content/claude-code-docs/` → `@./content/docs/claude-code/`
- `@./content/build-with-claude/` → `@./content/docs/build-with-claude/`
- etc.

**Phase 3:** Switch default to `mirror`

**Phase 4:** Deprecate legacy after validation

## Recommendations

### Immediate (Low Risk)
1. ✓ Add NPM manifest fetch (DONE)
2. ✓ Add GitHub CHANGELOG fetch (DONE)
3. Add missing API endpoints (6 URLs)

### Short-term (Medium Effort)
4. Implement `--output-style mirror` flag
5. Fetch using new structure in parallel
6. Validate completeness

### Long-term (Breaking Change)
7. Update CLAUDE.md references
8. Switch default to mirror structure
9. Deprecate legacy mapping
10. Clean up old code

## Summary

**Current State:** ~98% coverage, messy structure
**Proposed State:** 100% coverage, clean 1:1 mirror
**Effort:** Medium (implement flag + phased migration)
**Risk:** Low (can run both structures in parallel)
**Benefit:** High (maintainability, predictability, completeness)
