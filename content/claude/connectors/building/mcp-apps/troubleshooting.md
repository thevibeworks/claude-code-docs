> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Troubleshoot MCP Apps

> Debug MCP Apps in Claude with developer tools on desktop and iOS, and fix invisible apps, large tool results, iOS-only request failures, and ui.domain errors.

When an MCP App doesn't render or load correctly in Claude, the tool call usually still appears in the conversation, and the cause is in how the app connects, sizes itself, receives its data, or loads its assets. This page is for developers debugging their own MCP App. [Open the developer tools](#open-developer-tools) in Claude Desktop or on iOS to inspect the app's iframe, then match what you see against the [common problems](#fix-common-problems).

## Open developer tools

Claude Desktop and the Claude iOS app both let you inspect a running MCP App with browser developer tools.

### Claude Desktop

Claude Desktop's Developer Tools can help you debug MCP Apps. To use them:

<Steps>
  <Step title="Enable Developer Mode">
    Open **Help > Troubleshooting** and click **Enable Developer Mode**. A new **Developer** menu appears in the menu bar.
  </Step>

  <Step title="Open Developer Tools">
    Open Developer Tools by pressing `Cmd+Option+I` on Mac or `Ctrl+Shift+I` on Windows.
  </Step>

  <Step title="Find your app's iframe">
    Inspect the tool call element and look for an iframe nested inside another iframe. Your app is loaded as the content of the inner iframe.
  </Step>
</Steps>

<Tip>From the **Developer** menu, select **Reload MCP Configuration** after editing your `claude_desktop_config.json` to apply changes without restarting.</Tip>

### iOS

On iOS, the Claude app renders your MCP App inside a `WKWebView`. You can inspect it from a connected Mac using Safari's Web Inspector. Follow Apple's guide to [inspecting iOS](https://developer.apple.com/documentation/safari-developer-tools/inspecting-ios) for setup. Once connected, the Claude web view appears under your device in Safari's **Develop** menu, and you can use the console, network panel, and element inspector as you would on desktop.

## Fix common problems

These are the problems developers hit most often when an MCP App doesn't render or load correctly in Claude, each with its cause and fix.

### Tool call appears but the app is invisible

An invisible app under a visible tool call is the most common issue when developing MCP Apps. The cause is usually a missing `app.connect()` call or an iframe with zero height.

#### Missing `app.connect()` call

Your app must call [`app.connect()`](https://modelcontextprotocol.github.io/ext-apps/api/classes/app.App.html#connect) in vanilla JS or [`useApp()`](https://modelcontextprotocol.github.io/ext-apps/api/functions/_modelcontextprotocol_ext-apps_react.useApp.html) in React to establish communication with Claude Desktop. Register your handlers before connecting:

<CodeGroup>
  ```javascript Vanilla JS theme={null}
  import { App } from "@modelcontextprotocol/ext-apps";

  const app = new App({ name: "My App", version: "1.0.0" });

  // Register handlers before connecting
  app.ontoolresult = (result) => {
    // Handle tool results
  };

  await app.connect();
  ```

  ```javascript React theme={null}
  import { useApp } from "@modelcontextprotocol/ext-apps/react";

  function MyComponent() {
    // The useApp hook handles connection automatically
    const { app } = useApp({
      appInfo: { name: "My App", version: "1.0.0" },
      capabilities: {},
      onAppCreated: (app) => {
        app.ontoolresult = (result) => {
          // Handle tool results
        };
      }
    });
  }
  ```
</CodeGroup>

<Warning>Event handlers like `app.ontoolinput` and `app.ontoolresult` aren't invoked until the app is connected.</Warning>

#### Iframe has zero height

Your app needs a non-zero height to be visible. A zero height can occur if:

* Your app's container has no content yet
* You called `sendSizeChanged({ width, height: 0 })`

Check that your root element has explicit dimensions or content that gives it height.

### App doesn't render when tool results are large

When a tool result exceeds approximately 150,000 characters and Claude's code execution sandbox is active, Claude writes the result to the sandbox filesystem instead of passing it inline to the conversation. Your app receives a pointer to the stored file rather than the structured content it needs, so it never hydrates.

<Note>This \~150,000-character threshold is specific to claude.ai and Claude Desktop. Claude Code uses a separate 25,000-token default limit, configurable through `MAX_MCP_OUTPUT_TOKENS`.</Note>

To stay under the threshold, keep initial tool result payloads lean:

* **Paginate large results**: return a summary or the first page of data, and let the user request more through follow-up interactions
* **Fetch details on demand**: use app-initiated tool calls to load additional data from within your widget as the user explores, rather than returning everything upfront
* **Defer heavy content**: if your data includes large blobs such as full document text, base64-encoded images, or extensive logs, return identifiers or previews in the initial result and provide a separate tool to retrieve the full content when needed

### Assets or API requests fail only on iOS

If your app loads on desktop and web but fails to fetch scripts, images, or API data on iOS, check whether your server, CDN, or WAF is gating access on the `Referer` header.

WebKit on iOS, in both Safari and the Claude iOS app, omits the `Referer` header on cross-origin subresource requests as part of its tracking prevention, per WebKit bugs [206521](https://bugs.webkit.org/show_bug.cgi?id=206521) and [179053](https://bugs.webkit.org/show_bug.cgi?id=179053#c8). A server that requires a `Referer` to allow the request rejects iOS traffic even though the same app works elsewhere.

To fix the iOS failures, allowlist on the `Origin` header instead of `Referer`, because WebKit does send `Origin`. Requests from your app carry an `Origin` of `{hash}.claudemcpcontent.com`, and [Set `ui.domain` for Claude](/docs/connectors/building/mcp-apps/getting-started#set-ui-domain-for-claude) shows how to compute the hash for your server URL. Configure your infrastructure to allow requests whose `Origin` matches `*.claudemcpcontent.com` and return a corresponding `Access-Control-Allow-Origin` header.

<Note>The missing `Referer` header affects requests your app makes directly from the user's device, such as loading bundles and images or calling your own API from client-side code. MCP tool calls are proxied through Claude's backend and egress from Anthropic's published IP ranges, not the user's device.</Note>

### `ui.domain` validation fails

Setting [`_meta.ui.domain`](https://modelcontextprotocol.github.io/ext-apps/api/interfaces/app.McpUiResourceMeta.html#domain) on your resource opts your app into a stable sandbox origin, which you need if your app runs its own OAuth flow. Claude validates the value against your connector URL, and when validation fails it shows an `Invalid ui.domain format` or `ui.domain mismatch` error instead of rendering the app.

The value must be exactly `{hash}.claudemcpcontent.com`, where `{hash}` is the first 32 hexadecimal characters of the SHA-256 digest of your full connector URL. Compute it by running this command with your own URL:

```shell theme={null}
node -e 'const yourServerUrl = "https://example.com/mcp"; console.log(require("crypto").createHash("sha256").update(yourServerUrl).digest("hex").slice(0,32) + ".claudemcpcontent.com")'
```

A mismatch usually has one of these causes:

* **The URL you hashed differs from the URL Claude connects to**: the hash covers the full URL string including scheme, path, and any trailing slash, so `https://example.com/mcp` and `https://example.com/mcp/` produce different values. Hash the exact URL configured in **Customize > Connectors**
* **The connector is a local stdio server**: local connectors have no URL to hash, so `ui.domain` isn't available for them. Remove the field, or deploy the server as a remote connector to use a stable origin

[Set `ui.domain` for Claude](/docs/connectors/building/mcp-apps/getting-started#set-ui-domain-for-claude) explains how the origin is used across platforms.

## Next steps

* [Set `ui.domain` for Claude](/docs/connectors/building/mcp-apps/getting-started#set-ui-domain-for-claude): compute the sandbox origin Claude expects for your app
* [Design guidelines](/docs/connectors/building/mcp-apps/design-guidelines#mobile-guidelines): mobile layout, safe areas, and sizing rules that prevent clipped or invisible content
* [Get started with MCP Apps](/docs/connectors/building/mcp-apps/getting-started#build-your-own-mcp-app): SDK quickstart, examples, and agent skills
