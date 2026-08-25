> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Billing

> Use this page to see each billing account's balance and to set per-organization spend caps.

> **Who this is for:** Tenant administrators who monitor billing-account balances and set spend caps on organizations.

Use this page to see each billing account's balance and to set spend caps that limit how much any one organization can draw from it.

<Note>
  The **Billing** tab appears in the navigation only when credits apply to your tenant, which means at least one organization can use credits or there is a credit balance on any billing account in your tenant. If neither is true, the tab is hidden and **Seats** appears on its own in the navigation. This page is still reachable from a direct link and shows a short explanation. The tab appears automatically once Anthropic configures billing for your tenant.
</Note>

## How billing works

A **billing account** is a funding pool that Anthropic sets up for your tenant. It holds a dollar balance of credit, and Anthropic adds credit to the account as part of your agency's procurement. Each organization is linked to exactly one billing account, and several organizations may share the same one.

Usage by any organization draws directly from its billing account's balance. Because organizations share the balance, one organization's usage can reduce what is available to the others on the same account. To control that, you can set a **spend cap** on each organization.

A spend cap limits how much one organization can spend from its billing account in a rolling window. It is a policy limit, not a transfer of money. Nothing moves when you set or change a cap, and the billing account's balance is always the ultimate limit regardless of what caps are set.

Spend caps apply to usage on self-managed seat tiers. Usage on Anthropic-managed seat tiers is covered by the seat price rather than drawn from the account balance, so it is not counted against a cap.

## What the page shows

<Note>
  Billing account cards only appear once Anthropic has set up at least one billing account for your tenant. Until then, the page shows a message asking you to contact Anthropic.
</Note>

Each billing account appears as its own card showing:

* The **available balance**, which is the credit remaining in the account. Every organization on the account draws from this one balance.
* How many organizations the account funds.
* A **Spend caps** section listing each organization on the account with its current caps.

If every organization on an account uses only Anthropic-managed seat tiers, a banner explains that the balance and spend caps do not limit usage right now. They take effect once an organization starts using self-managed tiers.

## Setting a spend cap

In a billing account's **Spend caps** section, click an organization's row to expand the editor, enter a dollar amount for the **5-hour cap**, the **7-day cap**, or both, and click **Save caps**.

* Leave a cap blank for no limit on that window. The billing account's balance is still the ultimate limit.
* Both caps apply at the same time. An organization's usage is refused once either cap is reached, until that window rolls forward.
* Amounts can be from \$0 to \$1,000,000,000, and you can use cents.
* A cap of \$0 pauses the organization. Requests billed to the account are refused until you raise or clear the cap.

Changes take effect immediately. Raising or clearing a cap admits the organization's next request. Lowering a cap below the organization's current window usage refuses its next request until the window rolls forward.

## When you can't set caps

If an account is **deactivated**, its organizations' requests are refused and you cannot edit caps. Contact Anthropic to move the organizations to an active account.

## Things to know

* Spend caps are set by tenant administrators. Organization owners can see their own caps on their organization's Billing page, but cannot change them.
* Adding credit to a billing account is arranged with Anthropic as part of your agency's procurement. There is no form on this page to add credit.
* An organization that hits a spend cap does not affect other organizations on the same account. An account running out of balance affects every organization on it.
