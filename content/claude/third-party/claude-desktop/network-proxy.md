> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Network proxy

> How Claude Desktop on 3P and the Claude Code engine it runs use your network proxy: the default behavior, pinning a proxy from managed configuration, what is and is not routed through it, and how to troubleshoot.

Claude Desktop on 3P works behind a corporate HTTP proxy without extra configuration in most environments. This page explains which proxy each part of the product uses, how to pin a specific proxy from managed configuration, which traffic does not go through the proxy at all, and how a separately deployed Claude Code policy interacts with it.

Three parts of the product make network connections, and they do not all resolve the proxy the same way:

* **The app**: the Claude Desktop window itself, including sign-in, the connection test, Web Fetch in Chat and Cowork sessions, managed MCP servers the app connects to, and plugin marketplace sync.
* **The agent**: the Claude Code engine the app runs for every Chat, Cowork, and Code session. It sends inference requests and, in Code sessions, also makes its own web fetches, remote MCP connections, and plugin installs.
* **Cowork's sandboxed shell**: the isolated environment where commands the agent runs in a Cowork session (`curl`, `pip`, `npm`, and so on) execute.

## Default behavior

With no proxy-related configuration, the app follows the operating system's proxy settings, including a PAC (proxy auto-configuration) script or automatic proxy detection if the OS is set up that way. PAC rules are evaluated per request, so different hosts can go to different proxies or connect directly, exactly as the script says.

