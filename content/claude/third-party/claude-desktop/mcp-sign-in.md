> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Set up sign-in for managed MCP servers

> Decide whether a managed MCP server needs an OAuth client that you register and whether it also needs that client's secret, fill in the OAuth fields, and read the sign-in error messages.

For a remote [managed MCP server](https://claude.com/docs/third-party/claude-desktop/extensions.md#managed-mcp-servers-admin) that uses OAuth, Claude Desktop signs each user in through the browser: the user clicks **Connect**, signs in to the server's identity provider (the OAuth service its vendor runs, for example Google or Box), and Claude Desktop stores the resulting token encrypted on the device. What you configure depends on that identity provider. Some register Claude Desktop as a client automatically, some require an OAuth client that you register, and some also require that client's secret.

This page is for administrators who add servers on the **Connectors** page of the [Enterprise Admin Console](https://claude.com/docs/third-party/claude-desktop/admin-console.md). The [in-app configuration window](https://claude.com/docs/third-party/claude-desktop/in-app-configuration.md) has the same fields, and in an MDM or bootstrap configuration they are the `oauth` keys of a [`managedMcpServers`](https://claude.com/docs/third-party/claude-desktop/configuration#managedmcpservers) entry. For the redirect URI, discovery, and token handling in detail, see [OAuth sign-in](https://claude.com/docs/third-party/claude-desktop/extensions.md#oauth-sign-in).

## Choose the OAuth setting

In the Enterprise Admin Console ([claude.ai](https://claude.ai) → **Organization settings**), open the **Connectors** page under **Desktop 3P**. Each remote entry under **Managed MCP servers** has an **OAuth** menu. Choose the setting that matches what the server's identity provider requires.

| If the identity provider | **OAuth** setting | What you register at the identity provider | Fields to fill in |
| - | - | - | - |
| Supports dynamic client registration | **Auto-register (dynamic client registration)** | Nothing. Claude Desktop registers itself as a client on each device when the user first clicks **Connect** | None |
| Requires an OAuth client that you register (no dynamic client registration) | **Bring your own client** | A public OAuth client (native or desktop application type) with redirect URI `http://127.0.0.1:53280/callback` and no secret | **Client ID** |
| Requires a registered client and rejects token requests that don't carry the client secret | **Bring your own client** | An OAuth client with redirect URI `http://127.0.0.1:53280/callback`, plus its client secret | **Client ID**, **Authorization server**, and the secret in **Client secret** or **Client secret helper script** |

Leave the **OAuth** menu set to **None** for a server that needs no sign-in or that authenticates with request headers. The menu also lists **Anthropic-hosted client identity (requires Claude.ai sign-in)**, which this page doesn't cover.

Choose **Bring your own client** when the identity provider's documentation has you create an OAuth app, client, or integration and copy its client ID. You also need the secret when that client comes with one and the identity provider offers no public or PKCE-only client type. Otherwise start with **Auto-register (dynamic client registration)**. Single-tenant Microsoft Entra apps and identity providers that publish no discovery document need the extra fields listed under [OAuth fields](#oauth-fields).

Test each server yourself before you announce it: sign in to Claude Desktop as a member of the organization and click **Connect**. The Enterprise Admin Console has no connection test for MCP servers. If the setting doesn't match the server, **Connect** fails as described under [Troubleshoot sign-in](#troubleshoot-sign-in).

## Where the client secret goes

Add a client secret only when the identity provider refuses sign-in without one. The console stores a value in **Client secret** only for a Google OAuth client of the **Desktop app** type: the value begins with `GOCSPX-`, **Authorization server** is exactly `["https://accounts.google.com"]`, and **Tenant ID** is empty. Google doesn't treat a Desktop-app client secret as confidential, so the console accepts it. A Google **Web application** client's secret has the same `GOCSPX-` prefix but is confidential, so always create a **Desktop app** client.

For every other identity provider the secret stays on the device. Install a script that prints the secret, at the same absolute path on every device, and enter that path in the **Client secret helper script** field. The script must print exactly one JSON object, `{"clientSecret": "…"}`, on stdout and exit with code `0` within 30 seconds. Claude Desktop runs it each time the server connects or refreshes its sign-in in the background. The console stores only the path, so distribute the script through your device management, as described under [When a helper script is the right choice](https://claude.com/docs/third-party/claude-desktop/admin-console.md#when-a-helper-script-is-the-right-choice), and see [Connect to Box](https://claude.com/docs/third-party/claude-desktop/connectors-box.md) for a minimal script. A configuration delivered by MDM or a bootstrap server can instead carry any identity provider's secret inline in `oauth.clientSecret`.

**Authorization server** is required whenever **Client secret** or **Client secret helper script** is set. Claude Desktop sends the secret only to the token endpoint of the issuer you name there, so a misconfigured or compromised MCP server can't redirect the token exchange, and the secret, to another server.

## OAuth fields

These fields appear when **OAuth** is set to **Bring your own client**. The [`managedMcpServers` reference](https://claude.com/docs/third-party/claude-desktop/configuration#managedmcpservers) lists every `oauth` key.

| Field | When to set | What to enter |
| - | - | - |
| **Client ID** | You registered a client at the identity provider | The client ID from that registration |
| **Client secret** | The identity provider requires the secret and the client is a Google Desktop-app client | The secret, beginning `GOCSPX-` |
| **Client secret helper script** | The identity provider requires the secret (any identity provider) | The absolute path of the script on the device. Set this or **Client secret**, not both; in a configuration file that sets both, the script wins |
| **Authorization server** | Required with a secret or secret helper script. Also required, as a single entry, with **Omit resource parameter** unless you set **Tenant ID** or **Authorization URL** and **Token URL**. Optional otherwise, to pin sign-in to a known issuer | A JSON array holding the authorization server's `issuer` value exactly as its metadata states it, for example `["https://accounts.google.com"]` (no trailing slash) or `["https://api.box.com"]` |
| **Authorization URL** and **Token URL** | The identity provider publishes no discovery document | Both HTTPS endpoints, always as a pair. Hidden when **Tenant ID** or **Authorization server** is set |
| **Tenant ID** | The client is a single-tenant Microsoft Entra app. For a GCC High or DoD tenant, leave **Tenant ID** empty and enter the tenant's issuer, `["https://login.microsoftonline.us/<tenant-id>/v2.0"]`, in **Authorization server** | Your Directory (tenant) ID. Requires **Scope** |
| **Scope** | Required with **Tenant ID** or **Omit resource parameter**. Optional otherwise | Space-separated scopes for the authorize request. Leave empty to request the scopes the server advertises |
| **Omit resource parameter** | Sign-in fails because the identity provider rejects the OAuth `resource` parameter, for example with Microsoft Entra error `AADSTS9010010` | Turn on the **Omit resource parameter** switch, and fill in the fields it requires as described under [Omit the resource parameter](#omit-the-resource-parameter) |
| **Sign-in flow** | Shown after you enter **Tenant ID**. Set it when your devices have the [OS identity broker](https://claude.com/docs/third-party/claude-desktop/entra-broker.md) | **OS identity broker (WAM / Company Portal)**. The default is **System browser** |
| **Callback host** and **Callback port** | The redirect URI you registered uses `localhost` or a port other than `53280` | The host and port from that registration. Microsoft Entra ID accepts any loopback port, so leave both empty for Entra |
| **Additional redirect referrer hosts** | The identity provider completes sign-in from a host other than the one in its authorization URL, and `main.log` names a rejected referrer host | That hostname. Separate several with spaces |

### Omit the resource parameter

Turn on the **Omit resource parameter** switch only if the identity provider rejects the OAuth [`resource` parameter](https://claude.com/docs/third-party/claude-desktop/extensions#how-oauth-sign-in-works) that Claude Desktop sends at sign-in, for example with Microsoft Entra error `AADSTS9010010`. Claude Desktop then sends no `resource` parameter for that server. Set **OAuth** to **Bring your own client** to see the switch. In an MDM or bootstrap configuration, set `oauth.omitResource` to `true`.

With Microsoft Entra ID, you can also fix `AADSTS9010010` by adding the URL that Claude Desktop sends to the API's Application ID URIs, unless that URL ends in a slash. Microsoft Entra ID doesn't accept such a URI. Claude Desktop sends the `resource` field of the server's [protected-resource metadata](https://claude.com/docs/third-party/claude-desktop/extensions.md#how-oauth-sign-in-works), and adds a trailing slash if the field is only an origin. Compare the two fixes:

* **Register the URL**: follow [Microsoft Entra ID rejects the resource value](https://claude.com/docs/connectors/building/troubleshooting.md#microsoft-entra-id-rejects-the-resource-value). You need permission to edit the API's app registration. For a URL on a domain that your tenant hasn't verified, such as a vendor's hostname, the steps move every app that uses the API to v2.0 tokens, unless you use an alternative listed there. Microsoft Entra ID still refuses a token if a requested API scope belongs to a different app registration.
* **Turn on the switch**: nothing changes in Microsoft Entra ID. The token is for the API that the **Scope** field names.

With the switch on, the entry also needs all of the following:

* **Client ID**
* **Scope** with at least one scope besides `openid`, `profile`, `email`, `address`, `phone`, and `offline_access`
* **Tenant ID**, a single **Authorization server** entry, or **Authorization URL** and **Token URL** with **Authorization server** empty

If the entry doesn't meet all of them, Claude Desktop doesn't load it. The server then doesn't appear in Claude Desktop, and `main.log` records `managedMcpServers entry "<name>" dropped` with the reason.

> [!WARNING]
>
> With the switch on, Claude Desktop names the API that the token is for only through **Scope**, and doesn't check that the scope belongs to this server. Enter a scope of this server's API. If you enter a scope of another API, an identity provider such as Microsoft Entra ID can issue a token for that API, and Claude Desktop sends that token to this server.

For Microsoft Entra ID, write the scope in full. That is the Application ID URI shown under **Expose an API** on the app registration that represents the server's API, a slash, and the scope name, for example `api://<api-app-id>/<scope-name> offline_access`. Microsoft Entra ID treats a scope with no such prefix as a [Microsoft Graph scope](https://learn.microsoft.com/en-us/entra/identity-platform/scopes-oidc), so the server could receive a token for Microsoft Graph.

To check that a device applies the setting, go to **Customize → Connectors** in Claude Desktop on a device where the server isn't connected yet, and click **Connect** for the server. When sign-in opens in the system browser, the `opening authorize URL` line of `main.log`, in the [logs directory](https://claude.com/docs/third-party/claude-desktop/data-storage.md#where-data-lives), records `resourceParameter: 'not sent: oauth.omitResource is true for this server'`. If the line records another value or has no `resourceParameter`, the device isn't applying the setting. Restart Claude Desktop so that it picks up the [configuration update](https://claude.com/docs/third-party/claude-desktop/admin-console.md#configuration-updates), and check its version against the release that the [configuration changelog](https://claude.com/docs/third-party/claude-desktop/configuration-changelog.md) lists for `omitResource`.

## Settings for common servers

Add each server in this table with **Add → Blank**, the **Streamable HTTP** transport, and the values shown.

| Server | URL | **OAuth** setting | What you register |
| - | - | - | - |
| Linear | `https://mcp.linear.app/mcp` | **Auto-register (dynamic client registration)** | Nothing |
| Notion | `https://mcp.notion.com/mcp` | **Auto-register (dynamic client registration)** | Nothing |
| Sentry | `https://mcp.sentry.dev/mcp` | **Auto-register (dynamic client registration)** | Nothing |

## Troubleshoot sign-in

These messages appear in Claude Desktop, or in `main.log` in the [logs directory](https://claude.com/docs/third-party/claude-desktop/data-storage.md#where-data-lives) on the user's device.

| What the user sees or `main.log` records | Cause | Fix |
| - | - | - |
| "Couldn't connect to \{server} because it doesn't support automatic client registration" (Claude Desktop 2.110.0 or later), or `main.log` records that the authorization server does not support dynamic client registration | **OAuth** is **Auto-register** but the identity provider requires a client that you register | Register a public client with redirect URI `http://127.0.0.1:53280/callback`, set **OAuth** to **Bring your own client**, and fill in **Client ID** |
| The browser step succeeds, then the connection fails and `main.log` records the token endpoint's error, for example `client_secret is missing` | The entry has a **Client ID** but the identity provider also requires the secret | Add the secret and **Authorization server** as described under [Where the client secret goes](#where-the-client-secret-goes) |
| `main.log` names a rejected referrer host during sign-in | The identity provider completes sign-in from a host other than the one in its authorization URL | Add that hostname to **Additional redirect referrer hosts** |
| The browser or `main.log` shows Microsoft Entra error `AADSTS9010010` | Claude Desktop sends the URL that the MCP server publishes about itself as the OAuth `resource` parameter, and Microsoft Entra ID rejects a `resource` that isn't an Application ID URI of the API whose scopes are requested | Register that URL as an Application ID URI in Microsoft Entra ID, or turn on the **Omit resource parameter** switch, as described under [Omit the resource parameter](#omit-the-resource-parameter) |
| The server shows as connected but its tool calls fail, and `main.log` records `mid-session refresh did not rotate` with an OAuth error code such as `invalid_request` as its `reason` | The identity provider refused a token refresh with an error that Claude Desktop treats as temporary, so Claude Desktop keeps retrying and doesn't ask the user to sign in again | Look up the refused request in the identity provider's sign-in log and correct what it reports |

## Related connector guides

[Connect to Google Cloud](https://claude.com/docs/third-party/claude-desktop/connectors-google-cloud.md) and [Connect to Box](https://claude.com/docs/third-party/claude-desktop/connectors-box.md) walk through two servers that need a client you register and its secret. [Connect to GitHub](https://claude.com/docs/third-party/claude-desktop/connectors-github.md) and [Connect to Microsoft 365](https://claude.com/docs/third-party/claude-desktop/connectors-m365.md) cover those connectors end to end, including the [built-in servers](https://claude.com/docs/third-party/claude-desktop/built-in-connectors.md) that run inside the app. [Connect to Salesforce](https://claude.com/docs/third-party/claude-desktop/connectors-salesforce.md) covers Salesforce's plugin marketplace and its hosted MCP server. Add other partners' plugin marketplaces on the **Plugins** page, as described under [Plugin marketplaces](https://claude.com/docs/third-party/claude-desktop/admin-console.md#plugin-marketplaces).
