> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Moving from Claude for Government Web

> Find answers to the questions agencies ask most often when moving from Claude for Government Web to Claude Desktop.

> **Who this is for:** Administrators and IT staff at an agency that used Claude for Government Web (the web app) and is moving its users to Claude Desktop connected to Claude for Government. If you use Claude but don't administer it, see [Import your data from Claude for Government Web](https://claude.com/docs/government/desktop/import.md) instead.

This page answers the questions that only come up during the move and links each one to the page with the detail. For anything specific to your agency's agreement, contact your Anthropic representative.

## What the move involves

* **Is there a deadline for the move?** Your Anthropic representative confirms the timeline.
* **Do users need the Claude Desktop app?** Yes. After the move, people use Claude in the Claude Desktop app (Chat, Cowork, and Code), which your IT team deploys, and use the browser only to sign in, view [their account](https://claude.com/docs/government/account/overview.md), and administer. See [Connect Claude Desktop to Claude for Government](https://claude.com/docs/government/deploy-desktop/configure.md).
* **What changes for users?** They work in the Claude Desktop app instead of a browser, and conversations, projects, and files are stored on each user's device, so projects aren't shared between people. Administrators can still give everyone in the tenant or in one organization the same skills by adding them as a plugin in the admin portal. See [Data storage and retention](https://claude.com/docs/government/security/security-and-data-handling.md#data-storage-and-retention), [Chat and Cowork differences](https://claude.com/docs/government/security/security-and-data-handling.md#chat-and-cowork-differences), and [Skills for administrators](https://claude.com/docs/government/desktop/skills.md#skills-for-administrators).
* **Does anything carry over from the web app?** Each user can copy their own conversations and projects with the [Claude for Government Web import](https://claude.com/docs/government/desktop/import.md). Roles and administrative settings aren't copied from the web app, so your administrators set up the admin portal themselves, starting with the [setup wizard](https://claude.com/docs/government/tenant-admin/setup-wizard.md).
* **Can the web app's application be deleted from your identity provider?** Check the **Single sign-on** card on [Identity and access](https://claude.com/docs/government/tenant-admin/identity-and-access.md#single-sign-on) first. If the card's **Redirect URI / ACS URL** appears in that application, Claude for Government signs people in through it. If the application is deleted, single sign-on stops for everyone, and removing users from it can stop theirs.
* **What does each user do?** Install or receive Claude Desktop, choose **Sign in with your organization**, and optionally [run the import](https://claude.com/docs/government/desktop/import.md).

## First sign-ins and the admin portal

* **Where is the admin portal?** In the browser, at your Claude for Government address followed by `/gateway`, not in the Claude Desktop app. See [The three views](https://claude.com/docs/government/overview.md#the-three-views) for which view each role opens.
* **How does the first administrator sign in, before single sign-on is connected?** On the sign-in page at your Claude for Government address followed by `/gateway`, which can email them a single-use sign-in link. See [Tenant setup wizard](https://claude.com/docs/government/tenant-admin/setup-wizard.md).
* **How are user accounts created?** At each person's first sign-in through a routing rule, or ahead of time through SCIM. See [Routing rules](https://claude.com/docs/government/tenant-admin/identity-and-access.md#routing-rules) and [How seats are assigned automatically](https://claude.com/docs/government/org-admin/seats.md#how-seats-are-assigned-automatically).
* **Single sign-on works, but users are told they haven't been added to an organization.** A routing rule must cover them. See [Routing rules](https://claude.com/docs/government/tenant-admin/identity-and-access.md#routing-rules) and the [Readiness](https://claude.com/docs/government/tenant-admin/readiness.md) page.

## Deployment and network

* **Is this a separate government app?** No, it's the same Claude Desktop app used everywhere. One managed setting, which your IT team deploys, connects it to Claude for Government, and until a device has that setting, the app shows the regular claude.ai sign-in. See [The managed setting](https://claude.com/docs/government/deploy-desktop/configure.md#the-managed-setting) and [Order of deployment](https://claude.com/docs/government/deploy-desktop/configure.md#order-of-deployment).
* **Which hosts must the firewall allow, and what if claude.ai is blocked?** See [Network egress, required domains, and proxies](https://claude.com/docs/government/security/security-and-data-handling.md#network-egress-required-domains-and-proxies) and [Network access](https://claude.com/docs/government/deploy-desktop/windows-checklist.md#network-access) in the Windows fleet checklist.
* **Can Chat be rolled out first and Cowork enabled later?** Yes. See [If some devices are not ready for Cowork](https://claude.com/docs/government/deploy-desktop/windows-checklist.md#if-some-devices-are-not-ready-for-cowork).

## The Claude for Government Web import

* **How do users bring over their conversations and projects?** Each user runs the import themselves from Claude Desktop. See [Import your data from Claude for Government Web](https://claude.com/docs/government/desktop/import.md).
* **Can administrators remind users to run the import?** Yes. Turn on the [**Show the Claude for Government Web import banner**](https://claude.com/docs/government/config/settings.md#show-the-claude-for-government-web-import-banner) switch on the **Config** page.
* **The Import & export page in Claude Desktop says import isn't enabled.** See [Troubleshooting](https://claude.com/docs/government/desktop/import.md#troubleshooting) on the import page.
* **What comes across, and how does a user redo an import?** See [Things to know](https://claude.com/docs/government/desktop/import.md#things-to-know) and [Remove an import](https://claude.com/docs/government/desktop/import.md#remove-an-import).

## Other questions

Everything that isn't specific to the move, such as single sign-on, SCIM, seats, usage limits, settings, connectors, and the Compliance API, is in the [Claude for Government administrator guide](https://claude.com/docs/government/overview.md) and the pages listed beside it. Security and compliance reviewers start at [Security and data handling](https://claude.com/docs/government/security/security-and-data-handling.md). To report a problem, administrators contact their Anthropic representative or use the **Support** link in the admin portal footer, and service status is on [status.claude.com](https://status.claude.com) under Claude for Government.
