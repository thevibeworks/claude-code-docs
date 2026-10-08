# Monthly API credits for Max and Team plans

Max and Team plans include monthly credits for the Claude Platform. Use them to build Claude into your own apps and agents with the Claude API. This article explains who's eligible, how to claim your credit, what it covers, and what happens when it runs out.

Available on Max and Team plans, including discounted Team plans. Free, Pro, and Enterprise plans aren't eligible.

## Monthly credits by plan

| **Plan**                                      | **Monthly credit**                                        |
| --------------------------------------------- | --------------------------------------------------------- |
| Max 5x                                        | $100                                                      |
| Max 20x                                       | $200                                                      |
| Team (Standard seats)                         | $20 per seat\*                                            |
| Team (Premium seats)                          | $100 per seat\*                                           |
| Discounted Team plans (Nonprofit, Scientists) | $20 USD per Standard seat and $100 USD per Premium seat\* |

* On Team plans, credits for all seats are pooled into one monthly balance, capped at $500. For example, a team with three Standard seats and two Premium seats receives $260 a month. The pool is calculated from the seats on the plan when the credits are granted.

## Eligibility

- **Active plan.** Your Max or Team subscription must be active and in good standing.

- **Seven days on the plan.** New subscribers can claim once they've been on an eligible plan for seven days.

- **Mobile subscriptions.** You can subscribe on the web, iOS, or Android. Claim your credits on claude.ai in a web browser.

- **No payment method needed.** You don't need to add a card on Claude Platform to claim or use the credit.

## How to claim your credit

To claim your credit, you link a Claude Console organization to your plan. Credits go to that organization each month.

Before you begin, you need:

- **On your Claude plan:** Max: be the subscriber. Team: be a Primary Owner or Owner

- **In the Console organization:** the Owner, Admin, or Billing role. If you don't have a Console organization yet, you can create one during the claim flow or at **[platform.claude.com](https://platform.claude.com)**.

To claim your credit:

1. On claude.ai, go to **[Settings > Billing](https://claude.ai/settings/billing)** as a Max subscriber or **[Organization settings > Billing](https://claude.ai/admin-settings/billing)** as a Team Owner or Primary Owner.

2. In the **API credits** section, select "Link organization."

3. Choose the Console organization you want to receive the credits, or create a new one.

4. Review the **[Supplemental Credit Terms](https://www.anthropic.com/legal/credit-terms)**, then Link organization.

Your credits appear in that organization's balance, ready to use.

**Important:** You can link only one Console organization, and each Console organization can receive credits from only one plan. You can't change the linked organization yourself, so choose the one you plan to build in. To change it later, **[contact support](https://support.claude.com/en/articles/9015913-how-to-get-support)**.

**Tip:** Sign in to the Claude Console with the same email you use on claude.ai. If you’re seeing errors during the linking flow, please try again in a few hours.

## What the credits cover

The credits work with any available Claude model on the Claude Platform, including:

- The Claude API (Messages API and Message Batches API)

- The Playground in the Claude Console

- Claude Managed Agents

- The Claude Agent SDK

The credits don’t apply to:

- Interactive Claude Code in the terminal, IDE, desktop, or web

- Extra usage in Claude, Claude Code, or Claude Cowork

- Claude on Amazon Bedrock, Google Cloud Vertex AI, or Microsoft Foundry

## How the credits work

- **Refreshes each billing cycle.** New credits arrive shortly after your plan payment goes through. On annual plans, credits arrive monthly.

- **Doesn't roll over.** Unused credits expire at the end of each billing cycle.

- **Used first.** Your monthly credits are spent before any credits you've purchased.

- **Shared across the organization.** Everyone with an API key in the linked organization draws from the same balance.

- **Separate from your plan limits.** The credits don’t change your usage limits in Claude, Claude Code, or Claude Cowork.

- **Visible in the Console.** All credits appear under **[Settings > Billing](https://platform.claude.com/settings/billing)** in Claude Console with their amount and expiry date.

## What happens when your credits run out

- **If the organization has purchased credits or auto-reload,** usage continues and draws from those.

- **If the organization has no other credits,** API requests stop until your next monthly credits arrive. Usage is never charged to your Claude plan. To keep going, buy credits or turn on auto-reload in the Console.

- **If your organization is invoiced through Anthropic sales,** usage beyond the credits is billed as usual.

## If your plan changes

- **Cancel, downgrade to an ineligible plan, or refund.** New credits stop. Credits you already have stay usable until they expire.

- **Upgrade from Max 5x to Max 20x.** You receive prorated credits right away, then $200 each billing cycle after that.

- **Move from Max to Team.** Your Max link ends. A Team Owner or Primary Owner can claim the team's credits once the Team plan has been active for seven days.

## For Team Owners and Primary Owners

**One claim for the whole team.** One owner links a Console organization and claims the pooled credit, up to $500 a month.

**The pool follows your seat count.** It's calculated from the seats on your plan each time credits are deposited. For example, a team with three Standard seats and two Premium seats receives $260 a month. Adding another Premium seat would increase the next cycle’s credits to $360.

**Control who spends it.** Everyone with an API key in the linked organization can use the balance. To limit usage by project or teammate, set **[workspace spend limits](https://platform.claude.com/docs/en/api/rate-limits#setting-lower-limits-for-workspaces)** in the Console.

## Frequently asked questions

### Why can't I use the credits for Claude Code?

The credits are for building your own apps and agents on the Claude Platform. They don't cover interactive Claude Code sessions or extra usage after you hit your plan's limits.

### Why don't I see the offer yet?

We’re rolling out API credits over a few days so we might not have gotten to you yet. The offer appears after you've been on an eligible plan for seven days. If you're past seven days and still don't see it, check that you're on a Max or Team plan and that you have one of the required roles. If you think you should be eligible but don’t see the API credits, **[contact support](https://support.claude.com/en/articles/9015913-how-to-get-support)**.

### Is this the same as the Agent SDK credits announced in June?

No. That credit isn't available. API credits cover the Claude API, Claude Managed Agents, and the Claude Agent SDK, and you claim it into a Console organization.

### Can I split my credits across multiple organizations?

No. Credits go to a single Console organization.

### I'm on a Pro plan. Can I get this credit?

No. The credits are available on Max and Team plans only.

### Does this cover `claude -p` ?

API credits cover `claude -p` and the Claude Agent SDK when you run them yourself with an API key from your linked Claude Console organization, because that usage is billed as Agent SDK usage. When you're signed in with your Claude plan instead, `claude -p` and Agent SDK usage still draw from your plan's usage limits and don't use your API credits. Runs started by the Claude Code GitHub Action, an IDE extension or the Claude desktop app count as Claude Code usage, so API credits don't cover them, even with `-p`.