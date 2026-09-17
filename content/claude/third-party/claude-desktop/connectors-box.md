> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Connect to Box

> Give Claude access to your organization's Box content through Box's remote MCP server, with an OAuth client a Box admin creates and a client secret helper script on each device.

When Claude Desktop is deployed on third-party inference, Claude can work with your organization's Box content through Box's remote MCP server at `https://mcp.box.com`. The device talks to Box directly. No Box data or tokens pass through Anthropic's infrastructure.

## How the connection works

Box's MCP server requires an OAuth client that a Box admin creates, and Box's token endpoint requires that client's secret. The Enterprise Admin Console stores client secrets only for Google Desktop-app clients, so for Box each device supplies the secret through a helper script, as described under [Where the client secret goes](/docs/third-party/claude-desktop/mcp-sign-in#where-the-client-secret-goes). That page also explains each **OAuth** field.

## Set up the Box server

<Steps>
  <Step title="Create the client in Box">
    In the Box Admin Console, create integration credentials for the Box MCP server as described in Box's [remote MCP server guide](https://developer.box.com/guides/box-mcp/remote), with `http://127.0.0.1:53280/callback` as the redirect URI, and copy the generated client ID and client secret.
  </Step>

  <Step title="Install the secret helper script on every device">
    Write a script that prints the client secret as the JSON object `{"clientSecret": "…"}` and nothing else on stdout (the full contract is under [Where the client secret goes](/docs/third-party/claude-desktop/mcp-sign-in#where-the-client-secret-goes)). On macOS, save the script (for example at `/usr/local/bin/box-mcp-secret`) and mark it executable:

    ```bash theme={null}
    #!/bin/sh
    printf '{"clientSecret":"%s"}' "YOUR_BOX_CLIENT_SECRET"
    ```

    On Windows, save it as a `.cmd` file, for example `C:\Program Files\Corp\box-mcp-secret.cmd`:

    ```bat theme={null}
    @echo off
    echo {"clientSecret":"YOUR_BOX_CLIENT_SECRET"}
    ```

    A secret written into the script is readable by anyone who can read the file. Where your devices have a secret store or vault CLI, have the script read the secret from there instead.

    Distribute the script through your device management to the same absolute path on every device, in a location users can't modify. An entry holds one path for the whole organization, so if your fleet mixes macOS and Windows, add one entry per platform with its own name and script path, and assign each to the matching group of users with [per-group permission policies](/docs/third-party/claude-desktop/admin-console#per-group-permission-policies).
  </Step>

  <Step title="Add the server in the Enterprise Admin Console">
    In the Enterprise Admin Console ([claude.ai](https://claude.ai) → **Organization settings**), open the **Connectors** page under **Desktop 3P**. Under **Managed MCP servers**, click **Add → Blank** and fill in the entry:

    | Field                           | Value                                                                               |
    | ------------------------------- | ----------------------------------------------------------------------------------- |
    | **Name**                        | `Box`                                                                               |
    | **Transport**                   | **Streamable HTTP**                                                                 |
    | **URL**                         | `https://mcp.box.com`                                                               |
    | **OAuth**                       | **Bring your own client**                                                           |
    | **Client ID**                   | The client ID from step 1                                                           |
    | **Client secret helper script** | The script's absolute path from step 2, for example `/usr/local/bin/box-mcp-secret` |
    | **Authorization server**        | `["https://api.box.com"]`                                                           |

    Click **Save changes**. Users' apps pick up the new entry as described under [Configuration updates](/docs/third-party/claude-desktop/admin-console#configuration-updates). Devices need outbound HTTPS access to `mcp.box.com`, `account.box.com`, and `api.box.com`.

    If you manage configuration through MDM or a bootstrap server instead, the equivalent entry can carry the secret inline:

    ```json theme={null}
    {
      "name": "Box",
      "transport": "http",
      "url": "https://mcp.box.com",
      "oauth": {
        "clientId": "YOUR_BOX_CLIENT_ID",
        "clientSecret": "YOUR_BOX_CLIENT_SECRET",
        "authorizationServer": ["https://api.box.com"]
      }
    }
    ```
  </Step>

  <Step title="Have users connect">
    Each user opens **Customize → Connectors** in Claude Desktop, clicks **Connect** next to **Box**, and signs in to Box in the browser.
  </Step>
</Steps>
