> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Send messages to Claude from your MCP App

> Send a message from your MCP App's view to Claude with app.sendMessage. Handle each result, and keep messages within what Claude accepts.

You can send Claude a message from your [MCP App](https://claude.com/docs/connectors/building/mcp-apps/getting-started.md) when a user acts in the app and needs Claude to do something. For example, in a shopping list app, a user clicks a button to ask Claude to plan dinners from the list.

Claude acts on a message only with the user's agreement. Unless the user has already agreed to your app's messages, they agree by allowing the message or by sending it themselves from their message box.

> [!NOTE]
>
> This page is for developers whose MCP App already renders in Claude. If you don't have an MCP App yet, start with [Add an interactive UI to your MCP server](https://claude.com/docs/connectors/building/mcp-apps/quickstart.md).

## Send a message from a view

A view is one rendered instance of your app's UI in Claude.

To send Claude a message, call [`app.sendMessage`](https://modelcontextprotocol.github.io/ext-apps/api/classes/app.App.html#sendmessage) in the view's script. Claude receives the call as a `ui/message` request. Pass these fields:

* **`role`**: set it to `"user"`
* **`content`**: put the message here as `text` blocks

Send the message when the user clicks or presses a key in the view, not when the view loads, so that the user expects what follows.

This sample is the script for a view that shows a shopping list. It sends a message when the user clicks a button. To run the sample, add `<button id="plan">` and an element with `id="status"` to the view's HTML.

```ts theme={null}
import { App } from "@modelcontextprotocol/ext-apps";

const app = new App({ name: "Shopping list", version: "1.0.0" });
await app.connect();

const button = document.querySelector("#plan");
const status = document.querySelector("#status");

button?.addEventListener("click", async () => {
  let message = "Continue in the conversation.";
  try {
    const { isError } = await app.sendMessage({
      role: "user",
      content: [
        { type: "text", text: "Plan three dinners from this shopping list: milk, eggs, rice, and spinach." }
      ]
    });
    if (isError) {
      message = "Claude didn't take the request.";
    }
  } catch {
    message = "The request couldn't be confirmed.";
  }
  if (status) {
    status.textContent = message;
  }
});
```

To test the sample, click the button in Claude. Unless you've already agreed to this app's messages, Claude does one of these once it accepts the message:

* Asks you to allow the message
* Places the text in your message box, ready to send

## Write a message that the user can agree to

Write the message as a request that the user can read and agree to. Put everything that Claude needs in the message itself.

* **Caution**: when Claude fills the message box with your view's text, a caution can appear above the box. The caution opens with "Use caution before running this prompt."
* **Existing draft**: Claude doesn't replace a draft that the user already has in the message box unless they agree

## Handle the result of `app.sendMessage`

In the view's script, handle an error result, a result with no error, and a rejected promise, as the sample does:

* **`isError: true`**: treat the message as not accepted
* **A result with no error**: you can receive this result before the user agrees, and you can't learn their decision from it. Don't treat it as evidence that Claude read the message.
* **A rejected promise**: when the [MCP Apps SDK](https://modelcontextprotocol.github.io/ext-apps/api/index.html) stops waiting, after 60 seconds by default, the promise rejects. Don't tell the user that the message wasn't sent, because Claude can still have it after that time.

If you send a malformed request, the promise rejects or the result has `isError: true`.

Keep the control that sends the message usable, so that the user can try again.

## Messages that Claude accepts

If you break a length or character rule, Claude can refuse the message.

* **Content**: send `text` blocks that aren't blank. Claude refuses a blank message, and can refuse a message that contains any other kind of block.
* **Length**: send at most 8,000 characters, counted across all blocks, plus one for each block after the first
* **Invisible characters**: leave out invisible characters, such as soft hyphens and zero-width spaces, unless Claude recognizes them as part of an emoji or a writing system. Persian, Hindi, and Thai are examples of such writing systems.
* **Line breaks**: use at most three consecutive line breaks
* **Spaces and tabs**: use at most 64 consecutive spaces or tabs
* **Pace**: send a message when the user acts, not on a timer, and don't retry in code.
  * If you send messages quickly one after another, Claude can refuse them.
  * After the user declines a message, Claude can refuse later messages for a short time.

## Next steps

* [Let Claude call tools in your MCP App](https://claude.com/docs/connectors/building/mcp-apps/app-tools.md): let Claude change what the user has open in the view
* [Supersede older widget instances](https://claude.com/docs/connectors/building/mcp-apps/instance-supersession.md): stop an older copy of your app from sending messages
* [Design guidelines](https://claude.com/docs/connectors/building/mcp-apps/design-guidelines.md#interaction-patterns): decide which interactions belong in the app and which in the conversation
* [Troubleshoot MCP Apps](https://claude.com/docs/connectors/building/mcp-apps/troubleshooting.md): open developer tools to inspect the view's requests
