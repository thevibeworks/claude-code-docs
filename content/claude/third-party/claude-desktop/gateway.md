> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Deploy Claude Desktop on 3P with an LLM gateway

> Configure Claude Desktop on 3P to use Claude models on a self-hosted gateway that implements the Anthropic Messages API

To use a self-hosted LLM gateway (for example LiteLLM, Portkey, or an in-house proxy) as the inference provider, set `inferenceProvider` to `gateway` and supply the base URL and credentials described below.

The gateway must implement the Anthropic [Messages API](https://docs.claude.com/en/api/messages):

* `POST /v1/messages` with [streaming](https://docs.claude.com/en/api/streaming) and [tool use](https://docs.claude.com/en/docs/tool-use) is required.
* `GET /v1/models` is optional. If the gateway implements it, Claude Desktop on 3P auto-discovers available models; if not, set `inferenceModels` explicitly.

## Choose an authentication approach

| Scenario                                                                         | Use                                                                                                                    | Notes                                                                                   |
| -------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| Proof of concept, or your gateway already issues per-team keys                   | [Static API key](#static-api-key) (`inferenceGatewayApiKey`)                                                           | A long-lived secret distributed in the managed profile.                                 |
| Per-user attribution and identity-provider enforcement (MFA, conditional access) | [Single sign-on](#single-sign-on-with-your-identity-provider) (`inferenceGatewayOidc`)                                 | Each user signs in with their own work account. Requires app version 1.6889.0 or later. |
| Your organization already has tooling that obtains a gateway credential          | [Credential helper](/docs/third-party/claude-desktop/configuration#inferencecredentialhelper) (`inferenceCredentialHelper`) | An executable that prints the gateway credential to stdout at runtime.                  |

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

<Steps>
  <Step title="Register an application in Entra ID">
    In the [Microsoft Entra admin center](https://entra.microsoft.com), go to **Identity → Applications → App registrations** and select **New registration**. Give it a name such as `Claude Desktop gateway`, choose **Accounts in this organizational directory only**, and select **Register**.

    On the overview page, copy the **Application (client) ID** and **Directory (tenant) ID**. You will use both in the next two steps.

    Open the **Authentication** blade, select **Add a platform**, and choose **Mobile and desktop applications**. Under **Custom redirect URIs**, add exactly:

    ```text theme={null}
    http://127.0.0.1/callback
    ```

    A few details that matter here: use `127.0.0.1` (not `localhost`), include the `/callback` path, and add it under the **Mobile and desktop applications** platform specifically. That platform is the only one Entra allows to use any local port, which the app needs because it picks a free port at sign-in time. You do not need a client secret or any additional API permissions.
  </Step>

  <Step title="Configure your gateway to validate the token">
    Tell your gateway to accept the bearer token only if it was issued by your tenant **for this application**. In LiteLLM that looks like:

    ```yaml theme={null}
    general_settings:
      litellm_jwtauth:
        public_key_url: https://login.microsoftonline.com/YOUR_TENANT_ID/discovery/v2.0/keys
        audience: YOUR_CLIENT_ID
        user_id_jwt_field: oid
    ```

    Replace `YOUR_TENANT_ID` and `YOUR_CLIENT_ID` with the values from step 1.

    <Warning>
      The `audience` line is required. Without it, your gateway accepts tokens issued to any application in your tenant, not just this one.
    </Warning>

    For Kong, Envoy, or Azure API Management, configure the equivalent JWT validation policy with the same JWKS URL and audience.
  </Step>

  <Step title="Configure in the app">
    Open the [in-app configuration window](/docs/third-party/claude-desktop/in-app-configuration#open-the-configuration-window) (**Developer → Configure Third-Party Inference…**). In the **Connection** section, set **Inference provider** to **Gateway** and **Credential kind** to **Interactive sign-in**. This hides the API-key field and reveals **Gateway SSO IdP (OIDC)**:

    | Field                                  | Value                                                   |
    | -------------------------------------- | ------------------------------------------------------- |
    | Gateway base URL                       | `https://llm-gateway.example.corp`                      |
    | Credential kind                        | **Interactive sign-in**                                 |
    | Gateway SSO IdP (OIDC) → Client ID     | `YOUR_CLIENT_ID`                                        |
    | Gateway SSO IdP (OIDC) → Issuer URL    | `https://login.microsoftonline.com/YOUR_TENANT_ID/v2.0` |
    | Gateway SSO IdP (OIDC) → Scopes        | *leave empty for the default*                           |
    | Gateway SSO IdP (OIDC) → Redirect port | *leave empty*                                           |

    Then click **Export** to produce a `.mobileconfig` (macOS) or `.reg` (Windows) file for your MDM. See [Deploy with MDM](/docs/third-party/claude-desktop/mdm) for the export and deployment workflow.

    When a user next opens Claude Desktop, they see a **Sign in to your organization** button. Clicking it opens their browser to your Entra sign-in page; once they approve, they return to the app and can start working. The app keeps them signed in and refreshes the token in the background. If the session is revoked or expires under your tenant's policy, the app shows a **Sign in again** prompt; clicking it reopens the sign-in page in the browser.
  </Step>
</Steps>

#### Using Okta instead

In the Okta Admin Console, create a **Native** application with the **Authorization Code** and **Refresh Token** grant types. Okta requires the redirect URI to match exactly, including the port, so pick a fixed port (for example `53180`), register `http://127.0.0.1:53180/callback`, and set that same port in **Gateway SSO IdP (OIDC)**:

| Field         | Value                         |
| ------------- | ----------------------------- |
| Client ID     | `YOUR_CLIENT_ID`              |
| Issuer URL    | `https://YOUR_ORG.okta.com`   |
| Scopes        | *leave empty for the default* |
| Redirect port | `53180`                       |

<Note>
  Use the **issuer** value, not the **Metadata URI**. Okta's admin console shows the metadata URI (ending in `/.well-known/openid-configuration`) prominently — that is the discovery document the app fetches *from* the issuer, not the issuer itself. If you are unsure, open the metadata URI in a browser and copy the `"issuer"` field from the JSON response. For a custom Okta authorization server the issuer is `https://YOUR_ORG.okta.com/oauth2/AUTH_SERVER_ID`.
</Note>

Point your gateway's JWT validation at `https://YOUR_ORG.okta.com/oauth2/v1/keys` with `audience` set to the Okta client ID.

#### Map users at the gateway

Claude Desktop forwards the identity provider's token to your gateway verbatim — it does not add, remove, or rewrite any claims. With the default scopes (`openid profile email offline_access`), the ID token your gateway receives contains the standard OIDC `sub`, `email`, and `name` claims, plus whatever your provider includes for the `profile` scope. You can confirm exactly what is present by base64-decoding the middle segment of the `Authorization: Bearer` value your gateway receives.

Key the gateway's user record on the provider's immutable user ID rather than email, so the record survives email or name changes:

| Provider                           | Stable user-ID claim |
| ---------------------------------- | -------------------- |
| Entra ID                           | `oid`                |
| Okta and most other OIDC providers | `sub`                |

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

**Authorization servers that reject `offline_access`.** Standard OIDC providers (Entra ID, Okta, Auth0) accept `offline_access` and require it to issue a refresh token, so the automatic append is what you want. If your authorization server instead rejects unrecognized scopes with an `invalid_scope` error — for example, servers that issue refresh tokens via a provider-specific scope rather than `offline_access` — set `appendOfflineAccess` to `false` and include your provider's own refresh-token scope in `scopes` directly.

Refresh tokens govern whether users are re-prompted to sign in, not how long a sign-in may stay valid. To cap the sign-in lifetime under your identity provider's session policy, set [`inferenceSessionLifetimeSec`](/docs/third-party/claude-desktop/configuration#inferencesessionlifetimesec); Claude Desktop shows a re-authenticate banner before the session expires.

## Configure the app

Open the [in-app configuration window](/docs/third-party/claude-desktop/in-app-configuration#open-the-configuration-window) (**Developer → Configure Third-Party Inference…**). In the **Connection** section, set **Inference provider** to **Gateway**, then fill in the **Gateway credentials** card:

| Field               | Value                                                                                                                      |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| Gateway base URL    | `https://llm-gateway.example.corp`                                                                                         |
| Gateway API key     | your gateway key (or a placeholder if your gateway has none)                                                               |
| Credential kind     | **Static API key** (default), or **Interactive sign-in** for [single sign-on](#single-sign-on-with-your-identity-provider) |
| Gateway auth scheme | **Bearer** (default) or **x-api-key**                                                                                      |

Then click **Export** to produce a `.mobileconfig` (macOS) or `.reg` (Windows) file for your MDM. See [Deploy with MDM](/docs/third-party/claude-desktop/mdm) for the export and deployment workflow.

### Configuration keys

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

    ```yaml theme={null} theme={null} theme={null} theme={null} theme={null}
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

To send additional HTTP headers on every inference request (tenant routing, org IDs, and similar), set [`inferenceCustomHeaders`](/docs/third-party/claude-desktop/configuration#inferencecustomheaders). It applies to all providers, not just gateways.

### Single sign-on configuration keys

Single sign-on is enabled by setting `inferenceCredentialKind` to `interactive` **and** supplying `inferenceGatewayOidc`. Both are required — `interactive` alone (without `inferenceGatewayOidc`) selects a different mode where the gateway itself acts as the authorization server.

| Setting                | MDM key                        | Required                    | Description                                                                                                                                                                                                                                                                                                                      |
| ---------------------- | ------------------------------ | --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Credential kind        | `inferenceCredentialKind`      | Yes — must be `interactive` | Selects sign-in instead of an API key.                                                                                                                                                                                                                                                                                           |
| Gateway SSO IdP (OIDC) | `inferenceGatewayOidc`         | Yes                         | A **single JSON object** describing the identity provider (fields below). The resulting token is sent to the gateway as the bearer credential.                                                                                                                                                                                   |
| Sign-in flow           | `inferenceGatewayOidcAuthFlow` | No                          | `browser` (the default) runs the sign-in in the system browser. `broker` runs it through the [OS identity broker](/docs/third-party/claude-desktop/entra-broker) on Windows and macOS, which requires `issuer` to be a Microsoft Entra ID issuer (`https://login.microsoftonline.com/TENANT_ID/v2.0`) and needs no loopback redirect. |

The `inferenceGatewayOidc` value is one JSON object with these fields:

| Field                             | Required | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| --------------------------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `clientId`                        | Yes      | Application (client) ID registered with the identity provider.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `issuer`                          | Yes\*    | OIDC issuer URL — the base URL only, **without** `/.well-known/openid-configuration`. The app appends that path itself to discover the authorization and token endpoints.                                                                                                                                                                                                                                                                                                                                                                                                  |
| `authorizationUrl`                | No\*     | Explicit OIDC authorization endpoint. Use together with `tokenUrl` instead of `issuer` when the identity provider does not serve `/.well-known/openid-configuration`. Ignored when `issuer` is set.                                                                                                                                                                                                                                                                                                                                                                        |
| `tokenUrl`                        | No\*     | Explicit OIDC token endpoint. Must be set together with `authorizationUrl`. Ignored when `issuer` is set.                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `scopes`                          | No       | Space-separated OIDC scopes. Defaults to `openid profile email offline_access`. Required when `bearerTokenType` is `access_token`. See [Refresh tokens and session lifetime](#refresh-tokens-and-session-lifetime) for how this field interacts with silent refresh.                                                                                                                                                                                                                                                                                                       |
| `redirectPort`                    | No       | Fixed local port for the loopback redirect. Leave unset to let the app choose an ephemeral port (Entra). Set when the provider requires an exact port match (Okta).                                                                                                                                                                                                                                                                                                                                                                                                        |
| `bearerTokenType`                 | No       | Which token the app sends to the gateway as the `Authorization: Bearer` value. `id_token` (the default) sends the OIDC ID token — the gateway validates it offline against the provider's JWKS with `aud` equal to the client ID. `access_token` sends the OAuth access token instead — use this for gateways that validate as an OAuth resource server rather than validating the ID token directly. When set to `access_token`, `scopes` is required.                                                                                                                    |
| `appendOfflineAccess`             | No       | Whether to automatically append `offline_access` to `scopes` in `access_token` mode. Defaults to `true`. Set to `false` only if your authorization server rejects `offline_access` as an unrecognized scope. See [Refresh tokens and session lifetime](#refresh-tokens-and-session-lifetime).                                                                                                                                                                                                                                                                              |
| `resource`                        | No       | RFC 8707 resource indicator: an absolute `https://` URL identifying the gateway as the access-token audience. When set, the app sends `resource=<value>` on the authorization, token, and refresh requests. Use only with `bearerTokenType: "access_token"` and an identity provider that implements RFC 8707 (for example AD FS); leave unset for Microsoft Entra ID, which rejects the parameter; request the gateway's API scope in `scopes` instead. Changing it signs users in again. Ignored by the OS-broker sign-in flow (`inferenceGatewayOidcAuthFlow: broker`). |
| `additionalRedirectReferrerHosts` | No       | Space-separated hostnames also accepted as the referrer of the sign-in callback, for identity providers that complete sign-in from a different host than the authorization URL's (for example a portal or step-up page on a sibling host). When a callback is rejected for a referrer mismatch, the app log names the host to add.                                                                                                                                                                                                                                         |

\* Either `issuer`, or both `authorizationUrl` and `tokenUrl`, is required.

<Warning>
  `inferenceGatewayOidc` is **one MDM key whose value is a JSON string** — not separate keys like `inferenceGatewayOidc.clientId`. See [how object-typed keys are encoded](/docs/third-party/claude-desktop/configuration#value-types). The in-app **Export** produces the correct format automatically.
</Warning>

In a macOS `.mobileconfig` payload (Okta example):

```xml theme={null}
<key>inferenceCredentialKind</key>
<string>interactive</string>
<key>inferenceGatewayOidc</key>
<string>{"issuer":"https://YOUR_ORG.okta.com","clientId":"YOUR_CLIENT_ID","redirectPort":53180}</string>
```

Earlier app versions used `inferenceGatewayAuthScheme: "sso"` to select this mode. That value is deprecated; set `inferenceCredentialKind: "interactive"` instead. Existing deployments that still send `inferenceGatewayAuthScheme: "sso"` continue to work.

### Models

When `inferenceModels` is unset, Claude Desktop on 3P populates the model picker from your gateway's `GET /v1/models` response. Auto-discovery shows only models whose IDs are recognizably Claude; if your gateway advertises models under opaque aliases, set `inferenceModels` explicitly. Set [`inferenceModels`](/docs/third-party/claude-desktop/configuration#models) to override discovery with an explicit list — the picker will show exactly the entries you provide. Use the model IDs your gateway expects (for example `bedrock/us.anthropic.claude-opus-5` for a LiteLLM-style routing prefix).

If your gateway serves a Claude model under an opaque routing alias, it can mark the model as Claude by returning an `anthropic_family_tier` field (a Claude tier name such as `sonnet` or `opus`) on that model object in its `/v1/models` response, optionally with `is_family_default: true` when several models map to the same tier. Models marked this way pass the auto-discovery filter.

If your gateway does not implement `GET /v1/models`, give every `inferenceModels` entry the full model ID your gateway accepts; bare tier aliases such as `sonnet` rely on discovery to resolve. When every entry is a full model ID, the app skips the `/v1/models` call automatically. A list that contains a bare alias keeps discovery on, so for a gateway without the endpoint, replace the alias with the full model ID; a bare alias cannot be resolved without discovery. On earlier app versions that do not skip the call automatically, also set [`modelDiscoveryEnabled`](/docs/third-party/claude-desktop/configuration#modeldiscoveryenabled) to `false` to avoid the discovery attempt. The cost of leaving discovery on without the endpoint depends on how the gateway fails: an error response makes the app fall back to the `inferenceModels` list immediately, while an endpoint that accepts the request and hangs delays the model list by up to 10 seconds at launch.

If your deployment supports the 1M-token context window for a model, set `supports1m: true` on that model's entry:

```json theme={null}
[{"name": "bedrock/us.anthropic.claude-opus-5", "supports1m": true}]
```

The model picker then shows a second entry for the model, described as **1M context window**; the standard entry has no context-size label, and the default selection is unchanged. `supports1m` is an assertion about your gateway rather than something the app can verify: if the gateway does not accept 1M-token requests for that model, requests made from the 1M picker entry fail at inference time. Only set it on models you have confirmed against your deployment. The [Models section of the configuration reference](/docs/third-party/claude-desktop/configuration#models) documents the remaining entry fields, including display labels and tier mapping.

### MCP tool search

[MCP tool search](https://code.claude.com/docs/en/mcp#scale-with-mcp-tool-search) loads MCP tool schemas on demand instead of inlining every schema into the context window. It reduces context pressure when many MCP tools are configured (sessions that otherwise compact every turn or two). Claude Desktop on 3P turns it off by default, along with Claude Code's other experimental beta features, because strict gateways reject the experimental `anthropic-beta` request headers and request fields those features add. This suppression takes precedence over the `ENABLE_TOOL_SEARCH` environment variable, so setting that variable has no effect on Claude Desktop sessions. The variable applies only to terminal Claude Code running outside Claude Desktop.

To turn tool search on for Claude Desktop, set the [`toolSearchEnabled`](/docs/third-party/claude-desktop/configuration#toolsearchenabled) configuration key. Requires app version 1.21459.0 or later.

<Warning>
  Setting `toolSearchEnabled` causes sessions to send experimental `anthropic-beta` request headers, and the beta request fields that ride with them, to your gateway. Enable it only if your gateway forwards and accepts those headers and fields; when it does not, requests fail with HTTP 400. LiteLLM in passthrough mode and Cloudflare AI Gateway both forward `anthropic-beta` headers and `tool_reference` content blocks. As a preflight, run terminal Claude Code through the same gateway with `ENABLE_TOOL_SEARCH=true`: Claude Desktop sends the same request surface, so if the terminal works, Claude Desktop will too. Enabling the key also re-enables Claude Code's other experimental beta features for these sessions. Do not enable it on [Vertex](/docs/third-party/claude-desktop/vertex) deployments: Vertex rejects the tool-search beta header.
</Warning>

## Troubleshoot

**`gateway SSO: server does not advertise device_authorization_endpoint`** — The app could not read your `inferenceGatewayOidc` value, so it fell back to treating the gateway itself as the sign-in server. Almost always this means the value is missing or not valid JSON, for example because it was written as separate dotted keys instead of one `inferenceGatewayOidc` value. Re-export from the in-app configuration window, or copy the `.mobileconfig` snippet above.

**`OIDC discovery failed (HTTP 404)` or `(HTTP 405)`** — The `issuer` value is not the issuer base URL. Most often the metadata URI (ending in `/.well-known/openid-configuration`) was pasted instead, which doubles the path. Remove that suffix so `issuer` is just `https://YOUR_ORG.okta.com` (or the equivalent for your provider).

**`no credential configured for provider "gateway": set inferenceCredentialKind or one of the credential fields`** — `inferenceCredentialKind: "interactive"` is not present in the pushed configuration.

**Browser shows "Connected" but the app reports the sign-in failed, or `Token exchange failed (HTTP 401)`** — The browser step succeeded, but the identity provider rejected the follow-up token request. This usually means the IdP application is registered as a confidential (Web) client, which expects a client secret. Claude is a public PKCE client and doesn't send one. Register a public/native client instead: **Native Application** in Okta, or the **Mobile and desktop applications** platform in Entra ID. Application type generally can't be changed after creation, so you may need to create a new one.

<Note>
  Google Workspace can be used as the identity provider, but in the default `id_token` mode Google does not issue a fresh ID token on background refresh, so users are prompted to sign in again roughly once an hour. Setting `bearerTokenType` to `access_token` avoids this. Entra ID and Okta are not affected in either mode.
</Note>

**Model picker is empty or missing models.** Auto-discovery filters out model IDs that are not recognizably Claude, so models your gateway serves under opaque aliases appear only if the gateway marks them with `anthropic_family_tier` in its `/v1/models` response or you list them in `inferenceModels` (see [Models](#models)). When `/v1/models` is unreachable or returns an error, the picker falls back to the `inferenceModels` list; if that list is empty, so is the picker.

**The 1M context window entry does not appear in the picker.** `supports1m` takes effect only when the entry's `name` matches the model ID the picker uses. Setting it on a bare alias (for example `sonnet`) while discovery returns full model IDs produces no match. Set `supports1m` on an entry whose `name` is the exact ID your gateway's `/v1/models` endpoint returns.
