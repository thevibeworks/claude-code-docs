> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Authentication for connectors

> Meet Claude's OAuth requirements for remote MCP servers: supported authentication types, client registration, discovery, callback URLs, and token refresh.

A remote MCP server can let Claude in one of three ways:

* **OAuth 2.0**: each user signs in to your service with their own account when they connect
* **A static credential**: an organization Owner enters an API key or bearer token once when adding the connector, and Claude sends it in a request header on every call. This is in beta
* **No authentication**: the server accepts requests from anyone who has its URL

This page is for developers building a remote MCP server that people use in Claude. The same authentication infrastructure backs claude.ai, Claude Desktop, Claude mobile, Claude Code, and Cowork, so the requirements here apply to all of them.

If you already know MCP authorization, these are the places where Claude's OAuth client is stricter or more specific than the specification:

* A `401` is required to start sign-in, and Claude ignores a `WWW-Authenticate` header on a `200` response, as [Serve discovery metadata](#serve-discovery-metadata) describes
* Claude uses only the first entry in your metadata's `authorization_servers` list, as [Serve discovery metadata](#serve-discovery-metadata) describes
* Claude uses a Client ID Metadata Document only when your authorization server metadata advertises both values in [DCR and CIMD details](#dcr-and-cimd-details), and otherwise falls back to DCR
* Claude Code's loopback redirect needs a port-agnostic match for `localhost` as well as `127.0.0.1`, as [Callback URLs](#callback-urls) describes
* Claude gives your discovery, registration, and token endpoints 10 seconds to respond and refresh requests 30 seconds, as [Endpoint latency](#endpoint-latency) describes
* A machine-to-machine `client_credentials` grant isn't supported, and [Anthropic-held client credentials](#anthropic-held-client-credentials) are the consent-gated alternative

<Note>
  - If some of your tools work without the user's account, see [Lazy authentication](/docs/connectors/building/lazy-authentication) to let people use those right away and sign in only when Claude reaches a tool that needs their account
  - If you want enterprise users to connect through their organization's SSO without a consent screen, see [Enterprise Managed Auth](/docs/connectors/building/enterprise-managed-auth)
</Note>

Use this page to [pick an authentication type](#supported-authentication-types), [register Claude as an OAuth client](#register-claude-as-an-oauth-client), [make discovery and redirects work](#oauth-discovery-and-redirect-uris), and [meet the token endpoint requirements](#token-endpoint-requirements).

## Supported authentication types

Claude supports the following authentication types for remote MCP servers.

| Type                    | Description                                                                                                                                             | Availability                                                                                                                                       |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `oauth_dcr`             | OAuth 2.0 with Dynamic Client Registration ([RFC 7591](https://www.rfc-editor.org/rfc/rfc7591))                                                         | Supported by default                                                                                                                               |
| `oauth_cimd`            | OAuth 2.0 with [Client ID Metadata Document](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization#client-id-metadata-documents) | Supported by default                                                                                                                               |
| `oauth_anthropic_creds` | OAuth 2.0 with [Anthropic-held client credentials](#anthropic-held-client-credentials)                                                                  | Contact `mcp-review@anthropic.com`                                                                                                                 |
| `custom_connection`     | Custom URL or OAuth client credentials [entered at connection time](#credentials-entered-at-connection-time)                                            | Contact `mcp-review@anthropic.com`                                                                                                                 |
| `static_headers`        | Fixed credential (API key or bearer token) entered by an organization Owner as a request header when adding the connector                               | Beta, for a limited set of organizations                                                                                                           |
| `none`                  | No authentication (authless server)                                                                                                                     | Supported by default. To leave some tools open and require sign-in for others, see [Lazy authentication](/docs/connectors/building/lazy-authentication) |

If your server URL varies per customer, read [Servers with per-customer URLs](#servers-with-per-customer-urls) before you pick a type.

### Static credentials in request headers

With a static credential, an organization Owner enters an API key or bearer token once when they add your connector, and Claude sends it in a request header on every call from anyone in that organization. This type is in beta and available to a limited set of organizations. Owners whose organization doesn't have access don't see the **Request headers** section when they add a connector. If your server uses it:

* **Read the credential from a request header**: standard authentication header names such as `authorization`, `x-api-key`, and `x-auth-token` work for every connector. If you need a different header name, Anthropic has to approve it before Owners can save the connector, so ask `mcp-review@anthropic.com` first
* **Never accept it in the URL**: don't read tokens from query parameters such as `?token=` or `?apiKey=`. URLs end up in server logs, proxies, and browser history, and the MCP authorization specification [prohibits access tokens in the query string](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization#token-requirements)
* **Treat it as the organization's credential, not a person's**: every member's requests carry the same key, so don't use it to identify which user is calling. If your tools need to act as the individual user, use OAuth instead
* **Tell Owners what to enter**: document the header name and where they get the key. [Authenticate with request headers](/docs/connectors/custom/add-unlisted#authenticate-with-request-headers) shows what the Owner sees when adding the connector

### Servers with per-customer URLs

The submission portal's **Connection** step asks how users reach your server, and you pick one of these options:

* **Universal URL**: every user connects to the same URL
* **Multiple URLs**: you list a fixed set of labeled URLs, such as one per region, and users pick one when they connect
* **URL pattern**: you give an anchored regular expression that every customer's URL must match, such as `^https://[a-z0-9-]+\.mcp\.example\.com/mcp$`. Each user enters their own URL when they connect, and Claude accepts it only if it matches. Keep the host part of the pattern lowercase, because Claude lowercases the host of the URL the user enters before checking it

Listings with **Multiple URLs** or a **URL pattern** take longer to review.

You choose the URL option and the authentication type separately, but the URL option limits which authentication types work. The table shows which combinations work. Request headers (`static_headers`) are set up by the organization Owner who adds the connector and aren't covered here.

| Type                    | Universal URL | Multiple URLs | URL pattern |
| ----------------------- | ------------- | ------------- | ----------- |
| `oauth_dcr`             | Yes           | Yes           | Yes         |
| `oauth_cimd`            | Yes           | Yes           | Yes         |
| `oauth_anthropic_creds` | Yes           | Yes           | No          |
| `custom_connection`     | Yes           | No            | Yes         |
| `none`                  | Yes           | Yes           | Yes         |

For a URL pattern, use these authentication types in order of preference:

1. Client ID Metadata Document (CIMD). Every customer's authorization server must advertise both CIMD values listed in [DCR and CIMD details](#dcr-and-cimd-details).
2. [Dynamic Client Registration](#dcr-and-cimd-details) (DCR). Every customer's authorization server must expose a `registration_endpoint`.
3. [Credentials entered at connection time](#credentials-entered-at-connection-time), if your customers' authorization servers support neither. Each customer then has to create an OAuth client for Claude themselves.

## Register Claude as an OAuth client

For the OAuth types, Claude needs a client identity at your authorization server. Claude can register itself through DCR or identify itself with a CIMD, Anthropic can hold a client you create, or each customer can enter their own client when they connect.

### DCR and CIMD details

If your authorization server doesn't support DCR, meaning it exposes no `registration_endpoint`, you have these options:

* Expose a `registration_endpoint`
* Support CIMD instead. Claude selects CIMD only when your authorization server metadata advertises both `"client_id_metadata_document_supported": true` and `"none"` in `token_endpoint_auth_methods_supported`. The second is required because Claude's CIMD client authenticates as a public client at your token endpoint. If either is missing, Claude falls back to DCR. See [lazy authentication](/docs/connectors/building/lazy-authentication#identify-claude-with-a-client-id-metadata-document) for a worked CIMD example
* Switch to `oauth_anthropic_creds`, if your listing doesn't use a URL pattern

If your server URL varies per customer and DCR isn't available, CIMD is the recommended path. Every customer's authorization server must advertise both CIMD values. Otherwise Claude falls back to DCR for that customer, which needs a `registration_endpoint`.

For servers expecting high traffic from the directory, prefer CIMD or `oauth_anthropic_creds` over DCR. DCR causes Claude to register a new client on every fresh connection, which can result in very large numbers of registered clients on your authorization server. CIMD and Anthropic-held credentials avoid the registration call entirely.

### Anthropic-held client credentials

With `oauth_anthropic_creds`, you create an OAuth client for Claude in your own authorization server and Anthropic holds its credentials, so Claude has a stable, registered client without DCR or CIMD on your end. Users still go through your standard OAuth consent screen when they connect. A pure machine-to-machine `client_credentials` grant, where a token is issued with no user in the loop, isn't supported.

To use this type:

* **Create a confidential client**: create a `client_id` and `client_secret` for Claude in your authorization server
* **Send the credentials to Anthropic**: email `mcp-review@anthropic.com` with the `client_id` to set up Anthropic-held credentials. Anthropic replies with how to transfer the client secret securely, so don't put the secret in the email. Anthropic uses the credentials only for token exchange on behalf of consenting users
* **Plan for Claude Code separately**: the hosted Claude apps, which are claude.ai on the web, Desktop, mobile, and Cowork, share this client. Claude Code doesn't use it: it runs its own OAuth flow on the user's machine, identifies itself with its own [Client ID Metadata Document](#callback-urls), and redirects to a loopback callback URL
* **Tell Anthropic before you migrate authorization servers**: the credentials are bound to the authorization server that issued them. Email `mcp-review@anthropic.com` with the new `client_id` before cutting over, and transfer the new secret the same way as the first
* **Don't combine it with a URL pattern**: the credentials are tied to exact server URLs, so they can't be used where each customer enters their own server URL. See [Servers with per-customer URLs](#servers-with-per-customer-urls) for the alternatives

### Credentials entered at connection time

`custom_connection`, labeled **Custom URL or credentials at connection time** in the submission portal, asks each customer for the OAuth client that Claude should use, instead of Claude registering one or Anthropic holding one.

Each customer must be able to create an OAuth client in your product, which usually means an administrator sets up the connector for their organization. If your customers can't create OAuth clients, use CIMD or DCR instead.

When a user adds your connector, Claude shows a form with these fields:

* **Server URL**, if your listing uses a URL pattern. Claude accepts the URL only if it matches the pattern
* **OAuth client ID** and **OAuth client secret**. You choose which of the two to ask for, and whether each is required or optional

The form links to pages you supply: one for where the customer finds their server URL, and one for how they get the credentials. The credentials page must explain how a customer creates an OAuth client for Claude in your product and registers the redirect URI `https://claude.ai/api/mcp/auth_callback`.

If a user leaves an optional client secret blank, Claude uses the client ID as a public client. If a user leaves an optional client ID blank, Claude falls back to its standard order: Anthropic-held credentials for that URL if Anthropic holds any, then CIMD, then DCR. See [DCR and CIMD details](#dcr-and-cimd-details).

If you later stop asking for credentials, connections already made with user-entered credentials keep using them, and an organization keeps the form until no one in it still has the connector.

To use this flow, email `mcp-review@anthropic.com` with which fields you need, whether each is required, and the page each one should link to.

### PKCE and requested scopes

Claude includes a [PKCE](https://datatracker.ietf.org/doc/html/rfc7636) `code_challenge` with `code_challenge_method=S256` on every authorization request, regardless of which registration mechanism it uses. Your authorization server must support S256 PKCE. The [MCP authorization spec](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization#authorization-code-protection) also requires it to advertise `"code_challenge_methods_supported": ["S256"]` in its metadata so spec-compliant clients can verify support before starting the flow.

To control which scopes Claude requests, include a `scope` parameter in the `WWW-Authenticate` header on your `401` response. If you don't, Claude requests the scopes your protected resource metadata advertises in `scopes_supported`. Claude also appends `offline_access` when your authorization server metadata lists it in `scopes_supported`, to obtain a refresh token. See [lazy authentication](/docs/connectors/building/lazy-authentication#answer-a-protected-call-with-401-before-the-mcp-sdk-runs) for the canonical `401` shape.

## OAuth discovery and redirect URIs

Claude finds your authorization server by reading your protected resource metadata, then sends the user back to a redirect URI that depends on which Claude surface they're using. Both steps have requirements your server and authorization server must meet.

### Serve discovery metadata

Claude locates your authorization server through your [protected resource metadata](https://www.rfc-editor.org/rfc/rfc9728) document, and the authorization server it names can be on a different host from your MCP server. For Claude to find and use that document:

* **Return `401` with a `resource_metadata` pointer**: answer unauthenticated requests with a `401` whose `WWW-Authenticate` header points at the document
* **Make `resource` match your MCP server URL exactly**: the document's `resource` field must equal the URL as the user enters it in Claude, including any path component
* **List your primary issuer first**: the document's `authorization_servers` field must list your authorization server's issuer URL. If you list more than one, Claude uses the first entry and doesn't fall back to later entries
* **Serve authorization server metadata Claude can reach**: your authorization server must serve its own discovery metadata, either [RFC 8414](https://www.rfc-editor.org/rfc/rfc8414) authorization server metadata or [OpenID Connect Discovery 1.0](https://openid.net/specs/openid-connect-discovery-1_0.html), at its `/.well-known/` paths. That host must also be reachable from Anthropic's [published egress range](https://platform.claude.com/docs/en/api/ip-addresses). Discovery requests to the authorization server come from the same IP range as requests to your MCP server, so a WAF in front of your identity provider can break the flow even when your MCP server is reachable

The `401` response carries the pointer in its `WWW-Authenticate` header. This is the same handshake described in [Answer a protected call with 401 before the MCP SDK runs](/docs/connectors/building/lazy-authentication#answer-a-protected-call-with-401-before-the-mcp-sdk-runs):

```http theme={null}
HTTP/1.1 401 Unauthorized
WWW-Authenticate: Bearer resource_metadata="https://mcp.example.com/.well-known/oauth-protected-resource"
```

The `401` status is required, because Claude doesn't honor a `WWW-Authenticate` header on a `200` response. The `resource_metadata` URL doesn't have to be on the MCP server's origin. It can be any HTTPS location that serves the JSON document, which makes this the most reliable path on serverless or edge platforms that only route requests under a path prefix and can't serve `/.well-known/*` at the root.

If your `401` doesn't include a `resource_metadata` pointer, Claude can still infer the metadata location by probing your MCP server's origin: `/.well-known/oauth-protected-resource/<your-mcp-path>` first, then `/.well-known/oauth-protected-resource`. Treat this as a fallback, because it works only when your platform serves `/.well-known/*` paths.

<Note>
  If your authorization server is Microsoft Entra ID, you must also register the MCP server URL as an Application ID URI on your Entra app registration, or the token request fails with `AADSTS9010010`. By default, Entra accepts that URL as an Application ID URI only when it's on a domain your tenant has verified, as described in [Microsoft's identifier URI restrictions](https://learn.microsoft.com/en-us/entra/identity-platform/identifier-uri-restrictions), so an MCP server on a platform hostname such as `*.azurewebsites.net` needs a custom domain first. See [the troubleshooting entry](/docs/connectors/building/troubleshooting#microsoft-entra-id-rejects-the-resource-value) for the fix.
</Note>

If you control both hosts, an alternative is to serve the MCP endpoint and the authorization server behind a single custom domain that can route both `/.well-known/*` and your MCP path.

<Tip>
  A common symptom of a discovery failure is that your MCP server receives the initial request but your authorization server sees no traffic at all. That happens when neither path works: there's no `WWW-Authenticate: Bearer resource_metadata=…` header on your `401`, and the well-known paths on your MCP server's origin return `404`. With no metadata to read, Claude never learns where your authorization server is, and the connection fails with "Couldn't reach the MCP server." See [troubleshooting](/docs/connectors/building/troubleshooting) for the full diagnostic flow.
</Tip>

### Callback URLs

The redirect URI Claude sends depends on which surface the user connects from: the hosted Claude apps use one fixed callback URL and Claude Code uses a loopback redirect. Your authorization server must accept both.

For the hosted Claude apps, which are claude.ai on the web, Desktop, mobile, and Cowork, register exactly this redirect URI:

```text theme={null}
https://claude.ai/api/mcp/auth_callback
```

For Claude Code, accept a loopback redirect on any port. Claude Code is a native client and uses an [RFC 8252](https://datatracker.ietf.org/doc/html/rfc8252) loopback redirect on an ephemeral port that varies per session, such as:

```text theme={null}
http://localhost:3118/callback
```

Claude Code declares `http://localhost/callback` and `http://127.0.0.1/callback` in its [Client ID Metadata Document](https://claude.ai/oauth/claude-code-client-metadata), so match both with the port component ignored. [RFC 8252 section 7.3](https://datatracker.ietf.org/doc/html/rfc8252#section-7.3) requires this for the IP-literal form (`127.0.0.1`). Apply the same port-agnostic match to `localhost` so Claude Code works, even though RFC 8252 section 8.3 discourages `localhost`. See [lazy authentication](/docs/connectors/building/lazy-authentication#match-loopback-redirect-uris-without-the-port) for implementation details.

On your consent screen, display the redirect URI's hostname clearly. The [MCP authorization spec](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization#localhost-redirect-uri-risks) requires this and recommends an extra warning when the only registered redirect URIs are loopback addresses, because any local process can bind a port and claim to be the client.

## Token endpoint requirements

Your token endpoint handles Claude's initial code exchange and every later refresh, and Claude enforces response-time limits on it and on your other OAuth endpoints.

### Token refresh

Claude refreshes tokens reactively on a `401` response, and proactively up to five minutes before the stored expiry. To avoid refresh failures:

* Return RFC 6749-compliant error codes when a refresh token is no longer valid: `invalid_grant`, not `invalid_request` or a custom code
* Rotate refresh tokens for public-client connections. DCR and CIMD register Claude as a public client, and the [MCP authorization spec](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization#token-theft) adopts OAuth 2.1's requirement to rotate or sender-constrain refresh tokens for public clients. If you rotate, return the new refresh token in the same response that invalidates the old one

Your `/token` endpoint must accept `Content-Type: application/x-www-form-urlencoded` per [RFC 6749 section 4.1.3](https://www.rfc-editor.org/rfc/rfc6749#section-4.1.3). Claude sends both the initial token exchange and refresh requests with this content type. Some web frameworks default to JSON-only body parsing, so if your endpoint returns `415 Unsupported Media Type`, register a form-urlencoded body parser. Dynamic client registration at `/register` uses `application/json` per [RFC 7591 section 3.1](https://www.rfc-editor.org/rfc/rfc7591#section-3.1), so don't assume the same parser works for both.

### Endpoint latency

Claude waits up to 10 seconds for a response from your OAuth discovery, registration, and token endpoints, and up to 30 seconds for refresh token requests. If no response arrives within that window, Claude treats the flow as a failure, even if your server eventually completes the request. Aim well under these limits. A token endpoint that takes several seconds to respond produces intermittent connection failures for users.

If your token endpoint depends on slow downstream calls, return the HTTP response headers and body without buffering behind upstream work, and check that any reverse proxy, API gateway, or WAF in front of the endpoint isn't holding the response.

## Enterprise and custom connector authentication

You don't need a separate OAuth application for each enterprise customer, but a customer's organization can supply its own OAuth client or connect its users through SSO without a consent screen.

### Enterprise authentication

Unless your listing asks for credentials at connection time, enterprise customers connect through the same OAuth application as everyone else. Scope what each user can reach with your service's own per-user permissions rather than with a per-tenant OAuth app. These cases work differently:

* **SSO without a consent screen**: organizations using SSO can connect their users with an identity assertion signed by their identity provider instead of an interactive OAuth consent step. See [Enterprise Managed Auth](/docs/connectors/building/enterprise-managed-auth) for what your authorization server needs to support
* **Customer-supplied OAuth client**: a listing that asks for [credentials entered at connection time](#credentials-entered-at-connection-time) has each customer supply its own OAuth client, and an administrator who adds your server as a [custom connector](#custom-connectors) can enter one too

### Custom connectors

When a customer adds your server by URL as a custom connector, Claude identifies itself to your authorization server in one of three ways: with the Client ID Metadata Document that Anthropic hosts for it, through Dynamic Client Registration, or with an OAuth client ID the customer registered with you and enters in the dialog. [Choose authentication settings](/docs/connectors/custom/add-unlisted#choose-authentication-settings) shows the dialog the customer sees. On your side:

* **Support CIMD or DCR**: customers can then connect without registering a client with you first. See [DCR and CIMD details](#dcr-and-cimd-details) for what each needs from your authorization server
* **Require a client secret only for confidential clients**: the secret is optional in the dialog, so customers need one only if your authorization server requires confidential-client authentication
* **Use request headers for a fixed API key or token**: for servers that authenticate with a fixed credential rather than OAuth, request header authentication (`static_headers`) is available in beta. See [Supported authentication types](#supported-authentication-types) and [Authenticate with request headers](/docs/connectors/custom/add-unlisted#authenticate-with-request-headers) for what Owners see

## Network reference

Anthropic's outbound traffic to your server originates from `160.79.104.0/21`. See the [IP address reference](https://platform.claude.com/docs/en/api/ip-addresses) if you need to allowlist Anthropic for conditional access or firewall rules.

## Next steps

* [Lazy authentication](/docs/connectors/building/lazy-authentication): let people use the tools that don't need their account right away, and ask them to sign in only when Claude reaches one that does
* [Enterprise Managed Auth](/docs/connectors/building/enterprise-managed-auth): accept identity assertions from enterprise SSO instead of an interactive consent step
* [Test your connector](/docs/connectors/building/testing): add your server as a custom connector and exercise the auth flow
* [Troubleshoot your connector](/docs/connectors/building/troubleshooting): diagnose "Couldn't reach the MCP server" and "Authorization with the MCP server failed"
