> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Features

> Feature comparison between Claude Enterprise and Claude Desktop on third-party (3P)

Claude Desktop on third-party (3P) is a deployment mode of Claude Desktop that routes all model inference through [a provider you configure](https://claude.com/docs/third-party/claude-desktop/overview.md). Pricing is token-based consumption billed by your cloud provider, with no seat licensing.

## Key differences from Claude Enterprise

The Claude Enterprise features in this table are enduring differences between Claude Enterprise and Claude Desktop on 3P. Anthropic doesn't have the technical ability to bring these features to Claude Desktop on 3P based on its local and third-party [architecture](https://claude.com/docs/third-party/claude-desktop/overview.md#architecture).

| Feature | Claude Enterprise | Claude Desktop on 3P |
| - | :-: | :-: |
| [Connect to your cloud provider for inference](https://claude.com/docs/third-party/claude-desktop/configuration.md#connection) |  No |  **Yes** |
| [Data residency in multiple regions](https://claude.com/docs/third-party/claude-desktop/overview.md#data-residency-and-international-deployment) |  No |  **Yes** |
| [Conversation history stored on device](https://claude.com/docs/third-party/claude-desktop/data-storage.md#where-data-lives) |  No |  **Yes** |
| Mobile and claude.ai web-based access |  **Yes** |  No |
| Sessions in Anthropic's cloud |  **Yes** |  No |
| Sharing between users |  **Yes** |  No |
| Voice mode |  **Yes** |  No |
| Claude Security and [Claude Tag](https://claude.com/docs/claude-tag/overview.md) |  **Yes** |  No |

## Features in Claude Desktop on 3P

Some features have limits or need setup, described in [Good to know about Claude Desktop on 3P](#good-to-know-about-claude-desktop-on-3p).

Claude Desktop on 3P is administered from the web-based [admin console](https://claude.com/docs/third-party/claude-desktop/admin-console.md), and can also be configured through [MDM](https://claude.com/docs/third-party/claude-desktop/mdm.md) or a [bootstrap server](https://claude.com/docs/third-party/claude-desktop/bootstrap.md).

> **Everyday work**
>
> * [Chat](https://claude.com/docs/third-party/claude-desktop/chat.md)
> * [Cowork](https://claude.com/docs/third-party/claude-desktop/configuration.md#coworktabenabled)
> * Projects
> * Artifacts
> * [Memory](https://claude.com/docs/third-party/claude-desktop/data-storage.md#memory)
> * [Scheduled tasks](https://claude.com/docs/third-party/claude-desktop/configuration.md#scheduledtasksenabled)
> * [Code execution for analysis](https://claude.com/docs/third-party/claude-desktop/chat.md#advanced-file-analysis)
> * [File access, upload, and export](https://claude.com/docs/third-party/claude-desktop/local-access.md)
> * Global languages
> * [Automatically approve in Cowork](https://claude.com/docs/third-party/claude-desktop/configuration.md#automodeenabled)

> **Web and browser**
>
> * [Built-in browser](https://claude.com/docs/third-party/claude-desktop/browser.md#built-in-browser)
> * [Web search](https://claude.com/docs/third-party/claude-desktop/web-tools.md#web-search)
> * [Claude in Chrome](https://claude.com/docs/third-party/claude-desktop/browser.md#claude-in-chrome)

> **Connectors and extensions**
>
> * [Microsoft 365](https://claude.com/docs/third-party/claude-desktop/connectors-m365.md) and [GitHub](https://claude.com/docs/third-party/claude-desktop/connectors-github.md) connectors
> * [Local MCP](https://claude.com/docs/third-party/claude-desktop/extensions.md#user-extensions)
> * [Remote MCP](https://claude.com/docs/third-party/claude-desktop/extensions.md#managed-mcp-servers-admin)
> * [Skills, plugins, and hooks](https://claude.com/docs/third-party/claude-desktop/extensions.md)
> * [Plugin marketplaces](https://claude.com/docs/third-party/claude-desktop/extensions.md#plugin-marketplaces-admin)

> **Code**
>
> * [Code](https://claude.com/docs/third-party/claude-desktop/code.md)
> * [Auto mode in Code](https://claude.com/docs/third-party/claude-desktop/configuration.md#automodeenabled)
> * [SSH remote Code sessions](https://claude.com/docs/third-party/claude-desktop/ssh-remote-sessions.md)

> **Administration**
>
> * [Admin console](https://claude.com/docs/third-party/claude-desktop/admin-console.md)
> * [Endpoint or gateway configuration](https://claude.com/docs/third-party/claude-desktop/configuration.md#connection)
> * [Skills, hooks, and plugins distribution](https://claude.com/docs/third-party/claude-desktop/extensions.md#organization-plugins-admin)
> * [MCP server allowlist](https://claude.com/docs/third-party/claude-desktop/extensions.md#controlling-user-extensions)
> * [Feature toggles](https://claude.com/docs/third-party/claude-desktop/configuration.md#capabilities)
> * [Auto-updates](https://claude.com/docs/third-party/claude-desktop/installation.md#updates)
> * [Per-user usage caps](https://claude.com/docs/third-party/claude-desktop/configuration.md#inferencemaxtokensperwindow)
> * [User management via UI](https://claude.com/docs/third-party/claude-desktop/admin-console.md#connect-your-identity-provider)
> * [RBAC](https://claude.com/docs/third-party/claude-desktop/admin-console.md#per-group-permission-policies)

> **Monitoring and retention**
>
> * [OpenTelemetry export](https://claude.com/docs/third-party/claude-desktop/telemetry.md#sending-telemetry-to-your-own-collector)
> * [Turning off telemetry](https://claude.com/docs/third-party/claude-desktop/telemetry.md#telemetry-categories)
> * [Data retention policies](https://claude.com/docs/third-party/claude-desktop/data-storage.md#automatic-deletion-of-idle-sessions)

## Good to know about Claude Desktop on 3P

> **Notes on setup, limits, monitoring, and data handling**
>
> | Topic | What to know |
> | - | - |
> | Sessions and scheduled tasks | Sessions are local, except [Code sessions over SSH](https://claude.com/docs/third-party/claude-desktop/ssh-remote-sessions.md), and the device must be awake to run long processes and scheduled tasks. |
> | Memory | [Memory](https://claude.com/docs/third-party/claude-desktop/data-storage.md#memory) in Claude Desktop on 3P is stored on the device, not on Anthropic infrastructure. Chat-history search and nightly summary generation are not available in Chat on 3P. |
> | Web search | Amazon Bedrock deployments and gateways that do not forward Anthropic server tools need a [web search provider](https://claude.com/docs/third-party/claude-desktop/web-tools.md#web-search-options) configured first. |
> | Claude in Chrome | Claude in Chrome works with Claude Desktop on 3P only in organizations managed from the [Enterprise Admin Console](https://claude.com/docs/third-party/claude-desktop/admin-console.md). |
> | Automatically approve in Cowork | Cowork offers the **Automatically approve** mode when an administrator sets [`autoModeEnabled`](https://claude.com/docs/third-party/claude-desktop/configuration#automodeenabled) to `true`. |
> | User management via UI and RBAC | With the [Enterprise Admin Console](https://claude.com/docs/third-party/claude-desktop/admin-console.md), administrators add users and groups, connect single sign-on and SCIM, assign administrator roles, and set per-group permission policies from **Organization settings** on claude.ai. Deployments configured through MDM or a bootstrap server manage access through those channels. |
> | Monitoring | Many capabilities of the Compliance API and Analytics API can be achieved via [OpenTelemetry export](https://claude.com/docs/third-party/claude-desktop/telemetry.md#sending-telemetry-to-your-own-collector) to your own collector. |
> | Telemetry | Claude Desktop on 3P sends [crash reports and product analytics](https://claude.com/docs/third-party/claude-desktop/telemetry.md#telemetry-categories) to Anthropic by default. This telemetry contains no prompt or response content, and you can fully disable it via managed configuration. |
> | Data handling | [Data handling](https://claude.com/docs/third-party/claude-desktop/overview.md#data-handling-by-provider) at the inference endpoint depends on the provider you configure. For Google Cloud's Agent Platform and Amazon Bedrock, data handling is governed by Google Cloud and Amazon Bedrock respectively. For Microsoft Foundry, Anthropic operates the Claude models and handles conversation data as an independent processor for Microsoft. For the Anthropic API, Anthropic processes conversation data under your Anthropic agreement, as described on the [Claude API](https://claude.com/docs/third-party/claude-desktop/claude-api.md) page. |
