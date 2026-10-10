# Get started with Claude Dashboards

Claude Dashboards turn questions about your company's data into dashboards. Connect a data warehouse or another app, ask a question in plain language, and Claude writes the queries and builds the dashboard. This guide covers connecting your data, creating and refining a dashboard, and sharing it.

Claude Dashboards is available in beta on Pro, Max, Team, and Enterprise plans. On Enterprise plans, it's off by default until an owner turns it on in **[Organization settings > Artifacts](https://claude.ai/admin-settings/artifacts)**.

## How Claude Dashboards works

A dashboard is an artifact made from the Dashboards template. Claude writes a SQL query for each chart and runs it against your data source. Each chart shows its query, so you can see exactly what it's counting, along with when its data was last refreshed.

Dashboards are made for quick, exploratory questions, like how this week's signups compare with last month's. When a question needs deeper analysis, send the dashboard to another tool and continue there.

Every dashboard you create is saved in the **Artifacts** tab. Learn more about **[artifacts and how to use them](https://support.claude.com/en/articles/17153992)**.

## Connect your data

Before you create a dashboard, connect the data you want to ask about:

- **A data warehouse:** Connect your company's data platform, such as Amazon Redshift, BigQuery, ClickHouse, Databricks, or Snowflake.

- **Other apps you've connected to Claude:** For example, ask for a dashboard of your Salesforce opportunities.

Learn more about **[connecting your apps to Claude](https://support.claude.com/en/articles/11176164)**.

## Create a dashboard

### From a chat

Ask Claude for a dashboard in any chat. For example:

- "Build a dashboard of this quarter's revenue by region."

- "Show weekly signups for the last six months, split by plan."

- "Make a dashboard of my open Salesforce opportunities by stage and owner."

You can also select "Output" in the message box and choose "Dashboards."

### From the Artifacts tab

1. Go to the "Artifacts" tab.

2. Select a Dashboards template.

3. Describe the dashboard you want.

### Tips for better results

Say what you want to know, not just what to chart. "How do this month's signups by channel compare with last month's?" gets you further than "a signups chart." If the data lives in a specific table or app, name it.

## Refine your dashboard

- **Ask Claude:** Ask for changes in the chat, like "Add a filter for region" or "Change this to a weekly view."

- **Check the query:** Open a chart's query to see how Claude got the number. If it isn't counting what you meant, tell Claude what to change.

## Share and send a dashboard

Dashboards start private to you. To share one, open it and click "Share." Learn more about **[sharing artifacts](https://support.claude.com/en/articles/9547008)**.

## Usage

Claude Dashboards counts toward your plan's usage limits, like the rest of your work with Claude. Learn more about **[how usage and length limits work](https://support.claude.com/en/articles/11647753)**.

## Turn on Claude Dashboards for your organization

This section is for Owners and Primary Owners on Team and Enterprise plans.

Owners turn Claude Dashboards on or off in **[Organization settings > Artifacts](https://claude.ai/admin-settings/artifacts)**. On Enterprise plans, it's off by default, and owners can limit it to specific groups with custom roles. Learn more in the **[Artifacts admin guide for Team and Enterprise plans](https://support.claude.com/en/articles/16994751)**.