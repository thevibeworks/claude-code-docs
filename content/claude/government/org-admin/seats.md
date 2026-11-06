> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Seats

> See how many seats of each tier your organization holds and how many are assigned, and how new and unassigned users get a seat tier.

> **Who this is for:** Organization owners who need to see how many seats of each tier are available and how many are in use.

The **Seats** page shows how many seats your organization has for each [seat tier](https://claude.com/docs/government/org-admin/seat-tiers.md#the-tier-list) and how many of them are currently assigned to users. For each tier, **Assigned** is how many of your users are on that tier, and **Limit** is the number of seats your organization has been allocated. You cannot assign more users to a tier than its limit allows, and a self-managed tier [may have no limit](https://claude.com/docs/government/org-admin/seat-tiers.md#anthropic-managed-versus-self-managed-tiers). The **Assigned** count includes only [active users](https://claude.com/docs/government/org-admin/users.md#deactivated-users).

> [!NOTE]
>
> The **Seats** page is read-only. These tasks are covered on other pages:
>
> * **Move a user onto a different tier**: use the [Users](https://claude.com/docs/government/org-admin/users.md#assigning-a-seat-tier) page
> * **Create or edit self-managed tiers**: use the [Tiers](https://claude.com/docs/government/org-admin/seat-tiers.md) page
> * **Change how many seats your organization holds**: ask a [tenant administrator](https://claude.com/docs/government/tenant-admin/seats.md#change-seat-allocations), unless your organization manages its own billing account. Then a [Primary Owner](https://claude.com/docs/government/org-admin/users.md#understanding-roles) uses [Seats](https://claude.com/docs/government/org-admin/billing.md#seats) on the Billing page.

## How seats are assigned automatically

Someone who joins your organization gets the first of these that applies:

1. The tier one of their directory groups is [mapped to](https://claude.com/docs/government/org-admin/provisioning.md#group-to-seat-tier).
2. The tier marked **New members start here** on the [Tiers](https://claude.com/docs/government/org-admin/seat-tiers.md) page.
3. The tier with a **Limit**, a free seat, and the lowest **Sort order**.

If their mapped or marked tier is full, they get no seat, even if another tier has one free. If a full tier is the reason, someone new from your directory [isn't added yet](https://claude.com/docs/government/org-admin/provisioning.md#how-mappings-are-applied).

Anyone else with no seat is **Unassigned** and has no model access. Adding more seats later seats only those of them in a mapped group. For the rest, an owner can [choose a tier](https://claude.com/docs/government/org-admin/users.md#assigning-a-seat-tier), and so can a tenant administrator from your organization's admin view.

> [!NOTE]
>
> **Tiers with a seat limit.** A self-managed tier has no **Limit** unless one is set for it. People who hold a seat stay put when a **Limit** or **Sort order** changes, though [mapping groups to tiers](https://claude.com/docs/government/org-admin/provisioning.md#group-to-seat-tier) can move some.
