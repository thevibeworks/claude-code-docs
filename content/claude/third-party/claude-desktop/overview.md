> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Overview

> Run Claude Desktop against your own cloud inference provider

Claude Desktop on third-party (3P) is a deployment mode of Claude Desktop that routes all model inference through a provider you configure: Google Cloud's Agent Platform, Amazon Bedrock, Microsoft Foundry, any compatible gateway you operate, or the Anthropic API directly. The app runs from a bundled local web application, and conversation history is stored on the user's device.

You get the full Claude Desktop experience (Chat, Cowork, and Code, including file creation, multi-step research, and sub-agent coordination) with inference and billing handled by the provider you choose.

## Who it's for

Claude Desktop on 3P is designed for organizations whose security, regulatory, or contractual requirements prevent them from sending data to Anthropic's first-party infrastructure. Typical deployments include:

* **Highly regulated enterprises on 3P only:** organizations that use third-party inference for regulatory or security reasons
* **International enterprises with data residency requirements:** organizations that require in-region data residency and cannot send conversation data to the United States

If your organization can use Anthropic's first-party products directly, standard Claude Desktop with [Cowork](/docs/cowork/overview) on a Team or Enterprise plan is simpler to deploy, offers an in-app UI for user management, analytics, and RBAC, and releases new features more quickly than Claude Desktop on 3P. Choose Claude Desktop on 3P when routing inference through Anthropic's API is not an option.

## Architecture

Claude Desktop on 3P keeps the standard feature set and relocates inference to the provider you configure.

| Component              | Standard Claude Desktop    | Claude Desktop on 3P                                                                                                                   |
| ---------------------- | -------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| Model inference        | Anthropic API              | Your configured provider endpoint (Google Cloud's Agent Platform, Amazon Bedrock, Microsoft Foundry, or gateway), or the Anthropic API |
| Web application        | Loaded from claude.ai      | Bundled inside the desktop app                                                                                                         |
| User identity          | Anthropic account          | Local device identity only                                                                                                             |
| Conversation storage   | Anthropic backend          | Local disk on the user's machine                                                                                                       |
| Code execution sandbox | Local VM                   | Local VM (identical)                                                                                                                   |
| Configuration          | Admin console at claude.ai | OS-native configuration (MDM-managed or per-user)                                                                                      |

The desktop app detects 3P mode at launch from the configured inference provider. When a provider and its credentials are present, the sign-in screen offers the option to skip Anthropic authentication and start the app using your inference-provider configuration instead.

### Security posture

* **Conversation content goes only to your configured endpoint.** Prompts, responses, files, and tool outputs are sent only to your configured inference endpoint and stored only on the local machine; data handling at the provider is governed by your inference provider. For Microsoft Foundry deployments hosted on Azure, prompts and completions remain within Azure; only usage metadata and content flagged by Anthropic's safety systems egress to Anthropic.
* **Sandboxed tool execution.** Shell commands run in the hardened Cowork VM; file access is scoped to your allowed folders and web fetches to your egress allowlist.
* **Auditable telemetry.** Crash reports and product analytics are scrubbed of conversation and user data before being sent to Anthropic, and can be fully disabled via configuration keys. Independently, you can export session activity to your own OpenTelemetry collector. The export is metadata only by default, with prompt and tool content available as an explicit opt-in.
* **Centrally managed.** All configuration is delivered via your existing MDM (Jamf, Intune, Workspace ONE, Group Policy) and cannot be overridden by end users when an admin profile is present.

For a detailed treatment of the threat model, sandbox boundaries, and data flows, request access to the [Claude Cowork Desktop Security Architecture Overview](https://trust.anthropic.com/resources?s=2a7bbzo1lyymvdt551q7kl\&name=claude-cowork-desktop-security-architecture-overview) on Anthropic's Trust Center. For architecture, telemetry, and controls information specific to Claude Desktop on 3P, see the [Claude Desktop Security Overview (Third-party platforms)](https://trust.anthropic.com/resources?s=0c8rx4s7mm5ierz8ppetfs\&name=claude-cowork-security-overview-\(third-party-platforms\)) on the Trust Center.

## Data residency and international deployment

**Google Cloud's Agent Platform and Amazon Bedrock:** Inference requests go directly from the user's machine to the regional endpoint you configure. Conversation data goes only to that endpoint, to local disk, and optionally to your configured OpenTelemetry collector. Residency is determined by:

1. The cloud region you select for inference
2. The physical location of the user's device, where conversations are persisted

For multi-region organizations, deploy distinct MDM configuration profiles per geography so each user population points at an in-region endpoint. Google Cloud's Agent Platform and Amazon Bedrock each offer Claude models in the EU, UK, and Asia/Pacific regions; consult your provider's model-availability documentation for the current list.

## Public sector and highly regulated environments

This section applies when using Google Cloud's Agent Platform or Amazon Bedrock.

Because inference runs in your cloud tenant, Claude Desktop on 3P operates inside whatever compliance boundary your provider and region give you. The desktop application itself contacts Anthropic-operated hosts only to download the VM workspace bundle and Claude CLI binary (always required), and for crash reporting, product analytics, non-essential services (connector favicons, artifact previews, and MCP Apps widgets), and auto-updates. Each of the latter four can be disabled independently via managed configuration.

With Anthropic-bound telemetry, non-essential services, and updates all disabled, the only remaining Anthropic-operated egress is `downloads.claude.ai` for the VM bundle at session start. Beyond that, the compliance posture of your deployment is determined by your inference provider. See [Telemetry and egress](/docs/third-party/claude-desktop/telemetry) for the full set of network paths and how to lock them down.

## HIPAA

This section applies when using Google Cloud's Agent Platform or Amazon Bedrock.

Claude Desktop on 3P does not process user data, prompts, or completions. As such, Anthropic does not interact with PHI the user may upload to Claude Desktop on 3P; that data is transmitted only to the customer's cloud service provider or any remote MCP servers they optionally choose to configure. For a HIPAA-compliant solution, customers should ensure they have a BAA in place with their CSP and review any MCP servers for HIPAA compliance before connecting them to Claude Desktop on 3P.

Disabling telemetry is not required to run Claude Desktop on 3P in a HIPAA-compliant way, since Anthropic's telemetry does not collect user data, prompts, or completions, only redacted crash reporting and aggregated usage metrics that do not reveal sensitive data.

## Next steps

<Columns cols={2}>
  <Card title="Installation and setup" icon="download" href="/docs/third-party/claude-desktop/installation">
    Roll out Claude Desktop on 3P to your organization with MDM, or configure a single machine for evaluation.
  </Card>

  <Card title="Configuration reference" icon="sliders" href="/docs/third-party/claude-desktop/configuration">
    Every managed-configuration key, what it does, and recommended security profiles.
  </Card>

  <Card title="Extensions" icon="puzzle-piece" href="/docs/third-party/claude-desktop/extensions">
    Deploy MCP servers, plugins, skills, and hooks across your fleet.
  </Card>

  <Card title="Telemetry and egress" icon="shield-halved" href="/docs/third-party/claude-desktop/telemetry">
    What the app sends to Anthropic, how to turn it off, and the firewall allowlist you'll need.
  </Card>
</Columns>
