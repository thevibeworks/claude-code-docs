> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Seats

> Divide each billing account's seat pool among the organizations it funds, and see who can change an allocation and why a change is refused.

> **Who this is for:** Tenant administrators who distribute purchased seats to the organizations in their deployment.

## How seats are organized

A **seat** is what entitles one person to use Claude. Every seat belongs to a [**seat tier**](https://claude.com/docs/government/org-admin/seat-tiers.md#the-tier-list).

Anthropic sets up your [billing accounts](https://claude.com/docs/government/tenant-admin/credits.md#how-billing-works). Each organization must be linked to exactly one, and several can share one. If an account has a pool of seats, you divide it on this page among the organizations it funds. Organization owners then assign seat tiers to users individually or by [directory group](https://claude.com/docs/government/org-admin/provisioning.md). Organizations that [create their own seat tiers](https://claude.com/docs/government/org-admin/seat-tiers.md#creating-a-self-managed-tier) don't need a pool.

If you need more seats in a pool, or a new tier added to it, contact Anthropic.

## Change seat allocations

On the **Seats** page in the tenant admin portal, edit the number fields under an organization's name and click its **Save**. Changes take effect immediately.

The save is rejected in cases such as these:

* The account's organizations would together hold more seats than the pool has for a tier.
* You try to reduce a tier below the number of people already seated on it in that organization. Ask the organization's owners to unassign people from that tier first, then reduce the allocation.

To move seats between organizations on the same billing account, lower one and raise the other. If no seats remain in the pool, save the reduction first, then the increase.

If an account says **Managed by** an organization's administrators, that organization's [Primary Owners](https://claude.com/docs/government/org-admin/users.md#understanding-roles) manage its seats.

## How seats affect new users

A new person placed in an organization (by a routing rule on the [Identity and access](https://claude.com/docs/government/tenant-admin/identity-and-access.md) page) can be given a seat automatically: see [How seats are assigned automatically](https://claude.com/docs/government/org-admin/seats.md#how-seats-are-assigned-automatically).
