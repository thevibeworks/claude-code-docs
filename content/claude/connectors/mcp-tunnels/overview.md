> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# MCP tunnels

> Connect Claude to MCP servers inside your private network without opening inbound firewall ports or exposing the servers to the internet. How MCP tunnels work, what you deploy, network and plan requirements, and the security model.

<Note>
  MCP tunnels are in research preview and are available to organizations on the Claude Enterprise plan by request. To request access, contact your Anthropic account team. The preview is provided as-is, without uptime, support, or continuity commitments, and it depends on a third-party network provider (Cloudflare) that makes no availability commitment for the underlying transport. Anthropic may modify or discontinue MCP tunnels at any time.
</Note>

MCP tunnels connect Claude to [Model Context Protocol (MCP)](/docs/connectors/building/mcp) servers that run inside your private network. You run a small tunnel stack on a host in your network, the stack opens an outbound-only connection to Anthropic, and Claude sends MCP requests to your servers over that connection. Your firewall needs no inbound rules and your MCP servers need no public endpoint. Members of your organization use the tunneled servers as [custom connectors](/docs/connectors/custom/remote-mcp) in Claude, the same way they use any other remote MCP server.

This section is for administrators of claude.ai organizations on the Enterprise plan and the infrastructure teams they work with. To use MCP tunnels with the Claude Console, Claude Managed Agents, or the Messages API, see [MCP tunnels in the Claude Platform docs](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/overview). A tunnel belongs to the organization that created it, so a tunnel created from a Console organization can't serve connectors in claude.ai, and a tunnel created from claude.ai can't serve the API.

## When to use an MCP tunnel

Use a tunnel when the MCP server your organization wants to reach from Claude is only reachable inside your network, and your security policy rules out giving it a public endpoint or allowlisting Anthropic's IP ranges at your edge. Internal knowledge bases, ticketing systems, and data services wrapped in an MCP server are typical candidates.

If the MCP server is already reachable from the internet, you don't need a tunnel. Add it as a [custom connector](/docs/connectors/custom/remote-mcp) directly.

## How traffic flows

The tunnel stack is two containers that you run inside your network, from images that Anthropic and Cloudflare publish:

* **cloudflared** is Cloudflare's open-source tunnel connector. It dials out from your network to the tunnel edge and keeps that connection open. It never listens on an inbound port.
* **The proxy** (`mcp-proxy`) is Anthropic's routing component. It terminates an inner layer of TLS, checks that each destination address falls inside an allowed private range, and forwards each request to the right MCP server based on the hostname it was sent to.

When you create a tunnel, Anthropic assigns it a domain such as `abc123.tunnel.anthropic.com`. Each MCP server you expose gets a subdomain of that domain, chosen by you in the proxy's route configuration. A route named `docs` that points at `http://docs-mcp.example.corp:8080` makes that server reachable from Claude at `https://docs.abc123.tunnel.anthropic.com`.

A request then travels like this:

1. cloudflared opens an outbound connection from your network to the tunnel edge on port 7844 and holds it open.
2. A member uses the connector in Claude. Claude sends the MCP request to `docs.abc123.tunnel.anthropic.com`, and the request travels over the already-open connection to cloudflared and then to the proxy.
3. The proxy decrypts the request, looks up the `docs` route, and forwards the request to `docs-mcp.example.corp:8080`. The response returns along the same path.

Hostnames under `tunnel.anthropic.com` accept connections only from Claude. You can't open them in a browser or test them with `curl` from your own network, so you verify a tunnel by using it from Claude.

## What you need

