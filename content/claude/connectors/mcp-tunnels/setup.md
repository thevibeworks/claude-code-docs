> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Set up an MCP tunnel

> Create a Tunnels API key in claude.ai, deploy the MCP tunnel stack with Helm or Docker Compose, verify the connection, add tunneled MCP servers as custom connectors, rotate the tunnel token and certificates, and remove a tunnel.

<Note>
  MCP tunnels are in research preview and are available to organizations on the Claude Enterprise plan by request. To request access, contact your Anthropic account team.
</Note>

This page covers the full setup of an MCP tunnel for a claude.ai Enterprise organization, from creating the API key that provisioning uses to members calling a tunneled MCP server from Claude. You need the Owner or Primary Owner role in claude.ai, and someone who can deploy containers to a Kubernetes cluster or a Docker host inside your network. Read [MCP tunnels](/docs/connectors/mcp-tunnels/overview) first if the tunnel stack, the tunnel domain, and routes are unfamiliar.

The deployment steps on this page are reference deployments. You are responsible for adapting them to your organization's security requirements. For the full set of proxy options, certificate requirements, and hardening guidance, see the [MCP tunnels reference](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/reference) and [MCP tunnels security](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/security) pages in the Claude Platform docs. Those pages describe the Claude Console flow, which authenticates the setup component differently. For a claude.ai organization, follow the authentication steps on this page.

## Create a Tunnels API key

The setup component that runs alongside the tunnel stack needs a short-lived credential to create the tunnel, register its certificate authority (CA) certificate with Anthropic, and fetch the tunnel token. In claude.ai that credential is a Tunnels API key.

1. In claude.ai, go to **Organization settings > Tunnels**. This page appears once Anthropic has enabled MCP tunnels for your organization.
2. Open **Tunnels API** and create a key.
3. Copy the key somewhere safe for the next section. You pass it to the setup component once.

The tunnel stack does not use the key at runtime. Revoke the key as soon as setup completes, and create a fresh one later when you rotate the tunnel token.

## Deploy the tunnel stack

Choose Helm if you run Kubernetes. The chart provisions the tunnel, stores the credentials in a Secret, and renews the server certificate automatically. Choose Docker Compose for a single host or a VM, where you run the setup component and certificate renewal yourself.

Both paths need at least one route. A route maps a subdomain of your tunnel domain to the internal URL of an MCP server, in the form `scheme://host:port` with no path. The examples use `docs` pointing at `http://docs-mcp.example.corp:8080`. Replace them with your own servers.

