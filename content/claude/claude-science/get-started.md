> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get started

> Install Claude Science on macOS or Linux, sign in with your Claude account, and run your first analysis.

## Install

macOS: Download the installer from claude.com/product/claude-science and double-click to install. On first launch, the app sets up its runtime and starter Python and R environments, which takes a few minutes, then opens a new tab in your default browser. If no browser tab appears, choose Open from the menu bar icon.

<Note>
  Although Claude Science opens in a browser tab, it's a local application, not a website: there's no public URL to visit. Open it from the application itself, with the menu bar icon on macOS or the `claude-science` command on Linux. On a remote server, the sign-in link reaches your browser through an SSH tunnel; see [Run on a remote Linux server](/docs/claude-science/run-on-remote-linux-server).
</Note>

Linux: install the sandbox dependencies, then run the installer. The sandbox needs bubblewrap 0.8.0 or later and socat, and installing them takes administrator (`sudo`) access; if you don't have it, ask your system administrator to install them.

* Ubuntu or Debian: `sudo apt-get update && sudo apt-get install -y curl bubblewrap socat`
* Fedora or RHEL: `sudo dnf install -y curl bubblewrap socat`
* Arch: `sudo pacman -S curl bubblewrap socat`

Ubuntu 24.04's repositories carry a new enough bubblewrap and Ubuntu 22.04's don't; on any distribution, confirm with `bwrap --version` that the installed version is 0.8.0 or later before you start Claude Science.

```bash theme={null}
curl -fsSL https://claude.ai/install-claude-science.sh | bash
```

```bash theme={null}
claude-science serve
```

First launch prints a local URL right away, then continues setting up its starter Python and R environments. To run Claude Science on a remote server and use it from your computer, see [Run on a remote Linux server](/docs/claude-science/run-on-remote-linux-server).

## Sign in and complete setup

When the app opens in your browser, sign in with your Claude account. If the OAuth redirect can't return to the app (for example, through an SSH tunnel), use the Paste a code option on the sign-in screen instead. No API key is required.

After sign-in, a setup wizard walks you through enabling connectors and skills and setting which websites Claude can access. You can change these at any time in Settings.

<Note>
  Claude Science keeps all of its data in a single folder (`~/.claude-science`) in your home directory; on Linux, the `claude-science` command itself installs to `~/.local/bin`. It doesn't modify your existing conda installation, R libraries, or shell configuration.
</Note>

<Warning>
  Deleting that folder removes all projects, artifacts, and conversation history. Deleting the folder and the application removes Claude Science entirely.
</Warning>

## Run your first analysis

* Open the Example project, or create a new one.
* Start a conversation. Reference a folder on your computer by typing its path or using the @ picker in the composer.
* Review the folder-access card when it appears and choose whether to allow it.
* Review the code-execution card when Claude proposes running code and choose whether to allow it.
* Results appear as artifacts in the Files panel.

## Troubleshooting first launch

* macOS says the application isn't supported, or the app icon appears crossed out: the download page picked the build for the wrong processor. Return to the download page and choose Mac (Intel) or Mac (Apple Silicon) to match your Mac. To check which you have, open the Apple menu, choose About This Mac, and look at the Chip or Processor line.
* No browser tab appeared: on macOS, choose Open from the menu bar icon. On Linux, copy the printed URL into a browser on the same machine, or run `claude-science url` to print a fresh one.
* Linux refuses to start: a sandbox dependency is missing (install bubblewrap and socat as shown in the Install section), too old, or blocked. Check your bubblewrap version with `bwrap --version`, then match the error message to its fix in the [Linux troubleshooting table](/docs/claude-science/run-on-remote-linux-server#troubleshooting).
* Projects from another computer don't appear: by design, Claude Science keeps your work on the computer where it's installed, so each computer starts with its own projects. Your earlier projects are still on the other computer. See [Use Claude Science on more than one computer](/docs/claude-science/multiple-computers).
* Sign-in stops at claude.ai: your account is on the Free plan (upgrade required), the redirect couldn't return (use Paste a code), or your Team or Enterprise organization hasn't [enabled Claude Science](/docs/claude-science/enable-claude-science) yet.
