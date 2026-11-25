---
title: Run one sandbox per session
url: https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-per-session
description: Give each session its own self-hosted sandbox with the Helm chart on Kubernetes, a spawn script, or the SDK poller.
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

In the sandbox-per-session pattern, each session runs in a fresh sandbox, which can have its own filesystem, resource limits, and network controls. To compare it with the other patterns, see [Choose a deployment pattern](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-workers#choose-a-deployment-pattern).

You can set it up in three ways:

* **[Helm chart on Kubernetes](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-per-session#run-sandboxes-on-kubernetes):** Anthropic’s dispatcher claims work and starts a pod for each session on your cluster.
* **[Spawn script](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-per-session#launch-sandboxes-with-a-spawn-script):** The `ant` CLI claims work and calls your script, which launches a sandbox on any platform.
* **[SDK poller](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-per-session#launch-sandboxes-from-the-sdk-poller):** Your own code claims work and launches the sandbox.

The sections after [Run sandboxes on Kubernetes](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-per-session#run-sandboxes-on-kubernetes) apply to the spawn script and the SDK poller.

## Run sandboxes on Kubernetes

Anthropic publishes a Helm chart, `cma-sandboxes`, and its images. The chart runs one sandbox per session on your own Kubernetes cluster. Its dispatcher polls the environment’s work queue and gives each session a pod of its own:

* **Isolation:** Each pod runs under [gVisor](https://gvisor.dev/) behind the chart’s network policies. It has its own filesystem and resource limits. Only the dispatcher holds the environment key.
* **Session affinity:** Every message in a session goes to that session’s sandbox. After the session is idle for 30 minutes (the default of the chart’s `sandbox.idleTimeout` setting), its pod stops. Its `/workspace` volume stays until the session ends. The next message starts a pod on the same volume.
* **Warm pool:** Except on Google Kubernetes Engine (GKE), the chart keeps two pods ready for new sessions (the default of the chart’s `sandbox.warmPoolSize` setting).

Sandbox pods run the `ant` CLI worker. They support [memory stores](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-memory) with the default sync settings, and they don’t support [custom tools](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-custom-tools).

### Install the chart

The chart runs on GKE, Amazon EKS, and other clusters. Set up the following before you install it:

* **In the cluster:** The [Agent Sandbox](https://github.com/kubernetes-sigs/agent-sandbox) controller (on GKE, the Agent Sandbox add-on), nodes that run gVisor, and a network plugin that enforces NetworkPolicy.
* **In your own namespace:** Restricted Pod Security Standard labels, a Secret with the environment ID and [environment key](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes#run-your-first-session), and the dispatcher’s TLS certificate.

The [install guide on GitHub](https://github.com/anthropics/anthropic-cli/blob/main/sandboxes/kubernetes/README.md) has the setup steps for each kind of cluster. It also covers upgrades and key rotation.

Save your settings as `cma-values.yaml`. The install fails without the three settings in this file:

<File filename="cma-values.yaml">
  ```yaml
  platform: gke             # or eks, or generic for any other cluster
  egress:
    # The chart already blocks the private ranges. List your other addresses
    # that sandboxes must not reach.
    clusterCIDRs:
      - 203.0.113.10/32     # your cluster's Kubernetes API endpoint
    cmaServer:
      public: true          # the Claude API has a public address
  ```
</File>

The install guide lists the settings that depend on your cluster, such as `gke.dns` on GKE Autopilot. It also says when `egress.clusterIsPrivate: true` takes the place of `egress.clusterCIDRs`.

Then, install the chart:

```bash
helm install cma \
  oci://us-docker.pkg.dev/anthropic-public-registry/sandboxes/charts/cma-sandboxes \
  --version 0.1.0 \
  --namespace cma \
  -f cma-values.yaml \
  --wait
```

After the install, run the preflight check that the install guide describes.

<Warning>
  Don’t remove the chart with `helm uninstall` alone. That command deletes the network policies and leaves the sessions’ sandboxes running without them. Stop the dispatcher and delete the sandboxes first, in the order that the [Removal section of the install guide](https://github.com/anthropics/anthropic-cli/blob/main/sandboxes/kubernetes/README.md#removal) gives.
</Warning>

### Add tools to the sandbox image

The published sandbox image is Alpine Linux with `bash`, `curl`, `jq`, and the `ant` CLI. The chart runs it with a read-only root filesystem and as a non-root user, so an agent can’t install packages during a session.

To give your agents more tools, such as Python or Git, build both images from the repository at the release’s tag. The [Install section of the install guide](https://github.com/anthropics/anthropic-cli/blob/main/sandboxes/kubernetes/README.md#install) has the commands. Push the images to your registry as `cma-dispatcher` and `cma-sandbox`, with the chart’s version as the tag. Then, set `image.registry` to that registry. If you pin image digests, use the digests of your own images.

### Restrict network egress

By default, the chart’s network policies let a sandbox reach the public IPv4 internet. They block private address ranges, the cloud metadata server, and the addresses in `egress.clusterCIDRs`. A prompt-injected agent can send what it reads to any address that its sandbox can reach. [Network egress](https://github.com/anthropics/anthropic-cli/blob/main/sandboxes/kubernetes/README.md#network-egress) in the install guide has the details.

* **GKE with Dataplane V2:** Set `egress.mode: fqdnGke` to limit connections to port 443 on the hosts in `egress.fqdnGke.hosts`. Keep `api.anthropic.com` in that list, and add every host that your agents’ commands need. Unlike the default, this mode has no list of blocked ranges. It allows whatever address a listed host’s name resolves to, so list only hosts whose DNS you trust. A sandbox can still send data out inside DNS lookups.
* **Other clusters and GKE without Dataplane V2:** The default is the only mode.
* **Every cluster:** Network policies don’t cover the ports that the cluster’s own nodes listen on. See [Node isolation you own](https://github.com/anthropics/anthropic-cli/blob/main/sandboxes/kubernetes/README.md#node-isolation-you-own) in the install guide.

## Launch sandboxes with a spawn script

A poller on the host claims work and calls your script once for each work item. The script launches a sandbox for that one session.

<Steps>
  <Step title="Build the sandbox image">
    Install `ant` and set `ant beta:worker run` as the entrypoint. When a sandbox starts, it reads session details from environment variables, handles that session, and exits. The base image must provide `/bin/bash`; the build uses `curl` only to download `ant`.

    <File filename="Dockerfile">
      ```dockerfile
      FROM your-base-image
      ARG ANT_VERSION=2.14.0
      ARG TARGETARCH
      RUN ARCH=$([ "$TARGETARCH" = "arm64" ] && echo arm64 || echo amd64) && \
          curl -fsSL "https://github.com/anthropics/anthropic-cli/releases/download/v${ANT_VERSION}/ant_${ANT_VERSION}_linux_${ARCH}.tar.gz" \
            | tar -xz -C /usr/local/bin ant
      WORKDIR /workspace
      VOLUME /workspace
      ENTRYPOINT ["ant", "beta:worker", "run"]
      ```
    </File>
  </Step>

  <Step title="Write the spawn script">
    The script forwards the session details into a fresh sandbox. It requires `jq` on the poller host.

    <File filename="spawn.sh">
      ```bash
      #!/bin/bash
      # spawn.sh: called once for each claimed work item
      # The claimed work item arrives as JSON on stdin.
      ANTHROPIC_WORK_SECRET="$(jq -r '.secret // empty')"
      export ANTHROPIC_WORK_SECRET
      mkdir -p "/host/outputs/$ANTHROPIC_SESSION_ID"
      exec docker run --rm \
        -e ANTHROPIC_SESSION_ID -e ANTHROPIC_ENVIRONMENT_KEY \
        -e ANTHROPIC_WORK_ID -e ANTHROPIC_ENVIRONMENT_ID -e ANTHROPIC_BASE_URL \
        -e ANTHROPIC_WORK_SECRET \
        -v "/host/outputs/$ANTHROPIC_SESSION_ID":/workspace \
        your-image
      ```
    </File>

    The poller sets `ANTHROPIC_WORK_ID`, `ANTHROPIC_ENVIRONMENT_ID`, `ANTHROPIC_SESSION_ID`, and `ANTHROPIC_ENVIRONMENT_KEY`. `ANTHROPIC_BASE_URL` reaches the script only if you set it on the poller’s host. The script reads `ANTHROPIC_WORK_SECRET` from the work item’s JSON on standard input. See [Environment variables](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-reference#environment-variables).

    `/host/outputs` is a host directory you choose. Mounting it at `/workspace` lets you retrieve the session’s deliverables after the sandbox exits. The mount also picks up the downloaded `skills/` tree and any intermediate files.
  </Step>

  <Step title="Start the poller">
    ```bash
    ant beta:worker poll --on-work ./spawn.sh
    ```
  </Step>
</Steps>

## Forward the work item’s secret

Each claimed work item can carry a `secret` (csharp, go: `Secret`) that Anthropic issues for that session. The worker that runs the session needs it to mount [memory stores](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-memory).

A worker that claims and runs sessions in one process passes the secret along itself. `EnvironmentWorker` with `run()` (go: `Run()`) is one such worker, and `ant beta:worker poll` without `--on-work` is another. When your own code sits between the claim and the worker, you forward the secret:

| You claim work with | The secret arrives as | Pass it to the worker as |
| ----- | ----- | ----- |
| `ant beta:worker poll --on-work` | The `secret` field of the work item JSON on your script’s standard input | `ANTHROPIC_WORK_SECRET` in the sandbox’s environment |
| The Python, TypeScript, or Go SDK’s `work.poller()` (typescript: `new WorkPoller()`; go: `environments.NewWorkPoller()`) | The `secret` (go: `Secret`) field of each claimed work item | `ANTHROPIC_WORK_SECRET` in the sandbox’s environment or the `work_secret` (typescript: `workSecret`; go: `WorkSecret`) argument to `handle_item()` (typescript: `handleItem()`; go: `HandleItem()`) |

Pass the secret only into the sandbox that serves that session, and never log it. See [Security model](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-security) for how it relates to the environment key.

## Launch sandboxes from the SDK poller

To claim work from your own code instead of `ant beta:worker poll --on-work`, use the poller in the Python, TypeScript, or Go SDK: `work.poller()` (typescript: `new WorkPoller()`; go: `environments.NewWorkPoller()`). It polls the queue and gives you each claimed session, and you launch the sandbox:

<CodeGroup exclude="shell, csharp, java, php, ruby">
  <CodeGroupItem language="cURL">
    Claiming work in a loop and launching a sandbox for each session needs more logic than a single shell command. From the shell, run `ant beta:worker poll --on-work` with a spawn script, as in [Launch sandboxes with a spawn script](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-per-session#launch-sandboxes-with-a-spawn-script).
  </CodeGroupItem>

  <CodeGroupItem language="CLI">
    To claim work from the shell and launch a sandbox for each session, run `ant beta:worker poll --on-work` with a spawn script. See [Launch sandboxes with a spawn script](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-per-session#launch-sandboxes-with-a-spawn-script).
  </CodeGroupItem>

  ```python Python
  import asyncio
  import os

  from anthropic import AsyncAnthropic
  from anthropic.types.beta.environments import BetaSelfHostedWork

  SANDBOX_ENV = (
      "ANTHROPIC_ENVIRONMENT_ID",
      "ANTHROPIC_ENVIRONMENT_KEY",
      "ANTHROPIC_WORK_ID",
      "ANTHROPIC_SESSION_ID",
      "ANTHROPIC_WORK_SECRET",
      "ANTHROPIC_BASE_URL",  # forwarded only when set on this host
  )


  async def launch_container(work: BetaSelfHostedWork) -> None:
      print(f"claimed session {work.data.id}")
      # Replace `docker run` with your own sandbox launcher. Forward the environment
      # key (never your API key) and the work item's per-session secret: the worker
      # inside needs the secret to mount the session's memory stores.
      env = os.environ | {
          "ANTHROPIC_WORK_ID": work.id,
          "ANTHROPIC_SESSION_ID": work.data.id,
          "ANTHROPIC_WORK_SECRET": work.secret or "",
      }
      forward = [arg for name in SANDBOX_ENV for arg in ("-e", name)]
      launcher = await asyncio.create_subprocess_exec(
          "docker", "run", "--rm", "--detach", *forward, "your-image", env=env
      )
      await launcher.wait()


  async def main() -> None:
      environment_key = os.environ["ANTHROPIC_ENVIRONMENT_KEY"]
      environment_id = os.environ["ANTHROPIC_ENVIRONMENT_ID"]
      async with AsyncAnthropic(auth_token=environment_key) as client:
          async for work in client.beta.environments.work.poller(
              environment_id=environment_id,
              environment_key=environment_key,
              auto_stop=False,  # the launched sandbox owns the stop call
          ):
              await launch_container(work)


  asyncio.run(main())
  ```

  ```typescript TypeScript
  import { spawn } from "node:child_process";
  import { once } from "node:events";
  import Anthropic from "@anthropic-ai/sdk";
  import { WorkPoller } from "@anthropic-ai/sdk/helpers/beta/environments";
  import type { BetaSelfHostedWork } from "@anthropic-ai/sdk/resources/beta/environments";

  const SANDBOX_ENV = [
    "ANTHROPIC_ENVIRONMENT_ID",
    "ANTHROPIC_ENVIRONMENT_KEY",
    "ANTHROPIC_WORK_ID",
    "ANTHROPIC_SESSION_ID",
    "ANTHROPIC_WORK_SECRET",
    "ANTHROPIC_BASE_URL" // forwarded only when set on this host
  ];

  const environmentKey = process.env.ANTHROPIC_ENVIRONMENT_KEY!;
  const environmentId = process.env.ANTHROPIC_ENVIRONMENT_ID!;
  const client = new Anthropic({ authToken: environmentKey });

  async function launchContainer(work: BetaSelfHostedWork): Promise<void> {
    console.log(`claimed session ${work.data.id}`);
    // Replace `docker run` with your own sandbox launcher. Forward the environment
    // key (never your API key) and the work item's per-session secret: the worker
    // inside needs the secret to mount the session's memory stores.
    const env = {
      ...process.env,
      ANTHROPIC_WORK_ID: work.id,
      ANTHROPIC_SESSION_ID: work.data.id,
      ANTHROPIC_WORK_SECRET: work.secret ?? ""
    };
    const forward = SANDBOX_ENV.flatMap((name) => ["-e", name]);
    const launcher = spawn("docker", ["run", "--rm", "--detach", ...forward, "your-image"], {
      env,
      stdio: "inherit"
    });
    await once(launcher, "close");
  }

  const poller = new WorkPoller({
    client,
    environmentId,
    environmentKey,
    autoStop: false // the launched sandbox owns the stop call
  });

  for await (const work of poller) {
    await launchContainer(work);
  }
  ```

  <CodeGroupItem language="C#">
    The C# SDK does not have a helper that polls for work. To claim work from your own code, call the [Environments Work endpoints](https://platform.claude.com/docs/en/api/beta/environments/work) to poll for an item and acknowledge it.
  </CodeGroupItem>

  ```go Go
  package main

  import (
  	"context"
  	"fmt"
  	"log"
  	"os"
  	"os/exec"

  	"github.com/anthropics/anthropic-sdk-go/v2"
  	"github.com/anthropics/anthropic-sdk-go/v2/lib/environments"
  	"github.com/anthropics/anthropic-sdk-go/v2/option"
  	"github.com/anthropics/anthropic-sdk-go/v2/packages/param"
  )

  var sandboxEnv = []string{
  	"ANTHROPIC_ENVIRONMENT_ID",
  	"ANTHROPIC_ENVIRONMENT_KEY",
  	"ANTHROPIC_WORK_ID",
  	"ANTHROPIC_SESSION_ID",
  	"ANTHROPIC_WORK_SECRET",
  	"ANTHROPIC_BASE_URL", // forwarded only when set on this host
  }

  func launchContainer(ctx context.Context, work *anthropic.BetaSelfHostedWork) error {
  	fmt.Printf("claimed session %s\n", work.Data.ID)
  	// Replace `docker run` with your own sandbox launcher. Forward the environment
  	// key (never your API key) and the work item's per-session secret: the worker
  	// inside needs the secret to mount the session's memory stores.
  	args := []string{"run", "--rm", "--detach"}
  	for _, name := range sandboxEnv {
  		args = append(args, "-e", name)
  	}
  	launcher := exec.CommandContext(ctx, "docker", append(args, "your-image")...)
  	launcher.Env = append(os.Environ(),
  		"ANTHROPIC_WORK_ID="+work.ID,
  		"ANTHROPIC_SESSION_ID="+work.Data.ID,
  		"ANTHROPIC_WORK_SECRET="+work.Secret,
  	)
  	launcher.Stdout, launcher.Stderr = os.Stdout, os.Stderr
  	return launcher.Run()
  }

  func main() {
  	environmentID := os.Getenv("ANTHROPIC_ENVIRONMENT_ID")
  	environmentKey := os.Getenv("ANTHROPIC_ENVIRONMENT_KEY")

  	client := anthropic.NewClient(option.WithAuthToken(environmentKey))

  	ctx := context.Background()

  	poller := environments.NewWorkPoller(ctx, client, environments.WorkPollerOptions{
  		EnvironmentID:  environmentID,
  		EnvironmentKey: environmentKey,
  		AutoStop:       param.NewOpt(false), // the launched sandbox owns the stop call
  	})
  	defer poller.Close()

  	for work, err := range poller.All() {
  		if err != nil {
  			log.Fatal(err)
  		}
  		if err := launchContainer(ctx, work); err != nil {
  			log.Fatal(err)
  		}
  	}
  }
  ```

  <CodeGroupItem language="Java">
    The Java SDK does not have a helper that polls for work. To claim work from your own code, call the [Environments Work endpoints](https://platform.claude.com/docs/en/api/beta/environments/work) to poll for an item and acknowledge it.
  </CodeGroupItem>

  <CodeGroupItem language="PHP">
    The PHP SDK does not have a helper that polls for work. To claim work from your own code, call the [Environments Work endpoints](https://platform.claude.com/docs/en/api/beta/environments/work) to poll for an item and acknowledge it.
  </CodeGroupItem>

  <CodeGroupItem language="Ruby">
    The Ruby SDK does not have a helper that polls for work. To claim work from your own code, call the [Environments Work endpoints](https://platform.claude.com/docs/en/api/beta/environments/work) to poll for an item and acknowledge it.
  </CodeGroupItem>
</CodeGroup>

## Run the SDK worker inside the sandbox

Replace the `ant beta:worker run` entrypoint with an SDK entrypoint when the sandbox must [serve custom tools](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-custom-tools) or use [non-default memory sync settings](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-memory#configure-sync). The entrypoint constructs `EnvironmentWorker` and calls `handle_item()` (typescript: `handleItem()`; go: `HandleItem()`), which reads the same `ANTHROPIC_*` variables that the spawn script forwards.

<CodeGroup exclude="shell, csharp, java, php, ruby">
  <CodeGroupItem language="cURL">
    A worker is a long-running process, not a single HTTP request. To serve custom tools or change the memory sync settings, use `EnvironmentWorker` in the Python, TypeScript, or Go SDK.
  </CodeGroupItem>

  <CodeGroupItem language="CLI">
    The `ant` CLI worker (`ant beta:worker run`) can’t serve custom tools or change the memory sync settings. To do either, use `EnvironmentWorker` in the Python, TypeScript, or Go SDK.
  </CodeGroupItem>

  ```python Python
  import asyncio
  import contextlib
  import os
  import signal
  from anthropic import AsyncAnthropic
  from anthropic.lib.environments import EnvironmentWorker


  async def main() -> None:
      async with AsyncAnthropic(
          auth_token=os.environ["ANTHROPIC_ENVIRONMENT_KEY"]
      ) as client:
          worker = EnvironmentWorker(client, workdir="/workspace")
          # With no arguments, handle_item() reads the ANTHROPIC_* variables the spawn
          # script forwarded, including ANTHROPIC_WORK_SECRET.
          task = asyncio.create_task(worker.handle_item())
          # Canceling the task when the container is stopped lets the worker upload
          # changed memory files and remove the store directories before it exits.
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

  const client = new Anthropic({ authToken: process.env.ANTHROPIC_ENVIRONMENT_KEY });
  const controller = new AbortController();
  // Aborting when the container is stopped lets the worker upload changed memory
  // files and remove the store directories before it exits.
  process.once("SIGTERM", () => controller.abort());
  process.once("SIGINT", () => controller.abort());

  // With no arguments, handleItem() reads the ANTHROPIC_* variables the spawn
  // script forwarded, including ANTHROPIC_WORK_SECRET.
  await new EnvironmentWorker({
    client,
    workdir: "/workspace",
    signal: controller.signal
  }).handleItem();
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

  	"github.com/anthropics/anthropic-sdk-go/v2"
  	"github.com/anthropics/anthropic-sdk-go/v2/lib/environments"
  	"github.com/anthropics/anthropic-sdk-go/v2/option"
  )

  func main() {
  	// Canceling the context when the container is stopped lets the worker upload
  	// changed memory files and remove the store directories before it exits.
  	ctx, stop := signal.NotifyContext(context.Background(), os.Interrupt, syscall.SIGTERM)
  	defer stop()

  	client := anthropic.NewClient(option.WithAuthToken(os.Getenv("ANTHROPIC_ENVIRONMENT_KEY")))
  	worker := environments.NewEnvironmentWorker(client, environments.EnvironmentWorkerOptions{
  		Workdir: "/workspace",
  	})
  	// With zero-value options, HandleItem reads the ANTHROPIC_* variables the spawn
  	// script forwarded, including ANTHROPIC_WORK_SECRET.
  	if err := worker.HandleItem(ctx, environments.HandleItemOptions{}); err != nil {
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

## Stage files for a session

Anthropic doesn’t mount files or GitHub repositories into self-hosted sandboxes. To make session-specific files available:

1. Pass file references, such as an S3 path or commit SHA, in the session’s `metadata` (csharp, go: `Metadata`) field.
2. In your spawn script or `--on-work` handler, retrieve the session (`GET /v1/sessions/{session_id}`) and read `metadata` (csharp, go: `Metadata`). The claimed work item carries the session ID but not the metadata.
3. Stage the files into the working directory before any tool runs.

The cURL sample reads an access token from `ANTHROPIC_AUTH_TOKEN`. To get one, set up Workload Identity Federation with the default `workspace:developer` scope, as [Set up federation](https://platform.claude.com/docs/en/manage-claude/workload-identity-federation#set-up-federation) describes. Then, exchange your workload’s identity token for an access token, as [Authenticate from your workload](https://platform.claude.com/docs/en/manage-claude/workload-identity-federation#authenticate-from-your-workload) shows. Set `ANTHROPIC_AUTH_TOKEN` only in the shell where you run the cURL sample, because it takes precedence over your federation settings. [Authentication](https://platform.claude.com/docs/en/manage-claude/authentication) lists the other credentials that the API accepts, such as the API key from the quickstart.

<CodeGroup>
  ```bash cURL
  curl -sS --fail-with-body https://api.anthropic.com/v1/sessions \
    -H "authorization: Bearer $ANTHROPIC_AUTH_TOKEN" \
    -H "anthropic-version: 2026-10-21" \
    -H "anthropic-beta: managed-agents-2026-04-01" \
    -H "content-type: application/json" \
    -d '{
      "agent": "agent_011CYm1BLqPXpQRk5khsSXrs",
      "environment_id": "env_01595EKxaaTTGwwY3kyXdtbs",
      "metadata": {"input_file": "s3://my-bucket/data.csv"}
    }'
  ```

  ```bash CLI
  ant beta:sessions create \
    --agent agent_011CYm1BLqPXpQRk5khsSXrs \
    --environment-id env_01595EKxaaTTGwwY3kyXdtbs \
    --metadata '{"input_file": "s3://my-bucket/data.csv"}'
  ```

  ```python Python
  session = client.beta.sessions.create(
      agent=agent.id,
      environment_id=environment.id,
      metadata={"input_file": "s3://my-bucket/data.csv"},
  )
  ```

  ```typescript TypeScript
  const session = await client.beta.sessions.create({
    agent: agent.id,
    environment_id: environment.id,
    metadata: { input_file: "s3://my-bucket/data.csv" }
  });
  ```

  ```csharp C#
  var session = await client.Beta.Sessions.Create(new()
  {
      Agent = agent.ID,
      EnvironmentID = environment.ID,
      Metadata = new Dictionary<string, string> { ["input_file"] = "s3://my-bucket/data.csv" },
  });
  ```

  ```go Go
  session, err := client.Beta.Sessions.New(ctx, anthropic.BetaSessionNewParams{
  	Agent:         anthropic.BetaSessionNewParamsAgentUnion{OfString: anthropic.String(agent.ID)},
  	EnvironmentID: environment.ID,
  	Metadata: map[string]string{
  		"input_file": "s3://my-bucket/data.csv",
  	},
  })
  if err != nil {
  	panic(err)
  }
  ```

  ```java Java
  var session = client.beta().sessions().create(SessionCreateParams.builder()
      .agent(agent.id())
      .environmentId(environment.id())
      .metadata(SessionCreateParams.Metadata.builder()
          .putAdditionalProperty("input_file", JsonValue.from("s3://my-bucket/data.csv"))
          .build())
      .build());
  ```

  ```php PHP
  $session = $client->beta->sessions->create(
      agent: $agent->id,
      environmentID: $environment->id,
      metadata: ['input_file' => 's3://my-bucket/data.csv'],
  );
  ```

  ```ruby Ruby
  session = client.beta.sessions.create(
    agent: agent.id,
    environment_id: environment.id,
    metadata: {input_file: "s3://my-bucket/data.csv"}
  )
  ```
</CodeGroup>

## Next steps

<CardGroup cols={2}>
  <Card title="Monitor and troubleshoot self-hosted workers" icon="lightning" href="https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-operations">
    Read queue depth, stop sessions and workers cleanly, and fix common failures.
  </Card>
</CardGroup>
