> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Deploy with a bootstrap server

> Host an HTTPS endpoint that returns each user's configuration, for organizations without MDM or with role-based configuration too complex for per-group profiles

<Note>
  Requires Claude Desktop **1.10628.0** or later. Earlier builds ignore the `bootstrapUrl` keys.
</Note>

A **bootstrap server** is an HTTPS endpoint you host that authenticates each user against your identity provider and returns that user's configuration as JSON. Use it when your organization doesn't have MDM, or when configuration varies too widely for per-group profiles: per-user gateway credentials, per-team model allowlists, or per-user OpenTelemetry attribution. When one configuration or a few group-scoped profiles cover your fleet, [deploying with MDM](/docs/third-party/claude-desktop/mdm) is simpler; most MDMs support role-based distribution.

When a bootstrap response is available, it **is** the effective configuration. The MDM profile supplies the trust anchor (`bootstrapUrl`, optional `bootstrapOidc` or `bootstrapHeaders`/`bootstrapHeadersHelper`, and the `bootstrapEnabled` opt-out), and Claude Desktop does not consult MDM for any key the bootstrap server is permitted to set. A bootstrap-settable key that your response **omits** is treated as unset, not inherited from MDM, so return every key you want applied.

<Warning>
  Your bootstrap server is fully trusted. Its response can set inference credentials, the egress allowlist, MCP servers, and every other key in the [published schema](#response-schema). Treat compromise of this endpoint as credential compromise: restrict who can deploy it, log every response, and harden it as you would any secrets-issuing service.
</Warning>

Before the server can take over, each device needs the bootstrap keys that point at it. There are two ways to get them onto a device:

* **With MDM:** deploy a profile that sets `bootstrapUrl` (and `bootstrapOidc` if you use one).
* **Without MDM:** give each user a small JSON file containing those keys, which they load from **Developer → Configure Third-Party Inference… → Import configuration**.

Either way, the bootstrap server supplies everything else after the user signs in. See [Installation and setup](/docs/third-party/claude-desktop/installation) for the surrounding workflow.

If you set `deploymentOrganizationUuid`, include it in the MDM profile or imported configuration file, and return the same value in your bootstrap response, as a plain UUID without braces in both places. Claude Desktop uses the device-side value at startup to locate sessions, skills, and plugins stored on the device.

## How it works

1. Your managed configuration (MDM or imported) sets `bootstrapUrl` (and `bootstrapOidc` if you use a separate identity provider).
2. At launch, the app authenticates via one of the [modes below](#authentication) and sends `GET <bootstrapUrl>` with the resulting `Authorization: Bearer <token>` or the request headers you configured.
3. Your server validates the token, **authorizes** the caller against your directory or entitlement source, and returns a JSON object whose keys are the same managed-configuration key names documented in the [configuration reference](/docs/third-party/claude-desktop/configuration).
4. The app validates each key against the [response schema](#response-schema), drops anything it doesn't recognize or that fails validation, and applies the result as the effective configuration.
5. The response is cached in memory (until your `expiresAt`, or 1 hour by default). The app also re-polls in the background every 30 minutes with a conditional request, so an unchanged configuration costs your server a `304` (see [Caching and `expiresAt`](#caching-and-expiresat)).

If the user has not yet signed in, or the fetch fails with no cached response from this session, the app starts in a degraded state with no inference provider configured and prompts the user to sign in.

### Availability

The cached response is held **in memory only**; there is no on-disk fallback to a previous session's response. If your bootstrap server is unreachable when Claude Desktop launches, the user stays in the degraded sign-in state until the server recovers. A failed refetch *during* a running session keeps the in-memory response and retries, so an outage that starts mid-session does not disrupt active users until they relaunch.

Run the endpoint across multiple replicas or regions behind a load balancer. Do not rely on response caching for availability: responses are per-user and carry credentials (see the `Cache-Control: no-store` guidance under [Server responsibilities](#server-responsibilities)). If your configuration data lives in a database, a read replica of that store improves availability without caching responses.

A refetch that returns different values does **not** change the running session. The app keeps the configuration it launched with (inference credentials, egress allowlist, MCP servers, and renderer state such as the model picker all stay on the boot-time values), prompts the user to restart, and applies the new response when it relaunches.

Claude Desktop 1.40609.0 and later enforce that restart. Once a background re-poll returns a changed response, the user can keep working for [`relaunchEnforcementHours`](/docs/third-party/claude-desktop/configuration#relaunchenforcementhours) (1 hour by default, at most 336 hours, or `0` to require the restart at once). After that the app blocks further use until it restarts, and it relaunches on its own once it has been idle for two minutes (no Claude task running and no keyboard or pointer input). Return `relaunchEnforcementHours` in the bootstrap response to change the window. The app reads it from the newest response, so changing it does not itself require a restart.

When rotating an inference credential, keep the previous credential valid until your fleet has relaunched. For devices that are running, that is roughly the 30-minute re-poll interval plus the relaunch window. For devices that are off, it is their next launch.

## Server responsibilities

Your bootstrap endpoint is a security boundary. The response can carry inference credentials, so an unauthenticated or under-authorized endpoint leaks those credentials to anyone who can reach the URL. Host it on your private network (VPC, corporate intranet, or behind your zero-trust access proxy) rather than the public internet; reachability from managed devices is sufficient.

**Authenticate.** Verify the bearer token's signature against your identity provider's JWKS, and check `iss`, `aud`, and `exp`. Reject anything else with `401`.

**Authorize.** Verifying the token proves *who* the caller is, not that they're entitled to a configuration. Check the caller's identity claim against your directory before returning a response:

| Identity provider  | Stable per-user claim       | Group/role claim                   |
| ------------------ | --------------------------- | ---------------------------------- |
| Microsoft Entra ID | `oid` (directory object ID) | `roles` (app roles) or `groups`    |
| Okta               | `uid` or `sub`              | `groups` (via a custom claim rule) |
| Generic OIDC       | `sub`                       | provider-specific                  |

Return `403` when the token is valid but the caller is not entitled. Do not authorize on `email` or `preferred_username` alone; those claims are mutable and may be absent for guest or external-identity users.

**Key the response on the caller** when configuration needs to differ. A single default profile returned to every entitled user is valid; vary by user or group only where you need per-user credentials, model allowlists, or telemetry attribution.

### Mapping groups to profiles

The common pattern is one profile per directory group or app role. For Entra, define an app role on the registration (for example `cowork-power-user`), assign it to a group via **Enterprise applications → Users and groups**, and select the profile from the token's `roles` claim. For Okta, the equivalent is a `groups` claim on your custom authorization server; match on `payload.groups`. Moving a user between groups in your directory is picked up at the next refetch with no profile re-push to devices; the new configuration takes effect when the user's app next launches.

A reference Node.js handler showing token validation, role-based authorization, and profile selection:

```js theme={null}
import { createRemoteJWKSet, jwtVerify } from "jose";

const TENANT = process.env.ENTRA_TENANT;
const CLIENT_ID = process.env.CLIENT_ID;
const JWKS = createRemoteJWKSet(
  new URL(`https://login.microsoftonline.com/${TENANT}/discovery/v2.0/keys`),
);

const BASE = {
  inferenceProvider: "gateway",
  inferenceGatewayBaseUrl: "https://YOUR_GATEWAY_HOST",
  inferenceGatewayAuthScheme: "bearer",
};
const PROFILES = {
  default: { ...BASE, inferenceModels: ["claude-sonnet-5"] },
  power: {
    ...BASE,
    inferenceModels: ["claude-opus-5", "claude-sonnet-5"],
    coworkEgressAllowedHosts: ["pypi.org", "registry.npmjs.org"],
  },
};
const ENTITLED_ROLES = new Set(["cowork-user", "cowork-power-user"]);

export async function handleBootstrap(req, res) {
  res.set("Cache-Control", "no-store");
  const token = (req.headers.authorization ?? "").replace(/^Bearer /, "");
  let payload;
  try {
    ({ payload } = await jwtVerify(token, JWKS, {
      issuer: `https://login.microsoftonline.com/${TENANT}/v2.0`,
      audience: CLIENT_ID,
      algorithms: ["RS256"],
    }));
  } catch {
    return res.status(401).json({ error: "invalid_token" });
  }
  const roles = payload.roles ?? [];
  if (!roles.some((r) => ENTITLED_ROLES.has(r))) {
    return res.status(403).json({ error: "not_entitled" });
  }
  const profile = roles.includes("cowork-power-user")
    ? PROFILES.power
    : PROFILES.default;
  return res
    .status(200)
    .json({ ...profile, expiresAt: Date.now() + 3600_000 });
}
```

Set `Cache-Control: no-store` on the response. Without it, a reverse proxy or CDN between the app and your endpoint may cache one user's credentials and serve them to the next.

## Authentication

The bootstrap request is always authenticated: either each user signs in and the app sends their bearer token, or the device sends request headers you configure. The mode is chosen by which keys you set alongside `bootstrapUrl`:

| Mode                                                       | When to use it                                                                                                                                                                                                                                                                                                       | MDM keys                                                                                   |
| ---------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| **Separate identity provider (PKCE)**                      | Users sign in through your existing OIDC provider (Microsoft Entra ID, Okta, Ping, or any compliant provider). The app runs an OAuth authorization-code grant with PKCE in the system browser.                                                                                                                       | `bootstrapUrl` and `bootstrapOidc`                                                         |
| **Bootstrap server as authorization server (device code)** | Your bootstrap server (or the gateway it fronts) implements RFC 8414 discovery and the RFC 8628 device-code grant. One sign-in covers both the configuration fetch and inference when they share an origin.                                                                                                          | `bootstrapUrl` only                                                                        |
| **Request headers (no per-user sign-in)**                  | The endpoint authenticates the device or a service account rather than the user: a static `Authorization: Basic …` or API-key header, or a short-lived token a script on the device fetches from your secrets manager. No browser step; the response cannot vary by signed-in user unless your headers identify one. | `bootstrapUrl` and `bootstrapHeaders` and/or `bootstrapHeadersHelper` (1.32885.1 or later) |

### Separate identity provider (PKCE)

<Steps>
  <Step title="Register a public client in your identity provider">
    Register a native or public application with a loopback redirect URI and no client secret. The registration is identical to the one used for [gateway single sign-on](/docs/third-party/claude-desktop/gateway#set-up-single-sign-on); if you already have that, reuse it. See the [provider notes](#provider-notes) below for redirect-URI specifics.

    For Microsoft Entra ID, also set an **Application ID URI** on the registration (App registration → **Expose an API** → **Set**; accept the default `api://CLIENT_ID`). The `CLIENT_ID/.default` scope in the next step does not resolve without it.
  </Step>

  <Step title="Choose the scope your server will validate">
    The app sends the OAuth **access token** as the bearer. Your server validates that token's `aud`, so the scope you request must produce a token whose audience your server accepts. This is provider-specific:

    | Provider                           | Scope to request                                       | Resulting `aud`                      |
    | ---------------------------------- | ------------------------------------------------------ | ------------------------------------ |
    | Microsoft Entra ID                 | `openid offline_access CLIENT_ID/.default`             | your client ID                       |
    | Okta (custom authorization server) | `openid offline_access YOUR_API_SCOPE`                 | your authorization server's audience |
    | Generic OIDC                       | `openid offline_access` plus your API's resource scope | provider-specific                    |

    Include `offline_access` so the app receives a refresh token and can renew silently between launches.

    <Warning>
      For Entra, use the bare-GUID form `CLIENT_ID/.default`, **not** `api://CLIENT_ID/.default`. The `api://` form works on the initial authorize but fails on the refresh grant with `AADSTS90009` when the client and resource are the same application.
    </Warning>
  </Step>

  <Step title="Validate the token in your server">
    See [Server responsibilities](#server-responsibilities). What the token's `iss` and `aud` look like depends on your provider:

    | Provider                               | `iss` to expect                                      | `aud` to expect                                      | JWKS URL                                                       |
    | -------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | -------------------------------------------------------------- |
    | Microsoft Entra ID (token version `2`) | `https://login.microsoftonline.com/TENANT/v2.0`      | your client ID                                       | `https://login.microsoftonline.com/TENANT/discovery/v2.0/keys` |
    | Okta (custom authorization server)     | `https://YOUR_DOMAIN.okta.com/oauth2/AUTH_SERVER_ID` | the audience configured on that authorization server | `<issuer>/v1/keys`                                             |

    **Entra token version.** A new Entra app registration emits v1-format access tokens by default, with `iss` = `https://sts.windows.net/TENANT/` and `aud` = `api://CLIENT_ID`. Set the accepted-token-version field in the registration's **Manifest** to `2` so tokens match the table above. The portal shows this field as either `accessTokenAcceptedVersion` or `api.requestedAccessTokenVersion` depending on the manifest view; set whichever you see. If you cannot change it, your server must accept both the v1 and v2 forms.

    **Group and role claims.** Entra does not emit `groups` or `roles` in access tokens by default. Enable the groups claim under App registration → **Token configuration**, or define **App roles** and assign users via **Enterprise applications**. The `oid` claim is always present. For Okta, add a `groups` claim on your custom authorization server with a group filter.
  </Step>

  <Step title="Configure and export from Claude Desktop">
    Install Claude Desktop on an admin workstation (see [Installation](/docs/third-party/claude-desktop/installation)). From the menu bar, open **Developer → Configure Third-Party Inference…**. In the **Source** section, fill in the **Bootstrap config URL** card:

    | Field                                     | Value                                                   |
    | ----------------------------------------- | ------------------------------------------------------- |
    | Bootstrap config URL                      | `https://YOUR_BOOTSTRAP_HOST/user/bootstrap`            |
    | Bootstrap OIDC parameters → Client ID     | `YOUR_CLIENT_ID`                                        |
    | Bootstrap OIDC parameters → Issuer URL    | `https://login.microsoftonline.com/YOUR_TENANT_ID/v2.0` |
    | Bootstrap OIDC parameters → Scopes        | `openid offline_access YOUR_CLIENT_ID/.default`         |
    | Bootstrap OIDC parameters → Redirect port | leave empty for Entra; set for Okta                     |

    Click **Sign in** to test against your typed values. Once authenticated, the card shows the keys your server supplied. Click **Export** and choose the template format your MDM expects (`.mobileconfig`, ADMX, Intune OMA-URI JSON, or `.reg`). See [Deploy the configuration](/docs/third-party/claude-desktop/mdm#4-deploy-the-configuration) for per-platform instructions.
  </Step>
</Steps>

#### Provider notes

| Provider           | Redirect URI to register                                                       | Redirect port field                      | Additional setup                                                                                                                                                                           |
| ------------------ | ------------------------------------------------------------------------------ | ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Microsoft Entra ID | `http://127.0.0.1/callback` under **Mobile and desktop applications**          | Leave empty (any local port allowed)     | Manifest: set the accepted-token-version field to `2`. **Expose an API**: set the Application ID URI. **Token configuration**: add the `groups` claim if your server authorizes on groups. |
| Okta               | `http://127.0.0.1:53180/callback` (any fixed port) on a **Native** application | Set to the registered port               | Create a custom authorization server with an audience your bootstrap server validates.                                                                                                     |
| Other OIDC         | `http://127.0.0.1/callback`                                                    | Set only if exact-port match is enforced | None                                                                                                                                                                                       |

Use `127.0.0.1`, not `localhost`.

This page covers only the bootstrap sign-in. Authentication for inference is independent of bootstrap and depends on what your response provisions; see the relevant provider page ([gateway SSO](/docs/third-party/claude-desktop/gateway#single-sign-on-with-your-identity-provider), [Google Cloud's Agent Platform](/docs/third-party/claude-desktop/vertex), [Amazon Bedrock](/docs/third-party/claude-desktop/bedrock), [Microsoft Foundry](/docs/third-party/claude-desktop/foundry)).

### Bootstrap server as authorization server (device code)

Set only `bootstrapUrl` in MDM. The app discovers your authorization endpoints via RFC 8414 and runs an RFC 8628 device-code grant. The bearer is reused for inference when `inferenceGatewayBaseUrl` shares the `bootstrapUrl` origin and `inferenceCredentialKind` is `interactive`, so the user signs in once for both.

<Steps>
  <Step title="Publish RFC 8414 discovery metadata">
    Serve a metadata document under the `bootstrapUrl` path. If `bootstrapUrl` ends in `/bootstrap` or `/user/bootstrap`, that suffix is stripped to form the issuer base.

    ```text theme={null}
    GET https://YOUR_BOOTSTRAP_HOST/.well-known/oauth-authorization-server
    ```

    ```json theme={null}
    {
      "issuer": "https://YOUR_BOOTSTRAP_HOST",
      "token_endpoint": "https://YOUR_BOOTSTRAP_HOST/oauth/token",
      "device_authorization_endpoint": "https://YOUR_BOOTSTRAP_HOST/oauth/device"
    }
    ```

    Every endpoint URL must share the `bootstrapUrl` origin. Metadata that points off-origin is rejected.
  </Step>

  <Step title="Implement the device-code grant">
    `POST` to `device_authorization_endpoint` returns:

    ```json theme={null}
    {
      "device_code": "EXAMPLE-DEVICE-CODE-OPAQUE-TO-CLIENT",
      "user_code": "ABCD-EFGH",
      "verification_uri": "https://YOUR_BOOTSTRAP_HOST/activate",
      "verification_uri_complete": "https://YOUR_BOOTSTRAP_HOST/activate?user_code=ABCD-EFGH",
      "interval": 5,
      "expires_in": 600
    }
    ```

    `verification_uri` and `verification_uri_complete` must share the `bootstrapUrl` origin; federate behind your own pages rather than returning an upstream provider's URL directly. The app opens the verification URL in the user's browser and shows the user code.

    The app polls `token_endpoint` with `grant_type=urn:ietf:params:oauth:grant-type:device_code` and the `device_code`. Return `{"error":"authorization_pending"}` until the user approves, then:

    ```json theme={null}
    { "access_token": "eyJhbGciOiJSUzI1NiIs...", "expires_in": 3600 }
    ```

    The polling interval is clamped between 1 and 30 seconds; the grant times out after 5 minutes; the token lifetime you return is clamped between 5 minutes and 30 days (24 hours before 1.17377.1).

    When `inferenceGatewayBaseUrl` shares the `bootstrapUrl` origin, so the same sign-in also serves inference, you may also return a `refresh_token` (optionally with `refresh_token_expires_in` in seconds): as the access token nears expiry during use, Claude Desktop 1.34493.0 and later renews it with an RFC 6749 `grant_type=refresh_token` POST to your `token_endpoint` rather than interrupting the user. The configuration fetch at launch still asks the user to sign in if the access token itself has already expired. Answer `400` with `{"error":"invalid_grant"}` to revoke the refresh token and require a fresh sign-in.
  </Step>

  <Step title="Serve the configuration endpoint">
    On `GET <bootstrapUrl>` with a valid bearer, look up the user from the token claims and return their configuration (see [the HTTP contract](#the-http-contract)).
  </Step>
</Steps>

### Request headers (no per-user sign-in)

Requires Claude Desktop 1.32885.1 or later. Set `bootstrapHeaders` to a JSON object of headers to send on every bootstrap fetch, or `bootstrapHeadersHelper` to the absolute path of an executable that prints such an object on stdout (run with no arguments; its output is cached for a few minutes and merged over the static headers, the helper winning on a conflict). When either key is set and `bootstrapOidc` is not, the app treats the headers as sufficient authentication and fetches the configuration without prompting the user to sign in. If your server answers `401` or `403`, the app discards the cached helper output so the next fetch (the next background check, or a relaunch) re-runs the helper. At launch the app also shows a sign-in prompt; that sign-in succeeds only if your server implements the [device-code grant](#bootstrap-server-as-authorization-server-device-code), so a headers-only server should return `401`/`403` only for a genuinely unusable credential. A `401`/`403` on a background check keeps the running configuration and retries at the next check without prompting. A signed-in user's bearer token replaces any `Authorization` header you configured. Both keys are read from device management or the local configuration file only, never from the bootstrap response, and header values are masked in the diagnostic report. [Origin pinning](#origin-pinning) applies in this mode exactly as in device-code mode. Use this instead of embedding `user:password@` in `bootstrapUrl`, which the app refuses.

## The HTTP contract

### Request

```http theme={null}
GET /user/bootstrap HTTP/1.1
Host: YOUR_BOOTSTRAP_HOST
Authorization: Bearer eyJhbGciOiJSUzI1NiIs...
If-None-Match: "abc123"
```

In request-headers mode the `Authorization` line is whatever your configured headers supply.

The path is whatever you set in `bootstrapUrl`; there is no required path. Redirects are **not** followed: a `3xx` is treated as an error so a same-origin open redirect cannot exfiltrate the bearer. The request times out after 30 seconds.

### Response

Return `200 OK` with `Content-Type: application/json` and a JSON object whose keys are a subset of the [published response schema](#response-schema). Keys use the exact managed-configuration key names. Unknown keys, keys that fail validation, and keys outside that schema are silently dropped; one bad key never invalidates the rest.

```json theme={null}
{
  "inferenceProvider": "gateway",
  "inferenceGatewayBaseUrl": "https://llm-gateway.example.corp",
  "inferenceCredentialKind": "interactive",
  "inferenceModels": ["claude-opus-5", "claude-sonnet-5"],
  "managedMcpServers": [{ "name": "internal-tools", "url": "https://mcp.example.corp/sse", "transport": "sse" }],
  "coworkEgressAllowedHosts": ["*.example.corp", "pypi.org"],
  "otlpResourceAttributes": { "user.email": "alice@example.corp", "team": "trading" },
  "expiresAt": 1778700000
}
```

| Status                  | App behavior                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `200`                   | Parse and apply.                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `304`                   | Re-serve the cached response (the app sends `If-None-Match` when it has one).                                                                                                                                                                                                                                                                                                                                                                                                       |
| `401`, `403`            | Discard the cached token and prompt the user to sign in again. A `401` on a background refresh keeps the running configuration. When the same sign-in also serves inference, the app treats it as an ended session and asks the user to sign in again (1.34493.0 and later); otherwise it retries at the next check without prompting. Return `401` when the token is missing, expired, or the wrong audience; return `403` when the token is valid but the caller is not entitled. |
| Other non-2xx, or `3xx` | Fetch error. Falls back to the last good response from this session if one exists; otherwise the app stays in the degraded sign-in state.                                                                                                                                                                                                                                                                                                                                           |

<Warning>
  A `200` that is not a JSON object (an empty body, an HTML page from a captive portal or load balancer, or a JSON array) is a parse error. Make sure intermediate proxies do not rewrite the response.
</Warning>

### Response schema

The full set of bootstrap-settable keys is published as a machine-readable JSON Schema, generated from the same source as the [configuration reference](/docs/third-party/claude-desktop/configuration) and updated with each release:

* [`/third-party/claude-desktop/schemas/bootstrap-config-v2.schema.json`](/docs/third-party/claude-desktop/schemas/bootstrap-config-v2.schema.json) (recommended): nested response format with a discriminated `inference` object.
* [`/third-party/claude-desktop/schemas/bootstrap-config-v1.schema.json`](/docs/third-party/claude-desktop/schemas/bootstrap-config-v1.schema.json): flat key format, kept for configurations authored before the v2 cutover. The app accepts either format.

Reference the schema with `"$schema"` in your response template, or with `# yaml-language-server: $schema=…` in YAML, for autocomplete and validation.

The response can supply any key in that schema, including inference credentials, model allowlists, MCP servers, the egress allowlist, telemetry endpoints, and the organization banner.

<Note>
  Organization plugins and skills can be delivered over the network by returning `allowedPluginMarketplaces` in the bootstrap response (see [Plugin marketplaces](/docs/third-party/claude-desktop/extensions#plugin-marketplaces-admin)), or through the filesystem `org-plugins/` directory described in [Connectors and extensions](/docs/third-party/claude-desktop/extensions).
</Note>

A small set of keys are **structurally excluded** and ignored if returned:

* `bootstrapUrl`, `bootstrapOidc`, `bootstrapHeaders`, `bootstrapHeadersHelper`, `bootstrapEnabled`, and `trustBootstrapDelivery`: the trust anchor cannot redirect itself, authenticate itself, or grant trust in itself. These are the keys whose Availability column reads **MDM only** in the [configuration reference](/docs/third-party/claude-desktop/configuration).
* Loopback hosts (`127.0.0.1`, `localhost`, `[::1]`) in any URL-valued key, regardless of scheme.

`managedMcpServers` entries are not restricted by transport in version 1.19367.0 and later: remote (`http`/`sse`) servers, local `stdio` commands, and the built-in `microsoft365` and `websearch` connectors can all be delivered in the bootstrap response. Earlier versions accept only remote entries and drop the rest. Because a `stdio` entry names a command that runs on the device, a bootstrap response can start local processes — part of why the warning at the top of this page says to treat this endpoint as fully trusted. Entries whose server URL or OAuth authorization-server URL is loopback or non-HTTPS are still dropped, and the desktop log (see [Troubleshooting](#troubleshooting)) records which keys were dropped and why.

### Keys that require user consent

Some bootstrap-deliverable values point at local commands and credential files, or change where a user signs in. Examples are `inferenceCredentialHelper` and its related keys, `inferenceVertexCredentialsFile`, the AWS profile keys, and connector or marketplace entries that name a local command or helper. The app applies these values only after the user approves them.

When a response delivers such a value for the first time, the app applies the rest of the response and then shows a dialog listing each pending value. Choosing **Allow** applies the pending values and records the approval. Until then, the pending keys are held back, and the desktop log (see [Troubleshooting](#troubleshooting)) records them as stripped pending consent. Approval is per delivered value. If the server later changes an approved value, the dialog appears again. For a `managedMcpServers` or `allowedPluginMarketplaces` entry, one approval covers the entry's executable-related fields as a unit.

Whether the dialog appears depends on how `bootstrapUrl` reached the device:

* Deployed through machine-scoped device management (`HKLM` policy on Windows, a configuration profile on macOS, `/etc/claude-desktop` on Linux): delivered values are trusted without prompting, because the admin already made a device-level decision.
* Read from a local configuration file, or from user-scope registry policy: the dialog is shown by default.

The `trustBootstrapDelivery` key overrides the default in either direction, and the previous name `trustBootstrapLocalExec` is accepted until October 7, 2026. The key is accepted from device management or the local configuration file only, never from the bootstrap response itself. When the rest of your configuration is a local file, set the key in that same file next to `bootstrapUrl`. Delivering only this key through device management makes the whole installation managed, and the app then ignores the local file entirely, including its `bootstrapUrl`.

Consent gates only bootstrap-delivered values. The same keys delivered through device management apply without prompting. Versions that predate a key's availability ignore that key in a bootstrap response (the [configuration changelog](/docs/third-party/claude-desktop/configuration-changelog) records when each key became available), so a response can safely carry keys ahead of a fleet upgrade.

### Caching and `expiresAt`

| Field            | Type      | Description                                                                                                                                                                                                            |
| ---------------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `$schemaVersion` | `integer` | Marks the nested v2 wire format. Optional — a response carrying any cluster key is sniffed as v2 regardless — but setting it explicitly is the documented version marker and is what the app's own JSON export writes. |
| `expiresAt`      | `number`  | Unix epoch (seconds or milliseconds) after which the client should re-fetch this document. Optional; when absent the client uses its default refresh interval.                                                         |

<AccordionGroup>
  <Accordion title="$schemaVersion details">
    Omitted → the client infers the version from the document shape (any cluster key present → v2).
  </Accordion>

  <Accordion title="expiresAt details">
    Omitted → cache for 1 hour. A number ≥ 10¹² is read as Unix epoch **milliseconds**; below that, **seconds**.

    A failed re-fetch keeps the last good response from the current session and retries; the app only enters the degraded state when there has never been a usable response this session.
  </Accordion>
</AccordionGroup>

### Origin pinning

When no `bootstrapOidc` is set (device-code or request-headers mode), the response is fenced: `inferenceGatewayBaseUrl`, `inferenceVertexBaseUrl`, and `inferenceBedrockBaseUrl` must share the `bootstrapUrl` origin or the field is dropped. A compromised configuration response cannot redirect inference to an attacker-controlled host because the only host it can name is your bootstrap server's own origin.

When you supply `bootstrapOidc`, your configuration server and gateway are independent hosts you control, so origin pinning is disabled and the response can name any HTTPS host. In this mode the bootstrap server's integrity is the only control on where inference and MCP traffic are sent.

## MDM configuration keys

| Setting                                                                                              | Type      | Availability | Default | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ---------------------------------------------------------------------------------------------------- | --------- | ------------ | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <span id="bootstrapenabled" />Use bootstrap config<br />`bootstrapEnabled`                           | `boolean` | MDM only     | `true`  | Fetch and apply the URL above at launch. Turn off to keep the URL saved but skip the fetch. Defaults to `true`.                                                                                                                                                                                                                                                                                                                                                                                                                        |
| <span id="bootstrapurl" />Bootstrap config URL<br />`bootstrapUrl`                                   | `string`  | MDM only     | —       | HTTPS endpoint that returns a per-user JSON config overlay. Values from the response override local settings and become read-only.                                                                                                                                                                                                                                                                                                                                                                                                     |
| <span id="bootstrapoidc" />Bootstrap OIDC parameters<br />`bootstrapOidc`                            | `object`  | MDM only     | —       | When set, the bootstrap request sends a Bearer token from a browser sign-in (authorization-code-with-PKCE).                                                                                                                                                                                                                                                                                                                                                                                                                            |
| <span id="bootstrapheaders" />Bootstrap request headers<br />`bootstrapHeaders`                      | `object`  | MDM only     | —       | HTTP headers sent on every bootstrap config fetch. Use this instead of embedding user:pass@ in the URL. Deprecated: `bootstrapHeaders as a "Name=value,…" string or a ["Name: value", …] list` (accepted until October 7, 2026); use a JSON object such as \{"Name": "value"}. If it is still present after that, a string or list value will be rejected as malformed and no bootstrap request headers will be sent (the fetch may then fail to authenticate).                                                                        |
| <span id="bootstrapheadershelper" />Bootstrap headers helper script<br />`bootstrapHeadersHelper`    | `string`  | MDM only     | —       | Absolute path to an executable that prints a JSON object of bootstrap request headers. Merged over the static headers; the helper wins.                                                                                                                                                                                                                                                                                                                                                                                                |
| <span id="trustbootstrapdelivery" />Trust bootstrap-delivered settings<br />`trustBootstrapDelivery` | `boolean` | MDM only     | `false` | Skip the per-user consent prompt for sign-in targets, inference endpoints, helper scripts, and connectors the bootstrap server delivers. Defaults to `false`. Previously named `trustBootstrapLocalExec` (the old name is accepted until October 7, 2026). If it is still present after that, the key will read as false (its fail-closed value): each user will be asked to consent to bootstrap-delivered sign-in targets, endpoints, helper scripts and connectors, even when the bootstrap URL came from a device-managed profile. |

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
    Static headers sent on every request to the bootstrap config URL — for a service-account credential (`Authorization: Basic …`, an API key header) or a routing/tenant header. When either this or the headers helper script is set and no separate `bootstrapOidc` provider is configured, the app treats the headers as sufficient auth and does not require a per-user sign-in for the bootstrap fetch. These headers (and the helper script's below) also accompany requests to a plugin marketplace this server hosts on its own origin (`allowedPluginMarketplaces` with `credentialKind: "inferenceCredential"`). Header values are masked in diagnostics and telemetry. For a rotating token, use the headers helper script instead.
  </Accordion>

  <Accordion title="bootstrapHeadersHelper details">
    Absolute path to an executable that prints a single JSON object of HTTP headers on stdout, e.g. `{"Authorization": "Bearer …"}`. The app runs it (no arguments; output cached for a few minutes) before each bootstrap config fetch and merges the result over **Bootstrap request headers** (the helper wins on conflict). Use this instead of embedding `user:pass@` in the bootstrap URL, or when the bootstrap server needs a rotating token from a secrets manager. When either this or the static headers are set and no separate `bootstrapOidc` provider is configured, the app treats them as sufficient auth and does not require a per-user sign-in for the bootstrap fetch. If a per-user sign-in also runs (`bootstrapOidc` or the server’s own device-code flow), that Bearer token wins on `Authorization`.
  </Accordion>
</AccordionGroup>

No `inferenceProvider` is needed in the MDM profile when using bootstrap; the response supplies it.

## Troubleshooting

| Symptom                                                                      | Likely cause                                                                                                                                                                                                                                                                                                            |
| ---------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Identity provider shows `AADSTS900144` (Entra) or `invalid_request: scope`   | `bootstrapOidc.scopes` is empty. It is required.                                                                                                                                                                                                                                                                        |
| Server logs `unexpected "iss"` or `unexpected "aud"` for a valid Entra token | The app registration's accepted-token-version is at its default. Set it to `2` in the Manifest, or accept both v1 (`sts.windows.net` / `api://CLIENT_ID`) and v2 forms in your server.                                                                                                                                  |
| Sign-in succeeds in the browser but the app immediately re-prompts           | Your server returned `401` or `403`. For `401`, check the `aud` match: the requested scope must produce a token whose audience your server validates. For `403`, the user authenticated but is not in the entitled group or role.                                                                                       |
| Entra returns `AADSTS500011` ("resource principal not found")                | The app registration has no Application ID URI. Set one under **Expose an API**.                                                                                                                                                                                                                                        |
| Silent refresh fails after \~1 hour with `AADSTS90009`                       | `scopes` uses the `api://CLIENT_ID/.default` form. Use the bare-GUID `CLIENT_ID/.default` form.                                                                                                                                                                                                                         |
| Some keys you returned are not applied                                       | They failed schema validation, are structurally excluded, were dropped by origin pinning, or are held for [user consent](#keys-that-require-user-consent). The desktop log (`~/Library/Logs/Claude-3p/main.log` on macOS, `%LOCALAPPDATA%\Claude-3p\logs\main.log` on Windows) records which keys were dropped and why. |
| Browser opens to your identity provider's device page instead of yours       | In device-code mode, `verification_uri` must share the `bootstrapUrl` origin. Federate behind your own page.                                                                                                                                                                                                            |
