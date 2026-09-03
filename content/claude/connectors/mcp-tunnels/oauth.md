> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Authenticate to MCP servers behind a tunnel

> Make OAuth sign-in work for MCP servers reached through an MCP tunnel when the authorization server or identity provider is inside your network. Covers the Tunnel OAuth configuration fields (issuer, authorization endpoint, token endpoint, registration endpoint, scopes) and the split-metadata alternative.

<Note>
  MCP tunnels are in research preview and are available to organizations on the Claude Enterprise plan by request. To request access, [submit the MCP tunnels interest form](https://claude.com/form/mcp-tunnels) or contact your Anthropic account team.
</Note>

An MCP tunnel carries Claude's requests to an MCP server inside your network, but it does not authenticate to that server. Each tunneled server should still require OAuth, as the [MCP authorization specification](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization) describes, so that a member signs in with their own account before Claude can call the server's tools. This page is for the administrator adding a tunneled server as a custom connector, and explains what to configure when the OAuth authorization server is itself only reachable inside your network.

If your authorization server is reachable from the public internet and its metadata advertises public URLs, you don't need anything on this page. Add the connector as described in [Set up an MCP tunnel](/docs/connectors/mcp-tunnels/setup#add-tunneled-servers-as-connectors) and members sign in as they would for any other connector.

## How OAuth works through a tunnel

Two different parties make requests during an OAuth sign-in, and they reach your authorization server by different paths.

* **The member's browser** is redirected to the authorization endpoint to sign in and approve access. This request comes from the member's device, so the authorization endpoint must be a URL their browser can load, either on the public internet or on your corporate network. It can't be a `tunnel.anthropic.com` hostname, because tunnel hostnames accept connections only from Claude.
* **Claude's servers** fetch the authorization server's metadata, register an OAuth client if the server supports dynamic registration, and exchange the authorization code for tokens at the token endpoint. These requests come from Anthropic's network, so the endpoints must be reachable from there, either publicly or through the tunnel.

By default Claude discovers all of these URLs from the metadata your MCP server and authorization server publish. When the authorization server sits inside your network, that metadata usually advertises internal hostnames. Claude then can't reach the token endpoint, or the member's browser is sent to an address it can't load, and sign-in fails.

You fix this by routing Claude's server-to-server calls through the tunnel and telling Claude explicitly which URL to use for each endpoint.

## Route the authorization server through the tunnel

Add a route for the authorization server to the proxy configuration, next to the routes for your MCP servers, and apply it as described in [Add more servers later](/docs/connectors/mcp-tunnels/setup#add-more-servers-later).

```yaml theme={null}
routes:
  docs: http://docs-mcp.example.corp:8080
  auth: https://sso.example.corp:8443
```

With a tunnel domain of `abc123.tunnel.anthropic.com`, Claude can now reach the authorization server at `https://auth.abc123.tunnel.anthropic.com`. For an `https://` upstream like this one, also set `upstream.tls.ca_file` or `upstream.tls.include_system_cas` in the proxy configuration so the proxy can verify the server's certificate. See the [proxy configuration reference](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/reference#proxy-configuration).

## Set the Tunnel OAuth configuration

When you add the tunneled MCP server as a custom connector in **Organization settings > Connectors**, turn on **Tunnel OAuth configuration** in the connector dialog. The values you enter replace the ones Claude would otherwise read from the authorization server's metadata. Anthropic enables this option for each organization in the research preview on request, so if the toggle does not appear in the dialog, contact your Anthropic account team.

| Field                                | What to enter                                                                                                                                                                                                                                                                                                  | Example                                                   |
| ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| **Issuer**                           | The issuer identifier your authorization server puts in its metadata and tokens. This can be an internal URL, because Claude uses it for validation rather than as an address to connect to.                                                                                                                   | `https://sso.example.corp:8443`                           |
| **Authorization endpoint**           | The sign-in URL that members' browsers are redirected to. It must be loadable from their devices, on the public internet or your corporate network.                                                                                                                                                            | `https://sso.example.corp/authorize`                      |
| **Token endpoint**                   | The token endpoint Claude exchanges the authorization code at. Either the endpoint as reached through the tunnel (an `https://` URL under your tunnel domain), or a public `https://` URL on the same origin (scheme, host, and port) as the **Authorization endpoint**.                                       | `https://auth.abc123.tunnel.anthropic.com/oauth/token`    |
| **Registration endpoint (optional)** | The dynamic client registration endpoint, under the same rule as **Token endpoint**: a URL under your tunnel domain or one on the **Authorization endpoint**'s origin. Leave it blank if you select **Use your own OAuth client** and enter a client ID you registered with the authorization server yourself. | `https://auth.abc123.tunnel.anthropic.com/oauth/register` |
| **Requested scopes**                 | The scopes Claude requests at sign-in, separated by spaces.                                                                                                                                                                                                                                                    | `openid wiki:read wiki:write`                             |

The paths after the hostname (`/authorize`, `/oauth/token`, and so on) are whatever your authorization server uses. Copy them from its metadata document, usually served at `/.well-known/oauth-authorization-server` or `/.well-known/openid-configuration`, and change only the scheme and host.

After you save the connector, connect it yourself from your own connector settings. Your browser should land on your sign-in page, and after you approve access the connector should show as connected. If either step fails, see [Troubleshooting](/docs/connectors/mcp-tunnels/troubleshooting#sign-in-redirects-to-a-tunnel-address-that-does-not-load).

## Publish split metadata instead

If you operate the authorization server and can change the metadata it publishes, you can get the same result without the connector settings by advertising the split yourself. Point `authorization_endpoint` at the browser-reachable hostname and every other endpoint at the tunnel hostname in the authorization server's `/.well-known/oauth-authorization-server` document:

```json theme={null}
{
  "issuer": "https://auth.abc123.tunnel.anthropic.com",
  "authorization_endpoint": "https://sso.example.corp/authorize",
  "token_endpoint": "https://auth.abc123.tunnel.anthropic.com/oauth/token",
  "registration_endpoint": "https://auth.abc123.tunnel.anthropic.com/oauth/register",
  "code_challenge_methods_supported": ["S256"]
}
```

Then have the MCP server's `/.well-known/oauth-protected-resource` document name the tunnel hostname as its authorization server:

```json theme={null}
{
  "resource": "https://docs.abc123.tunnel.anthropic.com/mcp",
  "authorization_servers": ["https://auth.abc123.tunnel.anthropic.com"]
}
```

This approach also suits an authorization server that is publicly reachable but sits behind a source-IP allowlist that you don't want to open to Anthropic's egress ranges. The [platform troubleshooting guide](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/troubleshooting#oauth-fails-behind-a-source-ip-allowlist) walks through the same configuration.

Use **Tunnel OAuth configuration** when the authorization server is a product whose metadata you can't edit, or when you prefer to keep tunnel-specific addresses out of the server's configuration. Use split metadata when you control the authorization server and want the configuration to apply to every client that discovers it through the tunnel.
