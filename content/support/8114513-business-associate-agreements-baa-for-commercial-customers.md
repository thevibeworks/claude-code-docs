Title: Business Associate Agreements (BAA) for Commercial Customers

URL Source: https://support.claude.com/en/articles/8114513-business-associate-agreements-baa-for-commercial-customers

Markdown Content:
_This article is about our commercial products such as Claude for Work and the Anthropic API. For our consumer products such as Claude Free, Pro, Max and when accounts from those plans use Claude Code, see[here](https://privacy.claude.com/en/collections/10663362-consumers)._

_For Claude Enterprise features to be covered under a BAA, an administrator must activate HIPAA compliance in the HIPAA-ready Claude Enterprise admin settings under “Data & Privacy” and sign Anthropic's BAA. Standard Claude Enterprise plans do not include BAA coverage without action from an administrator._

Anthropic provides a Business Associate Agreement (BAA) covering our HIPAA-ready services, such as use of our first-party API or Enterprise plans. Claude Enterprise administrators can sign the BAA directly when activating HIPAA compliance in the admin settings under “Data & Privacy.” If you are a self-managed account and do not see the admin setting, please contact sales.

To use the 1P API with PHI, your organization’s administrator will need to sign a BAA and then contact sales to get this turned on.

For clarity, the BAA does not cover Workbench and Console, Claude Free, Pro, Max, or Team plans, Cowork, or features currently in beta such as Claude in Office and Claude Design. As part of the BAA, customers of Anthropic’s HIPAA-ready services are subject to certain configuration requirements and limitations on what features/integrations are available.

Not all API features are covered; see the [Implementation Guide](https://trust.anthropic.com/resources?s=2zblcrsgb00l3x9l2tpjf&name=[anthropic]-2025-type-1-hipaa-report-(-1-p-api).pdf) for the full list of eligible and non-eligible features.

Below is a breakdown of what’s covered under the BAA, by feature and product surface.

## What’s covered under Anthropic’s BAA

**Claude Enterprise Feature****Availability**
Chat✅ _Covered as Eligible Services under Anthropic BAA*_
Projects✅ _Covered as Eligible Services under Anthropic BAA*_
Artifacts✅ _Covered as Eligible Services under Anthropic BAA*_
File creation & code execution✅ _Covered as Eligible Services under Anthropic BAA*_

⚠️ _excluding network access and use of external websites_
Voice✅ _Covered as Eligible Services under Anthropic BAA*_
Web Search✅ _Covered as Eligible Services under Anthropic BAA*_
Research✅ _Covered as Eligible Services under Anthropic BAA*_
Skills✅ _Covered as Eligible Services under Anthropic BAA*_
MCPs / Connectors⚠️ _Available to use but sending data to 3rd parties via this feature isn’t covered under Anthropic’s BAA. Administrators who enable these features are responsible for ensuring their workforce uses them in compliance with applicable legal obligations._
Enterprise Search / “Ask Your Org”⚠️ _Available to use but sending data to 3rd parties via this feature isn’t covered under Anthropic’s BAA. Administrators who enable this feature are responsible for ensuring their workforce uses it in compliance with applicable legal obligations._
Claude in Chrome⚠️ _Available to use but sending data to 3rd parties via this feature isn’t covered under Anthropic’s BAA. Administrators who enable this feature are responsible for ensuring their workforce uses it in compliance with applicable legal obligations._
Cowork⚠️ _Available to use but feature is not covered under Anthropic’s BAA. Administrators who enable this feature are responsible for ensuring their workforce uses it in compliance with applicable legal obligations._
Claude for Office (Excel,PowerPoint, and Docs (beta))⚠️ _Available to use but some features are in beta and not covered under Anthropic’s BAA. Administrators who enable this feature are responsible for ensuring their workforce uses it in compliance with applicable legal obligations._
Claude Design [beta]⚠️ _Available to use but feature is in beta and not covered under Anthropic’s BAA. Administrators who enable this feature are responsible for ensuring their workforce uses it in compliance with applicable legal obligations._

**Claude Code Feature****Availability**
Claude Code CLI

(via 1P API console)✅ _Only covered under the BAA with ZDR enabled. If your org needs ZDR for 1P API, please contact a sales representative._

⚠️_Without ZDR enabled, this feature is available to use but is not covered under Anthropic’s BAA._
Claude Code CLI

(via Claude Enterprise OAuth)✅ _Only covered under the BAA with ZDR enabled.1 ZDR is available for qualified accounts only. If your org needs to use PHI with this feature, please contact a sales representative to evaluate options._

⚠️_Without ZDR enabled, this feature is available to use but is not covered under Anthropic’s BAA._
Claude Code in the desktop (local mode)✅ _Only covered under the BAA with ZDR enabled.1 ZDR is available for qualified accounts only. If your org needs to use PHI with this feature, please contact a sales representative to evaluate options._

⚠️_Without ZDR enabled, this feature is available to use but is not covered under Anthropic’s BAA._
Claude Code in the desktop (remote mode)⚠️ _Available to use without ZDR, but this feature is not covered under Anthropic’s BAA. This feature is incompatible with ZDR._
Claude Code in the web [beta]⚠️ _Available to use without ZDR, but this feature is not covered under Anthropic’s BAA. This feature is incompatible with ZDR._
Claude Code Review [beta]⚠️ _Available to use without ZDR but this feature is not covered under Anthropic’s BAA. This feature is incompatible with ZDR._
Claude Code Security [beta]⚠️ _Available to use without ZDR but this feature is not covered under Anthropic’s BAA. This feature is incompatible with ZDR._
Claude Code Computer Use [beta]⚠️ _Available to use without ZDR but this feature is not covered under Anthropic’s BAA. This feature is incompatible with ZDR._
Claude Code Remote Control [beta]⚠️ _Available to use without ZDR but this feature is not covered under Anthropic’s BAA. This feature is incompatible with ZDR._

*Covered under versions of the BAA signed after 12/2/25

**API Feature (on a HIPAA Ready API Org)****Availability**
Messages API _See table below_
Token Counting API✅ _Covered as Eligible Services under Anthropic BAA*_
Models API✅ _Covered as Eligible Services under Anthropic BAA*_
Org Management API✅ _Covered as Eligible Services under Anthropic BAA*_
Compliance API✅ _Covered as Eligible Services under Anthropic BAA*_
Batch API❌ _Not covered under Anthropic BAA and not accessible for HIPAA-Ready API users_
Files API [beta]❌ _Not covered under Anthropic BAA and not accessible for HIPAA-Ready API users_
Skills API [beta]❌ _Not covered under Anthropic BAA and not accessible for HIPAA-Ready API users_
Code Execution❌ _Not covered under Anthropic BAA and not accessible for HIPAA-Ready API users_
Computer Use [beta]❌ _Not covered under Anthropic BAA and not accessible for HIPAA-Ready API users_
Web Fetch❌ _Not covered under Anthropic BAA and not accessible for HIPAA-Ready API users_
External MCP⚠️ _Available to use but sending data to 3rd parties via this feature isn’t covered under Anthropic’s BAA. Administrators who enable these features are responsible for ensuring their workforce uses them in compliance with applicable legal obligations._

Data retention periods within a HIPAA-Enabled API Organization are described in Anthropic’s **[public documentation](http://platform.claude.com/docs/en/build-with-claude/api-and-data-retention)**.

The Messages API is covered as an Eligible Service under your BAA. The following Messages API features are covered under your BAA. Messages API features not listed below are not covered under your BAA.

**Messages API Feature****Availability**
Prompt Caching✅ _Covered as Eligible Services under Anthropic BAA*_
Structured Outputs✅ _Covered as Eligible Services under Anthropic BAA*_
Memory✅ _Covered as Eligible Services under Anthropic BAA*_
Web Search✅ _Covered as Eligible Services under Anthropic BAA*_
Bash tool✅ _Covered as Eligible Services under Anthropic BAA*_
Text Editor tool✅ _Covered as Eligible Services under Anthropic BAA*_

*Covered under versions of the BAA signed after 4/1/26

## Product BAA coverage by surface

### **CLAUDE ENTERPRISE**

(limited to features listed below)
**Core chat features****BAA coverage status**
Chat✅ Eligible under BAA
Projects✅ Eligible under BAA
Artifacts✅ Eligible under BAA
File creation & code execution✅ Eligible (excl. network / ext. sites)
Voice✅ Eligible under BAA
Web search✅ Eligible under BAA
Research✅ Eligible under BAA
Skills✅ Eligible under BAA
**Integrations (3rd-party data flows)****BAA coverage status**
MCPs / Connectors⚠️ 3P data flows not covered by Anthropic BAA
Enterprise Search ("Ask Your Org")⚠️ 3P data flows not covered by Anthropic BAA
Claude in Chrome⚠️ 3P data flows not covered by Anthropic BAA
**Claude Code****BAA coverage status**
Claude Code CLI (via 1P API console)✅ Eligible only with ZDR enabled
Claude Code CLI (via Claude Enterprise OAuth)✅ Eligible only with ZDR enabled (for qualified accounts)
Claude Code in Desktop (local mode)✅ Eligible only with ZDR enabled (for qualified accounts)
Claude Code in Desktop (remote mode)❌ Not covered under BAA
Claude Code in Web (beta)❌ Not covered under BAA
Claude Code Review (beta)❌ Not covered under BAA
Claude Code Security (beta)❌ Not covered under BAA
Claude Code Computer Use (beta)❌ Not covered under BAA
Claude Code Remote Control (beta)❌ Not covered under BAA
**Other beta features****BAA coverage status**
Cowork❌ Not covered under BAA
Claude for Office (Excel, PowerPoint, Docs (beta))❌ Not covered under BAA
Claude Design (beta)❌ Not covered under BAA
### **CLAUDE PLATFORM (1P API)**
**Native 1P API features****BAA coverage status**
Messages API (prompt caching, structured outputs, memory, web search, bash tool, text editor tool)✅ Eligible under BAA
Token Counting, Models, Org Management, Compliance APIs✅ Eligible under BAA
Batch API, Files API, Skills API, Code Execution, Computer Use, Web Fetch❌ Not covered under BAA
External MCP⚠️ 3P data flows not covered by Anthropic BAA
**ZDR-Eligible (covered under BAA with ZDR)****BAA coverage status**
Claude Code via API (CLI)✅ Eligible only with ZDR enabled (for qualified accounts)

Please see our **[Trust Portal](https://trust.anthropic.com/resources?s=rgirr4qe8u7ek8c2igx3&name=claude-for-enterprise-hipaa-ready-offering-implementation-guide)** for more information about our compliance commitments.

* * *

Related Articles

[HIPAA-ready Enterprise plans](https://support.claude.com/en/articles/13296973-hipaa-ready-enterprise-plans)[Public Sector FAQs](https://support.claude.com/en/articles/13756069-public-sector-faqs)[MCP connectors](https://support.claude.com/en/articles/14503689-mcp-connectors)[Real-time cyber safeguards on Claude](https://support.claude.com/en/articles/14604842-real-time-cyber-safeguards-on-claude)[Data retention practices for Mythos-class models](https://support.claude.com/en/articles/15425996-data-retention-practices-for-mythos-class-models)
