> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Core concepts

> A project groups related sessions and the artifacts they produce.

## Projects and sessions

A project groups related sessions and the artifacts they produce. Projects also let you set up custom instructions for Claude to read at the start of every session. Folder permissions you grant persist across sessions within a project.

A session is one conversation thread. Each session has its own workspace folder and multiple running kernels.

## Files stay on your computer

Claude reads and writes files in place, in the folders you grant. Anthropic doesn't host or store your files; file content that Claude reads to answer a prompt is sent to Anthropic as part of the conversation, and Anthropic retains it as [How Claude Science works with your data](/docs/claude-science/how-claude-science-works-with-your-data) describes. If you sign in to Claude Science on a different computer, your files, artifacts, and conversation history don't follow you there. See [Use Claude Science on more than one computer](/docs/claude-science/multiple-computers) for what your account does carry between computers.

The one exception to working in place is **Attach files** in the composer: attached files are copied into the application's local data folder so they stay with the conversation.

<Warning>
  Don't move, rename, or delete files inside \~/.claude-science directly. Doing so can break artifact links and version history. Manage artifacts through the app.
</Warning>

## Permission cards

A permission card appears in the conversation each time Claude needs a new kind of access. The card names exactly what's being requested. You can allow or deny each one.

| Action                 | Card title                                                  | Scope options                                     |
| ---------------------- | ----------------------------------------------------------- | ------------------------------------------------- |
| Read or write a folder | Access `<folder>` on your computer?                         | Read-only or Read & write; persists until revoked |
| Run code               | Run Python code? / Run a shell command? / Install packages? | Once or Always                                    |
| Reach a network host   | Connect to `<target>`?                                      | Persists until revoked                            |
| Use a connector tool   | Use `<tool>`?                                               | Once, This conversation, This project, or Global  |
| Run a remote job       | Run this job on `<host>`? / Start a Modal job?              | Once, This conversation, This project, or Global  |

All standing grants are listed in Settings > Permissions and can be revoked there.

## Plans

Claude might choose to propose a plan before starting multi-step work. You approve the plan or iterate with Claude on refining it; plan text can't be edited directly. Approved plan steps appear in the conversation and are marked complete as work finishes.

## Sandbox

All code Claude writes runs inside an operating-system sandbox on your computer. The sandbox can read and write only the workspace and the folders you've granted. Its network is deny-by-default: outbound connections go through a local proxy that allows only package managers, the scientific databases behind Featured connectors, and hosts you've approved.

## Delegation

**Delegation** lets Claude split a request into independent tracks that run in parallel. Turn it on or off per session in the session settings menu; your last choice becomes the default for new sessions. When work splits, a marker appears in the conversation for each track with a status indicator. Click a marker to open that track's transcript. **Stop** ends the whole session; individual tracks can't be stopped separately.

## Memory

Memory lets Claude save short facts about you, your projects, and your files across sessions. You choose whether memory is on during first-time setup, and you can change it anytime in Settings > Memory.

Saved facts are stored in the app's local database on your computer; they aren't synced to Anthropic. The Memory settings page lists every saved fact. You can edit, delete, add, or clear facts there. A per-session toggle in the session settings menu turns memory off for that session only.

## Composer shortcuts

* `@` inserts an artifact or uploaded file by name
* `#` inserts a past session by title
* `/` inserts a skill
