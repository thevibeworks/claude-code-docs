# Understanding your Claude API invoices

This article explains the invoices and receipts you'll receive for Claude API and Console usage, where to find them, and how to read the line items on them.

## Types of invoices you may receive

**Usage invoices.** If your organization is on a paid usage contract, we aggregate your usage across API calls, playground chats, and other services on your account, and you'll receive an invoice from Stripe at the end of every calendar month.

**Credit purchase receipts.** If your organization uses prepaid billing, you'll receive a receipt for each usage credit purchase, including purchases made automatically by auto-reload.

For details on how billing works, see **[How do I pay for my Claude API usage?](https://support.claude.com/en/articles/8977456)**

## Find your invoices

After each charge, we automatically email the invoice to your registered billing email address. To find a past invoice in your inbox, search for the subject line "Your receipt from Anthropic."

Invoices are also available in the Console to users with the Admin or Billing role:

1. Log in to the Console with an Admin or Billing role.

2. Go to **[Console Settings > Billing](https://platform.claude.com/settings/billing)**.

3. Find the **Invoice history** section.

4. Click "Download" to save the invoice directly, or click "View" to open it in a new Stripe tab and download it from there.

Expired credit grants also appear in **Invoice history**, even though they aren't charges. For help accessing older receipts and invoices that aren't available in the Console, **[contact our Support team](https://support.claude.com/en/articles/9015913)**.

## Read your invoice

**Applied balance.** An "Applied balance" line means an existing balance on your account was automatically applied to the invoice, reducing the amount due. A negative applied balance is credit being used, not a new charge or a discount. It comes from one of two places:

- A previous invoice totaled less than the minimum amount our billing system can charge ($0.50), so it rolled into this invoice.

- Your account carried a credit—for example, from a credit note or an overpayment—and it was applied automatically.

**Amount due.** The invoice total minus any applied balance. This is what your payment method is charged, or what you pay if your organization pays by bank transfer.

## Billing details on your invoice

The name, address, and tax information on an invoice come from your billing details at the time the invoice was issued. If you update your billing details, the changes apply to future invoices—issued invoices can't be modified. To update your details, go to **[Console Settings > Billing](https://platform.claude.com/settings/billing)**.

## Frequently asked questions

### Why is my invoice still past due after I paid?

If you pay by bank transfer, the payment must match the invoice amount exactly. A payment that's short by even a few cents won't be applied, and the invoice stays past due until the remaining amount arrives. Once the full amount is received, the invoice is marked paid automatically—this can take around five business days to process.

### Why didn't I receive an invoice for a small amount of usage?

Invoices below $0.50 aren't charged on their own. The amount rolls forward and appears as an applied balance on your next invoice.

### Can you correct the details on an invoice I already received?

No. Issued invoices can't be changed. Update your billing details in **[Console Settings > Billing](https://platform.claude.com/settings/billing)** and the changes will appear on future invoices.