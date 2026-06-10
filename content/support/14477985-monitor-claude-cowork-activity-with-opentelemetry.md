Title: Monitor Claude Cowork activity with OpenTelemetry

URL Source: https://support.claude.com/en/articles/14477985-monitor-claude-cowork-activity-with-opentelemetry

Markdown Content:
1.   [All Collections](https://support.claude.com/en/)
2.   [Team and Enterprise plans](https://support.claude.com/en/collections/9387370-team-and-enterprise-plans)
3.   [Analytics and usage](https://support.claude.com/en/collections/18901831-analytics-and-usage)
4.   Monitor Claude Cowork activity with OpenTelemetry

Updated over 3 weeks ago

This article explains how to use OpenTelemetry (OTel) to monitor Claude Cowork activity across your organization. With OTel, your security and operations teams can stream Cowork events into the observability tools you already use to track usage, investigate incidents, and analyze performance.

## What you can monitor

When you connect Claude Cowork to an OpenTelemetry collector, Cowork streams events covering:

A shared `prompt.id` attribute links every event triggered by a single user prompt, so you can reconstruct everything Claude did in response to one input.

## When to use OpenTelemetry

OpenTelemetry gives you a real-time stream of structured Cowork events that you can route into your existing SIEM and observability tools. It's the right choice for security monitoring and incident investigation, tracking tool and file access patterns across your organization, cost and performance analysis, and building dashboards and alerts in your existing pipeline.

## Compatible destinations

Cowork's OpenTelemetry output works with any standard OTel collector. Common destinations include:

You can route events to multiple destinations at once by configuring your collector accordingly.

## Set up OpenTelemetry monitoring

To configure Cowork to export events to your collector:

Events begin flowing to your collector immediately. Authentication headers are encrypted at rest on Anthropic servers.

## Security and privacy considerations

A few things to be aware of before you turn on OpenTelemetry export:

## Joining OpenTelemetry data with the Compliance API

While Cowork activity is **not captured** in the **[Compliance API](https://support.claude.com/en/articles/13015708-access-the-compliance-api)** at this time, each Cowork OTel event includes a shared user account identifier you can use to correlate events with records from the Compliance API. This lets you build a unified view that combines real-time telemetry from OTel with longer-term records from Compliance API queries.

* * *

Related Articles

[Get started with Claude Cowork](https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork)[Use Claude Cowork safely](https://support.claude.com/en/articles/13364135-use-claude-cowork-safely)[Use Claude Cowork on Team and Enterprise plans](https://support.claude.com/en/articles/13455879-use-claude-cowork-on-team-and-enterprise-plans)[Configure a custom OpenTelemetry collector for Office agents](https://support.claude.com/en/articles/14447276-configure-a-custom-opentelemetry-collector-for-office-agents)[Claude Cowork desktop architecture overview](https://support.claude.com/en/articles/14479288-claude-cowork-desktop-architecture-overview)
