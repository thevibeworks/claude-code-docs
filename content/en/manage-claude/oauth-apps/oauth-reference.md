---
title: OAuth reference
url: https://platform.claude.com/docs/en/manage-claude/oauth-apps/oauth-reference
description: Endpoints, client authentication, request parameters, scopes, token responses, revocation, lifetimes, redirect URI rules, and errors.
---

<Warning>
  Claude Platform OAuth is a Beta Service: prerelease software provided under your agreement with Anthropic, such as the [Commercial Terms of Service](https://www.anthropic.com/legal/commercial-terms), and the [Service Specific Terms](https://www.anthropic.com/legal/service-specific-terms). Endpoints, parameters, and behavior can change during the beta. It might not be suitable for production use.
</Warning>

This page collects the endpoints, parameters, validation rules, and error mappings for [Claude Platform OAuth](https://platform.claude.com/docs/en/manage-claude/oauth-apps/overview). For a walkthrough, see [Linked billing](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections).

## Endpoints

| Endpoint                                                     | URL                                                                          |
| ------------------------------------------------------------ | ---------------------------------------------------------------------------- |
| Issuer                                                       | `https://identity.anthropic.com/users`                                       |
| Discovery document                                           | `https://identity.anthropic.com/users/.well-known/openid-configuration`      |
| Signing keys (JWKS)                                          | The `jwks_uri` in the discovery document, hosted on `identity.anthropic.com` |
| Authorization endpoint (sign-in and consent page)            | `https://auth.claude.com/oauth/authorize`                                    |
| Pushed authorization request (PAR) endpoint                  | `https://auth.claude.com/v1/oauth/par`                                       |
| Token endpoint                                               | `https://auth.claude.com/v1/oauth/token`                                     |
| Revocation endpoint                                          | `https://auth.claude.com/v1/oauth/revoke`                                    |
| Claude API (user profiles and requests that bill a customer) | `https://api.anthropic.com`                                                  |

Read the signing keys from the discovery document rather than hardcoding them. The discovery document does not list the PAR endpoint or the revocation endpoint, so use the URLs in this table.

## Discovery document values

| Field                                   | Value                                            |
| --------------------------------------- | ------------------------------------------------ |
| `issuer`                                | `https://identity.anthropic.com/users`           |
| `authorization_endpoint`                | `https://auth.claude.com/oauth/authorize`        |
| `token_endpoint`                        | `https://auth.claude.com/v1/oauth/token`         |
| `jwks_uri`                              | `https://identity.anthropic.com/users/jwks.json` |
| `response_types_supported`              | `code`                                           |
| `grant_types_supported`                 | `authorization_code`, `refresh_token`            |
| `code_challenge_methods_supported`      | `S256`                                           |
| `token_endpoint_auth_methods_supported` | `private_key_jwt`                                |
| `id_token_signing_alg_values_supported` | `ES256`                                          |
| `scopes_supported`                      | `openid`, `email`                                |
| `subject_types_supported`               | `public`, `pairwise`                             |

`auth.claude.com` returns a refresh token for Linked billing only when the customer approved `offline_access` together with `billing:attribution`: see [OAuth tokens for a billing connection](https://platform.claude.com/docs/en/manage-claude/oauth-apps/oauth-reference#oauth-tokens-for-a-billing-connection).

## Client authentication

`auth.claude.com` authenticates a confidential client with the `private_key_jwt` method ([RFC 7523](https://www.rfc-editor.org/rfc/rfc7523)). Send these parameters on every request to the PAR endpoint, the token endpoint, and the revocation endpoint. Never send credentials in a URL query string: `auth.claude.com` rejects them.

| Parameter               | Value                                                                                                                                                                                |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `client_id`             | Your OAuth app’s client ID                                                                                                                                                           |
| `client_assertion_type` | `urn:ietf:params:oauth:client-assertion-type:jwt-bearer`                                                                                                                             |
| `client_assertion`      | A JWT from your identity provider with the claims in [Client assertion claims](https://platform.claude.com/docs/en/manage-claude/oauth-apps/oauth-reference#client-assertion-claims) |

### Client assertion claims

A client assertion must contain all of the following claims, and its header must contain the `kid` of a key in your JWKS.

| Claim | Requirement                                                                                                                                                                       |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `iss` | Your identity provider’s issuer URL, exactly as registered through [Workload Identity Federation](https://platform.claude.com/docs/en/manage-claude/workload-identity-federation) |
| `sub` | A value that matches the subject pattern in your app’s client authentication settings, if you set one                                                                             |
| `aud` | Exactly one audience: the value in your app’s client authentication settings. `auth.claude.com` rejects an assertion that lists more than one audience.                           |
| `iat` | The time your identity provider issued the JWT                                                                                                                                    |
| `exp` | The expiry time, no more than 1 hour after `iat`. Use a shorter lifetime where you can: anyone who intercepts an assertion can use it until it expires.                           |

Example assertion payload:

```json
{
  "iss": "https://idp.example.com",
  "sub": "workload:prod:claude-integration-backend",
  "aud": "YOUR_CONFIGURED_AUDIENCE",
  "iat": 1791230000,
  "exp": 1791230300
}
```

Make the subject pattern and claim conditions as narrow as your back end allows. `auth.claude.com` accepts any JWT from your identity provider that matches them as authentication for your app.

## Authorization request parameters

Send these parameters, except `request_uri`, in the JSON body of a pushed authorization request.

| Parameter                | Linked billing | Description                                                                                                                                                                                 |
| ------------------------ | -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `response_type`          | Required       | The value `code`                                                                                                                                                                            |
| `client_id`              | Required       | Your OAuth app’s client ID                                                                                                                                                                  |
| `redirect_uri`           | Required       | A URI that exactly matches a registered redirect URI, up to 2,048 characters                                                                                                                |
| `scope`                  | Required       | For a billing connection, `billing:attribution` or `billing:attribution offline_access`. See [Scopes](https://platform.claude.com/docs/en/manage-claude/oauth-apps/oauth-reference#scopes). |
| `state`                  | Required       | A random, single-use value, up to 2,048 characters, that you check on the callback                                                                                                          |
| `code_challenge`         | Required       | `BASE64URL(SHA256(code_verifier))`, where the `code_verifier` is 43 to 128 characters                                                                                                       |
| `code_challenge_method`  | Required       | The value `S256`                                                                                                                                                                            |
| `connection_type`        | Required       | The value `organization_shared`. This value requests an organization connection for billing.                                                                                                |
| `connection_auth_target` | Required       | Which organization the connection’s requests route to. For Linked billing, send `platform` (the owner of the OAuth app).                                                                    |
| `user_profile_id`        | Required       | The ID of an active user profile in your organization that represents the customer                                                                                                          |
| `request_uri`            | Required       | The value that the PAR endpoint returned. Send it to the authorization endpoint with `client_id` and no other parameters.                                                                   |

The PAR endpoint returns HTTP 201 with `request_uri` and `expires_in` (600 seconds).

## Scopes

| Category | Scope                     | Description                                                                                                                                                                                                                                                                                                                                                                        | Connection type       | Client type  |
| -------- | ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------- | ------------ |
| General  | `offline_access`          | Gives the app a refresh token representing the other requested scopes. On an `organization_shared` connection, send it only together with `billing:attribution`.                                                                                                                                                                                                                   | `organization_shared` | Confidential |
| Billing  | `billing:attribution`     | A connection that lets you bill a customer’s Claude organization for the Claude API requests that the customer directs you to make. Send it alone, or together with `offline_access` to also get a refresh token. See [OAuth tokens for a billing connection](https://platform.claude.com/docs/en/manage-claude/oauth-apps/oauth-reference#oauth-tokens-for-a-billing-connection). | `organization_shared` | Confidential |
| Billing  | `org:billing_attribution` | Deprecated: use `billing:attribution`.                                                                                                                                                                                                                                                                                                                                             | `organization_shared` | Confidential |

## Token request and response

Send token requests to `https://auth.claude.com/v1/oauth/token` with a JSON body.

| Parameter                                                | Value                                                                                                                             |
| -------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| `grant_type`                                             | `authorization_code`                                                                                                              |
| `code`                                                   | The code from the callback                                                                                                        |
| `redirect_uri`                                           | The same `redirect_uri` you sent in the authorization request                                                                     |
| `code_verifier`                                          | The PKCE code verifier                                                                                                            |
| `client_id`, `client_assertion_type`, `client_assertion` | As in [Client authentication](https://platform.claude.com/docs/en/manage-claude/oauth-apps/oauth-reference#client-authentication) |

The token response contains these fields:

| Response field             | Linked billing                                                                                                                                      |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| `access_token`             | [The connection’s access token](https://platform.claude.com/docs/en/manage-claude/oauth-apps/oauth-reference#oauth-tokens-for-a-billing-connection) |
| `token_type`               | `Bearer`                                                                                                                                            |
| `expires_in`               | At most `3600`                                                                                                                                      |
| `scope`                    | `workspace:inference`                                                                                                                               |
| `connection_id`            | The connection ID, for example `ocon_EXAMPLE`. Store it.                                                                                            |
| `refresh_token`            | Returned only when the customer approved `offline_access`                                                                                           |
| `refresh_token_expires_in` | Seconds until `refresh_token` expires. Absent when there is no `refresh_token`.                                                                     |

To refresh, send `grant_type` set to `refresh_token`, your `refresh_token`, and the parameters in [Client authentication](https://platform.claude.com/docs/en/manage-claude/oauth-apps/oauth-reference#client-authentication). A refresh of a billing connection follows the rules in [OAuth tokens for a billing connection](https://platform.claude.com/docs/en/manage-claude/oauth-apps/oauth-reference#oauth-tokens-for-a-billing-connection).

## OAuth tokens for a billing connection

For a billing connection, the token endpoint returns the connection’s access token. The token authenticates as your app’s [operator service account](https://platform.claude.com/docs/en/manage-claude/oauth-apps/oauth-reference#terms), in the workspace that the app’s `connection_token_workspace_id` setting names. On `/v1/messages` and `/v1/chat/completions`, a request with it is billed to that connection’s customer and to no other. When the customer also approved `offline_access`, the token endpoint returns a refresh token too, and the `refresh_token` grant renews both tokens. For the setup and the walkthrough, see [OAuth tokens for each connection](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections#oauth-tokens-for-each-connection) on the Linked billing page.

Both grants take the parameters in [Token request and response](https://platform.claude.com/docs/en/manage-claude/oauth-apps/oauth-reference#token-request-and-response), with [Client authentication](https://platform.claude.com/docs/en/manage-claude/oauth-apps/oauth-reference#client-authentication). A refresh must not send a `scope` parameter. The token response contains these fields:

| Response field             | Value                                                                                          |
| -------------------------- | ---------------------------------------------------------------------------------------------- |
| `access_token`             | The connection’s access token                                                                  |
| `token_type`               | `Bearer`                                                                                       |
| `expires_in`               | Seconds until the access token expires, at most `3600`                                         |
| `scope`                    | Always `workspace:inference`                                                                   |
| `connection_id`            | The connection ID, for example `ocon_EXAMPLE`. Only the `authorization_code` grant returns it. |
| `refresh_token`            | The connection’s refresh token. Returned only when the customer approved `offline_access`.     |
| `refresh_token_expires_in` | Seconds until `refresh_token` expires                                                          |

Each refresh returns a new `access_token` and a new `refresh_token`. The refresh token that you sent is replaced, and the earlier access token stops working within a few minutes. You can send the replaced refresh token one more time, within 30 seconds of the refresh that replaced it, to repeat a request whose response you lost. That second request returns another new pair and revokes the pair from the lost response: use the newest pair only. A third request with the replaced token gets `invalid_grant`, and so does a second request that arrives after the 30 seconds. Inside the 30 seconds, such a request revokes nothing. After the 30 seconds, it revokes every token of the connection and ends the connection. [Refresh the tokens](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections#refresh-the-connection) has the rules and the errors of a refresh.

Each of these events revokes the connection’s tokens, the current access token included:

* The customer or you unlink.
* The customer approves a new authorization request with different scopes for the same user profile, and you exchange that approval’s code. The new connection takes the place of the earlier one.
* The workspace that the tokens run in is archived.

For how the Claude API bills a request with a connection’s access token, see [Call Claude with a connection’s access token](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections#call-claude-with-a-connections-access-token).

## Revocation

Send revocation requests to `https://auth.claude.com/v1/oauth/revoke` with a JSON or form-encoded body. The endpoint follows [RFC 7009](https://www.rfc-editor.org/rfc/rfc7009) and also accepts connection and user profile IDs.

Send the parameters in [Client authentication](https://platform.claude.com/docs/en/manage-claude/oauth-apps/oauth-reference#client-authentication) and exactly one of the parameters in this table. The client assertion’s `aud` is the value in your app’s client authentication settings, not the revocation URL.

| Parameter         | What it ends                                                                                                                 |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `connection_id`   | One of your app’s connections, given as an `ocon_` ID                                                                        |
| `user_profile_id` | All of your app’s connections on one user profile, given as a `uprof_` ID                                                    |
| `token`           | For Linked billing, send `connection_id` or `user_profile_id` instead: sending an access token might not end the connection. |

`auth.claude.com` accepts `token_type_hint` and ignores it.

The endpoint returns HTTP 200 and the IDs of the connections that the request ended:

```json
{
  "revoked_connection_ids": ["ocon_EXAMPLE"]
}
```

The list is empty if the token or ID is unknown or belongs to another app, if the connection has already ended, or if the request ended a token but no connection. The response does not say which.

After a billing connection ends, the Claude API refuses requests that bill that customer, with `user_profile_not_billable`, and the connection’s OAuth tokens stop working. Do not rely after that on an access token from a connection approved with the deprecated `org:billing_attribution` scope: it might stop working at once, or work until it expires.

## Lifetimes

| Item                                | Lifetime                                                          |
| ----------------------------------- | ----------------------------------------------------------------- |
| `request_uri` from the PAR endpoint | 10 minutes, single use                                            |
| Authorization code                  | 5 minutes, single use                                             |
| `access_token`                      | Up to 1 hour                                                      |
| `refresh_token`                     | Up to 1 year from the code exchange. A refresh doesn’t extend it. |

These are the current values. Read `expires_in` and `refresh_token_expires_in` from each response rather than relying on fixed values.

## Redirect URI rules

* Each `redirect_uri` must exactly match a URI registered on your app. `auth.claude.com` does not use wildcard or prefix matching.
* Every redirect URI must use HTTPS and must not contain a fragment. Local-development URIs on `localhost`, `127.0.0.1`, or `[::1]` may use HTTP.
* A local-development URI registered with an asterisk as the port, such as `http://localhost:*/callback`, matches any port.
* You can register up to 10 redirect URIs for each app.
* `auth.claude.com` sends errors to your redirect URI only when the `redirect_uri` matches a registered URI. For any other `redirect_uri`, `auth.claude.com` does not redirect the browser.

## Errors

### Errors on the redirect

`auth.claude.com` returns errors as `error`, `error_description`, and `state` query parameters on your redirect URI. They are standard OAuth 2.0 errors ([RFC 6749](https://www.rfc-editor.org/rfc/rfc6749)), except `user_profile_already_linked`, which is specific to Anthropic.

| Error                         | When                                                                                                                                                                                                                                                   | What to show your user                                                                                                                                                                                                                                                                                                                                                                                                |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `access_denied`               | The person declined or cannot approve this request. For a billing connection, the person must be an administrator of a Claude organization.                                                                                                            | Explain that the connection did not complete, and do not assume that the person declined. For a billing connection, follow [Your redirect URI receives `error=access_denied`](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections#access-denied) in the Linked billing guide, which lists the causes and what to tell the person. Otherwise, ask the person to contact you. |
| `server_error`                | `auth.claude.com` failed to process the request.                                                                                                                                                                                                       | Ask the user to try again.                                                                                                                                                                                                                                                                                                                                                                                            |
| `user_profile_already_linked` | Linked billing only. The customer’s organization is already linked to your app through a different user profile. Each customer organization can have one connection to your app. `auth.claude.com` has already asked the administrator to contact you. | Explain that their organization is already linked to your app.                                                                                                                                                                                                                                                                                                                                                        |

If the `request_uri` has expired or you already used it, `auth.claude.com` shows an error page and does not redirect the browser back to your app. Start the flow again with a new pushed authorization request.

### Errors from the PAR and token endpoints

These endpoints return a JSON body with `error` and `error_description`.

| Error                         | When                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `invalid_request`             | A required parameter is missing or invalid, for example a missing `state` or PKCE challenge, or a `user_profile_id` that is not the ID of an active user profile in your organization.                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `invalid_client`              | `auth.claude.com` could not authenticate your app: the client ID is unknown, or the client assertion failed verification. Check the assertion’s `iss`, `sub`, and `aud` against your app’s client authentication settings, and check that your identity provider signed it with a key in your JWKS.                                                                                                                                                                                                                                                                                                              |
| `invalid_scope`               | The requested scope is not allowed for this app or this connection type. For a [billing connection’s tokens](https://platform.claude.com/docs/en/manage-claude/oauth-apps/oauth-reference#oauth-tokens-for-a-billing-connection), this also means that a refresh sent a `scope` parameter, which it doesn’t accept, or that `billing:attribution` is no longer registered for your app. At the code exchange, that second cause uses up the code.                                                                                                                                                                |
| `invalid_grant`               | The code has expired, you already used it, or it does not match the `redirect_uri` or `code_verifier`. For a refresh, the refresh token has expired or is no longer valid: follow [Refresh the tokens](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections#refresh-the-connection).                                                                                                                                                                                                                                                                                    |
| `unauthorized_client`         | Your app is not set up for this request. For Linked billing, first check the app’s operator service account and its workspace: see [The code exchange returns `unauthorized_client`](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections#code-exchange-unauthorized-client). For a [billing connection’s tokens](https://platform.claude.com/docs/en/manage-claude/oauth-apps/oauth-reference#oauth-tokens-for-a-billing-connection), `error_description` gives the cause, for example a missing workspace. This refusal uses up no code and revokes no refresh token. |
| `user_profile_already_linked` | Linked billing only, from the token endpoint. Between the approval and this request, the user profile was linked to your app through a different customer organization, or the customer’s organization was linked through a different user profile.                                                                                                                                                                                                                                                                                                                                                              |

If `auth.claude.com` rate-limits a request, has an outage, or receives an unknown `grant_type` or a parameter longer than its limit, it returns an error in a different format, which might not be JSON. Retry only on HTTP 429 and 5xx responses, with backoff. Treat any other status as a fault in the request. For a refresh of a billing connection, follow [Refresh the tokens](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections#refresh-the-connection) instead of a general backoff. If the response has a `retry-after` header, wait at least that long. Send the next request from your own code, and don’t rely on an HTTP client library’s automatic retries: they might not run for such a response. [Refresh the tokens](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections#refresh-the-connection) also says when a retry is safe, because a refresh token that was already used can end the connection when you send it again.

### Errors from the revocation endpoint

For most requests that `auth.claude.com` refuses, the revocation endpoint returns HTTP 400 and a JSON body with `error` and `error_description`.

| Error                 | When                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `invalid_request`     | A required parameter is missing or invalid, for example a missing `client_id`. The request sends none of `token`, `connection_id`, and `user_profile_id`, or more than one of them. An ID is malformed, for example it has the wrong prefix. A credential or `token` is in the URL query string. The user profile has too many connections for one request: the request might have ended some of them, so end the rest with `connection_id`. |
| `invalid_client`      | `auth.claude.com` could not authenticate your app. For what to check, see `invalid_client` in [Errors from the PAR and token endpoints](https://platform.claude.com/docs/en/manage-claude/oauth-apps/oauth-reference#errors-from-the-par-and-token-endpoints).                                                                                                                                                                               |
| `unauthorized_client` | Your app is not set up for this request. Contact your Anthropic account team.                                                                                                                                                                                                                                                                                                                                                                |

The responses in the next table use a different format, which might not be JSON. When the body is JSON, `error` is an object, not a string.

| Status | When                                                           | What to do                                                                                                                                                                                                                                                                                                                                                  |
| ------ | -------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 400    | A parameter is longer than its limit.                          | Correct the request. Do not retry.                                                                                                                                                                                                                                                                                                                          |
| 429    | Too many failed requests came from your IP address.            | Retry with backoff.                                                                                                                                                                                                                                                                                                                                         |
| 500    | `auth.claude.com` failed to process the request.               | Retry with backoff. If it keeps happening, contact your Anthropic account team.                                                                                                                                                                                                                                                                             |
| 501    | Anthropic has not enabled this endpoint for your organization. | Do not retry. Contact your Anthropic account team.                                                                                                                                                                                                                                                                                                          |
| 503    | The request did not finish. Anything it ended stays ended.     | Retry with backoff, with the same parameters and a new client assertion. The retry finishes the rest, and its list leaves out connections that the earlier request ended. If you sent `user_profile_id`, retry within a day: after that, a retry can return 200 with an empty list and finish nothing. A retry with each `connection_id` works at any time. |

### Billing errors

These apply to Claude API requests that set `billing_policy.bill_to` to `"user_profile"` or that authenticate with [a billing connection’s access token](https://platform.claude.com/docs/en/manage-claude/oauth-apps/oauth-reference#oauth-tokens-for-a-billing-connection). The Claude API does not bill either organization for a refused request. None of the 402 and 403 responses is retryable, except a `user_profile_not_billable` refusal in the first 10 seconds after a new connection.

| Status | Error type and code                                        | When                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ------ | ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 400    | `invalid_request_error`                                    | The request sends `billing_policy` without the `user-profiles-billing-2026-10-01` beta header. Or the `billing_policy` object has a missing or invalid field. With a billing connection’s access token, `bill_to` can be left out. Or the request uses code execution outside the allowed combination.                                                                                                                                                                                                                                                                                                                               |
| 400    | `invalid_request_error`, `user_profile_required`           | `bill_to` is `"user_profile"`, the request does not include a user profile ID, and it does not authenticate with a billing connection’s access token.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 400    | `invalid_request_error`, with no error code                | The request authenticates with a billing connection’s access token, and either sets `bill_to` to `"self"` or names a user profile other than the one the token is limited to. Each of these two refusals says what is wrong in `error.message`.                                                                                                                                                                                                                                                                                                                                                                                      |
| 401    | `authentication_error`                                     | The request authenticates with a billing connection’s access token that has expired, that a refresh has replaced, or whose connection has ended. The message says whether the token has expired or has been revoked. Send the request again with the current access token, or link the customer again if the connection has ended. After a connection ends, each new request with its access token can get this 401 or a 403 `user_profile_not_billable`, in no fixed order.                                                                                                                                                         |
| 402    | `billing_error`, `linked_organization_spend_limit_reached` | The customer organization has reached a spend limit it set for your OAuth app or for the whole organization. The Claude API sends the same code when the organization has no credit that can pay for the request. The response does not say which. Ask the customer to check both limits and its credit balance. [Expected errors](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections#expected-errors) for Linked billing says where each is set and what to change.                                                                                                                      |
| 402    | `billing_error`, `linked_organization_billing_unavailable` | Anthropic cannot currently bill the customer organization because of a problem with that organization’s own Anthropic account. The same code ends a reply that Claude has started when the organization’s credit runs out. Ask the customer to check its billing status with Anthropic.                                                                                                                                                                                                                                                                                                                                              |
| 403    | `permission_error`, with no error code                     | Anthropic does not bill your organization directly, so it cannot bill customers on your behalf.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| 403    | `permission_error`, `user_profile_not_billable`            | The user profile has no connection to a customer organization, an administrator or your back end ended the connection, the customer organization does not pay Anthropic directly for its API usage (prepaid credits and invoiced billing both count), or the request does not authenticate as your app’s service account. The response does not say which. A connection’s access token can also get it after the connection has ended. [Causes of `user_profile_not_billable`](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections#user-profile-not-billable) says what to check for each. |
| 503    | `overloaded_error`                                         | The Claude API temporarily cannot confirm whether it can bill the customer. Retry the request. If the response includes a `retry-after` header, wait that long before you retry.                                                                                                                                                                                                                                                                                                                                                                                                                                                     |

On `/v1/messages`, the error code is in `error.details.error_code`. On `/v1/chat/completions`, `error.type` is always `invalid_request_error`, `error.code` contains the Anthropic error type (for example `permission_error` or `billing_error`), and the response has no error code, so match on the HTTP status and `error.code`.

## Standards

| Standard                                                                           | Where it applies                                                                                                                                                  |
| ---------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [OAuth 2.0 (RFC 6749)](https://www.rfc-editor.org/rfc/rfc6749)                     | Authorization code flow, token endpoint, and error responses                                                                                                      |
| [PKCE (RFC 7636)](https://www.rfc-editor.org/rfc/rfc7636)                          | Required with `S256` on every authorization request                                                                                                               |
| [Pushed authorization requests (RFC 9126)](https://www.rfc-editor.org/rfc/rfc9126) | Required for Linked billing.                                                                                                                                      |
| [Token revocation (RFC 7009)](https://www.rfc-editor.org/rfc/rfc7009)              | The revocation endpoint, which also accepts connection and user profile IDs and returns the IDs of the connections it ended                                       |
| [JWT client authentication (RFC 7523)](https://www.rfc-editor.org/rfc/rfc7523)     | The `private_key_jwt` client authentication at the PAR, token, and revocation endpoints, and the service account token exchange for requests that bill a customer |

## Terms used on these pages

The following meanings apply only to Claude Platform OAuth.

| Term                               | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ---------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Claude organization                | An organization account with Anthropic. Your company has one, and so does each customer that links its organization for billing.                                                                                                                                                                                                                                                                                                                    |
| Administrator                      | A member of a Claude organization with the Admin or Billing role.                                                                                                                                                                                                                                                                                                                                                                                   |
| OAuth app                          | The registration in your Claude organization that identifies your product to `auth.claude.com`. It has a client ID, a name, a logo, a homepage URL, redirect URIs, and the connection types it supports.                                                                                                                                                                                                                                            |
| Connection type                    | Who approves a connection: an administrator on behalf of a whole organization (`organization_shared`, for Linked billing).                                                                                                                                                                                                                                                                                                                          |
| Identity provider                  | The service in your own infrastructure that signs short-lived JWTs for your back end and publishes its public keys as a JSON Web Key Set (JWKS), such as your cloud provider’s workload identity service or your own OIDC-compliant issuer. On these pages, “your identity provider” always means this service, not Anthropic.                                                                                                                      |
| Client assertion                   | A short-lived JWT that your identity provider signs and your back end sends to authenticate your OAuth app. This is the `private_key_jwt` client authentication method (RFC 7523).                                                                                                                                                                                                                                                                  |
| Pushed authorization request (PAR) | A request in which your back end sends the authorization parameters directly to `auth.claude.com` and receives a `request_uri` to use in the browser redirect (RFC 9126).                                                                                                                                                                                                                                                                           |
| Workload Identity Federation       | The Claude Console feature through which your organization registers your identity provider, so that Anthropic accepts JWTs signed with the keys in your JWKS.                                                                                                                                                                                                                                                                                      |
| Discovery document                 | The OIDC document that lists Anthropic’s issuer, endpoints, and signing keys.                                                                                                                                                                                                                                                                                                                                                                       |
| User profile                       | A record that you create in your own Claude organization to represent one of your customers. A billing connection links a user profile to the customer’s Claude organization.                                                                                                                                                                                                                                                                       |
| Service account                    | A non-human account in your Claude organization. For Linked billing, your OAuth app is linked to one service account, its operator service account, and your back end authenticates as that service account when it sends a request that bills a customer.                                                                                                                                                                                          |
| Connection’s OAuth tokens          | The access token that `auth.claude.com` returns for a billing connection, and the refresh token that it returns when the customer also approved `offline_access`. The access token authenticates as the operator service account and can bill only that connection’s user profile. See [OAuth tokens for a billing connection](https://platform.claude.com/docs/en/manage-claude/oauth-apps/oauth-reference#oauth-tokens-for-a-billing-connection). |
