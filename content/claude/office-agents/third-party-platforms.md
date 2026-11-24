> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Use Claude for M365 with third-party platforms

> Deploy the Office add-ins through Amazon Bedrock, Google Cloud Vertex AI, Azure AI Foundry, or an LLM gateway, without individual Claude accounts.

> [!WARNING]
>
> After the September and October 2026 Microsoft 365 updates on Windows, some
> users are missing their chat history and uploaded skills in the Claude add-in.
> Anthropic is working with Microsoft to solve this issue. In the meantime, see
> [what you and your IT team can do](https://claude.com/docs/office-agents/data-storage.md#chat-history-and-skills-missing-after-a-microsoft-365-update-on-windows).

Organizations using Amazon Bedrock, Google Cloud Vertex AI, Azure AI
Foundry, or an LLM gateway can deploy Claude's Office add-ins without
requiring individual Claude accounts. The add-in connects through your
organization's infrastructure, sends prompts to the provider your
organization chooses, and receives Claude's responses from it. See
[What Anthropic collects](#what-anthropic-collects) for what reaches
Anthropic on Amazon Bedrock, Google Cloud Vertex AI, and Azure AI
Foundry.

## Connection paths

Four connection paths are available. Your IT admin selects one during
deployment. End users see the same interface regardless.

| Path | How it works |
| - | - |
| LLM gateway | Requests route through your gateway (LiteLLM, Portkey, Kong, and others) to your chosen provider. Matches the pattern used by Claude Code. |
| Bedrock direct | The add-in authenticates via Microsoft Entra ID and calls Amazon Bedrock directly without intermediaries. |
| Vertex AI direct | The add-in authenticates through Google OAuth and calls Vertex AI directly. |
| Foundry direct | The add-in calls your Azure AI Foundry resource directly, authenticating with each user's Microsoft Entra ID token (keyless) or with the resource API key. |

## Requirements by connection path

All paths need:

* Claude for Excel, PowerPoint, Word, or Outlook installed from
  Microsoft AppSource or via admin deployment.
* Microsoft 365 with Entra ID for admin consent and token issuance.
* For Outlook: Microsoft Graph admin consent for `Mail.ReadWrite`,
  `Calendars.Read`, `User.Read`, and `offline_access`, granted via
  Anthropic's app or your own Entra app registration.
* For Outlook: Claude Opus 4.7 or later, or Claude Sonnet 5 or later,
  available on your connection path.

| Path | Additional requirements |
| - | - |
| LLM gateway | Gateway URL and API token from your IT team. |
| Bedrock direct | AWS account with Claude model access enabled in target region. IAM OIDC identity provider and role configured to trust Microsoft Entra ID tokens. |
| Vertex AI direct | Google Cloud project with Vertex AI API enabled and Claude model access. Google OAuth client configured with the add-in's redirect URI. |
| Foundry direct | Azure AI Foundry resource with at least one Claude model deployed. Deployment names must use default model IDs (for example, `claude-opus-4-8`), not custom names. Then one credential path: **keyless**, your own Entra app registration with the Azure Cognitive Services `user_impersonation` delegated permission (admin-consented) and users holding the Cognitive Services User role on the resource (see [Foundry direct without an API key](#foundry-direct-without-an-api-key)); or the resource API key from Azure Portal, your Foundry resource, Keys and Endpoint, KEY 1. |

Your organization's IT team manages these resources. Anthropic cannot
provide or reset credentials.

> [!NOTE]
>
> Bedrock direct does not support AWS GovCloud (US) regions. An alternative
> is an [LLM gateway](#gateway-requirements-for-it-teams) that your
> organization operates. Anthropic has not tested a gateway with Amazon
> Bedrock in GovCloud.

## Network allowlist

The add-in requires access to specific domains. The required domains
differ depending on whether your organization uses the Anthropic API
directly (1P) or a third-party platform (3P).

> [!NOTE]
>
> In all configurations, prompts and responses travel only to your chosen
> inference provider. Domains pointing to Anthropic (such as
> `pivot.claude.ai`) serve the add-in's interface, feature configuration,
> and operational telemetry, not prompt or response content.
>
> [Dictation](https://claude.com/docs/office-agents/dictation.md) is an exception. It is available
> only when users sign in with a Claude account and inference goes to
> `api.anthropic.com`. The add-in sends the user's Claude access token and
> streams the user's audio over a WebSocket connection to `pivot.claude.ai`,
> which forwards them to Anthropic's transcription service and returns the
> transcribed text.

### Anthropic API (1P)

Use this table if your organization signs in with Claude accounts and
inference goes to `api.anthropic.com`.

| Domain | Required when | Purpose |
| - | - | - |
| `pivot.claude.ai` | Always | Add-in host serving task pane UI, analytics, icon search, skill downloads, telemetry, and the WebSocket relay for dictation audio. |
| `claude.ai` | Always | Anthropic OAuth sign-in and feature-flag evaluation. |
| `hcaptcha.com`, `*.hcaptcha.com` | Always | hCaptcha browser check on the `claude.ai` sign-in and approval pages, which open in the user's web browser. If these domains are blocked, the sign-in approval can fail with a message that the browser couldn't be verified. |
| `api.anthropic.com` | Always | Claude inference API, file uploads, code-execution containers, and each user's list of MCP connectors. |
| `appsforoffice.microsoft.com` | Always | Microsoft Office.js runtime script (required by all Office add-ins). |
| `login.microsoftonline.com` | If using Outlook | Microsoft Entra ID sign-in via Nested App Auth for the Graph token. |
| `o1158394.ingest.us.sentry.io` | Optional | Crash and error reporting; blocking degrades diagnostics only. |
| `mcp-proxy.anthropic.com` | If using MCP connectors | Proxy for MCP connector tool calls. |
| `bridge.claudeusercontent.com` | If using work across apps | WebSocket bridge for the work-across-apps feature. |
| `graph.microsoft.com` | If using Outlook | Microsoft Graph mailbox and calendar API. |

If your organization has
[IP allowlisting](https://support.claude.com/en/articles/13200993-restrict-access-to-claude-with-ip-allowlisting)
enabled for Claude, route `bridge.claudeusercontent.com` through the same
proxy egress as `claude.ai` and `api.anthropic.com`, for example by
placing it in the same Zscaler app segment or Netskope steering policy. If
you cannot route it that way, add the egress address your proxy uses for
that domain to your organization's Claude IP allowlist, but only when that
address is dedicated to your organization: a shared proxy egress range also
admits the proxy vendor's other customers.

Anthropic checks connections to `bridge.claudeusercontent.com` against your
organization's Claude IP allowlist using the address they arrive from. If
your proxy sends traffic for that domain out through an address that is not
on that allowlist,
[work across apps](https://claude.com/docs/office-agents/work-across-apps.md) stops while the rest of
the add-in keeps working.

### Third-party platforms (3P)

Use this table if your organization signs in with Microsoft Entra ID
and inference goes to your LLM gateway, Bedrock, Vertex AI, or Azure
AI Foundry.

| Domain | Required when | Purpose |
| - | - | - |
| `pivot.claude.ai` | Always | Add-in host serving task pane UI, analytics, and telemetry. |
| `claude.ai/api/` | Always | Feature-flag evaluation without sign-in. |
| `appsforoffice.microsoft.com` | Always | Microsoft Office.js runtime script. |
| `login.microsoftonline.com` | Always | Microsoft Entra ID sign-in via Nested App Auth; reads admin config and issues tokens. |
| `o1158394.ingest.us.sentry.io` | Optional | Crash and error reporting; blocking degrades diagnostics only. |
| Your LLM gateway URL | If using LLM gateway | Organization's LLM gateway for inference. |
| `sts.amazonaws.com` | If using Bedrock direct | AWS STS for exchanging Entra ID token for temporary Bedrock credentials. |
| `bedrock-runtime.<region>.amazonaws.com` | If using Bedrock direct | Bedrock inference endpoint; replace `<region>` with your configured AWS region. |
| `accounts.google.com` | If using Vertex AI direct | Google OAuth consent screen. |
| `oauth2.googleapis.com` | If using Vertex AI direct | Google OAuth token exchange and refresh. |
| `aiplatform.googleapis.com` | If using Vertex AI direct | Vertex AI global inference endpoint. |
| `<region>-aiplatform.googleapis.com` | If using Vertex AI direct | Vertex AI regional inference endpoint; replace `<region>` with your GCP region. |
| `aiplatform.us.rep.googleapis.com`, `aiplatform.eu.rep.googleapis.com` | If using Vertex AI direct with region `us` or `eu` | Vertex AI multi-region inference endpoints. |
| `<resource>.services.ai.azure.com` | If using Foundry direct | Azure AI Foundry inference endpoint; replace `<resource>` with your resource name. |
| Your Vertex AI gateway URL | If using Vertex AI direct through your own gateway | The gateway or proxy set in `gcp_base_url`. Connections made while it is set do not call `aiplatform.googleapis.com` or `<region>-aiplatform.googleapis.com`. Google sign-in still uses `accounts.google.com` and `oauth2.googleapis.com`. |
| Your Foundry gateway URL | If using Foundry direct through your own gateway | The gateway or proxy set in `azure_base_url`. Connections made while it is set do not call `<resource>.services.ai.azure.com`. |
| Your MCP server URLs | If using connectors | The remote MCP servers listed in `mcp_servers`. The task pane calls them directly from the user's machine, so each must allow CORS for `https://pivot.claude.ai`. For servers that use OAuth sign-in, the same applies to their authorization server. |
| `graph.microsoft.com` | If using Outlook | Microsoft Graph mailbox and calendar API. |

## Deploy the add-in for your organization

Use the `claude-for-msft-365-install` plugin to configure and deploy the add-in
across your organization. The plugin provisions cloud resources (for
Bedrock or Vertex AI direct), generates the add-in manifest, and obtains
admin consent in a single guided flow.

### Run the setup wizard

[Install the plugin](https://github.com/anthropics/financial-services/tree/main/claude-for-msft-365-install)
from the financial services marketplace, then run the setup wizard
from inside Claude.

Add the marketplace in your shell:

```bash theme={null}
claude plugin marketplace add anthropics/financial-services
```

Install the plugin:

```bash theme={null}
claude plugin install claude-for-msft-365-install@claude-for-financial-services
```

Keep the plugin current before each deployment. List installed plugins
with `claude plugin list` and compare your version against the
[latest published version](https://github.com/anthropics/financial-services/blob/main/claude-for-msft-365-install/.claude-plugin/plugin.json).
If yours is older, update it:

```bash theme={null}
claude plugin update claude-for-msft-365-install@claude-for-financial-services
```

Then, from inside Claude, run the setup wizard:

```
/claude-for-msft-365-install:setup
```

The wizard walks you through the path you chose:

* **LLM gateway**: collects the gateway URL and token, determines the
  API format, generates the manifest, handles Azure admin consent.
* **Bedrock direct**: creates the IAM OIDC identity provider and role,
  generates the manifest, handles Azure admin consent.
* **Vertex AI direct**: walks through Google OAuth client creation,
  generates the manifest, handles Azure admin consent.
* **Foundry direct**: captures `azure_resource_name` and
  `azure_api_key`, then generates the manifest. For keyless Entra ID
  sign-in, add the parameters described in
  [Foundry direct without an API key](#foundry-direct-without-an-api-key)
  to the generated manifest.

When complete, the add-in is ready for tenant-wide deployment.

> [!NOTE]
>
> Bedrock and Vertex AI paths require Node.js for manifest generation and
> validation. The wizard checks for it and prompts installation if
> missing.

### Available commands

The plugin exposes the following slash commands once installed.

| Command | Function |
| - | - |
| `/claude-for-msft-365-install:setup` | Interactive wizard: provisions cloud resources, handles admin consent, writes manifest. |
| `/claude-for-msft-365-install:manifest` | Generates a customized add-in manifest XML. |
| `/claude-for-msft-365-install:consent` | Generates the Azure admin-consent URL for the add-in's app registration. |
| `/claude-for-msft-365-install:update-user-attrs` | Writes per-user connection values via Microsoft Graph extension attributes. |
| `/claude-for-msft-365-install:bootstrap` | Builds a bootstrap endpoint for per-user MCP servers, skills, and dynamic config. |
| `/claude-for-msft-365-install:debug` | Diagnoses deployment issues: stale config after a manifest update, connection failures, an add-in that does not appear, sign-in or admin-consent loops, and reading the add-in's error paste. |
| `/claude-for-msft-365-install:export-data` | Makes a read-only copy of a user's chat history, skills, connector registrations, and settings before a device is rebuilt. See [Data storage and retention](https://claude.com/docs/office-agents/data-storage.md). |

Run `/claude-for-msft-365-install:debug` whenever a connection or sign-in
does not behave as expected. It triages from the symptom, reads the "Copy
error details" paste from the connection-failed screen, and explains how
each connection path works, so you can resolve most third-party platform
questions without escalating.

### What the wizard provisions

The setup wizard creates resources in your cloud account based on the
connection path you choose.

| Path | Provisioned resources |
| - | - |
| LLM gateway | None. Collects your gateway URL and token, then generates the manifest. |
| Bedrock direct | IAM OIDC identity provider trusting Microsoft Entra ID tokens, role with `bedrock:InvokeModel` and `bedrock:InvokeModelWithResponseStream` permissions, trust policy scoped to the Claude add-in's application ID. |
| Vertex AI direct | Walks through creating a Google OAuth client in the GCP Console (not automatable via CLI), enables the Vertex AI API, captures client ID and secret for the manifest. |
| Foundry direct | None. Collects resource name and API key for the manifest. |

### Per-user configuration

If gateway, Bedrock, or Vertex AI connection values vary per user, such
as different gateway tokens or AWS roles for different teams, run
`/claude-for-msft-365-install:update-user-attrs` after initial setup to
write them as Microsoft Graph extension attributes. Set `entra_sso=1` in
the manifest so that the add-in reads them at sign-in, where they arrive
as claims in the user's ID token.

By default, the add-in signs in through
[Anthropic's Microsoft Entra application](#identify-anthropic%E2%80%99s-microsoft-entra-application),
which passes only these eight keys to the add-in:

* **LLM gateway**: `gateway_url` and `gateway_token`
* **Bedrock direct**: `aws_role_arn` and `aws_region`
* **Vertex AI direct**: `gcp_project_id`, `gcp_region`,
  `google_client_id`, and `google_client_secret`

Deliver every other key, such as the Foundry direct keys or
`disabled_features`, through the manifest. To vary one per user, return
it from a bootstrap endpoint instead.

If the add-in uses
[your own Entra app registration](https://claude.com/docs/office-agents/outlook.md#use-your-own-entra-app-instead)
through `graph_client_id`, you choose which keys it receives, and
`entra_sso=1` is still required. Configure each one on that application
as a directory extension attribute with an optional ID token claim, which
reaches the add-in as `extn.<key>`, such as `extn.otlp_endpoint`. An
attribute value holds at most 256 characters, so deliver a longer value,
such as most `access_policies` values, through the manifest or a
bootstrap endpoint.

With either application, neither a claim nor a bootstrap response can set
`entra_sso`, `graph_client_id`, `graph_cloud`, `entra_scope`, or
`gateway_auth_source`, so keep them in the manifest. With Anthropic's
application, `bootstrap_url` stays in the manifest too.

At load, the add-in resolves configuration from three sources in order of
precedence: a bootstrap endpoint, Microsoft Entra ID extension
attributes, then manifest parameters. Per-user values override the
manifest defaults, so one deployed manifest can serve teams with
different settings.

![The add-in resolves configuration from a bootstrap endpoint, then Entra ID extension attributes, then manifest parameters.](https://mintcdn.com/claude-ai/-4jzPa4NasvobarI/images/office-agents/architecture/config-discovery.png?fit=max\&auto=format\&n=-4jzPa4NasvobarI\&q=85\&s=b6c750272cf3ad9765ec2563af436806)

Configuration resolution at add-in load: bootstrap, Entra ID attributes, then manifest parameters. With Anthropic's Microsoft Entra application, Entra ID attributes carry only eight connection keys, not every configuration key.

### Keep credentials out of the manifest URL query string

Prefer a bootstrap endpoint (`bootstrap_url`) or Entra ID sign-in with
`gateway_auth_source=entra`, so no credential appears in the manifest or
in any URL. If you keep URL configuration, put `gateway_token`,
`azure_api_key`, `google_client_secret`, `otlp_headers`,
`inference_headers`, and `mcp_servers` after `#`, never after `?`:
the browser sends the query string to the server on every load, where
request logs record it, while the fragment stays in the browser. The
add-in warns in the console when one of these keys arrives in the query
string and ignores it there from October 19, 2026.

The following example shows the change. Apply it to both `SourceLocation`
and the `Taskpane.Url` resource, and keep `&` written as `&amp;` in the XML.

```text theme={null}
before: https://pivot.claude.ai/?gateway_url=https://ai-gateway.example.com/v1&amp;gateway_token=sk-gw-xxxxx&amp;m=excel3p-1.0.0.1
after:  https://pivot.claude.ai/?gateway_url=https://ai-gateway.example.com/v1&amp;m=excel3p-1.0.0.1#gateway_token=sk-gw-xxxxx
```

Before you redeploy the manifest from the Microsoft 365 admin center, raise
the number in its `<Version>` element, for example from `1.0.0.1` to
`1.0.0.2`. Microsoft requires a
[higher version number for every manifest change](https://learn.microsoft.com/en-us/office/dev/add-ins/publish/maintain-breaking-changes),
and without one, Office can keep using the old manifest.

### Admin feature controls

The `disabled_features` configuration key turns off individual add-in
features for your users. Set it as a comma-separated manifest parameter to
apply one list org-wide, or return it from a bootstrap endpoint as a JSON
array to vary it per user.

| Slug | Effect |
| - | - |
| `skills.authoring` | Blocks creating, editing, and uploading skills. Running admin-provisioned skills is unaffected. |
| `thumbs` | Blocks response feedback (thumbs up / down and the follow-up prompt). |
| `addin.access` | Kill switch: the add-in refuses to run. |
| `file.upload` | Blocks attaching files to the conversation. |
| `web_search` | Removes the built-in web search and web fetch tools, whose queries are served by Anthropic's search provider, along with the user-facing web search toggle. Code execution is unaffected. |
| `code_execution` | Removes server-side code execution, where Claude runs Python in a sandbox outside the user's device. Attached files stay in the add-in, which reads them there. Web search, and the code Claude runs in the add-in to read and edit the open document, are unaffected. |
| `permission_mode.accept_all_edits` | Keeps users in "Ask before edits": "Accept all edits" and "Skip all permissions" can't be turned on, and users already in either mode go back to "Ask before edits". Connector "Always allow" choices and Outlook's "Always allow mailbox search" are unaffected. |
| `permission_mode.dangerously_always_allow` | Removes the "Dangerously always allow" button from approval cards. It switches users to the mode shown as "Skip all permissions"; users already in that mode are moved to "Accept all edits". |

Unknown slugs are ignored, so setting a slug from a newer add-in version
on an older deployment is safe.

Disabling `web_search` pairs with the `mcp_servers` key: attach your own
search tool from a server inside your network, and with the built-in
search disabled the model uses the tool you provide. This keeps search
queries on infrastructure you control.

For document-scoped control, such as disabling a feature only on files
carrying certain sensitivity labels, use the `access_policies` key
instead; a statement without a resource behaves exactly like
`disabled_features`. The setup wizard's
`/claude-for-msft-365-install:manifest` and
`/claude-for-msft-365-install:access-policies` commands document both
keys in full.

### Skill limits for a bootstrap endpoint

A bootstrap endpoint can return a `skills` array of admin-provisioned
skills. The add-in applies these limits to each response.

| Limit | Value |
| - | - |
| Skills kept | The first 200 skill names, in array order. No setting changes this number. Uploaded and built-in skills don't count toward it. |
| Repeated names | One skill for each name: the last entry with that name, in the position of the first. |
| Skill `url` | HTTPS, no redirects, CORS for `https://pivot.claude.ai`, and 15 seconds for each download, including the time that it waits for a connection. The add-in downloads up to 20 files at a time. |
| Bootstrap call | 10 seconds in total to get the user's Microsoft Entra token, when the add-in uses one, and to receive the response. This limit applies to each bootstrap call, except the call made when the add-in sets up a new connection, for example at first use or after a sign-out. |

If a skill fails to load, the add-in doesn't replace it with a later
skill. To see which skills failed to load, select the + button at the
bottom of the chat pane, and then select Skills. A note at the top of the
list names up to three of those skills and gives the number of any others.
The note leaves out a skill that still has a copy from an earlier load.

If a response holds more than 200 different skill names, a note at the top
of the same list tells the user how many skills the organization has and
that Claude can use only 200 of them.

If a bootstrap call takes more than 10 seconds when the add-in
loads with an existing connection, the add-in has no admin-provisioned
skills until a later bootstrap call succeeds.

To stay within these limits:

* Put the most important skills first.
* Keep each `description` short. The add-in sends the name and description
  of every skill that it keeps to the model with each request, so long
  descriptions add to its size and cost.
* Give each `url` entry a `sha256`. Without one, the add-in downloads
  every file again each time a user opens a list of skills. See
  [Publish a new or changed skill](#publish-a-new-or-changed-skill).
* Keep skill files small. The add-in holds every skill that it loads in
  memory.
* Serve a long list of skill files over HTTP/2. Over HTTP/1.1, a browser
  opens about six connections to a host, and the other downloads wait for
  one. That wait counts toward the 15 seconds.
* Return a different list for each app. The `X-Claude-User-Agent` header
  on each bootstrap call starts with `claude-word`, `claude-excel`,
  `claude-powerpoint`, or `claude-outlook`.
* Use `url` instead of inline `content` for large skills. Inline content
  is part of the bootstrap response, so it counts toward the 10 seconds.
  The add-in downloads skill URLs after the bootstrap call, and only for
  the skills that it keeps.

If a response holds more than 200 different skill names, the add-in sends
the warning log record `Bootstrap skill count exceeds cap — truncating`
to your [OpenTelemetry collector](https://claude.com/docs/office-agents/opentelemetry.md) at
`{your_url}/v1/logs`. Your collector might not receive this record for
the bootstrap call made when the add-in sets up a new connection. On that
record, `count` is the number of different skill names in the response,
and `cap` is the limit, 200.

### Publish a new or changed skill

The add-in loads the `skills` array when the pane loads and at each
scheduled bootstrap call before the response expires. It also calls the
bootstrap endpoint when a user does one of these:

* Selects New chat.
* Starts the first message of a chat, by typing it or by selecting a
  suggested prompt.
* Opens a list of skills in any chat: types `/` at the start of a word in the
  chat input, or selects the + button at the bottom of the chat pane and then
  selects Skills.

At New chat and at a first message, that extra call happens at most once every
30 seconds in each open pane, counted from the last time the pane read the
skills. When a user opens a list of skills, the add-in always calls, unless an
earlier call still waits for its answer or the skills are still loading. So a
pane has one of these calls open at a time, and it ends a call that has no
answer after 10 seconds. Nothing else limits how many of these calls a pane
makes in a minute. A `/` typed while Claude is replying calls when the reply
ends.

The add-in retries a call up to three times if the endpoint can't be reached
or answers with a 5xx, 408, 425, or 429 status. Skill file downloads aren't
retried. From the response, the add-in uses only the `skills` array. It
doesn't apply a token or any other setting, so keep tokens from earlier calls
valid until they expire.

After that call, the add-in loads the array again if an entry might have
changed.

| Skill entry | Counts as changed when |
| - | - |
| With `sha256` | The `sha256`, `name`, or `description` differs. A different `url` alone doesn't count. |
| Inline `content`, no `sha256` | The `content`, `name`, or `description` differs. |
| `url`, no `sha256` | Always. The add-in can't tell whether the file changed. |

An added, removed, or reordered entry also counts as a change, and so does
an entry that failed to load the last time. For entries past the limit of
200, only a change in their number counts. When the add-in loads the array
again, it downloads the `url` of each skill within the limit of 200, unless
the entry has inline `content`. It does the same when the pane loads and at
each scheduled bootstrap call.

To avoid downloads on that extra call when nothing changed, give each `url`
entry a `sha256`: the SHA-256 of the file, as 64 hexadecimal characters.
Update the `sha256` whenever the file changes: the add-in refuses a file that
doesn't match it.

The load runs in the background and a chat never waits for it:

* A message sent before the load ends goes without the new skill. A message
  sent after the load ends has it.
* The skills of a load become available together, when its last download
  ends.
* If the call fails or takes more than 10 seconds, the add-in keeps the
  skills that it has.
* A skill that fails to load keeps the copy the pane already had, until a later
  load of that skill succeeds. The copy is held only in memory: if the pane
  reloads while the file still fails, the skill is missing until it loads. The
  add-in sends the warning log record `Bootstrap skill failed to load`
  to your [OpenTelemetry collector](https://claude.com/docs/office-agents/opentelemetry.md).
* A list of skills that is open when the load ends shows the new skill.

To remove every skill, return an empty `skills` array. If a response has
no `skills` key, the add-in keeps the skills that it has.

Serve the bootstrap response with `Cache-Control: no-store`, so that no
cache between the add-in and the endpoint answers with an older copy. A
response with `Last-Modified` and no `Cache-Control` can be stored too.

### Deploy to Outlook

Outlook requires a separate manifest file from Excel, PowerPoint, and
Word. Microsoft uses a different add-in schema for mail applications, so
the two cannot be combined into one file. When you tell the setup wizard
you are deploying to Outlook, it generates a second file named
`manifest-outlook.xml` alongside `manifest.xml`. Upload each file as its
own custom app in the steps below.

Claude for Outlook reads mail and calendar data through Microsoft Graph,
which requires a one-time tenant-wide grant from a Global Administrator or a
Cloud Application Administrator, regardless of which platform serves the model. Complete the
[Microsoft Graph admin consent](https://claude.com/docs/office-agents/outlook.md#grant-microsoft-graph-consent)
step before deployment so users are not prompted individually. The Graph
token stays in the user's Outlook client and is never sent to your
gateway or to Anthropic.

If your organization's policy does not permit consenting to a third-party
multi-tenant application, register your own single-tenant Entra
application with the same delegated Graph permissions and provide its
client ID to the setup wizard as `graph_client_id`. See
[Use your own Entra app instead](https://claude.com/docs/office-agents/outlook.md#use-your-own-entra-app-instead).

> [!NOTE]
>
> Claude for Outlook on third-party platforms supports Claude Opus 4.7 and
> later and Claude Sonnet 5 and later. Earlier model generations are not
> available on the Outlook surface. If your connection doesn't offer one of
> these models under an ID that Outlook accepts, messages in Outlook can fail.
> See
> [Outlook messages fail or the model menu is missing](#outlook-messages-fail-or-the-model-menu-is-missing).

### Deploy to Microsoft 365

After the wizard generates your manifest files:

**1. Upload the manifest**

Open the Microsoft 365 Admin Center and go to Settings, Integrated
apps, Upload custom apps. Select "Office Add-in" as the app type,
then upload the `manifest.xml` file. If you are deploying Outlook,
repeat this step with `manifest-outlook.xml` as a second custom app.

**2. Choose who gets the add-in**

If all users share the same configuration, select "Entire
organization". If you wrote per-user attributes, assign to "Specific
users/groups" matching exactly who was configured. Others would open
the add-in with no configuration.

**3. Finish deployment**

Accept permissions and finish deployment.

Propagation to users takes up to 24 hours, usually faster. The add-in
appears under Tools, Add-ins on Mac or Home, Add-ins on Windows in
Excel, PowerPoint, and Word once deployed. In Outlook it appears in the
message ribbon when an email is open.

Custom manifest deployment is where most issues surface: the add-in does
not appear, users see old configuration after an update, or sign-in
fails. Run `/claude-for-msft-365-install:debug` to diagnose these, or to
sideload and validate a manifest locally before a tenant-wide upload.

> [!NOTE]
>
> Start with a pilot group to confirm functionality, then widen
> assignment. You can change assignment later without redeploying.

## Manage the add-in from the Enterprise Admin Console

If you manage Claude Desktop from the
[Enterprise Admin Console](https://claude.com/docs/third-party/claude-desktop/admin-console.md), you
can manage Claude for Microsoft 365 there too. For the requirements and the
steps for admins and members, see
[Manage Claude for Microsoft 365 from the Enterprise Admin Console](https://claude.com/docs/office-agents/admin-console.md).

## Connection instructions for end users

### LLM gateway

**1. Open the add-in**

Open Excel, PowerPoint, Word, or Outlook and launch the Claude add-in.

**2. Select your connection mode**

On the sign-in screen, select "Cloud provider or gateway". Then
choose your connection: Gateway, Vertex, Bedrock, or Azure. Contact
your IT team for connection details if you're unsure which one to
select.

**3. Enter your credentials**

For Gateway, enter the gateway URL (HTTPS base URL of your LLM
proxy, for example
`https://llm-gateway.example.com`) and the API token your IT team
provided. By default the add-in sends the token in the `x-api-key`
header with every request. If your admin set
`gateway_auth_header: authorization` in the manifest, the add-in
sends `Authorization: Bearer <token>` instead.

**4. Connect**

The add-in checks the connection by sending a test request to the
gateway. On success, you see the main add-in experience.

Your credentials are stored locally in your browser's localStorage
within the add-in's sandboxed iframe and are not synced to Anthropic's
servers. Because the Office add-in runs in a sandboxed iframe within
Microsoft applications, it cannot use your OS keychain the way Claude
Code does. Only enter gateway-issued tokens, not raw cloud-provider
credentials.

In this path, every request travels from the add-in to your gateway,
which forwards it to the provider you configured.

![Requests flow from the add-in to your LLM gateway, which forwards them to the configured model provider.](https://mintcdn.com/claude-ai/-4jzPa4NasvobarI/images/office-agents/architecture/gateway.png?fit=max\&auto=format\&n=-4jzPa4NasvobarI\&q=85\&s=287ef25266391992109b8673f97e3f93)

LLM gateway request flow: the add-in calls your gateway, which routes to your chosen provider.

### Bedrock, Vertex AI, or Foundry direct

**1. Open the add-in**

Open Excel, PowerPoint, Word, or Outlook and launch the Claude add-in.

**2. Authenticate**

For Bedrock, sign in with your
Microsoft work account. The add-in uses your Entra ID token to
assume the AWS role your admin
configured, so no separate AWS credentials are needed.
For Vertex AI, sign in with the Google account your admin authorized
via the Google OAuth client created during setup.
For Foundry, the add-in connects automatically if your admin
pre-filled the Azure resource name and API key. If your admin enabled
keyless sign-in, the add-in uses your Microsoft work account and no
key is involved. Otherwise, enter the values your IT team provided
and select Connect.

**3. Start working**

The add-in reads the configuration your admin provisioned and
connects to Bedrock, Vertex AI, or Foundry directly.

If you see an error at sign-in, confirm with your IT team that your
account is in the group assigned to the add-in.

In a direct connection, the add-in authenticates with your identity
provider and calls the model provider without an intermediary gateway.
The flow differs by provider.

Bedrock direct uses your Microsoft Entra ID token to assume an AWS role,
then calls Amazon Bedrock.

![The add-in uses a Microsoft Entra ID token to assume an AWS role and call Amazon Bedrock directly.](https://mintcdn.com/claude-ai/-4jzPa4NasvobarI/images/office-agents/architecture/bedrock-direct.png?fit=max\&auto=format\&n=-4jzPa4NasvobarI\&q=85\&s=51c8233f704717f0ff1c3897356621cd)

Bedrock direct flow: the add-in exchanges an Entra ID token for an AWS role, then calls Bedrock.

Vertex AI direct authenticates through Google OAuth, then calls Vertex
AI.

![The add-in authenticates through Google OAuth and calls Google Cloud Vertex AI directly.](https://mintcdn.com/claude-ai/-4jzPa4NasvobarI/images/office-agents/architecture/vertex-direct.png?fit=max\&auto=format\&n=-4jzPa4NasvobarI\&q=85\&s=a33063abcecbfc36e346621f735453ef)

Vertex AI direct flow: the add-in authenticates with Google OAuth, then calls Vertex AI.

### Foundry direct without an API key

Instead of a shared resource key, each user can authenticate to your
Foundry resource with their own Microsoft Entra ID token. The add-in
acquires the token through Nested App Authentication inside Office,
sends it to `<resource>.services.ai.azure.com` as `Authorization: Bearer`,
renews it silently before it expires, and re-authenticates once if Azure
rejects a token early. No key is stored on the device and no key is
embedded in the manifest.

This uses the same Entra app registration that Claude Desktop's
in-app Foundry sign-in uses (`inferenceFoundryClientId`), with the add-in's
redirect URI added. Set up:

1. In your Entra app registration, add the **Azure Cognitive Services**
   delegated permission `user_impersonation` and grant admin consent.
   Register the add-in's redirect URI as described in
   [Use your own Entra app instead](https://claude.com/docs/office-agents/outlook.md#use-your-own-entra-app-instead).
2. Grant the users or groups who will sign in the **Cognitive Services
   User** role on the Foundry resource.
3. Put these parameters in the manifest URL (no `azure_api_key`):

| Parameter | Value |
| - | - |
| `azure_resource_name` | Your Foundry resource name. |
| `entra_sso` | `1` |
| `graph_client_id` | The application (client) ID of your Entra app registration. |
| `entra_scope` | `https://cognitiveservices.azure.com/.default` |
| `gateway_auth_source` | `entra` |

When `gateway_auth_source=entra` is set, the add-in ignores any
`azure_api_key` it receives: the administrator chose keyless sign-in.
Each user sees a one-time Microsoft sign-in prompt if silent sign-in is
not available; afterwards the add-in connects automatically.

### Route Foundry direct through your own gateway

If your organization reaches Azure AI Foundry through a gateway or proxy
it operates, such as Azure API Management, set `azure_base_url` to that
gateway's base URL, path included. The add-in then sends every Foundry
request to `<azure_base_url>/v1/messages` instead of
`https://<resource>.services.ai.azure.com/anthropic/v1/messages`, with
the same credential and headers it would send to the resource: the API
key as `x-api-key`, or each user's Microsoft Entra ID token as
`Authorization: Bearer` with keyless sign-in. `azure_resource_name` is
still required and names the resource behind the gateway.

Use the same value you would set as Claude Code's
`ANTHROPIC_FOUNDRY_BASE_URL`. The URL must use HTTPS. Because the add-in
calls the gateway from the browser, the gateway must meet the
[CORS requirements](#cors-requirements), and your network must allow its
domain as listed in the [network allowlist](#network-allowlist). On this
path the add-in also sends the `anthropic-beta` header, and with keyless
sign-in the `authorization` header, so the gateway's CORS preflight must
allow both and the gateway must forward `anthropic-beta` to Foundry.

Users who connected before you set `azure_base_url` keep their direct
connection until they log out and sign in again, as described in
[Change or update your gateway connection](#change-or-update-your-gateway-connection).
Until the setup wizard accepts this key, add `azure_base_url` to the
generated manifest URL by hand, or deliver it per user through a bootstrap
endpoint.

The following manifest parameters configure this path.

| Parameter | Value |
| - | - |
| `azure_resource_name` | Your Foundry resource name. |
| `azure_base_url` | The gateway base URL, for example `https://ai-gateway.example.com/foundry/anthropic`. |
| `azure_api_key` | The key the gateway expects as `x-api-key`. Omit it with keyless sign-in. |

### Route Vertex AI direct through your own gateway

If your organization reaches Vertex AI through a gateway or proxy it
operates, set `gcp_base_url` to that gateway's base URL, API version
included. Each user still signs in with Google, and the add-in keeps the
Vertex AI request format, but it sends every request to
`<gcp_base_url>/projects/<project>/locations/<region>/publishers/anthropic/models/<model>:rawPredict`,
or `:streamRawPredict` for streaming responses, instead of
`https://<region>-aiplatform.googleapis.com/v1/...`, with the user's
Google access token as `Authorization: Bearer`. Google sign-in and token
refresh still go to `accounts.google.com` and `oauth2.googleapis.com`.
`gcp_project_id`, `google_client_id`, and `google_client_secret` are
still required, and `gcp_region` still names the region in the request
path.

Use the same value you would set as Claude Code's
`ANTHROPIC_VERTEX_BASE_URL`. The URL must use HTTPS. Because the add-in
calls the gateway from the browser, the gateway must meet the
[CORS requirements](#cors-requirements), and your network must allow its
domain as listed in the [network allowlist](#network-allowlist). On this
path the add-in sends the same headers it sends to Vertex AI:
`authorization`, `content-type`, `accept`, and `user-agent`. The token
the gateway receives is the user's Google OAuth token with the
`cloud-platform` scope, so the gateway should forward it to Vertex AI
and not store it.

Users who connected before you set `gcp_base_url` keep their direct
connection until they log out and sign in again, as described in
[Change or update your gateway connection](#change-or-update-your-gateway-connection).
Until the setup wizard accepts this key, add `gcp_base_url` to the
generated manifest URL by hand, or deliver it per user through a bootstrap
endpoint.

| Parameter | Value |
| - | - |
| `gcp_project_id` | Your Google Cloud project ID. |
| `gcp_region` | The Vertex AI region, or `global`. |
| `gcp_base_url` | The gateway base URL, for example `https://ai-gateway.example.com/vertex/v1`. |

### Change or update your gateway connection

If your gateway API token expires or your IT team provides a new URL, log
out and sign in again with your new credentials. This applies to LLM
gateway, Bedrock, Vertex AI, and Foundry direct connections alike. A bootstrap
endpoint can change some details with no log-out: the token or URL of an LLM
gateway connection, and the API key of a Foundry connection to the same
resource.

Logging out deletes saved Claude for Outlook conversations, your writing
style, and what Claude has learned about your writing, for every account
that has used Claude on the device. It does this whether you log out in
Outlook or in another Office app that shares its storage. The add-in asks
you to confirm first, and deleted data can't be recovered. See
[Outlook data deleted when a sign-in ends](https://claude.com/docs/office-agents/data-storage.md#outlook-data-deleted-when-a-sign-in-ends).

Conversations in Excel, PowerPoint, and Word aren't deleted. If you sign in
with a different gateway URL, Foundry resource, Google Cloud project, or AWS
account, they stop appearing in chat history until you sign in with the
earlier details again. The same happens when your IT team adds or removes a
gateway in front of Foundry or Vertex AI.

When a bootstrap endpoint delivers a new LLM gateway URL, the change deletes
nothing, but conversations in every app, including Outlook, stop appearing in
chat history until the URL changes back.

In each of these cases, the conversations that stop appearing still count
toward the 50 that each app keeps, so the oldest are deleted as new ones are
saved. See [Data retention](https://claude.com/docs/office-agents/data-storage.md#data-retention).

Logging out also removes the stored token or key and connector sign-ins, and
it can sign out other Claude panes on the same device. See
[Sign-in and credentials](https://claude.com/docs/office-agents/data-storage.md#sign-in-and-credentials).

To log out, select More options, then Logout.

## Gateway requirements for IT teams

The Office add-ins support the same three API formats as Claude Code.
Set `gateway_api_format` in your add-in manifest to specify which format
your gateway uses.

### CORS requirements

The add-in's taskpane loads from `https://pivot.claude.ai`. Every
request to your gateway is cross-origin, and the browser silently
discards responses lacking CORS headers.

Your gateway must return `Access-Control-Allow-Origin: https://pivot.claude.ai`
(or `*`) on every response: GET, POST, OPTIONS, and all error responses.
Setting it only on the OPTIONS preflight is insufficient. For the
preflight, return `Access-Control-Allow-Headers` listing the request
headers the add-in sends, such as
`x-api-key, authorization, content-type, anthropic-version`. The `*`
wildcard does not cover the `Authorization` header per the Fetch
specification, so list it explicitly if you set
`gateway_auth_header: authorization`.

### Required endpoints

The endpoints your gateway must expose depend on which API format it
speaks.

**`gateway_api_format: anthropic` (default):**

| Endpoint | Description |
| - | - |
| `POST /v1/messages` | Send messages to Claude; supports both streaming and non-streaming responses. |
| `GET /v1/models` | List available models. |

**`gateway_api_format: bedrock`:**

| Endpoint | Description |
| - | - |
| `POST /model/{model-id}/invoke` | Send message and receive complete response. |
| `POST /model/{model-id}/invoke-with-response-stream` | Send message and receive streaming response. |

Native Bedrock `InvokeModel` pass-through. `gateway_url` must point at
the pass-through prefix, for example `https://litellm.example.com/bedrock`.

**`gateway_api_format: vertex`:**

| Endpoint | Description |
| - | - |
| `POST /projects/{project}/locations/{region}/publishers/anthropic/models/{model-id}:rawPredict` | Send message and receive complete response. |
| `POST /projects/{project}/locations/{region}/publishers/anthropic/models/{model-id}:streamRawPredict` | Send message and receive streaming response. |

Native Vertex pass-through. `gateway_url` must include the API-version
segment, for example `https://litellm.example.com/vertex_ai/v1`. Also
requires `gcp_project_id` and `gcp_region` so the add-in can build the
path.

### Required header

For `anthropic` format, the gateway must forward the `anthropic-version`
request header to the upstream provider.

For `bedrock` and `vertex` formats, the SDK places `anthropic_version`
in the request body instead. The gateway must preserve it there.

Failure to forward the header or preserve the body field may result in
reduced functionality or prevent the add-in from working.

### Authorization header

The add-in can send your gateway's authorization token in either the
`x-api-key` header or the `Authorization` header. The default is
`x-api-key`. To switch to `Authorization: Bearer`, set
`gateway_auth_header: authorization` in the manifest.

### Model discovery

For gateways using `gateway_api_format: anthropic`, the add-in discovers
available Claude models via `GET /v1/models` at sign-in and each time the
pane loads. Outlook offers only the listed models that it supports. See
[Outlook messages fail or the model menu is missing](#outlook-messages-fail-or-the-model-menu-is-missing)
for the model IDs that Outlook accepts.

If the response lists no Claude models, or the gateway refuses or doesn't
answer test requests to the listed models, the add-in usually prompts the
user for a model ID at sign-in. If a test request fails for a reason that
applies to the whole account, such as a 401 status, a budget limit, or a
server error, and no listed model works, sign-in stops with an error. If
`GET /v1/models` itself fails, sign-in stops with an error and the user
can't enter a model ID.

For `gateway_api_format: bedrock` and `gateway_api_format: vertex`, the
add-in uses a built-in model list and sends test requests until one model
responds, rather than calling `GET /v1/models`.

### Differences from Claude Code gateway setup

If your team already runs Claude Code through a gateway, the table
below summarizes how the Office add-in setup differs.

| Aspect | Claude Code | Office add-ins |
| - | - | - |
| Credential storage | OS keychain or environment variables | Browser localStorage (sandboxed iframe) |
| Auth configuration | Environment variables, settings file, helper scripts | Manual entry in add-in UI (gateway), Entra ID (Bedrock, keyless Foundry), Google OAuth (Vertex AI), or Azure API key (Foundry) |
| Token refresh | Supports helper scripts for rotation | Automatic via a bootstrap endpoint (gateway), Entra ID (Bedrock, keyless Foundry), or Google OAuth (Vertex AI); gateway tokens entered manually in the add-in UI require signing out and back in when they rotate |
| Custom model names | Configurable via environment variables | With `gateway_api_format: anthropic`, taken from your gateway's model list |

When gateway configuration comes from a bootstrap endpoint, the add-in
keeps the token current without user action. It calls the bootstrap
endpoint again about five minutes before the expiry declared in the
bootstrap response and applies the returned token to the running session.
If that call fails, the add-in tries again after about a minute, then at
growing intervals of up to 90 minutes, until a call succeeds.
Meanwhile, it also calls the endpoint before each message that a user
sends, at most once every 30 seconds.
If the gateway rejects a request as unauthorized before that expiry, the
add-in calls the bootstrap endpoint once and retries the request if the
token changed.

Gateway tokens entered manually in the add-in UI do not refresh
automatically. When one rotates, sign out and sign in again with the new
token, as described in
[Change or update your gateway connection](#change-or-update-your-gateway-connection).
Signing out deletes saved Claude for Outlook conversations. A bootstrap
endpoint keeps the token current, so users don't have to sign out.

## Example gateway configuration with LiteLLM

> [!WARNING]
>
> LiteLLM PyPI versions 1.82.7 and 1.82.8 contained credential-stealing
> malware. Do not install those versions. If already installed, remove the
> package, rotate all credentials on affected systems, and follow
> remediation steps in [BerriAI/litellm#24518](https://github.com/BerriAI/litellm/issues/24518).

LiteLLM is a third-party proxy service. Anthropic does not endorse,
maintain, or audit LiteLLM's security or functionality. This section is
informational and may become outdated. Use at your own discretion.

The example configurations below route Office add-in requests through
LiteLLM to Anthropic, Bedrock, Vertex AI, or Azure.

### Route to Anthropic directly

Use this `config.yaml` to point the gateway at the Anthropic API.

```yaml theme={null}
model_list:
  - model_name: claude-opus-4-7
    litellm_params:
      model: claude-opus-4-7
      api_key: os.environ/ANTHROPIC_API_KEY

litellm_settings:
  drop_params: true
```

### Route to Amazon Bedrock

Use this `config.yaml` to route requests through Amazon Bedrock.

```yaml theme={null}
model_list:
  - model_name: claude-opus-4-7
    litellm_params:
      model: bedrock/us.anthropic.claude-opus-4-7
      aws_region_name: us-east-1

litellm_settings:
  drop_params: true
```

### Route to Google Cloud Vertex AI

Use this `config.yaml` to route requests through Vertex AI.

```yaml theme={null}
model_list:
  - model_name: claude-opus-4-7
    litellm_params:
      model: vertex_ai/claude-opus-4-7
      vertex_project: your-gcp-project-id
      vertex_location: us-east5

litellm_settings:
  drop_params: true
```

### Route to Azure

Use this `config.yaml` to route requests through Azure AI Foundry.

```yaml theme={null}
model_list:
  - model_name: claude-opus-4-7
    litellm_params:
      model: azure_ai/claude-opus-4-7
      api_base: https://your-resource.services.ai.azure.com/anthropic
      api_key: os.environ/AZURE_API_KEY
      extra_headers:
        x-api-key: os.environ/AZURE_API_KEY

litellm_settings:
  drop_params: true
```

For detailed setup instructions, see
[LiteLLM's Anthropic format documentation](https://docs.litellm.ai/).

## What Anthropic collects

Even when inference goes through your own infrastructure, the add-in
communicates with `pivot.claude.ai` to load its interface and with
`claude.ai/api/` to evaluate feature flags. These connections transmit
operational telemetry such as which features are used, performance
timings, and error rates, so Anthropic can maintain and improve the
add-in experience. They do not transmit your prompts or Claude's
responses. For members of an organization that manages the add-in from
the Enterprise Admin Console, they also carry account details, as
[What leaves the device](https://claude.com/docs/office-agents/data-storage.md#what-leaves-the-device)
describes.

When the add-in uses Amazon Bedrock or Google Cloud Vertex AI, directly
or through a gateway, Anthropic collects information in accordance with
that platform's terms, consistent with Anthropic's arrangements with
customers. Anthropic does not have access to a customer's AWS or Google
instance, including prompts or outputs it contains. Anthropic does not
train generative models with such content or use it for other purposes.
Anthropic can access metadata such as tool use and token counts, and
uses such metadata for analytic and product-improvement purposes.

When the add-in uses Azure AI Foundry, directly or through a gateway,
Anthropic operates the Claude models as an independent processor for
Microsoft, and Anthropic's data use terms apply. For deployments hosted
on Azure, Anthropic processes prompts and completions on Azure
infrastructure and stores retained content there. Retained content
includes content flagged by Anthropic's safety systems for Anthropic to
review. Operational data that contains no prompts or completions is
stored on Anthropic's systems outside Azure. Examples include safety
classifier scores, identifiers, and usage and billing data. For
deployments hosted on Anthropic, prompts and responses are
processed on Anthropic's infrastructure. See
[Claude in Microsoft Foundry](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry)
for details.

For details on what your organization's gateway or cloud provider logs,
contact your IT team.

To route a full audit trail, including prompts, tool inputs, tool
outputs, and document references, to your own infrastructure, see
[Configure a custom OpenTelemetry collector](https://claude.com/docs/office-agents/opentelemetry.md).
That page covers the `otlp_endpoint`, `otlp_headers`, and
`otlp_attr_max_chars` configuration keys, the CORS requirements for the
collector endpoint, and the full span reference.

## Why sign-in redirects through pivot.claude.ai

During Google sign-in for Vertex AI, MCP connector authorization, or
Microsoft admin consent, your identity provider redirects the browser to a
page on `pivot.claude.ai`. Security reviewers sometimes ask whether this
means access tokens for your cloud provider, connector, or mailbox pass
through Anthropic's servers. They do not. This section explains what the
redirect carries in each flow and why the page cannot obtain a token.
[Claude account sign-in](#claude-account-sign-in-uses-no-redirect) involves
no redirect.

### OAuth authorization-code redirects

Google sign-in for Vertex AI uses the OAuth 2.0 authorization-code grant
and redirects to `pivot.claude.ai/auth/callback`. MCP connector
authorization uses the same grant with a dedicated
`pivot.claude.ai/auth/gateway-callback` redirect. In each case the URL
contains two query parameters:

* `code`: a one-time authorization code, not an access token
* `state`: a random value the add-in generated before sign-in started

The callback page is a static page served from `pivot.claude.ai`. It reads
those two parameters from the URL, shows a Copy button, and instructs you
to paste the value back into the add-in inside Office. The page has no
server-side logic that stores, forwards, or exchanges the code.

An authorization code on its own cannot be redeemed for an access token.
The token endpoint requires an additional secret that only the add-in
running on your machine holds:

* **MCP connector authorization**: a Proof Key for Code Exchange (PKCE)
  verifier. The add-in generates a random verifier locally, sends only its
  SHA-256 hash to the identity provider when sign-in starts, and keeps the
  verifier in browser session storage. The token endpoint rejects any
  exchange that does not present the original verifier.
* **Google sign-in for Vertex AI**: the `client_secret` belonging to the
  Google OAuth client your organization created during setup. This value
  is provisioned into the add-in's configuration on each user's machine
  and is sent only to `oauth2.googleapis.com` during token exchange.
  Anthropic does not have this value.

The add-in also verifies that the `state` value pasted back matches the
one it generated and stored locally before sign-in. A mismatch is
rejected. This prevents an attacker from tricking a user into completing
a sign-in the attacker initiated.

After the add-in exchanges the code, the resulting access and refresh
tokens are held in browser storage inside the Office add-in sandbox. The
add-in presents the access token only to the inference endpoint or MCP
server it was issued for, and presents the refresh token only to the OAuth
token endpoint. Each of these endpoints appears in the
[Network allowlist](#network-allowlist). These tokens never reach
`pivot.claude.ai`.

### Why the redirect cannot target localhost

Office add-ins run inside a sandboxed browser frame hosted by Microsoft
365\. There is no local web server to receive a loopback redirect, and the
browser tab that handles sign-in is isolated from the add-in frame's
storage. The redirect must therefore target a registered HTTPS URL, and
the callback page at `pivot.claude.ai` bridges the two contexts by
displaying the code for you to paste back into the add-in.

### Claude account sign-in uses no redirect

Signing in with a Claude account uses the OAuth 2.0 device authorization
grant, RFC 8628, instead of a redirect. The add-in requests a one-time
sign-in code from `claude.ai`, shows it in the task pane, and sends you to
`claude.ai` in your browser. It waits while you approve the sign-in there,
then obtains the access and refresh tokens directly from the `claude.ai`
token endpoint. During sign-in, no authorization code or token passes
through `pivot.claude.ai`, and there is nothing to paste back into the
add-in.

### Microsoft admin-consent redirects

The Microsoft Graph consent link in
[Grant Microsoft Graph consent](https://claude.com/docs/office-agents/outlook.md#grant-microsoft-graph-consent)
uses Microsoft's
[admin-consent endpoint](https://learn.microsoft.com/en-us/entra/identity-platform/v2-admin-consent).
By Microsoft's specification, the redirect back to
`pivot.claude.ai/auth/callback` carries only the consent outcome: an
`admin_consent` boolean and the `tenant` ID. It never carries an access
token or an authorization code. The callback page displays a confirmation
message and nothing else.

The Microsoft Graph access token itself is obtained separately through
[Nested App Authentication](https://learn.microsoft.com/en-us/office/dev/add-ins/develop/enable-nested-app-authentication-in-your-add-in),
where the Office host brokers the token directly into the add-in on the
user's machine. The Microsoft Authentication Library (MSAL) caches it in
the browser's local storage, and the add-in calls `graph.microsoft.com`
directly. The Graph token never reaches `pivot.claude.ai` or any other
Anthropic endpoint.

### Identify Anthropic's Microsoft Entra application

The admin consent link and Nested App Authentication both use a single
multi-tenant application that Anthropic publishes in Microsoft Entra ID.
When you review the consent prompt or the resulting enterprise
application in your tenant, confirm it matches these values.

| Field | Value |
| - | - |
| Display name | Claude for Office |
| Application (client) ID | `c2995f31-11e7-4882-b7a7-ef9def0a0266` |
| Publisher | Anthropic, PBC (verified publisher) |
| Supported account types | Accounts in any organizational directory |

The add-in uses the following redirect URIs with this application. Each
one exists for a specific Microsoft sign-in path, and none of them
receives a Microsoft access token in the URL.

| Redirect URI | Platform | Purpose |
| - | - | - |
| `https://pivot.claude.ai/auth/callback` | Web | admin consent confirmation page, receives only `admin_consent` and `tenant` from Microsoft. Google sign-in for Vertex AI reuses this URI for its [OAuth authorization-code redirect](#oauth-authorization-code-redirects) |
| `https://pivot.claude.ai/msal-redirect.html` | Single-page application | MSAL response bridge for Office on the web, where the host cannot broker tokens natively |
| `brk-multihub://pivot.claude.ai` | Single-page application | Nested App Authentication broker on Office desktop and Mac |

### Verify this in your own environment

You can confirm every claim above with a network capture on a test
machine:

* The redirect to `pivot.claude.ai/auth/callback` carries `code` and
  `state`, or `admin_consent` and `tenant`, in the query string. For an
  MCP connector the redirect to `pivot.claude.ai/auth/gateway-callback`
  carries `code` and `state`. No `access_token` parameter appears.
* The `POST` that exchanges the code goes to `oauth2.googleapis.com` for
  Vertex AI or to the connector's authorization server for an MCP
  connector, originates from the add-in frame, and includes the
  `client_secret` or `code_verifier` that never appeared in any request to
  `pivot.claude.ai`.
* A Claude account sign-in produces requests from the add-in frame to
  `claude.ai/v1/oauth/device_authorization` and `claude.ai/v1/oauth/token`,
  and no request to `pivot.claude.ai/auth/callback`.
* Microsoft Graph calls go directly to `graph.microsoft.com` with a
  bearer token that was issued by `login.microsoftonline.com` and never
  transited an Anthropic domain.

## Differences from signing in with a Claude account

When you sign in with a Claude account, the add-ins connect directly to
Anthropic, unless you sign in to an organization that manages them from
the Enterprise Admin Console. When you connect through a third-party
platform, the add-ins send inference requests to your organization's
infrastructure instead, and your IT team controls how that traffic is
routed and logged.

Some features work differently through third-party platforms, and
others aren't available. The third-party platform column also applies
to members of an organization that
[manages the add-in from the Enterprise Admin Console](https://claude.com/docs/office-agents/admin-console.md).

| Feature | Claude account | Third-party platform |
| - | - | - |
| Chat with your spreadsheet, deck, document, or email | Yes | Yes |
| Read and edit cells, slides, formulas, and document text | Yes | Yes |
| Read, search, and triage your mailbox and calendar (Outlook) | Yes | Yes |
| Connectors (S\&P, FactSet, and others) | Yes | Yes: remote MCP servers your admin configures. There's no connector directory, and users can't add their own. |
| Working across apps | Yes | No |
| Dictation | Yes | No |
| Skills | Yes | Yes: built-in skills, skills your admin provides, and skills users upload. |
| File uploads | Yes | Yes, but uploaded files aren't available to code execution. |
| Web search | Yes | Vertex AI direct, Foundry direct, and gateways the add-in detects as routing to Vertex AI, Foundry, or the Anthropic API, where the provider allows it. The add-in checks when it connects and when you change models. Not available on Bedrock. |
| Code execution | Yes | Foundry direct, and gateways the add-in detects as routing to Foundry or the Anthropic API, where the provider allows it, checked the same way. Not available on Bedrock or Vertex AI. |

On a gateway using `gateway_api_format: anthropic`, the add-in tells
where requests go from the `id` in the gateway's response, so the gateway
must pass the provider's response ID through unchanged.

If your team needs a feature that isn't available on your path, talk to
your Claude admin about which sign-in path fits your organization.

## Troubleshooting

### "Connection refused" or network error

The gateway URL or cloud endpoint is unreachable from the user's
network. Verify the URL is correct, the service is running, and there
are no firewall or VPN restrictions blocking the connection. Check the
[Network allowlist](#network-allowlist) to confirm all required domains
are allowed.

### 400 or "Something went wrong with your request"

The gateway or cloud provider rejected the request. Select Copy error
details, or the copy icon, next to the error: the text under `Raw error`
shows the gateway's or provider's own message. Your gateway or provider logs
have more.

In Outlook, if the model menu is missing or that message doesn't explain the
error, see
[Outlook messages fail or the model menu is missing](#outlook-messages-fail-or-the-model-menu-is-missing).

### 401 Unauthorized, "Authentication failed", or "Invalid authentication token"

The auth token is invalid or expired. For gateway connections, confirm
the token with your IT team. For direct-cloud connections, verify the
user's Entra ID account is in the assigned group and that the OIDC trust
or OAuth client is configured correctly. For Foundry with an API key,
regenerate the key in Azure Portal, Keys and Endpoint. For keyless
Foundry sign-in, confirm the Entra app has the Azure Cognitive Services
`user_impersonation` permission with admin consent and that
`entra_scope` is `https://cognitiveservices.azure.com/.default`.

In Outlook, if the model menu is missing or these checks don't explain the
error, see
[Outlook messages fail or the model menu is missing](#outlook-messages-fail-or-the-model-menu-is-missing).

### 403 Forbidden or "Access denied"

The token is valid but lacks the right permissions. For Bedrock, verify
the IAM role has `bedrock:InvokeModel` permissions. For Vertex, verify
your Google account has the Vertex AI User role on the project. For
gateways, check the token's scope with your IT admin, including which
models it may call. For Foundry, check
the resource's networking rules, or confirm the key belongs to the right
resource. For keyless Foundry sign-in, confirm the user holds the
Cognitive Services User role on the resource.

In Outlook, if the model menu is missing or these checks don't explain the
error, see
[Outlook messages fail or the model menu is missing](#outlook-messages-fail-or-the-model-menu-is-missing).

### 404 Not found

The add-in could not reach the expected API path. For gateways, verify
the URL is the base URL such as `https://litellm.example.com:4000`.
Don't include `/v1/messages` in the URL field. With
`gateway_api_format: anthropic`, the gateway must also answer
`GET /v1/models`. If that call fails, sign-in stops with an error.

In Outlook, if the error says that a model isn't available, the model menu
is missing, or these checks don't explain the error, see
[Outlook messages fail or the model menu is missing](#outlook-messages-fail-or-the-model-menu-is-missing).

### 500 or other server errors

The gateway or cloud provider encountered an internal error. Check your
gateway logs, such as `docker logs litellm` for LiteLLM, for
upstream provider errors. Try the request again, and contact your IT
admin if the issue persists.

### "Enter model name" screen or "No Claude model" error

The add-in could not find Claude models when it connected. On a gateway,
sign-in usually stops at an "Enter model name" screen. On Bedrock, Vertex
AI, or Foundry direct, the connection error usually starts with "No Claude
model" or "Model unavailable". Check the cause for your connection path.

* **Gateway with `gateway_api_format: anthropic`**: the gateway's
  `GET /v1/models` response lists no Claude models, or test requests to the
  models that it lists failed. The screen says that it could not retrieve
  the model list in both cases. If the list has no Claude models, your IT
  team can correct it or give you a model ID to enter. If it has Claude
  models, your IT team needs to correct the list or allow your token to call
  those models. Entering an ID yourself usually doesn't help then, because
  the add-in replaces an ID that isn't on the list.
* **Gateway with `gateway_api_format: bedrock` or `vertex`**: none of the
  built-in models responded to the add-in's test requests. Confirm with your
  IT team that the gateway routes to a region or project with Claude models
  enabled.
* **Bedrock or Vertex AI direct**: confirm that at least one Claude model,
  Claude Sonnet 4.5 or later, is enabled in your account and region.
* **Foundry direct**: confirm that at least one Claude model is deployed in
  the resource Model catalog under its default deployment name, such as
  `claude-opus-4-8`.

Connecting doesn't show that Outlook will work: a model that Outlook doesn't
support, such as Claude Sonnet 4.6, is enough to connect. If you use Outlook
and enter a model ID, enter the ID of a model that Outlook supports and your
gateway serves. The example that Outlook shows on the "Enter model name"
screen is a supported model.

If the add-in connects and Outlook has no model menu or its messages fail, see
[Outlook messages fail or the model menu is missing](#outlook-messages-fail-or-the-model-menu-is-missing).

### Outlook messages fail or the model menu is missing

In Outlook, messages fail, the model menu at the bottom of the chat pane
doesn't appear, or both.

Outlook supports fewer models than Excel, PowerPoint, and Word. It needs a
Claude Opus model at version 4.7 or later, or a Claude Sonnet model at
version 5 or later. A newer model in another family doesn't meet this
requirement. A connection that works in the other apps can therefore fail in
Outlook.

To see what failed, select Copy error details, or the copy icon, next to the
error, and paste the result into a text editor. The `status` line shows the
HTTP status, the `model` line shows the model ID that Outlook sent, and the
text under `Raw error` shows what your gateway or cloud provider said. If
you don't manage the connection, send this text and a link to this section
to your IT team.

On Foundry direct, and on an LLM gateway that uses the default
`gateway_api_format: anthropic`, Outlook shows no model menu when the
connection offers no model under an ID that Outlook accepts. A supported
model isn't enough if its ID is a gateway alias that doesn't include its
Anthropic model ID, or a Foundry deployment name other than the default.
With no accepted ID to offer, Outlook usually sends each message to
`claude-opus-4-7`. If your gateway or Foundry resource serves Claude Opus 4.7
under that ID, messages work without the menu. If it refuses that ID, the
error in the chat pane depends on the HTTP status it returns.

| Status | Error in the chat pane |
| - | - |
| 400 | Starts with "Something went wrong with your request." |
| 401 | Starts with "Authentication failed." and tells the user to sign out and sign back in. Some gateways return this status when a key or team isn't allowed to call the model. Signing out doesn't help then, and it deletes saved Outlook conversations. |
| 403 | Starts with "Access denied." On a gateway, the gateway's own message can follow. |
| 404 | Names the model and says that it "isn't available in your organization's Claude setup. Ask your administrator to enable it." |

Other statuses, and some gateway messages, show other errors.

Outlook can add this sentence to the 400, 401, and 403 errors in the table:
"If this keeps happening, tell your administrator that Claude for Outlook
needs Opus 4.7 or later, or Sonnet 5 or later." All four errors in the table
can also have a Learn more link, which opens
[Model availability](https://claude.com/docs/office-agents/outlook.md#model-availability).

The sentence or the link means that Outlook has a list of model IDs for the
connection and accepts none of them. The list holds the Claude models that
your gateway lists or the ID entered on the "Enter model name" screen. On
Foundry direct, it holds the deployments that have a default name. This can
happen even if you serve a supported model, because Outlook reads the model
family and version from the ID. An error without the sentence or the link can
have the same cause.

If your gateway or Foundry resource doesn't serve the ID on the `model` line,
or doesn't allow the user's token to call it, follow the steps for your
connection path. They can also bring back the model menu when messages work
without it.

On Foundry direct and on gateways that use the `anthropic` format, the menu
can also appear while the selected model fails. The errors then start the
same way, without the added sentence or the Learn more link. If the menu
holds more than one model, the 404 error ends with "or choose another in the
model menu." Choose another model in the menu.

On Foundry direct, the menu shows what the add-in found when the user signed
in, so a deployment removed since then stays in it until the user signs in
again.

#### Fix a gateway that uses the `anthropic` format

These steps are for your IT team.

**1. Choose a model ID that Outlook accepts**

Serve Claude Opus 4.7 as `claude-opus-4-7`, as in the
[LiteLLM examples](#example-gateway-configuration-with-litellm), or
another supported model under its Anthropic model ID, such as
`claude-opus-5`. If your gateway uses its own alias, the alias must
include the whole Anthropic model ID of the supported model that it routes
to, such as `prod-claude-opus-4-8` or `claude-sonnet-5-eu`. Outlook reads
the model family and version from the ID, so keep both in the alias and
write the version with hyphens.

**2. Serve and list the model**

Add the model to the gateway under that ID, and list the ID in the
response to `GET /v1/models` for your users' tokens. Outlook doesn't add a
model ID to its model menu when the ID appears only in the
`available_models` key in your manifest or bootstrap response.

If `GET /v1/models` fails, fix that first, because sign-in stops with an
error. If it succeeds but can't include any Claude models, serve Claude
Opus 4.7 as `claude-opus-4-7` if you can. For a user who is already signed
in, Outlook then usually sends messages to that ID, and they work without
the model menu and without a log-out. A user who signs in later has to
enter that ID on the "Enter model name" screen, so give it to them.

If you can't serve that ID, serve another supported model under its exact
Anthropic model ID and give that ID to users who sign in later. For users
who are already signed in, follow the steps after "Reopen the Claude pane".

**3. Allow your users' tokens to call the model**

If the gateway limits each key or team to a list of models, add the
model ID to that list.

**4. Reopen the Claude pane**

Check that `GET /v1/models` answers a user's token successfully within
5 seconds, because the model menu needs that answer. Then ask each Outlook
user to close the Claude pane, select an email, and select the
[Claude button](https://claude.com/docs/office-agents/outlook.md#install-for-yourself) again. The
add-in reads the gateway's model list each time the pane loads, so a
change to that list doesn't need a log-out. If the gateway now lists the
model and the menu still doesn't appear, ask the user to restart Outlook,
or to reload the page in Outlook on the web.

If `GET /v1/models` can't include any Claude models and you can't serve the ID
on the `model` line of a user's failed message, that user has to enter a model
ID, which takes a new sign-in. Use these steps only in that case.

**1. Confirm the model ID**

Confirm that the gateway serves a model that Outlook supports under that
model's exact Anthropic model ID, such as Claude Opus 5 as
`claude-opus-5`. The add-in doesn't test that ID at sign-in, so a wrong ID
shows up only when a message fails.

**2. Tell the user what logging out deletes**

Tell the user that logging out deletes their saved Outlook conversations,
their writing style, and what Claude has learned about their writing, as
described in
[Change or update your gateway connection](#change-or-update-your-gateway-connection).

**3. Ask the user to log out and sign in again**

Ask them to log out, sign in again, and enter that ID on the "Enter model
name" screen.

#### Fix a Foundry direct connection

These steps are for your IT team.

**1. Deploy a supported model under its default name**

In Azure AI Foundry, deploy a supported model and keep its default
deployment name, which is one of the following:

* `claude-opus-4-7`
* `claude-opus-4-8`
* `claude-opus-5`
* `claude-opus-5-5`
* `claude-sonnet-5`
* `claude-sonnet-5-5`

See
[Claude in Microsoft Foundry](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry)
for where each model is hosted. Outlook ignores a deployment with any
other name, even if the `available_models` key in your manifest or
bootstrap response lists it. A deployment's name can't be changed, so if
yours has a custom name, create a new deployment.

**2. Sign in again**

The add-in checks which models are deployed only when it connects. Ask
each Outlook user to send a message first, choosing another model if the
menu is there. If it works and they don't need the menu, they can skip
this step. Anyone else needs a new sign-in. Logging out deletes their
saved Outlook conversations, their writing style, and what Claude has
learned about their writing, so tell them that first. Then ask them to log
out and sign in again, as described in
[Change or update your gateway connection](#change-or-update-your-gateway-connection).

#### Fix Bedrock, Vertex AI, and gateways in those formats

On Bedrock direct, Vertex AI direct, and gateways that use
`gateway_api_format: bedrock` or `vertex`, the add-in uses a built-in model
list, so Outlook shows the model menu. If the selected model fails, choose
another in the menu. If every model fails, confirm that at least one of the
models in the menu is enabled in the account or project that serves your
requests and, on a gateway, that the gateway routes that model's ID. Then
choose that model in the menu.

### Streaming responses fail or hang

Verify that your gateway supports Server-Sent Events (SSE) pass-through.
Some proxy configurations strip or buffer SSE connections, which
prevents streaming responses from reaching the add-in.

### A feature I expected is not available

Dictation and working across apps aren't available through third-party
platforms, and connectors are limited to the MCP servers your admin
configures. If you need these, ask your admin about signing in with a
Claude account instead. Web search and code execution depend on where
your gateway or cloud provider sends requests; see
[Differences from signing in with a Claude account](#differences-from-signing-in-with-a-claude-account).