<Tabs>
  <Tab title="Helm">
    <Steps>
      <Step title="Fetch the default values">
        ```bash theme={null}
        helm show values \
          oci://us-docker.pkg.dev/anthropic-public-registry/charts/mcp-tunnel \
          --version 2.0.2 > values.yaml
        ```

        The file includes comments explaining each field.
      </Step>

      <Step title="Configure routes">
        Edit `values.yaml` and add a `routes` entry under `gateway.config` for each MCP server. Leave `tunnel.id` empty so the setup component creates the tunnel during install.

        ```yaml values.yaml theme={null}
        tunnel:
          id: ""
          # Increment to rotate the tunnel token on a later upgrade.
          tokenVersion: "1"

        gateway:
          config:
            routes:
              docs: http://docs-mcp.example.corp:8080
              search: http://10.0.12.7:9000
        ```

        With these routes, Claude reaches the servers at `docs.<your-tunnel-domain>` and `search.<your-tunnel-domain>`. If a route targets an address outside the RFC 1918 private ranges (some managed Kubernetes distributions allocate Service IPs elsewhere), add the range under `gateway.config.upstream.allowed_ips` as described in [Troubleshooting](/docs/connectors/mcp-tunnels/troubleshooting#proxy-logs-ip-validation-failed).
      </Step>

      <Step title="Review the rendered manifests">
        Render the chart with a placeholder key and review the output according to your organization's practices for third-party manifests. Rendering makes no API calls.

        ```bash theme={null}
        helm template mcp-tunnel \
          oci://us-docker.pkg.dev/anthropic-public-registry/charts/mcp-tunnel \
          --version 2.0.2 \
          -n mcp-tunnel \
          -f values.yaml \
          --set api.token=placeholder > rendered.yaml
        ```
      </Step>

      <Step title="Install">
        Read the Tunnels API key into an environment variable so it stays out of your shell history and values file, then install into a dedicated namespace.

        ```bash theme={null}
        # Paste the Tunnels API key (input is hidden)
        read -rs API_TOKEN && export API_TOKEN

        helm install mcp-tunnel \
          oci://us-docker.pkg.dev/anthropic-public-registry/charts/mcp-tunnel \
          --version 2.0.2 \
          --namespace mcp-tunnel --create-namespace \
          -f values.yaml \
          --set api.token="$API_TOKEN"
        ```

        The setup component runs as a pre-install hook, so `helm install` blocks until the tunnel is created, the CA is registered, and the credentials are stored in the `mcp-tunnel` Secret. If the install fails with a hook error, see [Troubleshooting](/docs/connectors/mcp-tunnels/troubleshooting#helm-install-fails-with-a-hook-error).

        <Warning>
          Revoke the Tunnels API key in **Organization settings > Tunnels > Tunnels API** as soon as the install completes. Helm records `--set` values in its release history Secrets, and Kubernetes Secrets are not encrypted at rest by default, so the key remains recoverable from the cluster until you revoke it.
        </Warning>
      </Step>

      <Step title="Read the tunnel domain">
        You need the tunnel domain to add connectors later.

        ```bash theme={null}
        kubectl -n mcp-tunnel get secret mcp-tunnel \
          -o jsonpath='{.data.tunnel-domain}' | base64 -d
        ```

        The value looks like `abc123.tunnel.anthropic.com`.
      </Step>
    </Steps>

    To restrict the pod's egress at the network level, set `networkPolicy.enabled: true` in `values.yaml` and list your MCP servers under `networkPolicy.mcpServers`. The policy already allows cloudflared to reach the tunnel edge. Your cluster's network plugin must support NetworkPolicy.

    For later configuration changes such as routes or replica count, edit `values.yaml` and run `helm upgrade` with the same `--version` and `-f values.yaml`, without the API key. Keep a complete `values.yaml` rather than relying on `--reuse-values`, because Helm's deep merge can silently keep a route you deleted.
  </Tab>

  <Tab title="Docker Compose">
    <Steps>
      <Step title="Prepare the deployment directory">
        ```bash theme={null}
        mkdir -p mcp-tunnel/{config,data}
        cd mcp-tunnel
        sudo chown 65532:65532 data
        ```

        The containers run as the non-root user ID `65532` and need write access to `data/`.
      </Step>

      <Step title="Write docker-compose.yaml">
        The compose file pins images by digest, runs every container as non-root with a read-only filesystem, drops all Linux capabilities, and disables privilege escalation.

        ```bash theme={null}
        cat > docker-compose.yaml <<'EOF'
        services:
          # One-time provisioning. Run with: docker compose run --rm setup
          setup:
            image: us-docker.pkg.dev/anthropic-public-registry/images/mcp-proxy@sha256:efb27b299d627e4134815663cb8896641eeaee025d734c0f695582b4df38f013
            entrypoint: ["/setup"]
            command:
              - init
              - --api-url=https://api.anthropic.com
              - --output=dir:/data
              - --token-version=1
            environment:
              - API_TOKEN
            volumes:
              - ./data:/data
            user: "65532:65532"
            read_only: true
            security_opt:
              - no-new-privileges:true
            cap_drop:
              - ALL
            profiles: ["setup"]

          cloudflared:
            image: cloudflare/cloudflared@sha256:6b599ca3e974349ead3286d178da61d291961182ec3fe9c505e1dd02c8ac31b0
            command: tunnel --no-autoupdate run --url http://localhost:8080
            environment:
              - TUNNEL_TOKEN
            # Share the proxy's network namespace so localhost:8080 reaches it.
            network_mode: "service:mcp-proxy"
            restart: unless-stopped
            user: "65532:65532"
            read_only: true
            security_opt:
              - no-new-privileges:true
            cap_drop:
              - ALL
            stop_grace_period: 30s
            logging:
              options:
                max-size: "10m"
                max-file: "3"

          mcp-proxy:
            image: us-docker.pkg.dev/anthropic-public-registry/images/mcp-proxy@sha256:efb27b299d627e4134815663cb8896641eeaee025d734c0f695582b4df38f013
            volumes:
              - ./config/mcp-proxy.yaml:/etc/mcp-gateway/config.yaml:ro
              - ./data:/data:ro
            restart: unless-stopped
            user: "65532:65532"
            read_only: true
            security_opt:
              - no-new-privileges:true
            cap_drop:
              - ALL
            # Match shutdown_timeout in the proxy config
            stop_grace_period: 30s
            logging:
              options:
                max-size: "10m"
                max-file: "3"
        EOF
        ```
      </Step>

      <Step title="Provision the tunnel">
        Read the Tunnels API key into an environment variable, then run the setup component. It creates the tunnel, generates the CA and server certificate, registers the CA with Anthropic, fetches the tunnel token, and writes everything to `data/`.

        ```bash theme={null}
        # Paste the Tunnels API key (input is hidden)
        read -rs API_TOKEN && export API_TOKEN

        docker compose run --rm setup
        ```

        Read the tunnel domain and keep it for later steps.

        ```bash theme={null}
        export TUNNEL_DOMAIN=$(sudo cat data/tunnel-domain)
        echo "$TUNNEL_DOMAIN"
        ```

        <Warning>
          Revoke the Tunnels API key in **Organization settings > Tunnels > Tunnels API** before continuing, and run `unset API_TOKEN`. The stack does not need the key at runtime.
        </Warning>
      </Step>

      <Step title="Write the proxy config">
        `tunnel_domain` is required so the proxy can strip the domain from incoming hostnames and look up the remaining subdomain in `routes`. `routes` is a map, not a list.

        ```bash theme={null}
        cat > config/mcp-proxy.yaml <<EOF
        listen_addr: ":8080"
        log_level: info
        shutdown_timeout: 30s
        tunnel_domain: ${TUNNEL_DOMAIN}
        tls:
          cert_file: /data/tls.crt
          key_file: /data/tls.key
        routes:
          docs: http://docs-mcp.example.corp:8080
          search: http://10.0.12.7:9000
        upstream:
          allowed_ips:
            - 10.0.0.0/8
        EOF
        ```

        `upstream.allowed_ips` is the proxy's protection against server-side request forgery. Use the narrowest ranges that cover your MCP servers. Setting it replaces the RFC 1918 default rather than extending it.
      </Step>

      <Step title="Start the stack">
        ```bash theme={null}
        export TUNNEL_TOKEN=$(sudo cat data/tunnel-token)
        docker compose up -d
        ```

        The compose file reads `TUNNEL_TOKEN` from the host environment with no default, so repeat the export in every fresh shell and after a reboot. For a multi-host deployment, copy the `mcp-tunnel/` directory to each host and start it the same way. The same tunnel token and certificates work across all replicas.
      </Step>
    </Steps>

    The `data/` directory now holds the tunnel ID, tunnel domain, tunnel token, CA key pair, and server key pair. Protect it with your organization's file-permission, encryption-at-rest, and secrets-management controls, and consider moving `ca.key` and `tunnel-token` to secure storage.
  </Tab>
</Tabs>

## Verify the connection

Check the logs on your side first. cloudflared logs four `Registered tunnel connection` lines when it has reached the tunnel edge, and the proxy logs one `route configured` line per route.

<CodeGroup>
  ```bash Helm theme={null}
  kubectl -n mcp-tunnel logs deploy/mcp-tunnel -c cloudflared | grep "Registered tunnel connection"
  kubectl -n mcp-tunnel logs deploy/mcp-tunnel -c mcp-proxy | grep "route configured"
  ```

  ```bash Docker Compose theme={null}
  docker compose logs cloudflared | grep "Registered tunnel connection"
  docker compose logs mcp-proxy | grep "route configured"
  ```
</CodeGroup>

The containers take a few seconds to start, so rerun the commands if they come back empty. If cloudflared never registers, see [Troubleshooting](/docs/connectors/mcp-tunnels/troubleshooting#the-tunnel-stack-starts-but-cloudflared-never-connects). The end-to-end check happens from Claude, in the next section.

## Add tunneled servers as connectors

Each route becomes a custom connector for your organization. The connector URL is the route's tunnel hostname plus the path your MCP server serves. Many servers serve at `/mcp`, and the proxy forwards the path unchanged.

1. In claude.ai, go to **Organization settings > Connectors**.
2. Select **Add**, then **Custom**. If Claude asks for the connector type, choose **Web**.
3. Enter the server URL, for example `https://docs.abc123.tunnel.anthropic.com/mcp`.
4. Configure authentication for the server. If its OAuth authorization server is also inside your network, turn on **Tunnel OAuth configuration** and follow [Authenticate to MCP servers behind a tunnel](/docs/connectors/mcp-tunnels/oauth).
5. Select **Add**.

Members then find the connector in their own connector settings and select **Connect** to sign in, as described in [Third party connectors with remote MCP](/docs/connectors/custom/remote-mcp#adding-custom-connectors). To confirm the tunnel end to end, connect the server yourself and ask Claude to use one of its tools while you watch the proxy logs for the request.

### Add more servers later

Add a route for the new server, apply the change, and register the new hostname as another custom connector. No certificate or cloudflared changes are needed, because the server certificate covers every subdomain of your tunnel domain.

<CodeGroup>
  ```bash Helm theme={null}
  # After adding the route under gateway.config.routes in values.yaml
  helm upgrade mcp-tunnel \
    oci://us-docker.pkg.dev/anthropic-public-registry/charts/mcp-tunnel \
    --version 2.0.2 \
    -n mcp-tunnel \
    -f values.yaml
  ```

  ```bash Docker Compose theme={null}
  # After adding the route in config/mcp-proxy.yaml
  docker compose restart mcp-proxy
  ```
</CodeGroup>

## Rotate credentials

Three credentials are involved, and each rotates differently.

**Tunnels API key.** Used only while the setup component runs. Revoke it after every use and create a new one in **Organization settings > Tunnels > Tunnels API** when you next need to run setup.

**Tunnel token.** Authenticates cloudflared's outbound connection. Rotate it on your regular schedule and immediately if you suspect exposure. Rotation does not sever connections that are already established, so you can rotate, restart cloudflared with the new value, and let the old connections drain.

<Tabs>
  <Tab title="Helm">
    Increment `tunnel.tokenVersion` in `values.yaml`, create a fresh Tunnels API key, and upgrade. The setup component re-runs, rotates the token, and updates the Secret.

    ```bash theme={null}
    read -rs API_TOKEN && export API_TOKEN

    helm upgrade mcp-tunnel \
      oci://us-docker.pkg.dev/anthropic-public-registry/charts/mcp-tunnel \
      --version 2.0.2 \
      -n mcp-tunnel \
      -f values.yaml \
      --set api.token="$API_TOKEN" \
      --set setup.force=true
    ```

    Revoke the API key once the upgrade completes.
  </Tab>

  <Tab title="Docker Compose">
    Edit `docker-compose.yaml` and increment the `--token-version` value in the `setup` service (for example from `1` to `2`), so the new value persists for future runs. Then create a fresh Tunnels API key and re-run setup.

    ```bash theme={null}
    read -rs API_TOKEN && export API_TOKEN
    docker compose run --rm setup

    export TUNNEL_TOKEN=$(sudo cat data/tunnel-token)
    docker compose up -d cloudflared
    ```

    Revoke the API key and run `unset API_TOKEN` once rotation completes. For a multi-host deployment, setup writes the new token only to the `data/` directory on the host where it ran, so copy the updated `data/` directory (at minimum `data/tunnel-token`) to every other host that runs a replica. Then repeat the last two commands on each of those hosts so every replica restarts with the new token.
  </Tab>
</Tabs>

**Server certificate.** The certificate the proxy presents is valid for 90 days, and you are responsible for renewing it before it expires. Renewal is local. It signs a new certificate with the CA already stored in your deployment, makes no API calls, and needs no API key. The proxy reloads the certificate file automatically, so no restart is required.

<Tabs>
  <Tab title="Helm">
    The chart deploys a CronJob that runs daily and renews the certificate once it is within 30 days of expiry. Monitor the CronJob and the certificate's expiry date to confirm renewal completes.
  </Tab>

  <Tab title="Docker Compose">
    Run the renewal from the deployment directory. With `--renew-before=720h` the command does nothing while more than 30 days of validity remain, so it is safe to run on a schedule such as a daily cron entry.

    ```bash theme={null}
    docker compose run --rm setup renew-cert --output=dir:/data --renew-before=720h
    ```
  </Tab>
</Tabs>

## Remove a tunnel

Decommission a tunnel when you no longer need it, or as the first steps of responding to a suspected compromise. Archiving a tunnel invalidates its token, detaches its domain, and is permanent.

<Steps>
  <Step title="Record the tunnel ID">
    <CodeGroup>
      ```bash Helm theme={null}
      TUNNEL_ID=$(kubectl -n mcp-tunnel get secret mcp-tunnel \
        -o jsonpath='{.data.tunnel-id}' | base64 -d)
      ```

      ```bash Docker Compose theme={null}
      TUNNEL_ID=$(sudo cat data/tunnel-id)
      ```
    </CodeGroup>
  </Step>

  <Step title="Stop the tunnel stack">
    <CodeGroup>
      ```bash Helm theme={null}
      helm uninstall mcp-tunnel -n mcp-tunnel
      ```

      ```bash Docker Compose theme={null}
      docker compose down
      ```
    </CodeGroup>

    If you are responding to a suspected compromise, use `docker compose down --timeout 0` to sever the connection immediately.
  </Step>

  <Step title="Remove the connectors">
    In **Organization settings > Connectors**, remove each custom connector that points at the tunnel's hostnames.
  </Step>

  <Step title="Archive the tunnel">
    Create a fresh Tunnels API key and call the [archive endpoint](https://platform.claude.com/docs/en/api/beta/tunnels/archive) of the Tunnels API. Revoke the key when you are done.

    ```bash theme={null}
    read -rs API_TOKEN && export API_TOKEN

    curl -X POST "https://api.anthropic.com/v1/tunnels/${TUNNEL_ID}/archive" \
      -H "Authorization: Bearer $API_TOKEN" \
      -H "anthropic-version: 2023-06-01" \
      -H "anthropic-beta: mcp-tunnels-2026-06-22"
    ```
  </Step>

  <Step title="Delete the stored credentials">
    <CodeGroup>
      ```bash Helm theme={null}
      # The setup component created this Secret, so helm uninstall leaves it behind
      kubectl -n mcp-tunnel delete secret mcp-tunnel
      ```

      ```bash Docker Compose theme={null}
      sudo rm -rf data
      ```
    </CodeGroup>
  </Step>
</Steps>

If you archived the tunnel because of a suspected compromise, also notify your Anthropic account team, rotate any OAuth tokens or secrets your MCP servers issued, and review the proxy, cloudflared, and MCP server logs for the affected period before you provision a replacement tunnel.
