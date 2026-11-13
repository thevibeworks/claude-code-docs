> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Organizations

> See every organization in your tenant, open an organization's admin view, add an organization and get it ready for people, and copy user email addresses.

> **Who this is for:** Tenant administrators who create and oversee the organizations within their agency's deployment.

## How organizations work

An **organization** is a workspace that holds a set of users, a set of seats, its own spend caps, and its own product settings. A user never belongs to more than one organization at a time, and each organization is linked to exactly one **billing account** (the credit and seat pool that funds it). Organizations share the tenant's sign-in and provisioning setup.

> [!NOTE]
>
> Which organization a user joins isn't controlled on this page. You set that with the routing rules on the [Identity and access](https://claude.com/docs/government/tenant-admin/identity-and-access.md) page.

## The organization list

Clicking an organization's name opens its organization admin view. When you do this you are acting as an Owner of that organization and can manage its users, seats, and settings. Unless the organization [manages its own billing account](https://claude.com/docs/government/org-admin/billing.md#seats), you can also grant or remove its [Primary Owner role](https://claude.com/docs/government/org-admin/users.md#understanding-roles) on its Users page.

To email everyone in your tenant, or in one organization, click **Copy user email addresses** at the top of the page. The page that opens lists the email addresses of everyone except deactivated users, for the whole tenant and for each organization.

## Adding an organization

Expand the **Add organization** section to create a new organization. You'll provide the following:

* **Name** is what the organization will be called. To rename an organization, contact Anthropic.
* **Primary Owner email (optional)** creates an account for the organization's first [Primary Owner](https://claude.com/docs/government/org-admin/users.md#understanding-roles). Use it only for someone who has no account in your tenant yet, at an address on one of your verified domains. No invitation is sent, so let them know [where to sign in](https://claude.com/docs/government/tenant-admin/identity-and-access.md#where-sign-in-starts). If you leave it blank, you [manage the organization yourself](#the-organization-list). Once people join, you can make one of them Primary Owner on its **Users** page.
* **Billing account** is where the organization's credits and seats come from. Several organizations can share one. Contact Anthropic if the account you need isn't listed, or to change an organization's account later.

### After you add an organization

The new organization appears in the list immediately and you can click through to its organization admin view. Before people can use it:

* Add a routing rule on the [Identity and access](https://claude.com/docs/government/tenant-admin/identity-and-access.md) page so that the right people are placed in the new organization when they sign in or are provisioned. A rule can also [move people](https://claude.com/docs/government/tenant-admin/identity-and-access.md#when-rules-move-people) who are already in another organization.
* Give it seats on the [Seats](https://claude.com/docs/government/tenant-admin/seats.md) page. If its billing account has no pool of seats, it needs [a seat tier of its own](https://claude.com/docs/government/org-admin/seat-tiers.md#creating-a-self-managed-tier) instead.
* If you want to limit how much the new organization can spend from its billing account, set a spend cap on it on the [Billing](https://claude.com/docs/government/tenant-admin/credits.md) page. With no cap, the account's balance is the only limit.

## Deactivating an organization

You cannot delete an organization from this page. If an organization is no longer needed, contact Anthropic to have it deactivated. Routing rules that target a deactivated organization stop matching. The users still in it are deactivated with it and cannot sign in. Reactivating the organization later does not necessarily reactivate them.
