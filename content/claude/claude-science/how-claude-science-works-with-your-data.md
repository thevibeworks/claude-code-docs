> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# How Claude Science works with your data

> Claude Science is a local-first application.

Claude Science is a local-first application. Conversation history and artifacts are stored only on the member's device. Anthropic doesn't host a session store for the app and has nothing to browse, sync, or export. Prompts and completions sent to the model are processed by Anthropic and handled under Anthropic's standard retention and Trust & Safety policies. The following sections cover what Anthropic does receive.

## What Anthropic receives

Each time the app calls Claude, the prompt and Claude's response travel to Anthropic's servers and are logged under Anthropic's standard retention policy for model traffic (see How long do you store my organization's data in the Privacy Center), the same policy that applies to other Claude products. If your organization has CMEK enabled, model-call logging follows the same CMEK handling as your other Claude products. Your organization's Custom Data Retention setting doesn't change that retention period; that setting governs conversation, project, and artifact data stored on Anthropic's servers, which this product doesn't create. The app also sends product-usage telemetry (event counts and timings, not conversation content), which can be turned off through device configuration.

## Remote compute

When a member chooses to connect the app to remote compute (an owned server or cloud account they control), the app sends code and data directly to that destination. That traffic doesn't pass through Anthropic. Admins can't yet restrict whether members can connect to remote compute. For setup details, see [Remote compute clusters](/docs/claude-science/remote-compute-clusters) and [Compute providers](/docs/claude-science/compute-providers) in the user documentation.

## Connectors

Directory connectors you publish as an admin are reached through Anthropic's hosted connector service, so your directory connector permissions and tunnels apply. Connectors a member adds locally (either running on their own computer or pointing at a custom URL) talk to their app directly, without routing through Anthropic.

## What this means for you as an admin

Because conversations and artifacts live on members' computers, the Anthropic-side data controls (Custom Data Retention, Org Data Export, and the Compliance API) don't reach them. Device management is the control you have for that data: your device management software (such as your MDM or EDR) governs the app's local folder the same way it governs any other local application data. Identity controls (SSO, SCIM, roles) apply because sign-in goes through claude.ai; see [Admin controls](/docs/claude-science/admin-controls) for what IP allowlisting and session duration cover.
