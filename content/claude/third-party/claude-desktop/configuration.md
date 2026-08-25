> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuration reference

> Every managed-configuration key Claude Desktop on 3P supports, what it controls, and recommended security profiles

<Tip>Most settings on this page are easier to configure in the [in-app configuration window](/docs/third-party/claude-desktop/in-app-configuration). Use this reference when you're scripting an MDM policy or bootstrap response by hand.</Tip>

Claude Desktop on third-party (3P) is configured entirely through OS-native managed preferences: a `.mobileconfig` profile on macOS, registry policy on Windows, or a root-owned JSON file on Linux. This page documents every supported key. For the desktop release each key first appeared in, see the [configuration changelog](/docs/third-party/claude-desktop/configuration-changelog).

The easiest way to author a configuration is the in-app configuration window (**Developer → Configure Third-Party Inference…**), which validates values, shows per-provider requirements, and exports directly to `.mobileconfig` or `.reg`. Use this reference when you need to author policy by hand, audit an existing profile, or understand exactly what a key does.

## How keys are read

| Platform | Managed (MDM) location                                                            | Local (user) location                                    |
| -------- | --------------------------------------------------------------------------------- | -------------------------------------------------------- |
| macOS    | `/Library/Managed Preferences/<user>/com.anthropic.claudefordesktop.plist`        | `~/Library/Application Support/Claude-3p/configLibrary/` |
| Windows  | `HKLM\SOFTWARE\Policies\Claude` (machine), `HKCU\SOFTWARE\Policies\Claude` (user) | `%LOCALAPPDATA%\Claude-3p\configLibrary\`                |
| Linux    | `/etc/claude-desktop/managed-settings.json`                                       | `~/.config/Claude-3p/configLibrary/`                     |

The local location is a directory: `_meta.json` records which saved configuration is applied, and each configuration is a `<id>.json` file alongside it. The in-app configuration window writes here.

When a managed source is present, it wins and locally written values are ignored. The exception is a managed source that sets only the update keys (`disableAutoUpdates`, `autoUpdaterEnforcementHours`, and `updateViaUpdatesHost`): those keys are enforced from the managed source, but the rest of the configuration stays local and user-editable. Configuration is read **once at launch**, so fully quit and reopen the app after any change. On Windows, the two policy hives are not merged: when machine policy is present under `HKLM\SOFTWARE\Policies\Claude`, the app ignores `HKCU\SOFTWARE\Policies\Claude` entirely; [Deploy the configuration](/docs/third-party/claude-desktop/mdm#4-deploy-the-configuration) has the exact rule. See [Deploy with MDM](/docs/third-party/claude-desktop/mdm#update-keys-and-managed-precedence) for the full precedence rules.

<Note>
  Claude Desktop on 3P reads the same managed-configuration sources as standard Claude Desktop but ignores keys scoped to standard deployments. Keys such as `forceLoginOrgUUID` have no effect in a 3P deployment.
</Note>

### Value types

Write every value as a **string** in the OS preference store, even booleans and arrays.

| Documented type  | What to write                                  | Example                                       |
| ---------------- | ---------------------------------------------- | --------------------------------------------- |
| string           | Plain string                                   | `vertex`                                      |
| boolean          | `"true"` or `"false"` (or `1` / `0`)           | `"true"`                                      |
| integer          | Decimal string                                 | `"3600"`                                      |
| string\[] (JSON) | JSON array **encoded as a string**             | `["claude-sonnet-5","claude-opus-5"]`         |
| object (JSON)    | JSON object mapping name to value, as a string | `{"X-Org-Id":"team1"}`                        |
| object\[] (JSON) | JSON array of objects, as a string             | see [`managedMcpServers`](#managedmcpservers) |

<Note>
  Array- and object-typed keys such as `inferenceModels`, `inferenceGatewayOidc`, `managedMcpServers`, `coworkEgressAllowedHosts`, and `otlpHeaders` are single keys whose value is a whole JSON document. The portable encoding is a JSON string, which works on every platform. In a `.mobileconfig` that is a single `<string>` element containing `[...]` or `{...}`, and on Windows a `REG_SZ` value. A macOS profile may instead carry the value as a native `<array>` or `<dict>`, which the app reads as the equivalent JSON. Separate keys with dotted names, such as `inferenceGatewayOidc.clientId`, are never read.
</Note>

On Windows, write registry values as `REG_SZ`, directly under the policy key rather than nested in a subkey (the app never reads subkeys). `REG_DWORD` is also accepted for boolean and integer keys and is read as its decimal value. Avoid `REG_EXPAND_SZ`: the app counts it toward machine policy being present but cannot read its contents. The app cannot see `REG_QWORD`, `REG_MULTI_SZ`, or `REG_BINARY` values at all.

### Linux

The managed source on Linux is a single JSON file, `/etc/claude-desktop/managed-settings.json`, with keys at the top level exactly as named in the [reference](#reference) — no wrapper object, no nesting:

```json theme={null}
{
  "inferenceProvider": "gateway",
  "inferenceGatewayBaseUrl": "https://gateway.example.com/v1",
  "inferenceGatewayApiKey": "sk-example",
  "inferenceCustomHeaders": { "X-Tenant-Id": "acme" }
}
```

Because the file is real JSON, array- and object-typed keys use native JSON values — the string-encoding rule above applies to plist and registry sources only. (String-encoded values are also accepted, so a profile generated for another platform can be reused.)

The file is only honored when it can't be edited by the user it configures:

* `managed-settings.json` must be a regular file (not a symlink), owned by root, and not group- or world-writable.
* `/etc/claude-desktop` itself must be a directory (not a symlink), owned by root, and not group- or world-writable.

A file that fails these checks is rejected: none of its settings are applied, the app treats the device as managed but unreadable, and local settings are also disabled until the file is fixed and the app is relaunched. The reason is logged to `main.log` in the app's logs directory — `~/.config/Claude/logs/` (or `~/.config/Claude-3p/logs/` once the app is running in 3P mode); search for `managed-settings.json`. The same log names any key that fails schema validation.

There is no per-user managed location on Linux; per-user configuration goes through the in-app configuration window, which writes to the local `configLibrary` directory above.

## Reference

The reference below is generated from the configuration schema and grouped to match the sidebar of the in-app configuration window. The **Availability** column shows whether a key can be set in an MDM profile, returned from a [bootstrap server](/docs/third-party/claude-desktop/bootstrap), or both.

## Connection

| Setting                                                                                                                                          | Type      | Availability    | Default | Description                                                                                                                                                                                                 |
| ------------------------------------------------------------------------------------------------------------------------------------------------ | --------- | --------------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <span id="inferencecustomheaders" />Custom inference headers<br />`inferenceCustomHeaders`                                                       | `object`  | MDM + Bootstrap | —       | Extra headers on every inference request — routing and tenant headers only (org IDs, Bedrock Guardrails). No credentials; use the credential helper for tokens. Previously named `inferenceGatewayHeaders`. |
| <span id="inferencesessionlifetimesec" />Sign-in session lifetime<br />`inferenceSessionLifetimeSec`                                             | `integer` | MDM + Bootstrap | —       | How long a sign-in stays valid under your IdP’s session policy. Shows a re-authenticate banner before it expires.                                                                                           |
| <span id="inferencecredentialhelper" />Helper script<br />`inferenceCredentialHelper`                                                            | `string`  | MDM + Bootstrap | —       | Absolute path to an executable that prints the credential, optionally with per-request headers.                                                                                                             |
| <span id="inferencecredentialhelperttlsec" />Helper script TTL<br />`inferenceCredentialHelperTtlSec`                                            | `integer` | MDM + Bootstrap | `3600`  | Helper output is cached for this many seconds. Re-runs at the next session start after expiry. Defaults to `3600`.                                                                                          |
| <span id="inferencecredentialhelpertimeoutsec" />Credential helper timeout<br />`inferenceCredentialHelperTimeoutSec`                            | `integer` | MDM + Bootstrap | `60`    | Maximum wait for the helper executable to finish. Raise this if the helper opens a browser for interactive sign-in. Defaults to `60`. Range: 1–600.                                                         |
| <span id="inferencecredentialhelpersilentrefreshenabled" />Re-run helper for silent refresh<br />`inferenceCredentialHelperSilentRefreshEnabled` | `boolean` | MDM + Bootstrap | `true`  | On credential expiry, re-run the helper (CLAUDE\_HELPER\_CONTEXT=mid-session-refresh) to recover silently. Turn off if the helper can’t run non-interactively. Defaults to `true`.                          |
| <span id="usercontentrendererurl" />Artifact preview iframe origin<br />`userContentRendererUrl`                                                 | `string`  | MDM + Bootstrap | —       | HTTPS origin of the user-content-renderer deployment used for artifact and file previews. Defaults to the commercial host when unset.                                                                       |
| <span id="inferenceprovider" />Inference provider<br />`inferenceProvider`                                                                       | `enum`    | MDM + Bootstrap | —       | Selects the inference backend. Setting this key activates third-party mode. One of: `gateway`, `anthropic`, `bedrock`, `mantle`, `vertex`, `foundry`.                                                       |
| <span id="inferencecredentialkind" />Credential kind<br />`inferenceCredentialKind`                                                              | `enum`    | MDM + Bootstrap | —       | Selects the credential source. When set, only that source is used (no fallback). One of: `static`, `helper-script`, `interactive`, `vendor-profile`, `oauth`, `workforce`.                                  |

<AccordionGroup>
  <Accordion title="inferenceCustomHeaders details">
    Sent on every inference and model-discovery request (joined into the CLI's `ANTHROPIC_CUSTOM_HEADERS`).

    Use this for fleet-wide, non-secret constants. **Do not put API keys, bearer tokens or other credentials here** — this map is stored and distributed as plain configuration. For tokens, and for per-user or per-session values, have the **credential helper script** emit JSON with a `headers` field; those are merged over these static entries (helper wins on conflict).
  </Accordion>

  <Accordion title="inferenceCredentialHelper details">
    Claude runs the executable with no arguments and reads **stdout** (trimmed). Exit code must be `0`; any output on **stderr** is logged but ignored. **Stdout must contain only one of the formats below** (no banners, prompts, or log lines).

    **Output format** is either:

    * a single bare token (the API key / bearer token), or
    * a JSON object `{"token": "...", "headers": {"Name": "Value", ...}}` when per-request headers are needed (merged over **Custom inference headers**, helper wins on conflict)

    The helper receives `CLAUDE_HELPER_CONTEXT` in its environment (`interactive`, `mid-session-refresh`, `background`, `scheduled-task`, `setup-test`) so it can decide whether to prompt the user — see the credential-helper docs for the full contract.

    Result is cached for the TTL below. On TTL expiry the helper is re-invoked transparently (no user prompt, no relaunch).

    **Expiry and refresh:** the app checks the active credential's expiry before each turn and refreshes silently when possible (re-runs the helper, or uses the stored refresh token for interactive sign-in kinds). If the provider returns HTTP 401 mid-turn, the same silent refresh is attempted before surfacing an error. When silent refresh fails, a prompt appears with a provider-specific action (re-sign-in for interactive kinds; admin-contact for static credentials). Applies to all providers, and to both Cowork and Code.

    **Typical use:** a shell script that pulls from Keychain, 1Password CLI, or an internal secret broker. Example:

    `security find-generic-password -s anthropic-api -w`

    If this field is set, static credential fields (API key, bearer token) are ignored. The helper always wins.
  </Accordion>

  <Accordion title="inferenceProvider details">
    The app activates 3P mode only when this is set and the required credential keys for the selected provider are present and valid; otherwise it launches in standard mode. Keys for providers other than the selected one are ignored. Each provider's required keys are documented on its dedicated page under Inference providers.
  </Accordion>
</AccordionGroup>

### Anthropic

| Setting                                                                              | Type     | Availability    | Default | Description                                                                                   |
| ------------------------------------------------------------------------------------ | -------- | --------------- | ------- | --------------------------------------------------------------------------------------------- |
| <span id="inferenceanthropicapikey" />Claude API key<br />`inferenceAnthropicApiKey` | `string` | MDM + Bootstrap | —       | Leave blank to fetch a key via browser sign-in, or to supply the key via a credential helper. |

### Bedrock

| Setting                                                                                          | Type     | Availability    | Default | Description                                                                                                       |
| ------------------------------------------------------------------------------------------------ | -------- | --------------- | ------- | ----------------------------------------------------------------------------------------------------------------- |
| <span id="inferencebedrockregion" />AWS region<br />`inferenceBedrockRegion`                     | `string` | MDM + Bootstrap | —       | AWS region for the Bedrock runtime endpoint.                                                                      |
| <span id="inferencebedrockbaseurl" />Bedrock base URL<br />`inferenceBedrockBaseUrl`             | `string` | MDM + Bootstrap | —       | For VPC endpoints or gateway proxies. Host origin only.                                                           |
| <span id="inferencebedrockservicetier" />Bedrock service tier<br />`inferenceBedrockServiceTier` | `enum`   | MDM + Bootstrap | —       | Sent as the X-Amzn-Bedrock-Service-Tier header. Leave unset for on-demand. One of: `flex`, `priority`.            |
| <span id="inferencebedrockbearertoken" />AWS bearer token<br />`inferenceBedrockBearerToken`     | `string` | MDM + Bootstrap | —       | Static bearer token for inference. For providers that support profile or helper-script credentials, prefer those. |
| <span id="inferencebedrockssostarturl" />AWS SSO start URL<br />`inferenceBedrockSsoStartUrl`    | `string` | MDM + Bootstrap | —       | Enables in-app AWS sign-in (no AWS CLI needed). Set with the three SSO fields below.                              |
| <span id="inferencebedrockssoregion" />AWS SSO region<br />`inferenceBedrockSsoRegion`           | `string` | MDM + Bootstrap | —       | IAM Identity Center home region.                                                                                  |
| <span id="inferencebedrockssoaccountid" />AWS SSO account ID<br />`inferenceBedrockSsoAccountId` | `string` | MDM + Bootstrap | —       | 12-digit AWS account ID assigned to users in IAM Identity Center.                                                 |
| <span id="inferencebedrockssorolename" />AWS SSO role name<br />`inferenceBedrockSsoRoleName`    | `string` | MDM + Bootstrap | —       | IAM Identity Center permission-set name granting bedrock:InvokeModel\* on the account above.                      |
| <span id="inferencebedrockprofile" />AWS profile name<br />`inferenceBedrockProfile`             | `string` | MDM + Bootstrap | —       | AWS named profile to use for Bedrock inference credentials.                                                       |
| <span id="inferencebedrockawsdir" />AWS config directory<br />`inferenceBedrockAwsDir`           | `string` | MDM + Bootstrap | —       | Folder with AWS config/credentials. Defaults to \~/.aws when no bearer token is set.                              |
| <span id="inferencebedrockawsclipath" />AWS CLI path<br />`inferenceBedrockAwsCliPath`           | `string` | MDM + Bootstrap | —       | Absolute path to the aws executable. Leave unset to find it on PATH.                                              |

<AccordionGroup>
  <Accordion title="inferenceBedrockServiceTier details">
    Tier availability varies by model and region. Reserved capacity uses a provisioned-throughput ARN as the model ID instead of this setting. Older bundled Claude Code CLI versions ignore this key.
  </Accordion>
</AccordionGroup>

### Foundry

| Setting                                                                                              | Type     | Availability    | Default | Description                                                                                                                           |
| ---------------------------------------------------------------------------------------------------- | -------- | --------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| <span id="inferencefoundryresource" />Azure AI Foundry resource name<br />`inferenceFoundryResource` | `string` | MDM + Bootstrap | —       | Azure AI Foundry resource name used to construct the endpoint URL.                                                                    |
| <span id="inferencefoundryapikey" />Azure AI Foundry API key<br />`inferenceFoundryApiKey`           | `string` | MDM + Bootstrap | —       | API key for Azure AI Foundry inference.                                                                                               |
| <span id="inferencefoundrytenantid" />Entra ID tenant ID<br />`inferenceFoundryTenantId`             | `string` | MDM + Bootstrap | —       | Directory (tenant) ID of the Entra ID app registration that has the Cognitive Services scope.                                         |
| <span id="inferencefoundryclientid" />Entra ID client ID<br />`inferenceFoundryClientId`             | `string` | MDM + Bootstrap | —       | Application (client) ID of the Entra ID app registration. Device-code sign-in requires the app to allow public client flows.          |
| <span id="inferencefoundryauthflow" />Entra ID sign-in flow<br />`inferenceFoundryAuthFlow`          | `enum`   | MDM + Bootstrap | —       | How Entra sign-in runs: device code (default), system browser, or the OS identity broker. One of: `device-code`, `browser`, `broker`. |

<AccordionGroup>
  <Accordion title="inferenceFoundryAuthFlow details">
    * **`device-code`** (default) — shows a code to enter at microsoft.com/devicelogin. The app registration must have **Allow public client flows** enabled.
    * **`browser`** — opens the system browser for an authorization-code (PKCE) sign-in on a loopback redirect URI. The app registration must include `http://127.0.0.1/callback` under the **Mobile and desktop applications** platform (Entra ignores the loopback port, but not the path). Works with **Allow public client flows** disabled, and is unaffected by Conditional Access policies that block device-code authentication.
    * **`broker`** — signs in through the OS identity broker (Web Account Manager on Windows, Company Portal on macOS), so it can satisfy Conditional Access policies that require a compliant/managed device or token protection. The app registration must include the broker redirect URIs `ms-appx-web://Microsoft.AAD.BrokerPlugin/{client-id}` (Windows) and `msauth.com.anthropic.claudefordesktop://auth` (macOS) under the **Mobile and desktop applications** platform. Not supported on Linux.

    App versions that predate this key always use device code; versions that predate the broker option treat `broker` as unset and use device code.
  </Accordion>
