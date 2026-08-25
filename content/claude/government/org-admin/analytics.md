> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Analytics

> Use this page to review requests, tokens, spend, top users, and credit balance over time across your organization, and to download the data as CSV files for offline reporting.

> **Who this is for:** Organization owners who need to understand how their organization is using Claude and how quickly it is consuming credits.

Use this page to review requests, tokens, spend, top users, and credit balance over time across your organization, and to download the data as CSV files for offline reporting.

Because this data takes a moment to compute, the page starts with a **Load analytics** button. After the data loads, the results are cached for the rest of your session. You can click **Refresh** to fetch the latest numbers, and this button becomes available again 30 seconds after the previous load.

A **Download** menu next to **Refresh** saves what the page shows as CSV files, described in [CSV exports](#csv-exports).

## How the data is gathered

Usage figures on this page are compiled from the same metering that enforces your users' rate limits, so the request, token, and spend numbers here will closely match what your users experienced. All times are shown in your browser's time zone; if your browser reports a time zone the service does not recognize, times fall back to UTC.

## Managed and self-managed views

A control at the top switches between **Anthropic-managed tiers** and **Self-managed tiers**. The two are shown separately because their economics differ: managed-tier seats are purchased as seats, while **self-managed tiers** (tiers your organization created itself on the [Tiers](/docs/government/org-admin/seat-tiers) page) draw down the billing account's balance. Spend figures and the credit panel are therefore shown only in the **Self-managed** view.

If your organization has only one kind of tier, the control does not appear and the page shows only the matching view. If all of your seat tiers are Anthropic-managed, you see only the managed view, with no spend figures, credit panel, or burndown chart.

## Credits (self-managed view only)

<Note>
  The credit panel and burndown chart only appear in the **Self-managed tiers** view, and only once credit data is available for your organization. The runway estimate within the panel only appears once there has been enough recent activity to compute a burn rate.
</Note>

When credit data is available, the credit panel shows the current position of the account your organization draws from as of right now. It displays the **Credits remaining** out of the total added to the account, with a progress bar marked at the 70 percent and 90 percent warning thresholds. It also shows a runway estimate that tells you roughly how many days remain at your trailing 7-day burn rate. A **Low balance** badge appears once 70 percent of the total has been used, and a **Depleted** badge replaces it when no credits remain.

The runway figure divides your remaining balance by your average daily spend over the last seven complete days. It is shown as "less than 1 day" when the balance is nearly exhausted and as "more than 180 days" when spend is low enough that a longer projection would not be meaningful. If there has been no spend at all in the last seven days, no runway is shown.

Below the panel, the **Credit burndown** chart plots your balance, with markers on the days credits were added, and projects forward to the date you are estimated to reach \$0. The chart reaches back 30 days, or 90 days when you set the time-window selector described below to **90 days**.

<Tip>
  The credit panel always reflects the current position and is not affected by the time-window selector. The 7-day lookback used for the burn rate is also fixed and does not change when you switch the usage window.
</Tip>

## Active users

The **Active users** section shows how many distinct people used Claude over fixed periods: the average number of daily active users over the last 7 days, the number of weekly active users over the last 7 days, and the number of monthly active users over the last 30 days. These figures always use the same fixed lookbacks and are not affected by the time-window selector below.

## Usage

Everything below the **Usage** divider is scoped to a time window that you choose with the **24 hours**, **7 days**, **30 days**, or **90 days** selector.

The summary tiles show the number of requests, the input and output token counts (a token is roughly a piece of a word, and it is the unit that Claude's usage is measured in), and, in the self-managed view, the estimated spend for the selected window.

The **Token usage** chart plots input and output tokens over the window. It shows hourly data when you select the 24-hour window and daily data for the longer windows.

The **Active users over time** chart plots the number of distinct users who made at least one request in each period of the window, using the same hourly or daily buckets as the token chart.

The **By product** table breaks usage down by which Claude product it came from (for example, Claude Desktop or Claude Code), with the same request, token, and spend columns as the other tables. This table only appears once your deployment has recorded usage from at least one product.

The **By model** table lists each model used in the window along with its request count, input tokens, output tokens, and, in the self-managed view, its spend.

The **Top users** table lists the most active users in the window with the same columns. The table starts with ten rows, and you can click **Show more** to reveal additional users. Up to 100 users are listed individually, and beyond that a note tells you how many more are not listed.

## CSV exports

The **Download** menu at the top of the page, next to **Refresh**, saves what the page shows as CSV files. **All** downloads a ZIP archive of the current view, one CSV file per table. The other entries download one table each: **Summary**, **Usage over time**, **By product**, **By model**, and **Top users**, with **Credit burndown** and **Credit top-ups** added in the self-managed view. The menu becomes available again 30 seconds after the previous download.

Exports follow the view and the time window you have selected. The credit files match the burndown chart, reaching back 30 days, or 90 days when you select the **90 days** window. In the summary file, the credit figures are the account's position at the time of the export, not spend within the window.

The ZIP archive includes an `export_info.csv` file recording the export's context, including when it was made, the organization, the view, the window and its date range, and the time zone the dates are in. In the self-managed view it also records the date range the credit files cover.

File names state the view, the time span, and the dates covered, and single-table files also name their table.

The top users file lists every user the **Top users** table can show, whether or not you have expanded the table with **Show more**, and adds each user's ID and account status to the columns shown on screen.

## Things to know

* Claude for Government does not currently offer a programmatic usage or analytics API. Usage data is available through this admin portal page. The [Compliance API](/docs/government/org-admin/compliance-api) returns governance and audit events, not usage metrics.
* A user counts as **active** in the selected window if they made at least one request in it, regardless of which seat tier they were on at the time.
* The **spend** column appears only in the self-managed view and is the amount debited from your billing account's balance. The managed view has no spend column because managed-tier usage is covered by the seat price rather than by credit drawdown.
* To see how close each user is to their 5-hour and 7-day limits, use the **Usage** bars on the [Users](/docs/government/org-admin/users) page. The **Top users** table on this page shows how much each listed user consumed in the window, not how close they are to a limit.
* If the credit panel is missing from the self-managed view, credit data for your organization's billing account is unavailable. The rest of the page will still load.
* Usage that was cleared with **Reset usage limits** on the [Users](/docs/government/org-admin/users) page still appears here. The reset only clears the counter that enforces a user's limit; it does not remove the activity from analytics.
