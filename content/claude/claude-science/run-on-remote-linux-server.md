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

Claude runs code inside a sandbox, and the sandbox needs two system packages: bubblewrap and socat. Installing them takes administrator (`sudo`) access. Without it, see [Run Claude Science without administrator access](#run-claude-science-without-administrator-access).

On Fedora, RHEL, or Arch, use the command for your distribution from the Linux tab of [Install](/docs/claude-science/get-started#install). On Ubuntu or Debian, run:

```bash theme={null}
sudo apt-get update && sudo apt-get install -y curl bubblewrap socat
```

<Note>
  The sandbox requires bubblewrap 0.8.0 or later; check with `bwrap --version`. Ubuntu 24.04 ships a new enough version, and Ubuntu 22.04 doesn't. If Claude Science can't set up the sandbox, it refuses to start rather than run code unsandboxed.
</Note>

## Run Claude Science without administrator access

If you don't have administrator (root or `sudo`) access to a shared server or cluster, choose one of these:

* **Ask the server's administrator** to set up what the sandbox needs: bubblewrap 0.8.0 or later, socat, and a kernel that allows unprivileged user namespaces.
* **Use the server as an SSH host.** Install Claude Science on your own computer and add the server as an SSH host (see [Remote compute clusters](/docs/claude-science/remote-compute-clusters)), if your organization allows SSH hosts. Claude runs jobs on the server under your own account, with your approval. Jobs run outside the sandbox, so the server doesn't need bubblewrap, socat, or the kernel setting, and you don't need administrator access there.

Administrators usually install bubblewrap and socat, and only an administrator can change the kernel setting. On Ubuntu 23.10 and later, bubblewrap can also need an AppArmor profile that lets it create user namespaces. Claude Science checks for these when it starts and names the first one that's missing. Once that's fixed, the next start names the next one, if any.

Installing Claude Science itself doesn't need root or `sudo`. The installer puts the `claude-science` command in `~/.local/bin`, or in another folder you own if you export `CLAUDE_SCIENCE_INSTALL_DIR` with that folder's path before you run it.

If you run Claude Science on a cluster's login node, these points differ from a server you have to yourself:

* Check your site's rules first. Claude runs its analysis code on the machine where Claude Science runs, and many sites limit long-running or heavy work on login nodes.
* Choose your own port, because someone else may already be using the default port, 8000. [Start Claude Science](#start-claude-science) shows how to pass a port. After you start it, `claude-science url` prints both ports. Forward each one with that number on both sides.
* If the cluster's address sends you to one of several login nodes, connect the tunnel to the node where Claude Science is running. Running `hostname` on that node prints its name.
* Claude Science needs about 5 GB in your home folder for its environments, even if you keep your projects elsewhere.

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

By default, the web app listens only on the server's localhost, so it isn't exposed to the network. An SSH tunnel makes it reachable from your computer. Claude Science uses two ports: one for the web app (8000) and a separate one for previews of generated HTML, served from its own origin so a previewed page can't read your session. The preview port defaults to the web app port plus one, so 8001. Forward both. In a terminal on your computer:

```bash theme={null}
ssh -L 8000:localhost:8000 -L 8001:localhost:8001 you@server.example.com
```

Leave that terminal open; the tunnel lasts as long as the SSH connection. If you work on the server through VS Code's Remote-SSH extension, it forwards ports automatically as the app uses them; check its Ports panel to confirm both ports are forwarded.

If the preview port is taken on the server, Claude Science uses a free port instead. After you start it, `claude-science url` prints both ports. Add a forward for the preview port it prints, with that number on both sides (`-L <port>:localhost:<port>`).

## Start Claude Science

On the server:

```bash theme={null}
claude-science serve --no-browser
```

First launch prints the sign-in link, of the form `http://localhost:8000/?nonce=...`, right away, and continues setting up its starter Python and R environments; the setup can take a few minutes and about 5 GB of disk. If port 8000 or 8001 is taken on either machine, pass a different port to serve (for example `--port 8765`) and change the `ssh -L` forwards to match. Previews then use the next port up, 8766, if it is free.

To run it in the background instead, use `claude-science serve --no-browser --detached`. `claude-science status` reports whether it's running, and `claude-science stop` stops it.

## Sign in

Open the printed link in your computer's browser. The link is single-use and expires about three minutes after it's printed; run `claude-science url` on the server to print a fresh one at any time. Restarting with `claude-science stop` then `claude-science serve --no-browser` also prints a fresh link.

Sign in with your Claude account. If the sign-in redirect can't find its way back through the tunnel, choose **Paste code instead** on the sign-in screen. Then complete the setup wizard as described in [Get started](/docs/claude-science/get-started).

## Keep it up to date

`claude-science update` checks for and installs updates. See [Command line settings](/docs/claude-science/command-line-settings) for the command reference, including `logs` and the `serve` flags.

## Troubleshooting

| Symptom | What it means |
| - | - |
| `command not found: claude-science` | `~/.local/bin` isn't on your PATH yet. Run `. ~/.profile` or open a new terminal. |
| An error mentioning `bwrap not found on PATH` | bubblewrap isn't installed, or isn't on your PATH. Install it as shown in [Install dependencies](#install-dependencies), or ask the server's administrator. |
| An error mentioning `socat is required` | socat isn't installed, or isn't on your PATH. Install it as shown in [Install dependencies](#install-dependencies), or ask the server's administrator. |
| An error mentioning `bwrap too old` | The server's bubblewrap is older than 0.8.0. Upgrade it, or use a distribution that ships a newer version, such as Ubuntu 24.04 or later. |
| An error mentioning `cannot create unprivileged user namespaces` | The kernel or an AppArmor profile blocks the sandbox from creating user namespaces; some Ubuntu 24.04 images restrict this. The error message names the settings to check on Ubuntu, Debian, and other distributions. |
| An error mentioning `port 8765 is already in use by another app` | Another program is using the port you chose with `--port`. Quit that program, or choose a different port. After you start Claude Science, `claude-science url` prints both ports to forward. |
| An error mentioning `port 8765 is already in use by another Claude Science daemon` | Another copy of Claude Science, probably one using a different data folder, holds the port. Run `claude-science stop` where that copy was started, or choose a different port. |
| A message mentioning `port 8000 is in use by another app — using port 8001 instead` | Claude Science started on the port it names. `claude-science url` prints both ports. Forward each one with that number on both sides. Or stop Claude Science and start it again with `--port`. |
| A message mentioning `daemon already running on port 8000` | Claude Science is already running. Run `claude-science url` for a fresh sign-in link, or `claude-science stop` to stop it. |
| The sign-in link shows an expired-link page | Links are single-use and valid for about three minutes. Run `claude-science url` on the server and open the fresh link; restarting with `claude-science stop` then `claude-science serve --no-browser` also prints one. |
| Sign-in stops at claude.ai | The redirect couldn't return through the tunnel (choose **Paste code instead**), your account is on the Free plan (an upgrade is required), or your Team or Enterprise organization hasn't [enabled Claude Science](/docs/claude-science/enable-claude-science) yet. |
| Interactive HTML previews render as static snapshots after a short delay (charts don't respond) | The tunnel isn't forwarding the preview port. Add the second `-L` forward for the preview port that `claude-science url` prints (8001 by default), with that number on both sides. |
| The browser can't reach `localhost:8000` | The tunnel isn't up; rerun the `ssh -L` command. If the tunnel is up, confirm Claude Science is running on the server with `claude-science status`. |
| The installer reports no binary for your platform | Claude Science on Linux needs x64 with glibc. arm64 servers and musl-based distributions such as Alpine aren't supported. |
