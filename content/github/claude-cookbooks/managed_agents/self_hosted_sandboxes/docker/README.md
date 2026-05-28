# Docker demo — Self-Hosted Sandboxes

The host runs `ant beta:worker poll` directly; per claimed work item its
`--on-work` script (`on-work.sh`) `docker run`s a per-session container whose
entrypoint is `ant beta:worker run`. Each container gets a `/workspace` (the
agent's working tree; skills download here) backed by a per-session Docker
volume so the tree and skills survive across containers for one session.

This is the no-cloud variant of `../cf/` (which runs the same
`ant beta:worker run` entrypoint, but in Cloudflare Containers): same CLI, same
env contract, just plain Docker on a host you control.

- **`Dockerfile`** — the per-session image: pinned `ant` CLI, `WORKDIR
  /workspace`, `ENTRYPOINT ["ant","beta:worker","run", …]`. The CLI owns
  heartbeat, backlog reconcile, SSE, the `bash`/`read`/`write`/`edit`/`glob`/
  `grep` toolset, and the work-item force-stop on exit.
- **`on-work.sh`** — invoked by the poller per work item. Reads the
  `ANTHROPIC_{WORK_ID,ENVIRONMENT_ID,SESSION_ID,ENVIRONMENT_KEY}` the poller
  sets, drains the work JSON on stdin, and starts a detached `--rm`
  per-session container (idempotent: a duplicate item for a live session is a
  no-op). Exits immediately so the poller claims the next item.
- **`start.sh`** — builds the image and execs the host poller with
  `--on-work on-work.sh`.

Idle policy is the SDK default: each container exits 60s after
`session.status_idle` with `stop_reason: end_turn`; any other event resets the
clock. `--rm` then removes it; the per-session volume persists for the next
message in that session.

No org API key anywhere: the only credential is the **environment key**. The
poller uses it to claim work; it's passed into each container as
`ANTHROPIC_ENVIRONMENT_KEY` (the per-session calls — event stream, lease
heartbeat, force-stop) **and** as `ANTHROPIC_AUTH_TOKEN` (the CLI's
skill-download client resolves only `ANTHROPIC_API_KEY` /
`ANTHROPIC_AUTH_TOKEN`, not `ANTHROPIC_ENVIRONMENT_KEY` — without it skills
silently fail to download).

## Prerequisites

- Docker
- `ant` on the host's PATH, the **same build** pinned in `Dockerfile`
  (`ARG ANT_VERSION`). Install it:

  ```sh
  VERSION=1.9.0
  OS=$(uname -s | tr '[:upper:]' '[:lower:]')
  ARCH=$(uname -m | sed -e 's/x86_64/amd64/' -e 's/aarch64/arm64/')
  curl -fsSL "https://github.com/anthropics/anthropic-cli/releases/download/v${VERSION}/ant_${VERSION}_${OS}_${ARCH}.tar.gz" \
    | sudo tar -xz -C /usr/local/bin ant
  ant --version
  ```

## Run

```sh
export ANTHROPIC_ENVIRONMENT_ID=env_...
export ANTHROPIC_ENVIRONMENT_KEY=sk-ant-oat...
./start.sh
```

Then create a session pointing at that `ANTHROPIC_ENVIRONMENT_ID` and send it a
message. You should see, in order:

```
[start] polling env=env_... base=https://api.anthropic.com
[on-work] session=sesn_... work=work_... container=... (started)
```

Container logs (`docker logs cma-sesn_...`) show the `ant beta:worker run`
JSON: `downloaded skill …`, `executing tool …`, etc. The container removes
itself after it idles out; the `cma-ws-<session_id>` volume remains for that
session's next message (`docker volume rm` to discard).

Unlike the webhook-driven demos (Modal/Daytona/Vercel/Cloudflare), there is no
webhook here — `ant beta:worker poll` long-polls the environment directly, so
nothing needs to be exposed to the internet.
