> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Give Claude access to your tools

> An Access bundle bundles the credentials Claude Tag acts with. See how to create the dedicated service accounts, what to connect first, and how allowed websites limit reach.

export const BetaNote = () => <Info>Claude Tag is in public beta. Features and behavior described here may change before general availability.</Info>;

<BetaNote />

<div className="tm-stepbar">
  <a className="tm-stepbar-seg tm-done" href="/docs/docs/claude-tag/admins/pair-workspace">1 · Pair workspace</a>
  <a className="tm-stepbar-seg tm-current" href="/docs/docs/claude-tag/admins/add-connections">2 · Give access</a>
  <a className="tm-stepbar-seg" href="/docs/docs/claude-tag/admins/configure-github">3 · Connect GitHub</a>
  <a className="tm-stepbar-seg" href="/docs/docs/claude-tag/admins/set-spend-limit">4 · Spend limit</a>
  <a className="tm-stepbar-seg" href="/docs/docs/claude-tag/admins/test-it">5 · See it work</a>
</div>

<div className="tm-stepmeta">
  <div className="tm-stepmeta-row"><span className="tm-stepmeta-label">Role you need</span><span>Owner in your Claude organization. You'll also need a credential for each service, created by you or by that service's admin.</span></div>
  <div className="tm-stepmeta-row"><span className="tm-stepmeta-label">Before this step</span><span>A <a href="/docs/docs/claude-tag/admins/pair-workspace">paired workspace</a></span></div>
  <div className="tm-stepmeta-row"><span className="tm-stepmeta-label">Do I need this?</span><span><span className="tm-meta-pill tm-meta-pill-opt">Optional to start</span>You need a connection only when Claude should act in a system beyond Slack, like querying BigQuery, reading Google Drive, or filing Linear tickets.<br /><br />You can add connections any time after setup (they apply immediately), but adding the systems your team expects before they onboard means their first requests succeed.</span></div>
</div>

<Tip>Claude starts delivering work before you connect anything. On Slack content alone, it can [catch a team up on a channel or thread](/docs/claude-tag/users/use-cases/catch-up), [triage a request channel](/docs/claude-tag/users/use-cases/triage-requests), [turn a discussion into a doc](/docs/claude-tag/users/use-cases/create-artifacts), and [track a project from channel history](/docs/claude-tag/users/use-cases/track-projects). Connections multiply what it can do from there; each one adds a system Claude can act in beyond Slack.</Tip>

## Your first Access bundle

