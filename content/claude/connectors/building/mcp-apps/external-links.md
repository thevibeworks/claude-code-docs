> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Opening external links from MCP Apps

> How Claude handles ui/open-link requests, and how directory connectors can allowlist destinations to skip the confirmation modal

When your MCP App sends a `ui/open-link` request, Claude shows an "Open external link" confirmation modal before navigating. This protects users from being silently redirected by an embedded app.

Directory connectors can declare a set of trusted destinations that open immediately without the modal. Custom connectors and locally configured servers always show the modal.

## Default behavior

A `ui/open-link` request displays a confirmation modal showing the destination URL. The link opens in a new tab when the user confirms; the request resolves as cancelled if they dismiss the modal.

## Allowlisting link destinations

If your connector is published in the [Connectors Directory](/docs/connectors/directory), you can declare destinations that skip the modal. Provide them in the **Allowed link URIs** field when you [submit](/docs/connectors/building/submission) or update your directory listing.

Each entry must be one of two shapes:

| Entry shape       | Example                         | Matches                                                                                                                                                               |
| ----------------- | ------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| HTTPS origin      | `https://docs.example.com`      | Any `https://` URL whose hostname is exactly `docs.example.com` (case-insensitive). Subdomains do not match implicitly; list each one you need. Port is not compared. |
| Custom URI scheme | `example-app` or `example-app:` | Any URL with the scheme `example-app:`, typically a deep link into your native mobile or desktop app.                                                                 |

Entries that do not fit one of these shapes are ignored. This includes bare hostnames such as `example.com`, `http://` origins, and malformed values.

### Example

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

* `https://blog.example.com` (subdomain not listed)
* `http://example.com` (not HTTPS)
* `https://example.com.attacker.net` (different hostname)

### Restrictions on custom schemes

A custom-scheme entry must name a scheme your application registers and owns. Entries that name a generic, browser-internal, or platform-reserved scheme are rejected. This includes `http`, `https`, `file`, `data`, `javascript`, `blob`, `mailto`, `tel`, `sms`, `intent`, `android-app`, browser-extension schemes, and Windows shell schemes such as `search-ms` and `shell`.

## User-activation requirement

The modal is bypassed only when the `ui/open-link` request follows a real user gesture in your app, such as a button click.

If your app sends `ui/open-link` without a preceding gesture (programmatically, on a timer, or after the browser's activation window has expired), the modal is shown so the user's confirmation click supplies the gesture the browser requires to open a new tab.

<Note>
  A bypassed `ui/open-link` request resolves successfully once the open is attempted; it does not indicate whether the browser actually opened the tab. Do not treat the response as confirmation that the user reached the destination.
</Note>

## Design for the modal

Even with an allowlist configured, your app should remain usable when the modal appears:

* Custom and local connectors always show the modal. Your app may run outside the directory during development or in self-hosted deployments.
* Destinations not on your allowlist, or added since your last published directory update, show the modal.
* Requests without user activation show the modal.

Provide enough context in your UI that the destination URL shown in the modal is recognizable to the user.
