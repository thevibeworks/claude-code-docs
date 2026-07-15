# Business Associate Agreements \(BAA\) for Commercial Customers

*This article is about our commercial products such as Claude for Work and the Anthropic API. For our consumer products such as Claude Free, Pro, Max and when accounts from those plans use Claude Code, see **[here](https://privacy.claude.com/en/collections/10663362-consumers)**.*

*For Claude Enterprise features to be covered under a Business Associate Agreement (BAA), the Primary Owner of the organization must activate HIPAA compliance in the HIPAA-ready Claude Enterprise organization settings under “Data and privacy” and accept Anthropic's BAA. Standard Claude Enterprise plans do not include BAA coverage without action from a Primary Owner.*

Anthropic provides a BAA covering our HIPAA-ready services, such as use of our first-party API or Enterprise plans. Claude Enterprise Primary Owners can accept the BAA directly when activating HIPAA compliance in the organization settings under “Data and privacy.”

**Important:** To use the 1P API with PHI, your organization’s Primary Owner will need to sign a BAA and then reach out to your Anthropic contact or our[**Sales team**](https://claude.com/contact-sales) to get this turned on.

For clarity, the BAA only covers the single organization that accepted it, and excludes features such as Workbench, Claude Console, Claude Cowork, or features currently in beta such as Claude in Office and Claude Design. As part of the BAA, customers of Anthropic’s HIPAA-ready services are subject to certain configuration requirements and limitations on what features/integrations are available.

Not all API features are covered; see the **[Implementation Guide](https://trust.anthropic.com/resources?s=2zblcrsgb00l3x9l2tpjf&name=[anthropic]-2025-type-1-hipaa-report-(-1-p-api).pdf)** for the full list of eligible and non-eligible features.

**Important: [Covered Models](https://support.claude.com/en/articles/15425695-covered-models)** require 30-day data retention and aren't available with zero data retention (ZDR) enabled. Some services, like Claude Code, are only covered under the BAA when ZDR is enabled, which means those services can't use Covered Models under the BAA. See **[Covered Models under Anthropic’s BAA](https://support.claude.com/en/articles/15455031)** for details.

Below is a breakdown of what’s covered under the BAA, by feature and product surface.

## What’s covered under Anthropic’s BAA

| **Claude Enterprise Feature**                         | **Availability**                                                                                                                                                                                                                                             |
| ----------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Chat                                                  | ✅ *Covered as Eligible Services under Anthropic BAA\**                                                                                                                                                                                                       |
| Projects                                              | ✅ *Covered as Eligible Services under Anthropic BAA\**                                                                                                                                                                                                       |
| Artifacts                                             | ✅ *Covered as Eligible Services under Anthropic BAA\**                                                                                                                                                                                                       |
| File creation & code execution                        | ✅ *Covered as Eligible Services under Anthropic BAA\**<br>⚠️ *excluding network access and use of external websites*                                                                                                                                         |
| Voice                                                 | ✅ *Covered as Eligible Services under Anthropic BAA\**                                                                                                                                                                                                       |
| Web Search                                            | ✅ *Covered as Eligible Services under Anthropic BAA\**                                                                                                                                                                                                       |
| Research                                              | ✅ *Covered as Eligible Services under Anthropic BAA\**                                                                                                                                                                                                       |
| Skills                                                | ✅ *Covered as Eligible Services under Anthropic BAA\**                                                                                                                                                                                                       |
| MCPs / Connectors                                     | ⚠️ *Available to use but sending data to 3rd parties via this feature isn’t covered under Anthropic’s BAA. Administrators who enable these features are responsible for ensuring their workforce uses them in compliance with applicable legal obligations.* |
| Enterprise Search / “Ask Your Org”                    | ⚠️ *Available to use but sending data to 3rd parties via this feature isn’t covered under Anthropic’s BAA. Administrators who enable this feature are responsible for ensuring their workforce uses it in compliance with applicable legal obligations.*     |
| Claude in Chrome                                      | ⚠️ *Available to use but sending data to 3rd parties via this feature isn’t covered under Anthropic’s BAA. Administrators who enable this feature are responsible for ensuring their workforce uses it in compliance with applicable legal obligations.*     |
| Cowork                                                | ⚠️ *Available to use but feature is not covered under Anthropic’s BAA. Administrators who enable this feature are responsible for ensuring their workforce uses it in compliance with applicable legal obligations.*                                         |
| Claude for Office (Excel,PowerPoint, and Docs (beta)) | ⚠️ *Available to use but some features are in beta and not covered under Anthropic’s BAA. Administrators who enable this feature are responsible for ensuring their workforce uses it in compliance with applicable legal obligations.*                      |
| Claude Design [beta]                                  | ⚠️ *Available to use but feature is in beta and not covered under Anthropic’s BAA. Administrators who enable this feature are responsible for ensuring their workforce uses it in compliance with applicable legal obligations.*                             |

| **Claude Code Feature**                              | **Availability**                                                                                                                                                                                                                                                                                                  |
| ---------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Claude Code CLI<br>(via 1P API console)<br>          | ✅ *Only covered under the BAA with ZDR enabled. If your org needs ZDR for 1P API, please contact a sales representative.*<br>⚠️*Without ZDR enabled, this feature is available to use but is not covered under Anthropic’s BAA.*                                                                                  |
| Claude Code CLI<br>(via Claude Enterprise OAuth)<br> | ✅ *Only covered under the BAA with ZDR enabled.1 ZDR is available for qualified accounts only. If your org needs to use PHI with this feature, please contact a sales representative to evaluate options.*<br>⚠️*Without ZDR enabled, this feature is available to use but is not covered under Anthropic’s BAA.* |
| Claude Code in the desktop (local mode)              | ✅ *Only covered under the BAA with ZDR enabled.1 ZDR is available for qualified accounts only. If your org needs to use PHI with this feature, please contact a sales representative to evaluate options.*<br>⚠️*Without ZDR enabled, this feature is available to use but is not covered under Anthropic’s BAA.* |
| Claude Code in the desktop (remote mode)             | ⚠️ *Available to use without ZDR, but this feature is not covered under Anthropic’s BAA. This feature is incompatible with ZDR.*                                                                                                                                                                                  |
| Claude Code in the web [beta]                        | ⚠️ *Available to use without ZDR, but this feature is not covered under Anthropic’s BAA. This feature is incompatible with ZDR.*                                                                                                                                                                                  |
| Claude Code Review [beta]                            | ⚠️ *Available to use without ZDR but this feature is not covered under Anthropic’s BAA. This feature is incompatible with ZDR.*                                                                                                                                                                                   |
| Claude Code Security [beta]                          | ⚠️ *Available to use without ZDR but this feature is not covered under Anthropic’s BAA. This feature is incompatible with ZDR.*                                                                                                                                                                                   |
| Claude Code Computer Use [beta]                      | ⚠️ *Available to use without ZDR but this feature is not covered under Anthropic’s BAA. This feature is incompatible with ZDR.*                                                                                                                                                                                   |
| Claude Code Remote Control [beta]                    | ⚠️ *Available to use without ZDR but this feature is not covered under Anthropic’s BAA. This feature is incompatible with ZDR.*                                                                                                                                                                                   |

*Covered under versions of the BAA accepted after 12/2/25

| **API Feature (on a HIPAA Ready API Org)** | **Availability**                                                                                                                                                                                                                                             |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Messages API                               | *See table below*                                                                                                                                                                                                                                            |
| Token Counting API                         | ✅ *Covered as Eligible Services under Anthropic BAA\**                                                                                                                                                                                                       |
| Models API                                 | ✅ *Covered as Eligible Services under Anthropic BAA\**                                                                                                                                                                                                       |
| Org Management API                         | ✅ *Covered as Eligible Services under Anthropic BAA\**                                                                                                                                                                                                       |
| Compliance API                             | ✅ *Covered as Eligible Services under Anthropic BAA\**                                                                                                                                                                                                       |
| Batch API                                  | ❌ *Not covered under Anthropic BAA and not accessible for HIPAA-Ready API users*                                                                                                                                                                             |
| Files API [beta]                           | ❌ *Not covered under Anthropic BAA and not accessible for HIPAA-Ready API users*                                                                                                                                                                             |
| Skills API [beta]                          | ❌ *Not covered under Anthropic BAA and not accessible for HIPAA-Ready API users*                                                                                                                                                                             |
| Code Execution                             | ❌ *Not covered under Anthropic BAA and not accessible for HIPAA-Ready API users*                                                                                                                                                                             |
| Computer Use [beta]                        | ❌ *Not covered under Anthropic BAA and not accessible for HIPAA-Ready API users*                                                                                                                                                                             |
| Web Fetch                                  | ❌ *Not covered under Anthropic BAA and not accessible for HIPAA-Ready API users*                                                                                                                                                                             |
| External MCP                               | ⚠️ *Available to use but sending data to 3rd parties via this feature isn’t covered under Anthropic’s BAA. Administrators who enable these features are responsible for ensuring their workforce uses them in compliance with applicable legal obligations.* |

Data retention periods within a HIPAA-Enabled API Organization are described in Anthropic’s **[public documentation](http://platform.claude.com/docs/en/build-with-claude/api-and-data-retention)**.

The Messages API is covered as an Eligible Service under your BAA. The following Messages API features are covered under your BAA. Messages API features not listed below are not covered under your BAA.

| **Messages API Feature** | **Availability**                                       |
| ------------------------ | ------------------------------------------------------ |
| Prompt Caching           | ✅ *Covered as Eligible Services under Anthropic BAA\** |
| Structured Outputs       | ✅ *Covered as Eligible Services under Anthropic BAA\** |
| Memory                   | ✅ *Covered as Eligible Services under Anthropic BAA\** |
| Web Search               | ✅ *Covered as Eligible Services under Anthropic BAA\** |
| Bash tool                | ✅ *Covered as Eligible Services under Anthropic BAA\** |
| Text Editor tool         | ✅ *Covered as Eligible Services under Anthropic BAA\** |

*Covered under versions of the BAA accepted after 4/1/26

## Product BAA coverage by surface

| **CLAUDE ENTERPRISE**<br>(limited to features listed below)                                        |                                                           |
| -------------------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| **Core chat features**                                                                             | **BAA coverage status**                                   |
| Chat                                                                                               | ✅ Eligible under BAA                                      |
| Projects                                                                                           | ✅ Eligible under BAA                                      |
| Artifacts                                                                                          | ✅ Eligible under BAA                                      |
| File creation & code execution                                                                     | ✅ Eligible (excl. network / ext. sites)                   |
| Voice                                                                                              | ✅ Eligible under BAA                                      |
| Web search                                                                                         | ✅ Eligible under BAA                                      |
| Research                                                                                           | ✅ Eligible under BAA                                      |
| Skills                                                                                             | ✅ Eligible under BAA                                      |
| **Integrations (3rd-party data flows)**                                                            | **BAA coverage status**                                   |
| MCPs / Connectors                                                                                  | ⚠️ 3P data flows not covered by Anthropic BAA             |
| Enterprise Search ("Ask Your Org")                                                                 | ⚠️ 3P data flows not covered by Anthropic BAA             |
| Claude in Chrome                                                                                   | ⚠️ 3P data flows not covered by Anthropic BAA             |
| **Claude Code**                                                                                    | **BAA coverage status**                                   |
| Claude Code CLI (via 1P API console)                                                               | ✅ Eligible only with ZDR enabled                          |
| Claude Code CLI (via Claude Enterprise OAuth)                                                      | ✅ Eligible only with ZDR enabled (for qualified accounts) |
| Claude Code in Desktop (local mode)                                                                | ✅ Eligible only with ZDR enabled (for qualified accounts) |
| Claude Code in Desktop (remote mode)                                                               | ❌ Not covered under BAA                                   |
| Claude Code in Web (beta)                                                                          | ❌ Not covered under BAA                                   |
| Claude Code Review (beta)                                                                          | ❌ Not covered under BAA                                   |
| Claude Code Security (beta)                                                                        | ❌ Not covered under BAA                                   |
| Claude Code Computer Use (beta)                                                                    | ❌ Not covered under BAA                                   |
| Claude Code Remote Control (beta)                                                                  | ❌ Not covered under BAA                                   |
| **Other beta features**                                                                            | **BAA coverage status**                                   |
| Cowork                                                                                             | ❌ Not covered under BAA                                   |
| Claude for Office (Excel, PowerPoint, Docs (beta))                                                 | ❌ Not covered under BAA                                   |
| Claude Design (beta)                                                                               | ❌ Not covered under BAA                                   |
| **CLAUDE PLATFORM (1P API)**                                                                       |                                                           |
| **Native 1P API features**                                                                         | **BAA coverage status**                                   |
| Messages API (prompt caching, structured outputs, memory, web search, bash tool, text editor tool) | ✅ Eligible under BAA                                      |
| Token Counting, Models, Org Management, Compliance APIs                                            | ✅ Eligible under BAA                                      |
| Batch API, Files API, Skills API, Code Execution, Computer Use, Web Fetch                          | ❌ Not covered under BAA                                   |
| External MCP                                                                                       | ⚠️ 3P data flows not covered by Anthropic BAA             |
| **ZDR-Eligible (covered under BAA with ZDR)**                                                      | **BAA coverage status**                                   |
| Claude Code via API (CLI)                                                                          | ✅ Eligible only with ZDR enabled (for qualified accounts) |

Please see our **[Trust Portal](https://trust.anthropic.com/resources?s=rgirr4qe8u7ek8c2igx3&name=claude-for-enterprise-hipaa-ready-offering-implementation-guide)** for more information about our compliance commitments.