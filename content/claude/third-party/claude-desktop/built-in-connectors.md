> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Built-in connectors

> MCP servers bundled inside Claude Desktop on 3P: which servers ship in the app, how built-in entries work, and where each one is documented

Claude Desktop ships copies of some MCP servers inside the app itself. A built-in server runs as a local process on the user's device and calls the data provider directly, so no data or tokens pass through Anthropic's infrastructure. There is nothing to install or host on your side: a [`managedMcpServers`](/docs/third-party/claude-desktop/configuration#managedmcpservers) entry activates the server, and the app runs it.

A built-in entry names the bundled server in a `server` field, in place of the `url`, `transport`, or `command` fields that remote and stdio entries use. An entry that mixes `server` with any remote or stdio field is rejected.

## Available servers

| Server        | `server` value | What Claude can reach                                                                                 | Setup guide                                                                                              |
| ------------- | -------------- | ----------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| Microsoft 365 | `microsoft365` | Outlook mail and calendar, OneDrive, SharePoint, and Teams, through Microsoft Graph                   | [Connect to Microsoft 365, local connector](/docs/third-party/claude-desktop/connectors-m365#local-connector) |
| Web search    | `websearch`    | Web search through Brave, Tavily, Exa, or a search endpoint you host                                  | [Built-in web search](/docs/third-party/claude-desktop/web-tools#built-in-web-search)                         |
| GitHub (beta) | `github`       | Repositories, issues, pull requests, and other GitHub data, on github.com or GitHub Enterprise Server | [Connect to GitHub, local connector](/docs/third-party/claude-desktop/connectors-github#local-connector)      |

Each guide covers its server in full, including how the built-in server compares with the remote alternative where one exists. The GitHub built-in server is in beta, and the **Add server** menu marks it with a **Beta** pill.

<Note>
  In the in-app configuration window, the **Add server** menu lists built-in servers separately from remote templates. A remote template (Box, or the Microsoft 365 remote connector) only pre-fills the form for a server that runs outside the app. The servers on this page are the ones bundled inside the app.
</Note>

## How built-in servers behave

All built-in servers share the same model:

* **Managed configuration only.** A built-in server activates only from a `managedMcpServers` entry. Users cannot add one themselves and cannot remove one you deploy.
* **Local execution.** The server runs on the user's device, and its network calls go directly to the data provider (Microsoft, your search provider, or GitHub). No Anthropic host is in the data path.
* **Sign-in on the device.** Where the server needs user credentials (Microsoft 365 and GitHub), the user signs in from the app, and tokens are stored encrypted on the device. **Disconnect** in connector settings signs the user out. The web search server has no user sign-in; you supply the search key in the entry.
* **Tool approvals.** Each entry accepts the same per-tool [`toolPolicy`](/docs/third-party/claude-desktop/configuration#managedmcpservers) as any managed server. Without a policy, built-in write tools ask the user before each call, and a small set of irreversible actions (sending mail or merging a pull request, for example) stays at ask or stricter no matter what the policy says.
* **Versioned with the app.** Each built-in server requires a Claude Desktop version that includes it. On older versions, the server is missing from the **Add server** menu, **Test connection** reports that it is not included, and a deployed entry is dropped. The fix is to upgrade Claude Desktop.
