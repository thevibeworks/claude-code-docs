# Offer linked billing in your platform

This article explains how to offer linked billing, which lets your customers link their own Claude Console organization to your app. We bill them directly, and you never hold their API key.

Linked billing is in beta.

## How linked billing works

A customer links its Claude Console organization to your platform using OAuth instead of pasting in an API key. Your platform holds a connection ID, not a key. You run Claude for the customer, and we bill the customer directly.

## What linked billing covers

Linked billing covers the `/v1/messages` and `/v1/chat/completions` endpoints. You choose who pays on each request: the customer or you.

The Message Batches API and Claude Managed Agents aren't covered yet.

Customer-paid requests can't use billable code execution. The API returns a 400 error, so send those requests as platform-paid.

If only some features bill the customer, tell customers which ones. Don't say all Claude usage is billed to their organization unless it is.

Linked billing works only for customers whose Claude Console organization is billed directly by Anthropic.

The following can't be linked:

- Customers who get Claude through a cloud provider, such as Bedrock, Vertex AI, or Foundry, can't link

- Claude subscription plans (Pro, Max, Ultra, Team, and Enterprise) can't be linked

- Claude Console organizations that pay through the AWS, Google Cloud, or Azure marketplace can’t use linked billing

Requests run in your platform's organization, not the customer's. Only the billing goes to the customer. Settings in the customer's organization, such as IP allowlists, encryption keys, and data retention, don't apply, and content is handled under your organization’s agreement with Anthropic.

All of your linked customers share your organization's rate limits, model access, and service tier.

## Move customers from API keys

You can keep offering customer API keys alongside linked billing and move customers over at your own pace.

To move a customer:

1. Keep using the customer's API key until you've stored their connection ID.

2. Mark the customer's requests as customer-paid.

3. Delete the stored API key and tell the customer you did.

## Set up linked billing

To set up linked billing:

1. Create an OAuth app in the Claude Console.

2. Under **What the app can do**, select "Bill and link to organizations."

3. Accept the Linked Billing Terms when prompted.

4. On the app's **Client authentication** tab, set up client authentication, an operator service account, and a default workspace.

