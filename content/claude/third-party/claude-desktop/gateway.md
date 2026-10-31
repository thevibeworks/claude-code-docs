> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Deploy Claude Desktop on 3P with an LLM gateway

> Configure Claude Desktop on 3P to use Claude models on a self-hosted gateway that implements the Anthropic Messages API

To use a self-hosted LLM gateway (for example LiteLLM, Portkey, or an in-house proxy) as the inference provider, set `inferenceProvider` to `gateway` and supply the base URL and credentials described below.

The gateway must implement the Anthropic [Messages API](https://docs.claude.com/en/api/messages):

* `POST /v1/messages` with [streaming](https://docs.claude.com/en/api/streaming) and [tool use](https://docs.claude.com/en/docs/tool-use) is required.
* `GET /v1/models` is optional. If the gateway implements it, Claude Desktop on 3P auto-discovers available models; if not, set `inferenceModels` explicitly.

The gateway should also preserve [prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching). Cowork and Code sessions send `cache_control` breakpoints with each turn so that the provider can reuse the tool definitions, system prompt, and earlier turns of the conversation instead of reprocessing them. A gateway that forwards these fields, or translates them for its upstream provider, keeps that behavior. A gateway that strips `cache_control`, or that changes the system prompt or tool list from one request to the next, makes the provider reprocess the whole conversation on every turn at full input-token cost and higher latency. To verify, check the [usage fields](https://platform.claude.com/docs/en/build-with-claude/prompt-caching#tracking-cache-performance) your gateway returns or logs for Claude Desktop traffic: after the first request of a session, `cache_read_input_tokens` should be well above zero on most requests. If it is zero on every request, review the gateway's request transformation and caching settings for the route that serves Claude models.

In each response's `usage`, return the provider's `cache_creation` object with its `ephemeral_5m_input_tokens` and `ephemeral_1h_input_tokens` fields. Without that object, the [API request event](https://claude.com/docs/cowork/monitoring.md#api-request-event) in your OpenTelemetry export reports `0` for both `cache_creation_5m_tokens` and `cache_creation_1h_tokens`.

## Choose an authentication approach

| Scenario | Use | Notes |
| - | - | - |
| Proof of concept, or your gateway already issues per-team keys | [Static API key](#static-api-key) (`inferenceGatewayApiKey`) | A long-lived secret distributed in the managed profile. |
| Per-user attribution and identity-provider enforcement (MFA, conditional access) | [Single sign-on](#single-sign-on-with-your-identity-provider) (`inferenceGatewayOidc`) | Each user signs in with their own work account. Requires app version 1.6889.0 or later. |
| Your organization already has tooling that obtains a gateway credential | [Credential helper](https://claude.com/docs/third-party/claude-desktop/configuration.md#inferencecredentialhelper) (`inferenceCredentialHelper`) | An executable that prints the gateway credential to stdout at runtime. |

## Prepare devices

### Static API key

No per-device preparation is required. Generate an API key in your gateway and place it in the managed configuration as `inferenceGatewayApiKey` (see [Configure the app](#configure-the-app)).

### Single sign-on with your identity provider

Instead of distributing a shared gateway API key, you can have each user sign in with their own work account. The first time a user opens Claude Desktop, the app opens their browser to your organization's normal sign-in page (Microsoft Entra ID, Okta, or any OpenID Connect provider). After they sign in, the app sends a per-user token to your gateway on every request, and your gateway checks that token to confirm who the user is.

This gives you per-user attribution in your gateway logs, lets your identity provider enforce MFA and conditional access, and means there is no long-lived credential to distribute or rotate.

You need three things in place:

* An LLM gateway that can validate JSON Web Tokens (LiteLLM, Kong, Envoy, and Azure API Management all support this)
* Admin access to your identity provider to register a new application
* A way to push managed configuration to user devices (your existing MDM)

The walkthrough below uses Microsoft Entra ID. An Okta variant follows.

#### Set up single sign-on

**1. Register an application in Entra ID**

In the [Microsoft Entra admin center](https://entra.microsoft.com), go to **Identity → Applications → App registrations** and select **New registration**. Give it a name such as `Claude Desktop gateway`, choose **Accounts in this organizational directory only**, and select **Register**.

On the overview page, copy the **Application (client) ID** and **Directory (tenant) ID**. You will use both in the next two steps.

Open the **Authentication** blade, select **Add a platform**, and choose **Mobile and desktop applications**. Under **Custom redirect URIs**, add exactly:

```text theme={null}
http://127.0.0.1/callback
```

A few details that matter here: use `127.0.0.1` (not `localhost`), include the `/callback` path, and add it under the **Mobile and desktop applications** platform specifically. That platform is the only one Entra allows to use any local port, which the app needs because it picks a free port at sign-in time. You do not need a client secret or any additional API permissions.

**2. Configure your gateway to validate the token**

Tell your gateway to accept the bearer token only if it was issued by your tenant **for this application**. In LiteLLM that looks like:

```yaml theme={null}
general_settings:
  litellm_jwtauth:
    public_key_url: https://login.microsoftonline.com/YOUR_TENANT_ID/discovery/v2.0/keys
    audience: YOUR_CLIENT_ID
    user_id_jwt_field: oid
```

Replace `YOUR_TENANT_ID` and `YOUR_CLIENT_ID` with the values from step 1.

> [!WARNING]
>
> The `audience` line is required. Without it, your gateway accepts tokens issued to any application in your tenant, not just this one.

For Kong, Envoy, or Azure API Management, configure the equivalent JWT validation policy with the same JWKS URL and audience.

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

> [!NOTE]
>
> Use the **issuer** value, not the **Metadata URI**. Okta's admin console shows the metadata URI (ending in `/.well-known/openid-configuration`) prominently — that is the discovery document the app fetches *from* the issuer, not the issuer itself. If you are unsure, open the metadata URI in a browser and copy the `"issuer"` field from the JSON response. For a custom Okta authorization server the issuer is `https://YOUR_ORG.okta.com/oauth2/AUTH_SERVER_ID`.

Point your gateway's JWT validation at `https://YOUR_ORG.okta.com/oauth2/v1/keys` with `audience` set to the Okta client ID.

#### Map users at the gateway

Claude Desktop forwards the identity provider's token to your gateway verbatim — it does not add, remove, or rewrite any claims. With the default scopes (`openid profile email offline_access`), the ID token your gateway receives contains the standard OIDC `sub`, `email`, and `name` claims, plus whatever your provider includes for the `profile` scope. You can confirm exactly what is present by base64-decoding the middle segment of the `Authorization: Bearer` value your gateway receives.

Key the gateway's user record on the provider's immutable user ID rather than email, so the record survives email or name changes:

| Provider | Stable user-ID claim |
| - | - |
| Entra ID | `oid` |
| Okta and most other OIDC providers | `sub` |

If your gateway has no existing user records to preserve, the simplest setup is to auto-provision on first sign-in. For LiteLLM, extend the validation block from step 2:

```yaml theme={null}
general_settings:
  enable_jwt_auth: true
  litellm_jwtauth:
    public_key_url: https://YOUR_ORG.okta.com/oauth2/v1/keys
    audience: YOUR_CLIENT_ID
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

Per [OpenID Connect Core 1.0 §11](https://openid.net/specs/openid-connect-core-1_0.html#OfflineAccess), requesting `offline_access` signals that the client may use the refresh token while the user is not present, and the provider must obtain consent for it. Claude Desktop therefore does not add this scope to an administrator-supplied `scopes` value in the default mode, so that requesting offline access remains an explicit choice.

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

Consent required (A value that a bootstrap server or a self-hosted session host delivers applies only after the user approves it, unless machine-scoped device management set that server's address. For a bootstrap server, the trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)

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

To send additional HTTP headers on every inference request (tenant routing, org IDs, and similar), set [`inferenceCustomHeaders`](https://claude.com/docs/third-party/claude-desktop/configuration#inferencecustomheaders). It applies to all providers, not just gateways.

### Single sign-on configuration keys

Single sign-on is enabled by setting `inferenceCredentialKind` to `interactive` **and** supplying `inferenceGatewayOidc`. `interactive` alone (without `inferenceGatewayOidc`) selects a different mode where the gateway itself acts as the authorization server.

From Claude Desktop 2.7032.0, `inferenceCredentialKind: "external-idp"` with [`inferenceIdpOidc`](https://claude.com/docs/third-party/claude-desktop/configuration#inferenceidpoidc) and `inferenceIdpAuthFlow`, the keys [Amazon Bedrock identity provider sign-in](https://claude.com/docs/third-party/claude-desktop/bedrock.md#sign-in-with-your-identity-provider) uses, is an equivalent spelling of this configuration; `interactive` with `inferenceGatewayOidc` keeps working, so keep it until every device runs 2.7032.0 or later.

| Setting | MDM key | Required | Description |
| - | - | - | - |
| Credential kind | `inferenceCredentialKind` | Yes | `interactive` selects sign-in instead of an API key. |
| Gateway SSO IdP (OIDC) | `inferenceGatewayOidc` | Yes | A **single JSON object** describing the identity provider (fields below). The resulting token is sent to the gateway as the bearer credential. |
| Gateway sign-in flow | `inferenceGatewayOidcAuthFlow` | No | `browser` (the default) runs the sign-in in the system browser. `broker` runs it through the [OS identity broker](https://claude.com/docs/third-party/claude-desktop/entra-broker.md) on Windows and macOS, which requires `issuer` to be a Microsoft Entra ID issuer (`https://login.microsoftonline.com/TENANT_ID/v2.0`) and needs no loopback redirect. |

The `inferenceGatewayOidc` value is one JSON object with these fields:

| Field | Required | Description |
| - | - | - |
| `clientId` | Yes | Application (client) ID registered with the identity provider. |
| `issuer` | Yes\* | OIDC issuer URL — the base URL only, **without** `/.well-known/openid-configuration`. The app appends that path itself to discover the authorization and token endpoints. |
| `authorizationUrl` | No\* | Explicit OIDC authorization endpoint. Use together with `tokenUrl` instead of `issuer` when the identity provider does not serve `/.well-known/openid-configuration`. Ignored when `issuer` is set. |
| `tokenUrl` | No\* | Explicit OIDC token endpoint. Must be set together with `authorizationUrl`. Ignored when `issuer` is set. |
| `scopes` | No | Space-separated OIDC scopes. Defaults to `openid profile email offline_access`. Required when `bearerTokenType` is `access_token`. See [Refresh tokens and session lifetime](#refresh-tokens-and-session-lifetime) for how this field interacts with silent refresh. |
| `redirectPort` | No | Fixed local port for the loopback redirect. Leave unset to let the app choose an ephemeral port (Entra). Set when the provider requires an exact port match (Okta). |
| `redirectHost` | No | Host in the loopback redirect URI, `127.0.0.1` (the default) or `localhost`. Set to `localhost` when the identity provider accepts only `localhost` in a registered redirect URI, and register the `localhost` form of the URI instead (`http://localhost/callback`, or `http://localhost:<port>/callback` with `redirectPort`). |
| `bearerTokenType` | No | Which token the app sends to the gateway as the `Authorization: Bearer` value. `id_token` (the default) sends the OIDC ID token — the gateway validates it offline against the provider's JWKS with `aud` equal to the client ID. `access_token` sends the OAuth access token instead — use this for gateways that validate as an OAuth resource server rather than validating the ID token directly. When set to `access_token`, `scopes` is required. |
| `appendOfflineAccess` | No | Whether to automatically append `offline_access` to `scopes` in `access_token` mode. Defaults to `true`. Set to `false` only if your authorization server rejects `offline_access` as an unrecognized scope. See [Refresh tokens and session lifetime](#refresh-tokens-and-session-lifetime). |
| `resource` | No | RFC 8707 resource indicator naming the gateway as the access-token audience: an `https://` URL, or, for AD FS, one of the relying-party trust's identifiers that has a scheme, such as `https://…` or `urn:…`, spelled as it is registered. A value with no scheme is sent as `https://<value>`; an identifier with a scheme of its own is sent exactly as written. When set, the app sends `resource=<value>` on the authorization, token, and refresh requests. Use only with `bearerTokenType: "access_token"` and an identity provider that implements RFC 8707 (for example AD FS); leave unset for Microsoft Entra ID, which rejects the parameter; request the gateway's API scope in `scopes` instead. Changing it signs users in again. Ignored by the OS-broker sign-in flow (`inferenceGatewayOidcAuthFlow: broker`). |
| `additionalRedirectReferrerHosts` | No | Space-separated hostnames also accepted as the referrer of the sign-in callback, for identity providers that complete sign-in from a different host than the authorization URL's (for example a portal or step-up page on a sibling host). When a callback is rejected for a referrer mismatch, the app log names the host to add. |

\* Either `issuer`, or both `authorizationUrl` and `tokenUrl`, is required.

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

Your gateway can mark which Claude tier a model serves by returning an `anthropic_family_tier` field (a tier name such as `sonnet` or `opus`) on that model object in its `/v1/models` response, optionally with `is_family_default: true` when several models map to the same tier. The app uses the marked model when it needs that tier, for example to resolve a bare `sonnet` alias. The app also reads other optional fields on each model object. `display_name` sets the picker label when the app cannot derive one from the model ID. `description` adds a one-line description beneath the label (Claude Desktop 1.49585.0 or later). `supports_1m: true`, or a `max_input_tokens` value of 1,000,000 or more, marks a discovered model as supporting the 1M-token context window, as `supports1m` does on an `inferenceModels` entry.

If your gateway doesn't implement `GET /v1/models`, give every `inferenceModels` entry the full model ID your gateway accepts. When every entry is a full model ID, the app skips the `/v1/models` call automatically. A bare tier alias such as `sonnet` can't be resolved without discovery, so a list that contains one keeps discovery on. On earlier app versions that don't skip the call automatically, also set [`modelDiscoveryEnabled`](https://claude.com/docs/third-party/claude-desktop/configuration#modeldiscoveryenabled) to `false`. If discovery stays on, a gateway that answers the call with an error makes the app fall back to the `inferenceModels` list immediately. A gateway that accepts the call and hangs delays the model list by up to 10 seconds at launch.

A session assumes 200K tokens for a model ID it doesn't recognize as having a native 1M context window (see [Context window and compaction](#context-window-and-compaction)). If your deployment supports the 1M-token context window for that model, set `supports1m: true` on its entry:

```json theme={null}
[{"name": "bedrock/us.anthropic.claude-opus-4-6-v1", "supports1m": true}]
```

The model picker then shows a second entry for the model, described as **1M context window**. The default selection is unchanged. If the gateway doesn't accept 1M-token requests for that model, requests made from the 1M picker entry fail at inference time. Only set `supports1m` on models you have confirmed against your deployment. The [Models section of the configuration reference](https://claude.com/docs/third-party/claude-desktop/configuration.md#models) documents the remaining entry fields, including display labels and tier mapping.

To show a model as one entry, add `prefer1m: true` next to `supports1m` on its entry, or use [`modelPrefer1mContext`](https://claude.com/docs/third-party/claude-desktop/configuration#modelprefer1mcontext), as described under [Model list and default model](https://claude.com/docs/third-party/claude-desktop/models.md#model-list-and-default-model).

### Context window and compaction

Cowork and Code sessions keep a long conversation within the model's context window by compacting it. To compact, the session sends one request that asks the model to summarize the conversation so far, then continues from the summary. Through a gateway, a session can't read the model's real context window from the provider, so it assumes one from the model ID and the picker entry:

* **Standard entry**: 1M tokens for a model the session recognizes as having a native 1M context window, as listed under [the context window behind a gateway](https://code.claude.com/docs/en/model-config#context-window-behind-a-gateway) in the Claude Code documentation, and 200K tokens for every other model ID, including an ID the session doesn't recognize whose `inferenceModels` entry doesn't set [`behavesAs`](https://claude.com/docs/third-party/claude-desktop/models#map-an-unrecognized-model-id-to-a-claude-model). On Claude Desktop versions earlier than 2.19675.0, a session assumes 200K tokens on this entry for every model.
* **1M context window entry**, or the single entry from `prefer1m` or `modelPrefer1mContext`: 1M tokens, regardless of the model ID.

If the gateway or the provider accepts less than the window a session assumes, requests past that limit fail. The session then compacts and retries only when the provider's too-long error reaches it unchanged. To make sessions compact earlier than the window they assume, for example when your provider serves a natively 1M model with only a 200K window, see [Set the auto-compact window](https://code.claude.com/docs/en/model-config#set-the-auto-compact-window) in the Claude Code documentation. For a model ID the session doesn't recognize, see [Correct the window for a gateway or custom model ID](https://code.claude.com/docs/en/model-config#correct-the-window-for-a-gateway-or-custom-model-id).

The following table lists what the model configuration and the gateway need to provide so that sessions use the full context window and compact when they reach it, and how to check each requirement.

| Requirement | What fails without it | How to check |
| - | - | - |
| Set `supports1m`, or mark the model in discovery (see [Models](#models)), for each model your provider serves with a 1M-token context window but a session assumes 200K tokens for. Also accept the `context-1m-2025-08-07` value in the `anthropic-beta` request header. | Sessions on such a model's standard picker entry assume a 200K-token window, even when the provider accepts 1M. A gateway that rejects the header value fails every request made from the **1M context window** entry. | From a session on the **1M context window** entry, confirm in the gateway's logs that requests carry the header value and that requests above 200K input tokens succeed. |
| [Stream responses](https://code.claude.com/docs/en/llm-gateway-protocol#streaming) through without buffering, including the provider's SSE `ping` events, and set the response timeout on every proxy and load balancer on the route longer than your slowest complete response. | The summary request carries the whole conversation, and while the provider works on it, pings can be the only bytes on the connection. If a proxy buffers them, the session sees no bytes and gives up after about five minutes, and if a proxy's response timeout is shorter than the response takes, it ends the request with its own error, such as `504`. | Run a streaming request with `curl -N` against the hostname clients use and confirm that events print as they are generated, not in one burst at the end. |
| Return the provider's `usage` object unchanged on every response, including `cache_creation_input_tokens` and `cache_read_input_tokens`. | The session counts the conversation's tokens from the `usage` of the latest response. With the cache fields missing it undercounts, and requests reach the provider's limit before the session compacts. | Compare the `usage` object in the gateway's upstream response log with the one the client receives for the same request. They should be identical, and where the provider supports prompt caching, `cache_read_input_tokens` is above zero after the first turn. |
| [Forward the provider's status code and error body unchanged](https://code.claude.com/docs/en/llm-gateway-protocol#automatic-retry-and-error-forwarding) when it rejects a request. | Where the provider's too-long error is the compaction trigger, the session compacts and retries only if that error reaches it unchanged. With a rewritten error, the session shows the error and doesn't compact. | Send an oversized request through the gateway and confirm that the client receives the provider's status code and error body. |

On a response that delivers only keep-alive pings, a session accepts about five minutes of pings and then waits [`inferenceStreamIdleTimeoutSec`](https://claude.com/docs/third-party/claude-desktop/configuration#inferencestreamidletimeoutsec) seconds more for model output (300 by default, so about ten minutes in all). Raise that key if your provider needs longer than that before its first output on a large request.

### MCP tool search

[MCP tool search](https://code.claude.com/docs/en/mcp#scale-with-mcp-tool-search) loads MCP tool schemas on demand instead of inlining every schema into the context window. It reduces context pressure when many MCP tools are configured (sessions that otherwise compact every turn or two).

On gateway deployments, Claude Desktop turns tool search off by default, along with Claude Code's other experimental beta features, because strict gateways reject the experimental `anthropic-beta` request headers and request fields those features add. The same applies to Microsoft Foundry deployments and to any provider configured with a custom base URL. Setting the `ENABLE_TOOL_SEARCH` environment variable to `true` does not lift this suppression. To turn tool search on for these deployments, set the [`toolSearchEnabled`](https://claude.com/docs/third-party/claude-desktop/configuration#toolsearchenabled) configuration key. Requires app version 1.21459.0 or later.

On Claude API, Google Cloud's Agent Platform, Amazon Bedrock, and Amazon Bedrock Mantle deployments with no custom base URL, tool search is on by default from Claude Desktop 1.49585.0 and `toolSearchEnabled` is not needed. These versions leave Claude Code's experimental beta features on for those providers, as terminal Claude Code does (on Google Cloud's Agent Platform, tool search applies to Claude 4.5 and newer models). To turn tool search off on these deployments, set `ENABLE_TOOL_SEARCH` to `false` in the `env` block of OS-level [Claude Code managed settings](https://code.claude.com/docs/en/settings#settings-files), with [`parentSettingsBehavior`](https://claude.com/docs/third-party/claude-desktop/code) set to `merge`. On earlier app versions these providers also have tool search off by default, and `toolSearchEnabled` turns it on.

> [!WARNING]
>
> Setting `toolSearchEnabled` causes sessions to send experimental request headers and fields to your gateway or provider. On gateway deployments running Claude Desktop 1.40609.0 or later this is only the tool-search request shape (the `tool-search-tool-2025-10-19` value in the `anthropic-beta` header, deferred tool loading, and `tool_reference` content blocks), and every other experimental Claude Code beta stays off. On earlier versions, on Microsoft Foundry, and on providers behind a custom base URL, the key instead lifts the experimental-beta suppression for these sessions, so requests also carry Claude Code's other experimental beta headers and fields for that provider. Enable it only if your gateway forwards and accepts what it will receive; when it does not, requests fail with HTTP 400. LiteLLM in passthrough mode and Cloudflare AI Gateway both forward `anthropic-beta` headers and `tool_reference` content blocks.

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

With these status codes, users see a general error or a card about a different problem, and Code's card hides or drops your message.

* **`429`**: Claude Desktop can retry for about three minutes or longer before it shows an error, unless the response carries `x-should-retry: false`. Code then shows **Server is temporarily limiting requests**.
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

**Model picker is empty or missing models.** Check your gateway's `GET /v1/models` response and your `inferenceModels` list (see [Models](#models)). When `/v1/models` is unreachable or returns an error, the picker falls back to the `inferenceModels` list; if that list is empty, so is the picker.

**Chat conversations and Cowork tasks fail with `SSL certificate verification failed (UNABLE_TO_VERIFY_LEAF_SIGNATURE)`.** Claude Code, which runs these sessions, couldn't find the certificate authority (CA) that issued your gateway's certificate. A gateway that doesn't send its intermediate certificate and a private CA that the device doesn't trust can both produce this message. A passing connection test in the app doesn't rule out a missing intermediate certificate, because the app can fetch one itself and Claude Code can't.

To see which certificates your gateway sends, run this command in a terminal on a machine that connects to the gateway directly. Use your gateway's host name in place of `llm-gateway.example.corp`:

```bash theme={null}
openssl s_client -connect llm-gateway.example.corp:443 -servername llm-gateway.example.corp -showcerts </dev/null
```

If the output doesn't include the intermediate certificate that issued the gateway's certificate, configure the gateway, or the load balancer in front of it, to send its full certificate chain. For a private CA, see [TLS-intercepting proxies](https://claude.com/docs/third-party/claude-desktop/network-proxy.md#tls-intercepting-proxies).

**The 1M context window entry does not appear in the picker.** `supports1m` takes effect only when the entry's `name` matches the model ID the picker uses. Setting it on a bare alias (for example `sonnet`) while discovery returns full model IDs produces no match. Set `supports1m` on an entry whose `name` is the exact ID your gateway's `/v1/models` endpoint returns. With `prefer1m` or `modelPrefer1mContext` set, a model whose `name` matches has one entry and no **1M context window** label.

**`Your context window is full` in a Code session, or `Couldn’t compact this conversation to free up space. Try again, or start a new session.` in a Cowork session.** The app shows these when Claude Code reports `Prompt is too long · automatic compaction failed: …`, meaning a session tried to compact the conversation and the summary request failed. On Claude Desktop versions earlier than 2.37337, a Cowork session shows `This conversation is too long to continue. Start a new session, or remove some tools to free up space.` for the same failure. The conversation isn't lost. After you fix the cause, the user's next message in the same session retries compaction. The error the summary request returned is in the gateway's logs as the response to the session's last `POST /v1/messages` request before the failure. Match it to a cause as follows.

* **A timeout, `504`, or `524`**: a proxy or load balancer on the route closed the summary response before it finished. See the streaming requirement in [Context window and compaction](#context-window-and-compaction).
* **`401`, `402`, or `403`**: the gateway credential expired, or the gateway's quota for the user is spent. Have the user sign in again or issue a new key, or raise the quota.
* **`API returned an empty or malformed response`**: after certain streaming failures, such as a stream that stops partway, Claude Code sends the summary request again with the `stream` field set to `false`. This message means that the non-streaming request got a success status but a body that wasn't a Messages API response, for example an empty body, an HTML page, a stream of server-sent events, or JSON in another format. Find that request in the gateway's logs and check what the gateway returned for it. If the request isn't in the logs, something in front of the gateway, such as a proxy, firewall, or sign-in page, answered it.
* **`400` with your gateway's own error text**: the gateway rejected the summary request itself, for example on a request-size or token limit of its own. Raise or remove that limit for these requests.

For `Prompt is too long` without `automatic compaction failed`, or your gateway's own request-too-large error shown in the session, check the `usage` and error-forwarding requirements in [Context window and compaction](#context-window-and-compaction) first. [Prompt is too long](https://code.claude.com/docs/en/errors#prompt-is-too-long) in the Claude Code error reference covers the other causes.
