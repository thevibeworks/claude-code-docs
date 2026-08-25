> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Troubleshooting connectors

> Diagnose and resolve common connection failures for custom and directory MCP connectors

This page covers the most common reasons a connector fails to connect or authenticate, and how to diagnose each one. The errors Claude shows in the UI ("Couldn't reach the MCP server" and "Authorization with the MCP server failed") cover more than one root cause, so the first step is figuring out which one you're hitting.

## Find your reference ID

When a connection fails, the error toast and the page URL include a reference ID that starts with `ofid_`. For example:

```text theme={null}
.../customize/connectors?step=start_error&flow_id=ofid_d32594c73257a651
```

Copy that ID and include it in any GitHub issue or support request. It lets Anthropic trace the exact failure on the server side. Reference IDs are time-limited, so report them soon after the failure.

<Tip>
  If you're filing on the [`anthropics/claude-ai-mcp` issue tracker](https://github.com/anthropics/claude-ai-mcp/issues), include the `ofid_` value, your server URL, and what your server-side access logs show during the Connect attempt.
</Tip>

## "Couldn't reach the MCP server"

This error appears when Claude can't complete the connection handshake. Despite the wording, it isn't always a network failure. Work through these causes in order.

### 1. Hostname resolves to a private IP

claude.ai connectors run on Anthropic's infrastructure and reach your server over the public internet. Before making any request, Claude resolves your server's hostname and validates the result. If **any** resolved address is not globally routable, Claude rejects the connection before any HTTP request leaves Anthropic's network. Your server's access logs see nothing, and Claude reports "Couldn't reach."

Claude rejects the connection when the hostname:

* resolves to a private address (`10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`)
* resolves to a carrier-grade NAT address (`100.64.0.0/10`)
* resolves to a loopback or link-local address
* resolves to a mix of public and non-public addresses — every returned address must be globally routable
* has no `A` record from public DNS — connectors are IPv4-only, so a hostname that only publishes `AAAA` records can't be reached

**Common gotchas:**

* **Works in Claude Code or `curl` but not claude.ai.** The CLI and `curl` connect from your machine, while claude.ai connects from Anthropic's servers. If your hostname resolves differently inside and outside your network (split-horizon DNS), claude.ai may be getting a private IP.
* **Dynamic DNS providers.** Dynamic DNS hostnames often resolve to a home network behind NAT or carrier-grade NAT.
* **Internal corporate DNS.** A hostname that resolves on your VPN won't resolve to a routable address from the public internet.

**How to check:** Run `dig +short your-server.example.com` from a machine outside your network, or use a public DNS lookup service. Every returned address must be globally routable.

