---
title: Deploy self-hosted workers
url: https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-workers
description: Choose how self-hosted sandbox workers claim work and where sessions run, then run an always-on worker or trigger workers from webhooks.
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

The [self-hosted sandboxes quickstart](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes#quickstart) runs one `ant` CLI worker that polls continuously and runs every session in one process. This page helps you choose a deployment pattern and then covers always-on and webhook-triggered workers.

## Choose a deployment pattern

When deploying workers, you need to make two choices: how the worker claims work, and where each session runs.

**How the worker claims work:**

* **Always-on:** A long-running process polls the queue continuously. The process makes only outbound HTTPS requests, so you don’t expose an endpoint to Anthropic.
* **Webhook-triggered:** A handler wakes on `session.status_run_started` and starts polling. This avoids an idle poller, but requires a [webhook](https://platform.claude.com/docs/en/managed-agents/webhooks) endpoint that Anthropic can reach.

**Where each session runs:**

* **In process:** The worker that claims a session also runs its tool calls, in one shared working directory.
* **Sandbox per session:** A poller launches a fresh sandbox for each claimed session. Choose this for stronger isolation: a fresh filesystem, resource limits, or per-session network controls. See [Run one sandbox per session](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-per-session), which also covers the Helm chart for Kubernetes.

The CLI and SDK workers support different combinations:

| Capability                                                                                                  | `ant` CLI                       | SDK (Python, TypeScript, Go) |
| ----------------------------------------------------------------------------------------------------------- | ------------------------------- | ---------------------------- |
| Always-on polling                                                                                           | Yes                             | Yes                          |
| Webhook-triggered                                                                                           | No                              | Yes                          |
| [Sandbox per session](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-per-session) | Yes                             | Yes                          |
| [Memory stores](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-memory)            | Yes, with default sync settings | Yes, with configurable sync  |
| [Custom tools](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-custom-tools)       | No                              | Yes                          |

See [Self-hosted worker reference](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-reference) for every CLI flag and SDK option.

For more control, call the [Environments Work endpoints](https://platform.claude.com/docs/en/api/beta/environments/work) directly and implement your own worker. Your worker then does what the SDK workers do. Among other things, it acknowledges each work item, sends heartbeats, and downloads the agent’s skills. It runs only the tool calls that the session’s [permission policy](https://platform.claude.com/docs/en/managed-agents/permission-policies#see-how-each-call-was-evaluated) allows. It returns each result as a `user.tool_result` or `user.custom_tool_result` event. At the end, it stops the item. Use the worker’s source in the [Python SDK](https://github.com/anthropics/anthropic-sdk-python/tree/main/src/anthropic/lib/environments), the [TypeScript SDK](https://github.com/anthropics/anthropic-sdk-typescript/tree/main/src/lib/environments), or the [Go SDK](https://github.com/anthropics/anthropic-sdk-go/tree/main/lib/environments) as a reference.

## Run an always-on worker

These samples use `/workspace` as the worker’s working directory. The directory must exist before the worker starts. On a new host, create it and give the worker’s user write access, as in the “Start the worker” step of [Run your first session](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes#run-your-first-session).

On macOS, `mkdir` can’t create `/workspace`, because the root volume is read-only. Create `~/workspace` instead, as that step shows. In place of `/workspace`, use the full path that `echo ~/workspace` prints, because the SDK doesn’t expand `~`.

Start a worker that polls the queue continuously. It authenticates with the [environment key](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes#run-your-first-session) from the quickstart:

<CodeGroup exclude="shell:cURL, csharp, java, php, ruby">
  <CodeGroupItem language="cURL">
    A worker is a long-running process, not a single HTTP request. Run the `ant` CLI worker instead: `ant beta:worker poll --workdir /workspace`.
  </CodeGroupItem>

  ```bash CLI
  ant beta:worker poll --workdir /workspace
  ```

  ```python Python
  import asyncio
  import contextlib
  import os
  import signal
  from anthropic import AsyncAnthropic
  from anthropic.lib.environments import EnvironmentWorker


  async def main() -> None:
      environment_key = os.environ["ANTHROPIC_ENVIRONMENT_KEY"]
      environment_id = os.environ["ANTHROPIC_ENVIRONMENT_ID"]
      async with AsyncAnthropic(auth_token=environment_key) as client:
          worker = EnvironmentWorker(
              client,
              environment_id=environment_id,
              environment_key=environment_key,
              workdir="/workspace",
          )
          task = asyncio.create_task(worker.run())
          # Canceling the task, rather than killing the process, lets the worker stop its
          # in-flight work item and upload changed memory files before it exits.
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

  const environmentKey = process.env.ANTHROPIC_ENVIRONMENT_KEY!;
  const environmentId = process.env.ANTHROPIC_ENVIRONMENT_ID!;
  const client = new Anthropic({ authToken: environmentKey });
  const controller = new AbortController();
  // Aborting on either signal lets the worker upload changed memory files and remove its
  // store directories before the process exits.
  process.once("SIGINT", () => controller.abort());
  process.once("SIGTERM", () => controller.abort());

  await new EnvironmentWorker({
    client,
    environmentId,
    environmentKey,
    workdir: "/workspace",
    signal: controller.signal
  }).run();
  ```

  <CodeGroupItem language="C#">
    The C# SDK does not have `EnvironmentWorker`. Run the `ant` CLI worker instead: `ant beta:worker poll --workdir /workspace`.
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
  )

  func main() {
  	environmentKey := os.Getenv("ANTHROPIC_ENVIRONMENT_KEY")
  	environmentID := os.Getenv("ANTHROPIC_ENVIRONMENT_ID")

  	ctx, stop := signal.NotifyContext(context.Background(), os.Interrupt, syscall.SIGTERM)
  	defer stop()

  	client := anthropic.NewClient(option.WithAuthToken(environmentKey))

  	worker := environments.NewEnvironmentWorker(client, environments.EnvironmentWorkerOptions{
  		EnvironmentID:  environmentID,
  		EnvironmentKey: environmentKey,
  		Workdir:        "/workspace",
  	})
  	if err := worker.Run(ctx); err != nil {
  		log.Fatalf("worker: %v", err)
  	}
  }
  ```

  <CodeGroupItem language="Java">
    The Java SDK does not have `EnvironmentWorker`. Run the `ant` CLI worker instead: `ant beta:worker poll --workdir /workspace`.
  </CodeGroupItem>

  <CodeGroupItem language="PHP">
    The PHP SDK does not have `EnvironmentWorker`. Run the `ant` CLI worker instead: `ant beta:worker poll --workdir /workspace`.
  </CodeGroupItem>

  <CodeGroupItem language="Ruby">
    The Ruby SDK does not have `EnvironmentWorker`. Run the `ant` CLI worker instead: `ant beta:worker poll --workdir /workspace`.
  </CodeGroupItem>
</CodeGroup>

## Trigger workers from webhooks

<Steps>
  <Step title="Subscribe to session webhooks">
    In the [Claude Console](https://platform.claude.com/settings/workspaces/default/webhooks), define a webhook endpoint that listens for `session.status_run_started` events. See [Subscribe to webhooks](https://platform.claude.com/docs/en/managed-agents/webhooks) for details.
  </Step>

  <Step title="Export the webhook signing key">
    Along with the environment ID and key from [Run your first session](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes#run-your-first-session), export the webhook signing key on your handler host. The handler uses it to verify incoming payloads.

    ```bash
    export ANTHROPIC_WEBHOOK_SIGNING_KEY="whsec_..."
    ```
  </Step>

  <Step title="Implement the webhook handler">
    Start the worker when `session.status_run_started` fires. The handler drains the queue and hands each claimed work item to `handle_item()` (typescript: `handleItem()`; go: `HandleItem()`) (in the Python, TypeScript, and Go SDKs). That method downloads skills, runs tool calls, posts results back, and returns.

    The samples use `/workspace` as the working directory. Before you start the handler, create that directory on the handler host. Make sure that the handler’s user can write to it, as in the “Start the worker” step of [Run your first session](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes#run-your-first-session).

    <CodeGroup exclude="shell, csharp, java, php, ruby">
      <CodeGroupItem language="cURL">
        This handler needs more logic than a single shell command. Use the Python, TypeScript, or Go SDK to run it.
      </CodeGroupItem>

      <CodeGroupItem language="CLI">
        This handler needs more logic than a single shell command. Use the Python, TypeScript, or Go SDK to run it.
      </CodeGroupItem>

      <CodeGroupItem>
        To verify webhook signatures, install the webhooks extra: `pip install "anthropic[webhooks]"`.

        ```python Python
        import asyncio
        import os
        import anthropic
        import standardwebhooks  # installed by the anthropic[webhooks] extra

        environment_key = os.environ["ANTHROPIC_ENVIRONMENT_KEY"]
        environment_id = os.environ["ANTHROPIC_ENVIRONMENT_ID"]
        client = anthropic.AsyncAnthropic(
            auth_token=environment_key,
        )
        # Canceled by shutdown() so an in-flight work item can upload changed memory files and
        # remove its store directories before the process exits.
        inflight: set[asyncio.Task[None]] = set()


        # Await this from the host's shutdown hook, such as an ASGI lifespan shutdown (the code after
        # `yield` in a FastAPI lifespan), which uvicorn runs on SIGTERM. uvicorn lets open requests
        # finish before that hook runs, so set --timeout-graceful-shutdown to bound the wait.
        async def shutdown() -> None:
            for task in inflight:
                task.cancel()
            await asyncio.gather(*inflight, return_exceptions=True)


        async def handle(raw: bytes, headers: dict[str, str]) -> tuple[dict[str, str], int]:
            try:
                event = client.beta.webhooks.unwrap(raw.decode(), headers=headers)
            except standardwebhooks.WebhookVerificationError:
                return {"error": "signature verification failed"}, 401
            if event.data.type != "session.status_run_started":
                return {"status": "ignored"}, 200
            task = asyncio.create_task(run_queued_work())
            inflight.add(task)
            task.add_done_callback(inflight.discard)
            try:
                # Shielded: a dropped or timed-out delivery must not cancel the item; shutdown() does.
                await asyncio.shield(task)
            except asyncio.CancelledError:
                return {"status": "shutting down"}, 503
            return {"status": "ok"}, 200


        async def run_queued_work() -> None:
            async for work in client.beta.environments.work.poller(
                environment_id=environment_id,
                environment_key=environment_key,
                block_ms=None,
                reclaim_older_than_ms=2000,
                drain=True,
                auto_stop=False,
            ):
                await client.beta.environments.work.worker(workdir="/workspace").handle_item(
                    work_id=work.id,
                    environment_id=environment_id,
                    session_id=work.data.id,
                    environment_key=environment_key,
                    # The per-session secret is what lets the worker mount the session's memory stores.
                    work_secret=work.secret,
                )
        ```
      </CodeGroupItem>

      ```typescript TypeScript
      import Anthropic from "@anthropic-ai/sdk";

      const environmentKey = process.env.ANTHROPIC_ENVIRONMENT_KEY!;
      const environmentId = process.env.ANTHROPIC_ENVIRONMENT_ID!;
      const client = new Anthropic({
        authToken: environmentKey
      });
      // Call shutdown.abort() from the host's SIGTERM/SIGINT handler, alongside closing the server,
      // then wait for in-flight handle() calls before exiting: the abort lets a running work item
      // upload changed memory files and remove its store directories first.
      export const shutdown = new AbortController();

      export async function handle(req: Request): Promise<Response> {
        // Never acknowledge a delivery whose work will not run here; a 503 makes the sender retry.
        if (shutdown.signal.aborted) {
          return Response.json({ status: "shutting down" }, { status: 503 });
        }
        const body = await req.text();
        let event;
        try {
          event = client.beta.webhooks.unwrap(body, { headers: Object.fromEntries(req.headers) });
        } catch {
          return new Response("signature verification failed", { status: 401 });
        }
        if (event.data.type !== "session.status_run_started") {
          return Response.json({ status: "ignored" });
        }

        for await (const work of client.beta.environments.work.poller({
          environmentId,
          environmentKey,
          blockMs: null,
          reclaimOlderThanMs: 2000,
          drain: true,
          autoStop: false,
          signal: shutdown.signal
        })) {
          await client.beta.environments.work.worker({ workdir: "/workspace" }).handleItem({
            workId: work.id,
            environmentId,
            sessionId: work.data.id,
            environmentKey,
            // The per-session secret is what lets the worker mount the session's memory stores.
            workSecret: work.secret ?? undefined,
            signal: shutdown.signal
          });
        }
        // The poller and handleItem return quietly on abort, so a drain cut short lands here.
        if (shutdown.signal.aborted) {
          return Response.json({ status: "shutting down" }, { status: 503 });
        }
        return Response.json({ status: "ok" });
      }
      ```

      <CodeGroupItem language="C#">
        The C# SDK does not have `EnvironmentWorker`. To handle work items from your own code, implement your own worker, as [Choose a deployment pattern](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-workers#choose-a-deployment-pattern) describes.
      </CodeGroupItem>

      ```go Go
      package main

      import (
      	"context"
      	"encoding/json"
      	"errors"
      	"io"
      	"log/slog"
      	"net/http"
      	"os"
      	"os/signal"
      	"syscall"

      	"github.com/anthropics/anthropic-sdk-go/v2"
      	"github.com/anthropics/anthropic-sdk-go/v2/lib/environments"
      	"github.com/anthropics/anthropic-sdk-go/v2/option"
      	"github.com/anthropics/anthropic-sdk-go/v2/packages/param"
      )

      var (
      	environmentKey = os.Getenv("ANTHROPIC_ENVIRONMENT_KEY")
      	environmentID  = os.Getenv("ANTHROPIC_ENVIRONMENT_ID")
      	client         = anthropic.NewClient(
      		option.WithAuthToken(environmentKey),
      		option.WithWebhookKey(os.Getenv("ANTHROPIC_WEBHOOK_SIGNING_KEY")),
      	)
      	worker = environments.NewEnvironmentWorker(client, environments.EnvironmentWorkerOptions{
      		Workdir: "/workspace",
      	})
      	// Canceled on SIGINT or SIGTERM (set in main) so an in-flight work item can
      	// upload changed memory files and remove its store directories before exit.
      	shutdown context.Context
      )

      func handle(w http.ResponseWriter, r *http.Request) {
      	body, err := io.ReadAll(r.Body)
      	if err != nil {
      		http.Error(w, "bad request", http.StatusBadRequest)
      		return
      	}
      	event, err := client.Beta.Webhooks.Unwrap(body, r.Header)
      	if err != nil {
      		http.Error(w, "signature verification failed", http.StatusUnauthorized)
      		return
      	}
      	if event.Data.Type != "session.status_run_started" {
      		json.NewEncoder(w).Encode(map[string]string{"status": "ignored"})
      		return
      	}

      	// The Go SDK does not provide a RunOne convenience: drain pending items
      	// with WorkPoller and run each one with HandleItem.
      	// Detach from r.Context(): the session can outlive the webhook delivery timeout.
      	// The process-wide shutdown context still ends the item cleanly on SIGTERM.
      	ctx := shutdown
      	poller := environments.NewWorkPoller(ctx, client, environments.WorkPollerOptions{
      		EnvironmentID:      environmentID,
      		EnvironmentKey:     environmentKey,
      		BlockMs:            param.Null[int64](),
      		ReclaimOlderThanMs: param.NewOpt[int64](2000),
      		Drain:              true,
      		AutoStop:           param.NewOpt(false),
      	})
      	defer poller.Close()
      	for poller.Next() {
      		item := poller.Current()
      		if err := worker.HandleItem(ctx, environments.HandleItemOptions{
      			WorkID:         item.ID,
      			EnvironmentID:  item.EnvironmentID,
      			SessionID:      item.Data.ID,
      			EnvironmentKey: environmentKey,
      			// The per-session secret is what lets the worker mount the session's memory stores.
      			WorkSecret: item.Secret,
      		}); err != nil {
      			slog.Error("handle work item", "work_id", item.ID, "err", err)
      			http.Error(w, "internal error", http.StatusInternalServerError)
      			return
      		}
      	}
      	if err := poller.Err(); err != nil {
      		slog.Error("poll work queue", "err", err)
      		http.Error(w, "internal error", http.StatusInternalServerError)
      		return
      	}
      	json.NewEncoder(w).Encode(map[string]string{"status": "ok"})
      }

      func main() {
      	ctx, stop := signal.NotifyContext(context.Background(), os.Interrupt, syscall.SIGTERM)
      	defer stop()
      	shutdown = ctx

      	server := &http.Server{Addr: ":8080"}
      	http.HandleFunc("POST /webhook", handle)
      	go func() {
      		if err := server.ListenAndServe(); err != nil && !errors.Is(err, http.ErrServerClosed) {
      			slog.Error("http server", "err", err)
      			os.Exit(1)
      		}
      	}()
      	// On a signal, stop accepting deliveries and return only after in-flight
      	// handlers, and therefore their work items' memory teardown, have finished.
      	<-ctx.Done()
      	if err := server.Shutdown(context.Background()); err != nil {
      		slog.Error("http shutdown", "err", err)
      	}
      }
      ```

      <CodeGroupItem language="Java">
        The Java SDK does not have `EnvironmentWorker`. To handle work items from your own code, implement your own worker, as [Choose a deployment pattern](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-workers#choose-a-deployment-pattern) describes.
      </CodeGroupItem>

      <CodeGroupItem language="PHP">
        The PHP SDK does not have `EnvironmentWorker`. To handle work items from your own code, implement your own worker, as [Choose a deployment pattern](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-workers#choose-a-deployment-pattern) describes.
      </CodeGroupItem>

      <CodeGroupItem language="Ruby">
        The Ruby SDK does not have `EnvironmentWorker`. To handle work items from your own code, implement your own worker, as [Choose a deployment pattern](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-workers#choose-a-deployment-pattern) describes.
      </CodeGroupItem>
    </CodeGroup>

    In the Python, TypeScript, and Go SDKs, `handle_item()` (typescript: `handleItem()`; go: `HandleItem()`) needs the work item’s secret to mount memory stores. A worker that polls with `run()` (go: `Run()`) already has the secret. This handler claims each item itself, so it passes the secret in the `work_secret` (typescript: `workSecret`; go: `WorkSecret`) argument. See [Forward the work item’s secret](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-per-session#forward-the-work-items-secret).
  </Step>
</Steps>

This handler runs every claimed item in one process, and it runs items from separate webhook deliveries at the same time. Those sessions share one filesystem, including `/workspace` and `/mnt/memory`. If your sessions attach the same memory store, see [Isolate sessions that share a store](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-memory#isolate-sessions-that-share-a-store).

## Next steps

<CardGroup cols={2}>
  <Card title="Run one sandbox per session" icon="cube" href="https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-per-session">
    Launch sandboxes with the Helm chart on Kubernetes, a spawn script, or the SDK poller.
  </Card>

  <Card title="Monitor and troubleshoot self-hosted workers" icon="lightning" href="https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-operations">
    Read queue depth, stop sessions and workers cleanly, and fix common failures.
  </Card>

  <Card title="Security model" icon="lock" href="https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-security">
    Shared responsibility model for self-hosted sandbox environments.
  </Card>
</CardGroup>

## Availability

Prebuilt self-hosted workers are in beta on every model.

### API support

#### [Managed Agents](https://platform.claude.com/docs/en/managed-agents/overview)

* Availability: Available

| Status | Cloud platforms                                                                                                    |
| ------ | ------------------------------------------------------------------------------------------------------------------ |
| Beta   | Claude API, [Claude Platform on AWS](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws) |

### Required beta headers

[Beta headers overview](https://platform.claude.com/docs/en/api/beta-headers)

Beta headers allow you to access experimental features and new model capabilities before they become part of the standard API.

* `managed-agents-2026-04-01`

### Data handling

[Data handling overview](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention#feature-eligibility)

| Item    | Zero data retention                                                                                                                                                                                                                                         | HIPAA                                                               |
| ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| Status  | Not eligible                                                                                                                                                                                                                                                | Not eligible                                                        |
| Details | Not eligible for ZDR, except for self-hosted Managed Agents. Sessions are stateful resources; transcripts persist until you delete them. [Learn more](https://platform.claude.com/docs/en/managed-agents/self-hosted-data-and-access#how-long-data-is-kept) | Not eligible for HIPAA. Applies to all Managed Agents sub-features. |

Applicable endpoints:

* `/v1/agents`
* `/v1/sessions`
* `/v1/environments`
