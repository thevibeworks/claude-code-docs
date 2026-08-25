> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Connect to GitHub

> Give Claude access to your organization's GitHub repositories, issues, and pull requests, either through GitHub's hosted MCP server or a server built into the desktop app.

When Claude Desktop is deployed on third-party inference, Claude can work with your organization's GitHub data (repositories, issues, pull requests, and more) through GitHub's open-source [github-mcp-server](https://github.com/github/github-mcp-server). Two connectors are available: a [remote connector](#remote-connector), where the desktop app connects to GitHub's hosted copy of the server, and a [local connector](#local-connector), a copy of the server built into the desktop app. In both cases the device talks to GitHub directly; no GitHub data or tokens pass through Anthropic's infrastructure.

## Choose a connector

Both connectors expose the same family of GitHub tools; they differ in where the server runs and how users authenticate. Use this table to pick one, then follow that connector's section below.

|                          | Remote connector                                                                     | Local connector                                                                                                  |
| ------------------------ | ------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------- |
| Where the server runs    | GitHub's infrastructure                                                              | On the user's device, bundled in the app                                                                         |
| Authentication           | A personal access token you issue and distribute                                     | OAuth device flow; no tokens to issue or distribute                                                              |
| Credential handling      | Token delivered through the entry's `headers` or a headers helper script             | User signs in; the token is acquired and stored encrypted on the device                                          |
| GitHub Enterprise Server | Not available; github.com only                                                       | Supported; set `host`                                                                                            |
| Tool surface controls    | Per-tool [`toolPolicy`](/docs/third-party/claude-desktop/configuration#managedmcpservers) | `toolsets`, `readOnly`, and per-tool [`toolPolicy`](/docs/third-party/claude-desktop/configuration#managedmcpservers) |
| Claude Desktop version   | Any version that supports managed MCP servers                                        | Requires a version that includes the bundled server (beta)                                                       |

## Remote connector

GitHub hosts a copy of github-mcp-server on its own infrastructure. Claude Desktop on 3P connects to it as a standard remote [`managedMcpServers`](/docs/third-party/claude-desktop/configuration#managedmcpservers) entry, authenticated with a GitHub personal access token: the device connects straight to GitHub's endpoint, and the token travels only in the request headers from the user's device.

```json theme={null}
{
  "name": "GitHub",
  "url": "https://api.githubcopilot.com/mcp/",
  "transport": "http",
  "headersHelper": "/opt/org/bin/github-token"
}
```

The `headersHelper` executable prints the request headers as a flat JSON object to stdout, for example `{"Authorization": "Bearer GITHUB_PAT"}`, and follows the execution model described under [short-lived credentials with a headers helper](/docs/third-party/claude-desktop/extensions#short-lived-credentials-with-a-headers-helper). Use it to fetch a per-user fine-grained token from your secrets manager. A static `headers` object also works, but it puts the same token on every device, so every session acts as that one identity; prefer the helper, a narrowly scoped fine-grained token, or the [local connector](#local-connector), which needs no tokens at all.

Check the endpoint URL, the supported authentication methods, and the token scopes your tools need against [GitHub's github-mcp-server documentation](https://github.com/github/github-mcp-server), which is the source of truth for the hosted server. GitHub Enterprise Server instances are not reachable through GitHub's hosted endpoint; use the local connector instead.

## Local connector

Claude Desktop includes a built-in copy of github-mcp-server and runs it as a local process when a `managedMcpServers` entry sets `server` to `github`. The server calls github.com, or your GitHub Enterprise Server instance, directly from the device.

Users sign in to GitHub from the app through the OAuth device flow, so there are no personal access tokens to issue, distribute, or rotate. You register one OAuth app in your GitHub organization and ship its client ID in the entry; each user then authorizes their own sign-in.

The local connector is in beta, and the in-app configuration window marks it with a **Beta** pill.

### Set up the local connector

<Steps>
  <Step title="Register a GitHub OAuth app">
    In your GitHub organization, open **Settings → Developer settings → OAuth Apps → New OAuth App** and register an app for Claude Desktop:

    1. Set **Application name** and **Homepage URL** to values your users will recognize on the authorization screen.
    2. Enter any valid URL as the **Authorization callback URL**. The device flow does not use a redirect, but GitHub requires the field.
    3. After registering, select **Enable Device Flow** on the app's settings page and save. Sign-in fails without it.
    4. Note the app's **Client ID**. Do not create a client secret; the device flow does not use one, and Claude Desktop never asks for it.

    A GitHub App works in place of an OAuth app: put its client ID in the same field. Its permissions come from the app registration itself (the entry's `scope` field is ignored), it must be installed where users need access, and its user tokens expire after about eight hours, so users sign in again more often than with an OAuth app.
  </Step>

  <Step title="Add the managed entry">
    In the Claude Desktop [in-app configuration window](/docs/third-party/claude-desktop/in-app-configuration), open **Connectors**, select **Add server**, and choose **GitHub** under the **Built-in** group. Enter the client ID from step 1, select **Test connection** to verify that the bundled server starts and lists its tools, and select **Save**.

    If you manage configuration through JSON or a plist directly, add an entry to [`managedMcpServers`](/docs/third-party/claude-desktop/configuration#managedmcpservers) with the `server` field set to `github`:

    ```json theme={null}
    {
      "name": "GitHub",
      "server": "github",
      "clientId": "OAUTH_APP_CLIENT_ID_FROM_STEP_1"
    }
    ```

    | Field        | Required | Description                                                                                                                                                                                               |
    | ------------ | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | `name`       | Yes      | Unique display name, shown to users in connector settings.                                                                                                                                                |
    | `server`     | Yes      | Must be `github`.                                                                                                                                                                                         |
    | `clientId`   | Yes      | The client ID of the OAuth app (or GitHub App) from step 1.                                                                                                                                               |
    | `host`       | No       | Base URL of your GitHub Enterprise Server instance, for example `https://github.example.com`. Leave unset for github.com. HTTPS is required.                                                              |
    | `scope`      | No       | Space-separated OAuth scopes to request at sign-in, for example `repo read:org`. Defaults to `repo read:org read:user`. Ignored for GitHub Apps.                                                          |
    | `toolsets`   | No       | Comma-separated [github-mcp-server toolsets](https://github.com/github/github-mcp-server) to enable, for example `context,repos,issues,pull_requests`. Defaults to the bundled server's default toolsets. |
    | `readOnly`   | No       | `true` starts the server with read tools only; write tools are not registered at all.                                                                                                                     |
    | `toolPolicy` | No       | Per-tool approval locks, the same as for any managed server. See [`toolPolicy`](/docs/third-party/claude-desktop/configuration#managedmcpservers).                                                             |

    In the in-app configuration window, the GitHub form offers the client ID, GitHub Enterprise Server URL, toolsets, and read-only fields; set `scope` through exported JSON or your device-management tool if you need a non-default scope set.
  </Step>

  <Step title="Allow the required network hosts">
    The server and the sign-in flow call GitHub directly from the device, so in addition to the [base egress hosts](/docs/third-party/claude-desktop/telemetry#required-egress-paths), devices need outbound HTTPS access to:

    | Host             | Purpose                   |
    | ---------------- | ------------------------- |
    | `github.com`     | OAuth device-flow sign-in |
    | `api.github.com` | GitHub API calls          |

    GitHub Enterprise Server deployments need access to the instance's own host instead. No egress to any Anthropic host is needed for GitHub data.
  </Step>
</Steps>

### How users sign in

The first time a user opens the GitHub connector, Claude Desktop shows a short code and opens GitHub's device-authorization page in the system browser. The user enters the code, reviews the requested access, and approves it. The resulting token is stored encrypted on the device and reused until it is revoked, it expires, or the entry's identity fields change; **Disconnect** in connector settings deletes it.

### Control what Claude can do

Three levers narrow the local connector, from coarsest to finest:

* **`readOnly`** removes every write tool from the server. Claude never sees them.
* **`toolsets`** selects which github-mcp-server tool groups are registered, so you can expose repositories and pull requests without, for example, the Actions tools.
* **`toolPolicy`** locks the approval state per tool. Without a policy, write tools ask the user before each call. A few irreversible GitHub actions (merging a pull request, pushing commits, or triggering a workflow, for example) stay at ask or stricter no matter what the policy says.

The default `repo` OAuth scope grants read and write access to repositories the user can reach, so pair a broad scope with `readOnly` or a restrictive `toolPolicy` rather than relying on the scope alone to keep sessions read-only. A narrower `scope` list, or a GitHub App with minimal permissions, limits what the token itself can do.
