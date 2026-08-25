> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Telemetry and egress

> What Claude Desktop on 3P sends to Anthropic, how to disable it, and the network paths your firewall needs to allow

When Claude Desktop on third-party (3P) is configured with Google Cloud's Agent Platform, Amazon Bedrock, or Microsoft Foundry, the app sends conversation content only to your configured inference endpoint. For Microsoft Foundry, how data is handled beyond that endpoint depends on the deployment's hosting option; see [Claude in Microsoft Foundry](/docs/third-party/claude-desktop/foundry). The app does, by default, send a small amount of operational telemetry (crash reports and product analytics) that helps Anthropic diagnose issues and improve the product. Each category can be disabled independently via managed configuration.

This page covers what each category contains, how to turn it off, and the complete set of outbound hostnames the app uses so you can configure your perimeter firewall.

## Telemetry categories

### Essential telemetry

Crash reports, error stack traces, and performance timings. Contains diagnostic metadata (app version, OS, error type, redacted stack frames) but **never prompt or response content**. Attributed to your organization via `deploymentOrganizationUuid` so Anthropic support can find issues you report.

| Setting                     | Default | Effect when `true`                        |
| --------------------------- | ------- | ----------------------------------------- |
| `disableEssentialTelemetry` | `false` | No crash or error data leaves the device. |

<Warning>
  Disabling essential telemetry opts you into a **manual support model**. Anthropic will have zero remote visibility into failures on your fleet, so to get help with an issue your team will need to collect application logs from affected machines and send them to Anthropic directly. Leave this enabled during initial rollout.
</Warning>

### Non-essential telemetry

Product-usage analytics: feature adoption, session counts, UI interactions. Used to understand how Claude Desktop is used in aggregate. Contains no prompt or response content. Also gates the **Send** button in Help → Generate Diagnostic Report; with this disabled, diagnostic bundles can only be saved locally.

| Setting                        | Default | Effect when `true`                     |
| ------------------------------ | ------- | -------------------------------------- |
| `disableNonessentialTelemetry` | `false` | No product analytics leave the device. |

