> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Troubleshooting MCP Apps

> Debug and resolve common issues with MCP Apps

## Using developer tools

### Desktop

Claude Desktop's Developer Tools can help you debug MCP Apps. To use them:

1. Open **Help > Troubleshooting** and click **Enable Developer Mode**. A new **Developer** menu appears in the menu bar.
2. Open Developer Tools by pressing `Cmd+Option+I` (Mac) or `Ctrl+Shift+I` (Windows)
3. Inspect the tool call element and look for an iframe nested inside another iframe. Your app will be loaded as the content of the inner iframe.

<Tip>From the **Developer** menu, select **Reload MCP Configuration** after editing your `claude_desktop_config.json` to apply changes without restarting.</Tip>

### iOS

On iOS, the Claude app renders your MCP app inside a `WKWebView`. You can inspect it from a connected Mac using Safari's Web Inspector—see Apple's guide to [inspecting iOS](https://developer.apple.com/documentation/safari-developer-tools/inspecting-ios) for setup. Once connected, the Claude web view appears under your device in Safari's **Develop** menu, and you can use the console, network panel, and element inspector just as you would on desktop.

## Problem: Tool call appears but the app is invisible

This is the most common issue when developing MCP Apps. Check these two causes:

### Missing `app.connect()` call

Your app must call [`app.connect()`](https://modelcontextprotocol.github.io/ext-apps/api/classes/app.App.html#connect) (Vanilla JS) or [`useApp()`](https://modelcontextprotocol.github.io/ext-apps/api/functions/_modelcontextprotocol_ext-apps_react.useApp.html) (React) to establish communication with Claude Desktop.

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

<Warning>Event handlers like `app.ontoolinput` and `app.ontoolresult` won't be invoked until the app is connected.</Warning>

### Iframe has zero height

Your app needs a non-zero height to be visible. A zero height can occur if:

* Your app's container has no content yet
* You called `sendSizeChanged({ width, height: 0 })`

Check that your root element has explicit dimensions or content that gives it height.

## Problem: App doesn't render when tool results are large

When a tool result exceeds approximately 150,000 characters and Claude's code execution sandbox is active, the result is written to the sandbox filesystem instead of being passed inline to the conversation. Your app receives a pointer to the stored file rather than the structured content it needs, so it never hydrates.

<Note>This \~150,000-character threshold is specific to Claude.ai and Claude Desktop. Claude Code uses a separate 25,000-token default limit configurable via `MAX_MCP_OUTPUT_TOKENS`.</Note>

To avoid this, keep initial tool result payloads lean:

* **Paginate large results.** Return a summary or the first page of data, and let the user request more through follow-up interactions.
* **Fetch details on demand.** Use app-initiated tool calls to load additional data from within your widget as the user explores, rather than returning everything upfront.
* **Defer heavy content.** If your data includes large blobs—full document text, base64-encoded images, extensive logs—return identifiers or previews in the initial result and provide a separate tool to retrieve the full content when needed.

## Problem: Assets or API requests fail only on iOS

If your app loads on desktop and web but fails to fetch scripts, images, or API data on iOS, check whether your server, CDN, or WAF is gating access on the `Referer` header.

WebKit on iOS—both Safari and in the Claude iOS app—omits the `Referer` header on cross-origin subresource requests as part of its tracking prevention (WebKit bugs [206521](https://bugs.webkit.org/show_bug.cgi?id=206521) and [179053](https://bugs.webkit.org/show_bug.cgi?id=179053#c8)). A server that requires a `Referer` to allow the request will reject iOS traffic even though the same app works elsewhere.

**Fix:** Allowlist on the `Origin` header instead, which WebKit does send. Requests from your app carry an `Origin` of `{hash}.claudemcpcontent.com`—see [Domain handling](/docs/connectors/building/mcp-apps/cross-compatibility#domain-handling) to compute the hash for your server URL. Configure your infrastructure to allow requests whose `Origin` matches `*.claudemcpcontent.com` and return a corresponding `Access-Control-Allow-Origin` header.

<Note>This applies to requests your app makes directly from the user's device—loading bundles, images, or calling your own API from client-side code. MCP tool calls are proxied through Claude's backend and egress from Anthropic's published IP ranges, not the user's device.</Note>

## Problem: ui.domain validation fails

Setting [`_meta.ui.domain`](https://modelcontextprotocol.github.io/ext-apps/api/interfaces/app.McpUiResourceMeta.html#domain) on your resource opts your app into a stable sandbox origin, which you need if your app runs its own OAuth flow. Claude validates the value against your connector URL and shows an `Invalid ui.domain format` or `ui.domain mismatch` error instead of rendering the app when validation fails.

The value must be exactly `{hash}.claudemcpcontent.com`, where `{hash}` is the first 32 hexadecimal characters of the SHA-256 digest of your full connector URL. Compute it by running this command with your own URL:

```shell theme={null}
node -e 'const yourServerUrl = "https://example.com/mcp"; console.log(require("crypto").createHash("sha256").update(yourServerUrl).digest("hex").slice(0,32) + ".claudemcpcontent.com")'
```

Common causes of a mismatch:

* **The URL you hashed differs from the URL Claude connects to.** The hash covers the full URL string including scheme, path, and any trailing slash, so `https://example.com/mcp` and `https://example.com/mcp/` produce different values. Hash the exact URL configured in **Customize > Connectors**.
* **The connector is local (stdio).** Local connectors have no URL to hash, so `ui.domain` is not available for them. Remove the field, or deploy the server as a remote connector to use a stable origin.

See [Domain handling](/docs/connectors/building/mcp-apps/cross-compatibility#domain-handling) for how the origin is used across platforms.
