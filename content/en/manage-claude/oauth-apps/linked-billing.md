---
title: Linked billing
url: https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing
description: Learn who pays, which customers are eligible, and whose terms apply so that you can decide whether Linked billing fits your business.
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

Linked billing lets your customers pay for the Claude usage in your product through their own Claude organization. It’s a feature of [Claude Platform OAuth](https://platform.claude.com/docs/en/manage-claude/oauth-apps/overview), so it works through an [OAuth app](https://platform.claude.com/docs/en/manage-claude/oauth-apps/overview#your-oauth-app) that you register for your product. A customer links their organization to your app once. After that, you choose on each Claude API request whether you or the customer pays.

## How it works

Suppose Acme uses your product and already pays Anthropic for its own Claude usage. You create a [user profile](https://platform.claude.com/docs/en/manage-claude/user-profiles) for Acme: a record in your organization that stands for that customer. Someone at Acme clicks the [Link your Claude organization button](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/link-button) in your product. On Claude’s approval page, they approve your app. Approving needs the Admin or Billing role in Acme’s Claude organization. They can also set a monthly [spend cap](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/what-your-customers-see#spend-caps) for it.

From then on, your back end sends Acme’s Claude API requests as your app’s [operator service account](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/set-up-your-app#service-account), a non-human account in your Claude organization. Only that account can bill linked customers. A customer’s own OAuth access token counts as that account, so a request with it can bill that customer and no other. Your back end marks the requests that Acme pays for, and Anthropic bills those to Acme’s organization, not to yours, at Acme’s own rates. The [Linked Billing Beta Terms](https://www.anthropic.com/legal/linked-billing-terms) set out how customers are charged.

### How a connection starts and ends

Linking creates a connection, which ties the customer’s Claude organization to their user profile. The connection belongs to the customer’s organization, not to the person who approved it, so it stays if that person leaves. These are the usual ways a connection ends:

* The customer unlinks your app.
* An Admin of your organization unlinks the customer in the Claude Console.
* Your back end ends the connection through the API.

There are also [less common ways a connection ends](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/what-your-customers-see#after-linking). Anthropic doesn’t tell you when a customer unlinks, so [check whether customers are still linked](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/manage-customers#check-a-links-status).

### Choose who pays on each request

Each request that your operator service account sends for a linked customer names their user profile in the `anthropic-user-profile-id` header. What’s in the request’s body decides who pays:

* **The customer pays** when the body’s [`billing_policy`](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/link-and-bill-a-customer#bill-a-request) field sets `bill_to` to `user_profile`.
* **You pay** when `bill_to` is `self` or when the body has no `billing_policy`.

You can therefore bill some of a customer’s usage to them and pay for the rest yourself. A request sent with the customer’s own access token instead bills only that customer: see [Use a separate credential for each customer](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/credential-for-each-customer).

### When a request is refused

If Anthropic can’t bill the customer for a request, the Claude API refuses the request. It never bills you instead. These are the usual causes:

* The customer reached the spend cap that they set for your app, or their organization reached its monthly spend limit.
* No credit on the customer’s account can pay for the request.
* The connection has ended.

You can send a refused request again as one that you pay for. For each refusal and its fix, see [Linked billing errors](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/errors).

## When to use it

Linked billing fits a product whose users are mostly Claude Platform customers with their own Claude organization. To offer it, your own organization must pay Anthropic directly, through prepaid credits or invoiced billing.

Some requests can’t be billed to a customer. To serve them, send them as requests that you pay for:

* Requests for a customer whose organization [can’t be billed this way](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing#eligible-customers)
* Requests to an [endpoint that can’t bill a customer](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing#which-endpoints-can-bill-a-customer)

### Eligible customers

A customer can be billed this way only if their Claude organization pays Anthropic directly for its API usage, through prepaid credits or invoiced billing. These organizations can’t be billed this way:

* Organizations billed through a cloud marketplace (AWS, Google Cloud, or Azure)
* Organizations that have only a Claude subscription with no Claude API access of their own

An organization that has only a Claude subscription can’t link your app. An organization billed through a cloud marketplace is refused either when it tries to link or on every request that you bill to it. So a completed link doesn’t show that such an organization can be billed.

### Which credits can pay

Not all credit can pay for a request that an app bills to a customer. What can pay depends on the organization that’s billed:

* **When your app bills a customer:** the customer’s organization
* **When another company’s app bills you:** your own organization

Credit bought in the Claude Console for that organization can pay for these requests. If that organization has invoiced billing, it’s invoiced for these requests.

Some promotional credits from Anthropic can’t pay for these requests. These include the monthly API credits that come with Claude Max, Ultra, and Team plans. Credits from Anthropic’s partner, VC, and startup programs aren’t eligible to pay for these requests.

When nothing on that organization’s account can pay for a request, the Claude API can refuse it with a 402. The response doesn’t say whether a lack of credit or a spend limit caused the refusal. See [`linked_organization_spend_limit_reached`](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/errors#linked-organization-spend-limit-reached).

### Which endpoints can bill a customer

| Endpoint | Can bill a customer |
| ----- | ----- |
| The Messages API (`/v1/messages`) | Yes, except with [billable code execution](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing#if-you-use-code-execution) |
| OpenAI SDK compatibility (`/v1/chat/completions`) | Yes |
| [Message Batches](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing#if-you-use-message-batches) | No |
| Claude Managed Agents | No |

To ask for another endpoint, contact [Anthropic support](https://support.claude.com/en/articles/9015913-how-to-get-support).

## Whose terms and limits apply

<Warning>
  Don’t offer Linked billing to a customer that needs HIPAA, FERPA, or customer-managed encryption key coverage for this usage.
</Warning>

Requests that you bill to a customer still run in your organization:

| Setting | Applies to these requests |
| ----- | ----- |
| Your rate limits, usage tier, model access, and [service tier](https://platform.claude.com/docs/en/api/service-tiers) | Yes |
| Your usage tier’s [monthly spend cap](https://platform.claude.com/docs/en/api/rate-limits#spend-limits) | Yes |
| Your data retention and encryption keys | Yes |
| The customer’s [zero data retention (ZDR)](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention#zero-data-retention-zdr-scope), business associate agreement (BAA), customer-managed encryption keys (CMEK), and IP allowlist | No |
| The customer’s spend cap for your app and their organization’s monthly spend limit | Yes |
| The spend limits you set for your organization and its workspaces | No |

Once your organization reaches your usage tier’s monthly spend cap, the Claude API refuses all its requests, including ones that bill a customer: see [`enforced_spend_limit_reached`](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/errors#enforced-spend-limit-reached). Usage that you bill to a customer doesn’t count toward that cap.

## What you may bill

Bill a customer only for the usage that they direct you to make. That’s the Claude usage that the customer and their users cause in your product. Don’t bill them for your own usage, such as testing, evaluations, or work for other customers. The Claude API can’t check this for you, so it’s your responsibility. You accept the [Linked Billing Beta Terms](https://www.anthropic.com/legal/linked-billing-terms) when you create your app.

## Who supports the customer

You support your customers for everything about your app, including the Claude usage that you bill to them. Anthropic gives them only [the approval page and the Linked platforms page](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/what-your-customers-see) in their Claude Console. All other questions about your app come to you, so tell your customers how to reach you.

## Rules and special cases

Some features can’t bill a customer, and some treat `billing_policy` in their own way.

### If you use Message Batches

Send the requests in a [message batch](https://platform.claude.com/docs/en/build-with-claude/batch-processing) as ones that you pay for: with `bill_to` set to `self` or without `billing_policy`. They’re billed to you as usual. A request in a batch that’s marked for the customer is refused. Its result is `errored` with an `invalid_request_error`, and nobody is billed for it. The batch’s other requests run as usual.

### If you use code execution

A request that bills a customer can’t use [billable code execution features](https://platform.claude.com/docs/en/about-claude/pricing#code-execution-tool): the API refuses it with a 400. Send such requests as ones that you pay for.

### If you count tokens

The token counting endpoint (`/v1/messages/count_tokens`) accepts the `billing_policy` field when the request has the `user-profiles-billing-2026-10-01` beta header, and ignores the field. You don’t need to remove it before you count tokens.

## Availability

Linked billing is in beta on every model.

### API support

#### [Messages API](https://platform.claude.com/docs/en/build-with-claude/working-with-messages)

* Availability: Available

| Status | Cloud platforms |
| ----- | ----- |
| Beta<sup>1</sup> | Claude API |

1. Only requests that send `billing_policy` need the beta header.

### Required beta headers

[Beta headers overview](https://platform.claude.com/docs/en/api/beta-headers)

Beta headers allow you to access experimental features and new model capabilities before they become part of the standard API.

* `user-profiles-billing-2026-10-01`
