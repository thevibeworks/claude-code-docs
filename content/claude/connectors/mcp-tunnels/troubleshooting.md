> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Troubleshoot MCP tunnels

> Fix MCP tunnel problems: cloudflared won't connect, connector added but tools don't appear, no route for host, IP validation failed, TLS handshake failed, expired certificate, OAuth sign-in redirects to a tunnel.anthropic.com URL, token exchange fails, and setup or Helm hook errors.

<Note>
  MCP tunnels are in research preview and are available to organizations on the Claude Enterprise plan by request. To request access, [submit the MCP tunnels interest form](https://claude.com/form/mcp-tunnels) or contact your Anthropic account team.
</Note>

A request through an [MCP tunnel](/docs/connectors/mcp-tunnels/overview) can fail at three points, and it helps to check them in order. First the outbound connection from cloudflared to the tunnel edge, then the inner TLS handshake between Anthropic and your proxy, then the proxy's routing to your MCP server. The cloudflared and proxy logs on your side show which point a request reached. If the proxy logs nothing at all for a request, it never arrived in your network.

<CodeGroup>
  ```bash Helm theme={null}
  kubectl -n mcp-tunnel logs deploy/mcp-tunnel -c cloudflared
  kubectl -n mcp-tunnel logs deploy/mcp-tunnel -c mcp-proxy
  ```

  ```bash Docker Compose theme={null}
  docker compose logs cloudflared
  docker compose logs mcp-proxy
  ```
</CodeGroup>

For proxy configuration fields and certificate rules referenced below, see the [MCP tunnels reference](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/reference). The [platform troubleshooting guide](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/troubleshooting) covers the same stack and applies to claude.ai tunnels as well, apart from its Console-specific steps.

## Connection

### The tunnel stack starts but cloudflared never connects

cloudflared logs four `Registered tunnel connection` lines when it reaches the tunnel edge. If they never appear, the cause is almost always one of two things. Either `TUNNEL_TOKEN` is missing, truncated, or from a token that has since been rotated, or a firewall is blocking outbound TCP and UDP on port 7844 to the edge ranges `198.41.192.0/19` and `2606:4700:a0::/44`. On Docker Compose, confirm the variable is exported in the shell that ran `docker compose up`. After a token rotation, restart cloudflared on every host with the new value.

### cloudflared logs `failed to sufficiently increase receive buffer size`

This is a QUIC tuning hint, not an error, and the tunnel works without addressing it. To remove the warning, raise the host's UDP buffer limits as described in the [quic-go UDP buffer documentation](https://github.com/quic-go/quic-go/wiki/UDP-Buffer-Sizes).

### The setup component fails with an authentication or permission error

The setup component authenticates to the Tunnels API with the key in `API_TOKEN` (Docker Compose) or `api.token` (Helm). A `401` or `403` means the key was revoked, was copied incompletely, or was created in a different organization from the one where MCP tunnels are enabled. Create a new key under **Organization settings > Tunnels > Tunnels API** in the claude.ai organization whose members will use the connectors, and run setup again.

### Setup fails with `Organization already has the maximum of 10 non-archived Tunnels`

Each organization can have at most 10 tunnels that are not archived, and every setup run with an empty `tunnel.id` (Helm) or no `--tunnel-id` (Docker Compose) creates a new one. Archive tunnels you no longer use, as described in [Remove a tunnel](/docs/connectors/mcp-tunnels/setup#remove-a-tunnel), then run setup again. To attach a new deployment to an existing tunnel instead of creating one, set `tunnel.id` in `values.yaml` or pass `--tunnel-id` to the setup command.

### Helm install fails with a hook error

The setup component runs as a pre-install hook Job, and on failure Helm leaves the Job behind for inspection. Read its logs, then delete it before retrying, because Helm does not manage hook resources.

```bash theme={null}
kubectl -n mcp-tunnel logs job/mcp-tunnel-setup
helm uninstall mcp-tunnel -n mcp-tunnel
kubectl -n mcp-tunnel delete job mcp-tunnel-setup
```

### A tunnel hostname does not respond to curl or a browser

This is expected. Hostnames under `tunnel.anthropic.com` accept connections only from Claude, so you can't test them from your own network or the internet. Verify the tunnel by connecting the custom connector in Claude and calling one of the server's tools while you watch the proxy logs.

## Routes and certificates

### Proxy logs `no route for host`

The hostname Claude sent the request to did not match any route. Check that `tunnel_domain` in the proxy configuration exactly matches the domain the setup component reported (Helm sets this for you), that the subdomain in the connector URL matches a key under `routes`, and that you restarted the proxy or ran `helm upgrade` after editing routes.

### Proxy logs `IP validation failed`

The full message is `IP validation failed: <ip> is not a private address`, and it means the MCP server's hostname resolved to an address outside the ranges the proxy is allowed to dial. By default those are the RFC 1918 private ranges, over IPv4 only. Check what the hostname resolves to from the proxy's host:

```bash theme={null}
dig +short docs-mcp.example.corp
```

If the address is legitimate, for example a Kubernetes Service range that your distribution allocates outside RFC 1918, add the narrowest covering range to `upstream.allowed_ips`. Setting `allowed_ips` replaces the default rather than extending it, so list the private ranges your other servers use as well.

```yaml theme={null}
upstream:
  allowed_ips:
    - 10.0.0.0/8
    - 172.16.0.0/12
    - 192.168.0.0/16
    - 100.64.12.0/22   # example: a cluster Service range outside RFC 1918
```

<Warning>
  Don't set `0.0.0.0/0` or `disable_ip_validation` outside of isolated testing. IP validation is the proxy's protection against server-side request forgery.
</Warning>

### Proxy exits with `cannot unmarshal !!seq into map[string]string`

`routes` was written as a YAML list. It must be a map from subdomain to upstream URL, for example `routes: { docs: "http://docs-mcp.example.corp:8080" }`.

### Proxy exits with `invalid upstream (must be scheme://host:port)`

A route value includes a path or omits the port. Each upstream must be exactly `scheme://host:port`. Put the path in the connector URL instead, because the proxy forwards the request path unchanged.

### Proxy logs `tls handshake failed`

Anthropic rejected the certificate the proxy presented. Check that the server certificate has not passed its 90-day validity, that its Subject Alternative Name covers `*.<your-tunnel-domain>`, and that it was signed by the CA the setup component registered for this tunnel. On Docker Compose, also confirm the files in `data/` are readable by user ID `65532`. To renew an expired certificate, see [Rotate credentials](/docs/connectors/mcp-tunnels/setup#rotate-credentials).

## Connectors and tools

### Adding the connector fails, or it connects but no tools appear

Work through these checks in order.

1. Confirm the stack is connected, using the log checks in [Verify the connection](/docs/connectors/mcp-tunnels/setup#verify-the-connection).
2. Confirm the tunnel was created with a Tunnels API key from the same claude.ai organization where you are adding the connector. A tunnel created from another organization, including a Claude Console organization, is refused before any traffic reaches your network, and your proxy logs show nothing.
3. Confirm the connector URL includes the path your MCP server serves, such as `/mcp`. A request to the bare hostname reaches the proxy but the server may answer `404`.
4. Watch the proxy logs while you retry. `no route for host` and `IP validation failed` point to the sections above. An upstream connection error means the proxy can't reach the MCP server from where it runs.

## OAuth sign-in

See [Authenticate to MCP servers behind a tunnel](/docs/connectors/mcp-tunnels/oauth) for how the sign-in flow splits between the member's browser and Claude's servers.

### Sign-in redirects to a tunnel address that does not load

The authorization server's metadata advertises an authorization endpoint on the `tunnel.anthropic.com` hostname or an internal hostname, and the member's browser can't load it. Turn on **Tunnel OAuth configuration** for the connector and set **Authorization endpoint** to the sign-in URL members' browsers can reach, or publish split metadata from the authorization server. Both are described on the [OAuth page](/docs/connectors/mcp-tunnels/oauth#set-the-tunnel-oauth-configuration).

### Sign-in succeeds in the browser but the connector never connects

Claude could not complete the token exchange, usually because the token endpoint in the metadata is an internal hostname or sits behind a source-IP allowlist. Add a proxy route for the authorization server and set **Token endpoint** (and **Registration endpoint**, if you rely on dynamic client registration) to the corresponding `https://<route>.<your-tunnel-domain>/...` URLs. Then watch the proxy logs during sign-in to confirm the token request arrives and the authorization server answers it.

### The Token endpoint field rejects the URL

**Token endpoint** and **Registration endpoint** accept an `https://` URL that is either under `tunnel.anthropic.com` or on the same origin (scheme, host, and port) as the **Authorization endpoint**. Any other URL is rejected, because Claude sends the token exchange and the client credentials to it. Add a route for your authorization server as shown in [Route the authorization server through the tunnel](/docs/connectors/mcp-tunnels/oauth#route-the-authorization-server-through-the-tunnel) and enter the resulting tunnel URL. The **Authorization endpoint** field has no such restriction, because browsers load it directly.

### The Tunnel OAuth configuration toggle is missing

Anthropic enables the option for each organization in the research preview on request. Contact your Anthropic account team.

## Get help

If these steps don't resolve the problem, contact your Anthropic account team with the tunnel domain, the time of a failed request, and the relevant cloudflared and proxy log lines.
