> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Run on a remote Linux server

> Install Claude Science on a cloud VM or lab server and use it from your own browser through an SSH tunnel.

Claude Science runs on a remote Linux server (a cloud VM or a lab machine) the same way it runs on a workstation: the application and your data stay on the server, and you use the web app from your computer's browser through an SSH tunnel. Setup takes about five minutes, plus a few minutes of environment setup on first launch.

<Note>
  This page covers running all of Claude Science on a remote machine. To keep Claude Science on your own computer and have it run jobs on a machine you reach over SSH, see [Remote compute clusters](/docs/claude-science/remote-compute-clusters).
</Note>

The server needs x64 Linux on a glibc-based distribution (arm64 and musl-based distributions such as Alpine aren't supported), about 5 GB of free disk space, and the system packages below. Your Claude account needs a Pro, Max, Team, or Enterprise plan; see [Requirements](/docs/claude-science/overview#requirements).

## Install dependencies

Claude runs code inside a sandbox, and the sandbox needs two system packages: bubblewrap and socat. On Ubuntu or Debian:

```bash theme={null}
sudo apt-get update && sudo apt-get install -y curl bubblewrap socat
```

<Note>
  The sandbox requires bubblewrap 0.8.0 or later; check with `bwrap --version`. Ubuntu 24.04 ships a new enough version, and Ubuntu 22.04 doesn't. The sandbox isn't optional: Claude Science refuses to start rather than run code unsandboxed.
</Note>

## Install Claude Science

```bash theme={null}
curl -fsSL https://claude.ai/install-claude-science.sh | bash
```

The installer downloads the current release, verifies its checksum, and installs the `claude-science` command in `~/.local/bin`. If it prints a PATH line at the end, add that line to your shell profile. Then confirm the command works:

```bash theme={null}
. ~/.profile
claude-science --version
```

## Forward the ports from your computer

Set up the tunnel before you start Claude Science: the sign-in link it prints is only valid for about three minutes.

By default, the web app listens only on the server's localhost, so it isn't exposed to the network. An SSH tunnel makes it reachable from your computer. Claude Science uses two ports: one for the web app (8000) and a separate one for previews of generated HTML, served from its own origin so a previewed page can't read your session. The preview port is always the web app port plus one, so 8001 by default. Forward both. In a terminal on your computer:

```bash theme={null}
ssh -L 8000:localhost:8000 -L 8001:localhost:8001 you@server.example.com
```

Leave that terminal open; the tunnel lasts as long as the SSH connection. If you work on the server through VS Code's Remote-SSH extension, it forwards ports automatically as the app uses them; check its Ports panel to confirm both ports are forwarded.

## Start Claude Science

On the server:

```bash theme={null}
claude-science serve --no-browser
```

First launch prints the sign-in link, of the form `http://localhost:8000/?nonce=...`, right away, and continues setting up its starter Python and R environments; the setup can take a few minutes and about 5 GB of disk. If port 8000 or 8001 is taken on either machine, pass a different port to serve (for example `--port 8765`; previews then use the next port up, 8766) and change the `ssh -L` forwards to match.

To run it in the background instead, use `claude-science serve --no-browser --detached`. `claude-science status` reports whether it's running, and `claude-science stop` stops it.

## Sign in

Open the printed link in your computer's browser. The link is single-use and expires about three minutes after it's printed; run `claude-science url` on the server to print a fresh one at any time. Restarting with `claude-science stop` then `claude-science serve --no-browser` also prints a fresh link.

Sign in with your Claude account. If the sign-in redirect can't find its way back through the tunnel, choose **Paste a code** on the sign-in screen. Then complete the setup wizard as described in [Get started](/docs/claude-science/get-started).

## Keep it up to date

`claude-science update` checks for and installs updates. See [Command line settings](/docs/claude-science/command-line-settings) for the full command reference, including `logs` and the `serve` flags.

## Troubleshooting

| Symptom                                                                                         | What it means                                                                                                                                                                                                                                             |
| ----------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `command not found: claude-science`                                                             | `~/.local/bin` isn't on your PATH yet. Run `. ~/.profile` or open a new terminal.                                                                                                                                                                         |
| An error mentioning `bwrap too old`                                                             | The server's bubblewrap is older than 0.8.0. Upgrade it, or use a distribution that ships a newer version, such as Ubuntu 24.04 or later.                                                                                                                 |
| An error mentioning `cannot create unprivileged user namespaces`                                | The kernel or an AppArmor profile blocks the sandbox from creating user namespaces; some Ubuntu 24.04 images restrict this. The error message names the exact setting to change for your distribution.                                                    |
| The sign-in link shows an expired-link page                                                     | Links are single-use and valid for about three minutes. Run `claude-science url` on the server and open the fresh link; restarting with `claude-science stop` then `claude-science serve --no-browser` also prints one.                                   |
| Sign-in stops at claude.ai                                                                      | The redirect couldn't return through the tunnel (choose **Paste a code**), your account is on the Free plan (an upgrade is required), or your Team or Enterprise organization hasn't [enabled Claude Science](/docs/claude-science/enable-claude-science) yet. |
| Interactive HTML previews render as static snapshots after a short delay (charts don't respond) | The tunnel isn't forwarding the preview port. Add the second `-L` forward; the preview port is the web app port plus one (8001 by default).                                                                                                               |
| The browser can't reach `localhost:8000`                                                        | The tunnel isn't up; rerun the `ssh -L` command. If the tunnel is up, confirm Claude Science is running on the server with `claude-science status`.                                                                                                       |
| The installer reports no binary for your platform                                               | Claude Science on Linux needs x64 with glibc. arm64 servers and musl-based distributions such as Alpine aren't supported.                                                                                                                                 |
