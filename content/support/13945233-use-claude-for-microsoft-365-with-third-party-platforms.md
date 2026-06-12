Title: Use Claude for Microsoft 365 with third-party platforms

URL Source: https://support.claude.com/en/articles/13945233-use-claude-for-microsoft-365-with-third-party-platforms

Markdown Content:
If your organization uses AWS Bedrock, Google Cloud Vertex AI, or an LLM gateway to access Claude, you can use the Claude for Excel, Claude for PowerPoint, Claude for Word, and Claude for Outlook add-ins without a Claude account. The add-in connects through your organization's infrastructure, so your prompts and responses stay within your existing trust boundary.

There are four connection paths, depending on how your organization accesses Claude:

Your IT admin chooses the path during deployment. As an end user, the experience is the same regardless of which path your organization uses.

## Requirements

Requirements vary by connection path.

**All paths:**

**LLM gateway:**

**Bedrock direct:**

**Vertex AI direct:**

**Foundry direct:**

Your organization's IT team manages these resources. If you don't have the credentials you need, contact them—Anthropic can't provide or reset them for you.

## Network allowlist

The add-in needs to reach specific domains to function. Which domains depend on whether your organization uses the Anthropic API directly (1P) or a third-party platform (3P). Share the applicable table with your network or security team so they can allowlist these domains.

### Anthropic API (1P)

Use this table if people in your organization sign in with a Claude account and inference goes to api.anthropic.com.

**Domain****Required when****Purpose**
pivot.claude.ai Always Add-in host. Serves the task pane UI and proxies analytics, icon search, skill downloads, and telemetry.
claude.ai Always Anthropic OAuth sign-in and feature-flag evaluation.
api.anthropic.com Always Claude inference API, file uploads, code-execution containers, and the MCP connector registry.
appsforoffice.microsoft.com Always Microsoft Office.js runtime script. Required by every Office add-in.
o1158394.ingest.us.sentry.io Optional Crash and error reporting. Blocking this degrades diagnostics only; the add-in still works.
mcp-proxy.anthropic.com If using MCP connectors Proxy for MCP connector tool calls.
bridge.claudeusercontent.com If using work across apps WebSocket bridge for the work across apps feature.

### Third-party platforms (3P)

Use this table if people in your organization sign in with Microsoft Entra ID and inference goes to your LLM gateway, Bedrock, or Vertex AI.

**Domain****Required when****Purpose**
pivot.claude.ai Always Add-in host. Serves the task pane UI and proxies analytics, icon search, and telemetry.
claude.ai/api/Always Feature-flag evaluation. No sign-in; the add-in only fetches its configuration from here.
appsforoffice.microsoft.com Always Microsoft Office.js runtime script (required by every Office add-in).
login.microsoftonline.com Always Microsoft Entra ID sign-in via Nested App Auth. Reads admin-provisioned gateway config and issues tokens for direct-cloud auth.
o1158394.ingest.us.sentry.io Optional Crash and error reporting. Blocking this degrades diagnostics only; the add-in still works.
Your LLM gateway URL If using an LLM gateway Your organization's LLM gateway (LiteLLM, Portkey, Kong, etc.). Inference goes here instead of api.anthropic.com.
sts.amazonaws.com If using Bedrock direct AWS STS. Exchanges the Entra ID token for temporary Bedrock credentials.
bedrock-runtime.<region>.amazonaws.com If using Bedrock direct Bedrock inference endpoint. Replace <region> with your configured AWS region (for example, us-east-1).
accounts.google.com If using Vertex AI direct Google OAuth consent screen.
oauth2.googleapis.com If using Vertex AI direct Google OAuth token exchange and refresh.
aiplatform.googleapis.com If using Vertex AI direct Vertex AI global inference endpoint.
<region>-aiplatform.googleapis.com If using Vertex AI direct Vertex AI regional inference endpoint. Replace <region> with your configured GCP region (for example, us-east5).
<resource>.services.ai.azure.com If using Foundry direct Azure AI Foundry inference endpoint. Replace <resource> with your resource name.

## Deploy the add-in for third-party use (IT admins)

Use the `claude-in-office` plugin to configure and deploy the add-in across your organization. This tool handles provisioning cloud resources (if using Bedrock or Vertex AI direct), generating the add-in manifest, and obtaining admin consent in a single guided flow.

### Use the setup wizard

The wizard walks you through your connection path:

When the wizard completes, the add-in is ready to deploy tenant-wide.

You can use the following commands inside a `claude-in-office` session:

**Command****What it does**
`/claude-in-office:setup`Interactive wizard—provisions cloud resources, admin consent, writes manifest
`/claude-in-office:manifest`Generates the customized add-in manifest XML
`/claude-in-office:consent`Generates the Azure admin consent URL for the add-in's app registration
`/claude-in-office:update-user-attrs`Writes per-user config via Microsoft Graph extension attributes
`/claude-in-office:bootstrap`Walks you through building a bootstrap endpoint—per-user MCP servers, skills, and dynamic config
`/claude-in-office:debug`Diagnoses deployment issues—stale config, connect failures, missing add-in

### Custom inference headers

If your inference endpoint or any proxy in front of it requires extra headers—for example, an internal application ID for cost accounting—set `inference_headers` to a JSON object of header name/value pairs. The add-in attaches these headers to every model-inference request it sends, so you don't need a separate header-injecting proxy.

This applies to gateway, Amazon Bedrock, and Google Vertex AI deployments.

Example: `inference_headers={"x-application-id":"app123"}`

You can set `inference_headers` in the manifest (org-wide) or in the bootstrap endpoint response (per-user).

### What the wizard provisions

The wizard automates resource creation based on your connection path. Here's what it sets up:

**LLM gateway**: No cloud resources to provision. The wizard collects your gateway URL and token, then generates the manifest.

**Bedrock direct**: Creates an IAM OIDC identity provider that trusts Microsoft Entra ID tokens, a role with bedrock:InvokeModel and bedrock:InvokeModelWithResponseStream permissions, and a trust policy scoped to the Claude add-in's application ID.

