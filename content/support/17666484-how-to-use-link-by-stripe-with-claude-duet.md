# How to use Link by Stripe with Claude Duet

Connect Link, Stripe's digital wallet, to Claude Duet so it can pay for purchases you approve.

Link is available in Claude Duet, a research preview for Pro, Max, and Ultra plans in the US with a US payment method. It isn't available in Claude, Cowork, or Claude Code for now.

Link is separate from the Stripe connector, which lets Claude work in your Stripe account. You can use either one without the other.

## What you can do

- **Approve every purchase.** Claude Duet is designed to ask you before each purchase and not submit the Link payment until you approve the maximum amount. When you approve, Link may place a temporary authorization on your selected payment method. The final charge is completed only if the merchant completes the purchase.

- **Pay with a one-time card.** Each purchase uses a one-time card that only works for that purchase.

## How to connect

Link isn't listed in the connectors directory. You connect it in Claude Duet.

1. Select your avatar in Claude Duet.

2. Select the option to connect payments, then choose Link.

3. Sign in to your Link account and approve access.

Claude Duet also suggests connecting Link when you ask for something that needs a payment.

Claude Duet can see the card type, last four digits of your card or bank account, nickname and expiration date of your saved payment methods, plus your shipping addresses. Claude isn’t given your full credit card number (PAN) or bank account number.

## How to pay with Link

1. Ask Claude Duet for what you need, like "Reorder ink for the office printer."

2. Claude Duet finds the item and asks you to approve the purchase.

3. Create or sign in to your Link account using the Link mobile app or app.link.com, then approve your Spend Request.

4. Claude Duet pays with a one-time card scoped to the merchant and amount.

## Current limitations

- Link is available only in Claude Duet, on Pro, Max, and Ultra plans in the US.

- A US payment method is required.

- Claude Duet can't pay with Link until you approve the amount in the Link app.

- A business may decline or block checkout after you approve the Spend Request.

- A failed purchase may temporarily appear as pending on the selected funding method.

- Claude Duet can’t make recurring payments with Link.

- Some sites can block Claude Duet from paying. If that happens, you may need to finish the purchase yourself.

---

## Frequently asked questions

### Can Claude Duet buy something without asking me?

Claude Duet is designed to ask before each purchase, and it can't pay with Link until you approve the amount in the Link app.

### Why can't I find Link in the connectors directory?

Link is built into Claude Duet, so you connect it there.

### Is Link the same as the Stripe connector?

No. The Stripe connector lets Claude work in your Stripe account, for example to check for unpaid invoices. Link pays for purchases. You connect them separately.

### Who do I contact about a charge, a refund, or a problem with a purchase?

- Contact the store for order status, delivery, cancellations, returns, damaged or incorrect products, and product refunds.

- Contact **[Link Support](https://support.link.com/topics/link-agent-wallet)** for Link account problems, approval problems, payment-method issues, duplicate or incorrect payment amounts, an unrecognized Link payment, or a payment authorization that remains pending after a failed purchase.

- Contact **[our Support team](https://support.claude.com/en/articles/9015913-how-to-get-support)** if Claude Duet selected a different product, store, quantity, or option than you requested, or if Claude Duet itself did not work correctly. You can tell Claude Duet what happened directly in the chat and it will pass your report to our team.

- If you do not recognize a purchase, deny any pending approval requests, disconnect Link from Claude Duet, and contact Link Support promptly.

### How do I disconnect Link?

1. In Claude Duet, select your Claude Duet avatar.

2. Select payments, then choose Link.

3. Select "Disconnect."