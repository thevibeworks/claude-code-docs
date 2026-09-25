> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Manage your directory listing

> Track submissions, monitor server health and usage metrics, and edit your directory listing

Organizations that submit a connector to the [directory](/docs/connectors/directory) get a submissions dashboard in the developer portal at [claude.ai/directory/manage](https://claude.ai/directory/manage). This page is for connector authors who have already [submitted a connector](/docs/connectors/building/submission). Use the dashboard to [track a submission through review](#track-submission-status), [monitor your published server's health and usage](#server-health-and-usage-metrics), and [edit your listing](#edit-your-listing).

<Note>
  This page covers directory-listed remote MCP servers. The dashboard shows only your own organization's submissions. Custom connectors and local servers packaged as desktop extensions don't appear here.
</Note>

## Access the dashboard

The dashboard uses the same access as submitting. [Who can submit to the directory](/docs/directory/publish#confirm-you-can-submit-to-the-directory) lists the plan and role requirements. That access covers everything on this page: viewing submissions, metrics, and reviewer feedback, and editing and submitting listings.

## Track submission status

The dashboard lists each of your organization's submissions with its current status. [Track your submission](/docs/directory/submission-status#mcp-connector-statuses) says what each status means and who acts next. Open a submission to see its full details and any reviewer feedback. When reviewers request changes, their feedback appears on the submission's detail page, where you address it and resubmit.

A published connector is listed with the **Community** label by default. [Connector verification](/docs/connectors/verification#list-your-own-connector) explains how a listing becomes Verified.

## Server health and usage metrics

Once your server is published, its **Overview** and **Usage** tabs in the developer portal show a health badge, topline usage numbers, an error breakdown, and usage by product and by tool.

<Note>
  Metrics are in beta. They're computed daily from directory usage and can lag by up to 24 hours. Time windows with fewer than 5 calls, per-tool rows with fewer than 5 calls, and per-product rows with fewer than 50 calls are omitted.
</Note>

### Review what the metrics cover

All of the metrics on this page measure traffic from Claude: claude.ai, Claude Desktop, Claude Code, and other Claude surfaces. Connections that people make to your server from other MCP clients, and local servers that run on a user's own machine, aren't visible to Anthropic and aren't counted. Your own server logs can therefore show activity that this page doesn't.

Tool call totals, error rates, and latency are measured at Anthropic's HTTP connector proxy. The **Used a tool** count and directory rank are measured from the MCP message stream, which covers both the HTTP and legacy WebSocket transports. If users reach your server only over the legacy WebSocket transport, you'll still see the **Used a tool** count and a directory rank, but no tool call totals, error rates, or latency data.

### Health

The health badge summarizes your server's recent reliability as one of these statuses:

| Status              | Meaning                                                              |
| ------------------- | -------------------------------------------------------------------- |
| **Healthy**         | Request errors are 2% or less of tool calls in the last 30 days      |
| **Worth a look**    | Request errors are above 2%                                          |
| **Degraded**        | Request errors are above 5%                                          |
| **Not enough data** | Request errors haven't been measured yet; metrics update daily       |
| **Not live**        | The server isn't published yet, and health appears after publication |

Request errors include tool calls rejected for authentication problems and exclude errors a tool returns in its own result.

### Topline metrics

The topline metric cards summarize your server's reach, usage, and reliability over the last 30 days:

* **Directory rank**: your position among published directory servers, highest first, ranked by the number of distinct Claude accounts that sent your server any MCP message in the last 30 days. Every MCP message counts toward the ranking, including `initialize` and `tools/list`, and it includes accounts whose connection attempt never finished authenticating, which is a broader population than the **Used a tool** card counts. A **Trending** tag marks servers in the top 10 by recent growth in that same message-based count
* **Used a tool**: the number of distinct Claude accounts that made at least one tool call (`tools/call`) to your server in the last 30 days. Accounts that only attempted to connect, or connected and browsed your tools without calling one, aren't counted. The renamed metric counts only accounts that actually used your tools, so it's usually much smaller than the number the old card showed
* **Tool calls (30d)**: the number of `tools/call` requests Anthropic received for your server in the last 30 days. Protocol messages such as `initialize` and `tools/list` aren't counted here. This is a count of requests, not of users, so retries are included, as are requests that were turned away for authentication problems
* **Error rate (30d)**: of those tool calls, the fraction that either failed at the request level, for example with a 5xx response or a timeout, or returned an MCP tool result with `isError: true`. Tool-call requests that were turned away for authentication problems aren't counted as errors, but they are included in the total number of tool calls that the rate is measured against. Shown with the most common error types

### Error breakdown

A table breaks errors out over 1-day, 7-day, and 30-day windows: total calls, overall error rate, tool versus request error rates, HTTP 4xx and 5xx rates, and the top error types in each window.

### Usage by product

A per-product table shows 7-day calls, error rate, and p50/p95/p99 latency, broken down by the Claude product the calls came from, such as claude.ai, Claude Desktop, Claude Code, and Cowork. Only a fixed set of Claude surfaces is shown, and Anthropic's own internal monitoring traffic is excluded.

Because the per-product table covers a shorter window, drops low-volume rows, shows only a fixed set of Claude surfaces, and excludes internal monitoring traffic, its call counts won't add up to the 30-day **Tool calls** total.

A high error rate on a single product may reflect a client-side issue on Anthropic's end rather than a problem with your server.

### Usage by tool

A per-tool table shows 7-day calls, the overall error rate, and the tool-result error rate for your top 15 tools by call volume.

## Edit your listing

You edit a published listing from its submission detail page in the dashboard. You can change these fields directly:

* **Listing metadata**: tagline, description, categories, tool and prompt names, documentation and privacy policy links, support contact, and icon
* **Company details**: company name and website
* **Display name**: editable, but changing the name of a published server affects existing users and requires re-review

Save your edits as you go, then submit them for review. Submitted changes show as pending until a reviewer approves them, and you can discard pending changes before they're approved.

The URL slug is locked. It's permanent after publication because it determines your listing URL.

For other edits or escalations, email `mcp-review@anthropic.com`.

## Next steps

* [After publishing](/docs/connectors/building/after-publishing): release updates to your server, and delist
* [Connector verification](/docs/connectors/verification#list-your-own-connector): see how a Community listing becomes Verified
* [Troubleshoot your connector](/docs/connectors/building/troubleshooting): diagnose the errors behind a degraded health badge or high error rate
