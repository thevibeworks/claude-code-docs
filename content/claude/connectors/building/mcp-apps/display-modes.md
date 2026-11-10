> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Show your MCP App in the side panel or full screen

> Move your MCP App from the conversation to the side panel or full screen. Declare display modes, request a mode, and lay out by the size Claude reports.

When the conversation is too small for your [MCP App](https://claude.com/docs/connectors/building/mcp-apps/getting-started.md), Claude can show the app in a larger area. For example, a dashboard can stay open next to the conversation while the user continues to chat with Claude.

A view is one rendered instance of your app's UI in Claude. On the web and in Claude Desktop, Claude shows a view in these places:

* **The conversation**: the view appears inline
* **The side panel**: the view appears in a panel next to the conversation, and the conversation stays visible
* **Full screen**: the view fills the chat area

Claude reports the display mode `inline` for a view in the conversation. It reports `fullscreen` for a view in the side panel and for a view that is full screen.

The side panel is available to a limited set of organizations, and not in every conversation, so [check whether your organization has the side panel](#check-whether-your-organization-has-the-side-panel). Outside that section, assume that the conversation has the side panel.

> [!NOTE]
>
> This page is for developers whose MCP App already renders in Claude. These tasks are described on other pages:
>
> * **Choosing a display mode for your content**: see [Design guidelines](https://claude.com/docs/connectors/building/mcp-apps/design-guidelines.md#display-modes)
> * **Designing for the mobile apps**: see [Mobile guidelines](https://claude.com/docs/connectors/building/mcp-apps/design-guidelines.md#mobile-guidelines)
> * **Fixing an app that doesn't render**: see [Troubleshoot MCP Apps](https://claude.com/docs/connectors/building/mcp-apps/troubleshooting.md)

## Declare the display modes that a view supports

In the view's script, pass the list of modes as `availableDisplayModes` in the second argument of the [`App`](https://modelcontextprotocol.github.io/ext-apps/api/classes/app.App.html) constructor. If your view works in both modes, list both, as in `{ availableDisplayModes: ["inline", "fullscreen"] }`.

* **No list**: Claude treats the view as supporting both modes
* **An empty list, or a list without `fullscreen`**: Claude shows no expand button above the view, and doesn't automatically move the view out of the conversation
* **`fullscreen` without `inline`**: a card appears in the conversation in place of the view.
  * When the user opens the view from the card, it opens in the side panel, or full screen where the panel can't open.
  * When Claude calls the tool, Claude also tries to open the view in the side panel without a click.

If you list a value that the [MCP Apps SDK](https://modelcontextprotocol.github.io/ext-apps/api/index.html) doesn't define, such as `sidebar`, [the view doesn't start](#invalid-params-error-when-a-view-starts-or-requests-a-mode).

## Open a view in the side panel without a click

To ask Claude to open a view in the side panel without a click, set `preferredDisplayMode` to `fullscreen` on your server.

Put the field in `_meta.ui` of the view's `ui://` resource, on the content item in the `resources/read` result. This example shows that content item:

```json theme={null}
{
  "uri": "ui://example/home",
  "mimeType": "text/html;profile=mcp-app",
  "text": "<!DOCTYPE html>...",
  "_meta": { "ui": { "preferredDisplayMode": "fullscreen" } }
}
```

With the SDK, return this item in `contents` from the [read callback](https://claude.com/docs/connectors/building/mcp-apps/quickstart.md#add-the-ui-to-the-tool) that you pass to `registerAppResource()`.

To test the preference, start a new conversation and ask Claude to open your app. The view opens in the side panel, and its [`displayMode`](#lay-out-a-view-by-the-size-that-claude-reports) is `fullscreen`.

> [!NOTE]
>
> `preferredDisplayMode` is an extension to `_meta.ui`. It isn't part of the MCP Apps specification or the SDK's types, so don't expect other hosts to read it. The place where you declare it can change.

* **Timing**: Claude tries once to move the view, after the view has started and the tool call has returned without an error
* **Full screen**: a preference doesn't open the view full screen
* **If the view doesn't move**: check [why a view with a preference stays in the conversation](#a-view-with-preferreddisplaymode-stays-in-the-conversation)

## Request full screen from a click or key press

To let the user move your view out of the conversation, give the view a button that requests `fullscreen`. In the view's script, call [`requestDisplayMode`](https://modelcontextprotocol.github.io/ext-apps/api/classes/app.App.html#requestdisplaymode) with `fullscreen` directly inside a click or key handler.

* **With a recent click or key press in the view**: Claude opens the view in the side panel, where the mode is also `fullscreen`
* **Without one**: Claude refuses the request

To run this sample, add `<button id="expand">` to the view's HTML. Use `@modelcontextprotocol/ext-apps` 1.4.0 or later, which the `addEventListener` call requires.

The sample is the script for a view. It declares both modes, shows a button where Claude offers `fullscreen`, and applies a compact layout when the view is narrower than 600 pixels:

```ts theme={null}
import { App } from "@modelcontextprotocol/ext-apps";

const app = new App(
  { name: "example-app", version: "1.0.0" },
  { availableDisplayModes: ["inline", "fullscreen"] }
);
const expandButton = document.querySelector<HTMLButtonElement>("#expand")!;

function layOut() {
  const context = app.getHostContext();
  const size = context?.containerDimensions;
  const canExpand = context?.availableDisplayModes?.includes("fullscreen") ?? false;
  expandButton.hidden = !canExpand || context?.displayMode === "fullscreen";
  document.body.classList.toggle("compact", !!size && "width" in size && size.width < 600);
}

app.addEventListener("hostcontextchanged", layOut);
expandButton.addEventListener("click", async () => {
  const { mode } = await app.requestDisplayMode({ mode: "fullscreen" });
  console.log(`Claude set the display mode to ${mode}`);
});

await app.connect();
layOut();
```

To test the sample, click the button in Claude. The view moves to the side panel, the button disappears, and [the view's console](https://claude.com/docs/connectors/building/mcp-apps/troubleshooting.md#open-developer-tools) shows `Claude set the display mode to fullscreen`.

Where the side panel can't open, such as in a narrow window or a browser without `Element.moveBefore`, the view opens full screen if Claude offers that mode.

### Read the result of `requestDisplayMode`

When you call `requestDisplayMode`, the SDK sends a `ui/request-display-mode` request, and the call resolves with the mode that Claude set. The call also resolves when Claude refuses the request.

To find out whether Claude granted the request, compare the returned `mode` with the mode that you requested:

| Outcome | Returned `mode` | What happens to the view |
| - | - | - |
| Claude grants a `fullscreen` request | `fullscreen` | The view moves, and then receives host context changes with the new `displayMode` and size |
| Claude refuses the request | The view's existing mode | The view doesn't move |
| You request `fullscreen` from the side panel | `fullscreen` | The view stays in the side panel |
| You request a value that the SDK doesn't define | None | The promise rejects with an invalid params error |

To return the view to the conversation, request `inline`. If Claude refuses a request, check [what a request needs](#the-returned-mode-differs-from-the-mode-that-you-requested).

## Lay out a view by the size that Claude reports

In the view's script, choose your layout from `hostContext.containerDimensions`, which gives the size of the view's container in pixels. `containerDimensions` has these fields in each mode:

* **In `fullscreen` mode**: `width` and `height`, once Claude has measured the container
* **In `inline` mode**: `width` and `maxHeight`

> [!NOTE]
>
> You can read the current mode from the `displayMode` field of the [host context](https://modelcontextprotocol.github.io/ext-apps/api/interfaces/app.McpUiHostContext.html), but the value is `fullscreen` in both the side panel and full screen.

Lay out again on each [`hostcontextchanged`](https://modelcontextprotocol.github.io/ext-apps/api/types/app.AppEventMap.html) event, as [the sample that requests full screen](#request-full-screen-from-a-click-or-key-press) does. The mode and the size both change during a view's life, for example when the user drags the panel's edge, moves the view to full screen, or narrows the window.

Design for these side panel widths:

* **Opening width**: about half the width of the chat area
* **Minimum width**: about 320 pixels

Keep controls within [`safeAreaInsets`](https://claude.com/docs/connectors/building/mcp-apps/design-guidelines#safe-areas). In the side panel, Claude reports an inset on the edge next to the conversation.

## Check whether your organization has the side panel

To check your access to the side panel, use a view that supports `fullscreen`:

1. Reload Claude on the web, or reload the main Claude Desktop window
2. Open your app in a conversation that has the [unified Claude experience](https://support.claude.com/en/articles/16761823-claude-cowork-and-chat-are-one-claude), which combines chat and Cowork. If the message box offers a choice of **Chat** or **Cowork**, your account doesn't have it.
3. Look for the expand button, an icon that Claude shows above an inline view. A user clicks it to open the view in the side panel, or full screen where the panel can't open.

If Claude shows no expand button, your organization may not have access. Keep your app working without the side panel, and test again later.

### Views in a conversation without the side panel

Keep your own full-screen button in the view, and expect this behavior:

* **A `fullscreen` request**: where the side panel isn't available, the view opens full screen when you request `fullscreen`, if Claude offers that mode
* **`fullscreen` without `inline`**: in an organization without the side panel, a view that lists `fullscreen` but not `inline` appears in the conversation

## What happens to an open view when Claude calls a tool

Claude opens a new view for each new tool call. If the new view supports `fullscreen`, it can replace a view that is already open in the side panel or full screen:

* **The open view is full screen**: the new view can replace it, whichever connector the open view came from.
  * The new view must send `ui/notifications/initialized` within 15 seconds of when Claude starts to load it. `app.connect()` sends that notification.
  * The 15 seconds include reading the `ui://` resource and loading the view.
  * A view that starts later appears in the conversation, behind the full-screen view.
* **The open view is in the side panel**: the new view replaces it if both views came from the same connector
* **The new view lists `fullscreen` but not `inline`**: the new view opens in place of anything that the side panel shows

The replaced view returns to the conversation, and its `displayMode` becomes `inline`. To stop that view from acting on outdated data, see [Supersede older widget instances](https://claude.com/docs/connectors/building/mcp-apps/instance-supersession.md).

## Troubleshoot display modes

To read what your view logs, such as the mode that a request returned, [open developer tools](https://claude.com/docs/connectors/building/mcp-apps/troubleshooting.md#open-developer-tools).

### The returned `mode` differs from the mode that you requested

Claude refused the request, and the view didn't move. Check that the request meets requirements such as these:

* **A recent click or key press in the view**: Claude refuses a `fullscreen` request with no recent press, such as a request when the view loads or from a timer
* **Focus in the view**: the view must also have focus. On a button that requests `fullscreen`, don't cancel `mousedown`.
* **A mode that Claude offers**: the requested mode must be in `hostContext.availableDisplayModes`. Check the list before you show your own button.
  * Claude lists `inline` and `fullscreen` there.
  * It lists only `inline` where views can't leave the conversation, such as a chat in its own Claude Desktop window.
* **No open prompt, for a return to the conversation**: while an approval or sign-in prompt is open, Claude refuses an `inline` request from the side panel.

### A view with `preferredDisplayMode` stays in the conversation

The view stays in the conversation in cases such as these:

* **The side panel shows something else**: such as a file, an artifact, or another connector's view
* **The user closed the side panel**: they closed it earlier in the same conversation, while it showed a view from your connector. This case no longer applies after the user opens one of your connector's views with the expand button, or reloads the page.
* **The side panel can't open**: for example, the window is narrow, or the side panel isn't available in the conversation
* **The view doesn't support `fullscreen`**: your [`availableDisplayModes`](#declare-the-display-modes-that-a-view-supports) list doesn't include the mode

### Invalid params error when a view starts or requests a mode

If you list a value that the SDK doesn't define, such as `sidebar`, in `availableDisplayModes`, `ui/initialize` fails with an invalid params error. `app.connect()` then rejects, and the view doesn't start.

If you pass such a value to `requestDisplayMode`, that call also rejects with an invalid params error. The SDK defines the values `inline`, `fullscreen`, and `pip`.

## Next steps

* [Let Claude call tools in your MCP App](https://claude.com/docs/connectors/building/mcp-apps/app-tools.md): let Claude change what the user has open in the view
* [Let people open your MCP App without asking Claude](https://claude.com/docs/connectors/building/mcp-apps/entry-points.md): list your app in Claude so that people open it themselves
