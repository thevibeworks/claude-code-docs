# Monitor Claude Cowork activity with OpenTelemetry

**Note:** Claude Cowork and chat are now one Claude. Ask for what you need, and Claude decides whether that’s a quick answer or a task. This is rolling out gradually to Pro and Max plans, and it's generally available on Enterprise plans, where it appears in admin settings as **Chat and Cowork unified**.

Team organizations, and Enterprise organizations that haven’t turned it on, keep chat and Claude Cowork as they are today, so everything in this article still applies. If you’re an Enterprise admin, learn more in **[Set up and manage the new unified Claude experience for your Enterprise organization](https://support.claude.com/en/articles/17444462)**, or read our **[blog post](https://claude.com/blog/cowork-is-now-claude)**.

This article explains how to use OpenTelemetry (OTel) to monitor Claude Cowork activity across your organization. With OTel, your security and operations teams can stream Cowork events into the observability tools you already use to track usage, investigate incidents, and analyze performance.

OpenTelemetry monitoring for Claude Cowork is available on Team and Enterprise plans. It covers Cowork sessions that run in the cloud (on desktop, web, and mobile) as well as local desktop sessions. Monitoring sessions in the cloud requires Claude Desktop version 1.22209.3 or later, and monitoring local desktop sessions requires Claude Desktop version 1.1.4173 or later.

---

## What you can monitor

When you connect Claude Cowork to an OpenTelemetry collector, Cowork streams events covering:

- **User prompts.** When content capture includes user prompts, the full text of prompts users submit to Cowork. Otherwise, each prompt is recorded without its text.

- **Tool and MCP invocations.** Every tool call Claude makes during a session, including the tool name, success or failure, and execution time. When content capture includes tool details, events also carry the tool's parameters (for MCP tools, including the MCP server and tool names) and the error message when a tool fails.

- **File access.** The folders users connect to a session. When content capture includes tool details, events also carry the file paths Claude reads, modifies, or otherwise touches, including files accessed through MCPs.

- **Skills and plugins.** Which skills and plugins Claude uses within a session. Unless content capture includes tool details, skills and plugins that don't come from Anthropic appear under a placeholder name.

- **Human approval decisions.** Whether each tool action was approved by the user, rejected by the user, or initiated automatically based on existing permissions.

- **API requests and errors.** Per-request model, token counts, estimated cost, duration, and any errors returned.

A shared `prompt.id` attribute links every event triggered by a single user prompt, so you can reconstruct everything Claude did in response to one input.

For the full list of event types and attributes, see the **[Cowork monitoring reference](https://claude.com/docs/cowork/monitoring#events)** on **claude.com/docs**.

---

## When to use OpenTelemetry

OpenTelemetry gives you a real-time stream of structured Cowork events that you can route into your existing SIEM and observability tools. It's the right choice for security monitoring and incident investigation, tracking tool and file access patterns across your organization, cost and performance analysis, and building dashboards and alerts in your existing pipeline.

## Compatible destinations

Cowork's OpenTelemetry output works with any standard OTel collector. Common destinations include:

- **SIEM platforms** like Splunk and Cribl

- **Log aggregation systems** like Elasticsearch and Loki

- **Columnar stores** like ClickHouse

- **Observability platforms** like Honeycomb and Datadog

You can route events to multiple destinations at once by configuring your collector accordingly.

---

## Set up OpenTelemetry monitoring

To configure Cowork to export events to your collector:

1. Go to **Organization settings > Cowork**.

2. Enter your **OTLP endpoint** (your OpenTelemetry collector URL).

3. Select the **OTLP protocol** your collector uses: HTTP/JSON or HTTP/protobuf.

4. Add any **OTLP headers** required for authentication, such as a bearer token.

5. Save your settings.

Events begin flowing to your collector immediately. Authentication headers are encrypted at rest on Anthropic servers.

---

## Security and privacy considerations

A few things to be aware of before you turn on OpenTelemetry export:

- **Prompt text, Claude's responses, and tool inputs are off by default in current versions of Claude Desktop.** Events only carry metadata unless you turn on content capture with the `otlpContentCapture` device policy, which you deploy with your device management tool. If you turn it on, route events through a collector that meets your organization's policies for logging that content. Learn more about **[content capture in the Cowork monitoring reference](https://claude.com/docs/cowork/monitoring#content-capture)**.

- **Some older versions of Claude Desktop send content when the policy isn't set.** That content can include prompt text, Claude’s responses, and tool inputs. These versions switch to metadata only once they update. On versions that support the policy, you can turn content off before then by setting `otlpContentCapture` to an empty list, written as the two characters `[]`.

- **The policy applies to Cowork sessions started from Claude Desktop, whether they run on the user's computer or in the cloud.** It doesn't apply to scheduled tasks that run in the cloud, or, where chat and Cowork are unified, to chats that Claude moves into the cloud. Those sessions carry metadata only. Cowork sessions started on the web or in the mobile app carry metadata only, and the policy doesn’t change that.

- **Tool parameters may include sensitive values.** When content capture includes tool details, file paths, command arguments, and other tool inputs are exported in the `tool_input` and `tool_parameters` fields. Plan your retention and access policies accordingly.

- **User email addresses, the paths of connected folders, and API error messages are included whatever the content capture setting.** An API error message can sometimes repeat part of the request that caused it, so filter or redact at your collector if that's a concern.

- **Events are only exported when an admin configures an OTLP endpoint.** No data flows by default.

---

## Joining OpenTelemetry data with the Compliance API

The Compliance API covers Cowork (via Claude, Claude Desktop, and Claude Mobile) and Claude Code (via CLI and Claude Desktop) alongside Claude chats, giving you one audit trail with every session attributable to an individual user. Organizations already using OpenTelemetry can run both in parallel, and OTel coverage includes Cowork on web and mobile too. Learn more about **[retrieving remote sessions in the Compliance API](https://platform.claude.com/docs/en/manage-claude/compliance-content-data)**.