</AccordionGroup>

### Gateway

| Setting                                                                                            | Type     | Availability    | Default  | Description                                                                                                                                      |
| -------------------------------------------------------------------------------------------------- | -------- | --------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| <span id="inferencegatewaybaseurl" />Gateway base URL<br />`inferenceGatewayBaseUrl`               | `string` | MDM + Bootstrap | —        | Full URL of the inference gateway endpoint.                                                                                                      |
| <span id="inferencegatewayapikey" />Gateway API key<br />`inferenceGatewayApiKey`                  | `string` | MDM + Bootstrap | —        | API key for the configured inference gateway.                                                                                                    |
| <span id="inferencegatewayauthscheme" />Gateway auth scheme<br />`inferenceGatewayAuthScheme`      | `enum`   | MDM + Bootstrap | `bearer` | How the gateway credential is sent on the wire (Authorization: Bearer vs x-api-key header). One of: `bearer`, `x-api-key`. Defaults to `bearer`. |
| <span id="inferencegatewayoidcauthflow" />Gateway sign-in flow<br />`inferenceGatewayOidcAuthFlow` | `enum`   | MDM + Bootstrap | —        | How the IdP sign-in runs: system browser (default) or the OS Microsoft Entra broker. One of: `browser`, `broker`.                                |
| <span id="inferencegatewayoidc" />Gateway SSO IdP (OIDC)<br />`inferenceGatewayOidc`               | `object` | MDM + Bootstrap | —        | External IdP for gateway sign-in. The user’s token from this issuer is sent to the gateway as the Bearer credential.                             |

