# Sentry triage × Claude Managed Agents

Scheduled deployment: cron → CMA session with `sentry-cli` and a vault env-var credential → triage report in `/mnt/session/outputs/`.

## When the user asks to set this up, get it working, or debug it

1. **Invoke `/claude-api` first.** That skill loads the full Managed Agents API reference (agents, sessions, environments, events, webhooks, deployments, vaults, memory stores). Use it as the source of truth for any SDK call you write or edit. Don't guess field names.
2. **Read `./skill.md`** and walk the user through it step by step. It has the ordered checklist, every gotcha (two separate host allowlists, immutable `secret_name`, replace-only `allowed_hosts`, DST cron semantics, auto-pause on permanent failures), and the debugging table.
3. **After the base schedule works, offer extensions.** Ask the user which (if any) they want, then edit `setup_agent.py` and/or `deploy.py` accordingly:
   - **Deliver the report** instead of leaving it in the sandbox: a `session.status_idled` webhook that downloads the report and posts to Slack (see `managed_agents/slack` for the bridge pattern)
   - **More CLIs**: add other env-var-authenticated CLIs as additional vault credentials, one credential per token with its own host allowlist
   - **Outcomes**: rubric-graded iterate loop (`user.define_outcome` event instead of `user.message` in `initial_events`)
   - **Memory store**: track issue history across runs so the agent can flag regressions it has seen before (`resources: [{type: "memory_store", ...}]`)

   Pull exact shapes from the `/claude-api` skill's `shared/managed-agents-*.md` docs.

One-time provisioning is `uv run python setup_agent.py`. Schedule with `uv run python deploy.py`. Smoke-test with `uv run python run_now.py`. Push prompt or model changes with `uv run python update_agent.py` (edits live in `agent_config.py`).
