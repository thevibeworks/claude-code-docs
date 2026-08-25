> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Glossary

> Claude Tag terms defined in one place. See agent identity, Access bundle, channel manager, connection, scope, Agent Proxy, routine, channel memory, environment, and session.

export const BetaNote = () => <Info>Claude Tag is in public beta. Features and behavior described here may change before general availability.</Info>;

<BetaNote />

## Access bundle

A named set of connections, [domain entries](/docs/claude-tag/admins/add-connections#add-a-domain), repository access, and rules that an Owner creates for Claude to use. Bundles attach to scopes, and one bundle can serve many scopes. See [Give Claude access](/docs/claude-tag/admins/add-connections).

## Agent identity

The service accounts Claude acts with: the Claude app in Slack, the Claude GitHub App on code, and the credentials an admin provisions for every other tool. See [How agent identity works](/docs/claude-tag/concepts/agent-identity).

## Agent Proxy

The network layer that injects credentials into Claude's outbound requests. The model and the sandbox are not given the key; Agent Proxy adds the credential at the network boundary when a request matches the rules an admin set. See [How agent identity works](/docs/claude-tag/concepts/agent-identity#agent-proxy).

## Channel manager

A member of your Claude organization whom an Owner has named to set up specific channels. For each channel assigned to them, a channel manager sets the default model, adds repositories their own GitHub account can write to, and manages credentials in the channel's own bundle, without holding the Owner role. See [Delegate channel setup to channel managers](/docs/claude-tag/admins/restrict-access#delegate-channel-setup-to-channel-managers).

## Channel memory

Facts Claude retains while working in a channel, including facts you told it to remember and notes it writes itself. Entries from public channels are shared across the workspace; entries from private channels are saved to that channel's own store. See [What Claude Tag remembers](/docs/claude-tag/users/memory).

## The earlier Claude in Slack

Claude Tag is the second generation of the Claude app in Slack:

|                | Legacy (the earlier Claude in Slack)        | New (Claude Tag)                                      |
| :------------- | :------------------------------------------ | :---------------------------------------------------- |
| Identity       | Each user links their own claude.ai account | One agent identity with org-level service credentials |
| Sessions       | Spawned per request                         | One persistent session per thread, shared             |
| Memory         | None                                        | Shared workspace memory plus private-channel memory   |
| Proactive work | None                                        | Routines and channel watching                         |

Your admin chooses which generation answers `@Claude` in a given channel, so two channels in the same workspace can work differently. See [Migrate from the earlier Claude in Slack](/docs/claude-tag/admins/restrict-access#migrate-from-the-earlier-claude-in-slack).

## Connection

A credential for one external service that Claude uses on the channel's behalf, like a Datadog API key or a GitHub App installation. Connections belong to the agent identity, not to any user, and are grouped into [Access bundles](#access-bundle) by an admin.

A connection is not a connector. A connector belongs to your personal claude.ai account. Claude cannot use your connectors in channels; it uses the channel's connections. The one exception is a DM, where it uses your own account instead; see [how DMs work in this model](/docs/claude-tag/concepts/agent-identity#direct-message-channels).

## Connector

A tool you add to your own claude.ai account, like Gmail, Google Drive, or a custom MCP server, listed under [Customize > Connectors](https://claude.ai/customize/connectors). Connectors are personal; in Slack they apply only in DMs. For the agent-side equivalent that works in channels, see [Connection](#connection).

## Environment

The sandboxed compute configuration a session runs in, including its network access setting. Environments used here must be scoped to the organization, not to an individual account, because channel sessions run with no user account attached.

## Plugin

A bundle of skills an Owner attaches to an Access bundle or scope, teaching Claude how to use a specific tool or follow a specific process. Anthropic provides plugins for common tools; you can add your own. See [Attach plugins](/docs/claude-tag/admins/add-connections#attach-plugins).

## Routine

A scheduled or run-once task Claude runs on its own, such as a daily digest or a channel watch. Anyone in a channel can ask Claude to set one up, list what's scheduled, or disable one. Routines run with the channel's connections, not the creator's.

Claude Code also has a feature named routines. Those run under an individual user's account; Claude Tag routines run under the agent identity.

## Rule

The match conditions Agent Proxy checks against each outbound request. A connection pairs one credential with the rule that decides when to inject it, and a request that matches the rule gets the credential attached at the boundary. A request that nothing allows (no rule, no domain entry, no [environment](#environment) network access setting) is blocked. See [Agent Proxy](/docs/claude-tag/concepts/agent-identity#agent-proxy).

## Scope

One of three levels Claude's settings can target: Default Slack access (the organization-wide root), one Slack workspace, or one channel (public or private). Scopes inherit downward, so a channel gets its workspace's settings plus any of its own. An Owner attaches [Access bundles](#access-bundle) and instructions at a scope. See [Attach the bundle to a scope](/docs/claude-tag/admins/attach-to-scope).

## Session

The unit of work behind one conversation. Each Slack thread binds to one persistent session, and anyone in the channel can continue it by replying in the thread. A channel where Claude works at the top level, outside threads, also carries one session for the channel itself, separate from every thread's. See [How Claude Tag works](/docs/claude-tag/concepts/how-it-works) and [Restart a stuck or wrong-context session](/docs/claude-tag/users/commands#restart-a-stuck-or-wrong-context-session).

## Related resources

* [How Claude Tag works](/docs/claude-tag/concepts/how-it-works): the scope, channel, and thread model in action
* [How agent identity works](/docs/claude-tag/concepts/agent-identity): how connection, scope, and Agent Proxy fit together when Claude runs a task
* [Set up Claude Tag](/docs/claude-tag/admins/setup-overview): where bundles, scopes, and connections get created in the console
