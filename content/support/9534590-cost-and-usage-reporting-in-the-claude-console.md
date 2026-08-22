# Cost and Usage Reporting in the Claude Console

**Note:** Usage and Cost reporting is visible to the following user roles: **Developer, Billing, and Admin**. See [Claude Console Roles and Permissions](https://support.claude.com/en/articles/10186004-claude-console-roles-and-permissions) for more information.

The Claude Console provides detailed cost and usage reporting to help you effectively manage your API usage and associated costs. This guide walks you through these features and how to use them.

## Accessing Cost and Usage Reports

Users with access to these reports can click into them on the left navigation menu on the Console:

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/1584654217/db0a977417e38e43639f060d96e0/image.png?expires=1787399100&amp;signature=6f31405532dc60fc2cbe5217824aa69cfdaa7b37993db4c36984eb12055f63d9&amp;req=dSUvEs97mYNeXvMW1HO4zYCWiSMbiM%2BbuqqBX2puyxS0ZwdFdx1le6bvneMH%0AViGT%2BEGyLvH69qhbhd8%3D%0A)

---

## Usage Reporting

The [Usage page](https://platform.claude.com/usage) offers a detailed breakdown of your API usage across different models and API keys.

### Key Features

- **Detailed Breakdown**: View usage data by model, date/time, and API key. Click into the bars on the bar chart for hour and minute granularity.

- **Flexible Filtering**: Use selectors to choose specific models, months, or API keys

- **Visual Representation**: A chart with input and output token counts.

- **Usage Statistics**: See total input and output tokens for your selected filters.

- **Rate-Limited Requests:** Review your requests that were blocked due to hitting rate limits.

- **Rate Limit Use:** Visualizations of input and output tokens per minute compared with the overall ITPM or OTPM rate limit.

- **CSV Export**: Download your usage data for further analysis or reporting.

### How to Use

1. Select the Workspace you want to view (or choose "All Workspaces").

2. Select the model you want to view (or choose "All Models").

3. Choose the month you're interested in (or narrow to a specific month/day).

4. Select an API key (or view data for all keys).

5. The chart and statistics will update based on your selections.

6. Use the export button to download a CSV of the displayed data.

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/1584664321/59b50eba0b61e0789f7055fcf9f4/image+%285%29.png?expires=1787399100&amp;signature=4605f610f80b8ae4df10cf9b57078d205bf966645ea3c6bb898cf9e317401d33&amp;req=dSUvEs94mYJdWPMW1HO4zQwER3QpKIZnqMITUZbanFC3vl30k%2BE%2BGKgnXPvp%0Ahl9Vbklcq7LlFJt1uYQ%3D%0A)

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/1584693386/aed472efe163abcbc14fa32f3699/rate+limited+requests.png?expires=1787399100&amp;signature=4a38662cfa384f19fa58b9a0a05753334839cfca2d744046108f8b6dd385d534&amp;req=dSUvEs93noJXX%2FMW1HO4zRxEwWxO71ht21D6pckxWMZsius5mmhURWpar%2F2x%0A1%2BrIro3fGdAVnmbQbqw%3D%0A)

### Rate Limit Use

The Usage page also includes a separate section displaying rate limit use per-model for input and output tokens. You can click the dropdown in the upper left corner of this section to change the model and view related rate limit metrics. These visualizations can be used to determine when you’re hitting peak use for your organization, which specific rate limits need to be increased, and how you can increase your caching rate.

**Rate Limit Use + Caching - Input Tokens:** This chart displays the hourly maximum number of uncached input tokens per minute (ITPM) alongside your cache rate (i.e. the percentage of input tokens read from the cache) and your current ITPM rate limit.

**Rate Limit Use - Output Tokens:** This chart displays the hourly maximum number of output tokens per minute (OTPM) alongside your current OTPM rate limit.

---

## Cost Reporting

The [Cost page](https://platform.claude.com/cost) helps you understand your spending across different models.

### Key Features

- **Model-Specific Data**: View costs for individual models or all models combined.

- **Monthly Breakdown**: See costs for specific months.

- **Daily Cost Chart**: Visualize your spending over time.

- **Total Cost Statistics**: Get an overview of your total spending for the selected period, including web search and code execution costs.

- **CSV Export**: Download cost data for your records for further analysis.

### How to Use

1. Choose the Workspace you want to view costs for (or select "All Workspaces").

2. Choose the model you want to view costs for (or select "All Models").

3. Select the month you're interested in.

4. You can see the chart, token cost, and tool use costs, which will update based on your selections.

5. Use the export button to download a CSV of the cost data.

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/1584679401/4d0bc8ed08625e1adee414e77030/CleanShot+2025-06-23+at+08_54_40%402x.png?expires=1787399100&amp;signature=d989fc3bb6a60b9db1451e4666b4c00fd0b206f70a09723ab217479f2d209881&amp;req=dSUvEs95lIVfWPMW1HO4zUR%2Bh5vAWtlgCyIF5nuUsbyQX2v%2BAt1zjXSMQWeY%0AJYJiZBJgKn%2B3ag4xFN0%3D%0A)

**Note**: Currently, it's not possible to break down usage or cost by individual users.