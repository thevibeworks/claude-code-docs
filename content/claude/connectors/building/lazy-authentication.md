> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Lazy authentication for MCP servers

> Let users call public tools immediately and defer OAuth until a protected tool is actually invoked.

Not every tool on an MCP server needs the user's identity. A product catalog can be browsed anonymously; an order history cannot. **Lazy authentication** (sometimes called *mixed auth*) lets a single server expose both: unauthenticated clients can connect, list tools, and call public ones, and the server only challenges for credentials when a protected tool is invoked. The challenge follows the [MCP authorization specification](https://modelcontextprotocol.io/specification/latest/basic/authorization).

In Claude, the challenge surfaces as an inline **Connect** card in the conversation. The user authenticates in a popup, Claude retries the same tool call automatically with the new token, and the turn continues — no context is lost.

<Note>
  If the user's organization has [Enterprise Managed Auth](/docs/connectors/building/enterprise-managed-auth) configured for your connector, the `401` triggers a silent token exchange instead of the **Connect** card. The tool call is retried automatically and the user sees no prompt.
</Note>

The examples below are drawn from a single-file Express app using `@modelcontextprotocol/sdk` over Streamable HTTP.

## Return 401, not a tool error

The only detail that matters is **how** the server refuses an unauthenticated call to a protected tool.

