> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Security, admin auditability, and analytics

> Security architecture diagrams, OpenTelemetry audit, usage analytics, and spend tracking for enterprise admins deploying Claude for M365.

Enterprise administrators deploying Claude for Excel, PowerPoint, Word,
and Outlook can review the security architecture for their chosen deployment
mode and connect audit logs, usage analytics, and spend tracking to
existing enterprise tooling.

## Security architecture

The Trust Center publishes architecture diagrams that show how user
prompts, document content, and responses flow between the Office
add-ins, Claude, and your infrastructure. Review the diagram that
matches your deployment mode before rollout.

* **Anthropic first-party**: users sign in with their Claude accounts
  and requests go directly to Claude. See the
  [first-party architecture overview](https://trust.anthropic.com/resources?s=e3n7pvyjnxjyahmdmqujcx\&name=claude-for-excel,-powerpoint,-word:-architecture-overview-%28anthropic-first-party%29).
* **Third-party platforms**: requests route through Amazon Bedrock, Google
  Cloud Vertex AI, Azure AI Foundry, or an LLM gateway. The companion
  third-party architecture diagram is listed alongside the first-party
  one in the [Trust Center resources](https://trust.anthropic.com/resources?s=e3n7pvyjnxjyahmdmqujcx);
  filter for "Claude for Excel, PowerPoint, Word".
  [Use Claude for M365 with third-party platforms](/docs/office-agents/third-party-platforms)
  has per-mode request-flow diagrams for the [LLM gateway](/docs/office-agents/third-party-platforms#llm-gateway)
  and [Bedrock, Vertex AI, or Foundry direct](/docs/office-agents/third-party-platforms#bedrock-vertex-ai-or-foundry-direct)
  paths, plus deployment guidance.

## Audit and observability

Forward Claude for M365 activity to your existing observability stack with
a custom OpenTelemetry collector endpoint. When a custom collector is
configured, spans are exported unfiltered to that endpoint and include
the full audit trail: session identifiers, surface, tool inputs and
outputs, prompt content, and document references. Treat the endpoint as
containing prompt and document content when scoping access controls
and retention.

Only spans sent to Anthropic's own collector are allowlist-filtered to
strip sensitive attributes; that path is bypassed entirely when a
custom endpoint is set.

The add-in exports its telemetry from each user's browser: the taskpane
at `https://pivot.claude.ai` posts directly to the custom collector
endpoint, so every export is a cross-origin request and the endpoint
must support CORS. The endpoint must answer the `OPTIONS` preflight
with `Access-Control-Allow-Origin` covering `https://pivot.claude.ai`
and `Access-Control-Allow-Headers` covering `Content-Type` plus any
headers you configure for the export, such as `Authorization`. It must
also return the same `Access-Control-Allow-Origin` header on the `POST`
response. The [CORS requirements for an LLM gateway](/docs/office-agents/third-party-platforms#cors-requirements)
describe the same browser behavior in more detail.

Managed OTLP ingest endpoints such as Grafana Cloud are designed for
server-to-server export and generally do not answer browser CORS
preflights, so the browser blocks the export before it sends any
authentication header. Point the collector endpoint at an OpenTelemetry
Collector that you run, configure the `cors` block on its OTLP HTTP
receiver, and have the collector forward to your backend. The collector
makes the authenticated call to your backend, so no credential needs to
appear in the export headers, which reach every signed-in user's
browser.

See [Configure a custom OpenTelemetry collector](/docs/office-agents/opentelemetry)
for the configuration keys, endpoint requirements, and full span reference.

<Note>
  The usage analytics and spend tracking sections below apply when users
  sign in with their Claude accounts directly. When connecting through a
  third-party platform such as Amazon Bedrock, Google Cloud Vertex AI,
  Azure AI Foundry, or an LLM gateway, usage and spend are tracked through
  your cloud provider's billing console and your gateway's logging instead.
</Note>

## Usage analytics

Pull Claude for M365 usage into your own BI or reporting pipeline through
the Claude Enterprise Analytics API. The API exposes per-user,
per-surface, and per-organization aggregates.

See [Claude Enterprise Analytics API reference guide](https://support.claude.com/en/articles/13703965-claude-enterprise-analytics-api-reference-guide)
for endpoints, request shapes, and aggregation windows.

## Spend tracking

Download CSV exports of Team and Enterprise plan usage from the usage
analytics dashboard in your admin console. Exports include per-seat
and per-surface spend, making them suitable for chargeback and
financial reconciliation.

See [View usage analytics for Team and Enterprise plans](https://support.claude.com/en/articles/12883420-view-usage-analytics-for-team-and-enterprise-plans)
for the steps to generate and download a report.

## Related

The pages below cover deployment paths and plugins relevant to
enterprise admins.

* [Data storage and retention](/docs/office-agents/data-storage)
* [Use Claude for M365 with third-party platforms](/docs/office-agents/third-party-platforms)
* [Install financial services plugins for Cowork](/docs/office-agents/fsi-plugins)
