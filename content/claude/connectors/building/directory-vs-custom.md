> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Directory connectors vs custom connectors

> Compare directory-listed and custom connectors: Anthropic review, in-product discovery, install links, Suggested Connectors, and per-tenant URL listings.

A directory connector is an MCP server listed in Anthropic's directory after review, and a custom connector is one that a user or an organization Owner adds to Claude by entering its URL. Both run on the same MCP infrastructure: the runtime, transport, authentication, and tool-calling code paths are identical. The difference is review, discoverability, and distribution.

This page is for developers deciding whether to list a server in the directory, distribute it as a custom connector, or do both. It compares the two, shows the install link each one gets, and covers listing patterns for enterprise and multi-tenant servers.

<Note>
  If you want to know what directory and custom connectors look like to a Claude user, including the Verified and Community labels, see [connector verification](/docs/connectors/verification).
</Note>

## Compare directory and custom connectors

Directory and custom connectors differ only in what surrounds the runtime: who reviews the server, how users find it, and which Anthropic-side features it can use.

|                                                                                | Directory connector                          | Custom connector                                           |
| ------------------------------------------------------------------------------ | -------------------------------------------- | ---------------------------------------------------------- |
| **Runtime**                                                                    | Same                                         | Same                                                       |
| **Anthropic review**                                                           | Yes                                          | No                                                         |
| **In-product discovery**                                                       | Browse, search, Suggested Connectors         | None                                                       |
| **Distribution**                                                               | [Directory link](#share-an-install-link)     | [Install link](#share-an-install-link) or manual URL entry |
| **Anthropic-held client credentials**                                          | Available                                    | Not available                                              |
| **[External link](/docs/connectors/building/mcp-apps/external-links) confirmation** | Can allowlist destinations to skip the modal | Always shows the modal                                     |
| **Appears as**                                                                 | Named card with logo                         | **Custom**                                                 |

## Share an install link

Both directory and custom connectors have a URL you can share from your own documentation, a **Connect to Claude** button, or an onboarding email.

### Directory connector listing URL

After publication, your connector has a permanent listing URL based on its slug:

```text theme={null}
https://claude.ai/directory/connectors/SLUG
```

For example, `https://claude.ai/directory/connectors/dovetail` opens the Dovetail listing with its description, screenshots, and a **Connect** button. You receive your slug when your submission is approved, and it [can't change afterward](/docs/connectors/building/after-publishing#directory-listing-urls-are-permanent).

### Custom connector install link

For a connector that isn't in the directory, link to the **Add custom connector** dialog with the name and URL prefilled:

```text theme={null}
https://claude.ai/customize/connectors?modal=add-custom-connector&connectorName=NAME&connectorUrl=ENCODED_URL
```

The link takes these query parameters:

| Parameter       | Description                                                                                                |
| --------------- | ---------------------------------------------------------------------------------------------------------- |
| `modal`         | Must be `add-custom-connector`                                                                             |
| `connectorName` | Display name shown to the user                                                                             |
| `connectorUrl`  | Your MCP server URL, [percent-encoded](https://developer.mozilla.org/en-US/docs/Glossary/Percent-encoding) |

For example, an install link for a server at `https://mcp.example.com/` looks like this:

```text theme={null}
https://claude.ai/customize/connectors?modal=add-custom-connector&connectorName=Example&connectorUrl=https%3A%2F%2Fmcp.example.com%2F
```

When a user follows the link, claude.ai opens the dialog with the name and URL prefilled and shows a notice that the values came from an external link. The user reviews the values and confirms before anything is added. A signed-out user is prompted to sign in first and then sees the prefilled dialog.

<Note>
  Install links only prefill the form. They don't bypass review by the user, and they don't grant your server any permissions the user hasn't confirmed.
</Note>

Organization Owners can use the same parameters on the admin path to prefill the org-wide connector dialog:

```text theme={null}
https://claude.ai/admin-settings/connectors?modal=add-custom-connector&connectorName=NAME&connectorUrl=ENCODED_URL
```

## Understand how listing affects discovery

Only a directory listing makes your connector discoverable inside Claude. Listings elsewhere, including the open MCP Registry, don't.

### Suggested Connectors

Directory connectors are eligible for Suggested Connectors, which means Claude can recommend your connector in-chat when it's relevant to the user's task. Custom connectors are never suggested. Every directory entry is automatically eligible, and there is no separate opt-in.

### The MCP Registry and the Anthropic Directory

The Anthropic Directory is independent of the open [MCP Registry](https://registry.modelcontextprotocol.io) and the `modelcontextprotocol/servers` GitHub repository. Publishing to those doesn't surface your server in Claude. Submit through the [directory submission form](/docs/connectors/building/submission) to appear in Claude products.

## Listing patterns for enterprise and multi-tenant servers

A single directory listing can still serve customers who need elevated permissions or their own server URL.

### Offer a listing and a custom connector

A supported pattern is to list a connector in the directory with safe, broadly applicable defaults, and provide enterprise customers a separate URL to add as a custom connector with elevated permissions or tenant-specific configuration. Document both paths in your own product docs.

### Per-tenant URLs

If your server URL varies per tenant, such as `{tenant}.mcp.example.com`, submit one directory listing with a URL pattern. Each user enters their own URL when they connect. See [Servers with per-customer URLs](/docs/connectors/building/authentication#servers-with-per-customer-urls) for how this choice limits your authentication options.

## Next steps

* [Authentication for connectors](/docs/connectors/building/authentication): the authentication types available to directory and custom connectors
* [Publish to the directory](/docs/directory/publish): who can submit, what review involves, and where to start
* [Add a connector by URL](/docs/connectors/custom/add-unlisted#add-a-connector-by-url): how users and Owners add a custom connector by URL
