# Cost and Usage Reporting in the Claude Console

**Note:** Usage and Cost reporting is visible to the following user roles: **Developer, Billing, and Admin**. See [Claude Console Roles and Permissions](https://support.claude.com/en/articles/10186004-claude-console-roles-and-permissions) for more information.

The Claude Console provides detailed cost and usage reporting to help you effectively manage your API usage and associated costs. This guide walks you through these features and how to use them.

## Accessing Cost and Usage Reports

Users with access to these reports can click into them on the left navigation menu on the Console:

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/1584654217/db0a977417e38e43639f060d96e0/image.png?expires=1785228300&amp;signature=cdd6352f9b43a0e6843bde276b3e9d7f7298cd86b2f9846520c28fdf6eb84c19&amp;req=dSUvEs97mYNeXvMW1HO4zYCWiSEag86ZuqqBX2puyxRRXyFAyyNZnho6O5CZ%0A5m%2BNF3tp63i6KGCuZPM%3D%0A)

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

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/1584664321/59b50eba0b61e0789f7055fcf9f4/image+%285%29.png?expires=1785228300&amp;signature=fdb2d1b5d8a392f31ebe6d8a8e8dfc74e2b3713b68711f5f9bae89c4f6d5adfb&amp;req=dSUvEs94mYJdWPMW1HO4zQwER3YoI4dlqMITUZbanFCxR1SS0PQJeSv7BU%2FQ%0A%2FS%2BAUpwZAVTFDqFnAn0%3D%0A)

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/1584693386/aed472efe163abcbc14fa32f3699/rate+limited+requests.png?expires=1785228300&amp;signature=70d927fcd20d3d26d6db5c98afac7349c58b87795a1523c132e87d1aae6c1852&amp;req=dSUvEs93noJXX%2FMW1HO4zRxEwW5P5Flv21D6pckxWMauLlWsG5wMpR7kYeZa%0Ag%2FES2Kq4egkDhjZ3FqE%3D%0A)

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

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/1584679401/4d0bc8ed08625e1adee414e77030/CleanShot+2025-06-23+at+08_54_40%402x.png?expires=1785228300&amp;signature=d69f742a5f3c687a934d643f0a79d70be962cb4f77e2ab69f90ce67b3f848ea6&amp;req=dSUvEs95lIVfWPMW1HO4zUR%2Bh5nBUdhiCyIF5nuUsbxZ4ozp1XwWXTNf4AI7%0A%2BJtjGlIcbCJ%2FTZJkwG4%3D%0A)

**Note**: Currently, it's not possible to break down usage or cost by individual users.