Leaving this enabled also adds `api.anthropic.com` to the [agent egress allowlist](#required-egress-paths) automatically, so Claude Code can deliver its usage telemetry from inside the sandbox. Allow that host at the perimeter too; it appears in the non-essential telemetry table below.

### Non-essential services

Cosmetic third-party fetches: favicons for connectors shown in the UI, the sandboxed iframe that renders interactive artifact previews, and the sandboxed iframes that render [MCP Apps](/docs/connectors/building/mcp-apps/getting-started), the interactive widgets connectors can display. Disabling these degrades the UI (generic icons, static artifact previews, and connector tool results shown as text instead of widgets) but doesn't affect functionality.

| Setting                       | Default | Effect when `true`                                                                                                                                    |
| ----------------------------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| `disableNonessentialServices` | `false` | Favicon, artifact-preview, and MCP App widget fetches are blocked. Connectors that return MCP Apps show the tool's text result instead of the widget. |

### Auto-updates

Checks Anthropic's update feed and downloads new builds.

| Setting              | Default | Effect when `true`                                                                        |
| -------------------- | ------- | ----------------------------------------------------------------------------------------- |
| `disableAutoUpdates` | `false` | The app never checks for or downloads updates. Your IT team must redistribute new builds. |

## Sending telemetry to your own collector

Independently of what's sent to Anthropic, you can export session activity to your own OpenTelemetry collector by setting `otlpEndpoint`. This is the recommended way to retain an audit trail in environments that disable Anthropic-bound telemetry.

For third-party deployments, the export includes session metadata (event names, durations, token counts, result counts, errors) by default, but not message content. It also identifies the signed-in user; see [User attribution](#user-attribution). See [Monitoring](/docs/cowork/monitoring) for the event schema and the [`otlp*` keys](/docs/third-party/claude-desktop/configuration#otlpendpoint) in the configuration reference.

The export carries logs and metrics. Cowork sessions, Code sessions, and the desktop application's own events arrive under the `service.name` values `cowork`, `claude-code-desktop`, and `claude-desktop` respectively. The app adds the collector host to the sandbox egress allowlist automatically, so `otlpEndpoint` does not need an entry in `coworkEgressAllowedHosts`; your perimeter firewall still needs to allow the host.

For collector authentication headers, extra resource attributes, and the log level of the desktop application's own event stream, see [`otlpHeaders`, `otlpResourceAttributes`, and `otlpDesktopLogLevel`](/docs/third-party/claude-desktop/configuration#otlpheaders) in the configuration reference.

### Collector endpoint and headers

Set [`otlpEndpoint`](/docs/third-party/claude-desktop/configuration#otlpendpoint) to the base address of your collector's OTLP/HTTP receiver, for example `https://otel-collector.example.com:4318`. The app appends the OpenTelemetry request paths itself (`/v1/logs`, `/v1/metrics`, and `/v1/traces` when [traces](#traces-beta) are enabled), so enter the address without those suffixes. A path prefix in front of them, such as `https://observability.example.com/otlp`, is kept.

The receiver must implement the OpenTelemetry protocol (OTLP) over HTTP in both its protobuf and JSON encodings, as an OpenTelemetry Collector does by default. If your logging or SIEM platform accepts only its own HTTP ingestion format, run an OpenTelemetry Collector that receives OTLP and forwards to that platform, and set `otlpEndpoint` to the collector's address. Each device opens its own connection to the collector, so the collector must present a TLS certificate the operating system trusts. See [Proxy support](#proxy-support) if a TLS-intercepting proxy sits in between.

[`otlpHeaders`](/docs/third-party/claude-desktop/configuration#otlpheaders) is a JSON object that maps each header name to its value, for example `{"Authorization":"Bearer <token>","X-Tenant":"agency"}`. As with the other object-typed keys described under [Value types](/docs/third-party/claude-desktop/configuration#value-types), write it as a JSON string.

The app reads both keys at launch, so users must restart it after a change. If the collector refuses requests or cannot be reached, the app keeps working, shows no error, and drops the affected telemetry batches. Check the collector's own request logs to confirm data is arriving.

For a collector credential that cannot be a static header, [`otlpHeadersHelper`](/docs/third-party/claude-desktop/configuration#otlpheadershelper) names a script on the device that prints the headers, and [`otlpAuthMode`](/docs/third-party/claude-desktop/configuration#otlpauthmode) set to `inference-credential` sends the user's own inference bearer token, which suits only a collector you operate. The configuration reference describes both.

### User attribution

Every record sent to your collector carries the user's identity as two resource attributes, on all three `service.name` streams:

* `enduser.id` — the signed-in user's identity. With an interactive sign-in flow (for example, Workforce Identity Federation or Google sign-in on Google Cloud's Agent Platform), this is the identity from the provider's claims, normally the user's email address. With credential methods that carry no identity claims (a static key, a credential helper, or an application default credentials file), it is the operating-system login name.
* `process.owner` — the operating-system login name.

`enduser.id` is the same identity the app shows in the sidebar and account menu, and is controlled by the [`endUserAttribution`](/docs/third-party/claude-desktop/configuration#enduserattribution) key: set it to `false` to remove the identity from both the app and the export. `process.owner` is not gated by that key — it is standard OpenTelemetry process metadata and is always present. A static value set under [`otlpResourceAttributes`](/docs/third-party/claude-desktop/configuration#otlpresourceattributes) overrides either attribute: a static `enduser.id` is always passed through — taking precedence over the signed-in identity, and surviving `endUserAttribution: false` — and a static `process.owner` replaces the login name.

These attributes are attached only to the OpenTelemetry export; the Anthropic-bound telemetry described earlier on this page does not carry them.

### Exporter protocol

The `otlpProtocol` key selects the transport for the telemetry export to your collector: `http/protobuf` (the default), `http/json`, or `grpc`. The protocol applies per session type:

* [Code](/docs/third-party/claude-desktop/code) sessions export over the protocol as configured, including `grpc`.
* Cowork sessions do not support gRPC export. When `otlpProtocol` is set to `grpc`, Cowork sessions export over `http/protobuf` instead; other protocol values apply as configured.
* The desktop application's own event stream (`claude-desktop`) always exports over `http/json`, whatever `otlpProtocol` is set to.

The fallback changes the protocol only, not the endpoint. When `otlpProtocol` is `grpc`, the Cowork and desktop-application exports go to the same `otlpEndpoint` over HTTP; if that address is your collector's OTLP/gRPC receiver (conventionally port 4317), that telemetry never reaches the collector. To receive all three streams with one collector, set `otlpProtocol` to `http/protobuf` and point `otlpEndpoint` at the collector's OTLP/HTTP receiver (conventionally port 4318).

### Content capture

To include content in the export, set `otlpContentCapture` to an array of categories:

| Category             | Captures                                                        |
| -------------------- | --------------------------------------------------------------- |
| `userPrompts`        | User message text                                               |
| `assistantResponses` | Model response text                                             |
| `toolDetails`        | Tool input arguments (for example, the web-search query string) |
| `toolContent`        | Tool output content                                             |
| `rawApiBodies`       | Full inference request and response bodies                      |

On Claude Desktop version 1.17377 or later, enabling `userPrompts` also captures model responses, even if `assistantResponses` is not listed. On those versions, no `otlpContentCapture` configuration captures user prompts without model responses.

Content is exported only to your configured `otlpEndpoint`. Anthropic does not receive it.

### Traces (beta)

The export carries logs (events) and metrics; it does not include traces unless you enable them. To export OpenTelemetry traces as well, set `otlpTracesEnabled` to `true`. Cowork and Code sessions then record a trace for each user interaction, with spans for model requests and tool executions, and every event emitted during a span carries that span's `trace_id` and `span_id`. This lets your backend correlate a prompt's events end-to-end natively, with no transformation on ingest.

Traces use the same `otlpEndpoint` and `otlpProtocol` as the rest of the export, including the Cowork gRPC fallback described in [Exporter protocol](#exporter-protocol). Span and span-event content is gated by the same `otlpContentCapture` categories as events: with no categories enabled, traces carry metadata only (timing, tool names, durations, token counts). Captured content appears primarily on events; spans stay close to metadata.

Two scope notes:

* The metrics in this export don't carry trace context, so trace-based correlation covers traces and events. Correlate metrics with a session via the `session.id` attribute.
* Trace export uses Claude Code's session-tracing beta, and the span structure may change while the feature is in beta.

`otlpTracesEnabled` requires Claude Desktop **1.22209.0** or later.

## Required egress paths

Claude Desktop on 3P has **two** independent network boundaries:

1. **Perimeter firewall:** your corporate network controls what the device can reach. The hostnames below are what you allowlist here.
2. **Agent egress allowlist:** the [`coworkEgressAllowedHosts`](/docs/third-party/claude-desktop/configuration#coworkegressallowedhosts) key controls what the agent's web-fetch and shell tools can reach. This is independent of, and stricter than, the perimeter.

<Note>
  The **Egress** section of the in-app configuration window is the authoritative source for your deployment. It computes the exact allowlist from your current settings, updates as you change them, and can export the list as a text file for your firewall team. Use the tables below as a static reference; defer to the configuration window for the precise set your build requires.
</Note>

All traffic is HTTPS on port 443. Allowlist by hostname (SNI); path-level rules aren't required.

### Always required

| Host                  | Purpose                                                             |
| --------------------- | ------------------------------------------------------------------- |
| `downloads.claude.ai` | VM workspace bundle and Claude CLI binary, fetched at session start |

Without this host reachable, Cowork sessions cannot start, unless the app was installed with the [offline installer variant](/docs/third-party/claude-desktop/installation#offline-installation), which includes both components in the installer package.

### Inference provider

The host(s) for your configured provider. These carry conversation content.

<Tabs>
  <Tab title="Google Cloud's Agent Platform">
    | Host                                 | Purpose                                                                                                                                                                                                                                                           |
    | ------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | `<region>-aiplatform.googleapis.com` | Model inference for single regions. The `global` region uses `aiplatform.googleapis.com`, and the `eu` / `us` multi-regions use `aiplatform.eu.rep.googleapis.com` / `aiplatform.us.rep.googleapis.com`. Replaced by the host of `inferenceVertexBaseUrl` if set. |
    | `oauth2.googleapis.com`              | Google auth token exchange                                                                                                                                                                                                                                        |
    | `sts.googleapis.com`                 | Google auth token exchange                                                                                                                                                                                                                                        |
    | `accounts.google.com`                | Google auth token exchange                                                                                                                                                                                                                                        |
    | `iamcredentials.googleapis.com`      | Google auth token exchange                                                                                                                                                                                                                                        |
  </Tab>

  <Tab title="Amazon Bedrock">
    | Host                                                               | Purpose                                                                    |
    | ------------------------------------------------------------------ | -------------------------------------------------------------------------- |
    | `bedrock-runtime.<region>.amazonaws.com`                           | Model inference. Replaced by the host of `inferenceBedrockBaseUrl` if set. |
    | `bedrock.<region>.amazonaws.com`                                   | Control plane (model discovery)                                            |
    | `sts.amazonaws.com`, `sts.<region>.amazonaws.com`                  | STS token exchange (profile auth only)                                     |
    | `portal.sso.<region>.amazonaws.com`, `oidc.<region>.amazonaws.com` | AWS SSO (profile auth only)                                                |

    With `inferenceBedrockBearerToken` set, the runtime and control-plane hosts are required.

    For AWS GovCloud regions (`us-gov-*`), the app automatically uses the FIPS endpoints instead: `bedrock-runtime-fips.<region>.amazonaws.com` and `bedrock-fips.<region>.amazonaws.com`.
  </Tab>

  <Tab title="Amazon Bedrock Mantle">
    | Host                              | Purpose                                                                    |
    | --------------------------------- | -------------------------------------------------------------------------- |
    | `bedrock-mantle.<region>.api.aws` | Model inference. Replaced by the host of `inferenceBedrockBaseUrl` if set. |
  </Tab>

  <Tab title="Microsoft Foundry">
    | Host                               | Purpose                                  |
    | ---------------------------------- | ---------------------------------------- |
    | `<resource>.services.ai.azure.com` | Model inference                          |
    | `login.microsoftonline.com`        | Entra ID auth (interactive sign-in only) |
  </Tab>

  <Tab title="Gateway">
    | Host                              | Purpose         |
    | --------------------------------- | --------------- |
    | Host of `inferenceGatewayBaseUrl` | Model inference |
  </Tab>

  <Tab title="Claude API">
    | Host                  | Purpose                                                                                                                                                      |
    | --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
    | `api.anthropic.com`   | Model inference; token exchange and API-key creation during browser sign-in                                                                                  |
    | `platform.claude.com` | Browser sign-in page. Dialed only when no static key or credential helper is configured; the in-app Egress list includes it for every Claude API deployment. |
  </Tab>
</Tabs>

### Auto-updates (`disableAutoUpdates: false`)

| Host                  | Purpose                                                            |
| --------------------- | ------------------------------------------------------------------ |
| `claude.ai`           | Update feed                                                        |
| `api.anthropic.com`   | Update feed (releases.claude.com when updateViaUpdatesHost is set) |
| `downloads.claude.ai` | Update binaries                                                    |

With [`updateViaUpdatesHost`](/docs/third-party/claude-desktop/configuration#updateviaupdateshost) set to `true`, the app reads the update feed from `releases.claude.com` instead of `claude.ai` and `api.anthropic.com`, so those two hosts are no longer needed for updates. Update binaries still come from `downloads.claude.ai`.

### Essential telemetry (`disableEssentialTelemetry: false`)

| Host                               | Purpose                   |
| ---------------------------------- | ------------------------- |
| `*.sentry.io`                      | Crash and error reporting |
| `*.ingest.us.sentry.io`            | Crash and error reporting |
| `sentry.io`                        | Crash and error reporting |
| `browser-intake-datadoghq.com`     | Performance timing        |
| `browser-intake-us3-datadoghq.com` | Performance timing        |
| `browser-intake-us5-datadoghq.com` | Performance timing        |
| `browser-intake-ap1-datadoghq.com` | Performance timing        |
| `browser-intake-ap2-datadoghq.com` | Performance timing        |
| `browser-intake-datadoghq.eu`      | Performance timing        |
| `browser-intake-ddog-gov.com`      | Performance timing        |

The `sentry.io` apex is listed alongside the wildcards because some firewalls don't match it under `*.sentry.io`, and `*.ingest.us.sentry.io` is listed separately for firewalls that match wildcards one label deep.

### Non-essential telemetry (`disableNonessentialTelemetry: false`)

| Host                  | Purpose                                                         |
| --------------------- | --------------------------------------------------------------- |
| `a-cdn.anthropic.com` | Analytics SDK                                                   |
| `a-api.anthropic.com` | Analytics events                                                |
| `claude.ai`           | Analytics events                                                |
| `api.anthropic.com`   | Claude Code usage telemetry, sent from inside the agent sandbox |

### Non-essential services (`disableNonessentialServices: false`)

| Host                        | Purpose                                |
| --------------------------- | -------------------------------------- |
| `www.google.com`            | Connector favicons                     |
| `*.gstatic.com`             | Connector favicons                     |
| `www.claudeusercontent.com` | Artifact preview iframe                |
| `cdnjs.cloudflare.com`      | Artifact preview asset CDNs            |
| `fonts.googleapis.com`      | Artifact preview asset CDNs            |
| `cdn.jsdelivr.net`          | Artifact preview asset CDNs            |
| `*.claudemcpcontent.com`    | MCP App widget iframe                  |
| `assets.claude.ai`          | Fonts loaded by MCP App widget iframes |

`*.claudemcpcontent.com` serves [MCP Apps](/docs/connectors/building/mcp-apps/getting-started), the interactive widgets connectors can render. Each widget loads in a sandboxed iframe on its own generated subdomain, so allowlist the wildcard.

### Optional features

| Host                                                                                                                                    | Required when                               |
| --------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------- |
| Host of `otlpEndpoint`                                                                                                                  | OpenTelemetry export is configured          |
| `github.com`, `objects.githubusercontent.com`, `pypi.org`, `files.pythonhosted.org`                                                     | Python-based desktop extensions are enabled |
| Hosts of each entry in `managedMcpServers` (server URL, plus `oauth.authorizationServer` and `login.microsoftonline.com` if configured) | Managed MCP servers are configured          |
| Hosts in `coworkEgressAllowedHosts`                                                                                                     | Sandbox web access is configured            |

## Disabling all Anthropic-bound connections

With `disableEssentialTelemetry`, `disableNonessentialTelemetry`, `disableNonessentialServices`, and `disableAutoUpdates` all set to `true`, the desktop application makes **no outbound connections to Anthropic-operated hosts at runtime**. The only required egress is `downloads.claude.ai` (for the VM bundle at session start) and your inference provider. With the [offline installer variant](/docs/third-party/claude-desktop/installation#offline-installation), `downloads.claude.ai` is not needed either, and your inference provider is the only required egress. This describes the application's own connections; what happens to conversation content after it reaches your inference provider is governed by that provider; see the [Overview](/docs/third-party/claude-desktop/overview).

See the [Locked down profile](/docs/third-party/claude-desktop/configuration#recommended-security-profiles) for a complete configuration.

## Proxy support

The Cowork sandbox honors the host operating system's proxy configuration, including PAC (proxy auto-configuration) files. If the device routes HTTPS through a corporate proxy, the sandbox will too, with no additional configuration required.

### TLS-intercepting proxies on macOS

If your proxy performs TLS interception, it presents its own certificate authority. Claude configures its CLI processes to trust the macOS System keychain in addition to the bundled CA roots, so a corporate CA installed there normally works without extra setup.

If inference or tool requests still fail certificate verification, the CA was likely added with policy-restricted trust: certificates installed via `security add-trusted-cert -p ssl …` are trusted by Safari and Chrome but are not picked up by the CLI runtime's keychain reader. Re-add the CA with full root trust (omit `-p`):

```bash theme={null}
sudo security add-trusted-cert -d -r trustRoot \
  -k /Library/Keychains/System.keychain /path/to/corp-ca.pem
```

If the certificate is MDM-managed and you cannot change how it is installed, set `NODE_EXTRA_CA_CERTS` as a fallback, then quit and relaunch Claude:

```bash theme={null}
security find-certificate -a -p /Library/Keychains/System.keychain > ~/corp-ca.pem
launchctl setenv NODE_EXTRA_CA_CERTS "$HOME/corp-ca.pem"
```

`launchctl setenv` makes the variable visible to apps launched from Finder or the Dock (shell-profile exports only reach terminal sessions). It applies until the next reboot; to make it permanent, run the command from a LaunchAgent at login.
