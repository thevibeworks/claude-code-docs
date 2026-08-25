> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# How agent identity works

> Claude Tag acts under its own service accounts in Slack channels, not as you. See how channel access is bounded, how credentials reach it, and why DMs differ.

export const BetaNote = () => <Info>Claude Tag is in public beta. Features and behavior described here may change before general availability.</Info>;

<BetaNote />

Claude Tag's identity depends on where you message it.

In Slack channels, Claude acts with its own service accounts, rather than as a specific user. An organization Owner [provisions this identity during setup](/docs/claude-tag/admins/setup-overview), so it arrives with its own account in each system it works in: the Claude app in Slack, the Claude GitHub App on GitHub, and a service account in every other connected tool. Actions it takes are attributed to those accounts; for example, posts come from the Claude app and pull requests show the Claude GitHub App as the author.

In direct messages (DMs) between a user and `@Claude`, the provisioned identity does not apply. DMs are one-to-one only; group DMs aren't supported. A DM has no channel to scope it to, so a DM session runs on [the individual's own claude.ai account](#direct-message-channels) instead, with their personal connectors. GitHub is the exception in attribution: a pull request opened from a DM is authored by the Claude GitHub App, the same as in channels, though the session can only work with repositories connected on that user's own account. Owners can disable DMs organization-wide; see [Allow or disable direct messages](/docs/claude-tag/admins/restrict-access#allow-or-disable-direct-messages).

<Note>
  How Claude behaves in channels (its standing instructions, plugins, and channel memory) is configured separately from its identity; see [custom instructions](/docs/claude-tag/admins/attach-to-scope#add-custom-instructions), [plugins](/docs/claude-tag/admins/add-connections#attach-plugins), and [memory](/docs/claude-tag/users/memory) for more information.
</Note>

## Channel sessions

When Claude works on a channel task, three systems are involved:

* The ask happens in your Slack workspace, when a user tags Claude to do something or a scheduled task starts.
* The work Claude does runs in a sandbox on Anthropic's infrastructure, with nothing installed in your network.
* The agent's credentials for any additional connections, such as GitHub or a data warehouse, reach those systems to pull the required information. An organization Owner sets up those credentials as part of [provisioning the identity](/docs/claude-tag/admins/setup-overview#setup-steps).

The diagram below traces one request through this process.

<img className="block dark:hidden" src="https://mintcdn.com/claude-ai/5JFKyLlO7sHMMf5J/images/claude-tag/diagrams/request-path.svg?fit=max&auto=format&n=5JFKyLlO7sHMMf5J&q=85&s=e8776cf0edd1f3ec912b9b044c9cc838" alt="Diagram showing the request path across three zones. A task mentioned in your Slack workspace runs in a session sandbox on Anthropic's infrastructure, one sandbox per thread, holding no credentials. Outbound requests pass to Agent Proxy, which injects the credential drawn from the credential store; a request matching no rule is blocked. Credentialed requests reach your systems, like GitHub, a data warehouse, monitoring, or any HTTP API. A dashed return path shows results posting back in the thread, as Claude." width="1000" height="440" data-path="images/claude-tag/diagrams/request-path.svg" />

<img className="hidden dark:block" src="https://mintcdn.com/claude-ai/5JFKyLlO7sHMMf5J/images/claude-tag/diagrams/request-path-dark.svg?fit=max&auto=format&n=5JFKyLlO7sHMMf5J&q=85&s=a2ed5f3270989c3ed3d9b9a78a72bff0" alt="Diagram showing the request path across three zones. A task mentioned in your Slack workspace runs in a session sandbox on Anthropic's infrastructure, one sandbox per thread, holding no credentials. Outbound requests pass to Agent Proxy, which injects the credential drawn from the credential store; a request matching no rule is blocked. Credentialed requests reach your systems, like GitHub, a data warehouse, monitoring, or any HTTP API. A dashed return path shows results posting back in the thread, as Claude." width="1000" height="440" data-path="images/claude-tag/diagrams/request-path-dark.svg" />

<Steps>
  <Step title="Tag Claude in a channel">
    A user asks Claude to chart last week's signups or fix a deploy test. The task gets a session in a thread under the message.
  </Step>

  <Step title="The session sandbox starts">
    Claude does the work in an isolated environment Anthropic builds for this thread, reading files, writing documents, and running code. The credentials you provision are not placed in the sandbox; they stay in the credential store and are injected at the proxy.
  </Step>

  <Step title="The request crosses Agent Proxy">
    When the work needs something outside the sandbox, like calling the GitHub API or querying a warehouse, the request crosses Agent Proxy, the network boundary between the sandbox and everything else. Agent Proxy checks it against the rules an admin configured, and decides whether it proceeds and what credential, if any, travels with it.
  </Step>

  <Step title="Agent Proxy attaches a credential">
    A matching credential comes from the credential store, where an admin's [connections](/docs/claude-tag/admins/add-connections) are kept. Once saved, a credential is never displayed again; Agent Proxy retrieves it only at the moment of injection and attaches it to the request at the boundary, so the model and the sandbox itself are not given the key.
  </Step>

  <Step title="The result posts back, as Claude">
    The credentialed request reaches your system, like GitHub or the warehouse, and the result returns to the thread.
  </Step>
</Steps>

### Agent Proxy

For each outbound request from the sandbox, Agent Proxy checks the destination against three allow layers. A request goes through if any one of them allows it; a host that none of them allows is blocked.

| When the destination                                                                                                                                                             | Result                                                                                                                                               |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------- |
| Matches a connection's rule, its [allowed websites](/docs/claude-tag/admins/add-connections#set-allowed-websites)                                                                     | The proxy attaches that connection's credential and forwards the request. The credential stays at the proxy; the model and sandbox are not given it. |
| Is on the [bundle](/docs/claude-tag/concepts/glossary#access-bundle)'s [Domains list](/docs/claude-tag/admins/add-connections#allow-a-host-without-a-credential) but matches no connection | The proxy forwards the request without a credential.                                                                                                 |
| Is allowed by the network access setting of the [environment](/docs/claude-tag/concepts/glossary#environment) the [scope](/docs/claude-tag/concepts/glossary#scope)'s sessions run on      | The proxy forwards the request without a credential.                                                                                                 |
| Matches none of these                                                                                                                                                            | The proxy blocks the request.                                                                                                                        |

A new environment's network access level defaults to Trusted access, so a fresh setup can reach a documented set of package registries and developer hosts before an admin has configured anything. The [cloud environments documentation](https://code.claude.com/docs/en/cloud-environments#default-allowed-domains) lists the covered hosts. To narrow that default, pin an environment with a stricter level, such as No access.

The same rules apply to code Claude runs in the sandbox, like `curl` or a `fetch` call: a request is blocked unless its host is allowed by one of the layers above.

Agent Proxy carries HTTP and HTTPS only. A protocol that isn't HTTP, such as SSH or a database's native wire protocol, can't cross the proxy even to an allowed host.

Nothing is installed inside your network. Your systems see only requests authenticated with the credentials Agent Proxy attached. For the endpoints and addresses your network team may need to allowlist, see [Network requirements](/docs/claude-tag/admins/network-requirements).

### How a host gets allowed

A host that none of the three layers above allows is blocked, and Claude names the blocked host in the thread so an admin can add it; see [Give Claude access to your tools](/docs/claude-tag/admins/add-connections).

### Web search vs. network requests

Claude can search the web from a channel without any Domains entry. Web search is [Anthropic's built-in web search tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool), which runs on Anthropic's servers, not code running in the channel's sandbox.

The sandbox sends nothing new for a search. Search requests travel to Anthropic the same way the session's model traffic already does, and the searching happens server-side. The [Agent Proxy](#agent-proxy) rules don't apply to web search; fetching a page or calling a service from the sandbox is an outbound network request and follows them.

Searching and opening a page are different actions. A search returns content from the pages it matches, which Claude reads and cites, so it can answer from a page that search surfaced. Opening a URL, whether one you pasted or one a search returned, is a fetch from the sandbox, and the host needs an allow layer. That is why Claude can quote a page it found through search and still report that it can't open the same link.

The web search capability setting in your organization's claude.ai admin settings governs claude.ai chat; it doesn't govern Claude Tag sessions, in channels or DMs. If Claude reports that it can't reach a host from a channel, the fix is a [domain entry](/docs/claude-tag/admins/add-connections#add-a-domain) or the scope's [environment](/docs/claude-tag/concepts/glossary#environment), not that setting.

### Agent access

What Claude can reach in a channel comes from the [Access bundles](/docs/claude-tag/admins/add-connections) an admin attached to that channel's scope. Anyone in the channel gets the same capability, and the same request can do more in `#platform-eng` than in a general channel.

This design has four consequences.

* **Configure once.** Everyone in the scope can use it immediately.
* **Predictability.** What Claude can do never changes based on who asked.
* **Personal connectors apply in DMs.** A shared channel uses only the service-account connections an admin attached, not connectors on anyone's claude.ai account.
* **Clean audit.** Actions in connected tools show up under a service account your security team already knows how to reason about.

That service-account identity is also how Claude appears wherever it acts. In Slack, it posts as the Claude app. On GitHub, commits and pull requests show the Claude GitHub App, and pull requests link back to the Slack thread they came from. In every other connected service, actions appear under the service account an admin provisioned, in that service's audit log.

## Direct message channels

A DM with Claude works differently from a channel. There is no scope to attach an identity to, so a DM session runs with your own claude.ai account instead, the same way a Claude Code session on the web does, using your own connectors and credentials, with results attributed to you (pull requests excepted; the Claude GitHub App authors those from DMs too). The diagram contrasts with the channel path above; the sandbox is the same engine, but everything around it is yours.

<img className="block dark:hidden" src="https://mintcdn.com/claude-ai/5JFKyLlO7sHMMf5J/images/claude-tag/diagrams/dm-identity.svg?fit=max&auto=format&n=5JFKyLlO7sHMMf5J&q=85&s=d4089034f46e4a760f9fac9d36a689cc" alt="Diagram showing how a DM session reaches your systems. A message to Claude in a direct message runs in a session sandbox on Anthropic's infrastructure, the same engine as a channel session, but it runs with your identity. From there it reaches your systems through your own connectors and accounts, like GitHub or Drive, using your own credentials. A dashed return path shows results posting back in the DM, as Claude." width="1000" height="270" data-path="images/claude-tag/diagrams/dm-identity.svg" />

<img className="hidden dark:block" src="https://mintcdn.com/claude-ai/5JFKyLlO7sHMMf5J/images/claude-tag/diagrams/dm-identity-dark.svg?fit=max&auto=format&n=5JFKyLlO7sHMMf5J&q=85&s=a3ca3c8aa926704742402882f4345b1b" alt="Diagram showing how a DM session reaches your systems. A message to Claude in a direct message runs in a session sandbox on Anthropic's infrastructure, the same engine as a channel session, but it runs with your identity. From there it reaches your systems through your own connectors and accounts, like GitHub or Drive, using your own credentials. A dashed return path shows results posting back in the DM, as Claude." width="1000" height="270" data-path="images/claude-tag/diagrams/dm-identity-dark.svg" />

The table lines up the two paths on the four dimensions that differ.

|             | In a channel                                   | In a DM                                                              |
| :---------- | :--------------------------------------------- | :------------------------------------------------------------------- |
| Acts as     | Its own service accounts                       | You                                                                  |
| Access      | The channel's Access bundles                   | Your personal connectors                                             |
| Attribution | The agent's accounts, in each tool's audit log | Your name, except pull requests, which the Claude GitHub App authors |
| Billing     | The organization                               | Your seat                                                            |

Three of those differences are worth spelling out.

* **Connectors.** The [connectors on your account](/docs/connectors/overview) are available, including MCP servers you've added.
* **Billing.** Usage bills to your seat rather than the organization's service key.
* **Channel-side configuration.** It doesn't follow you in; the agent's connections and repository grants don't apply in DMs.

DM work runs under your credentials, so most of it is attributed to you and can reach only what your own accounts can. Pull requests are the exception: Claude authors them as the Claude GitHub App from DMs too, so a repository's history shows the same author either way, while the repositories it can reach are still only the ones connected on your own account.

Use channels for shared work and DMs for personal tasks, or for data you'd rather access under your own authenticated identity than a shared channel credential.

### Claude Tag versus Claude Code in Slack

A DM with Claude Tag runs under your own account, which is also how [Claude Code in Slack](https://code.claude.com/docs/en/slack) works, routing a coding @-mention to a Claude Code session on the web under the requester's own account. The two can look identical. The table shows how to tell them apart.

|                | Claude Tag in a channel                                | Claude Code in Slack                                                            |
| :------------- | :----------------------------------------------------- | :------------------------------------------------------------------------------ |
| **Runs under** | The agent identity an admin provisioned                | Your own Claude account, linked in the Claude app                               |
| **GitHub**     | The Claude GitHub App; pull requests belong to the app | Your GitHub connection on claude.ai/code; pull requests open under your account |
| **Access**     | The Access bundles an admin attached to the channel    | Your personal connectors                                                        |
| **Billing**    | The organization                                       | Your seat                                                                       |

If `@Claude` in your workspace opens pull requests as you, you're seeing Claude Code in Slack, not a Claude Tag session.

## Related resources

* [Security and data handling](/docs/claude-tag/concepts/security-and-data): where credentials are stored, what leaves your tenant, and what runs unattended
* [Give Claude access](/docs/claude-tag/admins/add-connections): provision the access this page describes
* [Restrict where Claude Tag operates](/docs/claude-tag/admins/restrict-access): narrow where this agent identity is allowed to act
