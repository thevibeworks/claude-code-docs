> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Web search and web fetch

> How Claude Desktop on 3P reaches the internet, which providers support search, and how to control or disable web access

Claude Desktop includes two built-in tools for reaching the web:

* **Web Search** runs a search-engine query and returns ranked results.
* **Web Fetch** retrieves the contents of a specific URL.

In Claude Desktop on third-party (3P), both are subject to your configuration: search depends on your inference provider, and fetch depends on the egress allowlist you set.

## Web Search

Web Search is a **server-side tool** executed by your inference provider, not by the desktop app. Availability depends on which provider you've configured:

| Provider | Web Search |
| - | - |
| Google Cloud's Agent Platform | Available |
| Microsoft Foundry | Available on both [hosting options](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry#hosting-options) |
| Amazon Bedrock | Not available natively; use the [built-in web search](#built-in-web-search) below |
| Anthropic API | Available |
| Gateway | Available if your gateway implements Anthropic's `web_search` server tool, passes it through to a provider that does, or runs the search itself; see [Gateway-side search](#gateway-side-search) |

On any provider you can configure the [built-in web search](#built-in-web-search) to choose the search backend yourself. Once it is configured, the app stops offering provider-side search and routes the model's search calls to the built-in server. If you want no web search at all, add `"WebSearch"` to [`disabledBuiltinTools`](https://claude.com/docs/third-party/claude-desktop/configuration#disabledbuiltintools) instead. That entry also blocks the built-in web search tool, so do not combine the two.

The [Claude apps gateway](https://code.claude.com/docs/en/claude-apps-gateway) passes the `web_search` tool through to its upstream provider, so Web Search works in Claude Desktop behind that gateway when the upstream is Google Cloud's Agent Platform, Microsoft Foundry, or the Anthropic API. The exception is a gateway policy that holds settings under [`code`](https://code.claude.com/docs/en/claude-apps-gateway-config#apply-code-settings-in-the-code-tab), which turns Web Search off in Cowork, Chat, and Code. Claude Desktop can't see which upstream the gateway routes to, so if the gateway routes any model to Amazon Bedrock, configure the [built-in web search](#built-in-web-search), which replaces provider-side search on every route. To turn web search off instead, add `"WebSearch"` to `disabledBuiltinTools` in the gateway's [Claude Desktop overlay](https://code.claude.com/docs/en/claude-apps-gateway-config#claude-desktop-overlay).

Provider-side search runs on the provider's infrastructure, so queries and results travel over the same path as model inference and are subject to your provider's data-handling terms. It needs no additional firewall rules beyond the inference endpoint itself.

> [!NOTE]
>
> `coworkEgressAllowedHosts` governs client-side egress (Web Fetch and in-sandbox shell network activity). Provider-side Web Search executes at your inference provider, so the allowlist does not apply to it. The built-in `websearch` server under [Web search options](#web-search-options) runs in the desktop app itself, outside the sandbox, and `coworkEgressAllowedHosts` does not apply to it either. Its search provider's host (`api.search.brave.com`, `api.tavily.com`, `api.exa.ai`, or the host of your `customUrl`) does need to be reachable through your perimeter firewall and proxy, and the **Egress** section of the in-app configuration window lists that host. To let the agent fetch pages it finds via search, add the relevant hosts to `coworkEgressAllowedHosts` or set it to `["*"]`.

### Web search options

| Option | Best for | Where you configure it | Search backend |
| - | - | - | - |
| [Provider-native](#provider-native-search) | Google Cloud's Agent Platform, Microsoft Foundry | Your cloud provider's console | The provider's |
| [Built-in](#built-in-web-search) | Amazon Bedrock or a custom gateway; or any provider when you want to choose the search backend | `managedMcpServers` | Brave, Tavily, Exa, or your own server |
| [Gateway-side](#gateway-side-search) | A custom gateway you already run | Your gateway's configuration | Whatever your gateway is wired to |
| [Remote search MCP](#remote-search-mcp) | A search MCP you already run, or Amazon Bedrock AgentCore | `managedMcpServers` | Whatever that MCP exposes |

#### Provider-native search

Google Cloud's Agent Platform grounding and Microsoft Foundry both execute search inside the model call. There's nothing to configure in Claude Desktop. Any setup happens on the cloud provider's side.

#### Built-in web search

Add the bundled `websearch` server to [`managedMcpServers`](https://claude.com/docs/third-party/claude-desktop/configuration#managedmcpservers). Search runs in the desktop app itself, so it works on every inference provider, including Amazon Bedrock.

You can add it from the [in-app configuration window](https://claude.com/docs/third-party/claude-desktop/in-app-configuration.md): under **Connectors**, add a **Web search** server, choose the search provider, and supply the vendor key as a header or through a headers helper script.

![Web search server card in the in-app configuration window with fields for name, tool policy, headers, and headers helper script, and a search provider menu offering brave, tavily, exa, and custom.](https://mintcdn.com/claude-ai/iVbkJluVpijKTo5a/images/third-party/config-window-web-search.png?fit=max\&auto=format\&n=iVbkJluVpijKTo5a\&q=85\&s=19cf4844972d9fd47addec8690db09c8)

The Web search server in the Connectors section of the in-app configuration window, with the search provider menu open.

In the exported configuration, set `provider` to a hosted search vendor (`brave`, `tavily`, or `exa`) for the lowest setup, or to `custom` with `customUrl` to point at a search server you run.

Hosted vendor:

```json theme={null}
{
  "managedMcpServers": [
    {
      "name": "Web search",
      "server": "websearch",
      "provider": "tavily",
      "headersHelper": "/opt/org/bin/tavily-headers",
      "toolPolicy": { "web_search": "allow" }
    }
  ]
}
```

> [!NOTE]
>
> A hosted-vendor key configured in `headers` or returned by `headersHelper` is the same key on every device, and a local user can extract it. The exposure is limited to billing abuse on that key (it grants no data access). For regulated environments, set spend caps and rotate the key on a schedule, or have `headersHelper` fetch a per-user key: Tavily and Exa support per-user or per-team keys; see their key-management docs.

Your own server:

```json theme={null}
{
  "managedMcpServers": [
    {
      "name": "Web search",
      "server": "websearch",
      "provider": "custom",
      "customUrl": "https://search.internal.example.com/v1/search",
      "headersHelper": "/opt/org/bin/search-headers",
      "toolPolicy": { "web_search": "allow" }
    }
  ]
}
```

Set the per-entry `toolPolicy` to `"allow"` so users aren't prompted to approve each search in Cowork sessions and Chat conversations. For Code sessions, see [Tool permissions for managed MCP servers](https://claude.com/docs/third-party/claude-desktop/configuration.md#tool-permissions-for-managed-mcp-servers). `headersHelper` is an executable that prints the auth header as a JSON object to stdout; it follows the same execution model as [`inferenceCredentialHelper`](https://claude.com/docs/third-party/claude-desktop/credential-helper) (exit 0, stdout read as JSON), but the output here is a flat header map, not the `{token, headers}` shape `inferenceCredentialHelper` uses.

| Provider | Header your script should output |
| - | - |
| `brave` | `{"X-Subscription-Token": "<key>"}` |
| `tavily` | `{"Authorization": "Bearer <key>"}` |
| `exa` | `{"x-api-key": "<key>"}` |
| `custom` | Whatever your search server expects |

You can use a static `headers` object instead if you don't need a secrets manager.

With `provider: "custom"`, Claude Desktop sends each search as an HTTP `POST` to `customUrl` exactly as written (nothing is substituted into the URL), with `Content-Type: application/json`, any headers from `headers` and `headersHelper`, and the body `{"q": "<search terms>"}`. Your server must answer within 15 seconds with a 2xx status and a JSON body of the form `{"results": [{"title": "...", "url": "...", "snippet": "..."}]}`. Results without a `url` are dropped, at most 10 are used, and each `snippet` is truncated to 600 characters.

#### Gateway-side search

If your inference gateway can execute search itself, the search key stays server-side and never reaches end-user devices.

For LiteLLM proxy server, enable [`websearch_interception`](https://docs.litellm.ai/docs/tutorials/claude_code_websearch) in `callbacks` and configure a search backend in the proxy. The gateway intercepts the model's `web_search_20250305` request, runs the search, and returns results to Claude Desktop.

If your gateway translates between API formats (for example, Anthropic to OpenAI chat completions), note that `web_search_20250305` is an Anthropic server tool with no chat-completions equivalent. The translation layer needs to handle it explicitly: run the search when the model requests it and emit `server_tool_use` and `web_search_tool_result` blocks in the response. Ask your account team for a reference implementation.

#### Remote search MCP

Connect a search MCP server as a remote `managedMcpServers` entry: either one you host, or Amazon Bedrock AgentCore Gateway with the Web Search target enabled (configure AgentCore for JWT authentication through your identity provider). Whether this stays inside your boundary depends on where the server is hosted; AgentCore is available in commercial AWS regions.

#### Data handling

Search queries go to whichever backend you configure. In every option, the query is also visible to your inference provider as part of the conversation, because the model emits the search call. For Google Cloud's Agent Platform and Amazon Bedrock, Anthropic does not receive search queries in any of these options. For Microsoft Foundry, the Anthropic API, or a gateway, the query is part of the conversation content covered under [Data handling by provider](https://claude.com/docs/third-party/claude-desktop/overview.md#data-handling-by-provider). To keep the search backend itself inside your network, use `provider: "custom"` (or a self-hosted MCP) pointed at a search index that runs inside your boundary.

For audit, each search the model runs is recorded in the Cowork or Code session telemetry sent to your [OTLP collector](https://claude.com/docs/third-party/claude-desktop/telemetry.md#sending-telemetry-to-your-own-collector) as a `tool_result` event, whichever option you choose (a `WebSearch` event for provider-side or gateway-side search, an MCP tool event for the built-in or a remote search server). Add `toolDetails` to [`otlpContentCapture`](https://claude.com/docs/third-party/claude-desktop/telemetry#content-capture) to include the tool input, which carries the query text (long values are truncated). The built-in `websearch` server also emits a `builtin_websearch_call` event on the desktop application's own stream with the search provider, query length, result count, duration, and status, never the query text. The app exports that event only when [`otlpDesktopLogLevel`](https://claude.com/docs/third-party/claude-desktop/configuration#otlpdesktoploglevel) is `info` or `debug`, not at the default `error` level.

## Web Fetch

In Cowork and Chat, Web Fetch runs in the Claude Desktop main process on the user's device. The model supplies only the target URL; it cannot set headers, a request body, or credentials. Each request carries the app's own browser-style `User-Agent` header, which includes `Claude/<app version>`. The app checks every fetch, including redirect targets, against `coworkEgressAllowedHosts` before it sends the request. For Code sessions, see [How the egress allowlist applies in Code sessions](#how-the-egress-allowlist-applies-in-code-sessions).

Cowork and Chat refuse every fetch while the key is unset or empty. To permit fetches:

| Goal | Set `coworkEgressAllowedHosts` to |
| - | - |
| Allow specific domains | `["docs.example.com", "*.example.corp"]` |
| Allow all hosts (no sandbox filtering) | `["*"]` |
| Block all fetches, in Code sessions too | `[]` and add `"WebFetch"` to `disabledBuiltinTools` |

Wildcards match one or more leading subdomain labels (`*.example.com` matches `a.example.com` and `a.b.example.com`, but not `example.com`). A listed host that many organizations share, such as a cloud provider's API endpoint, is reachable from the agent's shell with any account's credentials. A command can then send data to an account outside your organization.

> [!NOTE]
>
> Your perimeter firewall is a separate, outer layer from `coworkEgressAllowedHosts`, so a host allowed by this key still won't be reachable if your corporate network blocks it. See [Telemetry and egress](https://claude.com/docs/third-party/claude-desktop/telemetry.md#required-egress-paths) for the distinction.

The same allowlist governs other in-sandbox network activity (for example, `curl` or `pip install` from the agent's shell), not just the Web Fetch tool. A command-line tool that a [plugin](https://claude.com/docs/third-party/claude-desktop/extensions.md#controlling-user-extensions) adds to the Cowork sandbox can also reach the hosts its plugin declares, whatever the list holds. Claude Desktop's own connections for inference, sign-in, model discovery, telemetry export, and MCP servers aren't checked against it and need no entry.

If a shell command or a Claude Code [HTTP hook](https://code.claude.com/docs/en/hooks#http-hook-fields) calls your gateway, inference provider, OTLP collector, or `api.anthropic.com`, add that host. Earlier versions of Claude Desktop added some of these hosts automatically, so when you update, add the ones the agent calls.

In [Code](https://claude.com/docs/third-party/claude-desktop/code.md) sessions, Claude Code's Web Fetch tool also asks `api.anthropic.com` whether each domain is on Anthropic's blocklist before fetching, and refuses the fetch if that lookup cannot complete. If your devices cannot reach `api.anthropic.com`, or you do not want fetched hostnames sent there, set [`skipWebFetchPreflight`](https://claude.com/docs/third-party/claude-desktop/configuration#skipwebfetchpreflight) to `true`. The key requires Claude Desktop 1.37937.0 or later. Cowork sessions do not perform this lookup.

### How the egress allowlist applies in Code sessions

In [Code](https://claude.com/docs/third-party/claude-desktop/code.md) sessions, the key reaches Claude Code's own Web Fetch tool and shell sandbox as managed settings, unless [Claude Code managed settings that you deploy separately](https://claude.com/docs/third-party/claude-desktop/code.md#interaction-with-claude-code%E2%80%99s-own-managed-settings) take precedence:

* **Web Fetch**: each host you list becomes a Claude Code `WebFetch` allow rule. The key doesn't block a fetch to another host. In Auto mode, which new Code sessions start in by default, and in bypass permissions mode, Claude Code doesn't ask the user before that fetch. For the other modes, see [WebFetch tool behavior](https://code.claude.com/docs/en/tools-reference#webfetch-tool-behavior).
* **Web Fetch controls**: to have the user approve every fetch, set `WebFetch` to `"ask"` in [`builtinToolPolicy`](https://claude.com/docs/third-party/claude-desktop/configuration#builtintoolpolicy), which also applies in Cowork and Chat. To remove the tool, see [Disabling web tools](#disabling-web-tools).
* **Shell commands**: commands that run in [Claude Code's sandbox](https://claude.com/docs/third-party/claude-desktop/code.md#applied-as-managed-policy) reach only the hosts you list, and no host while the list is empty. For a key that isn't set, see [Unset allowlist in Code sessions](#unset-allowlist-in-code-sessions). On Windows, and on Linux without Claude Code's sandbox dependencies, shell commands run unsandboxed and can reach any host your network allows. To keep Code off such devices, see [Disabling Code](https://claude.com/docs/third-party/claude-desktop/code.md#disabling-code). For SSH hosts, see [Sandbox status on the remote host](https://claude.com/docs/third-party/claude-desktop/ssh-remote-sessions.md#sandbox-status-on-the-remote-host).
* **Hooks, local MCP servers, and mods**: [hooks that run a command](https://code.claude.com/docs/en/hooks#hook-handler-fields), local (stdio) MCP servers, and [Claude Code mods](https://claude.com/docs/third-party/claude-desktop/code.md#claude-code-mods) run outside Claude Code's sandbox and can reach any host your network allows. To limit which of them run, see the warning under [Applied as managed policy](https://claude.com/docs/third-party/claude-desktop/code.md#applied-as-managed-policy).

#### Unset allowlist in Code sessions

The [in-app configuration window](https://claude.com/docs/third-party/claude-desktop/in-app-configuration.md) shows `coworkEgressAllowedHosts` as **Allowed egress hosts**, an unset key as **Not set**, and an empty list (`[]`) as **Allow none**. Where [Claude Code's sandbox](https://claude.com/docs/third-party/claude-desktop/code.md#applied-as-managed-policy) doesn't run, such as a Code session on Windows, shell commands run unsandboxed and can reach any host your network allows, whatever the key holds. To keep Code off those devices, see [Disabling Code](https://claude.com/docs/third-party/claude-desktop/code.md#disabling-code).

When you deliver configuration through the Enterprise Admin Console, a bootstrap server, or a [managed source](https://claude.com/docs/third-party/claude-desktop/configuration-format.md#where-claude-desktop-reads-configuration-on-a-device) such as an MDM profile, an unset key turns on Claude Code's sandbox. Where the sandbox runs, shell commands in it reach no host, and the **Local sandbox** and **Strict sandbox mode** toggles under **Settings > Claude Code** are on and locked. To let shell commands reach a host, add it to `coworkEgressAllowedHosts` in your configuration.

> [!WARNING]
>
> On a device whose only configuration is the local configuration file, including a file that you copy to the device with a script, an unset key doesn't turn on the sandbox by itself. Unless [`blockReadsOutsideWorkingDirectories`](https://claude.com/docs/third-party/claude-desktop/configuration#blockreadsoutsideworkingdirectories) is `true`, Claude Desktop doesn't limit the hosts that shell commands in Code sessions reach. Enrolling the device in MDM doesn't change that. What counts is a [managed source](https://claude.com/docs/third-party/claude-desktop/configuration-format.md#where-claude-desktop-reads-configuration-on-a-device) for Claude Desktop itself.
>
> To turn the sandbox on with no host allowed, set `coworkEgressAllowedHosts` to `[]` in the file. The device's user can edit the file, so to hold the setting, deliver the configuration from a managed source.

If you set up the device yourself in the in-app configuration window ([single-machine setup](https://claude.com/docs/third-party/claude-desktop/installation.md#single-machine-setup)) and left **Allowed egress hosts** at **Not set**, go to **Settings > Claude Code** and check the **Local sandbox** toggle:

* **The toggle is unlocked**: Code sessions follow your own Claude Code settings. While the toggle is off, shell commands run unsandboxed, and the session's permission mode and permission rules decide whether Claude Code asks you before it runs one. In Auto mode, the default for new Code sessions where the model supports it, a safety classifier decides instead of asking you. To run a local session's commands in the sandbox, turn on the toggle.
* **The toggle is on and locked**: something else keeps the sandbox on, for example:
  * **A [managed source](https://claude.com/docs/third-party/claude-desktop/configuration-format.md#where-claude-desktop-reads-configuration-on-a-device) on the device**: shell commands reach no host
  * **Block reads outside working directories** turned on: shell commands reach no host
  * **Allowed workspace folders** set, with neither of the other two: Claude Desktop doesn't limit the hosts, and [Claude Code's sandbox](https://code.claude.com/docs/en/sandboxing) decides which ones shell commands reach
* **The toggle is missing, or is off and can't be changed**: the sandbox doesn't run on the device, so shell commands in local sessions run unsandboxed

For what a list of hosts does, see [How the egress allowlist applies in Code sessions](#how-the-egress-allowlist-applies-in-code-sessions). To change the list, open the in-app configuration window, go to **Capabilities**, edit **Allowed egress hosts**, click **Apply Changes**, and then click **Save & Restart**. Removing the last host leaves **Allow none** selected, which allows no host. To unset the key again, select **Not set** once the list is empty.

## Disabling web tools

To remove web tools entirely, add them to `disabledBuiltinTools`:

```json theme={null}
["WebSearch", "WebFetch"]
```

With the web tools removed and `coworkEgressAllowedHosts` empty, commands in the agent's sandboxed shell reach no host other than those a [plugin declares for its command-line tool](#web-fetch). In Code sessions where [Claude Code's sandbox doesn't run](#how-the-egress-allowlist-applies-in-code-sessions), shell commands can reach any host your network allows.

The agent can still read and write local files, run code against them, and call any MCP servers you've provisioned. See the [Locked down profile](https://claude.com/docs/third-party/claude-desktop/configuration.md#recommended-security-profiles).

## User settings for web tools

Each user can make Web Search or Web Fetch stricter for themselves than your configuration requires, and can't make either tool looser. The user goes to **Customize > Connectors** and sets **Web search** or **Web fetch** under **Built-in tools**, or opens the message box's **+** menu and selects **Connectors**. Each tool's setting covers the user's Cowork, Chat, and Code sessions and takes one of these values:

* **Default**: your configuration and the session's permission mode decide whether Claude asks first
* **Always ask**: Claude asks the user before each call to the tool, including in Auto mode, which Cowork shows as **Automatically approve**
* **Blocked**: new sessions don't include the tool

A session that's already running can keep its earlier setting until it next starts. When a [scheduled Cowork task](https://claude.com/docs/third-party/claude-desktop/scheduled-tasks.md) runs on its schedule in **Automatically approve**, Claude Desktop declines a call to a tool that's at **Always ask** by the user's choice alone, and the run continues without that step.

Your configuration sets the minimum for each tool, and the user sees why a choice is missing:

* **`WebSearch` or `WebFetch` set to `"ask"` in [`builtinToolPolicy`](https://claude.com/docs/third-party/claude-desktop/configuration#builtintoolpolicy)**: the user selects **Always ask** or **Blocked**, next to the line **Restricted by your admin**
* **`WebSearch` or `WebFetch` listed in [`disabledBuiltinTools`](https://claude.com/docs/third-party/claude-desktop/configuration#disabledbuiltintools)**: the tool's row reads **Blocked by your admin**, and the user can't change it

The **Web search** row appears where your provider or gateway runs Web Search, and controls that tool. When you configure the [built-in web search](#built-in-web-search), that server has a row of its own in both places, and users control search from that row.

A user's setting is a preference that the user can change back at any time. **Blocked** removes that tool, and shell commands and browser tools still reach what your configuration allows. To enforce a restriction for everyone, see [Disabling web tools](#disabling-web-tools).
