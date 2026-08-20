# How do I pay for my Claude API usage?

This article explains how billing works for the Claude API, the playground, and Claude Code when you use them through a Claude Console account. Most organizations pay with prepaid usage credits. Organizations with an invoicing arrangement are billed monthly instead.

## Prepaid usage credits

Claude API and playground usage is billed through prepaid usage credits. Buy credits before you use the API, and they're applied to your usage according to our current **[pricing](https://claude.com/pricing#api)**. Credits cover API access, playground usage, and Claude Code.

You're billed only for successful API calls and completed tasks. Failed requests aren't charged.

**Note:** If your client disconnects or times out in the middle of a request that was on track to succeed, that request is still charged.

If you run out of credits, you can no longer call the API or use the playground until you add more.

## Buy credits

1. Log in to the Console with an Admin or Billing role.

2. Navigate to **[Settings > Billing](https://platform.claude.com/settings/billing)**.

3. Click "Buy credits."

4. Enter the amount of credits you want to purchase and confirm.

Purchased credits are available immediately. Your organization's available credit balance and credit usage are shown on the same **Billing** page.

## Set up auto-reload

Auto-reload purchases additional credits automatically when your balance falls below a threshold you set.

1. On the **Billing** page, click "Edit" in the **Auto-reload** section.

2. Toggle auto-reload on or off.

3. If auto-reload is on, set the minimum balance that triggers a purchase and the amount to reload to.

## Credit expiration and refunds

Purchased credits are subject to our **[Credit Terms](https://www.anthropic.com/legal/credit-terms)**. Credits expire one year from the purchase date, and the expiration date can't be extended. Expired credits appear in your **Invoice history** on the Billing page. All credit purchases are non-refundable.

Learn more about how credit usage relates to rate limits in the **[Claude API docs](https://platform.claude.com/docs/en/api/rate-limits)**.

## Monthly invoicing

Some organizations are billed monthly in arrears instead of buying credits upfront. This applies to Console organizations with an invoicing arrangement set up through our Sales team.

On monthly invoicing, we aggregate your usage across API calls, Console usage, and any other services associated with your account, and bill it at our standard **[pay-as-you-go pricing](https://claude.com/pricing#api)**. At the end of each calendar month, you'll receive an invoice from Stripe. Enter your payment details in Stripe to pay it.

You can view charges for the current billing period on the **[Billing](https://platform.claude.com/settings/billing)** page in your Console settings.

If you need custom rate limits, monthly invoicing, or hands-on support, **[contact our Sales team](https://claude.com/contact-sales)**.

## Update your Console payment method

1. Log in to the Console with an Admin or Billing role.

2. Navigate to **[Settings > Billing](https://platform.claude.com/settings/billing)**.

3. Click the pencil icon next to your current payment method.

4. Enter your new card details in the **Update payment method** modal, then click "Update."