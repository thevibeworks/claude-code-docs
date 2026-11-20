---
title: Self-hosted worker reference
url: https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-reference
description: "Reference for self-hosted sandbox workers: ant CLI flags, environment variables, host requirements, filesystem paths, and SDK helper options."
featureMetadata:
  topic:
    title: Managed Agents
    url: https://platform.claude.com/docs/en/managed-agents/overview
  status: beta
  betaHeader: managed-agents-2026-04-01
  zdr:
    eligibility: not-eligible
    note: Not eligible for ZDR, except for self-hosted Managed Agents. Sessions are stateful resources; transcripts persist until you delete them.
  supportedModels:
    - claude-fable-5-2
    - claude-mythos-5-2
    - claude-fable-5-1
    - claude-mythos-5-1
    - claude-fable-5
    - claude-mythos-5
    - claude-mythos-preview
    - claude-opus-5-5
    - claude-opus-5
    - claude-sonnet-5-5
    - claude-sonnet-5
    - claude-haiku-5-5
    - claude-haiku-4-5-20251001
    - claude-opus-4-8
    - claude-opus-4-7
    - claude-opus-4-6
    - claude-sonnet-4-6
    - claude-opus-4-5-20251101
    - claude-sonnet-4-5-20250929
  supportedPlatforms:
    Claude API: beta
    Claude Platform on AWS: beta
---

This page documents the prebuilt workers that serve a `self_hosted` environment. For task-oriented guides, start with [Self-hosted sandboxes](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes) and [Deploy self-hosted workers](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-workers).

## CLI commands and flags

| Command | Description |
| ----- | ----- |
| `ant beta:worker poll` | Claims work items from the environment’s queue and runs each session in process. With `--on-work`, calls your script for each work item instead. |
| `ant beta:worker run` | Handles one claimed session and exits. Use it as the entrypoint of a per-session sandbox. |