It must fail the **HTTP request** with `401 Unauthorized` and a [`WWW-Authenticate`](https://datatracker.ietf.org/doc/html/rfc6750#section-3) header:

```http theme={null}
HTTP/1.1 401 Unauthorized
WWW-Authenticate: Bearer error="invalid_token", resource_metadata="https://example.com/.well-known/oauth-protected-resource/mcp", scope="orders:read"

{"error":"invalid_token","error_description":"Authentication required for this tool"}
```

The body is advisory; the `401` status and `WWW-Authenticate` header carry the protocol signal. The optional `scope` parameter tells Claude which scopes to request during authorization — include the minimum your protected tools need. If you omit it, Claude requests the scopes your protected resource metadata advertises in `scopes_supported` (plus `offline_access` if your authorization server metadata lists it), which can produce an over-broad consent prompt.

It must **not** return a successful HTTP response wrapping a tool error:

```http theme={null}
HTTP/1.1 200 OK

{"jsonrpc":"2.0","result":{"isError":true,"content":[{"type":"text","text":"Please sign in"}]},"id":1}
```

<Warning>
  A `200` with `isError: true` is an application-level tool failure. Claude passes the error text to the model as the tool result and moves on — there is no auth prompt. Only a transport-level `401` causes Claude to pause the call, run the OAuth flow, and retry. A `403` triggers re-authentication only when accompanied by `WWW-Authenticate: Bearer error="insufficient_scope"` for scope step-up; any other `403` is surfaced as a terminal error. If users are seeing "please sign in" text in the chat instead of a **Connect** button, the server is returning the wrong one.
</Warning>

The `resource_metadata` parameter in the `WWW-Authenticate` header points at the server's [RFC 9728](https://datatracker.ietf.org/doc/html/rfc9728) Protected Resource Metadata (PRM), which in turn names the authorization server. That chain is how Claude discovers where to send the user without any of it being hard-coded in the client.

## Gate at the HTTP layer

Because the refusal must be an HTTP status, the check has to happen **before** the JSON-RPC message reaches the MCP SDK. Once a tool handler is running, its return value is already destined to be wrapped in a `200` response.

The sample inspects the parsed JSON-RPC body in the Express handler and short-circuits if the request is a `tools/call` for a protected tool and no valid bearer is present:

```ts src/index.ts theme={null}
const PROTECTED_TOOLS = new Set(["get_my_orders"]);

function callsProtectedTool(body: unknown): boolean {
  const messages = Array.isArray(body) ? body : [body];
  for (const msg of messages) {
    if (
      msg &&
      typeof msg === "object" &&
      (msg as { method?: unknown }).method === "tools/call"
    ) {
      const name = (msg as { params?: { name?: unknown } }).params?.name;
      if (typeof name === "string" && PROTECTED_TOOLS.has(name)) {
        return true;
      }
    }
  }
  return false;
}

const WWW_AUTHENTICATE =
  `Bearer error="invalid_token", ` +
  `error_description="Authentication required for this tool", ` +
  `resource_metadata="${BASE_URL}/.well-known/oauth-protected-resource/mcp", ` +
  `scope="orders:read"`;

async function handleMcpPost(req: Request, res: Response): Promise<void> {
  const token = extractBearer(req);
  const authed = isTokenValid(token);

  // Lazy-auth gate: fail with 401 BEFORE the MCP layer sees the request.
  // initialize, tools/list, and public tool calls fall through.
  if (!authed && callsProtectedTool(req.body)) {
    res
      .status(401)
      .set("WWW-Authenticate", WWW_AUTHENTICATE)
      .json({
        error: "invalid_token",
        error_description: "Authentication required for this tool",
      });
    return;
  }

  // Otherwise: stateless Streamable HTTP handling.
  const transport = new StreamableHTTPServerTransport({
    sessionIdGenerator: undefined,
    enableJsonResponse: true,
  });
  const mcp = buildMcpServer(authed ? "demo-user" : null);
  await mcp.connect(transport);
  await transport.handleRequest(req, res, req.body);
}

app.post("/mcp", (req, res) => {
  handleMcpPost(req, res).catch((err) => {
    console.error("mcp request error", err);
    if (!res.headersSent) {
      res.status(500).json({
        jsonrpc: "2.0",
        error: { code: -32603, message: "Internal error" },
        id: null,
      });
    }
  });
});
```

`initialize`, `tools/list`, and calls to `list_products` never hit the gate, so the connector is fully usable before sign-in. When the user already has a valid token, every request — public or protected — carries it and the gate is a no-op.

The same pattern covers **scope upgrades**: if the bearer is valid but lacks a required scope, return `403 Forbidden` with `WWW-Authenticate: Bearer error="insufficient_scope", scope="…"` and Claude prompts the user to re-consent. See [Step-up authorization](#step-up-authorization) below for what scopes Claude requests on re-consent and how the challenge is cached.

## Serve the discovery documents

After a 401, Claude fetches the URL from `resource_metadata` to learn which authorization server to use:

```ts src/index.ts theme={null}
function protectedResourceMetadata() {
  return {
    resource: `${BASE_URL}/mcp`,
    authorization_servers: [BASE_URL],
    bearer_methods_supported: ["header"],
  };
}

app.get("/.well-known/oauth-protected-resource", (_req, res) => {
  res.json(protectedResourceMetadata());
});

// Path-suffixed variant per RFC 9728 section 3.1 — clients try this first when
// the resource URL has a path component (/mcp).
app.get("/.well-known/oauth-protected-resource/mcp", (_req, res) => {
  res.json(protectedResourceMetadata());
});
```

Claude then fetches the authorization server's [RFC 8414](https://datatracker.ietf.org/doc/html/rfc8414) metadata to find the `/authorize` and `/token` endpoints.

## OAuth discovery caching

Claude caches the discovery documents — your protected resource metadata and the authorization-server metadata it points to — **globally, keyed by URL**, with a staleness window of about five minutes by default. All Claude users connecting to the same server URL share a single cache entry, and distinct server URLs (for example, staging versus production) cache independently.

The refresh is lazy and best-effort: after you change `scopes_supported` (or any other discovery field), the new value is picked up by the first authorization that successfully re-runs discovery once the staleness window has elapsed, then propagates to everyone. There is no per-user expiry to wait for. If a refresh fails, Claude serves the stale entry and tries again on a later request, so an unreachable discovery endpoint doesn't immediately break existing connections — it just delays the change.

## Step-up authorization

The scope-upgrade case at the end of [Gate at the HTTP layer](#gate-at-the-http-layer) is the MCP specification's [Step-Up Authorization Flow](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization#step-up-authorization-flow). When the bearer token is valid but missing a scope the requested tool needs, return `403 Forbidden` with a [`WWW-Authenticate`](https://datatracker.ietf.org/doc/html/rfc6750#section-3.1) challenge:

```http theme={null}
HTTP/1.1 403 Forbidden
WWW-Authenticate: Bearer error="insufficient_scope", scope="orders:write"
```

Claude prompts the user to re-authorize and, on consent, retries the same tool call with the new token.

**Which scopes Claude requests on re-authorization.** Claude unions the scopes named in your `403` challenge with the scope your server advertises during discovery (the `scope` parameter on your initial `401` `WWW-Authenticate` response, or your protected resource metadata's `scopes_supported` if you don't send one). Scopes the user picked up in an earlier step-up aren't reliably carried forward into the next one. To make sure the user keeps a permission they still need, follow the [MCP spec's recommended approach](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization#runtime-insufficient-scope-errors) and include it in the `403` `scope` value alongside the newly required scopes — don't return only the single missing scope and depend on the client to remember the rest.

If your `403` carries `error="insufficient_scope"` but **omits the `scope` parameter**, Claude still recognizes step-up and runs its normal scope selection: the discovery-time `WWW-Authenticate` scope first, then your protected resource metadata's `scopes_supported`, then the authorization server metadata's `scopes_supported`.

<Note>
  The `scope` value from your `403` is cached **per user, per server** for up to fifteen minutes and consumed by the next re-authorization that user starts against your server. The cache holds the most recent challenge — a new `403` overwrites the previous one — and is cleared once it's used. Combined with the [global discovery cache](#oauth-discovery-caching) above, a newly-added scope is available to step-up shortly after the discovery cache refreshes, typically within about five minutes of deploying the updated metadata.
</Note>

## Identify the client with CIMD

The sample does **not** implement Dynamic Client Registration. Instead it advertises support for **Client ID Metadata Documents** ([draft-ietf-oauth-client-id-metadata-document](https://datatracker.ietf.org/doc/draft-ietf-oauth-client-id-metadata-document/)) in its authorization-server metadata:

```ts src/index.ts theme={null}
function authorizationServerMetadata() {
  return {
    issuer: BASE_URL,
    authorization_endpoint: `${BASE_URL}/authorize`,
    token_endpoint: `${BASE_URL}/token`,
    scopes_supported: ["profile", "orders:read"],
    response_types_supported: ["code"],
    grant_types_supported: ["authorization_code", "refresh_token"],
    token_endpoint_auth_methods_supported: ["none"],
    code_challenge_methods_supported: ["S256"],
    client_id_metadata_document_supported: true,
  };
}
```

With CIMD the `client_id` is itself an HTTPS URL that dereferences to the client's OAuth registration metadata. There is no per-client database and no `POST /register` round-trip: at `/authorize`, the server fetches the `client_id` URL, verifies the document is self-referential (its `client_id` field equals the URL it was served from), and checks the requested `redirect_uri` against the document's `redirect_uris`. Because the document is self-asserted, the consent screen must display the **host of the `client_id` URL** (not the `client_name` field) as the relying party, and the listed `redirect_uris` should be required to be same-origin with the `client_id` URL.

<Note>
  Claude selects CIMD only when the authorization-server metadata advertises **both** `client_id_metadata_document_supported: true` **and** `"none"` in `token_endpoint_auth_methods_supported`. The second is required because Claude's CIMD client authenticates as a public client (`token_endpoint_auth_method: "none"`), so the token endpoint must accept [PKCE](https://datatracker.ietf.org/doc/html/rfc7636)-only requests without a client secret. If either property is missing, Claude falls back to looking for a `registration_endpoint`.
</Note>

For native clients, compare loopback IP `redirect_uri` values (`http://127.0.0.1/…`, `http://[::1]/…`) with the **port ignored**, per [RFC 8252 section 7.3](https://datatracker.ietf.org/doc/html/rfc8252#section-7.3) — native apps bind an ephemeral port at runtime. RFC 8252 section 8.3 discourages `http://localhost/…`, but Claude Code declares it in its CIMD and binds an ephemeral port at runtime, so apply the same port-agnostic match to `localhost` for compatibility. The sample's `redirectUriAllowed()` helper shows the comparison.

## Try it

<Steps>
  <Step title="Run the server">
    ```bash theme={null}
    npm install
    npm run build
    npm start
    ```

    The server listens on `http://localhost:3000/mcp`.
  </Step>

  <Step title="Call a public tool without auth: 200">
    ```bash theme={null}
    curl -s http://localhost:3000/mcp \
      -H 'Content-Type: application/json' \
      -H 'Accept: application/json, text/event-stream' \
      -d '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"list_products","arguments":{}}}'
    ```
  </Step>

  <Step title="Call a protected tool without auth: 401">
    ```bash theme={null}
    curl -si http://localhost:3000/mcp \
      -H 'Content-Type: application/json' \
      -H 'Accept: application/json, text/event-stream' \
      -d '{"jsonrpc":"2.0","id":2,"method":"tools/call","params":{"name":"get_my_orders","arguments":{}}}'
    ```

    Note the `WWW-Authenticate` header in the response.
  </Step>

  <Step title="Add it as a custom connector in Claude">
    Claude reaches custom connectors from Anthropic's infrastructure, so `localhost` is not reachable directly. Expose the server over a public HTTPS tunnel (for example, `cloudflared tunnel --url http://localhost:3000` or `ngrok http 3000`), then in **Customize > Connectors**, select **Add custom connector** and enter the tunnel's `/mcp` URL. See [Testing your connector](/docs/connectors/building/testing) for details.

    Ask Claude to list products (no prompt), then ask for your orders — the inline **Connect** card appears, and after authenticating the same call completes.
  </Step>
</Steps>

The sample's README includes a longer `curl` walkthrough that drives the stub `/authorize` and `/token` endpoints directly.

## Adapting to your server

* List your protected tools in `PROTECTED_TOOLS`.
* Replace `isTokenValid()` with real verification: JWT signature, `iss` matches your authorization server, `aud` equals the `resource` value you advertise in the PRM, and `exp`; or [RFC 7662](https://datatracker.ietf.org/doc/html/rfc7662) token introspection against your IdP.
* Point `authorization_servers` in the PRM at your real issuer and delete the stub `/authorize` and `/token` handlers. Keep `client_id_metadata_document_supported: true` in your issuer's metadata if you want registration-free onboarding for Claude clients.
* If your server uses stateful Streamable HTTP sessions, the gate still belongs in the `POST /mcp` handler, before `transport.handleRequest`.
