> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Let people open your MCP App without asking Claude

> Mark a tool as a global entry point so people can open your MCP App from the Artifacts page in Claude, and check why it might not appear.

A global entry point is a mark on one of your connector's tools. After you mark a tool, Claude can list your MCP App on the [**Artifacts**](https://claude.ai/artifacts) page. People open the app from that page without asking Claude for it, and they can pin it to the sidebar.

This page is for developers of a remote connector whose MCP App already renders in Claude. Check which organizations, connectors, and users can use entry points before you build:

* **Organizations**: a limited set of organizations has access, so [check whether your organization has access](#check-whether-your-organization-has-access-to-entry-points)
* **Connectors**: [Verified](https://claude.com/docs/connectors/verification.md#verified) directory connectors and [custom connectors](https://claude.com/docs/connectors/verification.md#custom) can have entry points. Connectors installed from a Community listing can't.
* **Users**: a user needs the unified Claude experience, which combines chat and Cowork

Outside these limits, people open your app by asking Claude for it in a conversation.

> [!NOTE]
>
> If your MCP App doesn't render in Claude yet, start with [Get started with MCP Apps](https://claude.com/docs/connectors/building/mcp-apps/getting-started.md).

## Mark a tool as a global entry point

To mark a tool, change its `_meta` on your server:

1. Add the `openai/ui` key
2. Set the key to an object whose `entrypoints` list contains a `global` entry
3. Keep `ui.resourceUri` in `_meta` as well

This example shows a marked tool as it appears in your server's `tools/list` result:

```json theme={null}
{
  "name": "open_studio",
  "title": "Example Studio",
  "description": "Open Example Studio.",
  "inputSchema": { "type": "object" },
  "_meta": {
    "ui": { "resourceUri": "ui://example/home" },
    "openai/ui": { "entrypoints": [{ "type": "global" }] }
  }
}
```

If you use the MCP Apps SDK, pass the same `_meta` object to [`registerAppTool()`](https://modelcontextprotocol.github.io/ext-apps/api/functions/server-helpers.registerAppTool.html).

You can mark several tools, and Claude can list one app for each marked tool.

### Confirm that Claude lists your app

To test the mark, follow these steps:

1. [Refresh the tools list](#refresh-the-tools-list-after-you-change-an-entry-point) for your connector
2. Open the [**Artifacts**](https://claude.ai/artifacts) page in Claude on the web

A listed app appears as its own tile, or as an item in the list that opens from the page's connectors tile.

If your app isn't listed, check the [conditions for showing an app](#conditions-for-showing-an-app-on-the-artifacts-page).

### Adapt a tool that declares entry points for another host

If your tool already declares the `openai/ui` key for a different host, check that the tool's `_meta` also has `ui.resourceUri`, which Claude needs. The key comes from the OpenAI MCP extensions.

## Design the view that people open from an entry point

A view is one rendered instance of your app's UI in Claude. When a user opens your app from an entry point, the view starts with no request from the user and no existing conversation.

* **Arguments**: make every input optional and show a useful starting state when the arguments are `{}`.
  * Claude can choose a value for an optional input, so don't treat a value as proof of the user's choice.
* **Conversation**: on the web, the app opens in a new conversation each time a user opens it
* **Display mode**: on the web, Claude shows the view full screen when the view supports `fullscreen`, so include `fullscreen` if you declare [`availableDisplayModes`](https://claude.com/docs/connectors/building/mcp-apps/design-guidelines#declare-supported-display-modes).
  * Without `fullscreen`, the view appears in the conversation.
* **Approval**: if the tool's permission is **Needs approval**, Claude asks the user for approval before the view opens. If the conversation's permission setting is **Auto**, Claude can open the view without asking.

### Set the title, name, and description of the marked tool

* **`title`**: set a `title`, because Claude displays it with the connector's name. Use 60 characters or fewer, and leave out Claude's name and Anthropic's name.
* **`name`**: don't put two underscores in a row, two dots in a row, or a dot next to an underscore in the `name`. With any of these, Claude lists the app but people can't open it from the entry point.
* **`description`**: write it for conversations too, because Claude can also call the same tool in a conversation where the connector is turned on

## Refresh the tools list after you change an entry point

After you add or edit an entry point, the change can take up to about two hours to appear, even after you reload the page.

To see the change immediately, refresh the tools list:

1. Go to [**Customize > Connectors**](https://claude.ai/customize/connectors) and select your connector
2. Open the three-dot menu and click **Refresh tools list**

You refresh the list for your own account. Other people can still wait for the change.

## Conditions for showing an app on the Artifacts page

Claude shows no error when it doesn't list your app on the [**Artifacts**](https://claude.ai/artifacts) page. If your app isn't listed, [refresh the tools list](#refresh-the-tools-list-after-you-change-an-entry-point) first, then check each condition.

In your server's `tools/list` result, check the `_meta` of the tool that you marked:

* **Entry point**: `_meta["openai/ui"].entrypoints` contains `{ "type": "global" }`
* **View**: `_meta.ui.resourceUri` points to a `ui://` resource
* **Visible to Claude**: `_meta.ui.visibility` is omitted or contains `model`, so that Claude can call the tool

Check the tool's connector:

* **Remote**: the connector is remote, not a local server
* **Verified or custom**: the connector has the Verified label in the directory, or it's a [custom connector](https://claude.com/docs/connectors/verification.md#custom).
  * If a user installs the connector from a Community listing, Claude doesn't show its apps on the **Artifacts** page or in the sidebar, including pinned apps.
  * For what each label means, see [Connector verification](https://claude.com/docs/connectors/verification.md#connector-labels).

For each user, including you while you test, check the account and the organization:

* **Unified Claude experience**: the user has [this experience](https://support.claude.com/en/articles/16761823-claude-cowork-and-chat-are-one-claude), which combines chat and Cowork.
  * If the message box offers a choice of **Chat** or **Cowork**, the account doesn't have it.
  * On Team and Enterprise plans, an Owner or Primary Owner controls it with the **Chat and Cowork unified** setting in [**Organization settings > Capabilities**](https://claude.ai/admin-settings/capabilities).
* **Connected**: the user has connected the connector
* **Turned on**: the user hasn't turned off the connector or set the tool to **Blocked**
* **Allowed by the organization**: on Team and Enterprise plans, the organization hasn't set the tool or the connector to **Blocked**
* **Organization access**: the user's organization [has access to entry points](#check-whether-your-organization-has-access-to-entry-points)

Claude can still list an app whose tool is set to **Needs approval**.

### Check whether your organization has access to entry points

To check your own organization, follow these steps:

1. [Refresh the tools list](#refresh-the-tools-list-after-you-change-an-entry-point), then reload Claude on the web
2. If your app isn't listed and meets all the other [conditions](#conditions-for-showing-an-app-on-the-artifacts-page), your organization may not have access
3. Keep your app working without an entry point, and test again later

### Entry points that appear while you test and stay hidden for other people

An app that you see on the **Artifacts** page while you test can still be hidden for other people. For example, suppose you add your server by URL and the same server also has a Community listing:

* **You**: you keep the entry point on the connector that you added by URL
* **People who install the Community listing**: they have no entry point

To move from a Community listing to Verified, see [Connector verification](https://claude.com/docs/connectors/verification.md#list-your-own-connector).

## Next steps

* [Show your MCP App in the side panel or full screen](https://claude.com/docs/connectors/building/mcp-apps/display-modes.md): lay out the view for full screen and for the side panel
* [Test your connector](https://claude.com/docs/connectors/building/testing.md): add your server as a custom connector and open the app yourself
* [Submit a connector](https://claude.com/docs/connectors/building/submission.md): list your connector and its MCP App in the directory
