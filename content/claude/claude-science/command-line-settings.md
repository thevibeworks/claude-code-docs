> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Command line settings

> Reference for the claude-science command: every subcommand, the serve flags, the single-use login link, and the environment variables Claude Science reads.

Reference for the claude-science command: every subcommand, the serve flags, the single-use login link, and the environment variables Claude Science reads.\
claude-science serve starts Claude Science and opens the web app in your browser at a single-use login link. Everyday use is that one command. The others manage the running program: they mint login links, report status, follow logs, install updates, and merge data directories.

## Commands

| Command                             | What it does                                                                                                                                                                                              |
| ----------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `claude-science serve`              | Start the background program and open the web app in your browser at a single-use login link. One runs per data directory; Ctrl-C stops it.                                                               |
| `claude-science open`               | Mint a fresh login link from the running program and open it in your browser.                                                                                                                             |
| `claude-science url`                | Print a fresh login link alone on standard output and nothing else.                                                                                                                                       |
| `claude-science status`             | Print whether the program is running, the version, and the port, as JSON.                                                                                                                                 |
| `claude-science logs`               | Print the newest log file from the data directory. `--tail` follows it live.                                                                                                                              |
| `claude-science stop`               | Stop the program cleanly.                                                                                                                                                                                 |
| `claude-science update`             | Check for and install an update. `--check` only reports; --to `<version>` installs a specific version, which is also how you roll back. Updates are signature-verified and replace the binary atomically. |
| `claude-science import` `<path>`    | Merge another data directory, or its database file, into this one.                                                                                                                                        |
| `claude-science --version`          | Print the version.                                                                                                                                                                                        |
| `claude-science` `<command>` --help | Print help for any command.                                                                                                                                                                               |

<Note>
  `import` has no preview and no undo. Back up the data directory before you run it; running the same import a second time is safe.
</Note>

## Global flags

These two work on every command.

| Flag                 | Default                         | What it does                    |
| -------------------- | ------------------------------- | ------------------------------- |
| `--data-dir` `<dir>` | `~/.claude-science`             | The data directory to use.      |
| `--config` `<file>`  | `~/.claude-science/config.toml` | The configuration file to read. |

## The login link

When serve starts, it prints a line of the form `Web UI -> http://localhost:<port>/?nonce=...`. The nonce is a one-time password: it signs one browser tab in and then expires, about three minutes after it is printed. The signed-in tab stays signed in until you restart the program.\
You never need to keep a link. claude-science open mints a fresh one and opens it in your browser whenever you want to sign in again. For a machine you reach over SSH, claude-science url prints a fresh link alone on standard output: run it there, then open the printed link through your tunnel. The app listens on 127.0.0.1 unless you change --host, so it is reachable only from your own machine.

## Flags for serve

| Flag                      | Default   | What it does                                                                                                                    |
| ------------------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------- |
| `--port` `<n>`            | `8000`    | The port the web app is served on. 0 picks a free port.                                                                         |
| `--no-browser`            | off       | Do not open a browser. url prints a login link any time you want one.                                                           |
| `--detached`              | off       | Run in the background. Implies --no-browser.                                                                                    |
| `--no-auto-update`        | off       | Do not check for or install updates. For a pinned or centrally managed install.                                                 |
| `--host` `<address>`      | 127.0.0.1 | The address the app listens on. Anything else exposes the app to your network; prefer an SSH tunnel.                            |
| `--base-path` `</prefix>` | unset     | Serve the app under a URL prefix behind a reverse proxy.                                                                        |
| `--allow-origin` `<url>`  | unset     | An extra browser Origin allowed to connect; repeat the flag for more than one. It does not change which sites Claude can reach. |
| `--sandbox-port` `<n>`    | port + 1  | The separate origin that previews of generated HTML are served from, so a previewed page cannot read your session.              |
| `--verbose`               | off       | Show startup and info log lines on the console; by default they go only to the log file.                                        |

## Dangerous flags

<Warning>
  `--dangerously-no-sandbox` runs code with full read and write access to your home directory and an unrestricted network. `--dangerously-skip-approvals` approves every permission card automatically, for everything, until you restart without the flag; questions addressed to you still appear. Neither belongs in everyday use.
</Warning>

## Environment variables

`DO_NOT_TRACK`, set to any value, turns usage analytics off. It is the same switch as `disable_telemetry = true` in the configuration file. `GITHUB_TOKEN` is optional and is used only against `api.github.com`, to lift the rate limit when you install a skill from a GitHub repository. Claude Science also reads the standard proxy variables (`HTTPS_PROXY`, `HTTP_PROXY`, `NO_PROXY`, and `ALL_PROXY`); see [Use Claude Science on a corporate network](/docs/claude-science/corporate-networks#connect-through-an-outbound-proxy). The proxy address variables are the one case where the environment overrides the configuration file, and `NO_PROXY` is merged with the `no_proxy` key rather than replacing it. Every other setting belongs in the configuration file.

## See also

<CardGroup cols={1}>
  <Card title="Remote compute clusters" href="/docs/claude-science/remote-compute-clusters">
    Connect an SSH host and run jobs on it.
  </Card>
</CardGroup>
