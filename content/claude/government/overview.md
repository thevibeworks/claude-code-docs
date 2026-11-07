> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Claude for Government administrator guide

> Set up and manage Claude for Government for your agency: how tenants, organizations, users, seats, and credits fit together.

> **Who this guide is for:** Administrators who set up and manage Claude for Government for their agency.

This guide covers the portals used to manage Claude for Government: how access, seats, and usage are organized, and who is responsible for each part. Members use Claude in the Claude apps, such as Claude Desktop, that your agency [makes available](https://claude.com/docs/government/config/settings.md#product-availability). Claude for Government isn't available in the Claude mobile apps.

> [!NOTE]
>
> These cases are covered on other pages:
>
> * **Managing your whole tenant**: see [Tenant administration](https://claude.com/docs/government/tenant-admin/overview.md)
> * **Managing one organization**: see [Organization administration](https://claude.com/docs/government/org-admin/overview.md)
> * **Setting up a new tenant**: see [Tenant setup wizard](https://claude.com/docs/government/tenant-admin/setup-wizard.md)
> * **Checking your own profile, usage, or sessions**: see [Your account](https://claude.com/docs/government/account/overview.md)
> * **Using Claude Desktop**: see [Video walkthroughs for Claude Desktop](https://claude.com/docs/government/desktop/video-walkthroughs.md)
> * **Installing Claude Desktop on agency devices**: see [Connect Claude Desktop to Claude for Government](https://claude.com/docs/government/deploy-desktop/configure.md)
> * **Reviewing security and data handling**: see [Security and data handling](https://claude.com/docs/government/security/security-and-data-handling.md)

## How your deployment is organized

Claude for Government is organized as a three-level hierarchy:

* **Tenant**: The tenant is the top level, and it represents your agency's overall deployment. The tenant is managed by a short list of [tenant administrators](https://claude.com/docs/government/tenant-admin/admins.md).
* **Organizations**: An organization is a group of users who share a pool of seats and a set of policies, with its own spend caps. Each organization has its own owners, its own members, its own seat assignments, and its own configuration. The organizations all share the tenant's single sign-on connection, so you configure identity once and every organization uses it.
* **Users**: A user never belongs to more than one organization at a time. Each user has a [role](https://claude.com/docs/government/org-admin/users.md#understanding-roles), which decides what they can manage, and a [seat tier](https://claude.com/docs/government/org-admin/seat-tiers.md), which decides which models they can use and how much. A user with no seat tier can sign in and see their account, but they can't send messages to Claude.

You might create one organization for each bureau, office, or program, or you might run the whole agency as a single organization. You would create more when you need any of the following:

* Separate billing accounts so one group's usage never draws down another group's balance
* Separate usage reporting for each bureau or program
* Different product settings, seat tiers, or access rules for different parts of your agency

A **billing account** is where your agency's credits and seats live. Anthropic sets up one or more billing accounts with your agency. Every organization is linked to exactly one billing account. Several organizations can share the same billing account, or each organization can have its own. Tenant administrators divide each billing account's [seat pool](https://claude.com/docs/government/tenant-admin/seats.md#how-seats-are-organized) among the organizations it funds, and can set per-organization [spend caps](https://claude.com/docs/government/tenant-admin/credits.md) to control how much any one organization draws from a shared balance.

## The three views

<video controls preload="metadata" playsInline src="https://mintcdn.com/claude-ai/mGbOjjHMKV3LYuqi/images/government/videos/admin-01-finding-your-way-around-v2.mp4?fit=max&auto=format&n=mGbOjjHMKV3LYuqi&q=85&s=4aaba8c318c1a044b343874cc64c95c3" aria-label="Video walkthrough: Finding your way around" />

Video: Finding your way around (2 min 24 s). Narrated with an AI-generated voice, with on-screen captions.

[Transcript](https://claude.com/docs/government/video-walkthroughs.md#finding-your-way-around)

Open the portal in a browser at your agency's Claude for Government address followed by `/gateway`. Which views you can reach depends on your role, and you switch between them using the link in the page footer.

* [**Tenant**](https://claude.com/docs/government/tenant-admin/overview.md): tenant administrators
* [**Organization admin**](https://claude.com/docs/government/org-admin/overview.md): organization owners and tenant administrators
* [**Account**](https://claude.com/docs/government/account/overview.md): everyone

Organization owners land on the organization admin view, and members with no administrative role land on their account view. Tenant administrators reach the tenant view from the **Switch to tenant view** link in the organization admin view's footer.

Being a [tenant administrator](https://claude.com/docs/government/tenant-admin/admins.md#how-tenant-admin-access-works) is separate from the role you hold inside an organization.

## How people get access

A tenant administrator connects your agency's [single sign-on](https://claude.com/docs/government/tenant-admin/identity-and-access.md#single-sign-on) and, optionally, [directory provisioning (SCIM)](https://claude.com/docs/government/tenant-admin/identity-and-access.md#scim-provisioning) on the [Identity and access](https://claude.com/docs/government/tenant-admin/identity-and-access.md) page. [Routing rules](https://claude.com/docs/government/tenant-admin/identity-and-access.md#routing-rules) then decide which organization each person joins. A new person who does not match any rule cannot sign in until a rule is added that covers them. A rule change can also move people who already have an account, as described in [When rules move people](https://claude.com/docs/government/tenant-admin/identity-and-access.md#when-rules-move-people).