* A claude.ai organization on the Enterprise plan with MCP tunnels enabled. Contact your Anthropic account team to request access.
* The Owner or Primary Owner role in that organization, to create the API key the tunnel setup uses and to add the tunneled servers as connectors.
* A place to run the tunnel stack inside your network: a Kubernetes cluster (deployed with Helm) or a Linux host with Docker and Docker Compose. One stack serves one tunnel, and you can run replicas of it on several hosts for availability.
* One or more MCP servers that speak the Streamable HTTP transport and are reachable from that cluster or host.
* Outbound network access from the stack as listed under [Network requirements](#network-requirements).

### Network requirements

| Component       | Destination                                          | Port and protocol            | Used during                  |
| --------------- | ---------------------------------------------------- | ---------------------------- | ---------------------------- |
| Setup component | `api.anthropic.com`                                  | 443 TCP                      | Provisioning, token rotation |
| cloudflared     | Tunnel edge (`198.41.192.0/19`, `2606:4700:a0::/44`) | 7844 TCP and UDP             | Runtime                      |
| Proxy           | Your MCP servers                                     | As configured in your routes | Runtime                      |

No inbound rules are required. See [Cloudflare's tunnel firewall documentation](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-with-firewall/) for the authoritative edge IP list.

## Security model

Three independent layers protect every request through a tunnel.

| Layer                                                                             | Protects against                                                         |
| --------------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| Outer mutual TLS between Anthropic and the transport provider, with IP validation | Unauthorized clients reaching the tunnel                                 |
| Inner TLS from Anthropic's backend to your proxy                                  | Payload inspection by the transport provider or any network intermediary |
| OAuth on each MCP server                                                          | Unauthorized use of MCP tools by traffic that has reached the server     |

The proxy terminates inner TLS with a certificate signed by a certificate authority (CA) that the setup component generates inside your environment and registers with Anthropic. Only your deployment holds the private keys, so Cloudflare carries ciphertext and cannot read MCP requests or responses. Anthropic does not connect to a tunnel until a CA certificate is registered for it. Cloudflare does receive connection metadata: the egress IP address and a host fingerprint of the machine running cloudflared, connection timing and byte volume, and the `tunnel.anthropic.com` subdomain assigned to your tunnel. Cloudflare acts as a subprocessor for this research preview.

The tunnel carries traffic to your MCP servers but does not authenticate to them. Configure each MCP server to require OAuth as described in the [MCP authorization specification](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization), and see [Authenticate to MCP servers behind a tunnel](/docs/connectors/mcp-tunnels/oauth) for how sign-in works when the authorization server is also inside your network.

### Shared responsibility

| Anthropic handles                                                     | Your organization handles                                                                                                                     |
| --------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| Restricting tunnel access so that only Anthropic can connect          | All content and traffic that transits your tunnel, and compliance with applicable third-party acceptable-use policies, including Cloudflare's |
| Validating your CA certificate before connecting to your proxy        | Securing the tunnel token, the Tunnels API key, and the TLS private keys                                                                      |
| Sending Claude's requests only to tunnels that your organization owns | Renewing the server certificate before it expires                                                                                             |
|                                                                       | Requiring OAuth on each MCP server and limiting each server to the tools it needs                                                             |
|                                                                       | Restricting network access for the proxy hosts and MCP servers                                                                                |
|                                                                       | Notifying Anthropic if you suspect a compromise                                                                                               |

<Warning>
  An attacker who obtains your tunnel token and one of your TLS private keys could impersonate your proxy and read MCP request payloads, including OAuth tokens. Store both with your organization's secrets-management controls, restrict file permissions, and rotate them on a schedule and immediately after any suspected exposure. See [Rotate credentials](/docs/connectors/mcp-tunnels/setup#rotate-credentials).
</Warning>

## Limits

* An organization can have up to 10 active tunnels.
* A tunnel holds up to two active CA certificates at a time, so you can rotate without downtime.
* The server certificate that the setup component generates is valid for 90 days.
* The proxy connects to upstream MCP servers over IPv4 only, and by default only to addresses in the RFC 1918 private ranges (`10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`).

## Next steps

<Columns cols={2}>
  <Card title="Set up an MCP tunnel" icon="rocket" href="/docs/connectors/mcp-tunnels/setup">
    Create the API key, deploy the tunnel stack with Helm or Docker Compose, and add your servers as connectors.
  </Card>

  <Card title="Authenticate through a tunnel" icon="lock" href="/docs/connectors/mcp-tunnels/oauth">
    Make OAuth sign-in work when your authorization server is inside your network.
  </Card>

  <Card title="Troubleshooting" icon="wrench" href="/docs/connectors/mcp-tunnels/troubleshooting">
    Diagnose connection, certificate, routing, and sign-in failures.
  </Card>

  <Card title="Platform reference" icon="book" href="https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/reference">
    Proxy configuration fields, certificate requirements, and the setup component.
  </Card>
</Columns>
