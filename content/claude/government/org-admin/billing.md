> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Billing

> Use this page to see the balance your organization spends from and any spend caps set on it, and to adjust your organization's seat allocation.

> **Who this is for:** Organization owners who want to see the balance their organization spends from and any spend caps set on it, and manage their organization's seat allocation.

Use this page to see the balance your organization spends from and any spend caps your tenant administrator has set, and to adjust your organization's seat allocation.

A **billing account** is the funding pool that pays for one or more organizations in your tenant. Your organization's usage on self-managed seat tiers draws directly from this account's balance, and Anthropic adds credit to the account. Your tenant administrator can also set a **spend cap** on your organization, which limits how much it can draw from the account in a rolling 5-hour or 7-day window.

<Note>
  The **Billing** tab appears in the navigation when the billing account is active and your own organization is active on it. If the tab is hidden, this page is still reachable from a direct link. Funding is arranged with Anthropic by your tenant administrators; contact them about credits or spend caps.
</Note>

## Billing account

At the top you see the billing account's available balance, or, when the balance is not shown to you, a line explaining who manages the account. The balance is shared by every organization the account funds.

Below the balance, the page shows the spend caps currently set on your organization, in the form "\$X per 5 hours, \$Y per 7 days", or "No spend caps are set" if none are. These caps are set by your tenant administrator and cannot be changed here. A cap of \$0 pauses your organization's spending from the account, and a banner appears on this page saying so.

When the account's balance reaches 70 percent, 90 percent, and 100 percent consumed, a spend-alert banner appears on every page of the organization admin portal and an email is sent to your organization's owners. The banner stays in place until Anthropic adds more credits to the account.

Your organization's usage against the account balance is shown on the [Analytics](/docs/government/org-admin/analytics) page.

## Seats

The **Seats** section shows the pool of Anthropic-managed seats funded by this account. For each tier the table shows the **Pool** total, which is the number of seats granted to the account, the **Distributed** count, which is how many of those seats have been handed out to organizations, and the **Remaining** count, which is the number still available to distribute.

<Note>
  The seat allocation editor below only appears when the account has at least one seat tier in its pool.
</Note>

An editor below the table lets you set how many seats of each tier your organization holds. Enter the number you want for each tier and click **Save**. The change takes effect immediately.

### Rules for changing seat allocations

The editor enforces the following rules and will refuse a save that violates any of them.

* You cannot request more seats for a tier than the billing account has remaining in its pool after accounting for other organizations.
* You cannot reduce a tier's seat count below the number of users currently seated on it in your organization. Move users off the tier on the [Users](/docs/government/org-admin/users) page first, then lower the count.
* You can set a tier to zero seats, which removes the tier from your organization entirely, but only if no one is seated on it.
* Each tier's seat count can be at most 100,000.

<Tip>
  Saving your organization's first seat allocation also gives seats to members who have no seat tier, Primary Owners first, as long as nobody holds a seat before the save. Saving any allocation also triggers a directory provisioning sync, so provisioned users who were left unassigned because their mapped tier was full are seated up to the new limit. Anyone else stays unassigned until an owner chooses a tier for them on the [Users](/docs/government/org-admin/users) page.
</Tip>