**How to fix:** Expose your server through a publicly-routable endpoint, such as a cloud host with a public IP, a public reverse proxy, or a tunnel. See [test a local server](/docs/connectors/building/testing#test-a-local-server) for the recommended tunnel setup.

### 2. Firewall or WAF blocks Anthropic's traffic

If your hostname resolves correctly but a CDN, WAF, bot-management rule, or rate limiter in front of your server blocks the request, the connection fails before your application sees it.

**How to check:** Look for `403` or `429` responses in your edge or CDN logs that your application didn't generate, especially during a Connect attempt.

**How to fix:** Allowlist Anthropic's published outbound IP range in your WAF or CDN configuration, or exempt your MCP and OAuth paths from the blocking rule. The current range is on the [IP address reference](https://platform.claude.com/docs/en/api/ip-addresses) page.

### 3. Your server URL redirects to a different host

If your registered MCP URL returns a `301`/`302`/`307`/`308` redirect to a different host (apex to `www.`, region routing, vanity domain to CDN), the `Authorization` header is dropped on the redirect per standard HTTP client security behavior. The redirect target receives an unauthenticated request and returns `401`, and the connection fails with "Authorization with the MCP server failed."

This also explains the common report "works in MCP Inspector or Claude Code CLI but not claude.ai." Local clients fail fast on a redirect, so the misconfiguration is visible immediately. claude.ai follows the redirect, drops the credential, and the failure surfaces later as an authorization error.

**How to check:** Run `curl -sI https://your-server.example.com/your-mcp-path` and look at the response status and `Location` header. If you see a `3xx` status pointing at a different host, that target is the URL you should register.

**How to fix:** Register the URL your server actually listens on, not a URL that redirects to it. Common culprits are apex-to-`www.` canonicalization, geographic or region routing, and vanity-domain-to-CDN redirects.

### 4. OAuth discovery fails

If your server requires authentication, Claude performs OAuth discovery before it can connect. A discovery failure surfaces as "Couldn't reach" even though your MCP endpoint itself is reachable. The most common causes:

* **Discovery metadata returns 404.** If your `401` response doesn't include a `WWW-Authenticate` header with a `resource_metadata` pointer, Claude looks for [RFC 9728](https://www.rfc-editor.org/rfc/rfc9728) protected resource metadata and authorization server metadata at the standard `/.well-known/` paths on your MCP server's origin. If those paths return `404` and you haven't pointed Claude elsewhere, Claude has no way to start the OAuth flow.
* **No way to register a client.** Claude needs one of: [RFC 7591 dynamic client registration](https://www.rfc-editor.org/rfc/rfc7591) (a `registration_endpoint` in your authorization server metadata), [Client ID Metadata Documents](/docs/connectors/building/authentication#dcr-and-cimd-details) (`"client_id_metadata_document_supported": true`), or a pre-registered client. Without any of these, Claude can't obtain a client identity. See [supported authentication types](/docs/connectors/building/authentication#supported-authentication-types).
* **Authorization server is on a different host than the MCP server.** Claude discovers protected resource metadata from your MCP server, then makes a *second* round of discovery requests against the authorization server host listed in `authorization_servers`. If that host lives behind a different CDN or WAF, it must also be reachable from Anthropic's egress range. See [cross-host authorization servers](/docs/connectors/building/authentication#cross-host-authorization-servers).

**How to check:** From a public network, run:

```bash theme={null}
curl -i https://your-server.example.com/.well-known/oauth-protected-resource
curl -i https://your-server.example.com/.well-known/oauth-authorization-server
curl -i https://your-server.example.com/.well-known/openid-configuration
```

If your MCP endpoint includes a path component (such as `https://your-server.example.com/mcp`), append it to the well-known path: `/.well-known/oauth-protected-resource/mcp`.

The protected resource metadata should return `200` with valid JSON. For authorization server metadata, your server only needs to answer **one** of the two discovery endpoints — Claude tries `/.well-known/oauth-authorization-server` ([RFC 8414](https://www.rfc-editor.org/rfc/rfc8414)) first, then falls back to `/.well-known/openid-configuration` ([OpenID Connect Discovery 1.0](https://openid.net/specs/openid-connect-discovery-1_0.html)). A `404` on one is expected if the other returns `200`. Most hosted identity providers (Auth0, Okta, Microsoft Entra, Keycloak, Supabase Auth) only serve `/.well-known/openid-configuration`.

Whichever metadata document resolves should advertise a `registration_endpoint` (DCR), `"client_id_metadata_document_supported": true` (CIMD), or you should be using pre-registered credentials. In a cross-host setup, run the protected-resource curl against your MCP server and the two authorization-server curls against your authorization server's issuer host.

## "Authorization with the MCP server failed"

This error appears after the OAuth flow has started. The most common causes:

* **Issuer mismatch.** The `issuer` value in your authorization server metadata must match the issuer that signs your tokens. If your tokens come from a third-party identity provider such as Supabase Auth or Auth0 but your metadata advertises a different issuer URL, validation can fail.
* **Audience mismatch.** The [MCP authorization spec](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization#token-handling) requires your server to verify each access token was issued for it. Claude sends the [RFC 8707](https://www.rfc-editor.org/rfc/rfc8707) `resource` parameter on authorization and token requests, set to the canonical form of your MCP server URL — lowercase scheme and host, no trailing slash, no fragment, no default port — including any path component. Your authorization server should issue tokens with that audience, and your MCP server should accept the canonical value when checking `aud` rather than doing a strict byte-for-byte comparison against what the user typed. Or use whatever audience-binding mechanism your token format supports, as long as it confirms the token was minted for your server and not another service.
* **PKCE not supported.** Claude includes a PKCE `code_challenge` with `code_challenge_method=S256` in every authorization request. If your authorization server doesn't implement S256 PKCE, the flow fails at the token endpoint. The [MCP authorization spec](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization#authorization-code-protection) also requires authorization servers to advertise `"code_challenge_methods_supported": ["S256"]` so spec-compliant clients can verify support before starting the flow.
* **Refresh failures.** Use RFC 6749-compliant error codes when a refresh token expires. See [token refresh](/docs/connectors/building/authentication#token-refresh).
* **Slow token endpoint.** Claude waits up to 10 seconds for your `/token` response; if no response bytes arrive in that window, the flow fails here even if your server eventually issues the token. Check the end-to-end latency of your token handler and any proxy or gateway in front of it. See [endpoint latency](/docs/connectors/building/authentication#endpoint-latency).

### Microsoft Entra ID rejects the resource value

If your authorization server is Microsoft Entra ID and the token request fails with `AADSTS9010010` (sometimes surfaced as `invalid_target`), Entra is rejecting the `resource` value Claude sends because it does not match any Application ID URI registered on your app. Claude sets `resource` to your MCP server URL, including the path, and Entra issues a token when that value is listed under **Expose an API** → **Application ID URI** (`identifierUris` in the manifest) on the app registration that represents your protected API. The default `api://{client-id}` URI alone is not sufficient here, because Claude sends the full MCP server URL as the resource value.

**How to fix:**

1. In the [Microsoft Entra admin center](https://entra.microsoft.com), open the app registration that represents your protected API. If you have separate registrations for the OAuth client and the API, this is the API registration, not the client.
2. Under **Expose an API**, add your MCP server URL as an additional [Application ID URI](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-configure-app-expose-web-apis). The value must match exactly, including the path, without a trailing slash.
3. If your server validates the token audience (for example, through Azure App Service Authentication), add the API app's Application (client) ID and its `api://` URI to the allowed token audiences so your server accepts tokens issued for the API. This is the **Allowed token audiences** setting, not **Allowed client applications**, which is a different list.
4. If the OAuth client and the API are separate app registrations, confirm the client has an admin-consented API permission for the scope your API exposes.

If the OAuth flow completes successfully on your server (you see the token issued in your logs) but the connection still fails, file a [GitHub issue](https://github.com/anthropics/claude-ai-mcp/issues) with the `ofid_` reference ID and the timestamps from your server's OAuth logs.

## Diagnostic checklist

Run through these in order before filing an issue:

<Steps>
  <Step title="Public DNS resolution">
    From a network outside your own, confirm `dig +short your-server.example.com` returns a globally-routable address.
  </Step>

  <Step title="Public reachability">
    From a public network, confirm `curl -i https://your-server.example.com/your-mcp-path` returns a response (a `401` or `405` is fine; a timeout or connection refused is not).
  </Step>

  <Step title="No redirect">
    Run `curl -sI https://your-server.example.com/your-mcp-path` and confirm the response is not a `3xx` redirect to a different host. If it is, register the redirect target instead.
  </Step>

  <Step title="No WAF block">
    Check your edge logs for `403` or `429` responses. Allowlist Anthropic's published egress range if needed. See the [IP address reference](https://platform.claude.com/docs/en/api/ip-addresses).
  </Step>

  <Step title="Discovery metadata">
    Confirm `/.well-known/oauth-protected-resource` returns `200` with valid JSON, and that one of `/.well-known/oauth-authorization-server` or `/.well-known/openid-configuration` does the same — only one is needed. The authorization server metadata should include a `registration_endpoint` (DCR) or advertise `"client_id_metadata_document_supported": true` (CIMD), or you should be using pre-registered credentials, and it should advertise `"code_challenge_methods_supported": ["S256"]`.
  </Step>

  <Step title="Cross-host hint">
    If your authorization server is on a different host than your MCP server, confirm your protected resource metadata's `authorization_servers` field points at it, and that the authorization server's host is reachable from Anthropic's egress range and answers `/.well-known/openid-configuration` (or `/.well-known/oauth-authorization-server`). See [cross-host authorization servers](/docs/connectors/building/authentication#cross-host-authorization-servers).
  </Step>

  <Step title="Collect the reference ID">
    Reproduce the failure and copy the `ofid_` value from the error URL. Include it, your server URL, and your server-side logs in your report.
  </Step>
</Steps>

## Related topics

<Columns cols={2}>
  <Card title="Authentication" icon="lock" href="/docs/connectors/building/authentication">
    OAuth requirements and supported auth types.
  </Card>

  <Card title="Testing" icon="flask" href="/docs/connectors/building/testing">
    How to test your server before publishing.
  </Card>

  <Card title="Lazy authentication" icon="hourglass" href="/docs/connectors/building/lazy-authentication">
    The 401 + WWW-Authenticate discovery handshake.
  </Card>

  <Card title="IP address reference" icon="network-wired" href="https://platform.claude.com/docs/en/api/ip-addresses">
    Anthropic's published IP ranges for allowlisting.
  </Card>
</Columns>
