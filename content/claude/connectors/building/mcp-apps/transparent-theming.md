> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Blend your MCP App with Claude's theme

> Make your widget background transparent and style it with Claude's style variables

Claude renders MCP Apps inside a sandboxed iframe, and every frame between your widget and the chat surface already has a transparent background, so the conversation can show through. When you leave your own background transparent and style text and borders with the host's [style variables](/docs/connectors/building/mcp-apps/design-guidelines#style-variables), your app looks like part of the conversation rather than an embedded box, and it follows the user's light or dark mode automatically.

The snippets on this page assume you have registered a UI resource and created an `App` instance from `@modelcontextprotocol/ext-apps`. See the [SDK Quickstart](https://modelcontextprotocol.github.io/ext-apps/api/documents/Quickstart.html) if you haven't.

## Let the host background show through

Three settings on your side keep the transparency intact.

### Don't paint a body background

Any opaque background on `<html>` or `<body>` hides the chat surface behind it. Explicitly set both to `transparent`:

```css theme={null}
html,
body {
  margin: 0;
  background: transparent;
}
```

### Declare `color-scheme` in your document head

Browsers give iframe documents an opaque canvas backdrop (white in light mode, near-black in dark mode) when the iframe's [`color-scheme`](https://developer.mozilla.org/docs/Web/CSS/color-scheme) differs from the embedding page. Declaring both schemes opts your document into whichever mode the host is in, so the browser drops the backdrop and makes the CSS [`light-dark()`](https://developer.mozilla.org/docs/Web/CSS/color_value/light-dark) values in Claude's tokens resolve correctly:

```html theme={null}
<meta name="color-scheme" content="light dark" />
```

### Request a borderless frame

Set [`prefersBorder: false`](https://modelcontextprotocol.github.io/ext-apps/api/interfaces/app.McpUiResourceMeta.html#prefersborder) in your UI resource's [`_meta.ui`](https://modelcontextprotocol.github.io/ext-apps/api/interfaces/app.McpUiResourceMeta.html) object so the host doesn't wrap your widget in its own bordered card. Claude web's default is already borderless, but other hosts differ, so being explicit keeps your app portable. Register the resource with [`registerAppResource`](https://modelcontextprotocol.github.io/ext-apps/api/functions/server-helpers.registerAppResource.html):

```ts theme={null}
import {
  registerAppResource,
  RESOURCE_MIME_TYPE,
} from "@modelcontextprotocol/ext-apps/server";

registerAppResource(server, "My Widget", "ui://my-app/widget.html", {}, async () => ({
  contents: [
    {
      uri: "ui://my-app/widget.html",
      mimeType: RESOURCE_MIME_TYPE,
      text: widgetHtml, // the bundled HTML string of your widget; see the SDK Quickstart
      _meta: {
        ui: {
          prefersBorder: false,
          // lets applyHostFonts load Anthropic Sans; see "Allow the host font origin in your CSP"
          csp: { resourceDomains: ["https://assets.claude.ai"] },
        },
      },
    },
  ],
}));
```

## Apply the host's style variables

Claude passes a [`hostContext`](https://modelcontextprotocol.github.io/ext-apps/api/interfaces/app.McpUiHostContext.html) object to your widget during the [`connect()`](https://modelcontextprotocol.github.io/ext-apps/api/classes/app.App.html#connect) handshake. The fields relevant to theming are:

| Field              | Contents                                                                                                                                                   |
| :----------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `theme`            | `"light"` or `"dark"`                                                                                                                                      |
| `styles.variables` | CSS custom properties: `--color-background-*`, `--color-text-*`, `--color-border-*`, `--color-ring-*`, `--font-*`, `--border-radius-*`, `--border-width-*` |
| `styles.css.fonts` | `@font-face` rules for Anthropic Sans, served from `https://assets.claude.ai`                                                                              |

The [Style variables](/docs/connectors/building/mcp-apps/design-guidelines#style-variables) section of the design guidelines lists every variable and its light- and dark-mode value.

### Read `hostContext` and listen for changes

The [`App`](https://modelcontextprotocol.github.io/ext-apps/api/classes/app.App.html) class exposes the initial context via [`getHostContext()`](https://modelcontextprotocol.github.io/ext-apps/api/classes/app.App.html#gethostcontext) once `connect()` resolves, and delivers subsequent updates (such as the user toggling dark mode) through the [`hostcontextchanged`](https://modelcontextprotocol.github.io/ext-apps/api/types/app.AppEventMap.html) event. Register the listener before you connect so you don't miss an early update.

The SDK provides three helpers that do the DOM work for you, plus React hooks that wrap them:

* [`applyDocumentTheme(theme)`](https://modelcontextprotocol.github.io/ext-apps/api/functions/app.applyDocumentTheme.html) sets `<html data-theme>` and the root `color-scheme`, so `[data-theme="dark"]` selectors and `light-dark()` values resolve correctly.
* [`applyHostStyleVariables(variables)`](https://modelcontextprotocol.github.io/ext-apps/api/functions/app.applyHostStyleVariables.html) writes every entry in `styles.variables` onto `:root` as a CSS custom property.
* [`applyHostFonts(fontCss)`](https://modelcontextprotocol.github.io/ext-apps/api/functions/app.applyHostFonts.html) injects the host's `@font-face` rules once.
* [`useApp(options)`](https://modelcontextprotocol.github.io/ext-apps/api/functions/_modelcontextprotocol_ext-apps_react.useApp.html) creates and connects the `App` instance for you in React.
* [`useHostStyles(app, hostContext)`](https://modelcontextprotocol.github.io/ext-apps/api/functions/_modelcontextprotocol_ext-apps_react.useHostStyles.html) applies all of the above and re-applies on `hostcontextchanged`.

Keep the `<meta name="color-scheme">` tag from the previous section even though `applyDocumentTheme` also sets `color-scheme` at runtime. The tag covers the first paint before your script runs and prevents an opaque-backdrop flash.

<CodeGroup>
  ```ts TypeScript theme={null}
  import {
    App,
    applyDocumentTheme,
    applyHostFonts,
    applyHostStyleVariables,
    type McpUiHostContext,
  } from "@modelcontextprotocol/ext-apps";

  function applyHostContext(ctx: Partial<McpUiHostContext>) {
    if (ctx.theme) applyDocumentTheme(ctx.theme);
    if (ctx.styles?.variables) applyHostStyleVariables(ctx.styles.variables);
    if (ctx.styles?.css?.fonts) applyHostFonts(ctx.styles.css.fonts);
  }

  const app = new App({ name: "my-app", version: "1.0.0" });

  // Updates carry only the fields that changed.
  app.addEventListener("hostcontextchanged", (changed) => applyHostContext(changed));

  await app.connect();
  const initial = app.getHostContext();
  if (initial) applyHostContext(initial);
  ```

  ```tsx React theme={null}
  import { useApp, useHostStyles } from "@modelcontextprotocol/ext-apps/react";

  function Widget() {
    const { app } = useApp({
      appInfo: { name: "my-app", version: "1.0.0" },
      capabilities: {},
    });
    // Applies theme + CSS variables + fonts, and re-applies on host-context-changed.
    useHostStyles(app, app?.getHostContext());
    return <div className="card">…</div>;
  }
  ```
</CodeGroup>

### Reference the variables in your CSS

Once the variables are on `:root`, reference them directly. Provide fallbacks so the widget is still readable when rendered outside a host:

```css theme={null}
body {
  font-family: var(--font-sans, system-ui, sans-serif);
  color: var(--color-text-primary, light-dark(#141413, #faf9f5));
}
.card {
  border: var(--border-width-regular, 0.5px) solid var(--color-border-primary);
  border-radius: var(--border-radius-md, 8px);
}
```

<Note>
  Claude's token values use CSS `light-dark()`, so once `applyDocumentTheme` has set the root `color-scheme`, every `--color-*` variable resolves to the right variant without any `[data-theme]` selectors on your side.
</Note>

### Allow the host font origin in your CSP

For `applyHostFonts` to load the `@font-face` files, your resource's [`_meta.ui.csp`](https://modelcontextprotocol.github.io/ext-apps/api/interfaces/app.McpUiResourceMeta.html#csp) allowlist must include `https://assets.claude.ai` in [`resourceDomains`](https://modelcontextprotocol.github.io/ext-apps/api/interfaces/app.McpUiResourceCsp.html#resourcedomains) (shown in the [`registerAppResource` snippet above](#request-a-borderless-frame)). `resourceDomains` also adds the listed origins to `script-src` and `style-src`, so keep it to origins you trust to serve executable code; prefer bundling third-party fonts into your widget rather than allowlisting public CDNs.

## Related topics

* [Design guidelines: Style variables](/docs/connectors/building/mcp-apps/design-guidelines#style-variables) and [Visual design](/docs/connectors/building/mcp-apps/design-guidelines#visual-design) for the full variable palette and usage guidance.
* [SDK API reference](https://modelcontextprotocol.github.io/ext-apps/api/index.html) for `App`, `McpUiHostContext`, and `McpUiResourceMeta`.
