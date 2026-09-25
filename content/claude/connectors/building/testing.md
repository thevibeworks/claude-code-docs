> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Test your connector

> Test your MCP server against Claude as a custom connector before you submit it to the directory, including a local server exposed through a tunnel.

You test an MCP server against the real Claude client by adding it to Claude as a custom connector. There is no separate staging environment, so you test in production. Custom connectors use the exact same runtime as directory connectors, and what works as a custom connector will work after publication.

This page is for developers with a running server, whether it's deployed or still on your machine. It covers adding the server to Claude, validating it with MCP Inspector, detecting Claude as the client, and preparing test credentials for directory review. If a connection fails while you test, [Troubleshoot your connector](/docs/connectors/building/troubleshooting) walks through each error message.

## Test in Claude as a custom connector

To test your server the way users will reach it, add it to your own Claude account as a custom connector by its URL. Any Claude account can do this, on Free, Pro, Max, Team, or Enterprise; [Add a connector that isn't in the directory](/docs/connectors/custom/add-unlisted#add-a-connector-by-url) has the steps for each plan, starting from [**Customize > Connectors**](https://claude.ai/customize/connectors).

Once the connector is added, check these:

* **The connection**: the connector shows **Connected** under **Your connectors**. If it shows **Connect** or **Reconnect** instead, sign-in didn't finish, and [Debug connection failures](#debug-connection-failures) covers the usual causes
* **Your tools**: open the connector's page and look under **Tool permissions**. Every tool your server advertises should be listed with the name and description you gave it, because those are what Claude reads when it decides to call a tool
* **A real call**: in a chat, turn the connector on from **+ > Connectors**, ask for something that needs one of your tools, and approve the call when Claude asks. Confirm on your server that the request arrived with the arguments you expected, and in Claude that the result reads well. [Use the connector in a conversation](/docs/connectors/getting-started#use-the-connector-in-a-conversation) shows what the user sees at each point

### Test a local server

Claude reaches your server from Anthropic's infrastructure, so a server running on your machine needs a public URL. Expose it with a tunnel such as [Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/) or `ngrok`, then add the tunnel URL as a custom connector. This is the recommended pattern for iterating on MCP Apps as well.

If your server uses the TypeScript SDK's `createMcpExpressApp()`, as the [quickstart server](/docs/connectors/building/quickstart) does, its DNS rebinding protection accepts only `localhost`, `127.0.0.1`, and `[::1]` in the `Host` header. A request that arrives with the tunnel's hostname in that header gets `403` with `Invalid Host: <hostname>`, and the connection fails. While you test through the tunnel, pass the tunnel's hostname in `allowedHosts`, replacing `abc123.example.com` with your tunnel's hostname:

```js theme={null}
const app = createMcpExpressApp({ allowedHosts: ['localhost', '127.0.0.1', 'abc123.example.com'] });
```

<Warning>
  A tunnel exposes your local server to the public internet. Keep authentication enabled on your server while tunneling, and shut the tunnel down when you're done testing.
</Warning>

### Validate with MCP Inspector

Before connecting to Claude, use the [MCP Inspector](https://modelcontextprotocol.io/docs/tools/inspector) to verify protocol compliance, exercise your auth flow, and inspect tool schemas. With your server running, run the Inspector's command-line mode from a terminal against your server's URL, replacing `http://localhost:3000/mcp` with your own:

```bash theme={null}
npx @modelcontextprotocol/inspector --cli http://localhost:3000/mcp --transport http --method tools/list
```

The command lists the tools your server advertises. Change `--method` to `tools/call` with `--tool-name` and `--tool-arg` options to call one.

## Detect Claude as the client

Claude identifies itself in the MCP `initialize` handshake through `clientInfo`, but the exact value depends on the surface and the request path. You may see `"name": "claude-ai"`, `"name": "Anthropic"`, sometimes with a service suffix, or `"name": "claude-code"`. One handshake looks like this:

```json theme={null}
{ "clientInfo": { "name": "Anthropic", "version": "1.0.0" } }
```

Don't gate behavior on an exact `name` or `version` string, because both vary across surfaces, request paths, and releases. Use `clientInfo` for telemetry and coarse feature detection only. It's also unauthenticated: any client can claim any name, so it must never feed an authorization decision.

## Prepare test credentials for review

Directory submission requires test credentials. Provide a fully populated account rather than an empty shell, so reviewers can exercise real functionality: list real records, search real data, and exercise write tools on real resources. Include step-by-step setup instructions for someone unfamiliar with your service.

## Debug connection failures

Use server-side logging on your end and the MCP Inspector to diagnose connection failures. An `initialize` timeout commonly has one of these causes:

* **Slow OAuth endpoints**: keep discovery, registration, and token responses under ten seconds, as described in [endpoint latency](/docs/connectors/building/authentication#endpoint-latency)
* **Strict `Origin`-header validation**: an overly strict check rejects Anthropic's requests
* **Firewalls**: a firewall drops Anthropic's egress traffic

If your infrastructure logs show `403 Forbidden` responses your application didn't generate, your CDN or WAF is likely blocking Anthropic's traffic. See [firewall or WAF blocks traffic from Anthropic](/docs/connectors/building/troubleshooting#firewall-or-waf-blocks-traffic-from-anthropic) for the fix.

For a structured walkthrough of the "Couldn't reach the MCP server" and "Authorization failed" errors, see [Troubleshoot your connector](/docs/connectors/building/troubleshooting). It includes DNS resolution checks, OAuth discovery diagnostics, and how to find the `ofid_` reference ID to include in a support request.

## Next steps

* [Troubleshoot your connector](/docs/connectors/building/troubleshooting): diagnose each error message Claude shows for a failed connection or tool call
* [Plugin structure and testing](/docs/plugins/build): bundle your tested connector with skills so people install both together
* [Publish to the directory](/docs/directory/publish): submit your connector for review and listing
