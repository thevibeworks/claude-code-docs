> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Core concepts

> A project groups related sessions and the artifacts they produce.

## Projects and sessions

A project groups related sessions and the artifacts they produce. Projects also let you set up custom instructions for Claude to read at the start of every session. Folder permissions you grant persist across sessions and apply to all projects.

A session is one conversation thread. Each session has its own workspace folder and multiple running kernels. From version 0.1.73, Claude Science is designed to keep Claude from opening another session's workspace files unless the current session came from that session through **Continue as a new session** or as a side chat. To use such files in the project's other sessions, have Claude first save them as [artifacts](https://claude.com/docs/claude-science/artifacts.md).

## Files stay on your computer

Claude reads files in place in the folders you grant, and its code can only read them, with exceptions on Windows (see [Sandbox](#sandbox)). Claude works on copies in the session's workspace folder, then saves finished files to **Read & write** folders.

Anthropic doesn't host or store your files; file content that Claude reads to answer a prompt is sent to Anthropic as part of the conversation, and Anthropic retains it as [How Claude Science works with your data](https://claude.com/docs/claude-science/how-claude-science-works-with-your-data.md) describes. If you sign in to Claude Science on a different computer, your files, artifacts, and conversation history don't follow you there. See [Use Claude Science on more than one computer](https://claude.com/docs/claude-science/multiple-computers.md) for what your account does carry between computers.

**Attach files** in the composer copies files to the app's local data folder, keeping them with the conversation.

> [!WARNING]
>
> Don't move, rename, or delete files inside \~/.claude-science directly. Doing so can break artifact links and version history. Manage artifacts through the app.

## Permission cards

A permission card appears in the conversation each time Claude needs a new kind of access. The card names exactly what's being requested. You can allow or deny each one. On a Mac or Linux, a folder's card starts on **Read-only**, even for write requests. With [auto mode](https://claude.com/docs/claude-science/auto-mode.md) on, Claude Science's own check can allow code, or a call to a remote or directory connector, without a card. If the check blocks a step or can't finish, a card asks you.

| Action | Card title | Scope options |
| - | - | - |
| Read or write a folder | Access `<folder>` on your computer? | Read-only or Read & write; persists until revoked |
| Save some kinds of files Claude doesn't save by itself, such as shell scripts, JSON, or archives, to a **Read & write** folder | Save this file into your folder? / Replace this file? / Make this folder? / Save a file that can't be shown / Replace a file with one that can't be shown | This file only; asked each time |
| Save `.py`, `.R`, or other source files to a **Read & write** folder | Allow Claude to save source files in this repo? / Allow Claude to save source files in this folder? | This file only, or that repo's or folder's source files for this session |
| Run code | Run Python code? / Run R code? / Run a shell command? / Run a PowerShell command? (Windows) / Install packages? | Once, This conversation, This project, or Global |
| Work in a **Read & write** folder too large to check for credential files (Linux) | This folder is too large to check fully / This folder changed past what was checked | Asked once per folder, and again when new or changed subfolders go unchecked |
| Reach a network host | Connect to `<target>`? | Persists until revoked |
| Use a connector tool | Use `<tool>`? | Once, This conversation, This project, or Global |
| Use a saved credential | Credentials | Once, This conversation, This project, or Global |
| Run a remote job | Run this job on `<host>`? / Start a Modal job? | Once, This conversation, This project, or Global |

Most standing grants are listed in **Settings > Permissions** and can be revoked there. Network hosts are listed in **Settings > Network**, where you can revoke them. Source-file grants aren't listed and end when the session ends, Claude Science restarts, or you revoke folder access. Claude Science can still ask about code using a saved credential despite a standing grant for code or credentials. See [What auto mode checks](https://claude.com/docs/claude-science/auto-mode.md#what-auto-mode-checks).

**Read & write** lets Claude save, change, and delete files in the folder, but code Claude runs can only read it, with exceptions on Windows (see [Sandbox](#sandbox)). When Claude overwrites a file there, Claude Science keeps the earlier version only in some cases, such as when another program may be writing it. Builds, package installs, and git writes there fail. See [Files in granted folders](https://claude.com/docs/claude-science/troubleshooting.md#files-in-granted-folders), [Environments in granted folders](https://claude.com/docs/claude-science/tools-and-environments.md#environments-in-granted-folders), and [Git in granted folders](https://claude.com/docs/claude-science/troubleshooting.md#git-in-granted-folders).

## Plans

Claude might choose to propose a plan before starting multi-step work. You approve the plan or iterate with Claude on refining it; plan text can't be edited directly. Approved plan steps appear in the conversation and are marked complete as work finishes.

## Sandbox

By default, Claude's code runs inside an operating-system sandbox on your computer, except steps you approve to run outside it, such as jobs on remote compute. The sandbox's network is deny-by-default: outbound connections go through a local proxy that allows only package managers, the scientific databases behind Featured connectors, and hosts you or your organization have approved.

The sandbox lets code write to these locations and, on macOS and Linux, nowhere else by default:

* Folders that Claude Science provides, such as the session's [workspace folder](#projects-and-sessions) and the project's [artifacts](https://claude.com/docs/claude-science/artifacts.md) folder
* Temporary storage, which is the shared `/tmp` folder on macOS and private folders on Linux and Windows

Granted folders aren't on this list. On macOS and Linux, code can only read them. On Windows, it can also write in a file or folder there whose own permissions let it, such as one that gives **ALL APPLICATION PACKAGES** write access. On Windows, a file or folder that code could write can keep that access when you move it into a granted folder or restore it with its old permissions. Make an ordinary copy in the granted folder instead of moving it. **Read & write** lets Claude Science save, change, and delete files there for Claude, outside the sandbox, under its own checks.

The sandbox is designed to block reading your home directory, except granted folders and those Claude Science needs to run code, such as the current session's workspace folder and saved tool results, [artifacts](https://claude.com/docs/claude-science/artifacts.md), and [conda environments](https://claude.com/docs/claude-science/tools-and-environments.md). Code can also read all projects' artifacts and, on Windows, all sessions' saved tool results, which can include copies of earlier messages from long conversations.

These rules limit what code can read, but they aren't a guarantee. Don't rely on the sandbox alone to protect sensitive files on your computer, including in your home directory, and keep Claude Science up to date, because new versions include sandbox fixes.

Outside your home directory, code can read these locations without a grant:

* **macOS**: most locations your account can read, such as `/Applications` and `/Users/Shared`, and the parts of other people's home folders that macOS lets your account read. Code isn't allowed to read external drives and network shares mounted under `/Volumes`, other than Claude Science's own folders if its data folder is on one. You can't grant folders there. Code can read a drive or network share that's mounted outside both `/Volumes` and your home directory, if your account can.
* **Linux**: system directories such as `/usr`, `/opt`, and `/nix`, and a fixed set of configuration files and folders in `/etc`. By default, code can't read other locations, apart from Claude Science's own folders, unless you grant them.
* **Windows**: locations that Windows makes readable to every sandboxed app, such as `C:\Windows` and `C:\Program Files`. Code can also read the environment variables saved for your Windows account, so don't store secrets such as API keys in them. Code may also be able to read and change files on some FAT and exFAT drives, even in folders you haven't granted, because such drives lack file permissions. **Settings > Permissions** lists the drives found. To protect files on one, move them to an NTFS drive (formatting a drive erases it) or, if you can, disconnect the FAT or exFAT drive before Claude works.

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
