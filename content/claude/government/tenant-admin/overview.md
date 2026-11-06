> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Tenant administration

> Manage the settings that apply across your whole agency: organizations, identity and sign-in, and how seats are distributed and spend caps are set.

> **Who this portal is for:** Tenant administrators who manage their agency's overall Claude for Government deployment across every organization. If you manage a single organization, see the [Organization administration](https://claude.com/docs/government/org-admin/overview.md) guide instead.

The tenant admin portal is where you manage the things that apply across every team using the service: identity, organization routing, seats, spend caps, and tenant-wide product settings.

## Tenants and organizations

For how your tenant, its organizations, and billing accounts fit together, see [How your deployment is organized](https://claude.com/docs/government/overview.md#how-your-deployment-is-organized).

The [**organization admin**](https://claude.com/docs/government/org-admin/overview.md#who-can-access-it) portal is where each organization's own owners manage that organization's users, seats, and settings. As a tenant administrator, you can open any organization's admin view from the [Organizations](https://claude.com/docs/government/tenant-admin/organizations.md) page, or you can use the **Switch to org view** link at the bottom of every tenant admin page.

## Who can use this portal

Only **tenant administrators** can open the tenant admin portal. Tenant administrators are a specific list of people that are managed on the [Admins](https://claude.com/docs/government/tenant-admin/admins.md) page, and this list is separate from any role someone holds inside an organization. If you need tenant-level access, ask an existing tenant administrator to add you on the [Admins](https://claude.com/docs/government/tenant-admin/admins.md) page.

## Getting set up for the first time

The [setup wizard](https://claude.com/docs/government/tenant-admin/setup-wizard.md) walks you through setting up a new tenant step by step. You reach it through the **Resume setup** banner that appears above the navigation until your tenant is fully set up. Add at least one more tenant administrator on the [Admins](https://claude.com/docs/government/tenant-admin/admins.md) page so that you are not the only person with tenant-level access.

## Pages in this portal

* **[Organizations](https://claude.com/docs/government/tenant-admin/organizations.md)**: see every organization in your tenant, open any organization's admin view, and create new organizations
* **[Identity and access](https://claude.com/docs/government/tenant-admin/identity-and-access.md)**: connect [single sign-on](https://claude.com/docs/government/tenant-admin/identity-and-access.md#single-sign-on), manage the [SCIM provisioning](https://claude.com/docs/government/tenant-admin/identity-and-access.md#scim-provisioning) token, write the [routing rules](https://claude.com/docs/government/tenant-admin/identity-and-access.md#routing-rules) that place users into organizations, and find out [why someone cannot sign in](https://claude.com/docs/government/tenant-admin/identity-and-access.md#when-someone-cannot-sign-in)
* **[Seats](https://claude.com/docs/government/tenant-admin/seats.md)**: distribute the seats in each billing account's pool to the organizations that account funds
* **[Billing](https://claude.com/docs/government/tenant-admin/credits.md)**: see each billing account's balance and set spend caps that limit how much each organization can draw from it
* **[Readiness](https://claude.com/docs/government/tenant-admin/readiness.md)**: see what is blocking your organizations from using Claude and where each item is resolved
* **[Config](https://claude.com/docs/government/tenant-admin/configuration.md)**: set product settings that apply to every organization, and optionally lock them so organizations can't override them
* **[Admins](https://claude.com/docs/government/tenant-admin/admins.md)**: manage who has access to this tenant admin portal
* **[Compliance API keys](https://claude.com/docs/government/org-admin/compliance-api.md)**: create and revoke API keys that stream audit events for every organization in your tenant, together with tenant-level activity, to a SIEM or log management system

Some tabs, such as **Billing** and **Compliance API keys**, appear in the navigation only when they are available to your tenant.
