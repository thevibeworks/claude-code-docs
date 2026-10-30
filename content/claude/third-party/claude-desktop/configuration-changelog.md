> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuration changelog

> Managed configuration keys by the Claude Desktop release they first shipped in

Configuration keys by Claude Desktop release. Each section lists keys added in that release, with the MDM key name (for plist/registry deployment) and the equivalent JSON shape (for local-file or bootstrap remote configuration).

**v4.4212.0**

2026-10-29

| MDM key | Type | Description |
| - | - | - |
| [`skillScanningEnabled`](https://claude.com/docs/third-party/claude-desktop/configuration#skillscanningenabled) · Beta | `boolean` | Scan user-created skills |
| [`projectsEnabled`](https://claude.com/docs/third-party/claude-desktop/configuration#projectsenabled) | `boolean` | Allow projects |
| [`sessionStatusLine`](https://claude.com/docs/third-party/claude-desktop/configuration#sessionstatusline) | `object` | Status line |

**JSON (e.g. for non-MDM users or Bootstrap):**

```json theme={null}
{
  "workspace": {
    "skillScanningEnabled": "<boolean>",
    "projectsEnabled": "<boolean>"
  },
  "appearance": {
    "sessionStatusLine": {
      "command": "<string>"
    }
  }
}
```

**Changed:**

* **Breaking:** `desktopHome`: at launches after 12:00 PM PT (20:00 UTC) on November 10, 2026, an unset key reads as `standard`: Unified Claude opens with Cowork on, even where `coworkTabEnabled` is `false`. In 4.29, an unset key did so only where Cowork was on. `chatTabEnabled` and `chatAdvancedFileAnalysisEnabled` have no effect under `standard`.
* `sshClientPath`: on Windows, a value may begin with `%LOCALAPPDATA%\`, which the app reads as the signed-in user's own local app data folder. It counts only when machine-wide policy (HKLM) itself sets it as a plain string (REG\_SZ), with `sshTransport: system-openssh` set by an administrator, and only while Claude does not run with administrator rights. Otherwise SSH sessions do not connect. Where a configuration server is in use, it must repeat this value and `sshTransport`, or the device's values are not used. The user can replace a program in that folder, so with such a value that user can get around this key and `sshHostAllowlist`, and the program can see SSH passwords.

**v4.29.0**

2026-10-27

| MDM key | Type | Description |
| - | - | - |
| [`inferenceTokenWarningPercent`](https://claude.com/docs/third-party/claude-desktop/configuration#inferencetokenwarningpercent) | `integer` | Token limit warning |

**JSON (e.g. for non-MDM users or Bootstrap):**

```json theme={null}
{
  "appearance": {
    "tokenLimitWarningPercent": "<integer>"
  }
}
```

**Changed:**

* `desktopHome`: from November 10, 2026 (12:00 PM PT, by the device's clock), an unset key opens Unified Claude at the app's next launch. With Cowork on, it reads as `standard`, under which `chatTabEnabled` and `chatAdvancedFileAnalysisEnabled` have no effect. A deployment with Cowork on that sets `chatSessionRetentionDays`, and does not set `coworkSessionRetentionDays` to the same number of days, keeps its current view. Earlier releases are unchanged.
* `inferenceModels`: an entry accepts `behavesAs`, the Claude model behind a Model ID that Claude Desktop cannot identify, such as a gateway alias. The ID then gets that model's effort levels and limits. Once any entry sets it, sessions that Claude Desktop starts no longer read a person's own `modelPicker` setting from Claude Code's settings.
* `managedMcpServers`: a remote entry accepts `defaultState`. Set it to `"off"` and the connector stays out of each person's sessions until they turn it on under Connectors in the + menu. Adding `"off"` to a connector in use turns it off for everyone who has not switched it on.
* `managedMcpServers`: a remote entry's `oauth` accepts `omitResource`. Set it to `true` when the identity provider rejects the OAuth `resource` parameter (Microsoft Entra ID: AADSTS9010010). It needs the entry's client ID, a scope that names the API, and exactly one sign-in server: a tenant ID, one authorization server, or an authorization URL and token URL. Otherwise the server is not loaded.
* `managedMcpServers`: a local, remote or web search entry accepts `platformOverrides`, which gives it a different command, arguments, environment or helper on Windows, macOS or Linux. A setting left out keeps the entry's own. A mistake under any operating system drops the server on every device. Earlier releases use the entry's own settings on every device.
* `managedMcpServers`: a local or remote entry accepts `toolTimeoutSec`, how many seconds (5 to 3,600) Claude waits for one tool call to that server, in place of `mcpToolTimeoutSec` for that server.
* `managedMcpServers` with `server: "github"`: `pull_request_review_write` now asks before every call whatever `toolPolicy` says, and is refused where Claude can show no prompt. `toolPolicy` can still block it. The connector is updated to github-mcp-server v2.0.2, whose new tools that make changes ask before every call unless `toolPolicy` allows them by name or with `"*"`.
* `managedMcpServers` with `server: "microsoft365"`: each user's saved sign-in is now kept per `tenantId`, `clientId`, `azureCloud` and `continuousAccessEvaluation`, so a change to any of them starts users from a fresh sign-in. Users who had connected sign in again once after this update.

**v3.6556.2**

2026-10-22

No configuration changes in this release.

**v3.6556.1**

2026-10-22

| MDM key | Type | Description |
| - | - | - |
| [`installedUpdateEnforcementEnabled`](https://claude.com/docs/third-party/claude-desktop/configuration#installedupdateenforcementenabled) | `boolean` | Restart to apply installed updates |
| [`installedUpdateEnforcementHours`](https://claude.com/docs/third-party/claude-desktop/configuration#installedupdateenforcementhours) | `integer` | Installed-update enforcement window |
| [`quickEntryScreenshotsEnabled`](https://claude.com/docs/third-party/claude-desktop/configuration#quickentryscreenshotsenabled) | `boolean` | Allow screenshots of the screen and other apps |
| [`quickEntryFileSharingEnabled`](https://claude.com/docs/third-party/claude-desktop/configuration#quickentryfilesharingenabled) | `boolean` | Allow sharing files open in other apps |

**JSON (e.g. for non-MDM users or Bootstrap):**

```json theme={null}
{
  "autoUpdate": {
    "installedUpdateEnforcement": {
      "enabled": "<boolean>",
      "enforcementHours": "<integer>"
    }
  },
  "workspace": {
    "quickEntry": {
      "screenshotsEnabled": "<boolean>",
      "fileSharingEnabled": "<boolean>"
    }
  }
}
```

**Changed:**

* A `managedMcpServers` entry accepts `headersHelperArgs` (remote and web search entries) or `envHelperArgs` (local entries): arguments for its helper script. Its helpers, `oauth.clientSecretHelper` included, also get the entry's `name` in `CLAUDE_CODE_MCP_SERVER_NAME`. Earlier releases ignore the lists and run the helper with no arguments.
* `allowedPluginMarketplaces`: moving an entry to a new source keeps its installed plugins when the new entry's `expectedName`, set in the same change, is the old marketplace's name. Plugins that the marketplace takes from another repository are still uninstalled.
* `allowedWorkspaceFolders` on SSH hosts: an entry is left out, and allows nothing, unless it is a full path for that host with no `..` (`~/work`, not `work`; on Windows `C:\work`, not `\work`). A symbolic link listed inside another listed folder is left out too: list the folder it points to.
* `allowedWorkspaceFolders`: a read-only entry whose `%VAR%` is unset or unsupported on a device (any `%VAR%` on an SSH host) now makes the folder holding the variable read-only (`~/Work` for `~/Work/%X%/a`; every allowed folder if the entry starts with it) instead of being ignored. A variable that only another operating system sets (`%APPDATA%` on macOS or on an SSH host) still leaves the entry without effect there.
* `disableAutoUpdates`: when a newer version is installed while Claude is open, the app now offers to relaunch into it (macOS, Linux, and the MSIX package on Windows).
* `managedMcpServers` with `server: "github"`: nine more write tools, among them `issue_write`, `pull_request_review_write` and `label_write`, now ask before every call. A `toolPolicy` key with a tool's exact name, or `"*"`, can still allow them. `actions_run_trigger` now asks before every call whatever `toolPolicy` says, and `toolPolicy` can still block it.
* `sshClientPath` (beta) on Windows accepts Git for Windows' `ssh.exe` or another OpenSSH 8.5 or newer under Program Files, where device management, or the bootstrap server it names, sets the key and also sets `sshTransport` to `system-openssh`.
* `updateViaUpdatesHost`: where `bootstrapUrl` is on `config.claude.com` and `bootstrapEnabled` is not off, update checks use `releases.claude.com` whatever this key says. Earlier releases do so only with the key on.

**v3.1623.4**

2026-10-22

**Changed:**

* `isLocalDevMcpEnabled` set to `false`, and `allowedPluginMcpServers`: a local MCP server from Claude Code's `managed-mcp.json` that uses `${VAR}` only in its `env` values now runs. One with a variable in its command or arguments is still stopped.

**v3.1623.1**

2026-10-21

No configuration changes in this release.

**v3.1623.0**

2026-10-20

| MDM key | Type | Description |
| - | - | - |
| [`releaseChannel`](https://claude.com/docs/third-party/claude-desktop/configuration#releasechannel) | `enum` | Release channel |
| [`quickEntryDefaultShortcut`](https://claude.com/docs/third-party/claude-desktop/configuration#quickentrydefaultshortcut) | `string` | Default Quick Entry shortcut |

**JSON (e.g. for non-MDM users or Bootstrap):**

```json theme={null}
{
  "autoUpdate": {
    "releaseChannel": "<stable|staggered>"
  },
  "workspace": {
    "quickEntryDefaultShortcut": "<string>"
  }
}
```

**Changed:**

* A remote or local `managedMcpServers` entry accepts an `icon` value: a PNG or JPEG as a base64 `data:` URI of at most 4,096 characters. Any other non-blank value is ignored, with a configuration warning. Earlier releases ignore `icon` and keep the entry.
* `builtinToolPolicy` accepts every built-in tool name this release's Claude Code publishes, such as `CronCreate` or `LSP`. An earlier release drops each name it does not know with a configuration error and, if none is left, asks before each tool it knows.
* `isLocalDevMcpEnabled`: `false` now also stops local MCP servers from plugins (your organization's marketplaces included, not the org-plugins directory), from Claude Code's `managed-mcp.json` if they use `${VAR}`, and in Code from Claude Code's own configuration files.
* `relaunchEnforcementHours`: no waiting period when a device-management profile that sets more than the app-behavior keys first applies to an app that started without one, and the app will run on that profile after restarting.
* `sshHostAllowlist` (beta): a session's jump hosts (`ProxyJump`, or a `ProxyCommand` written `ssh -W %h:%p host`) must now be on the list too, by `HostName`.

**v2.42304.2**

2026-10-19

No configuration changes in this release.

**v2.42304.0**

2026-10-15

**Changed:**

* `chatAdvancedFileAnalysisEnabled` and `coworkEgressAllowedHosts`: commands in Chat's file-analysis sandbox can now reach the listed hosts. With no list, or an empty one, they have no network access.
* `mcpPersistentAlwaysAllowEnabled`: `false` now also applies to Code sessions on the device, in WSL and over SSH.
* `claudeAiImport.automatic3pImport` now also reinstalls, without asking, the optional plugins that a user had switched on from any optional `allowedPluginMarketplaces` entry with the same source in the old and new organization.

**v2.37337.1**

2026-10-13

| MDM key | Type | Description |
| - | - | - |
| [`developerModeEnabled`](https://claude.com/docs/third-party/claude-desktop/configuration#developermodeenabled) | `boolean` | Allow Developer Mode |

**JSON (e.g. for non-MDM users or Bootstrap):**

```json theme={null}
{
  "workspace": {
    "developerModeEnabled": "<boolean>"
  }
}
```

**Changed:**

* `coworkEgressAllowedHosts`: your inference provider's, gateway's, and OTLP collector's hosts and `api.anthropic.com` are no longer added automatically. List them if tools call them.
* `managedMcpServers[].toolPolicy`: a value other than `allow`, `ask`, or `blocked` now blocks that tool, and a `toolPolicy` that is not a map of tool names blocks every tool. The entry is kept, with a configuration error, instead of being dropped.
* `sshTransport` (beta): a value that cannot be read now counts as `builtin`.
* `disableNonessentialServices` no longer turns off Chart.js, Grid.js, and Mermaid in artifacts, which now come with the app.
* `modelCatalogEnabled`: with `false`, picker names, descriptions, and effort options now come from the catalog bundled with the app.
* `coworkTabEnabled`: with `false`, Cowork tasks now stay listed in the sidebar and open read-only instead of disappearing.
* `disabledBuiltinTools`: a `WebFetch` or bare `Bash` entry added by device management now also applies to open Cowork and Chat conversations, and a tool name spelled with underscores or hyphens raises a configuration warning.

**Removed:**

The former key names below are now unrecognized keys: the setting no longer applies and the deprecation notice no longer appears. This replaces what the v1.40609.0 entry says these names do after the cut-off.

* `isDxtEnabled`: use `isDesktopExtensionEnabled` instead. Until then extensions are off on third-party deployments and allowed on standard deployments.
* `isDxtSignatureRequired`: use `isDesktopExtensionSignatureRequired` instead. Until then unsigned extensions load.
* `enduserAttribution`: use `endUserAttribution` instead. Until then end-user attribution is on. In the Windows registry, where names ignore case, the former name still reads as `endUserAttribution`.
* `trustBootstrapLocalExec`: use `trustBootstrapDelivery` instead. Until then a `bootstrapUrl` set by device management (on Windows, machine policy only) is trusted without asking each user, and any other `bootstrapUrl` asks each user.
* `inferenceGatewayHeaders`: use `inferenceCustomHeaders` instead. Until then no custom inference headers are sent.
* The deprecation notices for these spellings, which stopped being accepted on October 7, 2026 and are listed under v1.40609.0: header maps written as a string or list, `inferenceGatewayAuthScheme: "auto"`, `ask-session`, the older `managedMcpServers` entry forms, and the `orgPluginSettings` record form. Such a value is now reported like any other invalid value.

**v2.31226.1**

2026-10-09

No configuration changes in this release.

**v2.31226.0**

2026-10-08

| MDM key | Type | Description |
| - | - | - |
| [`otlpAttrMaxChars`](https://claude.com/docs/third-party/claude-desktop/configuration#otlpattrmaxchars) | `integer` | Telemetry attribute length limit |
| [`desktopHome`](https://claude.com/docs/third-party/claude-desktop/configuration#desktophome) | `enum` | Desktop home |

**JSON (e.g. for non-MDM users or Bootstrap):**

```json theme={null}
{
  "otlp": {
    "attrMaxChars": "<integer>"
  },
  "chatSurface": {
    "desktopHome": "<standard|off>"
  }
}
```

**Changed:**

* `allowedWorkspaceFolders`: in SSH sessions Claude's file tools can no longer modify a folder marked `ro`, as in a local Code session. Not enforced on Windows hosts, or on a host with Claude Code managed settings of its own (unless they set `parentSettingsBehavior` to `merge`).
* `claudeAiImport.automatic3pImport` now also brings over Cowork artifacts, projects, memory and global instructions, scheduled tasks from Cowork and Code, uploaded plugins (unless `userPluginUploadsEnabled` is off), saved skills (unless `skillCreationEnabled` is off) and the optional plugins a user had on from the organization's plugins directory or a marketplace served from its gateway's or bootstrap server's own address, also on computers that moved under an earlier release.
* `inferenceModels[].prefer1m` and `modelPrefer1mContext` now show one model picker entry for each model that offers 1M and has the preference, and start its new sessions at 1M, whichever entry a user had picked. Earlier releases only moved the starting selection of the first model.

**v2.26454.2**

2026-10-07

No configuration changes in this release.

**v2.26454.0**

2026-10-06

| MDM key | Type | Description |
| - | - | - |
| [`microsoftAuthDefaultAccount`](https://claude.com/docs/third-party/claude-desktop/configuration#microsoftauthdefaultaccount) | `enum` | Microsoft 365 sign-in with the Windows account |

**JSON (e.g. for non-MDM users or Bootstrap):**

```json theme={null}
{
  "authentication": {
    "microsoftAuthDefaultAccount": "<enabled|disabled>"
  }
}
```

**Changed:**

* `claudeAiImport` accepts a new `allowedOrganizationUuids` value, a list of Claude.ai organization IDs: when set, users can import history only by signing in to Claude.ai, and only from an organization on the list; a sign-in to any other organization or to a personal account is refused, and importing from a file or from earlier sessions on this computer is turned off. The list turns nothing on by itself, and `automatic3pImport` is not affected. Earlier releases ignore the list and keep allowing every import they allowed before, so the list limits imports only on devices running this release or later.
* `disableAutoUpdates` now also decides when Cowork's workspace is downloaded: in the background, instead of at the first task, unless it is `true`.

**Deprecated** (no end date has been set; this release and later keep reading the original spelling):

* `inferenceGatewayAuthScheme: "sso"`: use `inferenceCredentialKind: "interactive"` instead. If `inferenceCredentialKind` is not set, this release and later keep reading the original spelling as `inferenceCredentialKind: "interactive"` after October 7, 2026. Earlier releases stop reading it on that date, as announced under v1.40609.0.

**v2.19675.1**

2026-10-05

**Changed:**

* `allowedWorkspaceFolders`, when set, now also limits which of a project's folders a chat can read: only those inside a listed folder.

**v2.19675.0**

2026-10-01

No configuration changes in this release.

**v2.16120.0**

2026-09-29

| MDM key | Type | Description |
| - | - | - |
| [`deniedPluginMcpServers`](https://claude.com/docs/third-party/claude-desktop/configuration#deniedpluginmcpservers) | `object[]` | Blocked plugin MCP servers |

**JSON (e.g. for non-MDM users or Bootstrap):**

```json theme={null}
{
  "mcp": {
    "deniedPluginServers": [
      {
        "serverUrl": "<string>"
      }
    ]
  }
}
```

**Changed:**

* `userPluginMarketplacesEnabled`: when set to `false`, plugin marketplaces your organization did not provision are now hidden in every tab, installs and updates from them are refused, and the sessions the app starts load plugins only from your organization's marketplaces, the organization plugins directory, the app's own uploads and the user's own skills folder; nothing is deleted, and removing the key or setting it to `true` restores them. Earlier releases only blocked adding marketplaces, so on devices where the key is already `false`, plugins from marketplaces users added before stop loading once the app updates.

**v2.9939.4**

2026-09-27

No configuration changes in this release.

**v2.9939.2**

2026-09-24

**Changed:**

* `autoModeEnabled` no longer defaults to `false`. Left unset, the Code tab offers Auto mode and new Code tab sessions start in it where the model supports it; `true` does the same and also offers it in Cowork (Cowork sessions still start by asking before each action); `false` removes it from both tabs. Earlier releases treat an unset key as `false`, so Auto mode stays off on devices that have not updated.
* `inferenceIdpOidc` and `inferenceGatewayOidc`: `resource` accepts, besides a web address, an identifier with a scheme of its own that is not a web address, such as an AD FS relying-party identifier (`urn:…`), which is sent to the identity provider exactly as written; a value with no scheme is still sent as `https://<value>`. Earlier releases accept only a web address here and ignore the whole sign-in object, not just `resource`, when it carries such an identifier, so deploy one only once every device has updated.

**v2.7032.0**

2026-09-22

| MDM key | Type | Description |
| - | - | - |
| [`inferenceIdpAuthFlow`](https://claude.com/docs/third-party/claude-desktop/configuration#inferenceidpauthflow) | `enum` | Identity provider sign-in flow |
| [`inferenceIdpOidc`](https://claude.com/docs/third-party/claude-desktop/configuration#inferenceidpoidc) | `object` | Identity provider (OIDC) |
| [`mcpScheduledTaskApprovalLifetimeDays`](https://claude.com/docs/third-party/claude-desktop/configuration#mcpscheduledtaskapprovallifetimedays) | `integer` | Scheduled-task tool approval lifetime |
| [`keepAwakeEnabled`](https://claude.com/docs/third-party/claude-desktop/configuration#keepawakeenabled) | `boolean` | Allow keep awake |

**Set in the Claude admin console only:**

* [`disableLocalConfigCache`](https://claude.com/docs/third-party/claude-desktop/configuration#disablelocalconfigcache) — Keep only your organization ID and restrictions on disk

**JSON (e.g. for non-MDM users or Bootstrap):**

```json theme={null}
{
  "inference": {
    "credential": {
      "authFlow": "<browser|broker>",
      "oidc": {
        "clientId": "<string>",
        "issuer": "<string>",
        "authorizationUrl": "<string>",
        "tokenUrl": "<string>",
        "bearerTokenType": "<id_token|access_token>",
        "scopes": "<string>",
        "appendOfflineAccess": "<boolean>",
        "resource": "<string>",
        "redirectPort": "<integer>",
        "redirectHost": "<127.0.0.1|localhost>",
        "additionalRedirectReferrerHosts": "<string>"
      }
    }
  },
  "mcp": {
    "scheduledTaskApprovalLifetimeDays": "<integer>"
  },
  "workspace": {
    "keepAwakeEnabled": "<boolean>"
  }
}
```

**Changed:**

* `inferenceCredentialKind` accepts `external-idp` for the gateway and Bedrock providers: users sign in through your organization's OpenID Connect identity provider (`inferenceIdpOidc`, `inferenceIdpAuthFlow`) and the token is sent as the Bearer credential, on Bedrock to a token-validating proxy at `inferenceBedrockBaseUrl`, which that kind requires.

**Deprecated** (no end date has been set; the original spellings keep working):

* `inferenceCredentialKind: "interactive"` together with `inferenceGatewayOidc` (gateway): use `"external-idp"` instead once every desktop in the fleet is on 2.7032.0 or later; 2.7032.0 and later read the original spelling as `"external-idp"`.
* `inferenceGatewayOidc`: use `inferenceIdpOidc` with `inferenceCredentialKind: "external-idp"` instead, once every desktop in the fleet is on 2.7032.0 or later.
* `inferenceGatewayOidcAuthFlow`: use `inferenceIdpAuthFlow` together with `inferenceIdpOidc` instead, once every desktop in the fleet is on 2.7032.0 or later.

**v2.2553.13**

2026-09-21

No configuration changes in this release.

**v2.2553.1**

2026-09-18

No configuration changes in this release.

**v2.2553.0**

2026-09-17

| MDM key | Type | Description |
| - | - | - |
| [`inferenceCredentialHelperWindows`](https://claude.com/docs/third-party/claude-desktop/configuration#inferencecredentialhelperwindows) | `string` | Helper script (Windows) |
| [`allowedPluginMcpServers`](https://claude.com/docs/third-party/claude-desktop/configuration#allowedpluginmcpservers) | `object[]` | Allowed plugin MCP servers |
| [`builtinBrowserEnabled`](https://claude.com/docs/third-party/claude-desktop/configuration#builtinbrowserenabled) | `boolean` | Allow the built-in browser |
| [`builtinBrowserDefaultDomainPolicy`](https://claude.com/docs/third-party/claude-desktop/configuration#builtinbrowserdefaultdomainpolicy) | `enum` | Default site policy in the built-in browser |
| [`builtinBrowserAllowedDomains`](https://claude.com/docs/third-party/claude-desktop/configuration#builtinbrowseralloweddomains) | `string[]` | Allowed sites in the built-in browser |
| [`builtinBrowserBlockedDomains`](https://claude.com/docs/third-party/claude-desktop/configuration#builtinbrowserblockeddomains) | `string[]` | Blocked sites in the built-in browser |

**JSON (e.g. for non-MDM users or Bootstrap):**

```json theme={null}
{
  "inference": {
    "credential": {
      "commandWindows": "<string>"
    }
  },
  "mcp": {
    "allowedPluginServers": [
      {
        "serverUrl": "<string>"
      }
    ]
  },
  "builtinBrowser": {
    "enabled": "<boolean>",
    "defaultDomainPolicy": "<allow|block>",
    "allowedDomains": ["<string>"],
    "blockedDomains": ["<string>"]
  }
}
```

**Changed:**

* `inferenceFoundryResource` now requires the user's consent when delivered by a bootstrap URL the user configured themselves (`consentRequired`), as `inferenceFoundryBaseUrl` and the other providers' endpoint settings already do; declining quits the app, and because the resource name is required each such Foundry install prompts once after updating. A bootstrap URL set by device management, or covered by `trustBootstrapDelivery: true`, never prompts, and values delivered by MDM are unchanged. Earlier releases apply a served value without asking.

**v2.110.0**

2026-09-15

| MDM key | Type | Description |
| - | - | - |
| [`inferenceCredentialHelperArgs`](https://claude.com/docs/third-party/claude-desktop/configuration#inferencecredentialhelperargs) | `string[]` | Helper script arguments |
| [`inferenceFoundryBaseUrl`](https://claude.com/docs/third-party/claude-desktop/configuration#inferencefoundrybaseurl) | `string` | Azure AI Foundry base URL |
| [`defaultModelEffort`](https://claude.com/docs/third-party/claude-desktop/configuration#defaultmodeleffort) | `enum` | Default model effort |
| [`alwaysStartWithDefaultModel`](https://claude.com/docs/third-party/claude-desktop/configuration#alwaysstartwithdefaultmodel) | `boolean` | Always start with the default model |
| [`modelCatalogEnabled`](https://claude.com/docs/third-party/claude-desktop/configuration#modelcatalogenabled) | `boolean` | Model catalog metadata |
| [`modelCatalogUrl`](https://claude.com/docs/third-party/claude-desktop/configuration#modelcatalogurl) | `string` | Model catalog URL |
| [`scheduledTasksEnabled`](https://claude.com/docs/third-party/claude-desktop/configuration#scheduledtasksenabled) | `boolean` | Allow scheduled tasks |

**JSON (e.g. for non-MDM users or Bootstrap):**

```json theme={null}
{
  "inference": {
    "credential": {
      "args": ["<string>"]
    },
    "baseUrl": "<string>"
  },
  "models": {
    "defaultEffort": "<low|medium|high|xhigh|max>",
    "alwaysStartWithDefault": "<boolean>",
    "catalogEnabled": "<boolean>",
    "catalogUrl": "<string>"
  },
  "workspace": {
    "scheduledTasksEnabled": "<boolean>"
  }
}
```

**Changed:**

* `bootstrapOidc`, `inferenceGatewayOidc`, and `inferenceVertexWorkforceOidc` accept a new `redirectHost` value, `127.0.0.1` (the default) or `localhost`, which sets the host named in the browser sign-in's redirect URI (`http://<host>:<port>/callback`) for identity providers that only accept `localhost`; register exactly the URI you use. Earlier releases ignore the value and keep using `http://127.0.0.1:<port>/callback`, so a `localhost`-only registration still fails sign-in on them until they update.
* An `inferenceModels` entry accepts a new `maxEffort` value (`low`, `medium`, `high`, `xhigh`, or `max`): effort levels above it are hidden for that model in Chat, Cowork, and Code and never requested, and Code sessions are held to it; an unrecognized value caps that model at `low`. Earlier releases ignore the value and keep offering every effort level, so the cap holds only on devices running this release or later.
* A `managedMcpServers` entry accepts a new `transport` value, `policy-only`: the entry sets `toolPolicy` for an MCP server that an installed plugin provides, matched by `name`, without the app connecting to or launching anything, and takes precedence over `orgPluginSettings` for that server in Chat, Cowork, and Code. Earlier releases drop a `policy-only` entry (it appears under Configuration parse errors in the diagnostic report) and apply `orgPluginSettings` to that server instead; if every entry in the list is `policy-only` they cannot read `managedMcpServers` at all and, until they update, leave MCP servers that users added themselves or that a project's `.mcp.json` declares out of Code sessions. Keep the same permissions in `orgPluginSettings` while earlier releases are in use, and do not deploy a list made only of `policy-only` entries until every device has updated.

**v1.52386.6**

2026-09-13

No configuration changes in this release.

**v1.52386.3**

2026-09-11

No configuration changes in this release.

**v1.52386.0**

2026-09-10

| MDM key | Type | Description |
| - | - | - |
| [`sshTransport`](https://claude.com/docs/third-party/claude-desktop/configuration#sshtransport) · Beta | `enum` | SSH connection engine |
| [`chatSessionRetentionDays`](https://claude.com/docs/third-party/claude-desktop/configuration#chatsessionretentiondays) | `integer` | Chat retention period |
| [`coworkSessionRetentionDays`](https://claude.com/docs/third-party/claude-desktop/configuration#coworksessionretentiondays) | `integer` | Cowork retention period |
| [`codeSessionRetentionDays`](https://claude.com/docs/third-party/claude-desktop/configuration#codesessionretentiondays) | `integer` | Code retention period |
| [`sessionRetentionHold`](https://claude.com/docs/third-party/claude-desktop/configuration#sessionretentionhold) | `boolean` | Suspend session deletion |
| [`coworkVmIpv6Enabled`](https://claude.com/docs/third-party/claude-desktop/configuration#coworkvmipv6enabled) | `boolean` | Enable IPv6 in the workspace VM |

**JSON (e.g. for non-MDM users or Bootstrap):**

```json theme={null}
{
  "codeSurface": {
    "sshTransport": "<auto|system-openssh|builtin>"
  },
  "sessionRetention": {
    "chatDays": "<integer>",
    "coworkDays": "<integer>",
    "codeDays": "<integer>",
    "legalHold": "<boolean>"
  },
  "workspace": {
    "vmIpv6Enabled": "<boolean>"
  }
}
```

**v1.49585.0**

2026-09-08

**Changed:**

* `managedMcpServers`: the built-in Microsoft 365 server entry (`"server": "microsoft365"`) accepts a new `continuousAccessEvaluation` value, `enabled` (the default) or `disabled`. When enabled, the bundled connector requests Continuous Access Evaluation-capable Microsoft Graph tokens, which live up to about 28 hours but are cut off within minutes when an administrator revokes sessions or disables the account, or, where the tenant enforces a location or compliant-network Conditional Access policy, when the token is used from outside that network; `disabled` keeps standard one-hour tokens. A change applies to tokens issued after the connector next starts.
* `microsoftAuthBroker` accepts a new `required` value: Microsoft 365 sign-in fails when the OS sign-in broker (WAM on Windows, the Company Portal SSO extension on macOS) is unavailable instead of falling back to the browser, so the refresh token stays broker-held, and the connector removes the token cache an earlier browser sign-in left on disk. Linux has no broker, so `required` is not supported there. Earlier releases treat `required` as `disabled` (browser-only sign-in), so deploy it once every device is on this release or later.

**v1.46388.4**

2026-09-05

No configuration changes in this release.

**v1.46388.3**

2026-09-04

No configuration changes in this release.

**v1.46388.2**

2026-09-04

No configuration changes in this release.

**v1.46388.1**

2026-09-04

| MDM key | Type | Description |
| - | - | - |
| [`sshClientPath`](https://claude.com/docs/third-party/claude-desktop/configuration#sshclientpath) · Beta | `string` | SSH client program |
| [`configRecheckIntervalMinutes`](https://claude.com/docs/third-party/claude-desktop/configuration#configrecheckintervalminutes) | `integer` | Configuration re-check interval |
| [`disableBypassPermissionsMode`](https://claude.com/docs/third-party/claude-desktop/configuration#disablebypasspermissionsmode) | `boolean` | Disable bypass permissions mode |
| [`blockReadsOutsideWorkingDirectories`](https://claude.com/docs/third-party/claude-desktop/configuration#blockreadsoutsideworkingdirectories) | `boolean` | Block reads outside working directories |

**JSON (e.g. for non-MDM users or Bootstrap):**

```json theme={null}
{
  "codeSurface": {
    "sshClientPath": "<string>"
  },
  "lifecycle": {
    "configRecheckIntervalMinutes": "<integer>"
  },
  "workspace": {
    "disableBypassPermissionsMode": "<boolean>",
    "blockReadsOutsideWorkingDirectories": "<boolean>"
  }
}
```

**Changed:**

* **Breaking:** `relaunchEnforcementHours` moved in the nested served format from `bootstrap.relaunchEnforcementHours` to `lifecycle.relaunchEnforcementHours` (beside the new `lifecycle.configRecheckIntervalMinutes`). This release no longer reads the old path and earlier releases do not read the new one, so move the value under `lifecycle`; the MDM / flat key name `relaunchEnforcementHours` is unchanged. The key can now also be set from device management (availability MDM and served), and the default when no tier sets it is 24 hours (was 1).

**v1.44121.4**

2026-09-02

No configuration changes in this release.

**v1.44121.2**

2026-09-02

No configuration changes in this release.

**v1.44121.1**

2026-09-02

| MDM key | Type | Description |
| - | - | - |
| [`inferenceStreamIdleTimeoutSec`](https://claude.com/docs/third-party/claude-desktop/configuration#inferencestreamidletimeoutsec) | `integer` | Stream idle timeout |
| [`egressProxyUrl`](https://claude.com/docs/third-party/claude-desktop/configuration#egressproxyurl) | `string` | Proxy server URL |
| [`egressProxyPacUrl`](https://claude.com/docs/third-party/claude-desktop/configuration#egressproxypacurl) | `string` | Proxy auto-config (PAC) URL |
| [`claudeAiImport.automatic3pImport`](https://claude.com/docs/third-party/claude-desktop/configuration#claudeaiimport) | `boolean` | New subfield (beta): when `true` and `deploymentOrganizationUuid` is set, the app copies this computer's earlier third-party sessions stored before an organization ID was configured into that organization's session store, once per device and in the background; independent of `enabled` (default `false`). |

**JSON (e.g. for non-MDM users or Bootstrap):**

```json theme={null}
{
  "inference": {
    "streamIdleTimeoutSec": "<integer>"
  },
  "workspace": {
    "egressProxyUrl": "<string>",
    "egressProxyPacUrl": "<string>"
  },
  "claudeAiImport": {
    "automatic3pImport": "<boolean>"
  }
}
```

`egressProxyUrl` and `egressProxyPacUrl` are read from device management or a local configuration file only; a value served by a bootstrap URL is not applied.

**Changed:**

* **Breaking:** `inferenceModelPricingMultiplier` and `inferenceModelPricing` no longer turn on the Usage page's cost estimate by themselves; they apply only while `inferenceModelPricingEnabled` is `true` and are ignored otherwise. A configuration that sets either without `inferenceModelPricingEnabled: true` now shows token counts only; add that key to keep the estimate.

**v1.40609.1**

2026-08-30

No configuration changes in this release.

**v1.40609.0**

2026-08-27

| MDM key | Type | Description |
| - | - | - |
| [`sshHostAllowlist`](https://claude.com/docs/third-party/claude-desktop/configuration#sshhostallowlist) · Beta | `string[]` | SSH host allowlist |
| [`disableConfigDeprecationWarnings`](https://claude.com/docs/third-party/claude-desktop/configuration#disableconfigdeprecationwarnings) | `boolean` | Hide configuration deprecation warnings |

**JSON (e.g. for non-MDM users or Bootstrap):**

```json theme={null}
{
  "codeSurface": {
    "sshHostAllowlist": ["<string>"]
  },
  "bootstrap": {
    "relaunchEnforcementHours": "<integer>"
  },
  "appearance": {
    "disableConfigDeprecationWarnings": "<boolean>"
  }
}
```

`relaunchEnforcementHours` is read from served configuration only (a bootstrap URL); a value in a local configuration file or in device management is ignored with a warning.

**Changed:**

* `inferenceVertexProjectId` and `inferenceVertexWorkforceUserProject` now require the user's consent when delivered by a bootstrap URL the user configured themselves (`consentRequired`); a bootstrap URL set by device management, or covered by `trustBootstrapDelivery: true`, never prompts. Both keys must match the Google Cloud project format (`^[a-z0-9][a-z0-9.:-]*$`).
* `inferenceCredentialKind` accepts `interactive` for Vertex AI (Google sign-in); the Vertex `oauth` value is deprecated (below).
* `orgPluginSettings` is published as an array of `{ "serverName", "tools": [{ "toolName", "permission" }] }` entries; the `{ "mcpServers": {…} }` record form is deprecated (below).
* The published bootstrap JSON schema now rejects `authorityHost` on the Microsoft 365 entry, so a configuration that still uses it fails schema validation in tools that check against the schema; the app itself keeps mapping it to `azureCloud` until October 7, 2026.
* `allowedPluginMarketplaces` is no longer marked Beta.

**Deprecated** (each accepted until October 7, 2026, 12:00 PM Pacific Time; users see an in-app warning from September 10, 2026, which `disableConfigDeprecationWarnings` hides, and a final reminder in the 24 hours before the cut-off, which it does not):

* `inferenceGatewayHeaders`: use `inferenceCustomHeaders` instead. After the cut-off no custom inference headers are sent.
* `inferenceCustomHeaders`, `otlpHeaders`, `otlpResourceAttributes` and `bootstrapHeaders` written as a `"Name=value,…"` string or a `["Name: value", …]` list: use a JSON object such as `{"Name": "value"}` instead. After the cut-off a string or list value is rejected as malformed and no headers (or resource attributes) are sent.
* `inferenceGatewayAuthScheme: "sso"`: use `inferenceCredentialKind: "interactive"` instead. After the cut-off the value is reported as invalid and, unless another credential field says how to sign in, the gateway connection has no credential and inference does not start.
* `inferenceGatewayAuthScheme: "auto"`: use `"bearer"` instead, or remove the key (`bearer` is the default). After the cut-off the value is reported as invalid and the default applies.
* `inferenceCredentialKind: "oauth"` (Vertex AI): use `"interactive"` instead. After the cut-off `oauth` is reported as invalid and the kind is derived from the credential fields present.
* `inferenceCredentialKind: "interactive"` together with `inferenceVertexWorkforceAudience` (Vertex AI): use `"workforce"` instead, or remove the audience if Google sign-in is meant. After the cut-off the audience no longer implies Workforce Identity; `interactive` then needs `inferenceVertexOAuthClientId` or inference does not start.
* `isDxtEnabled` and `isDxtSignatureRequired`: use `isDesktopExtensionEnabled` and `isDesktopExtensionSignatureRequired` instead. After the cut-off the old names are unreadable: extensions are disabled, or only signed extensions load, until the name is updated.
* `trustBootstrapLocalExec`: use `trustBootstrapDelivery` instead. After the cut-off the key reads `false` and each user is asked to consent to bootstrap-delivered values.
* `enduserAttribution`: use `endUserAttribution` instead. After the cut-off the key reads `false` and end-user attribution stays off.
* `orgPluginSettings` as a `{ "mcpServers": {…} }` record: use the array form instead (read by desktop 1.15200.0 and later; older desktops ignore the array and enforce no tool locks). After the cut-off the record is rejected and every plugin-delivered MCP tool is blocked until the value is rewritten.
* `ask-session` in `builtinToolPolicy`, `orgPluginSettings[].tools[].permission` and `managedMcpServers[].toolPolicy`: use `ask` instead. After the cut-off it is treated as an unrecognized value: `ask` for a built-in tool, `blocked` for a plugin-delivered tool, and an invalid entry for a managed server.
* In `managedMcpServers` entries: replace `scopes` with `scope` (one space-separated string); remove `transport: "builtin"` and `source`; replace `authorityHost` with `azureCloud: "us-gov-high"` for a GCC High tenant; write `oauth` as `true` or an oauth object rather than a number or string; replace `oauth.scopes` (or `oauth.scope` as a list) with `oauth.scope` as one string; add `transport: "http"` (or `"sse"` / `"stdio"`) to an entry with no `transport` that is not a built-in server (a built-in Microsoft 365 or GitHub entry takes no `transport`). After the cut-off such an entry is rejected and that connector is unavailable until it is rewritten (`source` is ignored by the desktop but refused by a customer-run Apps Gateway).

**v1.37937.3**

2026-08-26

No configuration changes in this release.

**v1.37937.2**

2026-08-26

No configuration changes in this release.

**v1.37937.1**

2026-08-25

No configuration changes in this release.

**v1.37937.0**

2026-08-25

| MDM key | Type | Description |
| - | - | - |
| [`inferenceModelPricingEnabled`](https://claude.com/docs/third-party/claude-desktop/configuration#inferencemodelpricingenabled) | `boolean` | Show estimated cost |
| [`inferenceModelPricingMultiplier`](https://claude.com/docs/third-party/claude-desktop/configuration#inferencemodelpricingmultiplier) | `number` | Price multiplier |
| [`inferenceModelPricing`](https://claude.com/docs/third-party/claude-desktop/configuration#inferencemodelpricing) | `object[]` | Model pricing |
| [`userPluginMarketplacesEnabled`](https://claude.com/docs/third-party/claude-desktop/configuration#userpluginmarketplacesenabled) | `boolean` | Allow user-added plugin marketplaces |
| [`userPluginUploadsEnabled`](https://claude.com/docs/third-party/claude-desktop/configuration#userpluginuploadsenabled) | `boolean` | Allow user-added plugins |
| [`mcpToolTimeoutSec`](https://claude.com/docs/third-party/claude-desktop/configuration#mcptooltimeoutsec) | `integer` | MCP tool call timeout |
| [`skipWebFetchPreflight`](https://claude.com/docs/third-party/claude-desktop/configuration#skipwebfetchpreflight) | `boolean` | Skip WebFetch domain check |
| [`organizationInstructions`](https://claude.com/docs/third-party/claude-desktop/configuration#organizationinstructions) | `string` | Organization instructions |

**JSON (e.g. for non-MDM users or Bootstrap):**

```json theme={null}
{
  "models": {
    "pricing": {
      "enabled": "<boolean>",
      "multiplier": "<number>",
      "models": [
        {
          "name": "<string>",
          "inputPerMtok": "<number>",
          "outputPerMtok": "<number>",
          "cacheReadPerMtok": "<number>",
          "cacheWritePerMtok": "<number>"
        }
      ]
    }
  },
  "plugins": {
    "userPluginMarketplacesEnabled": "<boolean>",
    "userPluginUploadsEnabled": "<boolean>"
  },
  "mcp": {
    "toolTimeoutSec": "<integer>"
  },
  "workspace": {
    "skipWebFetchPreflight": "<boolean>",
    "organizationInstructions": "<string>"
  }
}
```

**Changed:**

* `builtinToolPolicy` accepts argument-scoped Claude Code permission rules such as `Bash(curl *)` or `Edit(**/*.env)` as keys, in addition to bare tool names; `WebSearch` and `WebFetch` take the bare name only, and a key that is not a usable rule is dropped with a configuration error. Deploy argument-scoped entries once your whole fleet is on this release: an older build drops an argument-scoped `ask` entry as an unknown tool, so that tool runs without a prompt.

**v1.34493.1**

2026-08-21

No configuration changes in this release.

**v1.34493.0**

2026-08-20

No configuration changes in this release.

**v1.32885.1**

2026-08-18

| MDM key | Type | Description |
| - | - | - |
| [`bootstrapHeaders`](https://claude.com/docs/third-party/claude-desktop/configuration#bootstrapheaders) | `object` | Bootstrap request headers |
| [`bootstrapHeadersHelper`](https://claude.com/docs/third-party/claude-desktop/configuration#bootstrapheadershelper) | `string` | Bootstrap headers helper script |

**JSON (e.g. for non-MDM users or Bootstrap):**

```json theme={null}
{
  "bootstrap": {
    "headers": "<object>",
    "headersHelper": "<string>"
  }
}
```

**Changed:**

* `managedMcpServers[].oauth` accepts a new `mode` value, `hosted`: the app signs in to that MCP server with an Anthropic-hosted client identity (Anthropic vouches for the client on each token request) instead of a client you register yourself, pinned to the exact issuer URL(s) you list in `authorizationServer`; it requires the Claude.ai sign-in and is available once the hosted signer is enabled for your organization.

**v1.32352.1**

2026-08-18

No configuration changes in this release.

**v1.32352.0**

2026-08-17

| MDM key | Type | Description |
| - | - | - |
| [`claudeAiImport.exportEnabled`](https://claude.com/docs/third-party/claude-desktop/configuration#claudeaiimport) | `boolean` | New subfield: lets users export this computer's chats, Cowork tasks, and Code sessions from Settings > Import & export as a zip that another install can import; no effect unless `enabled` is `true` (default `false`). |
| [`allowedPluginMarketplaces[].manifestSha256`](https://claude.com/docs/third-party/claude-desktop/configuration#allowedpluginmarketplaces) | `string` | New subfield (beta): SHA-256 of the exact hosted `marketplace.json` a `url` marketplace may serve; required when `installationPreference` is `auto_install` or `required`, and a served manifest with any other digest is refused. |

**JSON (e.g. for non-MDM users or Bootstrap):**

```json theme={null}
{
  "claudeAiImport": {
    "exportEnabled": "<boolean>"
  },
  "plugins": {
    "marketplaces": [
      {
        "source": "url",
        "url": "<string>",
        "manifestSha256": "<string>",
        "credentialKind": "<anonymous|userGit|credentialHelper|inferenceCredential>"
      }
    ]
  }
}
```

**Changed:**

* **Breaking:** Managed-config URL settings now reject values that embed credentials (`https://user:password@host…`). Configurations that relied on this fail to load until the credentials are removed; use `bootstrapHeaders` / `bootstrapHeadersHelper` (available from 1.32885.1) to send authentication instead.
* `allowedPluginMarketplaces[].source` (beta) accepts a new `url` value: a hosted `marketplace.json` whose plugins are zip archives, fetched over HTTPS with no git on the device; set `url` to the manifest address (`repo`, `ref`, and `path` do not apply).
* `allowedPluginMarketplaces[].credentialKind` (beta) accepts a new `inferenceCredential` value, for `url` marketplaces on the inference gateway's own origin: fetches carry the same bearer credential the app already sends the gateway for inference.

**v1.30096.5**

2026-08-14

No configuration changes in this release.

**v1.30096.1**

2026-08-13

| MDM key | Type | Description |
| - | - | - |
| [`otlpAuthMode`](https://claude.com/docs/third-party/claude-desktop/configuration#otlpauthmode) | `enum` | Collector authentication |
| [`otlpHeadersHelper`](https://claude.com/docs/third-party/claude-desktop/configuration#otlpheadershelper) | `string` | OpenTelemetry headers helper script |
| [`inferenceGatewayOidc.resource`](https://claude.com/docs/third-party/claude-desktop/configuration#inferencegatewayoidc) | `string` | New subfield: RFC 8707 resource indicator sent on gateway sign-in and token refresh so the IdP audience-restricts the access token to the gateway; leave unset for Microsoft Entra ID. |

**JSON (e.g. for non-MDM users or Bootstrap):**

```json theme={null}
{
  "otlp": {
    "authMode": "<none|inference-credential>",
    "headersHelper": "<string>"
  },
  "inference": {
    "credential": {
      "oidc": {
        "resource": "<string>"
      }
    }
  }
}
```

**Changed:**

* `inferenceBedrockBaseUrl` and `inferenceVertexBaseUrl`: only affects users who entered the bootstrap server URL themselves (in Settings or a local config file). Those users are now asked once to allow a Bedrock or Vertex endpoint that server delivers (and again if it changes) before it takes effect, the same `trustBootstrapDelivery` consent prompt `inferenceGatewayBaseUrl` already shows; the provider's default endpoint is used until they allow it. Managed deployments (bootstrap URL set by device management, or `trustBootstrapDelivery: true`) see no change.

**v1.28929.0**

2026-08-11

| MDM key | Type | Description |
| - | - | - |
| [`modelPrefer1mContext`](https://claude.com/docs/third-party/claude-desktop/configuration#modelprefer1mcontext) | `boolean` | Default to 1M context |
| [`claudeAiImport.enabled`](https://claude.com/docs/third-party/claude-desktop/configuration#claudeaiimport) | `boolean` | New subfield: turns history import on; the banner and import actions stay off until set to `true` (default `false`). |
| [`claudeAiImport.bannerBehavior`](https://claude.com/docs/third-party/claude-desktop/configuration#claudeaiimport) | `enum` | New subfield: when the import banner appears: `off` (default), `detect`, or `show`. |

**JSON (e.g. for non-MDM users or Bootstrap):**

```json theme={null}
{
  "models": {
    "prefer1mContext": "<boolean>"
  },
  "claudeAiImport": {
    "enabled": "<boolean>",
    "bannerBehavior": "<off|detect|show>"
  }
}
```

**Changed:**

* `inferenceGatewayBaseUrl` delivered by a bootstrap server now goes through the `trustBootstrapDelivery` consent prompt: unless the bootstrap URL came from device management or `trustBootstrapDelivery` is `true`, each user is asked once to allow the address, and again if it changes, before it takes effect.

**v1.26832.0**

2026-08-06

| MDM key | Type | Description |
| - | - | - |
| [`updateViaUpdatesHost`](https://claude.com/docs/third-party/claude-desktop/configuration#updateviaupdateshost) | `boolean` | Check for updates on releases.claude.com |
| [`allowedWorkspaceFolders[].mode`](https://claude.com/docs/third-party/claude-desktop/configuration#allowedworkspacefolders) | `enum` | New subfield: `ro` makes the folder read-only in Cowork; Code enforces file tools only. |

**JSON (e.g. for non-MDM users or Bootstrap):**

```json theme={null}
{
  "autoUpdate": {
    "viaUpdatesHost": "<boolean>"
  }
}
```

`trustBootstrapLocalExec` was renamed to `trustBootstrapDelivery`; the previous name is still accepted.

**v1.25927.0**

2026-08-04

| MDM key | Type | Description |
| - | - | - |
| [`inferenceGatewayOidcAuthFlow`](https://claude.com/docs/third-party/claude-desktop/configuration#inferencegatewayoidcauthflow) | `enum` | Gateway sign-in flow |
| [`inferenceVertexWorkforceAuthFlow`](https://claude.com/docs/third-party/claude-desktop/configuration#inferencevertexworkforceauthflow) | `enum` | Workforce Identity sign-in flow |
| [`trustBootstrapLocalExec`](https://claude.com/docs/third-party/claude-desktop/configuration#trustbootstrapdelivery) | `boolean` | Trust bootstrap-delivered local commands |
| [`skillCreationEnabled`](https://claude.com/docs/third-party/claude-desktop/configuration#skillcreationenabled) | `boolean` | Allow user-created skills |

**JSON (e.g. for non-MDM users or Bootstrap):**

```json theme={null}
{
  "inference": {
    "credential": {
      "authFlow": "<browser|broker>"
    }
  },
  "bootstrap": {
    "trustBootstrapLocalExec": "<boolean>"
  },
  "workspace": {
    "skillCreationEnabled": "<boolean>"
  }
}
```

**Changed:**

* `claudeAiImport`, `deploymentDisplayName`, and `deploymentDisplaySubtitle` now accept values from MDM and a local configuration file as well as a bootstrap server, and `disableDeepLinkRegistration`, `microsoftAuthBroker`, `userContentRendererUrl`, `inferenceFoundryTenantId`, `inferenceFoundryClientId`, `inferenceCredentialHelper` (with its TTL, timeout, and silent-refresh keys), `inferenceBedrockProfile`, `inferenceBedrockAwsDir`, `inferenceBedrockAwsCliPath`, and `inferenceVertexCredentialsFile` can now be delivered by a bootstrap server. The keys that name a local executable go through the `trustBootstrapLocalExec` consent prompt.
* `managedMcpServers` gains a built-in `github` server: set `server` to `github` and supply your own GitHub OAuth app client ID with the device flow enabled. The new `host`, `toolsets`, and `readOnly` subfields point the connector at a GitHub Enterprise Server instance, choose which toolsets load, and offer read tools only.
* `managedMcpServers[].oauth.authFlow` is a new subfield that lets a managed connector sign in through the operating system's Microsoft Entra account broker on Windows and macOS, so Conditional Access policies that require a managed device no longer block it. Devices without a broker keep using browser sign-in.
* `enduserAttribution` is renamed to the corrected spelling `endUserAttribution`. The previous spelling is still accepted and now records a configuration warning.
* `organizationPluginsUrl` is deprecated and removed from the configuration reference. The key is still honored, but organization plugins are better configured with `allowedPluginMarketplaces`.

**v1.24012.11**

2026-08-03

No configuration changes in this release.

**v1.24012.9**

2026-07-24

| MDM key | Type | Description |
| - | - | - |
| [`mcpPersistentAlwaysAllowEnabled`](https://claude.com/docs/third-party/claude-desktop/configuration#mcppersistentalwaysallowenabled) | `boolean` | Allow persistent tool approvals |

**JSON (e.g. for non-MDM users or Bootstrap):**

```json theme={null}
{
  "mcp": {
    "persistentAlwaysAllowEnabled": "<boolean>"
  }
}
```

**v1.24012.0**

2026-07-21

| MDM key | Type | Description |
| - | - | - |
| [`enduserAttribution`](https://claude.com/docs/third-party/claude-desktop/configuration#enduserattribution) | `boolean` | End-user attribution |
| [`userContentRendererUrl`](https://claude.com/docs/third-party/claude-desktop/configuration#usercontentrendererurl) | `string` | Artifact preview iframe origin |

**JSON (e.g. for non-MDM users or Bootstrap):**

```json theme={null}
{
  "deploymentDisplayName": "<string>",
  "deploymentDisplaySubtitle": "<string>",
  "enduserAttribution": "<boolean>",
  "userContentRendererUrl": "<string>"
}
```

**v1.22209.3**

2026-07-19

No configuration changes in this release.

**v1.22209.0**

2026-07-16

| MDM key | Type | Description |
| - | - | - |
| [`otlpTracesEnabled`](https://claude.com/docs/third-party/claude-desktop/configuration#otlptracesenabled) | `boolean` | Export traces (beta) |

**JSON (e.g. for non-MDM users or Bootstrap):**

```json theme={null}
{
  "otlp": {
    "tracesEnabled": "<boolean>"
  }
}
```

**v1.21459.3**

2026-07-16

No configuration changes in this release.

**v1.21459.0**

2026-07-14

| MDM key | Type | Description |
| - | - | - |
| [`disableFeatureDiscovery`](https://claude.com/docs/third-party/claude-desktop/configuration#disablefeaturediscovery) | `boolean` | Hide feature announcements |
| [`inferenceModels[].prefer1m`](https://claude.com/docs/third-party/claude-desktop/configuration#inferencemodels) | `boolean` | New subfield: make the 1M-context variant the default picker selection when this model is the default entry. |
| [`managedMcpServers[].envHelper`](https://claude.com/docs/third-party/claude-desktop/configuration#managedmcpservers) | `string` | New subfield: helper executable that prints environment variables as JSON for a managed stdio server. |
| [`managedMcpServers[].envHelperTtlSec`](https://claude.com/docs/third-party/claude-desktop/configuration#managedmcpservers) | `integer` | New subfield: maximum age in seconds of a cached `envHelper` result (default 300). |
| [`managedMcpServers[].headersHelperRefreshBufferSec`](https://claude.com/docs/third-party/claude-desktop/configuration#managedmcpservers) | `integer` | New subfield: how many seconds before credential expiry the `headersHelper` re-runs (default 60). |
| [`toolSearchEnabled`](https://claude.com/docs/third-party/claude-desktop/configuration#toolsearchenabled) | `boolean` | Enable tool search |

**JSON (e.g. for non-MDM users or Bootstrap):**

```json theme={null}
{
  "featureDiscovery": {
    "disabled": "<boolean>"
  },
  "workspace": {
    "toolSearchEnabled": "<boolean>"
  }
}
```

**Changed:**

* `chatTabEnabled` and `chatAdvancedFileAnalysisEnabled` are no longer Beta: the Chat tab and advanced file analysis are generally available. Availability and defaults are unchanged, and both remain opt-in.
* `orgPluginSettings[].tools.permission` accepts a new `ask-session` value. In this release the value is accepted but behaves as `ask` (a prompt on every use); the once-per-session approval flow is not yet enabled.

**v1.20186.9**

2026-07-14

No configuration changes in this release.

**v1.20186.0**

2026-07-09

No configuration changes in this release.

**v1.19367.0**

2026-07-07

| MDM key | Type | Description |
| - | - | - |
| [`inferenceFoundryAuthFlow`](https://claude.com/docs/third-party/claude-desktop/configuration#inferencefoundryauthflow) | `enum` | Entra ID sign-in flow |
| [`microsoftAuthBroker`](https://claude.com/docs/third-party/claude-desktop/configuration#microsoftauthbroker) | `enum` | Microsoft 365 native sign-in broker |
| [`managedMcpServers[].startupTimeoutSec`](https://claude.com/docs/third-party/claude-desktop/configuration#managedmcpservers) | `integer` | New subfield: maximum wait in seconds for the server to start and list its tools. |

**JSON (e.g. for non-MDM users or Bootstrap):**

```json theme={null}
{
  "inference": {
    "credential": {
      "authFlow": "<device-code|browser>"
    }
  },
  "authentication": {
    "microsoftAuthBroker": "<auto|disabled>"
  }
}
```

**Changed:**

* `isDesktopExtensionEnabled` — default changed from `true` to `false`: Desktop Extensions (`.dxt`, `.mcpb`) no longer load unless explicitly enabled.
* `allowedPluginMarketplaces` (beta) — can now be delivered per-user through the bootstrap server; previously MDM-only.

**v1.18286.2**

2026-07-07

No configuration changes in this release.

**v1.18286.0**

2026-07-02

**Removed:**

* `disableDefaultPlugins` — third-party deployments always skip the default plugin marketplaces and standard deployments always include them, so the key no longer has an effect.

**v1.17377.2**

2026-07-01

No configuration changes in this release.

**v1.17377.1**

2026-06-30

| MDM key | Type | Description |
| - | - | - |
| [`allowedPluginMarketplaces`](https://claude.com/docs/third-party/claude-desktop/configuration#allowedpluginmarketplaces) | `object[]` | Admin-configured plugin marketplace git URLs appear under the Directory's Organization tab. (MDM-only; not settable via bootstrap JSON.) |
| [`inferenceVertexWorkforceOidc.omitOfflineAccess`](https://claude.com/docs/third-party/claude-desktop/configuration#inferencevertexworkforceoidc) | `boolean` | New subfield: omit `offline_access` from the OIDC scope request. |

**JSON (Non-MDM User, Bootstrap Remote):**

```json theme={null}
{
  "inference": {
    "credential": {
      "oidc": {
        "omitOfflineAccess": "<boolean>"
      }
    }
  }
}
```

**v1.15962.2**

2026-06-30

No configuration changes in this release.

**v1.15962.1**

2026-06-26

No configuration changes in this release.

**v1.15962.0**

2026-06-25

| MDM key | Type | Description |
| - | - | - |
| [`otlpContentCapture`](https://claude.com/docs/third-party/claude-desktop/configuration#otlpcontentcapture) | `enum[]` | Content capture categories |
| [`disableBundledSkills`](https://claude.com/docs/third-party/claude-desktop/configuration#disablebundledskills) | `boolean` | Disable bundled skills and workflows |
| [`managedMcpServers[].server`](https://claude.com/docs/third-party/claude-desktop/configuration#managedmcpservers) | `enum` | Gained `"websearch"` — managed web search (Brave, Tavily, Exa or custom) |

**JSON (Non-MDM User, Bootstrap Remote):**

```json theme={null}
{
  "otlp": {
    "contentCapture": [
      "<userPrompts|assistantResponses|toolDetails|toolContent|rawApiBodies>"
    ]
  },
  "workspace": {
    "disableBundledSkills": "<boolean>"
  },
  "mcp": {
    "managedServers": [
      {
        "name": "Web search",
        "server": "websearch",
        "provider": "<brave|tavily|exa|custom>",
        "headers": { "<header-name>": "<string>" },
        "customUrl": "<string, provider=custom only>"
      }
    ]
  }
}
```

**v1.15200.0**

2026-06-23

No configuration changes in this release.

**v1.14271.0**

2026-06-18

| MDM key | Type | Description |
| - | - | - |
| `chatAdvancedFileAnalysisEnabled` | `boolean` | Advanced file analysis |
| `inferenceSessionLifetimeSec` | `integer` | Sign-in session lifetime |

**JSON (Non-MDM User, Bootstrap Remote):**

```json theme={null}
{
  "chatSurface": {
    "advancedFileAnalysis": "<boolean>"
  },
  "inference": {
    "sessionLifetimeSec": "<integer>"
  }
}
```

**Deprecated:**

* `betaFeaturesEnabled` — Allow beta features (added and deprecated in this release)

**v1.13576.0**

2026-06-16

| MDM key | Type | Description |
| - | - | - |
| `chatTabEnabled` | `boolean` | Allow Chat tab |
| `inferenceBedrockAwsCliPath` | `string` | AWS CLI path |

**JSON (Non-MDM User, Bootstrap Remote):**

```json theme={null}
{
  "chatSurface": {
    "enabled": "<boolean>"
  },
  "inference": {
    "awsEnv": {
      "awsCliPath": "<string>"
    }
  }
}
```

**v1.12603.0**

2026-06-11

| MDM key | Type | Description |
| - | - | - |
| `inferenceVertexOAuthLoginHint` | `string` | Vertex OAuth login hint |

**JSON (Non-MDM User, Bootstrap Remote):**

```json theme={null}
{
  "inference": {
    "credential": {
      "loginHint": "<string>"
    }
  }
}
```

**v1.10628.0**

2026-06-02

| MDM key | Type | Description |
| - | - | - |
| `inferenceVertexWorkforceAudience` | `string` | Workforce Identity audience |
| `inferenceVertexWorkforceUserProject` | `string` | Workforce Identity billing project |
| `inferenceVertexWorkforceOidc` | `object` | Workforce Identity IdP (OIDC) |
| `organizationPluginsUrl` | `string` | Organization plugins endpoint |
| `autoModeEnabled` | `boolean` | Allow Auto mode |
| `inferenceCredentialHelperSilentRefreshEnabled` | `boolean` | Re-run helper for silent refresh |
| `bootstrapEnabled` | `boolean` | Use bootstrap config |
| `bootstrapUrl` | `string` | Bootstrap config URL |
| `bootstrapOidc` | `object` | Bootstrap OIDC parameters |

**JSON (Non-MDM User, Bootstrap Remote):**

```json theme={null}
{
  "inference": {
    "credential": {
      "audience": "<string>",
      "userProject": "<string>",
      "oidc": {
        "issuer": "<string>",
        "authorizationUrl": "<string>",
        "tokenUrl": "<string>",
        "clientId": "<string>",
        "scopes": "<string>",
        "redirectPort": "<integer>"
      },
      "silentRefreshEnabled": "<boolean>"
    }
  }
}
```

**v1.9659.0**

2026-05-27

| MDM key | Type | Description |
| - | - | - |
| `coworkTabEnabled` | `boolean` | Allow Cowork tab |

**JSON (Non-MDM User, Bootstrap Remote):**

```json theme={null}
{
  "coworkSurface": {
    "enabled": "<boolean>"
  }
}
```

**v1.9255.0**

2026-05-26

| MDM key | Type | Description |
| - | - | - |
| `otlpDesktopLogLevel` | `enum` | Desktop telemetry export level |
| `inferenceFoundryTenantId` | `string` | Entra ID tenant ID |
| `inferenceFoundryClientId` | `string` | Entra ID client ID |

**JSON (Non-MDM User, Bootstrap Remote):**

```json theme={null}
{
  "otlp": {
    "desktopLogLevel": "<off|error|warn|info|debug>"
  },
  "inference": {
    "credential": {
      "tenantId": "<string>",
      "clientId": "<string>"
    }
  }
}
```

**v1.8555.0**

2026-05-21

| MDM key | Type | Description |
| - | - | - |
| `inferenceCredentialKind` | `enum` | Credential kind |

**JSON (Non-MDM User, Bootstrap Remote):**

```json theme={null}
{
  "inference": {
    "credential": {
      "kind": "<static|helper-script|interactive|vendor-profile>"
    }
  }
}
```

**v1.8089.0**

2026-05-19

| MDM key | Type | Description |
| - | - | - |
| `inferenceAnthropicApiKey` | `string` | Claude API key |
| `inferenceCustomHeaders` | `object` | Custom inference headers (renamed from `inferenceGatewayHeaders`) |
| `modelDiscoveryEnabled` | `boolean` | Model discovery |
| `orgPluginSettings` | `object` | Organization plugin settings |
| `builtinToolPolicy` | `object` | Built-in tool policy |
| `inferenceCredentialHelperTimeoutSec` | `integer` | Credential helper timeout |

**JSON (Non-MDM User, Bootstrap Remote):**

```json theme={null}
{
  "inference": {
    "credential": {
      "apiKey": "<string>",
      "timeoutSec": "<integer>"
    },
    "customHeaders": "<object>"
  }
}
```

**v1.7196.0**

2026-05-12

| MDM key | Type | Description |
| - | - | - |
| `banner` | `object` | Organization banner |

**v1.6889.0**

2026-05-08

| MDM key | Type | Description |
| - | - | - |
| `disableDeepLinkRegistration` | `boolean` | Disable claude:// deep-link handling |
| `inferenceGatewayOidc` | `object` | Gateway SSO IdP (OIDC) |

**JSON (Non-MDM User, Bootstrap Remote):**

```json theme={null}
{
  "inference": {
    "credential": {
      "oidc": {
        "issuer": "<string>",
        "authorizationUrl": "<string>",
        "tokenUrl": "<string>",
        "clientId": "<string>",
        "scopes": "<string>",
        "redirectPort": "<integer>",
        "bearerTokenType": "<id_token|access_token>",
        "appendOfflineAccess": "<boolean>"
      }
    }
  }
}
```

**v1.6259.0**

2026-05-05

| MDM key | Type | Description |
| - | - | - |
| `inferenceBedrockSsoStartUrl` | `string` | AWS SSO start URL |
| `inferenceBedrockSsoRegion` | `string` | AWS SSO region |
| `inferenceBedrockSsoAccountId` | `string` | AWS SSO account ID |
| `inferenceBedrockSsoRoleName` | `string` | AWS SSO role name |

**JSON (Non-MDM User, Bootstrap Remote):**

```json theme={null}
{
  "inference": {
    "credential": {
      "ssoStartUrl": "<string>",
      "ssoRegion": "<string>",
      "ssoAccountId": "<string>",
      "ssoRoleName": "<string>"
    }
  }
}
```

**v1.5354.0**

2026-04-29

| MDM key | Type | Description |
| - | - | - |
| `otlpResourceAttributes` | `object` | OpenTelemetry resource attributes |

**JSON (Non-MDM User, Bootstrap Remote):**

```json theme={null}
{
  "otlp": {
    "resourceAttributes": "<object>"
  }
}
```

**v1.5186.0**

2026-04-28

| MDM key | Type | Description |
| - | - | - |
| `inferenceBedrockServiceTier` | `enum` | Bedrock service tier |

**JSON (Non-MDM User, Bootstrap Remote):**

```json theme={null}
{
  "inference": {
    "serviceTier": "<flex|priority>"
  }
}
```

**v1.3834.0**

2026-04-21

| MDM key | Type | Description |
| - | - | - |
| `disableDeploymentModeChooser` | `boolean` | Disable Claude.ai sign-in |

**v1.3036.0**

2026-04-16

| MDM key | Type | Description |
| - | - | - |
| `inferenceGatewayAuthScheme` | `enum` | Gateway auth scheme |

**JSON (Non-MDM User, Bootstrap Remote):**

```json theme={null}
{
  "inference": {
    "credential": {
      "authScheme": "<auto|x-api-key|bearer|sso>"
    }
  }
}
```

**Baseline**

| MDM key | Type | Description |
| - | - | - |
| `isDesktopExtensionEnabled` | `boolean` | Allow desktop extensions (renamed from `isDxtEnabled`) |
| `isDesktopExtensionSignatureRequired` | `boolean` | Require signed extensions (renamed from `isDxtSignatureRequired`) |
| `isLocalDevMcpEnabled` | `boolean` | Allow user-added MCP servers |
| `isClaudeCodeForDesktopEnabled` | `boolean` | Allow Claude Code tab |
| `coworkEgressAllowedHosts` | `array<string>` | Allowed egress hosts |
| `otlpEndpoint` | `string` | OpenTelemetry collector endpoint |
| `otlpProtocol` | `enum` | OpenTelemetry exporter protocol |
| `otlpHeaders` | `object` | OpenTelemetry exporter headers |
| `autoUpdaterEnforcementHours` | `integer` | Auto-update enforcement window |
| `disableAutoUpdates` | `boolean` | Block auto-updates |
| `inferenceProvider` | `enum` | Inference provider |
| `inferenceGatewayBaseUrl` | `string` | Gateway base URL |
| `inferenceGatewayApiKey` | `string` | Gateway API key |
| `inferenceVertexProjectId` | `string` | GCP project ID |
| `inferenceVertexRegion` | `string` | GCP region |
| `inferenceVertexCredentialsFile` | `string` | GCP credentials file path |
| `inferenceVertexOAuthClientId` | `string` | Vertex OAuth client ID |
| `inferenceVertexOAuthClientSecret` | `string` | Vertex OAuth client secret |
| `inferenceVertexOAuthScopes` | `string` | Vertex OAuth scopes |
| `inferenceVertexBaseUrl` | `string` | Vertex AI base URL |
| `inferenceBedrockRegion` | `string` | AWS region |
| `inferenceBedrockBearerToken` | `string` | AWS bearer token |
| `inferenceBedrockBaseUrl` | `string` | Bedrock base URL |
| `inferenceBedrockProfile` | `string` | AWS profile name |
| `inferenceBedrockAwsDir` | `string` | AWS config directory |
| `inferenceFoundryResource` | `string` | Azure AI Foundry resource name |
| `inferenceFoundryApiKey` | `string` | Azure AI Foundry API key |
| `inferenceModels` | `array<string\|object>` | Model list |
| `deploymentOrganizationUuid` | `string` | Organization UUID |
| `disableEssentialTelemetry` | `boolean` | Block essential telemetry |
| `disableNonessentialTelemetry` | `boolean` | Block nonessential telemetry |
| `disableNonessentialServices` | `boolean` | Block nonessential services |
| `managedMcpServers` | `array<object\|object\|object\|null>` | Managed MCP servers |
| `disabledBuiltinTools` | `array<string>` | Disabled built-in tools |
| `allowedWorkspaceFolders` | `array<string\|object>` | Allowed workspace folders |
| `inferenceCredentialHelper` | `string` | Helper script |
| `inferenceCredentialHelperTtlSec` | `integer` | Helper script TTL |
| `inferenceMaxTokensPerWindow` | `integer` | Max tokens per window |
| `inferenceTokenWindowHours` | `integer` | Token cap window |

**Deprecated:**

* `requireCoworkFullVmSandbox` — Require full VM sandbox
