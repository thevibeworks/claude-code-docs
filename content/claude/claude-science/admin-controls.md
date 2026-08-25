> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Admin controls

> Members sign in to Claude Science with their Claude account, so your identity and billing controls apply automatically.

Members sign in to Claude Science with their Claude account, so your identity and billing controls apply automatically. Because the app stores conversations on each member's computer rather than on Anthropic's servers, most of the data-handling controls Anthropic provides don't reach that data today. The tables show, for each admin setting, whether it governs Claude Science in beta. Status values describe Claude Science specifically; other Claude products may differ.

Legend: Supported / Partial / Not available / Not applicable

## Identity and access

| Admin setting         | Status in Claude Science beta | Note                                                                                                                                                                                                          |
| --------------------- | ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SSO (SAML / OIDC)     | Supported                     | Sign-in goes through claude.ai, so your SSO policy applies automatically.                                                                                                                                     |
| SCIM / Directory Sync | Supported                     | Deprovisioning a member revokes their access.                                                                                                                                                                 |
| Domain capture        | Supported                     | Inherited from claude.ai account creation.                                                                                                                                                                    |
| Members management    | Supported                     | Adding or removing org members controls who can sign in.                                                                                                                                                      |
| Built-in roles        | Supported                     | All built-in roles get access once the product is enabled for the org.                                                                                                                                        |
| Custom roles          | Supported                     | Custom roles can grant or deny access to the app.                                                                                                                                                             |
| Groups                | Supported                     | Roles assigned through groups carry through.                                                                                                                                                                  |
| IP allowlisting       | Partial                       | Claude inference is IP-gated. Gating remote compute (running code on the member's own SSH hosts or cloud accounts) is on the roadmap. Custom connectors and local operation are outside this setting's scope. |
| Session duration      | Partial                       | Limits the browser sign-in step only; the app stays signed in after that.                                                                                                                                     |

## Capability toggles

| Admin setting                    | Status in Claude Science beta | Note                                                                                                                                                                                                                                                                                                                                                                            |
| -------------------------------- | ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Org enable toggle                | Supported                     | Off by default for Team and Enterprise; an Owner or Primary Owner turns it on under Organization settings > Claude Science. Assigning seats doesn't turn it on.                                                                                                                                                                                                                 |
| Completion feedback (thumbs)     | Supported                     | The org toggle hides the feedback buttons, same as Chat.                                                                                                                                                                                                                                                                                                                        |
| Organization custom instructions | Supported                     | The org's custom instructions are applied to the app's model calls, the same as Chat.                                                                                                                                                                                                                                                                                           |
| Skills allowlist                 | Partial                       | Org-published skills appear, but members can also install local skills without restriction. Adding admin control is on the roadmap.                                                                                                                                                                                                                                             |
| Web search                       | Not available                 | The app offers web search regardless of this setting. Adding admin control is on the roadmap.                                                                                                                                                                                                                                                                                   |
| Code execution                   | Not available                 | This setting controls Chat's hosted code sandbox only. Claude Science runs code locally regardless of this setting; that's core to the product.                                                                                                                                                                                                                                 |
| Code execution network allowlist | Not available                 | This setting controls Chat's hosted code sandbox only and is not yet available for Claude Science in Organization settings. Claude Science's local sandbox keeps its own allowlist, which members manage in the app and administrators can extend per device with the sandbox network keys in the [configuration file reference](/docs/claude-science/configuration-file-reference). |
| Location metadata                | Not applicable                | The app doesn't derive, store, or send any geolocation data.                                                                                                                                                                                                                                                                                                                    |
| Memory                           | Not applicable                | The claude.ai Memory setting doesn't control memory in Claude Science. The app keeps its own memory locally on the member's device, and it's off by default.                                                                                                                                                                                                                    |
| Projects                         | Not applicable                | No Projects integration; the app uses local workspaces instead.                                                                                                                                                                                                                                                                                                                 |

## Connectors

| Admin setting                      | Status in Claude Science beta | Note                                                                                                                                                                                                                              |
| ---------------------------------- | ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Org-published Directory connectors | Supported                     | Connectors the admin publishes are available in the app.                                                                                                                                                                          |
| Per-role connector restrictions    | Partial                       | Enforced for Directory connectors, not for connectors members add locally.                                                                                                                                                        |
| Org plugin allowlist               | Partial                       | Org-published plugins appear automatically; members can still add their own local skills and connectors. Adding admin control to restrict local skills and connectors is on the roadmap.                                          |
| Connector tunnels                  | Partial                       | Directory connectors the admin publishes reach the app through tunnels. Local connectors the member adds run on their own computer, so tunnels don't apply. Custom remote connectors the member adds don't route through tunnels. |
| Custom connector restrictions      | Not available                 | Members can add their own custom connectors regardless of the organization allowlist. Adding admin control is on the roadmap.                                                                                                     |
| Desktop Extension allowlist        | Not applicable                | Desktop Extension directory isn't available in the app.                                                                                                                                                                           |

## Data and privacy

| Admin setting             | Status in Claude Science beta | Note                                                                                                                                                                                 |
| ------------------------- | ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| CMEK                      | Supported                     | Applies to the product's model traffic the same as Chat.                                                                                                                             |
| Data processing geography | Partial                       | Covers Anthropic-hosted processing, not remote compute you configure (code the member runs on their own SSH hosts or cloud accounts) or the member's computer (same as Claude Code). |
| HIPAA                     | Partial                       | HIPAA-ready organizations can enable the Claude Science beta, but usage isn't covered under the BAA.                                                                                 |
| Custom Data Retention     | Not available                 | The auto-delete window doesn't cover local data or the usage logs Anthropic keeps for this product.                                                                                  |

## Audit and compliance

| Admin setting   | Status in Claude Science beta | Note                                                                                |
| --------------- | ----------------------------- | ----------------------------------------------------------------------------------- |
| Audit log       | Not available                 | No events recorded yet; on the roadmap.                                             |
| Compliance API  | Not available                 | Admins can't export or delete this product's data through the API.                  |
| Org data export | Not available                 | The export doesn't include data stored on members' computers (same as Claude Code). |

## Usage, models, and billing

| Admin setting         | Status in Claude Science beta | Note                                                                                                                                          |
| --------------------- | ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| Usage limits          | Supported                     | Usage counts toward the same 5-hour and weekly limits as Claude Code and Cowork.                                                              |
| Billing and seats     | Supported                     | Uses the same seat as the rest of claude.ai.                                                                                                  |
| Model access controls | Supported                     | Uses the standard model API, so the org's allowed-model list and model access grants apply to both the model picker and the calls themselves. |
| Usage analytics       | Supported                     | Open Analytics from the user menu; the Claude Science tab shows usage, and spend is filterable by product on the Overview tab.                |

## Offboarding and local data

| Admin setting            | Status in Claude Science beta | Note                                                                                                                |
| ------------------------ | ----------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| Offboarding (local data) | Not available                 | Removing a member doesn't wipe data already on their computer.                                                      |
| Local deletion signal    | Not available                 | Deleting local data doesn't notify Anthropic to drop the matching server-side record early. This is on the roadmap. |