An [Access bundle](/docs/claude-tag/concepts/glossary#access-bundle) is a named set of credentials, repository grants, and instructions that Claude uses in the channels the bundle covers. A connection is one service credential inside a bundle, like a Datadog API key or a warehouse service account, that Claude uses to act in that service from any channel under the bundle's [scope](/docs/claude-tag/concepts/glossary#scope).

If you're in [setup](/docs/claude-tag/admins/setup-overview), you add these connections there; skip to [Decide what to connect](#decide-what-to-connect). The steps below are for creating a bundle outside setup, on the admin page directly.

<Steps>
  <Step title="Open the admin page">
    Go to [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag). Under **Claude Tag's access**, the **Slack** tab shows your scopes (the organization-wide **Slack** row, each workspace, and any channels under them). The **Slack** row opens as **Default Slack access**.
  </Step>

  <Step title="Create a bundle on a scope">
    On the scope where you want the bundle to apply, click **+** next to **Access bundles** and choose **Create new bundle**. This creates the bundle and attaches it to that scope in one step; the bundle dialog opens.
  </Step>

  <Step title="Name the bundle">
    Click the pencil next to **Untitled access bundle** to rename it (the console uses "profile" and "Access bundle" interchangeably).
  </Step>
</Steps>

You can also create an unattached bundle by clicking **Create** on the **Access bundles** page in the left navigation, then attach it to scopes afterward.

Connections belong to the [agent identity](/docs/claude-tag/concepts/agent-identity), not to any person. Personal claude.ai connectors apply only in DMs.

Name a bundle after what it grants, since the name is what you'll read when deciding which bundles to bind to a channel: `data-readonly`, `github-write`, `monitoring`, `gtm-tools`. A capability name stays meaningful when the same bundle serves several teams; a team name (`devprod-team`) works when one team's full access is the unit you'll reuse.

### Why create more than one bundle

Multiple bundles let you grant access by capability and compose it per channel. For example, with separate `data-readonly`, `github-write`, and `monitoring` bundles: `#platform-eng` gets all three, `#gtm-analytics` gets only `data-readonly`, and `#incidents` gets `monitoring` plus `github-write`. Each credential is defined once, so rotating a Datadog key means editing one bundle without touching the others.

A bundle also has Domains, Plugins, and Instructions tabs alongside Credentials and Repositories. Use the bundle's Instructions for guidance that should travel with a credential; use [per-scope custom instructions](/docs/claude-tag/admins/attach-to-scope#add-custom-instructions) for guidance tied to a place.

## Decide what to connect

Six categories cover most of the work teams hand to Claude. Any service with an HTTP API can be added; start with the categories that match what your teams already do.

Read-only connections are most useful in combination: an answer that joins the ticket, the deploy, and the error rate needs all three systems connected. Connecting many systems read-only is a different decision from granting write access anywhere.

| Connect            | Examples                                                                                                                                                  | Recommended access | What it adds                                                                                                                          |
| :----------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------- | :------------------------------------------------------------------------------------------------------------------------------------ |
| Knowledge and docs | Google Drive, [Notion](/docs/claude-tag/admins/connections/notion), [Confluence](/docs/claude-tag/admins/connections/atlassian)                                     | Read               | Answers grounded in design docs, runbooks, and prior decisions                                                                        |
| Code               | GitHub, [GitLab](/docs/claude-tag/admins/connections/gitlab)                                                                                                   | Read and write     | Branches, pull requests, review, CI follow-up. GitHub is managed through the [Claude GitHub App](/docs/claude-tag/admins/configure-github) |
| Data warehouse     | BigQuery, [Snowflake](/docs/claude-tag/admins/connections/snowflake), Redshift                                                                                 | Read               | Data questions answered with charts in the thread; recurring reports                                                                  |
| Monitoring         | [Sentry](/docs/claude-tag/admins/connections/sentry), [Datadog](/docs/claude-tag/admins/connections/datadog), [PagerDuty](/docs/claude-tag/admins/connections/pagerduty) | Read               | Logs, metrics, and errors for debugging and incident work                                                                             |
| Issue tracking     | [Linear](/docs/claude-tag/admins/connections/linear), [Asana](/docs/claude-tag/admins/connections/asana), [Jira](/docs/claude-tag/admins/connections/atlassian)          | Read and write     | File tickets and post status updates where work lives                                                                                 |
| Go-to-market       | [HubSpot](/docs/claude-tag/admins/connections/hubspot), [Gong](/docs/claude-tag/admins/connections/gong), [Salesforce](/docs/claude-tag/admins/connections/salesforce)   | Read               | Pipeline and customer state for account questions                                                                                     |

Per-service instructions, with the credential fields and allowed-websites values, are in the [connection guides](/docs/claude-tag/admins/connections/overview).

### Create a dedicated account per service

<Warning>The credential you connect is Claude's account in that tool, not yours. Anyone in a channel under the bundle's scope can use it through Claude, so connect a dedicated identity you control rather than your personal login.</Warning>

For each tool, create that identity specifically for the agent rather than reusing a shared bot key. The pattern depends on the service.

| Service type                                                   | Recommended pattern                                                                                                                                                                                                                                                                                           |
| :------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Google Workspace (Drive, Calendar, Docs)                       | Create a virtual user like `claude@yourcompany.example.com` and share the folders and calendars it needs. If using a GCP service-account key with domain-wide delegation, restrict the delegation to that single subject and the minimum OAuth scopes; DWD can otherwise impersonate any user in your domain. |
| SaaS with native service accounts (Datadog, Snowflake, Sentry) | Create a service account in that tool's admin, scope it to the project or read-only role, and use its API key                                                                                                                                                                                                 |
| SaaS without service accounts (Linear, Asana)                  | Create a dedicated user seat for the agent and use a personal access token from that seat                                                                                                                                                                                                                     |
| Cloud APIs (AWS, GCP)                                          | Create a dedicated IAM principal with the narrowest policy that covers the work                                                                                                                                                                                                                               |

A dedicated account keeps the agent's activity separately auditable in each tool's logs and lets you revoke its access without touching anyone else's. Grant read-only wherever the categories below say read; Claude can never exceed what the key allows.

If the person who administers a service isn't you, send them this:

```text wrap theme={null}
Please create a service account in [service] for our Claude agent, scoped to [read-only / the specific project], and send me the credential through [your secrets channel]. It will be used by an org-managed agent, with the credential injected at a network proxy; the agent itself never holds the key. Details: https://claude.com/docs/claude-tag/admins/add-connections
```

### Limit access to specific resources

A connection has no setting for which pages, folders, or projects Claude can reach inside a tool. The connection's reach is whatever the connected account can access in that tool. To narrow Claude to a subset, narrow the account:

* **Confluence or another wiki:** give the service account read access to only the spaces or pages Claude should see
* **Google Drive:** share only the relevant folders with the dedicated Google account; see [Google Workspace](/docs/claude-tag/admins/connections/google)
* **Project or ticket trackers:** add the service account to only the projects it needs

The host, path, and method restrictions on a connection control which API endpoints Claude can call, not which records those endpoints return. Use them alongside account-level scoping, not instead of it.

For a shared or external channel, put the narrowed connection in its own bundle and [attach that bundle only to that channel](/docs/claude-tag/admins/attach-to-scope#attach-to-a-channel), so the credential is unavailable elsewhere.

## Connect a service that isn't in the list

The services with **Connect** buttons on the Credentials tab are presets, not the full set Claude can connect to. Any app with an API can be connected: click **Connect** next to **Custom tool** at the bottom of the tab. See the [Custom connection guide](/docs/claude-tag/admins/connections/custom) for the form fields, credential types, and how to add a custom MCP server.

## Allow a host without a credential

Claude does channel work in an isolated [sandbox](/docs/claude-tag/concepts/agent-identity#channel-sessions). A network request is traffic that sandbox sends to a host, such as an API call, a `curl` fetch, or a package install. Before Claude can make one from a channel, the destination host has to be allowed by one of three settings, the allow layers:

* **A domain entry**: a hostname listed on this bundle's **Domains** tab. Requests to it pass with no credential attached; see [Add a domain](#add-a-domain).
* **A [connection](#add-a-connection)**: a credential on this bundle's **Credentials** tab. Requests matching its [allowed websites](#set-allowed-websites) pass with that credential attached.
* **The scope's [environment](/docs/claude-tag/concepts/glossary#environment)**: the compute configuration the scope's sessions run in, which carries its own network access setting, starting at the Trusted access level that covers common package registries. Requests to hosts it allows pass with no credential; see [Broad web access through the environment](#broad-web-access-through-the-environment).

A host that none of these allows stays unreachable, and when more than one bundle is attached to a scope, the entries of all of them apply. Web search is governed by none of them, because searching happens on Anthropic's servers rather than in the sandbox; see [Web search vs. network requests](#web-search-vs-network-requests).

### Add a domain

A domain entry allowlists one hostname for every channel this bundle covers. After you add it, requests from those channels' sandboxes to that host go through with no credential attached.

To get there, open the bundle from the scope that covers the channel, under **Claude Tag's access** at [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag); if the scope has no bundle yet, [create one](#your-first-access-bundle) first. On the bundle's **Domains** tab, fill in the form and click **Add domain**:

* **Domain**: the hostname to allow; a wildcard is allowed as the leftmost label, like `*.example.com`, and covers subdomains at any depth but not `example.com` itself
* **Ports**: needed only when the service listens on something other than 443

You don't have to predict the full list up front. When a request is blocked, Claude says so in the thread and names the host, with wording like "blocked by the network egress proxy" (that is, by Agent Proxy); add that host here and retry. If the host is listed and Claude still reports it blocked, check these in order:

* **The bundle is attached to the channel's scope.** Claude can use a Domains entry only in channels whose scope, or an ancestor scope, has this bundle attached; see [Attach bundles to scopes](/docs/claude-tag/admins/attach-to-scope).
* **The entry matches the exact host.** A wildcard like `*.example.com` doesn't cover `example.com` itself, and `www.example.com` and `example.com` are different hosts.
* **The request didn't move to another host.** If the page redirects, or loads from a CDN or a sign-in host, allow that host too; Claude names the host it was blocked on.
* **The port is listed.** Needed only when the service listens on something other than 443.
* **A minute has passed since you saved.** Agent Proxy picks up a new entry within about a minute, in existing threads as well as new ones, so retry in the same thread after a short wait.
* **The request came from a channel, not a DM.** A bundle attached to a channel doesn't apply in DMs.

Typical entries are hosts the work calls without a key, such as a docs site or a public API. Common package registries are usually already reachable through the [environment's Trusted access default](#broad-web-access-through-the-environment), and a host that needs a credential belongs in a [connection](#add-a-connection) instead. Entries appear below the form, and each one can be edited or removed from its row.

<Note>[Agent Proxy](/docs/claude-tag/concepts/agent-identity#agent-proxy) carries only HTTP and HTTPS. A protocol that isn't HTTP, such as SSH, can't cross the proxy, so listing a host here doesn't make it reachable over SSH.</Note>

### Broad web access through the environment

Domain entries allow hosts one at a time. For a scope whose work needs more of the web, the environment setting grants broader access. An [environment](/docs/claude-tag/concepts/glossary#environment) is the sandboxed compute configuration the scope's sessions run in, and it carries its own network access setting.

A new environment's network access level is Trusted access, which allows a [documented set of package registries and developer hosts](https://code.claude.com/docs/en/cloud-environments#default-allowed-domains). A channel can already reach hosts like `pypi.org` and `registry.npmjs.org` with no domain entry.

To give a scope broader access, create an environment with a more permissive level and pin it on the scope.

<Steps>
  <Step title="Create the environment">
    From the **Cloud environments** page in [admin settings](https://claude.ai/admin-settings), add an [organization-shared environment](https://code.claude.com/docs/en/cloud-environments#organization-shared-environments) and set its network access level. **Full access** allows any domain; see [Network access in the Claude Code docs](https://code.claude.com/docs/en/cloud-environments#network-access) for the other levels. This step takes an Owner or admin.

    Don't create the environment at [`claude.ai/code`](https://claude.ai/code): environments you create there belong to your individual account, so they never appear in the picker.
  </Step>

  <Step title="Pin it on the scope">
    Open the scope's **Advanced** section and use the **Environment** picker. With nothing pinned, sessions use the organization default.
  </Step>
</Steps>

The environment must be scoped to the organization, not an individual account. If sessions don't pick up the one you pinned, see [the environment troubleshooting entry](/docs/claude-tag/admins/troubleshooting#channel-sessions-use-the-wrong-environment-or-can%E2%80%99t-find-one).

### Allow all hosts

Allow-all egress is off by default; ask your Anthropic account team to enable it for your organization. Once enabled, you can enter `*` alone as the domain. A `*` entry needs ports assigned; it admits any host on those ports, with no credential attached.

With `*` active:

* Requests to hosts that no connection covers go through with no credential attached.
* A `*` entry never carries a credential, and a connection's credential still travels only to its [allowed websites](#set-allowed-websites).
* Private and internal network addresses and cloud metadata endpoints remain blocked.

Without allow-all egress enabled, saving `*` fails with a generic "Couldn't add domain." error that doesn't name the cause. If the capability is later disabled, you can disable an existing `*` entry or narrow it to specific hosts, but you can't keep it active.

### Web search vs. network requests

Web search needs no domain entry, connection, or environment setting. It's [Anthropic's built-in web search tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool), and the searching happens on Anthropic's servers rather than in the channel's sandbox, so no allow layer applies.

Opening a page is not part of the search. A search returns content from the pages it matches, which Claude reads and cites; fetching a URL from the sandbox is a network request like any other, and the host needs an allow layer. Claude can answer from a page that search surfaced yet report that it can't open the same link.

If the work needs Claude to open and read pages rather than answer from search results, allow those hosts through the settings above. [Web search vs. network requests](/docs/claude-tag/concepts/agent-identity#web-search-vs-network-requests) covers the session mechanics behind the split.

## Add a connection

On the bundle's **Credentials** tab, click **Connect** next to a listed service, or next to **Custom tool** for a service not in the list.

For a custom connection, choose the credential type:

| Credential type                             | Use for                                                                                                                                                                           |
| :------------------------------------------ | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Bearer                                      | API keys and OAuth bearer tokens. Most SaaS REST APIs.                                                                                                                            |
| Basic                                       | HTTP Basic authentication.                                                                                                                                                        |
| Body parameter                              | A token the API expects in the request body or query string instead of a header.                                                                                                  |
| AWS SigV4                                   | Signed requests to AWS APIs with an access key pair.                                                                                                                              |
| GCP access token (with Service Account Key) | Google Cloud APIs via a service-account JSON key. Google Workspace services like Drive and Calendar also use this; see [the Google guide](/docs/claude-tag/admins/connections/google). |
| GCP IAP (with Service Account Key)          | Google Cloud services behind Identity-Aware Proxy.                                                                                                                                |
| OAuth 2.0 JWT bearer                        | Server-to-server OAuth.                                                                                                                                                           |
| OAuth 2.0 client credentials                | Server-to-server OAuth. Salesforce uses this.                                                                                                                                     |
| MCP Connector                               | Sign in once as an admin; the agent acts as that account.                                                                                                                         |

For GitHub repositories, use the GitHub connection at [Configure GitHub access](/docs/claude-tag/admins/configure-github) rather than a credential from this table.

Credentials are injected at the network boundary by Agent Proxy; the model and the sandbox are not given the key. A request to a host you haven't allowed is blocked, not sent. See [how Agent Proxy works](/docs/claude-tag/concepts/agent-identity#agent-proxy).

### Send a setup link to another admin

When someone else holds a service's secret, create a setup link instead of collecting the secret yourself. On the service's row in the **Credentials** tab, open the **Connect** button's menu and select **Copy link for another admin**. Whoever opens the link signs in to your Claude organization and submits the credential there. They don't need an admin role.

The row tracks the link. It shows **Pending** until the credential is submitted, then **Approval needed**. Select **Review** to check the submission and approve or reject it. The credential becomes active only after you approve it. The row shows **Expired** for a link that went unused, and until the credential is submitted you can revoke the link from the row's **⋮** menu.

Setup links are available for services that use the Bearer or Basic credential type. For other types, the **Connect** menu has no link option.

### Set allowed websites

List the hosts a connection's credential may be sent to. A wildcard works only as the leftmost label, like `*.example.com`; it covers subdomains at any depth but not `example.com` itself. You can't enter `*` alone here; a credential is always limited to specific hosts. To let Claude reach any host without a credential, see [Allow all hosts](#allow-all-hosts).

To change a connection's name or allowed websites after saving, open the **⋮** menu on that connection's row in the bundle's **Credentials** tab and choose **Edit**. The same menu has **Rotate secret** (where the credential type supports it) and **Delete**.

Check the host against your account's region before saving. Some presets fill a default host that may not match your account's region; a Datadog key, for example, only works against your account's Datadog site, like `api.datadoghq.com` or `api.datadoghq.eu`.

### Restrict by path or method

After saving, you can narrow a connection. Select **Edit** on the connection's row in the bundle's **Credentials** tab. The **Edit connection** dialog lets you rename the connection and, where the connection has an allow rule, restrict it by HTTP method and path, for example to allow `GET` but not `DELETE`.

Agent Proxy starts applying a change within about a minute of your saving it, in existing threads as well as new ones. It evaluates connections and Domains entries from the most specific scope outward (channel, then workspace, then organization), and within a scope by priority; the first match decides. A request that matches no connection, no Domains entry, and nothing in the environment's network access is blocked. Private IP ranges and cloud metadata endpoints stay blocked regardless.

### Connections vs claude.ai connectors

The connection gallery lists credential types the agent can hold, not the connectors your organization or its members have set up on claude.ai. A connection authenticates the agent, not a person; a connector on someone's personal claude.ai account doesn't appear here. For Google services, use a service-account key or the MCP Connector sign-in option, both of which give the agent one credential with access to the data the channel needs. Personal connectors keep working in [DMs](/docs/claude-tag/concepts/agent-identity#direct-message-channels).

## Attach plugins

A connection grants access; a plugin teaches Claude how to use it well. A plugin is a bundle of skills, reusable instructions for working with a specific tool or following a specific process, and you attach plugins to the same Access bundle or scope that carries the connection, so the credential arrives with directions for using it.

A Datadog API key, for example, makes the API reachable, and a Datadog plugin tells Claude which endpoints answer which questions. Sessions in covered channels pick up attached plugins automatically; there is nothing for channel members to install or enable.

Anthropic provides plugins for common tools, and you can add your own from a [skills repository](/docs/claude-tag/admins/skills-repo). To give Claude organization-wide skills, bundle them in a plugin.

Plugins attach in two places, and the two behave differently:

* A plugin added directly on a scope (the plugin chips on the scope's panel) is enabled there as soon as you add it.
* A bundle's **Plugins** tab lists the plugins available to your organization, each off until you toggle it on.

Registering a plugin at the organization level makes it available, not active. It takes effect only where a bundle enables it or a scope adds it directly.

Adding or removing plugins and skills applies to new threads only. A thread already running keeps the set it began with; start a fresh thread to pick up changes. See [What survives between replies](/docs/claude-tag/concepts/how-it-works#what-survives-between-replies).

Claude can't publish a new skill version from inside a thread; that update happens in admin settings.

## Verify the connection saved

* Each connection is listed in the bundle with the host you set.
* The [Access bundles page](https://claude.ai/admin-settings/claude-tag/access-bundles) shows a status for each connection when you expand the bundle.
  * **Active**: Claude can send the credential to its allowed hosts
  * **Not active**: the secret is stored but no allow rule uses it yet, so Claude can't send it.
  * **Approval needed**: another admin submitted the credential through a shared setup link. Select **Review** on its row, then **Approve**.
  * **Used** with a time, or **Never used**: when Claude last sent the credential; independent of the status
* New threads pick up new connections on their own. An existing thread isn't told about a connection added after it started, but the connection works there; ask Claude to use the service by name.

## Related resources

* [Set a spend limit](/docs/claude-tag/admins/set-spend-limit): fund usage so the connections you just added can run
* [Configure GitHub access](/docs/claude-tag/admins/configure-github): repository access, managed through the Claude GitHub App
* [How agent identity works](/docs/claude-tag/concepts/agent-identity#agent-proxy): how the credentials you just added reach Claude without entering its sandbox
