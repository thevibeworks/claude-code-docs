> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Write a credential helper

> Supply Claude Desktop on 3P with a short-lived inference token by running an executable you provide

A credential helper is an executable on the user's machine that prints an inference token to stdout. Claude Desktop on 3P runs it whenever it needs a credential for the configured inference provider, caches the result for a configurable time, and re-runs it when the credential expires. Use a helper when your token comes from an internal secret broker, a CLI, or an SSO flow that the built-in interactive sign-in options don't cover.

Configure the helper with the `inferenceCredentialHelper` key; see the [Configuration reference](/docs/third-party/claude-desktop/configuration#inferencecredentialhelper) for the full list of helper-related keys.

<Note>
  `inferenceCredentialHelper` supplies credentials for the inference connection only. An MCP server deployed through [`managedMcpServers`](/docs/third-party/claude-desktop/configuration#managedmcpservers) uses the separate per-server `headersHelper` key, which follows the same execution model but prints a flat JSON header map and has its own cache and renewal settings (`headersHelperTtlSec`, default 300, versus `inferenceCredentialHelperTtlSec`, default 3600). See [Short-lived credentials with a headers helper](/docs/third-party/claude-desktop/extensions#short-lived-credentials-with-a-headers-helper).
</Note>

## What the helper must do

Claude Desktop runs the executable at the configured path with no arguments and reads stdout. The exit code must be `0`. Anything written to stderr is logged for diagnostics but otherwise ignored.

Stdout must contain exactly one of the following, with no banners, prompts, or log lines mixed in:

* **A single bare token.** The whole trimmed stdout becomes the bearer token.
* **A JSON object**, when per-request headers are needed:

  ```json theme={null}
  { "token": "...", "headers": { "X-Org-Route": "prod" } }
  ```

  Headers from the JSON object are merged over [`inferenceCustomHeaders`](/docs/third-party/claude-desktop/configuration#inferencecustomheaders); the helper's value wins on a conflict.

## When the helper runs

Claude Desktop sets the `CLAUDE_HELPER_CONTEXT` environment variable on every invocation so the script can decide whether interactive authentication (opening a browser, prompting for a device code) is appropriate.

| Value                 | Meaning                                                                                         |
| --------------------- | ----------------------------------------------------------------------------------------------- |
| `interactive`         | The user started a session and is present. Interactive sign-in is acceptable.                   |
| `mid-session-refresh` | A running session's credential expired. Prefer a silent refresh; the user is waiting on a turn. |
| `scheduled-task`      | A scheduled task started with no user present.                                                  |
| `setup-test`          | The in-app configuration window's connection test.                                              |
| `background`          | A background probe or health check.                                                             |

A well-behaved helper should attempt its silent path (cached token, refresh-token grant) for any value other than `interactive`, and exit non-zero rather than block on user input when that path is exhausted. Claude Desktop treats a non-zero exit as a refresh failure and surfaces it to the user.

The legacy variable `CLAUDE_HELPER_MANUAL_RUN=1` is also set when `CLAUDE_HELPER_CONTEXT` is `setup-test`, for scripts written before the context variable existed. New scripts should branch on `CLAUDE_HELPER_CONTEXT` instead.

The helper runs with a `PATH` that includes the user's login-shell `PATH` and standard install locations in addition to the app's launch environment, so a script can invoke tools such as `aws` or `gcloud` by name even when the app was launched from the Dock or Finder rather than a terminal.

## Timeouts and caching

The helper's output is cached for `inferenceCredentialHelperTtlSec` seconds (default 3600). Claude Desktop checks the cached credential's expiry before each turn and, when it has expired or is about to, re-runs the helper transparently before sending the turn, with no sign-in prompt and no app relaunch. With a TTL of 120 seconds or less, Claude Desktop skips the per-turn check; the helper then re-runs at the next session start, or mid-session when the provider rejects the credential (see [Turn off mid-session re-runs](#turn-off-mid-session-re-runs)).

Each run is bounded by `inferenceCredentialHelperTimeoutSec` seconds (default 60, maximum 600). When Claude Desktop re-runs the helper to recover a session mid-turn (`CLAUDE_HELPER_CONTEXT=mid-session-refresh`), the timeout is additionally clamped to 20 seconds so a slow helper can't stall the turn. A helper's silent path should comfortably finish within that window.

## Turn off mid-session re-runs

By default, when a running session's credential is rejected, Claude Desktop re-runs the helper with `CLAUDE_HELPER_CONTEXT=mid-session-refresh` to recover without interrupting the user. If your helper can't run safely outside the `interactive` context, set `inferenceCredentialHelperSilentRefreshEnabled` to `false`. Claude Desktop then keeps the cached credential until the next session start and surfaces an expiry prompt instead of re-running the helper mid-session.
