> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Embed a website in an MCP App

> Embed your own website in an MCP App. Declare its origin in frameDomains, check whether it loads for your connector, and set your site's frame-ancestors header.

An embedded site is a website that your [MCP App](https://claude.com/docs/connectors/building/mcp-apps/getting-started.md) loads in an `<iframe>` inside its view. A view is one rendered instance of your app's UI in Claude. For example, you can show your product's own editor or dashboard in a view.

This page is for developers who have a working MCP App in Claude, served by a remote MCP server.

> [!NOTE]
>
> These cases are covered on other pages:
>
> * **Opening a site in a new tab instead**: see [Open external links from MCP Apps](https://claude.com/docs/connectors/building/mcp-apps/external-links.md)
> * **Building your first MCP App**: see [Add an interactive UI to your MCP server](https://claude.com/docs/connectors/building/mcp-apps/quickstart.md)

You declare your site's origin, and Claude has to allow that origin for your connector. Before you build, check these points:

* **Where sites load**: Claude applies different rules to directory connectors and custom connectors, so start with [where embedded sites load](#where-embedded-sites-load)
* **Device features**: check [which device features your connector's views lose](#device-features-in-views-that-embed-sites), such as the camera

## Where embedded sites load

Claude has to allow a site's origin for your connector before the site loads.

* **Directory connector**: a connector that has a listing in the [Connectors Directory](https://claude.com/docs/connectors/directory.md)
* **Custom connector**: a connector that a user adds to Claude by URL

| Your connector | When a site loads |
| - | - |
| Directory connector with a [Verified](https://claude.com/docs/connectors/verification.md#verified) listing | Only when the listing allows the site's origin |
| Directory connector with a [Community](https://claude.com/docs/connectors/verification.md#community) listing | Claude blocks the origin |
| Custom connector | Only after the user allows the origin in a conversation. Available to a [limited set of organizations](#availability-of-embedded-sites-for-custom-connectors), and not in every conversation. |
| Local server | Claude blocks the origin. A server on your own machine that Claude reaches through a [tunnel URL](https://claude.com/docs/connectors/building/testing.md#test-a-local-server) is a custom connector. |

### Allowed origins in a directory connector

For a directory connector, the Verified listing has to allow each origin. If you [declare a new origin](#declare-the-origins-that-a-view-embeds), it can't load until the listing allows it as well. For how a listing becomes Verified, see [Connector verification](https://claude.com/docs/connectors/verification.md#list-your-own-connector).

When Claude blocks an origin for a directory connector, the view opens and the `<iframe>` doesn't show the site. Claude shows no message, so [show a fallback in the view](#read-the-allowed-origins-in-the-view).

### Allowed origins in a custom connector

Where embedded sites are available for custom connectors, Claude lists the origins that you declare for the view and asks the user to allow them.

For embedded sites, a connector counts as custom when a user added it by URL and its address matches no directory listing. Check these details of your connector:

* **Characters in the path**: use a lower-case path without `%`, `;`, or `//`. If the path contains a capital letter or one of those characters, the connector doesn't count as custom, and Claude blocks its origins.
* **Query string**: to test a new build of a listed connector, serve the build at its own address. Claude doesn't use the query string when it matches an address to a listing.
* **Server URL that matches a listing**: Claude treats the connector as that directory connector. A site that loaded while you tested is blocked under a [Community](https://claude.com/docs/connectors/verification.md#community) listing.
* **Connector added many months ago**: the connector may not count as custom. If Claude doesn't ask you to allow the origins, remove the connector and add it again.

### Availability of embedded sites for custom connectors

For custom connectors, embedded sites are available to a limited set of organizations, and not in every conversation. Where they aren't available, expect this behavior:

* Claude blocks the origins, whatever the user allows
* Claude usually doesn't ask the user to allow the origins
* The view opens without the site

Keep a [fallback in the view](#read-the-allowed-origins-in-the-view) for these conversations.

To check your own organization, [test with a custom connector](#test-embedded-sites-with-a-custom-connector). You can't tell from your own organization's result what people in other organizations see.

## Declare the origins that a view embeds

On your server, declare each origin that you put in an `<iframe>` in the view:

1. Add one entry for each origin to [`_meta.ui.csp.frameDomains`](https://modelcontextprotocol.github.io/ext-apps/api/interfaces/app.McpUiResourceCsp.html#framedomains) on the view's `ui://` resource
2. Put `_meta` on the content item that your `resources/read` handler returns. The quickstart's [`resourceDomains` declaration](https://claude.com/docs/connectors/building/mcp-apps/quickstart#add-the-ui-to-the-tool) is in the same place.

This `_meta` object declares one origin:

```json theme={null}
{
  "_meta": {
    "ui": {
      "csp": {
        "frameDomains": ["https://editor.example.com"]
      }
    }
  }
}
```

Put the `_meta.ui` fields `csp`, `domain`, and `permissions` together on the content item. If you set `_meta.ui` on the content item, Claude ignores `_meta.ui` on the `resources/list` entry.

### Accepted forms for a `frameDomains` entry

Write each entry as an `https` origin in one of three forms:

| Form | Example | What the entry matches |
| - | - | - |
| Exact origin | `https://editor.example.com` | That host on the default HTTPS port |
| Origin with a port | `https://editor.example.com:8443` | That host on that port |
| Subdomain wildcard | `https://*.example.com` | Hosts below `example.com`, at any depth |

* You can also add a port to a wildcard entry, such as `https://*.example.com:8443`
* To embed `example.com` itself, add a separate `https://example.com` entry. A wildcard entry doesn't match that host.
* Omit the path and the trailing slash
* Write an internationalized host name in its `xn--` form

If you write an entry in any other form, Claude treats it as undeclared and still applies the remaining entries.

### Hosts that Claude refuses in `frameDomains`

Claude refuses some hosts in any form. Examples are:

* Anthropic's own domains
* IP addresses
* Private-network names, such as `app.internal`
* Wildcards over a suffix that unrelated parties share, such as `https://*.co.uk`

### Wildcard entries in a directory connector

For a directory connector, compare your wildcard entry with the origins that the listing allows:

* **The listing has the same wildcard or a wider one**: your entry matches all the hosts below the domain
* **The listing is narrower**: your entry matches the listed origins that the wildcard includes

## Read the allowed origins in the view

To see which origins Claude allowed for a view, read [`app.getHostCapabilities()?.sandbox?.csp?.frameDomains`](https://modelcontextprotocol.github.io/ext-apps/api/classes/app.App.html#gethostcapabilities) in the view's script after `app.connect()` resolves.

Choose what the view shows from the list that you read:

* **The list is empty, or it doesn't cover your site's origin**: show a fallback, such as a button that sends [`ui/open-link`](https://claude.com/docs/connectors/building/mcp-apps/external-links)
* **The list is missing**: Claude hasn't reported what it allowed. Load the `<iframe>`, and keep the fallback on screen.

Don't treat your declaration as a limit on what a view can embed. The reported list can include origins that the listing allows and that you didn't declare for the view.

Declare every origin that you embed anyway, because Claude can restrict a view to the origins that you declare for it.

## Allow Claude to frame your site

If your site restricts which pages can frame it, allow two origins in its response header: `https://claude.ai` and your connector's sandbox host.

The sandbox host serves the view and is a subdomain of `claudemcpcontent.com`.

1. On your server, set `ui.domain` on the view's `ui://` resource. Without `ui.domain`, the sandbox host differs between conversations. To compute the value, see [Set `ui.domain` for Claude](https://claude.com/docs/connectors/building/mcp-apps/getting-started#set-ui-domain-for-claude).
2. On your site, add both origins to the `frame-ancestors` directive of the `Content-Security-Policy` header

This response header from the site allows both origins. Replace `c3d80a4ed901ee05b21755a88273b4a4.claudemcpcontent.com` with your connector's own sandbox host:

```text theme={null}
Content-Security-Policy: frame-ancestors https://c3d80a4ed901ee05b21755a88273b4a4.claudemcpcontent.com https://claude.ai
```

The site renders in the view once the [`frameDomains` list that Claude reports to the view](#read-the-allowed-origins-in-the-view) covers the site's origin.

Browsers test `frame-ancestors` against every frame above the site, so the site doesn't load if either entry is missing.

> [!WARNING]
>
> List only the exact sandbox host. If you list a wildcard such as `https://*.claudemcpcontent.com`, the MCP Apps of other connectors can frame your site.

## Test embedded sites with a custom connector

To try a site before your connector has a listing, add your server to Claude as a custom connector.

For custom connectors, embedded sites are available to a [limited set of organizations](#availability-of-embedded-sites-for-custom-connectors), and not in every conversation.

1. [Declare the origin](#declare-the-origins-that-a-view-embeds)
2. [Allow Claude to frame your site](#allow-claude-to-frame-your-site). [Compute the sandbox host](https://claude.com/docs/connectors/building/mcp-apps/getting-started.md#set-ui-domain-for-claude) for the address that you test with, because the host derives from the server URL.
3. [Add your server to Claude as a custom connector](https://claude.com/docs/connectors/building/testing.md#test-in-claude-as-a-custom-connector)
4. In Claude on the web, start a conversation with the [unified Claude experience](https://support.claude.com/en/articles/16761823-claude-cowork-and-chat-are-one-claude), which combines chat and Cowork. If the message box offers a choice of **Chat** or **Cowork**, your account doesn't have it.
5. Ask Claude to open the view, and name your connector in the message
6. Allow the origins. Claude lists them in one of these places:
   * In the approval request for the tool that opens the view.
   * In a review that you open from a line beside the view. If the permission setting in the message box is **Auto**, Claude can open the view without asking, so use the review.
7. Confirm that the site renders in the view

After you allow the origins, each one appears in `app.getHostCapabilities()?.sandbox?.csp?.frameDomains`. A view that opened before you allowed them receives an empty list.

On Team and Enterprise plans, an Owner or Primary Owner controls the unified Claude experience with the **Chat and Cowork unified** setting in [**Organization settings > Capabilities**](https://claude.ai/admin-settings/capabilities).

### Check whether your organization has access to embedded sites

To see whether embedded sites are available for custom connectors where the view opened, read the [console line that names `frameDomains`](#console-line-names-framedomains).

After you follow the [test steps](#test-embedded-sites-with-a-custom-connector), your organization may not have access if all of these are true:

* Your connector [counts as custom](#allowed-origins-in-a-custom-connector)
* Claude didn't ask about the origins, in the approval request or beside the view
* The view opens without the site

### Limits on origins in a custom connector

* **All or none**: the view receives every origin that you declare in an accepted form, or none of them
* **Repeated requests**: expect Claude to ask again, for example in a new conversation, or when you declare an origin that the user hasn't seen listed. Keep the list of origins short and stable.
* **Claude's own check of the origins**: if the origins don't pass the check, the view doesn't open, and Claude shows a message in its place. If a single origin is refused, the whole view doesn't open. Delete that origin from `frameDomains`.

## Design your site for the iframe sandbox

An embedded site inherits the sandbox of the view around it, and the browser treats the site as a third-party frame.

* **Pop-ups and new tabs**: `window.open()` and `target="_blank"` links don't open. To open a link:
  1. Post a message from the site to the view.
  2. In the view's script, verify `event.origin` before you send [`ui/open-link`](https://claude.com/docs/connectors/building/mcp-apps/external-links).
* **Dialogs**: `alert()`, `prompt()`, and `print()` have no effect. `confirm()` returns `false`. Build dialogs into the page.
* **Downloads**: a link to a file doesn't download the file
* **Navigation**: the site can navigate its own frame and submit forms to its own origin. The site can't navigate the Claude page.
* **Redirects**: for a redirect in the frame, the destination and each origin that the redirect passes through must be origins that Claude allows

### Sessions and cookies in an embedded site

Claude passes no session to the site, and a call to `document.requestStorageAccess()` is rejected. To keep a session inside the frame:

* Set [`ui.domain`](https://claude.com/docs/connectors/building/mcp-apps/getting-started#set-ui-domain-for-claude) on the view's `ui://` resource, so that the site can use `localStorage` in the frame, and cookies in browsers that allow cookies in embedded sites
* Set the session cookie's attributes to `SameSite=None; Secure; Partitioned`
* Don't depend on a session from another tab

### Sign a user in to an embedded site

To sign a user in, pass a token from your server to the site through the view:

1. On your server, add a tool that returns a short-lived, single-use token
2. Set the tool's `_meta.ui.visibility` to `["app"]`, so that Claude can't call the tool
3. In the view's script, call the tool with [`app.callServerTool()`](https://modelcontextprotocol.github.io/ext-apps/api/classes/app.App.html#callservertool)
4. From the view, send the token to the frame with `postMessage`, and set the target origin to the site's exact origin
5. On the site, exchange the token for a session

If your sign-in pages can be framed, you can show a sign-in form inside the frame instead.

## Device features in views that embed sites

A view can't use the camera, the microphone, location, or clipboard write when Claude allows an origin for it. The sites that the view embeds can't use them either. The view loses these features even if you request them in `_meta.ui.permissions`.

Plan for other views to lose the same features, including views that embed nothing:

* **Directory connector**: when the listing allows an origin, plan for the connector's other views to lose them
* **Custom connector**: where [embedded sites are available for custom connectors](#availability-of-embedded-sites-for-custom-connectors), plan for every view of the connector to lose them

To see which features Claude granted a view, read `app.getHostCapabilities()?.sandbox?.permissions` in the view's script after `app.connect()` resolves. Each key is a granted feature.

Also plan for `Element.requestFullscreen()` to fail, in views and in embedded sites. Don't depend on a video player's full-screen button.

## Debug an embedded site that fails to load

When a view opens without its site, open the browser's developer console on the Claude page and match the message to its cause. In a Claude app, open the console from the [developer tools](https://claude.com/docs/connectors/building/mcp-apps/troubleshooting.md#open-developer-tools).

### Content Security Policy error names `frame-src`

Claude didn't allow the origin for this view, and your site receives no request. Check each of these:

* The entry has an [accepted form](#accepted-forms-for-a-framedomains-entry)
* The `_meta` object is [on the content item](#declare-the-origins-that-a-view-embeds)
* Claude [allows origins for your kind of connector](#where-embedded-sites-load)

### Content Security Policy error names `frame-ancestors`

Your site's header doesn't include the sandbox host or `https://claude.ai`, or the view has no fixed sandbox host. Follow the steps in [Allow Claude to frame your site](#allow-claude-to-frame-your-site).

### Console error names `X-Frame-Options`

Your site sends `DENY` or `SAMEORIGIN` in `X-Frame-Options`, and it sends no `frame-ancestors` directive. Send a [`frame-ancestors` directive](#allow-claude-to-frame-your-site) that lists the sandbox host and `https://claude.ai`. When a browser receives both headers, it obeys `frame-ancestors`.

### Console line names `frameDomains`

Look for a console line that begins with `[mcp-ext-apps-host]` and names `frameDomains`. In that line, Claude reports what it did with the origins that you declared. If the console has no such line, don't conclude that Claude allowed the origin.

For a custom connector, use the wording of the line to identify your case:

* `was opened without the sites its resource declares`: embedded sites are available for the connector in that conversation. Either the origins weren't allowed, or they didn't pass Claude's own check.
* `Not among the sites that Claude allows this connector to show`: embedded sites aren't available for custom connectors where the view opened, or the connector [doesn't count as custom](#allowed-origins-in-a-custom-connector)

Ignore errors such as `Unrecognized Content-Security-Policy directive 'webrtc'.`, which come from Claude's own frames.

## Next steps

* [Show your MCP App in the side panel or full screen](https://claude.com/docs/connectors/building/mcp-apps/display-modes.md): give the embedded site more room than the conversation offers
* [Design guidelines](https://claude.com/docs/connectors/building/mcp-apps/design-guidelines.md#content-security-policy): declare the other `_meta.ui.csp` fields, for the requests and assets that the view itself loads
