> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuration reference

> Every managed-configuration key Claude Desktop on 3P supports, what it controls, and recommended security profiles

| Key | Name in the app | Category | Works with (Unless a label in its entry says otherwise, a key can be set in an MDM profile or the local configuration file, or returned from a bootstrap server. A badge marks another kind of deployment that the key also works with.) |
| - | - | - | - |
| [`inferenceProvider`](#inferenceprovider) | Inference provider | Connection | Admin Console |
| [`inferenceCredentialKind`](#inferencecredentialkind) | Credential kind | Connection | Self-hosted Admin Console |
| [`inferenceSessionLifetimeSec`](#inferencesessionlifetimesec) | Sign-in session lifetime | Connection | Admin Console |
| [`userContentRendererUrl`](#usercontentrendererurl) | Artifact preview iframe origin | Connection | Admin Console |
| [`inferenceCustomHeaders`](#inferencecustomheaders) | Custom inference headers | Connection | Self-hosted Admin Console |
| [`inferenceCredentialHelper`](#inferencecredentialhelper) | Helper script | Connection | Self-hosted Admin Console |
| [`inferenceCredentialHelperWindows`](#inferencecredentialhelperwindows) | Helper script (Windows) | Connection | Self-hosted Admin Console |
| [`inferenceCredentialHelperArgs`](#inferencecredentialhelperargs) | Helper script arguments | Connection | Self-hosted Admin Console |
| [`inferenceCredentialHelperTtlSec`](#inferencecredentialhelperttlsec) | Helper script TTL | Connection | Self-hosted Admin Console |
| [`inferenceCredentialHelperTimeoutSec`](#inferencecredentialhelpertimeoutsec) | Credential helper timeout | Connection | Self-hosted Admin Console |
| [`inferenceCredentialHelperSilentRefreshEnabled`](#inferencecredentialhelpersilentrefreshenabled) | Re-run helper for silent refresh | Connection | Self-hosted Admin Console |
| [`egressProxyUrl`](#egressproxyurl) | Proxy server URL | Connection | Self-hosted |
| [`egressProxyPacUrl`](#egressproxypacurl) | Proxy auto-config (PAC) URL | Connection | Self-hosted |
| [`coworkVmIpv6Enabled`](#coworkvmipv6enabled) | Enable IPv6 in the workspace VM | Connection | Admin Console |
| [`inferenceGatewayBaseUrl`](#inferencegatewaybaseurl) | Gateway base URL | Connection | Admin Console |
| [`inferenceGatewayApiKey`](#inferencegatewayapikey) | Gateway API key | Connection | |
| [`inferenceGatewayAuthScheme`](#inferencegatewayauthscheme) | Gateway auth scheme | Connection | Admin Console |
| [`inferenceGatewayOidcAuthFlow`](#inferencegatewayoidcauthflow) | Gateway sign-in flow | Connection | Admin Console |
| [`inferenceGatewayOidc`](#inferencegatewayoidc) | Gateway SSO IdP (OIDC) | Connection | Admin Console |
| [`inferenceIdpAuthFlow`](#inferenceidpauthflow) | Identity provider sign-in flow | Connection | Self-hosted Admin Console |
| [`inferenceIdpOidc`](#inferenceidpoidc) | Identity provider (OIDC) | Connection | Self-hosted Admin Console |
| [`inferenceStreamIdleTimeoutSec`](#inferencestreamidletimeoutsec) | Stream idle timeout | Connection | Self-hosted Admin Console |
| [`inferenceAnthropicApiKey`](#inferenceanthropicapikey) | Claude API key | Connection | |
| [`inferenceBedrockRegion`](#inferencebedrockregion) | AWS region | Connection | Admin Console |
| [`inferenceBedrockBaseUrl`](#inferencebedrockbaseurl) | Bedrock base URL | Connection | Admin Console |
| [`inferenceBedrockServiceTier`](#inferencebedrockservicetier) | Bedrock service tier | Connection | Admin Console |
| [`inferenceBedrockBearerToken`](#inferencebedrockbearertoken) | AWS bearer token | Connection | |
| [`inferenceBedrockSsoStartUrl`](#inferencebedrockssostarturl) | AWS SSO start URL | Connection | Admin Console |
| [`inferenceBedrockSsoRegion`](#inferencebedrockssoregion) | AWS SSO region | Connection | Admin Console |
| [`inferenceBedrockSsoAccountId`](#inferencebedrockssoaccountid) | AWS SSO account ID | Connection | Admin Console |
| [`inferenceBedrockSsoRoleName`](#inferencebedrockssorolename) | AWS SSO role name | Connection | Admin Console |
| [`inferenceBedrockProfile`](#inferencebedrockprofile) | AWS profile name | Connection | Admin Console |
| [`inferenceBedrockAwsDir`](#inferencebedrockawsdir) | AWS config directory | Connection | Admin Console |
| [`inferenceBedrockAwsCliPath`](#inferencebedrockawsclipath) | AWS CLI path | Connection | Admin Console |
| [`inferenceVertexProjectId`](#inferencevertexprojectid) | GCP project ID | Connection | Admin Console |
| [`inferenceVertexRegion`](#inferencevertexregion) | GCP region | Connection | Admin Console |
| [`inferenceVertexBaseUrl`](#inferencevertexbaseurl) | Vertex AI base URL | Connection | Admin Console |
| [`inferenceVertexOAuthClientId`](#inferencevertexoauthclientid) | Vertex OAuth client ID | Connection | Admin Console |
| [`inferenceVertexOAuthClientSecret`](#inferencevertexoauthclientsecret) | Vertex OAuth client secret | Connection | Admin Console |
| [`inferenceVertexOAuthScopes`](#inferencevertexoauthscopes) | Vertex OAuth scopes | Connection | Admin Console |
| [`inferenceVertexOAuthLoginHint`](#inferencevertexoauthloginhint) | Vertex OAuth login hint | Connection | Admin Console |
| [`inferenceVertexWorkforceAudience`](#inferencevertexworkforceaudience) | Workforce Identity audience | Connection | Admin Console |
| [`inferenceVertexWorkforceUserProject`](#inferencevertexworkforceuserproject) | Workforce Identity billing project | Connection | Admin Console |
| [`inferenceVertexWorkforceAuthFlow`](#inferencevertexworkforceauthflow) | Workforce Identity sign-in flow | Connection | Admin Console |
| [`inferenceVertexWorkforceOidc`](#inferencevertexworkforceoidc) | Workforce Identity IdP (OIDC) | Connection | Admin Console |
| [`inferenceVertexCredentialsFile`](#inferencevertexcredentialsfile) | GCP credentials file path | Connection | Admin Console |
| [`inferenceFoundryResource`](#inferencefoundryresource) | Azure AI Foundry resource name | Connection | Admin Console |
| [`inferenceFoundryBaseUrl`](#inferencefoundrybaseurl) | Azure AI Foundry base URL | Connection | Admin Console |
| [`inferenceFoundryApiKey`](#inferencefoundryapikey) | Azure AI Foundry API key | Connection | |
| [`inferenceFoundryTenantId`](#inferencefoundrytenantid) | Entra ID tenant ID | Connection | Admin Console |
| [`inferenceFoundryClientId`](#inferencefoundryclientid) | Entra ID client ID | Connection | Admin Console |
| [`inferenceFoundryAuthFlow`](#inferencefoundryauthflow) | Entra ID sign-in flow | Connection | Admin Console |
| [`modelDiscoveryEnabled`](#modeldiscoveryenabled) | Model discovery | Connection | Admin Console |
| [`modelPrefer1mContext`](#modelprefer1mcontext) | Use 1M wherever it’s available | Connection | Self-hosted Admin Console |
| [`inferenceModels`](#inferencemodels) | Model list | Connection | Self-hosted Admin Console |
| [`defaultModelEffort`](#defaultmodeleffort) | Default model effort | Connection | Self-hosted Admin Console |
| [`alwaysStartWithDefaultModel`](#alwaysstartwithdefaultmodel) | Always start with the default model | Connection | Self-hosted Admin Console |
| [`inferenceModelPricingEnabled`](#inferencemodelpricingenabled) | Show estimated cost | Connection | Self-hosted Admin Console |
| [`inferenceModelPricingMultiplier`](#inferencemodelpricingmultiplier) | Price multiplier | Connection | Self-hosted Admin Console |
| [`inferenceModelPricing`](#inferencemodelpricing) | Model pricing | Connection | Self-hosted Admin Console |
| [`modelCatalogEnabled`](#modelcatalogenabled) | Model catalog metadata | Connection | Self-hosted |
| [`modelCatalogUrl`](#modelcatalogurl) | Model catalog URL | Connection | Self-hosted |
| [`coworkTabEnabled`](#coworktabenabled) | Allow Cowork | Capabilities | Admin Console |
| [`isClaudeCodeForDesktopEnabled`](#isclaudecodefordesktopenabled) | Allow Code | Capabilities | Self-hosted Admin Console |
| [`sshHostAllowlist`](#sshhostallowlist) | SSH host allowlist | Capabilities | Admin Console |
| [`sshClientPath`](#sshclientpath) | SSH client program | Capabilities | Admin Console |
| [`sshTransport`](#sshtransport) | SSH connection engine | Capabilities | Admin Console |
| [`chatTabEnabled`](#chattabenabled) | Allow Chat | Capabilities | Admin Console |
| [`desktopHome`](#desktophome) | Desktop home | Capabilities | Self-hosted Admin Console |
| [`chatAdvancedFileAnalysisEnabled`](#chatadvancedfileanalysisenabled) | Advanced file analysis | Capabilities | Admin Console |
| [`coworkEgressAllowedHosts`](#coworkegressallowedhosts) | Allowed egress hosts | Capabilities | Self-hosted Admin Console |
| [`allowedWorkspaceFolders`](#allowedworkspacefolders) | Allowed workspace folders | Capabilities | Self-hosted Admin Console |
| [`blockReadsOutsideWorkingDirectories`](#blockreadsoutsideworkingdirectories) | Block reads outside working directories | Capabilities | Self-hosted Admin Console |
| [`autoModeEnabled`](#automodeenabled) | Allow Auto mode | Capabilities | Self-hosted Admin Console |
| [`disableBypassPermissionsMode`](#disablebypasspermissionsmode) | Disable bypass permissions mode | Capabilities | Admin Console |
| [`disableBundledSkills`](#disablebundledskills) | Disable bundled skills and workflows | Capabilities | Self-hosted Admin Console |
| [`skillCreationEnabled`](#skillcreationenabled) | Allow user-created skills | Capabilities | Self-hosted Admin Console |
| [`userPluginMarketplacesEnabled`](#userpluginmarketplacesenabled) | Allow user-added plugin marketplaces | Capabilities | Self-hosted Admin Console |
| [`userPluginUploadsEnabled`](#userpluginuploadsenabled) | Allow user-added plugins | Capabilities | Self-hosted Admin Console |
| [`scheduledTasksEnabled`](#scheduledtasksenabled) | Allow scheduled tasks | Capabilities | Self-hosted Admin Console |
| [`keepAwakeEnabled`](#keepawakeenabled) | Allow keep awake | Capabilities | Self-hosted Admin Console |
| [`developerModeEnabled`](#developermodeenabled) | Allow Developer Mode | Capabilities | Self-hosted Admin Console |
| [`quickEntryDefaultShortcut`](#quickentrydefaultshortcut) | Default Quick Entry shortcut | Capabilities | Self-hosted Admin Console |
| [`quickEntryScreenshotsEnabled`](#quickentryscreenshotsenabled) | Allow screenshots of the screen and other apps | Capabilities | Self-hosted Admin Console |
| [`quickEntryFileSharingEnabled`](#quickentryfilesharingenabled) | Allow sharing files open in other apps | Capabilities | Self-hosted Admin Console |
| [`skipWebFetchPreflight`](#skipwebfetchpreflight) | Skip WebFetch domain check | Capabilities | Admin Console |
| [`builtinToolPolicy`](#builtintoolpolicy) | Built-in tool policy | Capabilities | Self-hosted Admin Console |
| [`disabledBuiltinTools`](#disabledbuiltintools) | Disabled built-in tools | Capabilities | Self-hosted Admin Console |
| [`toolSearchEnabled`](#toolsearchenabled) | Enable tool search | Capabilities | Self-hosted Admin Console |
| [`organizationInstructions`](#organizationinstructions) | Organization instructions | Capabilities | Self-hosted Admin Console |
| [`requireCoworkFullVmSandbox`](#requirecoworkfullvmsandbox) | Require full VM sandbox | Capabilities | |
| [`disableDeploymentModeChooser`](#disabledeploymentmodechooser) | Disable Claude.ai sign-in | Capabilities | Self-hosted |
| [`disableDeepLinkRegistration`](#disabledeeplinkregistration) | Disable claude:// deep-link handling | Capabilities | Self-hosted Admin Console |
| [`builtinBrowserEnabled`](#builtinbrowserenabled) | Allow the built-in browser | Capabilities | Admin Console |
| [`builtinBrowserDefaultDomainPolicy`](#builtinbrowserdefaultdomainpolicy) | Default site policy in the built-in browser | Capabilities | Admin Console |
| [`builtinBrowserAllowedDomains`](#builtinbrowseralloweddomains) | Allowed sites in the built-in browser | Capabilities | Admin Console |
| [`builtinBrowserBlockedDomains`](#builtinbrowserblockeddomains) | Blocked sites in the built-in browser | Capabilities | Admin Console |
| [`claudeAiImport`](#claudeaiimport) | Claude.ai data import | Capabilities | Self-hosted Admin Console |
| [`managedMcpServers`](#managedmcpservers) | Managed MCP servers | Connectors | Self-hosted Admin Console |
| [`mcpPersistentAlwaysAllowEnabled`](#mcppersistentalwaysallowenabled) | Allow persistent tool approvals | Connectors | Self-hosted Admin Console |
| [`mcpScheduledTaskApprovalLifetimeDays`](#mcpscheduledtaskapprovallifetimedays) | Scheduled-task tool approval lifetime | Connectors | Self-hosted Admin Console |
| [`isLocalDevMcpEnabled`](#islocaldevmcpenabled) | Allow local MCP servers | Connectors | Self-hosted Admin Console |
| [`allowedPluginMcpServers`](#allowedpluginmcpservers) | Allowed plugin MCP servers | Connectors | Self-hosted Admin Console |
| [`deniedPluginMcpServers`](#deniedpluginmcpservers) | Blocked plugin MCP servers | Connectors | Self-hosted Admin Console |
| [`mcpToolTimeoutSec`](#mcptooltimeoutsec) | MCP tool call timeout | Connectors | Self-hosted Admin Console |
| [`microsoftAuthBroker`](#microsoftauthbroker) | Microsoft 365 native sign-in broker | Connectors | Admin Console |
| [`microsoftAuthDefaultAccount`](#microsoftauthdefaultaccount) | Microsoft 365 sign-in with the Windows account | Connectors | Admin Console |
| [`isDesktopExtensionEnabled`](#isdesktopextensionenabled) | Allow desktop extensions | Connectors | Admin Console |
| [`isDesktopExtensionSignatureRequired`](#isdesktopextensionsignaturerequired) | Require signed extensions | Connectors | Admin Console |
| [`deploymentOrganizationUuid`](#deploymentorganizationuuid) | Organization UUID | Telemetry & updates | Self-hosted Admin Console |
| [`disableEssentialTelemetry`](#disableessentialtelemetry) | Block essential telemetry | Telemetry & updates | Self-hosted Admin Console |
| [`disableNonessentialTelemetry`](#disablenonessentialtelemetry) | Block nonessential telemetry | Telemetry & updates | Self-hosted Admin Console |
| [`disableNonessentialServices`](#disablenonessentialservices) | Block nonessential services | Telemetry & updates | Self-hosted Admin Console |
| [`otlpEndpoint`](#otlpendpoint) | OTLP endpoint | Telemetry & updates | Admin Console |
| [`otlpProtocol`](#otlpprotocol) | OTLP protocol | Telemetry & updates | Admin Console |
| [`otlpHeaders`](#otlpheaders) | OTLP headers | Telemetry & updates | Admin Console |
| [`otlpAuthMode`](#otlpauthmode) | Collector authentication | Telemetry & updates | Admin Console |
| [`otlpHeadersHelper`](#otlpheadershelper) | OTLP headers helper script | Telemetry & updates | Admin Console |
| [`otlpResourceAttributes`](#otlpresourceattributes) | Resource attributes | Telemetry & updates | Self-hosted Admin Console |
| [`otlpDesktopLogLevel`](#otlpdesktoploglevel) | Desktop telemetry export level | Telemetry & updates | Self-hosted Admin Console |
| [`otlpContentCapture`](#otlpcontentcapture) | Content capture | Telemetry & updates | Self-hosted Admin Console |
| [`otlpTracesEnabled`](#otlptracesenabled) | Export traces | Telemetry & updates | Self-hosted Admin Console |
| [`otlpAttrMaxChars`](#otlpattrmaxchars) | Telemetry attribute length limit | Telemetry & updates | Self-hosted Admin Console |
| [`disableAutoUpdates`](#disableautoupdates) | Block auto-updates | Telemetry & updates | Self-hosted Admin Console |
| [`installedUpdateEnforcementEnabled`](#installedupdateenforcementenabled) | Restart to apply installed updates | Telemetry & updates | Admin Console |
| [`installedUpdateEnforcementHours`](#installedupdateenforcementhours) | Installed-update enforcement window | Telemetry & updates | Admin Console |
| [`autoUpdaterEnforcementHours`](#autoupdaterenforcementhours) | Auto-update enforcement window | Telemetry & updates | Self-hosted Admin Console |
| [`updateViaUpdatesHost`](#updateviaupdateshost) | Check for updates on releases.claude.com | Telemetry & updates | Admin Console |
| [`releaseChannel`](#releasechannel) | Release channel | Telemetry & updates | Self-hosted Admin Console |
| [`relaunchEnforcementHours`](#relaunchenforcementhours) | Configuration relaunch window | Telemetry & updates | Self-hosted Admin Console |
| [`configRecheckIntervalMinutes`](#configrecheckintervalminutes) | Configuration re-check interval | Telemetry & updates | Self-hosted Admin Console |
| [`disableLocalConfigCache`](#disablelocalconfigcache) | Keep only your organization ID and restrictions on disk | Telemetry & updates | Admin Console |
| [`chatSessionRetentionDays`](#chatsessionretentiondays) | Chat retention period | Limits | Admin Console |
| [`coworkSessionRetentionDays`](#coworksessionretentiondays) | Cowork retention period | Limits | Self-hosted Admin Console |
| [`codeSessionRetentionDays`](#codesessionretentiondays) | Code retention period | Limits | Self-hosted Admin Console |
| [`sessionRetentionHold`](#sessionretentionhold) | Suspend session deletion | Limits | Self-hosted Admin Console |
| [`inferenceMaxTokensPerWindow`](#inferencemaxtokensperwindow) | Max tokens per window | Limits | Self-hosted Admin Console |
| [`inferenceTokenWindowHours`](#inferencetokenwindowhours) | Token cap window | Limits | Self-hosted Admin Console |
| [`endUserAttribution`](#enduserattribution) | End-user attribution | Appearance | Self-hosted Admin Console |
| [`deploymentDisplayName`](#deploymentdisplayname) | Deployment display name | Appearance | Self-hosted Admin Console |
| [`deploymentDisplaySubtitle`](#deploymentdisplaysubtitle) | Deployment display subtitle | Appearance | Self-hosted |
| [`disableConfigDeprecationWarnings`](#disableconfigdeprecationwarnings) | Hide configuration deprecation warnings | Appearance | Self-hosted Admin Console |
| [`banner`](#banner) | Organization banner | Appearance | Self-hosted Admin Console |
| [`disableFeatureDiscovery`](#disablefeaturediscovery) | Hide feature announcements | Appearance | Self-hosted Admin Console |
| [`allowedPluginMarketplaces`](#allowedpluginmarketplaces) | Plugin marketplaces | Plugins | Self-hosted Admin Console |
| [`orgPluginSettings`](#orgpluginsettings) | Organization plugin settings | Plugins | Self-hosted Admin Console |
| [`bootstrapEnabled`](#bootstrapenabled) | Use bootstrap config | Source | Self-hosted |
| [`bootstrapUrl`](#bootstrapurl) | Bootstrap config URL | Source | Self-hosted |
| [`bootstrapOidc`](#bootstrapoidc) | Bootstrap OIDC parameters | Source | Self-hosted |
| [`bootstrapHeaders`](#bootstrapheaders) | Bootstrap request headers | Source | Self-hosted |
| [`bootstrapHeadersHelper`](#bootstrapheadershelper) | Bootstrap headers helper script | Source | Self-hosted |
| [`trustBootstrapDelivery`](#trustbootstrapdelivery) | Trust bootstrap-delivered settings | Source | Self-hosted |

## Connection

### `inferenceProvider`

enumSince 1.2581.0

**Inference provider.** Selects the inference backend. Setting this key activates third-party mode.

One of: `gateway`, `anthropic`, `bedrock`, `mantle`, `vertex`, `foundry`

[Self-hosted install](#self-hosted-column): Not supported. Part of the device's own route to the model, and a session host's route is its operator's to set.

> **More detail**
>
> Setting this key asks for 3P mode. The app opens in 3P mode unless the user chose to sign in to Claude.ai at the login screen, a choice `disableDeploymentModeChooser` removes. In 3P mode, if the selected provider's required credential keys are missing or invalid, the app shows a configuration error. A value the app cannot read (a misspelt, wrongly cased or unknown provider, or a value of the wrong type) still counts as set when machine-wide device management sent it: a macOS configuration profile, Windows policy under `HKLM`, or the root-owned policy file on Linux. The app then asks for 3P mode and, in 3P mode, shows a configuration error whose details name this key. An unreadable `bootstrapUrl` from the same sources counts the same way unless `bootstrapEnabled` is `false`. An unreadable value does not count where the user can write it: the local configuration file, or Windows policy under `HKCU`. Neither does an empty value (a value of only spaces is unreadable, not empty), or a Windows value of type `REG_BINARY`, `REG_MULTI_SZ` or `REG_QWORD`. Each of those reads as not set. When this key is not set, the app launches in standard mode unless another setting asks for 3P mode, such as a `bootstrapUrl` that `bootstrapEnabled` has not turned off. Keys for providers other than the selected one are ignored. Each provider's required keys are documented on its dedicated page under Inference providers.

***

### `inferenceCredentialKind`

enumSince 1.8555.0

**Credential kind.** Selects the credential source. When set, only that source is used (no fallback).

One of: `static`, `helper-script`, `interactive`, `vendor-profile`, `workforce`, `external-idp`

> [!WARNING]
>
> **Deprecated**
>
> * `inferenceCredentialKind: "interactive" together with inferenceGatewayOidc (gateway)`; use "external-idp" once every desktop in the fleet is on a release that reads it. The original spelling will keep working ("interactive" with inferenceGatewayOidc is read as "external-idp"); no end date has been set.

[Self-hosted install](#self-hosted-column): MDM profile. In self-hosted mode it names the device's sign-in to the host, never the host's model credential.

***

### `inferenceSessionLifetimeSec`

integerRange: 1 or moreSince 1.14271.0

**Sign-in session lifetime.** How long a sign-in stays valid under your IdP’s session policy. Shows a re-authenticate banner before it expires.

[Self-hosted install](#self-hosted-column): Not supported. The session host is the one source for how long a sign-in to it lasts, and it reads no figure from this key.

***

### `userContentRendererUrl`

stringSince 1.24012.0

**Artifact preview iframe origin.** HTTPS origin of the user-content-renderer deployment used for artifact and file previews. Defaults to the commercial host when unset.

[Self-hosted install](#self-hosted-column): Not supported. Names where Desktop loads its previews from, and no session host passes the setting on to Desktop yet.

***

### `inferenceCustomHeaders`

object: name → valueSince 1.8089.0

**Custom inference headers.** Extra headers on every inference request — routing and tenant headers only (org IDs, Bedrock Guardrails). No credentials; use the credential helper for tokens.

[Self-hosted install](#self-hosted-column): Server side. The host makes the model calls, so it adds the admin's headers to them.

> **More detail**
>
> Sent on every inference and model-discovery request (joined into the CLI's `ANTHROPIC_CUSTOM_HEADERS`).
>
> Use this for fleet-wide, non-secret constants. **Do not put API keys, bearer tokens or other credentials here** — this map is stored and distributed as plain configuration. For tokens, and for per-user or per-session values, have the **credential helper script** emit JSON with a `headers` field; those are merged over these static entries (helper wins on conflict).

***

### `inferenceCredentialHelper`

string

Consent required (A value that a bootstrap server or a self-hosted session host delivers applies only after the user approves it, unless machine-scoped device management set that server's address. For a bootstrap server, the trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)

Since 1.2581.0

**Helper script.** Absolute path to an executable that prints the credential, optionally with per-request headers.

[Self-hosted install](#self-hosted-column): MDM profile. Names a program on the person's computer, reused for the device's sign-in to the host.

> **More detail**
>
> Claude runs the executable with the entries of **Helper script arguments** as its arguments (none by default) and reads **stdout** (trimmed). Exit code must be `0`; any output on **stderr** is logged but ignored. **Stdout must contain only one of the formats below** (no banners, prompts, or log lines).
>
> **Output format** is either:
>
> * a single bare token (the API key / bearer token), or
> * a JSON object `{"token": "...", "headers": {"Name": "Value", ...}}` when per-request headers are needed (merged over **Custom inference headers**, helper wins on conflict)
>
> The helper receives `CLAUDE_HELPER_CONTEXT` in its environment (`interactive`, `mid-session-refresh`, `background`, `scheduled-task`, `setup-test`) so it can decide whether to prompt the user — see the credential-helper docs for the full contract.
>
> Result is cached for the TTL below. On TTL expiry the helper is re-invoked transparently (no user prompt, no relaunch).
>
> **Expiry and refresh:** the app checks the active credential's expiry before each turn and refreshes silently when possible (re-runs the helper, or uses the stored refresh token for interactive sign-in kinds). If the provider returns HTTP 401 mid-turn, the same silent refresh is attempted before surfacing an error. When silent refresh fails, a prompt appears with a provider-specific action (re-sign-in for interactive kinds; admin-contact for static credentials). Applies to all providers, and to both Cowork and Code.
>
> **Typical use:** a shell script that pulls from Keychain, 1Password CLI, or an internal secret broker. Example:
>
> `security find-generic-password -s anthropic-api -w`
>
> If this field is set, static credential fields (API key, bearer token) are ignored. The helper always wins.

***

### `inferenceCredentialHelperWindows`

string

Consent required (A value that a bootstrap server or a self-hosted session host delivers applies only after the user approves it, unless machine-scoped device management set that server's address. For a bootstrap server, the trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)

Since 2.2553.0

**Helper script (Windows).** Absolute path of the helper executable on Windows devices, used there instead of Helper script. Leave unset to use Helper script on every operating system.

[Self-hosted install](#self-hosted-column): MDM profile. Names a Windows program on the person's computer, reused for the device's sign-in to the host.

> **More detail**
>
> When one configuration serves both Windows and macOS or Linux devices, set **Helper script** to the macOS/Linux path and this to the Windows path (`C:\...` or `C:/...`). Windows devices run this executable with the same arguments, timeout, TTL and environment as **Helper script**; macOS and Linux devices ignore it. An invalid value here stops the connection on Windows devices only. Desktop releases that predate this setting ignore it and run **Helper script** on every operating system.

***

### `inferenceCredentialHelperArgs`

string\[]

Consent required (A value that a bootstrap server or a self-hosted session host delivers applies only after the user approves it, unless machine-scoped device management set that server's address. For a bootstrap server, the trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)

Since 2.110.0

**Helper script arguments.** Arguments passed to the helper script, one per entry, in order. Leave unset to run it with none.

[Self-hosted install](#self-hosted-column): MDM profile. Gives arguments to a helper program on the person's computer, reused for the device's sign-in to the host.

> **More detail**
>
> Each entry reaches the executable as one argument, exactly as written: `["--environment", "production"]` runs `helper --environment production`. Use it to keep one installed script and let the configuration each user receives decide what it does (which environment, tenant or vault to read), instead of packaging a script per case.
>
> Entries may not be empty and may not contain a double quote (`"`), a percent sign (`%`) or control characters, on any platform: a Windows `.cmd`/`.bat` helper receives its arguments through `cmd.exe`, where those characters would change the command. A `.cmd`/`.bat` script sees each argument quoted (`%1` is `"production"`, `%~1` strips the quotes); `.ps1`, `.exe` and POSIX helpers receive them bare. Arguments are visible in the diagnostic report and to other processes on the machine, so do not put secrets in them; the helper exists to fetch the secret.
>
> A changed list takes effect the way a changed path does.

***

### `inferenceCredentialHelperTtlSec`

integerDefault: 3600

Consent required (A value that a bootstrap server or a self-hosted session host delivers applies only after the user approves it, unless machine-scoped device management set that server's address. For a bootstrap server, the trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)

Range: 1 or moreSince 1.2581.0

**Helper script TTL.** Helper output is cached for this many seconds; once it expires the helper re-runs without a relaunch (before the next turn when set above 120).

[Self-hosted install](#self-hosted-column): MDM profile. Sets how long the desktop app caches its helper's output, reused for the device's sign-in to the host.

***

### `inferenceCredentialHelperTimeoutSec`

integerDefault: 60

Consent required (A value that a bootstrap server or a self-hosted session host delivers applies only after the user approves it, unless machine-scoped device management set that server's address. For a bootstrap server, the trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)

Range: 1–600Since 1.8089.0

**Credential helper timeout.** Maximum wait for the helper executable to finish. Raise this if the helper opens a browser for interactive sign-in.

[Self-hosted install](#self-hosted-column): MDM profile. Bounds a helper program on the person's computer, reused for the device's sign-in to the host.

***

### `inferenceCredentialHelperSilentRefreshEnabled`

booleanDefault: true

Consent required (A value that a bootstrap server or a self-hosted session host delivers applies only after the user approves it, unless machine-scoped device management set that server's address. For a bootstrap server, the trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)

Since 1.10628.0

**Re-run helper for silent refresh.** On credential expiry, re-run the helper (CLAUDE\_HELPER\_CONTEXT=mid-session-refresh) to recover silently. Turn off if the helper can’t run non-interactively.

[Self-hosted install](#self-hosted-column): MDM profile. Decides how the desktop app re-runs its helper on the person's computer, reused for sign-in to the host.

***

### `egressProxyUrl`

string

MDM only (You can set the key only in an MDM profile or the local configuration file. Claude Desktop ignores it in a bootstrap server's response.)

Since 1.44121.1

**Proxy server URL.** Send the app’s and the agent’s traffic through this HTTP proxy instead of the operating system’s proxy settings.

[Guide for this setting](https://claude.com/docs/third-party/claude-desktop/network-proxy.md)

[Self-hosted install](#self-hosted-column): MDM profile. Names the proxy for the person's computer, and a host's network belongs to its operator.

[Admin Console](#the-works-with-column): Not available.

> **More detail**
>
> Pins the app (sign-in, the connection test, model discovery, MCP servers, plugins), the Claude Code engine behind Chat, Cowork, and Code, and on macOS and Windows the Cowork workspace VM (the agent's shell, package-install, `git`, and plugin commands) to one HTTP proxy. Use it when your gateway or the internet is reachable only through a corporate proxy and you cannot rely on the system proxy. It is a reachability setting, not an egress control.
>
> The value is an `http://` or `https://` URL, usually with a port. SOCKS proxies and embedded credentials (`user:pass@`) are rejected. Give a local forwarding proxy on the device as `http://127.0.0.1:port`; an `https://` loopback address cannot be verified from inside the Cowork workspace VM. Requests to `localhost`, `127.0.0.1`, `[::1]`, and `*.local` names bypass the proxy so local MCP servers keep working; everything else goes through it, and if the proxy is unreachable requests fail rather than connect directly. The engine receives it as `HTTPS_PROXY` and `HTTP_PROXY` with a matching `NO_PROXY`; if Claude Code managed settings on the device set those variables, they win for the engine on the host. Traffic that never uses this proxy: the Cowork workspace VM on Linux, credential and header helper scripts, the update download, the Windows sign-in broker, and pages opened in the system browser.
>
> Read once at launch from device management (MDM) or the local configuration file only; a configuration server cannot deliver it, because the app may need the proxy to reach that server. A profile that sets only this key (or only the other app-behavior keys, such as `disableAutoUpdates`) does not take over a connection users set up in the app, but those keys are read from one source as a group, so put the proxy in the same profile as your update settings. Changes apply at the next app start. When `egressProxyPacUrl` is also set, the PAC file wins and this key is ignored.

***

### `egressProxyPacUrl`

string

MDM only (You can set the key only in an MDM profile or the local configuration file. Claude Desktop ignores it in a bootstrap server's response.)

Since 1.44121.1

**Proxy auto-config (PAC) URL.** URL of a PAC file that decides the proxy per request. Wins over the proxy server URL when both are set.

[Guide for this setting](https://claude.com/docs/third-party/claude-desktop/network-proxy.md)

[Self-hosted install](#self-hosted-column): MDM profile. Describes the network of the person's computer, which Desktop applies to its own traffic.

[Admin Console](#the-works-with-column): Not available.

> **More detail**
>
> At launch the app downloads the PAC script and asks it which proxy to use for each request, as a browser would, instead of following the operating system's proxy settings. Same value rules, coverage, exclusions, and delivery as `egressProxyUrl`, except that bypassing is the script's decision: `localhost`, `127.0.0.1`, and `[::1]` still never use a proxy, but `*.local` names and everything else follow whatever it returns. If the PAC file cannot be downloaded, the app connects directly rather than failing.
>
> On macOS and Windows the Cowork workspace VM is handed a copy of the script when it starts and evaluates it for each request itself; there `myIpAddress()` returns the VM's internal address rather than the device's, so a script that chooses by client subnet gives the VM its off-network answer (if that download fails, the VM connects directly). The Claude Code engine behind Chat, Cowork, and Code cannot evaluate a PAC file, so the app hands it one proxy (whichever the script returns for your inference endpoint) plus a bypass for loopback and `*.local` names. If the script answers `DIRECT` or only `SOCKS` for that endpoint, the engine uses no proxy at all, so have it return an HTTP `PROXY host:port` entry there; if the engine needs different rules, set `HTTPS_PROXY` and `NO_PROXY` in Claude Code managed settings, which win for the engine on the host.

***

### `coworkVmIpv6Enabled`

booleanSince 1.52386.0

**Enable IPv6 in the workspace VM.** Give the Cowork workspace VM an IPv6 address and route so the agent’s tools can reach IPv6-only hosts through the device. macOS and Windows; off by default.

[Self-hosted install](#self-hosted-column): Not supported. Configures Cowork's local virtual machine, which a host session does not have.

> **More detail**
>
> When set to `true`, the Cowork workspace VM on macOS and Windows gets a static IPv6 address (a unique local `fd…` address) and an IPv6 default route on its virtual network next to its IPv4 address, and the VM's gateway forwards that traffic over the device's own IPv6 connectivity, as it already does for IPv4. Use it when the tools the agent runs in the VM (shell commands, package installs, `git`, and plugin commands) must reach IPv6-only destinations. The VM's resolver then also returns IPv6 (AAAA) answers. A connection the VM makes over IPv6 succeeds only where the device's own IPv6 does; on a device without working IPv6, destinations that have both keep working over IPv4 and IPv6-only destinations stay unreachable. Because the VM's address is unique-local, most tools in it keep preferring IPv4 for destinations that have both, so IPv6 mostly carries traffic to IPv6-only destinations.
>
> This is a reachability setting, not an egress control: `coworkEgressAllowedHosts` keeps deciding which hostnames the agent's tools may reach, by name, over either protocol, and IPv6 literals are still not accepted there. Hosts your policies allow must also be reachable, and filtered the way you intend, over IPv6 on your network.
>
> Unset (default): the VM is IPv4-only and its resolver returns no IPv6 answers. A change takes effect the next time the workspace VM starts, typically at the next app launch. Does not apply to the Cowork workspace VM on Linux or to Code sessions, which use the device's own network stack.

***

### Gateway

#### `inferenceGatewayBaseUrl`

string

Consent required (A value that a bootstrap server or a self-hosted session host delivers applies only after the user approves it, unless machine-scoped device management set that server's address. For a bootstrap server, the trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)

Origin-pinned (A URL that a bootstrap server delivers must share the origin of bootstrapUrl, or Claude Desktop drops it. The limit is lifted when bootstrapOidc is set, and it does not apply to a value set in an MDM profile, the local configuration file or the Enterprise Admin Console.)

Since 1.2581.0

**Gateway base URL.** Full URL of the inference gateway endpoint.

[Self-hosted install](#self-hosted-column): Not supported. Part of the device's own route to the model, and a session host's route is its operator's to set.

***

#### `inferenceGatewayApiKey`

stringSince 1.2581.0

**Gateway API key.** API key for the configured inference gateway.

[Self-hosted install](#self-hosted-column): Not supported. Part of the device's own route to the model, and a session host's route is its operator's to set.

[Admin Console](#the-works-with-column): Not available.

***

#### `inferenceGatewayAuthScheme`

enumDefault: bearerSince 1.3036.0

**Gateway auth scheme.** How the gateway credential is sent on the wire (Authorization: Bearer vs x-api-key header).

One of: `bearer` (default), `x-api-key`

> [!WARNING]
>
> **Deprecated**
>
> * `inferenceGatewayAuthScheme: "sso"`; use inferenceCredentialKind: "interactive". The original spelling will keep working; no end date has been set.

[Self-hosted install](#self-hosted-column): Not supported. Part of the device's own route to the model, and a session host's route is its operator's to set.

***

#### `inferenceGatewayOidcAuthFlow`

enumSince 1.25927.0

**Gateway sign-in flow.** How the IdP sign-in runs: system browser (default) or the OS Microsoft Entra broker.

One of: `browser`, `broker`

> [!WARNING]
>
> **Deprecated**
>
> * Use inferenceIdpAuthFlow together with inferenceIdpOidc once every desktop in the fleet is on a release that reads them. The original spelling will keep working; no end date has been set.

[Self-hosted install](#self-hosted-column): Not supported. Deprecated name for the choice of sign-in window on the person's computer.

> **More detail**
>
> * **`browser`** (default) — opens the system browser for an authorization-code (PKCE) sign-in on a loopback redirect URI. See the **IdP setup** notes on `inferenceGatewayOidc` for redirect-URI registration.
> * **`broker`** — signs in through the OS identity broker (Web Account Manager on Windows, Company Portal on macOS). Requires the IdP to be **Microsoft Entra ID** — the `issuer` on `inferenceGatewayOidc` must be `https://login.microsoftonline.com/{tenant-id}/v2.0`. The broker satisfies Conditional Access policies that require a compliant/managed device or token protection, and needs no loopback redirect. The Entra app registration must include the broker redirect URIs `ms-appx-web://Microsoft.AAD.BrokerPlugin/{client-id}` (Windows) and `msauth.com.anthropic.claudefordesktop://auth` (macOS) under the **Mobile and desktop applications** platform. Not supported on Linux.
>
> Broker mode mints a token in the customer's own Entra tenant with the customer-configured `scopes`, and forwards it to the customer's own gateway; both endpoints of that trust relationship are inside the customer's control. A desktop that has the `external-idp` kind reads this key, together with `inferenceGatewayOidc`, as that kind's sign-in flow; it stays readable.

***

#### `inferenceGatewayOidc`

object

Consent required (A value that a bootstrap server or a self-hosted session host delivers applies only after the user approves it, unless machine-scoped device management set that server's address. For a bootstrap server, the trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)

Since 1.6889.0

**Gateway SSO IdP (OIDC).** External IdP for gateway sign-in. The user’s token from this issuer is sent to the gateway as the Bearer credential.

> [!WARNING]
>
> **Deprecated**
>
> * Use inferenceIdpOidc with inferenceCredentialKind: "external-idp" once every desktop in the fleet is on a release that reads them. The original spelling will keep working; no end date has been set.

[Guide for this setting](https://claude.com/docs/third-party/claude-desktop/gateway.md#single-sign-on-with-your-identity-provider)

[Self-hosted install](#self-hosted-column): Not supported. Deprecated name for a sign-in that runs on the person's computer.

> **More detail**
>
> **External IdP mode.** The app discovers `<issuer>/.well-known/openid-configuration`, runs an OIDC authorization-code-with-PKCE sign-in in the system browser with `clientId`, and sends the resulting token as `Authorization: Bearer` on every inference request. Leave this unset for a gateway that hosts its own RFC 8414 metadata at `<baseUrl>/.well-known/oauth-authorization-server`. A desktop that has the `external-idp` kind reads this block as that kind's identity-provider key; it stays readable, so a fleet keeps this spelling until every desktop is on such a release.
>
> **Bearer token type.** `id_token` (the default) sends the OIDC ID token; the gateway validates signature, `iss`, and `aud` (the `clientId` configured here). `access_token` sends the OAuth access token, for gateways that validate as a resource server (Portkey, Kong, Envoy JWT filter, AWS API Gateway authorizers); `scopes` must then name the gateway's registered API scope. Either way the gateway must check `aud`, not just signature and issuer, or it accepts any token from your tenant.
>
> **IdP setup.** The callback is `http://127.0.0.1:<port>/callback` by default (`http://localhost:<port>/callback` with `redirectHost: "localhost"`); register exactly the one you use and include `/callback`. **Entra:** a public-client app with a *Mobile and desktop applications* redirect URI of `http://127.0.0.1/callback` (any port; omitting the path fails with `AADSTS50011`); in `access_token` mode also grant the gateway API's delegated permission, or sign-in fails with `AADSTS65001`. **Okta:** a *Native* app with the exact URI `http://127.0.0.1:<port>/callback` and that port in `redirectPort`.
>
> **Refresh.** With `offline_access` the app renews the token silently and prompts a browser sign-in only when refresh fails. Google never returns an `id_token` on refresh, so a Google Workspace-backed gateway in `id_token` mode re-prompts about hourly; `access_token` mode is unaffected.

> **Child attributes (11)**
>
> **clientId** `string` *required*
>
> OAuth client ID of the desktop app registration at your identity provider (public client, PKCE).
>
> **issuer** `string`
>
> HTTPS issuer with OIDC discovery. Set this, or set the authorization and token URLs instead.
>
> **authorizationUrl** `string`
>
> HTTPS authorization endpoint. Used with the token URL when no issuer is set.
>
> **tokenUrl** `string`
>
> HTTPS token endpoint. Used with the authorization URL when no issuer is set.
>
> **bearerTokenType** `enum` (default: id\_token)
>
> Which token to send as the bearer. Use access token for a gateway or proxy that validates as an OAuth resource server.
>
> One of: `id_token` (default), `access_token`
>
> > **More detail**
> >
> > In **access-token** mode the token's audience must be your gateway or proxy. On IdPs where the requested scopes decide the audience (**Entra ID**), include its API resource scope in `scopes` — `api://<gateway-app-id>/.default`, or a named delegated scope you exposed via *Expose an API*. With only the standard OIDC scopes (`openid profile email offline_access`) Entra returns a v1.0 Microsoft Graph token whose issuer (`https://sts.windows.net/<tenant>/`) doesn't match the v2.0 issuer configured here, so a gateway that validates `iss` rejects it. On IdPs that set the access-token audience out-of-band (Keycloak audience mapper, Auth0 default audience, Okta custom authorization server), a resource scope in `scopes` isn't required — the audience comes from the IdP-side configuration.
>
> **scopes** `string`
>
> Space-separated scopes. Required in access-token mode: set the gateway or proxy API scope. offline\_access is appended automatically unless disabled below.
>
> **appendOfflineAccess** `boolean` (default: true)
>
> Automatically append offline\_access to scopes so the IdP returns a refresh token for silent refresh.
>
> > **More detail**
> >
> > Turn off only if your authorization server rejects `offline_access` as an unknown scope; include the server’s own refresh-token scope in **Scopes** instead.
>
> **resource** `string`
>
> Access-token audience of the gateway or proxy: an https URL or an AD FS relying-party identifier, sent as the RFC 8707 resource. Leave unset for Entra ID.
>
> > **More detail**
> >
> > Set this only for an IdP that implements RFC 8707 resource indicators. The app then sends `resource=<value>` on the authorization, token and refresh requests, so the access token the IdP issues is audience-restricted to the gateway or proxy rather than to the IdP's own APIs. Use it with `bearerTokenType: access_token`; in `id_token` mode the ID token's audience is always `clientId`. Ignored with the OS-broker sign-in flow (the sign-in flow key set to `broker`), which is Entra-only.
> >
> > **Microsoft Entra ID:** leave unset — the v2.0 endpoint rejects `resource`; request the API scope in `scopes` instead (`api://<gateway-app-id>/.default`). **AD FS:** enter one of the relying-party trust's identifiers, spelled as it is registered there. A value with no scheme (a host name with or without a port or path, a single name, or a GUID; `name:digits` also reads as a host name with a port) is sent as `https://<value>`; an identifier with a scheme of its own (`urn:…`, or an organization-defined one such as `VENDOR:URI:…`) is sent exactly as written. A trust whose only identifier is a bare name or GUID will not match, because those are sent as `https://<value>`: add an `https://…` or `urn:…` identifier to the trust and enter that one here. With any other identity provider, use an absolute URI without a fragment (RFC 8707 — the IdP rejects one as `invalid_target`). Changing it signs users in again.
>
> **redirectPort** `integer`
>
> Fixed loopback port for the sign-in redirect. Leave unset to use a free port each time.
>
> **redirectHost** `enum`
>
> Use localhost only if your IdP’s registered redirect URI specifies it.
>
> One of: `127.0.0.1`, `localhost`
>
> **additionalRedirectReferrerHosts** `string`
>
> Space-separated hostnames also accepted as the referrer of the sign-in callback. Only needed when the IdP completes sign-in from a different host.
>
> > **More detail**
> >
> > Only needed when the IdP completes sign-in from a host other than the authorization URL’s. When a callback is rejected for a referrer mismatch, the rejected host is named in the app log — add that hostname here.

***

#### `inferenceIdpAuthFlow`

enumSince 2.7032.0

**Identity provider sign-in flow.** How the identity-provider sign-in runs: system browser (default) or the OS Microsoft Entra broker.

One of: `browser`, `broker`

[Self-hosted install](#self-hosted-column): MDM profile. Chooses a sign-in window on the person's computer, also used for the device's sign-in to the host.

> **More detail**
>
> * **`browser`** (default) — opens the system browser for an authorization-code (PKCE) sign-in on a loopback redirect URI. See the **IdP setup** notes on `inferenceIdpOidc` for redirect-URI registration.
> * **`broker`** — signs in through the OS identity broker (Web Account Manager on Windows, Company Portal on macOS). Requires the IdP to be **Microsoft Entra ID** — the `issuer` on `inferenceIdpOidc` must be `https://login.microsoftonline.com/{tenant-id}/v2.0`. The broker satisfies Conditional Access policies that require a compliant/managed device or token protection, and needs no loopback redirect. The Entra app registration must include the broker redirect URIs `ms-appx-web://Microsoft.AAD.BrokerPlugin/{client-id}` (Windows) and `msauth.com.anthropic.claudefordesktop://auth` (macOS) under the **Mobile and desktop applications** platform. Not supported on Linux.
>
> Broker mode mints a token in the customer's own Entra tenant with the customer-configured `scopes` and forwards it to the customer's own gateway or proxy; both endpoints of that trust relationship are inside the customer's control.

***

#### `inferenceIdpOidc`

object

Consent required (A value that a bootstrap server or a self-hosted session host delivers applies only after the user approves it, unless machine-scoped device management set that server's address. For a bootstrap server, the trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)

Since 2.7032.0

**Identity provider (OIDC).** Your organization’s OpenID Connect identity provider. The user’s token is sent as the Bearer credential to the gateway or the Bedrock proxy.

[Self-hosted install](#self-hosted-column): MDM profile. Configures an interactive sign-in on the person's computer, reused to sign the device in to the host.

> **More detail**
>
> Used with `inferenceCredentialKind: "external-idp"`. The app discovers `<issuer>/.well-known/openid-configuration`, runs an OIDC authorization-code (PKCE) sign-in in the browser with `clientId` (or through the OS broker, see `inferenceIdpAuthFlow`) and sends the token as `Authorization: Bearer` on every inference request: to `inferenceGatewayBaseUrl` on the gateway provider, or on Bedrock to `inferenceBedrockBaseUrl`, which is then required: only a proxy that validates the token accepts it, never Amazon Bedrock itself (to sign in straight to Bedrock use `interactive`, AWS IAM Identity Center). On Bedrock this kind has no model discovery: list the models in `inferenceModels`.
>
> **Bearer token type.** `id_token` (the default) sends the OIDC ID token; the receiver validates signature, `iss` and `aud` (the `clientId` here). `access_token` sends the OAuth access token, for gateways and proxies that validate as an OAuth resource server; `scopes` must then name the registered API scope. Either way the receiver must check `aud`, or it accepts any token from your tenant.
>
> **IdP setup.** The callback is `http://127.0.0.1:<port>/callback` (`localhost` with `redirectHost: "localhost"`); register exactly that. **Entra:** a public-client app with a *Mobile and desktop applications* redirect URI `http://127.0.0.1/callback` (omitting the path fails with `AADSTS50011`); in `access_token` mode also grant the API's delegated permission, or sign-in fails with `AADSTS65001`. **Okta:** a *Native* app with `http://127.0.0.1:<port>/callback` and that port in `redirectPort`.
>
> **Refresh.** With `offline_access` the app renews the token silently and asks for a browser sign-in only when refresh fails (Google returns no `id_token` on refresh, so `id_token` mode there re-prompts about hourly).
>
> **Older names.** Gateway configurations written before this key use `inferenceGatewayOidc` / `inferenceGatewayOidcAuthFlow` with the `interactive` kind; they stay readable and mean the same sign-in.

> **Child attributes (11)**
>
> **clientId** `string` *required*
>
> OAuth client ID of the desktop app registration at your identity provider (public client, PKCE).
>
> **issuer** `string`
>
> HTTPS issuer with OIDC discovery. Set this, or set the authorization and token URLs instead.
>
> **authorizationUrl** `string`
>
> HTTPS authorization endpoint. Used with the token URL when no issuer is set.
>
> **tokenUrl** `string`
>
> HTTPS token endpoint. Used with the authorization URL when no issuer is set.
>
> **bearerTokenType** `enum` (default: id\_token)
>
> Which token to send as the bearer. Use access token for a gateway or proxy that validates as an OAuth resource server.
>
> One of: `id_token` (default), `access_token`
>
> > **More detail**
> >
> > In **access-token** mode the token's audience must be your gateway or proxy. On IdPs where the requested scopes decide the audience (**Entra ID**), include its API resource scope in `scopes` — `api://<gateway-app-id>/.default`, or a named delegated scope you exposed via *Expose an API*. With only the standard OIDC scopes (`openid profile email offline_access`) Entra returns a v1.0 Microsoft Graph token whose issuer (`https://sts.windows.net/<tenant>/`) doesn't match the v2.0 issuer configured here, so a gateway that validates `iss` rejects it. On IdPs that set the access-token audience out-of-band (Keycloak audience mapper, Auth0 default audience, Okta custom authorization server), a resource scope in `scopes` isn't required — the audience comes from the IdP-side configuration.
>
> **scopes** `string`
>
> Space-separated scopes. Required in access-token mode: set the gateway or proxy API scope. offline\_access is appended automatically unless disabled below.
>
> **appendOfflineAccess** `boolean` (default: true)
>
> Automatically append offline\_access to scopes so the IdP returns a refresh token for silent refresh.
>
> > **More detail**
> >
> > Turn off only if your authorization server rejects `offline_access` as an unknown scope; include the server’s own refresh-token scope in **Scopes** instead.
>
> **resource** `string`
>
> Access-token audience of the gateway or proxy: an https URL or an AD FS relying-party identifier, sent as the RFC 8707 resource. Leave unset for Entra ID.
>
> > **More detail**
> >
> > Set this only for an IdP that implements RFC 8707 resource indicators. The app then sends `resource=<value>` on the authorization, token and refresh requests, so the access token the IdP issues is audience-restricted to the gateway or proxy rather than to the IdP's own APIs. Use it with `bearerTokenType: access_token`; in `id_token` mode the ID token's audience is always `clientId`. Ignored with the OS-broker sign-in flow (the sign-in flow key set to `broker`), which is Entra-only.
> >
> > **Microsoft Entra ID:** leave unset — the v2.0 endpoint rejects `resource`; request the API scope in `scopes` instead (`api://<gateway-app-id>/.default`). **AD FS:** enter one of the relying-party trust's identifiers, spelled as it is registered there. A value with no scheme (a host name with or without a port or path, a single name, or a GUID; `name:digits` also reads as a host name with a port) is sent as `https://<value>`; an identifier with a scheme of its own (`urn:…`, or an organization-defined one such as `VENDOR:URI:…`) is sent exactly as written. A trust whose only identifier is a bare name or GUID will not match, because those are sent as `https://<value>`: add an `https://…` or `urn:…` identifier to the trust and enter that one here. With any other identity provider, use an absolute URI without a fragment (RFC 8707 — the IdP rejects one as `invalid_target`). Changing it signs users in again.
>
> **redirectPort** `integer`
>
> Fixed loopback port for the sign-in redirect. Leave unset to use a free port each time.
>
> **redirectHost** `enum`
>
> Use localhost only if your IdP’s registered redirect URI specifies it.
>
> One of: `127.0.0.1`, `localhost`
>
> **additionalRedirectReferrerHosts** `string`
>
> Space-separated hostnames also accepted as the referrer of the sign-in callback. Only needed when the IdP completes sign-in from a different host.
>
> > **More detail**
> >
> > Only needed when the IdP completes sign-in from a host other than the authorization URL’s. When a callback is rejected for a referrer mismatch, the rejected host is named in the app log — add that hostname here.

***

#### `inferenceStreamIdleTimeoutSec`

integerRange: 300–1,800Since 1.44121.1

**Stream idle timeout.** Extra seconds to wait for model output on a streaming response that is sending only keep-alive pings. Gateway provider only. Default 300.

[Self-hosted install](#self-hosted-column): Server side. The host makes the model calls, so it sets how long a stream sending only keep-alive pings may wait for output.

> **More detail**
>
> Raises how long Cowork, Chat and Code sessions wait for the next model event on an open streaming response (Claude Code's `CLAUDE_STREAM_IDLE_TIMEOUT_MS`). It only helps when the gateway writes SSE keep-alive `ping` events (or `:` comment lines) into the response while the upstream model is silent — for example a LiteLLM proxy with keep-alive pings enabled in front of Amazon Bedrock. With pings arriving, Claude Code accepts at least about five minutes of keep-alives and then waits this many seconds more for real model output before abandoning the request. Gateway provider only; the other providers keep Claude Code's defaults.
>
> A response on which nothing at all arrives — no pings — still fails after about 5 minutes regardless of this key, because at the device a silent connection cannot be told apart from a dead one. If long generations fail behind a gateway that does not send pings, configure the gateway to send them rather than raising this value. A common case is automatic compaction, in which a session sends its whole conversation in one streaming request and waits for a long summary; when that request fails, the error reads `Prompt is too long · automatic compaction failed:` followed by the cause. While this key is set, the app's value takes precedence over `CLAUDE_STREAM_IDLE_TIMEOUT_MS` in Claude Code's own managed settings for sessions the app starts; when it is unset, that setting still applies. Values outside 300–1800 are rejected at parse time (the error is listed in the diagnostics report) and the default applies.

***

### Anthropic

#### `inferenceAnthropicApiKey`

stringSince 1.8089.0

**Claude API key.** Leave blank to sign in with your browser, or to supply the key via a credential helper.

[Self-hosted install](#self-hosted-column): Not supported. Part of the device's own route to the model, and a session host's route is its operator's to set.

[Admin Console](#the-works-with-column): Not available.

***

### Bedrock

#### `inferenceBedrockRegion`

stringSince 1.2581.0

**AWS region.** AWS region for the Bedrock runtime endpoint.

[Self-hosted install](#self-hosted-column): Not supported. Part of the device's own route to the model, and a session host's route is its operator's to set.

***

#### `inferenceBedrockBaseUrl`

string

Consent required (A value that a bootstrap server or a self-hosted session host delivers applies only after the user approves it, unless machine-scoped device management set that server's address. For a bootstrap server, the trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)

Origin-pinned (A URL that a bootstrap server delivers must share the origin of bootstrapUrl, or Claude Desktop drops it. The limit is lifted when bootstrapOidc is set, and it does not apply to a value set in an MDM profile, the local configuration file or the Enterprise Admin Console.)

Since 1.2581.0

**Bedrock base URL.** For VPC endpoints or gateway proxies. Host origin only.

[Self-hosted install](#self-hosted-column): Not supported. Part of the device's own route to the model, and a session host's route is its operator's to set.

***

#### `inferenceBedrockServiceTier`

enumSince 1.5186.0

**Bedrock service tier.** Sent as the X-Amzn-Bedrock-Service-Tier header. Leave unset for on-demand.

One of: `flex`, `priority`

[Self-hosted install](#self-hosted-column): Not supported. Part of the device's own route to the model, and a session host's route is its operator's to set.

> **More detail**
>
> Tier availability varies by model and region. Reserved capacity uses a provisioned-throughput ARN as the model ID instead of this setting. Older bundled Claude Code CLI versions ignore this key.

***

#### `inferenceBedrockBearerToken`

stringSince 1.2581.0

**AWS bearer token.** Static bearer token for inference. For providers that support profile or helper-script credentials, prefer those.

[Self-hosted install](#self-hosted-column): Not supported. Part of the device's own route to the model, and a session host's route is its operator's to set.

[Admin Console](#the-works-with-column): Not available.

***

#### `inferenceBedrockSsoStartUrl`

string

Consent required (A value that a bootstrap server or a self-hosted session host delivers applies only after the user approves it, unless machine-scoped device management set that server's address. For a bootstrap server, the trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)

Since 1.6259.0

**AWS SSO start URL.** Enables in-app AWS sign-in (no AWS CLI needed). Set with the three SSO fields below.

[Self-hosted install](#self-hosted-column): Not supported. Drives a browser sign-in on the person's computer, and a host never calls Bedrock as the person.

***

#### `inferenceBedrockSsoRegion`

string

Consent required (A value that a bootstrap server or a self-hosted session host delivers applies only after the user approves it, unless machine-scoped device management set that server's address. For a bootstrap server, the trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)

Since 1.6259.0

**AWS SSO region.** IAM Identity Center home region.

[Self-hosted install](#self-hosted-column): Not supported. Configures a browser sign-in on the person's computer, and a host-run session has no browser.

***

#### `inferenceBedrockSsoAccountId`

string

Consent required (A value that a bootstrap server or a self-hosted session host delivers applies only after the user approves it, unless machine-scoped device management set that server's address. For a bootstrap server, the trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)

Since 1.6259.0

**AWS SSO account ID.** 12-digit AWS account ID assigned to users in IAM Identity Center.

[Self-hosted install](#self-hosted-column): Not supported. Names an AWS account for a browser sign-in on the person's computer, which a host never performs.

***

#### `inferenceBedrockSsoRoleName`

string

Consent required (A value that a bootstrap server or a self-hosted session host delivers applies only after the user approves it, unless machine-scoped device management set that server's address. For a bootstrap server, the trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)

Since 1.6259.0

**AWS SSO role name.** IAM Identity Center permission-set name granting bedrock:InvokeModel\* on the account above.

[Self-hosted install](#self-hosted-column): Not supported. Names an AWS role for a browser sign-in that is only possible on the person's computer.

***

#### `inferenceBedrockProfile`

string

Consent required (A value that a bootstrap server or a self-hosted session host delivers applies only after the user approves it, unless machine-scoped device management set that server's address. For a bootstrap server, the trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)

Since 1.2581.0

**AWS profile name.** AWS named profile to use for Bedrock inference credentials.

[Self-hosted install](#self-hosted-column): Not supported. Part of the device's own route to the model, and a session host's route is its operator's to set.

***

#### `inferenceBedrockAwsDir`

string

Consent required (A value that a bootstrap server or a self-hosted session host delivers applies only after the user approves it, unless machine-scoped device management set that server's address. For a bootstrap server, the trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)

Since 1.2581.0

**AWS config directory.** Folder with AWS config/credentials. Defaults to \~/.aws when no bearer token is set.

[Self-hosted install](#self-hosted-column): Not supported. Names a folder on the person's computer that a host does not have.

***

#### `inferenceBedrockAwsCliPath`

string

Consent required (A value that a bootstrap server or a self-hosted session host delivers applies only after the user approves it, unless machine-scoped device management set that server's address. For a bootstrap server, the trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)

Since 1.13576.0

**AWS CLI path.** Absolute path to the aws executable. Leave unset to find it on PATH.

[Self-hosted install](#self-hosted-column): Not supported. Names a program on the person's computer, and a host has no such program, browser or person.

***

### Vertex

#### `inferenceVertexProjectId`

string

Consent required (A value that a bootstrap server or a self-hosted session host delivers applies only after the user approves it, unless machine-scoped device management set that server's address. For a bootstrap server, the trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)

Since 1.2581.0

**GCP project ID.** Google Cloud project ID for Vertex AI inference.

[Self-hosted install](#self-hosted-column): Not supported. Part of the device's own route to the model, and a session host's route is its operator's to set.

***

#### `inferenceVertexRegion`

stringSince 1.2581.0

**GCP region.** GCP region where your Vertex AI Claude models are deployed.

[Self-hosted install](#self-hosted-column): Not supported. Part of the device's own route to the model, and a session host's route is its operator's to set.

***

#### `inferenceVertexBaseUrl`

string

Consent required (A value that a bootstrap server or a self-hosted session host delivers applies only after the user approves it, unless machine-scoped device management set that server's address. For a bootstrap server, the trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)

Origin-pinned (A URL that a bootstrap server delivers must share the origin of bootstrapUrl, or Claude Desktop drops it. The limit is lifted when bootstrapOidc is set, and it does not apply to a value set in an MDM profile, the local configuration file or the Enterprise Admin Console.)

Since 1.2581.0

**Vertex AI base URL.** PSC endpoint, if using one.

[Self-hosted install](#self-hosted-column): Not supported. Part of the device's own route to the model, and a session host's route is its operator's to set.

***

#### `inferenceVertexOAuthClientId`

string

Consent required (A value that a bootstrap server or a self-hosted session host delivers applies only after the user approves it, unless machine-scoped device management set that server's address. For a bootstrap server, the trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)

Since 1.2581.0

**Vertex OAuth client ID.** Desktop-app OAuth client ID. Enables Sign in with Google instead of a credentials file.

[Self-hosted install](#self-hosted-column): Not supported. Configures a Google browser sign-in on the person's computer, and a host calls Vertex as its own identity.

***

#### `inferenceVertexOAuthClientSecret`

stringSince 1.2581.0

**Vertex OAuth client secret.** Secret for the Desktop-app OAuth client above. Google classifies installed-app client secrets as non-confidential, so this may be set from hosted config.

[Self-hosted install](#self-hosted-column): Not supported. Secret for the person's own Google sign-in, and a host calls Vertex as its own Google identity.

***

#### `inferenceVertexOAuthScopes`

stringSince 1.2581.0

**Vertex OAuth scopes.** Override the Google OAuth scopes (space-separated). Leave blank for the default.

[Self-hosted install](#self-hosted-column): Not supported. Sets scopes for a browser sign-in on the person's computer, and a host calls Vertex as its own identity.

***

#### `inferenceVertexOAuthLoginHint`

stringSince 1.12603.0

**Vertex OAuth login hint.** Pre-fill Google's account chooser and forward to your federated IdP. \{username} expands to the OS login name.

[Self-hosted install](#self-hosted-column): Not supported. Steers a browser sign-in on the person's computer, and a host calls Vertex as its own Google identity.

***

#### `inferenceVertexWorkforceAudience`

string

Consent required (A value that a bootstrap server or a self-hosted session host delivers applies only after the user approves it, unless machine-scoped device management set that server's address. For a bootstrap server, the trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)

Since 1.10628.0

**Workforce Identity audience.** Workforce-pool provider audience. When set, sign-in uses your own IdP plus a GCP STS exchange instead of a Google identity.

[Self-hosted install](#self-hosted-column): Not supported. Configures a sign-in the person completes on their computer, and a host calls Vertex as its own identity.

***

#### `inferenceVertexWorkforceUserProject`

string

Consent required (A value that a bootstrap server or a self-hosted session host delivers applies only after the user approves it, unless machine-scoped device management set that server's address. For a bootstrap server, the trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)

Since 1.10628.0

**Workforce Identity billing project.** GCP project for STS billing and quota. Defaults to the Vertex project ID above.

[Self-hosted install](#self-hosted-column): Not supported. Bills the exchange of the person's own sign-in token, and a host calls Vertex as its own identity.

***

#### `inferenceVertexWorkforceAuthFlow`

enumSince 1.25927.0

**Workforce Identity sign-in flow.** How the IdP sign-in runs: system browser (default) or the OS Microsoft Entra broker.

One of: `browser`, `broker`

[Self-hosted install](#self-hosted-column): Not supported. Chooses how the person signs in on their computer, and a host calls Vertex as its own identity.

> **More detail**
>
> * **`browser`** (default) — opens the system browser for an authorization-code (PKCE) sign-in on a loopback redirect URI. See the **IdP setup** notes on `inferenceGatewayOidc` for redirect-URI registration; the same rules apply here.
> * **`broker`** — signs in through the OS identity broker (Web Account Manager on Windows, Company Portal on macOS). Requires the workforce-pool IdP to be **Microsoft Entra ID** — the `issuer` on `inferenceVertexWorkforceOidc` must be `https://login.microsoftonline.com/{tenant-id}/v2.0`. The broker satisfies Conditional Access policies that require a compliant/managed device or token protection, and needs no loopback redirect. The Entra app registration must include the broker redirect URIs `ms-appx-web://Microsoft.AAD.BrokerPlugin/{client-id}` (Windows) and `msauth.com.anthropic.claudefordesktop://auth` (macOS) under the **Mobile and desktop applications** platform. Not supported on Linux.
>
> The GCP STS token-exchange step is unchanged in either flow; only how the Entra id\_token is acquired differs.

***

#### `inferenceVertexWorkforceOidc`

object

Consent required (A value that a bootstrap server or a self-hosted session host delivers applies only after the user approves it, unless machine-scoped device management set that server's address. For a bootstrap server, the trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)

Since 1.10628.0

**Workforce Identity IdP (OIDC).** Your organization’s OIDC IdP. The app runs an authorization-code-with-PKCE flow against this issuer and exchanges the returned ID token at GCP STS.

[Self-hosted install](#self-hosted-column): Not supported. Sets up the person's sign-in on their own computer, and a host calls Vertex as its own Google identity.

> **Child attributes (9)**
>
> **clientId** `string` *required*
>
> OAuth client ID of the desktop app registration at your identity provider (public client, PKCE).
>
> **issuer** `string`
>
> HTTPS issuer with OIDC discovery. Set this, or set the authorization and token URLs instead.
>
> **authorizationUrl** `string`
>
> HTTPS authorization endpoint. Used with the token URL when no issuer is set.
>
> **tokenUrl** `string`
>
> HTTPS token endpoint. Used with the authorization URL when no issuer is set.
>
> **scopes** `string`
>
> Space-separated scopes. Defaults to openid profile email offline\_access.
>
> **redirectPort** `integer`
>
> Fixed loopback port for the sign-in redirect. Leave unset to use a free port each time.
>
> **redirectHost** `enum`
>
> Use localhost only if your IdP’s registered redirect URI specifies it.
>
> One of: `127.0.0.1`, `localhost`
>
> **omitOfflineAccess** `boolean`
>
> Only enable if your IdP rejects the offline\_access scope on this client. Without it the app prompts for sign-in each time the token expires.
>
> **additionalRedirectReferrerHosts** `string`
>
> Space-separated hostnames also accepted as the referrer of the sign-in callback. Only needed when the IdP completes sign-in from a different host.
>
> > **More detail**
> >
> > Only needed when the IdP completes sign-in from a host other than the authorization URL’s. When a callback is rejected for a referrer mismatch, the rejected host is named in the app log — add that hostname here.

***

#### `inferenceVertexCredentialsFile`

string

Consent required (A value that a bootstrap server or a self-hosted session host delivers applies only after the user approves it, unless machine-scoped device management set that server's address. For a bootstrap server, the trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)

Since 1.2581.0

**GCP credentials file path.** Absolute path to service-account JSON. Leave blank to fall back to ADC.

[Self-hosted install](#self-hosted-column): Not supported. Names a file on the person's computer that no host has.

***

### Foundry

#### `inferenceFoundryResource`

string

Consent required (A value that a bootstrap server or a self-hosted session host delivers applies only after the user approves it, unless machine-scoped device management set that server's address. For a bootstrap server, the trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)

Since 1.2581.0

**Azure AI Foundry resource name.** Azure AI Foundry resource name used to construct the endpoint URL.

[Self-hosted install](#self-hosted-column): Not supported. Part of the device's own route to the model, and a session host's route is its operator's to set.

***

#### `inferenceFoundryBaseUrl`

string

Consent required (A value that a bootstrap server or a self-hosted session host delivers applies only after the user approves it, unless machine-scoped device management set that server's address. For a bootstrap server, the trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)

Origin-pinned (A URL that a bootstrap server delivers must share the origin of bootstrapUrl, or Claude Desktop drops it. The limit is lifted when bootstrapOidc is set, and it does not apply to a value set in an MDM profile, the local configuration file or the Enterprise Admin Console.)

Since 2.110.0

**Azure AI Foundry base URL.** Full base URL for a gateway or proxy in front of Foundry, path included (replaces [https://RESOURCE.services.ai.azure.com/anthropic](https://RESOURCE.services.ai.azure.com/anthropic)).

[Self-hosted install](#self-hosted-column): Not supported. Part of the device's own route to the model, and a session host's route is its operator's to set.

> **More detail**
>
> Set this only when the app reaches Foundry through a gateway or proxy you run, such as Azure API Management. Requests go to `<value>/v1/messages` instead of `https://<resource>.services.ai.azure.com/anthropic/v1/messages`, carrying the same credential and headers the app would send to Foundry: each user's Entra ID token for the Azure Cognitive Services audience as `Authorization: Bearer` with Entra sign-in, otherwise the API key or the credential helper's output. Claude Code sessions receive the value as `ANTHROPIC_FOUNDRY_BASE_URL`, so use the same value you would give Claude Code in a terminal. `inferenceFoundryResource` is still required and should name the resource behind the gateway; the app sends nothing to the resource directly while this is set. Must be https, or http to a proxy at a loopback address on the device itself (127.0.0.1, localhost or \[::1]).

***

#### `inferenceFoundryApiKey`

stringSince 1.2581.0

**Azure AI Foundry API key.** API key for Azure AI Foundry inference.

[Self-hosted install](#self-hosted-column): Not supported. Part of the device's own route to the model, and a session host's route is its operator's to set.

[Admin Console](#the-works-with-column): Not available.

***

#### `inferenceFoundryTenantId`

string

Consent required (A value that a bootstrap server or a self-hosted session host delivers applies only after the user approves it, unless machine-scoped device management set that server's address. For a bootstrap server, the trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)

Since 1.9255.0

**Entra ID tenant ID.** Directory (tenant) ID of the Entra ID app registration that has the Cognitive Services scope.

[Self-hosted install](#self-hosted-column): Not supported. Names the tenant for an Entra sign-in on the person's computer.

***

#### `inferenceFoundryClientId`

string

Consent required (A value that a bootstrap server or a self-hosted session host delivers applies only after the user approves it, unless machine-scoped device management set that server's address. For a bootstrap server, the trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)

Since 1.9255.0

**Entra ID client ID.** Application (client) ID of the Entra ID app registration. Device-code sign-in requires the app to allow public client flows.

[Self-hosted install](#self-hosted-column): Not supported. Configures an Entra sign-in the person completes on their computer.

***

#### `inferenceFoundryAuthFlow`

enumSince 1.19367.0

**Entra ID sign-in flow.** How Entra sign-in runs: device code (default), system browser, or the OS identity broker.

One of: `device-code`, `browser`, `broker`

[Self-hosted install](#self-hosted-column): Not supported. Chooses how the person's Entra sign-in runs on their computer.

> **More detail**
>
> * **`device-code`** (default) — shows a code to enter at microsoft.com/devicelogin. The app registration must have **Allow public client flows** enabled.
> * **`browser`** — opens the system browser for an authorization-code (PKCE) sign-in on a loopback redirect URI. The app registration must include `http://127.0.0.1/callback` under the **Mobile and desktop applications** platform (Entra ignores the loopback port, but not the path). Works with **Allow public client flows** disabled, and is unaffected by Conditional Access policies that block device-code authentication.
> * **`broker`** — signs in through the OS identity broker (Web Account Manager on Windows, Company Portal on macOS), so it can satisfy Conditional Access policies that require a compliant/managed device or token protection. The app registration must include the broker redirect URIs `ms-appx-web://Microsoft.AAD.BrokerPlugin/{client-id}` (Windows) and `msauth.com.anthropic.claudefordesktop://auth` (macOS) under the **Mobile and desktop applications** platform. Not supported on Linux.
>
> App versions that predate this key always use device code; versions that predate the broker option treat `broker` as unset and use device code.

***

### Models

#### `modelDiscoveryEnabled`

booleanSince 1.8089.0

**Model discovery.** Auto-populate the model picker from the provider at launch.

[Self-hosted install](#self-hosted-column): Not supported. A session host states the models it offers, so Desktop discovers none itself, whatever this says.

> **More detail**
>
> Auto-populate the model picker from the provider's model-list endpoint at launch. For gateway and Anthropic providers, a config that doesn't set this key skips discovery automatically when the model list below already makes it unnecessary; the toggle here only sets it explicitly on or off. Turn off if the endpoint isn't reachable from your network, or to use a fixed list. When off, the model list below is required and must use full model IDs (aliases like sonnet/opus are resolved via discovery).

***

#### `modelPrefer1mContext`

booleanSince 1.28929.0

**Use 1M wherever it’s available.** Every model that offers 1M, in your list or from your gateway, shows one option and requests 1M.

[Self-hosted install](#self-hosted-column): Server side. When on, the host gives a session that names no model the 1M-token context, and tells Desktop.

> **More detail**
>
> Every model that offers a 1M-token context window shows one option in the model picker, and sessions on it request 1M from your provider. A model offers 1M when its `inferenceModels` entry sets `supports1m` or, under discovery, when your gateway's model list marks it. Equivalent to setting `prefer1m` on each of those entries, but also applies under dynamic discovery. To leave one listed model out, remove its `supports1m`. Beside a model list in which no entry sets `supports1m`, this setting does nothing. Older Claude Desktop versions show both options and only start the default model on its 1M option.

***

#### `inferenceModels`

object\[]Since 1.2581.0

**Model list.** Override the auto-discovered model list. First entry is the default.

[Self-hosted install](#self-hosted-column): Server side. The host runs a session only on a model from this list, and tells Desktop what to show.

> **More detail**
>
> Use the **provider's exact model ID**: Vertex publisher IDs (`claude-sonnet-5`), Bedrock inference-profile IDs (`us.anthropic.claude-sonnet-5`), or Foundry deployment names. Entries may be plain ID strings or objects.
>
> **Gateway:** the `name` must be the exact ID your gateway's `/v1/models` endpoint returns. If you set `supports1m` on an alias (`sonnet`) but discovery returns the full ID, the variant won't appear.
>
> **Extended context** (`supports1m`) is a capability assertion you make about your deployment; only set it for models you've confirmed support the 1M-token window:
>
> ```json theme={null} theme={null} theme={null} theme={null} theme={null} theme={null} theme={null} theme={null} theme={null} theme={null} theme={null} theme={null}
> [{"name": "claude-sonnet-5", "supports1m": true}, "claude-opus-4-8"]
> ```
>
> `"claude-sonnet-5[1m]"` is shorthand for the same entry. When an ID is listed both bare and with `[1m]` (as a gateway lists it), the picker shows one model with a 1M variant; put `labelOverride` on the bare entry (a label on the `[1m]` spelling is ignored there); tier-tagged entries are not folded. `prefer1m: true` (no effect without `supports1m`) shows only the 1M variant of the model. Under dynamic discovery (no explicit list), set `modelPrefer1mContext` instead.
>
> **Display label** (`labelOverride`) is for IDs the picker can't derive a friendly name from (Bedrock ARNs, gateway routing aliases). Display-only; `name` is still what the app sends:
>
> ```json theme={null} theme={null} theme={null} theme={null} theme={null} theme={null} theme={null} theme={null} theme={null} theme={null} theme={null} theme={null}
> [{"name": "arn:aws:bedrock:us-east-1:123:application-inference-profile/abc", "labelOverride": "Claude Opus (Prod)"}]
> ```
>
> **Tier mapping** (`anthropicFamilyTier`) tells the app which Claude tier (`haiku`/`sonnet`/`opus`/`fable`/`mythos`) an entry stands in for, so bare tier aliases (e.g. in Code sessions) resolve to your model. `isFamilyDefault: true` picks the winner when several entries share a tier:
>
> ```json theme={null} theme={null} theme={null} theme={null} theme={null} theme={null} theme={null} theme={null} theme={null} theme={null} theme={null} theme={null}
> [{"name": "us.anthropic.claude-opus-4-8", "anthropicFamilyTier": "opus"}]
> ```
>
> **Auto mode on a gateway:** its safety classifier calls `claude-sonnet-5` by default, so include that exact ID in the list (see `autoModeEnabled`).

> **Child attributes (7)**
>
> **name** `string` *required*
>
> Model ID exactly as the provider expects it. The first entry is the default model.
>
> **labelOverride** `string`
>
> Shown in the model picker. Leave blank to auto-format from the ID.
>
> **supports1m** `boolean`
>
> Adds a 1M-context variant of this model to the picker. Set only if the deployment accepts 1M-token context for it.
>
> **prefer1m** `boolean`
>
> Shows one option for this model and requests 1M from your provider. Does nothing unless the entry offers 1M.
>
> **anthropicFamilyTier** `enum`
>
> Which Claude tier this model stands in for. Pins the bare alias (e.g. ‘opus’) and, for opus/fable, the refusal fallback.
>
> One of: `sonnet`, `opus`, `haiku`, `fable`, `mythos`
>
> **isFamilyDefault** `boolean`
>
> When several models share a tier alias, marks this one as the model the alias resolves to. Otherwise the first listed wins.
>
> **maxEffort** `enum`
>
> Highest effort level offered for this model; higher levels are hidden and never requested by Claude Desktop. An unrecognized value caps the model at low.
>
> One of: `low`, `medium`, `high`, `xhigh`, `max`

***

#### `defaultModelEffort`

enumSince 2.110.0

**Default model effort.** Effort level the default model (the first listed model) starts at, instead of Anthropic’s recommended level: low, medium, high, xhigh or max.

One of: `low`, `medium`, `high`, `xhigh`, `max`

[Self-hosted install](#self-hosted-column): Server side. The host sets the effort of a session that names none, and tells Desktop what to preselect.

> **More detail**
>
> The effort level the default model (the first `inferenceModels` entry, or the first model your endpoint returns under discovery) starts at in Chat, Cowork and Code, in place of Anthropic's recommended level for that model: one of `low`, `medium`, `high`, `xhigh`, `max`. It is a starting point, not a lock: a person's own effort choice for that model still applies unless `alwaysStartWithDefaultModel` is on, and other models keep their recommended level. A level the model doesn't offer falls to the nearest level it offers below it (its lowest level when none is lower), and it never exceeds that model's `maxEffort`. In Code sessions a `CLAUDE_CODE_EFFORT_LEVEL` environment variable or an `effortLevel` in Claude Code's own settings still takes precedence, as it does over any picker default.

***

#### `alwaysStartWithDefaultModel`

booleanSince 2.110.0

**Always start with the default model.** New conversations and tasks start on the default model and effort level, not each person’s last-used ones. People can still change both for the current one.

[Self-hosted install](#self-hosted-column): Server side. Desktop's model picker acts on it, starting each new session on the default model.

> **More detail**
>
> When `true`, each new conversation or task in Chat, Cowork and Code starts on the default model (the first `inferenceModels` entry), and the model and effort choices a person makes are no longer saved as their defaults. When unset or `false`, a person's last model and effort choice is remembered per tab, as before. Choices saved before the setting was turned on are kept and apply again if it is turned off.

***

#### `inferenceModelPricingEnabled`

booleanSince 1.37937.0

**Show estimated cost.** Show an estimated cost on the Usage page at Anthropic list price; turn on to set a multiplier or per-model rates.

[Self-hosted install](#self-hosted-column): Server side. When on, the host gives its sessions the admin's rates and multiplier; Desktop shows cost once they report it per turn.

> **More detail**
>
> Off unless set: the Usage page shows token counts only, since the app cannot know your negotiated provider rates. `true` turns on a USD estimate priced at Anthropic's published list price and is the only switch that does: `inferenceModelPricingMultiplier` and `inferenceModelPricing` refine the estimate while this is on and are ignored otherwise; turning this off hides them in the config editors without clearing them. Claude Code performs the calculation, so the same figures appear in its own cost reporting for Code sessions. Model IDs Claude Code cannot map to a Claude model (an opaque gateway alias, an inference-profile ARN it cannot resolve) are left out of the estimate until `inferenceModelPricing` gives them a rate. A machine-level Claude Code managed `modelPricing` (MDM / managed-settings.json / server-managed) takes precedence over all three keys.

***

#### `inferenceModelPricingMultiplier`

numberRange: 0–1Since 1.37937.0

**Price multiplier.** Scales every estimated cost (0.85 = 85% of the price); between 0 and 1.

[Self-hosted install](#self-hosted-column): Server side. While Show estimated cost is on, the host hands Claude Code this multiplier for the cost its sessions report.

> **More detail**
>
> Mirrors Claude Code's managed `modelPricing.multiplier`: a number in (0, 1] applied to every computed cost, whether the model was priced at Anthropic list price or by an `inferenceModelPricing` row; use it for a flat contracted discount. Applies only while `inferenceModelPricingEnabled` is `true`; on its own it does not turn the estimate on. Ignored when a machine-level Claude Code managed `modelPricing` is present.

***

#### `inferenceModelPricing`

object\[]Since 1.37937.0

**Model pricing.** Per-model rates replacing Anthropic list price in the Usage page’s estimate.

[Self-hosted install](#self-hosted-column): Server side. While Show estimated cost is on, the host hands Claude Code these rates for the cost its sessions report.

> **More detail**
>
> Each row replaces Anthropic list price for one model in the Usage page's estimate, in USD per million tokens (`inputPerMtok`, `outputPerMtok`, `cacheReadPerMtok`, `cacheWritePerMtok`, all four required; `cacheWritePerMtok` prices both 5-minute and 1-hour cache writes); rows apply only while `inferenceModelPricingEnabled` is `true` and do not turn the estimate on by themselves. Mirrors Claude Code's managed `modelPricing.overrides`, and `name` is matched the same way: a built-in Claude model ID (e.g. `claude-sonnet-4-6`, or its Bedrock, Vertex, or Foundry ID) covers every dated and provider spelling of that model; any other value (a gateway alias, an inference-profile ARN) matches that exact ID only (case-insensitive) and wins over a built-in row. An ID Claude Code cannot map to a Claude model at all gets no estimate until a row here prices it. `inferenceModelPricingMultiplier` still applies on top of a row.
>
> ```json theme={null} theme={null} theme={null} theme={null} theme={null} theme={null} theme={null} theme={null} theme={null} theme={null} theme={null} theme={null}
> {"inferenceModelPricingEnabled": true, "inferenceModelPricingMultiplier": 0.9, "inferenceModelPricing": [{"name": "claude-sonnet-4-6", "inputPerMtok": 2.4, "outputPerMtok": 12, "cacheReadPerMtok": 0.24, "cacheWritePerMtok": 3}]}
> ```
>
> These are estimates for visibility, not an invoice; your provider bills at its own rates. A machine-level Claude Code managed `modelPricing` (MDM / managed-settings.json / server-managed) takes precedence over this table.

> **Child attributes (5)**
>
> **name** `string` *required*
>
> A model ID from the list above, or any other ID or alias your provider serves. A built-in Claude ID also covers its dated and provider forms.
>
> **inputPerMtok** `number` *required*
>
> USD per million input tokens.
>
> **outputPerMtok** `number` *required*
>
> USD per million output tokens.
>
> **cacheReadPerMtok** `number` *required*
>
> USD per million prompt-cache read tokens.
>
> **cacheWritePerMtok** `number` *required*
>
> USD per million prompt-cache write tokens (5-minute and 1-hour writes alike).

***

#### `modelCatalogEnabled`

booleanSince 2.110.0

**Model catalog metadata.** Fetch the published Claude Code model catalog to get model picker names, descriptions, and effort options. When off, the app uses only its bundled copy.

[Self-hosted install](#self-hosted-column): Server side. The host serves the model catalog's rows to Desktop, and to nobody for whom this is off.

[Admin Console](#the-works-with-column): Not available.

> **More detail**
>
> When on (the default), the app reads the model catalog Anthropic publishes for Claude Code (a signed document fetched from `downloads.claude.ai`, or from `modelCatalogUrl` when that is set, and verified against a key built into the app; a copy bundled with the app is used until one has been fetched, or when the host is unreachable) and uses it to fill in each picker entry's display name, description, and thinking/effort options in the Chat, Cowork, and Code tabs. It never changes which models are offered, their order, or the default model (the first `inferenceModels` entry): those, 1M-context variants, and `labelOverride` still come from `inferenceModels` / discovery, and a model the catalog does not list keeps the built-in label. With `modelCatalogEnabled: false`, the app makes no catalog request and ignores any copy it fetched earlier. Picker names, descriptions, effort options, and recommended effort levels then come from the copy bundled with the installed app version, so they change only with app updates; `labelOverride`, `defaultModelEffort`, and `maxEffort` still apply. A model that copy does not list, typically one released after that version, may show no effort options until the app is updated. Applies to deployments configured on the device or by a bootstrap server; an install managed from the Claude admin console takes its model names and options from the console's settings and never fetches the catalog.

***

#### `modelCatalogUrl`

stringSince 2.110.0

**Model catalog URL.** Fetch the model catalog and its signature file from this URL (a mirror inside your network serving Anthropic’s published files) instead of downloads.claude.ai.

[Self-hosted install](#self-hosted-column): Server side. Only Desktop versions too old to take the model catalog's rows from their session host fetch from here.

[Admin Console](#the-works-with-column): Not available.

> **More detail**
>
> When set, the app fetches the catalog document and its signature file (the same URL with `.raw-sig.json` appended to the path) from this URL instead of `https://downloads.claude.ai/model-catalog/v1/catalog.json`, for a gateway or mirror inside your network serving Anthropic's two published files byte-for-byte. The document is still verified against the key built into the app, so an edited or re-signed copy is refused and the app keeps its last verified copy (or the bundled one); there is no key to configure. `https://` is required (`http://` only to a loopback address, and only when set on the device itself; a bootstrap server may not deliver a loopback or non-`https://` value); the server must answer the GET directly (redirects are not followed) and may honor `If-None-Match` with `304`, and must serve a document at least as new as the one the install last accepted (or the bundled seed) — an older one is refused and re-fetched on the retry interval until the mirror catches up. Ignored when `modelCatalogEnabled` is `false`, and on an install managed from the Claude admin console (which never fetches the catalog). A value that is not a valid URL, names a link-local or cloud-metadata host (e.g. `169.254.169.254`, `metadata.google.internal`), or is a loopback / non-`https://` value a bootstrap server delivers, turns the catalog fetch off (no fallback to `downloads.claude.ai`); the last fetched or bundled copy keeps labelling the pickers. On an install configured for a bootstrap server, the default location is not fetched until the server's configuration applies after sign-in, so a device does not poll `downloads.claude.ai` while the server may yet name a mirror; a mirror URL set on the device, cached earlier, or served in a pre-sign-in subset still fetches. Diagnostics report the location only as `hosted`, `custom`, `invalid` or `pending`; the value itself is treated like `bootstrapUrl`: host name only in telemetry, printed in full in the diagnostics bundle.

***

## Capabilities

### Cowork surface

#### `coworkTabEnabled`

booleanDefault: trueSince 1.9659.0

**Allow Cowork.** Enable Cowork. Claude works on longer tasks like research, analysis, and documents.

[Self-hosted install](#self-hosted-column): Not supported. On a session host desktopHome alone decides Cowork: to turn Cowork off, set desktopHome to off in its policy document.

***

### Code surface

#### `isClaudeCodeForDesktopEnabled`

booleanDefault: trueSince 1.2581.0

**Allow Code.** Enable Code. Claude writes and runs code.

[Self-hosted install](#self-hosted-column): Server side. The host refuses Code sessions and routines where the tab is off, and tells Desktop to hide it.

***

#### `sshHostAllowlist`

string\[]

Beta (The feature that the key configures is in beta.)

Since 1.40609.0

**SSH host allowlist.** SSH hosts for Code sessions. Unset: off unless the device’s Claude Code managed settings list hosts. An admin’s empty list: off even then. \* allows any host.

[Guide for this setting](https://claude.com/docs/third-party/claude-desktop/ssh-remote-sessions.md)

[Self-hosted install](#self-hosted-column): Not supported. Governs SSH sessions started from the person's computer, which self-hosted installs never offer.

> **More detail**
>
> When off, the SSH option is hidden and any connection attempt is refused.
>
> Entries are exact hostnames (`build01.corp.example.com`) or `*.` wildcards (`*.corp.example.com` matches the apex and subdomains at any depth); matching is case-insensitive and ignores a `user@` prefix. The list is compared with the `HostName` that the user's SSH configuration (`~/.ssh/config`) gives for the host they entered, or with the entered host itself when the configuration has no entry for it or cannot be evaluated. So an alias is allowed when the host it points to is listed, whatever the alias is called, and refused when it is not. A session's jump hosts (`ProxyJump`, or `ProxyCommand ssh -W %h:%p host`) must be listed too, by `HostName`. One the app fails to read, and any other `ProxyCommand` (`ssh -i`…), is permitted when the resolved host matches (this key governs which hosts the app offers, not network egress). The built-in SSH library refuses every `ProxyJump`.
>
> This is opt-in because a remote session runs Claude Code on the SSH host and the app forwards the session's inference credential to it, plus your OTLP collector endpoint and auth headers when `otlpEndpoint` is set. List only hosts you trust with those. Token-based credentials are forwarded. File-based credentials (Bedrock IAM Identity Center sign-in or AWS profile, Vertex Google sign-in or a credentials file) are never forwarded, and a session that needs one from the device is refused.
>
> If this key is unset, an `sshHostAllowlist` in Claude Code's own managed-settings file on the device still applies; when both are set, this key wins where the app's configuration is admin-managed (MDM, the admin console, or a device-managed bootstrap URL) and otherwise applies only while that file sets none. `allowedWorkspaceFolders` still applies on the remote host. Claude Code's managed settings on a host replace the sandbox, network, permission, and MCP rules this app sends unless they set `parentSettingsBehavior` to `"merge"`.

***

#### `sshClientPath`

string

Beta (The feature that the key configures is in beta.)

Consent required (A value that a bootstrap server or a self-hosted session host delivers applies only after the user approves it, unless machine-scoped device management set that server's address. For a bootstrap server, the trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)

Since 1.46388.1

**SSH client program.** Absolute path to the OpenSSH ssh program the app runs for SSH sessions. Unset: the first ssh on the user’s PATH.

[Guide for this setting](https://claude.com/docs/third-party/claude-desktop/ssh-remote-sessions.md)

[Self-hosted install](#self-hosted-column): Not supported. Names the ssh program on the person's computer, and self-hosted installs offer no SSH sessions.

> **More detail**
>
> Pins which OpenSSH client the app runs wherever it starts `ssh`: evaluating the user's SSH configuration (`ssh -G`), making the SSH connection and its channels, and the Code tab's terminal. `ssh-keygen` and `ssh-add` are taken from the same directory when they exist there, otherwise from PATH. The program must be OpenSSH 7.6 or newer. To carry the connection on Windows it must be Win32-OpenSSH 9.4 or newer, or another OpenSSH 8.5 or newer under Program Files, such as Git for Windows' `usr\bin\ssh.exe`, only where device policy, or the configuration server it names, sets this key and sets the SSH connection engine setting to `system-openssh`; the app points such a client at the `.ssh` folder of the user's Windows profile, and asks for a password, code or key passphrase only on a direct connection (no jump host, `ProxyCommand`, `Match exec`, `KnownHostsCommand`, `PKCS11Provider` or `SecurityKeyProvider`); otherwise only a key that needs nothing typed signs in. Set such a client only on desktops with one user. On macOS and Linux a wrapper script that ends in one is accepted, on Windows it must be an `.exe` (no .cmd, .bat or .ps1). When this key is set and the program is missing, cannot be run, or is too old, SSH sessions fail with an error telling the user to ask their IT administrator — the app never falls back to another ssh. The connection itself runs through this program on the system-OpenSSH engine, which the SSH connection engine setting's `system-openssh` value selects on every platform; when the app's built-in SSH library makes the connection instead, this key still governs configuration evaluation (`ssh -G`), host-key lookups (`ssh-keygen`) and the terminal. On a device that a Claude.ai sign-in has moved to an admin-console organization (see `disableDeploymentModeChooser`), the device profile's value is ignored: set the key in admin settings (which cannot name such a client). There, until the organization's configuration has loaded, no client is pinned.

***

#### `sshTransport`

enum

Beta (The feature that the key configures is in beta.)

Since 1.52386.0

**SSH connection engine.** Which SSH engine carries Code sessions: the OpenSSH ssh program on the device, or the app’s built-in SSH library. Unset or auto: the build’s default.

One of: `auto`, `system-openssh`, `builtin`

[Guide for this setting](https://claude.com/docs/third-party/claude-desktop/ssh-remote-sessions.md)

[Self-hosted install](#self-hosted-column): Not supported. Chooses the SSH engine on the person's computer, and self-hosted installs offer no SSH sessions.

> **More detail**
>
> `system-openssh`: the app makes every SSH connection by running an OpenSSH `ssh` program — the one `sshClientPath` names, otherwise the first `ssh` on the user's PATH (on Windows, a Win32-OpenSSH `ssh.exe`: the PATH one, else the in-box or Microsoft-installed client) — so the organization's own OpenSSH build, with its Kerberos/GSSAPI, certificate and `ssh_config` support, is what authenticates. The program must be OpenSSH 7.6 or newer (Windows: Win32-OpenSSH 9.4 or newer, or another OpenSSH that `sshClientPath` names: see that key). When `sshClientPath` is set and that program cannot be used, sessions fail with an error telling the user to ask their IT administrator rather than falling back; when it is unset and Windows has no usable client, the built-in library is used.
>
> `builtin`: the app's built-in SSH library makes the connection, whatever the build's default.
>
> `auto` or unset: the build's default engine.
>
> An explicit value overrides the default at each host's next connect or reconnect. An open app takes a device profile's change at its next configuration check. From a configuration server it takes only `builtin`, once two checks in a row return it (about 12 minutes by default); other values wait until it is reopened or the user signs in again. A value that cannot be read, such as a misspelling, counts as `builtin` and waits likewise. Once a server's configuration has loaded it decides, even if it omits the key; until then the device profile's value applies. On a device that a Claude.ai sign-in has moved to an admin-console organization (see `disableDeploymentModeChooser`), the device profile's value is ignored: set the key in the admin console. There, until the organization's configuration has loaded, the build's default engine is used.

***

### Chat surface

#### `chatTabEnabled`

booleanSince 1.13576.0

**Allow Chat.** Enable Chat. Quick questions and drafting.

[Self-hosted install](#self-hosted-column): Not supported. No Chat session can start on a session host, so the switch has nothing to turn on or off there.

***

#### `desktopHome`

enumSince 1.52386.0

**Desktop home.** Unifies Chat and Cowork into one home. When set, it replaces Allow Chat, Advanced file analysis, and Allow Cowork. Leave unset to keep those.

One of: `standard`, `off`

[Self-hosted install](#self-hosted-column): Server side. Alone decides Cowork, which is on only while this is unset or standard; else the host refuses it and Desktop hides it.

> **More detail**
>
> `standard` turns on Unified Claude, which combines Chat and Cowork into one experience. `off` turns Chat and Cowork off entirely. `isClaudeCodeForDesktopEnabled` still decides Code. Remove the key to hand control back to `chatTabEnabled`, `chatAdvancedFileAnalysisEnabled`, and `coworkTabEnabled`. Values are case-sensitive, so `Standard` is not recognized. A value that the app does not recognize is read as `off`, so update the app on devices before you deploy a value added in a later version.

***

#### `chatAdvancedFileAnalysisEnabled`

booleanSince 1.14271.0

**Advanced file analysis.** Allow Claude to run code in a local sandbox to analyze attached files it can’t read natively — like Excel and PowerPoint. Off by default.

[Self-hosted install](#self-hosted-column): Not supported. Configures a Chat session's local sandbox, and no Chat session can start on a self-hosted install.

> **More detail**
>
> Also enables inline data analysis. Of the user's own files, the sandbox can read only those attached to the conversation, plus folders added to the chat's project through the app (read-only).
>
> Commands in the sandbox can reach the hosts in `coworkEgressAllowedHosts`, and no others. If that list is unset or empty, they have no network access. With `*` in the list they can reach any host, as in Cowork. Plugin CLIs are the exception: they can always reach the hosts their plugin declares, plus the listed hosts (with `*`, only the declared hosts). Older app versions give the sandbox no network access by default.
>
> As in Cowork, commands run without an approval prompt. So they can upload anything the sandbox can read to a listed host, and run what they download from one. To have Claude ask before each command, set `Bash` to `ask` in `builtinToolPolicy`, which also applies to Cowork and Code. To let commands install packages, list the hosts of the package manager's default index (for pip, `pypi.org` and `files.pythonhosted.org`). For a private mirror, list its host instead. Nothing points package managers at a mirror, so each command must name it (for pip, `--index-url`).
>
> Project folders are not available in the sandbox of a chat started while a rule on `Read`, `Grep` or `Glob` is set: in `disabledBuiltinTools`, in `builtinToolPolicy` with a value other than `allow`, or as a deny or ask rule in Claude Code's own managed settings on the device, whether or not the rule covers the folder. They are not available either where those managed settings cannot be read, or where Claude Code takes its managed settings from a gateway. Claude's file tools still read what the rules allow.

***

### Workspace

#### `coworkEgressAllowedHosts`

string\[]Since 1.2581.0

**Allowed egress hosts.** Hosts agent tools may reach in Cowork and Chat (Code: in part). An empty list acts as unset for tools, but stops Claude opening sites in the built-in browser.

[Guide for this setting](https://claude.com/docs/third-party/claude-desktop/web-tools.md#web-fetch)

[Self-hosted install](#self-hosted-column): Server side. Tools in the host's sessions make the network calls, so the host limits which addresses they may reach.

> **More detail**
>
> Applies only to **tool calls**, in Cowork, Code and Chat. In Cowork it covers the sandbox's web fetch, shell commands and package installs. In Chat it covers web fetch and commands in the file-analysis sandbox. In Code it's [translated into Claude Code's network sandbox allowlist](https://claude.com/docs/third-party/claude-desktop/code.md#applied-as-managed-policy), and by default a separately deployed Claude Code managed-settings file takes precedence. It does **not** cover Web Search (which runs at your inference provider), inference, or MCP traffic. A list other than `*` also bounds where Claude may browse in the built-in browser. When unset, Cowork and Chat refuse web fetch.
>
> Entries are exact hostnames (`api.github.com`), wildcards (`*.corp.com` matches subdomains at any depth, not `corp.com` itself), or `*` to allow all. IP addresses match only when listed exactly. In Cowork and Chat, web fetch always blocks `localhost` and private addresses, and shells reach only listed hosts (not your inference provider's, unless listed), or none when unset. Code's shell obeys that limit only on macOS, and with bubblewrap and socat on Linux or WSL2; elsewhere, Windows included, it reaches any host. Code's web fetch isn't limited.
>
> Any entry except bare `*` may carry a `:port` suffix (`*.corp.com:8443`) restricting it to that port. IPv6 literals are not supported. Invalid entries are dropped with a log warning and the rest still work. An unreadable value counts as an empty list. Ports are enforced for the Cowork sandbox's web fetch, shell, and package-install egress; plugin CLIs also reach hosts their plugin declares and ignore port-scoped entries for now, and the Code translation treats them as the bare host. Only deploy port-scoped entries once your whole fleet supports them (`disableAutoUpdates` pins builds). On an older build, a single one invalidates the session's whole shell and package-install allowlist.
>
> Open listed hosts on your network firewall too.

***

#### `allowedWorkspaceFolders`

object\[]Since 1.2581.0

**Allowed workspace folders.** Folders where Claude may work. Applies to Cowork and Code sessions and to the project folders a chat reads. Leave unset for unrestricted access.

[Self-hosted install](#self-hosted-column): Server side. The host refuses file access outside folders listed as full paths, and Desktop checks those listed with \~ or a variable.

> **More detail**
>
> Paths can reference `~` and these environment variables, expanded per user: `%OneDrive%`, `%OneDriveCommercial%`, `%OneDriveConsumer%`, `%APPDATA%`, `%LOCALAPPDATA%`, `%USERNAME%`, `%XDG_DOCUMENTS_DIR%`. The set is fixed; an entry that references any other `%VAR%`, or one that is unset on the device, allows none.
>
> Each folder is interpreted on the machine the session runs on. For a Code session on an SSH host, `~` means the remote user's home, an entry that references a `%VAR%` allows none there, and the session's working directory must be inside one of the folders as they exist on that host. One list serves every machine: `["~/work", "/srv/work"]` governs `~/work` for each user, on a managed Mac or a Linux host, and `/srv/work` on a host that has it. A folder that names nothing real on a given machine allows nothing there. On an SSH host, an entry counts only if it is an absolute path as that host spells one (`~/work`, not `work`; on Windows `C:\work`, not `\work`), with no `..`. On Linux or Mac a `\` counts as `/`, except a leading `\\`. One inside another listed folder does not count on its own (its read-only mode still applies); if it is a link, list the folder it points to. An empty list allows none; unset leaves access unrestricted.
>
> A listed folder is one Claude may write as well as read, unless the entry's `mode` (Access mode in Setup) makes it read-only; that field's own description says how far read-only reaches. A Code session can reach every listed folder, not only the one it was opened in. Setting this key also turns on Claude Code's sandbox where it runs (macOS, or Linux and SSH hosts with bubblewrap): there a shell command normally writes in the listed folders without an approval prompt, and its writes to most other places, such as a package cache in the home directory, are refused. A home directory holds shell start-up files and SSH keys, so list work folders, not a whole home directory.
>
> The list also limits which folders of a project a chat reads.

> **Child attributes (3)**
>
> **path** `string` *required*
>
> Absolute folder path. May start with \~ or one of the listed %VAR% tokens, expanded per user. Subfolders are included.
>
> **isDefaultSelected** `boolean`
>
> Shows as a folder chip on the new-task page and skips the trust prompt. Users can remove it.
>
> **mode** `enum`
>
> Read-only folders can be viewed and searched but not modified in Cowork. In Code, applies to file tools only. Over SSH, also to Bash in its sandbox.
>
> One of: `rw`, `ro`
>
> > **More detail**
> >
> > Read-only folders can be viewed and searched but not modified in Cowork (by Claude or via the UI). Bash runs in Cowork's isolated workspace where the folder is mounted read-only at the OS level; file-tool writes (Edit, Write) are blocked in-process by Claude Desktop.
> >
> > In local Code sessions, read-only applies to Claude's file tools only; Bash does **not** yet enforce it.
> >
> > In SSH sessions (earlier versions ignore the mode on the host), read-only is enforced by Claude Code's own permission rules: its file tools cannot modify the folder. A writable folder inside a read-only one is read-only too. Shell commands are stopped only where Claude Code's sandbox runs (Linux needs bubblewrap and socat), and only as far as that sandbox goes: keep read-only folders outside writable ones, and use the operating system's permissions where a folder must not change. The sandbox does not cover a path with `* ? [ ] ( ) { } | +` or a double quote. List each folder by its real path: shell commands may not be stopped in a folder listed through a link. Not enforced on Windows hosts, nor on a host with Claude Code managed settings of its own unless they set `parentSettingsBehavior` to `merge`. Not covered: MCP servers, hooks, the terminal, commands in `sandbox.excludedCommands`, and git worktrees, which Claude Desktop and Claude Code still create inside the folder.
> >
> > If a read-only entry's `%VAR%` cannot be filled in (unset, unsupported, or any `%VAR%` over SSH), the folder above the variable is read-only instead, or every listed folder if the entry names none above it. A variable that only another operating system sets (`%APPDATA%` on macOS) leaves the entry without effect while it is unset there.
> >
> > A read-only folder that contains Claude's own data directory (for example the home folder; over SSH, `~/.claude` on the host) is enforced in Cowork only. Configure narrower folders for Code coverage. Over SSH, keep a Claude Code config folder moved by `CLAUDE_CONFIG_DIR` outside read-only folders.

***

#### `blockReadsOutsideWorkingDirectories`

booleanSince 1.46388.1

**Block reads outside working directories.** Keep Claude from reading files outside a Code session’s working directories. File tools refuse such reads; sandboxed shell commands lose the home directory.

[Self-hosted install](#self-hosted-column): Server side. The host starts Code sessions, so it hands Claude Code the block on reads outside their folders.

> **More detail**
>
> When set to `true`, Code sessions refuse reads outside their working directories (the session folder plus any `allowedWorkspaceFolders`). The file tools (Read, Grep, Glob) refuse them in every permission mode; where Claude Code's sandbox runs (macOS, or Linux and SSH hosts with bubblewrap, once `allowedWorkspaceFolders` is set or an egress allowlist applies: in third-party deployments one applies unless `coworkEgressAllowedHosts` contains `*`, in first-party deployments none does) shell commands cannot see the home directory and other user folders (`/Users`, `/home`, mounted volumes) and a read there is refused with no prompt; elsewhere (Windows, Linux without bubblewrap, or neither folders nor an egress allowlist in effect) such shell reads prompt for approval. The app keeps the user's git configuration files (which may themselves embed credentials such as URL tokens; a symlinked one stays hidden), its own Claude Code installation, and the session's plugin and attachment folders readable (not on a Windows SSH host, where plugin files and attachments stay out of the file tools' reach under the block). An allowed folder that is or contains the home directory leaves it readable.
>
> Users can re-open folders (even their whole home) in their own Claude Code settings with `sandbox.filesystem.allowRead` or `permissions.additionalDirectories`; settings files tracked in a git repository cannot. The key travels on Claude Code's managed-settings channel: another Claude Code managed-settings source replaces it unless that source sets `parentSettingsBehavior` to `"merge"`, and one that sets `sandbox.filesystem.allowManagedReadPathsOnly` reduces it to approval prompts. This is `permissions.blockReadsOutsideWorkingDirectories` in Claude Code's [managed settings](https://claude.com/docs/third-party/claude-desktop/code.md#interaction-with-claude-code%E2%80%99s-own-managed-settings).
>
> Unset (default): nothing changes.

***

#### `autoModeEnabled`

booleanSince 1.10628.0

**Allow Auto mode.** Offer Auto mode in Code (on unless set to false); set to true to also offer it in Cowork as “Automatically approve”. Claude decides which actions need approval.

[Self-hosted install](#self-hosted-column): Server side. The host allows or refuses Auto mode for the sessions it runs, and tells Desktop what to offer.

> **More detail**
>
> Left unset, users can select **Auto mode** in Code and new Code sessions start in it; a mode the user already chose, or a Claude Code settings file's `permissions.defaultMode`, takes precedence, and Cowork does not offer it. Set to `true` to also offer **Automatically approve** in Cowork (Cowork sessions still start by asking before each action until the user picks it). Set to `false` to remove the option from both tabs. In Auto mode Claude runs a safety classifier on each action and only prompts for approval on actions it judges risky, instead of following the static per-tool policy.
>
> Requires a session model that supports the safety classifier — which models qualify depends on the deployment's provider and the app version. With a model that lacks support the option is greyed out and Code sessions do not start in it. `builtinToolPolicy` and this key may both be set; Auto mode is a user-selectable option alongside the default policy, not a replacement for it.
>
> By default on a gateway, the safety classifier sends its own requests through your gateway to Claude Sonnet 5, whatever model the session uses. Make sure your gateway accepts the exact ID `claude-sonnet-5` and the `context-1m-2025-08-07` value in the `anthropic-beta` request header. If you set `inferenceModels`, list that ID there and in any group's model list (no `supports1m` needed). Sonnet 5 then also shows in the model picker. If the gateway rejects those requests or the list omits the ID, Auto mode stays available but can block actions it would otherwise allow. In Code, users see those actions marked **Blocked**.
>
> In Code sessions, a separately deployed Claude Code [managed-settings](https://claude.com/docs/third-party/claude-desktop/code.md#interaction-with-claude-code%E2%80%99s-own-managed-settings) file that sets `disableAutoMode` to `"disable"` also keeps Auto mode hidden and off, whatever this key says.

***

#### `disableBypassPermissionsMode`

booleanSince 1.46388.1

**Disable bypass permissions mode.** Remove the bypass permissions mode from Code sessions and Cowork tasks, so Claude always follows the permission policy. Off by default.

[Self-hosted install](#self-hosted-column): Not supported. A session host never offers bypass mode, so every session it runs already has it off.

> **More detail**
>
> When set to `true`, sessions cannot run in bypass permissions mode: the app stops offering the mode in Code and Cowork, and a session that requests it anyway is downgraded. This is the `disableBypassPermissionsMode` setting from the `permissions` section of Claude Code's [managed settings](https://claude.com/docs/third-party/claude-desktop/code.md#interaction-with-claude-code%E2%80%99s-own-managed-settings); a separately deployed Claude Code managed-settings file that sets it to `"disable"` also removes the mode, whichever source sets it.
>
> Unset (default): users the deployment otherwise allows can choose bypass permissions mode.

***

#### `disableBundledSkills`

booleanSince 1.15962.0

**Disable bundled skills and workflows.** Disables Claude Code’s bundled skills and workflows (deep-research and similar). Use where WebFetch/WebSearch aren’t available.

[Self-hosted install](#self-hosted-column): Server side. The host starts Claude Code, so it is the one that turns the bundled skills off.

***

#### `skillCreationEnabled`

booleanSince 1.25927.0

**Allow user-created skills.** Allow users to create and upload their own skills. When off, the creation and upload surfaces are hidden and the agent’s skill-creation tools are disabled.

[Self-hosted install](#self-hosted-column): Server side. The host stores people's skills, so when this is off it refuses new ones and tells Desktop to hide creation.

> **More detail**
>
> When on (default), users can create new skills and upload skill files in the app. Set to `false` to block user skill creation: the skill-creation and upload surfaces are hidden (the `skill_creation` feature is served as blocked by the organization), and the agent's skill-creation tools (saving skills from a conversation, skill proposals) are not offered in sessions — the same effect as turning off the **User-created skills** organization setting available to claude.ai enterprise admins.
>
> This is a feature-availability control enforced in the app's UI, not a data boundary: skills are files on the user's machine, and files already present there (or placed there outside the app) are not removed or blocked by this key. Skills themselves remain usable; organization-distributed plugins and bundled skills are unaffected (to disable bundled skills, use `disableBundledSkills`).

***

#### `userPluginMarketplacesEnabled`

booleanSince 1.37937.0

**Allow user-added plugin marketplaces.** Allow users to add plugin marketplaces. When off, marketplaces your organization did not provision are hidden and the app’s sessions do not load their plugins.

[Self-hosted install](#self-hosted-column): Server side. Desktop hides and refuses adding a marketplace when off; no session host loads a person's own marketplaces yet.

> **More detail**
>
> When on (default), users can add plugin marketplaces from the plugin browser. Set to `false` to restrict plugins to your organization's marketplaces: the add-marketplace surfaces are hidden, and the app refuses adds that still reach it (deep links, stale UI). Any other marketplace present on the device is then hidden in every tab, whether a user added it in the app earlier or something outside the app registered it (for example Claude Code in a terminal, under `~/.claude`): its plugins are not listed, and installs and updates from it are refused. The sessions the app starts load plugins only from your organization's marketplaces, the organization plugins directory, the app's own uploads and the user's own skills folder, enforced through Claude Code's marketplace allowlist (`strictKnownMarketplaces`, passed as the app's managed settings). Nothing is deleted: removing the key or setting it back to `true` restores them. Marketplaces provisioned by your organization (`allowedPluginMarketplaces`) and the organization plugins directory are unaffected, and plugins users uploaded are governed by `userPluginUploadsEnabled`, not this key.
>
> This is a feature-availability control, not a data boundary. Claude Code in a terminal reads the same `~/.claude` folder and is governed only by its own managed settings, not by this key. Claude Code may ignore this allowlist on a device that deploys its own Claude Code managed settings; restrict marketplaces in those settings as well.
>
> This key applies only while the app runs in third-party mode. If users could otherwise sign in to Claude.ai on the device, also set `disableDeploymentModeChooser` so the app stays in third-party mode.

***

#### `userPluginUploadsEnabled`

booleanSince 1.37937.0

**Allow user-added plugins.** Allow users to add their own plugins. When off, every in-app option for adding one is hidden and uploads that still reach the app are refused.

[Self-hosted install](#self-hosted-column): Server side. The host keeps the plugins people upload and loads them in their sessions, and refuses new ones when this is off.

> **More detail**
>
> When on (default), users can upload plugin files and create plugins with Claude. Set to `false` to stop users adding plugins of their own: every in-app option for doing so is hidden, and the app refuses uploads that still reach it.
>
> This is a feature-availability control enforced in the app, not a data boundary: plugins already installed (or placed on disk outside the app) are not removed or blocked by this key. Plugins from organization-provisioned marketplaces and the organization plugins directory are unaffected.
>
> This key applies only while the app runs in third-party mode. If users could otherwise sign in to Claude.ai on the device, also set `disableDeploymentModeChooser` so the app stays in third-party mode.

***

#### `scheduledTasksEnabled`

booleanSince 2.110.0

**Allow scheduled tasks.** Allow scheduled tasks in Cowork and Code. When off, the Scheduled page is hidden, existing tasks stop running, and Claude cannot create new ones.

[Self-hosted install](#self-hosted-column): Server side. The host runs scheduled tasks, so when this is off it refuses to create or run them.

> **More detail**
>
> When on (default), users can schedule Cowork tasks and Code sessions to run later or on a recurring schedule, and Claude can create such schedules when asked.
>
> Set to `false` to turn scheduled tasks off for every user. The Scheduled section in Cowork and the routines list in the Code tab are hidden, together with every other place a schedule can be created. Tasks that already exist on a device no longer run; they are kept, not deleted, and run again once the key is removed or set to `true`. Claude is not offered the tools that create, change or run these tasks, and sessions start without Claude Code's own in-session scheduling tools (the `/loop` command, its cron tools and its wake-up timer).
>
> It does not remove task files already on the user's machine. A change takes effect at the next app launch.

***

#### `keepAwakeEnabled`

booleanSince 2.7032.0

**Allow keep awake.** Let Claude keep the computer awake. When off, Claude never prevents sleep and hides the keep-awake switches in Settings, the Scheduled page and the Code tab.

[Self-hosted install](#self-hosted-column): Server side. Desktop itself asks the person's computer to stay awake, and shows the keep-awake switches.

> **More detail**
>
> When on (default), users can turn on **Keep computer awake** (Settings → This computer → System, also shown as **Keep awake** on the Scheduled page in Cowork and the Routines page in Code) so the computer does not idle-sleep while Claude is open and scheduled tasks keep running on an idle machine. The Code tab can also keep the computer awake while a session is working (**Keep computer awake while Claude works** in Settings → Claude Code, and a session's **Keep computer awake** menu item).
>
> Set to `false` to make sure Claude never prevents the computer from sleeping: those switches are hidden and no part of the app keeps the computer awake. Users' saved choices are kept but ignored, and apply again once the key is removed or set to `true`. Scheduled tasks are unaffected and still run only while the computer is awake and the app is open.
>
> A change takes effect on a running app.

***

#### `developerModeEnabled`

booleanSince 2.37337.1

**Allow Developer Mode.** Let users turn on Developer Mode. When off, the app’s developer tools and the option to install an unpacked extension are unavailable.

[Self-hosted install](#self-hosted-column): Server side. Desktop offers its own Developer menu, developer tools and debugger on the person's computer.

> **More detail**
>
> When on (default), a user can turn on **Developer Mode** (Help → Troubleshooting → Enable Developer Mode), which adds the **Developer** menu and lets them open the developer tools (Chrome DevTools, Inspect Element) and a debugger for the app's main process.
>
> Set to `false` to keep Developer Mode off on every device that receives this setting: the **Developer** menu and the Help → Troubleshooting → Enable Developer Mode item are removed, the developer tools and the debugger cannot be opened (any already open are closed), a user's own `developer_settings.json` opt-in is ignored, and the app refuses to install an extension from a folder. Packaged (`.mcpb`) extensions are governed by `isDesktopExtensionEnabled`, not this key.
>
> This is a feature control, not a sandbox: extensions already installed from a folder stay installed and keep working, and an extension folder copied into the app's extensions folder by hand is not blocked.
>
> A change takes effect on a running app, except that the **Install unpacked extension** button in Settings keeps its launch-time state until the app restarts (clicking it while the key is off shows an error).

***

#### `quickEntryDefaultShortcut`

stringSince 3.1623.0

**Default Quick Entry shortcut.** Set the shortcut that opens Quick Entry, such as Ctrl+Alt+K, for users who haven’t set their own in Settings. Use “off” for no shortcut.

[Self-hosted install](#self-hosted-column): Server side. Desktop registers its Quick Entry shortcut with the operating system of the person's computer.

> **More detail**
>
> Sets the default shortcut for Quick Entry, the small prompt window that opens over other apps. It replaces Claude's built-in shortcut (double-tap Option on macOS, Ctrl+Alt+Space on Windows and Linux) for users who haven't chosen their own.
>
> This is a default, not a lock. A shortcut that a user saves in Settings → This computer → System (**Quick access shortcut** on macOS, **Quick Entry keyboard shortcut** on Windows and Linux) takes precedence, including one saved before this key was set.
>
> Accepted values:
>
> * Modifiers and one key joined by `+`, such as `Ctrl+Alt+K` or `Alt+Space`. Modifiers include `Ctrl`, `Alt`, `Shift`, `Cmd` and `Super`. `CommandOrControl` means Cmd on macOS and Ctrl elsewhere, so one value works on every platform. A combination must pair `Ctrl`, `Cmd` or `Super` with `Alt` or `Shift`, except for `Alt+Space`. Write modifier and key names exactly as shown: `ctrl` is not read as `Ctrl`.
> * `off` (the string, not `false`): no shortcut. Users can still open Quick Entry from Claude's tray or menu bar icon and set a shortcut in Settings.
> * `double-tap-option`: macOS only. Windows and Linux keep the built-in shortcut.
>
> While Claude is running, other apps don't receive this shortcut. So Claude rejects other combinations, such as `F11`, `Ctrl+C`, `Shift+K` or `Alt+Shift+K`, which typing and other apps rely on. It also rejects any combination that includes `Insert`, `Capslock` or `F5`, which screen readers use. Choose a combination that users don't need elsewhere.
>
> If Claude can't use the value as a shortcut, it ignores the value and keeps the built-in one. If another app already uses the shortcut, Claude on macOS uses the built-in shortcut. On Windows and Linux, Quick Entry keeps its previous shortcut, or none at start-up. Users can choose another in Settings.
>
> A change takes effect on a running app.

***

#### `quickEntryScreenshotsEnabled`

booleanSince 3.6556.1

**Allow screenshots of the screen and other apps.** Let users take screenshots of their screen or other apps’ windows in Quick Entry on macOS. When off, it offers none and never asks for Screen Recording access.

[Self-hosted install](#self-hosted-column): Server side. Desktop takes the picture on the person's computer and offers it in its own Quick Entry window.

> **More detail**
>
> When on (default), Quick Entry on macOS lets a user click another app's window, or drag over part of the screen, to attach a picture of it to their prompt. Until the user grants the macOS Screen Recording permission, Quick Entry shows a **Turn on screenshots** button that asks for it.
>
> Set to `false` to turn this off on every device that receives this setting. Quick Entry still opens, but offers no screenshot and no such button, and Claude does not ask for that permission. Outside Quick Entry, another app's window that a user mentions with @ in a chat comes without its picture. Users cannot turn it back on.
>
> With `quickEntryFileSharingEnabled` off as well, Quick Entry shows no permission banner at all.
>
> On Windows and Linux, Quick Entry takes text only, so this key changes nothing there.
>
> This key does not cover:
>
> * A screenshot that a user takes with the operating system's own tools and then pastes or attaches. That is a file upload.
> * Pictures that Claude takes of its own content, such as an artifact, a file preview, a page in the built-in browser (`builtinBrowserEnabled`) or the feedback form.
> * A local MCP server or desktop extension that captures the screen (`isLocalDevMcpEnabled`, `isDesktopExtensionEnabled`).
> * Other apps, or the operating system, capturing Claude's windows.
>
> A change takes effect on a running app.

***

#### `quickEntryFileSharingEnabled`

booleanSince 3.6556.1

**Allow sharing files open in other apps.** Let users attach the file open in another app’s window in Quick Entry on macOS. When off, it offers none and never asks for Accessibility access.

[Self-hosted install](#self-hosted-column): Server side. Desktop finds the file on the person's computer and offers it in its own Quick Entry window.

> **More detail**
>
> When on (default), Quick Entry on macOS offers, on another app's window, to attach the file that is open in it to the user's prompt. Claude learns which file that is through the macOS Accessibility permission. Until the user grants it, Quick Entry shows a **Turn on file sharing** button that asks for it.
>
> Set to `false` to turn this off on every device that receives this setting, including devices where the permission is already granted. Quick Entry still opens, but offers no file from another app's window and no such button, and it does not ask for that permission. Outside Quick Entry, another app's window that a user mentions with @ in a chat comes without its file. Users cannot turn it back on.
>
> With `quickEntryScreenshotsEnabled` off as well, Quick Entry shows no permission banner at all.
>
> On Windows and Linux, Quick Entry takes text only, so this key changes nothing there.
>
> This key does not cover:
>
> * A file that a user attaches, pastes or drags into Claude themselves. That is a file upload.
> * Claude's other uses of the Accessibility permission where a user has granted it, such as telling a double tap of Option from a keyboard shortcut.
>
> A change takes effect on a running app.

***

#### `skipWebFetchPreflight`

booleanSince 1.37937.0

**Skip WebFetch domain check.** Skip Claude Code’s WebFetch domain lookup against api.anthropic.com in Code sessions. Off by default; turn on when that host is blocked.

[Self-hosted install](#self-hosted-column): Not supported. A session host always skips the web fetch preflight check, whatever is written.

> **More detail**
>
> Before fetching a page, Claude Code's WebFetch tool asks `api.anthropic.com` whether the domain is on Anthropic's content blocklist, and refuses the fetch if that lookup cannot complete. Third-party deployments route inference elsewhere and often block `api.anthropic.com` at the firewall; with the lookup on, every WebFetch in Code sessions then fails with "Unable to verify if domain … is safe to fetch", and where the host is reachable, every fetched hostname is sent to Anthropic. (Cowork sessions fetch through the app's own allowlisted fetch and never run this lookup.)
>
> Off (default): the lookup runs as it does today, so `api.anthropic.com` must be reachable from users' machines for Code-session WebFetch to work (listed under Egress Requirements). Set to `true` when users' machines cannot reach `api.anthropic.com` (corporate firewall, government network) or you do not want fetched hostnames sent there: Code sessions then fetch without the lookup and never contact that host for it. This is the same `skipWebFetchPreflight` setting Claude Code reads from its own [managed-settings](https://claude.com/docs/third-party/claude-desktop/code.md#interaction-with-claude-code%E2%80%99s-own-managed-settings) file; the app passes it to every session it starts. This key does not restrict which domains Claude may fetch. Neither does `coworkEgressAllowedHosts` in Code sessions, where it only pre-approves its hosts; `builtinToolPolicy` can require approval for every fetch.

***

#### `builtinToolPolicy`

object: name → valueSince 1.8089.0

**Built-in tool policy.** Approval per tool or rule such as Bash(curl \*). “ask” prompts the user before each matching call. “allow” is the default. To block, use Disabled built-in tools.

[Self-hosted install](#self-hosted-column): Server side. The host hands each session the admin's allow or ask rule for each built-in tool.

> **More detail**
>
> Keys use the same tool names and argument-scoped rule syntax as **Disabled built-in tools** (`disabledBuiltinTools`), and scopes apply in the same sessions. A bare `Bash` key also governs Claude Code's `PowerShell` tool (its shell on Windows PCs without Git for Windows); argument-scoped `Bash(…)` keys do not. Scoped **ask** rules reach sessions only through Claude Code's managed-settings channel, so another Claude Code managed-settings source replaces them unless it sets `parentSettingsBehavior` to `"merge"` (bare names hold either way). They need the same fleet-wide build support, and an older build drops a scoped **ask** entry as a configuration error (which also blocks WSL sessions on Windows until that client updates), so the tool runs unprompted.
>
> An **ask** entry, bare or scoped, also turns off the app's remembered “always allow” choices for that tool, so each prompted call is confirmed individually. **ask** on a file tool (`Read`, `Write`, `Edit`, `Glob`, `Grep`) prompts in Cowork, Chat and Code sessions. Calls that Cowork and Chat always refuse are still refused without a prompt: paths outside the session's connected folders (in Chat, outside its scratch directory and its project's folders) and protected or sensitive files inside them. A scheduled task in Cowork waits at the prompt, which appears in the task's session and, when that session is not in view, as a desktop notification. Code side chats cannot prompt, so they block matching calls. An unusable entry is dropped and recorded as a configuration error; a value other than `allow` or `ask` is treated as `ask` and reported. To remove a tool or deny a rule outright, use **Disabled built-in tools** instead.

***

#### `disabledBuiltinTools`

string\[]Since 1.2581.0

**Disabled built-in tools.** Built-in tools, or argument-scoped permission rules such as Read(//\*\*/.env), denied in Cowork and Code.

[Self-hosted install](#self-hosted-column): Server side. The host starts each session with the built-in tools and tool uses the admin denies turned off.

> **More detail**
>
> Each entry is a Claude Code [tool name](https://code.claude.com/docs/en/tools-reference) such as `Bash`, `Edit`, `WebFetch` or `WebSearch`, or an argument-scoped [permission rule](https://code.claude.com/docs/en/permissions#permission-rule-syntax) such as `Bash(curl *)` or `Edit(//**/*.env)`. A bare name covers every call (a bare `Bash` entry also covers the `PowerShell` tool); a scoped rule covers matching calls in every permission mode, including Auto and bypass. Scopes are matched for `Bash(…)` and `PowerShell(…)` (a command pattern) and for file paths written as `Read(…)` (covers `Read`, `Grep`, `Glob`) or `Edit(…)` (covers `Edit`, `Write`, `NotebookEdit`); many other tools take `Tool(<field>:<pattern>)`. `WebSearch` and `WebFetch` are bare-name only: to allow specific hosts, use `coworkEgressAllowedHosts`.
>
> Scoped `Bash(…)` rules apply in Code sessions only; Cowork's shell follows only a bare `Bash` entry. Start absolute file paths with `//`, not `/`: a relative pattern such as `Read(**/.env)` covers only a Code session's project folder and none of Cowork's connected folders. Scoped rules need fleet-wide build support (`disableAutoUpdates` pins builds): an older build passes a scoped entry to Claude Code unchecked. An entry whose pattern contains `)` followed by a space or comma is enforced only through Claude Code's managed-settings channel, so another Claude Code [managed-settings source](https://claude.com/docs/third-party/claude-desktop/code.md#interaction-with-claude-code%E2%80%99s-own-managed-settings) replaces it unless that source sets `parentSettingsBehavior` to `"merge"`; every other entry is enforced either way.
>
> An unusable entry (a tool name in the wrong letter case, an unbalanced parenthesis, a scoped `WebSearch(…)` or `WebFetch(…)`) is kept, because the deny list is served exactly as written, and raises a configuration warning.

***

#### `toolSearchEnabled`

booleanDefault: falseSince 1.21459.0

**Enable tool search.** Load MCP tool schemas on demand (tool search) instead of inlining every schema into context.

[Guide for this setting](https://claude.com/docs/third-party/claude-desktop/gateway.md#mcp-tool-search)

[Self-hosted install](#self-hosted-column): Server side. The host starts Claude Code, so it turns tool search on or off for its sessions.

> **More detail**
>
> When enabled, Cowork, Code, and Chat sessions place only tool names in context up front, and Claude fetches a tool's full schema the first time it needs it. Use this when many MCP tools are configured and their inlined schemas crowd out the context window. If your endpoint does not accept the request shape it then receives, requests fail with HTTP 400.
>
> * **Claude API, Vertex AI, Bedrock, or Bedrock Mantle with no custom base URL**: not needed. The app leaves Claude Code's experimental betas on there, as terminal Claude Code does, so tool search is on by default (on Vertex AI, for Claude 4.5 and newer models). To turn it off in Code, Cowork, and Chat, set `ENABLE_TOOL_SEARCH` to `false` in the `env` block of OS-level Claude Code managed settings (with `parentSettingsBehavior: "merge"`). Earlier app versions treat these like the last case.
> * **Gateway provider, app versions bundling Claude Code 2.1.247 or later**: requests add only the tool-search shape (the `tool-search-tool-2025-10-19` `anthropic-beta` value, deferred tool loading, `tool_reference` content blocks); every other experimental Claude Code beta stays suppressed. OS-level Claude Code managed settings that keep that suppression or turn `ENABLE_TOOL_SEARCH` off still win; set `ENABLE_TOOL_SEARCH` to `force` there instead (with `parentSettingsBehavior: "merge"`). Sessions the app runs in Claude Code's gateway mode (an opt-in for users on the gateway's own sign-in) get its gateway-safe tool-search shape instead.
> * **Foundry, a custom base URL, and earlier app versions**: the app suppresses Claude Code's experimental betas for the session and the key lifts that, so requests carry the tool-search shape together with Claude Code's other experimental betas for that provider. On Vertex with app versions bundling Claude Code older than 2.1.221, leave this unset while any model older than Claude 4.5 is in use; those engines send the header regardless of model and Vertex's pre-4.5 stacks reject it.

***

#### `organizationInstructions`

stringSince 1.37937.0

**Organization instructions.** Appended to Claude’s system prompt in Chat, Cowork, and Code. Guidance the model follows, not an enforced control. Up to 3,000 characters.

[Self-hosted install](#self-hosted-column): Server side. The host adds the admin's instructions to every session it starts.

> **More detail**
>
> Free-text instructions from your organization that Claude Desktop appends, in a clearly delimited block, after its own system prompt in **Chat**, **Cowork**, and **Code** (every chat, task, and Code session, including the sub-agents they spawn): for example house style, data-handling rules, or topics to decline. The model is told these instructions come from the organization's administrator and take priority over a user's personal preferences.
>
> This is guidance the model follows, not an enforced control: like any system-prompt text it steers the model's behavior and is usually honored, but it does not guarantee an outcome and is not a substitute for the restriction keys (tool policy, egress allowlist, folder allowlist). The app's own system prompt is never replaced or shortened by this key; in Code sessions it is added after Claude Code's own prompt and any `CLAUDE.md` instructions still apply.
>
> Read from the app's loaded configuration when a session starts; a changed value generally takes effect for sessions started after the next app launch. Leading and trailing whitespace is trimmed; an empty string is treated as unset. Maximum 3,000 characters; a longer value is rejected (the key is ignored with a configuration error) rather than truncated. Line breaks are preserved when the value is delivered as JSON, a bootstrap response, a `.mobileconfig` profile, or a `.reg` file; the Group Policy (ADMX) and Intune text box for this setting is single-line.

***

#### `requireCoworkFullVmSandbox`

booleanDefault: false

Deprecated (On third-party deployments Claude Desktop no longer reads the key and ignores any value set for it. Remove it from your configuration.)

Since 1.2581.0

**Require full VM sandbox.** Runs tools inside an isolated VM instead of the host. Stronger isolation; slower file access and no host-process tools.

[Self-hosted install](#self-hosted-column): Not supported. Chooses how Cowork runs on the person's own computer, and third-party installs no longer read it.

[Admin Console](#the-works-with-column): Not available.

***

### Authentication

#### `disableDeploymentModeChooser`

booleanDefault: falseSince 1.3834.0

**Disable Claude.ai sign-in.** Users see only this provider at the login screen. The option to sign in to Claude.ai is hidden.

[Self-hosted install](#self-hosted-column): MDM profile. Shapes Desktop's sign-in screen and configuration source, settled before Desktop reaches the host.

[Admin Console](#the-works-with-column): Not available.

> **More detail**
>
> Set in a device-management profile, this key also keeps that profile in charge. Without it, a user who signs in to Claude.ai with an organization whose Claude Desktop deployment is configured in the admin console moves the device to that organization's configuration, at later launches too. The profile then still supplies what no configuration server can deliver, such as the network proxy, and a few device safeguards, such as `sessionRetentionHold`; every other key, update keys included, comes from the organization's configuration. A profile that sets only app-behavior keys (`disableAutoUpdates`, …) and no other key, not even `forceLoginOrgUUID`, is not affected: it keeps those keys over the organization's configuration without this key, and adding this key there would make the profile the device's whole configuration. The account menu offers the way back to a profile that sets a provider or a server. `forceLoginOrgUUID` in the profile limits the move to the organizations it lists. A value served only by the profile's own `bootstrapUrl` server does not keep the device.

***

#### `disableDeepLinkRegistration`

booleanDefault: falseSince 1.6889.0

**Disable claude:// deep-link handling.** Stop external apps and websites from opening Claude Desktop via claude:// links.

[Self-hosted install](#self-hosted-column): MDM profile. Desktop registers claude:// links on the person's computer at launch, before it has signed in to the host.

***

### Built-in browser

#### `builtinBrowserEnabled`

booleanDefault: falseSince 2.2553.0

**Allow the built-in browser.** Offer the built-in browser in Cowork and Code sessions so users and Claude can open and work with web pages. Site sign-ins stay on the device until cleared.

[Self-hosted install](#self-hosted-column): Not supported. The browser pane lives in Desktop on the person's computer, and host sessions get no browser tools.

[Admin Console](#the-works-with-column): Set automatically.

> **More detail**
>
> When enabled, Cowork and Code sessions get a built-in browser pane. Users can open any site in it; Claude can open, read, and act on pages with its browser tools once the user approves each site (private-network hosts ask again per action unless the user always allows the host). Pages load directly from the user's machine, so your network controls apply; the pane's sign-ins and cookies stay in the app's browser profile on the device until cleared.
>
> Off (default): no browser pane; Code sessions keep the localhost-only dev-server preview. With `bootstrapUrl` set, put this key in the served configuration: a device-profile value alone leaves the browser off. On an install managed from the Claude admin console this follows the console's Built-in browser switch.
>
> When a public site opens or is framed in the pane, and before Claude works with it, the app checks its address (query removed) against Anthropic's site safety list on `releases.claude.com`, signed out, with no account, organization, or device identifier (admin console installs: signed in, on the host that serves their configuration). A site it blocks stays blocked to Claude under every key below. Private addresses, names resolving to them, and internal-suffix or single-label names are never sent (a name under a public domain is checked even if only your VPN resolves it). Allow `releases.claude.com` through your firewall: if a check fails, users can browse but Claude's page tools stay off for that site.
>
> `builtinBrowserDefaultDomainPolicy` and its two site lists restrict where Claude may browse. A separately deployed Claude Code [managed-settings](https://claude.com/docs/third-party/claude-desktop/code.md#interaction-with-claude-code%E2%80%99s-own-managed-settings) file still applies: `disableBrowserExternalNavigation: true` keeps the browser off even with this key on, and `browserExternalPageTools: "disabled"` keeps the pane but turns Claude's page tools off for external sites. Takes effect after the app restarts.

***

#### `builtinBrowserDefaultDomainPolicy`

enumDefault: allowSince 2.2553.0

**Default site policy in the built-in browser.** Whether Claude may open sites in the built-in browser by default; the allowed or blocked list is the exception. Mirrors the Claude in Chrome site policy.

One of: `allow` (default), `block`

[Self-hosted install](#self-hosted-column): Not supported. Sets the default for Desktop's browser tools, and host sessions get no browser tools to allow or block.

[Admin Console](#the-works-with-column): Set automatically.

> **More detail**
>
> Applies when `builtinBrowserEnabled` is on, in both Cowork and Code sessions, and decides which sites Claude may open, read, or act on with its browser tools; users can still view any site themselves. `allow` (default): every site except entries in `builtinBrowserBlockedDomains`. `block`: no site except entries in `builtinBrowserAllowedDomains`. Under either policy `coworkEgressAllowedHosts`, when set to anything but `*`, is an outer bound: sites outside it are refused to Claude in the browser too. A site Anthropic's site safety list blocks stays blocked to Claude under either policy (see `builtinBrowserEnabled`); for a site the list only flags for confirmation, Claude asks the user before each of its actions under `allow`, and skips that confirmation only when the site matches a `builtinBrowserAllowedDomains` entry under `block`. A value that cannot be read is treated as `block` until it is fixed.
>
> The policy also limits what pages load: a page in the pane, including one a user opened, cannot load frames, scripts, images, or other content from a site the policy does not admit (a blocked page a user opens still loads content from its own site). Under `block`, or with a `coworkEgressAllowedHosts` list, include the CDN and API hosts your allowed sites depend on.
>
> This key and the two site lists work the same way as the Claude in Chrome site policy in the admin console. They are set separately here, except on an install managed from the Claude admin console, where they follow your organization's browser site permissions there.

***

#### `builtinBrowserAllowedDomains`

string\[]Since 2.2553.0

**Allowed sites in the built-in browser.** Sites Claude may open, read, and act on in the built-in browser when the default site policy is block. Users can still view other sites.

[Self-hosted install](#self-hosted-column): Not supported. Lists sites allowed for Desktop's browser tools, and host sessions get no browser tools.

[Admin Console](#the-works-with-column): Set automatically.

> **More detail**
>
> Used when `builtinBrowserDefaultDomainPolicy` is `block`; ignored under `allow`. A site matching an entry is one Claude may open and work with using its browser tools; every other external site is treated as blocked by your organization: Claude cannot open it, cannot read or act on it, and frames, popups, and redirects into it from a page Claude is working on are refused. A user can still type its address and view it themselves. Listing a site here never unblocks a site Anthropic's site safety list blocks (see `builtinBrowserEnabled`); for a site that list only flags for confirmation, an entry here is your organization vouching for it, so Claude works with it without asking before each action.
>
> Entries use the same grammar as `coworkEgressAllowedHosts`, except that bare `*` is dropped: as in Claude in Chrome, no allowed-sites entry opens every site. Set the policy to `allow` for that. A wildcard whose base is a public suffix (`*.co.uk`, `*.github.io`) is likewise ignored so an entry can never open a whole shared registry. Any other entry outside that grammar is kept but matches nothing (the app log and the editor name it); a value that cannot be read at all allows nothing until it is fixed. A plain hostname entry (`example.com`) also covers its `www.` form, and a `www.` entry covers the bare name, but no other subdomain. `localhost` dev servers are always reachable, so listing them changes nothing.
>
> Empty or unset (default): under `block`, Claude may open no external site. On an install managed from the Claude admin console this follows your organization's browser site permissions there.

***

#### `builtinBrowserBlockedDomains`

string\[]Since 2.2553.0

**Blocked sites in the built-in browser.** Sites Claude may not open, read, or act on in the built-in browser when the default site policy is allow. Users can still view them.

[Self-hosted install](#self-hosted-column): Not supported. Lists sites blocked for Desktop's browser tools, and host sessions get no browser tools.

[Admin Console](#the-works-with-column): Set automatically.

> **More detail**
>
> Used when `builtinBrowserDefaultDomainPolicy` is `allow` (the default); ignored under `block`. A site matching an entry is treated as blocked by your organization: Claude cannot open it, cannot read or act on it with its browser tools, and frames, popups, and redirects into it from a page Claude is working on are refused. A user can still type its address and view it themselves: the pane shows a "blocked by your organization's policy" banner and Claude's tools stay off there. To take the external browser away from users as well, deploy Claude Code's `disableBrowserExternalNavigation` managed setting instead. A blocked site is refused before the site safety check, so its address is never sent to Anthropic.
>
> Entries use the same grammar as `coworkEgressAllowedHosts`; `*` blocks every external site. An entry outside that grammar is kept but matches nothing (the app log and the editor name it); a value that cannot be read at all blocks every external site until it is fixed. As in Claude in Chrome, a plain hostname entry (`example.com`) also covers its `www.` form, and a `www.` entry covers the bare name, but no other subdomain. `localhost` dev servers are never affected.
>
> Use this key for exceptions inside an allowed egress wildcard or when egress is open. Empty or unset (default): no sites beyond the egress list are blocked. On an install managed from the Claude admin console this follows your organization's browser site permissions there.

***

### Claude.ai data import

#### `claudeAiImport`

objectSince 1.10628.0

**Claude.ai data import.** Lets users import Claude.ai chats and projects, plus earlier Claude sessions on this computer, when `enabled` is true. `automatic3pImport` is a separate switch.

[Self-hosted install](#self-hosted-column): Server side. Desktop can still export sessions stored on the person's computer, and imports none, since no session runs there.

> **Child attributes (5)**
>
> **enabled** `boolean` (default: false)
>
> Lets users import a Claude.ai data export and earlier Claude sessions on this computer from Settings → Import. Doesn’t affect a provisioned sign-in import.
>
> **allowedOrganizationUuids** `string[]`
>
> When set, users import by sign-in only, and only from the Claude.ai organizations with these IDs.
>
> > **More detail**
> >
> > A list of Claude.ai organization IDs (UUIDs). When set, users can import only by signing in to Claude.ai, and only from an organization on the list: a sign-in to any other organization, or to a personal account, is refused before anything is downloaded. Importing from a file and from earlier sessions on this computer is turned off. The list narrows `enabled` and turns nothing on by itself; `automatic3pImport` is not affected. An entry that is not a UUID allows nothing and is reported. An empty list, or one that cannot be read, allows no organization, so no import is offered; a null or blank value is read as not set. A provisioned sign-in import names no organization, so it is not offered while the list is set. Each import is reported to your OpenTelemetry collector as the event `desktop_claude_ai_import`, with the ID of the organization it came from. It is an info-level event: set `otlpDesktopLogLevel` to `info` to receive it.
>
> **automatic3pImport** `boolean`
>
> Copy this computer’s earlier third-party sessions into the app once, in the background. Independent of `enabled`.
>
> > **More detail**
> >
> > Under device-delivered configuration (device management, a configuration file or a bootstrap URL) this runs only when set to `true`; for organizations managed from the Claude admin console (the hosted configuration) it is on unless an admin turns it off there. When the app launches under this organization, it copies this computer's earlier third-party sessions into its store, with Settings → Import's importer (originals are kept). It lists the earlier configuration's Cowork artifacts in this organization. If still offered, optional plugins the user switched on return. Organization plugins directory: switched on. `allowedPluginMarketplaces` entry with an unchanged source or on the new gateway or bootstrap origin: reinstalled without asking. Plugins the user uploaded (unless `userPluginUploadsEnabled` is off; they can run programs on this computer) and skills they saved (unless `skillCreationEnabled` is off) are installed again without asking, on or off as they were; a skill that declares tools, hooks, metadata or unknown settings arrives off. Not copied: plugins from user-added marketplaces or with code in another repository. Earlier Cowork projects are added, their instructions held until the user accepts them. The user's Cowork memory, global instructions and Instructions for Claude are copied and used at once, unreviewed (no memory if it was paused). Earlier scheduled tasks are added, each on or off as it was: one that was on runs at its next scheduled time. Runs at most once per device under device-delivered configuration and once more after it joins the hosted configuration. Under the hosted configuration it takes sessions from any earlier device configuration (including ones a console sign-in created) but never those stored under another organization's hosted configuration; under device-delivered configuration, only those stored while no organization ID was configured, and only once one is. Turn on `enabled` too so users can import skipped sessions by hand.
>
> **exportEnabled** `boolean` (default: false)
>
> Lets users export this computer’s chats, Cowork tasks, and Code sessions as a zip another install can import. No effect unless `enabled` is true.
>
> > **More detail**
> >
> > Allows users to write this computer's chats, Cowork tasks, and Code sessions to a portable zip that another install can import from Settings > Import. Transcripts contain conversation content including tool outputs; only session-record metadata is projected to a fixed field allowlist. Treat exported zips as sensitive data.
>
> **bannerBehavior** `enum`
>
> Prompt to import on a new chat or task. Off if unset. `show`: always; needs `enabled` or a sign-in import. `detect`: if `enabled` finds earlier Claude sessions.
>
> One of: `off`, `detect`, `show`

***

## Connectors

### MCP

#### `managedMcpServers`

object\[]Since 1.2581.0

**Managed MCP servers.** Org-pushed MCP servers: remote (HTTP/SSE) or local (stdio command). May embed bearer tokens.

[Self-hosted install](#self-hosted-column): Server side. The host connects the admin's MCP servers and applies each tool's rule, and tells Desktop which local ones to start.

> **More detail**
>
> For OAuth-authenticated entries, the app builds the redirect URI as `http://<callbackHost>:<callbackPort>/callback`; register that exact value with the OAuth provider. Tokens refresh automatically during a session.
>
> `toolPolicy` locks the per-tool approval state, keyed by tool name: `"blocked"` removes the tool from the session and labels it admin-blocked, `"ask"` requires approval on every call (Allow once / Deny only; no persistent always-allow; a scheduled Cowork task waits at that prompt), `"allow"` pre-approves. Tools **not listed** follow the user's choice: the prompt offers a persistent Always allow, except for tools that can modify data, which show a session-scoped **Allow for this task** alongside **Allow for all tasks** with a malicious-instruction warning. In Code sessions, `blocked` and `ask` are forwarded as Claude Code permission rules; `allow` is not.
>
> Keys may contain `*` wildcards (`"read_*"` matches every tool whose name starts with `read_`; anchored, and `*` is the only wildcard). When several wildcard keys match, the strictest applies (blocked > ask > allow). An exact-name key wins over matching wildcards, with two exceptions in the stricter direction: in Code sessions a wildcard `ask`, or a wildcard `blocked` other than the bare `"*"`, beats a less strict exact key (so `"*": "blocked"` plus exact `"allow"` entries still works as deny-by-default there); and in chat approval prompts and always-allow persistence a wildcard `ask` keeps every matching tool behind a per-call prompt even when a more permissive exact key matches, while direct tool invocations such as artifact or widget calls follow the exact key.
>
> For the bundled Microsoft 365 connector, the send tools (`outlook_send_mail`, `outlook_send_draft`, `outlook_forward_mail`, `outlook_create_event`, `outlook_update_event`, `teams_send_chat_message`, `teams_send_channel_message`, `teams_reply_channel_message`) cannot be loosened below `ask`; an `allow` setting resolves to `ask`.

> **Child attributes**
>
> **name** `string` *required*
>
> Unique name for this server. Shown to users and used to key tool policy and sign-in state.
>
> **toolPolicy** `object: name → value`
>
> Lock the approval state for specific tools. Unlisted tools stay user-controlled.
>
> > **More detail**
> >
> > Also governs the same server when an installed plugin provides it. A plugin's MCP server matches an entry by URL, else by name (case-insensitive; a plugin server that runs locally matches by name only), and then follows that entry's `toolPolicy` alone: `orgPluginSettings` is not consulted for it, even when the entry sets no `toolPolicy`. A built-in entry (one with `server`) is the exception: it applies to a plugin's server of the same name only when a `toolPolicy` is written on it, and then carries that `toolPolicy` and the built-in's rule that its send and other irreversible tools cannot be loosened below `ask`, but not the built-in's other default prompts. An `http`, `sse` or `stdio` entry is also a server the app itself connects to or launches. To set permissions for a server that only a plugin runs, without the app connecting to or launching anything, use an entry with `transport: "policy-only"`.
> >
> > Any value other than `allow`, `ask` or `blocked` is read as `blocked` for that tool, and a `toolPolicy` that is not a map of tool names blocks every tool of the server; both are reported as configuration errors.
> >
> > For a plugin server that Claude Code launches or connects to itself (a marketplace plugin's), the permissions travel on Claude Code's managed-settings channel: another Claude Code [managed-settings source](https://claude.com/docs/third-party/claude-desktop/code.md#interaction-with-claude-code%E2%80%99s-own-managed-settings) on the device replaces them unless that source sets `parentSettingsBehavior` to `"merge"`. `blocked` on a server the app connects to itself holds either way.
>
> **microsoft365**
>
> Applies when `server` is `microsoft365`. The in-app configuration window calls it **Microsoft 365**.
>
> **server** `string` *required*
>
> Which bundled connector this entry turns on. Set instead of a transport; each built-in server has its own fields.
>
> Must be: `microsoft365`
>
> **tenantId** `string` *required*
>
> Your organization’s Microsoft Entra directory (tenant) ID.
>
> **clientId** `string` *required*
>
> OAuth app client ID for this built-in server.
>
> **azureCloud** `enum`
>
> Microsoft cloud for sign-in and Graph. Leave as global for commercial Microsoft 365; US Government clouds require your own app registration (Client ID).
>
> One of: `global`, `us-gov-high`, `us-gov-dod`
>
> **continuousAccessEvaluation** `enum` (default: enabled)
>
> Request CAE-capable Microsoft Graph tokens: long-lived (up to about 28 hours) but revocable within minutes. Set “disabled” to keep standard one-hour tokens.
>
> One of: `enabled` (default), `disabled`
>
> > **More detail**
> >
> > With Continuous Access Evaluation the server declares the `cp1` client capability, so Microsoft Entra issues access tokens that live up to about 28 hours and are cut off within minutes by a claims challenge when an administrator revokes sessions, disables the account, or the user’s risk changes — and, where the tenant enforces an IP named-location or Global Secure Access compliant-network Conditional Access policy, when the token is presented from outside that network. Tenants without such a policy get the longer lifetime and the fast revocation but no network-based replay protection; set `disabled` to keep standard one-hour, non-CAE tokens on every sign-in path. A change applies to tokens issued after the connector respawns with it; an already-cached long-lived token is served until it expires (Disconnect → Connect signs in afresh).
>
> **scope** `string`
>
> What the server may request at sign-in. If blank, Desktop’s default read set is used.
>
> **websearch**
>
> Applies when `server` is `websearch`. The in-app configuration window calls it **Web search**.
>
> **headers** `object: name → value`
>
> Static headers sent on every request — routing and tenant headers only. No credentials here; use the headers helper script for tokens and rotating values.
>
> > **More detail**
> >
> > On a `websearch` entry, every provider but `custom` needs `headers` or `headersHelper`: the app drops an entry that sets neither.
>
> **headersHelper** `string`
>
> Consent required (A value that a bootstrap server or a self-hosted session host delivers applies only after the user approves it, unless machine-scoped device management set that server's address. For a bootstrap server, the trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)
>
> Script that prints the auth header as a JSON object to stdout. Runs before each request (cached for the TTL below).
>
> > **More detail**
> >
> > Absolute path to an executable that prints a single JSON object of request headers to stdout, e.g. `{"X-Subscription-Token": "…"}`. The app runs it before each request and caches the result for the TTL below. Use this to pull the key from a secrets manager instead of storing it inline in `headers`.
> >
> > The helper runs with `CLAUDE_CODE_MCP_SERVER_NAME` set to this entry’s `name`, so one executable can serve several servers. For a name that holds a double quote, a percent sign or a control character the variable is not set. Claude Code also sets `CLAUDE_CODE_MCP_SERVER_URL` for its own `headersHelper`; this app does not. A name can contain characters such as `&`: put it in double quotes, compare it with the names you expect, and do not pass it on to another command.
>
> **headersHelperArgs** `string[]`
>
> Consent required (A value that a bootstrap server or a self-hosted session host delivers applies only after the user approves it, unless machine-scoped device management set that server's address. For a bootstrap server, the trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)
>
> Arguments passed to the headers helper script, one per entry, in order. Leave unset to run it with none.
>
> > **More detail**
> >
> > Each entry reaches the executable as one argument, exactly as written: `["--environment", "production"]` runs `helper --environment production`. Use it to keep one installed script and let each server’s entry say what it does (which environment, tenant or endpoint to use), instead of packaging a script per server.
> >
> > Entries may not be empty and may not contain a double quote (`"`), a percent sign (`%`) or control characters, on any platform: a Windows `.cmd`/`.bat` helper receives its arguments through `cmd.exe`, where those characters would change the command. A `.cmd`/`.bat` script sees each argument quoted (`%1` is `"production"`, `%~1` strips the quotes); `.ps1`, `.exe` and POSIX helpers receive them bare. Arguments are visible in the app log and to other processes on the machine, so do not put secrets in them; the helper exists to fetch the secret. A server whose list breaks these rules is dropped, and reported, rather than run with other arguments.
> >
> > An app version that does not know this setting ignores it and runs the helper with no arguments: have the script fail when an argument it needs is missing.
>
> **headersHelperTtlSec** `integer`
>
> How long the helper’s headers are reused before it runs again, in seconds. Defaults to 300.
>
> **headersHelperRefreshBufferSec** `integer`
>
> Seconds before the TTL expires at which the helper re-runs mid-session. Defaults to 60. Keep it larger than the helper’s typical runtime.
>
> **server** `string` *required*
>
> Which bundled connector this entry turns on. Set instead of a transport; each built-in server has its own fields.
>
> Must be: `websearch`
>
> **provider** `enum` *required*
>
> Runs search from the desktop, for inference providers without native web search. Supply the provider’s API key through the headers helper script below.
>
> One of: `brave`, `tavily`, `exa`, `custom`
>
> > **More detail**
> >
> > For inference providers without native web search (Bedrock, custom gateways). On Anthropic API and Vertex, the model’s built-in web search is available without this.
> >
> > The provider’s API key is a credential — have the **headers helper script** print its auth header rather than storing it in `headers`:
> >
> > * **Brave** — `X-Subscription-Token`
> > * **Exa** — `x-api-key`
> > * **Tavily** — `Authorization` (Bearer …)
> >
> > To turn web search off entirely, or to require approval for each search, list the bare `WebSearch` name in `disabledBuiltinTools` or `builtinToolPolicy`; it takes no per-host scope.
>
> **customUrl** `string`
>
> POST endpoint accepting \{q} JSON and returning a results\[] array. Only used when provider is Custom.
>
> > **More detail**
> >
> > Required when `provider` is `custom`: the app drops such an entry without it.
>
> **github**
>
> Applies when `server` is `github`. The in-app configuration window calls it **GitHub**.
>
> **server** `string` *required*
>
> Which bundled connector this entry turns on. Set instead of a transport; each built-in server has its own fields.
>
> Must be: `github`
>
> **clientId** `string` *required*
>
> GitHub OAuth app client ID (device flow must be enabled on the app).
>
> **host** `string`
>
> Leave blank for github.com. For GitHub Enterprise Server, your instance’s base URL.
>
> **scope** `string`
>
> Space-separated GitHub OAuth scopes. If blank, Desktop’s default read set is used. Ignored for GitHub Apps (permissions come from the app registration).
>
> **toolsets** `string`
>
> Comma-separated github-mcp-server toolsets to enable. If blank, the bundled server’s default toolsets are used.
>
> **readOnly** `boolean`
>
> Offer only read tools — the server registers no write tools at all.
>
> **http / sse**
>
> Applies when `transport` is `http` or `sse`. The in-app configuration window calls it **Streamable HTTP** or **SSE (legacy)**.
>
> **transport** `enum` *required*
>
> How the app connects: Streamable HTTP, legacy SSE, or a local command (stdio). policy-only connects to nothing; it only sets a plugin server’s tool policy.
>
> One of: `http`, `sse`
>
> **url** `string` *required*
>
> HTTPS endpoint of the remote MCP server. Use the server’s final address: HTTP redirects are not followed.
>
> **oauth** `object`
>
> OAuth for a remote server: true to auto-register a client, a pre-registered client ID with tenant and scope, or mode “hosted” for an Anthropic-signed identity.
>
> [Guide for this setting](https://claude.com/docs/third-party/claude-desktop/mcp-sign-in.md)
>
> > **More detail**
> >
> > **Auto-register**: Claude registers itself as a client with the MCP server’s authorization server the first time a user connects. **Bring your own client**: for a server whose provider requires an OAuth client that you register. Enter its **Client ID**, and add a **Client secret** and **Authorization server** only when the provider also requires the secret. Leave **None** for a server that needs no sign-in or authenticates with headers.
>
> > **Child attributes**
> >
> > **dcr**
> >
> > Applies when `oauth.mode` is `dcr`. The in-app configuration window calls it **Auto-register (dynamic client registration)**. No other fields apply.
> >
> > Write `"oauth": true`. `{"mode": "dcr"}` means the same and takes no other member. To register automatically with scopes of your choice, write an object that sets any of `scope`, `appendOfflineAccess` and `additionalRedirectReferrerHosts` and nothing else, as Bring your own client describes.
> >
> > **byo**
> >
> > Applies when `oauth.mode` is `byo`. The in-app configuration window calls it **Bring your own client**.
> >
> > `mode` can be left out. Without `clientId` the object may set only `scope`, `appendOfflineAccess` and `additionalRedirectReferrerHosts`, and the app registers a client automatically; with any other member listed here and no `clientId`, the app drops the entry.
> >
> > **oauth.clientId** `string`
> >
> > OAuth client ID from your IdP app registration. Leave unset to auto-register (dynamic client registration) and only narrow scopes.
> >
> > **oauth.clientSecret** `string`
> >
> > Only for IdPs that require one (e.g. Box). Hosted config can store only a Google Desktop-app secret (GOCSPX-…); for other IdPs use the client secret helper.
> >
> > **oauth.clientSecretHelper** `string`
> >
> > Consent required (A value that a bootstrap server or a self-hosted session host delivers applies only after the user approves it, unless machine-scoped device management set that server's address. For a bootstrap server, the trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)
> >
> > Executable that prints the client secret on stdout as a JSON object with a single clientSecret key; any other output is rejected. Overrides the inline value.
> >
> > > **More detail**
> > >
> > > Claude runs the executable with no arguments whenever that server connects and whenever its sign-in is refreshed in the background (the result is not cached), and reads **stdout**, which must be exactly one JSON object of the form `{"clientSecret": "…"}`: no other keys, and no banner or log lines before or after it (write those to stderr, which is only logged; keep stdout and stderr together under 64 KB). The helper must exit with code `0` within 30 seconds. Any other output stops that server from connecting, with an error that names its `clientSecretHelper`, instead of sending a wrong value to the identity provider. Use this to pull the secret from Keychain, 1Password CLI, or an internal secret broker instead of writing it into the configuration, and prefer a helper that does not prompt the user, since it also runs during background refreshes.
> > >
> > > The helper runs with `CLAUDE_CODE_MCP_SERVER_NAME` set to this entry’s `name`, so one executable can serve several servers. For a name that holds a double quote, a percent sign or a control character the variable is not set. Claude Code also sets `CLAUDE_CODE_MCP_SERVER_URL` for its own `headersHelper`; this app does not. A name can contain characters such as `&`: put it in double quotes, compare it with the names you expect, and do not pass it on to another command.
> >
> > **oauth.authorizationServer** `string[]`
> >
> > Issuer URLs the OAuth sign-in may use, as a JSON array. Pre-filled by presets; ask your IdP admin if unsure.
> >
> > **oauth.authorizationUrl** `string`
> >
> > Only for IdPs that don’t serve a .well-known discovery document. Set together with Token URL; requires Client ID.
> >
> > **oauth.tokenUrl** `string`
> >
> > Only for IdPs that don’t serve a .well-known discovery document. Set together with Authorization URL; requires Client ID.
> >
> > **oauth.tenantId** `string`
> >
> > Required for single-tenant Entra apps. Leave blank for multi-tenant or non-Microsoft IdPs.
> >
> > **oauth.authFlow** `enum`
> >
> > How Entra sign-in runs for this server: the system browser (default) or the OS identity broker.
> >
> > One of: `browser`, `broker`
> >
> > > **More detail**
> > >
> > > * **`browser`** (default) — opens the system browser for an authorization-code (PKCE) sign-in on the loopback redirect URI.
> > > * **`broker`** — signs in through the OS identity broker (Web Account Manager on Windows, the Company Portal SSO extension on macOS), so it can satisfy Conditional Access policies that require a compliant or managed device or token protection. Requires **Tenant ID**, **Client ID**, and **Scope**. The app registration must list the broker redirect URIs `ms-appx-web://Microsoft.AAD.BrokerPlugin/{client-id}` (Windows) and `msauth.com.anthropic.claudefordesktop://auth` (macOS) under the **Mobile and desktop applications** platform, and the device must be Entra-registered (macOS also needs the Company Portal SSO extension). Not supported on Linux. When the broker is not available on a device, sign-in falls back to the system browser.
> > >
> > > App versions that predate this key always use the system browser.
> >
> > **oauth.scope** `string`
> >
> > Space-separated scopes sent on the authorize request. Leave unset to use the scopes the server advertises. Required when Tenant ID is set.
> >
> > **oauth.appendOfflineAccess** `boolean`
> >
> > Adds offline\_access to the authorize request so the IdP returns a refresh token for silent renewal.
> >
> > > **More detail**
> > >
> > > Leave off if Scope already includes `offline_access` or the server rejects it.
> > >
> > > With explicit endpoints (Authorization URL / Token URL, no discovery) this toggle can’t take effect on its own — the app can’t confirm the AS advertises `offline_access`, so include `offline_access` in **Scope** instead for silent refresh.
> >
> > **oauth.callbackHost** `enum`
> >
> > Use localhost only if your IdP’s registered redirect URI specifies it.
> >
> > One of: `127.0.0.1`, `localhost`
> >
> > **oauth.callbackPort** `integer`
> >
> > Only set if your IdP requires an exact-match redirect port. Entra accepts any.
> >
> > **oauth.additionalRedirectReferrerHosts** `string`
> >
> > Space-separated hostnames also accepted as the referrer of the sign-in callback. Only needed when the IdP completes sign-in from a different host.
> >
> > > **More detail**
> > >
> > > Only needed when the IdP completes sign-in from a host other than the authorization URL’s. When a callback is rejected for a referrer mismatch, the rejected host is named in the app log — add that hostname here.
> >
> > **hosted**
> >
> > Applies when `oauth.mode` is `hosted`. The in-app configuration window calls it **Anthropic-hosted client identity (requires Claude.ai sign-in)**.
> >
> > Always write `"mode": "hosted"`. Without it the object is read as Bring your own client, which needs `clientId` beside `authorizationServer`, so the app drops the entry.
> >
> > **oauth.clientId** `string`
> >
> > Set by the Claude.ai control plane when it serves this configuration (the URL of Anthropic’s hosted client-metadata document); not authored.
> >
> > **oauth.authorizationServer** `string[]` *required*
> >
> > The exact issuer string(s) the server’s OAuth authorization server advertises in its metadata, as a JSON array — matched exactly, including path and any trailing slash. Required: Anthropic signs the client identity only for an authorization server listed here.
> >
> > **oauth.scope** `string`
> >
> > Space-separated scopes sent on the authorize request. Leave unset to use the scopes the server advertises. Required when Tenant ID is set.
>
> **headers** `object: name → value`
>
> Static headers sent on every request — routing and tenant headers only. No credentials here; use the headers helper script for tokens and rotating values.
>
> **headersHelper** `string`
>
> Consent required (A value that a bootstrap server or a self-hosted session host delivers applies only after the user approves it, unless machine-scoped device management set that server's address. For a bootstrap server, the trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)
>
> Absolute path to an executable that prints a JSON object of HTTP headers on stdout. Merged over static headers; the helper wins on conflict.
>
> > **More detail**
> >
> > Absolute path to an executable that prints a single JSON object of request headers to stdout, e.g. `{"X-Subscription-Token": "…"}`. The app runs it before each request and caches the result for the TTL below. Use this to pull the key from a secrets manager instead of storing it inline in `headers`.
> >
> > The helper runs with `CLAUDE_CODE_MCP_SERVER_NAME` set to this entry’s `name`, so one executable can serve several servers. For a name that holds a double quote, a percent sign or a control character the variable is not set. Claude Code also sets `CLAUDE_CODE_MCP_SERVER_URL` for its own `headersHelper`; this app does not. A name can contain characters such as `&`: put it in double quotes, compare it with the names you expect, and do not pass it on to another command.
>
> **headersHelperArgs** `string[]`
>
> Consent required (A value that a bootstrap server or a self-hosted session host delivers applies only after the user approves it, unless machine-scoped device management set that server's address. For a bootstrap server, the trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)
>
> Arguments passed to the headers helper script, one per entry, in order. Leave unset to run it with none.
>
> > **More detail**
> >
> > Each entry reaches the executable as one argument, exactly as written: `["--environment", "production"]` runs `helper --environment production`. Use it to keep one installed script and let each server’s entry say what it does (which environment, tenant or endpoint to use), instead of packaging a script per server.
> >
> > Entries may not be empty and may not contain a double quote (`"`), a percent sign (`%`) or control characters, on any platform: a Windows `.cmd`/`.bat` helper receives its arguments through `cmd.exe`, where those characters would change the command. A `.cmd`/`.bat` script sees each argument quoted (`%1` is `"production"`, `%~1` strips the quotes); `.ps1`, `.exe` and POSIX helpers receive them bare. Arguments are visible in the app log and to other processes on the machine, so do not put secrets in them; the helper exists to fetch the secret. A server whose list breaks these rules is dropped, and reported, rather than run with other arguments.
> >
> > An app version that does not know this setting ignores it and runs the helper with no arguments: have the script fail when an argument it needs is missing.
>
> **headersHelperTtlSec** `integer`
>
> How long the helper’s headers are reused before it runs again, in seconds. Defaults to 300.
>
> **headersHelperRefreshBufferSec** `integer`
>
> Seconds before the TTL expires at which the helper re-runs mid-session. Defaults to 60. Keep it larger than the helper’s typical runtime.
>
> **icon** `string`
>
> Icon shown for this connector: a PNG or JPEG image as a base64 data: URI, at most 4,096 characters.
>
> > **More detail**
> >
> > Replaces the website's icon or the generic connector icon for this connector. The image is stored in the configuration itself, so the app makes no network request to show it. A PNG of 48 by 48 pixels or smaller works well. A URL, an SVG or another format, or a value over 4,096 characters (spaces and line breaks not counted) is not used: a device reports a configuration warning and shows the default icon, and the admin console will not save it. Each icon adds to the size of the configuration every device receives, and Windows Group Policy holds the whole `managedMcpServers` list in one value of at most 65,535 characters, so keep icons small.
>
> **stdio**
>
> Applies when `transport` is `stdio`. The in-app configuration window calls it **Local command (stdio)**.
>
> **transport** `string` *required*
>
> How the app connects: Streamable HTTP, legacy SSE, or a local command (stdio). policy-only connects to nothing; it only sets a plugin server’s tool policy.
>
> Must be: `stdio`
>
> **command** `string` *required*
>
> Consent required (A value that a bootstrap server or a self-hosted session host delivers applies only after the user approves it, unless machine-scoped device management set that server's address. For a bootstrap server, the trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)
>
> Absolute path to the server executable, run on the user’s machine.
>
> **args** `string[]`
>
> Consent required (A value that a bootstrap server or a self-hosted session host delivers applies only after the user approves it, unless machine-scoped device management set that server's address. For a bootstrap server, the trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)
>
> Arguments passed to the command, one per entry.
>
> **env** `object: name → value`
>
> Consent required (A value that a bootstrap server or a self-hosted session host delivers applies only after the user approves it, unless machine-scoped device management set that server's address. For a bootstrap server, the trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)
>
> Environment variables set for the command.
>
> **envHelper** `string`
>
> Consent required (A value that a bootstrap server or a self-hosted session host delivers applies only after the user approves it, unless machine-scoped device management set that server's address. For a bootstrap server, the trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)
>
> Script that prints environment variables as a JSON object to stdout. Runs when the local server starts (cached for the TTL below).
>
> > **More detail**
> >
> > Absolute path to an executable that prints a single JSON object of environment variables to stdout, e.g. `{"API_KEY": "…"}`. The app runs it before spawning the server and merges the result over `env` (the helper wins on conflict). Use this to pull secrets from a secrets manager instead of storing them inline in `env`.
> >
> > * If the helper fails, the server does not start; the failure names the helper path in the app log and the diagnostics report.
> > * A helper with nothing to set must print `{}`. Empty stdout is treated as a failure.
> > * A helper-emitted `PATH` replaces the static map’s `PATH` and supports the same `${PATH}` placeholder expansion as a static entry.
> > * The helper runs with `CLAUDE_CODE_MCP_SERVER_NAME` set to this entry’s `name`, so one executable can serve several servers. For a name that holds a double quote, a percent sign or a control character the variable is not set. Claude Code also sets `CLAUDE_CODE_MCP_SERVER_URL` for its own `headersHelper`; this app does not. A name can contain characters such as `&`: put it in double quotes, compare it with the names you expect, and do not pass it on to another command.
>
> **envHelperArgs** `string[]`
>
> Consent required (A value that a bootstrap server or a self-hosted session host delivers applies only after the user approves it, unless machine-scoped device management set that server's address. For a bootstrap server, the trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)
>
> Arguments passed to the environment helper script, one per entry, in order. Leave unset to run it with none.
>
> > **More detail**
> >
> > Each entry reaches the executable as one argument, exactly as written: `["--environment", "production"]` runs `helper --environment production`. Use it to keep one installed script and let each server’s entry say what it does (which environment, tenant or endpoint to use), instead of packaging a script per server.
> >
> > Entries may not be empty and may not contain a double quote (`"`), a percent sign (`%`) or control characters, on any platform: a Windows `.cmd`/`.bat` helper receives its arguments through `cmd.exe`, where those characters would change the command. A `.cmd`/`.bat` script sees each argument quoted (`%1` is `"production"`, `%~1` strips the quotes); `.ps1`, `.exe` and POSIX helpers receive them bare. Arguments are visible in the app log and to other processes on the machine, so do not put secrets in them; the helper exists to fetch the secret. A server whose list breaks these rules is dropped, and reported, rather than run with other arguments.
> >
> > An app version that does not know this setting ignores it and runs the helper with no arguments: have the script fail when an argument it needs is missing.
>
> **envHelperTtlSec** `integer` (default: 300)
>
> Maximum age of a cached helper result, in seconds (default 300). Applies when the server starts or restarts.
>
> > **More detail**
> >
> > How long the app may reuse the helper's output before running it again. The check happens only when the server process is (re)started. Environment variables are fixed at process creation, and a running server never sees refreshed values until its next restart. Set this at or below your token lifetime: a server that crash-loops because its token expired can be respawned with the same cached environment until the TTL lapses. Default: 300 seconds.
>
> **startupTimeoutSec** `integer` (default: 120)
>
> Maximum wait in seconds for the server to start and list its tools.
>
> **icon** `string`
>
> Icon shown for this connector: a PNG or JPEG image as a base64 data: URI, at most 4,096 characters.
>
> > **More detail**
> >
> > Replaces the website's icon or the generic connector icon for this connector. The image is stored in the configuration itself, so the app makes no network request to show it. A PNG of 48 by 48 pixels or smaller works well. A URL, an SVG or another format, or a value over 4,096 characters (spaces and line breaks not counted) is not used: a device reports a configuration warning and shows the default icon, and the admin console will not save it. Each icon adds to the size of the configuration every device receives, and Windows Group Policy holds the whole `managedMcpServers` list in one value of at most 65,535 characters, so keep icons small.
>
> **policy-only**
>
> Applies when `transport` is `policy-only`. The in-app configuration window calls it **Tool permissions only (plugin server)**.
>
> **transport** `string` *required*
>
> How the app connects: Streamable HTTP, legacy SSE, or a local command (stdio). policy-only connects to nothing; it only sets a plugin server’s tool policy.
>
> Must be: `policy-only`
>
> > **More detail**
> >
> > An entry with `transport: "policy-only"` is not a server: it sets tool permissions for an MCP server that an installed plugin provides, and nothing else. Set `name` to the server's name as the plugin declares it (matched case-insensitively) and `toolPolicy` to the permissions. The plugin keeps launching or connecting to its own server; the app never connects to, launches or lists anything for the entry, so it takes no `url`, `command`, `oauth` or other connection settings (an entry that sets one is rejected). It takes precedence over `orgPluginSettings` for that server in chat, Cowork and Code sessions alike; with no `toolPolicy` the server is left unrestricted. An entry whose name matches no installed plugin server does nothing.
> >
> > Desktop versions that predate `policy-only` do not recognise it: they drop the entry (listed under Configuration parse errors in the diagnostics report) and apply `orgPluginSettings` to that server instead. If every entry in the list is `policy-only`, those versions cannot read `managedMcpServers` at all: they report a parse error for it and, until they are updated, leave MCP servers that users added themselves, or that a project's `.mcp.json` declares, out of Code sessions. While older versions are still in use, keep the same permissions in `orgPluginSettings` too, and do not deploy a list made only of `policy-only` entries until every desktop has updated.

***

#### `mcpPersistentAlwaysAllowEnabled`

booleanDefault: trueSince 1.24012.9

**Allow persistent tool approvals.** Offer the persistent “Always allow” approval options for MCP tools. Disable to keep tool approvals per-call or session-scoped only.

[Self-hosted install](#self-hosted-column): Server side. When off, the host leaves lasting MCP tool approvals out of its sessions, and tells Desktop not to offer them.

> **More detail**
>
> When enabled (the default), approval prompts for tools without a `toolPolicy` entry offer a persistent grant: **Always allow**, or **Allow for all tasks** for tools that can modify data. The Tool permissions picker in Connector settings also lets users pre-approve tools. These grants persist across sessions with no expiry.
>
> When disabled, the persistent options are hidden from approval prompts and from the Connector settings picker, and previously stored persistent grants stop being honored. Scheduled-task runs also stop offering, recording, and replaying the **Allow for all scheduled runs** approval (**Always allow** in Code sessions), unless a scheduled-task approval lifetime of one day or more is set. Users can still approve each call. Outside scheduled-task runs, in chat and Cowork they can also choose **Allow for this task**, except for read-only tools on servers they added themselves.
>
> A per-tool `toolPolicy` entry on `managedMcpServers` always takes precedence over this key: `blocked`, `ask`, and `allow` behave exactly as documented there whether this key is enabled or not.
>
> This key governs chat and Cowork, and also Code sessions on the device (including WSL) or over SSH. In those Code sessions, with the key disabled, the prompt for an MCP tool offers **Allow for this session** instead of **Always allow**, except on scheduled-task runs. This approval is not saved to Claude Code's settings files. It lasts until the session is deleted, and sessions forked or started from it do not inherit it. Claude Code's own allow rules and hooks still apply. Allow rules in its settings files, including ones saved earlier with **Always allow**, and hooks in its settings or plugins keep allowing the tool until they are removed. Code sessions receive only the `blocked` and `ask` values of `toolPolicy` entries, so a tool set to `allow` still prompts there, and this key applies to it.

***

#### `mcpScheduledTaskApprovalLifetimeDays`

integerRange: 0–3,650Since 2.7032.0

**Scheduled-task tool approval lifetime.** How many days a scheduled task may reuse a lasting MCP-tool approval before it asks again. 0 removes the lasting option. Leave blank for no time limit.

[Self-hosted install](#self-hosted-column): Server side. The host limits how many days a scheduled task may reuse a lasting MCP tool approval, and tells Desktop.

> **More detail**
>
> On a scheduled task, the approval prompt for an MCP tool can offer a lasting approval, so later runs use that tool without asking: **Allow for all scheduled runs** in Cowork, **Always allow** in the Code tab. This setting limits how long that approval lasts. With a limit, the button reads **Allow for N days**. Once an approval is older than that, the next run asks again, and approving again renews it. `0` removes the lasting option, and approvals already stored stop being reused. Leave it blank to change nothing. Choose a number comfortably longer than the gap between runs.
>
> The limit covers MCP tools only, and a `toolPolicy` entry on `managedMcpServers` still takes precedence. If a configuration server delivers the setting, then after each launch scheduled tasks ask instead of reusing stored approvals (as at `0`) until the app has fetched the configuration again.
>
> If `mcpPersistentAlwaysAllowEnabled` is off, a limit of one day or more brings the lasting option back for scheduled tasks only.
>
> Code tab: the limit covers only lasting approvals given after this setting took effect. An earlier one was usually saved as an allow rule in Claude Code's own settings: for a scheduled task, the project's `.claude/settings.local.json`, under `permissions.allow`. Any allow rule in Claude Code's settings keeps allowing the tool without asking, even at `0`, until that entry is removed. That includes a rule written by hand, and one saved by **Always allow** in an ordinary Code session in the same project, which the app offers whenever `mcpPersistentAlwaysAllowEnabled` is on. In an ordinary Code session over SSH, if this setting has a value (even `0`), **Always allow** for a tool of a server set up on the host lasts for the session only and saves no rule there.

***

#### `isLocalDevMcpEnabled`

booleanDefault: trueSince 1.2581.0

**Allow local MCP servers.** Local stdio servers added via the Developer settings. On third-party deployments, off also stops plugins’ local servers. Remote servers keep working.

[Self-hosted install](#self-hosted-column): Server side. When off, only the local MCP servers the host names start on the person's computer, and none the person added.

> **More detail**
>
> On third-party deployments, `false` from any source also stops plugins' local (`stdio`) MCP servers in Cowork, Chat and Code sessions. That covers `.mcpb` bundles and plugins from every marketplace, your organization's included. In Code it also stops the local servers in Claude Code's own configuration files (`~/.claude.json`, a project's `.mcp.json`). It also stops a local server in Claude Code's `managed-mcp.json` whose command, arguments or environment use `${VAR}`. Remote servers keep working. Plugins placed in the org-plugins directory on the computer are not affected: the desktop still runs their servers.
>
> Set to `false` in a device-management profile, this key also locks down the local (`stdio`) entries of `managedMcpServers`: the app starts one only when that profile itself lists an entry of the same name, and with the profile's own command, arguments and environment. Only the profile's value engages this. A `false` from a configuration server or the admin console turns user-added servers off and does not engage it.
>
> Claude Code's own managed settings, on the device or (for Code sessions on a Claude API key) from the Claude Console, may override this key: see [managed settings](https://claude.com/docs/third-party/claude-desktop/code.md#interaction-with-claude-code%E2%80%99s-own-managed-settings).

***

#### `allowedPluginMcpServers`

object\[]Since 2.2553.0

**Allowed plugin MCP servers.** Servers plugins may connect in sessions, beyond the managed list above and organization plugins. An empty list allows none; unset keeps today’s rules.

[Self-hosted install](#self-hosted-column): Server side. The host connects a plugin's remote MCP server only where this list admits it; while it is unset, none connects.

> **More detail**
>
> Unset (default): with managed servers listed, sessions take MCP servers only from plugins and the desktop; with no managed servers listed, this key restricts nothing. Either way, `isLocalDevMcpEnabled` set to `false` stops plugins' local servers and, in Code, those of Claude Code's own configuration files.
>
> When set, Cowork, Chat and Code sessions connect the managed list above and the servers the desktop serves from the administrator's org-plugins directory, plus only servers declared by other plugins (user-installed or marketplace) that match an entry. An entry in the managed list above with `transport: "policy-only"` sets a plugin server's tool permissions but does not admit it; to admit that server, list the server's own URL here. Claude Code configuration-file servers (`~/.claude.json`, a project's `.mcp.json`, `claude mcp add`) are never connected. With the key set, the desktop starts no plugin server on the computer itself, whatever the entries say. The one exception is the MCP servers it serves to sessions from the org-plugins directory. Each entry is a URL pattern in Claude Code's form, `{"serverUrl": "https://*.example.com/*"}` (`*` wildcards; a host `*` spans `a.b`): a plugin's remote server connects when its URL matches an entry. No entry admits a plugin's local (stdio) server, and an empty list admits no plugin server. Other shapes, the `serverName` and `serverCommand` forms included, are dropped and reported; a value that is not a list, or has no readable entry, locks sessions to the managed list and the org-plugins directory's servers, and stops every other desktop-started plugin server. User-added local servers and extensions keep their own keys.
>
> Claude Code's own managed settings, on the device or (for Code sessions on a Claude API key) from the Claude Console, may override this key: see [managed settings](https://claude.com/docs/third-party/claude-desktop/code.md#interaction-with-claude-code%E2%80%99s-own-managed-settings).

> **Child attributes (1)**
>
> **serverUrl** `string` *required*
>
> URL pattern a plugin’s remote server must match, with \* wildcards.

***

#### `deniedPluginMcpServers`

object\[]Since 2.16120.0

**Blocked plugin MCP servers.** Remote servers plugins may not connect, even if the allowed list admits them; in Code sessions, configuration-file servers too. Unset or empty blocks none.

[Self-hosted install](#self-hosted-column): Server side. The host refuses a plugin's remote MCP server that this list matches, even where the allowed list admits it.

> **More detail**
>
> Unset (default) or an empty list: nothing is blocked.
>
> When set, Cowork, Chat and Code sessions do not connect a plugin's remote server whose URL matches an entry. The key works with or without `allowedPluginMcpServers`; a server that matches both lists stays blocked. In a Code session that reads Claude Code configuration-file servers (`~/.claude.json`, a project's `.mcp.json`, `claude mcp add`), a matching remote server from those files is refused as well. The managed list above, the servers the desktop serves from the administrator's org-plugins directory, user-added local servers and extensions are not affected: remove those at their own keys. Each entry is a URL pattern in Claude Code's form, `{"serverUrl": "https://*.example.com/*"}` (`*` wildcards; a host `*` spans `a.b`). An entry matches an address, not a server: the same server under another host name or an IP address, or behind a plugin's local (stdio) server, which has no URL, is not matched. `https://*.example.com/*` does not match `http://`, `wss://` or the bare `example.com`; a pattern such as `example.com/*`, which names no scheme, matches nothing, and a lone `*` matches every URL. To keep a plugin's servers out whatever address they use, set `allowedPluginMcpServers`, which admits only the servers it lists. The desktop reads no other shape, the `serverName` and `serverCommand` forms included: a value that is not a list, or that holds any entry the desktop cannot read, is reported and blocks every plugin's remote server (and those configuration-file remote servers), because skipping an entry of a block list would let its server connect. The servers named above as not affected still connect.
>
> Claude Code's own managed settings, on the device or (for Code sessions on a Claude API key) from the Claude Console, may override this key: see [managed settings](https://claude.com/docs/third-party/claude-desktop/code.md#interaction-with-claude-code%E2%80%99s-own-managed-settings).

> **Child attributes (1)**
>
> **serverUrl** `string` *required*
>
> URL pattern of the remote servers to block, with \* wildcards.

***

#### `mcpToolTimeoutSec`

integerRange: 60–3,600Since 1.37937.0

**MCP tool call timeout.** Per-call timeout for MCP tool calls, in seconds. Default 180 (3 minutes).

[Self-hosted install](#self-hosted-column): Server side. The host starts Claude Code, so it sets how long an MCP tool call may run.

> **More detail**
>
> Sets the per-call timeout the agent applies to every MCP tool call; a call that runs longer fails with a timeout error the model can see. Cowork and chat sessions default to 180 seconds. Code sessions have no desktop-imposed MCP tool timeout today, so setting this key introduces one there as well. The desktop's own request deadlines toward MCP servers — the managed servers above and, where `isLocalDevMcpEnabled` permits them, user-added local servers — follow this value so they never cut a call short first; while the key is unset, calls to user-added local servers are additionally limited to 60 seconds by the desktop. Values outside 60–3600 are rejected at parse time (the error is listed in the diagnostics report) and the defaults apply.
>
> The timeout is global (there is no per-server or per-tool form), so size it for the slowest tool you need to complete: long-running tools on one server extend the window during which a stuck call on any server holds its turn. Cowork's built-in shell tool runs under the same cap: a single command's `timeout_ms` (itself limited to 600 seconds) cannot exceed this value.

***

### Authentication

#### `microsoftAuthBroker`

enumDefault: autoSince 1.19367.0

**Microsoft 365 native sign-in broker.** “disabled” forces browser-based Microsoft 365 sign-in; “required” fails sign-in when the OS broker is unavailable, so the refresh token stays broker-held.

One of: `auto` (default), `disabled`, `required`

[Self-hosted install](#self-hosted-column): Not supported. Steers the sign-in of Desktop's bundled Microsoft 365 connector, started for no session on a self-hosted install.

> **More detail**
>
> `auto` (default): use the OS sign-in broker where available (WAM on Windows, the Company Portal SSO extension on macOS) and fall back to a browser sign-in otherwise. `disabled`: always use the browser sign-in. `required`: fail sign-in when the broker is unavailable rather than falling back to the browser, so the refresh token stays broker-held. Linux has no broker, so `required` is not supported there. Desktop builds older than the version that introduced `required` treat it as `disabled` (browser-only sign-in) — the opposite posture — so gate rollout on client version.

***

#### `microsoftAuthDefaultAccount`

enumDefault: disabledSince 2.26454.0

**Microsoft 365 sign-in with the Windows account.** “enabled”: when a user clicks Connect on Windows, Microsoft 365 signs in with the work account already signed in to Windows, without the account picker.

One of: `enabled`, `disabled` (default)

[Self-hosted install](#self-hosted-column): Not supported. Picks the account for Desktop's bundled Microsoft 365 connector, started for no session on a self-hosted install.

> **More detail**
>
> `disabled` (default): Connect shows the account picker when no account is connected. `enabled`: on Windows, when `microsoftAuthBroker` is not `disabled`, Connect first signs in silently with the account Windows already uses. The `tenantId` on the `microsoft365` entry in managed MCP servers must be a tenant GUID. With `common`, `organizations` or `consumers`, users always get the picker. Users also get the picker for accounts from another tenant, guest accounts and personal Microsoft accounts, when the silent sign-in fails, and when the computer cannot store credentials securely. A user who already signed in to Microsoft 365 through the browser keeps that account. After a user disconnects Microsoft 365, or a different person signs in to Claude on this computer, Connect always shows the picker for that connector on this computer, including for a disconnect that happened before this setting was turned on. Turning this setting off stops new silent sign-ins and signs nobody out: users already connected keep their account until they disconnect. macOS and Linux are not affected. Third-party deployments only: first-party installs ignore this setting.

***

### Extensions

#### `isDesktopExtensionEnabled`

booleanDefault: falseSince 1.2581.0

**Allow desktop extensions.** .dxt and .mcpb installs.

[Self-hosted install](#self-hosted-column): Not supported. Desktop keeps extensions off on a self-hosted install, whatever this setting says.

> **More detail**
>
> 1P builds default to enabled at runtime unless this is explicitly set. In 3P, enabling this allows loading extensions; local install additionally requires an org policy backend.

***

#### `isDesktopExtensionSignatureRequired`

booleanDefault: falseSince 1.2581.0

**Require signed extensions.** Reject desktop extensions that are not signed by a trusted publisher.

[Self-hosted install](#self-hosted-column): Not supported. Desktop installs no extension on a self-hosted install, so there is no signature for it to require.

***

## Telemetry & updates

### `deploymentOrganizationUuid`

stringSince 1.2581.0

**Organization UUID.** A UUID you generate. Tags telemetry so Anthropic support can locate your fleet’s events, and namespaces each user’s local data. Not used for auth.

[Self-hosted install](#self-hosted-column): MDM profile. Tags the desktop app's telemetry and names its local data on the person's computer.

[Admin Console](#the-works-with-column): Set automatically.

> **More detail**
>
> If unset, the app uses the organization of your Anthropic sign-in, where the connection has one. Otherwise, telemetry is tagged with a value the app derives from your connection settings. Where it cannot derive one, telemetry is tagged with a placeholder UUID shared with other unconfigured deployments. In the last two cases, local data is stored under the placeholder. **Changing this value orphans data** stored under the previous value (sessions, skills, plugins).

***

### `disableEssentialTelemetry`

booleanDefault: falseSince 1.2581.0

**Block essential telemetry.** Crash and performance reports to Anthropic.

[Guide for this setting](https://claude.com/docs/third-party/claude-desktop/telemetry.md#essential-telemetry)

[Self-hosted install](#self-hosted-column): MDM profile. Desktop starts its crash reports to Anthropic at launch, before sign-in, and a host's sessions never send any.

> **More detail**
>
> "Essential" means the signals Anthropic needs to keep your deployment working: **crash stacks**, **startup failure reasons**, **version/OS metadata**, and **crash dumps** (each an unfiltered copy of part of the app's memory). Reports carry a random install ID and an organization ID. The organization ID is the one you set, one the app takes from your Anthropic sign-in or derives from your connection settings, or a placeholder shared with other unconfigured deployments. Reports can also include a summary of your settings, the host names of addresses you configured, text you set for display (such as the display name, subtitle, and banner text and link), and a one-way digest of a session ID.
>
> **What you lose when this is on:** when a Claude Desktop build hits a bug that only reproduces on your OS version or locale, Anthropic can't see it unless a user manually reports. Fixes ship slower.
>
> **Why this is discouraged, not blocked:** some air-gapped environments require zero outbound telemetry as a matter of policy. The switch exists for them. If you don't have that constraint, leave it off.

***

### `disableNonessentialTelemetry`

booleanDefault: falseSince 1.2581.0

**Block nonessential telemetry.** Product-usage analytics (no message content) and diagnostic-report uploads.

[Guide for this setting](https://claude.com/docs/third-party/claude-desktop/telemetry.md#non-essential-telemetry)

[Self-hosted install](#self-hosted-column): MDM profile. Desktop sends usage analytics to Anthropic from before sign-in, and a host's sessions never send any.

> **More detail**
>
> "Nonessential" covers two things: **product-usage analytics** (which features get used, navigation patterns; no prompts or completions) and the **Send** action in Help → Generate Diagnostic Report. Turning this on stops both.
>
> Destinations are listed under Egress Requirements → Nonessential telemetry.

***

### `disableNonessentialServices`

booleanDefault: falseSince 1.2581.0

**Block nonessential services.** Connector favicons, artifact-preview and MCP Apps iframes, and the Linux spellcheck dictionary. Connector widgets fall back to text; spellcheck is off on Linux.

[Self-hosted install](#self-hosted-column): MDM profile. Desktop fetches connector icons, preview frames and a dictionary, starting before it has signed in to the host.

> **More detail**
>
> "Nonessential services" covers these outbound fetches the app runs without: **connector favicons** (the icon proxy), the **artifact-preview** iframe origin, the **MCP Apps widget** iframe origin (`*.claudemcpcontent.com`), and the **spellcheck dictionary** the built-in spellchecker downloads on Linux. Turning this on blocks all of them. (macOS and Windows use the system spellchecker. Windows still downloads a dictionary for a language it cannot check natively; this key does not stop that download.)
>
> **What you lose when this is on:** connectors show without icons, the hosted artifact preview frame does not load (artifacts still render locally), connectors that return MCP Apps show the text tool result instead of the widget, Excel files in the Code tab preview only through Claude’s workspace (the local VM) instead of that frame, and spellcheck underlines are off on Linux.
>
> Destinations are listed under Egress Requirements → Nonessential services.

***

### OTLP

#### `otlpEndpoint`

stringSince 1.2581.0

**OTLP endpoint.** Where OpenTelemetry logs and metrics are sent. Leave blank to disable.

[Self-hosted install](#self-hosted-column): Not supported. Whoever runs the host names the collector in the host's own configuration, for its sessions and Desktop's events.

***

#### `otlpProtocol`

enumDefault: http/protobufSince 1.2581.0

**OTLP protocol.** Transport protocol for the OpenTelemetry exporters.

One of: `http/protobuf` (default), `http/json`, `grpc`

[Self-hosted install](#self-hosted-column): Not supported. Set beside the collector's address in the host's own configuration.

> **More detail**
>
> Code sessions export over the protocol set here. Chats and Cowork tasks export over `http/protobuf` instead of `grpc` on Windows, and on other platforms whenever the Claude Code engine is given an HTTP proxy (the operating system's proxy, `egressProxyUrl` or `egressProxyPacUrl`, or `HTTPS_PROXY` / `HTTP_PROXY` in a Claude Code settings file); the application log notes the substitution. The desktop application's own events always go over `http/json` to `<endpoint>/v1/logs`. None of this changes the endpoint, so choose `grpc` only for a collector that also serves OTLP/HTTP at the same address; otherwise keep `http/protobuf` and point `otlpEndpoint` at the collector's OTLP/HTTP receiver (conventionally port 4318).

***

#### `otlpHeaders`

object: name → valueSince 1.2581.0

**OTLP headers.** Static collector headers — routing and tenant headers only. No credentials here; use Collector authentication or the headers helper script for tokens.

[Self-hosted install](#self-hosted-column): Not supported. The host keeps the collector's headers in its own configuration, so no document that a device fetches holds them.

***

#### `otlpAuthMode`

enumSince 1.30096.1

**Collector authentication.** inference-credential sends the user’s inference bearer token to the collector as Authorization: Bearer.

One of: `none`, `inference-credential`

[Self-hosted install](#self-hosted-column): Not supported. Would send the person's model token to the collector; a self-hosted Desktop holds none, and no host reads this.

> **More detail**
>
> `inference-credential` adds `Authorization: Bearer <token>` to every export, using the token the app currently holds for the inference provider, with no helper script to deploy. The collector must accept that token as issued: an identity-provider sign-in (`external-idp`, gateway or Bedrock proxy) forwards the identity provider’s token, which carries the audience you registered, Microsoft Entra on Foundry issues the Foundry resource’s token, and Vertex workforce identity forwards a Google Cloud access token; static gateway and Bedrock keys are forwarded as-is. Because the token can also call inference as the user, use this only for a collector you operate; for anything else, use the headers helper script with an ingest-scoped credential. Kinds that never produce a bearer (AWS SigV4 kinds on Bedrock, Google ADC / OAuth files on Vertex, API-key kinds) export without it, and so does Sign in with Claude Console, whose token is the user’s own and is never sent to a collector. Use the helper script instead. Cowork tasks pick up the current token each time they start; a Code session keeps the token it started with for as long as it stays open; the desktop’s own event exporter uses the current token on every flush. Before sign-in, exports go out unauthenticated. An `Authorization` header printed by the headers helper script wins over this.

***

#### `otlpHeadersHelper`

string

Consent required (A value that a bootstrap server or a self-hosted session host delivers applies only after the user approves it, unless machine-scoped device management set that server's address. For a bootstrap server, the trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)

Since 1.30096.1

**OTLP headers helper script.** Absolute path to an executable that prints a JSON object of collector headers. Merged over the static headers and Collector authentication; the helper wins.

[Self-hosted install](#self-hosted-column): Not supported. Desktop sends its own events to the host, which holds the collector's headers, so it runs no helper.

> **More detail**
>
> Absolute path to an executable that prints a single JSON object of HTTP headers on stdout, e.g. `{"Authorization": "Bearer …"}`. The desktop runs it (no arguments; output cached for a few minutes, and a failure is not retried for 30 seconds) whenever it needs collector headers and merges the result over **OTLP headers** and the **Collector authentication** header (the helper wins on conflict). Cowork tasks get the current output when they start; Code and Cowork sessions are also given the script as Claude Code’s own `otelHeadersHelper`, so an open session re-runs it as tokens rotate (on Windows this applies to `.exe`, `.cmd` and `.bat` helpers; a `.ps1` helper applies at session start only); the desktop’s own event exporter re-runs it per flush. Session start waits at most two seconds for a slow helper and otherwise proceeds without its headers until it finishes. Use this when the collector needs a credential the inference sign-in cannot provide, when the collector token rotates, or when the config comes from a hosted admin console, which cannot store header values. If the helper fails, telemetry is sent without its headers — check the app log.

***

#### `otlpResourceAttributes`

object: name → valueSince 1.5354.0

**Resource attributes.** Extra resource attributes to attach to every span/metric. A static enduser.id set here always wins over the runtime identity.

[Self-hosted install](#self-hosted-column): Server side. The host stamps these attributes on the session telemetry it sends and on Desktop's events that it forwards.

> **More detail**
>
> Extra resource attributes to attach to every span, metric, and log sent to your collector. When End-user attribution is on and no `enduser.id` is set here, the desktop fills it with the signed-in user's runtime identity; a value you set here always wins. `process.owner` (the OS login name) is always emitted; set it here to override.

***

#### `otlpDesktopLogLevel`

enumDefault: errorSince 1.9255.0

**Desktop telemetry export level.** Controls the Claude Desktop application’s events, separate from Cowork and Code sessions. Defaults to error.

One of: `off`, `error` (default), `warn`, `info`, `debug`

[Self-hosted install](#self-hosted-column): Server side. The host tells Desktop at which level to send its own events, and filters them again before it forwards them.

***

#### `otlpContentCapture`

enum\[]Since 1.15962.0

**Content capture.** Content categories Claude Desktop sends unredacted to your collector. `userPrompts` also sends Claude’s responses. If empty, no category is enabled (default).

Any of: `userPrompts`, `assistantResponses`, `toolDetails`, `toolContent`, `rawApiBodies`

[Self-hosted install](#self-hosted-column): Server side. The host decides how much of a session's content its telemetry carries.

> **More detail**
>
> Each category enables a class of raw content in OpenTelemetry events sent to your collector (this data never reaches Anthropic):
>
> * `userPrompts` — user-typed prompt text
> * `assistantResponses` — assistant message text
> * `toolDetails` — tool input arguments, e.g. the web-search query string
> * `toolContent` — tool output content, e.g. fetched page text or command stdout
> * `rawApiBodies` — inference API request and response bodies, each cut at 61,440 characters by default
>
> These mirror Claude Code's `OTEL_LOG_*` env vars; see the [Claude Code monitoring docs](https://code.claude.com/docs/en/monitoring-usage).
>
> In Claude Desktop, Claude's responses are included when user prompts are captured, even if `assistantResponses` is not listed. To exclude them, set `OTEL_LOG_ASSISTANT_RESPONSES` to `0` in the `env` block of Claude Code's managed settings, not in Claude Desktop's managed configuration. That `0` also wins when `assistantResponses` is listed, but `rawApiBodies` still includes responses. Claude Desktop ignores a `0` set in Claude Code's per-user Windows registry policy (`HKCU`). If a device has several managed sources, set the `0` in the highest-priority one with a policy. Excluding responses this way requires Claude Desktop 2.37337.1 or later.
>
> Claude Code managed settings set no policy if they are missing, empty, or hold only `wslInheritsWindowsSettings`, `managedSourcesBehavior`, or empty objects such as `"permissions": {}`. Adding `OTEL_LOG_ASSISTANT_RESPONSES` to such settings makes them a policy, so also set `parentSettingsBehavior` to `"merge"` there. Without `"merge"`, Claude Code can drop the restrictions that Claude Desktop passes to it. If the settings already set a policy, add only `OTEL_LOG_ASSISTANT_RESPONSES` to their `env` block, and read [Interaction with Claude Code's own managed settings](https://claude.com/docs/third-party/claude-desktop/code.md#interaction-with-claude-code%E2%80%99s-own-managed-settings) before you change `parentSettingsBehavior`.

***

#### `otlpTracesEnabled`

booleanSince 1.22209.0

**Export traces.** Also export OpenTelemetry traces from Cowork tasks and Code sessions. Uses Claude Code’s session tracing.

[Self-hosted install](#self-hosted-column): Server side. The host turns traces on or off in the session telemetry it sends.

> **More detail**
>
> Enables Claude Code's session tracing (`CLAUDE_CODE_ENHANCED_TELEMETRY_BETA=1` + `OTEL_TRACES_EXPORTER=otlp`) in spawned Cowork tasks and Code sessions. Each user interaction exports a trace whose spans and events carry `trace_id`/`span_id`, enabling end-to-end correlation in your observability backend (metrics do not carry trace context; correlate those via `session.id`). Traces go to the collector endpoint and protocol configured above. When `otlpEndpoint` is set, this key alone decides whether those sessions export traces: leaving it unset or `false` keeps traces off even if Claude Code's own settings or managed settings (for example a `managed-settings.json` on the device) turn tracing on. Without `otlpEndpoint` it has no effect. The span structure may evolve between Claude Code releases; see the [Claude Code monitoring docs](https://code.claude.com/docs/en/monitoring-usage).

***

#### `otlpAttrMaxChars`

integerRange: 256–15,000,000Since 2.31226.0

**Telemetry attribute length limit.** Maximum length, in characters, of captured content such as a raw API body (256–15,000,000). Cowork tasks and Code sessions use 61,440 when unset.

[Self-hosted install](#self-hosted-column): Server side. The host cuts long values in the session telemetry it sends.

> **More detail**
>
> Captured content longer than this is cut at the end and marked as truncated.
>
> * Cowork tasks and Code sessions: 61,440 when unset. Applies to model responses, tool content and raw API bodies. User prompts are not cut, and `tool_input` keeps its own smaller limits. A cut request body keeps the oldest messages and loses the newest, so to capture whole bodies with `rawApiBodies`, set this just above your longest body, not at the maximum. Lower it to reduce volume. While this key and `otlpEndpoint` are set, Claude Code's own settings and managed settings (for example a `managed-settings.json` on the device) cannot change the limit or the export interval.
> * Claude add-in for Microsoft 365: 4,000 when unset. Values above 32,000 count as 32,000.
> * The desktop application's own events are not affected.
>
> A collector refuses an export over its size limit, and every event in that export is lost. By default an OpenTelemetry Collector accepts 20 MiB per OTLP/HTTP request (`max_request_body_size`) and 4 MiB per gRPC message (`max_recv_msg_size_mib`). Keep that limit at a few times the size of your longest body: one export can carry several, and a character takes one byte in Latin text and up to three otherwise. With this key set, Code sessions export events as they happen, not every five seconds, as Cowork tasks already do, so the collector sees more, smaller requests.

***

### Auto update

#### `disableAutoUpdates`

booleanDefault: falseSince 1.2581.0

**Block auto-updates.** Stop Claude Desktop from fetching updates entirely (no time limit). You’ll need to push new versions yourself.

[Self-hosted install](#self-hosted-column): MDM profile. Desktop starts its updater at launch, before it has signed in to the host.

> **More detail**
>
> In third-party deployments this also keeps Cowork's workspace image and tools from being fetched ahead of use; they are then fetched when a task first needs them.
>
> When a newer version is installed on a device while Claude is open, the app shows "Relaunch to update" in the sidebar. The check makes no network request. On Windows this covers installs from the MSIX package, for one person or for the whole device, not the Microsoft Store version or the .exe installer. There it offers the newest version it finds on the device, which may be one installed for someone else. The click quits Claude, and Windows may then open the newer version. Where it does not (it did not on the Windows Server machines tested), people open Claude again and get the newer version. If Windows refuses the switch, Claude comes back on the version it had, and so does the notice. The switch may also end the Cowork tasks of others signed in on that computer. A separate setting has Claude restart by itself if nobody relaunches within a set number of hours.

***

#### `installedUpdateEnforcementEnabled`

booleanSince 3.6556.1

**Restart to apply installed updates.** With auto-updates blocked, Claude restarts for a newer version installed while it was open, after 72 hours or your window. On Windows it may stay closed.

[Self-hosted install](#self-hosted-column): Not supported. Governs Desktop's own restart for a version installed on the computer, and no session host passes it on to Desktop yet.

> **More detail**
>
> Set it where `disableAutoUpdates` is set. Both are app-behavior keys: a profile that sets any app-behavior key becomes the only source for all of them, so a profile that held this key alone would drop a `disableAutoUpdates` set elsewhere.
>
> Applies only while `disableAutoUpdates` is on, where you distribute new versions yourself. When a newer version is installed on a device while Claude is open, the app shows "Relaunch to update" in the sidebar. With this setting on, if nobody relaunches within the window, the app restarts itself and comes back on the page it was showing. `installedUpdateEnforcementHours` sets the window and says what holds the restart off.
>
> On Windows this covers installs from the MSIX package. Claude closes, switches to the newest version on the device (it may be one installed for someone else), and Windows may then open it. Where it does not, Claude stays closed, and scheduled tasks and background work stop, until someone opens it; opened after five minutes, it starts on its default page. If Windows refuses the switch, Claude comes back on the version it had and does not try again until it is reopened. The switch may also end the Cowork tasks of others signed in on that computer.
>
> Where it is not set, the restart is off in third-party deployments, and in first-party deployments it follows Anthropic's own rollout; `false` keeps it off. An unreadable value counts as `false`. Turning it on starts a whole new window. It has no effect on updates that Claude downloads itself; `autoUpdaterEnforcementHours` times those.
>
> A version from before this setting existed does not restart by itself and does not know the name: it ignores it in a macOS profile, and from other sources it may show people a configuration warning at every launch. A Windows machine policy that holds only such names, or a Linux managed-settings file that holds one and sets no connection, is rejected as unusable, and the app then also ignores the configuration saved on the device itself.

***

#### `installedUpdateEnforcementHours`

integerRange: 1–72Since 3.6556.1

**Installed-update enforcement window.** Hours Claude waits to restart for a newer version installed while it was open. Blank: 72 hours, then until the computer is idle. A number skips the idle wait.

[Self-hosted install](#self-hosted-column): Not supported. Times Desktop's own restart for a version installed on the computer, and no session host passes it on to Desktop yet.

> **More detail**
>
> No effect unless `disableAutoUpdates` is on and the restart is on (`installedUpdateEnforcementEnabled`). The window starts when the open app first finds a newer version installed; on Linux, where it cannot read the version, any replacement of the app counts. Only time with the app open and the computer awake counts.
>
> Leaving it blank uses the 72-hour default *and* then waits for the machine to be idle (10+ minutes without input) before restarting; setting any explicit value (including 72) restarts once the window elapses regardless of user activity. In both cases the restart holds off while Claude is mid-task, unless the task runs on an SSH host and the app expects to pick it up again after the restart. Where the system reports no idle time, as some Wayland sessions do, a blank window never restarts: set a number.

***

#### `autoUpdaterEnforcementHours`

integerRange: 1–72Since 1.2581.0

**Auto-update enforcement window.** Hours before a downloaded update force-installs. Only applies when auto-updates are enabled. Blank = 72-hour default.

[Self-hosted install](#self-hosted-column): Server side. Desktop itself quits and installs a downloaded update of the app on the person's computer.

> **More detail**
>
> Has no effect when `disableAutoUpdates` is in place at launch: nothing is downloaded, so this timer never arms. If the policy reaches an already-running app after an update has begun to download, that one update still installs on this timer; no further updates are fetched.
>
> Leaving it blank uses the 72-hour default *and* then waits for the machine to be idle (10+ minutes without input) before restarting; setting any explicit value (including 72) restarts once the window elapses regardless of user activity. In both cases the restart holds off while Claude is mid-task, unless the task runs on an SSH host and the app expects to pick it up again after the restart.

***

#### `updateViaUpdatesHost`

booleanDefault: falseSince 1.26832.0

**Check for updates on releases.claude.com.** Read the update feed from releases.claude.com so api.anthropic.com can stay blocked.

[Self-hosted install](#self-hosted-column): Not supported. Where the session host answers the app's update checks, no Anthropic update server is left to choose.

> **More detail**
>
> By default the app asks `api.anthropic.com` which version to install. That host also serves the model APIs, so organizations that block un-approved LLM endpoints at the network edge end up blocking updates too.
>
> Turn this on to read the same feed from `releases.claude.com`, a hostname that carries no model API. `api.anthropic.com` can then stay blocked without breaking auto-update. Rollout behavior is unchanged; the installer download still comes from `downloads.claude.ai` as before.
>
> If a device profile sets `bootstrapUrl` to a URL on `config.claude.com` and leaves `bootstrapEnabled` on, the app reads the feed from `releases.claude.com` whatever this key says. Older versions of the app do so only when this key is on, so turn it on as well.

***

#### `releaseChannel`

enumDefault: stableSince 3.1623.0

**Release channel.** On Stable, devices take each release as it rolls out. On Staggered, they update less often, usually to a version first out on Stable a week or more earlier.

One of: `stable` (default), `staggered`

[Self-hosted install](#self-hosted-column): MDM profile. On staggered, the person can update only once Desktop has downloaded a build; the session host ignores the channel.

> **More detail**
>
> Default: `stable`, which takes each release as it rolls out.
>
> Alternative: `staggered`, which usually updates on Thursdays to a release that has been live in production on `stable` with no known breaking issues. Typically the `staggered` release will be 7-14 days behind `stable`; urgent fixes may be released sooner.
>
> Devices download their new version at the next update check and install it on restart. Devices on `staggered` receive features and fixes, security fixes included, later than devices on `stable`. A device that's currently ahead of `staggered` will stay ahead until `staggered` catches up to its version.
>
> Switching to `stable` or removing the setting updates devices to the newest release.
>
> * An unreadable value, such as a misspelling or capital letter, is read as `staggered`.
> * The setting applies only in third-party mode. A user who signs in to Claude.ai follows `stable`, unless their organization manages Claude Desktop from the admin console.
> * On a device managed from the admin console, this setting applies only while a user is signed in. With no one signed in, the device follows `stable`.
> * The setting has no effect on Linux or Microsoft Store installs.
> * See [the installation page](https://claude.com/docs/third-party/claude-desktop/installation.md) for more details on where to set the key.

***

### Configuration updates

#### `relaunchEnforcementHours`

integerDefault: 24Range: 0–336Since 1.40609.0

**Configuration relaunch window.** Hours a user may keep working on the old configuration after a managed-configuration change is detected. 0 = restart required at once. Blank = 24 hours.

[Self-hosted install](#self-hosted-column): Server side. Desktop itself restarts on the person's computer after a change to the settings it reads from the device.

> **More detail**
>
> Set it via MDM (plist, registry, or file) or serve it from your configuration endpoint (remote bootstrap configuration). When the running app observes a managed-configuration change it cannot apply without restarting, it shows the sidebar relaunch card and starts this window. The window starts at the running app’s next configuration re-check (the re-check interval beside it), so allow up to one re-check interval on top of this value between saving a change and the restart dialog. When the window ends the app blocks with a restart dialog and restarts on its own after 2 minutes with no activity (no running Claude task and no keyboard or pointer input); the user can also restart right away. Defaults to 24 hours. Set a larger value (up to 336 = 14 days) to give users longer; `0` shows the dialog at the first observation. One case gets no window, whatever this value: when a device-management profile that sets more than app-behavior keys first applies to an app that started without one, and the app will run on that profile after restarting, the dialog shows at the re-check that confirms it, because until the restart the app stays connected the way it started.
>
> A served value is read from the newest served configuration, so tightening or loosening the window takes effect without a restart once two re-checks in a row have served it, and a change to this key alone never asks for one. Like the update keys beside it, a value from a device-management profile that sets only app-behavior keys applies without making the rest of the configuration device-managed, and takes precedence over a served one. Because the key is grouped with the other app-behavior keys, a profile that sets any of them claims the whole group: set this key in the same profile as the update keys you deploy, or a served value is ignored on those devices and the 24-hour default applies.

***

#### `configRecheckIntervalMinutes`

integerDefault: 10Range: 2–30Since 1.46388.1

**Configuration re-check interval.** Minutes between the running app’s checks for a changed managed configuration. Blank = 10 minutes.

[Self-hosted install](#self-hosted-column): Server side. The host refreshes its own copy of the policy at least this often, and tells Desktop how often to ask it again.

> **More detail**
>
> How often the running app re-checks its managed configuration for changes: it re-polls your configuration endpoint with a conditional request, so an unchanged configuration costs one `304` round-trip. A detected change shows the sidebar relaunch card and starts the `relaunchEnforcementHours` window, so a saved change reaches a running app within roughly one interval. Defaults to 10 minutes; each wait is jittered by ±10% so a fleet does not poll in lockstep. Values outside 2–30 are rejected with a parse error and the default applies.
>
> Applied without a restart: a new served value re-arms the timer once two checks in a row have served it, and a change to this key alone never asks for a relaunch. Set it via MDM or serve it from your configuration endpoint; like the update keys beside it, a value from a device-management profile that sets only app-behavior keys applies without making the rest of the configuration device-managed, and takes precedence over a served one. Because the key is grouped with the other app-behavior keys, a profile that sets any of them claims the whole group, and every key in it is then read from that profile alone: deploy this key in the same profile as the update keys (`disableAutoUpdates`, `autoUpdaterEnforcementHours`, …). A profile that sets the update keys without it ignores a served interval and the default applies; a profile that sets only this key ignores served update settings, so a served `disableAutoUpdates` no longer holds on those devices. A profile that also manages the connection itself (sets `bootstrapUrl` or the provider keys) follows the normal tier order instead: once a served configuration is in hand it, not the profile, supplies this key.

***

#### `disableLocalConfigCache`

booleanDefault: false

Admin Console only (Only the Enterprise Admin Console can set the key. Claude Desktop ignores it in an MDM profile, in the local configuration file and in a bootstrap server's response.)

Since 2.7032.0

**Keep only your organization ID and restrictions on disk.** Don’t keep your organization’s name or any permissive setting on disk between launches; only your organization ID and restrictions are kept.

> **More detail**
>
> By default the app keeps on disk, from the last configuration the admin console served, your organization’s ID and name and the few settings a launch applies before the console answers (the telemetry switches, the Microsoft 365 sign-in broker setting, the default Quick Entry shortcut, and restrictions). When this is on, it keeps only your organization ID and those restrictions (for example telemetry blocked, or local MCP servers off), never the name or anything you have allowed, and cuts an earlier copy down at the next launch that reaches the console, or at once when a running app confirms the change; signing out deletes the kept copy too. While on: the app’s crash reporting does not start on these devices, and the sign-in screen cannot show your organization’s name before the console answers. Error stack traces and performance timings still leave these devices unless **Block essential telemetry** is on.
>
> A running app picks up a change to this setting once two configuration checks in a row have served it; changing it alone never asks for a relaunch. It applies only to organizations managed from the Claude admin console; the setting is ignored when a customer configuration server or a device profile sends it.

***

## Limits

### Session retention

#### `chatSessionRetentionDays`

integerRange: 1–3,650Since 1.52386.0

**Chat retention period.** Delete chats, with their files, after this many days without activity. Unset: kept until the user deletes them. Projects and memory stay.

[Self-hosted install](#self-hosted-column): Not supported. Chat runs only on the person's computer, so a session host holds no chats to delete.

> **More detail**
>
> The app deletes whole sessions in the background shortly after it fetches this configuration (at launch and on each re-poll), or some minutes after launch and then daily when the configuration comes from device management alone. Idle time runs from the session's last activity; viewing an old Code session counts as activity, viewing an old chat or Cowork task without continuing it does not durably. A session that is running or open on screen is skipped and checked again on the next pass, as is a chat or Cowork task whose folder changed on disk within the period. Pinned sessions are not exempt. Minimum 1 day; a value that cannot be read as a whole number of days deletes nothing. Set through the served configuration or in the device-management profile that carries the rest of the configuration. What it does not reach: another account's sessions on the device (evaluated when that account signs in), Code sessions on a remote machine (SSH/WSL), Cowork background (dispatch) tasks the sidebar does not list, a chat or Cowork task whose folder cannot be located, and Claude Code files not named by a session id (prompt history, plans, shell snapshots), which keep Claude Code's own retention. Honored only by Claude Desktop configured for a third-party model provider.

***

#### `coworkSessionRetentionDays`

integerRange: 1–3,650Since 1.52386.0

**Cowork retention period.** Delete Cowork tasks, with their uploads and outputs, after this many days without activity. Unset: kept until the user deletes them. Spaces and memory stay.

[Self-hosted install](#self-hosted-column): Server side. The host keeps the Cowork sessions it runs, so it deletes those left idle longer than the admin allows.

> **More detail**
>
> The app deletes whole sessions in the background shortly after it fetches this configuration (at launch and on each re-poll), or some minutes after launch and then daily when the configuration comes from device management alone. Idle time runs from the session's last activity; viewing an old Code session counts as activity, viewing an old chat or Cowork task without continuing it does not durably. A session that is running or open on screen is skipped and checked again on the next pass, as is a chat or Cowork task whose folder changed on disk within the period. Pinned sessions are not exempt. Minimum 1 day; a value that cannot be read as a whole number of days deletes nothing. Set through the served configuration or in the device-management profile that carries the rest of the configuration. What it does not reach: another account's sessions on the device (evaluated when that account signs in), Code sessions on a remote machine (SSH/WSL), Cowork background (dispatch) tasks the sidebar does not list, a chat or Cowork task whose folder cannot be located, and Claude Code files not named by a session id (prompt history, plans, shell snapshots), which keep Claude Code's own retention. Honored only by Claude Desktop configured for a third-party model provider.

***

#### `codeSessionRetentionDays`

integerRange: 1–3,650Since 1.52386.0

**Code retention period.** Delete Code sessions, conversation included, after this many days without activity. Unset: kept until the user deletes them. Uncommitted work stays on disk.

[Self-hosted install](#self-hosted-column): Server side. The host keeps the Code sessions it runs, so it deletes those left idle longer than the admin allows.

> **More detail**
>
> The app deletes whole sessions in the background shortly after it fetches this configuration (at launch and on each re-poll), or some minutes after launch and then daily when the configuration comes from device management alone. Idle time runs from the session's last activity; viewing an old Code session counts as activity, viewing an old chat or Cowork task without continuing it does not durably. A session that is running or open on screen is skipped and checked again on the next pass, as is a chat or Cowork task whose folder changed on disk within the period. Pinned sessions are not exempt. Minimum 1 day; a value that cannot be read as a whole number of days deletes nothing. Set through the served configuration or in the device-management profile that carries the rest of the configuration. What it does not reach: another account's sessions on the device (evaluated when that account signs in), Code sessions on a remote machine (SSH/WSL), Cowork background (dispatch) tasks the sidebar does not list, a chat or Cowork task whose folder cannot be located, and Claude Code files not named by a session id (prompt history, plans, shell snapshots), which keep Claude Code's own retention. Honored only by Claude Desktop configured for a third-party model provider.

***

#### `sessionRetentionHold`

booleanSince 1.52386.0

**Suspend session deletion.** Suspend all automatic session deletion for these users (legal hold). While on, the retention periods above delete nothing.

[Self-hosted install](#self-hosted-column): Server side. The host keeps the sessions, so it is the one that stops deleting them during a hold.

> **More detail**
>
> Meant to be set per user or group, through the served configuration's group overrides or in the same device-management profile that carries the rest of the configuration (a profile carrying only this key makes the device profile-managed, like any policy key); a hold in the device's profile also counts when the served configuration does not restate it. Deletion stops at the first configuration fetch that carries this value, before it takes effect as configuration at the next relaunch; a device that cannot reach its configuration server deletes nothing.

***

### Token limits

#### `inferenceMaxTokensPerWindow`

integerRange: 1 or moreSince 1.2581.0

**Max tokens per window.** Limits each person’s input and output tokens per window. Cached tokens do not count, so this does not cap your provider’s bill. Leave blank for no limit.

[Self-hosted install](#self-hosted-column): Server side. The host makes the model calls, so it counts each person's tokens and stops them at the cap.

> **More detail**
>
> Requires `inferenceTokenWindowHours` to also be set — without a window length the cap is inert and no limit is enforced.
>
> Where the app runs the sessions, it keeps each person’s count in a local file, so someone who uses two devices has a separate count on each.

***

#### `inferenceTokenWindowHours`

integerRange: 1–720Since 1.2581.0

**Token cap window.** The count resets to zero at the end of each window. A window can last 1 to 720 hours (30 days).

[Self-hosted install](#self-hosted-column): Server side. Sets the length of the window for the token cap, which the host counts.

> **More detail**
>
> Required when `inferenceMaxTokensPerWindow` is set — the cap only takes effect once both are configured.
>
> Each person’s window starts the first time they use the app after their previous window ends, so 24 hours does not mean midnight to midnight.

***

## Appearance

### `endUserAttribution`

booleanSince 1.25927.0

**End-user attribution.** Show the signed-in user’s identity-provider identity in the sidebar and account menu, and emit it as the OpenTelemetry enduser.id resource attribute.

[Self-hosted install](#self-hosted-column): Server side. The host puts the person's identity on the telemetry it sends, and tells Desktop whether to show the person's name.

> **More detail**
>
> When on (default), the app resolves the signed-in user's identity from the configured credential source (the identity provider claim, or the OS login name when no claim is available) and shows it in the sidebar footer, the account menu, and the Code session greeting. If an OpenTelemetry collector is configured, the same identity is also emitted as the `enduser.id` resource attribute on every span, metric, and log sent to your collector — unless you have set a static `enduser.id` under **Resource attributes**, in which case your static value is kept and the runtime identity is not emitted. When off, no identity is shown in the app and no runtime `enduser.id` is emitted; a static `enduser.id` under **Resource attributes** still passes through unchanged. This setting does not gate the `process.owner` resource attribute (the OS login name), which is standard OpenTelemetry process metadata and is always emitted — set a static `process.owner` under **Resource attributes** to override it. Applies to both Cowork tasks and Code sessions.

***

### `deploymentDisplayName`

stringSince 1.24012.0

**Deployment display name.** Overrides the provider label shown in the sidebar footer, user-menu header, and connection-error banner.

[Self-hosted install](#self-hosted-column): Server side. Desktop shows this name in place of the provider's name in its own window.

[Admin Console](#the-works-with-column): Set automatically.

> **More detail**
>
> Set this to the name users should see for this deployment (for example, "Claude for Government"). When unset, the desktop shows the default provider label. Maximum 60 characters.

***

### `deploymentDisplaySubtitle`

stringSince 1.24012.0

**Deployment display subtitle.** Optional detail shown after the deployment display name in the account-menu header.

[Self-hosted install](#self-hosted-column): Server side. Desktop shows this detail after the deployment's name in its account menu.

[Admin Console](#the-works-with-column): Not available.

> **More detail**
>
> Optional detail shown after the deployment display name in the account-menu header (for example, "Claude for Veterans Affairs · Claude for Government"). Shown only when the display name is also set. Maximum 60 characters.

***

### `disableConfigDeprecationWarnings`

booleanSince 1.40609.0

**Hide configuration deprecation warnings.** Don’t show users the in-app warning that this configuration uses a deprecated field. The final reminder in the 24 hours before the cut-off still appears.

[Self-hosted install](#self-hosted-column): Server side. Desktop shows its warning about deprecated settings in its own window, for configuration that Desktop reads itself.

> **More detail**
>
> When the organization's configuration uses a field that is deprecated — a renamed key, or a legacy value or entry form — the app shows every user a dismissable warning naming the field, what to use instead, and the date support ends (each field's cut-off is listed in the configuration changelog and takes effect at 12:00 PM Pacific Time on that date). The warning shows from the field's announced warning date until dismissed, and once more in the 24 hours before the cut-off. Set this to `true` to suppress the first showing for your users while you migrate; the final 24-hour reminder is always shown, and the deprecation stays listed in the diagnostic report (Help → Troubleshooting) and the hosted configuration editor regardless.

***

### `banner`

objectSince 1.7196.0

**Organization banner.** A persistent banner across the top of the app window after sign-in.

[Self-hosted install](#self-hosted-column): Server side. Desktop draws the admin's banner across the top of its own window.

> **More detail**
>
> Use this for compliance notices, an internal-support link, or to identify the deployment. The banner is shown on every page after sign-in and cannot be dismissed by the user. Colors are six-digit hex (`#RRGGBB`); when `linkUrl` is set the banner text becomes an HTTPS link.

> **Child attributes (5)**
>
> **enabled** `boolean`
>
> Turns the banner on. When false or unset, the other banner fields are ignored.
>
> **text** `string`
>
> Single line, truncated on overflow. Maximum 200 characters.
>
> **backgroundColor** `string` (default: #F5F5F5)
>
> Six-digit hex (#RRGGBB). Applied exactly as configured; not theme-adapted.
>
> **textColor** `string` (default: #000000)
>
> Six-digit hex (#RRGGBB). Applied exactly as configured; not theme-adapted.
>
> **linkUrl** `string`
>
> Optional HTTPS URL. The banner text becomes a link when set.

***

### Feature discovery

#### `disableFeatureDiscovery`

booleanDefault: falseSince 1.21459.0

**Hide feature announcements.** Suppress unprompted feature-announcement UI: the post-update “What’s new” nudge and new-feature tips. Users can still open release notes themselves.

[Self-hosted install](#self-hosted-column): Server side. Desktop hides its own announcements of new features.

> **More detail**
>
> Covers the version-shipped announcement UI baked into each release: the **What's new** button that appears on its own after an update, and the one-time **New feature** tips (coach-marks) that point out newly shipped capabilities. Useful when your organization gates feature availability and doesn't want the app advertising capabilities you haven't rolled out.
>
> User-initiated surfaces stay: the What's-new menu item and header button still open the release notes on demand. Auto-update behavior is unaffected — that is governed by `disableAutoUpdates` and `autoUpdaterEnforcementHours`.

***

## Plugins

### `allowedPluginMarketplaces`

object\[]Since 1.17377.1

**Plugin marketplaces.** Git repositories or hosted marketplace.json URLs to surface as plugin marketplaces in the Directory’s Organization tab. The app re-fetches each periodically.

[Self-hosted install](#self-hosted-column): Server side. The host fetches the admin's plugin marketplaces and loads their plugins into the sessions it runs.

> **Child attributes**
>
> **expectedName** `string`
>
> Rejects the marketplace if its manifest name differs.
>
> > **More detail**
> >
> > When set, each fetch or clone is rejected if the marketplace's `manifest.name` differs, so an upstream rename cannot silently replace another configured marketplace. It also lets a new entry replace a removed one. Any change to an entry's `url`, `repo` or `path` (not `ref`) counts as removing that marketplace and adding another, which uninstalls the plugins that users installed from it, unless the new entry names the marketplace it replaces: in the same change that removes the old entry, set the new entry's `expectedName` to exactly the old marketplace's manifest name (letter case counts), and keep it set. The plugins that users installed then stay installed, with their stored settings, and load from the new source, where the new marketplace lists them under the same names. A plugin that is installed outside the marketplace's own folder and cannot be moved into it (its code comes from another repository, the new marketplace does not list it, or the new entry has not installed yet) is uninstalled as at any removal. The new entry's `installationPreference` applies as for any new entry; under `available` nothing else is installed and a plugin that a user switched off stays off. Until the new entry installs (it cannot be fetched, or it is refused), the plugins that stay installed do not load; they load again, with no reinstall, once it does. Removing the old entry first and adding the new one in a later change uninstalls the plugins on every computer that syncs in between.
>
> **installationPreference** `enum`
>
> Whether users install plugins themselves or get them automatically.
>
> One of: `available`, `auto_install`, `required`
>
> > **More detail**
> >
> > `available` (the default) lets users install from the Directory's Organization tab. `auto_install` installs automatically once per pin (the commit SHA, or a `url` source's `manifestSha256`); a plugin the user removes stays removed until the pin changes. `required` reinstalls on every sync, so it cannot stay removed. A change that only moves the pin of existing entries, with nothing else in the configuration changed, reaches running apps without a restart once the app's next two configuration checks both return it; any other change to this list asks for a restart. An `auto_install` or `required` entry without that pin (a full 40-character commit SHA in `ref`, or `manifestSha256` for a `url` source) is treated as `available` and reported as a config warning: the marketplace still lists, but the entry installs nothing. Left at (or treated as) `available`, a `url` marketplace served from your inference gateway's or bootstrap server's own origin may instead mark individual plugins `"installationPreference": "auto_install"` in its `marketplace.json`: those install automatically with no pin (each such archive needs a `sha256`), and a plugin the user removes stays removed. On any other origin those marks are ignored.
>
> **credentialHelper** `string`
>
> Consent required (A value that a bootstrap server or a self-hosted session host delivers applies only after the user approves it, unless machine-scoped device management set that server's address. For a bootstrap server, the trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)
>
> Executable that prints an access token for this marketplace.
>
> > **More detail**
> >
> > Prints to stdout one of: a bare token (sent as the git password for username `x-access-token`, which GitHub, GitLab and Azure DevOps accept, and as `Authorization: Bearer` for `url` sources); git-credential lines `username=<user>` and `password=<token>` when the host needs a particular username (Bitbucket Data Center project or repository access tokens on 9.3+: `x-token-auth`; GitLab deploy tokens: `gitlab+deploy-token-N`) — sent as HTTP Basic for `url` sources; `authtype=Bearer` and `credential=<token>` to send `Authorization: Bearer <token>` (Bitbucket Data Center HTTP access tokens on any version); or, for `url` sources only, a JSON object of HTTP headers such as `{"Authorization": "Bearer …", "X-Tenant": "acme"}` (the form an MCP server's `headersHelper` prints), all sent on every request to that marketplace — a `git` source refuses this form. Other keys, blank lines and CRLF are ignored in the line forms; output that opens with `{` must be a valid header object or the fetch is refused.
>
> **github**
>
> Applies when `source` is `github`. The in-app configuration window calls it **GitHub**.
>
> **source** `string` *required*
>
> Where the marketplace is fetched from: a GitHub repository (set repo), any Git remote (set url), or a hosted marketplace.json file (set url).
>
> Must be: `github`
>
> **repo** `string` *required*
>
> GitHub repository in owner/repo form. Case-insensitive.
>
> **ref** `string`
>
> Commit SHA, branch, or tag. Leave empty to track the default branch; auto\_install and required need a full 40-character commit SHA.
>
> **path** `string`
>
> Folder within the repository that contains the marketplace, when it isn’t at the root.
>
> **credentialKind** `enum`
>
> How fetches authenticate: anonymously, with the user’s git credentials, via a helper executable, or as the app does to its gateway or bootstrap server (url).
>
> One of: `anonymous`, `userGit`, `credentialHelper`
>
> **git**
>
> Applies when `source` is `git`. The in-app configuration window calls it **Git URL**.
>
> **source** `string` *required*
>
> Where the marketplace is fetched from: a GitHub repository (set repo), any Git remote (set url), or a hosted marketplace.json file (set url).
>
> Must be: `git`
>
> **url** `string` *required*
>
> HTTPS Git remote of the marketplace repository (git), or direct HTTPS URL of a hosted marketplace.json file (url).
>
> > **More detail**
> >
> > For `git` sources, the HTTPS remote the app clones. For `url` sources, the HTTPS address of a `marketplace.json` whose plugins are `archive` entries (a zip `url` plus its `sha256`; `ref` and `path` do not apply). Archive URLs must be same-origin with the manifest URL: that origin is the only host to open on the firewall and the only one a credential is sent to. If any archive fails to download or verify, nothing from that fetch is installed and the next sync retries.
> >
> > When Installation is `auto_install` or `required`, set `manifestSha256` to the SHA-256 of that exact file and give every archive a `sha256`: a served manifest with a different digest is refused and unpinned archives are skipped, so publishing a new manifest means updating `manifestSha256`; with no `manifestSha256` at all the entry is treated as `available` (and a config warning says so). A marketplace served from your inference gateway's or bootstrap server's own origin may instead leave Installation at `available` and mark individual plugins `"installationPreference": "auto_install"` in the manifest (each with a `sha256`); those install with no pin and a new manifest is picked up on the periodic re-fetch. On any other origin the per-plugin marks are ignored.
> >
> > `credentialKind` selects what is sent: `anonymous` (the default) nothing, `userGit` the user's stored git credential for that host as HTTP Basic, `credentialHelper` the helper's output as `Authorization` (or, for `url` sources, as the HTTP headers it prints as a JSON object), and `inferenceCredential` (`url` sources only) the credential the app already sends your inference gateway or enabled bootstrap server, so the manifest must be on one of those two origins; when there is nothing to send yet, no request is made and the entry reports why. See [Host the marketplace over HTTPS](https://claude.com/docs/third-party/claude-desktop/extensions.md#host-the-marketplace-over-https-instead-of-git) for an example manifest and credential details.
>
> **ref** `string`
>
> Commit SHA, branch, or tag. Leave empty to track the default branch; auto\_install and required need a full 40-character commit SHA.
>
> **path** `string`
>
> Folder within the repository that contains the marketplace, when it isn’t at the root.
>
> **credentialKind** `enum`
>
> How fetches authenticate: anonymously, with the user’s git credentials, via a helper executable, or as the app does to its gateway or bootstrap server (url).
>
> One of: `anonymous`, `userGit`, `credentialHelper`
>
> **url**
>
> Applies when `source` is `url`. The in-app configuration window calls it **Marketplace URL**.
>
> **source** `string` *required*
>
> Where the marketplace is fetched from: a GitHub repository (set repo), any Git remote (set url), or a hosted marketplace.json file (set url).
>
> Must be: `url`
>
> **url** `string` *required*
>
> HTTPS Git remote of the marketplace repository (git), or direct HTTPS URL of a hosted marketplace.json file (url).
>
> > **More detail**
> >
> > For `git` sources, the HTTPS remote the app clones. For `url` sources, the HTTPS address of a `marketplace.json` whose plugins are `archive` entries (a zip `url` plus its `sha256`; `ref` and `path` do not apply). Archive URLs must be same-origin with the manifest URL: that origin is the only host to open on the firewall and the only one a credential is sent to. If any archive fails to download or verify, nothing from that fetch is installed and the next sync retries.
> >
> > When Installation is `auto_install` or `required`, set `manifestSha256` to the SHA-256 of that exact file and give every archive a `sha256`: a served manifest with a different digest is refused and unpinned archives are skipped, so publishing a new manifest means updating `manifestSha256`; with no `manifestSha256` at all the entry is treated as `available` (and a config warning says so). A marketplace served from your inference gateway's or bootstrap server's own origin may instead leave Installation at `available` and mark individual plugins `"installationPreference": "auto_install"` in the manifest (each with a `sha256`); those install with no pin and a new manifest is picked up on the periodic re-fetch. On any other origin the per-plugin marks are ignored.
> >
> > `credentialKind` selects what is sent: `anonymous` (the default) nothing, `userGit` the user's stored git credential for that host as HTTP Basic, `credentialHelper` the helper's output as `Authorization` (or, for `url` sources, as the HTTP headers it prints as a JSON object), and `inferenceCredential` (`url` sources only) the credential the app already sends your inference gateway or enabled bootstrap server, so the manifest must be on one of those two origins; when there is nothing to send yet, no request is made and the entry reports why. See [Host the marketplace over HTTPS](https://claude.com/docs/third-party/claude-desktop/extensions.md#host-the-marketplace-over-https-instead-of-git) for an example manifest and credential details.
>
> **manifestSha256** `string`
>
> SHA-256 of the exact marketplace.json to accept. Without it auto\_install and required act as available; a served manifest with any other digest is refused.
>
> **credentialKind** `enum`
>
> How fetches authenticate: anonymously, with the user’s git credentials, via a helper executable, or as the app does to its gateway or bootstrap server (url).
>
> One of: `anonymous`, `userGit`, `credentialHelper`, `inferenceCredential`

***

### `orgPluginSettings`

object\[]Since 1.8089.0

**Organization plugin settings.** Admin policy applied to plugin-delivered MCP servers.

[Self-hosted install](#self-hosted-column): Server side. The host applies the admin's per-tool locks, and no plugin's MCP server is started on the computer.

> **More detail**
>
> Locks per-tool permissions on MCP servers provided by any installed plugin — from the org-plugins directory or a plugin marketplace, remote or run locally — one entry per server name (compared case-insensitively):
>
> ```json theme={null} theme={null} theme={null} theme={null} theme={null} theme={null} theme={null} theme={null} theme={null} theme={null} theme={null} theme={null}
> [{"serverName": "internal-search", "tools": [{"toolName": "delete_document", "permission": "blocked"}]}]
> ```
>
> The older record form (`{"mcpServers": {"internal-search": {"toolPolicy": {"delete_document": "blocked"}}}}`) is no longer accepted. Desktop versions before 1.15200.0 parse only the record form: on those builds an array value is ignored and plugin tool locks are **not enforced**, so update the fleet past 1.15200.0 before deploying the array form.
>
> If a Managed MCP servers entry is for the same server (same URL, else same name), that entry decides alone: its `toolPolicy` (if any) applies and the entry here is ignored. A value that cannot be read blocks every tool of every plugin-provided MCP server no Managed MCP servers entry covers.
>
> For a plugin server that Claude Code launches or connects to itself (a marketplace plugin's), the permissions travel on Claude Code's managed-settings channel: another Claude Code [managed-settings source](https://claude.com/docs/third-party/claude-desktop/code.md#interaction-with-claude-code%E2%80%99s-own-managed-settings) on the device replaces them unless that source sets `parentSettingsBehavior` to `"merge"`. `blocked` on a server the app connects to itself holds either way.

> **Child attributes (2)**
>
> **serverName** `string` *required*
>
> Name of the plugin-delivered MCP server this policy applies to.
>
> **tools** `object[]`
>
> Per-tool approval locks for this server.
>
> > **Child attributes (2)**
> >
> > **tools.toolName** `string` *required*
> >
> > MCP tool name as the server reports it.
> >
> > **tools.permission** `enum` *required*
> >
> > Approval state locked for this tool. Unlisted tools stay user-controlled.
> >
> > One of: `allow`, `ask`, `blocked`

***

## Source

### Bootstrap

#### `bootstrapEnabled`

booleanDefault: true

MDM only (You can set the key only in an MDM profile or the local configuration file. Claude Desktop ignores it in a bootstrap server's response.)

Since 1.10628.0

**Use bootstrap config.** Fetch and apply the URL above at launch. Turn off to keep the URL saved but skip the fetch.

[Self-hosted install](#self-hosted-column): MDM profile. Controls whether the desktop app fetches its configuration, so it cannot travel inside that document.

[Admin Console](#the-works-with-column): Not available.

***

#### `bootstrapUrl`

string

MDM only (You can set the key only in an MDM profile or the local configuration file. Claude Desktop ignores it in a bootstrap server's response.)

Since 1.10628.0

**Bootstrap config URL.** HTTPS endpoint that returns a per-user JSON config overlay. Values from the response override local settings and become read-only.

[Self-hosted install](#self-hosted-column): MDM profile. Tells the desktop app where to fetch its configuration, so it cannot travel inside that document.

[Admin Console](#the-works-with-column): Not available.

***

#### `bootstrapOidc`

object

MDM only (You can set the key only in an MDM profile or the local configuration file. Claude Desktop ignores it in a bootstrap server's response.)

Since 1.10628.0

**Bootstrap OIDC parameters.** When set, the bootstrap request sends a Bearer token from a browser sign-in (authorization-code-with-PKCE).

[Guide for this setting](https://claude.com/docs/third-party/claude-desktop/bootstrap.md)

[Self-hosted install](#self-hosted-column): MDM profile. Names the sign-in the desktop app uses to fetch its configuration, so it cannot travel inside it.

[Admin Console](#the-works-with-column): Not available.

> **More detail**
>
> Set this to use a separate identity provider (Microsoft Entra ID, Okta, Ping, or any compliant OIDC provider) for the bootstrap sign-in. The app runs an authorization-code-with-PKCE flow in the system browser. Omit to use device-code mode against the bootstrap server's own origin.
>
> This is an **object-typed key** — in an MDM profile it is a single JSON-string value, not separate keys with dotted names like `bootstrapOidc.clientId`. Writing the sub-fields as separate registry values causes the app to silently fall through to device-code mode.

> **Child attributes (8)**
>
> **clientId** `string` *required*
>
> OAuth client ID of the desktop app registration at your identity provider (public client, PKCE).
>
> **issuer** `string`
>
> HTTPS issuer with OIDC discovery. Set this, or set the authorization and token URLs instead.
>
> **authorizationUrl** `string`
>
> HTTPS authorization endpoint. Used with the token URL when no issuer is set.
>
> **tokenUrl** `string`
>
> HTTPS token endpoint. Used with the authorization URL when no issuer is set.
>
> **scopes** `string`
>
> Space-separated; the token’s audience must match what your bootstrap server validates.
>
> **redirectPort** `integer`
>
> Fixed loopback port for the sign-in redirect. Leave unset to use a free port each time.
>
> **redirectHost** `enum`
>
> Use localhost only if your IdP’s registered redirect URI specifies it.
>
> One of: `127.0.0.1`, `localhost`
>
> **additionalRedirectReferrerHosts** `string`
>
> Space-separated hostnames also accepted as the referrer of the sign-in callback. Only needed when the IdP completes sign-in from a different host.
>
> > **More detail**
> >
> > Only needed when the IdP completes sign-in from a host other than the authorization URL’s. When a callback is rejected for a referrer mismatch, the rejected host is named in the app log — add that hostname here.

***

#### `bootstrapHeaders`

object: name → value

MDM only (You can set the key only in an MDM profile or the local configuration file. Claude Desktop ignores it in a bootstrap server's response.)

Since 1.32885.1

**Bootstrap request headers.** HTTP headers sent on every bootstrap config fetch. Use this instead of embedding user:pass@ in the URL.

[Guide for this setting](https://claude.com/docs/third-party/claude-desktop/bootstrap.md)

[Self-hosted install](#self-hosted-column): MDM profile. Sets headers the desktop app sends to fetch its configuration, so it cannot travel inside that document.

[Admin Console](#the-works-with-column): Not available.

> **More detail**
>
> Static headers sent on every request to the bootstrap config URL — for a service-account credential (`Authorization: Basic …`, an API key header) or a routing/tenant header. When either this or the headers helper script is set and no separate `bootstrapOidc` provider is configured, the app treats the headers as sufficient auth and does not require a per-user sign-in for the bootstrap fetch. These headers (and the helper script's below) also accompany requests to a plugin marketplace this server hosts on its own origin (`allowedPluginMarketplaces` with `credentialKind: "inferenceCredential"`). Header values are masked in diagnostics and telemetry. For a rotating token, use the headers helper script instead.

***

#### `bootstrapHeadersHelper`

string

MDM only (You can set the key only in an MDM profile or the local configuration file. Claude Desktop ignores it in a bootstrap server's response.)

Since 1.32885.1

**Bootstrap headers helper script.** Absolute path to an executable that prints a JSON object of bootstrap request headers. Merged over the static headers; the helper wins.

[Guide for this setting](https://claude.com/docs/third-party/claude-desktop/bootstrap.md)

[Self-hosted install](#self-hosted-column): MDM profile. Names a program on the person's computer that supplies headers for fetching the app's configuration.

[Admin Console](#the-works-with-column): Not available.

> **More detail**
>
> Absolute path to an executable that prints a single JSON object of HTTP headers on stdout, e.g. `{"Authorization": "Bearer …"}`. The app runs it (no arguments; output cached for a few minutes) before each bootstrap config fetch and merges the result over **Bootstrap request headers** (the helper wins on conflict). Use this instead of embedding `user:pass@` in the bootstrap URL, or when the bootstrap server needs a rotating token from a secrets manager. When either this or the static headers are set and no separate `bootstrapOidc` provider is configured, the app treats them as sufficient auth and does not require a per-user sign-in for the bootstrap fetch. If a per-user sign-in also runs (`bootstrapOidc` or the server’s own device-code flow), that Bearer token wins on `Authorization`.

***

#### `trustBootstrapDelivery`

booleanDefault: false

MDM only (You can set the key only in an MDM profile or the local configuration file. Claude Desktop ignores it in a bootstrap server's response.)

Since 1.26832.0

**Trust bootstrap-delivered settings.** Skip the per-user consent prompt for sign-in targets, inference endpoints, helper scripts, and connectors the bootstrap server delivers.

[Self-hosted install](#self-hosted-column): MDM profile. Skips a consent prompt on the person's computer for what the configuration server sends.

[Admin Console](#the-works-with-column): Not available.

***

## Labels and badges

### Entry labels

The labels under a key start with its type and, where one is recorded, its default, and end with the Claude Desktop version that added the key. Between those, a label appears only where the key differs from most keys.

* **No MDM only or Admin Console only label**: You can set the key in an MDM profile or the local configuration file, or return it from a bootstrap server.
* **MDM only**: You can set the key only in an MDM profile or the local configuration file. Claude Desktop ignores it in a bootstrap server's response. [Read more](https://claude.com/docs/third-party/claude-desktop/bootstrap.md#response-schema).
* **Admin Console only**: Only the Enterprise Admin Console can set the key. Claude Desktop ignores it in an MDM profile, in the local configuration file and in a bootstrap server's response. [Read more](https://claude.com/docs/third-party/claude-desktop/admin-console.md).
* **Beta**: The feature that the key configures is in beta.
* **Deprecated**: On third-party deployments Claude Desktop no longer reads the key and ignores any value set for it. Remove it from your configuration.
* **Consent required**: A value that a bootstrap server or a self-hosted session host delivers applies only after the user approves it, unless machine-scoped device management set that server's address. For a bootstrap server, the trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval. [Read more](https://claude.com/docs/third-party/claude-desktop/bootstrap.md#keys-that-require-user-consent).
* **Origin-pinned**: A URL that a bootstrap server delivers must share the origin of bootstrapUrl, or Claude Desktop drops it. The limit is lifted when bootstrapOidc is set, and it does not apply to a value set in an MDM profile, the local configuration file or the Enterprise Admin Console. [Read more](https://claude.com/docs/third-party/claude-desktop/bootstrap.md#origin-pinning).
* **required**: The object or list entry that holds this field is not valid without it. Depending on the key, Claude Desktop then drops that entry alone, treats the key as unset, or applies a restrictive value in its place.

### The Works with column

Unless a label in its entry says otherwise, a key can be set in an MDM profile or the local configuration file, or returned from a bootstrap server. A badge marks another kind of deployment that the key also works with.

* **Self-hosted**: Something acts on the key on a self-hosted install. Its [Self-hosted install](#self-hosted-column) line gives the reason, and reads Server side or MDM profile, as the badge does on hover. Without the badge, that line reads Not supported, or the entry has none.
* **Admin Console**: The key takes effect where your organization manages Claude Desktop from the Enterprise Admin Console. [Read more](https://claude.com/docs/third-party/claude-desktop/admin-console.md).

  * **No hover text**: The hosted configuration can hold the key. Set it on the console's pages or, where no page has a field for it, by importing a configuration file or through the Admin API.
  * **Set automatically** on hover and in the key's entry: Anthropic fills the key in from your organization's own settings, such as its name or its built-in browser settings, each time an app downloads the configuration. A value written for the key in the hosted configuration has no effect.
  * **No badge**, and **Not available** in the key's entry: The hosted configuration can't hold the key, so you can't set it from the console.

  The hosted configuration refuses some values of keys that it can hold, for example an API key or token in a request header, and the Claude API as the inference provider. On a device that also has an MDM profile, the app still reads a few keys from the profile, for example the network proxy keys, which the console can't set. The Enterprise Admin Console guide lists them.

### Self-hosted install line

The self-hosted word matters only on a self-hosted install, where sessions run on a session host that your organization operates and not on the person's computer. The word says who acts on the key on such an install, and so where to set it; the text beside it gives the reason. On any other install, ignore it.

* **Server side** (`server`): in the document your session host reads; the host applies it itself.
* **Server side** (`reported`): in the same document; the host passes it on to Claude Desktop, which applies it in its own windows or on the person's computer.
* **MDM profile** (`client`): in Claude Desktop's own configuration on the computer (device management, the local file, or a bootstrap server that configuration names); the session host ignores it.
* **Not supported** (`none`): nothing acts on it on a self-hosted install, whichever of those places sets it.

One exception to the four words: where a device-management profile sets only app-behavior keys, that profile alone decides all of them (of the keys here: `disableAutoUpdates`, `installedUpdateEnforcementEnabled`, `installedUpdateEnforcementHours`, `autoUpdaterEnforcementHours`, `updateViaUpdatesHost`, `releaseChannel`, `relaunchEnforcementHours`, `configRecheckIntervalMinutes`, `egressProxyUrl`, `egressProxyPacUrl`).

The word is what this Claude Desktop release declares. A session host acts on a `server` or `reported` key only from the host version that reads it; until then nothing applies the key on a self-hosted install, and Claude Desktop does not fall back to a value set on the computer.

## Guides

* [Configuration implementation](https://claude.com/docs/third-party/claude-desktop/configuration-format.md): how configuration differs between a device's own configuration, the Enterprise Admin Console, and a self-hosted install, and how to write each value type.
* [Configuration changelog](https://claude.com/docs/third-party/claude-desktop/configuration-changelog.md): the desktop release each key first appeared in.
* [Models and effort levels](https://claude.com/docs/third-party/claude-desktop/models.md): how the keys under **Models** work together.
* [Unified Claude](https://claude.com/docs/third-party/claude-desktop/unified-claude.md#how-unified-claude-interacts-with-chat-and-cowork-settings): how `desktopHome` overrides the other keys under **Chat surface** and **Cowork surface**.
* [Automatic deletion of idle sessions](https://claude.com/docs/third-party/claude-desktop/data-storage.md#automatic-deletion-of-idle-sessions): which key under **Session retention** covers a conversation started from the home screen.

### Recommended security profiles

The profiles below are illustrative examples rather than built-in presets, and the labels are descriptive only. Use them as starting points and adjust for your environment. Layer the inference-provider keys for your cloud on top of whichever profile you choose.

**Standard**

Recommended for most enterprise deployments. Telemetry and auto-updates stay on so Anthropic can diagnose issues and ship fixes; users can extend Claude Desktop with their own connectors.

| Key | Value |
| - | - |
| [`deploymentOrganizationUuid`](#deploymentorganizationuuid) | `<your-org-uuid>` |
| [`autoUpdaterEnforcementHours`](#autoupdaterenforcementhours) | `24` |
| [`isDesktopExtensionSignatureRequired`](#isdesktopextensionsignaturerequired) | `true` |
| [`otlpEndpoint`](#otlpendpoint) | `<your-collector>` |

**Restricted**

For regulated environments that need to control what users can connect Claude Desktop to, while keeping Anthropic supportability.

| Key | Value |
| - | - |
| [`deploymentOrganizationUuid`](#deploymentorganizationuuid) | `<your-org-uuid>` |
| [`disableDeploymentModeChooser`](#disabledeploymentmodechooser) | `true` |
| [`disableNonessentialTelemetry`](#disablenonessentialtelemetry) | `true` |
| [`disableNonessentialServices`](#disablenonessentialservices) | `true` |
| [`isLocalDevMcpEnabled`](#islocaldevmcpenabled) | `false` |
| [`isDesktopExtensionEnabled`](#isdesktopextensionenabled) | `false` |
| [`allowedWorkspaceFolders`](#allowedworkspacefolders) | `[{"path":"~/Documents/Claude"}]` |
| [`coworkEgressAllowedHosts`](#coworkegressallowedhosts) | `["*.example.corp"]` |
| [`otlpEndpoint`](#otlpendpoint) | `<your-collector>` |

**Locked down**

For air-gapped or maximally restricted environments. **The app's own traffic goes only to your inference endpoint and OTLP collector**, plus `downloads.claude.ai` for the VM bundle and Claude CLI binary at session start unless you deploy the [offline installer](https://claude.com/docs/third-party/claude-desktop/installation.md#offline-installation). Code sessions on Windows, and on Linux without Claude Code's sandbox dependencies, [run shell commands unsandboxed](https://claude.com/docs/third-party/claude-desktop/code.md#applied-as-managed-policy), so those commands can reach any host your network allows. To prevent that, [turn off Code](https://claude.com/docs/third-party/claude-desktop/code.md#disabling-code) on those devices. With this profile, Anthropic receives no telemetry or logs from the app and does not deliver updates, so your team owns log collection and update distribution. On Microsoft Foundry, the Claude models behind your inference endpoint run in an Anthropic-operated service, so conversation content still reaches Anthropic-operated infrastructure under this profile, as described under [Data handling by provider](https://claude.com/docs/third-party/claude-desktop/overview.md#data-handling-by-provider).

| Key | Value |
| - | - |
| [`disableDeploymentModeChooser`](#disabledeploymentmodechooser) | `true` |
| [`disableEssentialTelemetry`](#disableessentialtelemetry) | `true` |
| [`disableNonessentialTelemetry`](#disablenonessentialtelemetry) | `true` |
| [`disableNonessentialServices`](#disablenonessentialservices) | `true` |
| [`disableAutoUpdates`](#disableautoupdates) | `true` |
| [`modelCatalogEnabled`](#modelcatalogenabled) | `false` |
| [`isLocalDevMcpEnabled`](#islocaldevmcpenabled) | `false` |
| [`isDesktopExtensionEnabled`](#isdesktopextensionenabled) | `false` |
| [`skillCreationEnabled`](#skillcreationenabled) | `false` |
| [`userPluginMarketplacesEnabled`](#userpluginmarketplacesenabled) | `false` |
| [`userPluginUploadsEnabled`](#userpluginuploadsenabled) | `false` |
| [`scheduledTasksEnabled`](#scheduledtasksenabled) | `false` |
| [`disabledBuiltinTools`](#disabledbuiltintools) | `["WebSearch","WebFetch"]` |
| [`coworkEgressAllowedHosts`](#coworkegressallowedhosts) | `[]` |
| [`allowedWorkspaceFolders`](#allowedworkspacefolders) | `[{"path":"~/Documents/Claude"}]` |
| [`otlpEndpoint`](#otlpendpoint) | `<your-collector>` |

### Tool permissions for managed MCP servers

Each [`managedMcpServers`](#managedmcpservers) entry can carry a `toolPolicy` that locks the approval state per tool:

* `"allow"` — the tool runs without prompting.
* `"ask"` — the user approves every call; no session-scoped or standing grants are offered.
* `"blocked"` — the tool is removed from Claude's session; connector settings show it as blocked by your organization.

In Cowork's [**Automatically approve**](#automodeenabled), a safety classifier still reviews calls to a tool set to `"allow"`, and can block them. See [Run vetted connector tools without classifier review](https://claude.com/docs/third-party/claude-desktop/code.md#run-vetted-connector-tools-without-classifier-review).

Tools with no policy entry stay user-controlled (built-in connectors apply default policies to some tools): the user is prompted and can approve once, approve for the rest of the task (offered for tools that can modify data), or grant a standing approval unless [`mcpPersistentAlwaysAllowEnabled`](#mcppersistentalwaysallowenabled) is `false`. The app reads a `toolPolicy` value other than `"allow"`, `"ask"`, or `"blocked"`, such as `"ask-session"`, as `"blocked"` for that tool and reports a configuration error, so write `"ask"` in place of `"ask-session"`. Managed policies take precedence over user grants, and enforcement happens in the desktop host process, not only in the prompt UI. A deny-by-default posture, `"*": "blocked"` plus exact `"allow"` entries for approved tools, is supported, including in Code sessions (where an allowed tool still gets Claude Code's own approval prompt). See the [`managedMcpServers` reference](#managedmcpservers) for wildcard matching, precedence rules, and built-in connector defaults.

On a scheduled Cowork task, the prompt can also offer an **Allow for all scheduled runs** option. See [Tool approvals on scheduled tasks](#tool-approvals-on-scheduled-tasks).

### Tool approvals on scheduled tasks

On a scheduled task, the approval prompt for an MCP tool that has no [`toolPolicy`](#tool-permissions-for-managed-mcp-servers) entry can offer a standing approval: **Allow for all scheduled runs** in Cowork, **Always allow** in Code. Later runs of the task then use the tool without asking.

To make these approvals expire, set [`mcpScheduledTaskApprovalLifetimeDays`](#mcpscheduledtaskapprovallifetimedays) to a whole number of days from `1` to `3650`. With a value of `30`, the option reads **Allow for 30 days**, the approval lasts 30 days from the moment the user chooses it, and after that the task asks again. Set the value comfortably longer than the time between a task's runs. The key requires Claude Desktop 2.7032.0 or later. Add it after your devices run that release.

The key's values:

* **Unset (default):** approvals never expire. The prompt offers the option, and stored approvals are used, only while [`mcpPersistentAlwaysAllowEnabled`](#mcppersistentalwaysallowenabled) is `true`.
* **`1` to `3650`:** each approval lasts that many days. The prompt offers the option even while `mcpPersistentAlwaysAllowEnabled` is `false`.
* **`0`:** the prompt doesn't offer the option, and stored approvals aren't used. A value that isn't a whole number from `0` to `3650` is treated as `0`. An empty value is treated as unset.

In Code sessions, an allow rule already in Claude Code's own settings files keeps allowing the tool even while `mcpPersistentAlwaysAllowEnabled` is `false`, until someone removes it.

The time limit doesn't cover:

* **Folder, browser, and built-in tool approvals:** these approvals never expire.
* **Account-wide grants in Cowork:** the account-wide **Always allow** and **Allow for all tasks** grants never expire. Of the two keys, only `mcpPersistentAlwaysAllowEnabled` affects them.
* **Claude Code allow rules in Code sessions:** an allow rule in Claude Code's own settings files, such as one saved when a user chose **Always allow** before the key was set, keeps allowing the tool, even with a value of `0`, until someone removes it. For a scheduled task, look in the project's `.claude/settings.local.json` file.
