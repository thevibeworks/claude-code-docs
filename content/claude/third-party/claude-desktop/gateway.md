> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Deploy Claude Desktop on 3P with an LLM gateway

> Configure Claude Desktop on 3P to use Claude models on a self-hosted gateway that implements the Anthropic Messages API

To use a self-hosted LLM gateway (for example LiteLLM, Portkey, or an in-house proxy) as the inference provider, set `inferenceProvider` to `gateway` and supply the base URL and credentials described below.

The gateway must implement the Anthropic [Messages API](https://docs.claude.com/en/api/messages):

* `POST /v1/messages` with [streaming](https://docs.claude.com/en/api/streaming) and [tool use](https://docs.claude.com/en/docs/tool-use) is required.
* `GET /v1/models` is optional. If the gateway implements it, Claude Desktop on 3P auto-discovers available models; if not, set `inferenceModels` explicitly.

The gateway should also preserve [prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching). Chat, Cowork, and Code sessions send `cache_control` breakpoints with each turn so that the provider can reuse the tool definitions, system prompt, and earlier turns of the conversation instead of reprocessing them. A gateway that forwards these fields, or translates them for its upstream provider, keeps that behavior. A gateway that strips `cache_control`, or that changes the system prompt or tool list from one request to the next, makes the provider reprocess the whole conversation on every turn at full input-token cost and higher latency. To verify, check the [usage fields](https://platform.claude.com/docs/en/build-with-claude/prompt-caching#tracking-cache-performance) your gateway returns or logs for Claude Desktop traffic: after the first request of a session, `cache_read_input_tokens` should be well above zero on most requests. If it is zero on every request, review the gateway's request transformation and caching settings for the route that serves Claude models.

In Chat and Cowork, the main conversation's breakpoints ask for a one-hour lifetime (`"ttl": "1h"`). In each response's `usage`, return the provider's `cache_creation` object with its `ephemeral_5m_input_tokens` and `ephemeral_1h_input_tokens` fields. Without that object, the [API request event](https://claude.com/docs/cowork/monitoring.md#api-request-event) in your OpenTelemetry export reports `0` for both `cache_creation_5m_tokens` and `cache_creation_1h_tokens`.

## Choose an authentication approach

| Scenario | Use | Notes |
| - | - | - |
| Proof of concept, or your gateway already issues per-team keys | [Static API key](#static-api-key) (`inferenceGatewayApiKey`) | A long-lived secret distributed in the managed profile. |
| Per-user attribution and identity-provider enforcement (MFA, conditional access) | [Single sign-on](#single-sign-on-with-your-identity-provider) (`inferenceGatewayOidc`) | Each user signs in with their own work account. |
| Your organization already has tooling that obtains a gateway credential | [Credential helper](https://claude.com/docs/third-party/claude-desktop/configuration.md#inferencecredentialhelper) (`inferenceCredentialHelper`) | An executable that prints the gateway credential to stdout at runtime. |

## Prepare devices

### Static API key

No per-device preparation is required. Generate an API key in your gateway and place it in the managed configuration as `inferenceGatewayApiKey` (see [Configure the app](#configure-the-app)).

### Single sign-on with your identity provider

Instead of distributing a shared gateway API key, you can have each user sign in with their own work account. The first time a user opens Claude Desktop, the app opens their browser to your organization's normal sign-in page (Microsoft Entra ID, Okta, or any OpenID Connect provider). After they sign in, the app sends a per-user token to your gateway on every request, and your gateway checks that token to confirm who the user is.

You need three things in place:

* An LLM gateway that can validate JSON Web Tokens (LiteLLM, Kong, Envoy, and Azure API Management all support this)
* Admin access to your identity provider to register a new application
* A way to push managed configuration to user devices (your existing MDM)

#### Set up single sign-on

**1. Register an application in Entra ID**

In the [Microsoft Entra admin center](https://entra.microsoft.com), go to **Identity → Applications → App registrations** and select **New registration**. Give it a name such as `Claude Desktop gateway`, choose **Accounts in this organizational directory only**, and select **Register**.

On the overview page, copy the **Application (client) ID** and **Directory (tenant) ID**. You will use both in the next two steps.

Open the **Authentication** blade, select **Add a platform**, and choose **Mobile and desktop applications**. Under **Custom redirect URIs**, add exactly:

```text theme={null}
http://127.0.0.1/callback
```

A few details that matter here: use `127.0.0.1` (not `localhost`), include the `/callback` path, and add it under the **Mobile and desktop applications** platform specifically. That platform is the only one Entra allows to use any local port, which the app needs because it picks a free port at sign-in time. You do not need a client secret or any additional API permissions.

If you manage this configuration from the Enterprise Admin Console, and developers also sign in to the gateway from Claude Code in the terminal, add a second redirect URI. See [Register the redirect URI for the terminal](https://claude.com/docs/third-party/claude-desktop/admin-console-claude-code.md#prepare-your-gateway).

**2. Configure your gateway to validate the token**

Tell your gateway to accept the bearer token only if it was issued by your tenant **for this application**.

In LiteLLM, this setup requires a LiteLLM Enterprise license, a database, and a master key. For the full configuration, see LiteLLM's [JWT-based Auth](https://docs.litellm.ai/docs/proxy/token_auth) guide. Merge these settings into your LiteLLM `config.yaml`:

```yaml theme={null}
environment_variables:
  JWT_PUBLIC_KEY_URL: https://login.microsoftonline.com/YOUR_TENANT_ID/discovery/v2.0/keys
  JWT_AUDIENCE: YOUR_CLIENT_ID
  JWT_ISSUER: https://login.microsoftonline.com/YOUR_TENANT_ID/v2.0

general_settings:
  enable_jwt_auth: true
  litellm_jwtauth:
    user_id_jwt_field: oid
```

Replace `YOUR_TENANT_ID` and `YOUR_CLIENT_ID` with the values from step 1. Set `JWT_ISSUER` to the `iss` claim of the token your gateway receives. By default the app sends an ID token, and its `iss` is the **Issuer URL** you enter in the next step.

LiteLLM rejects a user who has no LiteLLM user record. Create each record with the user's `oid` value as its user ID. To create records automatically at first sign-in, see [Map users at the gateway](#map-users-at-the-gateway).

> [!WARNING]
>
> The `JWT_AUDIENCE` line is required. Without it, your gateway accepts tokens issued to any application in your tenant, not just this one.

For Kong, Envoy, or Azure API Management, configure the equivalent JWT validation policy with the same JWKS URL, audience, and issuer.

**3. Configure in the app**

Open the [in-app configuration window](https://claude.com/docs/third-party/claude-desktop/in-app-configuration.md#open-the-configuration-window) (**Developer → Configure Third-Party Inference…**). In the **Connection** section, set **Inference provider** to **Gateway** and **Credential kind** to **Interactive sign-in**. This hides the API-key field and reveals **Gateway SSO IdP (OIDC)**:

| Field | Value |
| - | - |
| Gateway base URL | `https://llm-gateway.example.corp` |
| Credential kind | **Interactive sign-in** |
| Gateway SSO IdP (OIDC) → Client ID | `YOUR_CLIENT_ID` |
| Gateway SSO IdP (OIDC) → Issuer URL | `https://login.microsoftonline.com/YOUR_TENANT_ID/v2.0` |
| Gateway SSO IdP (OIDC) → Scopes | *leave empty for the default* |
| Gateway SSO IdP (OIDC) → Redirect port | *leave empty* |

Then click **Export** to produce a `.mobileconfig` (macOS) or `.reg` (Windows) file for your MDM. See [Deploy with MDM](https://claude.com/docs/third-party/claude-desktop/mdm.md) for the export and deployment workflow.

When a user next opens Claude Desktop, they see a **Sign in with your organization** button. Clicking it opens their browser to your Entra sign-in page; once they approve, they return to the app and can start working. The app keeps them signed in and refreshes the token in the background. If the session is revoked or expires under your tenant's policy, the app shows a **Sign in again** prompt; clicking it reopens the sign-in page in the browser.

#### Using Okta instead

In the Okta Admin Console, create a **Native** application with the **Authorization Code** and **Refresh Token** grant types. Okta requires the redirect URI to match exactly, including the port, so pick a fixed port (for example `53180`), register `http://127.0.0.1:53180/callback`, and set that same port in **Gateway SSO IdP (OIDC)**:

| Field | Value |
| - | - |
| Client ID | `YOUR_CLIENT_ID` |
| Issuer URL | `https://YOUR_ORG.okta.com` |
| Scopes | *leave empty for the default* |
| Redirect port | `53180` |

The [second redirect URI for Claude Code in the terminal](https://claude.com/docs/third-party/claude-desktop/admin-console-claude-code.md#prepare-your-gateway) uses the same port.

> [!NOTE]
>
> Use the **issuer** value, not the **Metadata URI**. Okta's admin console shows the metadata URI (ending in `/.well-known/openid-configuration`) prominently — that is the discovery document the app fetches *from* the issuer, not the issuer itself. If you are unsure, open the metadata URI in a browser and copy the `"issuer"` field from the JSON response. For a custom Okta authorization server the issuer is `https://YOUR_ORG.okta.com/oauth2/AUTH_SERVER_ID`.

Point your gateway's JWT validation at `https://YOUR_ORG.okta.com/oauth2/v1/keys`, or for a custom authorization server, at the `jwks_uri` value from its metadata document. Set the audience to the Okta client ID and the issuer to your **Issuer URL**. In LiteLLM, also set `user_id_jwt_field` to `sub`.

#### Map users at the gateway

Claude Desktop forwards the identity provider's token to your gateway verbatim — it does not add, remove, or rewrite any claims. With the default scopes (`openid profile email offline_access`), the ID token your gateway receives contains the standard OIDC `sub`, `email`, and `name` claims, plus whatever your provider includes for the `profile` scope. You can confirm exactly what is present by base64-decoding the middle segment of the `Authorization: Bearer` value your gateway receives.

Key the gateway's user record on the provider's immutable user ID rather than email, so the record survives email or name changes:

| Provider | Stable user-ID claim |
| - | - |
| Entra ID | `oid` |
| Okta and most other OIDC providers | `sub` |

If your gateway has no existing user records to preserve, the simplest setup is to auto-provision on first sign-in. For LiteLLM, add `user_email_jwt_field` and `user_id_upsert` to the validation block from step 2. With the values from [Using Okta instead](#using-okta-instead), the block looks like this:

```yaml theme={null}
environment_variables:
  JWT_PUBLIC_KEY_URL: https://YOUR_ORG.okta.com/oauth2/v1/keys
  JWT_AUDIENCE: YOUR_CLIENT_ID
  JWT_ISSUER: https://YOUR_ORG.okta.com

general_settings:
  enable_jwt_auth: true
  litellm_jwtauth:
    user_id_jwt_field: sub          # use "oid" for Entra ID
    user_email_jwt_field: email
    user_id_upsert: true
```

If you need additional claims (for example, a `groups` claim for team-level budgets), add them on your identity provider's authorization server — they pass through to the gateway unchanged. To request a non-default scope, set `scopes` in `inferenceGatewayOidc` (see [Single sign-on configuration keys](#single-sign-on-configuration-keys)).

#### Refresh tokens and session lifetime

Silent token refresh requires a refresh token from your identity provider, which in turn requires the `offline_access` scope on the authorization request. Whether Claude Desktop sends that scope depends on how you set `scopes` and `bearerTokenType`:

* **`scopes` left unset** — the default (`openid profile email offline_access`) includes `offline_access`, so a refresh token is issued.
* **`bearerTokenType: "access_token"`** — Claude Desktop automatically appends `offline_access` to whatever `scopes` value you supply, unless `appendOfflineAccess` is set to `false`.
* **`bearerTokenType: "id_token"` (the default) with `scopes` set explicitly** — Claude Desktop does **not** add `offline_access` for you. Include it in your `scopes` value if you want silent refresh; without it, users are prompted to sign in again each time the ID token expires (commonly about one hour).

**Authorization servers that reject `offline_access`.** Standard OIDC providers (Entra ID, Okta, Auth0) accept `offline_access` and require it to issue a refresh token, so keep the automatic append. If your authorization server rejects `offline_access` with an `invalid_scope` error, set `appendOfflineAccess` to `false` and include your provider's own refresh-token scope in `scopes`.

Refresh tokens govern whether users are re-prompted to sign in, not how long a sign-in may stay valid. To cap the sign-in lifetime under your identity provider's session policy, set [`inferenceSessionLifetimeSec`](https://claude.com/docs/third-party/claude-desktop/configuration#inferencesessionlifetimesec); Claude Desktop shows a re-authenticate banner before the session expires.

## Configure the app

Open the [in-app configuration window](https://claude.com/docs/third-party/claude-desktop/in-app-configuration.md#open-the-configuration-window) (**Developer → Configure Third-Party Inference…**). In the **Connection** section, set **Inference provider** to **Gateway**, then fill in the **Gateway credentials** card:

| Field | Value |
| - | - |
| Gateway base URL | `https://llm-gateway.example.corp` |
| Gateway API key | your gateway key (or a placeholder if your gateway has none) |
| Credential kind | **Static API key** (default), or **Interactive sign-in** for [single sign-on](#single-sign-on-with-your-identity-provider) |
| Gateway auth scheme | **Bearer** (default) or **x-api-key** |

Then click **Export** to produce a `.mobileconfig` (macOS) or `.reg` (Windows) file for your MDM. See [Deploy with MDM](https://claude.com/docs/third-party/claude-desktop/mdm.md) for the export and deployment workflow.

### Configuration keys

[Entry labels](https://claude.com/docs/third-party/claude-desktop/configuration.md#entry-labels) says what each label means.

#### `inferenceGatewayBaseUrl`

string

Consent required (A value that a bootstrap server delivers applies only after the user approves it, unless machine-scoped device management set that server's address. The trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)

Origin-pinned (A URL that a bootstrap server delivers must share the origin of bootstrapUrl, or Claude Desktop drops it. The limit is lifted when bootstrapOidc is set, and it does not apply to a value set in an MDM profile, the local configuration file or the Enterprise Admin Console.)

Since 1.2581.0

**Gateway base URL.** Full URL of the inference gateway endpoint.

***

#### `inferenceGatewayApiKey`

stringSince 1.2581.0

**Gateway API key.** API key for the configured inference gateway.

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
> * **`broker`:** uses Web Account Manager on Windows or Company Portal on macOS, and does not work on Linux. It can satisfy Conditional Access policies requiring a compliant or managed device, or token protection.
>
> `broker` needs Microsoft Entra ID, with the `issuer` in `inferenceGatewayOidc` set to `https://login.microsoftonline.com/{tenant-id}/v2.0`. Add the redirect URIs from [Register the Entra ID application](https://claude.com/docs/third-party/claude-desktop/entra-broker.md#register-the-entra-id-application).

***

#### `inferenceGatewayOidc`

object

Consent required (A value that a bootstrap server delivers applies only after the user approves it, unless machine-scoped device management set that server's address. The trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)

Since 1.6889.0

**Gateway SSO IdP (OIDC).** External IdP for gateway sign-in. The user’s token from this issuer is sent to the gateway as the Bearer credential.

> [!WARNING]
>
> **Deprecated**
>
> * Use inferenceIdpOidc with inferenceCredentialKind: "external-idp" once every desktop in the fleet is on a release that reads them. The original spelling will keep working; no end date has been set.

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
> > The app log names a host rejected for a referrer mismatch. Add that hostname here.

***

#### `inferenceIdpAuthFlow`

enumSince 2.7032.0

**Identity provider sign-in flow.** How the identity-provider sign-in runs: system browser (default) or the OS Microsoft Entra broker.

One of: `browser`, `broker`

> [accordion] More detail
>
> * **`browser`:** register the redirect URI `http://127.0.0.1:<port>/callback` with your identity provider (for Entra, `http://127.0.0.1/callback`).
> * **`broker`:** uses Web Account Manager on Windows or Company Portal on macOS, and does not work on Linux. It can satisfy Conditional Access policies requiring a compliant or managed device, or token protection.
>
> `broker` needs Microsoft Entra ID, with the `issuer` in `inferenceIdpOidc` set to `https://login.microsoftonline.com/{tenant-id}/v2.0`. Add the redirect URIs from [Register the Entra ID application](https://claude.com/docs/third-party/claude-desktop/entra-broker.md#register-the-entra-id-application).

***

#### `inferenceIdpOidc`

object

Consent required (A value that a bootstrap server delivers applies only after the user approves it, unless machine-scoped device management set that server's address. The trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)

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
> > The app log names a host rejected for a referrer mismatch. Add that hostname here.

***

#### `inferenceStreamIdleTimeoutSec`

integerRange: 300–1,800Since 1.44121.1

**Stream idle timeout.** Extra seconds to wait for model output on a streaming response that is sending only keep-alive pings. Gateway provider only. Default 300.

> [accordion] More detail
>
> With pings arriving (SSE `ping` events or `:` comment lines), sessions accept at least about five minutes of them, then wait this many seconds more. With no pings, each attempt at a silent response fails a minute or so after this many seconds. An attempt with no response headers fails after 15 minutes at most. On the Code tab, 16 minutes of silence ends the session, so values above 900 add nothing there.
>
> While this key is set, it takes priority over `CLAUDE_STREAM_IDLE_TIMEOUT_MS` in Claude Code's managed settings for sessions the app starts.

***

#### `inferenceGatewayAutoModeServerChecks`

booleanSince 4.16336.0

**Server-side Auto mode checks.** Temporary setting: sends session details, such as folder paths and a user name, so your gateway’s provider checks risky Auto mode actions.

> [accordion] More detail
>
> On unless you set it to `false`. A Claude apps gateway's `gateway.yaml` can't set it. While off, Auto mode's built-in check reviews risky actions.
>
> This setting goes away when Claude Code drops that check. After that, only turning off Auto mode (**Allow Auto mode**) avoids the provider's check.
>
> While on, Auto mode requests carry a `safeguards` field with session details such as rules, folder paths and a user name. They add one `anthropic-beta` value, which a session keeps sending after it leaves Auto mode.
>
> Your gateway must pass both on, and `safeguard_results` and tool-use IDs back, unchanged. If it drops the result or answers 400, 403, 422, 500 or 502, the built-in check takes over. Other errors or an unreadable result can break every turn: turn this off and have users restart the app.

***

To send additional HTTP headers on every inference request (tenant routing, org IDs, and similar), set [`inferenceCustomHeaders`](https://claude.com/docs/third-party/claude-desktop/configuration#inferencecustomheaders). It applies to all providers, not just gateways.

### Single sign-on configuration keys

Single sign-on is enabled by setting `inferenceCredentialKind` to `interactive` **and** supplying `inferenceGatewayOidc`. `interactive` alone (without `inferenceGatewayOidc`) selects a different mode where the gateway itself acts as the authorization server.

From Claude Desktop 2.7032.0, `inferenceCredentialKind: "external-idp"` with [`inferenceIdpOidc`](https://claude.com/docs/third-party/claude-desktop/configuration#inferenceidpoidc) and `inferenceIdpAuthFlow`, the keys [Amazon Bedrock identity provider sign-in](https://claude.com/docs/third-party/claude-desktop/bedrock.md#sign-in-with-your-identity-provider) uses, is an equivalent spelling of this configuration; `interactive` with `inferenceGatewayOidc` keeps working, so keep it until every device runs 2.7032.0 or later.

For the fields of [`inferenceGatewayOidc`](#inferencegatewayoidc), and for [`inferenceGatewayOidcAuthFlow`](#inferencegatewayoidcauthflow), which can run the sign-in through the [OS identity broker](https://claude.com/docs/third-party/claude-desktop/entra-broker.md), see their entries under [Configuration keys](#configuration-keys).

> [!WARNING]
>
> `inferenceGatewayOidc` is **one MDM key whose value is a JSON string** — not separate keys like `inferenceGatewayOidc.clientId`. See [how object-typed keys are encoded](https://claude.com/docs/third-party/claude-desktop/configuration-format.md#value-types). The in-app **Export** produces the correct format automatically.

In a macOS `.mobileconfig` payload (Okta example):

```xml theme={null}
<key>inferenceCredentialKind</key>
<string>interactive</string>
<key>inferenceGatewayOidc</key>
<string>{"issuer":"https://YOUR_ORG.okta.com","clientId":"YOUR_CLIENT_ID","redirectPort":53180}</string>
```

Earlier app versions used `inferenceGatewayAuthScheme: "sso"` to select this mode. That value is deprecated, so set `inferenceCredentialKind: "interactive"` instead. The [configuration changelog](https://claude.com/docs/third-party/claude-desktop/configuration-changelog.md#v2-26454-0) says which app versions read the deprecated value.

### Models

When `inferenceModels` is unset, Claude Desktop on 3P populates the model picker from your gateway's `GET /v1/models` response. Auto-discovery shows only models whose IDs are recognizably Claude. Set [`inferenceModels`](https://claude.com/docs/third-party/claude-desktop/configuration#models) to replace discovery with an explicit list. Use the model IDs your gateway expects (for example `bedrock/us.anthropic.claude-opus-5` for a LiteLLM-style routing prefix).

If your gateway serves Claude models under routing aliases, list each alias in `inferenceModels` and set `behavesAs` on its entry to the ID of the Claude model it routes to, such as `claude-sonnet-5`. For an alias without a model version, users then get that model's **Effort** control, and sessions assume that model's context window. Requires Claude Desktop 4.29.0 or later. For an alias that contains a model version, see [Map an unrecognized model ID to a Claude model](https://claude.com/docs/third-party/claude-desktop/models.md#map-an-unrecognized-model-id-to-a-claude-model).

Your gateway can mark which Claude tier a model serves by returning an `anthropic_family_tier` field (a tier name such as `sonnet` or `opus`) on that model object in its `/v1/models` response, optionally with `is_family_default: true` when several models map to the same tier. The app and its sessions use the marked model when they need that tier, such as for a sub-agent that asks for `sonnet`, even if the user picked another model. The app also reads other optional fields on each model object. `display_name` sets the picker label when the app cannot derive one from the model ID. `description` adds a one-line description beneath the label. `supports_1m: true`, or a `max_input_tokens` value of 1,000,000 or more, marks a discovered model as supporting the 1M-token context window, as `supports1m` does on an `inferenceModels` entry.

If your gateway doesn't implement `GET /v1/models`, give every `inferenceModels` entry the full model ID your gateway accepts. When every entry is a full model ID, the app skips the `/v1/models` call automatically. A bare tier alias such as `sonnet` can't be resolved without discovery, so a list that contains one keeps discovery on. If discovery stays on, a gateway that answers the call with an error makes the app fall back to the `inferenceModels` list immediately. A gateway that accepts the call and hangs delays the model list by up to 10 seconds at launch.

### Context window and compaction

Chat, Cowork, and Code sessions keep a long conversation within the model's context window by compacting it. To compact, the session sends one request that asks the model to summarize the conversation so far, then continues from the summary. Through a gateway, a session can't read the model's real context window from the provider, so it assumes one from the model ID and the picker entry:

* **Standard entry**: 1M tokens for a model the session recognizes as having a native 1M context window, as listed under [the context window behind a gateway](https://code.claude.com/docs/en/model-config#context-window-behind-a-gateway) in the Claude Code documentation, and 200K tokens for every other model ID, including an ID the session doesn't recognize whose `inferenceModels` entry doesn't set [`behavesAs`](https://claude.com/docs/third-party/claude-desktop/models#map-an-unrecognized-model-id-to-a-claude-model). On Claude Desktop versions earlier than 2.19675.0, a session assumes 200K tokens on this entry for every model.
* **1M context window entry**, or the single entry from `prefer1m` or `modelPrefer1mContext`: 1M tokens, regardless of the model ID.

If the gateway or the provider accepts less than the window a session assumes, requests past that limit fail. The session then compacts and retries only when the provider's too-long error reaches it unchanged. To make sessions compact earlier than the window they assume, for example when your provider serves a natively 1M model with only a 200K window, see [Set the auto-compact window](https://code.claude.com/docs/en/model-config#set-the-auto-compact-window) in the Claude Code documentation. For a model ID the session doesn't recognize, see [Context window for unrecognized model IDs](#context-window-for-unrecognized-model-ids).

The following table lists what the model configuration and the gateway need to provide so that sessions use the full context window and compact when they reach it, and how to check each requirement.

| Requirement | What fails without it | How to check |
| - | - | - |
| [Set a larger context window](https://claude.com/docs/third-party/claude-desktop/models.md#set-a-larger-context-window-for-a-model) for each model your provider serves with a 1M-token context window but a session assumes 200K tokens for. With discovery, mark the model (see [Models](#models)) and set `modelPrefer1mContext`. Where you use `supports1m` or mark the model, also accept the `context-1m-2025-08-07` value in the `anthropic-beta` request header. | Sessions on the model assume a 200K-token window, even when the provider accepts 1M. If the gateway rejects the header value with a `400` whose message contains `context-1m-2025-08-07`, the session sends the request again without the value and assumes a 200K-token window. After a `400` with only your gateway's own text, such as `upstream rejected the request`, the session doesn't send the request again, and the user's first message fails. | From a new session that uses the 1M window, confirm in the gateway's logs that requests above 200K input tokens succeed and, where you use `supports1m` or mark the model, that requests carry the header value. |
| [Stream responses](https://code.claude.com/docs/en/llm-gateway-protocol#streaming) through without buffering, including the provider's SSE `ping` events, and set the response timeout on every proxy and load balancer on the route longer than your slowest complete response. | The summary request carries the whole conversation, and while the provider works on it, pings can be the only bytes on the connection. If a proxy buffers them, the session sees no bytes, and each attempt fails after about five minutes, or later if you raised `inferenceStreamIdleTimeoutSec`. If a proxy's response timeout is shorter than the response takes, it ends the request with its own error, such as `504`. | Run a streaming request with `curl -N` against the hostname clients use and confirm that events print as they are generated, not in one burst at the end. |
| Return the provider's `usage` object unchanged on every response, including `cache_creation_input_tokens` and `cache_read_input_tokens`. | The session counts the conversation's tokens from the `usage` of the latest response. With the cache fields missing it undercounts, and requests reach the provider's limit before the session compacts. | Compare the `usage` object in the gateway's upstream response log with the one the client receives for the same request. They should be identical, and where the provider supports prompt caching, `cache_read_input_tokens` is above zero after the first turn. |
| [Forward the provider's status code and error body unchanged](https://code.claude.com/docs/en/llm-gateway-protocol#automatic-retry-and-error-forwarding) when it rejects a request. | Where the provider's too-long error is the compaction trigger, the session compacts and retries only if that error reaches it unchanged. With a rewritten error, the session shows the error and doesn't compact. | Send an oversized request through the gateway and confirm that the client receives the provider's status code and error body. |

The entry for [`inferenceStreamIdleTimeoutSec`](https://claude.com/docs/third-party/claude-desktop/configuration#inferencestreamidletimeoutsec) gives how long a session waits with and without keep-alive pings. Raise that key if your provider needs longer than that before its first output on a large request.

#### Context window for unrecognized model IDs

A session assumes a 200K-token window for a model ID that it doesn't recognize, such as a routing alias whose `inferenceModels` entry doesn't set `behavesAs`, even when your provider accepts more. It compacts a long conversation near 200K tokens. If the summary request fails, the turn stops with `Prompt is too long`. The session doesn't send the request for Claude's reply to your gateway, even when your provider would accept it. For what users see and can do, see [`Your context window is full`](#troubleshoot) under Troubleshoot.

If the model behind the ID accepts more than 200K tokens, declare its window:

* **In your configuration**, for a model that accepts 1M-token requests: [set a larger context window for the model](https://claude.com/docs/third-party/claude-desktop/models.md#set-a-larger-context-window-for-a-model).
* **On each device**, for a window other than 1M tokens: set [`CLAUDE_CODE_MAX_CONTEXT_TOKENS`](https://code.claude.com/docs/en/model-config#which-ids-claude_code_max_context_tokens-applies-to) to the window in tokens, such as `500000`, in the `env` block of [Claude Code managed settings](https://code.claude.com/docs/en/settings#settings-files). It changes the window only where a session would assume 200K tokens for an ID that it doesn't recognize. It does that for every such ID on the device, so use the smallest window among the models behind them. If the device already has Claude Code managed settings, add the variable to those settings and leave [`parentSettingsBehavior`](https://claude.com/docs/third-party/claude-desktop/code#interaction-with-claude-code%E2%80%99s-own-managed-settings) as it is, set or unset. If the device has none yet, also set `parentSettingsBehavior` to `"merge"` in the settings that you create.

A [Claude apps gateway](https://code.claude.com/docs/en/claude-apps-gateway) doesn't accept `inferenceModels` in its policy's `desktop` block, so you can't set `behavesAs` or `prefer1m` on a model there. For the gateway's own ways to offer the 1M context window, see [Extended context in Claude Desktop](https://code.claude.com/docs/en/claude-apps-gateway-config#extended-context-in-claude-desktop) in the Claude Code documentation.

### Gateway requirements for preserved thinking

On models with [preserved thinking](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking), the provider ties each thinking block that Claude produces to the `system`, `tools`, and `messages` content that came before it. A session sends the thinking blocks from earlier turns back in later requests. That content can change after Claude produces a block, for example in your gateway or after a Claude Desktop update. If it has changed, the provider can reject the request with a `400` whose message says that the block is `bound to a different conversation`.

On these models, your gateway needs to do the following:

* **Forward the request content unchanged**: send `system`, `tools`, and `messages` to the provider as the session sent them, including the [attribution block](https://code.claude.com/docs/en/llm-gateway-protocol#system-prompt-attribution-block) that Claude Code puts first in the `system` array. To check, compare these fields in the request that the gateway received and in the one that it sent to the provider. Apart from `cache_control` markers, their content should be identical.
* **Forward the rejection unchanged**: when the provider's status code and error body reach the session unchanged, the session removes the earlier thinking blocks and retries. The user sees only the reply. If your gateway rewrites the error, the user can see the error. Each later message in that conversation then fails the same way. To check, see the error-forwarding requirement in [Context window and compaction](#context-window-and-compaction).

### MCP tool search

[MCP tool search](https://code.claude.com/docs/en/mcp#scale-with-mcp-tool-search) loads MCP tool schemas on demand instead of inlining every schema into the context window. It reduces context pressure when many MCP tools are configured (sessions that otherwise compact every turn or two).

On gateway deployments, Claude Desktop turns off tool search and Claude Code's other experimental beta features by default, apart from the provider's [Auto mode review](#auto-mode-checks), because strict gateways reject the experimental `anthropic-beta` request headers and request fields those features add. The same applies to Microsoft Foundry deployments and to any provider configured with a custom base URL. Setting the `ENABLE_TOOL_SEARCH` environment variable to `true` does not lift this suppression. To turn tool search on for these deployments, set the [`toolSearchEnabled`](https://claude.com/docs/third-party/claude-desktop/configuration#toolsearchenabled) configuration key. Requires app version 1.21459.0 or later.

On Claude API, Google Cloud's Agent Platform, Amazon Bedrock, and Amazon Bedrock Mantle deployments with no custom base URL, tool search is on by default from Claude Desktop 1.49585.0 and `toolSearchEnabled` is not needed. These versions leave Claude Code's experimental beta features on for those providers, as terminal Claude Code does (on Google Cloud's Agent Platform, tool search applies to Claude 4.5 and later models). To turn tool search off on these deployments, set `ENABLE_TOOL_SEARCH` to `false` in the `env` block of [Claude Code managed settings](https://code.claude.com/docs/en/settings#settings-files) on the device. If the device already has Claude Code managed settings, add the variable to those settings and leave [`parentSettingsBehavior`](https://claude.com/docs/third-party/claude-desktop/code#interaction-with-claude-code%E2%80%99s-own-managed-settings) as it is, set or unset. If the device has none yet, also set `parentSettingsBehavior` to `"merge"` in the settings that you create. On earlier app versions these providers also have tool search off by default, and `toolSearchEnabled` turns it on.

> [!WARNING]
>
> Setting `toolSearchEnabled` causes sessions to send experimental request headers and fields to your gateway or provider. On gateway deployments running Claude Desktop 1.40609.0 or later the key adds only the tool-search request shape (the `tool-search-tool-2025-10-19` value in the `anthropic-beta` header, deferred tool loading, and `tool_reference` content blocks). On earlier versions, on Microsoft Foundry, and on providers behind a custom base URL, the key instead lifts the experimental-beta suppression for these sessions, so requests also carry Claude Code's other experimental beta headers and fields for that provider. Enable it only if your gateway forwards and accepts what it will receive; when it does not, requests fail with HTTP 400. LiteLLM in passthrough mode and Cloudflare AI Gateway both forward `anthropic-beta` headers and `tool_reference` content blocks.

### Auto mode checks

In [**Auto mode**](https://claude.com/docs/third-party/claude-desktop/configuration.md#automodeenabled), which Cowork shows as **Automatically approve**, a safety check reviews Claude's actions and blocks the ones it judges risky.

> [!NOTE]
>
> If a card or notice titled **Auto mode switched to its built-in safety check for this session** sent you here, you can keep working, and the built-in safety check reviews Claude's actions. In Code, select **Continue** on the card within five minutes, or the turn ends. Share this section with whoever manages Claude Desktop or the gateway for you.

On a gateway deployment, one of these does the review:

* **The model provider behind your gateway (the default)**: the session asks for the review in its normal request, and the provider returns its decision on each action, called a verdict, with the response. The request describes the session to the provider, with [details such as folder paths and a user name](#gateway-requirements-for-auto-mode-checks). The session sends no separate request for an action that gets a verdict.
* **Claude Code's built-in safety check**: it reviews actions on devices where the provider's review is off, and it can take over when no verdict arrives. It sends its own requests through your gateway, and you pay for them like the rest of your usage. While it reviews, shell commands in Cowork wait for it too, which usually adds one request for each command. For what your gateway must accept for this check, and for when shell commands are refused or aren't checked, see [`autoModeEnabled`](https://claude.com/docs/third-party/claude-desktop/configuration#automodeenabled). To use another model for this check, see [Choose the Auto mode classifier model](https://claude.com/docs/third-party/claude-desktop/code.md#choose-the-auto-mode-classifier-model).

Sessions ask the provider for the review while **Server-side Auto mode checks** ([`inferenceGatewayAutoModeServerChecks`](https://claude.com/docs/third-party/claude-desktop/configuration#inferencegatewayautomodeserverchecks)) is on. If you don't set the key, the setting is on. Your gateway needs to [pass the review through unchanged](#gateway-requirements-for-auto-mode-checks). To check that it does, [test Auto mode checks on one device](#test-auto-mode-checks-on-one-device).

If your gateway doesn't pass the review through:

* **What happens**: in a few cases, such as when your gateway drops the verdicts, the built-in safety check takes over. In the other cases, every Auto mode turn fails or actions that need a review don't run, as described in [What users see when no Auto mode verdict arrives](#what-users-see-when-no-auto-mode-verdict-arrives).
* **How to keep the built-in safety check until your gateway is ready**: [turn off **Server-side Auto mode checks**](#turn-off-server-side-auto-mode-checks). You can't turn the setting off for devices that get their configuration from a [Claude apps gateway](https://code.claude.com/docs/en/claude-apps-gateway), the gateway server included with Claude Code.

#### Gateway requirements for Auto mode checks

For the provider's review, your gateway needs to pass these parts of each Auto mode request and response through unchanged.

| What to pass through | Where it appears |
| - | - |
| The `dangerous-tool-use-2026-09-03` value | The `anthropic-beta` request header |
| The `safeguards` field | The top level of the request body |
| The `safeguard_results` field | The `delta` object of the `message_delta` streaming event |
| The `id` of each `tool_use` content block | The `content_block_start` streaming events |

The provider behind your gateway also needs to run the review for the model that a session uses. The [test](#test-auto-mode-checks-on-one-device) shows whether it does for the model you test with.

> [!WARNING]
>
> The `safeguards` field describes the session so that the provider can judge each action. A gateway that logs request bodies logs this field too. The field includes details such as the following:
>
> * [Auto mode rules](https://claude.com/docs/third-party/claude-desktop/code.md#tune-the-auto-mode-classifier), including any that your organization or, in Code sessions, the user added
> * Permission rules and folder paths, including the user's home folder
> * A user name, such as the login name on the device or the part of the user's Git email address before the `@`
> * Git state such as the branch, the remotes, and the number of changed files

#### What users see when no Auto mode verdict arrives

In sessions that ask the provider for the review, users see one of the following when your gateway or provider doesn't meet the requirements.

* **A card or notice, and the built-in safety check takes over**: no result comes back, or the provider answers that it doesn't run the review or has turned the review off. The same happens when the request gets one of these errors and then succeeds when the session sends it again without asking for the review: `400`, `403`, `422`, or a `500` or `502` whose response has no `request-id` header. Code shows a card titled **Auto mode switched to its built-in safety check for this session**, and Cowork shows the same words as a notice. In Code, the turn continues once the user selects **Continue**. If nobody answers the card within five minutes, the turn ends, and the action that waited reads `Stopped` and doesn't run.
* **Nothing, and work continues**: the `tool_use` IDs are rewritten, or the provider answers that it couldn't run the review this time. The built-in safety check reviews actions.
* **Actions don't run**: the `safeguard_results` field arrives in a form the session can't read. Actions that need a review read `Blocked` in Code and, after the turn, `Failed` in Cowork. The turn can stop with a card titled `Auto mode’s safety check was unavailable` in Code, and with a notice that begins `Auto mode is unavailable` in Cowork. [Turn the setting off](#turn-off-server-side-auto-mode-checks).
* **Every Auto mode turn fails**: each request that asks for the review gets an error, and the session doesn't send it again without asking for the review. This happens after every other error, such as `401`, `404`, or `413`. This includes a `500` or `502` whose response has a `request-id` header, which the session treats as the provider's own error. See [Troubleshoot](#troubleshoot).

To find out which of these a user saw, have the user go to **Help > Troubleshooting > Generate Diagnostic Report** and select **Export to file** right after it happens. If Code shows the card, the user selects **Continue** first. Read the report as described in [Test Auto mode checks on one device](#test-auto-mode-checks-on-one-device). A Code session on an SSH host doesn't write its Auto mode lines to this report.

After a user selects **Continue**, the card stays hidden for 24 hours, so rely on the diagnostic report when you test again.

#### Test Auto mode checks on one device

Run the test on a device where [**Server-side Auto mode checks**](#auto-mode-checks) is on. If the device has a version of Claude Desktop where the setting is on by default, and you haven't turned it off, there's nothing to set.

Otherwise, turn the setting on for one test device alone. Pick a device that isn't signed in to an Enterprise Admin Console organization and doesn't get its configuration from a Claude apps gateway. The Enterprise Admin Console can't limit the setting to a group, and a [Claude apps gateway](https://code.claude.com/docs/en/claude-apps-gateway) doesn't start if its configuration holds the key. Turn the setting on in whichever of these holds the device's gateway settings:

* **A managed profile that doesn't set `bootstrapUrl`**: set `inferenceGatewayAutoModeServerChecks` to `true` in the device's profile, then quit and reopen Claude Desktop.
* **A [bootstrap server](https://claude.com/docs/third-party/claude-desktop/bootstrap.md)**: return the key as `true` in the response for the device's user, then quit and reopen Claude Desktop.
* **The [in-app configuration window](https://claude.com/docs/third-party/claude-desktop/in-app-configuration.md#open-the-configuration-window)**: turn on the **Server-side Auto mode checks** toggle under **Connection**, then click **Apply Changes** and **Save & Restart**.

**1. Run one task in Auto mode**

Note the time in UTC. Start a Code session on the device itself, not on an SSH host, and select **Auto mode**. Ask Claude for an action that Auto mode reviews, such as creating a file outside the project folder or fetching a web page. If the card appears, select **Continue**, because the session may write its result only after you answer.

**2. Read the result in the diagnostic report**

Right after the task, go to **Help > Troubleshooting > Generate Diagnostic Report** and select **Export to file**. In the exported report, open `cli-diagnostics-log.txt` and find the lines whose `event` is `cli_api_auto_mode_server_check`. Every session on the device writes to this log, so read only the lines whose `timestamp` is later than the time you noted. Each line's `data` holds a `state`, a `switch`, and sometimes a `reason`. Look them up under [Auto mode check results in the diagnostic report](#auto-mode-check-results-in-the-diagnostic-report).

#### Auto mode check results in the diagnostic report

A `requested` line means that the session asked for the review. The lines after it are the result. A session writes each kind of line only once, so start a new session for each test.

| Line in the report | What it means | What to do |
| - | - | - |
| `verdict` | Your gateway passes the review through. | Repeat the test with each model that your users can select. If a `no_verdict` line also appears, follow its row first. |
| `no_verdict`, `server_no_result` | No result came back. Part of the review was dropped on the way, or the provider returned none. | Compare what the gateway sent upstream and returned to the client with [the requirements](#gateway-requirements-for-auto-mode-checks). If it passed everything through, follow the `server_unsupported` row. |
| `no_verdict`, `server_unsupported` | The provider doesn't run the review for this model or key. | Use a provider and model that run the review, or [turn the setting off](#turn-off-server-side-auto-mode-checks). |
| `no_verdict`, `other_tool_use_ids` | Verdicts came back under IDs that none of the response's actions has. | Return the provider's `tool_use` IDs unchanged. |
| `no_verdict`, `server_unrecognized_result` | The session can't read the `safeguard_results` field. | [Turn the setting off](#turn-off-server-side-auto-mode-checks), because actions that need a review don't run. Then compare what your gateway returned to the client with [the requirements](#gateway-requirements-for-auto-mode-checks). |
| `not_requested`, `beta_rejected` | Your gateway, or the provider behind it, returned a `400`, `403`, `422`, `500`, or `502` to an earlier request that asked for the review, so the session stopped asking. | Check your gateway's logs for which of the two refused the request. For your gateway, accept the header value and the field. For the provider, follow the `server_unsupported` row. |
| `not_requested`, `betas_disabled`, `switch` is `off` | **Server-side Auto mode checks** is off for this device, because you turned it off, because Claude Desktop can't read the key's value, or because the key isn't set and the device has an earlier version of Claude Desktop, where the setting is off by default. | [Turn the setting on for the device](#test-auto-mode-checks-on-one-device). On an earlier version, you can update Claude Desktop instead. |
| `not_requested`, `betas_disabled`, `switch` is `on` | The device's own Claude Code managed settings or a compliance policy turn experimental betas off, which takes priority. | If a `requested` line follows, ignore this line. If none follows, check whether the device's [Claude Code managed settings](https://code.claude.com/docs/en/managed-settings) set `CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS`. |
| Only `requested`, and Claude's actions read `Blocked`, or `Failed` with an error that names auto mode | The session couldn't read the verdicts, or the response ended before they arrived. | If the log also holds `cli_stream_failed` lines, see the streaming requirement in [Context window and compaction](#context-window-and-compaction). Otherwise, follow the `server_unrecognized_result` row. |
| Only `requested`, and the turn failed with an error that doesn't name Auto mode | The request that asked for the review got an error. | See [Troubleshoot](#troubleshoot). |
| Only `requested`, and the turn finished | No action in the turn got a verdict. | Check your gateway's logs for errors on the requests that asked for the review. If you find a `500` or `502`, follow the `beta_rejected` row. If there are no errors, start a new session, and ask for an action that Auto mode reviews. |
| No `cli_api_auto_mode_server_check` line | The session recorded nothing about the review. | Check that the session ran in **Auto mode**, then update Claude Desktop. |

For any other line, or if these steps don't help, share the report with your Anthropic representative.

#### Turn off server-side Auto mode checks

Set [`inferenceGatewayAutoModeServerChecks`](https://claude.com/docs/third-party/claude-desktop/configuration#inferencegatewayautomodeserverchecks) to `false` to have Claude Code's built-in safety check review Auto mode's actions. If you leave the key out, the setting is on, so set it to `false`, except on devices that a [Claude apps gateway](https://code.claude.com/docs/en/claude-apps-gateway) configures. The setting is temporary. It goes away when Claude Code drops its built-in safety check, so use it only while you bring your gateway up to [the requirements](#gateway-requirements-for-auto-mode-checks).

Set the key in whichever of these holds the device's gateway settings:

* **A managed profile that doesn't set `bootstrapUrl`**: add the key to the profile that already holds your gateway settings. On devices whose gateway settings were made in the in-app configuration window, don't add the key to a profile that lacks those settings. Otherwise, [the managed configuration takes effect](https://claude.com/docs/third-party/claude-desktop/configuration-format.md#which-configuration-source-applies-on-a-device), and Claude Desktop ignores the gateway settings made in the window. To write the key in your profile's format, use the **Export** menu in the in-app configuration window.
* **A [bootstrap server](https://claude.com/docs/third-party/claude-desktop/bootstrap.md) that you host, other than a Claude apps gateway**: return the key in the response.
* **The [in-app configuration window](https://claude.com/docs/third-party/claude-desktop/in-app-configuration.md#apply-locally-or-export-for-a-fleet)**: turn off the **Server-side Auto mode checks** toggle under **Connection**. The window stores the toggle only after you change it, so if the toggle already shows off, turn it on and then off. Then use the **Export** menu for a profile to deploy, or click **Apply Changes** on a device that takes its settings from the window.
* **The [Enterprise Admin Console](https://claude.com/docs/third-party/claude-desktop/admin-console.md#configure-claude-desktop)**: open **Organization settings** and go to the **Connection** page under **Desktop 3P**. If the **Server-side Auto mode checks** switch is off and its row shows **Reset to default**, the console already stores the setting as off. Otherwise, turn off the switch, or turn it on and then off if it already shows off. Then click **Save changes**.
* **A [Claude apps gateway](https://code.claude.com/docs/en/claude-apps-gateway)**: leave the key out of the Claude apps gateway's configuration. The Claude apps gateway [doesn't start](https://code.claude.com/docs/en/claude-apps-gateway-config#claude-desktop-overlay) if a `desktop` block holds the key, whatever its value, and upgrading the Claude apps gateway doesn't change that. It never sends the key to the devices that it configures, and a copy of the key in a device's managed profile has no effect. Those devices follow the default, so their sessions ask for the provider's review. To avoid the review, set [`autoModeEnabled`](https://claude.com/docs/third-party/claude-desktop/configuration#automodeenabled) to `false` in the `desktop` block of each policy that serves them, which turns Auto mode off in Claude Desktop for everyone that the policy serves.

Set the key even if [Claude Code managed settings](https://code.claude.com/docs/en/managed-settings) or a user's `~/.claude/settings.json` already set Claude Code's [`CLAUDE_CODE_AUTO_MODE_SERVER`](https://code.claude.com/docs/en/permission-modes#server-side-classifier-review) variable to `0`. Claude Desktop's setting takes priority over that variable.

The change takes effect once each user [quits and reopens Claude Desktop](https://claude.com/docs/third-party/claude-desktop/configuration-format.md#when-a-configuration-change-on-a-device-takes-effect). To confirm the key on a device after the user reopens Claude Desktop, go to **Help > Troubleshooting > Generate Diagnostic Report** and select **Export to file**. In the exported report, `managed-config.txt` lists `inferenceGatewayAutoModeServerChecks = false`.

## Block requests at a spend limit

To show users your own message when your gateway blocks them at a budget or spend limit, return HTTP `402` with the message in a [Messages API error body](https://platform.claude.com/docs/en/api/errors#error-shapes):

```json theme={null}
{
  "type": "error",
  "error": {
    "type": "billing_error",
    "message": "You reached your monthly spend limit of $500. Ask your manager for an increase."
  }
}
```

Claude Desktop doesn't retry a `402`. Once your gateway accepts requests again, the user's next message in the same session goes through.

Cowork, Chat, and Code show a **Billing issue** card, with your message below the app's own explanation.

![Cowork card titled Billing issue. The app's explanation reads: You won't be able to start tasks until your IT team adds credits or updates billing. Below it, in monospace, is the gateway's message: You reached your monthly spend limit of \$500. Ask your manager for an increase.](https://mintcdn.com/claude-ai/_XP3pgAHpW92TgGc/images/third-party/gateway-billing-issue-card.png?fit=max\&auto=format\&n=_XP3pgAHpW92TgGc\&q=85\&s=b54737876348e2fa4f53a0adc5d01a1d)

The Billing issue card in Cowork, with an example gateway message in monospace.

> [!NOTE]
>
> The **Billing issue** card in Cowork and Chat requires Claude Desktop 4.4212.0 or later. In earlier versions, both show your message in a **Something went wrong** card with a **Try again** button.

### Write the spend limit message

Keep `error.message` short and say who can raise the limit. The **Billing issue** card shows your message as plain text, so a URL or email address in it isn't clickable. To give users a clickable HTTPS link, set `linkUrl` on the [`banner`](https://claude.com/docs/third-party/claude-desktop/configuration#banner), the notice across the top of the app window.

Avoid phrases from the app's own error messages, such as "usage limit", "hit your limit", "hit your monthly limit", "out of usage", and "credit balance is too low". If your message contains one, the app can show its own card or text instead.

### Other status codes at a spend limit

With these status codes, users can see a general error or a card about a different problem, and Code's card can hide or drop your message.

* **`429`**: Claude Desktop can retry for about three minutes or longer before it shows an error, unless the response carries `x-should-retry: false`. Code then shows **Server is temporarily limiting requests**. In Claude Desktop 4.23118.0 or later, when a [Claude apps gateway](https://code.claude.com/docs/en/claude-apps-gateway) blocks a user at a spend limit, local Code sessions outside WSL show **Spend limit reached** with the gateway's message instead.
* **`401` or `403`**: Code shows a card about credentials, sign-in, or permissions.
* **`400`**: Code shows **Invalid request**.

### Warn users before the spend limit

To tell users where they stand before your gateway blocks them, show one line of text in one of these places:

* **Across the top of the app window**: set the [`banner`](https://claude.com/docs/third-party/claude-desktop/configuration#banner) configuration key to show a one-line notice. If you serve configuration per user, for example from a [bootstrap server](https://claude.com/docs/third-party/claude-desktop/bootstrap.md), each user's notice can show their own figure, such as "You have used 82% of your monthly budget."
* **Above the message box**: set up a [status line](https://claude.com/docs/third-party/claude-desktop/status-line.md). Claude Desktop runs a program that you install on the user's device and shows the line it prints.

Claude Desktop can also limit each user's tokens, separately from your gateway's budget, and warn users before they reach that limit. To set up the limit and check where it applies, see the [token limit keys](https://claude.com/docs/third-party/claude-desktop/configuration.md#inferencemaxtokensperwindow) in the configuration reference.

## Troubleshoot

**`gateway SSO: server does not advertise device_authorization_endpoint`** — The app could not read your `inferenceGatewayOidc` value, so it fell back to treating the gateway itself as the sign-in server. Almost always this means the value is missing or not valid JSON, for example because it was written as separate dotted keys instead of one `inferenceGatewayOidc` value. Re-export from the in-app configuration window, or copy the `.mobileconfig` snippet above.

**`OIDC discovery failed (HTTP 404)` or `(HTTP 405)`** — The `issuer` value is not the issuer base URL. Most often the metadata URI (ending in `/.well-known/openid-configuration`) was pasted instead, which doubles the path. Remove that suffix so `issuer` is just `https://YOUR_ORG.okta.com` (or the equivalent for your provider).

**`no credential configured for provider "gateway": set inferenceCredentialKind or one of the credential fields`.** `inferenceCredentialKind: "interactive"` isn't present in the configuration Claude Desktop is using. Add it where Claude Desktop gets its configuration:

* **A managed profile that doesn't set `bootstrapUrl`**: add the key to the profile you push to devices.
* **A [bootstrap server](https://claude.com/docs/third-party/claude-desktop/bootstrap.md)**: return the key in the response, then quit and reopen Claude Desktop. A copy of the key in the managed profile has no effect. A message that also includes `bootstrap response failed validation` comes from this case.

A [Claude apps gateway](https://code.claude.com/docs/en/claude-apps-gateway) is a bootstrap server that sets the connection keys in its response itself, so you can't add this key in the gateway's configuration. Earlier gateway versions send `inferenceGatewayAuthScheme: "sso"` in place of this key. [Upgrade the gateway](https://code.claude.com/docs/en/claude-apps-gateway-deploy#upgrades) to the current Claude Code version, then quit and reopen Claude Desktop. Or update Claude Desktop to a version that [reads `inferenceGatewayAuthScheme: "sso"`](https://claude.com/docs/third-party/claude-desktop/configuration-changelog#v2-26454-0).

**Browser shows "Connected" but the app reports the sign-in failed, or `Token exchange failed (HTTP 401)`** — The browser step succeeded, but the identity provider rejected the follow-up token request. This usually means the IdP application is registered as a confidential (Web) client, which expects a client secret. Claude is a public PKCE client and doesn't send one. Register a public/native client instead: **Native Application** in Okta, or the **Mobile and desktop applications** platform in Entra ID. Application type generally can't be changed after creation, so you may need to create a new one.

> [!NOTE]
>
> Google Workspace can be used as the identity provider, but in the default `id_token` mode Google does not issue a fresh ID token on background refresh, so users are prompted to sign in again roughly once an hour. Setting `bearerTokenType` to `access_token` avoids this. Entra ID and Okta are not affected in either mode.

**`Auto mode’s safety check was unavailable` or `Auto mode is unavailable`, after actions that read `Blocked` or `Failed`.** The session can't read the verdicts of the provider's [Auto mode review](#auto-mode-checks). Follow the `server_unrecognized_result` row under [Auto mode check results in the diagnostic report](#auto-mode-check-results-in-the-diagnostic-report). If Code shows `Connection problem` cards instead, or Cowork shows `API Error: Connection lost mid-response` first, the responses end before the verdicts arrive. See the streaming requirement in [Context window and compaction](#context-window-and-compaction).

**Every Auto mode turn fails, and new sessions in Manual mode work.** Your gateway, or the provider behind it, rejects the requests that ask for the provider's [Auto mode review](#auto-mode-checks). The built-in safety check doesn't take over after such errors, as described in [What users see when no Auto mode verdict arrives](#what-users-see-when-no-auto-mode-verdict-arrives). For example, users see these messages, which don't name Auto mode or **Server-side Auto mode checks**:

* **`401` with a static API key**: Code shows `Credentials rejected` right away.
* **`401` where users sign in through an identity provider**: the session can first retry for a few minutes, and Code then shows `Authentication failed`.
* **`404`**: Code shows `Model isn’t available`, and Cowork shows `This model isn’t available`.
* **`500` with a `request-id` header**: the session retries for about three minutes, and Code and Cowork then show `Server error`.

Until the gateway meets [the requirements](#gateway-requirements-for-auto-mode-checks), either of these stops the failures:

* Set `inferenceGatewayAutoModeServerChecks` to `false`, as described in [Turn off server-side Auto mode checks](#turn-off-server-side-auto-mode-checks).
* Have users start new sessions in **Manual** mode, which Cowork shows as **Manually approve**. In a Code session where turns already failed, switching to **Manual** mode may not stop the failures, because the session keeps sending [the review's `anthropic-beta` value](#gateway-requirements-for-auto-mode-checks). **Plan** mode doesn't stop them: while Auto mode is available, Code sessions in **Plan** mode ask for the review too, and Claude can enter **Plan** mode on its own.

**`Automatically approve isn’t available for this task. Switched to Manually approve.` or `Couldn’t switch to Automatically approve.`** Claude Code can't run Auto mode for the Cowork task, for example because the task's model [doesn't support it](https://code.claude.com/docs/en/permission-modes#eliminate-prompts-with-auto-mode). Have the user pick a model that does, and then pick **Automatically approve**. A scheduled task keeps its stored mode, so each run on a model that doesn't support Auto mode switches again.

**Model picker is empty or missing models.** Check your gateway's `GET /v1/models` response and your `inferenceModels` list (see [Models](#models)). When `/v1/models` is unreachable or returns an error, the picker falls back to the `inferenceModels` list; if that list is empty, so is the picker.

**Chat conversations and Cowork tasks fail with `SSL certificate verification failed (UNABLE_TO_VERIFY_LEAF_SIGNATURE)`.** Claude Code, which runs these sessions, couldn't find the certificate authority (CA) that issued your gateway's certificate. A gateway that doesn't send its intermediate certificate and a private CA that the device doesn't trust can both produce this message. A passing connection test in the app doesn't rule out a missing intermediate certificate, because the app can fetch one itself and Claude Code can't.

To see which certificates your gateway sends, run this command in a terminal on a machine that connects to the gateway directly. Use your gateway's host name in place of `llm-gateway.example.corp`:

```bash theme={null}
openssl s_client -connect llm-gateway.example.corp:443 -servername llm-gateway.example.corp -showcerts </dev/null
```

If the output doesn't include the intermediate certificate that issued the gateway's certificate, configure the gateway, or the load balancer in front of it, to send its full certificate chain. For a private CA, see [TLS-intercepting proxies](https://claude.com/docs/third-party/claude-desktop/network-proxy.md#tls-intercepting-proxies).

**The 1M context window entry does not appear in the picker.** `supports1m` takes effect only when the entry's `name` matches the model ID the picker uses. Setting it on a bare alias (for example `sonnet`) while discovery returns full model IDs produces no match. Set `supports1m` on an entry whose `name` is the exact ID your gateway's `/v1/models` endpoint returns. With `prefer1m` or `modelPrefer1mContext` set, a model whose `name` matches has one entry and no **1M context window** label.

**`Your context window is full`.** The app shows this card when Claude Code reports `Prompt is too long · automatic compaction failed: …`. A session tried to shorten the conversation by summarizing it (compacting), and the summary request failed. In Chat and Cowork, the card also reads `Couldn’t compact this conversation to free up space. Try again, or start a new session.` On Claude Desktop versions earlier than 2.37337, a Cowork session shows `This conversation is too long to continue. Start a new session, or remove some tools to free up space.` for the same failure. The conversation isn't lost:

* **Code**: before the card appears, the session runs `/compact` itself, up to two times. If one run succeeds, Claude continues with no action from the user.
* **Chat and Cowork**: after you fix the cause, **Try again** compacts the conversation and finishes the stopped turn. While summary requests still fail, **Go back** removes the user's last message and puts its text back in the message box, so the user can go on with a smaller request.

After you fix the cause, the user's next message in the same session also retries compaction. The error the summary request returned is in the gateway's logs as the response to the session's last `POST /v1/messages` request before the failure. Match it to a cause as follows.

* **A timeout, `504`, or `524`**: a proxy or load balancer on the route closed the summary response before it finished. See the streaming requirement in [Context window and compaction](#context-window-and-compaction).
* **`401`, `402`, or `403`**: the gateway credential expired, or the gateway's quota for the user is spent. Have the user sign in again or issue a new key, or raise the quota.
* **`API returned an empty or malformed response`**: after certain streaming failures, such as a stream that stops partway, Claude Code sends the summary request again with the `stream` field set to `false`. This message means that the non-streaming request got a success status but a body that wasn't a Messages API response, for example an empty body, an HTML page, a stream of server-sent events, or JSON in another format. Find that request in the gateway's logs and check what the gateway returned for it. If the request isn't in the logs, something in front of the gateway, such as a proxy, firewall, or sign-in page, answered it.
* **`400` with your gateway's own error text**: the gateway rejected the summary request itself, for example on a request-size or token limit of its own. Raise or remove that limit for these requests.

On a routing alias or another model ID that sessions don't recognize, a session compacts near 200K tokens, even when your provider accepts more. To declare a larger window, see [Context window for unrecognized model IDs](#context-window-for-unrecognized-model-ids). Then have the user relaunch Claude Desktop and start a new session. If you already set `supports1m` or marked the model, check that your gateway accepts the header value, as described in [Context window and compaction](#context-window-and-compaction).

For `Prompt is too long` without `automatic compaction failed`, or your gateway's own request-too-large error shown in the session, check the `usage` and error-forwarding requirements in [Context window and compaction](#context-window-and-compaction) first. [Prompt is too long](https://code.claude.com/docs/en/errors#prompt-is-too-long) in the Claude Code error reference covers the other causes.

**Every message in one conversation fails, and new conversations work.** In the gateway's logs, find the provider's response to one of the failed requests. If its message says that a thinking block is `bound to a different conversation`, compare it with the response that your gateway returned for that request. If the status code or the error body differs, see [Gateway requirements for preserved thinking](#gateway-requirements-for-preserved-thinking). Once your gateway forwards the error unchanged, the user's next message in the same conversation goes through.
