> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Command line settings

> Reference for the claude-science command: its subcommands, the serve flags, the single-use login link, and the environment variables you can set.

Reference for the claude-science command: its subcommands, the serve flags, the single-use login link, and the environment variables you can set.\
claude-science serve starts Claude Science and opens the web app in your browser at a single-use login link. On Linux, everyday use is that one command. The others manage the running program: they mint login links, report status, follow logs, install updates, and merge data directories. On Windows, the installer adds the command to your PATH for new terminals. There the app window you open from the Start menu is the everyday way in, and the commands below manage the same running program.

## Commands

| Command | What it does |
| - | - |
| `claude-science serve` | Start the background program and open the web app in your browser at a single-use login link. One runs per data directory; Ctrl-C stops it. |
| `claude-science open` | Mint a fresh login link from the running program and open it in your browser. |
| `claude-science url` | Print a fresh login link. At a terminal, the link comes inside a short banner. When you pipe or capture the output, standard output carries only the link. |
| `claude-science status` | Print whether the program is running, the version, and the port, as JSON. |
| `claude-science logs` | Print the newest log file from the data directory. `--tail` follows it live. |
| `claude-science stop` | Stop the program cleanly. |
| `claude-science update` | Check for and install an update. `--check` only reports; `--to <build>` installs a specific build, which is also how you roll back (see [Roll back to an earlier build](#roll-back-to-an-earlier-build)). Updates are signature-verified and replace the binary atomically. |
| `claude-science import` `<path>` | Merge another data directory, or its database file, into this one. |
| `claude-science install` | Windows only. Install the app for your user account, with a PATH entry, a Start menu shortcut, and an uninstall entry under Windows **Settings > Apps > Installed apps**. Run it again to repair them. |
| `claude-science uninstall` | Windows only. Remove the app, its shortcuts, and its PATH entry while keeping your data; `--purge` also deletes the data directory. Quit Claude Science first. |
| `claude-science --version` | Print the version. |
| `claude-science <command> --help` | Print help for any command. |

<Note>
  `import` has no preview and no undo. Back up the data directory before you run it; running the same import a second time is safe.
</Note>

### Roll back to an earlier build

`claude-science update --to <build>` installs one specific build. `<build>` is an 8-character build ID such as `3f9a01bc`, not a version number. `claude-science update --check` prints the ID of the installed build as `Current`.

Claude Science checks for updates in the background and shows **Update available** when one is ready. Note the `Current` ID before you choose **Restart to update**, so you know which build to go back to.

If a newer build has already changed how your data directory stores sessions, the command refuses an older build and installs nothing, because an older build can permanently lose part of every session it writes to. The refusal names a flag that overrides it, `--accept-layout-downgrade`, and says when that is safe. If you cannot tell from the message whether it is safe for you, do not add the flag.

<Note>
  An older build that does install can still refuse to start if a newer build has already updated the database in your data directory. When it does, it stops at startup and changes nothing in your data. At a terminal, it says the data was `written by a NEWER version`. To start the app again, run `claude-science update`, which installs the latest build.
</Note>

## Global flags

These two work on every command. On Windows, `~` in the defaults below is your user profile folder, `%USERPROFILE%`.

| Flag | Default | What it does |
| - | - | - |
| `--data-dir` `<dir>` | `~/.claude-science` | The data directory to use. Sign-in tokens and the shared package environment stay under `~/.claude-science` whichever directory you choose, so all your data directories share one sign-in. |
| `--config` `<file>` | `~/.claude-science/config.toml` | The configuration file to read. |

## The login link

When serve starts, it prints a line of the form `Web UI → http://localhost:<port>/?nonce=...`. The nonce is a one-time password: it signs one browser tab in and then expires, about three minutes after it is printed. The signed-in tab stays signed in until you restart the program.\
You never need to keep a link. claude-science open mints a fresh one and opens it in your browser whenever you want to sign in again.

The app listens on 127.0.0.1 unless you change `--host`, so it is reachable only from the machine it runs on. For a machine you reach over SSH, first forward two ports from your computer, the web app port and the preview port (by default the web app port plus one), as [Run on a remote Linux server](/docs/claude-science/run-on-remote-linux-server#forward-the-ports-from-your-computer) shows. Then run claude-science url on that machine and open the link it prints in your own browser.

## Flags for serve

| Flag | Default | What it does |
| - | - | - |
| `--port` `<n>` | `8000` | The port the web app is served on. 0 picks a free port. If you did not pass `--port` and 8000 is busy, the app takes the next free port and says so. If you passed `--port` and that port is busy, serve exits and tells you to pick a different one. `claude-science status` prints the port in use. |
| `--no-browser` | off | Do not open a browser. url prints a login link any time you want one. |
| `--detached` | off | Run in the background. Implies `--no-browser`. |
| `--no-auto-update` | off | Do not check for or install updates. For a pinned or centrally managed install. |
| `--host` `<address>` | 127.0.0.1 | The address the app listens on. Any other address exposes the app to your network. To work from another machine, use an SSH tunnel. |
| `--base-path` `</prefix>` | unset | Serve the app under a URL prefix behind a reverse proxy. |
| `--allow-origin` `<url>` | unset | An extra browser Origin allowed to connect, written as `https://<host>` with an optional port and no path. A value that starts with `http://`, has a path, or has no `https://` in front is ignored without a message. Repeat the flag for more than one. It does not change which sites Claude can reach. |
| `--sandbox-port` `<n>` | port + 1 | The separate origin that previews of generated HTML are served from, so a previewed page cannot read your session. |
| `--verbose` | off | Show startup and info log lines on the console; by default they go only to the log file. |

## Dangerous flags

`claude-science serve` accepts two flags that each turn off a protection.

<Warning>
  * `--dangerously-no-sandbox` turns the [sandbox](/docs/claude-science/core-concepts#sandbox) off. On macOS and Linux, the code Claude runs then has full read and write access to your home directory and unrestricted network access. On Windows, code cells do not run at all while the flag is set.
  * `--dangerously-skip-approvals` approves [permission cards](/docs/claude-science/core-concepts#permission-cards) for you without showing them, until you restart without the flag. That includes Claude's requests to run code, reach network hosts, open folders, and use connector tools. Cards still show for a connector tool you set to [**Ask each time**](/docs/claude-science/custom-connectors) and for requests only you can answer, such as entering an SSH password, permanently deleting artifacts, or spending usage credits. On Linux, the card for a folder too large to check for credential files also still shows. Questions Claude asks you still appear.

  These flags are acceptable only on a machine that is already isolated, such as a container or a disposable virtual machine. Never use them with data or prompts that came from someone else, because Claude may follow instructions hidden in them. Neither belongs in everyday use.
</Warning>

If your organization [manages the network allowlist](/docs/claude-science/admin-controls#network-allowlist), the app ignores `--dangerously-no-sandbox` and keeps the sandbox on. If the app learns of that setting only after it has started without the sandbox, it pauses new sessions and messages until you restart it.

## Environment variables

`DO_NOT_TRACK`, set to any value other than `0` or `false`, turns usage analytics and error reports off. It is the same switch as `disable_telemetry = true` in the configuration file. `GITHUB_TOKEN` (or `GH_TOKEN`) is optional and is used only against `api.github.com`, to lift the rate limit when you install a skill from a GitHub repository. Claude Science also reads the standard proxy variables (`HTTPS_PROXY`, `HTTP_PROXY`, `NO_PROXY`, and `ALL_PROXY`); see [Use Claude Science on a corporate network](/docs/claude-science/corporate-networks#connect-through-an-outbound-proxy). The proxy address variables are the one case where the environment overrides the configuration file, and `NO_PROXY` is merged with the `no_proxy` key rather than replacing it. Every other setting belongs in the configuration file.

An app started from the macOS Dock or Finder, or from the Windows Start menu, does not see variables exported in a terminal.

* **macOS**: the app reads the `env` file in the data directory (by default `~/.claude-science/env`) when it starts. It applies only a fixed list of variables from the file, which includes `DO_NOT_TRACK` and the proxy variables but not `GITHUB_TOKEN` or `GH_TOKEN`. Put `DO_NOT_TRACK` or a proxy variable there as a `KEY=VALUE` line, then quit and reopen the app. Add a GitHub token under **Settings > Credentials** instead, and delete its line from the file. Before version 0.1.56, the file could set any variable.
* **Windows**: set the variable as a user environment variable, then quit and reopen the app.

See [How the environment variables reach the app](/docs/claude-science/corporate-networks#how-the-environment-variables-reach-the-app).

## See also

<CardGroup cols={1}>
  <Card title="Run on a remote Linux server" href="/docs/claude-science/run-on-remote-linux-server">
    Install Claude Science on a server and use it from your own browser through an SSH tunnel.
  </Card>

  <Card title="Configuration file reference" href="/docs/claude-science/configuration-file-reference">
    Find the `config.toml` file and set its network-related keys.
  </Card>

  <Card title="Remote compute clusters" href="/docs/claude-science/remote-compute-clusters">
    Connect an SSH host and run jobs on it.
  </Card>
</CardGroup>
