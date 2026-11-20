---
title: App testing and review
url: https://platform.claude.com/docs/en/manage-claude/oauth-apps/app-review
description: How a new Linked billing app moves out of testing and opens to your customers, and what happens when you change a live app.
---

<Warning>
  Claude Platform OAuth is a Beta Service: prerelease software provided under your agreement with Anthropic, such as the [Commercial Terms of Service](https://www.anthropic.com/legal/commercial-terms), and the [Service Specific Terms](https://www.anthropic.com/legal/service-specific-terms). Endpoints, parameters, and behavior can change during the beta. It might not be suitable for production use.
</Warning>

With [Linked billing](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections), a customer links their Claude organization to your OAuth app. A new Linked billing app starts in testing, where only the test users that you name can link their organizations to it. To open the app to your customers, you publish it, and Anthropic reviews it.

If your organization has invoiced billing, Anthropic doesn’t review your app. See [Invoiced billing](https://platform.claude.com/docs/en/manage-claude/oauth-apps/app-review#invoiced-billing).

An app is live when Anthropic has approved it or when you have published it with invoiced billing. Any [eligible customer](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections#eligible-customers-and-endpoints) can link their organization to a live app, and the links that its test users made stay. On the OAuth apps page in the Claude Console, a live app’s status reads **Active**.

Until the app is live, the Console shows one of these statuses for it:

| Status | What it means |
| ----- | ----- |
| **Testing** | You haven’t published the app. |
| **In review** | Anthropic is reviewing the app or a change that you made while it was live. |
| **Not approved** | Anthropic reviewed the app or the change and didn’t approve it. |

An app that goes back to review after a change isn’t live again until Anthropic approves the change. Each app has its own status and its own test users. See the note in [Step 1: Create the app](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections#step-1-create-the-app) in the Linked billing guide.

## Before you begin

Complete the [Setup process](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections#setup-process) in the Linked billing guide.

## Manage test users

### Add test users

1. Open the app’s page from the [OAuth apps page](https://platform.claude.com/settings/oauth-apps) in the Console.
2. On the **Settings** tab, go to the **Test users** list under **Who can link**.
3. Enter the email address of a test user’s Claude account and click **Add**. Repeat for each test user.
4. Click **Save changes**.

After you save, the people on the list can link their organizations to your app. Until your app is live, the Claude approval page, where a person approves the link, refuses anyone else. For what your app then receives, see [Your redirect URI receives `error=access_denied`](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections#access-denied) in the Linked billing guide.

**Who can link** stays on **Test users only** while the app isn’t live, and you can’t change it. The list holds up to 10 test users. Each address has to match the account’s address exactly, but letter case doesn’t matter. An address with a plus tag, such as `name+test@example.com`, counts as a different address from `name@example.com`.

### Link a test user’s organization

A test user links their organization from your app and approves the link on the page that your customers use. They need the Admin or Billing role in that organization. The steps are Steps 4 to 8 of the Linked billing guide. [Test as a customer](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections#test-as-a-customer) in that guide takes you through them and says how to check that the link was made.

To test the app yourself, add your own email address to the list. The organization that owns the app can’t link to it, so use a second Claude organization of yours.

After a test user has linked their organization, [send requests that you bill to it](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections#step-3-update-calls-to-claude) to try your app. Testing uses real money. Anthropic charges each test user’s organization for the requests that you bill to it, as it does for any customer.

Until your app is live, each new link needs a monthly spend cap of $50 USD or less. For the cap’s rules, see [While your app is in testing](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections#while-your-app-is-in-testing) in the guide.

### Remove a test user

Removing a test user takes effect at once. It ends each link to your app that the person approved. After a link ends, the Claude API refuses the requests that you bill to that organization. See [Expected errors](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections#expected-errors).

1. If the **Settings** tab has unsaved changes, click **Save changes** or **Discard**. Until you do, the Console doesn’t let you remove a saved test user.
2. Remove the test user’s address from the **Test users** list.
3. When the Console asks, click **Remove** to confirm. You don’t need to click **Save changes**.

## Publish the app

Publishing can ask you to prove that you control your app’s domain by adding a DNS record. Anthropic then reviews the app. A DNS change takes time, so start before you need customers to link.

Before you publish, check these things:

* Client authentication is set up. You can’t publish the app until it is.
* Your app has a homepage, which you set on the **Appearance** tab.
* You can change the DNS records of the homepage’s domain.
* Each redirect URI is on the homepage’s domain or on one of its subdomains.

For what counts as the homepage’s domain and for the exceptions, see [Domain rules](https://platform.claude.com/docs/en/manage-claude/oauth-apps/app-review#domain-rules).

Follow these steps to publish the app:

1. On the app’s page in the Console, click **Publish app**. A dialog box opens.
2. If the dialog box shows **Prove your domain**, add the DNS TXT record that it gives you where you manage DNS for your domain. Otherwise, go to step 5.
3. Click **Check**. If the domain still shows **Not proven yet**, see [If you can’t prove the domain](https://platform.claude.com/docs/en/manage-claude/oauth-apps/app-review#if-you-cant-prove-the-domain).
4. When the domain shows **Proven**, click **Continue**.
5. If the dialog box shows a checkbox to accept the Linked Billing Terms, select it. Then, click **Publish app** in the dialog box to confirm.

While Anthropic reviews the app, its status is **In review**. For the outcomes, see [The review](https://platform.claude.com/docs/en/manage-claude/oauth-apps/app-review#the-review).

### If you can’t prove the domain

* **The domain still shows Not proven yet:** A DNS change can take up to 48 hours to take effect. You can close the dialog box and come back later. If you were publishing, click **Publish app** again. If you were changing a live app, make the same edit again, and the Console gives you the same record until it expires.
* **Check says that the record has expired:** The DNS record works for 30 days from when the Console first shows it. After that, click **Get a new record** and add the new record. A domain that shows **Proven** stays proven.
* **The dialog box shows a message in place of a record:** For example, the message can say that your organization already has 20 domain names. You can’t continue until that is resolved. If you need help, [contact support](https://support.claude.com/en/articles/9015913-how-to-get-support).

### Domain rules

A domain is a hostname without a leading `www.`, and your domain is your homepage’s. For example, the domain of a homepage at `https://www.example.com` is `example.com`. A proven domain covers itself and its subdomains.

* **Shared domains:** A hosting service’s shared domain doesn’t qualify, so use a domain of your own.
* **Local redirect URIs:** Redirect URIs on `localhost`, `127.0.0.1`, or `[::1]` don’t have to be on the homepage’s domain.
* **Sibling subdomains:** If your homepage is on `app.example.com`, your domain is that subdomain, and it doesn’t cover a redirect URI on `auth.example.com`. One way to use both is to put your homepage on `example.com`, which covers them.
* **A domain that your organization has already proven:** Your organization might have proven a domain earlier, for example for another app. If it covers your homepage and every redirect URI that isn’t local, the dialog box skips **Prove your domain**. The redirect URIs then don’t have to be on the homepage’s domain. For example, with `example.com` proven, the homepage and a redirect URI can be on different subdomains of it.

## The review

When the review ends, the app’s page in the Console shows the result:

* **Anthropic approves the app:** The app is live. **Who can link** then shows **Any Claude user** without any action from you, and the Console hides the **Test users** list.
* **Anthropic doesn’t approve the app:** The app’s status changes to **Not approved**.

During the review and after a **Not approved** result, your test users keep their links, and you can still add and remove test users.

### If the app isn’t approved

You can’t publish the app again yourself. To ask about the decision, [contact support](https://support.claude.com/en/articles/9015913-how-to-get-support). You can still [change the app](https://platform.claude.com/docs/en/manage-claude/oauth-apps/app-review#change-an-app-that-isnt-live), but a change doesn’t start a new review.

## Change a live app

A change to a live app’s name, logo, homepage, or redirect URIs sends the app back to review. Until Anthropic approves the change, only your test users can link their organizations to the app. See [Until Anthropic approves the change](https://platform.claude.com/docs/en/manage-claude/oauth-apps/app-review#until-anthropic-approves-the-change). Other changes, such as permissions or client authentication, don’t send the app back to review.

Follow these steps to change the name, homepage, or redirect URIs:

1. Change the app on its **Appearance** tab (name and homepage) or its **Settings** tab (redirect URIs).

2. Click **Save changes**. A dialog box opens before anything is saved.

3. If the dialog box shows **Prove your domain**, prove each domain that it names:

   1. Add the DNS TXT record for the domain. Then, click **Check**. If the domain still shows **Not proven yet**, see [If you can’t prove the domain](https://platform.claude.com/docs/en/manage-claude/oauth-apps/app-review#if-you-cant-prove-the-domain).
   2. When the domain shows **Proven**, click **Next domain** if another domain is left. Otherwise, click **Continue**.

4. Click **Save and send to review**.

The Console then saves the change, and the change takes effect without waiting for the review. While Anthropic reviews the change, the app’s status is **In review**.

To change the logo, choose or remove it on the **Appearance** tab. The dialog box opens at once. Click **Send to review**. If you cancel, the logo doesn’t change.

To change the app again while its status is **In review** or **Not approved**, see [Change an app that isn’t live](https://platform.claude.com/docs/en/manage-claude/oauth-apps/app-review#change-an-app-that-isnt-live).

### When the Console asks you to prove a domain

The Console asks only if you changed the homepage or a redirect URI. It also checks the homepage and the redirect URIs that you didn’t change, so the dialog box can name their domains too. It names only domains that no proven domain of your organization covers. It doesn’t check local redirect URIs, but a change to one still sends the app back to review.

After a change, the redirect URIs can be on domains other than the homepage’s if your organization proves each one.

### Until Anthropic approves the change

These rules apply from when you send the change to review:

* **Customers who have already linked:** Their organizations stay linked, and the requests that you bill to them keep working. A customer who unlinks can’t link again unless the person who links is on the **Test users** list.
* **New links:** The **Who can link** setting goes back to **Test users only**. The Console shows the **Test users** list again with the people who were on it before.
* **Test users:** You can add and remove people on the list. Removing a person also ends a link that they made to a customer’s organization while the app was live. See [Remove a test user](https://platform.claude.com/docs/en/manage-claude/oauth-apps/app-review#remove-a-test-user).
* **Spend caps of linked organizations:** A linked organization keeps its current [spend cap](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections#spend-caps) setting even if its cap is above $50 USD or it has no cap. A setting that it changes has to follow the rules in [While your app is in testing](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections#while-your-app-is-in-testing).

### When the review of the change ends

The review ends in one of two ways:

* **Anthropic approves the change:** The app is live again. Any eligible customer can link, the Console hides the **Test users** list, and the cap rules for an app that isn’t live no longer apply.
* **Anthropic doesn’t approve the change:** The app’s status changes to **Not approved**. The change stays in effect, and the rules in [Until Anthropic approves the change](https://platform.claude.com/docs/en/manage-claude/oauth-apps/app-review#until-anthropic-approves-the-change) still apply. See [If the app isn’t approved](https://platform.claude.com/docs/en/manage-claude/oauth-apps/app-review#if-the-app-isnt-approved).

## Change an app that isn’t live

Follow these steps while the app’s status is **Testing**, **In review**, or **Not approved**:

1. Change the app on its **Appearance** tab (name, logo, and homepage) or its **Settings** tab (redirect URIs).
2. Click **Save changes**. A logo change saves when you choose or remove the logo.

No dialog box asks you to confirm, and the change doesn’t alter the app’s status.

When you save a change to the homepage or a redirect URI, the Console checks domains only while the status is **In review**. An app in testing meets the domain check when you publish. During a review, the changed app’s homepage and every redirect URI that isn’t local have to be on proven domains of your organization. Otherwise, the Console refuses the change, and it doesn’t ask you to prove a domain. To move to a domain that isn’t proven, wait until the review ends.

## Invoiced billing

With invoiced billing, Anthropic invoices the organization that owns your app for its API usage, and that organization doesn’t buy prepaid credits. Your app still starts in testing, and the rules for test users and the spend cap still apply. After that, three things differ:

* **[Publish the app](https://platform.claude.com/docs/en/manage-claude/oauth-apps/app-review#publish-the-app):** On the app’s page, click **Publish app**. Then, click **Publish app** in the dialog box to confirm. Anthropic doesn’t review the app, so it is live as soon as you publish it.
* **Homepage and domain:** You prove no domain, so the dialog box skips **Prove your domain**. Your app needs no homepage to publish, and the rule for redirect URIs under [Publish the app](https://platform.claude.com/docs/en/manage-claude/oauth-apps/app-review#publish-the-app) doesn’t apply. Client authentication still has to be set up first.
* **[Change a live app](https://platform.claude.com/docs/en/manage-claude/oauth-apps/app-review#change-a-live-app):** The Console saves a change when you click **Save changes** or when you choose or remove a logo. It doesn’t ask you to prove a domain or to confirm, and no review follows.
