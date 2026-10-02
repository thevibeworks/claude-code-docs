---
title: Monitor and troubleshoot self-hosted workers
url: https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-operations
description: Read queue depth, stop sessions and workers without losing work, and fix common self-hosted sandbox failures.
featureMetadata:
  topic:
    title: Managed Agents
    url: https://platform.claude.com/docs/en/managed-agents/overview
  status: beta
  betaHeader: managed-agents-2026-04-01
---

The monitoring calls on this page run from your monitoring or operations tooling, authenticated with your Claude API key. The worker helpers handle the claim and keep-alive loop, so you don't call those endpoints directly.

<Warning>
  These endpoints accept either your organization API key or the environment key. Call them from outside the worker host with your organization API key. Setting `ANTHROPIC_API_KEY` on the worker host exposes an organization-scoped credential to agent tool calls.
</Warning>

## Read queue depth

`GET /v1/environments/{environment_id}/work/stats` (curl; python, typescript, ruby: `client.beta.environments.work.stats()`; go, csharp: `client.Beta.Environments.Work.Stats()`; java: `client.beta().environments().work().stats()`; php: `$client->beta->environments->work->stats()`; cli: `ant beta:environments:work stats`) returns the queue state for an environment:

| Field              | Meaning                                                                                                                                                         | Use it to                                                                                             |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `depth`            | Items waiting to be claimed.                                                                                                                                    | Scale your worker fleet or alert on backlog.                                                          |
| `pending`          | Items claimed by a worker but not yet acknowledged. The worker helpers acknowledge each item before processing it, so this stays near zero in normal operation. | Detect a worker that stalled between claiming and acknowledging: alert on a sustained non-zero value. |
| `oldest_queued_at` | Timestamp of the oldest item still in the queue, either waiting to be claimed or claimed but not yet acknowledged. `null` when there is none.                   | See how long the oldest item has waited.                                                              |
| `workers_polling`  | Workers that have polled in the last 30 seconds.                                                                                                                | Alert on liveness.                                                                                    |

<CodeGroup>
  ```bash cURL
  curl -sS "https://api.anthropic.com/v1/environments/$ANTHROPIC_ENVIRONMENT_ID/work/stats" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-beta: managed-agents-2026-04-01" \
    -H "anthropic-version: 2023-06-01"
  ```

  ```bash CLI
  ant beta:environments:work stats --environment-id "$ANTHROPIC_ENVIRONMENT_ID"
  ```

  ```python Python
  import os

  import anthropic

  client = anthropic.Anthropic()

  stats = client.beta.environments.work.stats(os.environ["ANTHROPIC_ENVIRONMENT_ID"])
  print(f"depth={stats.depth} pending={stats.pending}")
  ```

  ```typescript TypeScript
  import Anthropic from "@anthropic-ai/sdk";

  const client = new Anthropic();

  const stats = await client.beta.environments.work.stats(process.env.ANTHROPIC_ENVIRONMENT_ID!);

  console.log(`depth=${stats.depth} pending=${stats.pending}`);
  ```

  ```csharp C#
  using Anthropic;

  var client = new AnthropicClient();

  var environmentId = Environment.GetEnvironmentVariable("ANTHROPIC_ENVIRONMENT_ID")!;

  var stats = await client.Beta.Environments.Work.Stats(environmentId);

  Console.WriteLine($"depth={stats.Depth} pending={stats.Pending}");
  ```

  ```go Go
  package main

  import (
  	"context"
  	"fmt"
  	"os"

  	"github.com/anthropics/anthropic-sdk-go"
  )

  func main() {
  	client := anthropic.NewClient()
  	environmentID := os.Getenv("ANTHROPIC_ENVIRONMENT_ID")

  	stats, err := client.Beta.Environments.Work.Stats(
  		context.Background(),
  		environmentID,
  		anthropic.BetaEnvironmentWorkStatsParams{},
  	)
  	if err != nil {
  		panic(err)
  	}

  	fmt.Printf("depth=%d pending=%d\n", stats.Depth, stats.Pending)
  }
  ```

  ```java Java
  import com.anthropic.client.AnthropicClient;
  import com.anthropic.client.okhttp.AnthropicOkHttpClient;
  import com.anthropic.models.beta.environments.work.BetaSelfHostedWorkQueueStats;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      BetaSelfHostedWorkQueueStats stats = client.beta()
          .environments()
          .work()
          .stats(System.getenv("ANTHROPIC_ENVIRONMENT_ID"));

      IO.println("depth=" + stats.depth() + " pending=" + stats.pending());
  }
  ```

  ```php PHP
  <?php

  use Anthropic\Client;

  $client = new Client();

  $stats = $client->beta->environments->work->stats(getenv('ANTHROPIC_ENVIRONMENT_ID'));

  printf("depth=%d pending=%d\n", $stats->depth, $stats->pending);
  ```

  ```ruby Ruby
  require "anthropic"

  client = Anthropic::Client.new

  stats = client.beta.environments.work.stats(ENV.fetch("ANTHROPIC_ENVIRONMENT_ID"))

  puts "depth=#{stats.depth} pending=#{stats.pending}"
  ```
