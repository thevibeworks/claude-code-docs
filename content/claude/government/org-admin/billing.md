> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Billing

> See the balance your organization spends from, the spend caps set on it, and its seats, and what happens as the billing account's balance runs low.

> **Who this is for:** Organization owners who want to see the balance their organization spends from, any spend caps set on it, and its seat allocation.

A **billing account** is the funding pool that pays for one or more organizations in your tenant. Your organization's usage on [self-managed seat tiers](https://claude.com/docs/government/org-admin/seat-tiers.md#anthropic-managed-versus-self-managed-tiers) draws directly from this account's balance, and Anthropic adds credit to the account.

> [!NOTE]
>
> The **Billing** tab appears in the navigation when the billing account is active and your own organization is active on it. Funding is arranged with Anthropic by your tenant administrators; contact them about credits or spend caps.

## Billing account

The page shows the account's available balance if your organization uses self-managed seat tiers and either manages the account or is the only organization on it. Otherwise it says why no balance is shown. The balance is shared by every organization the account funds. Your organization's usage against the account balance is shown on the [Analytics](https://claude.com/docs/government/org-admin/analytics.md) page.

The page also shows the [spend caps](https://claude.com/docs/government/tenant-admin/credits.md#how-billing-works) currently set on your organization. These caps are set by your tenant administrator and cannot be changed here. A cap of \$0 pauses your organization's spending from the account.

As the account's balance runs low, and again when it runs out and requests are refused, a spend-alert banner appears on every page of the organization admin portal and an email is sent to your organization's Owners and Primary Owners. The banner stays in place until Anthropic adds more credits to the account. People on Anthropic-managed seat tiers keep working, so [moving someone to one](https://claude.com/docs/government/org-admin/users.md#assigning-a-seat-tier) gets them working again. An organization that has only Anthropic-managed seat tiers gets neither banner nor email, so moving everyone to them and [deleting your self-managed tiers](https://claude.com/docs/government/org-admin/seat-tiers.md#deleting-a-tier) also clears the banner.

## Seats

The **Seats** section shows the seats allocated to your organization. Whoever manages the billing account can change them:

* **Your tenant administrators manage the account.** Ask a tenant administrator.
* **Your organization manages the account.** A Primary Owner sees the account's seat pool here. Enter the number you want for each tier and click **Save**. The change takes effect immediately.

If a save is refused, see [Change seat allocations](https://claude.com/docs/government/tenant-admin/seats.md#change-seat-allocations). For who is seated when seats are added, see [How seats are assigned automatically](https://claude.com/docs/government/org-admin/seats.md#how-seats-are-assigned-automatically).
