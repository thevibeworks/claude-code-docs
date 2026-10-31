> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuration reference

> Every managed-configuration key Claude Desktop on 3P supports, what it controls, and recommended security profiles

| Key | Name in the app | Category | Works with (Unless a label in its entry says otherwise, a key can be set in an MDM profile or the local configuration file, or returned from a bootstrap server. A badge marks another kind of deployment that the key also works with.) |
| - | - | - | - |
| [`inferenceProvider`](#inferenceprovider) | Inference provider | Connection | Admin Console |
| [`inferenceCredentialKind`](#inferencecredentialkind) | Credential kind | Connection | Admin Console |
| [`inferenceSessionLifetimeSec`](#inferencesessionlifetimesec) | Sign-in session lifetime | Connection | Admin Console |
| [`userContentRendererUrl`](#usercontentrendererurl) | Artifact preview iframe origin | Connection | Admin Console |
| [`inferenceCustomHeaders`](#inferencecustomheaders) | Custom inference headers | Connection | Admin Console |
| [`inferenceCredentialHelper`](#inferencecredentialhelper) | Helper script | Connection | Admin Console |
| [`inferenceCredentialHelperWindows`](#inferencecredentialhelperwindows) | Helper script (Windows) | Connection | Admin Console |
| [`inferenceCredentialHelperArgs`](#inferencecredentialhelperargs) | Helper script arguments | Connection | Admin Console |
| [`inferenceCredentialHelperTtlSec`](#inferencecredentialhelperttlsec) | Helper script TTL | Connection | Admin Console |
| [`inferenceCredentialHelperTimeoutSec`](#inferencecredentialhelpertimeoutsec) | Credential helper timeout | Connection | Admin Console |
| [`inferenceCredentialHelperSilentRefreshEnabled`](#inferencecredentialhelpersilentrefreshenabled) | Re-run helper for silent refresh | Connection | Admin Console |
| [`egressProxyUrl`](#egressproxyurl) | Proxy server URL | Connection | |
| [`egressProxyPacUrl`](#egressproxypacurl) | Proxy auto-config (PAC) URL | Connection | |
| [`coworkVmIpv6Enabled`](#coworkvmipv6enabled) | Enable IPv6 in the workspace VM | Connection | Admin Console |
| [`inferenceGatewayBaseUrl`](#inferencegatewaybaseurl) | Gateway base URL | Connection | Admin Console |
| [`inferenceGatewayApiKey`](#inferencegatewayapikey) | Gateway API key | Connection | |
| [`inferenceGatewayAuthScheme`](#inferencegatewayauthscheme) | Gateway auth scheme | Connection | Admin Console |
| [`inferenceGatewayOidcAuthFlow`](#inferencegatewayoidcauthflow) | Gateway sign-in flow | Connection | Admin Console |
| [`inferenceGatewayOidc`](#inferencegatewayoidc) | Gateway SSO IdP (OIDC) | Connection | Admin Console |
| [`inferenceIdpAuthFlow`](#inferenceidpauthflow) | Identity provider sign-in flow | Connection | Admin Console |
| [`inferenceIdpOidc`](#inferenceidpoidc) | Identity provider (OIDC) | Connection | Admin Console |
| [`inferenceStreamIdleTimeoutSec`](#inferencestreamidletimeoutsec) | Stream idle timeout | Connection | Admin Console |
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
| [`modelPrefer1mContext`](#modelprefer1mcontext) | Use 1M wherever it’s available | Connection | Admin Console |
| [`inferenceModels`](#inferencemodels) | Model list | Connection | Admin Console |
| [`defaultModelEffort`](#defaultmodeleffort) | Default model effort | Connection | Admin Console |
| [`alwaysStartWithDefaultModel`](#alwaysstartwithdefaultmodel) | Always start with the default model | Connection | Admin Console |
| [`inferenceModelPricingEnabled`](#inferencemodelpricingenabled) | Show estimated cost | Connection | Admin Console |
| [`inferenceModelPricingMultiplier`](#inferencemodelpricingmultiplier) | Price multiplier | Connection | Admin Console |
| [`inferenceModelPricing`](#inferencemodelpricing) | Model pricing | Connection | Admin Console |
| [`modelCatalogEnabled`](#modelcatalogenabled) | Model catalog metadata | Connection | |
| [`modelCatalogUrl`](#modelcatalogurl) | Model catalog URL | Connection | |
| [`coworkTabEnabled`](#coworktabenabled) | Allow Cowork | Capabilities | Admin Console |
| [`isClaudeCodeForDesktopEnabled`](#isclaudecodefordesktopenabled) | Allow Code | Capabilities | Admin Console |
| [`sshHostAllowlist`](#sshhostallowlist) | SSH host allowlist | Capabilities | Admin Console |
| [`sshClientPath`](#sshclientpath) | SSH client program | Capabilities | Admin Console |
| [`sshTransport`](#sshtransport) | SSH connection engine | Capabilities | Admin Console |
| [`chatTabEnabled`](#chattabenabled) | Allow Chat | Capabilities | Admin Console |
| [`desktopHome`](#desktophome) | Desktop home | Capabilities | Admin Console |
| [`chatAdvancedFileAnalysisEnabled`](#chatadvancedfileanalysisenabled) | Advanced file analysis | Capabilities | Admin Console |
| [`coworkEgressAllowedHosts`](#coworkegressallowedhosts) | Allowed egress hosts | Capabilities | Admin Console |
| [`allowedWorkspaceFolders`](#allowedworkspacefolders) | Allowed workspace folders | Capabilities | Admin Console |
| [`blockReadsOutsideWorkingDirectories`](#blockreadsoutsideworkingdirectories) | Block reads outside working directories | Capabilities | Admin Console |
| [`autoModeEnabled`](#automodeenabled) | Allow Auto mode | Capabilities | Admin Console |
| [`disableBypassPermissionsMode`](#disablebypasspermissionsmode) | Disable bypass permissions mode | Capabilities | Admin Console |
| [`disableBundledSkills`](#disablebundledskills) | Disable bundled skills and workflows | Capabilities | Admin Console |
| [`skillCreationEnabled`](#skillcreationenabled) | Allow user-created skills | Capabilities | Admin Console |
| [`skillScanningEnabled`](#skillscanningenabled) | Scan user-created skills | Capabilities | Admin Console |
| [`userPluginMarketplacesEnabled`](#userpluginmarketplacesenabled) | Allow user-added plugin marketplaces | Capabilities | Admin Console |
| [`userPluginUploadsEnabled`](#userpluginuploadsenabled) | Allow user-added plugins | Capabilities | Admin Console |
| [`scheduledTasksEnabled`](#scheduledtasksenabled) | Allow scheduled tasks | Capabilities | Admin Console |
| [`projectsEnabled`](#projectsenabled) | Allow projects | Capabilities | Admin Console |
| [`keepAwakeEnabled`](#keepawakeenabled) | Allow keep awake | Capabilities | Admin Console |
| [`developerModeEnabled`](#developermodeenabled) | Allow Developer Mode | Capabilities | Admin Console |
| [`quickEntryDefaultShortcut`](#quickentrydefaultshortcut) | Default Quick Entry shortcut | Capabilities | Admin Console |
| [`quickEntryScreenshotsEnabled`](#quickentryscreenshotsenabled) | Allow screenshots of the screen and other apps | Capabilities | Admin Console |
| [`quickEntryFileSharingEnabled`](#quickentryfilesharingenabled) | Allow sharing files open in other apps | Capabilities | Admin Console |
| [`skipWebFetchPreflight`](#skipwebfetchpreflight) | Skip WebFetch domain check | Capabilities | Admin Console |
| [`builtinToolPolicy`](#builtintoolpolicy) | Built-in tool policy | Capabilities | Admin Console |
| [`disabledBuiltinTools`](#disabledbuiltintools) | Disabled built-in tools | Capabilities | Admin Console |
| [`toolSearchEnabled`](#toolsearchenabled) | Enable tool search | Capabilities | Admin Console |
| [`organizationInstructions`](#organizationinstructions) | Organization instructions | Capabilities | Admin Console |
| [`requireCoworkFullVmSandbox`](#requirecoworkfullvmsandbox) | Require full VM sandbox | Capabilities | |
| [`disableDeploymentModeChooser`](#disabledeploymentmodechooser) | Disable Claude.ai sign-in | Capabilities | |
| [`disableDeepLinkRegistration`](#disabledeeplinkregistration) | Disable claude:// deep-link handling | Capabilities | Admin Console |
| [`builtinBrowserEnabled`](#builtinbrowserenabled) | Allow the built-in browser | Capabilities | Admin Console |
| [`builtinBrowserDefaultDomainPolicy`](#builtinbrowserdefaultdomainpolicy) | Default site policy in the built-in browser | Capabilities | Admin Console |
| [`builtinBrowserAllowedDomains`](#builtinbrowseralloweddomains) | Allowed sites in the built-in browser | Capabilities | Admin Console |
| [`builtinBrowserBlockedDomains`](#builtinbrowserblockeddomains) | Blocked sites in the built-in browser | Capabilities | Admin Console |
| [`claudeAiImport`](#claudeaiimport) | Claude.ai data import | Capabilities | Admin Console |
| [`managedMcpServers`](#managedmcpservers) | Managed MCP servers | Connectors | Admin Console |
| [`mcpPersistentAlwaysAllowEnabled`](#mcppersistentalwaysallowenabled) | Allow persistent tool approvals | Connectors | Admin Console |
| [`mcpScheduledTaskApprovalLifetimeDays`](#mcpscheduledtaskapprovallifetimedays) | Scheduled-task tool approval lifetime | Connectors | Admin Console |
| [`isLocalDevMcpEnabled`](#islocaldevmcpenabled) | Allow local MCP servers | Connectors | Admin Console |
| [`allowedPluginMcpServers`](#allowedpluginmcpservers) | Allowed plugin MCP servers | Connectors | Admin Console |
| [`deniedPluginMcpServers`](#deniedpluginmcpservers) | Blocked plugin MCP servers | Connectors | Admin Console |
| [`mcpToolTimeoutSec`](#mcptooltimeoutsec) | MCP tool call timeout | Connectors | Admin Console |
| [`microsoftAuthBroker`](#microsoftauthbroker) | Microsoft 365 native sign-in broker | Connectors | Admin Console |
| [`microsoftAuthDefaultAccount`](#microsoftauthdefaultaccount) | Microsoft 365 sign-in with the Windows account | Connectors | Admin Console |
| [`isDesktopExtensionEnabled`](#isdesktopextensionenabled) | Allow desktop extensions | Connectors | Admin Console |
| [`isDesktopExtensionSignatureRequired`](#isdesktopextensionsignaturerequired) | Require signed extensions | Connectors | Admin Console |
| [`deploymentOrganizationUuid`](#deploymentorganizationuuid) | Organization UUID | Telemetry & updates | Admin Console |
| [`disableEssentialTelemetry`](#disableessentialtelemetry) | Block essential telemetry | Telemetry & updates | Admin Console |
| [`disableNonessentialTelemetry`](#disablenonessentialtelemetry) | Block nonessential telemetry | Telemetry & updates | Admin Console |
| [`disableNonessentialServices`](#disablenonessentialservices) | Block nonessential services | Telemetry & updates | Admin Console |
| [`otlpEndpoint`](#otlpendpoint) | OTLP endpoint | Telemetry & updates | Admin Console |
| [`otlpProtocol`](#otlpprotocol) | OTLP protocol | Telemetry & updates | Admin Console |
| [`otlpHeaders`](#otlpheaders) | OTLP headers | Telemetry & updates | Admin Console |
| [`otlpAuthMode`](#otlpauthmode) | Collector authentication | Telemetry & updates | Admin Console |
| [`otlpHeadersHelper`](#otlpheadershelper) | OTLP headers helper script | Telemetry & updates | Admin Console |
| [`otlpResourceAttributes`](#otlpresourceattributes) | Resource attributes | Telemetry & updates | Admin Console |
| [`otlpDesktopLogLevel`](#otlpdesktoploglevel) | Desktop telemetry export level | Telemetry & updates | Admin Console |
| [`otlpContentCapture`](#otlpcontentcapture) | Content capture | Telemetry & updates | Admin Console |
| [`otlpTracesEnabled`](#otlptracesenabled) | Export traces | Telemetry & updates | Admin Console |
| [`otlpAttrMaxChars`](#otlpattrmaxchars) | Telemetry attribute length limit | Telemetry & updates | Admin Console |
| [`disableAutoUpdates`](#disableautoupdates) | Block auto-updates | Telemetry & updates | Admin Console |
| [`installedUpdateEnforcementEnabled`](#installedupdateenforcementenabled) | Restart to apply installed updates | Telemetry & updates | Admin Console |
| [`installedUpdateEnforcementHours`](#installedupdateenforcementhours) | Installed-update enforcement window | Telemetry & updates | Admin Console |
| [`autoUpdaterEnforcementHours`](#autoupdaterenforcementhours) | Auto-update enforcement window | Telemetry & updates | Admin Console |
| [`updateViaUpdatesHost`](#updateviaupdateshost) | Check for updates on releases.claude.com | Telemetry & updates | Admin Console |
| [`releaseChannel`](#releasechannel) | Release channel | Telemetry & updates | Admin Console |
| [`relaunchEnforcementHours`](#relaunchenforcementhours) | Configuration relaunch window | Telemetry & updates | Admin Console |
| [`configRecheckIntervalMinutes`](#configrecheckintervalminutes) | Configuration re-check interval | Telemetry & updates | Admin Console |
| [`disableLocalConfigCache`](#disablelocalconfigcache) | Keep only your organization ID and restrictions on disk | Telemetry & updates | Admin Console |
| [`chatSessionRetentionDays`](#chatsessionretentiondays) | Chat retention period | Limits | Admin Console |
| [`coworkSessionRetentionDays`](#coworksessionretentiondays) | Cowork retention period | Limits | Admin Console |
| [`codeSessionRetentionDays`](#codesessionretentiondays) | Code retention period | Limits | Admin Console |
| [`sessionRetentionHold`](#sessionretentionhold) | Suspend session deletion | Limits | Admin Console |
| [`inferenceMaxTokensPerWindow`](#inferencemaxtokensperwindow) | Max tokens per window | Limits | Admin Console |
| [`inferenceTokenWindowHours`](#inferencetokenwindowhours) | Token cap window | Limits | Admin Console |
| [`inferenceTokenWarningPercent`](#inferencetokenwarningpercent) | Token limit warning | Limits | Admin Console |
| [`endUserAttribution`](#enduserattribution) | End-user attribution | Appearance | Admin Console |
| [`deploymentDisplayName`](#deploymentdisplayname) | Deployment display name | Appearance | Admin Console |
| [`deploymentDisplaySubtitle`](#deploymentdisplaysubtitle) | Deployment display subtitle | Appearance | |
| [`disableConfigDeprecationWarnings`](#disableconfigdeprecationwarnings) | Hide configuration deprecation warnings | Appearance | Admin Console |
| [`banner`](#banner) | Organization banner | Appearance | Admin Console |
| [`sessionStatusLine`](#sessionstatusline) | Status line | Appearance | Admin Console |
| [`disableFeatureDiscovery`](#disablefeaturediscovery) | Hide feature announcements | Appearance | Admin Console |
| [`allowedPluginMarketplaces`](#allowedpluginmarketplaces) | Plugin marketplaces | Plugins | Admin Console |
| [`orgPluginSettings`](#orgpluginsettings) | Organization plugin settings | Plugins | Admin Console |
| [`bootstrapEnabled`](#bootstrapenabled) | Use bootstrap config | Source | |
| [`bootstrapUrl`](#bootstrapurl) | Bootstrap config URL | Source | |
| [`bootstrapOidc`](#bootstrapoidc) | Bootstrap OIDC parameters | Source | |
| [`bootstrapHeaders`](#bootstrapheaders) | Bootstrap request headers | Source | |
| [`bootstrapHeadersHelper`](#bootstrapheadershelper) | Bootstrap headers helper script | Source | |
| [`trustBootstrapDelivery`](#trustbootstrapdelivery) | Trust bootstrap-delivered settings | Source | |

## Connection

### `inferenceProvider`

enumSince 1.2581.0

**Inference provider.** Selects the inference backend. Setting this key activates third-party mode.

One of: `gateway`, `anthropic`, `bedrock`, `mantle`, `vertex`, `foundry`

> [accordion] More detail
>
> The app opens in third-party mode unless the user chose to sign in to Claude.ai at the login screen. `disableDeploymentModeChooser` removes that choice.
>
> When this key is unset, the app opens in standard mode unless another key, such as `bootstrapUrl`, asks for third-party mode.
>
> A misspelt value from a machine-wide MDM profile still asks for third-party mode, which then shows a configuration error. From the local configuration file or Windows policy under `HKCU`, it reads as unset.

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

***

### `inferenceSessionLifetimeSec`

integerRange: 1 or moreSince 1.14271.0

**Sign-in session lifetime.** Seconds your identity provider keeps a sign-in valid. The app shows a re-authenticate banner before then.

***

### `userContentRendererUrl`

stringSince 1.24012.0

**Artifact preview iframe origin.** HTTPS origin of the server that artifact and file previews load from. Unset: [www.claudeusercontent.com](http://www.claudeusercontent.com).

***

### `inferenceCustomHeaders`

object: name → valueSince 1.8089.0

**Custom inference headers.** Extra headers sent with every model request. Routing and tenant headers only: do not put credentials here.

> [accordion] More detail
>
> This key is stored and distributed as plain configuration. For tokens, and for values that differ per user or session, have `inferenceCredentialHelper` print JSON with a `headers` field. On a conflict, the helper script's header takes priority.

***

### `inferenceCredentialHelper`

string

Consent required (A value that a bootstrap server or a self-hosted session host delivers applies only after the user approves it, unless machine-scoped device management set that server's address. For a bootstrap server, the trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)

Since 1.2581.0

**Helper script.** Absolute path to an executable that prints the credential, optionally with per-request headers.

> [accordion] More detail
>
> The helper script must exit with code `0`. Its standard output must hold only one of these, with no banners, prompts or log lines:
>
> * the token by itself
> * `{"token": "...", "headers": {"Name": "Value"}}`, to also send headers with each request
>
> The app sets `CLAUDE_HELPER_CONTEXT` so that the script can decide whether to prompt the user. [Write a credential helper](https://claude.com/docs/third-party/claude-desktop/credential-helper.md) lists its values.

***

### `inferenceCredentialHelperWindows`

string

Consent required (A value that a bootstrap server or a self-hosted session host delivers applies only after the user approves it, unless machine-scoped device management set that server's address. For a bootstrap server, the trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)

Since 2.2553.0

**Helper script (Windows).** Full path to the script that Windows devices run instead of Helper script. Unset: Helper script runs on every platform.

***

### `inferenceCredentialHelperArgs`

string\[]

Consent required (A value that a bootstrap server or a self-hosted session host delivers applies only after the user approves it, unless machine-scoped device management set that server's address. For a bootstrap server, the trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)

Since 2.110.0

**Helper script arguments.** Arguments passed to the helper script, one per entry, in order. Leave unset to run it with none.

> [accordion] More detail
>
> Do not put secrets in arguments: the diagnostic report and other processes on the device can see them.
>
> A Windows `.cmd` or `.bat` helper script receives each argument in double quotes. Read it with `%~1` to strip them.

***

### `inferenceCredentialHelperTtlSec`

integerDefault: 3600

Consent required (A value that a bootstrap server or a self-hosted session host delivers applies only after the user approves it, unless machine-scoped device management set that server's address. For a bootstrap server, the trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)

Range: 1 or moreSince 1.2581.0

**Helper script TTL.** Seconds the helper script’s output is cached. When it expires, the script runs again. Unset: 3600.

***

### `inferenceCredentialHelperTimeoutSec`

integerDefault: 60

Consent required (A value that a bootstrap server or a self-hosted session host delivers applies only after the user approves it, unless machine-scoped device management set that server's address. For a bootstrap server, the trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)

Range: 1–600Since 1.8089.0

**Credential helper timeout.** Seconds to wait for the helper script to finish. Raise this if it opens a browser for sign-in. Unset: 60.

***

### `inferenceCredentialHelperSilentRefreshEnabled`

booleanDefault: true

Consent required (A value that a bootstrap server or a self-hosted session host delivers applies only after the user approves it, unless machine-scoped device management set that server's address. For a bootstrap server, the trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)

Since 1.10628.0

**Re-run helper for silent refresh.** When the credential expires mid-session, run the helper script again to recover silently. Turn off if it cannot run without user input.

***

### `egressProxyUrl`

string

MDM only (You can set the key only in an MDM profile or the local configuration file. Claude Desktop ignores it in a bootstrap server's response.)

Since 1.44121.1

**Proxy server URL.** Send the app’s and the agent’s traffic through this HTTP proxy instead of the operating system’s proxy settings.

[Guide for this setting](https://claude.com/docs/third-party/claude-desktop/network-proxy.md)

[Admin Console](#the-works-with-column): Not available.

> [accordion] More detail
>
> This sets a route. It is not a network access control. If the proxy is unreachable, requests fail instead of connecting directly.
>
> **Not sent through this proxy:** Cowork's workspace VM on Linux, credential and header helper scripts, update downloads, the OS identity broker and the system browser.
>
> SOCKS proxies and embedded credentials (`user:pass@`) are rejected.
>
> This is an app-behavior key, like `disableAutoUpdates`. If your MDM profile holds nothing but such keys, the app reads them all from that profile alone, so put every one you use there.

***

### `egressProxyPacUrl`

string

MDM only (You can set the key only in an MDM profile or the local configuration file. Claude Desktop ignores it in a bootstrap server's response.)

Since 1.44121.1

**Proxy auto-config (PAC) URL.** URL of a PAC file that decides the proxy per request. Wins over the proxy server URL when both are set.

[Guide for this setting](https://claude.com/docs/third-party/claude-desktop/network-proxy.md)

[Admin Console](#the-works-with-column): Not available.

> [accordion] More detail
>
> If the PAC file cannot be downloaded, the app connects directly. On macOS and Windows, the Cowork workspace VM gets its own copy at each start. If that download fails, the VM connects directly until it next starts, with no warning. Block direct connections on your network if that is unacceptable.
>
> Claude Code, which runs Chat, Cowork and Code sessions, uses one proxy: the one the script returns for your inference endpoint. Return an HTTP `PROXY host:port` entry there. With `DIRECT` or only `SOCKS`, it uses no proxy.
>
> What `egressProxyUrl` lists as not sent through its proxy skips the PAC file too.
>
> This is an app-behavior key, like `disableAutoUpdates`. If your MDM profile holds nothing but such keys, the app reads them all from that profile alone, so put every one you use there.

***

### `coworkVmIpv6Enabled`

booleanSince 1.52386.0

**Enable IPv6 in the workspace VM.** Give the Cowork workspace VM an IPv6 address so Claude’s tools can reach IPv6-only hosts through the device. macOS and Windows only.

> [accordion] More detail
>
> IPv6 works in the VM only where the device's own IPv6 works.
>
> This is not a network access control. `coworkEgressAllowedHosts` still decides which hosts tools can reach, by name, over either protocol. It does not accept IPv6 addresses. Make sure your network filters the allowed hosts over IPv6 the way you intend.

***

### Gateway

#### `inferenceGatewayBaseUrl`

string

Consent required (A value that a bootstrap server or a self-hosted session host delivers applies only after the user approves it, unless machine-scoped device management set that server's address. For a bootstrap server, the trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)

Origin-pinned (A URL that a bootstrap server delivers must share the origin of bootstrapUrl, or Claude Desktop drops it. The limit is lifted when bootstrapOidc is set, and it does not apply to a value set in an MDM profile, the local configuration file or the Enterprise Admin Console.)

Since 1.2581.0

**Gateway base URL.** Full URL of the inference gateway endpoint.

***

#### `inferenceGatewayApiKey`

stringSince 1.2581.0

**Gateway API key.** API key for the configured inference gateway.

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

> [accordion] More detail
>
> * **`browser`:** register the redirect URI `http://127.0.0.1:<port>/callback` with your identity provider (for Entra, `http://127.0.0.1/callback`).
> * **`broker`:** uses Web Account Manager on Windows or Company Portal on macOS, and does not work on Linux. It can satisfy Conditional Access policies that require a compliant or managed device, or token protection.
>
> `broker` needs Microsoft Entra ID, with the `issuer` in `inferenceGatewayOidc` set to `https://login.microsoftonline.com/{tenant-id}/v2.0`. Add the redirect URIs listed under [Register the Entra ID application](https://claude.com/docs/third-party/claude-desktop/entra-broker.md#register-the-entra-id-application).

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

> [accordion] More detail
>
> Used with `inferenceCredentialKind` set to `interactive`. Leave it unset for a gateway that runs its own sign-in and serves `<baseUrl>/.well-known/oauth-authorization-server`.
>
> Your gateway must check the token's audience (`aud`). Otherwise it accepts any token from your tenant.
>
> Register the redirect URI given under `inferenceGatewayOidcAuthFlow`.

> [accordion] Child attributes (11)
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
> > [accordion] More detail
> >
> > An ID token's audience (`aud`) is `clientId`. An access token's audience must be your gateway or proxy.
> >
> > With Entra ID the scopes decide the audience, so add the gateway's API scope to `scopes`, such as `api://<gateway-app-id>/.default`.
>
> **scopes** `string`
>
> Space-separated scopes. Access-token mode needs the gateway or proxy API scope, and adds offline\_access unless Append offline\_access is off.
>
> > [accordion] More detail
> >
> > In ID-token mode, `offline_access` is not added to scopes that you set. Include it yourself, or users sign in again each time the token expires.
>
> **appendOfflineAccess** `boolean` (default: true)
>
> In access-token mode, add offline\_access to scopes so the identity provider returns a refresh token for silent refresh.
>
> > [accordion] More detail
> >
> > Turn off only if your authorization server rejects `offline_access` as an unknown scope. Then add the server’s own refresh-token scope to `scopes`.
>
> **resource** `string`
>
> Access-token audience of the gateway or proxy: an https URL or an AD FS relying-party identifier. Leave unset for Entra ID.
>
> > [accordion] More detail
> >
> > Use it only with `bearerTokenType` set to `access_token`, and only if your identity provider supports RFC 8707. Changing it signs users in again.
> >
> > For AD FS, enter one of the relying-party trust's identifiers. A value with no scheme is sent as `https://<value>`, so a plain name or GUID does not match. Add an `https://…` or `urn:…` identifier to the trust and enter that.
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
> Space-separated hostnames also accepted as the referrer of the sign-in callback, besides the authorization URL’s host.
>
> > [accordion] More detail
> >
> > If a callback is rejected for a referrer mismatch, the app log names the rejected host. Add that hostname here.

***

#### `inferenceIdpAuthFlow`

enumSince 2.7032.0

**Identity provider sign-in flow.** How the identity-provider sign-in runs: system browser (default) or the OS Microsoft Entra broker.

One of: `browser`, `broker`

> [accordion] More detail
>
> * **`browser`:** register the redirect URI `http://127.0.0.1:<port>/callback` with your identity provider (for Entra, `http://127.0.0.1/callback`).
> * **`broker`:** uses Web Account Manager on Windows or Company Portal on macOS, and does not work on Linux. It can satisfy Conditional Access policies that require a compliant or managed device, or token protection.
>
> `broker` needs Microsoft Entra ID, with the `issuer` in `inferenceIdpOidc` set to `https://login.microsoftonline.com/{tenant-id}/v2.0`. Add the redirect URIs listed under [Register the Entra ID application](https://claude.com/docs/third-party/claude-desktop/entra-broker.md#register-the-entra-id-application).

***

#### `inferenceIdpOidc`

object

Consent required (A value that a bootstrap server or a self-hosted session host delivers applies only after the user approves it, unless machine-scoped device management set that server's address. For a bootstrap server, the trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)

Since 2.7032.0

**Identity provider (OIDC).** Your organization’s OpenID Connect identity provider. The user’s token is sent as the Bearer credential to the gateway or the Bedrock proxy.

> [accordion] More detail
>
> Used when `inferenceCredentialKind` is `external-idp`. Register the redirect URI given under `inferenceIdpAuthFlow` with your identity provider.
>
> Your gateway or proxy must check the token's audience (`aud`). Otherwise it accepts any token from your tenant.
>
> On Bedrock, set `inferenceBedrockBaseUrl` to a proxy that checks the token, because Amazon Bedrock itself does not accept it. Also list your models in `inferenceModels`.

> [accordion] Child attributes (11)
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
> > [accordion] More detail
> >
> > An ID token's audience (`aud`) is `clientId`. An access token's audience must be your gateway or proxy.
> >
> > With Entra ID the scopes decide the audience, so add the gateway's API scope to `scopes`, such as `api://<gateway-app-id>/.default`.
>
> **scopes** `string`
>
> Space-separated scopes. Access-token mode needs the gateway or proxy API scope, and adds offline\_access unless Append offline\_access is off.
>
> > [accordion] More detail
> >
> > In ID-token mode, `offline_access` is not added to scopes that you set. Include it yourself, or users sign in again each time the token expires.
>
> **appendOfflineAccess** `boolean` (default: true)
>
> In access-token mode, add offline\_access to scopes so the identity provider returns a refresh token for silent refresh.
>
> > [accordion] More detail
> >
> > Turn off only if your authorization server rejects `offline_access` as an unknown scope. Then add the server’s own refresh-token scope to `scopes`.
>
> **resource** `string`
>
> Access-token audience of the gateway or proxy: an https URL or an AD FS relying-party identifier. Leave unset for Entra ID.
>
> > [accordion] More detail
> >
> > Use it only with `bearerTokenType` set to `access_token`, and only if your identity provider supports RFC 8707. Changing it signs users in again.
> >
> > For AD FS, enter one of the relying-party trust's identifiers. A value with no scheme is sent as `https://<value>`, so a plain name or GUID does not match. Add an `https://…` or `urn:…` identifier to the trust and enter that.
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
> Space-separated hostnames also accepted as the referrer of the sign-in callback, besides the authorization URL’s host.
>
> > [accordion] More detail
> >
> > If a callback is rejected for a referrer mismatch, the app log names the rejected host. Add that hostname here.

***

#### `inferenceStreamIdleTimeoutSec`

integerRange: 300–1,800Since 1.44121.1

**Stream idle timeout.** Extra seconds to wait for model output on a streaming response that is sending only keep-alive pings. Gateway provider only. Default 300.

> [accordion] More detail
>
> With pings arriving (SSE `ping` events or `:` comment lines), sessions accept at least about five minutes of them, then wait this many seconds more. With no pings, a silent response still fails after about 5 minutes whatever this value, so make the gateway send them.
>
> While this key is set, it takes priority over `CLAUDE_STREAM_IDLE_TIMEOUT_MS` in Claude Code's managed settings for sessions the app starts.

***

### Anthropic

#### `inferenceAnthropicApiKey`

stringSince 1.8089.0

**Claude API key.** Leave blank to sign in with your browser, or to supply the key via a credential helper.

[Admin Console](#the-works-with-column): Not available.

***

### Bedrock

#### `inferenceBedrockRegion`

stringSince 1.2581.0

**AWS region.** AWS region for the Bedrock runtime endpoint.

***

#### `inferenceBedrockBaseUrl`

string

Consent required (A value that a bootstrap server or a self-hosted session host delivers applies only after the user approves it, unless machine-scoped device management set that server's address. For a bootstrap server, the trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)

Origin-pinned (A URL that a bootstrap server delivers must share the origin of bootstrapUrl, or Claude Desktop drops it. The limit is lifted when bootstrapOidc is set, and it does not apply to a value set in an MDM profile, the local configuration file or the Enterprise Admin Console.)

Since 1.2581.0

**Bedrock base URL.** For VPC endpoints or gateway proxies. Enter https\:// and the host, with no path.

***

#### `inferenceBedrockServiceTier`

enumSince 1.5186.0

**Bedrock service tier.** Sent as the X-Amzn-Bedrock-Service-Tier header. Leave unset for on-demand.

One of: `flex`, `priority`

***

#### `inferenceBedrockBearerToken`

stringSince 1.2581.0

**AWS bearer token.** Static bearer token for inference. For providers that support profile or helper-script credentials, prefer those.

[Admin Console](#the-works-with-column): Not available.

***

#### `inferenceBedrockSsoStartUrl`

string

Consent required (A value that a bootstrap server or a self-hosted session host delivers applies only after the user approves it, unless machine-scoped device management set that server's address. For a bootstrap server, the trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)

Since 1.6259.0

**AWS SSO start URL.** Enables in-app AWS sign-in (no AWS CLI needed). Set with the three SSO fields below.

***

#### `inferenceBedrockSsoRegion`

string

Consent required (A value that a bootstrap server or a self-hosted session host delivers applies only after the user approves it, unless machine-scoped device management set that server's address. For a bootstrap server, the trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)

Since 1.6259.0

**AWS SSO region.** IAM Identity Center home region.

***

#### `inferenceBedrockSsoAccountId`

string

Consent required (A value that a bootstrap server or a self-hosted session host delivers applies only after the user approves it, unless machine-scoped device management set that server's address. For a bootstrap server, the trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)

Since 1.6259.0

**AWS SSO account ID.** 12-digit AWS account ID assigned to users in IAM Identity Center.

***

#### `inferenceBedrockSsoRoleName`

string

Consent required (A value that a bootstrap server or a self-hosted session host delivers applies only after the user approves it, unless machine-scoped device management set that server's address. For a bootstrap server, the trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)

Since 1.6259.0

**AWS SSO role name.** IAM Identity Center permission-set name granting bedrock:InvokeModel\* on the account above.

***

#### `inferenceBedrockProfile`

string

Consent required (A value that a bootstrap server or a self-hosted session host delivers applies only after the user approves it, unless machine-scoped device management set that server's address. For a bootstrap server, the trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)

Since 1.2581.0

**AWS profile name.** AWS named profile to use for Bedrock inference credentials.

***

#### `inferenceBedrockAwsDir`

string

Consent required (A value that a bootstrap server or a self-hosted session host delivers applies only after the user approves it, unless machine-scoped device management set that server's address. For a bootstrap server, the trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)

Since 1.2581.0

**AWS config directory.** Folder with AWS config/credentials. Defaults to \~/.aws when no bearer token is set.

***

#### `inferenceBedrockAwsCliPath`

string

Consent required (A value that a bootstrap server or a self-hosted session host delivers applies only after the user approves it, unless machine-scoped device management set that server's address. For a bootstrap server, the trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)

Since 1.13576.0

**AWS CLI path.** Absolute path to the aws executable. Leave unset to find it on PATH.

***

### Vertex

#### `inferenceVertexProjectId`

string

Consent required (A value that a bootstrap server or a self-hosted session host delivers applies only after the user approves it, unless machine-scoped device management set that server's address. For a bootstrap server, the trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)

Since 1.2581.0

**GCP project ID.** Google Cloud project ID for Vertex AI inference.

***

#### `inferenceVertexRegion`

stringSince 1.2581.0

**GCP region.** GCP region where your Vertex AI Claude models are deployed.

***

#### `inferenceVertexBaseUrl`

string

Consent required (A value that a bootstrap server or a self-hosted session host delivers applies only after the user approves it, unless machine-scoped device management set that server's address. For a bootstrap server, the trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)

Origin-pinned (A URL that a bootstrap server delivers must share the origin of bootstrapUrl, or Claude Desktop drops it. The limit is lifted when bootstrapOidc is set, and it does not apply to a value set in an MDM profile, the local configuration file or the Enterprise Admin Console.)

Since 1.2581.0

**Vertex AI base URL.** Private Service Connect endpoint, if you use one.

***

#### `inferenceVertexOAuthClientId`

string

Consent required (A value that a bootstrap server or a self-hosted session host delivers applies only after the user approves it, unless machine-scoped device management set that server's address. For a bootstrap server, the trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)

Since 1.2581.0

**Vertex OAuth client ID.** Desktop-app OAuth client ID. Enables Sign in with Google instead of a credentials file.

***

#### `inferenceVertexOAuthClientSecret`

stringSince 1.2581.0

**Vertex OAuth client secret.** Secret for the Desktop-app OAuth client above. Google does not treat such secrets as confidential, so the Admin Console can set it.

***

#### `inferenceVertexOAuthScopes`

stringSince 1.2581.0

**Vertex OAuth scopes.** Override the Google OAuth scopes (space-separated). Leave blank for the default.

***

#### `inferenceVertexOAuthLoginHint`

stringSince 1.12603.0

**Vertex OAuth login hint.** Pre-fill Google's account chooser and forward to your federated IdP. \{username} expands to the OS login name.

***

#### `inferenceVertexWorkforceAudience`

string

Consent required (A value that a bootstrap server or a self-hosted session host delivers applies only after the user approves it, unless machine-scoped device management set that server's address. For a bootstrap server, the trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)

Since 1.10628.0

**Workforce Identity audience.** Workforce-pool provider audience. When set, sign-in uses your own IdP plus a GCP STS exchange instead of a Google identity.

***

#### `inferenceVertexWorkforceUserProject`

string

Consent required (A value that a bootstrap server or a self-hosted session host delivers applies only after the user approves it, unless machine-scoped device management set that server's address. For a bootstrap server, the trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)

Since 1.10628.0

**Workforce Identity billing project.** GCP project for STS billing and quota. Defaults to the Vertex project ID above.

***

#### `inferenceVertexWorkforceAuthFlow`

enumSince 1.25927.0

**Workforce Identity sign-in flow.** How the IdP sign-in runs: system browser (default) or the OS Microsoft Entra broker.

One of: `browser`, `broker`

> [accordion] More detail
>
> * **`browser`:** register the redirect URI `http://127.0.0.1:<port>/callback` with your identity provider (for Entra, `http://127.0.0.1/callback`).
> * **`broker`:** uses Web Account Manager on Windows or Company Portal on macOS, and does not work on Linux. It can satisfy Conditional Access policies that require a compliant or managed device, or token protection.
>
> `broker` needs Microsoft Entra ID, with the `issuer` in `inferenceVertexWorkforceOidc` set to `https://login.microsoftonline.com/{tenant-id}/v2.0`. Add the redirect URIs listed under [Register the Entra ID application](https://claude.com/docs/third-party/claude-desktop/entra-broker.md#register-the-entra-id-application).

***

#### `inferenceVertexWorkforceOidc`

object

Consent required (A value that a bootstrap server or a self-hosted session host delivers applies only after the user approves it, unless machine-scoped device management set that server's address. For a bootstrap server, the trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)

Since 1.10628.0

**Workforce Identity IdP (OIDC).** Your organization’s OpenID Connect identity provider. Users sign in there, and the app exchanges their ID token at GCP STS.

> [accordion] Child attributes (9)
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
> Turn on only if your identity provider rejects offline\_access on this client. Users then sign in again each time the token expires.
>
> **additionalRedirectReferrerHosts** `string`
>
> Space-separated hostnames also accepted as the referrer of the sign-in callback, besides the authorization URL’s host.
>
> > [accordion] More detail
> >
> > If a callback is rejected for a referrer mismatch, the app log names the rejected host. Add that hostname here.

***

#### `inferenceVertexCredentialsFile`

string

Consent required (A value that a bootstrap server or a self-hosted session host delivers applies only after the user approves it, unless machine-scoped device management set that server's address. For a bootstrap server, the trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)

Since 1.2581.0

**GCP credentials file path.** Full path to a service-account JSON file. Unset: Application Default Credentials.

***

### Foundry

#### `inferenceFoundryResource`

string

Consent required (A value that a bootstrap server or a self-hosted session host delivers applies only after the user approves it, unless machine-scoped device management set that server's address. For a bootstrap server, the trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)

Since 1.2581.0

**Azure AI Foundry resource name.** Azure AI Foundry resource name used to construct the endpoint URL.

***

#### `inferenceFoundryBaseUrl`

string

Consent required (A value that a bootstrap server or a self-hosted session host delivers applies only after the user approves it, unless machine-scoped device management set that server's address. For a bootstrap server, the trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)

Origin-pinned (A URL that a bootstrap server delivers must share the origin of bootstrapUrl, or Claude Desktop drops it. The limit is lifted when bootstrapOidc is set, and it does not apply to a value set in an MDM profile, the local configuration file or the Enterprise Admin Console.)

Since 2.110.0

**Azure AI Foundry base URL.** Full base URL for a gateway or proxy in front of Foundry, path included (replaces [https://RESOURCE.services.ai.azure.com/anthropic](https://RESOURCE.services.ai.azure.com/anthropic)).

> [accordion] More detail
>
> Point it only at a gateway or proxy that you run. Requests carry the credential that the app would send to Foundry: the user's Entra ID token, the API key or the helper script's output.
>
> Use the value that you would give Claude Code as `ANTHROPIC_FOUNDRY_BASE_URL`. `inferenceFoundryResource` is still required and should name the resource behind the gateway.

***

#### `inferenceFoundryApiKey`

stringSince 1.2581.0

**Azure AI Foundry API key.** API key for Azure AI Foundry inference.

[Admin Console](#the-works-with-column): Not available.

***

#### `inferenceFoundryTenantId`

string

Consent required (A value that a bootstrap server or a self-hosted session host delivers applies only after the user approves it, unless machine-scoped device management set that server's address. For a bootstrap server, the trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)

Since 1.9255.0

**Entra ID tenant ID.** Directory (tenant) ID of the Entra ID app registration that has the Cognitive Services scope.

***

#### `inferenceFoundryClientId`

string

Consent required (A value that a bootstrap server or a self-hosted session host delivers applies only after the user approves it, unless machine-scoped device management set that server's address. For a bootstrap server, the trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)

Since 1.9255.0

**Entra ID client ID.** Application (client) ID of the Entra ID app registration. Device-code sign-in requires the app to allow public client flows.

***

#### `inferenceFoundryAuthFlow`

enumSince 1.19367.0

**Entra ID sign-in flow.** How Entra sign-in runs: device code (default), system browser, or the OS identity broker.

One of: `device-code`, `browser`, `broker`

> [accordion] More detail
>
> * **`device-code`:** shows a code to enter at microsoft.com/devicelogin. The app registration must have **Allow public client flows** enabled.
> * **`browser`:** register `http://127.0.0.1/callback` under **Mobile and desktop applications**. It works with **Allow public client flows** disabled. Conditional Access policies that block device-code sign-in do not affect it.
> * **`broker`:** uses Web Account Manager on Windows or Company Portal on macOS, and does not work on Linux. It can satisfy Conditional Access policies that require a compliant or managed device, or token protection. Add the redirect URIs listed under [Register the Entra ID application](https://claude.com/docs/third-party/claude-desktop/entra-broker.md#register-the-entra-id-application).

***

### Models

#### `modelDiscoveryEnabled`

booleanSince 1.8089.0

**Model discovery.** Auto-populate the model picker from the provider at launch.

> [accordion] More detail
>
> Turn this off if your network cannot reach your inference provider's model-list endpoint.
>
> * **Off:** `inferenceModels` is required and must use full model IDs. Tier aliases such as `sonnet` need discovery.
> * **Unset:** on. With a gateway or the Anthropic provider, the app skips discovery when `inferenceModels` is set and holds no tier alias.

***

#### `modelPrefer1mContext`

booleanSince 1.28929.0

**Use 1M wherever it’s available.** Every model that offers 1M context shows only its 1M option in the model picker.

> [accordion] More detail
>
> A listed model offers 1M when its `inferenceModels` entry sets `supports1m`. Without a list, a model offers 1M when your gateway's model list marks it.

***

#### `inferenceModels`

object\[]Since 1.2581.0

**Model list.** Override the auto-discovered model list. First entry is the default.

> [accordion] More detail
>
> Each entry is a model ID string or an object:
>
> ```json theme={null}
> [
>   {"name": "claude-sonnet-5",
>    "supports1m": true},
>   "claude-opus-4-8"
> ]
> ```
>
> Use your inference provider's exact model ID:
>
> * **Vertex:** the publisher ID (`claude-sonnet-5`).
> * **Bedrock:** the inference-profile ID (`us.anthropic.claude-sonnet-5`).
> * **Foundry:** the deployment name.
> * **Gateway:** the exact ID that its `/v1/models` endpoint returns.
>
> For Auto mode on a gateway, also list `claude-sonnet-5`. Its safety classifier calls that ID by default (see `autoModeEnabled`).

> [accordion] Child attributes (8)
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
> The Claude tier this model stands in for. A tier alias such as ‘opus’ then uses this model.
>
> One of: `sonnet`, `opus`, `haiku`, `fable`, `mythos`
>
> **isFamilyDefault** `boolean`
>
> When several models share a tier alias, marks this one as the model the alias resolves to. Otherwise the first listed wins.
>
> **behavesAs** `string`
>
> The Claude model behind an ID that the app cannot identify, such as a gateway alias. The ID gets that model’s effort levels and limits.
>
> > [accordion] More detail
> >
> > Enter a Claude model ID such as `claude-sonnet-5`. Region prefixes, dates and upper case are fine. A family name without `claude-`, such as `sonnet-5`, is ignored. The model picker also ignores a model that Claude Desktop does not know.
> >
> > If `name` contains a Claude model name with its version, as in `acme-claude-sonnet-4`, Claude Code uses that model and ignores this value. Enter that same model here. If that ID serves a different model, rename it so that it contains no version.
>
> **maxEffort** `enum`
>
> Highest effort level offered for this model. Claude Desktop hides higher levels and never requests them. An unrecognized value means low.
>
> One of: `low`, `medium`, `high`, `xhigh`, `max`

***

#### `defaultModelEffort`

enumSince 2.110.0

**Default model effort.** Effort level the default model (the first listed model) starts at, instead of Anthropic’s recommended level.

One of: `low`, `medium`, `high`, `xhigh`, `max`

> [accordion] More detail
>
> * A user's own effort choice for that model still applies, unless `alwaysStartWithDefaultModel` is on.
> * A level that the model does not offer becomes the nearest lower level, or its lowest if none is lower.
> * In Code, the `CLAUDE_CODE_EFFORT_LEVEL` environment variable or `effortLevel` in Claude Code's settings takes priority.
>
> Without `inferenceModels`, the default model is the first one your endpoint returns.

***

#### `alwaysStartWithDefaultModel`

booleanSince 2.110.0

**Always start with the default model.** Each new conversation or task starts on the default model and effort, not the user’s last choice. Users can still change both for that one.

***

#### `inferenceModelPricingEnabled`

booleanSince 1.37937.0

**Show estimated cost.** Show an estimated cost on the Usage page, at Anthropic list price unless you set a multiplier or per-model rates.

> [accordion] More detail
>
> The estimate is in USD. `inferenceModelPricingMultiplier` and `inferenceModelPricing` adjust it, and are ignored while this is off.
>
> Model IDs that cannot be matched to a Claude model, such as an opaque gateway alias, are left out until `inferenceModelPricing` gives them a rate.
>
> A `modelPricing` in Claude Code's managed settings takes priority over all three keys.

***

#### `inferenceModelPricingMultiplier`

numberRange: 0–1Since 1.37937.0

**Price multiplier.** Scales every estimated cost (0.85 = 85% of the price); between 0 and 1.

***

#### `inferenceModelPricing`

object\[]Since 1.37937.0

**Model pricing.** Per-model rates replacing Anthropic list price in the Usage page’s estimate.

> [accordion] Child attributes (5)
>
> **name** `string` *required*
>
> A model ID from the list above, or another ID or alias your provider serves. A built-in Claude ID also covers its dated and provider forms.
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

**Model catalog metadata.** Fetch Anthropic’s model catalog for model picker names, descriptions and effort options. When off, the app uses only its bundled copy.

[Admin Console](#the-works-with-column): Not available.

> [accordion] More detail
>
> On unless set to `false`. The app fetches Anthropic's signed catalog from `downloads.claude.ai`, or from `modelCatalogUrl` if that is set. The catalog never changes which models are offered, their order or the default model.
>
> When off, the app makes no catalog request. A model released after the installed version may then show no effort options until the app is updated.

***

#### `modelCatalogUrl`

stringSince 2.110.0

**Model catalog URL.** Get the model catalog from a mirror inside your network instead of downloads.claude.ai.

[Admin Console](#the-works-with-column): Not available.

> [accordion] More detail
>
> Mirror two Anthropic files unchanged: `https://downloads.claude.ai/model-catalog/v1/catalog.json` and its signature file. The app looks for the signature at this URL with `.raw-sig.json` added to the path.
>
> * The app refuses an edited or re-signed copy and keeps its last good one.
> * Use `https://`. The app does not follow redirects.
> * An invalid value turns the catalog fetch off. The app does not fall back to `downloads.claude.ai`.

***

## Capabilities

### Cowork surface

#### `coworkTabEnabled`

booleanDefault: trueSince 1.9659.0

**Allow Cowork.** Enable Cowork. Claude works on longer tasks like research, analysis, and documents.

***

### Code surface

#### `isClaudeCodeForDesktopEnabled`

booleanDefault: trueSince 1.2581.0

**Allow Code.** Enable Code. Claude writes and runs code.

***

#### `sshHostAllowlist`

string\[]

Beta (The feature that the key configures is in beta.)

Since 1.40609.0

**SSH host allowlist.** SSH hosts for Code sessions. Unset: off, unless the device’s Claude Code managed settings list hosts. \* allows any host.

[Guide for this setting](https://claude.com/docs/third-party/claude-desktop/ssh-remote-sessions.md)

> [accordion] More detail
>
> The app forwards the session's inference credential to the SSH host, plus your collector endpoint and auth headers when `otlpEndpoint` is set. List only hosts you trust with those.
>
> * **Entries:** a hostname (`build01.corp.example.com`) or a wildcard (`*.corp.example.com`, which also matches `corp.example.com`).
> * **Aliases:** list the `HostName` that the user's `~/.ssh/config` gives for a host, not its alias. List jump hosts too.
>
> This key governs which hosts the app offers, not network access. A host's own Claude Code managed settings replace the rules the app sends, unless they set `parentSettingsBehavior` to `"merge"`.

***

#### `sshClientPath`

string

Beta (The feature that the key configures is in beta.)

Consent required (A value that a bootstrap server or a self-hosted session host delivers applies only after the user approves it, unless machine-scoped device management set that server's address. For a bootstrap server, the trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)

Since 1.46388.1

**SSH client program.** Absolute path to the OpenSSH ssh program the app runs for SSH sessions. Unset: the first ssh on the user’s PATH.

[Guide for this setting](https://claude.com/docs/third-party/claude-desktop/ssh-remote-sessions.md)

> [accordion] More detail
>
> The app never runs another `ssh` in its place. If the program is missing, too old or cannot run, SSH sessions fail. So deliver this key only to devices that have the program.
>
> It must be OpenSSH 7.6 or newer. On Windows it must be an `.exe`, and the SSH remote sessions page lists stricter rules for its version and folder. With `sshTransport` set to `system-openssh`, a Windows path may start with `%LOCALAPPDATA%\` for a copy in each user's profile. Device management must set it as a plain string: a server may only repeat it.
>
> Choose a path that users cannot write to. Anyone who can replace the program can see SSH passwords and get around this key and `sshHostAllowlist`.

***

#### `sshTransport`

enum

Beta (The feature that the key configures is in beta.)

Since 1.52386.0

**SSH connection engine.** How Code connects over SSH: with the OpenSSH ssh program on the device, or with the app’s built-in SSH library. Unset: the app’s default.

One of: `auto`, `system-openssh`, `builtin`

[Guide for this setting](https://claude.com/docs/third-party/claude-desktop/ssh-remote-sessions.md)

> [accordion] More detail
>
> With `system-openssh`, your OpenSSH client's own Kerberos, certificate and `ssh_config` support applies. See `sshClientPath` for which program runs.
>
> * The program must be OpenSSH 7.6 or newer, and on Windows normally Win32-OpenSSH 9.4 or newer.
> * If `sshClientPath` is unset and Windows has no usable client, the app uses its built-in library instead.

***

### Chat surface

#### `chatTabEnabled`

booleanSince 1.13576.0

**Allow Chat.** Enable Chat. Quick questions and drafting.

***

#### `desktopHome`

enumSince 1.52386.0

**Desktop home.** Unified Claude: Chat and Cowork in one view. It replaces Allow Chat, Advanced file analysis, and Allow Cowork.

One of: `standard`, `off`

> [accordion] More detail
>
> `standard` turns on Unified Claude. `off` turns Chat and Cowork off, which leaves only Code, or nothing where Code is off. `isClaudeCodeForDesktopEnabled` still decides Code.
>
> **Unset:** the three settings that this key replaces decide until November 10, 2026 (12:00 PM PT). Current versions of the app started after that read an unset key as `standard`, whatever those three say. Cowork is then on even where `coworkTabEnabled` is `false`. One exception: where `chatSessionRetentionDays` is set and `coworkSessionRetentionDays` is not set to the same number of days, the three settings go on deciding.
>
> A non-empty value that the app does not recognize, such as `Standard`, is read as `off`.

***

#### `chatAdvancedFileAnalysisEnabled`

booleanSince 1.14271.0

**Advanced file analysis.** Allow Claude to run code in a local sandbox to analyze attached files it can’t read natively — like Excel and PowerPoint.

> [accordion] More detail
>
> Of the user's files, the sandbox can read only those attached to the conversation and folders added to the chat's project through the app (read-only).
>
> Commands reach the hosts in `coworkEgressAllowedHosts`, and none if that list is unset or empty. Plugin CLIs can always reach the hosts that their plugin declares.
>
> Commands run without an approval prompt. So they can upload anything the sandbox can read to a listed host, and run what they download from one. To have Claude ask before each command, set `Bash` to `ask` in `builtinToolPolicy`, which also applies to Cowork and Code.

***

### Workspace

#### `coworkEgressAllowedHosts`

string\[]Since 1.2581.0

**Allowed egress hosts.** Hosts that Claude’s tools can reach from Chat and Cowork, and partly from Code. Unset or empty: no web fetch in Chat and Cowork.

[Guide for this setting](https://claude.com/docs/third-party/claude-desktop/web-tools.md#web-fetch)

> [accordion] More detail
>
> Does not cover web search, model requests or MCP servers.
>
> * **Entries:** a hostname (`api.github.com`), a wildcard (`*.corp.com`, subdomains only) or `*` for all hosts.
> * **Ports:** an entry other than `*` can end in `:port`. In Cowork, web fetch and shell commands enforce the port. Code allows any port. Update all devices first: on an older version one such entry blocks every host for Cowork's shell commands.
> * **Plugins:** a plugin's command-line tools also reach the hosts that the plugin declares.
> * **Built-in browser:** a list other than `*`, even an empty one, also limits where Claude can browse.
> * **Code:** only shell commands are limited, and only where Claude Code's sandbox runs (see `allowedWorkspaceFolders`). Claude Code's own managed settings, where a session has any, take priority by default.

***

#### `allowedWorkspaceFolders`

object\[]Since 1.2581.0

**Allowed workspace folders.** Folders that Claude can use in chat projects, Cowork and Code. Code’s shell commands are only partly limited. Unset: all folders.

> [accordion] More detail
>
> Claude can read and write in every listed folder unless its `mode` is `ro`. An empty list allows none.
>
> * **Paths:** `~` and these variables expand per user: `%OneDrive%`, `%OneDriveCommercial%`, `%OneDriveConsumer%`, `%APPDATA%`, `%LOCALAPPDATA%`, `%USERNAME%`, `%XDG_DOCUMENTS_DIR%`. An entry with any other variable, or an unset one, adds no folder.
> * **Code shell commands:** this key turns on Claude Code's sandbox on macOS, and on Linux and WSL2 with bubblewrap and socat. There, most writes outside the list are refused, and most reads are not. Elsewhere, Windows included, only Claude's file tools follow the list. Claude Code's own managed settings, where a session has any, take priority by default.
>
> Do not list a home folder: it holds SSH keys and shell start-up files.

> [accordion] Child attributes (3)
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
> With `ro`, Cowork can view the folder but not change it. In Code this mostly limits file tools, not shell commands.
>
> One of: `rw`, `ro`
>
> > [accordion] More detail
> >
> > * **Code on the device:** Claude's file tools cannot change the folder. Shell commands still can.
> > * **Code over SSH:** the same, but shell commands are partly limited where Claude Code's sandbox runs on the host. Nothing is enforced on Windows hosts.
> >
> > In Code, a device or SSH host with Claude Code managed settings enforces nothing, unless they set `parentSettingsBehavior` to `merge`. Where a folder must not change, use the operating system's permissions. A read-only folder that holds Claude's own data, such as the home folder, is enforced in Cowork only.

***

#### `blockReadsOutsideWorkingDirectories`

booleanSince 1.46388.1

**Block reads outside working directories.** Keep Claude’s file tools from reading outside a Code session’s working directories. Shell commands are only partly limited.

> [accordion] More detail
>
> * **File tools** refuse most reads outside the session folder and any `allowedWorkspaceFolders`, in every permission mode.
> * **Shell commands:** where Claude Code's sandbox runs (see `allowedWorkspaceFolders`), most reads in the home folder and other user folders are refused. Elsewhere such reads ask for approval.
> * **Users** can re-open folders, even their whole home folder, in their own Claude Code settings.
>
> The user's git configuration files stay readable, and they can hold credentials.
>
> Claude Code's own managed settings, where a session has any, take priority by default.

***

#### `autoModeEnabled`

booleanSince 1.10628.0

**Allow Auto mode.** Offer Auto mode, where Claude decides which actions need approval. Unset: in Code only. True adds Cowork.

> [accordion] More detail
>
> Unless it is `false`, new Code sessions normally start in Auto mode.
>
> By default on a gateway, Auto mode sends its own requests to Claude Sonnet 5. Your gateway must accept the ID `claude-sonnet-5` and the `anthropic-beta` value `context-1m-2025-08-07`. If you set `inferenceModels`, list that ID there and in any group's model list. If not, Auto mode can block actions it would normally allow.

***

#### `disableBypassPermissionsMode`

booleanSince 1.46388.1

**Disable bypass permissions mode.** Remove the bypass permissions mode from Code sessions and Cowork tasks, so Claude always follows the permission policy. Off by default.

***

#### `disableBundledSkills`

booleanSince 1.15962.0

**Disable bundled skills and workflows.** Disables Claude Code’s bundled skills and workflows (deep-research and similar). Use where WebFetch/WebSearch aren’t available.

***

#### `skillCreationEnabled`

booleanSince 1.25927.0

**Allow user-created skills.** Let users create and upload their own skills, and let Claude save skills. Skill files added outside the app are not blocked.

> [accordion] More detail
>
> Skills already on the device stay usable. Plugins from your organization and bundled skills are not affected. To turn off bundled skills, use `disableBundledSkills`.

***

#### `skillScanningEnabled`

boolean

Beta (The feature that the key configures is in beta.)

Since 3.1623.0

**Scan user-created skills.** Run a security scan on each skill a user creates or uploads before it can be used. Skills that fail the security scan are blocked.

[Guide for this setting](https://claude.com/docs/third-party/claude-desktop/skill-scanning.md)

> [accordion] More detail
>
> How well the scan catches unsafe skills depends on your model. A skill judged possibly unsafe becomes usable, with a caution. Scan tokens count toward the user's usage and token limit.
>
> The app does not scan:
>
> * plugins
> * skills saved before you turn this on
> * skill files added or changed any other way, such as by a Code session
> * skills a session loads from `.claude/skills` folders
> * files in a skill named as PDFs or as some image, font, audio or video types, whatever they hold, and dependency lock files
>
> With `otlpEndpoint` set and `otlpDesktopLogLevel` not `off`, the app sends your OpenTelemetry collector one record for each finished scan, with no retry. It holds the skill's name, a scan id, the verdict and the model's short summary of why, which may quote the skill.

***

#### `userPluginMarketplacesEnabled`

booleanSince 1.37937.0

**Allow user-added plugin marketplaces.** Let users add plugin marketplaces. When off, the app hides the ones your organization did not add and normally does not load their plugins.

> [accordion] More detail
>
> Nothing is deleted: turning it back on restores the hidden marketplaces.
>
> * It does not limit Claude Code in a terminal.
> * Claude Code's own managed settings, where a session has any, take priority by default. Restrict marketplaces in those settings as well.
>
> Applies only while the app runs in third-party mode. If users could otherwise sign in to Claude.ai on the device, also set `disableDeploymentModeChooser` so the app stays in third-party mode.

***

#### `userPluginUploadsEnabled`

booleanSince 1.37937.0

**Allow user-added plugins.** Allow users to add their own plugins. When off, the app hides every option for adding one and refuses uploads.

> [accordion] More detail
>
> Plugins that are already installed, or placed on disk outside the app, are not removed or blocked.
>
> Applies only while the app runs in third-party mode. If users could otherwise sign in to Claude.ai on the device, also set `disableDeploymentModeChooser` so the app stays in third-party mode.

***

#### `scheduledTasksEnabled`

booleanSince 2.110.0

**Allow scheduled tasks.** Allow scheduled tasks in Cowork and Code. When off, scheduling is hidden, existing tasks stop running and Claude cannot create new ones.

> [accordion] More detail
>
> Existing tasks are kept, not deleted, and run again when this is turned back on. While off, sessions also start without Claude Code's own scheduling tools, such as the `/loop` command.

***

#### `projectsEnabled`

booleanSince 4.4212.0

**Allow projects.** Let users group chats and Cowork tasks into projects. When off, projects are hidden, not deleted.

> [accordion] More detail
>
> Turning this off only hides projects. Their tasks and chats stay in the list, ungrouped. Their data stays on the user's device, and they come back when you turn it on again.
>
> A task that is still open in a project keeps working with what it was started with. A scheduled task set up in a project keeps running in it. To stop it, turn off `scheduledTasksEnabled`, which stops all scheduled tasks.

***

#### `keepAwakeEnabled`

booleanSince 2.7032.0

**Allow keep awake.** Let Claude keep the device awake. When off, Claude never prevents sleep and hides its keep-awake switches.

***

#### `developerModeEnabled`

booleanSince 2.37337.1

**Allow Developer Mode.** Let users turn on Developer Mode. When off, the app’s developer tools and the option to install an unpacked extension are unavailable.

> [accordion] More detail
>
> Unpacked extensions that are already installed keep working. An extension folder copied by hand into the app's extensions folder is not blocked. Packaged (`.mcpb`) extensions follow `isDesktopExtensionEnabled`, not this key.

***

#### `quickEntryDefaultShortcut`

stringSince 3.1623.0

**Default Quick Entry shortcut.** Set the shortcut that opens Quick Entry, such as Ctrl+Alt+K, for users who haven’t set their own in Settings. Use “off” for no shortcut.

> [accordion] More detail
>
> Unset keeps the built-in shortcut: double-tap Option on macOS, `Ctrl+Alt+Space` elsewhere.
>
> * **Combination:** pair `Ctrl`, `Cmd` or `Super` with `Alt` or `Shift`, plus one key other than `Insert`, `Capslock` or `F5`. Names are case-sensitive.
> * `off`: the string, not `false`.
> * `double-tap-option`: macOS only.
>
> Claude ignores a value that it does not accept, as if unset. Other apps do not receive the shortcut while Claude runs, so choose one that users do not need elsewhere.

***

#### `quickEntryScreenshotsEnabled`

booleanSince 3.6556.1

**Allow screenshots of the screen and other apps.** Let users screenshot their screen or other apps’ windows in Quick Entry on macOS. When off, it never asks for Screen Recording access.

> [accordion] More detail
>
> When off, another app's window that a user mentions with @ in a chat also comes without its picture.
>
> Not covered: screenshots that users take with the operating system's own tools and paste in, and pictures that Claude takes of its own content. A local MCP server or desktop extension can still capture the screen (`isLocalDevMcpEnabled`, `isDesktopExtensionEnabled`).

***

#### `quickEntryFileSharingEnabled`

booleanSince 3.6556.1

**Allow sharing files open in other apps.** Let users attach the file open in another app’s window in Quick Entry on macOS. When off, it never asks for Accessibility access.

> [accordion] More detail
>
> Off applies even where the Accessibility permission is already granted. Another app's window that a user mentions with @ in a chat then also comes without its file. Not covered: Claude's other uses of that permission, and files that users attach themselves.

***

#### `skipWebFetchPreflight`

booleanSince 1.37937.0

**Skip WebFetch domain check.** Skip Claude Code’s WebFetch domain lookup against api.anthropic.com in Code sessions. Off by default; turn on when that host is blocked.

> [accordion] More detail
>
> Before fetching a page, Claude Code's WebFetch tool asks `api.anthropic.com` whether the domain is on Anthropic's content blocklist.
>
> * **Off:** where the host is reachable, every fetched hostname is sent to Anthropic. Where it is blocked, every WebFetch in Code sessions fails.
> * **On:** Code sessions fetch without the lookup and never contact that host for it.

***

#### `builtinToolPolicy`

object: name → valueSince 1.8089.0

**Built-in tool policy.** Approval per tool or rule such as Bash(curl \*). “ask” prompts the user before each matching call. To block, use Disabled built-in tools.

> [accordion] More detail
>
> Entries use the same tool names and rules as `disabledBuiltinTools`, with the same limits. Command rules are not a security boundary, and `Bash(…)` rules do not cover `PowerShell`.
>
> `ask` also turns off the user's saved “always allow” choices for that tool. A scheduled task in Cowork waits at the prompt.
>
> **Rules such as `Bash(curl *)`:** Claude Code's own managed settings, where a session has any, take priority by default. A tool name such as `Bash` still applies. Update all devices first: an older version drops these rules, so the tool runs without a prompt.
>
> An unusable entry is dropped and recorded as a configuration error.

***

#### `disabledBuiltinTools`

string\[]Since 1.2581.0

**Disabled built-in tools.** Built-in tools, or rules such as Read(//etc/\*\*), blocked in Cowork and Code. Shell commands do not fully follow file-path rules.

> [accordion] More detail
>
> An entry is a [tool name](https://code.claude.com/docs/en/tools-reference) such as `Bash`, or a [permission rule](https://code.claude.com/docs/en/permissions#permission-rule-syntax) such as `Edit(//etc/**)`.
>
> Start a full path with `//`, not `/`. A relative rule such as `Read(**/.env)` covers only a Code session's project folder. `Bash(…)` rules apply in Code only. Command rules match command text and are not a security boundary.
>
> Only Code's sandbox (see `allowedWorkspaceFolders`) hides a denied folder from its shell: list the full path (`Read(//srv/keys/**)`). Don't rely on it alone: keep secrets the user's account can't read.

***

#### `toolSearchEnabled`

booleanDefault: falseSince 1.21459.0

**Enable tool search.** Load MCP tool definitions only when Claude needs them (tool search), instead of keeping all of them in context.

[Guide for this setting](https://claude.com/docs/third-party/claude-desktop/gateway.md#mcp-tool-search)

> [accordion] More detail
>
> Your gateway or provider must accept what tool search adds, such as `tool-search-tool-2025-10-19` in the `anthropic-beta` header. Otherwise requests fail with HTTP 400. On Foundry or a custom base URL, requests also carry Claude Code's other experimental betas.
>
> On Claude API, Vertex AI, Bedrock and Bedrock Mantle with no custom base URL, tool search is normally on and this key has no effect.

***

#### `organizationInstructions`

stringSince 1.37937.0

**Organization instructions.** Appended to Claude’s system prompt in Chat, Cowork, and Code. Guidance the model follows, not an enforced control. Up to 3,000 characters.

> [accordion] More detail
>
> Claude is told that they take priority over a user's personal preferences.
>
> A value over 3,000 characters is ignored with a configuration error, not shortened. The Group Policy (ADMX) and Intune text box holds a single line. JSON, `.mobileconfig` and `.reg` files keep line breaks.

***

#### `requireCoworkFullVmSandbox`

booleanDefault: false

Deprecated (On third-party deployments Claude Desktop no longer reads the key and ignores any value set for it. Remove it from your configuration.)

Since 1.2581.0

**Require full VM sandbox.** Runs tools inside an isolated VM instead of the host. Stronger isolation; slower file access and no host-process tools.

[Admin Console](#the-works-with-column): Not available.

***

### Authentication

#### `disableDeploymentModeChooser`

booleanDefault: falseSince 1.3834.0

**Disable Claude.ai sign-in.** Users see only this provider at the login screen. The option to sign in to Claude.ai is hidden.

[Admin Console](#the-works-with-column): Not available.

> [accordion] More detail
>
> In an MDM profile, this key also keeps that profile in charge. Without it, a user can sign in to Claude.ai with an organization that configures Claude Desktop in the Admin Console. The device then mostly follows that organization's configuration, at later launches too.
>
> * A value sent only by the bootstrap server does not do this.
> * `forceLoginOrgUUID` in the profile limits the move to the organizations it lists.
> * Added to a profile that sets only app-behavior keys such as `disableAutoUpdates`, it makes that profile the device's whole configuration.

***

#### `disableDeepLinkRegistration`

booleanDefault: falseSince 1.6889.0

**Disable claude:// deep-link handling.** Stop external apps and websites from opening Claude Desktop via claude:// links.

***

### Built-in browser

#### `builtinBrowserEnabled`

booleanDefault: falseSince 2.2553.0

**Allow the built-in browser.** A browser in Cowork and Code where users and Claude can open and work with web pages. Site sign-ins stay on the device until cleared.

[Admin Console](#the-works-with-column): Set automatically.

> [accordion] More detail
>
> The app checks the addresses of public sites that open or are framed in the browser (query removed) against Anthropic's site safety list on `releases.claude.com`.
>
> * The check is signed out, with no account, organization, or device identifier. In an Admin Console organization it is signed in, on the host that serves the configuration.
> * Private addresses, names resolving to them, and internal-suffix or single-label names are never sent. A name under a public domain is checked even if only your VPN resolves it.
> * Allow `releases.claude.com` through your firewall. If a check fails, users can browse but Claude's page tools stay off for that site.

***

#### `builtinBrowserDefaultDomainPolicy`

enumDefault: allowSince 2.2553.0

**Default site policy in the built-in browser.** Whether Claude may open sites in the built-in browser by default. Users can still view any site. Unset: allow.

One of: `allow` (default), `block`

[Admin Console](#the-works-with-column): Set automatically.

> [accordion] More detail
>
> A `coworkEgressAllowedHosts` list other than `*` applies on top of either value: Claude cannot open sites outside it.
>
> Pages, even ones that a user opened, cannot load frames, scripts or images from other sites that the policy does not allow. Under `block`, or with a `coworkEgressAllowedHosts` list, include the CDN and API hosts that your allowed sites depend on.

***

#### `builtinBrowserAllowedDomains`

string\[]Since 2.2553.0

**Allowed sites in the built-in browser.** Sites Claude may open, read, and act on in the built-in browser when the default site policy is block. Users can still view other sites.

[Admin Console](#the-works-with-column): Set automatically.

> [accordion] More detail
>
> Entries use the same format as `coworkEgressAllowedHosts`, except:
>
> * `example.com` also covers `www.example.com`, but no other subdomain.
> * `*` is ignored, and so is a wildcard on a public suffix, such as `*.co.uk`.
>
> A site that Anthropic's site safety list blocks stays blocked to Claude. Where that list only asks for confirmation, Claude works with a listed site without asking before each action.

***

#### `builtinBrowserBlockedDomains`

string\[]Since 2.2553.0

**Blocked sites in the built-in browser.** Sites Claude may not open, read, or act on in the built-in browser when the default site policy is allow. Users can still view them.

[Admin Console](#the-works-with-column): Set automatically.

> [accordion] More detail
>
> Entries use the same format as `coworkEgressAllowedHosts`. `*` blocks every external site. `example.com` also covers `www.example.com`, but no other subdomain. An entry outside that format matches nothing.
>
> A blocked site is refused before the site safety check, so its address is never sent to Anthropic.

***

### Claude.ai data import

#### `claudeAiImport`

objectSince 1.10628.0

**Claude.ai data import.** Lets users import Claude.ai chats and projects, and earlier Claude sessions on this device.

> [accordion] Child attributes (5)
>
> **enabled** `boolean` (default: false)
>
> Lets users import a Claude.ai data export and earlier Claude sessions on this device from Settings → Import.
>
> **allowedOrganizationUuids** `string[]`
>
> When set, users import by sign-in only, and only from the Claude.ai organizations with these IDs.
>
> > [accordion] More detail
> >
> > * The list narrows `enabled`. It turns nothing on by itself and does not affect `automatic3pImport`.
> > * An empty list, or one that cannot be read, allows no organization, so no import is offered. A null or empty string counts as unset.
> > * Each import is reported to your OpenTelemetry collector with the ID of its organization. Set `otlpDesktopLogLevel` to `info` to receive it.
>
> **automatic3pImport** `boolean`
>
> Copy this computer’s earlier third-party sessions into the app once, in the background. Independent of `enabled`.
>
> > [accordion] More detail
> >
> > Unset is off, except in Admin Console organizations, where it is on unless an admin turns it off. Without the Admin Console, also set `deploymentOrganizationUuid`. Only sessions stored before you set it are copied.
> >
> > It brings back more than sessions, without asking the user. That includes:
> >
> > * The user's Cowork memory, global instructions and Instructions for Claude, which are used at once, unreviewed.
> > * Scheduled tasks. A task that was on runs at its next scheduled time.
> > * Uploaded plugins, unless `userPluginUploadsEnabled` is off. They can run programs on the device.
> > * Saved skills, unless `skillCreationEnabled` is off.
>
> **exportEnabled** `boolean` (default: false)
>
> Lets users export this device’s chats, Cowork tasks and Code sessions as a zip to import elsewhere. No effect unless Enable import is on.
>
> > [accordion] More detail
> >
> > Transcripts contain conversation content including tool outputs. Treat exported zips as sensitive data.
>
> **bannerBehavior** `enum`
>
> Prompt to import on a new chat or task, if Enable import is on. `show`: always. `detect`: if earlier Claude sessions are found. Unset: off.
>
> One of: `off`, `detect`, `show`

***

## Connectors

### MCP

#### `managedMcpServers`

object\[]Since 1.2581.0

**Managed MCP servers.** Org-pushed MCP servers: remote (HTTP/SSE) or local (stdio command).

> [accordion] More detail
>
> Values of an entry's `toolPolicy`, per tool name:
>
> * `allow`: pre-approves the tool, except in Code and for built-in connector tools that send or cannot be undone.
> * `ask`: every call needs approval, with no option to always allow. A scheduled Cowork task waits at the prompt.
> * `blocked`: the tool is removed from the session.
>
> A name can contain `*`, as in `read_*`. When several wildcards match, the strictest applies. An exact name normally takes priority over a wildcard. To block by default, use `"*": "blocked"` plus exact `allow` entries.

> [accordion] Child attributes
>
> **name** `string` *required*
>
> Must be unique. A rename resets each user’s on/off choice, tool permissions and device sign-in, and can break a plugin server’s match.
>
> > [accordion] More detail
> >
> > After a rename:
> >
> > * Users' own choices start over: a server they had turned off can be on again, and a tool they had blocked is no longer blocked.
> > * If a plugin's server matched this entry by name, the entry's `toolPolicy` may stop applying to it.
> > * In the Admin Console, enter a permission policy's rules for the server again. They do not carry over.
> > * Giving the entry its old name back restores users' choices and tool permissions.
> >
> > Do not reuse an old name for a different server. It can inherit choices that users made for the old one.
>
> **toolPolicy** `object: name → value`
>
> Lock the approval state for specific tools. Unlisted tools stay user-controlled.
>
> > [accordion] More detail
> >
> > Also applies to an installed plugin's server that matches this entry by URL, or else by name (letter case is ignored).
> >
> > * That server follows this entry instead of `orgPluginSettings`, even if the entry sets no `toolPolicy`. A built-in entry (one with `server`) applies only if it sets one.
> > * For a server that only a plugin runs, use an entry with `transport: "policy-only"`.
> > * Claude Code runs or connects to some plugin servers itself. For those: Claude Code's own managed settings, where a session has any, take priority by default.
>
> > [tab] microsoft365
> >
> > Applies when `server` is `microsoft365`. The in-app configuration window calls it **Microsoft 365**.
> >
> > **server** `string` *required*
> >
> > Which bundled connector this entry turns on. Set instead of a transport; each built-in server has its own fields.
> >
> > Must be: `microsoft365`
> >
> > **tenantId** `string` *required*
> >
> > Your organization’s Microsoft Entra directory (tenant) ID.
> >
> > **clientId** `string` *required*
> >
> > OAuth app client ID for this built-in server.
> >
> > **azureCloud** `enum`
> >
> > Microsoft cloud for sign-in and Graph. Use global for commercial Microsoft 365. US Government clouds need your own app registration.
> >
> > One of: `global`, `us-gov-high`, `us-gov-dod`
> >
> > **continuousAccessEvaluation** `enum` (default: enabled)
> >
> > Requests Microsoft Graph tokens that last up to about 28 hours but can be revoked within minutes. “disabled” keeps one-hour tokens.
> >
> > One of: `enabled` (default), `disabled`
> >
> > > [accordion] More detail
> > >
> > > With a Conditional Access policy on IP named locations or Global Secure Access compliant networks, a token presented from outside that network is cut off. Tenants without such a policy get no network-based replay protection.
> > >
> > > After a change, users sign in again.
> >
> > **scope** `string`
> >
> > What the server may request at sign-in. If blank, Desktop’s default read set is used.
>
> > [tab] websearch
> >
> > Applies when `server` is `websearch`. The in-app configuration window calls it **Web search**.
> >
> > **headers** `object: name → value`
> >
> > Static headers sent on every request: routing and tenant headers only. No credentials here: use the headers helper script for those.
> >
> > **headersHelper** `string`
> >
> > Consent required (A value that a bootstrap server or a self-hosted session host delivers applies only after the user approves it, unless machine-scoped device management set that server's address. For a bootstrap server, the trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)
> >
> > Script that prints the auth header as a JSON object to stdout. Runs before each request (cached for the TTL below).
> >
> > > [accordion] More detail
> > >
> > > The helper script normally runs with `CLAUDE_CODE_MCP_SERVER_NAME` set to this entry's `name`, so one script can serve several servers. Put the variable in double quotes, compare it with the names you expect, and do not pass it to another command.
> >
> > **headersHelperArgs** `string[]`
> >
> > Consent required (A value that a bootstrap server or a self-hosted session host delivers applies only after the user approves it, unless machine-scoped device management set that server's address. For a bootstrap server, the trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)
> >
> > Arguments passed to the headers helper script, one per entry, in order. Leave unset to run it with none.
> >
> > > [accordion] More detail
> > >
> > > * On every platform, an argument cannot be empty or contain a double quote, a percent sign or a control character.
> > > * Do not put secrets in arguments. They are visible in the app log and to other processes on the device.
> > > * Have the script fail when a needed argument is missing. An app version that does not know this setting passes none.
> >
> > **headersHelperTtlSec** `integer`
> >
> > How long the helper’s headers are reused before it runs again, in seconds. Defaults to 300.
> >
> > **headersHelperRefreshBufferSec** `integer`
> >
> > Seconds before the TTL expires at which the helper re-runs mid-session. Defaults to 60. Keep it larger than the helper’s typical runtime.
> >
> > **server** `string` *required*
> >
> > Which bundled connector this entry turns on. Set instead of a transport; each built-in server has its own fields.
> >
> > Must be: `websearch`
> >
> > **provider** `enum` *required*
> >
> > Runs web search from the user’s device, for inference providers without built-in search. Supply the API key with the headers helper script.
> >
> > One of: `brave`, `tavily`, `exa`, `custom`
> >
> > > [accordion] More detail
> > >
> > > Not needed on the Anthropic API or Vertex, where the model's built-in web search is available.
> > >
> > > Every search provider except `custom` needs an auth header. The API key is a credential, so have `headersHelper` print the header rather than storing it in `headers`:
> > >
> > > * **Brave:** `X-Subscription-Token`
> > > * **Exa:** `x-api-key`
> > > * **Tavily:** `Authorization` (Bearer …)
> >
> > **platformOverrides** `object`
> >
> > On that operating system, each setting here replaces the entry’s own. A setting left out keeps the entry’s.
> >
> > > [accordion] More detail
> > >
> > > A value written here replaces the entry's value whole: lists and maps are not merged.
> > >
> > > * A local (`stdio`) entry can repeat `command`, `args`, `env`, `envHelper` and `envHelperArgs`. It always needs its own `command` too.
> > > * A remote or web search entry can repeat `headersHelper` and `headersHelperArgs`. If it gives `headersHelper` here, it needs its own too.
> > > * A mistake under any operating system drops the server on all of them.
> > > * An older version ignores this setting and runs the entry's own values. Until all devices are updated, put the Windows values in the entry itself.
> >
> > > [accordion] Child attributes (3)
> > >
> > > **platformOverrides.win32** `object: name → value`
> > >
> > > On Windows, these replace the entry’s own settings. A setting left out keeps the entry’s.
> > >
> > > **platformOverrides.darwin** `object: name → value`
> > >
> > > On macOS, these replace the entry’s own settings. A setting left out keeps the entry’s.
> > >
> > > **platformOverrides.linux** `object: name → value`
> > >
> > > On Linux, these replace the entry’s own settings. A setting left out keeps the entry’s.
> >
> > **customUrl** `string`
> >
> > POST endpoint accepting \{q} JSON and returning a results\[] array. Only used when provider is Custom.
>
> > [tab] github
> >
> > Applies when `server` is `github`. The in-app configuration window calls it **GitHub**.
> >
> > **server** `string` *required*
> >
> > Which bundled connector this entry turns on. Set instead of a transport; each built-in server has its own fields.
> >
> > Must be: `github`
> >
> > **clientId** `string` *required*
> >
> > GitHub OAuth app client ID (device flow must be enabled on the app).
> >
> > **host** `string`
> >
> > Leave blank for github.com. For GitHub Enterprise Server, your instance’s base URL.
> >
> > **scope** `string`
> >
> > Space-separated GitHub OAuth scopes. Unset: Desktop’s default scopes. Ignored for GitHub Apps: their registration sets the permissions.
> >
> > **toolsets** `string`
> >
> > Comma-separated github-mcp-server toolsets to enable. If blank, the bundled server’s default toolsets are used.
> >
> > > [accordion] More detail
> > >
> > > Every tool that can change something asks before each call unless `toolPolicy` says otherwise.
> > >
> > > These tools cannot be set looser than `ask`, and `allow` is treated as `ask`: `merge_pull_request`, `push_files`, `create_or_update_file`, `delete_file`, `actions_run_trigger`, `pull_request_review_write`, `delete_repository`. Where no prompt can be shown, their calls are refused.
> >
> > **readOnly** `boolean`
> >
> > Offer only read tools — the server registers no write tools at all.
>
> > [tab] http / sse
> >
> > Applies when `transport` is `http` or `sse`. The in-app configuration window calls it **Streamable HTTP** or **SSE (legacy)**.
> >
> > **transport** `enum` *required*
> >
> > How the app connects: HTTP, legacy SSE or a local command (stdio). policy-only connects to nothing: it sets a plugin server’s tool policy.
> >
> > One of: `http`, `sse`
> >
> > **url** `string` *required*
> >
> > HTTPS endpoint of the remote MCP server. Use the server’s final address: HTTP redirects are not followed.
> >
> > **oauth** `object`
> >
> > OAuth sign-in for a remote server: register a client automatically, use your own client ID, or use an Anthropic-hosted client identity.
> >
> > [Guide for this setting](https://claude.com/docs/third-party/claude-desktop/mcp-sign-in.md)
> >
> > > [accordion] More detail
> > >
> > > Choose **Bring your own client** when the provider requires an OAuth client that you register, and set `clientId`. Add `clientSecret` and `authorizationServer` only when the provider also requires the secret.
> >
> > > [accordion] Child attributes
> > >
> > > > [tab] dcr
> > > >
> > > > Applies when `oauth.mode` is `dcr`. The in-app configuration window calls it **Auto-register (dynamic client registration)**. No other fields apply.
> > > >
> > > > Write `"oauth": true`. `{"mode": "dcr"}` means the same and takes no other member. To register automatically with scopes of your choice, write an object that sets any of `scope`, `appendOfflineAccess` and `additionalRedirectReferrerHosts` and nothing else, as Bring your own client describes.
> > >
> > > > [tab] byo
> > > >
> > > > Applies when `oauth.mode` is `byo`. The in-app configuration window calls it **Bring your own client**.
> > > >
> > > > `mode` can be left out. Without `clientId` the object may set only `scope`, `appendOfflineAccess` and `additionalRedirectReferrerHosts`, and the app registers a client automatically; with any other member listed here and no `clientId`, the app drops the entry.
> > > >
> > > > **oauth.clientId** `string`
> > > >
> > > > OAuth client ID from your identity provider’s app registration. Unset: auto-register (dynamic client registration).
> > > >
> > > > **oauth.clientSecret** `string`
> > > >
> > > > Only if the provider requires one. The Admin Console stores only a Google Desktop-app secret (GOCSPX-…). For others use the helper script.
> > > >
> > > > **oauth.clientSecretHelper** `string`
> > > >
> > > > Consent required (A value that a bootstrap server or a self-hosted session host delivers applies only after the user approves it, unless machine-scoped device management set that server's address. For a bootstrap server, the trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)
> > > >
> > > > Script that prints the client secret as a JSON object with a single clientSecret key. Takes priority over Client secret.
> > > >
> > > > > [accordion] More detail
> > > > >
> > > > > * Its standard output must be exactly `{"clientSecret": "…"}`, with no other keys or lines. Any other output stops the server from connecting.
> > > > > * It must exit with code `0` within 30 seconds.
> > > > > * It runs with no arguments each time the server connects and each time its sign-in is renewed in the background. Choose a script that does not prompt the user.
> > > > >
> > > > > The helper script normally runs with `CLAUDE_CODE_MCP_SERVER_NAME` set to this entry's `name`, so one script can serve several servers. Put the variable in double quotes, compare it with the names you expect, and do not pass it to another command.
> > > >
> > > > **oauth.authorizationServer** `string[]`
> > > >
> > > > Issuer URLs the OAuth sign-in may use, as a JSON array. Pre-filled by presets; ask your IdP admin if unsure.
> > > >
> > > > **oauth.authorizationUrl** `string`
> > > >
> > > > Only for IdPs that don’t serve a .well-known discovery document. Set together with Token URL; requires Client ID.
> > > >
> > > > **oauth.tokenUrl** `string`
> > > >
> > > > Only for IdPs that don’t serve a .well-known discovery document. Set together with Authorization URL; requires Client ID.
> > > >
> > > > **oauth.tenantId** `string`
> > > >
> > > > Required for single-tenant Entra apps. Leave blank for multi-tenant or non-Microsoft IdPs.
> > > >
> > > > > [accordion] More detail
> > > > >
> > > > > For a GCC High or DoD tenant, leave this unset and set `authorizationServer` to `https://login.microsoftonline.us/<tenant-id>/v2.0`.
> > > >
> > > > **oauth.authFlow** `enum`
> > > >
> > > > How Entra sign-in runs for this server: the system browser (default) or the OS identity broker.
> > > >
> > > > One of: `browser`, `broker`
> > > >
> > > > > [accordion] More detail
> > > > >
> > > > > `broker` signs in through the OS identity broker: Web Account Manager on Windows, the Company Portal SSO extension on macOS. It can satisfy Conditional Access policies that require a compliant or managed device, or token protection.
> > > > >
> > > > > * It requires `tenantId`, `clientId` and `scope`, and an Entra-registered device.
> > > > > * The app registration must list the [broker redirect URIs](https://claude.com/docs/third-party/claude-desktop/entra-broker.md).
> > > > > * `broker` is not supported on Linux. Where the broker is not available, sign-in falls back to the system browser.
> > > >
> > > > **oauth.scope** `string`
> > > >
> > > > Space-separated scopes to request. Unset: the scopes the server advertises. Required if Tenant ID is set or the resource parameter omitted.
> > > >
> > > > **oauth.appendOfflineAccess** `boolean`
> > > >
> > > > Adds offline\_access to the authorize request so the IdP returns a refresh token for silent renewal.
> > > >
> > > > > [accordion] More detail
> > > > >
> > > > > Leave off if `scope` already includes `offline_access` or the server rejects it.
> > > > >
> > > > > If you set `authorizationUrl` and `tokenUrl`, this switch does not work on its own. Add `offline_access` to `scope` instead.
> > > >
> > > > **oauth.omitResource** `boolean`
> > > >
> > > > Sends no OAuth resource parameter. Use only if your identity provider rejects it. Requires Client ID, Scope and one sign-in server.
> > > >
> > > > > [accordion] More detail
> > > > >
> > > > > By default, sign-in sends the URL that this server publishes as the OAuth `resource` parameter, which ties the token to this server. Microsoft Entra ID rejects it with `AADSTS9010010` when the URL is not an Application ID URI in your tenant.
> > > > >
> > > > > * **Requires:** `clientId`, a `scope` with an API scope, and exactly one of `tenantId`, a single `authorizationServer`, or `authorizationUrl` with `tokenUrl`. Otherwise the entry is not loaded.
> > > > > * **Risk:** `scope` alone now says which API the token is for, so check that it names this server's app. A scope for another app is accepted, and this server then receives a token meant for that app.
> > > > > * **Entra ID:** write the scope in full, as in `api://<app-id>/<scope>`.
> > > >
> > > > **oauth.callbackHost** `enum`
> > > >
> > > > Use localhost only if your IdP’s registered redirect URI specifies it.
> > > >
> > > > One of: `127.0.0.1`, `localhost`
> > > >
> > > > **oauth.callbackPort** `integer`
> > > >
> > > > Only set if your IdP requires an exact-match redirect port. Entra accepts any.
> > > >
> > > > **oauth.additionalRedirectReferrerHosts** `string`
> > > >
> > > > Space-separated hostnames also accepted as the referrer of the sign-in callback, besides the authorization URL’s host.
> > > >
> > > > > [accordion] More detail
> > > > >
> > > > > If a callback is rejected for a referrer mismatch, the app log names the rejected host. Add that hostname here.
> > >
> > > > [tab] hosted
> > > >
> > > > Applies when `oauth.mode` is `hosted`. The in-app configuration window calls it **Anthropic-hosted client identity (requires Claude.ai sign-in)**.
> > > >
> > > > Always write `"mode": "hosted"`. Without it the object is read as Bring your own client, which needs `clientId` beside `authorizationServer`, so the app drops the entry.
> > > >
> > > > **oauth.clientId** `string`
> > > >
> > > > Filled in by Claude.ai: the URL of Anthropic’s hosted client-metadata document. Do not set it.
> > > >
> > > > **oauth.authorizationServer** `string[]` *required*
> > > >
> > > > The exact issuer string(s) that the server’s authorization server advertises, as a JSON array. Anthropic signs the identity only for these.
> > > >
> > > > **oauth.scope** `string`
> > > >
> > > > Space-separated scopes to request. Unset: the scopes the server advertises. Required if Tenant ID is set or the resource parameter omitted.
> >
> > **headers** `object: name → value`
> >
> > Static headers sent on every request: routing and tenant headers only. No credentials here: use the headers helper script for those.
> >
> > **headersHelper** `string`
> >
> > Consent required (A value that a bootstrap server or a self-hosted session host delivers applies only after the user approves it, unless machine-scoped device management set that server's address. For a bootstrap server, the trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)
> >
> > Absolute path to an executable that prints a JSON object of HTTP headers on stdout. Merged over static headers; the helper wins on conflict.
> >
> > > [accordion] More detail
> > >
> > > The helper script normally runs with `CLAUDE_CODE_MCP_SERVER_NAME` set to this entry's `name`, so one script can serve several servers. Put the variable in double quotes, compare it with the names you expect, and do not pass it to another command.
> >
> > **headersHelperArgs** `string[]`
> >
> > Consent required (A value that a bootstrap server or a self-hosted session host delivers applies only after the user approves it, unless machine-scoped device management set that server's address. For a bootstrap server, the trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)
> >
> > Arguments passed to the headers helper script, one per entry, in order. Leave unset to run it with none.
> >
> > > [accordion] More detail
> > >
> > > * On every platform, an argument cannot be empty or contain a double quote, a percent sign or a control character.
> > > * Do not put secrets in arguments. They are visible in the app log and to other processes on the device.
> > > * Have the script fail when a needed argument is missing. An app version that does not know this setting passes none.
> >
> > **headersHelperTtlSec** `integer`
> >
> > How long the helper’s headers are reused before it runs again, in seconds. Defaults to 300.
> >
> > **headersHelperRefreshBufferSec** `integer`
> >
> > Seconds before the TTL expires at which the helper re-runs mid-session. Defaults to 60. Keep it larger than the helper’s typical runtime.
> >
> > **platformOverrides** `object`
> >
> > On that operating system, each setting here replaces the entry’s own. A setting left out keeps the entry’s.
> >
> > > [accordion] More detail
> > >
> > > A value written here replaces the entry's value whole: lists and maps are not merged.
> > >
> > > * A local (`stdio`) entry can repeat `command`, `args`, `env`, `envHelper` and `envHelperArgs`. It always needs its own `command` too.
> > > * A remote or web search entry can repeat `headersHelper` and `headersHelperArgs`. If it gives `headersHelper` here, it needs its own too.
> > > * A mistake under any operating system drops the server on all of them.
> > > * An older version ignores this setting and runs the entry's own values. Until all devices are updated, put the Windows values in the entry itself.
> >
> > > [accordion] Child attributes (3)
> > >
> > > **platformOverrides.win32** `object: name → value`
> > >
> > > On Windows, these replace the entry’s own settings. A setting left out keeps the entry’s.
> > >
> > > **platformOverrides.darwin** `object: name → value`
> > >
> > > On macOS, these replace the entry’s own settings. A setting left out keeps the entry’s.
> > >
> > > **platformOverrides.linux** `object: name → value`
> > >
> > > On Linux, these replace the entry’s own settings. A setting left out keeps the entry’s.
> >
> > **toolTimeoutSec** `integer`
> >
> > Maximum time in seconds that Claude waits for one tool call to this server. Leave empty to use the MCP tool call timeout.
> >
> > > [accordion] More detail
> > >
> > > For Claude's calls to this server it takes the place of `mcpToolTimeoutSec`. Use a whole number from 5 to 3600: any other value is ignored.
> > >
> > > * Progress messages from the server do not extend the limit.
> > > * Time that a user spends on a sign-in or consent step during the call counts toward the limit. On a server that asks for sign-in, set a generous value.
> >
> > **icon** `string`
> >
> > Icon shown for this connector: a PNG or JPEG image as a base64 data: URI, at most 4,096 characters.
> >
> > > [accordion] More detail
> > >
> > > A PNG of 48 by 48 pixels or smaller works well. Keep icons small: Windows Group Policy holds the whole `managedMcpServers` list in one value of at most 65,535 characters.
> >
> > **defaultState** `enum`
> >
> > Whether this connector starts on or off for each person.
> >
> > One of: `on`, `off`
> >
> > > [accordion] More detail
> > >
> > > Unset means `on`.
> > >
> > > * This is a starting point, not a restriction: each user can turn the connector on. To withhold a connector, remove it or block its tools with `toolPolicy`.
> > > * Adding `off` to a connector already in use turns it off for all users who have not switched it on themselves, scheduled tasks included.
> > > * This setting does not apply to a plugin's server that matches this entry.
>
> > [tab] stdio
> >
> > Applies when `transport` is `stdio`. The in-app configuration window calls it **Local command (stdio)**.
> >
> > **transport** `string` *required*
> >
> > How the app connects: HTTP, legacy SSE or a local command (stdio). policy-only connects to nothing: it sets a plugin server’s tool policy.
> >
> > Must be: `stdio`
> >
> > **command** `string` *required*
> >
> > Consent required (A value that a bootstrap server or a self-hosted session host delivers applies only after the user approves it, unless machine-scoped device management set that server's address. For a bootstrap server, the trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)
> >
> > Absolute path to the server executable, run on the user’s machine.
> >
> > **args** `string[]`
> >
> > Consent required (A value that a bootstrap server or a self-hosted session host delivers applies only after the user approves it, unless machine-scoped device management set that server's address. For a bootstrap server, the trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)
> >
> > Arguments passed to the command, one per entry.
> >
> > **env** `object: name → value`
> >
> > Consent required (A value that a bootstrap server or a self-hosted session host delivers applies only after the user approves it, unless machine-scoped device management set that server's address. For a bootstrap server, the trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)
> >
> > Environment variables set for the command.
> >
> > **envHelper** `string`
> >
> > Consent required (A value that a bootstrap server or a self-hosted session host delivers applies only after the user approves it, unless machine-scoped device management set that server's address. For a bootstrap server, the trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)
> >
> > Script that prints environment variables as a JSON object to stdout. Runs when the local server starts (cached for the TTL below).
> >
> > > [accordion] More detail
> > >
> > > * Its values take priority over `env`.
> > > * If the script fails, the server does not start.
> > > * A script with nothing to set must print `{}`. Empty output counts as a failure.
> > > * The helper script normally runs with `CLAUDE_CODE_MCP_SERVER_NAME` set to this entry's `name`, so one script can serve several servers. Put the variable in double quotes, compare it with the names you expect, and do not pass it to another command.
> >
> > **envHelperArgs** `string[]`
> >
> > Consent required (A value that a bootstrap server or a self-hosted session host delivers applies only after the user approves it, unless machine-scoped device management set that server's address. For a bootstrap server, the trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)
> >
> > Arguments passed to the environment helper script, one per entry, in order. Leave unset to run it with none.
> >
> > > [accordion] More detail
> > >
> > > * On every platform, an argument cannot be empty or contain a double quote, a percent sign or a control character.
> > > * Do not put secrets in arguments. They are visible in the app log and to other processes on the device.
> > > * Have the script fail when a needed argument is missing. An app version that does not know this setting passes none.
> >
> > **envHelperTtlSec** `integer` (default: 300)
> >
> > Maximum age of a cached helper result, in seconds (default 300). Applies when the server starts or restarts.
> >
> > > [accordion] More detail
> > >
> > > Set this at or below your token lifetime. Otherwise a server that crashes because its token expired can restart with the same cached values until this time is up.
> >
> > **startupTimeoutSec** `integer` (default: 120)
> >
> > Maximum wait in seconds for the server to start and list its tools.
> >
> > **platformOverrides** `object`
> >
> > On that operating system, each setting here replaces the entry’s own. A setting left out keeps the entry’s.
> >
> > > [accordion] More detail
> > >
> > > A value written here replaces the entry's value whole: lists and maps are not merged.
> > >
> > > * A local (`stdio`) entry can repeat `command`, `args`, `env`, `envHelper` and `envHelperArgs`. It always needs its own `command` too.
> > > * A remote or web search entry can repeat `headersHelper` and `headersHelperArgs`. If it gives `headersHelper` here, it needs its own too.
> > > * A mistake under any operating system drops the server on all of them.
> > > * An older version ignores this setting and runs the entry's own values. Until all devices are updated, put the Windows values in the entry itself.
> >
> > > [accordion] Child attributes (3)
> > >
> > > **platformOverrides.win32** `object: name → value`
> > >
> > > On Windows, these replace the entry’s own settings. A setting left out keeps the entry’s.
> > >
> > > **platformOverrides.darwin** `object: name → value`
> > >
> > > On macOS, these replace the entry’s own settings. A setting left out keeps the entry’s.
> > >
> > > **platformOverrides.linux** `object: name → value`
> > >
> > > On Linux, these replace the entry’s own settings. A setting left out keeps the entry’s.
> >
> > **toolTimeoutSec** `integer`
> >
> > Maximum time in seconds that Claude waits for one tool call to this server. Leave empty to use the MCP tool call timeout.
> >
> > > [accordion] More detail
> > >
> > > For Claude's calls to this server it takes the place of `mcpToolTimeoutSec`. Use a whole number from 5 to 3600: any other value is ignored.
> > >
> > > * Progress messages from the server do not extend the limit.
> > > * Time that a user spends on a sign-in or consent step during the call counts toward the limit. On a server that asks for sign-in, set a generous value.
> >
> > **icon** `string`
> >
> > Icon shown for this connector: a PNG or JPEG image as a base64 data: URI, at most 4,096 characters.
> >
> > > [accordion] More detail
> > >
> > > A PNG of 48 by 48 pixels or smaller works well. Keep icons small: Windows Group Policy holds the whole `managedMcpServers` list in one value of at most 65,535 characters.
>
> > [tab] policy-only
> >
> > Applies when `transport` is `policy-only`. The in-app configuration window calls it **Tool permissions only (plugin server)**.
> >
> > **transport** `string` *required*
> >
> > How the app connects: HTTP, legacy SSE or a local command (stdio). policy-only connects to nothing: it sets a plugin server’s tool policy.
> >
> > Must be: `policy-only`
> >
> > > [accordion] More detail
> > >
> > > For a `policy-only` entry:
> > >
> > > * Set `name` to the server's name as the plugin declares it (letter case is ignored), and `toolPolicy` to the permissions. A name that matches no installed plugin server does nothing.
> > > * It takes priority over `orgPluginSettings` for that server. With no `toolPolicy`, the server is left unrestricted.
> > > * An older version drops the entry and applies `orgPluginSettings` instead. Until all devices are updated, keep the same permissions there, and do not deploy a list made only of `policy-only` entries.

***

#### `mcpPersistentAlwaysAllowEnabled`

booleanDefault: trueSince 1.24012.9

**Allow persistent tool approvals.** Offer the persistent “Always allow” approval options for MCP tools. Disable to keep tool approvals per-call or session-scoped only.

> [accordion] More detail
>
> When off, persistent approvals that users saved earlier in Chat and Cowork stop applying. Scheduled tasks also stop offering and reusing them, unless `mcpScheduledTaskApprovalLifetimeDays` is 1 or more.
>
> In Code, any allow rule in a user's or a project's Claude Code settings keeps allowing a tool until it is removed. So do hooks in its settings or plugins.

***

#### `mcpScheduledTaskApprovalLifetimeDays`

integerRange: 0–3,650Since 2.7032.0

**Scheduled-task tool approval lifetime.** Days a scheduled task can reuse a persistent MCP tool approval before it asks again. 0 turns reuse off. Unset: no limit.

> [accordion] More detail
>
> * If `mcpPersistentAlwaysAllowEnabled` is off, a limit of 1 or more brings the persistent option back for scheduled tasks only.
> * In Code, any allow rule in a user's or a project's Claude Code settings keeps allowing the tool, even at `0`, until it is removed. Earlier approvals were usually saved as such rules.
> * If the bootstrap server sets this key, scheduled tasks ask again after each app start until the app has fetched the configuration.

***

#### `isLocalDevMcpEnabled`

booleanDefault: trueSince 1.2581.0

**Allow local MCP servers.** Lets users run local (stdio) MCP servers added in Developer settings. On third-party deployments, off also stops plugins’ local servers.

> [accordion] More detail
>
> On third-party deployments, `false` covers `.mcpb` bundles and plugins from every marketplace, your organization's included. Plugins in the org-plugins directory on the device are not affected. In Code, it also stops the local servers that a user or a project configures for Claude Code.
>
> When `false` comes from an MDM profile, the app starts only the local `managedMcpServers` entries in that same profile, exactly as written there. A `false` from any other source does not do this.
>
> Claude Code's own managed settings, where a session has any, take priority by default.

***

#### `allowedPluginMcpServers`

object\[]Since 2.2553.0

**Allowed plugin MCP servers.** Remote MCP servers that user-installed and marketplace plugins can connect, as URL patterns. Empty list: none. Unset: no limit.

> [accordion] More detail
>
> * **Entries:** `{"serverUrl": "https://*.example.com/*"}`. No other entry form is read.
> * **Once set:** no entry allows a plugin's local (`stdio`) server, and servers that a user or a project configures for Claude Code are not connected.
> * **`policy-only`:** a `managedMcpServers` entry with that `transport` does not allow its server. List the server's own URL here too.
>
> Claude Code's own managed settings, where a session has any, take priority by default.

> [accordion] Child attributes (1)
>
> **serverUrl** `string` *required*
>
> URL pattern a plugin’s remote server must match, with \* wildcards.

***

#### `deniedPluginMcpServers`

object\[]Since 2.16120.0

**Blocked plugin MCP servers.** URL patterns of remote MCP servers that plugins cannot connect, even if the Allowed plugin MCP servers list allows them.

> [accordion] More detail
>
> An entry matches an address, not a server. The same server under another host name or IP address, or behind a plugin's local server, is not matched. To keep a plugin's servers out whatever address they use, set `allowedPluginMcpServers`.
>
> * **Entries:** `{"serverUrl": "https://*.example.com/*"}`. This example does not match `http://`, `wss://` or `example.com` itself. A pattern with no scheme matches nothing.
> * **Not affected:** `managedMcpServers` and servers from the org-plugins directory on the device.
> * **Any other form**, such as `serverName`, is reported and blocks every plugin's remote server.
>
> Claude Code's own managed settings, where a session has any, take priority by default.

> [accordion] Child attributes (1)
>
> **serverUrl** `string` *required*
>
> URL pattern of the remote servers to block, with \* wildcards.

***

#### `mcpToolTimeoutSec`

integerRange: 60–3,600Since 1.37937.0

**MCP tool call timeout.** Per-call timeout for MCP tool calls, in seconds. Unset: 180 in Chat and Cowork.

> [accordion] More detail
>
> * **Unset:** Chat and Cowork use 180 seconds, and the app sets no timeout in Code. Calls to user-added local servers are also limited to 60 seconds.
> * **Set:** the value applies in Code too.
> * **One server:** `toolTimeoutSec` on its `managedMcpServers` entry replaces this value for that server.
> * **Cowork's shell tool:** a single command's timeout cannot exceed this value, or 600 seconds if that is lower.

***

### Authentication

#### `microsoftAuthBroker`

enumDefault: autoSince 1.19367.0

**Microsoft 365 native sign-in broker.** How Microsoft 365 signs in. “auto”: OS identity broker, else browser. “disabled”: browser only. “required”: fails without the broker.

One of: `auto` (default), `disabled`, `required`

> [accordion] More detail
>
> The OS identity broker is Web Account Manager on Windows and the Company Portal SSO extension on macOS. Linux has no broker, so `required` is not supported there.
>
> With `required` the refresh token stays held by the broker.
>
> Update all devices first: an older version treats `required` as `disabled`, so it signs in through the browser.

***

#### `microsoftAuthDefaultAccount`

enumDefault: disabledSince 2.26454.0

**Microsoft 365 sign-in with the Windows account.** “enabled”: on Windows, connecting Microsoft 365 uses the work account already signed in to Windows. “disabled”: account picker.

One of: `enabled`, `disabled` (default)

> [accordion] More detail
>
> It needs both of these:
>
> * `microsoftAuthBroker` is not `disabled`.
> * The `tenantId` of the `microsoft365` entry in `managedMcpServers` is a tenant GUID, not `common`, `organizations` or `consumers`.
>
> Users still get the account picker in some cases, such as a failed silent sign-in or a guest or personal account. They also get it once they have disconnected Microsoft 365 on the device.
>
> Turning this off signs nobody out.

***

### Extensions

#### `isDesktopExtensionEnabled`

booleanDefault: falseSince 1.2581.0

**Allow desktop extensions.** Let Claude Desktop load desktop extensions (.dxt and .mcpb files). Unset: on where users sign in with Claude.ai.

> [accordion] More detail
>
> In a third-party deployment, turning this on loads extensions that are already installed. Users cannot install new ones.

***

#### `isDesktopExtensionSignatureRequired`

booleanDefault: falseSince 1.2581.0

**Require signed extensions.** Reject desktop extensions that are not signed by a trusted publisher.

***

## Telemetry & updates

### `deploymentOrganizationUuid`

stringSince 1.2581.0

**Organization UUID.** A UUID you generate. Tags telemetry so Anthropic support can find your events, and users’ local data is stored under it. Not used for auth.

[Admin Console](#the-works-with-column): Set automatically.

> [accordion] More detail
>
> If unset, the app uses the organization of your Anthropic sign-in, where the connection has one. Otherwise, local data is stored under a placeholder UUID shared with other unconfigured deployments. Telemetry is then tagged with a value the app derives from your connection settings, or with that placeholder.
>
> **Changing this value leaves data behind.** Sessions, skills and plugins stored under the previous value do not move to the new one.

***

### `disableEssentialTelemetry`

booleanDefault: falseSince 1.2581.0

**Block essential telemetry.** Crash and performance reports to Anthropic.

[Guide for this setting](https://claude.com/docs/third-party/claude-desktop/telemetry.md#essential-telemetry)

> [accordion] More detail
>
> Reports include **crash stacks**, **startup failure reasons**, **version/OS metadata**, and **crash dumps** (each an unfiltered copy of part of the app's memory). They carry a random install ID and an organization ID, which the app picks if you set none (see `deploymentOrganizationUuid`).
>
> Reports can also include:
>
> * a summary of your settings
> * the host names of addresses you configured
> * text you set for display
> * a one-way digest of a session ID
>
> Leave this off unless your policy requires zero outbound telemetry.

***

### `disableNonessentialTelemetry`

booleanDefault: falseSince 1.2581.0

**Block nonessential telemetry.** Product-usage analytics (no message content) and diagnostic-report uploads.

[Guide for this setting](https://claude.com/docs/third-party/claude-desktop/telemetry.md#non-essential-telemetry)

> [accordion] More detail
>
> Applies only while the app runs in third-party mode. If users could otherwise sign in to Claude.ai on the device, also set `disableDeploymentModeChooser` so the app stays in third-party mode.

***

### `disableNonessentialServices`

booleanDefault: falseSince 1.2581.0

**Block nonessential services.** Connector icons, hosted artifact previews, MCP Apps widgets and the Linux spellcheck dictionary. Widgets fall back to text.

> [accordion] More detail
>
> With this on:
>
> * Artifacts still render locally.
> * Excel files in the Code tab preview only through Claude’s workspace (the local VM).
> * Spellcheck underlines are off on Linux.
>
> Windows still downloads a dictionary for a language it cannot check natively. This key does not stop that download.

***

### OTLP

#### `otlpEndpoint`

stringSince 1.2581.0

**OTLP endpoint.** Where OpenTelemetry logs and metrics are sent. Leave blank to disable.

***

#### `otlpProtocol`

enumDefault: http/protobufSince 1.2581.0

**OTLP protocol.** Transport protocol for the OpenTelemetry exporters.

One of: `http/protobuf` (default), `http/json`, `grpc`

> [accordion] More detail
>
> With `grpc`, some exports still go over HTTP to the same endpoint, such as the app's own events.
>
> Choose `grpc` only if your collector also accepts OTLP/HTTP at that address. Otherwise keep `http/protobuf` and point `otlpEndpoint` at the collector's OTLP/HTTP receiver, usually port 4318.

***

#### `otlpHeaders`

object: name → valueSince 1.2581.0

**OTLP headers.** Static headers for routing and tenants only. No credentials here: use Collector authentication or the OTLP headers helper script.

***

#### `otlpAuthMode`

enumSince 1.30096.1

**Collector authentication.** inference-credential sends a user’s bearer-token inference credential to the collector. Use it only for a collector you operate.

One of: `none`, `inference-credential`

> [accordion] More detail
>
> The credential can also make model requests as the user. For a collector you do not operate, use `otlpHeadersHelper` with a credential that can only send telemetry.
>
> The collector must accept the credential as issued. Some credentials are never sent, such as an AWS profile, a Google credentials file or a Claude Console sign-in. Telemetry then exports without the header, so use `otlpHeadersHelper` instead.

***

#### `otlpHeadersHelper`

string

Consent required (A value that a bootstrap server or a self-hosted session host delivers applies only after the user approves it, unless machine-scoped device management set that server's address. For a bootstrap server, the trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)

Since 1.30096.1

**OTLP headers helper script.** Full path to a helper script that prints collector headers as JSON. They take priority over OTLP headers and Collector authentication.

> [accordion] More detail
>
> The app runs it with no arguments. Sample output: `{"Authorization": "Bearer …"}`.
>
> Cowork and Code sessions that stay open run it again as tokens rotate. On Windows use an `.exe`, `.cmd` or `.bat` file for that: a `.ps1` file applies at session start only.
>
> If it fails, telemetry is sent without its headers.

***

#### `otlpResourceAttributes`

object: name → valueSince 1.5354.0

**Resource attributes.** Extra attributes to attach to every span, metric and log. An enduser.id set here takes priority over the signed-in user’s identity.

> [accordion] More detail
>
> `process.owner` (the OS login name) is always sent to your collector. Set it here to replace the value.

***

#### `otlpDesktopLogLevel`

enumDefault: errorSince 1.9255.0

**Desktop telemetry export level.** Lowest level of the Claude Desktop application’s own events to export, separate from Cowork and Code sessions. Unset: error.

One of: `off`, `error` (default), `warn`, `info`, `debug`

***

#### `otlpContentCapture`

enum\[]Since 1.15962.0

**Content capture.** Content categories Claude Desktop sends unredacted to your collector. `userPrompts` also sends Claude’s responses.

Any of: `userPrompts`, `assistantResponses`, `toolDetails`, `toolContent`, `rawApiBodies`

> [accordion] More detail
>
> This data never reaches Anthropic.
>
> * `userPrompts`: what users type, and Claude's responses
> * `assistantResponses`: Claude's responses
> * `toolDetails`: tool inputs, such as a web search query
> * `toolContent`: tool outputs, such as fetched page text or command output
> * `rawApiBodies`: model request and response bodies
>
> To send prompts without responses, leave out `rawApiBodies`. Then set `OTEL_LOG_ASSISTANT_RESPONSES` to `0` in the `env` block of the highest-priority Claude Code managed settings, not a per-user Windows registry policy. Update all devices first: an older version still sends responses.
>
> Without `parentSettingsBehavior` set to `"merge"` in [those settings](https://claude.com/docs/third-party/claude-desktop/code.md#interaction-with-claude-code%E2%80%99s-own-managed-settings), Claude Code can drop the restrictions that Claude Desktop passes to it.

***

#### `otlpTracesEnabled`

booleanSince 1.22209.0

**Export traces.** Also export OpenTelemetry traces from Cowork tasks and Code sessions. Uses Claude Code’s session tracing.

> [accordion] More detail
>
> Has no effect without `otlpEndpoint`. With it set, this key alone decides whether Cowork tasks and Code sessions export traces. Unset or `false` keeps traces off even if a user's or a project's Claude Code settings, or managed settings, turn tracing on.

***

#### `otlpAttrMaxChars`

integerRange: 256–15,000,000Since 2.31226.0

**Telemetry attribute length limit.** Maximum length, in characters, of captured content such as a raw API body. Unset: 61,440 in Cowork tasks and Code sessions.

> [accordion] More detail
>
> In Cowork tasks and Code sessions it applies to model responses, tool content and raw API bodies, not to user prompts.
>
> A cut request body loses its newest messages. To capture whole bodies with `rawApiBodies`, set this just above your longest body, not at the maximum.
>
> Keep your collector's request size limit at a few times your longest body. A collector refuses an export over its limit, and every event in that export is lost.
>
> The Claude add-in for Microsoft 365 uses 4,000 when unset, and counts values above 32,000 as 32,000.

***

### Auto update

#### `disableAutoUpdates`

booleanDefault: falseSince 1.2581.0

**Block auto-updates.** Stop Claude Desktop from fetching updates entirely (no time limit). You’ll need to push new versions yourself.

> [accordion] More detail
>
> When you install a newer version while Claude is open, the app shows a restart notice in the sidebar. To have Claude restart by itself if nobody restarts it, use `installedUpdateEnforcementEnabled`.
>
> On Windows the notice covers installs from the MSIX package, not the Microsoft Store version or the .exe installer. The switch to the newer version may end the Cowork tasks of other users signed in on that device.
>
> This is an app-behavior key, like `releaseChannel`. If your MDM profile holds nothing but such keys, the app reads them all from that profile alone, so put every one you use there.

***

#### `installedUpdateEnforcementEnabled`

booleanSince 3.6556.1

**Restart to apply installed updates.** With auto-updates blocked, Claude restarts by itself for a newer version installed while it was open. On Windows it may stay closed.

> [accordion] More detail
>
> `installedUpdateEnforcementHours` sets how long the app waits.
>
> * **Unset:** off in third-party deployments. Where users sign in with Claude.ai it follows Anthropic's rollout, and `false` keeps it off.
> * **Windows:** if Windows does not reopen Claude, scheduled tasks and background work stop until a user opens it. The restart may also end the Cowork tasks of other users signed in on that device.
>
> This is an app-behavior key, like `disableAutoUpdates`. If your MDM profile holds nothing but such keys, the app reads them all from that profile alone, so put every one you use there.

***

#### `installedUpdateEnforcementHours`

integerRange: 1–72Since 3.6556.1

**Installed-update enforcement window.** Hours before Claude restarts for a newer version installed while it was open. Unset: 72 hours, then when idle. A number skips the idle wait.

> [accordion] More detail
>
> Applies only while `disableAutoUpdates` is on and the restart is on (see `installedUpdateEnforcementEnabled`).
>
> * Only time with the app open and the device awake counts toward the hours.
> * Idle means 10 minutes without input. Where the system reports no idle time, as some Wayland sessions do, an unset key never restarts: set a number.
> * The restart waits while Claude is mid-task on the device.
>
> This is an app-behavior key, like `disableAutoUpdates`. If your MDM profile holds nothing but such keys, the app reads them all from that profile alone, so put every one you use there.

***

#### `autoUpdaterEnforcementHours`

integerRange: 1–72Since 1.2581.0

**Auto-update enforcement window.** Hours before a downloaded update force-installs. Only applies when auto-updates are enabled. Blank = 72-hour default.

> [accordion] More detail
>
> * **Unset:** after 72 hours the app restarts once the device has been idle for 10 minutes.
> * **Any number, even 72:** the app restarts when the time is up, whether or not the user is active.
>
> In both cases the restart waits while Claude is mid-task on the device.
>
> This is an app-behavior key, like `disableAutoUpdates`. If your MDM profile holds nothing but such keys, the app reads them all from that profile alone, so put every one you use there.

***

#### `updateViaUpdatesHost`

booleanDefault: falseSince 1.26832.0

**Check for updates on releases.claude.com.** Read the update feed from releases.claude.com so api.anthropic.com can stay blocked.

> [accordion] More detail
>
> The installer still downloads from `downloads.claude.ai`, so keep that host open.
>
> If an MDM profile sets `bootstrapUrl` to a `config.claude.com` URL and leaves `bootstrapEnabled` on, the app reads the feed from `releases.claude.com` whatever this key says. Turn this key on anyway: an older version reads it from there only when this key is on.
>
> This is an app-behavior key, like `disableAutoUpdates`. If your MDM profile holds nothing but such keys, the app reads them all from that profile alone, so put every one you use there.

***

#### `releaseChannel`

enumDefault: stableSince 3.1623.0

**Release channel.** On Stable, devices take each release as it rolls out. On Staggered, they update less often, usually a week or more behind. Unset: Stable.

One of: `stable` (default), `staggered`

> [accordion] More detail
>
> `staggered` usually updates on Thursdays and is typically 7 to 14 days behind `stable`.
>
> * Devices on `staggered` get features and fixes, security fixes included, later than devices on `stable`.
> * Write the value in lowercase. A value that cannot be read, such as `Stable`, is read as `staggered`.
> * Users who sign in to Claude.ai follow `stable`, unless their organization manages Claude Desktop from the Admin Console.
> * No effect on Linux or Microsoft Store installs.
>
> This is an app-behavior key, like `disableAutoUpdates`. If your MDM profile holds nothing but such keys, the app reads them all from that profile alone, so put every one you use there.

***

### Configuration updates

#### `relaunchEnforcementHours`

integerDefault: 24Range: 0–336Since 1.40609.0

**Configuration relaunch window.** Hours users can keep working after a configuration change that needs a restart. 0: restart required at once. Unset: 24 hours.

> [accordion] More detail
>
> When the time is up, a restart dialog blocks the app. The app then restarts by itself after 2 minutes with no activity and no running task.
>
> When an MDM profile that sets more than app-behavior keys first reaches a running app, the restart dialog can show with no countdown.
>
> This is an app-behavior key, like `disableAutoUpdates`. If your MDM profile holds nothing but such keys, the app reads them all from that profile alone, so put every one you use there.

***

#### `configRecheckIntervalMinutes`

integerDefault: 10Range: 2–30Since 1.46388.1

**Configuration re-check interval.** Minutes between the running app’s checks for a changed managed configuration. Blank = 10 minutes.

> [accordion] More detail
>
> A change that needs a restart starts the `relaunchEnforcementHours` countdown.
>
> This is an app-behavior key, like `disableAutoUpdates`. If your MDM profile holds nothing but such keys, the app reads them all from that profile alone, so put every one you use there.

***

#### `disableLocalConfigCache`

booleanDefault: false

Admin Console only (Only the Enterprise Admin Console can set the key. Claude Desktop ignores it in an MDM profile, in the local configuration file and in a bootstrap server's response.)

Since 2.7032.0

**Keep only your organization ID and restrictions on disk.** Between launches, keep on disk only your organization ID and restrictions, not its name or anything you have allowed.

> [accordion] More detail
>
> While this is on, the app's crash reporting does not start on these devices. Error stack traces and performance timings still leave these devices unless `disableEssentialTelemetry` is on.
>
> An earlier copy is cut down at the next launch that reaches the Admin Console.
>
> Only the Admin Console can set this key. A value from an MDM profile or a bootstrap server is ignored.

***

## Limits

### Session retention

#### `chatSessionRetentionDays`

integerRange: 1–3,650Since 1.52386.0

**Chat retention period.** Delete chats, with their files, after this many days without activity. Unset: no deletion. Projects and memory stay.

> [accordion] More detail
>
> Applies only while the app runs in third-party mode. Deletion can start shortly after the app gets this configuration. Pinned sessions are not exempt. Opening an old chat or Cowork task without continuing it does not reliably keep it.
>
> It does not delete, for example:
>
> * a session while it is running or open on screen
> * another account's sessions, until that account signs in
> * Code sessions on an SSH host or in WSL
> * Cowork background tasks that the sidebar does not list
> * Claude Code's prompt history, plans and shell snapshots, which keep its own retention
>
> A value that cannot be read as a whole number of days deletes nothing.

***

#### `coworkSessionRetentionDays`

integerRange: 1–3,650Since 1.52386.0

**Cowork retention period.** Delete Cowork tasks, with their uploads and outputs, after this many days without activity. Unset: no deletion. Spaces and memory stay.

> [accordion] More detail
>
> Applies only while the app runs in third-party mode. Deletion can start shortly after the app gets this configuration. Pinned sessions are not exempt. Opening an old chat or Cowork task without continuing it does not reliably keep it.
>
> It does not delete, for example:
>
> * a session while it is running or open on screen
> * another account's sessions, until that account signs in
> * Code sessions on an SSH host or in WSL
> * Cowork background tasks that the sidebar does not list
> * Claude Code's prompt history, plans and shell snapshots, which keep its own retention
>
> A value that cannot be read as a whole number of days deletes nothing.

***

#### `codeSessionRetentionDays`

integerRange: 1–3,650Since 1.52386.0

**Code retention period.** Delete Code sessions, conversation included, after this many days without activity. Unset: no deletion. Uncommitted work stays on disk.

> [accordion] More detail
>
> Applies only while the app runs in third-party mode. Deletion can start shortly after the app gets this configuration. Pinned sessions are not exempt. Opening an old chat or Cowork task without continuing it does not reliably keep it.
>
> It does not delete, for example:
>
> * a session while it is running or open on screen
> * another account's sessions, until that account signs in
> * Code sessions on an SSH host or in WSL
> * Cowork background tasks that the sidebar does not list
> * Claude Code's prompt history, plans and shell snapshots, which keep its own retention
>
> A value that cannot be read as a whole number of days deletes nothing.

***

#### `sessionRetentionHold`

booleanSince 1.52386.0

**Suspend session deletion.** Suspend the chat, Cowork and Code retention periods (legal hold). Claude Code’s own transcript cleanup (cleanupPeriodDays) still runs.

> [accordion] More detail
>
> Meant to be set per user or group.
>
> * Deletion stops at the first configuration fetch that carries the hold, before any restart.
> * A device that cannot reach its bootstrap server deletes nothing.
>
> In MDM, do not deploy the hold in a profile of its own: the app would then ignore the device's local configuration.

***

### Token limits

#### `inferenceMaxTokensPerWindow`

integerRange: 1 or moreSince 1.2581.0

**Max tokens per window.** Caps each user’s input and output tokens per window. Cached tokens do not count, so it does not cap your bill. Unset: no limit.

> [accordion] More detail
>
> Has no effect unless `inferenceTokenWindowHours` is also set. A user with two devices can have a separate count on each.

***

#### `inferenceTokenWindowHours`

integerRange: 1–720Since 1.2581.0

**Token cap window.** Length of each token cap window, in hours. The count resets to zero when a window ends.

> [accordion] More detail
>
> Used with `inferenceMaxTokensPerWindow`. Each user's window starts the first time they use the app after their previous window ends. So 24 hours does not mean midnight to midnight.

***

#### `inferenceTokenWarningPercent`

integerRange: 1–100Since 4.29.0

**Token limit warning.** Warn users once they have used this percent of their token limit. Unset: 75. At 100, the only warning comes at the limit.

> [accordion] More detail
>
> Has no effect unless `inferenceMaxTokensPerWindow` and `inferenceTokenWindowHours` are both set.
>
> Usage is counted each time Claude finishes a reply. One long-running request can reach the limit before the warning appears.

***

## Appearance

### `endUserAttribution`

booleanSince 1.25927.0

**End-user attribution.** Show the signed-in user’s identity in the app, add it to Claude’s system prompt, and send it to your OpenTelemetry collector as enduser.id.

> [accordion] More detail
>
> The identity comes from the user's sign-in, or is the OS login name when sign-in gives none. A static `enduser.id` in `otlpResourceAttributes` takes priority in telemetry, and is sent even when this setting is off.
>
> The `process.owner` attribute (the OS login name) is always sent. To replace it, set a static `process.owner` in `otlpResourceAttributes`.

***

### `deploymentDisplayName`

stringSince 1.24012.0

**Deployment display name.** Overrides the provider label shown in the sidebar footer, user-menu header, and connection-error banner.

[Admin Console](#the-works-with-column): Set automatically.

***

### `deploymentDisplaySubtitle`

stringSince 1.24012.0

**Deployment display subtitle.** Optional detail shown after the deployment display name in the account-menu header.

[Admin Console](#the-works-with-column): Not available.

***

### `disableConfigDeprecationWarnings`

booleanSince 1.40609.0

**Hide configuration deprecation warnings.** Hide the in-app warning that your configuration uses a deprecated field. A final reminder still shows in the 24 hours before the cut-off.

***

### `banner`

objectSince 1.7196.0

**Organization banner.** A persistent banner across the top of the app window after sign-in.

> [accordion] Child attributes (5)
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

### `sessionStatusLine`

object

Consent required (A value that a bootstrap server or a self-hosted session host delivers applies only after the user approves it, unless machine-scoped device management set that server's address. For a bootstrap server, the trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)

Since 4.4212.0

**Status line.** Claude runs this program and shows the first line it prints above the message box in Cowork, Chat and Code. Off unless set.

> [accordion] More detail
>
> * **Runs:** on the user's device, as the signed-in user, when a session opens, a turn ends, the app regains focus or the model changes.
> * **Input:** one JSON line on standard input: `{"session_id": "…", "model": {"id": "…", "display_name": "…"}}`. Fields with no value are left out.
> * **Output:** Claude shows the first non-empty line, up to 200 characters. ANSI codes 31 to 36 and 91 to 96 set the color.
> * **Limits:** 10 seconds and 64 KiB of output. Past either, Claude stops the program.

> [accordion] Child attributes (1)
>
> **command** `string` *required*
>
> Full local path to the program or executable script.
>
> > [accordion] More detail
> >
> > Users must not be able to change the file.
> >
> > * **macOS and Linux:** a program, or an executable script that starts with `#!`. The file and every parent folder must be owned by root and not writable by group or others. It cannot be under `/home`, `/net` or `/Volumes`.
> > * **Windows:** an `.exe`, `.ps1`, `.cmd` or `.bat` file. It must be under a Program Files folder on the Windows drive.
> >
> > Otherwise it does not run, and the log says why.
> >
> > Claude does not check the interpreter on a `#!` line, so keep that out of users' reach too. An interpreter can also load code from the user's folders. Start Python isolated (for example `#!/usr/bin/python3 -I`) or use a compiled program.

***

### Feature discovery

#### `disableFeatureDiscovery`

booleanDefault: falseSince 1.21459.0

**Hide feature announcements.** Hide unprompted feature announcements: the “What’s new” nudge after an update and new-feature tips. Users can still open release notes.

***

## Plugins

### `allowedPluginMarketplaces`

object\[]Since 1.17377.1

**Plugin marketplaces.** Git repositories or hosted marketplace.json files shown as plugin marketplaces in the Directory’s Organization tab.

> [accordion] Child attributes
>
> **expectedName** `string`
>
> Rejects the marketplace if its manifest name differs.
>
> > [accordion] More detail
> >
> > Also use it to move a marketplace. A change to an entry's `url`, `repo` or `path` (not `ref`) counts as removing the marketplace, which uninstalls the plugins that users installed from it.
> >
> > To avoid that, set the new entry's `expectedName` to the old marketplace's manifest name, in the same change that removes the old entry. Match the letter case and leave it set. Plugins that the new marketplace holds under the same names then normally stay installed. [Move a marketplace to a new source](https://claude.com/docs/third-party/claude-desktop/extensions.md#move-a-marketplace-to-a-new-source) lists the exceptions.
>
> **installationPreference** `enum`
>
> Whether users install plugins themselves or get them automatically.
>
> One of: `available`, `auto_install`, `required`
>
> > [accordion] More detail
> >
> > * `available` (default): users install from the Directory's Organization tab.
> > * `auto_install`: installs once per pin. A plugin that a user removes stays removed until the pin changes.
> > * `required`: reinstalls at every sync, so a plugin cannot stay removed.
> >
> > Both automatic values need a pin: a full commit SHA in `ref`, or `manifestSha256` for a `url` source.
>
> **credentialHelper** `string`
>
> Consent required (A value that a bootstrap server or a self-hosted session host delivers applies only after the user approves it, unless machine-scoped device management set that server's address. For a bootstrap server, the trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)
>
> Executable that prints the access token to send.
>
> > [accordion] More detail
> >
> > The helper script prints a token. It is sent as the Git password for user `x-access-token`, which GitHub, GitLab and Azure DevOps accept. For `url` sources it is sent as `Authorization: Bearer`.
> >
> > [Marketplace credentials](https://claude.com/docs/third-party/claude-desktop/extensions.md#marketplace-credentials) lists other forms, for hosts that need a username or for custom HTTP headers.
>
> > [tab] github
> >
> > Applies when `source` is `github`. The in-app configuration window calls it **GitHub**.
> >
> > **source** `string` *required*
> >
> > Where the marketplace comes from: a GitHub repository (set repo), a Git remote (set url) or a hosted marketplace.json file (set url).
> >
> > Must be: `github`
> >
> > **repo** `string` *required*
> >
> > GitHub repository in owner/repo form. Case-insensitive.
> >
> > **ref** `string`
> >
> > Commit SHA, branch, or tag. Leave empty to track the default branch; auto\_install and required need a full 40-character commit SHA.
> >
> > **path** `string`
> >
> > Folder within the repository that contains the marketplace, when it isn’t at the root.
> >
> > **credentialKind** `enum`
> >
> > Sent with a fetch: nothing (unset), the user’s Git credential, a helper script’s output, or the gateway or bootstrap credential (url only).
> >
> > One of: `anonymous`, `userGit`, `credentialHelper`
>
> > [tab] git
> >
> > Applies when `source` is `git`. The in-app configuration window calls it **Git URL**.
> >
> > **source** `string` *required*
> >
> > Where the marketplace comes from: a GitHub repository (set repo), a Git remote (set url) or a hosted marketplace.json file (set url).
> >
> > Must be: `git`
> >
> > **url** `string` *required*
> >
> > HTTPS Git remote of the marketplace repository (git), or direct HTTPS URL of a hosted marketplace.json file (url).
> >
> > > [accordion] More detail
> > >
> > > For a `url` source, `marketplace.json` lists each plugin as an `archive`: a zip `url` plus its `sha256`. [Host the marketplace over HTTPS](https://claude.com/docs/third-party/claude-desktop/extensions.md#host-the-marketplace-over-https-instead-of-git) has an example.
> > >
> > > * Archives must be on the same origin as the manifest. Open that host on your firewall. A credential is sent only to it.
> > > * With `credentialKind` set to `inferenceCredential`, the manifest must be on your gateway's or bootstrap server's origin.
> >
> > **ref** `string`
> >
> > Commit SHA, branch, or tag. Leave empty to track the default branch; auto\_install and required need a full 40-character commit SHA.
> >
> > **path** `string`
> >
> > Folder within the repository that contains the marketplace, when it isn’t at the root.
> >
> > **credentialKind** `enum`
> >
> > Sent with a fetch: nothing (unset), the user’s Git credential, a helper script’s output, or the gateway or bootstrap credential (url only).
> >
> > One of: `anonymous`, `userGit`, `credentialHelper`
>
> > [tab] url
> >
> > Applies when `source` is `url`. The in-app configuration window calls it **Marketplace URL**.
> >
> > **source** `string` *required*
> >
> > Where the marketplace comes from: a GitHub repository (set repo), a Git remote (set url) or a hosted marketplace.json file (set url).
> >
> > Must be: `url`
> >
> > **url** `string` *required*
> >
> > HTTPS Git remote of the marketplace repository (git), or direct HTTPS URL of a hosted marketplace.json file (url).
> >
> > > [accordion] More detail
> > >
> > > For a `url` source, `marketplace.json` lists each plugin as an `archive`: a zip `url` plus its `sha256`. [Host the marketplace over HTTPS](https://claude.com/docs/third-party/claude-desktop/extensions.md#host-the-marketplace-over-https-instead-of-git) has an example.
> > >
> > > * Archives must be on the same origin as the manifest. Open that host on your firewall. A credential is sent only to it.
> > > * With `credentialKind` set to `inferenceCredential`, the manifest must be on your gateway's or bootstrap server's origin.
> >
> > **manifestSha256** `string`
> >
> > SHA-256 of the marketplace.json to accept (url sources). Any other file is refused. Without it, auto\_install and required act as available.
> >
> > **credentialKind** `enum`
> >
> > Sent with a fetch: nothing (unset), the user’s Git credential, a helper script’s output, or the gateway or bootstrap credential (url only).
> >
> > One of: `anonymous`, `userGit`, `credentialHelper`, `inferenceCredential`

***

### `orgPluginSettings`

object\[]Since 1.8089.0

**Organization plugin settings.** Locks tool permissions on the MCP servers that plugins provide.

> [accordion] More detail
>
> * If a `managedMcpServers` entry is for the same server (same URL, otherwise same name), the entry here is ignored. Put the locks in that entry's `toolPolicy`.
> * Update all devices first: an older version ignores this list and enforces no locks.
> * Claude Code's own managed settings, where a session has any, take priority by default.

> [accordion] Child attributes (2)
>
> **serverName** `string` *required*
>
> Name of the plugin-delivered MCP server this policy applies to.
>
> **tools** `object[]`
>
> Per-tool approval locks for this server.
>
> > [accordion] Child attributes (2)
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

**Use bootstrap config.** Fetch and apply settings from the bootstrap config URL at launch. Turn off to keep the URL saved but skip the fetch.

[Admin Console](#the-works-with-column): Not available.

***

#### `bootstrapUrl`

string

MDM only (You can set the key only in an MDM profile or the local configuration file. Claude Desktop ignores it in a bootstrap server's response.)

Since 1.10628.0

**Bootstrap config URL.** HTTPS endpoint that returns a per-user JSON config overlay. Values from the response override local settings and become read-only.

[Admin Console](#the-works-with-column): Not available.

***

#### `bootstrapOidc`

object

MDM only (You can set the key only in an MDM profile or the local configuration file. Claude Desktop ignores it in a bootstrap server's response.)

Since 1.10628.0

**Bootstrap OIDC parameters.** Your organization’s OpenID Connect identity provider. The user’s token from a browser sign-in is sent as Bearer to the bootstrap server.

[Guide for this setting](https://claude.com/docs/third-party/claude-desktop/bootstrap.md)

[Admin Console](#the-works-with-column): Not available.

> [accordion] More detail
>
> When unset, the bootstrap sign-in uses a device code on the bootstrap server's own origin.
>
> In an MDM profile, write this key as one JSON string. Separate values such as `bootstrapOidc.clientId` do not work: the app silently uses the device-code sign-in instead.

> [accordion] Child attributes (8)
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
> Space-separated hostnames also accepted as the referrer of the sign-in callback, besides the authorization URL’s host.
>
> > [accordion] More detail
> >
> > If a callback is rejected for a referrer mismatch, the app log names the rejected host. Add that hostname here.

***

#### `bootstrapHeaders`

object: name → value

MDM only (You can set the key only in an MDM profile or the local configuration file. Claude Desktop ignores it in a bootstrap server's response.)

Since 1.32885.1

**Bootstrap request headers.** HTTP headers sent on every bootstrap config fetch. Use this instead of embedding user:pass@ in the URL.

[Guide for this setting](https://claude.com/docs/third-party/claude-desktop/bootstrap.md)

[Admin Console](#the-works-with-column): Not available.

> [accordion] More detail
>
> If `bootstrapOidc` is unset, the app treats these headers as sufficient authentication and requires no per-user sign-in for the bootstrap fetch.
>
> These headers, and those of `bootstrapHeadersHelper`, also go to a plugin marketplace on this server's own origin, if its `allowedPluginMarketplaces` entry sets `credentialKind: "inferenceCredential"`.
>
> Header values are masked in diagnostics and telemetry.

***

#### `bootstrapHeadersHelper`

string

MDM only (You can set the key only in an MDM profile or the local configuration file. Claude Desktop ignores it in a bootstrap server's response.)

Since 1.32885.1

**Bootstrap headers helper script.** Absolute path to an executable that prints a JSON object of bootstrap request headers. Merged over the static headers; the helper wins.

[Guide for this setting](https://claude.com/docs/third-party/claude-desktop/bootstrap.md)

[Admin Console](#the-works-with-column): Not available.

> [accordion] More detail
>
> Example output: `{"Authorization": "Bearer …"}`. The app runs the helper script with no arguments and reuses its output for a few minutes.
>
> If `bootstrapOidc` is unset, the app treats these headers as sufficient authentication and requires no per-user sign-in for the bootstrap fetch. If a per-user sign-in also runs, its token takes priority for the `Authorization` header.

***

#### `trustBootstrapDelivery`

booleanDefault: false

MDM only (You can set the key only in an MDM profile or the local configuration file. Claude Desktop ignores it in a bootstrap server's response.)

Since 1.26832.0

**Trust bootstrap-delivered settings.** Skip the per-user consent prompt for sign-in settings, inference endpoints, helper scripts, and connectors the bootstrap server delivers.

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

* **Admin Console**: The key takes effect where your organization manages Claude Desktop from the Enterprise Admin Console. [Read more](https://claude.com/docs/third-party/claude-desktop/admin-console.md).

  * **No hover text**: The hosted configuration can hold the key. Set it on the console's pages or, where no page has a field for it, by importing a configuration file or through the Admin API.
  * **Set automatically** on hover and in the key's entry: Anthropic fills the key in from your organization's own settings, such as its name or its built-in browser settings, each time an app downloads the configuration. A value written for the key in the hosted configuration has no effect.
  * **No badge**, and **Not available** in the key's entry: The hosted configuration can't hold the key, so you can't set it from the console.

  The hosted configuration refuses some values of keys that it can hold, for example an API key or token in a request header, and the Claude API as the inference provider. On a device that also has an MDM profile, the app still reads a few keys from the profile, for example the network proxy keys, which the console can't set. The Enterprise Admin Console guide lists them.

## Guides

* [Configuration implementation](https://claude.com/docs/third-party/claude-desktop/configuration-format.md): how configuration differs between a device's own configuration and the Enterprise Admin Console, and how to write each value type.
* [Configuration changelog](https://claude.com/docs/third-party/claude-desktop/configuration-changelog.md): the desktop release each key first appeared in.
* [Models and effort levels](https://claude.com/docs/third-party/claude-desktop/models.md): how the keys under **Models** work together.
* [Unified Claude](https://claude.com/docs/third-party/claude-desktop/unified-claude.md#how-unified-claude-interacts-with-chat-and-cowork-settings): how `desktopHome` overrides the other keys under **Chat surface** and **Cowork surface**.
* [Automatic deletion of idle sessions](https://claude.com/docs/third-party/claude-desktop/data-storage.md#automatic-deletion-of-idle-sessions): which key under **Session retention** covers a conversation started from the home screen.
* [Skill scanning](https://claude.com/docs/third-party/claude-desktop/extensions.md#skill-scanning): what `skillScanningEnabled` turns on, which model runs a scan, and what users and your collector see.
* [Status line](https://claude.com/docs/third-party/claude-desktop/status-line.md): where to install the program that `sessionStatusLine` runs, what the program receives, and what it can print.

### Recommended security profiles

The profiles below are illustrative examples rather than built-in presets, and the labels are descriptive only. Use them as starting points and adjust for your environment. Layer the inference-provider keys for your cloud on top of whichever profile you choose.

> [tab] Standard
>
> Recommended for most enterprise deployments. Telemetry and auto-updates stay on so Anthropic can diagnose issues and ship fixes; users can extend Claude Desktop with their own connectors.
>
> | Key | Value |
> | - | - |
> | [`deploymentOrganizationUuid`](#deploymentorganizationuuid) | `<your-org-uuid>` |
> | [`autoUpdaterEnforcementHours`](#autoupdaterenforcementhours) | `24` |
> | [`isDesktopExtensionSignatureRequired`](#isdesktopextensionsignaturerequired) | `true` |
> | [`otlpEndpoint`](#otlpendpoint) | `<your-collector>` |

> [tab] Restricted
>
> For regulated environments that need to control what users can connect Claude Desktop to, while keeping Anthropic supportability.
>
> | Key | Value |
> | - | - |
> | [`deploymentOrganizationUuid`](#deploymentorganizationuuid) | `<your-org-uuid>` |
> | [`disableDeploymentModeChooser`](#disabledeploymentmodechooser) | `true` |
> | [`disableNonessentialTelemetry`](#disablenonessentialtelemetry) | `true` |
> | [`disableNonessentialServices`](#disablenonessentialservices) | `true` |
> | [`isLocalDevMcpEnabled`](#islocaldevmcpenabled) | `false` |
> | [`isDesktopExtensionEnabled`](#isdesktopextensionenabled) | `false` |
> | [`allowedWorkspaceFolders`](#allowedworkspacefolders) | `[{"path":"~/Documents/Claude"}]` |
> | [`coworkEgressAllowedHosts`](#coworkegressallowedhosts) | `["*.example.corp"]` |
> | [`otlpEndpoint`](#otlpendpoint) | `<your-collector>` |

> [tab] Locked down
>
> For air-gapped or maximally restricted environments. **The app's own traffic goes only to your inference endpoint and OTLP collector**, plus `downloads.claude.ai` for the VM bundle and Claude CLI binary at session start unless you deploy the [offline installer](https://claude.com/docs/third-party/claude-desktop/installation.md#offline-installation). Code sessions on Windows, and on Linux without Claude Code's sandbox dependencies, [run shell commands unsandboxed](https://claude.com/docs/third-party/claude-desktop/code.md#applied-as-managed-policy), so those commands can reach any host your network allows. To prevent that, [turn off Code](https://claude.com/docs/third-party/claude-desktop/code.md#disabling-code) on those devices. With this profile, Anthropic receives no telemetry or logs from the app and does not deliver updates, so your team owns log collection and update distribution. On Microsoft Foundry, the Claude models behind your inference endpoint run in an Anthropic-operated service, so conversation content still reaches Anthropic-operated infrastructure under this profile, as described under [Data handling by provider](https://claude.com/docs/third-party/claude-desktop/overview.md#data-handling-by-provider).
>
> | Key | Value |
> | - | - |
> | [`disableDeploymentModeChooser`](#disabledeploymentmodechooser) | `true` |
> | [`disableEssentialTelemetry`](#disableessentialtelemetry) | `true` |
> | [`disableNonessentialTelemetry`](#disablenonessentialtelemetry) | `true` |
> | [`disableNonessentialServices`](#disablenonessentialservices) | `true` |
> | [`disableAutoUpdates`](#disableautoupdates) | `true` |
> | [`modelCatalogEnabled`](#modelcatalogenabled) | `false` |
> | [`isLocalDevMcpEnabled`](#islocaldevmcpenabled) | `false` |
> | [`isDesktopExtensionEnabled`](#isdesktopextensionenabled) | `false` |
> | [`skillCreationEnabled`](#skillcreationenabled) | `false` |
> | [`userPluginMarketplacesEnabled`](#userpluginmarketplacesenabled) | `false` |
> | [`userPluginUploadsEnabled`](#userpluginuploadsenabled) | `false` |
> | [`scheduledTasksEnabled`](#scheduledtasksenabled) | `false` |
> | [`disabledBuiltinTools`](#disabledbuiltintools) | `["WebSearch","WebFetch"]` |
> | [`coworkEgressAllowedHosts`](#coworkegressallowedhosts) | `[]` |
> | [`allowedWorkspaceFolders`](#allowedworkspacefolders) | `[{"path":"~/Documents/Claude"}]` |
> | [`otlpEndpoint`](#otlpendpoint) | `<your-collector>` |

### Tool permissions for managed MCP servers

Each [`managedMcpServers`](#managedmcpservers) entry can carry a `toolPolicy` that sets the approval state per tool:

* `"allow"`: in Cowork sessions, the tool runs without an approval prompt, except that a built-in server's [irreversible actions](https://claude.com/docs/third-party/claude-desktop/built-in-connectors.md#how-built-in-servers-behave) stay at `"ask"` or stricter. In local Code sessions and Code sessions on an SSH host, `"allow"` doesn't pre-approve the tool, so the user can see an approval prompt for it.
* `"ask"`: the user approves every call; no session-scoped or standing grants are offered.
* `"blocked"`: the tool is removed from Claude's session; connector settings show it as blocked by your organization.

In Cowork's [**Automatically approve**](#automodeenabled), a safety classifier still reviews calls to a tool set to `"allow"`, and can block them. See [Run vetted connector tools without classifier review](https://claude.com/docs/third-party/claude-desktop/code.md#run-vetted-connector-tools-without-classifier-review).

Tools with no policy entry stay user-controlled (built-in connectors apply default policies to some tools): the user is prompted and can approve once, approve for the rest of the task (offered for tools that can modify data), or grant a standing approval unless [`mcpPersistentAlwaysAllowEnabled`](#mcppersistentalwaysallowenabled) is `false`. The app reads a `toolPolicy` value other than `"allow"`, `"ask"`, or `"blocked"`, such as `"ask-session"`, as `"blocked"` for that tool and reports a configuration error, so write `"ask"` in place of `"ask-session"`. Managed policies take precedence over user grants, and enforcement happens in the desktop host process, not only in the prompt UI. A deny-by-default posture, `"*": "blocked"` plus exact `"allow"` entries for approved tools, is supported, including in Code sessions. See the [`managedMcpServers` reference](#managedmcpservers) for wildcard matching, precedence rules, and built-in connector defaults.

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
