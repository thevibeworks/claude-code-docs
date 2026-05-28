# Prerequisites

When asked to setup the folder/repository, make sure the prerequisites listed in the README.md are met (Node >=22 installed, `ant` CLI installed, Docker installed, `ANTHROPIC_API_KEY` set in environment). Do not deploy the resources yet.
Offer to install them for the user if missing (if Docker is missing, point them to the installation website)
Kick off `docker build -t cwc-pptx-render .` asap in a subagent to make sure the docker image is pre-built.

Write the `ANTHROPIC_API_KEY` from your environment into a `.env` file for reference (in case your terminal gets reopened and loses it). Do not override it though if the `.env` file already consists with a key inside.

# Repository structure

Assume you're at the workshop unless told otherwise.

- `resources/` contains the agent and environment definition. All changes to the agent will be made here.
- `solutions/` contains **solutions** for evolved agent definitions. Do not reference these unless explicitly asked. If asked, do no deploy these agents directly, copy the system prompt changes over to `resources/agent.yaml` and iterate on that agent.
- `src/eval-runner.ts` is the eval runner. It should not be modified during the workshop.
- `src/graders.ts` is where the eval graders leave. Add more graders here when asked.
- `src/graders/...` contains the **solutions** to graders. Don't import these unless asked to, default to adding new graders to `graders.ts`. You may get asked at some point to import the predefined graders so we're all on the same base.

# YAML resources

When asked to set up the agent resources, create the resources by piping them to the `ant` CLI:

```
ant beta:agents create < ./resources/agent.yaml
```

Then from the output, take the `id` (and `version` for agent) and insert it as an extra key at the top of the YAML file:

```diff
+ id: agent_abc123...
+ version: 1
  name: workshop-pptx-01-polish
```

Additionally, update `AGENT_ID` and `ENVIRONMENT_ID` in `src/create-slides.ts`.

Same for `workshop-pptx.environment.yaml`, but only with the `id` (environments are not versioned).

When you are asked to update any resource, pipe the YAML file into the `update` command.

```
ant beta:agents update < ./resources/agent.yaml
```

then afterwards, you just need to bump the version again to the new version from the response:

```diff
  id: agent_abc123...
- version: 1
+ version: 2
  name: workshop-pptx-01-polish
```

# Troubleshooting

If a resource suddenly gives a 404, you were probably ran in a different terminal.
Load the `ANTHROPIC_API_KEY` from the `.env` file.


# Git operations

DO NOT COMMIT ANYTHING UNLESS EXPLICITLY ASKED BY THE USER.

# TypeScript Code Style

- Never add an explicit type guard signature to predicates like `.filter((x): x is Foo => x !== null)`. TypeScript infers type guards in latest versions, it's enough to write `.filter((x) => x !== null)` which is more type safe.
- Don't use `export default`, always name exports

# License headers

All `.ts` files need to have this license header at the top:

```
// Copyright 2026 Anthropic PBC
// SPDX-License-Identifier: Apache-2.0
```
