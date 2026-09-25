> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Submit a connector to the directory

> Submit a remote MCP server or MCP App to the Connectors Directory through the developer portal: requirements, screenshot specs, and what each step asks for.

You submit a remote MCP server to the [Connectors Directory](/docs/connectors/directory) through the developer portal at [claude.ai/directory/manage](https://claude.ai/directory/manage), where you choose **MCP connector**.

This page is for connector authors who are ready to submit. It starts with a [checklist](#pre-submission-checklist-for-connectors), then covers [where to submit your connector](#choose-where-to-submit-your-connector), the [requirements every submission must meet](#meet-the-submission-requirements), and [what to have ready for each step of the portal](#submit-through-the-developer-portal). [Connector review criteria](/docs/connectors/building/review-criteria) explains what reviewers look for in your tools and server, so read it alongside the checklist.

<Note>
  If you're submitting a plugin rather than a connector, see [Submit a plugin](/docs/plugins/submit) instead.
</Note>

## Pre-submission checklist for connectors

Work through this list before you open the portal. Each item links to where it is explained, and the rest of this page covers the requirements and the portal steps in detail.

* **Your server is remote and reachable over HTTPS**: the portal asks for an `https://` URL. A local server can't be submitted on its own; include it in a [plugin](/docs/plugins/submit) instead
* **Authentication works for Claude's client**: OAuth 2.0 if your tools act on a user's account, or no authentication for public data, as [Authentication for connectors](/docs/connectors/building/authentication) describes. You don't need Verified status or any separate approval for authentication to work
* **Every tool has a `title` and a `readOnlyHint` or `destructiveHint` annotation**: the portal flags tools that are missing them, and [review criteria](/docs/connectors/building/review-criteria#design-tools-that-pass-review) explain how reviewers read tool names and descriptions
* **You've tested it in Claude**: add the server as a [custom connector](/docs/connectors/building/testing#test-in-claude-as-a-custom-connector) and call each tool from a conversation; the portal's **Test & launch** step asks you to confirm this
* **You have the listing materials**: documentation URL, privacy policy URL, support contact, an icon, and for an [MCP App](/docs/connectors/building/mcp-apps/getting-started) the [carousel screenshots](#carousel-screenshots-for-mcp-apps)
* **You have a test account for reviewers**: credentials for a fully populated account, which you enter in the portal and which only reviewers see
* **Your account can submit**: any paid Claude plan. See [who can submit](/docs/directory/publish#confirm-you-can-submit-to-the-directory)
* **If a plugin of yours points at this server, submit the server anyway**: the connector listing gives your organization the server's details, authentication configuration, and dashboard, and lets you pair it with the plugin. See [Submit your plugin, and your MCP server as a connector](/docs/directory/publish#submit-your-plugin-and-your-mcp-server-as-a-connector)

Then open the [developer portal](https://claude.ai/directory/manage), select **Submit new**, and choose **MCP connector**.

## Choose where to submit your connector

A connector submission is an MCP server, and where you submit it depends on whether the server is remote or local:

* **Remote MCP servers**: internet-hosted servers that provide tools and data to Claude. Submit them through the [developer portal](https://claude.ai/directory/manage) and choose **MCP connector**
* **MCP Apps**: remote MCP servers that [surface interactive UI](/docs/connectors/building/mcp-apps/getting-started). Submit them through the portal as remote servers, and include [carousel screenshots](#carousel-screenshots-for-mcp-apps) for the directory listing
* **Local MCP servers**: desktop extension listings in the directory are deprecated, and the directory no longer accepts local servers packaged as [MCP Bundles (MCPB)](/docs/connectors/building/mcpb). To distribute a local server through the directory, include it in a [plugin](/docs/plugins/submit)

Skills aren't a standalone submission type. Bundle them in a [plugin](/docs/plugins/submit).

Anyone on a paid Claude plan can submit through the portal. [Who can submit to the directory](/docs/directory/publish#confirm-you-can-submit-to-the-directory) has the plan, role, and organization requirements, which are the same for connectors and plugins.

## Meet the submission requirements

Every connector in the directory must comply with the directory terms and meet a fixed set of security, annotation, authentication, privacy, and documentation requirements. MCP Apps add screenshot requirements, and connectors that open external links can add an allowlist.

### Directory terms

All servers in the directory must comply with:

* [Anthropic Software Directory Terms](https://support.claude.com/en/articles/13145338-anthropic-software-directory-terms)
* [Anthropic Software Directory Policy](https://support.claude.com/en/articles/13145358-anthropic-software-directory-policy)

By submitting a connector, you also agree to:

* Maintain your connector's security and functionality
* Respond to security issues promptly
* Provide accurate descriptions and documentation

### Requirements for every connector

All MCP connectors submitted to the directory must meet these requirements:

* **Security**: meet Anthropic's security standards
* **Tool annotations**: every tool includes a `title` and the applicable `readOnlyHint` or `destructiveHint`
* **Authentication**: use OAuth 2.0 for authenticated services
* **Privacy policy**: local connectors must include privacy policies
* **Documentation**: provide clear setup and usage instructions

If your connector opens external links, also provide your [allowed link URIs](#allowed-link-uris) so users aren't prompted to confirm each one.

### Privacy policy for local connectors

Local connectors must include:

* A "Privacy Policy" section in `README.md`
* A `privacy_policies` array in `manifest.json`, for `manifest_version` 0.2 and later
* HTTPS URLs to privacy policies

The privacy policy must cover:

* Data collection practices
* Usage and storage
* Third-party sharing
* Data retention
* Contact information

<Warning>
  Missing or incomplete privacy policies result in immediate rejection.
</Warning>

### Allowed link URIs

If your connector uses the `ui/open-link` capability to open URLs in the user's browser or native apps, provide the list of link targets your server will request. Claude uses this list to suppress the **Open external link** confirmation prompt for destinations you've declared. Links to any other destination still work, but users are asked to confirm before the link opens.

The allowed link URIs list is optional. If you omit it, your connector functions normally, and users see a confirmation prompt each time it opens a link.

Provide each entry in one of these forms:

* **HTTPS origin**: `https://example.com`. Only the scheme and hostname are matched, and paths, ports, and query strings are ignored. Subdomains aren't implied, so list each one, such as `https://app.example.com` and `https://docs.example.com`
* **Custom URI scheme**: `myapp:` for deep links into a native app you own. Only the scheme is matched

Every origin and scheme you list must be owned by you, the submitting organization. You may not list third-party domains or URI schemes registered to apps you don't publish. Entries you don't own are removed during review. [Open external links from MCP Apps](/docs/connectors/building/mcp-apps/external-links) explains how Claude matches entries and when the prompt still appears.

### Carousel screenshots for MCP Apps

An MCP App submission includes screenshots for its directory listing carousel. Prepare them to these specifications:

* **Format**: PNG
* **Width**: at least 1000px
* **Count**: 3–5 images
* **Crop**: to the app response only, without the prompt in the image
* **Aspect ratio**: any
* **Paired prompts**: provide the prompt text separately for each screenshot
* **Mobile**: no separate mobile assets are required, and one batch covers all surfaces
* **Video or GIF**: not accepted

A carousel template is available in the [Anthropic MCP Apps Figma community file](https://www.figma.com/community/file/1597641111449594397/mcp-apps-for-claude).

### Detail card description

You write the detail card description in the submission portal, and Anthropic can't edit it. The disclaimer text shown on connector cards is general and not customizable per partner.

## Submit through the developer portal

The developer portal at [claude.ai/directory/manage](https://claude.ai/directory/manage) takes your submission in a series of steps. Before you open it, have these ready:

* Your documentation URL and privacy policy URL
* Your connector's icon
* Test account credentials for reviewers
* Carousel screenshots, if you're submitting an MCP App, per the [screenshot specifications](#carousel-screenshots-for-mcp-apps)

Your progress saves automatically in your browser as you move between steps, so within a browser session you can return to earlier steps without losing work. Each step asks for the following:

<Steps>
  <Step title="Connection">
    Connect the server you're submitting, by pasting its `https://` URL or choosing a custom connector you've already added to Claude. If your users connect to different URLs, select **Users connect to different URLs** and choose **Multiple URLs** or **URL pattern**.
  </Step>

  <Step title="Tools">
    Your server's tools, prompts, and resources sync automatically from the connected server, grouped by whether their annotations declare them read-only or write. If any tools are flagged for missing titles or annotations, fix them on your server before submitting.
  </Step>

  <Step title="Listing">
    The public-facing listing: server name up to 100 characters, one-liner up to 200 characters, description up to 2,000 characters, one to five categories, documentation URL, privacy policy URL, support contact, icon, and the URL slug for your listing page. The slug is permanent once published.
  </Step>

  <Step title="Use cases">
    The primary use cases, what users need before they can connect, such as accounts, plans, or other setup, and whether the connector reads data, writes data, or both.
  </Step>

  <Step title="Company">
    Company name and website, plus a primary contact for review updates.
  </Step>

  <Step title="Authentication">
    How users authenticate: OAuth with dynamic client registration, client ID metadata documents, or Anthropic-held client credentials; a custom connection where users supply their own URL or credentials at connection time; or no authentication. [Authentication](/docs/connectors/building/authentication) covers which modes are supported directly and which need coordination with the review team. If your server starts without authentication and individual tools prompt for it on demand, you can flag that here.

    If you chose **URL pattern** in the Connection step, Anthropic-held client credentials can't be used. If you chose **Multiple URLs**, a custom connection can't be used.
  </Step>

  <Step title="Data handling">
    Whether the underlying API is your own, proxied from a partner with permission, or a third party's you don't control, and whether the connector handles personal health data or sponsored content.
  </Step>

  <Step title="Test & launch">
    Test-account setup and access instructions detailed enough for a reviewer to connect to your server and run its tools: every link, credential, and step, including credentials for a fully populated account where relevant. You also confirm you've run every tool yourself, either through MCP Inspector or as a custom connector in Claude.
  </Step>

  <Step title="Compliance">
    Seven policy acknowledgments covering the directory guidelines, first-party API usage, financial transactions, AI media generation, prompt injection, conversation data collection, and public documentation. All seven are required.
  </Step>

  <Step title="Review and submit">
    Everything you've entered, for a final check before you submit. Any quality warnings, such as very short answers, appear here and are shared with the review team alongside your submission.
  </Step>
</Steps>

## After you submit

Anthropic scans your submission automatically for policy compliance and, by default, lists it as a Community connector with no action from you. Some submissions also get a review from a person, and those review times vary with queue volume. The portal is always open for new submissions. Your submission's status and any reviewer feedback appear in the portal at [claude.ai/directory/manage](https://claude.ai/directory/manage), and [Track your directory submission](/docs/directory/submission-status#mcp-connector-statuses) explains what each status in the portal means. [Manage your directory listing](/docs/connectors/building/managing-your-listing) covers reviewer feedback, listing edits, and the server health and usage metrics you get after publication.

For escalations, email `mcp-review@anthropic.com`.

If a submission is stuck, [Contact Anthropic about a submission](/docs/directory/submission-status#contact-anthropic-about-a-submission) gives the channel for an MCP connector.

## Next steps

* [Manage your directory listing](/docs/connectors/building/managing-your-listing): track review status, respond to reviewer feedback, and edit your listing
* [After publishing](/docs/connectors/building/after-publishing): release updates to your server, and delist
* [Connector verification](/docs/connectors/verification#list-your-own-connector): see how a Community listing becomes Verified and what each label means to users
