# Get started with Claude Data

Claude Data turns questions about your company’s data into dashboards, data stories, narrated short videos, and letters. Connect a data warehouse or another app, ask a question in plain language, and Claude writes the queries and builds the result.

This guide covers connecting your data, creating and refining your work, and sharing it. Claude Data was previously called Claude Dashboards, and dashboards you’ve already made keep working.

Claude Data is available on Pro, Max, Ultra, Team, and Enterprise plans. Certified queries and live sharing are in beta. On Team plans, Claude Data and both beta features are on by default. On Enterprise plans, Claude Data turns on by default on November 19, 2026, unless an owner has already saved a setting, and both beta features are off by default.

## How Claude Data works

Claude writes a SQL query for each chart and runs it against your data source. Each chart shows its query, so you can see exactly what it’s counting, along with when its data was last refreshed.

Dashboards are one format you can make. You can also ask for:

- **Scrollyteller:** Scrolling stories built from your numbers

- **Visual short:** Short videos that walk through your numbers

- **Visual analysis:** Written summaries of your numbers

Dashboards are made for quick, exploratory questions, like how this week’s signups compare with last month’s. When a question needs deeper analysis, send the dashboard to another tool and continue there.

Everything you create is saved in the **Artifacts** tab. Learn more about **[artifacts and how to use them](https://support.claude.com/en/articles/17153992)**.

## Connect your data

Before you create anything, connect the data you want to ask about:

- **A data warehouse:** Connect your company’s data platform, such as Amazon Redshift, BigQuery, ClickHouse, Databricks, or Snowflake.

- **Other apps you’ve connected to Claude:** For example, ask for a dashboard of your Salesforce opportunities.

Learn more about **[connecting your apps to Claude](https://support.claude.com/en/articles/11176164)**.

## Create with Claude Data

### From a chat

Ask Claude in any chat. For example:

- "Build a dashboard of this quarter’s revenue by region."

- "Show weekly signups for the last six months, split by plan."

- "Turn this quarter’s revenue numbers into a data story."

### From the Artifacts tab

1. Go to the "Artifacts" tab.

2. Select "Data."

3. Describe what you want to make.

### Tips for better results

Say what you want to know, not just what to chart. "How do this month’s signups by channel compare with last month’s?" gets you further than "a signups chart." If the data lives in a specific table or app, name it.

### Refine your work

- **Ask Claude:** Ask for changes in the chat, like "Add a filter for region" or "Change this to a weekly view."

- **Edit directly:** Click a title, caption, or chart to change it yourself, without asking Claude.

- **Check the query:** Open a chart’s query to see how Claude got the number. If it isn’t counting what you meant, tell Claude what to change.

### Restore an earlier version

Version history shows earlier versions. Edits you make directly appear there too.

1. Open the dashboard and open its version history.

2. Select a version to preview it. The preview is read-only and doesn’t change the dashboard.

3. Click "Restore."

The dashboard returns to that version for everyone who opens it, and the restore appears as its own entry in version history. People with view-only access can’t edit a dashboard or restore a version.

### How data refreshes

Claude refreshes a dashboard's data when someone opens it and the data is due for a refresh. It doesn't refresh on a schedule, but **Refresh data** intelligently re-queries for data based on specified interval and user access patterns.

## Use certified queries (beta)

Certified queries are the official queries your data team has approved. Claude can reuse them when it builds new dashboards. Charts built on certified queries carry a badge. To check a number, click it or open the data sidebar.

Your data team can certify queries in directly Claude, or use the definitions it already has in dbt, Looker, or Cube (via existing MCP connectors).  Anyone with write access to a Data artifact can certify.

**To certify a query:**

1. Open a chart’s query and edit it.

2. Turn on "Certify query."

3. Add any instructions for Claude, one per line.

4. Click "Test."

5. Click "Publish."

The query shows as certified after a check finishes.

**Note:** Editing a certified query removes its certification. To remove a certification yourself, turn off "Certify query" and click "Publish." Dashboards that use that query lose their certified badge.

If your organization stores certified queries in a Git-backed plugin, manage them in GitHub with pull request review instead.

## Share and send your work

Everything you make in Claude Data starts private to you. To share it, open it and click "Share." They can also be shared outside your organization. Learn more about **[sharing artifacts](https://support.claude.com/en/articles/9547008)**.

## Share live results with your organization (beta)

Without live sharing, a shared dashboard loads its data with each person's own connections. With live sharing, people in your organization can see results from yours, including saved results. It's limited to the exact queries the dashboard needs, and those can't change without an editor's approval.

To turn on live sharing, visit the **Sources** menu on an artifact and select "Your access" next to each MCP connector.

**Important:** Live sharing runs on your access to the data source. Anyone you share the dashboard with sees those results, even if they don’t have access to that source. Check what a dashboard shows before you share it this way.

## Usage

Claude Data counts toward your plan’s usage limits, like the rest of your work with Claude. Learn more about **[how usage and length limits work](https://support.claude.com/en/articles/11647753)**.

## Turn on Claude Data for your organization

This section is for Owners and Primary Owners on Team and Enterprise plans.

Owners manage Claude Data in **[Organization settings > Artifacts](https://claude.ai/admin-settings/artifacts)**, under **Templates**. Certified queries and live sharing have their own settings under **Data**. On Enterprise plans, owners can limit Claude Data to specific groups with custom roles. Learn more in the **[Artifacts admin guide for Team and Enterprise plans](https://support.claude.com/en/articles/16994751)**.