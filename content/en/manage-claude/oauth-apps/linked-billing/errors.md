---
title: Linked billing errors
url: https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/errors
description: Find what to do about each error that linking or billing a customer can return, with its causes in the order to check them.
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

These are the errors that `auth.claude.com` returns while linking and the Claude API returns while billing, apart from a [failed refresh](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/credential-for-each-customer#if-a-refresh-fails).

## While linking

These errors arrive on your redirect URI or from the code exchange. A connection is the record that ties a customer’s Claude organization to one of your [user profiles](https://platform.claude.com/docs/en/manage-claude/user-profiles). In each case, no connection is made. For the standard OAuth errors, see [OAuth endpoints and parameters](https://platform.claude.com/docs/en/manage-claude/oauth-apps/endpoints-and-parameters#errors).

### `access_denied`

First, check your app: causes 3 and 4 are yours to fix.

Otherwise, tell the person that linking didn’t complete, and don’t assume that they declined. Ask them to check which Claude account they signed in with and their role in the organization they want to link. To let them try again, [send them to approve](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/link-and-bill-a-customer#send-them-to-approve) with a new pushed authorization request.

For these causes, your redirect URI receives `error=access_denied` with your `state` value:

1. The person clicked **Cancel** on an approval screen.

2. The approval page had no organization to offer, and the person clicked the button that returns to your app. That happens when:

   * the person doesn’t have the Admin or Billing role in any Claude organization
   * the person’s only organization is the one that owns your app
   * the user profile that you sent is already linked to another organization, where the person doesn’t have the Admin or Billing role
   * the person’s only organizations are of a kind that can’t link: see [eligible customers](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing#eligible-customers)

3. Your app’s **Who can link** setting reads “only” after your organization’s name. Nobody can link such an app. On its **Settings** tab, select **Any Claude user** and click **Save changes**.

4. Your app isn’t live, the person isn’t on its **Test users** list, and they clicked the button that returns to your app. [Add them as a test user](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/test-and-publish#add-test-users), or [publish the app](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/test-and-publish#publish-the-app).

For these causes, `error_description` reads `the user declined the request`, so it can’t tell you which one happened. If it reads `the request cannot be approved for this organization` instead, the organization that the person selected can’t approve your app. Ask them to select another.

### `user_profile_already_linked`

Each customer’s organization can have only one connection to your app at a time, and so can each of your profiles. `error_description` says which of these two causes applies:

1. **The organization already has a connection**, through another of your profiles. This is the usual cause, and `error_description` starts `This organization already has an active connection`. On your [User profiles page](https://platform.claude.com/user-profiles), look for another profile of this customer that shows as **Linked**. Anthropic doesn’t show which organization a profile is linked to, so confirm with the customer that it’s theirs.

   * **You find it:** Bill the customer through that profile, or [unlink that profile](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/manage-customers#unlink-a-customer) and send the customer to approve again with the profile that was refused.
   * **None of this customer’s profiles is linked:** The person might have selected an organization that belongs to another of your customers. Send them to approve again, and ask them to check which organization they select.

2. **The profile you sent already has a connection**, to another organization. Its `error_description` starts `This user profile already has an active connection`. End that connection first: see [Move a customer to another organization](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/manage-customers#move-a-customer-to-another-organization).

You can’t catch this error early: the pushed authorization request succeeds.

The error arrives in one of two places:

* **On your redirect URI:** If the person returns to your app, the redirect carries `error=user_profile_already_linked` with your `state` value. `auth.claude.com` has already asked them to contact you with this code.
* **From the token endpoint:** The code exchange returns it if the connection was made after the approval.

The error doesn’t name the profile that holds the connection.

### No redirect

If the person comes back to your product without a callback, send them to approve again with a new pushed authorization request. You get no callback and can’t tell these cases apart:

* The person closed the approval page.
* The `request_uri` had expired. It expires 10 minutes after you create it.
* The `request_uri` was already used. Each one works once.

In the last two cases, the approval page displays an error and doesn’t send the browser back to your app.

### `unauthorized_client` from the code exchange

Check your app’s setup in the Claude Console, fix what’s missing, and exchange the same code again. This refusal doesn’t use up the code, which lasts 5 minutes.

| Check | `error_description` | Fix |
| ----- | ----- | ----- |
| The app has an operator service account | `the client is not registered for this grant` | [Choose an operator service account](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/set-up-your-app#service-account) |
| The app has a default workspace that isn’t archived | Names the workspace problem | [Choose a default workspace](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/set-up-your-app#default-workspace) |
| The operator service account is a member of that workspace | Names the workspace problem | [Choose a workspace](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/set-up-your-app#default-workspace) that the account is a member of, such as the built-in workspace named **Default** |

A saved change can take a few minutes to reach `auth.claude.com`, so if the exchange is refused again, wait and retry. If the code expires first, send the customer to approve again.

If the Console says that the service account no longer exists, see [If you change the service account](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/set-up-your-app#if-you-change-the-service-account). For any other cause, contact [Anthropic support](https://support.claude.com/en/articles/9015913-how-to-get-support) or your Anthropic account team if you have one.

## While billing

A request that the Claude API refuses before Claude starts a reply bills no one. Where the error’s details are depends on the endpoint:

| Endpoint | Where the error code is | Request ID header |
| ----- | ----- | ----- |
| `/v1/messages` | `error.details.error_code` | `request-id` |
| `/v1/chat/completions` | Not sent | `x-request-id` |

On `/v1/chat/completions`, the error takes another form:

* `error.type` is `invalid_request_error`.
* `error.code` holds the error type, such as `billing_error`, not one of the error codes in this page’s headings.

Match on the HTTP status and `error.code`. The two `402` errors look alike there, and so do the `403` errors, so follow every entry that fits. A `401` for an access token has the `/v1/messages` form and the `request-id` header on both endpoints.

A refusal on `/v1/messages` has this form:

```json
{
  "type": "error",
  "error": {
    "type": "billing_error",
    "message": "...",
    "details": {
      "error_code": "linked_organization_spend_limit_reached"
    }
  }
}
```

The `401` and `503` errors later on this page have no error code. On `/v1/messages`, match them on the status and `error.type`.

In the Anthropic SDK, catch the error class for the HTTP status, then read the error code from its `error_code` (typescript: `errorCode`; csharp: `ErrorCode`; go: `ErrorCode()`; java: `errorCode()`; php: `getErrorCode()`). The class for a `402` is `PaymentRequiredError` (ruby: `Anthropic::Errors::PaymentRequiredError`; java, php: `PaymentRequiredException`; csharp: `AnthropicPaymentRequiredException`; go: `*anthropic.Error`), and the class for a `403` is `PermissionDeniedError` (ruby: `Anthropic::Errors::PermissionDeniedError`; java, php: `PermissionDeniedException`; csharp: `AnthropicForbiddenException`; go: `*anthropic.Error`).

Outside Go, each class covers every error with its status. Go has one type, `*anthropic.Error`, for every status: check its `StatusCode`. One code can also arrive inside a streamed reply: see [`linked_organization_billing_unavailable`](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/errors#linked-organization-billing-unavailable).

Log the whole `error.message` and the request ID of each refused request. To serve a refused customer at your own cost, send the request again [as one that you pay for](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/link-and-bill-a-customer#you-pay), with `bill_to: "self"` in `billing_policy`. Send it as your [operator service account](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/set-up-your-app#service-account), not with a customer’s access token.

For a `402` or `403`, sending the same request again doesn’t help while the cause lasts. A new connection’s first seconds are an exception: see [`user_profile_billing_not_authorized`](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/errors#user-profile-billing-not-authorized).

A request that fits causes of both `403` codes can get either code, for example the wrong credential for a customer who also isn’t linked. Handle the two codes together, and if one entry’s causes don’t explain a refusal, check the other’s.

### 403 `user_profile_billing_not_authorized`

No connection lets your request bill the user profile it names. The response doesn’t say why. To tell causes 2 to 4 apart, [check whether the customer is linked](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/manage-customers#check-a-links-status) through the app you expect.

Check these causes in order:

1. **Your request.** The request must name the user profile that this customer linked. It must also authenticate as the operator service account of the app that they linked through, or with that connection’s access token. The service account of another of your apps gets this error if the customer hasn’t linked through that app. Correct the request: a new connection doesn’t help.

2. **The customer hasn’t linked through this app.** The [connection status](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/manage-customers#check-a-links-status) reads `not_connected`. A profile linked only through another of your apps, such as a [separate test app](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/set-up-your-app#if-you-run-several-apps), isn’t linked to this one. Until the customer [links through this app](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/link-and-bill-a-customer#send-them-to-approve), a request can bill only you, with `bill_to: "self"`.

3. **The connection has ended.** The connection status reads `disconnected`, and the profile shows as **Unlinked** on your [User profiles page](https://platform.claude.com/user-profiles). The status’s `last_revoked_reason.type` says why. Until the customer [links again](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/manage-customers#link-a-customer-again), a request can bill only you, with `bill_to: "self"`.

4. **The connection status reads `connected`, and the request is still refused.**

   * **A new connection:** A new connection usually works at once, but it can take about 10 seconds after the code exchange. If the connection is that new, wait until about 10 seconds have passed since the exchange and then send the request once more.
   * **An earlier connection’s access token:** A customer’s access token works only for the connection that issued it. After that connection ends, a request with its token can get this error or a [`401 authentication_error`](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/errors#authentication-error), even if the customer has linked again. Use the new connection’s access token.
   * **Neither:** Send a refused request’s ID to [Anthropic support](https://support.claude.com/en/articles/9015913-how-to-get-support) or to your Anthropic account team if you have one.

### 403 `user_profile_not_billable`

Find the cause before you ask the customer to link again, because linking the same organization again can fix only cause 2.

Check these causes in order:

1. **Your request’s credential.** The request must authenticate as your app’s [operator service account](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/set-up-your-app#service-account) or with a customer’s access token. Any other credential is refused, such as an API key that isn’t bound to a service account. So is a service account that operates no OAuth app, such as an [operator that you replaced](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/set-up-your-app#if-you-change-the-service-account). Correct the request.

2. **Operator-only authentication.** If you [turned off operator-only authentication](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/credential-for-each-customer#turn-off-operator-only-authentication), only a customer’s own access token can bill them. A request from your service account alone is refused, even though the customer shows as **Linked**.

   * **You hold the customer’s access token:** Send the request with it. If it has expired, [refresh the OAuth tokens](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/credential-for-each-customer#refresh-the-tokens) first.
   * **You hold no refresh token, or the refresh returns `invalid_grant`:** [Link the customer again](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/manage-customers#link-a-customer-again).

3. **The customer’s organization.** You can’t see its status from your side, so ask the customer how their organization pays for its Claude API usage.

   * **It isn’t eligible:** It must [pay Anthropic directly](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing#eligible-customers). Some organizations billed through a cloud marketplace can link, and then every request that you bill to them gets this error.
   * **It has no billing set up:** A new organization can link before it has billing set up. Until then, it gets this error, not the out-of-credit `402`. Ask the customer to buy credits on their [Billing page](https://platform.claude.com/settings/billing) and then send the request again. A purchase can take some time to apply, so if you still get this error or [`linked_organization_spend_limit_reached`](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/errors#linked-organization-spend-limit-reached), try again later.

4. **Something only Anthropic can see.** The customer shows as **Linked**, and your request is correct. Send a refused request’s ID to [Anthropic support](https://support.claude.com/en/articles/9015913-how-to-get-support) or to your Anthropic account team if you have one.

### 402 `linked_organization_spend_limit_reached`

Ask a person with the Admin or Billing role at the customer to check these in the Claude Console. The response doesn’t say which one applies:

* **Their spend cap for your app:** On the page for your app under [Linked platforms](https://platform.claude.com/linked-platforms), they can set or raise it. A cap set there replaces the default cap that they set for all linked platforms.
* **Their organization’s monthly spend limit:** Under [Spend limits](https://platform.claude.com/settings/billing#spend-limits), they can raise it.
* **Their credit balance:** On their [Billing page](https://platform.claude.com/settings/billing), they can buy credits. A purchase can take some time to apply, so a request soon after it can still get this error. If so, try again later. Some credits can’t pay for these requests: see [Which credits can pay](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing#which-credits-can-pay). A balance above $0 USD can therefore still get this error.

While your app isn’t live, a cap can’t go above $50 USD. A refusal at $50 USD then lasts until the next month begins (UTC): see [Caps while testing](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/test-and-publish#caps-while-testing).

An organization that has billing set up but no credit gets this code. One whose billing isn’t set up yet gets [`user_profile_not_billable`](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/errors#user-profile-not-billable).

### 402 `linked_organization_billing_unavailable`

What to do depends on when the error arrives:

* **Before a reply starts:** Anthropic can’t bill the customer’s organization, for example because it’s suspended. The response doesn’t say why. Ask the customer to check their Claude account and their billing status with Anthropic.
* **After Claude has started a reply:** Usually, the organization’s credit ran out, though a suspension can also cut a reply. Ask the customer to buy credits on their [Billing page](https://platform.claude.com/settings/billing) or to check their account.

A request that isn’t streamed gets an HTTP `402` in both cases, so follow both. A customer who has no credit when the request arrives gets [`linked_organization_spend_limit_reached`](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/errors#linked-organization-spend-limit-reached) instead.

On a streamed reply, the HTTP status is already `200` when the reply is cut, and the error arrives in the stream:

* **On `/v1/messages`:** As an `error` event whose `error.type` is `billing_error` and whose `error.details.error_code` is this code. The SDK’s class for a `402` doesn’t catch it.
* **On `/v1/chat/completions`:** As a last `data:` line that holds an OpenAI error object, with `billing_error` in `error.code` and no `[DONE]` after it.

No one pays for the reply that was cut. If the request had already finished a step, such as Claude’s turn before a web search, the customer pays for that step.

### 400 `user_profile_required`

Send the customer’s user profile ID in the `anthropic-user-profile-id` header. The request set `bill_to: "user_profile"` without it. A request with a [customer’s access token](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/credential-for-each-customer#call-claude-with-a-token) doesn’t need the header.

### 401 `authentication_error`

Send the request again with the customer’s newest access token, or [refresh the OAuth tokens](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/credential-for-each-customer#refresh-the-tokens). [Link the customer again](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/manage-customers#link-a-customer-again) only if their profile shows as **Unlinked**, you hold no refresh token for them, or the refresh returns `invalid_grant`.

This entry covers requests with a customer’s access token, which no longer works: it expired, a refresh replaced it, or it was revoked. A refresh revokes the earlier token too, so “revoked” in `error.message` doesn’t alone mean that the connection ended. After a connection ends, each request with its token can get this error or a [`403 user_profile_billing_not_authorized`](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/errors#user-profile-billing-not-authorized), in no fixed order.

### 429 `enforced_spend_limit_reached`

[Request a higher monthly spend cap](https://platform.claude.com/docs/en/api/rate-limits#requesting-higher-limits) for your organization, or wait until the next month begins (UTC). Sending the request again doesn’t help, even as one that you pay for.

Your organization reached your usage tier’s monthly spend cap. The customer’s spend cap for your app isn’t the cause, so the customer can’t fix it. See [Reaching your spend cap](https://platform.claude.com/docs/en/api/rate-limits#reaching-your-spend-cap).

### 503 `overloaded_error`

Retry with backoff. If the response has a `retry-after` header, wait at least that long. The Claude API couldn’t confirm whether it can bill the customer, so it didn’t serve or bill the request.

### Other errors with no code

| Status and type | Cause | Fix |
| ----- | ----- | ----- |
| `400 invalid_request_error` | The `anthropic-user-profile-id` header holds an ID that is malformed or isn’t one of your organization’s user profiles | Send the customer’s user profile ID |
| `400 invalid_request_error` | The request sends `billing_policy` without the `user-profiles-billing-2026-10-01` beta header | Add the beta header |
| `400 invalid_request_error` | `billing_policy` has a missing or invalid field | Correct `billing_policy` |
| `400 invalid_request_error` | The request bills a customer and uses [billable code execution features](https://platform.claude.com/docs/en/about-claude/pricing#code-execution-tool) | Send it as your operator service account, billed to you |
| `invalid_request_error` in an `errored` batch result | A request in a batch bills a customer: see [If you use Message Batches](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing#if-you-use-message-batches) | Send it billed to you |
| `400 invalid_request_error` | The request uses a customer’s access token and sets `bill_to: "self"` | Send requests that you pay for as your operator service account |
| `400 invalid_request_error` | The request uses a customer’s access token and names another user profile | Name only that customer’s profile |
| `403 permission_error` | The request uses a customer’s access token on an endpoint that doesn’t take it, such as [Message Batches](https://platform.claude.com/docs/en/build-with-claude/batch-processing) | Send it as your operator service account |
| `403 permission_error` | Anthropic doesn’t bill your organization directly, so it can’t bill customers on your behalf | Bill customers from an organization that pays Anthropic directly |
