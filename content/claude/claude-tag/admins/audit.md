> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Review what Claude Tag has done

> Claude Tag actions appear under its own service accounts in each connected tool's audit log. See what the Activity page covers, how to trace an action to its source, and where each connected tool keeps logs.

> [!NOTE]
>
> Claude Tag is in public beta. Features and behavior described here may change before general availability.

Use this page to review what Claude Tag is doing across your organization: which routines are scheduled, what memory it has saved, and where to find records of its actions.

The **Activity** page opens for Owners of your Claude organization. The other trails on this page are visible to anyone with access to the underlying surface.

Claude Tag activity is auditable in these places:

* **[The Activity page](#what-the-activity-page-lists)** in admin settings, with tabs for scheduled work, memory, and network events
* **Memory files** for each workspace, and for each channel that has memory of its own (open the workspace's or channel's page from the **Channels** tab under **Claude's access**, then choose **View memory files** from its **⋯** menu, if the menu lists it), where you can review what Claude has saved
* **[Attribution on each action](#trace-an-action-to-its-source)** Claude takes in a connected tool
* **[The audit logs of each connected service](#trace-an-action-to-its-source)**, where its actions appear under the service account you provisioned
* **[Session transcripts](#read-claude-tag-session-transcripts)**, which you read through the Compliance API on the Enterprise plan

## What the Activity page lists

To open the **Activity** page, go to [`claude.ai/admin-settings/claude-tag/audit`](https://claude.ai/admin-settings/claude-tag/audit), or select **Claude Tag** in the admin settings sidebar and then **Activity** under it. The page has these tabs:

| Tab | What it shows |
| :- | :- |
| **Scheduled work** | The routines set up in channels across your organization, with a **Scope** filter and a per-row **⋮** menu with actions such as **View details**, **Pause** or **Resume**, and **Delete** |
| **Memory** | Each scope's memory files, where you can read what Claude has saved for that workspace or channel. Owners can also edit or delete entries there. |
| **Network events** | A best-effort hourly JSON export of the outbound requests Claude made through [Agent Proxy](https://claude.com/docs/claude-tag/concepts/agent-identity.md#agent-proxy). Git and MCP traffic are not included, and [other requests can be missing](#what-the-network-events-export-can-miss). Select a date and hour to download. |

Each routine on the **Scheduled work** tab shows **Created by** (the member who set it up) in its **View details** dialog. There is no per-action log of every task and who asked. To follow up on one action, see [Trace an action to its source](#trace-an-action-to-its-source).

### What the network events export can miss

The export on the [**Activity** page's](https://claude.ai/admin-settings/claude-tag/audit) **Network events** tab is best effort. A request can go through without an entry in the export, so a missing entry doesn't show that Claude didn't make the request.

To find out whether Claude made a request to a connected service, check [that service's audit log](#trace-an-action-to-its-source) as well as the export. On the Enterprise plan with the [Compliance API](https://platform.claude.com/docs/en/manage-claude/compliance-api-access) enabled, also check the [session's transcript](#read-claude-tag-session-transcripts), which includes Claude's tool calls and their results.

## Read Claude Tag session transcripts

If your organization is on the Enterprise plan and has the [Compliance API](https://platform.claude.com/docs/en/manage-claude/compliance-api-access) enabled, you can [list Claude Tag sessions and read their transcripts](https://platform.claude.com/docs/en/manage-claude/compliance-sessions#retrieve-remote-sessions) through the API. A transcript includes the text of prompts, Claude's responses, and tool calls with their results.

## Trace an action to its source

In channels, Claude acts as itself unless a task uses a member's [personal connectors](https://claude.com/docs/claude-tag/concepts/personal-connectors.md), which run with that member's permissions and are recorded under their name. Each action Claude takes as itself carries the service-account identity:

* **In Slack**, it posts as the Claude app, and its work happens in threads anyone in the channel can read.
* **On code**, commits and pull requests show the Claude GitHub App as the author, and each one links back to the Slack thread it came from.
* **In every other connected service**, actions appear under the service account you created for the connector.

That last one is the general-purpose trail: because you provisioned the credential, the connected service's audit log shows Claude's actions under an account your security team already monitors.

## See what's scheduled in a channel

Anyone in the channel can see its standing work. Ask in the channel:

```text wrap theme={null}
@Claude what triggers do you have set up in this channel?
```

Claude lists the channel's scheduled jobs and watches, and anyone there can ask it to disable one.

Routines run with the channel's credentials, so the channel listing is also the permission picture. See [proactivity](https://claude.com/docs/claude-tag/users/proactivity.md#manage-standing-work).

## Related resources

* [How agent identity works](https://claude.com/docs/claude-tag/concepts/agent-identity.md): how attribution differs in channels and DMs
* [Restrict where Claude Tag operates](https://claude.com/docs/claude-tag/admins/restrict-access.md): the controls when an audit turns something up
* [Security and data handling](https://claude.com/docs/claude-tag/concepts/security-and-data.md): the model behind the trails
