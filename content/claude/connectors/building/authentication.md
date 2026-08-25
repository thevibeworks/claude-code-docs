> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Authentication for connectors

> OAuth and authentication options for MCP servers in Claude

Authentication is the most common source of partner questions. Claude's auth support differs in a few places from the generic MCP specification, so read this page even if you're already familiar with MCP auth.

## Supported authentication types

Claude supports the following authentication types for remote MCP servers. The same infrastructure backs Claude.ai, Claude Desktop, Claude mobile, Claude Code, and Cowork.

| Type                    | Description                                                                                                                                             | Availability                                              |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| `oauth_dcr`             | OAuth 2.0 with Dynamic Client Registration ([RFC 7591](https://www.rfc-editor.org/rfc/rfc7591))                                                         | Supported out of the box                                  |
| `oauth_cimd`            | OAuth 2.0 with [Client ID Metadata Document](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization#client-id-metadata-documents) | Supported out of the box                                  |
| `oauth_anthropic_creds` | OAuth 2.0 with Anthropic-held client credentials                                                                                                        | Contact `mcp-review@anthropic.com`                        |
| `custom_connection`     | Custom URL or credentials supplied at connection time (for example, Snowflake-style)                                                                    | Contact `mcp-review@anthropic.com`                        |
| `static_headers`        | Fixed credential (API key or bearer token) entered by an organization administrator as a request header when adding the connector                       | Beta                                                      |
| `none`                  | No authentication (authless server)                                                                                                                     | Supported. An optional partial-auth mode is experimental. |

Static bearer tokens and API keys are supported in beta through request headers (`static_headers`). An organization administrator enters the credential once when adding the connector, and Claude sends it on every request. The credential is shared by the organization rather than pasted per user. See [Authenticating with request headers](/docs/connectors/custom/remote-mcp#authenticating-with-request-headers) for what administrators see and how to document the expected header for them.

Tokens or API keys passed in the connector URL (for example, `?token=`, `?apiKey=`, or `?userToken=` query parameters) are **not recommended**. A credential in a URL is a security vulnerability: URLs are routinely recorded in server logs, proxies, and browsing history, so a query-string credential is easy to leak. The MCP authorization specification explicitly [prohibits access tokens in the URI query string](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization#token-requirements). Use OAuth or [request headers](/docs/connectors/custom/remote-mcp#authenticating-with-request-headers) instead.

## Anthropic-held client credentials

A pure machine-to-machine `client_credentials` grant—where a server-to-server token is issued with no user in the loop—is **not supported**. Every connection requires user consent.

`oauth_anthropic_creds` is the consent-gated alternative. The flow works like this:

1. You create an OAuth `client_id` and `client_secret` in your own authorization server and send them to Anthropic.
2. Anthropic stores those credentials securely and associates them with your directory entry.
3. When a user connects your server, they go through a standard OAuth consent screen.
4. After consent, Anthropic uses the stored client credentials to complete the token exchange on the user's behalf.

This gives you a stable, registered OAuth client without requiring DCR or CIMD on your end, while keeping the user-consent step. Anthropic stores your credentials securely and uses them only for token exchange on behalf of consenting users; they are shared across the hosted Claude surfaces (Claude.ai web, Desktop, mobile, and Cowork). Claude Code runs its own OAuth flow on the user's machine and identifies itself with its own [Client ID Metadata Document](#callback-urls), so it does not use Anthropic-held credentials. Claude Managed Agents uses a separate credential set.

Anthropic-held credentials are bound to the authorization server that issued them. If you migrate to a new authorization server, email `mcp-review@anthropic.com` with the new `client_id` and `client_secret` before cutting over. CIMD-based connectors don't have this constraint — a CIMD `client_id` is a self-hosted URL, so it works against any authorization server that fetches it.

To use this flow, email `mcp-review@anthropic.com` with your `client_id` and secret.

## DCR and CIMD details

If your authorization server does **not** expose a `registration_endpoint` (i.e., does not support DCR), you have several options:

* Expose a `registration_endpoint`
* Support CIMD instead. Claude selects CIMD only when your authorization server metadata advertises **both** `"client_id_metadata_document_supported": true` **and** `"none"` in `token_endpoint_auth_methods_supported` — the second is required because Claude's CIMD client authenticates as a public client at your token endpoint. If either is missing, Claude falls back to DCR. See [lazy authentication](/docs/connectors/building/lazy-authentication#identify-the-client-with-cimd) for a worked CIMD example.
* Switch to `oauth_anthropic_creds`

For servers expecting high traffic from the directory, prefer **CIMD or `oauth_anthropic_creds` over DCR**. DCR causes Claude to register a new client on every fresh connection, which can result in very large numbers of registered clients on your authorization server. CIMD and Anthropic-held credentials avoid the registration call entirely.

Claude includes a [PKCE](https://datatracker.ietf.org/doc/html/rfc7636) `code_challenge` with `code_challenge_method=S256` on every authorization request, regardless of which registration mechanism it uses. Your authorization server must support S256 PKCE, and the [MCP authorization spec](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization#authorization-code-protection) requires it to advertise `"code_challenge_methods_supported": ["S256"]` in its metadata so spec-compliant clients can verify support before starting the flow.

To control which scopes Claude requests, include a `scope` parameter in the `WWW-Authenticate` header on your `401` response. If you don't, Claude requests the scopes your protected resource metadata advertises in `scopes_supported`. Claude also appends `offline_access` when your authorization server metadata lists it in `scopes_supported`, to obtain a refresh token. See [lazy authentication](/docs/connectors/building/lazy-authentication#return-401-not-a-tool-error) for the canonical `401` shape.

## Cross-host authorization servers

A cross-host authorization server doesn't need anything special on its own. The `authorization_servers` field in your [protected resource metadata](https://www.rfc-editor.org/rfc/rfc9728) tells Claude where the authorization server is, and Claude resolves it regardless of which host it points at. The thing to get right is making sure Claude can find the protected resource metadata in the first place.

**Always return a `401` with a `WWW-Authenticate` header** whose `resource_metadata` parameter points at your protected resource metadata document — the same handshake described in [Return 401, not a tool error](/docs/connectors/building/lazy-authentication#return-401-not-a-tool-error):

```http theme={null}
HTTP/1.1 401 Unauthorized
WWW-Authenticate: Bearer resource_metadata="https://mcp.example.com/.well-known/oauth-protected-resource"
```

The `401` status is required — Claude does not honor a `WWW-Authenticate` header on a `200` response — and the `resource_metadata` URL doesn't have to be on the MCP server's origin; it can be any HTTPS location that serves the JSON document. That's what makes this the most reliable path for hosting platforms that can't serve `/.well-known/*` at the root, such as Supabase Edge Functions, Cloudflare Workers without a `/.well-known/*` route, and Lambda function URLs that only route a path prefix.

If your `401` doesn't include a `resource_metadata` pointer, Claude can still infer the metadata location by probing your MCP server's origin: `/.well-known/oauth-protected-resource/<your-mcp-path>` first, then `/.well-known/oauth-protected-resource`. Treat this as a fallback — it only works when your platform serves `/.well-known/*` paths, and it adds round-trips to every connection.

Whichever way Claude finds the document:

* The protected resource metadata document's `resource` field must match your MCP server URL exactly as the user enters it in Claude, including any path component.
* The metadata's `authorization_servers` field must list your authorization server's issuer URL. If you list more than one, Claude uses the first entry and does not fall back to later entries — list your primary issuer first.
* Your authorization server must serve its own discovery metadata — [RFC 8414](https://www.rfc-editor.org/rfc/rfc8414) authorization server metadata or [OpenID Connect Discovery 1.0](https://openid.net/specs/openid-connect-discovery-1_0.html) — at its `/.well-known/` paths, and that host must also be reachable from Anthropic's [published egress range](https://platform.claude.com/docs/en/api/ip-addresses). Discovery requests to the authorization server come from the same IP range as requests to your MCP server, so a WAF in front of your identity provider can break the flow even when your MCP server is reachable.

<Note>
  If your authorization server is Microsoft Entra ID, you must also register the MCP server URL as an Application ID URI on your Entra app registration, or the token request fails with `AADSTS9010010`. See [the troubleshooting entry](/docs/connectors/building/troubleshooting#microsoft-entra-id-rejects-the-resource-value) for the fix.
</Note>

If you control both hosts, an alternative is to serve the MCP endpoint and the authorization server behind a single custom domain that can route both `/.well-known/*` and your MCP path.

<Tip>
  A common symptom of a discovery failure is that your MCP server receives the initial request but your authorization server sees no traffic at all. That happens when neither path works: there's no `WWW-Authenticate: Bearer resource_metadata=…` header on your `401`, and the well-known paths on your MCP server's origin return `404`. With no metadata to read, Claude never learns where your authorization server is, and the connection fails with "Couldn't reach the MCP server." See [troubleshooting](/docs/connectors/building/troubleshooting) for the full diagnostic flow.
</Tip>

## Callback URLs

For the hosted Claude surfaces (Claude.ai web, Desktop, mobile, and Cowork), register the following redirect URI:

```
https://claude.ai/api/mcp/auth_callback
```

**Claude Code** is a native client and uses an RFC 8252 loopback redirect on an ephemeral port — for example:

```
http://localhost:3118/callback
```

The port varies per session. Claude Code declares `http://localhost/callback` and `http://127.0.0.1/callback` in its [Client ID Metadata Document](https://claude.ai/oauth/claude-code-client-metadata), so your authorization server must accept both with the port component ignored. [RFC 8252 section 7.3](https://datatracker.ietf.org/doc/html/rfc8252#section-7.3) requires this for the IP-literal form (`127.0.0.1`); apply the same port-agnostic match to `localhost` so Claude Code works, even though RFC 8252 section 8.3 discourages `localhost`. See [lazy authentication](/docs/connectors/building/lazy-authentication) for implementation details.

A Client ID Metadata Document can't prevent loopback impersonation on its own — any local process can bind a port and claim to be the legitimate client. The [MCP authorization spec](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization#localhost-redirect-uri-risks) requires authorization servers to display the redirect URI hostname clearly on the consent screen and recommends an extra warning when the only registered redirect URIs are loopback addresses.

## Token refresh

Claude refreshes tokens **reactively on a 401 response**, with a proactive refresh up to five minutes before the stored expiry. To avoid refresh failures:

* Return RFC 6749-compliant error codes (`invalid_grant`, not `invalid_request` or a custom code) when a refresh token is no longer valid
* Rotate refresh tokens for public-client connections. DCR and CIMD register Claude as a public client, and the [MCP authorization spec](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization#token-theft) adopts OAuth 2.1's requirement to rotate or sender-constrain refresh tokens for public clients. If you rotate, return the new refresh token in the same response that invalidates the old one.

Your `/token` endpoint must accept `Content-Type: application/x-www-form-urlencoded` per [RFC 6749 section 4.1.3](https://www.rfc-editor.org/rfc/rfc6749#section-4.1.3). Claude sends both the initial token exchange and refresh requests with this content type. Some web frameworks default to JSON-only body parsing—if your endpoint returns `415 Unsupported Media Type`, register a form-urlencoded body parser. Dynamic client registration (`/register`) uses `application/json` per [RFC 7591 section 3.1](https://www.rfc-editor.org/rfc/rfc7591#section-3.1), so don't assume the same parser works for both.

## Enterprise authentication

<Note>
  Organizations using SSO can also connect their users to your server without an interactive OAuth consent step, using an identity assertion signed by their identity provider. See [Enterprise Managed Auth](./enterprise-managed-auth) for what your authorization server needs to support.
</Note>

Directory connectors use a **single shared OAuth application per connector**. There is no per-org OAuth client for directory connectors — enterprise customers connect to the same OAuth app as everyone else, and access is scoped by the user's own permissions on your service. Custom connectors are different: an admin can supply their own OAuth client credentials when adding the connector, which scopes the OAuth client to that organization. See [custom connectors](#custom-connectors).

## Custom connectors

When a user adds a custom connector by URL, the OAuth Client Secret field is **optional**. Supply it only if your authorization server requires confidential-client authentication.

Supplying your own pre-registered client ID (and secret, if your server requires one) as static client credentials is a good option when you want a stable OAuth client per organization: it avoids dynamic client registration entirely, and the credentials are scoped to the organization that entered them.

For servers that authenticate with a fixed API key or token rather than OAuth, request header authentication (`static_headers`) is available in beta. See [Supported authentication types](#supported-authentication-types) above and [Authenticating with request headers](/docs/connectors/custom/remote-mcp#authenticating-with-request-headers) for what administrators see.

## Endpoint latency

Claude waits up to **10 seconds** for a response from your OAuth discovery, registration, and token endpoints, and up to **30 seconds** for refresh token requests. If no response arrives within that window the flow is treated as a failure, even if your server eventually completes the request. Aim well under these limits; a token endpoint that takes several seconds to respond will produce intermittent connection failures for users.

If your token endpoint depends on slow downstream calls, return the HTTP response headers and body without buffering behind upstream work, and check that any reverse proxy, API gateway, or WAF in front of the endpoint isn't holding the response.

## Network reference

Anthropic's outbound traffic to your server originates from `160.79.104.0/21`. See the [IP address reference](https://platform.claude.com/docs/en/api/ip-addresses) if you need to allowlist Anthropic for conditional access or firewall rules.
