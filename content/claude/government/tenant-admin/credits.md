> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Billing

> See each billing account's credit balance and set per-organization spend caps, with what a cap counts, what it stops, and when a change takes effect.

> **Who this is for:** Tenant administrators who monitor billing-account balances and set spend caps on organizations.

The **Billing** page shows each billing account's **available balance** and any credit that [expired unspent](https://claude.com/docs/government/org-admin/billing.md#billing-account) since credit was last added. This is also where you set per-organization spend caps, which limit how much any one organization can draw from its account.

> [!NOTE]
>
> The **Billing** tab appears in the navigation only when credits apply to your tenant.

## How billing works

A **billing account** is a funding pool that Anthropic sets up for your tenant. It holds a dollar balance of credit, and Anthropic adds credit to the account as part of your agency's procurement. Each organization is linked to exactly one billing account, and several organizations may share the same one. Usage on [self-managed seat tiers](https://claude.com/docs/government/org-admin/seat-tiers.md#anthropic-managed-versus-self-managed-tiers) draws directly from the billing account's balance.

A spend cap limits how much one organization can spend from its billing account in a 5-hour or 7-day window.

* **What a cap counts.** Spend caps apply to usage on self-managed seat tiers. Usage on Anthropic-managed seat tiers is covered by the seat price rather than drawn from the account balance, so it is not counted against a cap.
* **Who is affected.** An organization that hits a spend cap does not affect other organizations on the same account. An account running out of balance stops usage on self-managed tiers in every organization on it. Low-balance alerts go to organization Owners and Primary Owners, as described under [Billing account](https://claude.com/docs/government/org-admin/billing.md#billing-account).
* **Who sets caps.** Spend caps are set by tenant administrators. Organization owners can see their own caps on their organization's [Billing](https://claude.com/docs/government/org-admin/billing.md) page, but cannot change them.

## Setting a spend cap

In a billing account's **Spend caps** section, click an organization's row to expand the editor, enter a dollar amount for the **5-hour cap**, the **7-day cap**, or both, and click **Save caps**.

* Leave a cap blank for no limit on that window.
* Both caps apply at the same time. An organization's usage is refused once either cap is reached, until that window resets.
* A cap of \$0 refuses the organization's requests billed to the account until you raise or clear the cap.

Changes take effect immediately. Raising or clearing a cap admits the organization's next request. Lowering a cap below the organization's current window usage refuses its next request until the window resets.
