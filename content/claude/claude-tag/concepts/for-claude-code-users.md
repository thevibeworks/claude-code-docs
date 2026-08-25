> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Claude Tag for Claude Code users

> Which parts of a Claude Code setup carry into Claude Tag, which move to admin settings, and how Slack threads map to sessions.

export const BetaNote = () => <Info>Claude Tag is in public beta. Features and behavior described here may change before general availability.</Info>;

<BetaNote />

Claude Tag runs the same engine as Claude Code. When you tag `@Claude` in Slack with a task, a session starts in a sandbox that Anthropic hosts and your organization configures, not on your machine. That sandbox is the same managed compute behind [Claude Code on the web](https://code.claude.com/docs/en/web-quickstart), described in [Compute and the sandbox](/docs/claude-tag/concepts/security-and-data#compute-and-the-sandbox).

If you use Claude Code on the web, a session works the way a web session does, from a fresh clone of your repository rather than from files on your machine. The configuration you checked into that repository, such as `CLAUDE.md`, hooks, and skills, applies in the session as it does in a web session.

If you run Claude Code in your terminal, the settings on your own machine don't reach a session, because the session runs in the sandbox and can't read your machine. For most of those settings, an admin sets a channel-wide counterpart instead, and a few have no counterpart at all. This page shows what happens when a session starts, which admin settings replace your local ones, and how Slack threads map to sessions.

## What happens when a session starts

A session begins with a fresh sandbox and no repository checked out. Your repository's Claude Code configuration takes effect only after Claude clones the repository, which happens when your message names a repository that an admin has [granted to the channel](/docs/claude-tag/admins/configure-github#grant-repository-access).

| Step                                    | What applies                                                                                                                                                                          |
| :-------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| You tag `@Claude` with a task           | Your message is the task, and Claude starts work in a sandbox with no repository                                                                                                      |
| Your message names a granted repository | Claude clones it into the sandbox                                                                                                                                                     |
| The clone completes                     | `CLAUDE.md`, `.claude/CLAUDE.md`, `.claude/rules/*.md`, and the skills in `.claude/skills/` [load into the session](/docs/claude-tag/admins/configure-github#what-loads-from-a-repository) |
| Claude works on the task                | Hooks defined in the repository's `.claude/settings.json` run as they do under Claude Code                                                                                            |

### How hooks run in the sandbox

Hooks run inside the sandbox, and every session runs on the same standard sandbox image, no matter which repository it clones. If a hook calls a command that the image doesn't include, add an install step for it to the repository's `CLAUDE.md`, as described in [Install project dependencies](/docs/claude-tag/admins/configure-github#install-project-dependencies).

## Local settings versus admin settings

A session reads configuration from your repository, not from your machine. The `CLAUDE.md`, hooks, and skills you checked into the repository load when Claude clones it, as described in [What happens when a session starts](#what-happens-when-a-session-starts).

The settings on your machine never load into a session, because a session runs in the sandbox and can't read your machine. That includes your `~/.claude` directory, your personal `settings.json`, your shell environment, and the MCP servers you configured locally. They still apply when you run Claude Code in your terminal.

### Admin counterparts for local settings

The table shows what takes the place of each setting from your machine. Where a counterpart exists, an admin sets it for the whole channel.

| Claude Code setting on your machine                  | In Claude Tag                                                                                                                                                                                                                                                                                        |
| :--------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `/model`                                             | An admin sets the [default model per channel](/docs/claude-tag/admins/customize#choose-the-model-for-a-scope), and you can [switch models in a thread](/docs/claude-tag/users/models)                                                                                                                          |
| Effort level                                         | Not configurable. Sessions run at the model's default effort.                                                                                                                                                                                                                                        |
| MCP servers in `.mcp.json`                           | Not loaded, even when `.mcp.json` is checked into the repository. A session reaches external services only through the [connections an admin set for the channel](/docs/claude-tag/admins/add-connections), and each connection holds that service's credentials.                                         |
| Secrets and API keys in your environment             | An admin provisions them as channel connections. The raw key never enters the sandbox. It is [added to requests at the network layer](/docs/claude-tag/concepts/agent-identity#agent-proxy).                                                                                                              |
| Environment variables and a personal `settings.json` | No counterpart. Every session runs on the same standard sandbox image, so there is no per-person environment to customize. Put non-secret setup in `CLAUDE.md` as [install steps](/docs/claude-tag/admins/configure-github#install-project-dependencies), and ask an admin to add secrets as connections. |
| A setup script for your workspace                    | No counterpart. Use `CLAUDE.md` install steps instead.                                                                                                                                                                                                                                               |
| Permission prompts                                   | Sessions run in auto mode, where Claude's permission checker reviews each action and can stop it. An admin pre-approves routine actions with [auto mode allow rules](/docs/claude-tag/admins/customize#auto-mode-allow-rules) instead of you approving in the moment.                                     |

To change what a session can reach, ask an admin to [add a connection](/docs/claude-tag/admins/add-connections). The change applies to every session in the channel.

## How Slack threads map to sessions

You start a session by tagging `@Claude` in a thread with a task, and that session gets its own sandbox. Each reply in the same thread continues the session, so there is no `--continue` or `/resume` to run, and a session stays attached to the thread it started in. See [the lifecycle of a request](/docs/claude-tag/concepts/how-it-works#lifecycle-of-a-request) for what happens between replies.

Each thread is its own session with its own sandbox, so run parallel tasks in separate threads the way you would in separate terminal tabs. The sandbox is released after a quiet period, but the conversation stays in the thread, and a later reply continues the session. See [what survives between replies](/docs/claude-tag/concepts/how-it-works#what-survives-between-replies).

## Whose credentials a session uses

Claude Code acts with your credentials. What a session acts with depends on whether you tag Claude in a channel or in a direct message.

### In a channel

In a channel, Claude acts with credentials of its own, service accounts that [an admin provisions](/docs/claude-tag/concepts/agent-identity#channel-sessions). A pull request comes from the Claude GitHub App rather than from you, and a query against a connected service runs with the channel's credentials no matter who asked. Access is set per channel, not per person.

### In a direct message

A [direct message](/docs/claude-tag/concepts/agent-identity#direct-message-channels) runs on your own claude.ai account, with the connectors you added to that account rather than the connections an admin set for the channel, so a DM is the closest match to a Claude Code session on your own credentials.

## Steer a session in the thread

Where you would interrupt Claude Code and edit a file or reprompt, [reply in the thread](/docs/claude-tag/concepts/how-it-works#reply-in-the-thread-to-steer). Corrections and added constraints land as messages, and Claude folds them into the running task.

### Keep instructions in channel memory

For instructions that should persist beyond one thread, use channel memory, the instructions Claude keeps for one channel and reads in every session there. Keep repository conventions in `CLAUDE.md`. Put channel conventions in memory by telling Claude to remember them:

```text theme={null}
@Claude remember for this channel: reports go out as tables
```

See [What Claude remembers](/docs/claude-tag/users/memory) for how memory is scoped and how to correct it.

## Claude Tag versus a bot you build on the API

A Slack bot you build on the Claude API is software your team writes and hosts. It calls the API with your key, holds its own Slack tokens, and has the tools and memory you code into it.

Claude Tag is Anthropic's hosted Slack app. It takes care of the parts you would otherwise build.

* **Hosting.** Each thread gets a Claude Code session in a sandbox Anthropic runs, or in the [environment](/docs/claude-tag/concepts/glossary#environment) your organization pins, under an [agent identity](/docs/claude-tag/concepts/agent-identity) of its own.
* **Credentials.** An admin gives Claude [connections](/docs/claude-tag/admins/add-connections) to your tools, and [Agent Proxy](/docs/claude-tag/concepts/agent-identity#agent-proxy) attaches the credentials at the network boundary, outside the sandbox.
* **Customization.** [Custom instructions](/docs/claude-tag/admins/attach-to-scope#add-custom-instructions), [channel memory](/docs/claude-tag/users/memory), and [routines](/docs/claude-tag/users/proactivity) are built in.
* **Governance and billing.** [Access controls](/docs/claude-tag/admins/restrict-access) and spend limits are set in claude.ai admin settings, and usage is [billed to the organization's usage balance](/docs/claude-tag/overview#billing-and-spend-limits).

## Related resources

* [How Claude Tag works](/docs/claude-tag/concepts/how-it-works): the session model this page maps your setup onto
* [How agent identity works](/docs/claude-tag/concepts/agent-identity): why a channel uses the agent's access and a DM uses yours
* [Claude Tag settings map](/docs/claude-tag/concepts/settings-map): where each setting your organization owns is set
* [Configure GitHub access](/docs/claude-tag/admins/configure-github): what loads from a repository and how installs work in the sandbox