</CodeGroup>

```text wrap
{
  "type": "work_queue_stats",
  "depth": 0,
  "pending": 0,
  "oldest_queued_at": null,
  "workers_polling": 0
}
```

## Stop a session gracefully

Use `POST /v1/environments/{environment_id}/work/{work_id}/stop` (curl; python, typescript, ruby: `client.beta.environments.work.stop()`; go, csharp: `client.Beta.Environments.Work.Stop()`; java: `client.beta().environments().work().stop()`; php: `$client->beta->environments->work->stop()`; cli: `ant beta:environments:work stop`) to ask the worker handling a specific session to shut it down.

By default the work item moves to `stopping`. The worker notices on its next lease heartbeat, cancels the session's in-flight tool call, and confirms the shutdown. The work item then becomes `stopped`.

Pass `force: true` (python: `force=True`; cli: `--force`) to mark the work item `stopped` immediately instead of waiting for the worker's confirmation.

Because these calls run from your operations tooling rather than the worker host, `ANTHROPIC_WORK_ID` isn't set automatically. Set it to the target work item's ID before running the following examples. To find a work item's ID, list the environment's work items through the [Environments Work endpoints](https://platform.claude.com/docs/en/api/beta/environments/work).

<CodeGroup>
  ```bash cURL
  curl -sS "https://api.anthropic.com/v1/environments/$ANTHROPIC_ENVIRONMENT_ID/work/$ANTHROPIC_WORK_ID/stop" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-beta: managed-agents-2026-04-01" \
    -H "anthropic-version: 2023-06-01" \
    -H "content-type: application/json" \
    -d '{}'
  ```

  ```bash CLI
  ant beta:environments:work stop \
    --environment-id "$ANTHROPIC_ENVIRONMENT_ID" \
    --work-id "$ANTHROPIC_WORK_ID"
  ```

  ```python Python
  import os

  import anthropic

  client = anthropic.Anthropic()

  work = client.beta.environments.work.stop(
      os.environ["ANTHROPIC_WORK_ID"],
      environment_id=os.environ["ANTHROPIC_ENVIRONMENT_ID"],
  )
  print(work.state)
  ```

  ```typescript TypeScript
  import Anthropic from "@anthropic-ai/sdk";

  const client = new Anthropic();

  const work = await client.beta.environments.work.stop(process.env.ANTHROPIC_WORK_ID!, {
    environment_id: process.env.ANTHROPIC_ENVIRONMENT_ID!
  });

  console.log(work.state);
  ```

  ```csharp C#
  using Anthropic;

  var client = new AnthropicClient();

  var work = await client.Beta.Environments.Work.Stop(
      Environment.GetEnvironmentVariable("ANTHROPIC_WORK_ID")!,
      new()
      {
          EnvironmentID = Environment.GetEnvironmentVariable("ANTHROPIC_ENVIRONMENT_ID")!
      }
  );

  Console.WriteLine(work.State);
  ```

  ```go Go
  package main

  import (
  	"context"
  	"fmt"
  	"os"

  	"github.com/anthropics/anthropic-sdk-go"
  )

  func main() {
  	client := anthropic.NewClient()

  	work, err := client.Beta.Environments.Work.Stop(
  		context.Background(),
  		os.Getenv("ANTHROPIC_WORK_ID"),
  		anthropic.BetaEnvironmentWorkStopParams{
  			EnvironmentID: os.Getenv("ANTHROPIC_ENVIRONMENT_ID"),
  		},
  	)
  	if err != nil {
  		panic(err)
  	}
  	fmt.Println(work.State)
  }
  ```

  ```java Java
  import com.anthropic.client.AnthropicClient;
  import com.anthropic.client.okhttp.AnthropicOkHttpClient;
  import com.anthropic.models.beta.environments.work.BetaSelfHostedWork;
  import com.anthropic.models.beta.environments.work.BetaSelfHostedWorkStopRequest;
  import com.anthropic.models.beta.environments.work.WorkStopParams;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      BetaSelfHostedWork work = client.beta().environments().work().stop(
          WorkStopParams.builder()
              .environmentId(System.getenv("ANTHROPIC_ENVIRONMENT_ID"))
              .workId(System.getenv("ANTHROPIC_WORK_ID"))
              .betaSelfHostedWorkStopRequest(BetaSelfHostedWorkStopRequest.builder().build())
              .build()
      );

      IO.println(work.state());
  }
  ```

  ```php PHP
  <?php

  use Anthropic\Client;

  $client = new Client();

  $work = $client->beta->environments->work->stop(
      getenv('ANTHROPIC_WORK_ID'),
      environmentID: getenv('ANTHROPIC_ENVIRONMENT_ID'),
  );

  echo $work->state . "\n";
  ```

  ```ruby Ruby
  require "anthropic"

  client = Anthropic::Client.new

  work = client.beta.environments.work.stop(
    ENV.fetch("ANTHROPIC_WORK_ID"),
    environment_id: ENV.fetch("ANTHROPIC_ENVIRONMENT_ID")
  )

  puts work.state
  ```
</CodeGroup>

## Stop workers gracefully

A worker that is cancelled while a session runs stops its in-flight work before it exits. If the session has [memory stores](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-memory) attached, the worker skips the final sync but still uploads changed files and removes the store directories.

A killed process runs no teardown. To stop a worker cleanly:

1. **Make sure SIGTERM and SIGINT cancel the worker.** How depends on the worker:

   | Worker                             | What to do                                                                                                                             |
   | ---------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
   | `ant` CLI                          | Nothing. The CLI handles both signals itself: it cancels any in-flight tool call, posts its error result, and releases the work item.  |
   | SDK worker that is its own process | `EnvironmentWorker` installs no signal handlers. Cancel the worker from a signal handler, as the standalone worker examples do.        |
   | SDK worker inside a webhook server | Cancel the worker from the server's own shutdown hook, as the webhook examples do. The worker must not take over the server's signals. |

2. **Stop the worker with SIGTERM, and allow at least 30 seconds before any hard kill.** The final upload can take that long. Docker sends SIGKILL 10 seconds after the stop signal by default. Raise that limit with `--stop-timeout` on `docker run`, or with your orchestrator's termination grace period.

If a worker is killed before its teardown runs, any memory edits that had not synced are lost. On a long-lived host, also remove the leftover store directory under `/mnt/memory/` before the next session that attaches that store. A sandbox that serves one session and is then discarded needs no cleanup.

## Troubleshooting

### The worker doesn't connect

If `workers_polling` stays at 0, the worker isn't reaching the queue. Confirm that `ANTHROPIC_ENVIRONMENT_KEY` and `ANTHROPIC_ENVIRONMENT_ID` are set on the worker host.

### A session stays queued

No worker is claiming work. A queued session waits rather than failing. Check `workers_polling` and `depth` in [Read queue depth](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-operations#read-queue-depth).

### Memory stores fail to mount

The worker logs mount and background sync failures rather than reporting them to the session. Only read-only refusals reach the agent, as tool errors (see [Read-only stores and conflicts](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-memory#read-only-stores-and-conflicts)).

If the worker cannot mount a memory store when it claims a session, it fails the work item. The session emits no error event and stays idle.

| Symptom                                                                                                                                 | Cause                                                                                                                                                                                | Fix                                                                                                                                                                                                                                                    |
| --------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| The worker log contains `the work item carried no sessions token` (in Go, the `ErrSessionMemoryNoToken` error) and the work item fails. | The work item's per-session `secret` did not reach the worker. Either your code did not forward it, or memory stores on self-hosted sandboxes are not enabled for your organization. | [Forward the work item's secret](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-workers#forward-the-work-items-secret). If the worker polls and runs sessions in one process and still logs this, contact support.           |
| The worker log contains `something already exists at the memory store's path`.                                                          | A directory left over from a previous session, usually one whose worker was killed before its teardown ran.                                                                          | Remove the leftover directory that the log line names. Edits in it that had not synced are lost.                                                                                                                                                       |
| The worker log contains `cannot create the memory store's folder` and `the worker host must make this mount path writable`.             | The user the worker runs as cannot create directories under `/mnt/memory`.                                                                                                           | Create `/mnt/memory` and `chown` it to that user. See [Prepare the host](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-memory#prepare-the-host).                                                                            |
| The session sits `idle` with a `requires_action` stop reason and no error event shortly after a worker claimed it.                      | The worker failed the work item because it could not mount a memory store, for one of the preceding reasons.                                                                         | Fix the cause on the host, then send a [`user.interrupt`](https://platform.claude.com/docs/en/managed-agents/events-and-streaming#integrating-events) event. The session's work is queued again, and the next worker that claims it retries the mount. |

### A custom tool call never returns

If the session sits paused with a `requires_action` stop reason, no worker or client serves that tool. See [Serve a custom tool](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-custom-tools#serve-a-custom-tool).

### A wrapped MCP tool call hangs

Without a timeout on the MCP client, a hung call to a [wrapped MCP server](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-custom-tools#wrap-an-mcp-server-as-custom-tools) becomes an error tool result only when a backstop fires:

| SDK        | Backstop                                                       | Fires after                  |
| ---------- | -------------------------------------------------------------- | ---------------------------- |
| Python     | The worker's own tool call limit                               | About two and a half minutes |
| TypeScript | The MCP SDK's default request timeout                          | About a minute               |
| Go         | The worker cancels a tool call that outlives its default limit | 120 seconds                  |
