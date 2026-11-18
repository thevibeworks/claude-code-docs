---
title: Memory stores in self-hosted sandboxes
url: https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-memory
description: "Attach memory stores to Claude Managed Agents sessions that run in self-hosted sandboxes: prepare the host, configure sync, and handle read-only stores and conflicts."
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
---

Sessions on a self-hosted environment attach [memory stores](https://platform.claude.com/docs/en/managed-agents/memory) exactly as sessions on cloud environments do. List them in `resources` (csharp, go: `Resources`) when you create the session, as shown in [Attach a memory store to a session](https://platform.claude.com/docs/en/managed-agents/memory#attach-a-memory-store-to-a-session). A session accepts up to 8 memory stores.

The difference is who materializes the store. On a self-hosted environment your worker, rather than Anthropic’s infrastructure, downloads each store into the sandbox and syncs the agent’s changes back.

## Requirements

* **A worker that mounts memory stores:** Use `ant` CLI 1.33.0 or later, or `EnvironmentWorker` from the Python, TypeScript, or Go SDK.
* **A POSIX filesystem:** Windows hosts are not supported, because the worker requires `O_NOFOLLOW` when it opens memory files. Anthropic recommends a case-sensitive filesystem, so that memory paths that differ only in case do not collide. macOS volumes are case-insensitive by default, so such paths collide there.
* **A writable `/mnt/memory` directory:** See [Prepare the host](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-memory#prepare-the-host). On macOS, see [Prepare a macOS host](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-memory#prepare-a-macos-host).
* **The work item’s secret:** If your own code launches the worker, [forward the work item’s secret](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-per-session#forward-the-work-items-secret) to it.

## Prepare the host

On macOS, skip the next command and follow [Prepare a macOS host](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-memory#prepare-a-macos-host) instead.

Before you start the worker, create the parent directory and make it writable by the user the worker runs as:

```bash
sudo mkdir -p /mnt/memory && sudo chown "$USER" /mnt/memory
```

Don’t create any store’s directory yourself. The worker creates each store’s `mount_path` (java, php: `mountPath`; csharp, go: `MountPath`) directory, such as `/mnt/memory/user-preferences`, when it claims a session and removes it when it finishes with that session. If anything already exists at that path, even an empty directory, the worker fails the work item.

In the [sandbox-per-session pattern](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-per-session), the sandbox image needs a writable `/mnt/memory`. You don’t need to bind-mount the memory directories to the host, because the store holds the lasting copy of every memory.

### Prepare a macOS host

On macOS, the root volume is read-only, so `mkdir` can’t create `/mnt`. Instead, create `/System/Volumes/Data/mnt/memory` on the data volume, which is writable. Then add a line to `/etc/synthetic.conf`, so that macOS creates `/mnt` as a symbolic link to `/System/Volumes/Data/mnt`. These steps need administrator rights.

Without this setup, the worker can’t create a store’s directory, so it fails the work item. The session then stays idle with no error event. See [Memory stores fail to mount or sync](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-operations#memory-stores-fail-to-mount).

<Steps>
  <Step title="Create the directory on the data volume">
    Create the `memory` directory and make the worker’s user its owner. `$USER` is your own username. If the worker runs as another user, replace `"$USER"` with that user’s name.

    ```bash
    sudo mkdir -p /System/Volumes/Data/mnt/memory && sudo chown "$USER" /System/Volumes/Data/mnt/memory
    ```

    This location is only one option. If you use another, change the path in the `synthetic.conf` line to match. Anthropic has tested only `/System/Volumes/Data/mnt`.
  </Step>

  <Step title="Add a line to synthetic.conf">
    Run `cat -et /etc/synthetic.conf`, which shows each tab as `^I` and each line end as `$`.

    * If a line reads `mnt^ISystem/Volumes/Data/mnt$`, this step is already done. Go to the next step.
    * If another line starts with `mnt`, stop. Something else on this Mac already defines `/mnt`.
    * If the last line doesn’t end with `$`, run `echo | sudo tee -a /etc/synthetic.conf` to end it. Then, add the line.
    * If it prints nothing or reports `No such file or directory`, add the line. The following command creates the file if it’s missing.
    * Otherwise, add the line.

    To add the line, run this command. Run it only once, because each run appends another line.

    ```bash
    printf 'mnt\tSystem/Volumes/Data/mnt\n' | sudo tee -a /etc/synthetic.conf
    ```

    The command prints the line that it adds. The line maps the name `mnt` to the directory that holds `memory`. The file needs a tab between the two columns, which `\t` writes.
  </Step>

  <Step title="Create the link">
    Run `apfs.util` with the `-t` option. It creates the link from the line you added, without a restart.

    ```bash
    sudo /System/Library/Filesystems/apfs.fs/Contents/Resources/apfs.util -t
    ```
  </Step>

  <Step title="Check the result">
    List `/mnt` and `/mnt/memory`.

    ```bash
    ls -ld /mnt /mnt/memory
    ```

    The first line ends with `/mnt -> System/Volumes/Data/mnt`. The second line shows the worker’s user as the owner of `/mnt/memory`. You can now start the worker.
  </Step>
</Steps>

Anthropic has tested this setup on macOS 26.7.1 with the `ant` CLI worker.

### Isolate sessions that share a store

Two sessions cannot mount the same store on one filesystem at the same time because both need the same path. To run sessions that share a store side by side, give each session its own filesystem. If you use a sandbox for each session, each session gets its own filesystem automatically. See [Run one sandbox per session](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-per-session). One host can run many such sandboxes.

## How the worker handles memory

When the worker claims a work item whose session has memory stores attached, it:

1. **Downloads each store to its `mount_path` (java, php: `mountPath`; csharp, go: `MountPath`).** This is the same directory under `/mnt/memory/` that cloud sessions use, and the session’s system prompt describes it to the agent. For example, a store named “User Preferences” lands at `/mnt/memory/user-preferences/`.
2. **Opens those directories to the file tools.** The agent works on memories with the same file tools it uses in the working directory.
3. **Syncs after tool calls.** The worker syncs after a tool call if the [sync interval](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-memory#sync-interval) (15 seconds by default) has passed since its last sync. Each sync writes changed memories from the store to disk and uploads files that the agent changed.
4. **Runs a final sync when the session ends or stays idle for the worker’s idle limit.** The final sync can take up to 60 seconds. Changes not uploaded by then are lost. The worker then removes the directories it created.

The idle limit is 60 seconds by default. [When the worker finishes with a session](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-reference#when-the-worker-finishes-with-a-session) says what the limit covers and how to change it.

The agent’s `write` and `edit` tools change only the local copy, and the worker uploads those changes at its next sync. Paths under `/mnt/memory/` outside the store directories are not scratch space. The worker’s file tools refuse to write to them, and anything that a shell command writes there is never synced to a store.

[Memory versions](https://platform.claude.com/docs/en/managed-agents/memory#audit-memory-changes), redaction, and viewing or editing memories in the Claude Console work as they do for cloud sessions. The agent’s memory reads and writes appear in the [event stream](https://platform.claude.com/docs/en/managed-agents/events-and-streaming) as ordinary tool events.

Each store directory contains a marker file named `.anthropic-memory-store` that ties the directory to its store. Leave it in place. If the marker is missing or altered and the directory still holds files, the worker doesn’t sync the directory. It also doesn’t remove the directory when it finishes with the session.

<Warning>
  If you stop a worker gracefully during a session or [stop the session’s work item](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-operations#stop-a-session-gracefully), the worker still uploads new and changed files. It also removes the store directories. It sends no deletions, so a memory that the agent deleted stays in the store unless an earlier sync already deleted it from the store. A worker that is killed rather than stopped runs no teardown, so unsynced edits are lost and the store directories stay behind. See [Stop workers gracefully](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-operations#stop-workers-gracefully).
</Warning>

## Configure sync

Two `EnvironmentWorker` options control memory behavior. Set them wherever you construct the worker, including in a webhook handler. The `ant` CLI worker always uses the defaults.

### Sync interval

`memory_sync_interval` (typescript: `memorySyncIntervalMs`; go: `MemorySyncInterval`) sets the shortest time between two syncs while the session runs.

| Setting                | Value                                               |
| ---------------------- | --------------------------------------------------- |
| Default                | 15 seconds                                          |
| Minimum                | 5 seconds                                           |
| Example (10 seconds)   | `10` (typescript: `10_000`; go: `10 * time.Second`) |
| Disable memory support | `None` (typescript: `null`; go: `-1`)               |

The worker doesn’t sync on a timer. It checks the interval after each call to a tool that runs in your sandbox, such as `bash`, `read`, or a custom tool. The call doesn’t have to touch memory. Without tool calls, nothing syncs until the [final sync](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-memory#how-the-worker-handles-memory). A change in one session reaches another running session only after both have synced, so the wait has no fixed length.

A shorter interval narrows the window in which another session sees stale memories, at the cost of more memory store requests.

Disable memory support only on workers whose sessions attach no memory stores. A disabled worker neither downloads nor syncs stores, so a session with stores attached runs without them even though its system prompt still describes them.

While memory support is enabled, a work item that arrives without a `secret` (csharp, go: `Secret`) for a session with attached stores fails rather than running without memory. See [Memory stores fail to mount or sync](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-operations#memory-stores-fail-to-mount).

### Deletions

`memory_sync_deletions` (typescript: `memorySyncDeletions`; go: `MemorySyncDeletions`) sets whether a file the agent deletes locally is also deleted from the store. Uploads and downloads are unaffected.

| Value                                                                 | Behavior                                                                                                                                         |
| --------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| `"enabled"` (go: `environments.MemorySyncDeletionsEnabled`) (default) | Deletes the memory from the store once a later sync confirms the file is still gone.                                                             |
| `"log_only"` (go: `environments.MemorySyncDeletionsLogOnly`)          | Runs the same checks but only logs what it would have deleted. Use it to watch what your workers would delete before you trust the enabled mode. |
| `"disabled"` (go: `environments.MemorySyncDeletionsDisabled`)         | Never deletes from the store.                                                                                                                    |

For example, to sync at most once every 10 seconds and only log the deletions the worker would have made, use the following sample. The sample uses `/workspace` as the working directory, which must exist before the worker starts. [Run an always-on worker](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-workers#run-an-always-on-worker) says how to create the directory and what to use on macOS.

<CodeGroup exclude="shell, csharp, java, php, ruby">
  <CodeGroupItem language="cURL">
    A worker is a long-running process, not a single HTTP request. To change the sync settings, use `EnvironmentWorker` in the Python, TypeScript, or Go SDK.
  </CodeGroupItem>

  <CodeGroupItem language="CLI">
    The `ant` CLI worker always uses the default sync settings. To change them, use `EnvironmentWorker` in the Python, TypeScript, or Go SDK.
  </CodeGroupItem>

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
              memory_sync_interval=10,  # seconds
              memory_sync_deletions="log_only",
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

  const environmentKey = process.env.ANTHROPIC_ENVIRONMENT_KEY!;
  const environmentId = process.env.ANTHROPIC_ENVIRONMENT_ID!;
  const client = new Anthropic({ authToken: environmentKey });
  const controller = new AbortController();
  process.once("SIGINT", () => controller.abort());
  process.once("SIGTERM", () => controller.abort());

  const worker = new EnvironmentWorker({
    client,
    environmentId,
    environmentKey,
    workdir: "/workspace",
    signal: controller.signal,
    memorySyncIntervalMs: 10_000,
    memorySyncDeletions: "log_only"
  });
  await worker.run();
  ```

  <CodeGroupItem language="C#">
    The C# SDK does not have `EnvironmentWorker`.
  </CodeGroupItem>

  ```go Go
  package main

  import (
  	"context"
  	"log"
  	"os"
  	"os/signal"
  	"syscall"
  	"time"

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
  		EnvironmentID:       environmentID,
  		EnvironmentKey:      environmentKey,
  		Workdir:             "/workspace",
  		MemorySyncInterval:  10 * time.Second,
  		MemorySyncDeletions: environments.MemorySyncDeletionsLogOnly,
  	})
  	if err := worker.Run(ctx); err != nil {
  		log.Fatalf("worker: %v", err)
  	}
  }
  ```

  <CodeGroupItem language="Java">
    The Java SDK does not have `EnvironmentWorker`.
  </CodeGroupItem>

  <CodeGroupItem language="PHP">
    The PHP SDK does not have `EnvironmentWorker`.
  </CodeGroupItem>

  <CodeGroupItem language="Ruby">
    The Ruby SDK does not have `EnvironmentWorker`.
  </CodeGroupItem>
</CodeGroup>

## Read-only stores and conflicts

### Read-only stores

For a store attached with `access: "read_only"`, the `write` and `edit` tools refuse to change files inside its directory. The worker never uploads anything from it.

Changes made through `bash` or through a custom tool or MCP server you serve from the sandbox are not blocked locally. They never reach the store. A changed file stays changed until one of these things happens:

* **That memory gets a new version in the store.** The worker’s next sync overwrites the file with that version.
* **The worker finishes with the session.** It removes the directory.

To keep the local copy unchanged too, disable the `bash` tool for that agent. Also, give it no custom tools or MCP servers that write to the sandbox’s filesystem. Don’t mount a read-only volume at the store’s path. The mount puts a directory at that path, and the worker fails the work item if anything already exists there.

### Conflicts

A conflict is a memory that changed both in the store and in the sandbox since the previous sync. A deletion counts as a change. For a store attached with `access: "read_write"`, the worker resolves the conflict at the next sync:

| In the store | In the sandbox | Result                                                     |
| ------------ | -------------- | ---------------------------------------------------------- |
| Changed      | Changed        | The store’s version overwrites the file.                   |
| Changed      | Deleted        | The worker writes the store’s version back to the sandbox. |
| Deleted      | Changed        | The worker creates the memory again from the file.         |

In the first two rows, the agent’s change or deletion is lost, even though the tool call succeeded. Nothing tells the agent, and the only sign of the loss is a warning in the worker’s log. In the last row, the deletion in the store is undone.

## Troubleshooting

See [Memory stores fail to mount or sync](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-operations#memory-stores-fail-to-mount) for the worker’s log messages and their fixes.

## Availability

Memory stores in self-hosted sandboxes are in beta on every model.

### API support

#### [Managed Agents](https://platform.claude.com/docs/en/managed-agents/overview)

* Availability: Available

| Status | Cloud platforms |
| ------ | --------------- |
| Beta   | Claude API      |

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
