# Modal demo — Self-Hosted Sandboxes

Reference implementation of the [usage guide](../docs/usage-guide.md)'s webhook flow on [Modal](https://modal.com). Two files:

- `modal_sandbox_webhook.py` — Modal app that receives the `session.status_run_started` webhook, verifies it with `client.beta.webhooks.unwrap()`, drains the environment work queue with `client.beta.environments.work.poller(drain=True, auto_stop=False)`, and spins up a per-session Modal Sandbox per item. A per-session `modal.Volume` is mounted at `/workspace` so the agent's working tree and downloaded skills persist across sandbox restarts for the same session. The sandbox env vars use the same `ANTHROPIC_*` contract as `ant beta:worker poll --on-work`.
- `sandbox_runner.py` — runs inside that Sandbox: `client.beta.environments.work.worker(environment_key=..., workdir="/workspace", unrestricted_paths=True).handle_item()`. It reads the `ANTHROPIC_*` env vars, builds the per-session `AgentToolContext` and downloads the agent's skills into `/workspace/skills/<name>/`, runs a `SessionToolRunner` (heartbeat + reconcile + event stream + `bash`/`read`/`write`/`edit`/`glob`/`grep` dispatch + result posting), and force-stops the work item on exit. Idle policy is the SDK default: it exits 60s after `session.status_idle` with `stop_reason: end_turn`; any other event resets the clock.

No org API key anywhere: the webhook polls with the environment key, and the runner authenticates with that same environment key — the single credential for both the control plane and the per-session calls.

## Prerequisites

```shell
pip install modal
modal setup   # auth to your Modal workspace
```

## Configure

```shell
modal secret create cma-self-hosted-sandboxes-secrets \
    ANTHROPIC_WEBHOOK_SECRET=placeholder \
    ANTHROPIC_ENVIRONMENT_ID='env_...' \
    ANTHROPIC_ENVIRONMENT_KEY='sk-ant-oat...'
```

## Deploy

```shell
modal deploy modal_sandbox_webhook.py
```

This prints a `*.modal.run` URL. Register that URL as a webhook for `session.status_run_started` in Console (or via the API), copy the issued secret, then update:

```shell
modal secret create cma-self-hosted-sandboxes-secrets \
    ANTHROPIC_WEBHOOK_SECRET='whsec_...' \
    ANTHROPIC_ENVIRONMENT_ID='env_...' \
    ANTHROPIC_ENVIRONMENT_KEY='sk-ant-oat...' \
    --force
```

(no redeploy needed — secrets are read at container start.)

## Test

Create a session pointing at your environment id and send it a message:

```py
session = client.beta.sessions.create(agent=agent_id, environment_id=ENVIRONMENT_ID)
client.beta.sessions.events.send(session.id, events=[{"type": "user.message", "content": "ls -la"}])
```

You should see, in order:

```shell
modal app logs cma-self-hosted-sandboxes
# [webhook] event=session.status_run_started session_id=...
# [webhook] acked work=... session=... sandbox=sb-... (created)
```

Sandbox stdout (the `[runner]` lines) shows in the Modal dashboard under
**Apps → cma-self-hosted-sandboxes → Sandboxes**.

## Iterating

Editing either Python file requires a redeploy (`modal deploy ...`). Editing only secrets does not. To force a clean slate while iterating, `modal app stop cma-self-hosted-sandboxes` before redeploying.
