> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Moving from Claude for Government Web

> Find answers to the questions agencies ask most often when moving from Claude for Government Web to Claude Desktop.

> **Who this is for:** Administrators and IT staff at an agency that used Claude for Government Web (the web app) and is moving its users to Claude Desktop connected to Claude for Government. If you use Claude but don't administer it, see [Import your data from Claude for Government Web](/docs/government/desktop/import) instead.

This page answers the questions that only come up during the move and links each one to the page with the detail. For anything specific to your agency's agreement, contact your Anthropic representative.

## What the move involves

* **Is there a deadline for the move?** Your Anthropic representative confirms the timeline.
* **Do users need the Claude Desktop app?** Yes. After the move, people use Claude in the Claude Desktop app (Chat, Cowork, and Code), which your IT team deploys, and use the browser only to sign in, view [their account](/docs/government/account/overview), and administer. See [Connect Claude Desktop to Claude for Government](/docs/government/deploy-desktop/configure).
* **What changes for users?** They work in the Claude Desktop app instead of a browser, and conversations, projects, and files are stored on each user's device, so projects aren't shared between people. Administrators can still give everyone in the tenant or in one organization the same skills by adding them as a plugin in the admin portal. See [Data storage and retention](/docs/government/security/security-and-data-handling#data-storage-and-retention), [Chat and Cowork differences](/docs/government/security/security-and-data-handling#chat-and-cowork-differences), and [Skills for administrators](/docs/government/desktop/skills#skills-for-administrators).
* **Does anything carry over from the web app?** Each user can copy their own conversations and projects with the [Claude for Government Web import](/docs/government/desktop/import). Roles and administrative settings aren't copied from the web app, so your administrators set up the admin portal themselves, starting with the [setup wizard](/docs/government/tenant-admin/setup-wizard).
* **What does each user do?** Install or receive Claude Desktop, choose **Sign in with your organization**, and optionally [run the import](/docs/government/desktop/import).

## First sign-ins and the admin portal

* **Where is the admin portal?** In the browser, at your Claude for Government address followed by `/gateway`, not in the Claude Desktop app. See [The three views](/docs/government/overview#the-three-views) for which view each role opens.
* **How does the first administrator sign in, before single sign-on is connected?** On the sign-in page at your Claude for Government address followed by `/gateway`, which can email them a single-use sign-in link. See [Tenant setup wizard](/docs/government/tenant-admin/setup-wizard).
* **How are user accounts created?** At each person's first sign-in through a routing rule, or ahead of time through SCIM. See [Routing rules](/docs/government/tenant-admin/identity-and-access#routing-rules) and [How seats are assigned automatically](/docs/government/org-admin/seats#how-seats-are-assigned-automatically).
* **Single sign-on works, but users are told they haven't been added to an organization.** A routing rule must cover them. See [Routing rules](/docs/government/tenant-admin/identity-and-access#routing-rules) and the [Readiness](/docs/government/tenant-admin/readiness) page.

## Deployment and network

* **Is this a separate government app?** No, it's the same Claude Desktop app used everywhere. One managed setting, which your IT team deploys, connects it to Claude for Government, and until a device has that setting, the app shows the regular claude.ai sign-in. See [The managed setting](/docs/government/deploy-desktop/configure#the-managed-setting) and [Order of deployment](/docs/government/deploy-desktop/configure#order-of-deployment).
* **Which hosts must the firewall allow, and what if claude.ai is blocked?** See [Network egress, required domains, and proxies](/docs/government/security/security-and-data-handling#network-egress-required-domains-and-proxies) and [Network access](/docs/government/deploy-desktop/windows-checklist#network-access) in the Windows fleet checklist.
* **Can Chat be rolled out first and Cowork enabled later?** Yes. See [If some devices are not ready for Cowork](/docs/government/deploy-desktop/windows-checklist#if-some-devices-are-not-ready-for-cowork).

## The Claude for Government Web import

* **How do users bring over their conversations and projects?** Each user runs the import themselves from Claude Desktop, which signs in to their web app account. See [Import your data from Claude for Government Web](/docs/government/desktop/import).
* **Can administrators remind users to run the import?** Yes. Turn on the [**Show the Claude for Government Web import banner**](/docs/government/config/settings#show-the-claude-for-government-web-import-banner) switch on the **Config** page.
* **The Import & export page in Claude Desktop says import isn't enabled.** See [Troubleshooting](/docs/government/desktop/import#troubleshooting) on the import page.
* **What comes across, and how does a user redo an import?** See [Things to know](/docs/government/desktop/import#things-to-know) and [Remove an import](/docs/government/desktop/import#remove-an-import).

## Other questions

Everything that isn't specific to the move, such as single sign-on, SCIM, seats, usage limits, settings, connectors, and the Compliance API, is in the [Claude for Government administrator guide](/docs/government/overview) and the pages listed beside it. Security and compliance reviewers start at [Security and data handling](/docs/government/security/security-and-data-handling). To report a problem, administrators contact their Anthropic representative or use the **Support** link in the admin portal footer, and service status is on [status.claude.com](https://status.claude.com) under Claude for Government.
