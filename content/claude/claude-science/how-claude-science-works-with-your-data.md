> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# How Claude Science works with your data

> What Anthropic receives from Claude Science, what stays on members' computers, and what Enterprise organizations can retrieve through the Compliance API.

Claude Science is a local-first application. Conversation history and artifacts are stored on the member's computer, and Anthropic doesn't sync them to the member's Claude account or to other devices. Anthropic does receive the prompts and responses the app exchanges with Claude, and handles them under its standard retention and Trust & Safety policies. For Enterprise organizations with the Compliance API enabled, Anthropic also retains those exchanges as session transcripts that the organization can retrieve; [Compliance API coverage](#compliance-api-coverage) explains what they contain. The following sections cover each of these, plus remote compute and connectors.

## What Anthropic receives

Each time the app calls Claude, the prompt and Claude's response travel to Anthropic's servers and are logged under Anthropic's standard retention policy for model traffic (see How long do you store my organization's data in the Privacy Center), the same policy that applies to other Claude products. If your organization has CMEK enabled, model-call logging follows the same CMEK handling as your other Claude products. Your organization's Custom Data Retention setting doesn't change how long these model-call logs are kept. It does apply to the session transcripts that Anthropic keeps for Enterprise organizations with the Compliance API enabled, described in [Compliance API coverage](#compliance-api-coverage). The app also sends product-usage telemetry (event counts and timings, not conversation content), which can be turned off through device configuration.

## Compliance API coverage

If your organization is on an Enterprise plan and has the [Compliance API](https://platform.claude.com/docs/en/manage-claude/compliance-api) enabled, your compliance team can retrieve transcripts of members' Claude Science sessions through it. Coverage of Claude Science sessions is in beta.

Anthropic captures a session only while the Compliance API is enabled for your organization and the member is signed in with their Claude Enterprise account. Transcripts aren't available for sessions that ran before capture began for your organization, although such sessions can still appear in the session list with their content marked unavailable. Anthropic records each session on its servers as the app's requests reach the Claude API, without installing anything extra on the member's computer or capturing anything beyond the requests the app already sends to Claude. Sessions in organizations with [HIPAA compliance enabled](/docs/claude-science/enable-claude-science#hipaa-organizations) aren't captured, and [Retrieve session transcripts](https://platform.claude.com/docs/en/manage-claude/compliance-sessions) lists the other cases the Compliance API doesn't return.

A transcript is reconstructed from what the app exchanged with Claude during the session: the member's prompts, Claude's responses, tool calls (including code and file content Claude wrote through them), and the text portions of tool results, including text from files that Claude read, subject to the size limits the Compliance API applies. Claude's extended thinking and the app's system prompt aren't included (a placeholder marks where the system prompt was), tool definitions and connector (MCP server) configuration are omitted, and images, PDFs, and other non-text content appear as placeholders. Content that never reached the Claude API, such as a local file the session never sent, isn't in the transcript.

Anthropic keeps these transcripts for six years from capture by default. If your organization has set a Custom Data Retention period (in claude.ai under Organization settings > Data and privacy), that period applies to the transcripts instead, and when more than one retention period is set, the shortest applies. If your organization uses CMEK, the transcripts are encrypted under your key. The session endpoints are read-only, so transcripts can't be deleted through the API before they expire; see [Retention and deletion](https://platform.claude.com/docs/en/manage-claude/compliance-sessions#retention-and-deletion) for the current terms.

The Compliance API's [Activity Feed](https://platform.claude.com/docs/en/manage-claude/compliance-activity-feed) also records changes to your Claude Science organization settings, such as turning the product on or off. The [Compliance API reference](https://platform.claude.com/docs/en/api/compliance/activities/list) describes these events.

## Remote compute

When a member chooses to connect the app to remote compute (an owned server or cloud account they control), the app sends code and data directly to that destination. That traffic doesn't pass through Anthropic. Admins can't yet restrict whether members can connect to remote compute. For setup details, see [Remote compute clusters](/docs/claude-science/remote-compute-clusters) and [Compute providers](/docs/claude-science/compute-providers) in the user documentation.

## Connectors

Directory connectors you publish as an admin are reached through Anthropic's hosted connector service, so your directory connector permissions and tunnels apply. Connectors a member adds locally (either running on their own computer or pointing at a custom URL) talk to their app directly, without routing through Anthropic.

## What this means for you as an admin

Because conversations and artifacts live on members' computers, Custom Data Retention and Org Data Export don't reach that local data. For Enterprise organizations with the Compliance API enabled, Anthropic also keeps session transcripts captured from the app's model calls, which include file text the app sent to Claude, and a record of settings changes (see [Compliance API coverage](#compliance-api-coverage)). Device management is the control you have for local data: your device management software (such as your MDM or EDR) governs the app's local folder the same way it governs any other local application data. Identity controls (SSO, SCIM, roles) apply because sign-in goes through claude.ai. See [Admin controls](/docs/claude-science/admin-controls) for what IP allowlisting and session duration cover.
