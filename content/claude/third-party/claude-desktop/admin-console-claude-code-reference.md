> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# How Claude Code in the terminal applies your console settings

> Look up which Enterprise Admin Console settings Claude Code in the terminal applies, how it uses your connection, and where data goes.

Look up which [Enterprise Admin Console](https://claude.com/docs/third-party/claude-desktop/admin-console.md) settings Claude Code applies in the terminal and in VS Code, how it handles credentials and gateways, where data goes, and what the settings can't prevent.

> [!NOTE]
>
> To set up Claude Code in the terminal, see [Manage Claude Code in the terminal from the Enterprise Admin Console](https://claude.com/docs/third-party/claude-desktop/admin-console-claude-code.md).

## Console settings that Claude Code follows

This table shows the fields under **Organization settings > Desktop 3P** that Claude Code follows:

| Page | Field | Effect in the terminal |
| - | - | - |
| **Connection** | **Inference provider**, and the fields for that provider | Sends model requests to that provider or gateway |
| **Connection** | **Model list** | `/model` in Claude Code lists your models. Developers can pick only the models on your list. |
| **Connection** | **Tier alias** and **Max effort**, on an entry in the **Model list** | Uses that model for the tier, as with `--model haiku`. Developers can't raise that model's effort above the level that you set. |
| **Capabilities** | **Disabled built-in tools** | Claude can't use the [tools](https://code.claude.com/docs/en/tools-reference) you list |
| **Capabilities** | **Built-in tool policy** | Asks the developer before a call that matches an `ask` entry, and refuses it where nobody can answer, as in `claude -p`. `allow` entries have no effect. |
| **Capabilities** | **Disable bypass permissions mode** | Refuses bypass permissions mode |
| **Capabilities** | **Allow Auto mode** | When it's off, developers can't use Auto mode |
| **Capabilities** | **Allowed egress hosts** | On macOS, Linux, and WSL2, Bash commands run in the [sandbox](https://code.claude.com/docs/en/sandboxing). They can reach the hosts you list, your OpenTelemetry endpoint, and `api.anthropic.com` unless **Block nonessential telemetry** is on. A developer can exclude a command from the sandbox in their own settings. On native Windows, or where the sandbox can't start, the list doesn't limit Bash commands. A list that has a `*` entry has no effect in the terminal. |
| **Capabilities** | **Block reads outside working directories** | Claude's file tools can't read files outside the session's working directories. Claude Code asks before a Bash command that names such a path. |
| **Capabilities** | **Skip WebFetch domain check** | Skips the [domain safety check](https://code.claude.com/docs/en/data-usage#webfetch-domain-safety-check) |
| **Capabilities** | **Disable bundled skills and workflows** | Turns off the bundled skills and workflows |
| **Connectors** | **Allowed plugin MCP servers** | Connects only to remote MCP servers whose URL matches an entry, apart from built-in servers and the computer's managed servers. Ignores the servers in developers' and projects' settings. |
| **Connectors** | **Blocked plugin MCP servers** | Doesn't connect to remote MCP servers whose URL matches an entry, including ones that developers add themselves |
| **Connectors** | **MCP tool call timeout** | Sets the default time limit for an MCP tool call |
| **Connectors** | **Managed MCP servers** | Not added in the terminal. Each entry's **Tool policy** applies to a plugin's MCP server with the same name or URL. |
| **Connectors** | **Allow local MCP servers** | Not applied in the terminal. To stop the local MCP servers that developers, projects, and plugins add, enter `{"allowManagedMcpServersOnly": true, "allowedMcpServers": [{"serverUrl": "*"}]}` in the [JSON](#claude-code-settings-as-json) on the **Claude Code** page. It doesn't stop remote MCP servers. |
| **Plugins** | **Plugin marketplaces** | `/plugin` in Claude Code lists your marketplaces as `offered by your organization`. It skips some, such as ones that need a helper script. Developers can't use the plugin directory (`/plugin directory`), and plugins installed from it don't load. |
| **Plugins** | **Organization plugin settings** | On a plugin's MCP server with that **Server name**, Claude can't use a tool set to **Blocked**. Claude Code asks before it uses a tool set to **Ask each time**. If **Managed MCP servers** has an entry with the same name, Claude Code uses only that entry's **Tool policy**, even if the entry has none. Set **Blocked** and **Ask each time** there. |
| **Telemetry & updates** | **Block essential telemetry** | Sends no [error reports](https://code.claude.com/docs/en/data-usage#telemetry-services) |
| **Telemetry & updates** | **Block nonessential telemetry** | Turns off automatic updates and `/feedback` |
| **Telemetry & updates** | **OTLP endpoint** and the other OTLP fields | Sends OpenTelemetry data to [your collector](#where-data-goes). **Desktop telemetry export level** and **Telemetry attribute length limit** have no effect in the terminal. |
| **Appearance** | **End-user attribution** | When it's off, the data sent to your collector leaves out `enduser.id` |

If you block an MCP server that the developer added and that's already running, the server keeps answering in that session.

## Claude Code settings as JSON

The JSON on the **Claude Code** page has the same format as `managed-settings.json`, but Claude Code applies only a fixed list of its settings. No setting in the JSON can grant a permission, run a command, sign in, or choose a provider or a model. To enter the JSON, see [Add Claude Code settings as JSON](https://claude.com/docs/third-party/claude-desktop/admin-console-claude-code.md#add-claude-code-settings-as-json).

### Settings that Claude Code applies

This table shows the main settings that Claude Code applies. For what each one does, see the [settings reference](https://code.claude.com/docs/en/settings-reference).

| Settings | Applied when the value is |
| - | - |
| `permissions.deny`, `permissions.ask` | A list of rules |
| `permissions.disableBypassPermissionsMode`, `permissions.disableAutoMode` | `"disable"` |
| `permissions.blockReadsOutsideWorkingDirectories` | `true` |
| `deniedModels`, `maxEffortLevel` | A list of models, or an effort level |
| `deniedMcpServers`, `disabledMcpjsonServers`, `allowedMcpServers`, `allowManagedMcpServersOnly` | A list, or `true` for `allowManagedMcpServersOnly`, which applies only with an `allowedMcpServers` list |
| `blockedMarketplaces` | A list of marketplace sources. An entry that gives only a name blocks nothing. |
| `allowManagedHooksOnly` | `true` |
| Switches such as `disableWorkflows`, `disableBundledSkills`, `disableSkillShellExecution`, and `disableClaudeAiConnectors` | `true` |
| `sandbox.filesystem.denyRead`, `sandbox.filesystem.denyWrite`, `sandbox.network.deniedDomains`, `sandbox.allowUnsandboxedCommands`, `sandbox.autoAllowBashIfSandboxed` | A list, or `false` for the last two |
| Variables in `env` that turn off a feature or telemetry to Anthropic, such as `DISABLE_TELEMETRY` and `CLAUDE_CODE_DISABLE_BACKGROUND_TASKS` | `1` or `true` |
| `CLAUDE_CODE_ENABLE_TELEMETRY` and the `OTEL_LOG_` variables in `env`, which can only turn OpenTelemetry or some of its logging off | `0` or `false` |
| Timeouts and size limits in `env`, such as `BASH_MAX_TIMEOUT_MS` | A whole number |
| `companyAnnouncements` | A list of text |

Claude Code ignores every setting that isn't on its list, such as `permissions.allow`, `model`, `hooks`, `forceLoginOrgUUID`, `requiredMinimumVersion`, and `cleanupPeriodDays`. It also ignores a switch that loosens a limit, such as `disableWorkflows: false`.

Some settings have conditions:

* **Sandbox settings**: these apply when the sandbox is on. Your JSON can't turn it on, but **Allowed egress hosts**, the computer's managed settings, or a developer's own settings can.
* **`permissions.ask`**: if a developer sets `sandbox.autoAllowBashIfSandboxed` to `true`, a `Bash` rule with no pattern, such as `Bash` or `Bash(*)`, stops asking for sandboxed commands. To keep the rule asking, set that key to `false` in your JSON.
* **A switch or a group with a value that Claude Code can't read**, such as `"disableBypassPermissionsMode": "allow"` in `permissions`: for most of these, Claude Code applies the strictest value. In this example, bypass permissions mode stays blocked for every developer until you correct the value.
* **A deny setting that isn't a list**, such as `"deniedModels": 5`: it denies nothing
* **A setting that a group's policy also sets**: in the JSON, lists such as `permissions.deny` add together, so a policy can't remove an organization-wide deny rule. A single value, or the whole `allowedMcpServers` list, comes from the highest-ranked policy that sets it. A console field in a policy replaces the organization-wide value.

## Credentials and gateways

While a terminal uses your connection, the developer's own Claude login or API key doesn't go to the gateway. Check these settings before developers sign in:

* **Helper scripts**: Claude Code checks the **Helper script** on your **Connection** page and the **OTLP headers helper script** on your **Telemetry & updates** page before it runs them. To install them, see [Install the helper for Claude Code in the terminal](https://claude.com/docs/third-party/claude-desktop/credential-helper.md#install-the-helper-for-claude-code-in-the-terminal).
* **A gateway that Claude Code can't use**: Claude Code in the terminal doesn't use your gateway if, for example, the **Helper script** is missing from the computer, or the sign-in flow is `broker` and you haven't [allowed browser sign-in](https://claude.com/docs/third-party/claude-desktop/entra-broker.md#allow-browser-sign-in-where-your-gateway-uses-the-entra-broker). `/status` in Claude Code names the setting. The session then uses the provider and the credentials that are set on the computer. These can be the developer's own Claude login or API key, even when `ANTHROPIC_BASE_URL` on the computer is your gateway's address. If nothing on the computer sets a provider, Claude Code doesn't start. In that case, it doesn't send prompts to the Anthropic API with the developer's own login or key.
* **Gateway-managed Claude Code**: if the console doesn't show this switch, it's off. With an identity provider, the switch changes nothing in a terminal. If the switch is on with **Interactive sign-in** and no identity provider, a provider that the developer or the computer set stays in use until the developer runs `/login` in Claude Code. After that, the session follows the gateway's own settings, and none of your console settings apply. In that setup, on a computer whose `forceLoginOrgUUID` lists your organization, Claude Code doesn't sign in to the gateway. It refuses prompts there unless the developer or the computer set a provider or `ANTHROPIC_BASE_URL`.

## Managed settings beside the console

If you [keep managed settings beside the console](https://claude.com/docs/third-party/claude-desktop/admin-console-claude-code.md#keep-managed-settings-beside-the-console), this is how the two sets of settings combine while a developer is signed in:

* **Many settings persist**: these include cloud credentials, proxy variables in `env`, model names, hooks, required versions, managed MCP servers, and plugins
* **Your connection replaces these `env` values**: the cloud provider, region, project, resource, provider base URL, and custom request headers. If you have a **Model list**, it replaces `availableModels`.
* **Your collector replaces the computer's**: if you filled in **OTLP endpoint**, OpenTelemetry data goes only to your collector. Your OTLP fields replace the computer's OpenTelemetry address, protocol, resource attributes, and content settings. `CLAUDE_CODE_ENABLE_TELEMETRY` set to `0` on the computer doesn't turn off the export. To turn it off, use the [JSON](#claude-code-settings-as-json). `OTEL_LOG_ASSISTANT_RESPONSES` set to `0` on the computer still applies, with the limits under [Content capture](https://claude.com/docs/third-party/claude-desktop/telemetry.md#content-capture).
* **Certificates for your collector**: exports to your collector don't use `OTEL_EXPORTER_OTLP_CERTIFICATE`, `OTEL_EXPORTER_OTLP_CLIENT_CERTIFICATE`, or `OTEL_EXPORTER_OTLP_CLIENT_KEY`, even over gRPC. Use `NODE_EXTRA_CA_CERTS` for a private CA, and `CLAUDE_CODE_CLIENT_CERT` and `CLAUDE_CODE_CLIENT_KEY` for a [client certificate](https://code.claude.com/docs/en/network-config#mtls-authentication).
* **These stop applying, and you can enter them in the console**: `companyAnnouncements` and `allowedMcpServers` if you set it without `allowManagedMcpServersOnly`
* **These stop applying, and the console can't set them**: `permissions.allow`, the default permission mode, added directories, `statusLine`, `skillOverrides`, `claudeMdExcludes`, `autoMemoryEnabled`, and display preferences. The developer's own settings decide these. A skill that you turned off with `skillOverrides` is available again.
* **Your proxy for sandboxed commands stops applying**: Claude Code ignores `sandbox.network.httpProxyPort` and `sandbox.network.socksProxyPort` in the computer's managed settings. The console can't set them. Sandboxed commands no longer go through your proxy. To limit the hosts that sandboxed commands reach, use **Allowed egress hosts**.
* **These apply together with your console settings**: `permissions.deny`, `permissions.ask`, `deniedModels`, `deniedMcpServers`, `disabledMcpjsonServers`, `sandbox.network.deniedDomains`, `sandbox.filesystem.denyRead`, `sandbox.filesystem.denyWrite`, blocked marketplaces, and Auto mode's deny rules
* **`sandbox.filesystem.allowRead` persists**: sandboxed commands can read the paths in that list, even if your console settings deny them
* **The stricter value applies**: switches that only restrict, such as `permissions.disableBypassPermissionsMode`, `allowManagedHooksOnly`, and `sandbox.enabled`

### Managed settings that conflict with the console

Check the computer's managed settings for these:

* **A private endpoint**: the managed settings can give Claude Code a private address for your provider, such as `ANTHROPIC_BEDROCK_BASE_URL` for a VPC endpoint. Your connection overrides that address, and requests go to the provider's default address. To keep the private address, enter it in the provider's base URL field on the **Connection** page, such as **Bedrock base URL**. Claude Desktop then uses that address. Claude Code in the terminal stops using your connection, and uses the provider, region, address, and credentials that are set on the computer. Your restrictions still apply, but your **Model list** and custom headers don't. The base URL field applies to every developer who signs in, so Claude Code doesn't start on a computer that sets no provider.
* **A Microsoft Foundry key**: if the managed settings set `ANTHROPIC_FOUNDRY_API_KEY` or `ANTHROPIC_FOUNDRY_AUTH_TOKEN`, check which of these applies, and make the change in the managed settings. Don't set both `ANTHROPIC_FOUNDRY_RESOURCE` and `ANTHROPIC_FOUNDRY_BASE_URL`, because Foundry requests then fail.
  * **If the managed settings set `ANTHROPIC_FOUNDRY_RESOURCE`, or set neither that variable nor `ANTHROPIC_FOUNDRY_BASE_URL`**: make sure that `ANTHROPIC_FOUNDRY_RESOURCE` is set beside the Foundry key. Otherwise, Claude Code refuses each Foundry request once the computer has `forceLoginOrgUUID`, even before a sign-in. If your provider is Microsoft Foundry, use the resource on your **Connection** page. With any other resource, Claude Code refuses each Foundry request after a sign-in.
  * **If the managed settings set `ANTHROPIC_FOUNDRY_BASE_URL` and your provider is Microsoft Foundry**: a sign-in overrides that base URL, and Claude Code then refuses each Foundry request. Replace it with `ANTHROPIC_FOUNDRY_RESOURCE`, set to the resource on your **Connection** page. To keep it as a private endpoint instead, follow **A private endpoint** in this list.
* **`forceLoginMethod` and `forceLoginGatewayUrl`**: remove `forceLoginGatewayUrl`, and don't set `forceLoginMethod` to `console` or `gateway`. Otherwise, Claude Code refuses the sign-in to your organization.
* **`allowedProviders`**: add your provider to the list. For a gateway, add `customEndpoint`, and set `ANTHROPIC_BASE_URL` in the managed `env` to your **Gateway base URL**, with a lower-case host and no trailing slash.
* **Model names**: `model`, `fallbackModel`, and `modelOverrides` persist. If those model names are for a different provider than your connection, remove them.
* **A [policy helper](https://code.claude.com/docs/en/settings-reference#policyhelper)**: the computer ignores your console, even with `forceLoginOrgUUID`

To go back, remove your organization's ID from `forceLoginOrgUUID`, or remove `forceLoginOrgUUID` if your organization's ID is the only one. Also remove `enforceAnthropicSignIn` and `parentSettingsBehavior` if you set them. Ask developers to run `claude auth logout` in their terminal, which removes the leftover sign-in and their other Claude Code logins.

## Where data goes

While a terminal uses your connection, model requests and their content go from the developer's terminal to your provider or gateway. For the sign-in and your settings, the terminal exchanges the following with Anthropic:

* **At sign-in**: after the developer approves in their browser, Claude Code receives a token that can read the developer's profile and the Claude Desktop configuration that applies to them, including your **Connection** settings. The token can't run a model.
* **At each download**: Claude Code sends that token to `api.anthropic.com` and receives the settings for that developer
* **To complete, renew, or end the sign-in**: Claude Code sends the sign-in's own tokens to `platform.claude.com`

Claude Code's own telemetry includes the following:

* **Usage metrics**: the sign-in itself sends some [usage metrics](https://code.claude.com/docs/en/data-usage#telemetry-services) to `api.anthropic.com` and to Datadog (`http-intake.logs.us5.datadoghq.com`), even with **Block nonessential telemetry** on, because Claude Code downloads that setting after the sign-in
* **Error reports**: a session under your settings sends none
* **WebFetch domain check**: a session sends each page's host name to `api.anthropic.com`, unless you turn on **Skip WebFetch domain check**

If you filled in **OTLP endpoint**, Claude Code also sends OpenTelemetry data directly from the developer's computer to your collector, not through Anthropic.

* **Metrics and logs**: Claude Code sends these, and traces if **Export traces** is on
* **Content**: prompts, responses, tool details, tool content, and raw API bodies go only if you select them under **Content capture**. If you select prompts, responses go too. Raw API bodies hold full requests and responses, so they include prompts, responses, and tool content even if you didn't select those.
* **The developer's identity**: each record includes the computer's user name as `process.owner`. Unless **End-user attribution** is off, it also includes `enduser.id`. This is the name from the developer's sign-in to your gateway or identity provider, or else their account's email address.
* **A token, if you choose to send one**: if **Collector authentication** is **Reuse the inference credential**, Claude Code sends the collector the bearer token, if there is one, from your **Helper script**, your gateway's sign-in, or your identity provider. That token can also make model requests as the developer, so use this option only for a collector that you operate. After the token expires, Claude Code sends data without a valid token until the next model request. If your collector refuses that data, it's lost.
* **Which sessions send**: a `claude ssh` session sends nothing to your collector. On a computer with no managed settings, neither does a session that uses a Claude login, an Anthropic API key, or a base URL of the developer's own. On a computer whose managed settings name your organization, your collector gets the session's telemetry whichever login or key signs the requests.

Claude Code keeps these on the developer's computer, among other files:

* **The sign-in, and the sign-in to your gateway**: in Claude Code's credential store. This is the Keychain on macOS, and the file `.credentials.json` in Claude Code's configuration directory on Linux, or on macOS if the Keychain refuses the write. On Windows, it's that file or Windows Credential Manager.
* **The stored copy of your settings**: in Claude Code's configuration directory, `~/.claude` by default. It doesn't hold your connection or your collector's address and headers.
* **A record of where your connection sent requests**: in `~/.claude.json`. The record holds your organization's ID and no credentials. For a cloud provider, it also holds the provider with its region, project, resource, AWS profile, and Amazon Bedrock inference profiles, which can include an AWS account ID. For a gateway, it holds the gateway's host and your identity provider's address.

## Security considerations

A developer doesn't need administrator access to bypass your settings. These are some of the ways a developer can work without them, and what limits each one:

* **Signs in to another organization that's set up this way, on a computer with no managed settings**: the other organization's settings, including its OpenTelemetry collector, apply instead of your organization's settings. `forceLoginOrgUUID` in the computer's managed settings limits this.
* **Signs in to your organization while still signed in to a Claude apps gateway, on a computer with no managed settings**: sessions stay on that gateway, and your settings don't apply. The sign-in then prints `Claude Code still uses the gateway at`. To fix it, the developer runs `claude auth logout` in their terminal and signs in to your organization again. If their own settings set `forceLoginMethod` to `gateway`, they first remove it and `forceLoginGatewayUrl`. `forceLoginOrgUUID` limits this. `/status` in Claude Code shows a session that follows a gateway's own settings as `Cloud gateway`, and the **Allow sign-in from Claude Code in terminals and IDEs** switch doesn't stop it.
* **Signs in with their own Claude account**: Claude Code ends the organization sign-in and removes the stored copy of your settings. `forceLoginOrgUUID` limits this. On a computer that requires the sign-in, a claude.ai login still starts sessions on the Anthropic API, without your settings.
* **Changes how Claude Code starts on their own computer**: the sign-in keys are checked on the developer's computer. Sessions can run on the Anthropic API under another login, without your settings. `allowedProviders` without `"anthropic"` in the computer's managed settings limits this, if developers don't need direct access to the Anthropic API. Otherwise, only controls outside Claude Code limit this.
* **Sends Claude Code's traffic through their own proxy and certificate authority**: the proxy can answer in place of Anthropic, so Claude Code can accept settings that Anthropic didn't send. Only controls outside Claude Code limit this.
* **Runs `claude mcp serve`, which gives another program access to Claude Code's tools**: calls from that program skip your permission rules. The sandbox from **Allowed egress hosts** still applies. Only controls outside Claude Code limit this.
* **Sets `sandbox.filesystem.allowRead` in their own settings**: sandboxed commands can then read those paths, even if you deny them with `sandbox.filesystem.denyRead`, `Read` deny rules, or **Block reads outside working directories**. Claude's file tools still follow your `Read` deny rules and **Block reads outside working directories**. `sandbox.filesystem.allowManagedReadPathsOnly` set to `true` in the computer's managed settings stops this for `sandbox.filesystem.denyRead` and `Read` deny rules. The console can't set this key. Don't set it if you use **Block reads outside working directories**, because that setting then [doesn't reach sandboxed commands](https://code.claude.com/docs/en/settings-reference#sandboxed-commands-under-the-block).
* **Installs a plugin that contains a [mod](https://code.claude.com/docs/en/plugins/mods/overview), loads one with `--plugin-dir`, or has Claude write one**: the mod runs code as the developer. Your deny rules, **Disabled built-in tools**, and **Built-in tool policy** don't apply to actions of the mod itself. `allowManagedHooksOnly` set to `true` in your JSON limits this. It also stops developers' own hooks, and hooks and mods in plugins that developers add, including plugins from your **Plugin marketplaces**.
* **Runs an old version that doesn't have the organization sign-in**: it ignores your settings and `enforceAnthropicSignIn`. `requiredMinimumVersion` in the computer's managed settings limits this. Don't set it on a computer that also runs Claude Desktop on your provider.

The sign-in keys and your own settings have limits too:

* **`forceLoginOrgUUID`**: the check runs on the developer's computer and isn't a security boundary. It doesn't check the organization of a saved Claude Console key or an [Anthropic profile](https://code.claude.com/docs/en/authentication#anthropic-profiles-and-federation-credentials). Unless you also [require the sign-in](https://claude.com/docs/third-party/claude-desktop/admin-console-claude-code.md#require-the-sign-in-with-managed-settings), both still work on the Anthropic API, and a saved Claude Console key also works at an `ANTHROPIC_BASE_URL` that the developer sets.
* **`enforceAnthropicSignIn`**: it applies only when Claude Code can read the managed settings that set it. If you set no `forceLoginOrgUUID`, no session starts on a cloud provider or a custom base URL.
* **After a sign-in ends**: on a cloud provider that the developer or the computer set, most restrictions in the stored copy, though not `deniedModels`, stay in force until the developer runs `claude auth logout` in their terminal or signs in with another account
* **OpenTelemetry export**: a developer can still stop it on their own computer, for example with a very short export timeout. They can also change the identity that it sends.
* **Credential settings**: **AWS profile name**, **AWS config directory**, **GCP credentials file path**, and **Helper script** on your **Connection** page, and **OTLP headers helper script** on your **Telemetry & updates** page, can run a command on the developer's computer, in some cases without asking the developer. Give the Owner role, and any other access to the **Desktop 3P** pages, only to people you trust to run programs there.

To enforce budgets and rate limits and to log each model request, use an LLM gateway.
