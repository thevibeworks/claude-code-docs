---
title: Set up your app for Linked billing
url: https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/set-up-your-app
description: Register your product as an OAuth app in the Claude Console and give your back end an identity that can bill your customers with Linked billing.
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

With [Linked billing](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing), your customers pay for the Claude usage in your product through their own Claude organization. Before any customer can link, you set up your app once in the Claude Console.

When you’re done, your app has a client ID, [client authentication](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/set-up-your-app#set-up-client-authentication), an [operator service account](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/set-up-your-app#service-account), and a [default workspace](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/set-up-your-app#default-workspace). You’ve also chosen [whether to get refresh tokens](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/set-up-your-app#choose-whether-to-get-refresh-tokens). The end of the page covers changes to an app that customers already use.

## Before you begin

* **The Admin role:** You need the Admin role in your Claude organization for every step on this page.
* **An identity provider for your back end:** Your back end proves who it is with short-lived tokens from your own identity provider, through Workload Identity Federation.
* **An organization that Anthropic bills directly:** Your organization must pay Anthropic directly for its API usage, through prepaid credits or invoiced billing. An organization billed through a cloud marketplace can’t bill customers this way.

If your identity provider isn’t among the [identity providers](https://platform.claude.com/docs/en/manage-claude/workload-identity-federation#identity-providers), you can register any OpenID Connect provider as a [federation issuer](https://platform.claude.com/docs/en/manage-claude/workload-identity-federation#federation-issuers).

## Create the app

The app is your product’s registration with Anthropic. It ties your redirect URI, the address in your product that receives the browser after a customer approves, to a client ID.

1. On the [OAuth apps](https://platform.claude.com/settings/oauth-apps) page in the Console, click **Create**.

2. Enter your app’s name and redirect URI.

   * **Name:** Customers see it when they approve, so start it with your product’s name, as “Example Analytics for Claude” does. It can’t start with “Claude” or “Anthropic” or a look-alike, and it can’t put “official” next to either.
   * **Redirect URI:** The address must follow the [redirect URI rules](https://platform.claude.com/docs/en/manage-claude/oauth-apps/endpoints-and-parameters#redirect-uri-rules).

3. Under **What the app can do**, make sure that **Bill and link to organizations** is selected. This gives the app the `billing:attribution` scope, which lets it bill your customers.

4. Select the checkbox **I accept Linked Billing Terms on behalf of** your organization and click **Continue**. Those terms are the [Linked Billing Beta Terms](https://www.anthropic.com/legal/linked-billing-terms).

5. When the dialog box asks for client authentication, click **Skip for now**. The Console creates the app, and you set up client authentication in the next section. Until then, the app’s page warns that it can’t authenticate.

6. Copy the **Client ID** at the top of the app’s page. It starts with `clid_`. Every request to `auth.claude.com`, Anthropic’s authorization server, carries it, including the redirect that sends a customer to the approval page. The client ID is public.

7. On the **Appearance** tab, enter your homepage and click **Save changes**.

8. Upload your logo, a square PNG or JPEG file, 256 to 2,048 pixels a side and at most 2 MB. It saves at once. Without a logo, customers see your app’s initials.

A new app starts in testing. Until it’s live, only people on its **Test users** list can link it: see [Publish the app](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/test-and-publish#publish-the-app).

## Set up client authentication

Your back end proves that a request to `auth.claude.com` comes from your app with a client assertion: a short-lived JWT that your identity provider issues to your back end. Anthropic doesn’t issue client secrets for OAuth apps. To set up client authentication:

1. On the app’s **Client authentication** tab, select your **Identity provider**, the issuer that signs your back end’s tokens, such as AWS, Google Cloud, or Kubernetes. To add one, click **Register a new issuer**, fill it in, and click **Register**, or see [Workload Identity Federation](https://platform.claude.com/docs/en/manage-claude/workload-identity-federation).
2. Set a **Subject pattern** that your back end’s tokens match in their `sub` claim, or set claim conditions under **Advanced match options**. `auth.claude.com` accepts any token from your identity provider that matches them, so make them as narrow as your back end allows. For the pattern’s syntax, see [Rule matching semantics](https://platform.claude.com/docs/en/manage-claude/wif-reference#rule-matching-semantics).
3. Click **Save**. The tab then displays the **Expected audience**.
4. Have your identity provider issue your back end’s client assertions with exactly that audience in their `aud` claim. Keep their lifetime short, within your issuer’s [maximum lifetime](https://platform.claude.com/docs/en/manage-claude/wif-reference#jwt-verification), 1 hour by default: anyone who intercepts a client assertion can use it until it expires.

For every claim that a client assertion must contain, see [Client assertion claims](https://platform.claude.com/docs/en/manage-claude/oauth-apps/endpoints-and-parameters#client-assertion-claims).

## Give your back end an identity

Your back end calls the Claude API as a service account, which is a non-human account in your Claude organization. The one that you choose as the app’s operator is the only account that can bill your linked customers. It bills in one of two ways:

* With its own credential, naming a customer’s [user profile](https://platform.claude.com/docs/en/manage-claude/user-profiles)
* Through a customer’s [own OAuth access token](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/credential-for-each-customer), which counts as that account and can bill only that customer

### Choose the operator service account

The service account authenticates with its own federation rule, which is separate from client authentication. Client authentication proves that a request to `auth.claude.com` comes from your app. The federation rule lets your back end call the Claude API as the service account.

1. [Create a service account and its federation rule](https://platform.claude.com/docs/en/manage-claude/workload-identity-federation#set-up-federation).

   * **An account of its own:** Use a service account that isn’t the operator of another app, because each app needs its own.
   * **The rule’s scope:** Keep the default scope, `workspace:developer`, which your back end needs to create user profiles, check whether customers are linked, and unlink them. Don’t add `org:admin`, which covers the whole Admin API.
   * **The rule’s audience:** If you leave it blank, it usually differs from your app’s **Expected audience**, so you need two JWTs: see [when the two audiences differ](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/link-and-bill-a-customer#if-the-audiences-differ).

2. On the app’s **Client authentication** tab, under **Operator service account**, select the service account and click **Save**.

<Warning>
  Once customers are linked, changing or archiving the operator service account can stop some or all billing as your app.
</Warning>

A change stops customers’ OAuth tokens from billing, and an archive stops all billing as your app. To recover from either, see [If you change the service account](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/set-up-your-app#if-you-change-the-service-account).

### Choose the default workspace

Requests that use a customer’s own access token run in one workspace of your organization, the app’s default workspace. Every new app needs one, even if you never use those tokens. In the last step of linking, your back end exchanges a one-time code for a connection to the customer’s organization. Without a default workspace, that exchange fails with `unauthorized_client`. That refusal doesn’t use up the code, so you can set the workspace and send the same code again within its 5 minutes.

The setting appears once an operator service account is saved:

1. On the app’s **Client authentication** tab, under the operator service account, find **Default workspace for platform auth mode OAuth tokens** (the app’s `connection_token_workspace_id` setting) and click **Choose workspace**.
2. Select a workspace that isn’t archived and that the service account is a member of, and click **Save**. Every service account is a member of your organization’s built-in workspace named **Default**, so you can always select that one.

<Warning>
  Once a customer is linked, don’t archive the app’s default workspace: archiving revokes every OAuth token that runs in it, and it can’t be undone.
</Warning>

To use another workspace, follow [If you move to another workspace](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/set-up-your-app#if-you-move-to-another-workspace).

## Choose whether to get refresh tokens

Each connection gives you an access token for its customer, which can bill only that customer and expires within 1 hour. A refresh token gets new access tokens without asking the customer again. What decides is how your back end bills:

* **Only with the operator service account’s own credential:** Leave **Offline access** off.
* **With customers’ own access tokens:** Turn on **Offline access**. You bill this way if code that you don’t fully control calls Claude for a customer, such as an agent in a sandbox. You also bill this way if you want every billed request to use the customer’s own access token.

To get refresh tokens, go to the app’s **Permissions** tab and turn on **Offline access**, which lets you ask for the `offline_access` scope. Then, ask for `billing:attribution offline_access` when you [send each customer to approve](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/link-and-bill-a-customer#send-them-to-approve). Turn it on before your customers link. If you turn it on later, each linked customer must [approve again](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/set-up-your-app#implementation-details) to give you a refresh token. You don’t unlink them first.

If the **Permissions** tab also lists the deprecated scope `org:billing_attribution`, removing it can’t be undone: see [If you still use the deprecated scope](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/set-up-your-app#if-you-still-use-the-deprecated-scope).

## Check the result

On the app’s page in the Console, check these:

* The page displays no warning that the app can’t authenticate.
* The **Client authentication** tab displays your identity provider and its **Expected audience**.
* The same tab displays your operator service account and the app’s default workspace.
* The **Permissions** tab displays `billing:attribution` turned on under **Billing**.
* If you chose refresh tokens, the **Permissions** tab also displays **Offline access** turned on.

A saved change can take a few minutes to reach `auth.claude.com`. Wait a few minutes after your last change before you link a customer.

## Decide whether to use a separate test app

A new app starts in testing, so you can try linking with your production app and its test users. You can also register a separate app for testing. Each app has its own connections, test users, status, and operator service account.

<Warning>
  Keep Linked billing on one production app for as long as you offer it: a customer’s connection works only with the app that they linked.
</Warning>

## Rules and special cases

These cases come up when you change an app that customers already use or when your app still uses the deprecated scope. Two terms recur:

* **Approve again:** Send the customer through the same approval as when they first linked. Use their existing user profile, and don’t unlink them first.
* **Link again:** Follow [Link a customer again](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/manage-customers#link-a-customer-again), which covers each case.

### If you change scopes

To give a linked customer a refresh token:

1. Turn on **Offline access** on the **Permissions** tab.
2. Have the customer approve again, asking for the scopes `billing:attribution offline_access`.
3. Replace the stored connection ID with the new one that the code exchange returns.

If a pushed authorization request asks for a scope the app doesn’t have, `auth.claude.com` refuses it with `invalid_scope`. It also refuses one sent in the few minutes after you change the app’s scopes, before the change reaches it: wait and send it again.

### If you change the service account

After you change or archive the operator service account, `auth.claude.com` refuses every refresh of a working token with `unauthorized_client`. A token that was already revoked or has expired gets `invalid_grant` after a change and can get either error after an archive.

**If you changed it:**

| Request | Result |
| ----- | ----- |
| With a customer’s access token that you hold or as the earlier service account | Stops billing customers shortly after the change |
| As the new operator service account | Can still bill your linked customers unless you [turned off operator-only authentication](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/credential-for-each-customer#turn-off-operator-only-authentication), which lets only customers’ own access tokens bill |

To recover, make sure that your back end authenticates as the new operator service account. The account must be a member of the app’s default workspace. Then, link again each customer whose tokens you use. Customers whom you bill only as the operator service account need nothing more.

**If you archived it:** Nothing can bill as your app, and `auth.claude.com` refuses every code exchange, until the app has a new operator service account. The Console says that the service account no longer exists and displays a **Delete app** button, but you don’t need to delete the app. If the app’s default workspace is archived too, the Console can’t select a new service account: contact [Anthropic support](https://support.claude.com/en/articles/9015913-how-to-get-support).

A person with the Admin or Billing role at each customer has to link again, so agree on a time with them first. Then:

1. [Unlink each linked customer in the Console](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/manage-customers#unlink-a-customer). The unlink endpoint can’t do this, because it needs the archived account.
2. Create [another operator service account](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/set-up-your-app#service-account) and its federation rule. It must be a member of the app’s default workspace.
3. On the app’s **Client authentication** tab, click **Change** under **Operator service account**. Select the new service account and click **Change service account**.
4. Make sure that your back end authenticates as the new service account, and wait a few minutes.
5. Have each customer link again with their existing user profile, and store the new connection ID and OAuth tokens in place of the earlier ones.

### If you move to another workspace

Requests with a customer’s own access token run in the app’s default workspace. To move to another one, follow these steps in order. Don’t archive the earlier workspace before step 6: archiving revokes its customers’ OAuth tokens.

1. Make sure that the operator service account is a member of the new workspace.
2. On the app’s **Client authentication** tab, click **Change workspace**, select the new workspace, and click **Save**.
3. Wait a few minutes for the change to reach `auth.claude.com`. A refresh during the wait can return tokens that still run in the earlier workspace.
4. Refresh the OAuth tokens of every customer who has a refresh token.
5. Have each customer without a refresh token approve again with the same scope.
6. If you no longer need the earlier workspace, archive it.

If you archived the earlier workspace too soon, stop refreshing its customers at once. What happens next:

| When | Customer with a refresh token | Customer without one |
| ----- | ----- | ----- |
| Before you choose a new default workspace | Refreshes get `invalid_grant` | The access token stops working within a few minutes |
| After you choose one | A refresh ends the connection | Stays linked |

Once you choose a new default workspace, link again each customer who had a refresh token, and have each customer without one approve again.

### If you still use the deprecated scope

An app created before `billing:attribution` existed can have the deprecated scope `org:billing_attribution`. A customer who approved only that scope gets no token of their own, so you bill them only as the operator service account:

* The code exchange returns an `access_token`, but it isn’t a customer’s own access token. Don’t use it as one.
* Billing them stops when their connection ends or when you [turn off operator-only authentication](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/credential-for-each-customer#turn-off-operator-only-authentication).

Two rules apply to the deprecated scope:

* **Send it alone:** With `billing:attribution` or `offline_access`, a pushed authorization request gets `invalid_scope`.
* **Removing it is final:** If you remove `org:billing_attribution` on the **Permissions** tab, you can’t add it back.

To give such a customer their own tokens:

1. On the app’s **Permissions** tab, turn on `billing:attribution` under **Billing** and turn on **Offline access**.
2. Make sure that the app has a [default workspace](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/set-up-your-app#default-workspace).
3. Have the customer approve again, asking for `billing:attribution offline_access`.

## Next steps

<CardGroup cols={1}>
  <Card title="Link your Claude organization button" icon="link" href="https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/link-button">
    The button that sends a customer from your product to approve your app
  </Card>
</CardGroup>
