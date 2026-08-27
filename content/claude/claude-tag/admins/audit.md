> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Review what Claude Tag has done

> Claude Tag actions appear under its own service accounts in each connected tool's audit log. See what the Audit page covers, how to trace an action to its source, and where each connected tool keeps logs.

export const BetaNote = () => <Info>Claude Tag is in public beta. Features and behavior described here may change before general availability.</Info>;

<BetaNote />

Use this page to review what Claude Tag is doing across your organization: which routines are scheduled, what memory it has saved, and where to find a record of each action it took.

<Note>The Audit page opens for Owners in your Claude organization; the other trails on this page are visible to anyone with access to the underlying surface.</Note>

Claude Tag activity is auditable in four places:

* **[The Audit page](#what-the-audit-view-lists)** in admin settings, with tabs for scheduled work, memory, and network events
* **Memory files on each scope** (select the scope in the **Claude Tag's access** section, then choose **View memory files** from its **⋯** menu), where you can review what Claude has saved
* **[Attribution on each action](#trace-an-action-to-its-source)** Claude takes in a connected tool
* **[The audit logs of each connected service](#trace-an-action-to-its-source)**, where its actions appear under the service account you provisioned

## What the Audit view lists

The Audit page, labeled **Activity** in the admin console's left nav and page heading, at [`claude.ai/admin-settings/claude-tag/audit`](https://claude.ai/admin-settings/claude-tag/audit) has these tabs:

| Tab                | What it shows                                                                                                                                                     |
| :----------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Scheduled work** | Every routine across your organization, with a **Scope** filter and a per-row **⋮** menu (View details, Pause/Resume, Delete)                                     |
| **Memory**         | Each scope's memory files, where you can read what Claude has saved for that workspace or channel. Owners can also edit or delete entries there.                  |
| **Network events** | An hourly JSON export of outbound calls Claude made through Agent Proxy. Git and MCP traffic are not included in this export. Select a date and hour to download. |

Each routine on the **Scheduled work** tab shows **Created by** (the member who set it up) in its **View details** dialog. There is no per-action log of every task and who asked; for that, use the trails below.

## Trace an action to its source

In channels, Claude acts as itself, so each action there carries the service-account identity:

* **In Slack**, it posts as the Claude app, and its work happens in threads anyone in the channel can read.
* **On code**, commits and pull requests show the Claude GitHub App as the author, and each one links back to the Slack thread it came from.
* **In every other connected service**, actions appear under the service account you created for the connection.

That last one is the general-purpose trail: because you provisioned the credential, the connected service's audit log shows everything Claude did there, under an account your security team already monitors.

The [See it work](/docs/claude-tag/admins/test-it) page uses this check to validate a new connection.

## See what's scheduled in a channel

Anyone in the channel can see its standing work. Ask in the channel:

```text wrap theme={null}
@Claude what triggers do you have set up in this channel?
```

Claude lists the channel's scheduled jobs and watches, and anyone there can ask it to disable one.

Routines run with the channel's credentials, so the channel listing is also the permission picture. See [proactivity](/docs/claude-tag/users/proactivity#manage-standing-work).

## Related resources

* [How agent identity works](/docs/claude-tag/concepts/agent-identity): how attribution differs in channels and DMs
* [Restrict where Claude Tag operates](/docs/claude-tag/admins/restrict-access): the controls when an audit turns something up
* [Security and data handling](/docs/claude-tag/concepts/security-and-data): the model behind the trails