<AccordionGroup>
  <Accordion title="inferenceGatewayOidcAuthFlow details">
    * **`browser`** (default) — opens the system browser for an authorization-code (PKCE) sign-in on a loopback redirect URI. See the **IdP setup** notes on `inferenceGatewayOidc` for redirect-URI registration.
    * **`broker`** — signs in through the OS identity broker (Web Account Manager on Windows, Company Portal on macOS). Requires the IdP to be **Microsoft Entra ID** — the `issuer` on `inferenceGatewayOidc` must be `https://login.microsoftonline.com/{tenant-id}/v2.0`. The broker satisfies Conditional Access policies that require a compliant/managed device or token protection, and needs no `127.0.0.1/callback` loopback redirect. The Entra app registration must include the broker redirect URIs `ms-appx-web://Microsoft.AAD.BrokerPlugin/{client-id}` (Windows) and `msauth.com.anthropic.claudefordesktop://auth` (macOS) under the **Mobile and desktop applications** platform. Not supported on Linux.

    Broker mode mints a token in the customer's own Entra tenant with the customer-configured `scopes`, and forwards it to the customer's own gateway; both endpoints of that trust relationship are inside the customer's control.
  </Accordion>

  <Accordion title="inferenceGatewayOidc details">
    **External IdP mode.** The app discovers `<issuer>/.well-known/openid-configuration`, runs an OIDC authorization-code-with-PKCE flow in the system browser with `clientId`, and sends the resulting token as `Authorization: Bearer` on every inference request — see **Bearer token type** below for how the gateway validates it.

    **Bearer token type.** `id_token` (the default) sends the OIDC ID token — the gateway validates signature + `iss` + `aud`, where `aud` is the `clientId` configured here. `access_token` sends the OAuth access token — the gateway validates as an OAuth resource server against the audience/scope the IdP issued the token for; set `scopes` to the gateway's registered API scope (required in this mode). Use `access_token` for gateways that expect a resource-server token (Portkey, Kong, Envoy JWT filter, AWS API Gateway authorizers).

    **The gateway MUST validate `iss` AND `aud`, not just the signature.** Signature + issuer alone accepts *any* token from the same tenant, including tokens issued to unrelated apps. In `id_token` mode the audience is the `clientId`:

    ```yaml theme={null}
    # LiteLLM example — `audience` is REQUIRED, not optional
    general_settings:
      litellm_jwtauth:
        public_key_url: https://login.microsoftonline.com/<tenant>/discovery/v2.0/keys
        audience: <clientId>           # ⚠ omitting this accepts any token from the tenant
    ```

    **IdP setup.** The app's loopback callback binds `http://127.0.0.1:<port>/callback` (RFC 8252 §7.3). Register `127.0.0.1`; most IdPs do **not** treat `localhost` and `127.0.0.1` as interchangeable. **Entra:** register a public-client app, add a *Mobile and desktop applications* redirect URI of `http://127.0.0.1/callback`. (Microsoft's docs say the path is wildcarded for loopback; in practice it is not: `http://127.0.0.1` without `/callback` fails with `AADSTS50011`. The port IS wildcarded.) Grant `openid profile email offline_access` (delegated, no admin consent); in `access_token` mode **also** add the gateway API's delegated permission under *API permissions* (and ensure the gateway's own app registration exposes that scope via *Expose an API*) — without it Entra rejects the sign-in with `AADSTS65001`. **Okta:** register a *Native* app with the exact redirect URI `http://127.0.0.1:<port>/callback` and set `redirectPort` here to that port (Okta requires an exact match).

    **Refresh:** `offline_access` returns a refresh token; the app refreshes the bearer silently before expiry. When refresh fails (revoked, idle past the IdP's window), the user re-authenticates in the browser. **Google Workspace caveat (`id_token` mode only):** Google never returns `id_token` on a refresh-token grant, so a Google-backed gateway in `id_token` mode will prompt a browser sign-in roughly once per ID-token TTL (\~1h). Entra and Okta return a fresh `id_token` and are unaffected; `access_token` mode is unaffected on all IdPs.

    **Leave this unset** for a gateway that hosts its own RFC 8414 metadata at `<baseUrl>/.well-known/oauth-authorization-server` (the original gateway-as-AS path).

    | Field                             | Type      | Default    | Description                                                                                                                                                |
    | --------------------------------- | --------- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | `clientId`                        | `string`  | —          | OAuth client ID of the desktop app registration at your identity provider (public client, PKCE).                                                           |
    | `issuer`                          | `string`  | —          | HTTPS issuer with OIDC discovery. Set this, or set the authorization and token URLs instead.                                                               |
    | `authorizationUrl`                | `string`  | —          | HTTPS authorization endpoint. Used with the token URL when no issuer is set.                                                                               |
    | `tokenUrl`                        | `string`  | —          | HTTPS token endpoint. Used with the authorization URL when no issuer is set.                                                                               |
    | `bearerTokenType`                 | `enum`    | `id_token` | Which token to send as the gateway bearer. Use access token for gateways that validate as an OAuth resource server. One of: `id_token`, `access_token`.    |
    | `scopes`                          | `string`  | —          | Space-separated scopes. Required in access-token mode: set the gateway’s API scope. offline\_access is appended automatically unless disabled below.       |
    | `appendOfflineAccess`             | `boolean` | `true`     | Automatically append offline\_access to scopes so the IdP returns a refresh token for silent refresh.                                                      |
    | `resource`                        | `string`  | —          | Absolute URL identifying the gateway as the access-token audience. Sent as the RFC 8707 resource parameter when set; leave unset for Microsoft Entra ID.   |
    | `redirectPort`                    | `integer` | —          | Fixed loopback port for the sign-in redirect ([http://127.0.0.1:PORT/callback](http://127.0.0.1:PORT/callback)). Leave unset to use a free port each time. |
    | `additionalRedirectReferrerHosts` | `string`  | —          | Space-separated hostnames also accepted as the referrer of the sign-in callback. Only needed when the IdP completes sign-in from a different host.         |
  </Accordion>
</AccordionGroup>

### Models

| Setting                                                                             | Type       | Availability    | Default | Description                                                                                                           |
| ----------------------------------------------------------------------------------- | ---------- | --------------- | ------- | --------------------------------------------------------------------------------------------------------------------- |
| <span id="modeldiscoveryenabled" />Model discovery<br />`modelDiscoveryEnabled`     | `boolean`  | MDM + Bootstrap | —       | Auto-populate the model picker from the provider at launch.                                                           |
| <span id="modelprefer1mcontext" />Default to 1M context<br />`modelPrefer1mContext` | `boolean`  | MDM + Bootstrap | —       | When a user has no saved selection, start the picker on the 1M-context variant of the default model if it offers one. |
| <span id="inferencemodels" />Model list<br />`inferenceModels`                      | `object[]` | MDM + Bootstrap | —       | Override the auto-discovered model list. First entry is the default.                                                  |

<AccordionGroup>
  <Accordion title="modelDiscoveryEnabled details">
    Auto-populate the model picker from the provider's model-list endpoint at launch. For gateway and Anthropic providers, a config that doesn't set this key skips discovery automatically when the model list below already makes it unnecessary; the toggle here only sets it explicitly on or off. Turn off if the endpoint isn't reachable from your network, or to use a fixed list. When off, the model list below is required and must use full model IDs (aliases like sonnet/opus are resolved via discovery).
  </Accordion>

  <Accordion title="modelPrefer1mContext details">
    When a user has no saved selection, start the picker on the 1M-context variant of the default model (the first listed model, or the first model your endpoint returns under discovery) if it offers one. A saved selection is always kept; users who picked a model before this version need to pick the 1M row once, after which it persists. Equivalent to setting `prefer1m` on the default entry of `inferenceModels`, but also applies under dynamic discovery.
  </Accordion>

  <Accordion title="inferenceModels details">
    Use the **provider's exact model ID**: Vertex publisher IDs (`claude-sonnet-5`), Bedrock inference-profile IDs (`us.anthropic.claude-sonnet-5`), or Foundry deployment names. The first entry is the default. Entries may be plain ID strings or objects.

    **Gateway:** the `name` must be the exact ID your gateway's `/v1/models` endpoint returns. If you set `supports1m` on an alias (`sonnet`) but discovery returns the full ID, the variant won't appear.

    **Extended context** (`supports1m`) is a capability assertion you make about your deployment; only set it for models you've confirmed support the 1M-token window:

    ```json theme={null}
    [{"name": "claude-sonnet-5", "supports1m": true}, "claude-opus-4-8"]
    ```

    **Default to 1M context** (`prefer1m`) makes the 1M-context variant the default picker selection when this entry is the default model (the first entry); users can still switch to the standard variant, and an explicit user pick is always kept. No effect without `supports1m`. Under dynamic discovery (no explicit list), the equivalent flat key in the **Models** group applies instead:

    ```json theme={null}
    [{"name": "claude-opus-4-8", "supports1m": true, "prefer1m": true}]
    ```

    **Display label** (`labelOverride`) is for IDs the picker can't derive a friendly name from (Bedrock ARNs, gateway routing aliases). Display-only; `name` is still what the app sends:

    ```json theme={null}
    [{"name": "arn:aws:bedrock:us-east-1:123:application-inference-profile/abc", "labelOverride": "Claude Opus (Prod)"}]
    ```

    **Tier mapping** (`anthropicFamilyTier`) tells the app which Claude tier (`haiku`/`sonnet`/`opus`/`fable`/`mythos`) an entry stands in for, so bare tier aliases (e.g. in Code sessions) resolve to your model. `isFamilyDefault: true` picks the winner when several entries share a tier:

    ```json theme={null}
    [{"name": "us.anthropic.claude-opus-4-8", "anthropicFamilyTier": "opus"}]
    ```

    | Field                 | Type      | Default | Description                                                                                                                                                                    |
    | --------------------- | --------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
    | `name`                | `string`  | —       | Model ID exactly as the provider expects it. The first entry is the default model.                                                                                             |
    | `labelOverride`       | `string`  | —       | Shown in the model picker. Leave blank to auto-format from the ID.                                                                                                             |
    | `supports1m`          | `boolean` | —       | Adds a 1M-context variant of this model to the picker. Set only if the deployment accepts 1M-token context for it.                                                             |
    | `prefer1m`            | `boolean` | —       | Make the 1M-context variant the default picker selection when this model is the default (first) entry. Users can still choose the standard variant.                            |
    | `anthropicFamilyTier` | `enum`    | —       | Which Claude tier this model stands in for. Pins the bare alias (e.g. ‘opus’) and, for opus/fable, the refusal fallback. One of: `sonnet`, `opus`, `haiku`, `fable`, `mythos`. |
    | `isFamilyDefault`     | `boolean` | —       | When several models share a tier alias, marks this one as the model the alias resolves to. Otherwise the first listed wins.                                                    |
  </Accordion>
</AccordionGroup>

### Vertex

| Setting                                                                                                                        | Type     | Availability    | Default | Description                                                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------------ | -------- | --------------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <span id="inferencevertexprojectid" />GCP project ID<br />`inferenceVertexProjectId`                                           | `string` | MDM + Bootstrap | —       | Google Cloud project ID for Vertex AI inference.                                                                                                          |
| <span id="inferencevertexregion" />GCP region<br />`inferenceVertexRegion`                                                     | `string` | MDM + Bootstrap | —       | GCP region where your Vertex AI Claude models are deployed.                                                                                               |
| <span id="inferencevertexbaseurl" />Vertex AI base URL<br />`inferenceVertexBaseUrl`                                           | `string` | MDM + Bootstrap | —       | PSC endpoint, if using one.                                                                                                                               |
| <span id="inferencevertexoauthclientid" />Vertex OAuth client ID<br />`inferenceVertexOAuthClientId`                           | `string` | MDM + Bootstrap | —       | Desktop-app OAuth client ID. Enables Sign in with Google instead of a credentials file.                                                                   |
| <span id="inferencevertexoauthclientsecret" />Vertex OAuth client secret<br />`inferenceVertexOAuthClientSecret`               | `string` | MDM + Bootstrap | —       | Secret for the Desktop-app OAuth client above. Google classifies installed-app client secrets as non-confidential, so this may be set from hosted config. |
| <span id="inferencevertexoauthscopes" />Vertex OAuth scopes<br />`inferenceVertexOAuthScopes`                                  | `string` | MDM + Bootstrap | —       | Override the Google OAuth scopes (space-separated). Leave blank for the default.                                                                          |
| <span id="inferencevertexoauthloginhint" />Vertex OAuth login hint<br />`inferenceVertexOAuthLoginHint`                        | `string` | MDM + Bootstrap | —       | Pre-fill Google's account chooser and forward to your federated IdP. \{username} expands to the OS login name.                                            |
| <span id="inferencevertexworkforceaudience" />Workforce Identity audience<br />`inferenceVertexWorkforceAudience`              | `string` | MDM + Bootstrap | —       | Workforce-pool provider audience. When set, sign-in uses your own IdP plus a GCP STS exchange instead of a Google identity.                               |
| <span id="inferencevertexworkforceuserproject" />Workforce Identity billing project<br />`inferenceVertexWorkforceUserProject` | `string` | MDM + Bootstrap | —       | GCP project for STS billing and quota. Defaults to the Vertex project ID above.                                                                           |
| <span id="inferencevertexworkforceauthflow" />Workforce Identity sign-in flow<br />`inferenceVertexWorkforceAuthFlow`          | `enum`   | MDM + Bootstrap | —       | How the IdP sign-in runs: system browser (default) or the OS Microsoft Entra broker. One of: `browser`, `broker`.                                         |
| <span id="inferencevertexworkforceoidc" />Workforce Identity IdP (OIDC)<br />`inferenceVertexWorkforceOidc`                    | `object` | MDM + Bootstrap | —       | Your organization’s OIDC IdP. The app runs an authorization-code-with-PKCE flow against this issuer and exchanges the returned ID token at GCP STS.       |
| <span id="inferencevertexcredentialsfile" />GCP credentials file path<br />`inferenceVertexCredentialsFile`                    | `string` | MDM + Bootstrap | —       | Absolute path to service-account JSON. Leave blank to fall back to ADC.                                                                                   |

<AccordionGroup>
  <Accordion title="inferenceVertexWorkforceAuthFlow details">
    * **`browser`** (default) — opens the system browser for an authorization-code (PKCE) sign-in on a loopback redirect URI. See the **IdP setup** notes on `inferenceGatewayOidc` for redirect-URI registration; the same rules apply here.
    * **`broker`** — signs in through the OS identity broker (Web Account Manager on Windows, Company Portal on macOS). Requires the workforce-pool IdP to be **Microsoft Entra ID** — the `issuer` on `inferenceVertexWorkforceOidc` must be `https://login.microsoftonline.com/{tenant-id}/v2.0`. The broker satisfies Conditional Access policies that require a compliant/managed device or token protection, and needs no `127.0.0.1/callback` loopback redirect. The Entra app registration must include the broker redirect URIs `ms-appx-web://Microsoft.AAD.BrokerPlugin/{client-id}` (Windows) and `msauth.com.anthropic.claudefordesktop://auth` (macOS) under the **Mobile and desktop applications** platform. Not supported on Linux.

    The GCP STS token-exchange step is unchanged in either flow; only how the Entra id\_token is acquired differs.
  </Accordion>

  <Accordion title="inferenceVertexWorkforceOidc details">
    | Field                             | Type      | Default | Description                                                                                                                                                |
    | --------------------------------- | --------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | `clientId`                        | `string`  | —       | OAuth client ID of the desktop app registration at your identity provider (public client, PKCE).                                                           |
    | `issuer`                          | `string`  | —       | HTTPS issuer with OIDC discovery. Set this, or set the authorization and token URLs instead.                                                               |
    | `authorizationUrl`                | `string`  | —       | HTTPS authorization endpoint. Used with the token URL when no issuer is set.                                                                               |
    | `tokenUrl`                        | `string`  | —       | HTTPS token endpoint. Used with the authorization URL when no issuer is set.                                                                               |
    | `scopes`                          | `string`  | —       | Space-separated scopes. Defaults to openid profile email offline\_access.                                                                                  |
    | `redirectPort`                    | `integer` | —       | Fixed loopback port for the sign-in redirect ([http://127.0.0.1:PORT/callback](http://127.0.0.1:PORT/callback)). Leave unset to use a free port each time. |
    | `omitOfflineAccess`               | `boolean` | —       | Only enable if your IdP rejects the offline\_access scope on this client. Without it the app prompts for sign-in each time the token expires.              |
    | `additionalRedirectReferrerHosts` | `string`  | —       | Space-separated hostnames also accepted as the referrer of the sign-in callback. Only needed when the IdP completes sign-in from a different host.         |
  </Accordion>
</AccordionGroup>

## Workspace

### Authentication

| Setting                                                                                                          | Type      | Availability    | Default | Description                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------- | --------- | --------------- | ------- | -------------------------------------------------------------------------------------------------------------------- |
| <span id="disabledeploymentmodechooser" />Disable Claude.ai sign-in<br />`disableDeploymentModeChooser`          | `boolean` | MDM + Bootstrap | `false` | Users see only this provider at the login screen. The option to sign in to Claude.ai is hidden. Defaults to `false`. |
| <span id="disabledeeplinkregistration" />Disable claude:// deep-link handling<br />`disableDeepLinkRegistration` | `boolean` | MDM + Bootstrap | `false` | Stop external apps and websites from opening Cowork via claude:// links. Defaults to `false`.                        |

### Chat surface

| Setting                                                                                                    | Type      | Availability    | Default | Description                                                                                                                               |
| ---------------------------------------------------------------------------------------------------------- | --------- | --------------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| <span id="chattabenabled" />Allow Chat<br />`chatTabEnabled`                                               | `boolean` | MDM + Bootstrap | —       | Enable Chat. Quick questions and drafting.                                                                                                |
| <span id="chatadvancedfileanalysisenabled" />Advanced file analysis<br />`chatAdvancedFileAnalysisEnabled` | `boolean` | MDM + Bootstrap | —       | Allow Claude to run code in a local sandbox to analyze attached files it can’t read natively — like Excel and PowerPoint. Off by default. |

<AccordionGroup>
  <Accordion title="chatAdvancedFileAnalysisEnabled details">
    Also enables inline data analysis. The sandbox can only read files attached to the conversation and has no network access.
  </Accordion>
</AccordionGroup>

### Code surface

| Setting                                                                                    | Type      | Availability    | Default | Description                                                   |
| ------------------------------------------------------------------------------------------ | --------- | --------------- | ------- | ------------------------------------------------------------- |
| <span id="isclaudecodefordesktopenabled" />Allow Code<br />`isClaudeCodeForDesktopEnabled` | `boolean` | MDM + Bootstrap | `true`  | Enable Code. Claude writes and runs code. Defaults to `true`. |

### Cowork surface

| Setting                                                            | Type      | Availability    | Default | Description                                                                                             |
| ------------------------------------------------------------------ | --------- | --------------- | ------- | ------------------------------------------------------------------------------------------------------- |
| <span id="coworktabenabled" />Allow Cowork<br />`coworkTabEnabled` | `boolean` | MDM + Bootstrap | `true`  | Enable Cowork. Claude works on longer tasks like research, analysis, and documents. Defaults to `true`. |

### Workspace

| Setting                                                                                            | Type       | Availability                 | Default | Description                                                                                                                                                 |
| -------------------------------------------------------------------------------------------------- | ---------- | ---------------------------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <span id="disabledbuiltintools" />Disabled built-in tools<br />`disabledBuiltinTools`              | `string[]` | MDM + Bootstrap              | —       | Built-in tools removed from Cowork.                                                                                                                         |
| <span id="disablebundledskills" />Disable bundled skills and workflows<br />`disableBundledSkills` | `boolean`  | MDM + Bootstrap              | —       | Disables Claude Code’s bundled skills and workflows (deep-research and similar). Use where WebFetch/WebSearch aren’t available.                             |
| <span id="skillcreationenabled" />Allow user-created skills<br />`skillCreationEnabled`            | `boolean`  | MDM + Bootstrap              | —       | Allow users to create and upload their own skills. When off, the creation and upload surfaces are hidden and the agent’s skill-creation tools are disabled. |
| <span id="builtintoolpolicy" />Built-in tool policy<br />`builtinToolPolicy`                       | `object`   | MDM + Bootstrap              | —       | Per-tool approval policy for built-in tools. “ask” requires user approval before each call; “allow” is the default.                                         |
| <span id="automodeenabled" />Allow Auto mode<br />`autoModeEnabled`                                | `boolean`  | MDM + Bootstrap              | `false` | Offer Auto mode in the Cowork and Code permission selectors. Claude decides which actions need approval. Defaults to `false`.                               |
| <span id="toolsearchenabled" />Enable tool search<br />`toolSearchEnabled`                         | `boolean`  | MDM + Bootstrap              | `false` | Load MCP tool schemas on demand (tool search) instead of inlining every schema into context. Defaults to `false`.                                           |
| <span id="allowedworkspacefolders" />Allowed workspace folders<br />`allowedWorkspaceFolders`      | `object[]` | MDM + Bootstrap              | —       | Folders where Claude may work. Applies to both Cowork and Code sessions. Leave unset for unrestricted access.                                               |
| <span id="coworkegressallowedhosts" />Allowed egress hosts<br />`coworkEgressAllowedHosts`         | `string[]` | MDM + Bootstrap              | —       | Hostnames the agent’s tools may reach from Cowork and Code sessions. Also surfaced under Egress Requirements.                                               |
| <span id="requirecoworkfullvmsandbox" />Require full VM sandbox<br />`requireCoworkFullVmSandbox`  | `boolean`  | MDM + Bootstrap · Deprecated | `false` | Runs tools inside an isolated VM instead of the host. Stronger isolation; slower file access and no host-process tools. Defaults to `false`.                |

<AccordionGroup>
  <Accordion title="skillCreationEnabled details">
    When on (default), users can create new skills and upload skill files in the app. Set to `false` to block user skill creation: the skill-creation and upload surfaces are hidden (the `skill_creation` feature is served as blocked by the organization), and the agent's skill-creation tools (saving skills from a conversation, skill proposals) are not offered in sessions — the same effect as turning off the **User-created skills** organization setting available to claude.ai enterprise admins.

    This is a feature-availability control enforced in the app's UI, not a data boundary: skills are files on the user's machine, and files already present there (or placed there outside the app) are not removed or blocked by this key. Skills themselves remain usable; organization-distributed plugins and bundled skills are unaffected (to disable bundled skills, use `disableBundledSkills`).
  </Accordion>

  <Accordion title="builtinToolPolicy details">
    `ask-session` is accepted for compatibility and treated as `ask`. To remove a tool entirely, use **Disabled built-in tools** instead.
  </Accordion>

  <Accordion title="autoModeEnabled details">
    When enabled, users can select **Auto mode** (Code) / **Automatically approve** (Cowork). Claude runs a safety classifier on each action and only prompts for approval on actions it judges risky, instead of following the static per-tool policy.

    Requires a model that supports the safety classifier — which models qualify depends on the deployment's provider and the app version. Models without support show the option greyed out. `builtinToolPolicy` and this key may both be set; Auto mode is a user-selectable option alongside the default policy, not a replacement for it.

    In Code sessions, a separately deployed Claude Code [managed-settings](https://claude.com/docs/third-party/claude-desktop/code#interaction-with-claude-code%E2%80%99s-own-managed-settings) file that sets `disableAutoMode` to `"disable"` overrides this key and keeps Auto mode hidden.
  </Accordion>

  <Accordion title="toolSearchEnabled details">
    When enabled, Cowork, Code, and Chat sessions load MCP tool schemas on demand ("tool search"): only tool names are placed in context up front, and Claude fetches a tool's full schema the first time it needs it. Use this when many MCP tools are configured and their inlined schemas crowd out the context window (sessions that compact every turn or two). Equivalent to running terminal Claude Code with `ENABLE_TOOL_SEARCH=true` against the same endpoint.

    **Enabling this key causes sessions to send experimental `anthropic-beta` request headers, and the beta request fields that ride with them, to your inference endpoint** — tool search (`advanced-tool-use`, with `tool_reference` content blocks and deferred tool loading) and context management (a `context_management` request field on supported models) among them. Enable it only if your gateway forwards and accepts these; when it does not, requests fail with HTTP 400 on the beta header or fields. A practical preflight: run terminal Claude Code through the same gateway with `ENABLE_TOOL_SEARCH=true` — Claude Desktop then sends the same request surface, so if the terminal works, Desktop will too. **Do not enable this on Vertex-provider deployments** — Vertex rejects the tool-search beta header, and this key overrides the protection Claude Code applies to Vertex by default, turning working (inlined) MCP tools into failing requests.

    Claude Desktop otherwise suppresses **all** of Claude Code's experimental beta features on 3P deployments (it pins `CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS=1` into session environments, because strict gateways reject unrecognized beta headers and fields). Enabling this key lifts that suppression, so other experimental betas — for example, on gateway- and Foundry-backed deployments, `context_management` request fields on models that support them — are re-enabled as well. This matches the request surface terminal Claude Code presents through the same gateway by default. Leave unset to keep the conservative default.
  </Accordion>

  <Accordion title="allowedWorkspaceFolders details">
    Paths can reference `~` and these environment variables, expanded per user: `%OneDrive%`, `%OneDriveCommercial%`, `%OneDriveConsumer%`, `%APPDATA%`, `%LOCALAPPDATA%`, `%USERNAME%`, `%XDG_DOCUMENTS_DIR%`. The set is fixed; an entry that references any other `%VAR%`, or one that is unset on the device, is ignored.

    Each folder is interpreted on the machine the session runs on. For a Code session on an SSH host, `~` means the remote user's home, an entry that references a `%VAR%` is ignored there (environment variables belong to the machine that defines them), and the session's working directory must fall inside one of the folders as they exist on that host. One list serves every machine: `["/Users", "~"]` governs `/Users` on a managed Mac and the signed-in user's home on a Linux host. A folder that names nothing real on a given machine simply allows nothing there.

    | Field               | Type      | Default | Description                                                                                                                                                                  |
    | ------------------- | --------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | `path`              | `string`  | —       | Absolute folder path. May start with \~ or one of the listed %VAR% tokens, expanded per user. Subfolders are included.                                                       |
    | `isDefaultSelected` | `boolean` | —       | Shows as a folder chip on the new-task page and skips the trust prompt. Users can remove it.                                                                                 |
    | `mode`              | `enum`    | —       | Read-only folders can be viewed and searched but not modified in Cowork. In Code, applies to file tools only; Bash and SSH do not yet enforce read-only. One of: `rw`, `ro`. |
  </Accordion>

  <Accordion title="coworkEgressAllowedHosts details">
    Applies to **both** Cowork and Code. In Cowork it governs the sandbox's web fetch, shell commands, and package installs. In Code sessions it is [translated into Claude Code's network sandbox allowlist](https://claude.com/docs/third-party/claude-desktop/code#applied-as-managed-policy); a separately deployed Claude Code managed-settings file on the endpoint takes precedence by default.

    Does **not** apply to Web Search, which runs server-side at your inference provider rather than from the sandbox.

    Only affects **tool calls**. Inference and MCP traffic are covered by their own allowlists elsewhere. When unset, only the inference endpoint is reachable from the sandbox; the agent's package installs (pip/npm) and web fetches will fail with a 403.

    Accepts exact hostnames (`api.github.com`), wildcards (`*.corp.com` matches subdomains at any depth — `docs.corp.com` and `a.b.corp.com` both match), and `*` to allow all. `*.corp.com` does not match `corp.com` itself; add both if you need the apex. IP addresses only match when listed exactly — wildcards never match IP addresses, so an unlisted IP destination is blocked. `localhost` and private-network addresses are blocked in the sandbox's web fetch regardless of this list; shell commands and package installs run inside a network sandbox that can only reach hosts on this list (plus your inference provider's endpoints). With `*`, the network sandbox is disabled and web fetch still blocks private addresses.

    Any entry except bare `*` may carry a `:port` suffix (`internal.corp.com:8443`, `*.corp.com:8443`) restricting that entry to the named port; an entry with no port allows any port. A port on a wildcard applies to every matched subdomain. IPv6 literals are not supported. Entries outside this grammar are dropped individually, with a warning naming the entry in the app log; the remaining valid entries keep working. Port restrictions are enforced for the Cowork sandbox's web fetch and for its shell and package-install egress. Plugin CLIs additionally keep their own stricter in-VM filter and treat port-scoped entries as absent for now. In Code sessions, the Claude Code translation treats a port-restricted entry as its bare host (any port). The `:port` syntax requires the Claude Desktop release it first shipped in or newer — hold off deploying port-scoped entries until your whole fleet is on that build (note `disableAutoUpdates` pins builds); on older builds a port-scoped entry invalidates the sandbox's whole shell and package-install allowlist for the session (the older sandbox runtime rejects the entire list), and web fetch simply never matches it.

    Hosts you add here also need to be open on your network firewall, on the listed ports. See **Egress Requirements** for the full allowlist.
  </Accordion>
</AccordionGroup>

## Connectors

| Setting                                                                 | Type     | Availability    | Default | Description                                                                                                                                 |
| ----------------------------------------------------------------------- | -------- | --------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| <span id="claudeaiimport" />Claude.ai data import<br />`claudeAiImport` | `object` | MDM + Bootstrap | —       | Lets users import Claude.ai chats and projects, plus earlier Claude sessions on this computer, into this deployment when `enabled` is true. |

<AccordionGroup>
  <Accordion title="claudeAiImport details">
    | Field            | Type      | Default | Description                                                                                                                                                                                    |
    | ---------------- | --------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | `enabled`        | `boolean` | `false` | Lets users import a Claude.ai data export and earlier Claude sessions on this computer from Settings → Import. Doesn’t affect a provisioned sign-in import.                                    |
    | `exportEnabled`  | `boolean` | `false` | Lets users export this computer’s chats, Cowork tasks, and Code sessions as a zip another install can import. No effect unless `enabled` is true.                                              |
    | `bannerBehavior` | `enum`    | —       | Prompt to import at the top of a new chat or task. `detect`: only when earlier Claude sessions are found on this computer. `show`: always. Hidden when unset. One of: `off`, `detect`, `show`. |
  </Accordion>
</AccordionGroup>

### Authentication

| Setting                                                                                         | Type   | Availability    | Default | Description                                                                                                                                                                   |
| ----------------------------------------------------------------------------------------------- | ------ | --------------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <span id="microsoftauthbroker" />Microsoft 365 native sign-in broker<br />`microsoftAuthBroker` | `enum` | MDM + Bootstrap | `auto`  | Set to “disabled” to force browser-based Microsoft 365 sign-in instead of the native Company Portal / Windows account broker. One of: `auto`, `disabled`. Defaults to `auto`. |

### Extensions

| Setting                                                                                                               | Type      | Availability    | Default | Description                                                                                                                           |
| --------------------------------------------------------------------------------------------------------------------- | --------- | --------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| <span id="isdesktopextensionenabled" />Allow desktop extensions<br />`isDesktopExtensionEnabled`                      | `boolean` | MDM + Bootstrap | `false` | .dxt and .mcpb installs. Defaults to `false`. Previously named `isDxtEnabled`.                                                        |
| <span id="isdesktopextensionsignaturerequired" />Require signed extensions<br />`isDesktopExtensionSignatureRequired` | `boolean` | MDM + Bootstrap | `false` | Reject desktop extensions that are not signed by a trusted publisher. Defaults to `false`. Previously named `isDxtSignatureRequired`. |

<AccordionGroup>
  <Accordion title="isDesktopExtensionEnabled details">
    1P builds default to enabled at runtime unless this is explicitly set. In 3P, enabling this allows loading extensions; local install additionally requires an org policy backend.
  </Accordion>
</AccordionGroup>

### MCP

| Setting                                                                                                             | Type       | Availability    | Default | Description                                                                                                                                             |
| ------------------------------------------------------------------------------------------------------------------- | ---------- | --------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <span id="managedmcpservers" />Managed MCP servers<br />`managedMcpServers`                                         | `object[]` | MDM + Bootstrap | —       | Org-pushed MCP servers: remote (HTTP/SSE) or local (stdio command). May embed bearer tokens.                                                            |
| <span id="mcppersistentalwaysallowenabled" />Allow persistent tool approvals<br />`mcpPersistentAlwaysAllowEnabled` | `boolean`  | MDM + Bootstrap | `true`  | Offer the persistent “Always allow” approval options for MCP tools. Disable to keep tool approvals per-call or session-scoped only. Defaults to `true`. |
| <span id="islocaldevmcpenabled" />Allow user-added MCP servers<br />`isLocalDevMcpEnabled`                          | `boolean`  | MDM + Bootstrap | `true`  | Local stdio servers added via the Developer settings. Remote servers come from the managed list above or organization plugins. Defaults to `true`.      |

<AccordionGroup>
  <Accordion title="managedMcpServers details">
    For OAuth-authenticated entries, the app builds the redirect URI as `http://<callbackHost>:<callbackPort>/callback`; register that exact value with the OAuth provider. Tokens refresh automatically during a session, so users aren't interrupted when the initial access token expires.

    `toolPolicy` locks the per-tool approval state, keyed by tool name. Keys may contain `*` wildcards (`"read_*"` matches every tool whose name starts with `read_`; matching is anchored and `*` is the only wildcard, identical to Claude Code permission-rule globs). An exact-name key wins over matching wildcard keys, with two exceptions in the stricter direction: in Code sessions, a forwarded `ask` wildcard rule, or a `blocked` wildcard other than the bare `"*"`, takes precedence over a less strict exact key (the deny-by-default form, `"*": "blocked"` plus exact `"allow"` entries, is honored in Code sessions too), and in chat approval flows and always-allow persistence a wildcard `ask` key keeps every matching tool behind a per-call prompt (no persistent always-allow), even when a more permissive exact-name key matches — for direct (imperative) tool invocations such as artifact or widget tool calls, the exact-name key still decides. When several wildcard keys match a tool, the strictest applies (blocked > ask > allow). `"blocked"` removes the tool from the session and labels it admin-blocked. `"ask"` requires approval on every call (Allow once / Deny only; no persistent always-allow). `"ask-session"` is accepted for compatibility and behaves exactly as `"ask"`. `"allow"` pre-approves. Tools **not listed** follow the user's choice: the prompt offers a persistent Always allow, except for tools that can modify data, which instead show a session-scoped **Allow for this task** alongside **Allow for all tasks** with a malicious-instruction warning. In Code sessions, `blocked` and `ask` (including `ask-session`) are forwarded as Claude Code permission rules; `allow` is not.

    For the bundled Microsoft 365 connector, the send tools (`outlook_send_mail`, `outlook_send_draft`, `outlook_forward_mail`, `outlook_create_event`, `outlook_update_event`, `teams_send_chat_message`, `teams_send_channel_message`, `teams_reply_channel_message`) cannot be loosened below `ask` — an `allow` setting resolves to `ask`.

    | Field                                   | Type       | Default | Description                                                                                                                                                                                             |
    | --------------------------------------- | ---------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | `name`                                  | `string`   | —       | Unique name for this server. Shown to users and used to key tool policy and sign-in state.                                                                                                              |
    | `server`                                | `string`   | —       | Which bundled connector this entry turns on. Set instead of a transport; each built-in server has its own fields. One of: `microsoft365`, `websearch`, `github`.                                        |
    | `tenantId`                              | `string`   | —       | Your organization’s Microsoft Entra directory (tenant) ID.                                                                                                                                              |
    | `clientId`                              | `string`   | —       | OAuth app client ID for this built-in server.                                                                                                                                                           |
    | `azureCloud`                            | `enum`     | —       | Microsoft cloud for sign-in and Graph. Leave as global for commercial Microsoft 365; US Government clouds require your own app registration (Client ID). One of: `global`, `us-gov-high`, `us-gov-dod`. |
    | `scope`                                 | `string`   | —       | What the server may request at sign-in. If blank, Desktop’s default read set is used.                                                                                                                   |
    | `toolPolicy`                            | `object`   | —       | Lock the approval state for specific tools. Unlisted tools stay user-controlled.                                                                                                                        |
    | `headers`                               | `object`   | —       | Static headers sent on every request — routing and tenant headers only. No credentials here; use the headers helper script for tokens and rotating values.                                              |
    | `headersHelper`                         | `string`   | —       | Script that prints the auth header as a JSON object to stdout. Runs before each request (cached for the TTL below).                                                                                     |
    | `headersHelperTtlSec`                   | `integer`  | —       | How long the helper’s headers are reused before it runs again, in seconds. Defaults to 300.                                                                                                             |
    | `headersHelperRefreshBufferSec`         | `integer`  | —       | Seconds before the TTL expires at which the helper re-runs mid-session. Defaults to 60. Keep it larger than the helper’s typical runtime.                                                               |
    | `provider`                              | `enum`     | —       | Runs search from the desktop, for inference providers without native web search. Supply the provider’s API key through the headers helper script below. One of: `brave`, `tavily`, `exa`, `custom`.     |
    | `customUrl`                             | `string`   | —       | POST endpoint accepting \{q} JSON and returning a results\[] array. Only used when provider is Custom.                                                                                                  |
    | `host`                                  | `string`   | —       | Leave blank for github.com. For GitHub Enterprise Server, your instance’s base URL.                                                                                                                     |
    | `toolsets`                              | `string`   | —       | Comma-separated github-mcp-server toolsets to enable. If blank, the bundled server’s default toolsets are used.                                                                                         |
    | `readOnly`                              | `boolean`  | —       | Offer only read tools — the server registers no write tools at all.                                                                                                                                     |
    | `transport`                             | `enum`     | —       | How the app connects: Streamable HTTP or legacy SSE for remote servers, or a local command over stdio. One of: `http`, `sse`, `stdio`.                                                                  |
    | `url`                                   | `string`   | —       | HTTPS endpoint of the remote MCP server.                                                                                                                                                                |
    | `oauth`                                 | `object`   | —       | OAuth for a remote server: true to auto-register a client, a pre-registered client ID with tenant and scope, or mode “hosted” for an Anthropic-signed identity.                                         |
    | `oauth.clientId`                        | `string`   | —       | OAuth client ID from your IdP app registration. Leave unset to auto-register (dynamic client registration) and only narrow scopes.                                                                      |
    | `oauth.clientSecret`                    | `string`   | —       | Only for IdPs whose token endpoint requires a client secret (e.g. Box). Leave blank for PKCE-only public clients.                                                                                       |
    | `oauth.clientSecretHelper`              | `string`   | —       | Executable that prints the client secret on stdout. Overrides the inline value.                                                                                                                         |
    | `oauth.authorizationServer`             | `string[]` | —       | Issuer URLs the OAuth sign-in may use, as a JSON array. Pre-filled by presets; ask your IdP admin if unsure.                                                                                            |
    | `oauth.authorizationUrl`                | `string`   | —       | Only for IdPs that don’t serve a .well-known discovery document. Set together with Token URL; requires Client ID.                                                                                       |
    | `oauth.tokenUrl`                        | `string`   | —       | Only for IdPs that don’t serve a .well-known discovery document. Set together with Authorization URL; requires Client ID.                                                                               |
    | `oauth.tenantId`                        | `string`   | —       | Required for single-tenant Entra apps. Leave blank for multi-tenant or non-Microsoft IdPs.                                                                                                              |
    | `oauth.authFlow`                        | `enum`     | —       | How Entra sign-in runs for this server: the system browser (default) or the OS identity broker. One of: `browser`, `broker`.                                                                            |
    | `oauth.scope`                           | `string`   | —       | Space-separated scopes sent on the authorize request. Leave unset to use the scopes the server advertises. Required when Tenant ID is set.                                                              |
    | `oauth.appendOfflineAccess`             | `boolean`  | —       | Adds offline\_access to the authorize request so the IdP returns a refresh token for silent renewal.                                                                                                    |
    | `oauth.callbackHost`                    | `enum`     | —       | Use localhost only if your IdP’s registered redirect URI specifies it. One of: `127.0.0.1`, `localhost`.                                                                                                |
    | `oauth.callbackPort`                    | `integer`  | —       | Only set if your IdP requires an exact-match redirect port. Entra accepts any.                                                                                                                          |
    | `oauth.additionalRedirectReferrerHosts` | `string`   | —       | Space-separated hostnames also accepted as the referrer of the sign-in callback. Only needed when the IdP completes sign-in from a different host.                                                      |
    | `command`                               | `string`   | —       | Absolute path to the server executable, run on the user’s machine.                                                                                                                                      |
    | `args`                                  | `string[]` | —       | Arguments passed to the command, one per entry.                                                                                                                                                         |
    | `env`                                   | `object`   | —       | Environment variables set for the command.                                                                                                                                                              |
    | `envHelper`                             | `string`   | —       | Script that prints environment variables as a JSON object to stdout. Runs when the local server starts (cached for the TTL below).                                                                      |
    | `envHelperTtlSec`                       | `integer`  | `300`   | Maximum age of a cached helper result, in seconds (default 300). Applies when the server starts or restarts.                                                                                            |
    | `startupTimeoutSec`                     | `integer`  | `120`   | Maximum wait in seconds for the server to start and list its tools.                                                                                                                                     |
  </Accordion>

  <Accordion title="mcpPersistentAlwaysAllowEnabled details">
    When enabled (the default), approval prompts for tools without a `toolPolicy` entry offer a persistent grant — **Always allow**, or **Allow for all tasks** for tools that can modify data — the Tool permissions picker in Connector settings lets users pre-approve tools, and those grants persist across sessions with no expiry.

    When disabled, the persistent options are hidden from approval prompts and from the Connector settings picker, previously stored persistent grants stop being honored, and scheduled-task runs no longer record or replay cross-run tool approvals. Session-scoped approvals are unchanged: users can still approve each call, and tools that can modify data keep the session-scoped **Allow for this task** option.

    A per-tool `toolPolicy` entry on `managedMcpServers` always takes precedence over this key: `blocked`, `ask`, `ask-session`, and `allow` behave exactly as documented there whether this key is enabled or not.

    This key governs the chat and Cowork surfaces. Code sessions use a separate permission path this key does not cover — govern Code tool approvals with per-tool `toolPolicy` entries, whose `blocked` and `ask` values are forwarded there.
  </Accordion>
</AccordionGroup>

## Telemetry & updates

| Setting                                                                                                    | Type      | Availability    | Default | Description                                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------- | --------- | --------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| <span id="deploymentorganizationuuid" />Organization UUID<br />`deploymentOrganizationUuid`                | `string`  | MDM + Bootstrap | —       | A UUID you generate. Tags telemetry so Anthropic support can locate your fleet’s events, and namespaces each user’s local data. Not used for auth. |
| <span id="disableessentialtelemetry" />Block essential telemetry<br />`disableEssentialTelemetry`          | `boolean` | MDM + Bootstrap | `false` | Crash and performance reports to Anthropic. Defaults to `false`.                                                                                   |
| <span id="disablenonessentialtelemetry" />Block nonessential telemetry<br />`disableNonessentialTelemetry` | `boolean` | MDM + Bootstrap | `false` | Product-usage analytics and diagnostic-report uploads. No message content. Defaults to `false`.                                                    |
| <span id="disablenonessentialservices" />Block nonessential services<br />`disableNonessentialServices`    | `boolean` | MDM + Bootstrap | `false` | Connector favicons and the artifact-preview and MCP Apps widget iframe origins. Artifacts will not render. Defaults to `false`.                    |

<AccordionGroup>
  <Accordion title="deploymentOrganizationUuid details">
    If unset, a shared placeholder UUID is used: telemetry can’t be distinguished from other unconfigured deployments, and local data is stored under the placeholder. **Changing this value orphans data** stored under the previous value (sessions, skills, plugins).
  </Accordion>

  <Accordion title="disableEssentialTelemetry details">
    "Essential" means the signals Anthropic needs to keep your deployment working: **crash stacks**, **startup failure reasons**, and **version/OS metadata**. No prompts, completions, file contents, or identifiers beyond a random install ID.

    **What you lose when this is on:** when a Cowork build hits a bug that only reproduces on your OS version or locale, Anthropic can't see it unless a user manually reports. Fixes ship slower.

    **Why this is discouraged, not blocked:** some air-gapped environments require zero outbound telemetry as a matter of policy. The switch exists for them. If you don't have that constraint, leave it off.
  </Accordion>

  <Accordion title="disableNonessentialTelemetry details">
    "Nonessential" covers two things: **product-usage analytics** (which features get used, navigation patterns; no prompts or completions) and the **Send** action in Help → Generate Diagnostic Report. Turning this on stops both.

    Destinations are listed under Egress Requirements → Nonessential telemetry.
  </Accordion>

  <Accordion title="disableNonessentialServices details">
    "Nonessential services" covers three outbound fetches the app runs without: **connector favicons** (the icon proxy), the **artifact-preview** iframe origin, and the **MCP Apps widget** iframe origin (`*.claudemcpcontent.com`). Turning this on blocks all three.

    **What you lose when this is on:** connectors show without icons, artifacts do not render in conversations, and connectors that return MCP Apps show the text tool result instead of the widget.

    Destinations are listed under Egress Requirements → Nonessential services.
  </Accordion>
</AccordionGroup>

### Auto update

| Setting                                                                                                    | Type      | Availability    | Default | Description                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------- | --------- | --------------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| <span id="disableautoupdates" />Block auto-updates<br />`disableAutoUpdates`                               | `boolean` | MDM + Bootstrap | `false` | Stop Cowork from fetching updates entirely (no time limit). You’ll need to push new versions yourself. Defaults to `false`.        |
| <span id="autoupdaterenforcementhours" />Auto-update enforcement window<br />`autoUpdaterEnforcementHours` | `integer` | MDM + Bootstrap | —       | Hours before a downloaded update force-installs. Only applies when auto-updates are enabled. Blank = 72-hour default. Range: 1–72. |
| <span id="updateviaupdateshost" />Check for updates on releases.claude.com<br />`updateViaUpdatesHost`     | `boolean` | MDM + Bootstrap | `false` | Read the update feed from releases.claude.com so api.anthropic.com can stay blocked. Defaults to `false`.                          |

<AccordionGroup>
  <Accordion title="autoUpdaterEnforcementHours details">
    Has no effect when `disableAutoUpdates` is in place at launch: the updater never starts, so nothing is downloaded and this timer never arms. If the policy reaches an already-running app after an update has downloaded, that one staged update still installs on this timer; no further updates are fetched.

    Leaving it blank uses the 72-hour default *and* then waits for the machine to be idle (10+ minutes without input) before restarting; setting any explicit value (including 72) restarts once the window elapses regardless of user activity. In both cases the restart holds off while Claude is mid-task.
  </Accordion>

  <Accordion title="updateViaUpdatesHost details">
    By default the app asks `api.anthropic.com` which version to install. That host also serves the model APIs, so organizations that block un-approved LLM endpoints at the network edge end up blocking updates too.

    Turn this on to read the same feed from `releases.claude.com`, a hostname that serves only the desktop update-check route and carries no model API. `api.anthropic.com` can then stay blocked without breaking auto-update. Rollout behavior is unchanged; the installer download still comes from `downloads.claude.ai` as before.
  </Accordion>
</AccordionGroup>

### OTLP

| Setting                                                                                             | Type      | Availability    | Default         | Description                                                                                                                                                                                                         |
| --------------------------------------------------------------------------------------------------- | --------- | --------------- | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <span id="otlpendpoint" />OpenTelemetry collector endpoint<br />`otlpEndpoint`                      | `string`  | MDM + Bootstrap | —               | Where Cowork sends OpenTelemetry logs and metrics. Leave blank to disable.                                                                                                                                          |
| <span id="otlpprotocol" />OpenTelemetry exporter protocol<br />`otlpProtocol`                       | `enum`    | MDM + Bootstrap | `http/protobuf` | grpc or http/protobuf. One of: `http/protobuf`, `http/json`, `grpc`. Defaults to `http/protobuf`.                                                                                                                   |
| <span id="otlpheaders" />OpenTelemetry exporter headers<br />`otlpHeaders`                          | `object`  | MDM + Bootstrap | —               | Static collector headers — routing and tenant headers only. No credentials here; use Collector authentication or the headers helper script for tokens.                                                              |
| <span id="otlpauthmode" />Collector authentication<br />`otlpAuthMode`                              | `enum`    | MDM + Bootstrap | —               | inference-credential sends the user’s inference bearer token to the collector as Authorization: Bearer. One of: `none`, `inference-credential`.                                                                     |
| <span id="otlpheadershelper" />OpenTelemetry headers helper script<br />`otlpHeadersHelper`         | `string`  | MDM + Bootstrap | —               | Absolute path to an executable that prints a JSON object of collector headers. Merged over the static headers and Collector authentication; the helper wins.                                                        |
| <span id="otlpresourceattributes" />OpenTelemetry resource attributes<br />`otlpResourceAttributes` | `object`  | MDM + Bootstrap | —               | Extra resource attributes to attach to every span/metric. A static enduser.id set here always wins over the runtime identity.                                                                                       |
| <span id="otlpdesktoploglevel" />Desktop telemetry export level<br />`otlpDesktopLogLevel`          | `enum`    | MDM + Bootstrap | `error`         | Controls the Claude Desktop application’s events, separate from Cowork and Code sessions. Defaults to error. One of: `off`, `error`, `warn`, `info`, `debug`. Defaults to `error`.                                  |
| <span id="otlpcontentcapture" />Content capture categories<br />`otlpContentCapture`                | `enum[]`  | MDM + Bootstrap | —               | Content categories the desktop exporter sends unredacted to your collector. Leave empty to redact all content (default). One of: `userPrompts`, `assistantResponses`, `toolDetails`, `toolContent`, `rawApiBodies`. |
| <span id="otlptracesenabled" />Export traces (beta)<br />`otlpTracesEnabled`                        | `boolean` | MDM + Bootstrap | —               | Also export OpenTelemetry traces from Cowork tasks and Code sessions. Uses Claude Code’s session-tracing beta.                                                                                                      |

<AccordionGroup>
  <Accordion title="otlpAuthMode details">
    `inference-credential` adds `Authorization: Bearer <token>` to every export, using the token the app currently holds for the inference provider, with no helper script to deploy. The collector must accept that token as issued: a gateway OIDC token carries the gateway’s audience, Microsoft Entra on Foundry issues the Foundry resource’s token, and Vertex workforce identity forwards a Google Cloud access token; static gateway and Bedrock keys are forwarded as-is. Because the token can also call inference as the user, use this only for a collector you operate; for anything else, use the headers helper script with an ingest-scoped credential. Kinds that never produce a bearer (AWS SigV4 kinds on Bedrock, Google ADC / OAuth files on Vertex, API-key kinds) export without it — use the helper script instead. Cowork tasks pick up the current token each time they start; a Code session keeps the token it started with for as long as it stays open; the desktop’s own event exporter uses the current token on every flush. Before sign-in, exports go out unauthenticated. An `Authorization` header printed by the headers helper script wins over this.
  </Accordion>

  <Accordion title="otlpHeadersHelper details">
    Absolute path to an executable that prints a single JSON object of HTTP headers on stdout, e.g. `{"Authorization": "Bearer …"}`. The desktop runs it (no arguments; output cached for a few minutes, and a failure is not retried for 30 seconds) whenever it needs collector headers and merges the result over **OpenTelemetry exporter headers** and the **Collector authentication** header (the helper wins on conflict). Cowork tasks get the current output when they start; Code sessions and host-run Cowork sessions are also given the script as Claude Code’s own `otelHeadersHelper`, so an open session re-runs it as tokens rotate (on Windows this applies to `.exe`, `.cmd` and `.bat` helpers; a `.ps1` helper applies at session start only); the desktop’s own event exporter re-runs it per flush. Session start waits at most two seconds for a slow helper and otherwise proceeds without its headers until it finishes. Use this when the collector needs a credential the inference sign-in cannot provide, when the collector token rotates, or when the config comes from a hosted admin console, which cannot store header values. If the helper fails, telemetry is sent without its headers — check the app log.
  </Accordion>

  <Accordion title="otlpResourceAttributes details">
    Extra resource attributes to attach to every span, metric, and log sent to your collector. When End-user attribution is on and no `enduser.id` is set here, the desktop fills it with the signed-in user's runtime identity; a value you set here always wins. `process.owner` (the OS login name) is always emitted; set it here to override.
  </Accordion>

  <Accordion title="otlpContentCapture details">
    Each category enables a class of raw content in OpenTelemetry events sent to your collector (this data never reaches Anthropic):

    * `userPrompts` — user-typed prompt text
    * `assistantResponses` — assistant message text
    * `toolDetails` — tool input arguments, e.g. the web-search query string
    * `toolContent` — tool output content, e.g. fetched page text or command stdout
    * `rawApiBodies` — full inference API request and response bodies

    These mirror Claude Code's `OTEL_LOG_*` env vars; see the [Claude Code monitoring docs](https://code.claude.com/docs/en/monitoring-usage).
  </Accordion>

  <Accordion title="otlpTracesEnabled details">
    Enables Claude Code's session-tracing beta (`CLAUDE_CODE_ENHANCED_TELEMETRY_BETA=1` + `OTEL_TRACES_EXPORTER=otlp`) in spawned Cowork tasks and Code sessions. Each user interaction exports a trace whose spans and events carry `trace_id`/`span_id`, enabling end-to-end correlation in your observability backend (metrics do not carry trace context; correlate those via `session.id`). Traces go to the collector endpoint and protocol configured above. While the Claude Code feature is in beta the span structure may evolve; see the [Claude Code monitoring docs](https://code.claude.com/docs/en/monitoring-usage).
  </Accordion>
</AccordionGroup>

## Limits

### Token limits

| Setting                                                                                           | Type      | Availability    | Default | Description                                                                                  |
| ------------------------------------------------------------------------------------------------- | --------- | --------------- | ------- | -------------------------------------------------------------------------------------------- |
| <span id="inferencemaxtokensperwindow" />Max tokens per window<br />`inferenceMaxTokensPerWindow` | `integer` | MDM + Bootstrap | —       | Per-user soft cap, counted client-side over the duration below. Not a server-enforced quota. |
| <span id="inferencetokenwindowhours" />Token cap window<br />`inferenceTokenWindowHours`          | `integer` | MDM + Bootstrap | —       | Tumbling window length for the token cap. Max 720 hours (30 days). Range: 1–720.             |

<AccordionGroup>
  <Accordion title="inferenceMaxTokensPerWindow details">
    Requires `inferenceTokenWindowHours` to also be set — without a window length the cap is inert and no limit is enforced.
  </Accordion>

  <Accordion title="inferenceTokenWindowHours details">
    Required when `inferenceMaxTokensPerWindow` is set — the cap only takes effect once both are configured.
  </Accordion>
</AccordionGroup>

## Appearance

| Setting                                                                                             | Type      | Availability    | Default | Description                                                                                                                                                                                  |
| --------------------------------------------------------------------------------------------------- | --------- | --------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <span id="enduserattribution" />End-user attribution<br />`endUserAttribution`                      | `boolean` | MDM + Bootstrap | —       | Show the signed-in user’s identity-provider identity in the sidebar and account menu, and emit it as the OpenTelemetry enduser.id resource attribute. Previously named `enduserAttribution`. |
| <span id="deploymentdisplayname" />Deployment display name<br />`deploymentDisplayName`             | `string`  | MDM + Bootstrap | —       | Overrides the provider label shown in the sidebar footer, user-menu header, and connection-error banner.                                                                                     |
| <span id="deploymentdisplaysubtitle" />Deployment display subtitle<br />`deploymentDisplaySubtitle` | `string`  | MDM + Bootstrap | —       | Optional detail shown after the deployment display name in the account-menu header.                                                                                                          |
| <span id="banner" />Organization banner<br />`banner`                                               | `object`  | MDM + Bootstrap | —       | A persistent banner across the top of the app window after sign-in.                                                                                                                          |

<AccordionGroup>
  <Accordion title="endUserAttribution details">
    When on (default), the app resolves the signed-in user's identity from the configured credential source (the identity provider claim, or the OS login name when no claim is available) and shows it in the sidebar footer, the account menu, and the Code session greeting. If an OpenTelemetry collector is configured, the same identity is also emitted as the `enduser.id` resource attribute on every span, metric, and log sent to your collector — unless you have set a static `enduser.id` under OpenTelemetry resource attributes, in which case your static value is kept and the runtime identity is not emitted. When off, no identity is shown in the app and no runtime `enduser.id` is emitted; a static `enduser.id` under OpenTelemetry resource attributes still passes through unchanged. This setting does not gate the `process.owner` resource attribute (the OS login name), which is standard OpenTelemetry process metadata and is always emitted — set a static `process.owner` under OpenTelemetry resource attributes to override it. Applies to both Cowork tasks and Code sessions.
  </Accordion>

  <Accordion title="deploymentDisplayName details">
    Set this to the name users should see for this deployment (for example, "Claude for Government"). When unset, the desktop shows the default provider label. Maximum 60 characters.
  </Accordion>

  <Accordion title="deploymentDisplaySubtitle details">
    Optional detail shown after the deployment display name in the account-menu header (for example, "Claude for Veterans Affairs · Claude for Government"). Shown only when the display name is also set. Maximum 60 characters.
  </Accordion>

  <Accordion title="banner details">
    Use this for compliance notices, an internal-support link, or to identify the deployment. The banner is shown on every page after sign-in and cannot be dismissed by the user. Colors are six-digit hex (`#RRGGBB`); when `linkUrl` is set the banner text becomes an HTTPS link.

    | Field             | Type      | Default   | Description                                                                    |
    | ----------------- | --------- | --------- | ------------------------------------------------------------------------------ |
    | `enabled`         | `boolean` | —         | Turns the banner on. When false or unset, the other banner fields are ignored. |
    | `text`            | `string`  | —         | Single line, truncated on overflow. Maximum 200 characters.                    |
    | `backgroundColor` | `string`  | `#F5F5F5` | Six-digit hex (#RRGGBB). Applied exactly as configured; not theme-adapted.     |
    | `textColor`       | `string`  | `#000000` | Six-digit hex (#RRGGBB). Applied exactly as configured; not theme-adapted.     |
    | `linkUrl`         | `string`  | —         | Optional HTTPS URL. The banner text becomes a link when set.                   |
  </Accordion>
</AccordionGroup>

### Feature discovery

| Setting                                                                                        | Type      | Availability    | Default | Description                                                                                                                                                               |
| ---------------------------------------------------------------------------------------------- | --------- | --------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <span id="disablefeaturediscovery" />Hide feature announcements<br />`disableFeatureDiscovery` | `boolean` | MDM + Bootstrap | `false` | Suppress unprompted feature-announcement UI: the post-update “What’s new” nudge and new-feature tips. Users can still open release notes themselves. Defaults to `false`. |

<AccordionGroup>
  <Accordion title="disableFeatureDiscovery details">
    Covers the version-shipped announcement UI baked into each release: the **What's new** button that appears on its own after an update, and the one-time **New feature** tips (coach-marks) that point out newly shipped capabilities. Useful when your organization gates feature availability and doesn't want the app advertising capabilities you haven't rolled out.

    User-initiated surfaces stay: the What's-new menu item and header button still open the release notes on demand. Auto-update behavior is unaffected — that is governed by `disableAutoUpdates` and `autoUpdaterEnforcementHours`.
  </Accordion>
</AccordionGroup>

## Plugins

| Setting                                                                                     | Type       | Availability           | Default | Description                                                                                                                                                   |
| ------------------------------------------------------------------------------------------- | ---------- | ---------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <span id="orgpluginsettings" />Organization plugin settings<br />`orgPluginSettings`        | `object[]` | MDM + Bootstrap        | —       | Admin policy applied to plugin-delivered MCP servers.                                                                                                         |
| <span id="allowedpluginmarketplaces" />Plugin marketplaces<br />`allowedPluginMarketplaces` | `object[]` | MDM + Bootstrap · Beta | —       | Git repositories or hosted marketplace.json URLs to surface as plugin marketplaces in the Directory’s Organization tab. The app re-fetches each periodically. |

<AccordionGroup>
  <Accordion title="orgPluginSettings details">
    Applies `toolPolicy` locks to MCP servers that arrive via the org-plugins directory, keyed by server name. Either shape is accepted; when hand-authoring a profile, use the legacy record shape until your fleet floor parses the canonical array form:

    ```json theme={null}
    {"mcpServers": {"internal-search": {"toolPolicy": {"delete_document": "blocked"}}}}
    ```

    If a Managed MCP servers entry and an org-plugin server share a name, the Managed MCP servers entry wins and its `toolPolicy` (if any) applies; the entry here for that name is ignored.

    | Field              | Type       | Default | Description                                                                                                                 |
    | ------------------ | ---------- | ------- | --------------------------------------------------------------------------------------------------------------------------- |
    | `serverName`       | `string`   | —       | Name of the plugin-delivered MCP server this policy applies to.                                                             |
    | `tools`            | `object[]` | —       | Per-tool approval locks for this server.                                                                                    |
    | `tools.toolName`   | `string`   | —       | MCP tool name as the server reports it.                                                                                     |
    | `tools.permission` | `enum`     | —       | Approval state locked for this tool. Unlisted tools stay user-controlled. One of: `allow`, `ask`, `ask-session`, `blocked`. |
  </Accordion>

  <Accordion title="allowedPluginMarketplaces details">
    | Field                    | Type     | Default | Description                                                                                                                                                                                                                       |
    | ------------------------ | -------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | `source`                 | `string` | —       | Where the marketplace is fetched from: a GitHub repository (set repo), any Git remote (set url), or a hosted marketplace.json file (set url). One of: `github`, `git`, `url`.                                                     |
    | `repo`                   | `string` | —       | GitHub repository in owner/repo form. Case-insensitive.                                                                                                                                                                           |
    | `ref`                    | `string` | —       | Commit SHA, branch, or tag. Leave empty to track the default branch.                                                                                                                                                              |
    | `path`                   | `string` | —       | Folder within the repository that contains the marketplace, when it isn’t at the root.                                                                                                                                            |
    | `expectedName`           | `string` | —       | Rejects the marketplace if its manifest name differs.                                                                                                                                                                             |
    | `installationPreference` | `enum`   | —       | Whether users install plugins themselves or get them automatically. One of: `available`, `auto_install`, `required`.                                                                                                              |
    | `credentialKind`         | `enum`   | —       | How fetches authenticate: anonymously, with the user’s git credentials, via a helper executable, or as inference does (url sources the gateway hosts). One of: `anonymous`, `userGit`, `credentialHelper`, `inferenceCredential`. |
    | `credentialHelper`       | `string` | —       | Executable that prints an access token for this marketplace.                                                                                                                                                                      |
    | `url`                    | `string` | —       | HTTPS Git remote of the marketplace repository (git), or direct HTTPS URL of a hosted marketplace.json file (url).                                                                                                                |
    | `manifestSha256`         | `string` | —       | SHA-256 of the exact marketplace.json to accept. Required when Installation is auto\_install or required; a served manifest with any other digest is refused.                                                                     |
  </Accordion>
</AccordionGroup>

## Source

### Bootstrap

| Setting                                                                                              | Type      | Availability | Default | Description                                                                                                                                                                                               |
| ---------------------------------------------------------------------------------------------------- | --------- | ------------ | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <span id="bootstrapenabled" />Use bootstrap config<br />`bootstrapEnabled`                           | `boolean` | MDM only     | `true`  | Fetch and apply the URL above at launch. Turn off to keep the URL saved but skip the fetch. Defaults to `true`.                                                                                           |
| <span id="bootstrapurl" />Bootstrap config URL<br />`bootstrapUrl`                                   | `string`  | MDM only     | —       | HTTPS endpoint that returns a per-user JSON config overlay. Values from the response override local settings and become read-only.                                                                        |
| <span id="bootstrapoidc" />Bootstrap OIDC parameters<br />`bootstrapOidc`                            | `object`  | MDM only     | —       | When set, the bootstrap request sends a Bearer token from a browser sign-in (authorization-code-with-PKCE).                                                                                               |
| <span id="bootstrapheaders" />Bootstrap request headers<br />`bootstrapHeaders`                      | `object`  | MDM only     | —       | HTTP headers sent on every bootstrap config fetch. Use this instead of embedding user:pass@ in the URL.                                                                                                   |
| <span id="bootstrapheadershelper" />Bootstrap headers helper script<br />`bootstrapHeadersHelper`    | `string`  | MDM only     | —       | Absolute path to an executable that prints a JSON object of bootstrap request headers. Merged over the static headers; the helper wins.                                                                   |
| <span id="trustbootstrapdelivery" />Trust bootstrap-delivered settings<br />`trustBootstrapDelivery` | `boolean` | MDM only     | `false` | Skip the per-user consent prompt for sign-in targets, inference endpoints, helper scripts, and connectors the bootstrap server delivers. Defaults to `false`. Previously named `trustBootstrapLocalExec`. |

<AccordionGroup>
  <Accordion title="bootstrapOidc details">
    Set this to use a separate identity provider (Microsoft Entra ID, Okta, Ping, or any compliant OIDC provider) for the bootstrap sign-in. The app runs an authorization-code-with-PKCE flow in the system browser. Omit to use device-code mode against the bootstrap server's own origin.

    This is an **object-typed key** — in an MDM profile it is a single JSON-string value, not separate keys with dotted names like `bootstrapOidc.clientId`. Writing the sub-fields as separate registry values causes the app to silently fall through to device-code mode.

    | Field                             | Type      | Default | Description                                                                                                                                                |
    | --------------------------------- | --------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | `clientId`                        | `string`  | —       | OAuth client ID of the desktop app registration at your identity provider (public client, PKCE).                                                           |
    | `issuer`                          | `string`  | —       | HTTPS issuer with OIDC discovery. Set this, or set the authorization and token URLs instead.                                                               |
    | `authorizationUrl`                | `string`  | —       | HTTPS authorization endpoint. Used with the token URL when no issuer is set.                                                                               |
    | `tokenUrl`                        | `string`  | —       | HTTPS token endpoint. Used with the authorization URL when no issuer is set.                                                                               |
    | `scopes`                          | `string`  | —       | Space-separated; the token’s audience must match what your bootstrap server validates.                                                                     |
    | `redirectPort`                    | `integer` | —       | Fixed loopback port for the sign-in redirect ([http://127.0.0.1:PORT/callback](http://127.0.0.1:PORT/callback)). Leave unset to use a free port each time. |
    | `additionalRedirectReferrerHosts` | `string`  | —       | Space-separated hostnames also accepted as the referrer of the sign-in callback. Only needed when the IdP completes sign-in from a different host.         |
  </Accordion>

  <Accordion title="bootstrapHeaders details">
    Static headers sent on every request to the bootstrap config URL — for a service-account credential (`Authorization: Basic …`, an API key header) or a routing/tenant header. When either this or the headers helper script is set and no separate `bootstrapOidc` provider is configured, the app treats the headers as sufficient auth and does not require a per-user sign-in for the bootstrap fetch. Header values are masked in diagnostics and telemetry. For a rotating token, use the headers helper script instead.
  </Accordion>

  <Accordion title="bootstrapHeadersHelper details">
    Absolute path to an executable that prints a single JSON object of HTTP headers on stdout, e.g. `{"Authorization": "Bearer …"}`. The app runs it (no arguments; output cached for a few minutes) before each bootstrap config fetch and merges the result over **Bootstrap request headers** (the helper wins on conflict). Use this instead of embedding `user:pass@` in the bootstrap URL, or when the bootstrap server needs a rotating token from a secrets manager. When either this or the static headers are set and no separate `bootstrapOidc` provider is configured, the app treats them as sufficient auth and does not require a per-user sign-in for the bootstrap fetch. If a per-user sign-in also runs (`bootstrapOidc` or the server’s own device-code flow), that Bearer token wins on `Authorization`.
  </Accordion>
</AccordionGroup>

## Guides

### Recommended security profiles

The profiles below are illustrative examples rather than built-in presets, and the labels are descriptive only. Use them as starting points and adjust for your environment. Layer the inference-provider keys for your cloud on top of whichever profile you choose.

<Tabs>
  <Tab title="Standard">
    Recommended for most enterprise deployments. Telemetry and auto-updates stay on so Anthropic can diagnose issues and ship fixes; users can extend Claude Desktop with their own connectors.

    | Key                                                                           | Value              |
    | ----------------------------------------------------------------------------- | ------------------ |
    | [`deploymentOrganizationUuid`](#deploymentorganizationuuid)                   | `<your-org-uuid>`  |
    | [`autoUpdaterEnforcementHours`](#autoupdaterenforcementhours)                 | `24`               |
    | [`isDesktopExtensionSignatureRequired`](#isdesktopextensionsignaturerequired) | `true`             |
    | [`otlpEndpoint`](#otlpendpoint)                                               | `<your-collector>` |
  </Tab>

  <Tab title="Restricted">
    For regulated environments that need to control what users can connect Claude Desktop to, while keeping Anthropic supportability.

    | Key                                                             | Value                             |
    | --------------------------------------------------------------- | --------------------------------- |
    | [`deploymentOrganizationUuid`](#deploymentorganizationuuid)     | `<your-org-uuid>`                 |
    | [`disableNonessentialTelemetry`](#disablenonessentialtelemetry) | `true`                            |
    | [`disableNonessentialServices`](#disablenonessentialservices)   | `true`                            |
    | [`isLocalDevMcpEnabled`](#islocaldevmcpenabled)                 | `false`                           |
    | [`isDesktopExtensionEnabled`](#isdesktopextensionenabled)       | `false`                           |
    | [`allowedWorkspaceFolders`](#allowedworkspacefolders)           | `[{"path":"~/Documents/Claude"}]` |
    | [`coworkEgressAllowedHosts`](#coworkegressallowedhosts)         | `["*.example.corp"]`              |
    | [`otlpEndpoint`](#otlpendpoint)                                 | `<your-collector>`                |
  </Tab>

  <Tab title="Locked down">
    For air-gapped or maximally restricted environments. **The only traffic leaving the device goes to your inference endpoint and OTLP collector.** With this profile, Anthropic receives no telemetry or logs from the app and does not deliver updates, so your team owns log collection and update distribution. On Microsoft Foundry, the Claude models behind your inference endpoint run in an Anthropic-operated service, so conversation content still reaches Anthropic-operated infrastructure under this profile, as described under [Data handling by provider](/docs/third-party/claude-desktop/overview#data-handling-by-provider).

    | Key                                                             | Value                             |
    | --------------------------------------------------------------- | --------------------------------- |
    | [`disableEssentialTelemetry`](#disableessentialtelemetry)       | `true`                            |
    | [`disableNonessentialTelemetry`](#disablenonessentialtelemetry) | `true`                            |
    | [`disableNonessentialServices`](#disablenonessentialservices)   | `true`                            |
    | [`disableAutoUpdates`](#disableautoupdates)                     | `true`                            |
    | [`isLocalDevMcpEnabled`](#islocaldevmcpenabled)                 | `false`                           |
    | [`isDesktopExtensionEnabled`](#isdesktopextensionenabled)       | `false`                           |
    | [`skillCreationEnabled`](#skillcreationenabled)                 | `false`                           |
    | [`disabledBuiltinTools`](#disabledbuiltintools)                 | `["WebSearch","WebFetch"]`        |
    | [`coworkEgressAllowedHosts`](#coworkegressallowedhosts)         | `[]`                              |
    | [`allowedWorkspaceFolders`](#allowedworkspacefolders)           | `[{"path":"~/Documents/Claude"}]` |
    | [`otlpEndpoint`](#otlpendpoint)                                 | `<your-collector>`                |
  </Tab>
</Tabs>

### Tool permissions for managed MCP servers

Each [`managedMcpServers`](#managedmcpservers) entry can carry a `toolPolicy` that locks the approval state per tool:

* `"allow"` — the tool runs without prompting.
* `"ask"` — the user approves every call; no session-scoped or standing grants are offered.
* `"blocked"` — the tool is removed from Claude's session; connector settings show it as blocked by your organization.

Tools with no policy entry stay user-controlled (built-in connectors apply default policies to some tools — see the reference above): the user is prompted and can approve once, approve for the rest of the task (offered for tools that can modify data), or grant a standing approval unless [`mcpPersistentAlwaysAllowEnabled`](#mcppersistentalwaysallowenabled) is `false`. Full prompt options require version 1.22209.0 or later; earlier third-party builds offered only per-call approval. The reference above also lists an `"ask-session"` value; it is accepted for compatibility and behaves exactly as `"ask"`. Managed policies take precedence over user grants, and enforcement happens in the desktop host process, not only in the prompt UI. A deny-by-default posture — `"*": "blocked"` plus exact `"allow"` entries for approved tools — is supported, including in Code sessions (where an allowed tool still gets Claude Code's own approval prompt). See the [`managedMcpServers` reference](#managedmcpservers) for wildcard matching, precedence rules, and built-in connector defaults.
