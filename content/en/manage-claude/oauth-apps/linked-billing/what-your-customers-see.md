---
title: What your customers see
url: https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/what-your-customers-see
description: "Explain Linked billing to your customers: the approval page, their spend cap for your app, how a connection ends, and the emails they get."
featureMetadata:
  status: beta
  betaHeader: user-profiles-billing-2026-10-01
  supportedModels:
    - claude-fable-5-2
    - claude-mythos-5-2
    - claude-fable-5-1
    - claude-mythos-5-1
    - claude-fable-5
    - claude-mythos-5
    - claude-mythos-preview
    - claude-opus-5-5
    - claude-opus-5
    - claude-sonnet-5-5
    - claude-sonnet-5
    - claude-haiku-5-5
    - claude-haiku-4-5-20251001
    - claude-opus-4-8
    - claude-opus-4-7
    - claude-opus-4-6
    - claude-sonnet-4-6
    - claude-opus-4-5-20251101
    - claude-sonnet-4-5-20250929
  supportedPlatforms:
    Claude API:
      availability: beta
      note: Only requests that send `billing_policy` need the beta header.
---

<Warning>
  Claude Platform OAuth is a Beta Service: prerelease software provided under your agreement with Anthropic, such as the [Commercial Terms of Service](https://www.anthropic.com/legal/commercial-terms), and the [Service Specific Terms](https://www.anthropic.com/legal/service-specific-terms). Endpoints, parameters, and behavior can change during the beta. It might not be suitable for production use.
</Warning>

With [Linked billing](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing), your customers approve your app, set any [spend cap](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/what-your-customers-see#spend-caps) for it, and unlink it on Anthropic’s pages, not in your product. Anthropic also sends them emails. Your product and support teams can use this page to explain Linked billing to customers. Your engineers can use it to plan for what your app can’t see.

## How it works

For example, an Admin at Acme approves your app on Claude’s approval page and sets a monthly spend cap of $200 USD for it. Later, Acme can change the cap or unlink your app on its [Linked platforms](https://platform.claude.com/linked-platforms) page. Anthropic emails Acme’s Admin and Billing members when the connection is made and when Acme unlinks your app. It also emails them when spend reaches 80 percent of the cap.

### Approving your app

The approval page is on `auth.claude.com`. It uses whichever Claude account is signed in to the browser and offers only that account’s Claude organizations. The person who approves needs the Admin or Billing role in the organization that they link. Every screen displays your app’s name and has a **Cancel** button:

| Screen | What the person does |
| ----- | ----- |
| **Select an organization** | Selects the Claude organization to link (appears only if they have a choice) |
| **How billing works** | Reads that the organization pays for this usage at its own rates and clicks **Continue** |
| **Set a monthly spend limit** | Enters your app’s spend cap in whole US dollars or clicks **Continue without a limit** and confirms |
| The last screen | Reviews what your app can do, including the cap, and clicks **Link and authorize** |

On the **Set a monthly spend limit** screen, the amount field starts empty. **Continue without a limit** saves no new cap. A cap that the customer saved earlier for your app still applies. Without one, their [default cap](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/what-your-customers-see#spend-caps) applies. Until your app is live, other rules apply: see [Caps while testing](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/test-and-publish#caps-while-testing).

After **Link and authorize**, the browser goes back to your app with no confirmation screen.

In these cases, the approval goes differently:

* **The wrong account is signed in:** The person might be signed in with a personal account instead of a work account, for example. The page displays which account is signed in and lets the person switch. Your app can’t choose the account: the OpenID Connect parameters `prompt=select_account` and `login_hint` don’t change it. The page can also ask a signed-in person to sign in again.
* **The account belongs to no Claude Platform organization:** The page offers **Set up Claude Platform**, which opens the Claude Console to create an organization and then returns to the approval. Until that organization has billing set up, requests billed to it get [`user_profile_not_billable`](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/errors#user-profile-not-billable).
* **The person has no organization that they can link:** They don’t have the Admin or Billing role in any Claude organization that’s [eligible to link](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing#eligible-customers), so the page has no organization to offer. If they go back to your app, it receives the `access_denied` error. For its other causes, see [`access_denied` in Linked billing errors](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/errors#access-denied).
* **The person clicks Cancel:** No connection is made. When the browser comes back, your app receives `access_denied`.

### After linking

The connection belongs to the customer’s whole Claude organization, not to the person who approved it, so it stays if that person leaves. The customer manages it on the [Linked platforms](https://platform.claude.com/linked-platforms) page in their Claude Console. There, a member with the Admin or Billing role can see what your app has cost this month. They can also set a spend cap for it. To unlink it, they click your app, then **Unlink**, and confirm in the dialog box.

A connection ends in these ways, and some of them email the customer’s Admin and Billing members:

| How the connection ends | Email to the customer |
| ----- | ----- |
| The customer unlinks your app | Yes, without naming who unlinked it |
| Your back end ends the connection through the API | Yes |
| An Admin of your organization unlinks the customer in the Console | No |
| Your back end [reuses a refresh token](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/credential-for-each-customer#if-a-refresh-fails) more than 30 seconds after its first use | No |
| You remove the test user who approved it from your app’s **Test users** list | No |
| The customer approves again with other scopes, which replaces the connection with a new one, so the customer stays linked | No |
| You [delete your app](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/test-and-publish#delete-the-app), which ends every connection at once | No |

If your app still exists and no new connection replaces the ended one, requests billed to that customer are typically refused within about 10 seconds. The error is [`user_profile_billing_not_authorized`](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/errors#user-profile-billing-not-authorized). A request with the ended connection’s access token can get a [`401 authentication_error`](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/errors#authentication-error) instead. Their profile reads **Unlinked** on your User profiles page, and you can [link them again with the same profile](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/manage-customers#link-a-customer-again).

### Spend caps

Your app’s spend cap is an amount in US dollars that limits what your app can bill a customer each month. The approval page labels it a monthly spend limit. Two other settings are easy to confuse with it:

* **The organization’s Monthly spend limit:** It limits all of the organization’s usage and is set under [Spend limits](https://platform.claude.com/settings/billing#spend-limits). Your app’s cap can be higher than it.
* **The customer’s default cap:** It applies in full to each linked app that has no cap of its own.

Your app’s cap or the organization’s limit can refuse the requests that you bill to the customer, with the [`linked_organization_spend_limit_reached`](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/errors#linked-organization-spend-limit-reached) error. So can a lack of [credit that can pay](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing#which-credits-can-pay). The error doesn’t say which. Your app’s cap works this way:

* Refusals last until 00:00 UTC on the first day of the next month or until the customer raises or removes the cap.
* The cap counts token costs and web search fees at list prices, before any negotiated discount. The customer’s bill can therefore differ from what the cap counts, and a customer with a discount can reach the cap before their bill does.
* The request that crosses the cap is still served, and requests already running finish. The total can therefore end above the cap, by more when many requests run at once.
* A change to the cap takes about a minute to apply. The smallest cap is $0 USD, which refuses every request. The Console takes whole dollars and has no practical maximum once your app is live.
* Anthropic emails the customer’s Admin and Billing members at 80 percent of the cap and again at the cap, except for a $0 USD cap.

On the Linked platforms page, a member with the Admin or Billing role manages caps:

* **Set or change your app’s cap:** Click your app, then **Set spend cap** or **Edit spend cap**.
* **Set a default cap:** Under **Default spend cap**, click **Set default** or **Edit**.
* **Remove your app’s cap:** Click your app, **Edit spend cap**, and then **Remove cap**. Your app then uses the default cap or has no cap.

### Emails

Anthropic emails the customer at these times:

* When linking completes
* When a connection ends in one of the [ways that send email](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/what-your-customers-see#after-linking)
* At [80 percent of a cap and at the cap](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/what-your-customers-see#spend-caps)

Emails about linking and unlinking link to the customer’s Linked platforms page. Some organizations get no emails at all. Whether linking sends an email depends on the code exchange:

| Event | Email to the customer |
| ----- | ----- |
| Your back end exchanges the code after the customer approves | Yes |
| The customer approves, but your back end never exchanges the code | No |
| The customer approves again while still linked | No |

## Decide how to keep customers informed

Your app can’t see some of what the customer sees, so plan what your product tells them:

* **Unlinks:** Anthropic doesn’t tell you when a customer unlinks: you get no webhook event and no email. [Decide how often to check](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/manage-customers#decide-how-often-to-check-link-status) whether customers are still linked.
* **Caps:** You can’t see a customer’s cap or how much of it they’ve used. When requests are refused with `linked_organization_spend_limit_reached`, ask the customer to check their cap for your app, their organization’s **Monthly spend limit**, and their credit.
* **Emails:** Anthropic doesn’t guarantee that an email is sent or delivered. Tell the customer yourself whenever you unlink them, and don’t rely on email to tell them that they’re linked.

## Next steps

<CardGroup cols={2}>
  <Card title="Link your Claude organization button" icon="code" href="https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/link-button">
    The button’s HTML, CSS, colors, and logo
  </Card>

  <Card title="Link and bill a customer" icon="link" href="https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/link-and-bill-a-customer">
    Link a customer and bill requests to them, starting with a test customer
  </Card>
</CardGroup>
