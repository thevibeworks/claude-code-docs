> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Features

> Feature comparison between Claude Enterprise and Claude Desktop on third-party (3P)

The tables below compare the feature set of Claude Desktop on third-party (3P) to Claude Enterprise.

## Key differences

**Configuration.** Both are administered from the web-based [admin console](/docs/third-party/claude-desktop/admin-console) in **Organization settings** on claude.ai. Claude Desktop on 3P can also be configured through [MDM](/docs/third-party/claude-desktop/mdm) (Jamf, Intune, Group Policy) or a [bootstrap server](/docs/third-party/claude-desktop/bootstrap).

**Telemetry.** Claude Desktop on 3P sends usage and debugging metrics only, and these can be fully disabled via managed configuration. Claude Enterprise does not offer telemetry toggles. See [Telemetry and egress](/docs/third-party/claude-desktop/telemetry).

**Inference.** Claude Desktop on 3P routes all inference through the provider you configure, and data handling at the inference endpoint depends on that provider. For Google Cloud's Agent Platform and Amazon Bedrock, data handling is governed by Google Cloud and Amazon Bedrock respectively. For Microsoft Foundry, Anthropic operates the Claude models and handles conversation data as an independent processor for Microsoft. See [Data handling by provider](/docs/third-party/claude-desktop/overview#data-handling-by-provider) on the Overview page for each provider's data path.

**Pricing.** Claude Desktop on 3P is token-based consumption billed by your cloud provider, with no seat licensing.

**Features not available in 3P.** Features marked with — are absent from the UI. Users see a clean interface without error states for unavailable features.

## User features

| Feature                                                                                                                             | Claude Enterprise | Claude Desktop on 3P |
| ----------------------------------------------------------------------------------------------------------------------------------- | :---------------: | :------------------: |
| Chat                                                                                                                                |         ✓         |           ✓          |
| Cowork                                                                                                                              |         ✓         |           ✓          |
| Code                                                                                                                                |         ✓         |           ✓          |
| Auto mode (Code)                                                                                                                    |         ✓         |           ✓          |
| [SSH remote Code sessions](/docs/third-party/claude-desktop/ssh-remote-sessions)                                                         |         ✓         |           ✓          |
| Automatically approve / Skip all approvals (Cowork)                                                                                 |        — ¶        |           ✓          |
| Projects                                                                                                                            |         ✓         |           ✓          |
| Code execution for analysis                                                                                                         |         ✓         |           ✓          |
| Web search                                                                                                                          |         ✓         |          ✓ §         |
| File access, upload, and export                                                                                                     |         ✓         |           ✓          |
| Local MCP                                                                                                                           |         ✓         |           ✓          |
| Remote MCP                                                                                                                          |         ✓         |           ✓          |
| [Microsoft 365](/docs/third-party/claude-desktop/connectors-m365) and [GitHub](/docs/third-party/claude-desktop/connectors-github) connectors |         ✓         |           ✓          |
| Skills, plugins, and hooks                                                                                                          |         ✓         |           ✓          |
| Artifacts                                                                                                                           |         ✓         |           ✓          |
| Memory                                                                                                                              |         ✓         |          ✓ †         |
| Scheduled tasks                                                                                                                     |         ✓         |           ✓          |
| Global languages                                                                                                                    |         ✓         |           ✓          |
| Project and plugin sharing                                                                                                          |         ✓         |           —          |
| Plugin marketplaces                                                                                                                 |         ✓         |           ✓          |
| Mobile                                                                                                                              |         ✓         |           —          |
| claude.ai web-based access                                                                                                          |         ✓         |           —          |
| Voice mode                                                                                                                          |         ✓         |           —          |
| Claude in Chrome                                                                                                                    |         ✓         |           —          |
| Claude Design                                                                                                                       |         ✓         |           —          |
| Claude Security                                                                                                                     |         ✓         |           —          |
| Claude Tag                                                                                                                          |         ✓         |           —          |
| Computer use                                                                                                                        |         —         |           —          |

§ Amazon Bedrock deployments and gateways that do not forward Anthropic server tools need a web search provider configured first; see [Web search options](/docs/third-party/claude-desktop/web-tools#web-search-options).

† Memory in Claude Desktop on 3P is stored on the device, not on Anthropic infrastructure. Users can review, delete, or pause it under **Settings → Cowork → Memory**; see [Memory](/docs/third-party/claude-desktop/data-storage#memory). Chat-history search and nightly summary generation are not available in Chat on 3P.

¶ Cowork's Automatically approve and Skip all approvals modes are not available for Claude Enterprise organizations.

## Admin features

| Feature                                                                                       | Claude Enterprise | Claude Desktop on 3P |
| --------------------------------------------------------------------------------------------- | :---------------: | :------------------: |
| Endpoint / gateway configuration                                                              |         —         |           ✓          |
| Skills, hooks, and plugins distribution                                                       |         ✓         |           ✓          |
| MCP server allowlist                                                                          |         ✓         |           ✓          |
| Feature toggles (web search, local MCP, etc.)                                                 |         ✓         |           ✓          |
| Auto-updates                                                                                  |         ✓         |           ✓          |
| Per-user usage caps                                                                           |         ✓         |           ✓          |
| [Data retention policies](/docs/third-party/claude-desktop/configuration#chatsessionretentiondays) |         ✓         |           ✓          |
| Compliance API                                                                                |         ✓         |          — ‡         |
| Analytics API                                                                                 |         ✓         |          — ‡         |
| OpenTelemetry export                                                                          |         ✓         |           ✓          |
| User management via UI                                                                        |         ✓         |          ✓ ◊         |
| RBAC                                                                                          |         ✓         |          ✓ ◊         |

‡ Many of these capabilities can be achieved via OpenTelemetry export to your own collector. See [Monitoring](/docs/cowork/monitoring).

◊ With the [Enterprise Admin Console](/docs/third-party/claude-desktop/admin-console), administrators add users and groups, connect single sign-on and SCIM, assign administrator roles, and set per-group permission policies from **Organization settings** on claude.ai. Deployments configured through MDM or a bootstrap server manage access through those channels.