The agent does not read the OS settings itself. When a session starts, the app asks the OS which proxy applies to your inference endpoint (your gateway URL, or the provider endpoint for Google Cloud's Agent Platform, Amazon Bedrock, and Microsoft Foundry) and hands that one proxy to the agent as `HTTPS_PROXY` and `HTTP_PROXY`, with `NO_PROXY` set to `localhost,127.0.0.1,::1,.local`. The agent then uses that proxy for all of its own traffic. If the OS answer for the inference endpoint is a direct connection, the agent gets no proxy variables and connects directly.

On macOS and Windows, Cowork's sandboxed shell also follows the OS proxy settings, including a PAC script, which the sandbox evaluates per request itself. On Linux, no proxy settings reach the sandboxed shell and its commands connect directly.

A few limits apply to the agent regardless of how the proxy is chosen:

* Only `http://` and `https://` proxies are handed to the agent. If the OS or PAC answer is a SOCKS proxy, the app skips it and the agent connects directly.
* There is no interactive proxy sign-in. If your proxy requires a username and password, neither the app nor the agent can prompt for them and requests fail. Run a local forwarding proxy that authenticates upstream on the device (for example, Cntlm or Px) and point the OS or the pinned key at it.
* If your proxy intercepts TLS, see [TLS-intercepting proxies](#tls-intercepting-proxies) below.

## Pin a proxy from managed configuration

<Note>
  Pinning requires Claude Desktop 1.44121.1 or later. Earlier releases ignore the `egressProxyUrl` and `egressProxyPacUrl` keys and keep following the OS proxy settings.
</Note>

If you want the app, the agent, and (on macOS and Windows) Cowork's sandboxed shell to use a specific proxy regardless of what the device's OS settings say, set one of two managed configuration keys:

| Key                 | Value                                                                                           | Effect                                                                                                                                                                                                                                                                                                        |
| ------------------- | ----------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `egressProxyUrl`    | An `http://` or `https://` proxy URL, for example `http://proxy.example.com:8080`               | The app sends its traffic through this proxy, and the agent receives it as `HTTPS_PROXY` and `HTTP_PROXY` in every session on the device. On macOS and Windows, commands in Cowork's sandboxed shell receive the same variables. Loopback and `.local` hosts still connect directly.                          |
| `egressProxyPacUrl` | An `http://` or `https://` URL to a PAC script, for example `http://wpad.example.com/proxy.pac` | The app evaluates the script per request. The agent receives the single proxy the script returns for your inference endpoint. On macOS and Windows, Cowork's sandboxed shell is handed a copy of the script when the sandbox starts and evaluates it per request itself. If both keys are set, this one wins. |

Both keys are read once at launch; a change takes effect the next time the app starts. While either key is set, the OS proxy settings are ignored for the app, the agent, and (on macOS and Windows) Cowork's sandboxed shell; with neither key set, the sandboxed shell keeps following the OS settings as described under [Default behavior](#default-behavior). SOCKS URLs and URLs with embedded credentials (`user:password@`) are rejected.

If you point the key at a local forwarding proxy on the device, give it as `http://127.0.0.1:<port>`. Cowork's sandboxed shell reaches the device's loopback address through a host alias, so an `https://` loopback proxy cannot pass TLS verification from inside the sandbox and the shell's commands fail to connect; the app logs a warning at sandbox start when it sees that combination.

These keys are read from an MDM profile, registry policy, or local configuration file only; they are ignored if returned from a bootstrap server. They also follow the same precedence rule as the update keys: when an MDM profile or registry policy sets any key in that group, values for these keys in a local configuration file are ignored. See [Update keys and managed precedence](/docs/third-party/claude-desktop/mdm#update-keys-and-managed-precedence).

On Linux, or wherever you deploy the local configuration file, the key sits alongside your other settings:

```json /etc/claude-desktop/managed-settings.json theme={null}
{
  "egressProxyUrl": "http://proxy.example.com:8080"
}
```

In a macOS configuration profile the same key is a `<key>egressProxyUrl</key><string>http://proxy.example.com:8080</string>` pair in the `com.anthropic.claudefordesktop` payload, and on Windows it is a `REG_SZ` value named `egressProxyUrl` under `HKLM\SOFTWARE\Policies\Claude`. See [Value types](/docs/third-party/claude-desktop/configuration#value-types) and [Deploy with MDM](/docs/third-party/claude-desktop/mdm) for the surrounding profile and registry structure.

Three behaviors to plan for:

* If the pinned proxy is unreachable, requests fail. The app does not fall back to a direct connection.
* If a pinned PAC script cannot be downloaded, the app connects directly and the agent gets no proxy. Cowork's sandboxed shell gets its own copy of the script through a separate download when the sandbox starts; if that download fails, the shell connects directly too. Combine the key with network-layer egress rules if a silent fallback to direct is not acceptable (see the warning below).
* Inside Cowork's sandboxed shell, a pinned PAC script's `myIpAddress()` returns the sandbox's internal address rather than the device's, so a script that chooses a proxy by client subnet gives the shell its off-network answer.

## What is and is not routed

The table summarizes which proxy source each kind of traffic follows. "App proxy" means the pinned key if one is set, otherwise the OS settings, with PAC rules applied per request.

| Traffic                                                                                    | Proxy it follows                                                                                                                  |
| ------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------- |
| App window, in-app sign-in, connection test, model list                                    | App proxy                                                                                                                         |
| Inference requests from Chat, Cowork, and Code sessions                                    | The single proxy resolved for the inference endpoint (from the pinned key or the OS), or Claude Code managed settings if deployed |
| Agent web fetch, remote MCP servers, and plugin installs in Code sessions                  | Same single proxy as inference                                                                                                    |
| Web Fetch and managed MCP servers in Chat and Cowork sessions                              | App proxy (the app makes these connections)                                                                                       |
| Plugin marketplace sync and `aws` CLI calls the app makes for Bedrock sign-in              | App proxy, resolved for the specific host                                                                                         |
| Cowork sandbox download from `downloads.claude.ai`                                         | App proxy                                                                                                                         |
| Telemetry and crash reports to Anthropic, if enabled                                       | App proxy                                                                                                                         |
| OpenTelemetry export to your collector                                                     | App proxy for the app's own events; the same single proxy as inference for Claude Code metrics and logs                           |
| Commands in Cowork's sandboxed shell on macOS and Windows                                  | The pinned key if one is set (a pinned PAC script is evaluated per request inside the sandbox), otherwise the OS proxy settings   |
| Commands in Cowork's sandboxed shell on Linux                                              | None; commands connect directly                                                                                                   |
| The agent in an [SSH remote Code session](/docs/third-party/claude-desktop/ssh-remote-sessions) | None from the device; the remote host's own network route applies                                                                 |
| App update check and download                                                              | OS proxy settings only                                                                                                            |
| Credential helper and header helper scripts you configure                                  | None injected; the script's own environment applies                                                                               |
| Brokered Microsoft Entra sign-in (Company Portal on macOS, Web Account Manager on Windows) | The OS broker's own settings                                                                                                      |
| Pages opened in the system browser                                                         | The browser's own settings                                                                                                        |

## Traffic that bypasses the app proxy

Some traffic never uses the pinned key or the proxy the app resolved, and it is worth being explicit about each case and what you can do about it.

* **App updates.** Checking for and downloading Claude Desktop updates is handled by the OS-native updater on macOS and Windows, which follows the OS proxy settings only. This is the one app-controlled path with no admin-side option other than the OS proxy: neither the pinned key nor Claude Code managed settings reach it. If updates must not traverse a direct path, configure the OS proxy on the device or distribute updates yourself with [`disableAutoUpdates`](/docs/third-party/claude-desktop/configuration) and your software-distribution tool. On Linux, updates come from your package manager, which has its own proxy configuration.
* **Commands in Cowork's sandboxed shell on Linux.** No proxy settings reach the Cowork sandbox on Linux, so `curl`, `pip`, `npm`, `git`, and anything else the agent runs there connect directly. On macOS and Windows those commands follow the pinned key, or the OS proxy settings when no key is set, and are not a bypass. On every platform, [`coworkEgressAllowedHosts`](/docs/third-party/claude-desktop/web-tools) still applies inside the sandbox and sits in front of any proxy: a host must be on the allowlist to be reachable at all, and an allowed host is then reached through the proxy.
* **SSH remote Code sessions.** When a user runs a Code session on another machine through [`sshHostAllowlist`](/docs/third-party/claude-desktop/ssh-remote-sessions), the agent runs on that host and connects to the inference endpoint from there. Claude Desktop passes the endpoint address to the remote agent but not the pinned key, the device's OS proxy settings, or proxy variables from Claude Code managed settings on the device. The host's own network route and any Claude Code managed settings installed on the host apply instead. See [Inference credentials on the remote host](/docs/third-party/claude-desktop/ssh-remote-sessions#inference-credentials-on-the-remote-host).
* **Pages opened in the system browser.** Some sign-in flows open your default browser. That traffic follows the browser's proxy settings, which normally track the OS; pin it with the browser's own policy (for example, the Chrome or Edge `ProxySettings` policy) or the device's network profile.
* **Brokered Microsoft Entra sign-in.** When [brokered authentication](/docs/third-party/claude-desktop/entra-broker) is in use, the token request is made by Company Portal (macOS) or Web Account Manager (Windows), not by the app. Those components follow the OS proxy settings; configure them through the same MDM that manages the device.
* **Helper scripts.** An `inferenceCredentialHelper` or MCP `headersHelper` script runs with the app's environment and no injected proxy variables, because helpers typically talk to internal vaults or identity providers that should not go through the inference proxy. If a helper needs a proxy, set it inside the script.
* **Programs that ignore proxy variables.** The agent passes `HTTPS_PROXY`, `HTTP_PROXY`, and `NO_PROXY` to the programs it launches on the device, but a program that does not honor those variables connects directly if the network allows it. The only complete control for this case is blocking direct egress at the network layer.

<Warning>
  A proxy setting is routing, not enforcement. Nothing on this page prevents a process on the device from connecting directly if the network permits it. If you need a guarantee that traffic leaves only through your proxy, block direct egress at the firewall or secure web gateway and allow only the proxy. The inverse also holds: on an open network, a misconfigured or unreachable PAC script can quietly result in direct connections.
</Warning>

### The agent uses one proxy

The agent sends all of its own traffic (inference, and in Code sessions its web fetches, remote MCP connections, and plugin installs) through the one proxy resolved for your inference endpoint. Per-host PAC rules are not re-evaluated inside the agent. For most organizations this is the desirable outcome: everything the agent does is logged and inspected at one place, with nothing further to configure.

It needs attention only when that one proxy is not right for everything the agent reaches: typically some hosts (an internal MCP server, a private package registry, a self-hosted plugin marketplace) must be reached directly while the proxy only carries public traffic, or the reverse. In order of preference:

1. Let the proxy these devices use carry both kinds of traffic. Nothing else needs configuring.
2. Otherwise, list the domains that must connect directly in `NO_PROXY` through Claude Code managed settings (see the next section), using leading-dot suffixes such as `.example.corp`, and accept that everything not listed goes to the proxy.

The inverse edge case: if your PAC script returns `DIRECT` for the inference endpoint (common when the gateway is on your internal network), the agent gets no proxy at all, even for hosts the script would proxy. If the agent's other traffic must go through a proxy in that layout, set `HTTPS_PROXY` and a `NO_PROXY` entry for the gateway's domain through Claude Code managed settings.

## Interaction with Claude Code managed settings

<Note>
  The precedence described here requires Claude Desktop 1.44121.1 or later, the same release as the pinned-proxy keys above.
</Note>

If you deploy Claude Code [managed settings](https://code.claude.com/docs/en/settings#settings-files) on the device (a `managed-settings.json` file or an OS-level Claude Code policy) and its `env` block sets `HTTPS_PROXY`, `HTTP_PROXY`, or `NO_PROXY`, those values apply to the agent in Chat, Cowork, and Code sessions alike and take precedence over what the app would have supplied. Precedence is per variable: a managed `HTTPS_PROXY` replaces the app's proxy while the app's loopback `NO_PROXY` entries stay in place, and a managed `NO_PROXY` replaces the app's list (the loopback entries are appended for you when the app is also supplying the proxy). See Claude Code's [network configuration](https://code.claude.com/docs/en/network-config) page for the variables themselves.

```json managed-settings.json theme={null}
{
  "env": {
    "HTTPS_PROXY": "http://proxy.example.com:8080",
    "NO_PROXY": "localhost,127.0.0.1,::1,.example.corp"
  },
  "parentSettingsBehavior": "merge"
}
```

Set `parentSettingsBehavior` to `"merge"` whenever you deploy a Claude Code managed-settings file alongside Claude Desktop on 3P: without it, the presence of that file makes Claude Code ignore the policy Claude Desktop supplies (network and filesystem sandbox, allowed MCP servers), even if the file only sets proxy variables. [Claude Code in Claude Desktop on 3P](/docs/third-party/claude-desktop/code#interaction-with-claude-code%E2%80%99s-own-managed-settings) explains the merge behavior.

`NO_PROXY` matching in the agent follows these rules:

* A bare hostname matches that host exactly. To cover a domain and its subdomains, use a leading dot: `.example.corp` matches `example.corp` and `api.example.corp`.
* IP addresses match literally. CIDR ranges such as `10.0.0.0/8` are not supported.
* `host:port` entries match that host on that port only.
* `*` disables the proxy entirely, and only when it is the whole value; it is not a wildcard inside a list.

These settings reach the agent process only. The app itself and Cowork's sandboxed shell keep the proxy behavior described above, and the other paths listed under [Traffic that bypasses the app proxy](#traffic-that-bypasses-the-app-proxy) are likewise unaffected by Claude Code managed settings.

## TLS-intercepting proxies

If your proxy performs TLS interception, it presents its own certificate authority. The app trusts the operating system's certificate store. On macOS, the app also configures the agent to trust the System keychain in addition to the bundled CA roots, so a corporate CA installed there normally works without extra setup.

If inference or tool requests still fail certificate verification, the CA was likely added with policy-restricted trust: certificates installed via `security add-trusted-cert -p ssl …` are trusted by Safari and Chrome but are not picked up by the agent's keychain reader. Re-add the CA with full root trust (omit `-p`):

```bash theme={null}
sudo security add-trusted-cert -d -r trustRoot \
  -k /Library/Keychains/System.keychain /path/to/corp-ca.pem
```

If the certificate is MDM-managed and you cannot change how it is installed, set `NODE_EXTRA_CA_CERTS` as a fallback, then quit and relaunch Claude:

```bash theme={null}
security find-certificate -a -p /Library/Keychains/System.keychain > ~/corp-ca.pem
launchctl setenv NODE_EXTRA_CA_CERTS "$HOME/corp-ca.pem"
```

`launchctl setenv` makes the variable visible to apps launched from Finder or the Dock (shell-profile exports only reach terminal sessions). It applies until the next reboot; to make it permanent, run the command from a LaunchAgent at login.

## Troubleshoot

**"Can't reach" banner.** The app could not get a response from the inference host the banner names. Behind a proxy this usually means the proxy resolved for that host is unreachable, requires a sign-in the app cannot perform, or does not allow the host. Use **Copy report** on the banner to capture the details, confirm the device's OS proxy settings (or the pinned key) point at a reachable HTTP proxy, and confirm the proxy allows the inference host listed in [Required egress paths](/docs/third-party/claude-desktop/telemetry#required-egress-paths).

**Confirm which proxy is in effect.** Open `main.log` in the app's [logs directory](/docs/third-party/claude-desktop/data-storage). When a key is pinned, startup logs `[egress-proxy] pinned to fixed proxy at proxy.example.com:8080; OS proxy settings ignored` (or `pinned to PAC script at …`). When a session starts, the log records the proxy handed to the agent, for example `Resolved system proxy for Code sessions: http://proxy.example.com:8080`, and a `Skipping SOCKS proxy entry` line if the OS answer was SOCKS. If Claude Code managed settings supplied any proxy variable, a line names the variables it set or replaced and the settings file they came from. For Cowork's sandboxed shell, `cowork_vm_node.log` in the same directory records `[VM:start] guest egress pinned to fixed proxy at …` (or `PAC script at …`) when the sandbox starts with a key pinned, and `[VM:start] PAC fetch from … failed (…); guest connects directly` if the sandbox's copy of the script could not be downloaded.

**Agent connects directly while the app is proxied.** The OS or PAC answer for the inference endpoint was `DIRECT` or SOCKS-only. Adjust the PAC rule for the inference host, or pin `egressProxyUrl`.

**Web fetches or MCP connections fail in Code sessions but inference works.** Either the proxy resolved for the inference endpoint does not carry that traffic, or the answer for the inference endpoint was `DIRECT` and the agent has no proxy. See [The agent uses one proxy](#the-agent-uses-one-proxy).

**Certificate errors.** See [TLS-intercepting proxies](#tls-intercepting-proxies).

## Related

* [Configuration reference](/docs/third-party/claude-desktop/configuration) for `egressProxyUrl`, `egressProxyPacUrl`, and `coworkEgressAllowedHosts`
* [Telemetry and egress](/docs/third-party/claude-desktop/telemetry#required-egress-paths) for the hosts your proxy must allow
* [Claude Code in Claude Desktop on 3P](/docs/third-party/claude-desktop/code) for how Claude Code managed settings combine with Claude Desktop policy
* [Web tools](/docs/third-party/claude-desktop/web-tools) for `coworkEgressAllowedHosts`
