> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Let Claude call tools in your MCP App

> Register tools in your MCP App so that Claude can change what's on screen. Test a tool and fix SDK errors.

With an app tool, Claude can change what your [MCP App](https://claude.com/docs/connectors/building/mcp-apps/getting-started.md) shows while a user has it open. For example, in a shopping list app, a user asks Claude to add milk, and milk appears in the list on screen.

This page is for developers whose MCP App already renders in Claude. App tools are available to a limited set of organizations, and not in every conversation, so [check whether your organization has access](#check-whether-your-organization-has-access-to-app-tools).

> [!NOTE]
>
> If you don't have an MCP App yet, start with [Add an interactive UI to your MCP server](https://claude.com/docs/connectors/building/mcp-apps/quickstart.md).

## Register an app tool in a view

A view is one rendered instance of your app's UI in Claude.

To give Claude an action in your app, register a tool in the view's script, either with a schema library or with your own JSON Schema:

* **[With a schema library](#register-with-app-registertool-and-a-schema-library)**: call `app.registerTool`
* **[With your own JSON Schema](#register-with-handlers-and-your-own-json-schema)**: set the `onlisttools` and `oncalltool` handlers

Call `app.registerTool` before the script calls `app.connect()`, so that the view declares the `tools` capability when it connects.

The [MCP Apps SDK](https://modelcontextprotocol.github.io/ext-apps/api/index.html) has two functions with similar names. Use the one that runs in the view:

* **[`registerAppTool`](https://modelcontextprotocol.github.io/ext-apps/api/functions/server-helpers.registerAppTool.html)**: call it on your server to register the tool that opens the view
* **[`app.registerTool`](https://modelcontextprotocol.github.io/ext-apps/api/classes/app.App.html#registertool)**: call it in the view to register an app tool

The two samples do the same thing. Each is the script for a view that shows a shopping list, and each registers one tool, `add_item`, which adds an item to that list.

To run either sample, add `<ul id="items"></ul>` to the view's HTML.

### Register with `app.registerTool` and a schema library

Use this option to describe each tool's input with a schema library, so that you don't write JSON Schema yourself. Call `app.registerTool` once for each tool. This option has these requirements:

* **Schema library**: for the input schema, pass a schema object from a library that implements [Standard Schema](https://standardschema.dev/) with JSON Schema output, such as zod 4.2 or later
* **SDK version**: `app.registerTool` requires `@modelcontextprotocol/ext-apps` 1.7.0 or later
* **Bundler**: the sample imports both packages by name, which a browser can't resolve, so bundle the view's script. If your view loads the SDK from a CDN, as in the [quickstart](https://claude.com/docs/connectors/building/mcp-apps/quickstart.md#add-the-ui-to-the-tool), [register with handlers](#register-with-handlers-and-your-own-json-schema).

This sample registers `add_item` and writes its input schema with zod:

```ts theme={null}
import { App } from "@modelcontextprotocol/ext-apps";
import { z } from "zod";

const app = new App({ name: "Shopping list", version: "1.0.0" });

app.registerTool(
  "add_item",
  {
    title: "Add item",
    description: "Add an item to the shopping list that is open in this view.",
    inputSchema: z.object({ name: z.string().describe("The item to add") })
  },
  async ({ name }) => {
    const item = document.createElement("li");
    item.textContent = name;
    document.querySelector("#items")?.append(item);
    return { content: [{ type: "text", text: "Added " + name + "." }] };
  }
);

await app.connect();
```

### Register with handlers and your own JSON Schema

Use this option to write each tool's JSON Schema yourself. Write these pieces:

* **`onlisttools`**: return the tool definitions
* **`oncalltool`**: run each call. Check the arguments, because the handlers don't validate them.
* **`App` constructor**: pass `{ tools: { listChanged: true } }` as the second argument

This sample registers `add_item` this way:

```ts theme={null}
import { App } from "@modelcontextprotocol/ext-apps";

const app = new App(
  { name: "Shopping list", version: "1.0.0" },
  { tools: { listChanged: true } }
);

app.onlisttools = async () => ({
  tools: [
    {
      name: "add_item",
      title: "Add item",
      description: "Add an item to the shopping list that is open in this view.",
      inputSchema: {
        type: "object",
        properties: { name: { type: "string", description: "The item to add" } },
        required: ["name"]
      }
    }
  ]
});

app.oncalltool = async ({ name, arguments: args }) => {
  if (name !== "add_item" || typeof args?.name !== "string") {
    return {
      content: [
        { type: "text", text: "Nothing was added. Call add_item with the item's name as a string." }
      ]
    };
  }
  const item = document.createElement("li");
  item.textContent = args.name;
  document.querySelector("#items")?.append(item);
  return { content: [{ type: "text", text: "Added " + args.name + "." }] };
};

await app.connect();
```

In a view that loads the SDK from a CDN, keep [the CDN import from the quickstart](https://claude.com/docs/connectors/building/mcp-apps/quickstart.md#add-the-ui-to-the-tool) instead of the import line in this sample.

## Test an app tool in Claude

To confirm that Claude can find and call your tool, test it in Claude on the web. For `add_item` from the [shopping list samples](#register-an-app-tool-in-a-view), follow these steps:

1. [Add your server to Claude as a custom connector](https://claude.com/docs/connectors/building/testing.md#test-in-claude-as-a-custom-connector)
2. Start a new conversation with the [unified Claude experience](https://support.claude.com/en/articles/16761823-claude-cowork-and-chat-are-one-claude), which combines chat and Cowork. If the message box offers a choice of **Chat** or **Cowork**, your account doesn't have it.
3. Set the permission setting in the message box to **Manual**. In **Auto**, Claude can use a tool without asking.
4. Ask Claude to open the app, and name your connector in the message
5. In a second message, ask for a change, such as adding milk to the list.

Claude asks you to approve the **Add item** tool, and after you allow it, milk appears in the view.

### Check whether your organization has access to app tools

App tools are available to a limited set of organizations, so the account that you test with may not have them. To check your access, follow these steps:

1. [Test a tool in Claude](#test-an-app-tool-in-claude)
2. If Claude doesn't ask you to approve the tool and doesn't run it, rule out the causes under [Claude finds no tools in the view](#claude-finds-no-tools-in-the-view)
3. If none of those causes applies, your organization may not have access. Keep your app working without app tools, and test again later.

In an organization without app tools, the rest of the view continues to work.

## Update app tools while a view is open

You can enable, disable, update, remove, or add tools while a view is open. For example, disable an editing tool while no document is open.

* **With `app.registerTool`**: keep the handle that the function returns. Call `enable()`, `disable()`, `update()`, or `remove()` on that handle.
* **To add a tool after `connect()`**: call `app.registerTool` again
* **With the `onlisttools` handler**: call `app.sendToolListChanged()` when the list that the handler returns changes. `app.sendToolListChanged` requires `@modelcontextprotocol/ext-apps` 1.7.0 or later.

## Design app tools

A conversation can hold two views of your app, and each of Claude's calls reaches only one of them. Write each tool to change only its own view's state.

### Approval before an app tool runs

Claude asks the user to approve a tool before the tool runs, unless the user's saved choice, such as **Always allow**, or the conversation's permission setting already applies to the call.

* **What the prompt names**: the connector and the tool's `title`. If you set no `title`, the user sees the `name`.
* **What else the user can read**: the values that Claude is sending, your `description`, and the tool's inputs
* **If the user declines**: the tool isn't called, and Claude receives an error result that says so
* **Always allow**: the prompt can offer this option, and Claude can then run that tool on later calls without asking

When your view calls your own server's tools with `app.callServerTool`, the user doesn't see the prompt.

### Keep each app tool definition constant

A user saves a choice on the approval prompt, such as **Always allow**, for the tool as you defined it. Claude can ask for approval again after changes such as these:

* A change to the tool's name, title, description, or input schema
* A change to the server tool that opens the view

Put a value that changes, such as the name of the open file, in the tool's results.

### Write a complete first line for each tool description

Write the first line so that Claude can understand it without the rest of the description. When Claude lists a view's tools, it receives each tool's name and the first line of its description, up to 200 characters. Claude receives the rest of the description when it looks up that tool.

### Return text from app tools

Put what Claude needs in a `text` block, because Claude reads the `text` blocks in a result's `content`.

* **`structuredContent`**: Claude reads it, as JSON, only when it receives no text at all from `content`
* **Other block types**: if you return a block of another type, such as an image, Claude receives text for that block too and doesn't read the result's `structuredContent`

### Report a failure from an app tool

To report a failure, return `isError: true` or throw an error. Claude receives an error result, which might not contain your message.

When Claude can recover, for example by changing an input, return a normal result that says what to change.

## Limits on app tools

| What is limited | Limit | If you exceed the limit |
| - | - | - |
| Tools in one view | 64 | Claude can't use any of the view's tools |
| All of a view's tool definitions together | 1 MiB as JSON | Claude can't use any of the view's tools |
| Tool name | Letters, digits, `.`, `_`, and `-`. Up to 128 characters. Unique in the view. | Claude doesn't receive the tool |
| Input schema type | Every tool has `type: "object"` at the root of its `inputSchema` | Claude can't use any of the view's tools |
| Input schema size | Up to 64 KiB as JSON, nested up to 32 levels | Claude receives an empty object schema for the tool, and the user doesn't see **Always allow** in the prompt |
| Time to respond | 45 seconds, not counting the user's approval | Claude receives an error result that says the view didn't respond and the action might have happened |
| Result text | 100,000 characters | Claude receives the first 100,000 characters of text and a line that says the rest was removed. If `structuredContent` is longer than the limit, Claude can receive none of it. |

For work that can take longer than the time limit, start the work and return immediately. Register a second tool that reports the outcome.

## Views that Claude can reach

If Claude doesn't call your view's tools, check the view's connector, where you test, and whether the view is loaded:

* **Remote connector**: the view must come from a remote connector. Claude doesn't call the tools of a view from a local server, such as one in the Claude Desktop configuration file.
* **Where to test**: test on the web, in a conversation with the [unified Claude experience](#test-an-app-tool-in-claude).
  * On Team and Enterprise plans, an Owner or Primary Owner controls it with the **Chat and Cowork unified** setting in [**Organization settings > Capabilities**](https://claude.ai/admin-settings/capabilities).
* **Loaded view**: if the view isn't loaded in the Claude page that the user has open, Claude's call isn't sent. Claude receives an error result that says so.
  * When a view loads again, it starts from your HTML, so store on your server anything that you need to keep.

## Troubleshoot app tools

To see the messages between your view and Claude, [open developer tools](https://claude.com/docs/connectors/building/mcp-apps/troubleshooting.md#open-developer-tools). The SDK logs these protocol messages with `console.debug`, so in Chrome you see them at the **Verbose** level.

### Claude finds no tools in the view

The view renders and throws no exception, but Claude doesn't use a tool that you registered. Check for each of these causes:

* **You asked for the change in the message that opened the app**: when the first view opens in a conversation, Claude receives its tools with your next message. Ask Claude to open the app, and name your connector in the message. Then ask for the change in a second message.
* **You passed an `inputSchema` that isn't a schema object**:
  * **Cause**: `app.registerTool` can't convert a plain object, such as JSON Schema or the `{ name: z.string() }` shape that server tools take.
  * **Effect**: the view responds to `tools/list` with an error, and Claude can't see the view's other tools either.
  * **Fix**: pass a schema object from your schema library, or use [the `onlisttools` and `oncalltool` handlers](#register-with-handlers-and-your-own-json-schema).
* **The view exceeds a limit, or Claude can't reach it**: check the [limits on app tools](#limits-on-app-tools) and the [views that Claude can reach](#views-that-claude-can-reach)
* **Your organization or conversation doesn't have app tools**: [check whether your organization has access](#check-whether-your-organization-has-access-to-app-tools)

### `app.registerTool is not a function`

The installed `@modelcontextprotocol/ext-apps` package is older than 1.7.0. Upgrade the package, or use [the `onlisttools` and `oncalltool` handlers](#register-with-handlers-and-your-own-json-schema).

### `Client does not support tool capability`

On an `App` that declared no `tools` capability, the SDK throws this error when you:

* Call `app.registerTool` for the first time after `connect()`
* Set `onlisttools` or `oncalltool`

The full message ends with `(required for tools/call)` or `(required for tools/list)`.

To fix the error, register the tool before `connect()`, or pass `{ tools: { listChanged: true } }` as the second argument to the `App` constructor.

### `Schema (vendor: zod) does not implement Standard JSON Schema (~standard.jsonSchema)`

* **Cause**: with `@modelcontextprotocol/ext-apps` 2.x, the view responds to `tools/list` with this error when the schema comes from zod 4.1 or earlier
* **Where it appears**: in the view's console at the **Verbose** level, in a line that starts with `Sending message`
* **Fix**: upgrade zod to 4.2 or later

## Next steps

* [Send messages to Claude from your MCP App](https://claude.com/docs/connectors/building/mcp-apps/send-messages.md): send Claude a request when the user acts in the view
* [Supersede older widget instances](https://claude.com/docs/connectors/building/mcp-apps/instance-supersession.md): keep one copy of the app active when Claude opens it more than once
* [Design guidelines](https://claude.com/docs/connectors/building/mcp-apps/design-guidelines.md#interaction-patterns): decide which interactions belong in the app and which in the conversation
* [Troubleshoot MCP Apps](https://claude.com/docs/connectors/building/mcp-apps/troubleshooting.md): fix an app that doesn't appear or loses its assets