| Flag | Description |
| ----- | ----- |
| `--environment-id` | The environment to poll for work. Also reads from `ANTHROPIC_ENVIRONMENT_ID`. |
| `--environment-key` | Authenticates the worker with this environment. Also reads from `ANTHROPIC_ENVIRONMENT_KEY`. |
| `--workdir` | Directory where the worker downloads skills and where tools read and write files. Defaults to `.` (the current directory). The directory must exist before the worker starts. |
| `--on-work` | Script to call for each claimed work item instead of running tools in process. Receives session details as environment variables and the work item as JSON on standard input. |
| `--max-idle` | How long the worker waits while a session is idle before `ant beta:worker run` exits or `ant beta:worker poll` moves on to the next work item. Idle time with a [`requires_action` stop reason](https://platform.claude.com/docs/en/managed-agents/events-and-streaming#respond-when-the-session-goes-idle) does not count. Defaults to `60s`. Set it to `0` to turn off the timeout. With an `--on-work` script, `ant beta:worker poll` ignores this flag. Pass it instead to the `ant beta:worker run` command that your script starts. |
| `--log-format` | Log output format. Use `json` for structured log ingestion. Defaults to `text`. |

## Environment variables

| Variable | Description | Set by |
| ----- | ----- | ----- |
| `ANTHROPIC_ENVIRONMENT_ID` | The environment whose queue the worker serves. | You, on the worker host. The poller passes it to the `--on-work` script. |
| `ANTHROPIC_ENVIRONMENT_KEY` | Authenticates the worker to its queue. | You, on the worker host. The poller passes it to the `--on-work` script. |
| `ANTHROPIC_SESSION_ID` | The session that a claimed work item represents. | The poller, for the `--on-work` script. |
| `ANTHROPIC_WORK_ID` | The claimed work item. | The poller, for the `--on-work` script. |
| `ANTHROPIC_WORK_SECRET` | The work item’s secret for its session. | You. The poller does not set it. See [Forward the work item’s secret](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-per-session#forward-the-work-items-secret). |
| `ANTHROPIC_BASE_URL` | Overrides the default API endpoint. Optional. | You, on the worker host. |
| `ANTHROPIC_WEBHOOK_SIGNING_KEY` | Verifies incoming webhook payloads. | You, on a webhook handler host. |

## Host requirements

| Worker | Requirement |
| ----- | ----- |
| All workers | A Linux or macOS host with `/bin/bash` at that exact path. The worker’s `bash` tool runs it directly, without consulting `PATH`. On macOS, that is the system Bash 3.2. |
| TypeScript SDK | `unzip` and `tar` on the `PATH`, and Node.js 22 or later. |
| Python and Go SDKs | No additional binaries. These SDKs use their standard libraries for archive extraction. |

[Memory stores](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-memory#requirements) add their own requirements.

On macOS, the root volume is read-only, so `mkdir` can’t create `/workspace`. Set the worker’s working directory to one that you can write to, such as a `workspace` directory in your home directory. To use memory stores on macOS, first [prepare the macOS host](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-memory#prepare-a-macos-host).

## Sandbox filesystem

| Path | Contents |
| ----- | ----- |
| `/workspace` | The working directory in the samples on the self-hosted sandboxes pages. It is not the worker’s default: the worker uses the current directory unless you set `--workdir` or `workdir` (go: `Workdir`). Anthropic’s cloud sandboxes keep skills and repositories in `/workspace`. If you use a different working directory, update your agent’s system prompt so Claude can locate the skill files. |
| `<workdir>/skills/<name>/` | The agent’s downloaded skills. |
| `/mnt/memory/<store>/` | A local copy of each attached memory store, one directory per store. The API returns each directory’s full path in the `mount_path` (java, php: `mountPath`; csharp, go: `MountPath`) field of the session’s memory store resource (for example, `/mnt/memory/user-preferences/`). |

The worker creates the memory store directories when it claims a session. It removes them when it finishes with that session or when you [stop the worker gracefully](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-operations#stop-workers-gracefully). That removes only the local copies, and the memories stay in the store.

Skills can include executables that the agent can run directly. The CLI and SDK workers preserve the executable permissions recorded in the skill bundle when they extract it. If you download skills yourself, set their executable permissions yourself.

### When the worker finishes with a session

The worker finishes with a session in any of these cases:

* The session ends.
* You [stop the session’s work item](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-operations#stop-a-session-gracefully).
* The session stays idle for the worker’s idle limit. The session itself stays open. When you then send it a new event, such as a user message, the same worker or another one claims it. That worker downloads the stores again.

The idle limit is 60 seconds by default. To change it, use [`--max-idle`](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-reference#cli-commands-and-flags) for the `ant` CLI worker or [`max_idle` (typescript: `maxIdleMs`; go: `MaxIdle`)](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-reference#environment-worker) for `EnvironmentWorker`. The [`cma-sandboxes` Helm chart](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-per-session#run-sandboxes-on-kubernetes) starts its workers with a limit of 30 minutes instead. To change that limit, change the chart’s `sandbox.idleTimeout` setting.

### Final deliverables

Self-hosted sandboxes have no `/mnt/session/outputs` directory. On Anthropic’s cloud sandboxes, the session’s system prompt tells the agent to copy final deliverables there. On self-hosted environments, the system prompt leaves that instruction out. Final deliverables stay wherever the agent writes them, typically under the working directory, and the worker doesn’t upload them.

To collect final deliverables in one place, give the full path of a directory in your agent’s system prompt. Choose a directory that the worker’s file tools can write to:

* **Inside the working directory:** For example, `/workspace/outputs` if the working directory is `/workspace`.
* **Anywhere else, with an SDK worker only:** Add the directory to `allowed_roots` (typescript: `allowedRoots`; go: `AllowedRoots`). See [AgentToolContext and the agent toolset](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-reference#agent-tool-context-and-the-agent-toolset).

## SDK helpers

The Python, TypeScript, and Go SDKs provide three helpers at different levels of control:

| Helper | What it does | Use it when |
| ----- | ----- | ----- |
| [`EnvironmentWorker`](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-reference#environment-worker) | Handles polling, setup, and tool runs end to end. | Most cases. |
| [`work.poller()` (typescript: `new WorkPoller()`; go: `environments.NewWorkPoller()`)](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-reference#work-poller) | Polls the work queue and gives you each claimed session. | You determine how to handle each session, for example by launching a sandbox rather than running tools in process. |
| [`client.beta.sessions.events.tool_runner()` (typescript: `client.beta.sessions.events.toolRunner()`; go: `client.Beta.Sessions.Events.NewToolRunner()`)](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-reference#session-tool-runner) | Runs tool calls for a single session, given the session ID and a tool list. | You’ve already claimed the work and only need to run the tools. |

### EnvironmentWorker

| Method | Description |
| ----- | ----- |
| `run()` (go: `Run()`) | Runs indefinitely, picking up sessions as they arrive. |
| `handle_item()` (typescript: `handleItem()`; go: `HandleItem()`) | Handles one work item already claimed by a poller. The poller can be `ant beta:worker poll --on-work` or your own code. The method returns when the worker finishes with the item’s session. You can pass `work_id` (typescript: `workId`; go: `WorkID`), `session_id` (typescript: `sessionId`; go: `SessionID`), `environment_id` (typescript: `environmentId`; go: `EnvironmentID`), and `work_secret` (typescript: `workSecret`; go: `WorkSecret`). For each one that you leave out, the method reads the matching [`ANTHROPIC_*` variable](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-reference#environment-variables). |

| Option | Description |
| ----- | ----- |
| `tools` (go: `ToolsFunc`) | A factory that receives the session’s `AgentToolContext` and returns the tool list. Defaults to the standard agent toolset. |
| `max_idle` (typescript: `maxIdleMs`; go: `MaxIdle`) | How long the worker waits while a session is idle before it finishes with the session. Idle time with a [`requires_action` stop reason](https://platform.claude.com/docs/en/managed-agents/events-and-streaming#respond-when-the-session-goes-idle) does not count. Defaults to 60 seconds. To wait 5 minutes, set it to `300` (typescript: `300_000`; go: `anthropic.Ptr(5 * time.Minute)`). To turn the limit off, set it to `None` (typescript: `0`; go: `new(time.Duration)`). |
| `memory_sync_interval` (typescript: `memorySyncIntervalMs`; go: `MemorySyncInterval`) | The shortest time between two syncs of the attached memory stores while the session runs. The worker checks the interval after each call to a tool that runs in your sandbox, not on a timer. Defaults to 15 seconds. See [Sync interval](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-memory#sync-interval). |
| `memory_sync_deletions` (typescript: `memorySyncDeletions`; go: `MemorySyncDeletions`) | Whether files the agent deletes locally are also deleted from the store. See [Deletions](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-memory#deletions). |

`EnvironmentWorker` manages the `AgentToolContext` and the toolset automatically. Pass a `tools` (go: `ToolsFunc`) factory to customize the tool list:

<CodeGroup exclude="shell, csharp, java, php, ruby">
  <CodeGroupItem language="cURL">
    A worker is a long-running process, not a single HTTP request. To customize the tool list, use `EnvironmentWorker` in the Python, TypeScript, or Go SDK.
  </CodeGroupItem>

  <CodeGroupItem language="CLI">
    The `ant` CLI worker always uses the standard agent toolset. To customize the tool list, use `EnvironmentWorker` in the Python, TypeScript, or Go SDK.
  </CodeGroupItem>

  ```python Python
  import asyncio
  import contextlib
  import os
  import signal
  from anthropic import AsyncAnthropic, beta_async_tool
  from anthropic.lib.environments import EnvironmentWorker
  from anthropic.lib.tools.agent_toolset import beta_bash_tool


  @beta_async_tool
  async def get_order_status(order_id: str) -> str:
      """Look up an order in the internal fulfillment system by order ID."""
      return f"Order {order_id}: shipped"


  async def main() -> None:
      environment_key = os.environ["ANTHROPIC_ENVIRONMENT_KEY"]
      environment_id = os.environ["ANTHROPIC_ENVIRONMENT_ID"]
      async with AsyncAnthropic(auth_token=environment_key) as client:
          worker = EnvironmentWorker(
              client,
              environment_id=environment_id,
              environment_key=environment_key,
              # List every tool that the agent can call. The worker answers no other tool.
              tools=lambda env: [beta_bash_tool(env), get_order_status],
          )
          task = asyncio.create_task(worker.run())
          loop = asyncio.get_running_loop()
          for signum in (signal.SIGINT, signal.SIGTERM):
              loop.add_signal_handler(signum, task.cancel)
          with contextlib.suppress(asyncio.CancelledError):
              await task


  asyncio.run(main())
  ```

  ```typescript TypeScript
  import Anthropic from "@anthropic-ai/sdk";
  import { EnvironmentWorker } from "@anthropic-ai/sdk/helpers/beta/environments";
  import { betaTool } from "@anthropic-ai/sdk/helpers/beta/json-schema";
  import { betaBashTool } from "@anthropic-ai/sdk/tools/agent-toolset/node";

  const getOrderStatus = betaTool({
    name: "get_order_status",
    description: "Look up an order in the internal fulfillment system by order ID.",
    inputSchema: {
      type: "object",
      properties: { order_id: { type: "string", description: "The order ID" } },
      required: ["order_id"]
    },
    run: async ({ order_id }) => `Order ${order_id}: shipped`
  });

  const environmentKey = process.env.ANTHROPIC_ENVIRONMENT_KEY!;
  const environmentId = process.env.ANTHROPIC_ENVIRONMENT_ID!;
  const client = new Anthropic({ authToken: environmentKey });
  const controller = new AbortController();
  process.once("SIGINT", () => controller.abort());
  process.once("SIGTERM", () => controller.abort());

  await new EnvironmentWorker({
    client,
    environmentId,
    environmentKey,
    signal: controller.signal,
    // List every tool that the agent can call. The worker answers no other tool.
    tools: (ctx) => [betaBashTool(ctx), getOrderStatus]
  }).run();
  ```

  <CodeGroupItem language="C#">
    The C# SDK does not have `EnvironmentWorker`. To answer custom tool calls from your own code, send each result on the session’s event stream, as in [Return a custom tool result](https://platform.claude.com/docs/en/managed-agents/events-and-streaming#return-a-custom-tool-result).
  </CodeGroupItem>

  ```go Go
  package main

  import (
  	"context"
  	"log"
  	"os"
  	"os/signal"
  	"syscall"

  	"github.com/anthropics/anthropic-sdk-go/v2"
  	"github.com/anthropics/anthropic-sdk-go/v2/lib/environments"
  	"github.com/anthropics/anthropic-sdk-go/v2/option"
  	"github.com/anthropics/anthropic-sdk-go/v2/toolrunner"
  	"github.com/anthropics/anthropic-sdk-go/v2/tools/agenttoolset"
  )

  type orderStatusInput struct {
  	OrderID string `json:"order_id"`
  }

  func main() {
  	environmentKey := os.Getenv("ANTHROPIC_ENVIRONMENT_KEY")
  	environmentID := os.Getenv("ANTHROPIC_ENVIRONMENT_ID")

  	ctx, stop := signal.NotifyContext(context.Background(), os.Interrupt, syscall.SIGTERM)
  	defer stop()

  	getOrderStatus := toolrunner.NewBetaTool(
  		"get_order_status",
  		"Look up an order in the internal fulfillment system by order ID.",
  		anthropic.BetaToolInputSchemaParam{
  			Properties: map[string]any{
  				"order_id": map[string]any{"type": "string", "description": "The order ID"},
  			},
  			Required: []string{"order_id"},
  		},
  		func(ctx context.Context, input orderStatusInput) (anthropic.BetaToolResultBlockParamContentUnion, error) {
  			return anthropic.BetaToolResultBlockParamContentUnion{
  				OfText: &anthropic.BetaTextBlockParam{Text: "Order " + input.OrderID + ": shipped"},
  			}, nil
  		},
  	)

  	client := anthropic.NewClient(option.WithAuthToken(environmentKey))

  	worker := environments.NewEnvironmentWorker(client, environments.EnvironmentWorkerOptions{
  		EnvironmentID:  environmentID,
  		EnvironmentKey: environmentKey,
  		// List every tool that the agent can call. The worker answers no other tool.
  		ToolsFunc: func(env *agenttoolset.AgentToolContext) []anthropic.BetaTool {
  			return []anthropic.BetaTool{agenttoolset.BetaBashTool(env), getOrderStatus}
  		},
  	})
  	if err := worker.Run(ctx); err != nil {
  		log.Fatalf("worker: %v", err)
  	}
  }
  ```

  <CodeGroupItem language="Java">
    The Java SDK does not have `EnvironmentWorker`. To answer custom tool calls from your own code, send each result on the session’s event stream, as in [Return a custom tool result](https://platform.claude.com/docs/en/managed-agents/events-and-streaming#return-a-custom-tool-result).
  </CodeGroupItem>

  <CodeGroupItem language="PHP">
    The PHP SDK does not have `EnvironmentWorker`. To answer custom tool calls from your own code, send each result on the session’s event stream, as in [Return a custom tool result](https://platform.claude.com/docs/en/managed-agents/events-and-streaming#return-a-custom-tool-result).
  </CodeGroupItem>

  <CodeGroupItem language="Ruby">
    The Ruby SDK does not have `EnvironmentWorker`. To answer custom tool calls from your own code, send each result on the session’s event stream, as in [Return a custom tool result](https://platform.claude.com/docs/en/managed-agents/events-and-streaming#return-a-custom-tool-result).
  </CodeGroupItem>
</CodeGroup>

### Work poller

| Option | Description |
| ----- | ----- |
| `drain` (go: `Drain`) | Whether to stop polling once the queue is empty rather than waiting for new work. |
| `block_ms` (typescript: `blockMs`; go: `BlockMs`) | How long each poll waits for work to arrive before returning, in milliseconds. Must be between 1 and 999. The helper polls again automatically. Pass `null` (python: `None`; go: `param.Null[int64]()`) for a non-blocking check. Defaults to a 999ms long-poll. |
| `reclaim_older_than_ms` (typescript: `reclaimOlderThanMs`; go: `ReclaimOlderThanMs`) | Reclaims work items that were claimed but never acknowledged within this many milliseconds. |
| `auto_stop` (typescript: `autoStop`; go: `AutoStop`) | Whether the poller posts a stop signal for each work item once your loop body finishes with it. Defaults to `true` (python: `True`). Set it to `false` (python: `False`; go: `param.NewOpt(false)`) in the two cases that follow this table. |

Set `auto_stop` (typescript: `autoStop`; go: `AutoStop`) to `false` (python: `False`; go: `param.NewOpt(false)`) in two cases:

1. Your loop calls `handle_item()` (typescript: `handleItem()`; go: `HandleItem()`), which posts the stop itself.
2. Your loop launches a sandbox for the item and moves on. The worker in that sandbox must post the stop when the session’s work ends, as `ant beta:worker run` and `handle_item()` (typescript: `handleItem()`; go: `HandleItem()`) do.

For a complete example, see [Launch sandboxes from the SDK poller](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-per-session#launch-sandboxes-from-the-sdk-poller).

### Session tool runner

`client.beta.sessions.events.tool_runner()` (typescript: `client.beta.sessions.events.toolRunner()`; go: `client.Beta.Sessions.Events.NewToolRunner()`) takes a tool list as `tools` (go: `Tools`). To build that list, set up `AgentToolContext` yourself and call `beta_agent_toolset_20260401(env)` (typescript: `betaAgentToolset20260401(ctx)`; go: `agenttoolset.BetaAgentToolset20260401(env)`):

<CodeGroup exclude="shell, csharp, java, php, ruby">
  <CodeGroupItem language="cURL">
    `AgentToolContext` is a helper in the Python, TypeScript, and Go SDKs. cURL has no equivalent. Use one of those SDKs.
  </CodeGroupItem>

  <CodeGroupItem language="CLI">
    `AgentToolContext` is a helper in the Python, TypeScript, and Go SDKs. The `ant` CLI has no equivalent. Use one of those SDKs.
  </CodeGroupItem>

  ```python Python
  from anthropic.lib.tools.agent_toolset import (
      AgentToolContext,
      beta_agent_toolset_20260401,
  )

  async with AgentToolContext(
      workdir="/workspace", client=client, session_id=work.data.id
  ) as env:
      # skills downloaded to /workspace/skills/<name>/
      tools = beta_agent_toolset_20260401(env)
  ```

  ```typescript TypeScript
  import {
    setupSkills,
    betaAgentToolset20260401
  } from "@anthropic-ai/sdk/tools/agent-toolset/node";

  const ctx = { workdir: "/workspace", client, sessionId: work.data.id };
  await setupSkills(ctx);
  const tools = betaAgentToolset20260401(ctx);
  ```

  <CodeGroupItem language="C#">
    The C# SDK does not have `AgentToolContext`.
  </CodeGroupItem>

  ```go Go
  env := &agenttoolset.AgentToolContext{Workdir: "/workspace"}
  if err := env.SetupSkills(ctx, client, work.Data.ID); err != nil {
  	panic(err)
  }
  // skills downloaded to /workspace/skills/<name>/
  tools := agenttoolset.BetaAgentToolset20260401(env)
  ```

  <CodeGroupItem language="Java">
    The Java SDK does not have `AgentToolContext`.
  </CodeGroupItem>

  <CodeGroupItem language="PHP">
    The PHP SDK does not have `AgentToolContext`.
  </CodeGroupItem>

  <CodeGroupItem language="Ruby">
    The Ruby SDK does not have `AgentToolContext`.
  </CodeGroupItem>
</CodeGroup>

### AgentToolContext and the agent toolset

`AgentToolContext` is the execution context for tool calls. It defines the working directory and path policy, and can download the session’s skills.

| Option | Description |
| ----- | ----- |
| `allowed_roots` (typescript: `allowedRoots`; go: `AllowedRoots`) | Directories, in addition to the working directory, that the file tools (`read`, `write`, `edit`, `glob`, `grep`) can reach. |
| `read_only_roots` (typescript: `readOnlyRoots`; go: `ReadOnlyRoots`) | Directories under which `write` and `edit` refuse paths. |

`EnvironmentWorker` adds the session’s memory store directories to `allowed_roots` (typescript: `allowedRoots`; go: `AllowedRoots`) itself, and the directories of stores attached with `access: "read_only"` to `read_only_roots` (typescript: `readOnlyRoots`; go: `ReadOnlyRoots`).

The confinement is a guardrail for the file tools only, not a sandbox. It does not constrain `bash`.

`beta_agent_toolset_20260401(env)` (typescript: `betaAgentToolset20260401(ctx)`; go: `agenttoolset.BetaAgentToolset20260401(env)`) takes an `AgentToolContext` and returns the standard tool implementations (`bash`, `read`, `write`, `edit`, `glob`, `grep`).
