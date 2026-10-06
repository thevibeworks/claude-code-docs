> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Give Claude access to your tools

> Add connectors so Claude Tag acts in your tools with its own credentials. Covers service accounts, bundles, allowed websites, domain entries, and plugins.

export const BetaNote = () => <Info>Claude Tag is in public beta. Features and behavior described here may change before general availability.</Info>;

<BetaNote />

<Tip>Claude starts delivering work before you connect anything. On Slack content alone, it can [catch a team up on a channel or thread](/docs/claude-tag/users/use-cases/catch-up), [triage a request channel](/docs/claude-tag/users/use-cases/triage-requests), [turn a discussion into a doc](/docs/claude-tag/users/use-cases/create-artifacts), and [track a project from channel history](/docs/claude-tag/users/use-cases/track-projects).</Tip>

A connector gives Claude its own credential for one of your tools, like a Datadog API key or a warehouse service account, so Claude can act in that tool from Slack channels. This page is for the admins who add connectors and decide where they apply. To let Claude act as a member with that member's own claude.ai connectors, see [Personal connectors](/docs/claude-tag/concepts/personal-connectors) instead.

Adding connectors and bundles requires the **Owner** role or the [**Claude Tag Admin** permission](/docs/claude-tag/admins/restrict-access#delegate-claude-tag-administration) in your Claude organization. You manage both in [**Organization settings > Claude Tag**](https://claude.ai/admin-settings/claude-tag), under **Claude's access**, which appears once the **Enable Claude Tag in Slack** switch is on.

Connectors belong to the [agent identity](/docs/claude-tag/concepts/agent-identity), not to any person. Personal claude.ai connectors apply in one-to-one DMs. Claude can also [use a member's own connectors in a channel](/docs/claude-tag/concepts/personal-connectors) for that member's own tasks, after the member allows it.

## Decide what to connect

Six categories cover most of the work teams give Claude. Any service with an HTTP API can be added; start with the categories that match what your teams already do.

Read-only connectors are most useful in combination: an answer that joins the ticket, the deploy, and the error rate needs all three systems connected.

| Connect | Examples | Recommended access | What it adds |
| :- | :- | :- | :- |
| Knowledge and docs | Google Drive, [Notion](/docs/claude-tag/admins/connections/notion), [Confluence](/docs/claude-tag/admins/connections/atlassian) | Read | Answers grounded in design docs, runbooks, and prior decisions |
| Code | GitHub, [GitLab](/docs/claude-tag/admins/connections/gitlab) | Read and write | On GitHub, branches, pull requests, review, and CI follow-up through the [Claude GitHub App](/docs/claude-tag/admins/configure-github). On GitLab, issues, merge request comments, and pipeline checks through its API |
| Data warehouse | BigQuery, [Snowflake](/docs/claude-tag/admins/connections/snowflake), Redshift | Read | Data questions answered with charts in the thread; recurring reports |
| Monitoring | [Sentry](/docs/claude-tag/admins/connections/sentry), [Datadog](/docs/claude-tag/admins/connections/datadog), [PagerDuty](/docs/claude-tag/admins/connections/pagerduty) | Read | Logs, metrics, and errors for debugging and incident work |
| Issue tracking | [Linear](/docs/claude-tag/admins/connections/linear), [Asana](/docs/claude-tag/admins/connections/asana), [Jira](/docs/claude-tag/admins/connections/atlassian) | Read and write | File tickets and post status updates where work lives |
| Go-to-market | [HubSpot](/docs/claude-tag/admins/connections/hubspot), [Gong](/docs/claude-tag/admins/connections/gong), [Salesforce](/docs/claude-tag/admins/connections/salesforce) | Read | Pipeline and customer state for account questions |

Per-service instructions, with the credential fields and allowed-websites values, are in the [connection guides](/docs/claude-tag/admins/connections/overview).

### Create a dedicated account per service

<Warning>The credential you connect is Claude's account in that tool, not yours. Anyone in a channel where the connector applies can use it through Claude, so connect a dedicated identity you control rather than your personal login.</Warning>

For each tool, create that identity specifically for the agent rather than reusing a shared bot key. The pattern depends on the service.

| Service type | Recommended pattern |
| :- | :- |
| Google Workspace (Drive, Calendar, Docs) | Create a virtual user like `claude@yourcompany.example.com` and share the folders and calendars it needs. If using a GCP service-account key with domain-wide delegation, restrict the delegation to that single subject and the minimum OAuth scopes; DWD can otherwise impersonate any user in your domain. |
| SaaS with native service accounts (Datadog, Snowflake, Sentry) | Create a service account in that tool's admin, scope it to the project or read-only role, and use its API key |
| SaaS without service accounts (Linear, Asana) | Create a dedicated user seat for the agent and use a personal access token from that seat |
| Cloud APIs (AWS, GCP) | Create a dedicated IAM principal with the narrowest policy that covers the work |

A dedicated account keeps the agent's activity separately auditable in each tool's logs and lets you revoke its access without touching anyone else's. Grant read-only wherever the categories above say read; Claude can never exceed what the key allows.

If the person who administers a service isn't you, [send them a setup link](#send-a-setup-link-to-another-admin), or send them this:

```text wrap theme={null}
Please create a service account in [service] for our Claude agent, scoped to [read-only / the specific project], and send me the credential through [your secrets channel]. It will be used by an org-managed agent, with the credential injected at a network proxy; the agent itself never holds the key. Details: https://claude.com/docs/claude-tag/admins/add-connections
```

### Limit access to specific resources

A connector has no setting for which pages, folders, or projects Claude can reach inside a tool. The connector's reach is whatever the connected account can access in that tool. To narrow Claude to a subset, narrow the account:

* **Confluence or another wiki:** give the service account read access to only the spaces or pages Claude should see
* **Google Drive:** share only the relevant folders with the dedicated Google account; see [Google Workspace](/docs/claude-tag/admins/connections/google)
* **Project or ticket trackers:** add the service account to only the projects it needs

The host, path, and method restrictions on a credential control which API endpoints Claude can call, not which records those endpoints return. Use them alongside account-level scoping, not instead of it.

For a shared or external channel, put the narrowed credential in its own [bundle](#create-a-bundle) and add only that channel under the bundle's **Where it applies**, so the credential is unavailable elsewhere.

<a id="add-a-connection" />

<a id="where-a-new-connector-applies" />

## Add a connector

The first credential you add for a service from the **Connectors** tab is on in every workspace and channel as soon as you save it. You can give it narrower reach:

* **One workspace or channel from the start**: [connect it from that place's page](#connect-a-service-for-one-workspace-or-channel) instead.
* **Some channels**: add it from the **Connectors** tab, then [restrict it on its page](#restrict-a-connector-to-some-channels).
* **Off everywhere until you choose where it applies**: add it to a new [bundle](#create-a-bundle) instead.

If the service, or a custom connector's host, is already on the **Connectors** tab, the new credential starts off everywhere until you choose where it applies.

<Steps>
  <Step title="Open the Connectors tab">
    Go to [**Organization settings > Claude Tag**](https://claude.ai/admin-settings/claude-tag). Under **Claude's access**, select the **Connectors** tab and click **Add**.
  </Step>

  <Step title="Pick the service">
    In the **Add a connector** dialog, search for the service and select it. A service Claude already holds a credential for shows **Connected**. For GitHub, see [Configure GitHub access](/docs/claude-tag/admins/configure-github). For a service that isn't listed, select **Custom connector** at the bottom of the list; see [Connect a service that isn't in the list](#connect-a-service-that-isn%E2%80%99t-in-the-list).

    For a service that offers a sign-in as well as a key, such as Amplitude, the dialog then shows **How Claude authenticates**. Leave **Paste an API key** selected, or select the sign-in option, such as **Sign in to Amplitude as Claude**, and click **Continue to** *service*.
  </Step>

  <Step title="Enter the credential">
    In the connect form, enter the credential from the service's [dedicated account](#create-a-dedicated-account-per-service). On the form's **Advanced** tab, check the hosts under **Allowed websites** (see [Set allowed websites](#set-allowed-websites)), then click **Connect**.

    If you chose the sign-in option, click the form's sign-in button, such as **Sign in with Amplitude**, and sign in with an account made for Claude.
  </Step>
</Steps>

After you click **Connect**, the connector's page opens. The line under the new credential's name in the **Access from** table reads **On for all of Slack.** when the credential applies everywhere, or **Not assigned yet. Choose where Claude can use it.** when it waits for you to pick its places under **Assign access**.

### Connect a service for one workspace or channel

To connect a service that applies in one workspace or channel only, start from that place's page instead of the **Connectors** tab.

<Steps>
  <Step title="Open the place's page">
    Go to [**Organization settings > Claude Tag**](https://claude.ai/admin-settings/claude-tag). Under **Claude's access**, select the **Channels** tab and open the workspace's or channel's page.
  </Step>

  <Step title="Pick the service">
    On that page, click **Add** under **Claude's access** and select **Connector**. On the dialog's **Connectors** tab, select the service under **Connect new**, or select **Custom connector** there for a service that isn't listed, and click **Continue**.
  </Step>

  <Step title="Enter the credential">
    In the connect form, enter the credential from the service's [dedicated account](#create-a-dedicated-account-per-service) and click **Connect**.
  </Step>
</Steps>

The credential applies only in that workspace or channel, and a workspace's credential reaches every channel in it. To use it in more places, pick it in each place's row under **Assign access** on the connector's page, selecting **Add place** for a place that isn't listed.

### Set allowed websites

List the hosts a credential may be sent to under **Allowed websites** in the connect form. A wildcard works only as the leftmost label, like `*.example.com`; it covers subdomains at any depth but not `example.com` itself. You can't enter `*` alone here; a credential is always limited to specific hosts. To let Claude reach any host without a credential, see [Allow all hosts](#allow-all-hosts).

<Note>You can't save a connector whose **Allowed websites** include an `anthropic.com`, `claude.ai`, or `claude.com` host, such as `api.anthropic.com`.</Note>

Check the host against your account's region before saving. Some services fill a default host that may not match your account's region; a Datadog key, for example, only works against your account's Datadog site, like `api.datadoghq.com` or `api.datadoghq.eu`.

Where the connect form has a **Test connection** button, the test can check the service's default host rather than the one you entered, so a key for a regional or self-hosted instance can fail the test and still work. Replace the prefilled host with your service's API host rather than adding yours alongside it. You can save the connector even if the test fails, and the credential is sent only to the hosts you listed.

To change a credential's name or hosts after saving, open the **⋮** menu on its row in the connector page's **Access from** table and select **Edit**. Where the **Edit connection** dialog lets you change the hosts, the field is labeled **Allowed hosts**.

### Send a setup link to another admin

When someone else holds a service's secret, send them a setup link instead of collecting the secret yourself. In the service's connect form, click **Copy setup link for another admin**. Whoever opens the link signs in to your Claude organization and submits the credential there. They don't need an admin role.

<Note>Setup links work for the Bearer and Basic credential types. For other types the button is unavailable.</Note>

After the teammate submits the credential, it waits for your approval. Go to [**Notifications**](https://claude.ai/admin-settings/notifications) in admin settings, open the **Requests** tab, and click **Review** on the **Approval needed** row. Then click **Approve** or **Reject**. The credential becomes active only after you approve it.

A link that hasn't been used yet is listed in one of two places:

* **If the service already has a connector page**: the link shows there as a row in **Access from** that reads **Setup link waiting for a teammate**, or **Setup link expired** once it lapses
* **If no connector covers the service yet**: the link is listed on the **Connectors** tab, under **Setup links waiting for a teammate**

In both places, the row's **⋮** menu has **Revoke link**, and **Copy link for another admin** until the link expires.

### Claude Tag connectors vs personal claude.ai connectors

The **Add a connector** dialog lists services Claude can hold its own credential for, not the connectors your organization or its members have set up on claude.ai. A Claude Tag connector authenticates the agent, not a person; a connector on someone's personal claude.ai account doesn't appear there. For Google services, use a service-account key or sign in with an account made for Claude, both of which give the agent one credential with access to the data the channel needs. Personal connectors keep working in [DMs](/docs/claude-tag/concepts/agent-identity#direct-message-channels).

## Change an existing connector

You change where a connector applies, and which credentials it holds, on the connector's page. To open it, go to [**Organization settings > Claude Tag**](https://claude.ai/admin-settings/claude-tag), select the **Connectors** tab under **Claude's access**, and select the connector. On that page, **Assign access** lists where Claude can use the connector, and the **Access from** table lists each credential Claude holds for the service.

### Restrict a connector to some channels

For a connector you added from the **Connectors** tab, the **Slack** row under **Assign access** holds its first credential in the **Access** column, so every workspace and channel has it.

When a bundle holds the connector's credential along with other access, such as other connectors, **Assign access** can't add that credential to a place or take it off one. If **Assign access** refuses a credential with "This credential was added for one place only", that credential stays where it is. To use the service in another place, connect it again there, as [Use a different credential in one workspace or channel](#use-a-different-credential-in-one-workspace-or-channel) describes.

<Steps>
  <Step title="Open the connector's page">
    Go to [**Organization settings > Claude Tag**](https://claude.ai/admin-settings/claude-tag). Under **Claude's access**, select the **Connectors** tab, then select the connector to open its page.
  </Step>

  <Step title="Take the credential off the Slack row">
    Under **Assign access**, open the picker in the **Access** column of the **Slack** row and clear the credential's checkbox.
  </Step>

  <Step title="Add each place that keeps the connector">
    Click **Add place** and choose the workspace or channel under **Where**. The dialog fills in one of the connector's credentials under **Credential**, which you can change if the connector holds more than one. Click **Add**, and repeat for each place that should keep the connector. A workspace you add also covers every channel in it.
  </Step>

  <Step title="Save">
    Click **Save changes**.
  </Step>
</Steps>

Each row's **Access** picker lists the connector's own credentials first, then each bundle on the **Bundles** tab that holds one of its credentials. Selecting a bundle there attaches that bundle at the place, along with everything else the bundle holds.

### Manage a connector's credentials

A connector's credentials are listed in the **Access from** table on its page, which you open by selecting the connector on the **Connectors** tab.

* **Edit, rotate, or remove a credential**: open the row's **⋮** menu and select **Edit**, **Rotate secret** where the credential type supports it, or **Remove credential**
* **Add a second credential for the same service**: open the **⋮** menu at the top of the connector's page and select **Add credential**. A second credential is off everywhere until you choose where Claude may use it under **Assign access**.
* **Remove the connector and all its credentials**: select **Remove connector** from the menu at the top of its page. If a bundle holds one of its credentials, delete that credential on the bundle's page first.

The table's **Set by** column reads **Here** for a credential added directly, or names the bundle for a credential that a bundle on the **Bundles** tab holds. A credential whose **Set by** column names a bundle has no **Remove credential**; remove it on that bundle's page instead.

### Use a different credential in one workspace or channel

To give one workspace or channel its own credential for a service Claude already holds a credential for, start from that place's page and follow [Connect a service for one workspace or channel](#connect-a-service-for-one-workspace-or-channel). Under **Connect new**, the service shows **Connect a different** *service* **credential** under its name.

* **If the place has its own credential for that service**: the new one replaces it
* **If the place inherits the service**: Claude uses the new credential there instead of the one it inherits from its workspace or from **Slack**

Where the credential can't be changed at that place, such as when a channel rule brings the service there, the row is unavailable and says why.

If you send a [setup link](#send-a-setup-link-to-another-admin) from the connect form for a custom connector or for a credential that replaces one, the place doesn't switch on its own. Once the link is used, pick the new credential for the place under **Assign access** on the connector's page.

### Restrict by path or method

After you save a credential, you can narrow it further than its allowed websites. Select **Edit** from the **⋮** menu on its row in the connector page's **Access from** table. Where the credential has an allow rule, the **Edit connection** dialog lets you restrict it by HTTP method and path, for example to allow `GET` but not `DELETE`.

To narrow a credential before any channel can use it, add the connector to a new [bundle](#create-a-bundle), select **Edit** from the menu on its row under **What's in it**, and add the bundle's places last.

Agent Proxy starts applying an edit to a credential or a domain entry within about a minute after you save it, in existing threads as well as new ones. It checks the channel's credentials and domain entries first, then the workspace's, then the organization's, and within each by priority. A request that matches no credential, no domain entry, and nothing in the environment's network access is blocked. Private IP ranges and cloud metadata endpoints stay blocked regardless.

<a id="your-first-access-bundle" />

## Create a bundle

A [bundle](/docs/claude-tag/concepts/glossary#access-bundle) is a named set of connectors, repositories, domain entries, plugins, and instructions that Claude takes on wherever the bundle applies. Use one to give a group of channels the same access, and to add a connector to only some channels from the start.

<Steps>
  <Step title="Create the bundle">
    Go to [**Organization settings > Claude Tag**](https://claude.ai/admin-settings/claude-tag). Under **Claude's access**, select the **Bundles** tab and click **Add**. In the **Create a bundle** dialog, enter a **Name** and an optional **Description**, pick a **Color** and **Icon**, and click **Create**. The bundle's page opens.
  </Step>

  <Step title="Add what's in it">
    Under **What's in it**, click **Add** and choose **Connector**, **Repository**, **Domain**, or **Plugin**. Each item saves as soon as you add it. A connector added here applies only where the bundle applies.
  </Step>

  <Step title="Choose where it applies">
    Under **Where it applies**, turn on the switch in the **Slack** row to apply the bundle in every workspace and channel, or in a workspace's row to apply it in that workspace. For a channel, click **Add place**, choose the channel under **Where**, and click **Add**. Then click **Save changes**. A bundle applies nowhere until you turn on a row or add a place.
  </Step>
</Steps>

To add an existing bundle from a workspace or channel instead, open that place's page from the **Channels** tab, click **Add** under **Claude's access**, and select **Bundle**. [Attach bundles to workspaces and channels](/docs/claude-tag/admins/attach-to-scope) covers channel rules and how bundles combine.

Name a bundle after what it grants, since the name is what you'll read when deciding which bundles to add to a channel: `data-readonly`, `github-write`, `monitoring`, `gtm-tools`. A capability name stays meaningful when the same bundle serves several teams; a team name (`devprod-team`) works when one team's full access is the unit you'll reuse.

Use the bundle's **Instructions** section for guidance that should travel with its connectors; use [workspace or channel instructions](/docs/claude-tag/admins/attach-to-scope#add-custom-instructions) for guidance tied to a place.

### Why create more than one bundle

Multiple bundles let you grant access by capability and compose it per channel. For example, with separate `data-readonly`, `github-write`, and `monitoring` bundles, `#platform-eng` gets all three, `#gtm-analytics` gets only `data-readonly`, and `#incidents` gets `monitoring` plus `github-write`. Each credential is defined once, so rotating a Datadog key means editing one bundle without touching the others.

## Connect a service that isn't in the list

The **Add a connector** list covers common services, not the full set Claude can connect to. Any app with an API can be connected. In the **Add a connector** dialog, select **Custom connector** at the bottom of the list. See the [custom connector guide](/docs/claude-tag/admins/connections/custom) for the form fields, credential types, and how to add a custom MCP server.

For a custom connector, choose the **Credential type** that matches how the service authenticates:

| Credential type | Use for |
| :- | :- |
| Bearer | API keys and OAuth bearer tokens. Most SaaS REST APIs. |
| Basic | HTTP Basic authentication. |
| Body parameter | A token the API expects in the request body or query string instead of a header. |
| AWS SigV4 | Signed requests to AWS service endpoints with an access key pair. |
| GCP access token (with Service Account Key) | Google Cloud APIs via a service-account JSON key. Google Workspace services like Drive and Calendar also use this; see [the Google guide](/docs/claude-tag/admins/connections/google). |
| GCP IAP (with Service Account Key) | Google Cloud services behind Identity-Aware Proxy. |
| OAuth 2.0 JWT bearer | Server-to-server OAuth. |
| OAuth 2.0 client credentials | Server-to-server OAuth. Salesforce uses this. |
| MCP Connector | Sign in once as an admin; the agent acts as that account. The picker offers a fixed set of providers plus the [remote MCP connectors](/docs/connectors/custom/add-unlisted) your organization has added on claude.ai. Other OAuth APIs can't be connected this way. |

For GitHub repositories, use the Claude GitHub App at [Configure GitHub access](/docs/claude-tag/admins/configure-github) rather than a credential from this table.

Credentials are injected at the network boundary by Agent Proxy; the model and the sandbox are not given the key. A request to a host you haven't allowed is blocked, not sent. See [how Agent Proxy works](/docs/claude-tag/concepts/agent-identity#agent-proxy).

You can also add connectors from a channel's [Configure page](/docs/claude-tag/users/good-habits#configure-claude-for-a-channel). The option to add one appears there only for people who can manage Claude's setup for that channel or for the whole organization. [Channel managers](/docs/claude-tag/admins/restrict-access#delegate-channel-setup-to-channel-managers) can manage setup for their assigned channels. Other channel members see the channel's connectors on the Configure page but can't add one.

## Allow a host without a credential

Claude does channel work in an isolated [sandbox](/docs/claude-tag/concepts/agent-identity#channel-sessions). A network request is traffic that sandbox sends to a host, such as an API call, a `curl` fetch, or a package install. Before Claude can make one from a channel, the destination host has to be allowed by one of three settings, the allow layers:

* **A domain entry**: a hostname added to a bundle that applies to the channel. Requests to it pass with no credential attached; see [Add a domain](#add-a-domain).
* **A [connector](#add-a-connector)**: a credential that applies to the channel. Requests matching its [allowed websites](#set-allowed-websites) pass with that credential attached.
* **The channel's [environment](/docs/claude-tag/concepts/glossary#environment)**: the compute configuration the channel's sessions run in, which carries its own network access setting, starting at the Trusted access level that covers common package registries. Requests to hosts it allows pass with no credential; see [Broad web access through the environment](#broad-web-access-through-the-environment).

A host that none of these allows stays unreachable, and when more than one bundle applies to a channel, the entries of all of them apply. Web search is governed by none of them, because searching happens on Anthropic's servers rather than in the sandbox; see [Web search vs. network requests](#web-search-vs-network-requests).

### Add a domain

A domain entry allowlists one hostname for every channel a bundle applies to. After you add it, requests from those channels' sandboxes to that host go through with no credential attached.

Open the bundle's page from the **Bundles** tab under **Claude's access** in [**Organization settings > Claude Tag**](https://claude.ai/admin-settings/claude-tag). Under **What's in it**, click **Add** and choose **Domain**. To add the domain for one workspace or channel instead, open that place's page from the **Channels** tab, click **Add** under **Claude's access**, and select **Domain**. Fill in the **Add a domain** dialog and click **Add**:

* **Domain**: the hostname to allow; a wildcard is allowed as the leftmost label, like `*.example.com`, and covers subdomains at any depth but not `example.com` itself
* **Ports**: `443` unless the service listens on another port
* **Advanced**: the HTTP methods the entry allows, **Read-only** (`GET`, `HEAD`, and `OPTIONS`) unless you change it. Select **All methods** or **Custom** for a host that needs other methods, such as the `POST` requests an MCP server or `git clone` sends

For example, to let Claude check a vendor's status page at `status.example.org`, enter `status.example.org` in the **Domain** field and leave the other fields as they are.

You don't have to predict the full list up front. When a request is blocked, Claude says so in the thread and names the host, with wording like "blocked by the network egress proxy" (that is, by Agent Proxy); add that host here and retry. If the host is listed and Claude still reports it blocked, check these in order:

* **The bundle applies to the channel.** The bundle's **Where it applies** list must include the channel, its workspace, a channel group that matches it, or **Slack**; see [Attach bundles to workspaces and channels](/docs/claude-tag/admins/attach-to-scope).
* **The entry matches the exact host.** A wildcard like `*.example.com` doesn't cover `example.com` itself, and `www.example.com` and `example.com` are different hosts.
* **The request didn't move to another host.** If the page redirects, or loads from a CDN or a sign-in host, allow that host too; Claude names the host it was blocked on.
* **The port is listed.** Needed only when the service listens on something other than 443.
* **The method is allowed.** A **Read-only** entry doesn't allow `POST`, `PUT`, `PATCH`, or `DELETE` requests to the host.
* **A minute has passed since you saved the entry.** Agent Proxy picks up a new entry within about a minute, in existing threads as well as new ones, so retry in the same thread after a short wait.
* **The bundle applied before the thread started.** A bundle added to a channel after a thread started isn't guaranteed to reach that thread, so start a fresh thread to use its entries.
* **The request came from a channel, not a DM.** A bundle added to a channel doesn't apply in DMs.

Typical entries are hosts the work calls without a key, such as a docs site or a public API. Common package registries are usually already reachable through the [environment's Trusted access default](#broad-web-access-through-the-environment), and a host that needs a credential belongs in a [connector](#add-a-connector) instead. Entries appear under **What's in it** with the type **Domain**, and each row's menu has **Edit** and **Remove**.

<Note>[Agent Proxy](/docs/claude-tag/concepts/agent-identity#agent-proxy) carries only HTTP and HTTPS. A protocol that isn't HTTP, such as SSH, can't cross the proxy, so a domain entry doesn't make a host reachable over SSH.</Note>

### Broad web access through the environment

Domain entries allow hosts one at a time. For a channel whose work needs more of the web, the environment setting grants broader access. An [environment](/docs/claude-tag/concepts/glossary#environment) is the sandboxed compute configuration the channel's sessions run in, and it carries its own network access setting.

A new environment's network access level is Trusted access, which allows a [documented set of package registries and developer hosts](https://code.claude.com/docs/en/cloud-environments#default-allowed-domains). A channel can already reach hosts like `pypi.org` and `registry.npmjs.org` with no domain entry.

To give a workspace or channel broader access, create an organization-shared environment with a more permissive level and set it on that place's page, under **Advanced > Sessions > Environment**, as described in [Configure the environment for a scope](/docs/claude-tag/admins/customize#configure-the-environment-for-a-scope). **Full access** allows any domain; see [Network access in the Claude Code docs](https://code.claude.com/docs/en/cloud-environments#network-access) for the other levels.

### Allow all hosts

To allow every host, enter `*` alone as the **Domain** in the **Add a domain** dialog. A `*` entry needs ports assigned. It admits requests to any host on those ports that use a method the entry allows, with no credential attached. A new entry is **Read-only** until you select **All methods** or **Custom** under **Advanced**, as [Add a domain](#add-a-domain) describes.

With `*` active:

* Requests the entry allows, to hosts that no connector covers, go through with no credential attached.
* A `*` entry never carries a credential, and a connector's credential still travels only to its [allowed websites](#set-allowed-websites).
* Private and internal network addresses and cloud metadata endpoints remain blocked.

<a id="web-search-vs-network-requests" />

### Web search vs. network requests

Web search needs no domain entry, connector, or environment setting. It's [Anthropic's built-in web search tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool), and the searching happens on Anthropic's servers rather than in the channel's sandbox, so no allow layer applies.

Opening a page is not part of the search. A search returns content from the pages it matches, which Claude reads and cites; fetching a URL from the sandbox is a network request, and the host needs an allow layer. Claude can answer from a page that search surfaced yet report that it can't open the same link.

If the work needs Claude to open and read pages rather than answer from search results, allow those hosts through the settings above. [Web search vs. network requests](/docs/claude-tag/concepts/agent-identity#web-search-vs-network-requests) covers the session mechanics behind the split.

## Attach plugins

A plugin is a packaged set of skills: reusable instructions for working with a specific tool or following a specific process. Add a plugin wherever its connector applies, so the credential arrives with directions for using it.

A Datadog API key, for example, makes the API reachable, and a Datadog plugin tells Claude which endpoints answer which questions. Sessions in the channels where you add a plugin pick it up automatically.

Where you add a plugin decides where it applies:

* **All of Slack**: under **Claude's access**, select the **Skills and plugins** tab, click **Add**, pick the plugin or skill, and click **Add**. To limit it afterward, open its page from the same tab and use **Assign access**.
* **Wherever a bundle applies**: on the bundle's page, under **What's in it**, click **Add** and choose **Plugin**.
* **One workspace or channel**: on that place's page, under **Claude's access**, click **Add** and select **Plugin** or **Skill**, then pick the plugin or skill in the dialog and click **Add**. The dialog lists only the plugins and skills already on the **Skills and plugins** tab. For one that isn't on the tab yet, add it there and then limit it under **Assign access** on its page, or add a plugin to a bundle that applies to the place.
* **Along with a connector**: when a connect form shows a checkbox to include the service's plugin, leave it selected to add that plugin with the credential.
* **By a channel member**: a member can ask Claude to add a plugin available to your organization, in the channel or from the channel's [Configure page](/docs/claude-tag/users/good-habits#configure-claude-for-a-channel), unless **Channel member edits** is set to **Block**; see [Restrict who can set channel instructions](/docs/claude-tag/admins/attach-to-scope#restrict-who-can-set-channel-instructions). Claude proposes the change and adds the plugin only after someone in that channel selects **Confirm**.

Anthropic provides plugins for common tools and processes, and you can add your own from a [skills repository](/docs/claude-tag/admins/skills-repo). To give Claude organization-wide skills, package them as a plugin. Adding a plugin to your organization's library on claude.ai makes it available to Claude, not active; it takes effect only where you add it in one of the ways above.

Adding or removing plugins and skills applies to new threads only. A thread already running keeps the set it began with; start a fresh thread to pick up changes. See [What survives between replies](/docs/claude-tag/concepts/how-it-works#what-survives-between-replies).

Claude can't publish a new skill version from inside a thread; that update happens in admin settings.

### Code review with the Security Guidance plugin

Anthropic's **Security Guidance** [plugin](https://code.claude.com/docs/en/plugins) has Claude review the code it writes. With the plugin on in a channel, Claude is warned about risky patterns as it edits files, and the plugin reviews the code changes in the session's repository when Claude commits, pushes, or finishes a reply, checking for vulnerabilities such as injection, cross-site scripting, and hardcoded secrets. Claude addresses the findings or reports them in the thread.

**Security Guidance** is off by default. Add it on the **Skills and plugins** tab or a bundle's page, and new threads in the channels it covers pick it up. The plugin flags problems and suggests fixes; it doesn't block a commit or a push. To require review before code merges, use your repository's branch protection and required checks.

<a id="verify-the-connection-saved" />

## Verify the connector saved

* The connector appears on the **Connectors** tab, under **Services** or **Custom hosts**.
* On the connector's page, the **Access from** table lists each credential with the hosts it's sent to, and its **Used at** column shows where it applies.
* A credential marked **Not enabled** is stored, but no allow rule sends it yet, so Claude can't use it. To let Claude reach its hosts with the credential, click **Enable** beside it and confirm.
* A credential a teammate submitted through a setup link waits on the **Requests** tab of [**Notifications**](https://claude.ai/admin-settings/notifications) as **Approval needed** until you review and approve it.
* New threads pick up new connectors on their own, and a connector that uses a key or token works in a thread that started before you added it.

## Related resources

* [Set a spend limit](/docs/claude-tag/admins/set-spend-limit): fund usage so the connectors you just added can run
* [Configure GitHub access](/docs/claude-tag/admins/configure-github): repository access, managed through the Claude GitHub App
* [How agent identity works](/docs/claude-tag/concepts/agent-identity#agent-proxy): how the credentials you just added reach Claude without entering its sandbox
