> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Managing your directory listing

> Track submissions, monitor server health and usage metrics, and edit your Connectors Directory listing

Organizations that submit to the [Connectors Directory](/docs/connectors/directory) get a submissions dashboard in Claude.ai at [Organization settings > Directory](https://claude.ai/admin-settings/directory/submissions). Use it to track submissions through review, monitor your published server's health and usage, and edit your listing.

<Note>
  The dashboard covers directory-listed remote MCP servers only. Custom connectors and local servers (desktop extensions) don't appear here, and the dashboard shows only your own organization's submissions.
</Note>

## Access the dashboard

The dashboard is part of your organization's admin settings, so you need:

* **A Team or Enterprise organization**
* **Directory management access.** By default, only organization Owners and Primary owners have it. On Enterprise, an Owner can delegate access through a custom role with the **Directory** or **Libraries** permission; see [Before you start](/docs/connectors/building/submission#before-you-start) for the steps. Team plans don't have custom roles, so on Team this stays with Owners.

The same access covers everything on this page: viewing submissions, metrics, and reviewer feedback, and editing and submitting listings.

## Track submission status

The dashboard lists each of your organization's submissions with its current status. Open a submission to see its full details and any reviewer feedback. When reviewers request changes, their feedback appears on the submission's detail page; address it and resubmit from the same page.

## Server health and usage metrics

<Note>
  Metrics are in beta. They're computed daily from directory usage and can lag by up to 24 hours. Time windows with fewer than 5 calls, per-tool rows with fewer than 5 calls, and per-product rows with fewer than 50 calls are omitted.
</Note>

Once your server is published, its detail page shows health and usage data.

### What the metrics cover

All of the metrics on this page measure traffic from Claude: Claude.ai, Claude Desktop, Claude Code, and other Claude surfaces. Connections that people make to your server from other MCP clients, and local servers that run on a user's own machine, aren't visible to Anthropic and aren't counted. Your own server logs can therefore show activity that this page doesn't.

Tool call totals, error rates, and latency are measured at Anthropic's HTTP connector proxy. Tool call users and directory rank are measured from the MCP message stream, which covers both the HTTP and legacy WebSocket transports. If users reach your server only over the legacy WebSocket transport, you'll still see tool call users and a directory rank, but no tool call totals, error rates, or latency data.

### Health

The health badge summarizes your server's recent reliability:

| Status          | Meaning                                                                                                      |
| --------------- | ------------------------------------------------------------------------------------------------------------ |
| **Healthy**     | The 30-day disconnect rate is at or below 5%                                                                 |
| **Degraded**    | The 30-day disconnect rate is above 5%                                                                       |
| **Collecting…** | The server is published, but there isn't enough data yet to compute a disconnect rate (metrics update daily) |
| **Not live**    | The server isn't published yet; health appears after publication                                             |

The disconnect rate is measured against every distinct Claude account that sent your server any MCP message in the last 30 days, including connection attempts that never completed: it is the share of those accounts that chose to disconnect your connector during those 30 days.

### Topline metrics

* **Directory rank**: your position among published directory servers, highest first, ranked by the number of distinct Claude accounts that sent your server any MCP message in the last 30 days. Every MCP message counts toward the ranking, including `initialize` and `tools/list`, and it includes accounts whose connection attempt never finished authenticating — a broader population than the Tool call users card below. A "Trending" tag marks servers in the top 10 by recent growth in that same message-based count.
* **Tool call users (30d)**: the number of distinct Claude accounts that made at least one tool call (`tools/call`) to your server in the last 30 days. Accounts that only attempted to connect, or connected and browsed your tools without calling one, aren't counted. This card was previously labeled "Active users (30d)" and counted every MCP message, including handshakes from connection attempts that never completed; the renamed metric counts only accounts that actually used your tools, so it is usually much smaller than the number the old card showed.
* **Tool calls (30d)**: the number of `tools/call` requests Anthropic received for your server in the last 30 days. Protocol messages such as `initialize` and `tools/list` aren't counted here. This is a count of requests, not of users, so retries are included, as are requests that were turned away for authentication problems.
* **Error rate (30d)**: of the tool calls above, the fraction that either failed at the request level (for example, with a 5xx response or a timeout) or returned an MCP tool result with `isError: true`. Tool-call requests that were turned away for authentication problems aren't counted as errors, but they are included in the total number of tool calls that the rate is measured against. Shown with the most common error types.

### Error breakdown

A table breaks errors out over 1-day, 7-day, and 30-day windows: total calls, overall error rate, tool versus request error rates, HTTP 4xx and 5xx rates, and the top error types in each window.

### Usage by product

A per-product table shows 7-day calls, error rate, and p50/p95/p99 latency, broken down by the Claude product the calls came from, such as Claude.ai, Claude Desktop, Claude Code, and Cowork. Only a fixed set of Claude surfaces is shown, and Anthropic's own internal monitoring traffic is excluded.

Because this table covers a shorter window, drops low-volume rows, shows only a fixed set of Claude surfaces, and excludes internal monitoring traffic, its call counts won't add up to the 30-day tool call total above. That's expected.

A high error rate on a single product may reflect a client-side issue on Anthropic's end rather than a problem with your server.

### Usage by tool

A per-tool table shows 7-day calls, the overall error rate, and the tool-result error rate for your top 15 tools by call volume.

## Edit your listing

Open your submission's detail page to edit the listing. You can change directly:

* **Listing metadata**: tagline, description, categories, documentation and privacy policy links, support contact, and icon
* **Company details**: company name and website
* **Display name**: editable, but changing the name of a published server affects existing users and requires re-review

Save your edits as you go, then submit them for review. Submitted changes show as pending until a reviewer approves them, and you can discard pending changes before they're approved.

The URL slug is locked: it's permanent after publication, since it determines your listing URL.

For other edits or escalations, email `mcp-review@anthropic.com`.