5. Add a button to your app that starts linking, such as "Link your Claude organization." Use our **[branding samples](https://platform.claude.com/docs/en/manage-claude/oauth-apps/branding-samples)**.

6. Create one user profile for each customer organization that will pay. Each app allows one profile per customer organization, and one customer organization per profile.

7. On each request the customer should pay for, send the customer's profile ID, the billing beta header, and `billing_policy` with `bill_to` set to `user_profile`.

8. Publish the app when you're ready for customers.

A new app starts in testing. Only the test users you list (up to 10) can link it, each with a monthly limit of $50 or less. Unless your organization has invoiced billing, you verify your app's domain, and Anthropic reviews the app before it's live.

### Linking rules

- If a customer's organization is already linked to your app through another profile, the link is refused.

- A profile that's already linked to your app can't be linked to a second organization.

- To move a link, unlink it first, and then link again.

- You can't link your app to the Claude Console organization that owns it. To test linked billing as a customer would, use a second Claude Console organization that can link.

- Use the same user profile ID to start the link and to make that customer's requests.

- A customer-paid request that names a profile with no link is refused with a 403 error, even when the customer's Console shows your platform as **Linked**.

- A customer-paid request that names another of your customers' profiles is billed to that customer.

To pay for your own usage, send requests without `billing_policy`.

For the full steps and header values, see the **[Claude Platform Docs](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections)**.

## What customers see when they link

When customers link their organization:

1. They click the button you added to your app, such as "Link your Claude organization."

2. They sign in to Claude. If their email belongs to more than one organization, they pick one. If they don't have a Claude account or Claude Console organization yet, they can create them here, add credits, and then come back to finish linking.

3. They read how billing works, then set a monthly spend limit for your app or continue without one. If your app is still in testing, they must set a limit of $50 or less.

4. They see an approval page with your app's name and what you're asking for. It says usage is billed under the organization's existing billing terms.

5. They approve and return to your app.

Only a user with the Admin or Billing role can approve. Learn more about **[Claude Console roles and permissions](https://support.claude.com/en/articles/10186004-claude-console-roles-and-permissions)**. If anyone else tries to approve, we send them back to your app with an access denied error. Plan a handoff, such as a way to pass the request to an administrator.

One approval covers the whole organization. The link belongs to the organization, so it stays active if the approver leaves. Each organization can have one link per app.

After the approval, the customer's Admin and Billing members usually get an email that confirms the link, and another if they unlink.

## How customers manage a link

Customers manage every link on the **[Linked platforms](https://platform.claude.com/linked-platforms)** page in the Claude Console. They can set a monthly spend limit for your platform and unlink at any time. Link to this page from your app.

You can also unlink a customer. An Admin in your organization does this on the **[User profiles](https://platform.claude.com/user-profiles)** page. The customer gets no email when you unlink them in the Console, so tell them yourself. You can also unlink a customer from your back end, and Anthropic usually emails them when you do.

You can also create, list, and update your customers' profiles with the **[User Profiles API](https://platform.claude.com/docs/en/manage-claude/user-profiles)**.

## Manage unlinked customers

Anthropic doesn't send your app a notification when a customer unlinks. You find out when a customer-paid request for that customer is refused with a 403 error, or from the **Link status** on your **User profiles** page in the Console. A 403 can also mean the customer can't be billed for another reason.

A **Linked** status only says that the link exists. A request can still be refused, for example, when the customer is out of credit or has reached a spend limit.

Unlinking usually stops new calls within about 10 seconds. Calls already running finish and are billed to the customer. Show the customer a clear message and a way to link again.

## Manage billing errors

If a customer can't be billed, we refuse the request. We don’t bill you for that request.

- If the customer has reached its spend limit or Anthropic can't currently bill it (for example, because it's out of credits or suspended), you get a 402 error.

- If Anthropic can't bill the customer for any other reason, you get a 403 error.

- If Anthropic can't confirm right now whether the customer can be billed, you may get a 503 error. Retry with backoff, and don't show the customer an error.

A 402 means that the customer has to act. Ask them to check their limits and billing in the Claude Console.

You decide what happens next. You can pause the feature until the customer acts, or you can cover the usage yourself by resending the request as platform-paid. If you cover it, tell the customer for how long.

## Monitor usage and spend

You see each customer's usage and what it costs you. You never see what the customer actually pays.

You can monitor each customer's usage in two ways:

- **In the Claude Console:** Select a customer on the **[User profiles](https://platform.claude.com/user-profiles)** page to see its usage. **Your spend** is only what you paid on the customer's behalf.

- **With the API:** Group results by `user_profile_id` in the **[Usage and Cost Analytics API](https://platform.claude.com/docs/en/manage-claude/usage-cost-analytics-api)**, which is in beta. The usage endpoint returns tokens. On the cost endpoint, `amount` is your cost before credits, and it's 0 for requests that your customer pays for. `list_amount` is the cost at list price, whoever pays.

Both views include every request for the customer, whoever paid. Keep your own record of which requests were customer-paid. API data typically refreshes within four hours and can take up to 24 hours.

## Frequently asked questions

### Can customers with HIPAA, FERPA, or CMEK requirements link?

Not during the beta. Linked requests run in your organization, so a customer's business associate agreement (BAA), encryption keys, and retention settings, including zero data retention, don't apply. Don't link customers who need HIPAA, FERPA, or CMEK coverage.

### Which credits can pay for linked usage?

Linked usage is billed to the customer's prepaid balance or invoice. Some promotional credits can't be used.

**What can pay**

- Credit the customer purchased (its prepaid balance)

- The customer's invoice, if it's billed monthly

- Billing corrections from Anthropic

- Credits written into the customer's agreement

**What can't pay**

- **[Monthly API credits that come with Max, Ultra, and Team plans](https://support.claude.com/en/articles/17154008-monthly-api-credits-for-max-ultra-and-team-plans)**

- Sign-up credits limited to specific products

- Credits from Anthropic's partner, venture capital, and startup programs (we're still rolling this out)

If nothing on the customer's account can pay, its requests may be refused. After the customer adds funds, the purchase can take some time to apply. We may update this list as our credit programs change.