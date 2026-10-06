> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Glossary

> Claude Tag terms defined in one place, including agent identity, bundle, connector, personal connector, scope, Agent Proxy, routine, and session.

export const BetaNote = () => <Info>Claude Tag is in public beta. Features and behavior described here may change before general availability.</Info>;

<BetaNote />

## Agent identity

The service accounts Claude acts with: the Claude app in Slack, the Claude GitHub App on code, and the credentials an admin provisions for every other tool. See [How agent identity works](/docs/claude-tag/concepts/agent-identity).

## Agent Proxy

The network layer that injects credentials into Claude's outbound requests. The model and the sandbox are not given the key; Agent Proxy adds the credential at the network boundary when a request matches the rules an admin set. See [How agent identity works](/docs/claude-tag/concepts/agent-identity#agent-proxy).

<a id="access-bundle" />

## Bundle

A named set of connectors, repositories, [allowed domains](/docs/claude-tag/admins/add-connections#add-a-domain), plugins, and instructions that Claude uses for one kind of work, such as support triage. An Owner or a [Claude Tag admin](#claude-tag-admin) creates bundles on the **Bundles** tab under **Claude's access** at [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag), then adds the places where each one applies: all of Slack, a workspace, or a channel. One bundle can apply in many places, and an Owner can also apply one to every channel whose name matches a pattern. See [Give Claude access](/docs/claude-tag/admins/add-connections).

## Channel manager

A member of your Claude organization named to set up specific channels. For each channel assigned to them, a channel manager sets the default model, adds repositories their own GitHub account is an admin of, and manages credentials and plugins in the channel's own bundle, without holding the Owner role. See [Delegate channel setup to channel managers](/docs/claude-tag/admins/restrict-access#delegate-channel-setup-to-channel-managers).

## Channel memory

Facts Claude retains while working in a channel, including facts you told it to remember and notes it writes itself. Each channel keeps its own entries. From a public channel Claude can also save workspace notes, which it reads in every channel in the workspace. See [What Claude Tag remembers](/docs/claude-tag/users/memory).

## Claude Tag admin

A member of your Claude organization whose custom role includes the **Claude Tag Admin** permission, available on the Enterprise plan. A Claude Tag admin manages [bundles](#bundle), chooses where they apply, and edits workspace and channel settings, without holding the Owner role. A Claude Tag admin whose role also sets **Identity & Access** to **Can manage** can add and remove [channel managers](#channel-manager). See [Delegate Claude Tag administration](/docs/claude-tag/admins/restrict-access#delegate-claude-tag-administration).

## The earlier Claude in Slack

Claude Tag is the second generation of the Claude app in Slack:

| | Legacy (the earlier Claude in Slack) | New (Claude Tag) |
| :- | :- | :- |
| Identity | Each user links their own claude.ai account | One agent identity with org-level service credentials |
| Sessions | Spawned per request | One persistent session per thread, shared |
| Memory | None | Per-channel memory, plus workspace notes shared from public channels |
| Proactive work | None | Routines and channel watching |

Your admin chooses which generation answers `@Claude` in a given channel, so two channels in the same workspace can work differently. See [Migrate from the earlier Claude in Slack](/docs/claude-tag/admins/workspaces#turn-claude-tag-on-or-off-and-set-the-version-for-a-scope).

<a id="connection" />

## Connector

A service Claude Tag reaches with a credential of its own. An Owner or a [Claude Tag admin](#claude-tag-admin) adds connectors on the **Connectors** tab under **Claude's access**, and each connector holds one or more credentials, such as an API key for the service, that belong to the agent identity rather than to any user. To add a connector and choose where its credentials apply, see [Add a connector](/docs/claude-tag/admins/add-connections#add-a-connection). The [federated access](/docs/claude-tag/admins/federated-access/overview) pages and their console screens say **connection** for a gateway, cloud role, or authorization server Claude reaches with a token instead of a stored key.

A channel session uses the Claude Tag connectors that apply to its channel. Claude can also [use your personal connectors there](/docs/claude-tag/concepts/personal-connectors) for your own tasks, after you allow it. A one-to-one DM uses your own account instead, as [how DMs work in this model](/docs/claude-tag/concepts/agent-identity#direct-message-channels) describes.

## Environment

The sandboxed compute configuration a session runs in, including its network access setting. Environments used here must be scoped to the organization, not to an individual account, because channel sessions run with no user account attached.

## Personal connector

A tool you add to your own claude.ai account, like Gmail, Google Drive, or a custom MCP server, listed under [Customize > Connectors](https://claude.ai/customize/connectors). Personal connectors apply in your one-to-one DMs with Claude. Claude can also [use them in a channel](/docs/claude-tag/concepts/personal-connectors) for your own tasks, after you allow it. For the connectors an admin adds for Claude Tag, see [Connector](#connection).

## Plugin

A package of skills that teaches Claude how to use a specific tool or follow a specific process. An Owner or a [Claude Tag admin](#claude-tag-admin) adds a plugin to a bundle, or to all of Slack, a workspace, or a channel directly. Anthropic provides plugins for common tools; you can add your own. See [Attach plugins](/docs/claude-tag/admins/add-connections#attach-plugins).

## Routine

A scheduled or run-once task Claude runs on its own, such as a daily digest or a channel watch. Anyone in a channel can ask Claude to set one up, list what's scheduled, or disable one. Routines run with the channel's access, not the creator's.

Claude Code also has a feature named routines. Those run under an individual user's account; Claude Tag routines run under the agent identity.

## Rule

The match conditions Agent Proxy checks against each outbound request. Each credential has a rule that decides when to inject it, and a request that matches the rule gets the credential attached at the boundary. A request that nothing allows (no rule, no domain entry, no [environment](#environment) network access setting) is blocked. See [Agent Proxy](/docs/claude-tag/concepts/agent-identity#agent-proxy).

## Scope

One of three levels Claude's settings can target: all of Slack (the **Slack** page, the organization-wide root), one Slack workspace, or one channel (public or private). Scopes inherit downward, so a channel gets its workspace's settings plus any of its own. In Claude Tag admin settings, all of Slack, each workspace, and each channel have their own pages, which you open from the **Channels** tab under **Claude's access**. An Owner or a [Claude Tag admin](#claude-tag-admin) adds [bundles](#bundle), connectors, plugins, and instructions there. See [Attach the bundle to a scope](/docs/claude-tag/admins/attach-to-scope).

## Session

The unit of work behind one conversation. Each Slack thread binds to one persistent session, and anyone in the channel can continue it by replying in the thread. A channel where Claude works at the top level, outside threads, also carries one session for the channel itself, separate from every thread's. See [How Claude Tag works](/docs/claude-tag/concepts/how-it-works) and [Restart a stuck or wrong-context session](/docs/claude-tag/users/commands#restart-a-stuck-or-wrong-context-session).

## Related resources

* [How Claude Tag works](/docs/claude-tag/concepts/how-it-works): the scope, channel, and thread model in action
* [How agent identity works](/docs/claude-tag/concepts/agent-identity): how connectors, scopes, and Agent Proxy fit together when Claude runs a task
* [Set up Claude Tag](/docs/claude-tag/admins/setup-overview): where bundles and connectors get set up in Claude Tag admin settings
