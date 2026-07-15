# Use analytics chat to ask Claude about usage

Analytics chat lets you ask Claude questions about your organization’s usage in plain language. Instead of clicking through dashboard tabs or exporting data, type a question. Claude runs the right query against your organization’s data and responds with a chart and a short summary of what it found.

Analytics chat is available on the Enterprise plan. Access requires the same permissions as the rest of the analytics dashboard.

## Access analytics chat

If you can already see the **All activity** view under Analytics, you have access to analytics chat.

1. Sign in to your Claude account.

2. In the left sidebar, select “Analytics.”

3. Click the “Analytics Chat” tab.

---

## How it works

Type a question, or select one of the suggested prompts below the input box. Claude matches your question to the closest supported query, runs it against your organization’s pre-aggregated usage data, and returns:

- A chart, table, or stat card rendered directly in the conversation, which you can expand, drill into, and export.

- A brief written summary calling out the key trend or numbers.

You can follow up in the same conversation. Claude keeps context, so you can refine a result ("what about just last week?"), drill in ("break that down by product"), or pivot to a related metric without starting over.

---

## What you can ask

Analytics chat answers questions across these areas.

### Active users and adoption

- "Show me daily, weekly, and monthly active users"

- "How did our key metrics change week over week?"

- "Is our stickiness going up or down?"

### Spend

- "Show me daily spend for the last 30 days"

- "Break down spend by model"

- "Compare spend on Claude vs Claude Code"

- "What's our cost per active user?"

- "What will we spend this month at the current rate?"

### Seats and users

- "What's our seat utilization rate?"

- "Which seats haven't been used in 30 days?"

- "Who are our top spenders?"

- "Who are our least active users?"

- "How many pending invites do we have?"

### Groups and teams

- "Which teams doubled their Claude usage this month?"

- "Where are we getting the most value per seat?"

- "Show me spend by group"

### Claude Code and Claude Cowork

- "Show me Claude Code adoption"

- "What percentage of our users are using Claude Code?"

- "Show me Cowork adoption"

- "Which connectors are Cowork users using?"

### Connectors and skills

- "Which connectors are being used?"

- "Which skills are being used most?"

By default, results cover the **last 30 days**, but you can specify a different range in your question. For example: "show me daily spend since January 1."

---

## Review the results

### The chart is the answer

It renders inline, and Claude’s summary below it calls out direction and magnitude of change—for example, "spend dropped roughly 40% starting March 12." Claude won’t judge whether a number is good or bad for your organization, but you can ask it to compare against a prior period.

### Data is refreshed daily

Analytics chat reads from tables that are typically updated within one to two days. The date shown on each result reflects the most recent data available and isn’t real-time.

### User-level results are capped

Queries that list individual users (top spenders, inactive seats, least active users) return up to 20 users at a time.

---

## Export and share results

When Claude returns a chart, hover over it and click to download it. You can share the exported file with stakeholders who don't have access to the analytics dashboard.

---

## Limitations

- **Analytics questions only.** Analytics chat is scoped to your organization’s usage data. If you ask an unrelated question, Claude will suggest starting a regular conversation instead. Web search, file uploads, and connectors aren't available here.

- **Your organization only.** Results are always scoped to the organization you’re signed into. Cross-organization comparisons aren’t available.

---

## Tips

- **Start with a suggested prompt.** The chips below the input show common starting points. Selecting one is the fastest way to see what's available, and you can refine from there.

- **Ask follow-ups instead of starting over.** After any chart, "now compare that to last month" or "show me just Claude Code" will refine the result in place.

- **Be specific about dates.** "Last 30 days" is the default; say "for March" or "year to date" to change the window.

---

## Troubleshooting

### A query times out or shows raw data instead of a chart

Queries can take up to two minutes for large organizations. If one repeatedly fails, try a shorter date range, or contact support and include a screenshot of the result.

### Data looks out of date

Check the date shown on the result. The underlying data typically lags by one to two days. If it’s more than two days behind, **[contact Support](https://support.claude.com/en/articles/9015913-how-to-get-support)**.

### The Analytics Chat tab is missing

Confirm your organization is on the Enterprise plan and that your account has access to the analytics dashboard. If you’re an admin and still don’t see it, contact your Anthropic account team.