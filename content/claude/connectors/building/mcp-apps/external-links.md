> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Open external links from MCP Apps

> Declare allowed link destinations so ui/open-link requests from your directory connector's MCP App open without Claude's confirmation modal.

When your MCP App sends a `ui/open-link` request, Claude shows an **Open external link** confirmation modal before navigating. The modal protects users from being silently redirected by an embedded app.

If your connector is published in the [Connectors Directory](/docs/connectors/directory), you can declare a set of trusted destinations that open immediately without the modal. Custom connectors and locally configured servers always show it. To skip the modal for a directory connector, [allowlist your destinations](#allowlist-link-destinations) and send each request after a [real user gesture](#user-activation-requirement), then [design your app](#design-for-the-modal) for the cases where the modal still appears.

## Default link behavior

A `ui/open-link` request displays a confirmation modal showing the destination URL. If the user confirms, the link opens in a new tab. If they dismiss the modal, the request resolves as cancelled.

## Allowlist link destinations

A directory connector declares the destinations that skip the modal in its directory listing. Provide them in the **Allowed link URIs** field when you [submit](/docs/connectors/building/submission#allowed-link-uris) or update your listing.

Each entry must be an HTTPS origin or a custom URI scheme:

| Entry shape       | Example                         | Matches                                                                                                                                                               |
| ----------------- | ------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| HTTPS origin      | `https://docs.example.com`      | Any `https://` URL whose hostname is exactly `docs.example.com`, case-insensitive. Subdomains don't match implicitly, so list each one you need. Port isn't compared. |
| Custom URI scheme | `example-app` or `example-app:` | Any URL with the scheme `example-app:`, typically a deep link into your native mobile or desktop app.                                                                 |

Entries that don't fit one of these shapes are ignored. This includes bare hostnames such as `example.com`, `http://` origins, and malformed values.

### Allowlist example

Given the following allowlist:

```text theme={null}
https://example.com
https://docs.example.com
example-app
```

These destinations open immediately:

* `https://example.com/pricing`
* `https://docs.example.com/getting-started?ref=claude`
* `example-app://open/project/123`

These destinations still show the confirmation modal:

* `https://blog.example.com`, because the subdomain isn't listed
* `http://example.com`, because it isn't HTTPS
* `https://example.com.attacker.net`, because the hostname is different

### Restrictions on custom schemes

A custom-scheme entry must name a scheme your application registers and owns. Entries that name a generic, browser-internal, or platform-reserved scheme are rejected. This includes `http`, `https`, `file`, `data`, `javascript`, `blob`, `mailto`, `tel`, `sms`, `intent`, `android-app`, browser-extension schemes, and Windows shell schemes such as `search-ms` and `shell`.

## User-activation requirement

Claude bypasses the modal only when the `ui/open-link` request follows a real user gesture in your app, such as a button click.

If your app sends `ui/open-link` without a preceding gesture, for example programmatically, on a timer, or after the browser's activation window has expired, Claude shows the modal so the user's confirmation click supplies the gesture the browser requires to open a new tab.

<Note>
  A bypassed `ui/open-link` request resolves successfully once the open is attempted. It doesn't indicate whether the browser actually opened the tab, so don't treat the response as confirmation that the user reached the destination.
</Note>

## Design for the modal

Even with an allowlist configured, the modal still appears in some cases, so your app should remain usable when it does:

* Custom and local connectors always show the modal, and your app may run outside the directory during development or in self-hosted deployments
* Destinations not on your allowlist, or added since your last published directory update, show the modal
* Requests without user activation show the modal

Provide enough context in your UI that the destination URL shown in the modal is recognizable to the user.

## Next steps

* [Submit a connector](/docs/connectors/building/submission#allowed-link-uris): where the **Allowed link URIs** field fits in your directory submission
* [Design guidelines](/docs/connectors/building/mcp-apps/design-guidelines#interaction-patterns): which interactions belong in your app and which belong in chat
* [Troubleshoot MCP Apps](/docs/connectors/building/mcp-apps/troubleshooting): developer tools for inspecting your app's requests
