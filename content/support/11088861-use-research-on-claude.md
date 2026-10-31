# Use research on Claude

With research, Claude investigates your question in depth. It runs multiple searches that build on each other and decides what to look into next based on what it finds. It explores different angles of your question and works through open questions systematically.

Research is available for users with paid Claude plans (Pro, Max, Ultra, Team, or Enterprise) using Claude on the web, Claude Desktop, or Claude Mobile.

## Enable or disable research

**Important:**  You must have **[web search](https://support.claude.com/en/articles/10684626)** turned on for research to function.

Click the “+” button on the bottom left of your chat interface, then "Research." A blue indicator will appear on the bottom of the chat window. Click the indicator again to disable research.

## Use research

Once research is turned on, you can ask Claude a question. Claude researches the web and your connected tools, including **[Google Workspace](https://support.claude.com/en/articles/10166901)** (Gmail, Google Calendar, and Google Docs) and any other connectors you’ve turned on for the chat. During research, Claude can use tools from your connectors automatically, without asking for approval each time. Learn more about **[custom connectors](https://support.claude.com/en/articles/11175166)**.

**Important:** When you start research in Claude Mobile, Claude only searches the web and doesn’t use your connectors. You won’t see an error or other sign that your connectors were skipped. To include your connectors, start research in Claude on the web or in Claude Desktop. Note that research can’t use tools from local MCP servers configured in Claude Desktop.

To see an example of using Claude's research feature to plan a team offsite, watch the video here: **[Using research](https://claude.com/resources/tutorials/using-research)**.

---

## Frequently asked questions

### I enabled research, but Claude doesn’t seem to be researching. What should I do?

In this case, you can steer and prompt Claude to use Research by saying “Claude, please use the research tool to…”

### Research isn’t pulling from my connectors. What should I do?

If you started research in Claude Mobile, Claude only searches the web. Start research in Claude on the web or in Claude Desktop instead. Otherwise, steer and prompt Claude to “Pull relevant context from [relevant internal knowledge source].”

### Does research count against usage limits differently than normal conversations?

Research is subject to the same limits as standard Claude conversations. However, research sessions can use up your limits faster due to Claude retrieving multiple sources and providing comprehensive responses.

### Which model does research use?

Research runs on Claude Opus 5.5 and falls back to Claude Opus 4.8 when needed. It uses these models no matter which model you’ve selected for your chat.

On Team and Enterprise plans, if your admin has turned off both Claude Opus 5.5 and Claude Opus 4.8 for your role, research won’t work. Ask your admin to turn on at least one of these models.