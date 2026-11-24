---
title: Security model
url: https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-security
description: Shared responsibility model for self-hosted sandbox environments.
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
    Claude Models on Google Cloud (Anthropic managed):
      availability: beta
      note: You write your own worker, which calls the Environments Work endpoints.
---

In every environment, Anthropic secures the parts it runs: session and work queue integrity, multitenant isolation, and agent-context minimization. When you self-host sandboxes, the following responsibilities fall to you.

## What you own

* **Sandbox image quality and runtime hardening.** Anthropic does not inspect or verify your sandbox image. Follow best practices such as dropping unnecessary Linux capabilities, running as a non-root user, and using a read-only root filesystem.

* **Network egress controls.** Your VPC and firewall rules determine your sandbox’s network access. Without egress restrictions, a compromised tool execution can reach arbitrary external hosts. Restrict outbound traffic to only the endpoints your tools require.

* **Service key storage and rotation.** The environment service key (`ANTHROPIC_ENVIRONMENT_KEY`) authorizes polling your environment’s work queue and submitting results back to sessions. Store it in a secrets manager, not in environment files or sandbox images. Rotate it immediately if you suspect exposure.

* **Untrusted workload isolation.** The environment service key is scoped to one environment’s work queue. If you run untrusted code inside your sandbox, consider provisioning a separate workspace and environment for each trust boundary. This way, each key reaches only one trust boundary’s sessions, such as one user’s, rather than every session in a shared environment. On a cloud platform, see [Worker credentials on cloud platforms](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-security#worker-credentials-on-cloud-platforms).

* **Per-session credentials.** Each work item your worker claims can carry a per-session `secret` (csharp, go: `Secret`), which the worker uses in place of the environment service key. Access to [memory stores](https://platform.claude.com/docs/en/managed-agents/memory) requires the `secret` (csharp, go: `Secret`): the memory store endpoints reject the environment service key (see [Forward the work item’s secret](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-per-session#forward-the-work-items-secret)). Pass the `secret` (csharp, go: `Secret`) only into the sandbox that serves that session, keep it out of images and shared volumes, and never log it.

* **Tool-execution blast radius.** Tools run inside your sandbox with whatever permissions your process has. Apply least privilege to the process user and mount only the directories your tools require.

* **Log retention and session content.** Conversation content and tool outputs pass through your worker and stay in your environment. You are responsible for retaining, redacting, or deleting that data in compliance with your own policies. Anthropic has no visibility into what your worker does with session content once delivered.

* **Memory store contents.** Anthropic hosts [memory stores](https://platform.claude.com/docs/en/managed-agents/memory), including their version history. When a session attaches one, the worker keeps a working copy under `/mnt/memory/` in your sandbox while it serves the session and syncs changes back. The worker deletes that copy when it finishes with the session (see [How the worker handles memory](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-memory#how-the-worker-handles-memory)). A worker that exits without running its teardown leaves the copy behind. Cleanup of leftover copies, the permissions on that path, and isolation between sessions that share a filesystem are your responsibility.

* **Read-only memory stores.** A store attached with `read_only` access is protected from upload, not from local modification.

  * **What is blocked:** The worker’s `write` and `edit` tools refuse to write under the store’s directory. The worker uploads nothing from that directory. The memory store endpoints reject requests that use the session’s `secret` (csharp, go: `Secret`) to write to the store.
  * **What is not blocked:** Commands that the agent runs through the `bash` tool can change the local copy. So can [custom tools](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-custom-tools) or MCP servers that you serve from the sandbox, which run with the worker’s permissions.
  * **What happens to a changed file:** For as long as the worker serves the session, later tool calls read the changed file. The worker doesn’t restore it on its own. If that file gets a new version in the store during that time, the worker’s next sync overwrites the local file with that version.
  * **How to prevent local changes too:** Disable the `bash` tool for that agent, and give it no custom tools or MCP servers that write to the sandbox’s filesystem.

## What Anthropic cannot do for you

* **Know that your key leaked.** Anthropic can detect anomalous usage patterns, but cannot know your key was compromised. If you suspect `ANTHROPIC_ENVIRONMENT_KEY` leaked, revoke it and generate a replacement immediately. Revocation is validated on every request, so it takes effect on the worker’s next call.
* **Verify your worker build.** Anthropic does not inspect your sandbox image or runtime. A supply-chain compromise in your image is not detectable from Anthropic’s side.
* **Isolate tools inside your sandbox.** Anthropic’s security boundary stops at the sandbox. How you isolate individual tool executions from each other inside that boundary is entirely your responsibility.
* **Enforce data retention in your environment.** Once session content reaches your worker, it is outside Anthropic’s data lifecycle controls.

## Worker credentials on cloud platforms

If you use Managed Agents through a cloud platform, your worker authenticates with that platform’s credentials instead of the environment service key. See [Worker authentication on cloud platforms](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes#worker-authentication-on-cloud-platforms).

On Claude Models on Google Cloud (Anthropic managed), take these precautions:

* **Keep untrusted workloads apart:** The worker’s IAM role applies to every workspace in the Google Cloud project. Separate workspaces in that project don’t limit what the worker can reach. Use a separate project for each untrusted workload. See [Access on cloud platforms](https://platform.claude.com/docs/en/manage-claude/workspaces#access-on-cloud-platforms).
* **Protect the worker’s credentials:** Run tool calls where they can’t reach the worker’s Google Cloud credentials or the cloud metadata server.
