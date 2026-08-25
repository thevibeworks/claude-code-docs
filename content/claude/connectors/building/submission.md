> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Submitting to the Connectors Directory

> Submit your MCP connector to the Connectors Directory

The [Connectors Directory](/docs/connectors/directory) aims to be a collection of high-quality, vetted, and reviewed MCP servers that are helpful and harmless to users. Anyone is welcome to build MCP servers, but only servers meeting the review standards outlined on this page will be included in the directory.

## What you can submit

Developers can submit:

* **Remote MCP servers** — internet-hosted servers that provide tools and data to Claude
* **Desktop extensions** — local MCP servers packaged as [MCP Bundles (MCPB)](https://github.com/modelcontextprotocol/mcpb) for Claude Desktop
* **[MCP Apps](/docs/connectors/building/mcp-apps/getting-started)** — MCP servers that surface interactive UI elements. These have the additional requirement of including screenshots for submission and listing in the directory.

## Before you start

Remote MCP server submissions happen inside Claude.ai, in the [submission portal](https://claude.ai/admin-settings/directory/submissions/new). The portal is part of your organization's settings, so you need:

* **A Team or Enterprise organization.** Organization settings aren't available on individual plans.
* **Directory management access.** By default, only organization Owners and Primary owners can submit and manage directory listings. On Enterprise, an Owner can delegate this to other members by creating a custom role in **Organization settings > Roles** with either the **Directory** permission (directory submissions only) or the **Libraries** permission (broader: it also covers managing the organization's plugins, connectors, and skills), and assigning that role. Team plans don't have custom roles, so on Team this stays with Owners.

Desktop extensions (MCPB) use a separate [submission form](https://clau.de/desktop-extention-submission) and don't require the portal.

## Directory terms & conditions

All servers in the directory must comply with:

* [Anthropic Software Directory Terms](https://support.claude.com/en/articles/13145338-anthropic-software-directory-terms)
* [Anthropic Software Directory Policy](https://support.claude.com/en/articles/13145358-anthropic-software-directory-policy)

By submitting a connector, you also agree to:

* Maintain your connector's security and functionality
* Respond to security issues promptly
* Provide accurate descriptions and documentation

## Submission requirements

All MCP connectors submitted to the directory must meet:

1. **Security**: Meet Anthropic's security standards
2. **Tool annotations**: All tools must include a `title` and the applicable `readOnlyHint` or `destructiveHint`
3. **Authentication**: Use OAuth 2.0 for authenticated services
4. **Privacy Policy**: Local connectors must include privacy policies
5. **Documentation**: Provide clear setup and usage instructions

If your connector opens external links, also provide your [allowed link URIs](#allowed-link-uris) so users aren't prompted to confirm each one.

## Privacy policy requirements

Local connectors must include:

1. "Privacy Policy" section in README.md
2. `privacy_policies` array in manifest.json (manifest\_version 0.2+)
3. HTTPS URLs to privacy policies

The privacy policy must cover:

* Data collection practices
* Usage and storage
* Third-party sharing
* Data retention
* Contact information

<Warning>
  Missing or incomplete privacy policies result in immediate rejection.
</Warning>

## Allowed link URIs

If your connector uses the `ui/open-link` capability to open URLs in the user's browser or native apps, provide the list of link targets your server will request. Claude uses this list to suppress the "Open external link" confirmation prompt for destinations you've declared. Links to any other destination still work—users are simply asked to confirm before the link opens.

Provide each entry in one of two forms:

* **HTTPS origin** — `https://example.com`. Only the scheme and hostname are matched; paths, ports, and query strings are ignored. Subdomains are not implied—list each one (`https://app.example.com`, `https://docs.example.com`).
* **Custom URI scheme** — `myapp:` for deep links into a native app you own (for example, `spotify:` or `notion:`). Only the scheme is matched.

Every origin and scheme you list **must be owned by you** (the submitting organization). You may not list third-party domains or URI schemes registered to apps you don't publish. Entries you don't own will be removed during review.

<Note>
  This field is optional. If omitted, your connector functions normally, but users are shown a confirmation prompt each time it opens a link.
</Note>

## Asset specifications

### Carousel screenshots (MCP Apps)

* **Format:** PNG
* **Width:** at least 1000px
* **Count:** 3–5 images
* **Crop:** to the app response only—**do not include the prompt** in the image
* **Aspect ratio:** any
* **Paired prompts:** provide the prompt text separately for each screenshot
* **Mobile:** no separate mobile assets are required—one batch covers all surfaces
* **Video/GIF:** not accepted

A carousel template is available in the [Anthropic MCP Apps Figma community file](https://www.figma.com/community/file/1597641111449594397/mcp-apps-for-claude).

### Detail card description

You write the detail card description in the submission portal. It is not editable by Anthropic. The disclaimer text shown on connector cards is general and not customizable per partner.

## Review process

Review times vary with queue volume. The submission portal is always open.

After you submit, track your submission's status and read reviewer feedback in the [submissions dashboard](https://claude.ai/admin-settings/directory/submissions). See [Managing your listing](/docs/connectors/building/managing-your-listing) for what's available there, including server health and usage metrics after publication. Email `mcp-review@anthropic.com` for escalations.

Run the [pre-submission checklist](/docs/connectors/building/review-criteria) and, for plugins, `claude plugin validate` before you submit.

## Submit your connector

Ready to submit? Use the path that matches your connector type:

* **Remote MCP servers (including MCP Apps)**: submit through the [submission portal](https://claude.ai/admin-settings/directory/submissions/new) in your organization's settings on Claude.ai. See [Before you start](#before-you-start) for access requirements.
* **Desktop extensions (MCPB)**: use the [desktop extension submission form](https://clau.de/desktop-extention-submission).

Skills are not a standalone submission type—bundle them in a [plugin](/docs/plugins/submit).

### What to expect in the portal

Before you start, have your documentation URL, privacy policy URL, icon, and test account credentials ready, plus carousel screenshots if you're submitting an MCP App (see [asset specifications](#asset-specifications) above).

The portal walks you through the following steps. Your progress saves automatically in your browser as you move between steps, so within a browser session you can jump back to earlier steps without losing work.

<Steps>
  <Step title="Introduction">
    Explains what a directory listing does and doesn't do: inclusion makes your connector discoverable but doesn't change the tools it exposes. The portal accepts remote MCP servers only. Local servers are distributed as [desktop extensions](https://clau.de/desktop-extention-submission) or [plugins](/docs/plugins/submit) instead.
  </Step>

  <Step title="Connection">
    Connect the server you're submitting. You confirm the server URL (must be `https://`), the transport (streamable HTTP or SSE), and whether every user connects to the same URL or different users connect to different URLs.
  </Step>

  <Step title="Tools">
    Your server's tools, prompts, and resources sync automatically from the connected server, grouped by whether their annotations declare them read-only or write (tools without annotations are grouped separately). If any tools are flagged for missing titles or annotations, fix them on your server before submitting.
  </Step>

  <Step title="Listing">
    The public-facing listing: server name (100 characters max), tagline (55 characters max), description (2,000 characters max), one to five categories, documentation URL, privacy policy URL, support contact, icon, and the URL slug for your listing page. The slug is permanent once published.
  </Step>

  <Step title="Use cases">
    Describe the primary use cases, what users need before they can connect (accounts, plans, or other setup), and whether the connector reads data, writes data, or both.
  </Step>

  <Step title="Company">
    Company name and website, plus a primary contact for review updates. The contact name and email are pre-filled from your account.
  </Step>

  <Step title="Authentication">
    How users authenticate: OAuth (with dynamic client registration, client ID metadata documents, or a static client ID held by Anthropic), a custom connection where users supply their own URL or credentials at connection time, or no authentication. See [authentication](/docs/connectors/building/authentication) for which modes are supported out of the box and which need coordination with the review team. If your server starts without authentication and individual tools prompt for it on demand, you can flag that here.
  </Step>

  <Step title="Data handling">
    Whether the underlying API is your own, proxied from a partner with permission, or a third party's you don't control, and whether the connector handles personal health data or sponsored content.
  </Step>

  <Step title="Test & launch">
    Test-account setup and access instructions detailed enough for a reviewer to access your server end to end: every link, credential, and step, including credentials for a fully populated account where relevant. You also confirm you've run every tool yourself, either via MCP Inspector or as a custom connector in Claude.
  </Step>

  <Step title="Compliance">
    Seven policy acknowledgments covering the directory guidelines, first-party API usage, financial transactions, AI media generation, prompt injection, conversation data collection, and public documentation. All seven are required.
  </Step>

  <Step title="Review">
    A final read-through of everything you've entered. Any quality warnings (for example, very short answers) are shown here and shared with the review team alongside your submission. Submit when you're ready.
  </Step>
</Steps>

After you submit, your submission's status and any reviewer feedback appear in the [submissions dashboard](https://claude.ai/admin-settings/directory/submissions). See [Managing your listing](/docs/connectors/building/managing-your-listing).
