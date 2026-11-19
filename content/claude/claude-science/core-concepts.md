> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Core concepts

> A project groups related sessions and the artifacts they produce.

## Projects and sessions

A project groups related sessions and the artifacts they produce. Projects also let you set up custom instructions for Claude to read at the start of every session. Folder permissions you grant persist across sessions and apply to all projects.

A session is one conversation thread. Each session has its own workspace folder and multiple running kernels.

## Files stay on your computer

Claude reads and writes files in place, in the folders you grant. Anthropic doesn't host or store your files; file content that Claude reads to answer a prompt is sent to Anthropic as part of the conversation, and Anthropic retains it as [How Claude Science works with your data](https://claude.com/docs/claude-science/how-claude-science-works-with-your-data.md) describes. If you sign in to Claude Science on a different computer, your files, artifacts, and conversation history don't follow you there. See [Use Claude Science on more than one computer](https://claude.com/docs/claude-science/multiple-computers.md) for what your account does carry between computers.

The one exception to working in place is **Attach files** in the composer: attached files are copied into the application's local data folder so they stay with the conversation.

> [!WARNING]
>
> Don't move, rename, or delete files inside \~/.claude-science directly. Doing so can break artifact links and version history. Manage artifacts through the app.

## Permission cards

A permission card appears in the conversation each time Claude needs a new kind of access. The card names exactly what's being requested. You can allow or deny each one. With [auto mode](https://claude.com/docs/claude-science/auto-mode.md) on, Claude Science's own check can allow code, or a call to a remote or directory connector, without a card. If the check blocks a step or can't finish, a card asks you.

| Action | Card title | Scope options |
| - | - | - |
| Read or write a folder | Access `<folder>` on your computer? | Read-only or Read & write; persists until revoked |
| Run code | Run Python code? / Run R code? / Run a shell command? / Run a PowerShell command? (Windows) / Install packages? | Once, This conversation, This project, or Global |
| Work in a write-access folder too large to check for credential files (Linux) | This folder is too large to check fully / This folder changed past what was checked | Asked once per folder, and again when new or changed subfolders go unchecked |
| Reach a network host | Connect to `<target>`? | Persists until revoked |
| Use a connector tool | Use `<tool>`? | Once, This conversation, This project, or Global |
| Use a saved credential | Credentials | Once, This conversation, This project, or Global |
| Run a remote job | Run this job on `<host>`? / Start a Modal job? | Once, This conversation, This project, or Global |

Most standing grants are listed in **Settings > Permissions** and can be revoked there. Network hosts are listed in **Settings > Network**, where you can revoke them.

On Linux, a uv, conda, mamba, or pixi environment in a folder you've granted **Read & write** can still be read-only to Claude. See [Environments in granted folders](https://claude.com/docs/claude-science/tools-and-environments.md#environments-in-granted-folders).

## Plans

Claude might choose to propose a plan before starting multi-step work. You approve the plan or iterate with Claude on refining it; plan text can't be edited directly. Approved plan steps appear in the conversation and are marked complete as work finishes.

## Sandbox

By default, Claude's code runs inside an operating-system sandbox on your computer, except steps you approve to run outside it, such as jobs on remote compute. The sandbox's network is deny-by-default: outbound connections go through a local proxy that allows only package managers, the scientific databases behind Featured connectors, and hosts you or your organization have approved.

The sandbox lets code write to these locations and, on macOS and Linux, nowhere else by default:

* Folders where you've [granted](#permission-cards) **Read & write** access
* Folders that Claude Science provides, such as the session's [workspace folder](#projects-and-sessions) and the project's [artifacts](https://claude.com/docs/claude-science/artifacts.md) folder
* Temporary storage, which is the shared `/tmp` folder on macOS and private folders on Linux and Windows

The sandbox is designed to block reads of your home directory, apart from folders you've granted and folders that Claude Science needs to run the code, such as workspace folders, [artifacts](https://claude.com/docs/claude-science/artifacts.md), saved tool results, and [conda environments](https://claude.com/docs/claude-science/tools-and-environments.md). These folders can belong to other sessions and projects:

* Code can read the artifacts of all your projects and the saved tool results of all your sessions, which can include copies of earlier messages from long conversations.
* On macOS, code can also read the workspace folders of all your sessions.

These rules limit what code can read, but they aren't a guarantee. Don't rely on the sandbox alone to protect sensitive files on your computer, including in your home directory, and keep Claude Science up to date, because new versions include sandbox fixes.

Outside your home directory, code can read these locations without a grant:

* **macOS**: most locations your account can read, such as `/Applications` and `/Users/Shared`, and the parts of other people's home folders that macOS lets your account read. Code isn't allowed to read external drives and network shares mounted under `/Volumes`, other than Claude Science's own folders if its data folder is on one. You can't grant folders there. Code can read a drive or network share that's mounted outside both `/Volumes` and your home directory, if your account can.
* **Linux**: system directories such as `/usr`, `/opt`, and `/nix`, and a fixed set of configuration files and folders in `/etc`. By default, code can't read other locations, apart from Claude Science's own folders, unless you grant them.
* **Windows**: locations that Windows makes readable to every sandboxed app, such as `C:\Windows` and `C:\Program Files`. Code can also read the environment variables saved for your Windows account, so don't store secrets such as API keys in them.

## Delegation

**Delegation** lets Claude split a request into independent tracks that run in parallel. Turn it on or off per session in the session settings menu; your last choice becomes the default for new sessions. When work splits, a marker appears in the conversation for each track with a status indicator. Click a marker to open that track's transcript. **Stop** ends the whole session; individual tracks can't be stopped separately.

## Memory

Memory lets Claude save short facts about you, your projects, and your files across sessions. You choose whether memory is on during first-time setup, and you can change it anytime in Settings > Memory.

Saved facts are stored in the app's local database on your computer; they aren't synced to Anthropic. The Memory settings page lists every saved fact. You can edit, delete, add, or clear facts there. A per-session toggle in the session settings menu turns memory off for that session only.

Facts Claude recalls for a session are sent to Anthropic as part of that session's conversation, and Anthropic retains them as [How Claude Science works with your data](https://claude.com/docs/claude-science/how-claude-science-works-with-your-data.md) describes. On Team and Enterprise plans, your organization's admin can turn memory off for the organization. Memory is then off for you whatever you chose, and your saved facts stay on your computer, where you can still review and delete them (see [Memory](https://claude.com/docs/claude-science/admin-controls.md#memory) in the admin controls).

## Composer shortcuts

* `@` inserts an artifact or uploaded file by name
* `#` inserts a past session by title
* `/` inserts a skill
