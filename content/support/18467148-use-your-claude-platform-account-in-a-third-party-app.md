# Use your Claude Platform account in a third-party app

This article explains linked billing, which lets an administrator (Admin or Billing member) link your Claude Console organization to an app. You pay Anthropic directly for your usage in that app, and you never share an API key.

Linked billing is in beta, and not every app offers it yet.

## How linked billing works

Some apps run Claude for you, and you may have shared your API key with one. With linked billing, you approve a connection instead. The app never receives your API key or your Claude password. Anthropic bills your organization directly for Claude usage in that app.

The app runs Claude in its own organization, not yours. Only the billing goes to you. Settings in your organization, such as IP allowlists, encryption keys, and data retention (including zero data retention), don't apply to these requests.

This connection changes how this usage is billed. It doesn't change the terms or data arrangements that apply to your organization's use of Claude in the app.

## Who can link an app

Your organization must be billed directly by Anthropic, and only a user with the Admin or Billing role in your organization can approve a connection. If you don't have one of these roles, pass the request to someone who does. Learn more about **[Claude Console roles and permissions](https://support.claude.com/en/articles/10186004-claude-console-roles-and-permissions)**.

The following can't be linked:

- Organizations that get Claude through a cloud provider, such as Bedrock, Vertex AI, or Foundry, can't link

- Claude subscription plans (Pro, Max, Ultra, Team, and Enterprise) can't be linked

- Claude Console organizations that pay through the AWS, Google Cloud, or Azure marketplace can’t use linked billing

If you don't have a Claude account or Claude Console organization yet, you can create them for free while you link. Add credits before the app makes requests.

One approval covers your whole organization. The link belongs to the organization, so it stays active if the approver leaves. Your organization can have one link per app.

## Link an app

To link an app:

1. In the app, click the button to link your Claude organization.

2. Sign in to Claude. If you have more than one organization, pick the one to link.

3. Read how billing works, then set a monthly spend limit or select "Continue without a limit." If the app is still in testing, you must set a limit of $50 or less.

4. Review the approval screen. It shows the app's name and asks for permission to bill your organization for the Claude requests the app makes for you. It also says usage is billed under your organization's existing billing terms.

5. Select "Link and authorize." You return to the app.

Your organization's Admin and Billing members usually get an email that confirms the link.

## Set a spend limit

Set a monthly limit (Console calls this a spend cap) for each app on the **[Linked platforms](https://platform.claude.com/linked-platforms)** page in the Claude Console. You can also set a default limit that applies to each app separately. It isn’t a shared cap across apps.

To set a limit for one app, open its page under **Linked platforms**. A limit set there replaces your default limit. Your organization's own monthly limit is under **Spend limits**.

Limits are optional and in US dollars. The exception is an app in testing, which needs a limit of $50 or less. Set a whole-dollar amount from $1, or $0 to refuse every request from the app. Your organization's own monthly limit still applies, and requests are refused when you reach either one.

When you reach the limit, requests from that app are refused until you raise it or the month resets on the 1st (UTC).

The limit isn't exact. The request that crosses the limit is still served, and calls already running also finish, so your total can end up a little above the limit.

Your organization's admins get an email when usage in an app reaches 80% of the limit, and another at 100%. A $0 limit sends no email. Some organizations don't get these emails.

Usage is counted at list price. It includes tokens and web searches. The amount counted can differ from the amount on your invoice.

## Unlink an app

A user with the Admin or Billing role can unlink an app on the **[Linked platforms](https://platform.claude.com/linked-platforms)** page. An app may also let you unlink from inside it. The app's team can unlink it from their side. However the link ends, the app then shows as **Unlinked** on that page.

If you unlink the app, your organization's Admin and Billing members usually get an email. If the app's team unlinks it, they may not get one.

New calls usually stop within about 10 seconds. Calls already running finish and are billed to your organization. Past usage stays in **Usage** and **Billing**. To link the app again, approve the connection.

## How linked usage is billed

Anthropic bills linked usage, not the app. Any subscription the app charges is billed separately by the app. Learn more about **[how to pay for your Claude API usage](https://support.claude.com/en/articles/8977456-how-do-i-pay-for-my-claude-api-usage)**.

Linked usage is billed to your organization's prepaid balance or invoice. Some promotional credits can't be used.

### What can pay

- Credit you've purchased (your prepaid balance)

- Your invoice, if you're billed monthly

- Billing corrections from Anthropic

- Credits written into your agreement

### What can't pay

- **[Monthly API credits that come with Max, Ultra, and Team plans](https://support.claude.com/en/articles/17154008-monthly-api-credits-for-max-ultra-and-team-plans)**

- Sign-up credits limited to specific products

- Credits from Anthropic's partner, venture capital, and startup programs

### What to expect

- If nothing on your account can pay, the app's requests may be refused. After you add funds, the purchase can take some time to apply.

- Your purchased balance may go down while a promotional balance stays the same.

- We may update this list as our credit programs change.

## View linked usage

The **Linked platforms** page in the Console lists each linked app, and you can set limits and unlink there. The page also shows what each app has cost you this month.

## Frequently asked questions

### Can my organization link if it has HIPAA, FERPA, or CMEK requirements?

Not during the beta. Linked requests run in the app's organization, so your organization's business associate agreement (BAA), encryption keys, and retention settings, including zero data retention, don't apply.

## Get help

For questions about the app, contact the app's team. For questions about your organization or your bill, contact **[our support team](https://support.claude.com/en/articles/9015913-how-to-get-support)**.