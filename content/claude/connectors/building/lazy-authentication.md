> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Lazy authentication for MCP servers

> Let users call public tools immediately and defer OAuth until a protected tool is actually invoked.

A connector that uses OAuth sign-in normally asks each person to sign in as soon as they add it. With lazy authentication, sometimes called mixed auth, your MCP server lets Claude connect, list tools, and call the tools that don't need the person's account right away, and asks for sign-in only when Claude calls a tool that does. A product catalog can be browsed anonymously, for example, while an order history can't.

When Claude reaches a protected tool, it shows the sign-in prompt inline in the conversation, and after the person signs in it retries the same tool call. The challenge your server sends to trigger that prompt follows the [MCP authorization specification](https://modelcontextprotocol.io/specification/latest/basic/authorization).

This page is for developers whose MCP server has some tools that work without the user's identity. It walks through excerpts from an example Express server, a single `src/index.ts` file built on `@modelcontextprotocol/sdk` over Streamable HTTP, to show what your own server needs at each step. For the OAuth requirements every server must meet regardless of when it asks for sign-in, see [Authentication for connectors](/docs/connectors/building/authentication).

## See what the user experiences

A user of a lazy-auth connector goes through these steps:

1. They add your connector and start using it. Claude calls your public tools with no sign-in prompt.
2. They ask for something that needs their account. Claude calls the protected tool, your server refuses it, and an inline **Connect** card appears in the conversation.
3. They click **Connect** and sign in to your service in a popup.
4. Claude retries the same tool call automatically with the new token, and the turn continues with no context lost.

<Note>
  If the user's organization has [Enterprise Managed Auth](/docs/connectors/building/enterprise-managed-auth) configured for your connector, the same refusal triggers a silent token exchange instead of the **Connect** card. Claude retries the tool call automatically and the user sees no prompt.
</Note>

## Build lazy authentication on your server

Your MCP server and your authorization server each have a part in making lazy authentication work.

### Decide which tools need the user's account

Split your tools into the ones anyone can call and the ones that act on the signed-in user's data. Claude can call the first group before sign-in, so keep it to tools that are safe without an identity, such as browsing a public catalog.

In the example server, `list_products` is public and `get_my_orders` is protected. The protected names go in a `PROTECTED_TOOLS` set that the [HTTP handler's gate](#answer-a-protected-call-with-401-before-the-mcp-sdk-runs) checks. List your own protected tools there.

### Answer a protected call with 401 before the MCP SDK runs

Claude starts sign-in only when the HTTP request itself fails with `401 Unauthorized` and a [`WWW-Authenticate`](https://datatracker.ietf.org/doc/html/rfc6750#section-3) header. A tool handler can't produce that response: once the MCP SDK is running a tool, whatever the handler returns is wrapped in a `200`. The check has to run in your HTTP handler, on the parsed JSON-RPC body, before the request reaches the SDK.

On your server, when a request is a `tools/call` for a protected tool and carries no valid bearer token:

* Respond with HTTP status `401`
* Set a `WWW-Authenticate: Bearer` header whose `resource_metadata` parameter points at your [protected resource metadata](#serve-the-discovery-documents) document
* Optionally add a `scope` parameter naming the minimum scopes your protected tools need
* Return from the handler before calling the MCP SDK, and keep the check before `transport.handleRequest` even if your server uses stateful Streamable HTTP sessions

The response Claude expects looks like this:

```http theme={null}
HTTP/1.1 401 Unauthorized
WWW-Authenticate: Bearer error="invalid_token", error_description="Authentication required for this tool", resource_metadata="https://example.com/.well-known/oauth-protected-resource/mcp", scope="orders:read"

{"error":"invalid_token","error_description":"Authentication required for this tool"}
```

The `401` status and the `WWW-Authenticate` header carry the signal, and the body is advisory. The `scope` parameter tells Claude which scopes to request during authorization. If you omit it, Claude requests every scope your protected resource metadata advertises in `scopes_supported`, plus `offline_access` if your authorization server metadata lists it, which can produce an over-broad consent prompt.

In the example server's `POST /mcp` handler, the load-bearing lines are the `PROTECTED_TOOLS` set, the `WWW_AUTHENTICATE` header value with its `resource_metadata` URL, and the gate that sends the `401` and returns before the SDK transport is created. Those lines are highlighted:

```ts src/index.ts {1,22-26,33-41} theme={null}
const PROTECTED_TOOLS = new Set(["get_my_orders"]); // tools that need the user's account

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

// Claude starts sign-in only on HTTP 401 with this header.
// resource_metadata is where Claude looks up your authorization server.
const WWW_AUTHENTICATE =
  `Bearer error="invalid_token", ` +
  `error_description="Authentication required for this tool", ` +
  `resource_metadata="${BASE_URL}/.well-known/oauth-protected-resource/mcp", ` +
  `scope="orders:read"`;

async function handleMcpPost(req: Request, res: Response): Promise<void> {
  const token = extractBearer(req);
  const authed = isTokenValid(token);

  // The gate. initialize, tools/list, and public tool calls fall through.
  if (!authed && callsProtectedTool(req.body)) {
    res
      .status(401)
      .set("WWW-Authenticate", WWW_AUTHENTICATE)
      .json({
        error: "invalid_token",
        error_description: "Authentication required for this tool",
      });
    return; // Return here, before the SDK, or the refusal turns into a 200 tool result.
  }

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

`initialize`, `tools/list`, and calls to `list_products` never hit the gate, so the connector is fully usable before sign-in. When the user already has a valid token, every request carries it, public or protected, and the gate does nothing.

The example server's `isTokenValid()` is a stub. In your server, replace it with real verification: either check the JWT signature, that `iss` matches your authorization server, that `aud` equals the `resource` value you advertise in your protected resource metadata, and `exp`, or use [RFC 7662](https://datatracker.ietf.org/doc/html/rfc7662) token introspection against your identity provider.

#### Don't wrap the refusal in a 200 tool error

A successful HTTP response that wraps a tool error doesn't start sign-in. This is the shape to avoid:

```http theme={null}
HTTP/1.1 200 OK

{"jsonrpc":"2.0","result":{"isError":true,"content":[{"type":"text","text":"Please sign in"}]},"id":1}
```

<Warning>
  A `200` with `isError: true` is an application-level tool failure. Claude passes the error text to the model as the tool result and moves on, and there is no auth prompt. Only a transport-level `401` causes Claude to pause the call, run the OAuth flow, and retry. A `403` triggers re-authentication only when accompanied by `WWW-Authenticate: Bearer error="insufficient_scope"` for [scope step-up](#ask-for-more-scope-with-403), and any other `403` is surfaced as a terminal error. If users are seeing "please sign in" text in the chat instead of a **Connect** button, the server is returning the wrong one.
</Warning>

### Serve the discovery documents

After the `401`, Claude needs to find out where to send the user to sign in, and nothing about your server is hard-coded in Claude. It fetches the `resource_metadata` URL from your `WWW-Authenticate` header, which serves your protected resource metadata: a small [RFC 9728](https://datatracker.ietf.org/doc/html/rfc9728) JSON document that names your MCP endpoint as the `resource` and lists the authorization server that issues tokens for it. Claude then fetches that authorization server's [RFC 8414](https://datatracker.ietf.org/doc/html/rfc8414) metadata to find its `/authorize` and `/token` endpoints.

On your server:

* Serve the protected resource metadata at `/.well-known/oauth-protected-resource/<your-mcp-path>`, the path-suffixed form clients try first when your MCP URL has a path such as `/mcp`, and at `/.well-known/oauth-protected-resource`
* Set `resource` to your MCP endpoint URL and `authorization_servers` to your real issuer

In the example server, one function builds the protected resource metadata document and two routes serve it. The `resource` and `authorization_servers` fields and the path-suffixed route are highlighted:

```ts src/index.ts {3-4,15} theme={null}
function protectedResourceMetadata() {
  return {
    resource: `${BASE_URL}/mcp`, // must match the MCP URL the user adds in Claude
    authorization_servers: [BASE_URL], // your issuer; the example is its own
    bearer_methods_supported: ["header"],
  };
}

app.get("/.well-known/oauth-protected-resource", (_req, res) => {
  res.json(protectedResourceMetadata());
});

// Path-suffixed variant per RFC 9728 section 3.1. Clients try this first
// when the resource URL has a path component (/mcp).
app.get("/.well-known/oauth-protected-resource/mcp", (_req, res) => {
  res.json(protectedResourceMetadata());
});
```

The example server acts as its own authorization server with stub `/authorize` and `/token` handlers. When you point `authorization_servers` at your real issuer, delete those stubs.

### Identify Claude with a client ID metadata document

Before your authorization server shows a consent screen, it has to know which app is asking. The example identifies Claude with a Client ID Metadata Document (CIMD), defined in [draft-ietf-oauth-client-id-metadata-document](https://datatracker.ietf.org/doc/draft-ietf-oauth-client-id-metadata-document/).

With CIMD, Claude's `client_id` is an HTTPS URL, and your authorization server fetches it during `/authorize` to read Claude's registration details. That means you don't register Claude ahead of time, keep a client database, or run a Dynamic Client Registration (DCR) endpoint.

Your `/authorize` endpoint should:

* Fetch the `client_id` URL and check that the document's own `client_id` field equals that URL
* Check the requested `redirect_uri` exactly against the document's `redirect_uris`, matching loopback URIs as [Match loopback redirect URIs without the port](#match-loopback-redirect-uris-without-the-port) describes. You can additionally require non-loopback `redirect_uris` to share the `client_id` URL's origin
* On the consent screen, name the host of the `client_id` URL as the app asking for access, not the document's `client_name`, because the document is self-asserted

Your authorization server advertises CIMD support in its own metadata, the [RFC 8414](https://datatracker.ietf.org/doc/html/rfc8414) document Claude fetches after reading `authorization_servers`. Serve it at the RFC 8414 well-known path, which for the example's issuer is `/.well-known/oauth-authorization-server`. In the example, the two values Claude checks before it uses CIMD are highlighted:

```ts src/index.ts {9,11} theme={null}
function authorizationServerMetadata() {
  return {
    issuer: BASE_URL,
    authorization_endpoint: `${BASE_URL}/authorize`,
    token_endpoint: `${BASE_URL}/token`,
    scopes_supported: ["profile", "orders:read"],
    response_types_supported: ["code"],
    grant_types_supported: ["authorization_code", "refresh_token"],
    token_endpoint_auth_methods_supported: ["none"], // Claude's CIMD client is a public client
    code_challenge_methods_supported: ["S256"],
    client_id_metadata_document_supported: true, // tells Claude it can send its client_id URL
  };
}
```

<Note>
  Claude selects CIMD only when the authorization-server metadata advertises both `client_id_metadata_document_supported: true` and `"none"` in `token_endpoint_auth_methods_supported`. The second is required because Claude's CIMD client authenticates as a public client with `token_endpoint_auth_method: "none"`, so the token endpoint must accept [PKCE](https://datatracker.ietf.org/doc/html/rfc7636)-only requests without a client secret. If either property is missing, Claude falls back to looking for a `registration_endpoint`.
</Note>

If you move to a real issuer, keep `client_id_metadata_document_supported: true` in that issuer's metadata if you want registration-free onboarding for Claude clients.

#### Match loopback redirect URIs without the port

Claude Code is a native client, and native apps bind an ephemeral port at runtime, so the `redirect_uri` Claude Code sends carries a port your `redirect_uris` check can't know in advance. When you compare a requested `redirect_uri` against the document:

* Compare loopback IP values such as `http://127.0.0.1/…` and `http://[::1]/…` with the port ignored, per [RFC 8252 section 7.3](https://datatracker.ietf.org/doc/html/rfc8252#section-7.3)
* Apply the same port-agnostic match to `http://localhost/…`. RFC 8252 section 8.3 discourages `localhost`, but Claude Code declares it in its CIMD, so accept it for compatibility

### Ask for more scope with 403

When a signed-in user calls a tool that needs a scope their token lacks, your server can ask Claude to re-authorize them instead of failing the call. This is the MCP specification's [Step-Up Authorization Flow](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization#step-up-authorization-flow). From the same gate in your HTTP handler, return `403 Forbidden` with a [`WWW-Authenticate`](https://datatracker.ietf.org/doc/html/rfc6750#section-3.1) challenge that names the scopes:

```http theme={null}
HTTP/1.1 403 Forbidden
WWW-Authenticate: Bearer error="insufficient_scope", scope="orders:write"
```

Claude prompts the user to re-authorize and, on consent, retries the same tool call with the new token. The scopes Claude requests on that re-authorization are the union of two sources:

* **Your `403` challenge**: the scopes named in its `scope` parameter. List every scope the user still needs alongside the newly required ones, not only the one that's missing, because scopes the user picked up in an earlier step-up aren't reliably carried forward into the next one. This is the [MCP spec's recommended approach](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization#runtime-insufficient-scope-errors), and it avoids depending on the client to remember the rest
* **Your discovery scope**: the `scope` parameter on your initial `401` `WWW-Authenticate` response, or your protected resource metadata's `scopes_supported` if you don't send one

If your `403` carries `error="insufficient_scope"` but omits the `scope` parameter, Claude still recognizes step-up and runs its normal scope selection: the discovery-time `WWW-Authenticate` scope first, then your protected resource metadata's `scopes_supported`, then the authorization server metadata's `scopes_supported`.

### Allow for discovery caching

After you change `scopes_supported` or any other discovery field, allow about five minutes before Claude uses the new values. Claude caches your protected resource metadata and the authorization-server metadata it points to globally, keyed by URL, with a staleness window of about five minutes by default.

How the cache is keyed and refreshed decides when a change reaches your users:

* **One cache entry per server URL**: all Claude users connecting to the same server URL share a single entry, and distinct URLs, such as staging versus production, cache independently. There is no per-user expiry to wait for
* **Lazy refresh**: the first authorization that successfully re-runs discovery after the window has elapsed picks up the new value, and it then propagates to everyone
* **Stale on failure**: if a refresh fails, Claude serves the stale entry and tries again on a later request, so an unreachable discovery endpoint doesn't immediately break existing connections. It only delays the change

## Test the lazy-auth path

You can confirm the public and protected paths with `curl` and Claude Code against your own server before connecting it to Claude as a custom connector, then check the sign-in prompt in a conversation. The commands below use `http://localhost:3000/mcp` as the server URL and the example's tool names; substitute your own.

<Steps>
  <Step title="Call a public tool without a token">
    In a terminal, send a `tools/call` for a public tool with no `Authorization` header, with `-i` so the status line prints:

    ```bash theme={null}
    curl -si http://localhost:3000/mcp \
      -H 'Content-Type: application/json' \
      -H 'Accept: application/json, text/event-stream' \
      -d '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"list_products","arguments":{}}}'
    ```

    The server answers `200 OK` with the JSON-RPC tool result and no `WWW-Authenticate` header.
  </Step>

  <Step title="Call a protected tool without a token">
    Send the same request for a protected tool:

    ```bash theme={null}
    curl -si http://localhost:3000/mcp \
      -H 'Content-Type: application/json' \
      -H 'Accept: application/json, text/event-stream' \
      -d '{"jsonrpc":"2.0","id":2,"method":"tools/call","params":{"name":"get_my_orders","arguments":{}}}'
    ```

    The server answers `401 Unauthorized` with a `WWW-Authenticate` header carrying `resource_metadata`. If you see `200` with `isError: true` instead, your server is returning a tool error rather than failing the HTTP request.
  </Step>

  <Step title="Check both paths from Claude Code">
    If you have [Claude Code](https://code.claude.com/docs/en/setup) installed and signed in, you can see how a Claude client treats each path before you set up a tunnel, because Claude Code connects to a `localhost` server directly. In your terminal, from your server's project folder, add the server:

    ```bash theme={null}
    claude mcp add --transport http authtest http://localhost:3000/mcp
    ```

    Then check the connection:

    ```bash theme={null}
    claude mcp list
    ```

    The list shows `authtest: http://localhost:3000/mcp (HTTP) - ✔ Connected` with no sign-in, because connecting and listing tools never reach the gate. Next, have Claude call the public tool with [`claude -p`](https://code.claude.com/docs/en/headless), which sends one prompt and prints the answer:

    ```bash theme={null}
    claude -p "List the products from the authtest server." --allowedTools mcp__authtest__list_products
    ```

    Claude reports the products and no sign-in prompt appears. Run the same command asking for your orders with `--allowedTools mcp__authtest__get_my_orders`. The tool result Claude receives is `MCP server "authtest" needs you to sign in again (run /mcp to re-authenticate)` rather than order data.

    To sign in from Claude Code, run `/mcp` in an interactive session as [Authenticate with remote MCP servers](https://code.claude.com/docs/en/mcp#authenticate-with-remote-mcp-servers) describes. When you're done testing, run `claude mcp remove authtest`.
  </Step>

  <Step title="Add the server to Claude as a custom connector">
    Claude reaches custom connectors from Anthropic's infrastructure, so `localhost` isn't reachable directly. To add a local server:

    1. Expose the server over a public HTTPS tunnel, such as `cloudflared tunnel --url http://localhost:3000` or `ngrok http 3000`. Keep the tunnel up only while you test, because it exposes your local server publicly and the example's `/authorize`, `/token`, and `isTokenValid()` are stubs that treat anyone as signed in.
    2. In Claude, go to [**Customize > Connectors**](https://claude.ai/customize/connectors) and select **Add custom connector**.
    3. Enter the tunnel's `/mcp` URL.

    See [Test a local server](/docs/connectors/building/testing#test-a-local-server) for details. If your app comes from the SDK's `createMcpExpressApp()`, that section also shows the `allowedHosts` option you need before requests through the tunnel succeed.
  </Step>

  <Step title="Try both paths in a conversation">
    1. Ask Claude to list products. No sign-in prompt appears.
    2. Ask for your orders. The inline **Connect** card appears, and after you authenticate the same call completes.
  </Step>
</Steps>

## Next steps

* [Authentication for connectors](/docs/connectors/building/authentication): check the OAuth requirements your authorization server must meet, including redirect URIs and token refresh
* [Enterprise Managed Auth](/docs/connectors/building/enterprise-managed-auth): let organizations with SSO answer the same `401` with a silent token exchange
* [Test your connector](/docs/connectors/building/testing): expose the server through a tunnel and add it as a custom connector
* [Troubleshoot your connector](/docs/connectors/building/troubleshooting): diagnose discovery and authorization failures
