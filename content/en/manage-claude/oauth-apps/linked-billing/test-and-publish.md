---
title: Test and publish your app
url: https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/test-and-publish
description: Add test users, publish your Linked billing app so that any eligible customer can link it, and change the app once customers depend on it.
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

A new [Linked billing](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing) app starts in testing, where only the [test users](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/test-and-publish#manage-test-users) you name can link their organizations to it. To open it to your customers, you prove your domain and [publish the app](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/test-and-publish#publish-the-app), and Anthropic reviews it. This page also covers how the [spend cap works while you test](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/test-and-publish#caps-while-testing) and how to change or delete the app.

The [OAuth apps](https://platform.claude.com/settings/oauth-apps) page in the Claude Console displays each app’s status:

| Status | What it means |
| ----- | ----- |
| **Testing** | You haven’t published the app |
| **In review** | Anthropic is reviewing the app or a change to it |
| **Not approved** | Anthropic reviewed the app or the change and didn’t approve it |
| **Active** | The app is live: any [eligible customer](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing#eligible-customers) can link to it |

If Anthropic invoices your organization for its API usage, your app skips the review: see [If your organization has invoiced billing](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/test-and-publish#with-invoiced-billing).

## Before you begin

You need the Admin role in your organization and an app that’s [set up for Linked billing](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/set-up-your-app).

## Manage test users

Until your app is live, its **Who can link** setting reads **Test users only**, and you can’t change it. Only the people on its **Test users** list can link their organizations to it, and each app has its own list. The approval page refuses anyone else, and if they go back to your app, your app receives [`access_denied`](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/errors#access-denied). Each person who links while the app isn’t live must set a monthly spend cap of $50 USD or less: see [Caps while testing](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/test-and-publish#caps-while-testing).

### Add test users

Testing uses real money: Anthropic charges each test user’s organization for the requests that you bill to it, as for any customer. A test user [links an organization](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/link-and-bill-a-customer) where they have the Admin or Billing role. That organization can’t be the one that owns the app. To test the app yourself, add your own address and link a second Claude organization of yours.

1. Open the app from the [OAuth apps](https://platform.claude.com/settings/oauth-apps) page in the Console.
2. On the **Settings** tab, find the **Test users** list under **Who can link**.
3. Enter the email address of a test user’s Claude account and click **Add**. Repeat for each test user.
4. Click **Save changes**.

The list has these rules:

* It holds up to 10 people.
* An address must match the account’s address exactly, but letter case doesn’t matter. `name+test@example.com` is a different address from `name@example.com`.

### Remove a test user

<Warning>
  Removing a test user ends every connection to your app that they approved.
</Warning>

During a live app’s change review, that can include a connection to a customer’s organization. New requests that bill those organizations typically stop within about 10 seconds and are refused with [`user_profile_billing_not_authorized`](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/errors#user-profile-billing-not-authorized). A request with an ended connection’s access token can get a [`401 authentication_error`](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/errors#authentication-error) instead. To remove someone:

1. If the **Settings** tab has unsaved changes, click **Save changes** or **Discard**. The Console doesn’t let you remove a saved test user until you do.
2. Remove the person’s address from the **Test users** list.
3. When the Console asks, click **Remove**. You don’t need to click **Save changes**.

## Publish the app

Publishing can ask you to add a DNS record that proves you control your app’s domain. A DNS change can take up to 48 hours to take effect, so publish well before you need customers to link. Before you publish, check these things:

* [Client authentication](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/set-up-your-app#set-up-client-authentication) is set up. You can’t publish until it is.
* The app has a homepage, set on its **Appearance** tab, on a domain of your own. A hosting service’s shared domain doesn’t qualify.
* You can change the DNS records of the homepage’s domain.
* Each redirect URI is on the homepage’s hostname, without a leading `www.`, or a subdomain of it. For the exceptions, see [Domain rules](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/test-and-publish#domain-rules).

To publish the app:

1. Save any unsaved changes on the app’s tabs, because the Console doesn’t let you publish until you do. Then, click **Publish app** on the app’s page.
2. If the dialog box displays **Prove your domain**, add the DNS TXT record that it gives you, where you manage DNS for your domain. Then, click **Check**. If the domain doesn’t read **Proven**, see [If you can’t prove the domain](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/test-and-publish#if-you-cant-prove-the-domain). When it reads **Proven**, click **Continue**.
3. If the dialog box displays a checkbox to accept the Linked Billing Terms, select it. They’re the [Linked Billing Beta Terms](https://www.anthropic.com/legal/linked-billing-terms).
4. Click **Publish app** in the dialog box.

The app’s status is then **In review**. During the review and after a **Not approved** result, your test users keep their connections, and you can still add and remove test users. When the review ends, the app’s page displays the result, and Anthropic usually emails it to the person who published the app:

* **Approved:** The app is live, and its status on the OAuth apps page reads **Active**. **Who can link** reads **Any Claude user**, the Console hides the **Test users** list, and test users’ connections stay.
* **Not approved:** You can’t publish the app again yourself: see [If the app isn’t approved](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/test-and-publish#if-the-app-isnt-approved).

With invoiced billing, Anthropic doesn’t review your app: see [If your organization has invoiced billing](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/test-and-publish#with-invoiced-billing).

## Change a live app

<Warning>
  Changing a live app’s name, logo, homepage, or redirect URIs limits new connections to test users until Anthropic approves the change.
</Warning>

Until Anthropic approves the change:

* Customers who already linked stay linked, and the requests that you bill to them keep working.
* A customer who unlinks can link again only through a person on the **Test users** list.
* A change to a cap follows [Caps while testing](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/test-and-publish#caps-while-testing).

If Anthropic rejects the change, the limit stays: see [If the app isn’t approved](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/test-and-publish#if-the-app-isnt-approved). For the rest of the rules, see [While a change is in review or not approved](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/test-and-publish#while-a-change-is-in-review).

A change takes effect as soon as the Console saves it, so customers see it before the review ends. Changes to the app’s permissions or client authentication don’t start a review, and with [invoiced billing](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/test-and-publish#with-invoiced-billing), no change does.

To change the name, homepage, or redirect URIs:

1. Change the app on its **Appearance** tab (name and homepage) or its **Settings** tab (redirect URIs).
2. Click **Save changes**. A dialog box opens before anything is saved.
3. If the dialog box displays **Prove your domain**, prove each domain that it names, one at a time. For each, add its DNS TXT record, click **Check**, and when it reads **Proven**, click **Next domain** or **Continue**. For which domains it names, see [Domain rules](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/test-and-publish#domain-rules).
4. Click **Save and send**, which saves the change and sends it to review.

To change the logo, upload or remove it on the **Appearance** tab, then click **Send to review** in the dialog box that opens. If you cancel, the logo doesn’t change.

While Anthropic reviews the change, the app’s status reads **In review**. When the review ends, Anthropic usually emails the result to the person who saved the change.

## Change an app in testing or in review

Follow this section while the app’s status is **Testing**, **In review**, or **Not approved**. That includes a live app whose change is in review. Change the app on its **Appearance** tab (name, logo, and homepage) or its **Settings** tab (redirect URIs), then click **Save changes**. A logo change saves when you upload or remove the logo.

No dialog box asks you to confirm, and the status doesn’t change. During a review, the change replaces what Anthropic reviews with the app as you edited it.

The Console checks an app in testing for proven domains only when you publish. While the status is **In review**, the homepage and every redirect URI that isn’t local must already be on proven domains of your organization. Otherwise, the Console refuses the change and doesn’t ask you to prove a domain. To move to a domain that isn’t proven, wait until the review ends.

## Delete the app

<Warning>
  Deleting an app unlinks every customer and can’t be undone.
</Warning>

Requests that bill a customer are refused, every OAuth token is revoked, and the client ID stops working. Anthropic doesn’t email your customers, so tell them first. To delete the app:

1. On the app’s **Settings** tab, save or discard any unsaved changes.
2. Under **Danger zone**, click **Delete app** and confirm with **Delete app**. The app’s row menu on the [OAuth apps](https://platform.claude.com/settings/oauth-apps) page also has **Delete**.

To offer Linked billing again, create a new app, and have each customer link it. The new app starts in testing with a new client ID, and customers’ spend caps don’t carry over.

## Rules and special cases

The rest of this page covers the rules behind publishing and changing an app. It also covers cases such as a domain that won’t prove.

### Domain rules

A domain is a hostname without a leading `www.`, so a homepage at `https://www.example.com` has the domain `example.com`. Your domain is your homepage’s. A proven domain covers itself and its subdomains, and it stays proven.

* **Local redirect URIs:** Redirect URIs on `localhost`, `127.0.0.1`, or `[::1]` don’t have to be on the homepage’s domain.
* **Sibling subdomains:** A homepage on `app.example.com` doesn’t cover a redirect URI on `auth.example.com`. Put the homepage on `example.com` to cover both.
* **Domains your organization has already proven:** If they cover the homepage and every redirect URI that isn’t local, publishing skips **Prove your domain**. The redirect URIs then don’t have to be on the homepage’s domain.

When you change a live app, the Console asks you to prove a domain only if you changed the homepage or a redirect URI. It then checks every domain of the app, changed or not, and names each one that no proven domain of your organization covers. After such a change, redirect URIs can be on domains other than the homepage’s, if your organization proves each one. The Console doesn’t check local redirect URIs, but changing one still sends the app to review.

### If you can’t prove the domain

* **The domain still reads Not proven:** The DNS change hasn’t taken effect. Close the dialog box and come back later. If you were publishing, click **Publish app** again. If you were changing a live app, make the same edit again: the Console gives you the same record until it expires.
* **Check says that the record has expired:** A record works for 30 days from when the Console first displays it. Click **Get a new record** and add the new record.
* **The dialog box displays a message in place of a record:** The message might say, for example, that your organization already has 20 domain names. You can’t continue until that’s resolved. For help, contact [Anthropic support](https://support.claude.com/en/articles/9015913-how-to-get-support).

### If the app isn’t approved

You can’t publish the app again yourself, and a change doesn’t start a new review. To ask for another review, contact [Anthropic support](https://support.claude.com/en/articles/9015913-how-to-get-support). After a rejected change to a live app, the change stays in effect, and new connections stay limited to your test users.

### While a change is in review or not approved

From when you send a live app’s change to review until Anthropic approves it:

* **New connections:** **Who can link** goes back to **Test users only**. The Console displays the **Test users** list again with the people who were on it before.
* **Test users:** You can add and remove people.
* **Caps already set:** A linked organization keeps its cap setting, even above $50 USD or with no cap.

When the review ends, one of these happens:

* **Approved:** The app is live again. Any eligible customer can link, the Console hides the **Test users** list, and the testing cap rules stop.
* **Not approved:** The status changes to **Not approved**, and these rules still apply.

### Caps while testing

A customer’s spend cap for your app limits what you can bill them each month. The approval page calls it a monthly spend limit. These rules apply to the person who links and to the customer’s Admin and Billing members in the Console:

| Cap setting | While the app is in testing, in review, or not approved | While it’s live |
| ----- | ----- | ----- |
| A spend cap on the approval page | Required, $50 USD or less | Optional |
| The amount field on the approval page | Starts at $50 USD | Starts empty |
| **Continue without a limit** | Not offered | Offered |
| Removing the cap in the Console | Not possible | Possible |
| The largest cap they can set | $50 USD | No practical maximum |

Once the app is live, a cap that a customer saved while it was in testing stays in place. The customer can then raise or remove it. For the other rules on caps, see [Spend caps in What your customers see](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/what-your-customers-see#spend-caps).

### If your organization has invoiced billing

With invoiced billing, Anthropic invoices your organization for its API usage, and your organization doesn’t buy prepaid credits. Your app still starts in testing, and the rules for test users and caps still apply. After that, three things differ:

* To publish, click **Publish app** and then click **Publish app** in the dialog box. Anthropic doesn’t review the app, so it’s live as soon as you publish it.
* You prove no domain, and the app needs no homepage to publish. The rule for redirect URIs doesn’t apply. Client authentication still has to be set up first.
* A change to the live app saves when you click **Save changes** or when you upload or remove a logo. No domain check, confirmation, or review follows.

## Next steps

<CardGroup cols={2}>
  <Card title="Manage linked customers" icon="list" href="https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/manage-customers">
    See usage, check whether a customer is linked, and unlink or link them again
  </Card>

  <Card title="Use a separate credential for each customer" icon="lock" href="https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/credential-for-each-customer">
    Limit a credential to one customer, for single-tenant products and sandboxes
  </Card>
</CardGroup>
