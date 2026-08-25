> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Testing your connector

> Test your MCP server against Claude before submitting to the directory

Test your server against the real Claude client before submitting. There is no separate staging environment—you test in production using a custom connector.

## Test as a custom connector

Any Claude account (Free, Pro, Max, Team, or Enterprise) can add a custom connector. Go to **Customize > Connectors**, select **Add custom connector**, and enter your server's URL. Custom connectors use the exact same runtime as directory connectors, so what works here will work after publication.

## Test a local server

To test a server running on your machine, expose it as a public URL with a tunnel such as [Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/) or `ngrok`, then add the tunnel URL as a custom connector. This is the recommended pattern for iterating on MCP Apps as well.

<Warning>
  A tunnel exposes your local server to the public internet. Keep authentication enabled on your server while tunneling, and shut the tunnel down when you're done testing.
</Warning>

## Validate with MCP Inspector

Use the [MCP Inspector](https://modelcontextprotocol.io/docs/tools/inspector) to verify protocol compliance, exercise your auth flow, and inspect tool schemas before connecting to Claude.

## Detect Claude as the client

Claude identifies itself in the MCP `initialize` handshake via `clientInfo`, but the exact value depends on the surface and the request path. You may see `"name": "claude-ai"`, `"name": "Anthropic"` (sometimes with a service suffix), or `"name": "claude-code"`:

```json theme={null}
{ "clientInfo": { "name": "Anthropic", "version": "1.0.0" } }
```

Don't gate behavior on an exact `name` or `version` string — both vary across surfaces, request paths, and releases. Use `clientInfo` for telemetry and coarse feature detection only, and remember it's unauthenticated: any client can claim any name, so it must never feed an authorization decision.

## Prepare test credentials for review

Directory submission requires test credentials. Provide a **fully populated account**—not an empty shell—so reviewers can exercise real functionality (list real records, search real data, exercise write tools on real resources). Include step-by-step setup instructions for someone unfamiliar with your service.

## Debugging

Partner-visible error logs are in development. In the meantime, use server-side logging on your end and the MCP Inspector to diagnose connection failures. Common causes of `initialize` timeouts include slow OAuth endpoints (keep discovery, registration, and token responses under ten seconds; see [endpoint latency](/docs/connectors/building/authentication#endpoint-latency)), overly strict `Origin`-header validation rejecting Anthropic's requests, and firewalls dropping Anthropic's egress traffic.

If your infrastructure logs show `403 Forbidden` responses your application didn't generate, your CDN or WAF is likely blocking Anthropic's traffic. See [firewall or WAF blocks Anthropic's traffic](/docs/connectors/building/troubleshooting#2-firewall-or-waf-blocks-anthropic%E2%80%99s-traffic) for the fix.

For a structured walkthrough of "Couldn't reach the MCP server" and "Authorization failed" errors, including DNS resolution checks, OAuth discovery diagnostics, and how to find the `ofid_` reference ID to include in a support request, see [troubleshooting connectors](/docs/connectors/building/troubleshooting).
