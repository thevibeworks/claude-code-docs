<!-- Copyright 2026 Anthropic PBC -->
<!-- SPDX-License-Identifier: Apache-2.0 -->

> **Workshop materials. Not maintained and not accepting contributions.**

# Eval-Driven Agent Development

A hands-on workshop: build an eval for a Claude Managed Agent that generates
slide decks, then iterate the agent against it and see what the eval reveals.

## Requirements

| Tool | Version | Install |
|---|---|---|
| **Node.js** | >=22 | <https://nodejs.org> or `brew install node` |
| **`ant` CLI** | >=1.6.0 | `brew install anthropics/tap/ant` (macOS) — see [docs](https://platform.claude.com/docs/en/api/sdks/cli) for Linux/Windows |
| **Docker** | any recent | <https://www.docker.com/products/docker-desktop/> or OrbStack |
| **Anthropic API key** | — | Get one from <https://platform.claude.com/settings/keys> |

## Setup

```bash
# 1. Clone and install
git clone <REPO_URL>
cd eval-driven-agent-development
npm install

# 2. Authenticate
export ANTHROPIC_API_KEY=sk-ant-...

# 3. Build the render image (LibreOffice in a container — used by the grader)
docker build -t cwc-pptx-render .
```

Check your install:

```bash
node --version    # should be v22.x or higher
ant --version
docker ps         # should not error
```

## Running it

The presenter will walk you through these in order, but for reference:

```bash
# Create the cloud environment + agent from YAML, paste the returned IDs
# into src/create-slides.ts (ENVIRONMENT_ID, AGENT_ID, WORKSPACE_ID)
ant beta:environments create < resources/workshop-pptx.environment.yaml
ant beta:agents create        < resources/agent.yaml

# Run the agent on one task
npm run create-slides -- technology
npm run create-slides -- --all

# Render the resulting deck to per-slide JPGs
npm run render -- technology

# Grade it (programmatic checks + LLM judge)
npm run eval -- technology
npm run eval -- --all

# The first time, pass --baseline to record the score as the baseline (future runs will show deltas against this result):
npm run eval -- --all --baseline

# To show the stored baseline eval results again at any point:
npm run show-baseline
```

## Repo layout

```
resources/
  workshop-pptx.environment.yaml   cloud env definition
  agents/00-naive.agent.yaml       baseline agent (and 01-04 for each round)
src/
  create-slides.ts                 starts a CMA session, downloads the pptx
  render.ts                        pptx → JPGs via local Docker
  parse-pptx.ts                    pptx → structural metrics
  graders.ts                       declarative grader definitions (the eval rubric)
  eval-runner.ts                      the harness — runs every grader on every task
tasks.json                         the 5 task prompts (the test set)
runs/                              outputs land here per task
```
