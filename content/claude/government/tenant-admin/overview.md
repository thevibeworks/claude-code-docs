> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Tenant administration

> Manage the settings that apply across your whole agency: organizations, identity and sign-in, and how seats are distributed and spend caps are set.

> **Who this portal is for:** Tenant administrators who manage their agency's overall Claude for Government deployment across every organization. If you manage a single organization, see the [Organization administration](/docs/government/org-admin/overview) guide instead.

The tenant admin portal is where you manage the things that apply across every team using the service: identity, organization routing, seats, spend caps, and tenant-wide product settings.

## Tenants and organizations

Your **tenant** is your agency's top-level account. Within your tenant you create one or more **organizations**, which are separate workspaces for different teams, bureaus, or programs. All organizations in your tenant share the same sign-in setup, so one connection to your identity provider covers everyone. What differs between organizations is who belongs to each one, how many seats each one is allocated and what spend caps are set on it, and which product settings each one can adjust for itself.

Funding flows through **billing accounts**, which are credit and seat pools that Anthropic sets up with your agency. Every organization is linked to exactly one billing account, and several organizations may draw from the same one. The [Seats](/docs/government/tenant-admin/seats) page is where you divide each billing account's seat pool among its organizations, and the [Billing](/docs/government/tenant-admin/credits) page is where you see each account's balance and set per-organization spend caps.

There are two admin portals:

* The **tenant admin** portal (this one) is where you create organizations, connect your identity provider, decide which organization each user lands in, distribute seats and set spend caps, and set tenant-wide policy. Only tenant administrators can see it.
* The **organization admin** portal is where each organization's own owners manage that organization's users, seats, and settings. As a tenant administrator, you can open any organization's admin view from the [Organizations](/docs/government/tenant-admin/organizations) page, or you can use the **Switch to org view** link at the bottom of every tenant admin page.

## Who can use this portal

Only **tenant administrators** can open the tenant admin portal. Tenant administrators are a specific list of people that are managed on the [Admins](/docs/government/tenant-admin/admins) page, and this list is separate from any role someone holds inside an organization.

> **For organization owners:** Owning an organization does *not* make you a tenant administrator. If you need tenant-level access, ask an existing tenant administrator to add you on the [Admins](/docs/government/tenant-admin/admins) page.

Every page of this portal requires tenant administrator access. If you follow a link in this guide without tenant access, you'll be turned away with a permission error.

## Getting set up for the first time

The [setup wizard](/docs/government/tenant-admin/setup-wizard) walks you through all of this step by step.

If your tenant has just been created, work through the pages in this order:

1. **[Identity and access](/docs/government/tenant-admin/identity-and-access).** Connect single sign-on so that people can authenticate with their agency credentials, optionally connect SCIM provisioning so that your directory syncs users and groups automatically, and add at least one routing rule so that users are placed in an organization when they sign in. Until a rule exists, nobody else can sign in.
2. **[Seats](/docs/government/tenant-admin/seats) and [Billing](/docs/government/tenant-admin/credits).** Distribute seats from your billing account to the organizations that will use them, and optionally set spend caps.
3. **[Admins](/docs/government/tenant-admin/admins).** Add at least one more tenant administrator so that you are not the only person with tenant-level access.

<Warning>
  There is a short setup period after Anthropic first creates your tenant. During that period, a banner appears on the Identity and access page and nobody at your agency can sign in yet, including people who would normally be routed to an organization. You can still use that time to configure your single sign-on connection and routing rules, and they will start working automatically as soon as the setup period ends.
</Warning>

## Pages in this portal

The navigation groups the pages into three sections.

**Organizations and identity**

* The **[Organizations](/docs/government/tenant-admin/organizations)** page lets you see every organization in your tenant, open any organization's admin view, and create new organizations.
* The **[Identity and access](/docs/government/tenant-admin/identity-and-access)** page lets you connect single sign-on (using either the OIDC or SAML protocol, whichever your identity provider supports), manage the SCIM provisioning token, write the routing rules that place users into organizations, preview how a specific person would be routed, and review people who haven't been placed yet.

**Seats and billing**

* The **[Seats](/docs/government/tenant-admin/seats)** page lets you distribute the seats in each billing account's pool to the organizations that account funds.
* The **[Billing](/docs/government/tenant-admin/credits)** page shows each billing account's balance and lets you set spend caps that limit how much each organization can draw from it.

**Settings**

* The **[Config](/docs/government/tenant-admin/configuration)** page lets you set product settings that apply to every organization, and optionally lock them so organizations can't override them.
* The **[Admins](/docs/government/tenant-admin/admins)** page lets you manage who has access to this tenant admin portal.
* The **[Readiness](/docs/government/tenant-admin/readiness)** page shows what is blocking your organizations from using Claude and where each item is resolved.

The [setup wizard](/docs/government/tenant-admin/setup-wizard) is not a page in this list; you reach it through the **Resume setup** banner that appears above the navigation until your tenant is fully set up.
