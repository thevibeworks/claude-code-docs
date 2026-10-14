> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Features

> Feature comparison between Claude Enterprise and Claude Desktop on third-party (3P)

Claude Desktop on third-party (3P) is a deployment mode of Claude Desktop that routes all model inference through [a provider you configure](/docs/third-party/claude-desktop/overview). Pricing is token-based consumption billed by your cloud provider, with no seat licensing.

## Key differences from Claude Enterprise

<div className="feature-compare">
  | Feature | Claude Enterprise | Claude Desktop on 3P |
  | - | :-: | :-: |
  | [Connect to your cloud provider for inference](/docs/third-party/claude-desktop/configuration#connection) | <Icon icon="xmark" color="#9E9E9E" /> No | <Icon icon="circle-check" iconType="solid" /> **Yes** |
  | [Data residency in multiple regions](/docs/third-party/claude-desktop/overview#data-residency-and-international-deployment) | <Icon icon="xmark" color="#9E9E9E" /> No | <Icon icon="circle-check" iconType="solid" /> **Yes**, depending on provider |
  | [Run inference outside Anthropic's cloud](/docs/third-party/claude-desktop/overview#data-handling-by-provider) | <Icon icon="xmark" color="#9E9E9E" /> No | <Icon icon="circle-check" iconType="solid" /> **Yes**, depending on provider |
  | Mobile and claude.ai web-based access | <Icon icon="circle-check" iconType="solid" /> **Yes** | <Icon icon="xmark" color="#9E9E9E" /> No |
  | Sessions in Anthropic's cloud | <Icon icon="circle-check" iconType="solid" /> **Yes** | <Icon icon="xmark" color="#9E9E9E" /> No |
  | Sharing between users | <Icon icon="circle-check" iconType="solid" /> **Yes** | <Icon icon="xmark" color="#9E9E9E" /> No |
  | Voice mode | <Icon icon="circle-check" iconType="solid" /> **Yes** | <Icon icon="xmark" color="#9E9E9E" /> No |
  | Claude Security and [Claude Tag](/docs/claude-tag/overview) | <Icon icon="circle-check" iconType="solid" /> **Yes** | <Icon icon="xmark" color="#9E9E9E" /> No |
</div>

## Features in Claude Desktop on 3P

Some features have limits or need setup, described in [Good to know about Claude Desktop on 3P](#good-to-know-about-claude-desktop-on-3p).

Claude Desktop on 3P is administered from the web-based [admin console](/docs/third-party/claude-desktop/admin-console), and can also be configured through [MDM](/docs/third-party/claude-desktop/mdm) or a [bootstrap server](/docs/third-party/claude-desktop/bootstrap).

<Card title="Everyday work" icon="briefcase" color="#737373" horizontal>
  <div className="feature-chips not-prose">
    * [Chat](/docs/third-party/claude-desktop/chat)
    * [Cowork](/docs/third-party/claude-desktop/configuration#coworktabenabled)
    * Projects
    * Artifacts
    * [Memory](/docs/third-party/claude-desktop/data-storage#memory)
    * [Scheduled tasks](/docs/third-party/claude-desktop/configuration#scheduledtasksenabled)
    * [Code execution for analysis](/docs/third-party/claude-desktop/chat#advanced-file-analysis)
    * [File access, upload, and export](/docs/third-party/claude-desktop/local-access)
    * Global languages
    * [Automatically approve in Cowork](/docs/third-party/claude-desktop/configuration#automodeenabled)
  </div>
</Card>

<Card title="Web and browser" icon="globe" color="#737373" horizontal>
  <div className="feature-chips not-prose">
    * [Built-in browser](/docs/third-party/claude-desktop/browser#built-in-browser)
    * [Web search](/docs/third-party/claude-desktop/web-tools#web-search)
    * [Claude in Chrome](/docs/third-party/claude-desktop/browser#claude-in-chrome)
  </div>
</Card>

<Card title="Connectors and extensions" icon="plug" color="#737373" horizontal>
  <div className="feature-chips not-prose">
    * [Microsoft 365](/docs/third-party/claude-desktop/connectors-m365) and [GitHub](/docs/third-party/claude-desktop/connectors-github) connectors
    * [Local MCP](/docs/third-party/claude-desktop/extensions#user-extensions)
    * [Remote MCP](/docs/third-party/claude-desktop/extensions#managed-mcp-servers-admin)
    * [Skills, plugins, and hooks](/docs/third-party/claude-desktop/extensions)
    * [Plugin marketplaces](/docs/third-party/claude-desktop/extensions#plugin-marketplaces-admin)
  </div>
</Card>

<Card title="Code" icon="code" color="#737373" horizontal>
  <div className="feature-chips not-prose">
    * [Code](/docs/third-party/claude-desktop/code)
    * [Auto mode in Code](/docs/third-party/claude-desktop/configuration#automodeenabled)
    * [SSH remote Code sessions](/docs/third-party/claude-desktop/ssh-remote-sessions)
  </div>
</Card>

<Card title="Administration" icon="sliders" color="#737373" horizontal>
  <div className="feature-chips not-prose">
    * [Admin console](/docs/third-party/claude-desktop/admin-console)
    * [Endpoint or gateway configuration](/docs/third-party/claude-desktop/configuration#connection)
    * [Skills, hooks, and plugins distribution](/docs/third-party/claude-desktop/extensions#organization-plugins-admin)
    * [MCP server allowlist](/docs/third-party/claude-desktop/extensions#controlling-user-extensions)
    * [Feature toggles](/docs/third-party/claude-desktop/configuration#capabilities)
    * [Auto-updates](/docs/third-party/claude-desktop/installation#updates)
    * [Per-user usage caps](/docs/third-party/claude-desktop/configuration#inferencemaxtokensperwindow)
    * [User management via UI](/docs/third-party/claude-desktop/admin-console#connect-your-identity-provider)
    * [RBAC](/docs/third-party/claude-desktop/admin-console#per-group-permission-policies)
  </div>
</Card>

<Card title="Monitoring and retention" icon="chart-line" color="#737373" horizontal>
  <div className="feature-chips not-prose">
    * [OpenTelemetry export](/docs/third-party/claude-desktop/telemetry#sending-telemetry-to-your-own-collector)
    * [Turning off telemetry](/docs/third-party/claude-desktop/telemetry#telemetry-categories)
    * [Data retention policies](/docs/third-party/claude-desktop/data-storage#automatic-deletion-of-idle-sessions)
  </div>
</Card>

## Good to know about Claude Desktop on 3P

<Accordion title="Notes on setup, limits, monitoring, and data handling">
  | Topic | What to know |
  | - | - |
  | Sessions and scheduled tasks | Sessions are local, except [Code sessions over SSH](/docs/third-party/claude-desktop/ssh-remote-sessions), and the device must be awake to run long processes and scheduled tasks. |
  | Memory | [Memory](/docs/third-party/claude-desktop/data-storage#memory) in Claude Desktop on 3P is stored on the device, not on Anthropic infrastructure. Chat-history search and nightly summary generation are not available in Chat on 3P. |
  | Web search | Amazon Bedrock deployments and gateways that do not forward Anthropic server tools need a [web search provider](/docs/third-party/claude-desktop/web-tools#web-search-options) configured first. |
  | Claude in Chrome | Claude in Chrome works with Claude Desktop on 3P only in organizations managed from the [Enterprise Admin Console](/docs/third-party/claude-desktop/admin-console). |
  | Automatically approve in Cowork | Cowork offers the **Automatically approve** mode when an administrator sets [`autoModeEnabled`](/docs/third-party/claude-desktop/configuration#automodeenabled) to `true`. |
  | User management via UI and RBAC | With the [Enterprise Admin Console](/docs/third-party/claude-desktop/admin-console), administrators add users and groups, connect single sign-on and SCIM, assign administrator roles, and set per-group permission policies from **Organization settings** on claude.ai. Deployments configured through MDM or a bootstrap server manage access through those channels. |
  | Monitoring | Many capabilities of the Compliance API and Analytics API can be achieved via [OpenTelemetry export](/docs/third-party/claude-desktop/telemetry#sending-telemetry-to-your-own-collector) to your own collector. |
  | Telemetry | Claude Desktop on 3P sends [crash reports and product analytics](/docs/third-party/claude-desktop/telemetry#telemetry-categories) to Anthropic by default. This telemetry contains no prompt or response content, and you can fully disable it via managed configuration. |
  | Data handling | [Data handling](/docs/third-party/claude-desktop/overview#data-handling-by-provider) at the inference endpoint depends on the provider you configure. For Google Cloud's Agent Platform and Amazon Bedrock, data handling is governed by Google Cloud and Amazon Bedrock respectively. For Microsoft Foundry, Anthropic operates the Claude models and handles conversation data as an independent processor for Microsoft. For the Anthropic API, Anthropic processes conversation data under your Anthropic agreement, as described on the [Claude API](/docs/third-party/claude-desktop/claude-api) page. |
</Accordion>