**Vertex AI direct**: Walks you through creating a Google OAuth client in the GCP Console (this step can't be automated via CLI), enables the Vertex AI API, and captures the client ID and secret for the manifest.

**Foundry direct**: No cloud resources to provision; the wizard collects the resource name and API key for the manifest.

### Per-user configuration with Microsoft Entra extension attributes

If some values vary per user—for example, different gateway tokens or different AWS roles for different teams—the wizard can write per-user configuration via Microsoft Graph extension attributes. Run `/claude-in-office:update-user-attrs` with the per-user keys after the initial setup.

### Per-user configuration with a bootstrap endpoint

If some values vary per user or if per-user values need server-side logic—for example, MCP server lists, skills, inference headers, or short-lived gateway tokens vended from your secrets store—configure a bootstrap endpoint instead. Set `bootstrap_url` in the manifest to an HTTPS endpoint you host; the add-in calls it with the user's Entra token and applies whatever JSON you return. Run `/claude-in-office:bootstrap` for the request/response contract and a handler scaffold.

### Deploy to Microsoft 365

After the wizard generates your manifest:

Propagation to users takes up to 24 hours (usually much faster). The add-in appears under **Home**>**Add-ins** in Excel, PowerPoint, Word, and Outlook once it lands.

## Deploy to Outlook

Outlook requires a separate manifest file from Excel, PowerPoint, and Word. Microsoft uses a different add-in schema for mail applications, so the two cannot be combined into one file. When you tell the setup wizard you are deploying to Outlook, it generates a second file named manifest-outlook.xml alongside manifest.xml. Upload each file as its own custom app in the Microsoft 365 Admin Center, following the same steps described in the next section.

### Grant Microsoft Graph consent

Claude for Outlook reads mail and calendar data through Microsoft Graph, which requires a one-time tenant-wide grant from a Global Administrator. This is separate from the Integrated apps deployment above. Have a Global Admin open the below admin consent link below in a browser where they are signed in to your Microsoft 365 tenant:

After deploying the add-in, your users can connect by following the steps below.

## Connection instructions for end users

### LLM gateway

Your credentials are stored locally in your browser's localStorage within the add-in's sandboxed iframe. They aren't synced to Anthropic's servers. Because the Office add-in runs inside a sandboxed iframe within the Microsoft application, it can't use your OS keychain the way Claude Code does—for this reason, only enter gateway-issued tokens, not raw cloud provider credentials.

### Bedrock, Vertex AI, or Foundry direct

If you see an error at sign-in, confirm with your IT team that your account is in the group assigned to the add-in.

### Change or update your connection

If your API token expires or your IT team gives you a new URL, go to "Settings" in the add-in sidebar, enter the new values, and select "Test connection."

## Gateway requirements for IT teams

The Office add-ins support the same three API formats as Claude Code. Set `gateway_api_format` in your add-in manifest to tell the add-in which format your gateway speaks.

### CORS requirements

The add-in's taskpane loads from [`https://pivot.claude.ai`](https://pivot.claude.ai/). Every request to your gateway is therefore cross-origin, and the browser will silently discard any response that lacks CORS headers.

Your gateway must return `Access-Control-Allow-Origin: https://pivot.claude.ai` (or `*`) on every response: GET, POST, OPTIONS, and all error responses. Setting it only on the OPTIONS preflight is not sufficient. For the preflight, return `Access-Control-Allow-Headers: *`.

### Required endpoints

The endpoints your gateway must expose depend on which API format it speaks. Set `gateway_api_format` in your manifest to match.

**gateway_api_format: anthropic (default)**

**gateway_api_format: bedrock**

Native Bedrock InvokeModel pass-through. `gateway_url` must point at the pass-through prefix (for example, [`https://litellm.example.com/bedrock`](https://litellm.example.com/bedrock)).

**gateway_api_format: vertex**

Native Vertex pass-through. `gateway_url` must include the API-version segment (for example, [`https://litellm.example.com/vertex_ai/v1`](https://litellm.example.com/vertex_ai/v1)). Also requires `gcp_project_id` and `gcp_region` so the add-in can build the path.

### Required header

For `anthropic` and `vertex` formats, the gateway must forward the `anthropic-version` request header to the upstream provider.

For `bedrock` format, the SDK puts `anthropic_version` in the request body instead — the gateway must preserve it there.

Failure to forward the header or preserve the body field may result in reduced functionality or prevent the add-in from working.

### Authorization header

The add-in can send your gateway’s authorization token in either the `x-api-key` or the `Authorization` header.

### Model discovery

On login, the add-in attempts to discover available Claude models via GET /v1/models. If your gateway doesn't expose a model list at that path, the add-in falls back to prompting the user for a model ID manually.

### Differences from Claude Code gateway setup

**Aspect****Claude Code****Claude for Excel, PowerPoint, Word, and Outlook**
Credential storage OS keychain or environment variables Browser localStorage (sandboxed iframe)
Auth configuration Environment variables, settings file, helper scripts Manual entry in add-in UI (gateway), Entra ID (direct cloud), or Azure API key (Foundry)
Token refresh Supports helper scripts for rotation Manual re-entry in settings (gateway) or automatic via Entra ID (direct cloud)
Custom model names Configurable via environment variables Not configurable in v1

## Example gateway configuration with LiteLLM

Many organizations use **LiteLLM** as their gateway. Below is a minimal litellm_config.yaml for routing Office add-in requests to Anthropic, Bedrock, or Vertex.

### Routing to Anthropic directly

**yaml**

### Routing to Amazon Bedrock

**yaml**

### Routing to Google Cloud Vertex AI

**yaml**

### Routing to Azure

**yaml**

## What Anthropic collects

Even when inference goes through your own infrastructure, the add-in communicates with pivot.claude.ai to load its interface and with claude.ai/api/ to evaluate feature flags. These connections transmit operational telemetry—such as which features are used, performance timings, and error rates—so Anthropic can maintain and improve the add-in experience. They don't transmit your prompts or Claude's responses.

Anthropic collects information in accordance with AWS Bedrock, Google Cloud Vertex AI, or Microsoft Azure's terms, consistent with Anthropic's arrangements with customers. Anthropic doesn't have access to a customer's AWS, Google, or Microsoft instance, including prompts or outputs it contains. Anthropic doesn't train generative models with such content or use it for other purposes. Anthropic can access metadata—such as tool use, token counts, and similar items—and use such metadata for analytic and product improvement purposes.

For details on what your organization's gateway or cloud provider logs, contact your IT team.

## How this differs from signing in with a Claude account

When you sign in with a Claude account, the add-ins connect directly to Anthropic. When you connect through a third-party platform, the add-ins send inference requests to your organization's infrastructure instead, and your IT team controls how that traffic is routed and logged.

Some features that rely on having a Claude account aren't available through third-party platforms yet, but we're working on adding support:

**Feature****Claude account****Third-party platform**
Chat with your spreadsheet, deck, or document✓✓
Read and edit cells, slides, formulas, and document text✓✓
Connectors (S&P, FactSet, etc.)✓✓
Working across apps✓—
Skills✓✓
File uploads✓✓
Web search✓Vertex only

If your team needs these features, talk to your Claude admin about which sign-in path fits your organization.

### Add MCP connectors to third-party add-ins

MCP connectors are now supported in Claude for Excel, PowerPoint, and Word. As an administrator, you can set the MCP gateway in the add-in manifest following the documentation here: **[MCP servers](https://github.com/anthropics/financial-services-plugins/blob/main/claude-in-office/commands/manifest.md#mcp-servers)**. If you prefer to use the bootstrap endpoint, you can configure MCP connectors following the documentation here: **[`mcp_servers`](https://github.com/anthropics/financial-services-plugins/blob/main/claude-in-office/commands/bootstrap.md#mcp_servers)**.

### Add Skills to third-party add-ins

Skills are now supported in Claude for Excel, PowerPoint, and Word. The Anthropic financial services skills are available by default. Additional Skills may be added by administrators or manually by individuals.

Administrators can add skills using the bootstrap endpoint, following the documentation here: **[`skills`](https://github.com/anthropics/financial-services-plugins/blob/main/claude-in-office/commands/bootstrap.md#skills)**.

Individuals can manually upload local skills (either as a .zip, .skill, or SKILL.md file) and manage them individually. Skills are uploaded by selecting the "+" button, then Skills → "Upload Skills."

### Add file uploads to third-party add-ins

File uploads are now supported in Claude for Excel, PowerPoint, and Word. Individuals can upload files by selecting the "+" button, then "Add files or photos" .

## Troubleshooting

### "Connection refused" or network error

The gateway URL or cloud endpoint is unreachable from the user's network. Verify the URL is correct, the service is running, and there are no firewall or VPN restrictions blocking the connection. Check the **Network allowlist** section above to confirm all required domains are allowed.

### 401 Unauthorized or "Invalid token"

The auth token is invalid or expired. For gateway connections, confirm the token with your IT team. For direct-cloud connections, verify the user's Entra ID account is in the assigned group and that the OIDC trust or OAuth client is configured correctly. For Foundry, regenerate the key in Azure Portal → Keys and Endpoint.

### 403 Forbidden or "Access denied"

The token is valid but lacks the right permissions. For Bedrock, verify the IAM role has `bedrock:InvokeModel` permissions. For Vertex, verify the service account has `aiplatform.endpoints.predict` permissions. For gateways, check the token's scope with your IT admin. For Foundry, check the resource’s networking rules, or confirm the key belongs to the right resource.

### 404 Not found

The add-in couldn't reach the expected API path. For gateways, verify the URL is the base URL (for example, [https://litellm-server:4000)—don't](https://litellm-server:4000)%E2%80%94don't) include /v1/messages in the URL field.

### 500 or other server errors

The gateway or cloud provider encountered an internal error. Check your gateway logs (for example, docker logs litellm if using LiteLLM) for upstream provider errors. Try the request again, and contact your IT admin if the issue persists.

### "No models available"

The add-in couldn't find Claude models. For gateways, your gateway may not expose a model list at GET /v1/models. Your IT team can either configure the gateway to serve a model list or give you a specific model ID to enter manually. For Bedrock or Vertex, confirm that at least one Claude model (Claude Sonnet 4.5 or later) is enabled in your account and region. For Foundry, confirm at least one Claude model is deployed in the resource (Model catalog).

### Streaming responses fail or hang

Verify that your gateway supports Server-Sent Events (SSE) pass-through. Some proxy configurations strip or buffer SSE connections, which prevents streaming responses from reaching the add-in.

### A feature I expected isn't available

Connectors, skills, file uploads, and Working Across Apps aren't available through third-party platforms yet. If you need these, ask your admin about signing in with a Claude account instead.

* * *

Related Articles

[Use Claude in Microsoft Foundry](https://support.claude.com/en/articles/12864745-use-claude-in-microsoft-foundry)[Public Sector FAQs](https://support.claude.com/en/articles/13756069-public-sector-faqs)[Model availability in Claude for Government](https://support.claude.com/en/articles/14503794-model-availability-in-claude-for-government)[Real-time cyber safeguards on Claude](https://support.claude.com/en/articles/14604842-real-time-cyber-safeguards-on-claude)[Covered Models](https://support.claude.com/en/articles/15425695-covered-models)
