> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Analytics

> Review your organization's requests, tokens, spend, active users, top users, and credit balance over time, and download the data as CSV files for reporting.

> **Who this is for:** Organization owners who need to understand how their organization is using Claude and how quickly it is consuming credits.

The **Analytics** page shows requests, tokens, spend, top users, and credit balance over time across your organization. Usage figures on this page are compiled from the same metering that enforces your users' spend limits. Times are shown in your browser's time zone.

> [!NOTE]
>
> These cases are covered on other pages:
>
> * **How close each user is to their 5-hour and 7-day limits**: use the **Usage** bars on the [Users](https://claude.com/docs/government/org-admin/users.md#reset-usage-limits) page
> * **Usage records sent to your own collector**: see [Compliance and telemetry](https://claude.com/docs/government/config/settings.md#compliance-and-telemetry)

## Managed and self-managed views

**Anthropic-managed tiers** and **Self-managed tiers** are shown separately because their economics differ: managed-tier seats are purchased as seats, while self-managed tiers (tiers your organization created itself on the [Tiers](https://claude.com/docs/government/org-admin/seat-tiers.md) page) draw down the billing account's balance. Spend figures and the credit panel are shown only in the **Self-managed** view. If your organization has only one kind of tier, the page shows only the matching view.

## Credits (self-managed view only)

When credit data is available, the credit panel displays the **Credits remaining** for the account your organization draws from, with [how much was used and how much expired](https://claude.com/docs/government/org-admin/billing.md#billing-account) under it. A **Low balance** badge appears as the balance runs low, and a **Depleted** badge replaces it when no credits remain. When credits expire within 30 days, the panel also shows [how much expires next and the last day you can use it](https://claude.com/docs/government/org-admin/billing.md#billing-account), in UTC.

The panel's runway estimate tells you roughly how many days remain at your organization's own 7-day pace, its average daily spend over the trailing 7 days. The estimate leaves out any of the credits shown as expiring that you wouldn't spend in time. When the runway says "until your credits expire", it instead counts the days until your remaining credits expire, because they expire before you would spend them all.

The **Credit burndown** chart plots your balance, with markers on the days credits were added and the days credits expired. It projects forward at the 7-day pace to the date you are estimated to reach \$0. The projection steps down on the last day you can use the credits shown as expiring, by the amount that would go unspent.

## Active users

The **Active users** section shows how many distinct people used Claude over fixed periods, as daily, weekly, and monthly active users. A user counts as **active** if Claude answered them at least once in the period.

## Usage

Everything below the **Usage** divider is scoped to a time window that you choose, from **24 hours** to **90 days**. The figures are requests, input tokens, output tokens, and, in the self-managed view, estimated spend. Estimated spend includes input stored or reused through prompt caching. Input tokens do not, so token counts alone understate cost.

* The **By product** table breaks usage down by which Claude product it came from (for example, Claude Desktop or Claude Code). Chat and Cowork activity in Claude Desktop is counted together in a single Claude Desktop row. Code sessions in Claude Desktop run on Claude Code, so they are counted in the Claude Code row along with any use of the standalone Claude Code command-line tool.
* The **By model** table lists each model used in the window.
* The **Top users** table lists the users with the most tokens in the window, and each user's figures combine their usage across all products. Up to 100 users are listed individually, and beyond that a note tells you how many more are not listed. Usage from before a person's move stays with the organization they left.

## CSV exports

The **Download** menu saves what the page shows as CSV files. **All** downloads a ZIP archive of the current view, one CSV file per table. The other entries download one table each.

* **What an export covers.** Exports follow the view and the time window you have selected. The credit files match the burndown chart, reaching back 30 days, or 90 days when you select the **90 days** window. In the summary file, the credit figures are the account's position at the time of the export, not spend within the window.
* **Export context.** The ZIP archive includes an `export_info.csv` file recording the export's context, including when it was made, the organization, the view, the window and its date range, and the time zone the dates are in.
* **Per-user data.** The top users file lists the same users as the **Top users** table, up to 100, and adds each user's ID and account status to the columns shown on screen.

To read usage and estimated cost from a script, or for more than the top 100 users, use the [Analytics API](https://claude.com/docs/government/org-admin/analytics-api.md).
