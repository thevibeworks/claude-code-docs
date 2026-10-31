> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Network proxy

> How Claude Desktop on 3P and the Claude Code engine it runs use your network proxy: the default behavior, pinning a proxy from managed configuration, what is and is not routed through it, and how to troubleshoot.

Claude Desktop on 3P works behind a corporate HTTP proxy without extra configuration in most environments.

Three parts of the product make network connections, and they do not all resolve the proxy the same way:

* **The app**: the Claude Desktop window itself, including sign-in, the connection test, Web Fetch in Chat and Cowork sessions, managed MCP servers the app connects to, and sync of the plugin marketplaces you configure.
* **The agent**: the Claude Code engine the app runs for every Chat, Cowork, and Code session. It sends inference requests and makes its own remote MCP connections, for example to [a server that a marketplace plugin or a user-added plugin bundles](https://claude.com/docs/third-party/claude-desktop/extensions.md#remote-mcp-servers-in-plugins). In Code sessions, it also makes its own web fetches and plugin installs.
* **Cowork's sandboxed shell**: the isolated environment where commands the agent runs in a Cowork session (`curl`, `pip`, `npm`, and so on) execute.

With [Unified Claude](https://claude.com/docs/third-party/claude-desktop/unified-claude.md) on, a Cowork session started from the home screen runs its commands in Cowork's sandboxed shell.

## Default behavior

With no proxy-related configuration, the app follows the operating system's proxy settings, including a PAC (proxy auto-configuration) script or automatic proxy detection if the OS is set up that way. PAC rules are evaluated per request, so different hosts can go to different proxies or connect directly, exactly as the script says.

The agent does not read the OS settings itself. When a session starts, the app asks the OS which proxy applies to your inference endpoint (your gateway URL, or the provider endpoint for Google Cloud's Agent Platform, Amazon Bedrock, and Microsoft Foundry) and hands that one proxy to the agent as `HTTPS_PROXY` and `HTTP_PROXY`, with `NO_PROXY` set to `localhost,127.0.0.1,::1,.local`. The agent then uses that proxy for all of its own traffic. If the OS answer for the inference endpoint is a direct connection, the agent gets no proxy variables and connects directly, unless the OS has named an `http://` or `https://` proxy for that endpoint since Claude Desktop started (see [Troubleshoot](#troubleshoot)).

On macOS and Windows, Cowork's sandboxed shell also follows the OS proxy settings, including a PAC script, which the sandbox evaluates per request itself. On Linux, no proxy settings reach the sandboxed shell and its commands connect directly.

A few limits apply to the agent regardless of how the proxy is chosen:

* Only `http://` and `https://` proxies are handed to the agent. If the OS or PAC answer is a SOCKS proxy, the app skips it, and the agent connects directly or through the last `http://` or `https://` proxy named for the inference endpoint since Claude Desktop started.
* There is no interactive proxy sign-in. If your proxy requires a username and password, neither the app nor the agent can prompt for them and requests fail. Run a local forwarding proxy that authenticates upstream on the device (for example, Cntlm or Px) and point the OS or the pinned key at it.
* If your proxy intercepts TLS, see [TLS-intercepting proxies](#tls-intercepting-proxies) below.

### PAC script for the sandboxed shell

On macOS and Windows, Cowork's sandboxed shell works from its own copy of the PAC script, which the app downloads from the address in the OS proxy settings when the sandbox starts. Without a copy, the shell's commands connect directly, or through a proxy server that the OS proxy settings also name.

* **PAC script address on macOS.** macOS refuses the download of the sandboxed shell's copy from a plain `http://` address such as `http://pac.example.com/proxy.pac`. The app and the agent are then still proxied as the script directs, and the sandboxed shell gets no copy. macOS accepts plain `http://` only when the host is a name with no dot in it, a `.local` name, a loopback address, or a private-network IPv4 address such as `10.0.0.5`. Serve the script over `https://`.
* **Failed downloads.** The download can fail when the sandbox starts, for example right after a VPN change. For the address in the OS proxy settings, the app retries for about a minute and then again when new commands start in the sandbox. When a retry succeeds, commands that start afterward use the script without an app restart. A failed download leaves in place a script the shell already has from the same address. A response that isn't a PAC script, such as a sign-in page, counts as a failed download.
* **Host names with no dot.** Inside the sandbox, a host name with no dot in it is looked up under the device's DNS search domains when the name alone doesn't resolve. One example is a proxy that the PAC script names as `proxy-server`. A name with a dot in it is looked up as written.
* **Rules that test the device's address.** Inside the sandbox, `myIpAddress()` returns the sandbox's internal address, not the device's, so a script that chooses a proxy by client subnet can give the shell a different answer than it gives the device.

## Pin a proxy from managed configuration

> [!NOTE]
>
> Pinning requires Claude Desktop 1.44121.1 or later. Earlier releases ignore the `egressProxyUrl` and `egressProxyPacUrl` keys and keep following the OS proxy settings.

If you want the app, the agent, and (on macOS and Windows) Cowork's sandboxed shell to use a specific proxy regardless of what the device's OS settings say, set one of two managed configuration keys:

| Key | Value | Effect |
| - | - | - |
| `egressProxyUrl` | An `http://` or `https://` proxy URL, for example `http://proxy.example.com:8080` | The app sends its traffic through this proxy, and the agent receives it as `HTTPS_PROXY` and `HTTP_PROXY` in every session on the device. On macOS and Windows, commands in Cowork's sandboxed shell receive the same variables. Loopback and `.local` hosts still connect directly. |
| `egressProxyPacUrl` | An `http://` or `https://` URL to a PAC script, for example `http://wpad.example.com/proxy.pac` | The app evaluates the script per request. The agent receives the single proxy the script returns for your inference endpoint. On macOS and Windows, Cowork's sandboxed shell is handed a copy of the script when the sandbox starts and evaluates it per request itself. If both keys are set, this one wins. |

Both keys are read once at launch; a change takes effect the next time the app starts. While either key is set, the OS proxy settings are ignored for the app, the agent, and (on macOS and Windows) Cowork's sandboxed shell. SOCKS URLs and URLs with embedded credentials (`user:password@`) are rejected.

If you point the key at a local forwarding proxy on the device, give it as `http://127.0.0.1:<port>`. An `https://` loopback proxy cannot pass TLS verification from inside Cowork's sandboxed shell, so the shell's commands fail to connect. The app logs a warning at sandbox start when it sees that combination.

These keys are read from an MDM profile, registry policy, or local configuration file only; they are ignored if returned from a bootstrap server. They also follow the same precedence rule as the update keys: when an MDM profile or registry policy sets any key in that group, values for these keys in a local configuration file are ignored. See [Update keys and managed precedence](https://claude.com/docs/third-party/claude-desktop/mdm.md#update-keys-and-managed-precedence).

On Linux, or wherever you deploy the local configuration file, the key sits alongside your other settings:

```json /etc/claude-desktop/managed-settings.json theme={null}
{
  "egressProxyUrl": "http://proxy.example.com:8080"
}
```

In a macOS configuration profile the same key is a `<key>egressProxyUrl</key><string>http://proxy.example.com:8080</string>` pair in the `com.anthropic.claudefordesktop` payload. On Windows it is a `REG_SZ` value named `egressProxyUrl` under `HKLM\SOFTWARE\Policies\Claude`, or under `HKCU\SOFTWARE\Policies\Claude` if the rest of your registry policy is there. The app [ignores `HKCU` policy when machine policy is present](https://claude.com/docs/third-party/claude-desktop/mdm#4-deploy-the-configuration). See [Value types](https://claude.com/docs/third-party/claude-desktop/configuration-format.md#value-types) and [Deploy with MDM](https://claude.com/docs/third-party/claude-desktop/mdm.md) for the surrounding profile and registry structure.

Three behaviors to plan for:

* If the pinned proxy is unreachable, requests fail. The app does not fall back to a direct connection.
* If a pinned PAC script cannot be downloaded, the app connects directly and the agent gets no proxy. Cowork's sandboxed shell gets its own copy of the script through a separate download when the sandbox starts. If that download fails or returns something other than a PAC script, such as a sign-in page, the shell connects directly. The download isn't tried again until the sandbox next starts, so quit and reopen Claude Desktop on the affected device once the script is reachable. Combine the key with network-layer egress rules if a silent fallback to direct is not acceptable (see the warning below).
* Inside Cowork's sandboxed shell, a pinned PAC script's `myIpAddress()` returns the sandbox's internal address rather than the device's, so a script that chooses a proxy by client subnet can give the shell a different answer than it gives the device.

## What is and is not routed

The table summarizes which proxy source each kind of traffic follows. "App proxy" means the pinned key if one is set, otherwise the OS settings, with PAC rules applied per request.

| Traffic | Proxy it follows |
| - | - |
| App window, in-app sign-in, connection test, model list | App proxy |
| Inference requests from Chat, Cowork, and Code sessions | The single proxy resolved for the inference endpoint (from the pinned key or the OS), or Claude Code managed settings if deployed |
| Agent web fetch, remote MCP servers, and plugin installs in Code sessions | Same single proxy as inference |
| The agent's remote MCP connections in Chat and Cowork sessions, to servers that a marketplace plugin or a user-added plugin bundles | Same single proxy as inference |
| Web Fetch and managed MCP servers in Chat and Cowork sessions | App proxy (the app makes these connections) |
| Sync of the plugin marketplaces you configure, and `aws` CLI calls the app makes for Bedrock sign-in | App proxy, resolved for the specific host |
| Cowork sandbox download from `downloads.claude.ai` | App proxy |
| Telemetry and crash reports to Anthropic, if enabled | App proxy |
| OpenTelemetry export to your collector | App proxy for the app's own events; the same single proxy as inference for Claude Code metrics and logs |
| Commands in Cowork's sandboxed shell on macOS and Windows | The pinned key if one is set (a pinned PAC script is evaluated per request inside the sandbox), otherwise the OS proxy settings |
| Commands in Cowork's sandboxed shell on Linux | None; commands connect directly |
| The agent in an [SSH remote Code session](https://claude.com/docs/third-party/claude-desktop/ssh-remote-sessions.md) | None from the device; the remote host's own network route applies |
| App update check and download | OS proxy settings only |
| Credential helper and header helper scripts you configure | None injected; the script's own environment applies |
| Brokered Microsoft Entra sign-in (Company Portal on macOS, Web Account Manager on Windows) | The OS broker's own settings |
| Pages opened in the system browser | The browser's own settings |

## Traffic that bypasses the app proxy

Some traffic never uses the pinned key or the proxy the app resolved.

* **App updates.** Checking for and downloading Claude Desktop updates is handled by the OS-native updater on macOS and Windows, which follows the OS proxy settings only. This is the one app-controlled path with no admin-side option other than the OS proxy: neither the pinned key nor Claude Code managed settings reach it. If updates must not traverse a direct path, configure the OS proxy on the device or distribute updates yourself with [`disableAutoUpdates`](https://claude.com/docs/third-party/claude-desktop/configuration) and your software-distribution tool. On Linux, updates come from your package manager, which has its own proxy configuration.
* **Commands in Cowork's sandboxed shell.** No proxy settings reach the Cowork sandbox on Linux, so `curl`, `pip`, `npm`, `git`, and anything else the agent runs there connect directly. On macOS and Windows those commands follow the pinned key, or the OS proxy settings when no key is set. When the key or the OS settings name a PAC script, the commands follow it only while the sandbox has [its copy of the script](#pac-script-for-the-sandboxed-shell). If the download of a pinned PAC script fails when the sandbox starts, the commands connect directly until the sandbox next starts. On every platform, [`coworkEgressAllowedHosts`](https://claude.com/docs/third-party/claude-desktop/web-tools) still applies inside the sandbox and sits in front of any proxy.
* **SOCKS proxies in Cowork's sandboxed shell.** On macOS and Windows, the sandboxed shell skips SOCKS proxies. Its commands connect directly to a host for which a PAC script returns only SOCKS proxies, and to every host when the OS proxy settings name only a SOCKS proxy. Have the script return a `PROXY` or `HTTPS` entry for each host that must go through a proxy, or [pin a proxy from managed configuration](#pin-a-proxy-from-managed-configuration).
* **Cowork's sandboxed shell when every host is allowed.** With a list of hosts in [`coworkEgressAllowedHosts`](https://claude.com/docs/third-party/claude-desktop/web-tools), the shell's commands reach the network only through a filter inside the sandbox, and a program that ignores proxy variables has no route around it. When the list contains `*`, that filter is off and commands make their own connections. On macOS and Windows they get the proxy setting only as `HTTPS_PROXY`, `HTTP_PROXY`, and `NO_PROXY`, so a program that ignores those variables connects directly.
* **SSH remote Code sessions.** When a user runs a Code session on another machine through [`sshHostAllowlist`](https://claude.com/docs/third-party/claude-desktop/ssh-remote-sessions), the agent runs on that host and connects to the inference endpoint from there. Claude Desktop passes the endpoint address to the remote agent but not the pinned key, the device's OS proxy settings, or proxy variables from Claude Code managed settings on the device. The host's own network route and any Claude Code managed settings installed on the host apply instead. See [Inference credentials on the remote host](https://claude.com/docs/third-party/claude-desktop/ssh-remote-sessions.md#inference-credentials-on-the-remote-host).
* **Pages opened in the system browser.** Some sign-in flows open your default browser. That traffic follows the browser's proxy settings, which normally track the OS; pin it with the browser's own policy (for example, the Chrome or Edge `ProxySettings` policy) or the device's network profile.
* **Brokered Microsoft Entra sign-in.** When [brokered authentication](https://claude.com/docs/third-party/claude-desktop/entra-broker.md) is in use, the token request is made by Company Portal (macOS) or Web Account Manager (Windows), not by the app. Those components follow the OS proxy settings; configure them through the same MDM that manages the device.
* **Helper scripts.** An `inferenceCredentialHelper` or MCP `headersHelper` script runs with the app's environment and no injected proxy variables. If a helper needs a proxy, set it inside the script.
* **Programs that ignore proxy variables.** The agent passes `HTTPS_PROXY`, `HTTP_PROXY`, and `NO_PROXY` to the programs it launches on the device, but a program that does not honor those variables connects directly if the network allows it. The only complete control for this case is blocking direct egress at the network layer.

> [!WARNING]
>
> A proxy setting is routing, not enforcement. Nothing on this page prevents a process on the device from connecting directly if the network permits it. If you need a guarantee that traffic leaves only through your proxy, block direct egress at the firewall or secure web gateway and allow only the proxy. The inverse also holds: on an open network, a misconfigured or unreachable PAC script can quietly result in direct connections.

### The agent uses one proxy

The agent sends all of its own traffic (inference, its remote MCP connections, and in Code sessions its web fetches and plugin installs) through the one proxy resolved for your inference endpoint. Per-host PAC rules are not re-evaluated inside the agent. For most organizations this is the desirable outcome: everything the agent does is logged and inspected at one place, with nothing further to configure.

It needs attention only when that one proxy is not right for everything the agent reaches: typically some hosts (an internal MCP server, a private package registry, a self-hosted plugin marketplace) must be reached directly while the proxy only carries public traffic, or the reverse. In order of preference:

1. Let the proxy these devices use carry both kinds of traffic. Nothing else needs configuring.
2. Otherwise, list the domains that must connect directly in `NO_PROXY` through Claude Code managed settings (see the next section), using leading-dot suffixes such as `.example.corp`, and accept that everything not listed goes to the proxy.

The inverse edge case: if your PAC script returns `DIRECT` for the inference endpoint (common when the gateway is on your internal network), the agent gets no proxy at all, even for hosts the script would proxy. If the agent's other traffic must go through a proxy in that layout, set `HTTPS_PROXY` and a `NO_PROXY` entry for the gateway's domain through Claude Code managed settings.

## Interaction with Claude Code managed settings

> [!NOTE]
>
> The precedence described here requires Claude Desktop 1.44121.1 or later, the same release as the pinned-proxy keys above.

In Claude Code [managed settings](https://code.claude.com/docs/en/settings#settings-files) on the device (a `managed-settings.json` file or an OS-level Claude Code policy), you can set `HTTPS_PROXY`, `HTTP_PROXY`, or `NO_PROXY` in the `env` block. Those values apply to the agent in Chat, Cowork, and Code sessions and take precedence over what the app would have supplied. Precedence is per variable:

* A managed `HTTPS_PROXY` replaces the app's proxy, and the app's loopback `NO_PROXY` entries stay in place.
* A managed `NO_PROXY` replaces the app's list. When the app is also supplying the proxy, the loopback entries are appended.

See Claude Code's [network configuration](https://code.claude.com/docs/en/network-config) page for the variables themselves.

```json managed-settings.json theme={null}
{
  "env": {
    "HTTPS_PROXY": "http://proxy.example.com:8080",
    "NO_PROXY": "localhost,127.0.0.1,::1,.example.corp"
  },
  "parentSettingsBehavior": "merge"
}
```

Set `parentSettingsBehavior` to `"merge"` whenever you deploy a Claude Code managed-settings file alongside Claude Desktop on 3P, even if the file only sets proxy variables. Without `"merge"`, that file makes Claude Code ignore Claude Desktop's policy (network and filesystem sandbox, allowed MCP servers), except in a Code session that gets [`code` settings from a Claude apps gateway](https://code.claude.com/docs/en/claude-apps-gateway-config#apply-code-settings-in-the-code-tab). [Claude Code in Claude Desktop on 3P](https://claude.com/docs/third-party/claude-desktop/code.md#interaction-with-claude-code%E2%80%99s-own-managed-settings) explains both cases and the merge behavior.

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

**"Can't reach" banner.** The app could not get a response from the inference host the banner names. Behind a proxy this usually means the proxy resolved for that host is unreachable, requires a sign-in the app cannot perform, or does not allow the host. Use **Copy report for IT** on the banner to capture the details, confirm the device's OS proxy settings (or the pinned key) point at a reachable HTTP proxy, and confirm the proxy allows the inference host listed in [Required egress paths](https://claude.com/docs/third-party/claude-desktop/telemetry.md#required-egress-paths).

**Confirm which proxy is in effect.** Open `main.log` in the app's [logs directory](https://claude.com/docs/third-party/claude-desktop/data-storage.md) and look for these lines:

* **Key pinned**: at startup, `[egress-proxy] pinned to fixed proxy at proxy.example.com:8080; OS proxy settings ignored` (or `pinned to PAC script at …`)
* **Proxy handed to the agent**: logged the first time and whenever it changes, for example `Resolved system proxy for Code sessions: http://proxy.example.com:8080`
* **Last proxy reused**: a `Keeping system proxy` line, when the OS answer was direct, SOCKS, or missing
* **SOCKS answer from the OS**: a `Skipping SOCKS proxy entry` line
* **Proxy variables from Claude Code managed settings**: a line that names the variables set or replaced, and the settings file they came from

For Cowork's sandboxed shell, open `cowork_vm_node.log` in the same directory and look for these lines:

* **Key pinned when the sandbox starts**: `[VM:start] guest egress pinned to fixed proxy at …` (or `PAC script at …`)
* **Sandbox's copy of the script not downloaded**: `[VM:start] PAC fetch from … failed (…); guest connects directly`

**Agent connects directly while the app is proxied.** The OS or PAC answer for the inference endpoint was `DIRECT` or SOCKS-only. Adjust the PAC rule for the inference host, or pin `egressProxyUrl`.

**New sessions keep using a proxy after the device leaves its network.** Once the app has been given a proxy for the inference endpoint, it keeps handing that proxy to new sessions while the OS or PAC answer is a direct connection, a SOCKS proxy, or no answer. Quit and reopen Claude Desktop.

**Cowork's sandboxed shell has no proxy on macOS while the app is proxied.** Check the PAC address in the OS proxy settings. The sandboxed shell uses its own copy of the PAC script. macOS refuses the download of that copy from a plain `http://` address unless the host is one of the exceptions listed under [PAC script for the sandboxed shell](#pac-script-for-the-sandboxed-shell). The app's logs then record `PAC fetch from … refused: macOS requires https for this address (App Transport Security)`, which you can search for in the [logs directory](https://claude.com/docs/third-party/claude-desktop/data-storage.md). Serve the script over `https://`.

**Web fetches or MCP connections fail in Code sessions but inference works.** Either the proxy resolved for the inference endpoint does not carry that traffic, or the answer for the inference endpoint was `DIRECT` and the agent has no proxy. See [The agent uses one proxy](#the-agent-uses-one-proxy).

**Certificate errors.** See [TLS-intercepting proxies](#tls-intercepting-proxies).

## Related

* [Configuration reference](https://claude.com/docs/third-party/claude-desktop/configuration.md) for `egressProxyUrl`, `egressProxyPacUrl`, and `coworkEgressAllowedHosts`
* [Telemetry and egress](https://claude.com/docs/third-party/claude-desktop/telemetry.md#required-egress-paths) for the hosts your proxy must allow
* [Claude Code in Claude Desktop on 3P](https://claude.com/docs/third-party/claude-desktop/code.md) for how Claude Code managed settings combine with Claude Desktop policy
* [Web tools](https://claude.com/docs/third-party/claude-desktop/web-tools.md) for `coworkEgressAllowedHosts`
