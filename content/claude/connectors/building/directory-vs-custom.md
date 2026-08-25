> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Directory connectors vs custom connectors

> Understand the difference between directory-listed and custom connectors

Directory connectors and custom connectors run on the **same MCP infrastructure**. The runtime, transport, authentication, and tool-calling code paths are identical. The difference is review, discoverability, and distribution.

|                                                                                | Directory connector                          | Custom connector                                           |
| ------------------------------------------------------------------------------ | -------------------------------------------- | ---------------------------------------------------------- |
| **Runtime**                                                                    | Same                                         | Same                                                       |
| **Anthropic review**                                                           | Yes                                          | No                                                         |
| **In-product discovery**                                                       | Browse, search, Suggested Connectors         | None                                                       |
| **Distribution**                                                               | [Directory link](#share-an-install-link)     | [Install link](#share-an-install-link) or manual URL entry |
| **Anthropic-held client credentials**                                          | Available                                    | Not available                                              |
| **[External link](/docs/connectors/building/mcp-apps/external-links) confirmation** | Can allowlist destinations to skip the modal | Always shows the modal                                     |
| **Appears as**                                                                 | Named card with logo                         | "Custom"                                                   |

For what directory and custom connectors look like to a Claude user, including the Verified and Community labels, see [connector verification](/docs/connectors/verification).

## Share an install link

Both directory and custom connectors have a URL you can share from your own documentation, a "Connect to Claude" button, or an onboarding email.

### Directory connectors

After publication, your connector has a permanent listing URL based on its slug:

```text theme={null}
https://claude.ai/directory/connectors/SLUG
```

For example, `https://claude.ai/directory/connectors/dovetail` opens the Dovetail listing with its description, screenshots, and a **Connect** button. You receive your slug when your submission is approved, and it [cannot change afterward](/docs/connectors/building/after-publishing#slugs-are-permanent).

### Custom connectors

For a connector that is not in the directory, link to the **Add custom connector** dialog with the name and URL prefilled:

```text theme={null}
https://claude.ai/customize/connectors?modal=add-custom-connector&connectorName=NAME&connectorUrl=ENCODED_URL
```

| Parameter       | Description                                                                                                 |
| --------------- | ----------------------------------------------------------------------------------------------------------- |
| `modal`         | Must be `add-custom-connector`.                                                                             |
| `connectorName` | Display name shown to the user.                                                                             |
| `connectorUrl`  | Your MCP server URL, [percent-encoded](https://developer.mozilla.org/en-US/docs/Glossary/Percent-encoding). |

For example, an install link for a server at `https://mcp.example.com/` looks like this:

```text theme={null}
https://claude.ai/customize/connectors?modal=add-custom-connector&connectorName=Example&connectorUrl=https%3A%2F%2Fmcp.example.com%2F
```

When a user follows the link, claude.ai opens the dialog with the name and URL prefilled and shows a notice that the values came from an external link. The user reviews the values and confirms before anything is added. If the user is signed out, they are prompted to sign in first and then land on the prefilled dialog.

<Note>
  Install links only prefill the form. They do not bypass review by the user, and they do not grant your server any permissions the user has not confirmed.
</Note>

Organization administrators can use the same parameters on the admin path to prefill the org-wide connector dialog:

```text theme={null}
https://claude.ai/admin-settings/connectors?modal=add-custom-connector&connectorName=NAME&connectorUrl=ENCODED_URL
```

## Suggested Connectors

Directory connectors are eligible for **Suggested Connectors**—Claude can recommend your connector in-chat when it's relevant to the user's task. Custom connectors are never suggested. Every directory entry is automatically eligible; there is no separate opt-in.

## Use both: directory plus elevated custom

A supported pattern is to list a connector in the directory with safe, broadly-applicable defaults, **and** provide enterprise customers a separate URL to add as a custom connector with elevated permissions or tenant-specific configuration. Document both paths in your own product docs.

## Per-tenant URLs

If your server URL varies per tenant (for example, `{tenant}.mcp.example.com`), this is typically handled either as separate per-tenant directory entries or via the [`custom_connection`](/docs/connectors/building/authentication#supported-authentication-types) authentication type, where users supply their tenant-specific URL at connection time. `custom_connection` is enabled per partner—email `mcp-review@anthropic.com` to request it. The directory does not currently template a single entry across tenant subdomains.

## What the directory is not

The Anthropic Directory is independent of the open [MCP Registry](https://registry.modelcontextprotocol.io) and the `modelcontextprotocol/servers` GitHub repository. Publishing to those does **not** surface your server in Claude. Submit through the [directory submission form](/docs/connectors/building/submission) to appear in Claude products.
