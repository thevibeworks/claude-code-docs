---
title: Linked billing
url: https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections
description: Let your customers link their Claude Platform organization to your app with OAuth, and bill Claude usage to the customer's organization.
---

<Warning>
  Claude Platform OAuth is a Beta Service: prerelease software provided under your agreement with Anthropic, such as the [Commercial Terms of Service](https://www.anthropic.com/legal/commercial-terms), and the [Service Specific Terms](https://www.anthropic.com/legal/service-specific-terms). Endpoints, parameters, and behavior can change during the beta. It might not be suitable for production use.
</Warning>

Linked billing lets your customers pay for the Claude usage in your app through their own Claude organization. A customer links their Claude organization to your app once. The API calls this link a connection. After the customer has linked, you choose on each Claude API request whether the customer or you pays. The customer can unlink your app at any time. If a request you mark for the customer can’t be billed to them, the Claude API refuses it rather than billing you.

This guide is for developers whose app users are primarily Claude Platform customers. You add a “Link your Claude organization” button to your app. Your user clicks it, signs in to Claude, and approves your app to bill their Claude organization for the Claude API requests the customer directs you to make. Your app then adds a [`billing_policy`](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections#step-3-update-calls-to-claude) field to the requests that the customer pays for.

## Eligible customers and endpoints

**Eligible customers:** A customer can be billed this way only if their Claude Platform organization pays Anthropic directly for its API usage. Prepaid credits and invoiced billing both count. Organizations billed through a cloud marketplace (AWS, Google Cloud, or Azure) can’t be billed through this integration. The same is true of organizations that have only a Claude subscription plan. Requests for them are refused with 403 `user_profile_not_billable`.

Requests run in your organization, so your rate limits, model access, service tier, data retention, and encryption keys apply. Your customer’s own data arrangements don’t apply to these requests, including [zero data retention (ZDR)](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention#zero-data-retention-zdr-scope), a business associate agreement (BAA), and customer-managed encryption keys (CMEK). Don’t link customers that need HIPAA, FERPA, or CMEK coverage for this usage.

**Supported endpoints:** `billing_policy` is supported on:

* `/v1/messages`
  * Known limitation: a request that bills your customer (`bill_to: "user_profile"`) can’t use [billable code execution features](https://platform.claude.com/docs/en/about-claude/pricing#code-execution-tool) (the API returns a 400), so send those requests with `bill_to: "self"` or without `billing_policy`.
* `/v1/chat/completions`
* `/v1/messages/count_tokens` accepts the `billing_policy` field and ignores it, so you can count tokens on the exact body you’re about to send.

[Message Batches](https://platform.claude.com/docs/en/build-with-claude/batch-processing) (`/v1/messages/batches`) doesn’t currently support billing your customer. Send the requests in a batch with `bill_to: "self"` or without `billing_policy`, and they’re billed to you as usual. A request in a batch that sets `bill_to: "user_profile"` is refused: its result is `errored` with an `invalid_request_error`, neither you nor your customer is billed for it, and the batch’s other requests run as usual.

To ask for support on another endpoint, contact your Anthropic account team.

### Which credits can pay

Not all credit can pay for a request that a platform bills to a customer. What can pay depends on the organization that’s billed: the customer if you bill a customer, or your organization if a platform bills you.

Credit bought in the Claude Console for that organization can pay for these requests. If that organization has invoiced billing, it’s invoiced for these requests.

Some promotional credits from Anthropic can’t pay for these requests. These include the monthly API credits that come with Claude Max, Ultra, and Team plans. Credits from Anthropic’s partner, VC, and startup programs aren’t eligible to pay for these requests.

When nothing on that organization’s account can pay for a request, the Claude API can refuse it with a 402. The response doesn’t say whether a lack of credit or a spend limit caused the refusal. See [Expected errors](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections#expected-errors).

## Setup process

You do these three steps once. They register your app with Anthropic. You need the Admin role in your organization for all three. After them, [Which user profile to link](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections#which-user-profile-to-link) explains a rule that you need before you create user profiles.

### Step 1: Create the app

Create the OAuth app in the Claude Console. It is the registration that identifies your product to Anthropic: it ties your redirect URI to a client ID, and its name is what your user sees on the approval page.

A member of your organization with the Admin role opens the [OAuth apps](https://platform.claude.com/settings/oauth-apps) page in the Console and clicks **Create**. Enter your app’s name and redirect URI (the address in your app that the browser returns to after the approval). Under **What the app can do**, select **Bill and link to organizations**.

The new app’s page opens. Copy the client ID that the Console shows for the app. Your app sends it in Step 5 when it requests an approval page, in Step 6 when it redirects the browser, and in Step 8 when it exchanges the code, so that Anthropic knows which app is asking. The client ID is public. On the **Appearance** tab, set your app’s name, homepage, and logo URL.

On the **Settings** tab, **Who can link** reads **Test users only** for a new app, which starts in testing. After you [publish your app](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections#publish-your-app) and it is live, the setting reads **Any Claude user**.

<Note>
  An organization can register several OAuth apps, for example one for production and one for testing. Each app has its own connections: a customer who links your test app is not linked to your production app. Keep Linked billing on one production app for the life of your integration.
</Note>

### Step 2: Set up client authentication

Set up how your back end proves to `auth.claude.com` that its requests come from your app. This takes the place of a client secret: Anthropic does not issue client secrets for OAuth apps.

On the app’s **Client authentication** tab, select your **Identity provider**. This is the issuer that signs your back end’s tokens, such as AWS, Google Cloud, or Kubernetes. To add one, click **Register a new issuer** or see [Workload Identity Federation](https://platform.claude.com/docs/en/manage-claude/workload-identity-federation). Then, set a **Subject pattern** or claim conditions under **Advanced match options** that those tokens must match. After you save, the tab shows the expected audience. Your client assertion’s `aud` claim must be exactly that value.

Your app authenticates to the PAR, token, and revocation endpoints with a variation of the `private_key_jwt` method (RFC 7523). With each request, your back end sends a client assertion, a JWT that your identity provider issues. `auth.claude.com` checks the token’s signature with the keys registered for that issuer. It also checks the token against the subject or claim conditions you set here. For the claims a client assertion must contain, see [Client assertion claims](https://platform.claude.com/docs/en/manage-claude/oauth-apps/oauth-reference#client-assertion-claims).

### Step 3: Set up your back end’s identity

Your back end needs an identity of its own to call the Claude API. Create two things:

* **A service account.** This is a non-human account in your Claude organization. Your back end authenticates as this account when it calls the Claude API.
* **A second federation rule.** Like the rule for the app’s client authentication in Step 2, it lets your back end authenticate with tokens from your own identity provider.

To set them up in the Claude Console, follow the [Workload Identity Federation](https://platform.claude.com/docs/en/manage-claude/workload-identity-federation) guide.

Then, on the app’s **Client authentication** tab, select that service account as the app’s operator service account. Only that service account is authorized to send inference requests and attribute billing to the linked user profiles. A service account can be the operator of only one OAuth app.

By default, any authenticated request as that service account can bill every linked customer, by setting the user profile header and `bill_to` in the Messages API. To obtain authentication tokens constrained only to a specific connection, see [OAuth tokens for each connection](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections#oauth-tokens-for-each-connection). Before you link customers, [set a workspace](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections#settings-for-a-connections-oauth-tokens) for your app. Step 8 returns such a token for each customer, and requires the app to specify a default workspace in your organization against which inference runs. If you want refresh tokens for each connection, also turn on **Offline access** for your app. Then request `offline_access` in the authorization flow, in Step 5, before you link customers.

### Which user profile to link

A user profile is a record in your own Claude organization that represents one of your customers. Each request that bills the customer includes the profile’s ID, so that Anthropic knows which customer to bill. For the rest of what profiles do, see [User profiles for end-customer attribution](https://platform.claude.com/docs/en/manage-claude/user-profiles).

Settle which user profile stands for each customer before you link your first customer. Within one app, connections are one to one:

* A customer’s Claude organization can be linked to only one of your user profiles.
* A user profile can be linked to only one Claude organization.

The customer’s Claude organization is the one that the user selects when they approve your app. To learn how a customer’s teams use Claude organizations, ask the customer. To apply the one-to-one rule to your customer records:

* **Several teams of one customer share a Claude organization:** Use one user profile for all of the teams.
* **Each team has its own Claude organization:** Create a user profile for each organization.

Any active user profile in your organization can be linked, as long as the one-to-one rule holds. Linking doesn’t change the profile, its ID, or its usage history. If you link a second user profile to a Claude organization that is already linked, the approval is refused: see [`user_profile_already_linked`](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections#user-profile-already-linked).

#### A user profile for each person

You might already have a user profile for each person who uses your product. Several of those people might work for the same customer. In that case, Anthropic recommends that you create one more user profile for the customer’s Claude organization and link that profile.

The profile ID to send depends on who pays for the request:

* **Requests that you bill to the customer:** Send the ID of the customer’s profile. To also identify the person on a `/v1/messages` request, set [`metadata.user_id`](https://platform.claude.com/docs/en/api/messages/create) to an identifier for that person. This identifier is optional and helps Anthropic detect misuse by one person. Use an opaque value, not a name, an email address, or a phone number.
* **Requests that you pay for:** You can keep sending the person’s own profile ID.

## Link each customer

You do Steps 4 to 8 for each customer that links their organization. The following Python code snippets require the Anthropic SDK and some standard imports; see [Code snippet initialization](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections#code-snippet-initialization). The examples in other languages and the CLI take their credentials from the environment. Ensure `ANTHROPIC_API_KEY` is not set, because your app needs to authenticate with Workload Identity Federation.

Add a **Link your Claude organization** button where your customers manage billing or integrations in your product. For the button’s HTML, colors, and logo, see [Branding samples](https://platform.claude.com/docs/en/manage-claude/oauth-apps/branding-samples). Tell your customers that to link, they must have the Admin or Billing role in their Claude organization.

To go through the steps yourself first, see [Test as a customer](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections#test-as-a-customer).

<Frame>
  ![Sequence diagram of Steps 5 to 8: the approval request, the user's approval, and the exchange for a connection ID](https://platform.claude.com/docs/images/oauth-apps-billing-connection-flow.svg)
</Frame>

### Step 4: Create a user profile for the customer

Create one user profile for each customer’s Claude organization, and store the profile’s ID against the customer’s record in your product.

If you already have a user profile for this customer’s Claude organization, skip this step and use that profile’s ID. To decide which profile that is, see [Which user profile to link](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections#which-user-profile-to-link).

<CodeGroup>
  ```bash cURL
  curl https://api.anthropic.com/v1/user_profiles \
    -H "Authorization: Bearer $ACCESS_TOKEN" \
    -H "anthropic-version: 2026-10-21" \
    -H "content-type: application/json" \
    -d '{
      "name": "Example Customer Inc.",
      "external_user_details": {"reference_id": "your-customer-id-123"}
    }'
  ```

  ```bash CLI
  ant user-profiles create \
    --name "Example Customer Inc." \
    --external-user-details.reference-id your-customer-id-123
  ```

  ```python Python
  def create_user_profile(name: str, customer_id: str) -> str:
      profile = client.user_profiles.create(
          name=name,
          external_user_details={"reference_id": customer_id},
      )
      return profile.id  # "uprof_..."


  user_profile_id = create_user_profile("Example Customer Inc.", "your-customer-id-123")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const profile = await client.userProfiles.create({
    name: "Example Customer Inc.",
    external_user_details: { reference_id: "your-customer-id-123" }
  });

  console.log(profile.id); // "uprof_..."
  ```

  ```csharp C#
  AnthropicClient client = new();

  var profile = await client.UserProfiles.Create(
      new()
      {
          Name = "Example Customer Inc.",
          ExternalUserDetails = new() { ReferenceID = "your-customer-id-123" },
      }
  );

  Console.WriteLine(profile.ID);
  ```

  ```go Go
  client := anthropic.NewClient()

  profile, err := client.UserProfiles.New(context.Background(), anthropic.UserProfileNewParams{
  	Name: anthropic.String("Example Customer Inc."),
  	ExternalUserDetails: anthropic.UserProfileExternalUserDetailsParams{
  		ReferenceID: anthropic.String("your-customer-id-123"),
  	},
  })
  if err != nil {
  	log.Fatal(err)
  }

  fmt.Println(profile.ID)
  ```

  ```java Java
  import com.anthropic.models.userprofiles.UserProfileCreateParams;
  import com.anthropic.models.userprofiles.UserProfileExternalUserDetailsParams;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      var params = UserProfileCreateParams.builder()
          .name("Example Customer Inc.")
          .externalUserDetails(UserProfileExternalUserDetailsParams.builder()
              .referenceId("your-customer-id-123")
              .build())
          .build();
      var profile = client.userProfiles().create(params);

      IO.println(profile.id());
  }
  ```

  ```php PHP
  $client = new Client();

  $profile = $client->userProfiles->create(
      name: 'Example Customer Inc.',
      externalUserDetails: ['referenceID' => 'your-customer-id-123'],
  );

  echo $profile->id, PHP_EOL;
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  profile = client.user_profiles.create(
    name: "Example Customer Inc.",
    external_user_details: { reference_id: "your-customer-id-123" }
  )

  puts(profile.id)
  ```
</CodeGroup>

If your organization resells API access, also send `"access_type": "passthrough"` when you create this profile. These samples leave `access_type` out, which creates an `application` profile. For the two types, see [Decide who gets a profile](https://platform.claude.com/docs/en/manage-claude/user-profiles#decide-who-gets-a-profile).

The response contains the profile’s `id`, for example `uprof_01HV9Z`.

<Note>
  Every create request makes a new profile, even with the same `reference_id` (your own ID for the customer), so reuse the stored ID instead of creating a profile on every connection attempt.
</Note>

### Step 5: Create a pushed authorization request URL

Create a pushed authorization request that references the customer’s user profile from Step 4. The response gives you a `request_uri`. In the next step, you use it to redirect your user to the approval page.

Before it sends the request, your back end creates two random values and stores them against the browser session and the customer record. It uses both again in Step 8:

* A `state` value, which lets you check that the browser that comes back to your app is the one that started this request.
* A PKCE code verifier, a secret that only your back end knows. The request carries a hash of it (the code challenge), and Step 8 sends the verifier itself, so that only your back end can use the code that comes back.

<CodeGroup exclude="shell:CLI, typescript, csharp, go, java, php, ruby">
  ```bash cURL
  curl https://auth.claude.com/v1/oauth/par \
    -H "content-type: application/json" \
    -d '{
      "response_type": "code",
      "client_id": "YOUR_CLIENT_ID",
      "redirect_uri": "https://app.example.com/claude/billing/callback",
      "scope": "billing:attribution",
      "connection_type": "organization_shared",
      "connection_auth_target": "platform",
      "user_profile_id": "uprof_01HV9Z",
      "state": "RANDOM_STATE",
      "code_challenge": "BASE64URL_SHA256_OF_VERIFIER",
      "code_challenge_method": "S256",
      "client_assertion_type": "urn:ietf:params:oauth:client-assertion-type:jwt-bearer",
      "client_assertion": "YOUR_CLIENT_ASSERTION_JWT"
    }'
  ```

  ```python Python
  def push_authorization_request(user_profile_id: str) -> dict:
      state = secrets.token_urlsafe(32)
      code_verifier = secrets.token_urlsafe(64)
      code_challenge = create_s256_code_challenge(code_verifier)

      response = httpx.post(
          f"{AUTH}/v1/oauth/par",
          json={
              "response_type": "code",
              "client_id": CLIENT_ID,
              "redirect_uri": REDIRECT_URI,
              "scope": "billing:attribution",
              "connection_type": "organization_shared",
              "connection_auth_target": "platform",
              "user_profile_id": user_profile_id,
              "state": state,
              "code_challenge": code_challenge,
              "code_challenge_method": "S256",
              "client_assertion_type": JWT_BEARER,
              "client_assertion": client_assertion(),
          },
      )
      response.raise_for_status()  # on an error, do not redirect the browser

      return {
          "state": state,
          "code_verifier": code_verifier,
          "request_uri": response.json()["request_uri"],  # valid for 600 seconds
          "user_profile_id": user_profile_id,
      }


  par = push_authorization_request(user_profile_id)
  ```
</CodeGroup>

`auth.claude.com` responds with HTTP 201, a `request_uri`, and `expires_in` of 600 seconds. The `request_uri` identifies the approval page for this request. The `scope` must be exactly `billing:attribution` or `billing:attribution offline_access`. See [Scopes for a billing connection](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections#scopes-for-a-billing-connection) for details. The examples send `billing:attribution`. If your app doesn’t have this scope, add it under **Billing** on the app’s **Permissions** tab.

`connection_auth_target` must be `platform`: inference requests run in your own organization and authenticate as the operator service account, but they can bill the customer.

`user_profile_id` must be the ID of an active user profile in your organization. If the pushed authorization request fails, `auth.claude.com` returns an OAuth error response to your back end. Do not redirect the browser in that case.

### Step 6: Send your user to the Claude approval page

First, show your user which account in your product they are linking, and tell them to check the Claude account that the approval page shows. The page shows which Claude account is signed in and lets the user switch to another. The approval page offers only the organizations of the Claude account that is signed in to the browser, so the wrong account can link the wrong organization. The organization that the user links pays.

<Note>
  The person who approves must be an administrator of the customer’s Claude organization: a member with the Admin or Billing role.
</Note>

Then, redirect your user to the authorization endpoint, which shows an approval page. Include only your `client_id` and the `request_uri` from Step 5.

```python
def authorize_url(par: dict) -> str:
    query = urlencode({"client_id": CLIENT_ID, "request_uri": par["request_uri"]})
    return f"{AUTH}/oauth/authorize?{query}"


redirect_to = authorize_url(par)  # answer the click with a 302 to this URL
```

### Step 7: The user approves

Your app does nothing in this step. The user goes through these steps on `auth.claude.com`:

1. The user signs in to Claude, unless the browser is already signed in.

2. The approval page shows the following screens, each with your app’s name. For what the user does on each screen, see [Linking](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections#connecting).

   1. **Select an organization**, only if the user has a choice of organization.
   2. **How billing works**.
   3. **Set a monthly spend limit**.
   4. A last screen with a **Link and authorize** button.

3. When the user clicks **Link and authorize**, `auth.claude.com` sends the browser back to your app. The approval page shows no confirmation screen.

If the user cancels or can’t approve, no connection is made: see [If linking doesn’t complete](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections#if-linking-doesnt-complete).

<Note>
  The connection belongs to the whole Claude organization, not to the user who approved it. If that user leaves the organization, the connection stays active. Any administrator of the customer’s organization or of yours can end the connection at any time, and so can your back end.
</Note>

### Step 8: Handle the callback and save the connection

After the approval, `auth.claude.com` sends the browser back to your redirect URI with a one-time code and your `state` value. This request to your redirect URI is called the callback. Your back end exchanges the code for a connection ID and stores it on the customer’s record. This completes the connection. The callback can carry an `error` parameter and no code. No connection was made then: see [If linking doesn’t complete](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections#if-linking-doesnt-complete).

Check that the `state` matches the value you stored in Step 5, then exchange the code immediately from your back end, together with the PKCE code verifier. The code is single-use and expires after 5 minutes.

<CodeGroup exclude="shell:CLI, typescript, csharp, go, java, php, ruby">
  ```bash cURL
  curl https://auth.claude.com/v1/oauth/token \
    -H "content-type: application/json" \
    -d '{
      "grant_type": "authorization_code",
      "code": "AUTH_CODE",
      "code_verifier": "ORIGINAL_CODE_VERIFIER",
      "redirect_uri": "https://app.example.com/claude/billing/callback",
      "client_id": "YOUR_CLIENT_ID",
      "client_assertion_type": "urn:ietf:params:oauth:client-assertion-type:jwt-bearer",
      "client_assertion": "YOUR_CLIENT_ASSERTION_JWT"
    }'
  ```

  ```python Python
  def handle_callback(par: dict, params: dict) -> str:
      if not secrets.compare_digest(
          params.get("state", "").encode(), par["state"].encode()
      ):
          raise ValueError("state does not match")
      if "error" in params:  # for example access_denied
          raise PermissionError(params["error"])
      code = params["code"]  # single-use, expires after 5 minutes
      response = httpx.post(
          f"{AUTH}/v1/oauth/token",
          json={
              "grant_type": "authorization_code",
              "code": code,
              "code_verifier": par["code_verifier"],
              "redirect_uri": REDIRECT_URI,
              "client_id": CLIENT_ID,
              "client_assertion_type": JWT_BEARER,
              "client_assertion": client_assertion(),
          },
          timeout=10,  # a response that times out loses the tokens in it
      )
      response.raise_for_status()
      tokens = response.json()
      # To use the connection's tokens, store tokens["access_token"], its expiry
      # time (from tokens["expires_in"]), and, with offline_access,
      # tokens["refresh_token"] as secrets here: the code can't be exchanged again.
      # "ocon_..."; store it on the customer record
      return tokens["connection_id"]
  ```
</CodeGroup>

The response contains the connection ID and [the connection’s access token](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections#oauth-tokens-for-each-connection), which can authenticate and bill the approving customer. If the customer approved `offline_access`, the response also contains a refresh token. Store `connection_id` and the tokens now: the exchange returns the tokens only once. [Store the tokens](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections#keep-the-tokens-from-step-8) describes the response.

The examples on this page that call the Claude API authenticate as the service account from Step 3, not with a token from this response. [Call Claude with a connection’s access token](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections#call-claude-with-a-connections-access-token) says how to use the token in its place.

The response does not identify which Claude organization the user linked.

A completed connection does not guarantee that Anthropic can bill the customer. For example, the customer’s organization might not be one of the [eligible customers](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections#eligible-customers-and-endpoints). See [Update calls to Claude](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections#step-3-update-calls-to-claude) and [Expected errors](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections#expected-errors) for how the Claude API checks this. Because of that check, word your success message as “linked” rather than “billing active.”

If the exchange is refused with `unauthorized_client`, see [The code exchange returns `unauthorized_client`](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections#code-exchange-unauthorized-client).

<Note>
  A user can approve again for a user profile that is already linked. The outcome depends on the scopes:

  * Approved again for the same user profile and the same scopes: the connection stays, and the token response returns the same `connection_id` and a new access token. The exception is a connection with `billing:attribution offline_access`: the code exchange returns `invalid_grant`, the connection stays as it was, and [Link a customer again](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections#connect-a-customer-again) says what to do.
  * Approved again for the same user profile with other scopes, for example `billing:attribution offline_access` after `billing:attribution`: your exchange of the new code makes a new connection with a new `connection_id`, which takes the place of the earlier one. The tokens of an earlier `billing:attribution` connection are revoked. Store the new `connection_id` in place of the earlier one. If the exchange fails with a 5xx response, run Steps 5 to 8 again. [Scopes for a billing connection](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections#scopes-for-a-billing-connection) says when you need this.
  * After a connection is revoked, you can link the same user profile again.
</Note>

### Test as a customer

To check that linking works, link an organization of your own. You need these first:

* A second Claude organization of yours to act as the customer. You can’t link your app to the organization that owns it. The approval page doesn’t offer that organization. The second organization must be one of the [eligible customers](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections#eligible-customers-and-endpoints).
* A person with the Admin or Billing role in that organization to approve the link.
* Until your app is live, that person must be on your app’s **Test users** list. The list is on the app’s **Settings** tab under **Who can link**. Add the person by the email address of their Claude account and click **Save changes**. [While your app is in testing](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections#while-your-app-is-in-testing) has the spend cap that applies. Removing someone from the list ends the links that they approved.

Then, run Steps 4 to 8, and have that person approve in Step 7. When the link is made, the user profile reads **Linked** on your [User profiles](https://platform.claude.com/user-profiles) page in the Console.

### If linking doesn’t complete

When the user doesn’t finish the approval, or `auth.claude.com` refuses it, no connection is made. These entries cover the outcomes that are specific to Linked billing. For every other error, see [Errors](https://platform.claude.com/docs/en/manage-claude/oauth-apps/oauth-reference#errors) in the OAuth reference.

#### Your redirect URI receives `error=access_denied`

The request also carries your `state` value. Your redirect URI receives this error in cases such as these:

1. The user clicks **Cancel** on any approval screen.

2. The approval page has no organization to offer the user, and the user clicks the button that returns to your app. For example:

   * The user doesn’t have the Admin or Billing role in any Claude Platform organization.
   * The user’s only organization is the one that owns your app. See [Test as a customer](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections#test-as-a-customer).
   * The user profile is already linked to another Claude organization, and the user doesn’t have the Admin or Billing role in that organization.
   * Until your app is live, the user isn’t on its **Test users** list.

In each case in this list, the `error_description` reads `the user declined the request`, so you can’t use it to tell them apart.

One more cause is in your app’s settings. If your app is live and **Who can link** shows your organization only, nobody outside your organization can link the app. Select **Any Claude user** and click **Save changes**.

Tell the user that linking didn’t complete, and don’t assume that they declined. Ask them to check which Claude account they signed in with and their role in the organization that they want to link. A `request_uri` can’t be used again after the user cancels or returns, so to let the user try again, start again from Step 5.

#### Your app receives `user_profile_already_linked`

The customer’s Claude organization is already linked to your app through another of your user profiles. `auth.claude.com` asks the user to contact you. If the user returns to your app, your redirect URI receives `error=user_profile_already_linked` and your `state` value. The token endpoint can also return this error when you exchange the code in Step 8. That happens, for example, when the organization was linked through another user profile in the meantime.

Anthropic doesn’t tell you which Claude organization a customer links, so you can’t see this in advance. The pushed authorization request in Step 5 succeeds, and `auth.claude.com` refuses the connection only when the user approves.

The error doesn’t name the user profile that holds the connection. The likeliest holder is another linked profile of this customer. Anthropic doesn’t show which organization a profile is linked to, so confirm with the customer before you act. If that profile holds the connection, do one of the following:

* On the requests that you bill to this customer, send the ID of that user profile.
* End that connection, as [Unlinking a customer](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections#disconnecting-a-customer) describes, and then run Steps 5 to 8 again with the user profile that was refused.

If none of this customer’s profiles is linked, the user might have selected an organization that belongs to another of your customers. Start again from Step 5, and have the user check which organization they select.

#### Your redirect URI receives nothing

Your app can’t detect these two cases:

* The user closes the approval page.
* The `request_uri` has expired or was already used. The approval page then shows an error and doesn’t send the browser back to your app.

If the user comes back to your product without a callback, start again from Step 5. A `request_uri` that wasn’t used expires 10 minutes after you created it.

#### The code exchange returns `unauthorized_client`

Your app is not set up for this request. For a workspace problem, the `error_description` names the cause. For a missing operator service account, it reads only `the client is not registered for this grant`. The refusal doesn’t use up the code, so you can exchange the same code again until it expires. First, check these in the Claude Console:

| Check | Where | Fix |
| ----- | ----- | ----- |
| The app has an operator service account | **Operator service account** on the app’s **Client authentication** tab | Select one and click **Save**. Step 3 says how to set one up. |
| The app’s workspace isn’t missing or archived | [Set up your app](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections#settings-for-a-connections-oauth-tokens) | Choose a workspace. While the app has none, the exchange is refused with `unauthorized_client` too. |

A saved service account can take a minute or two to reach `auth.claude.com`, so if the exchange is refused again, wait that long and retry. If the code has expired by then, have the user approve again (Steps 5 to 8). For the causes that `error_description` names for a connection’s tokens, see [Store the tokens](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections#keep-the-tokens-from-step-8) and [Refresh the tokens](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections#refresh-the-connection).

In any other case, contact your Anthropic account team. Do the same if the Console says that the service account no longer exists.

### Publish your app

Until your app is live, only the people on its **Test users** list can link it, so your customers can’t. To publish the app, click **Publish app** on the app’s page in the Claude Console. A dialog box opens.

* If your organization has invoiced billing, the app is live as soon as you confirm in that dialog box.
* Otherwise, you first prove in that dialog box that you control the app’s domain, and Anthropic then reviews the app.

**The domain proof:** The domain is the domain of your app’s homepage. Every redirect URI must be on that domain or on a subdomain of it, except one on `localhost`, `127.0.0.1`, or `[::1]`. The proof is a DNS TXT record. DNS changes can take up to 48 hours, so start before you need customers to link. If your organization has already proven a domain that covers the homepage and those redirect URIs, the dialog box skips the proof. A proven domain covers its subdomains.

You confirm on the dialog box’s last step. If that step shows a checkbox to accept the Linked Billing Terms, select it. Then, click **Publish app** in the dialog box.

**The review:** During the review, the app’s status in the Console reads **In review**. The app is live when Anthropic approves it. If Anthropic doesn’t approve it, the status reads **Not approved**, and you can’t publish the app again yourself. To ask about the decision, contact support.

Unless your organization has invoiced billing, a change to a live app’s name, logo, homepage, or redirect URIs sends the app back to review. Customers who are already linked stay linked and keep the cap that they saved. Until Anthropic approves the change, only the people on the **Test users** list can link the app.

## Update calls to Claude

Send the `anthropic-user-profile-id` header on each call to `/v1/messages` and `/v1/chat/completions` for a linked customer. On a request that you bill to the customer, the header’s value is the ID of the user profile that holds that customer’s connection. Calls that set `billing_policy` must also send the `user-profiles-billing-2026-10-01` beta header.

Each request for a linked customer is billed either to the customer or to you, and you choose which on each request. The following examples show both.

[OAuth tokens for each connection](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections#oauth-tokens-for-each-connection) describes another way to authenticate a customer’s requests: an access token that can bill only that customer. On `/v1/messages` and `/v1/chat/completions`, a request with such a token can’t be billed to you. It is billed to that customer, even without `billing_policy` or the `anthropic-user-profile-id` header, where those are optional: see the note in [Call Claude with a connection’s access token](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections#call-claude-with-a-connections-access-token). If it names another user profile or sets `bill_to: "self"`, it is refused. Never use one for a request that you pay for.

### Your customer pays

Add `billing_policy` with `bill_to: "user_profile"` to the request body, and send the billing beta header and the profile ID header.

<Warning>
  Check that the header names the profile of the customer that the request is for. By default, your operator service account’s own credential can bill every customer linked through this app. If a request with that credential names a different profile linked through this app, Anthropic bills that profile’s organization, and no error tells you. A [connection’s access token](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections#oauth-tokens-for-each-connection) can bill only its own customer.
</Warning>

Set `bill_to: "user_profile"` only on requests the customer directs you to make: the Claude usage that the customer and their users cause in your product. Don’t bill a customer for your own usage, such as testing, evaluations, or work for other customers. The Claude API can’t check this for you, so it’s your responsibility.

<CodeGroup>
  ```bash cURL
  curl https://api.anthropic.com/v1/messages \
    -H "Authorization: Bearer $ACCESS_TOKEN" \
    -H "anthropic-version: 2026-10-21" \
    -H "anthropic-beta: user-profiles-billing-2026-10-01" \
    -H "anthropic-user-profile-id: uprof_01HV9Z" \
    -H "content-type: application/json" \
    -d '{
      "model": "claude-sonnet-5-5",
      "max_tokens": 1024,
      "messages": [{"role": "user", "content": "Hello, Claude"}],
      "billing_policy": {"type": "billing_policy", "bill_to": "user_profile"}
    }'
  ```

  ```bash CLI
  ant beta:messages create \
    --beta user-profiles-billing-2026-10-01 \
    --user-profile-id uprof_01HV9Z \
    --model claude-sonnet-5-5 \
    --max-tokens 1024 \
    --message '{role: user, content: "Hello, Claude"}' <<'YAML'
  billing_policy:
    type: billing_policy
    bill_to: user_profile
  YAML
  ```

  ```python Python
  def message_billed_to_user(user_profile_id: str, prompt: str) -> BetaMessage:
      return client.beta.messages.create(
          model="claude-opus-5-5",
          max_tokens=1024,
          messages=[{"role": "user", "content": prompt}],
          betas=[BILLING_BETA],
          extra_headers={"anthropic-user-profile-id": user_profile_id},
          extra_body={
              "billing_policy": {"type": "billing_policy", "bill_to": "user_profile"}
          },
      )
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const message = await client.beta.messages.create({
    model: "claude-sonnet-5-5",
    max_tokens: 1024,
    messages: [{ role: "user", content: "Hello, Claude" }],
    betas: ["user-profiles-billing-2026-10-01"],
    user_profile_id: "uprof_01HV9Z",
    billing_policy: { type: "billing_policy", bill_to: "user_profile" }
  });

  console.log(message.content);
  ```

  ```csharp C#
  using Anthropic.Models.Beta.Messages;
  using System.Text.Json;
  using Model = Anthropic.Models.Messages.Model;

  AnthropicClient client = new();

  var parameters = new MessageCreateParams
  {
      Model = Model.ClaudeSonnet5_5,
      MaxTokens = 1024,
      Messages = [new BetaUserMessageParam { Content = "Hello, Claude" }],
      Betas = ["user-profiles-billing-2026-10-01"],
      UserProfileID = "uprof_01HV9Z",
  };
  var body = new Dictionary<string, JsonElement>(parameters.RawBodyData)
  {
      ["billing_policy"] = JsonSerializer.SerializeToElement(
          new { type = "billing_policy", bill_to = "user_profile" }
      ),
  };

  var message = await client.Beta.Messages.Create(
      MessageCreateParams.FromRawUnchecked(parameters.RawHeaderData, parameters.RawQueryData, body)
  );

  Console.WriteLine(string.Join("\n", message.Content));
  ```

  ```go Go
  client := anthropic.NewClient()

  params := anthropic.BetaMessageNewParams{
  	Model:     anthropic.ModelClaudeSonnet5_5,
  	MaxTokens: 1024,
  	Messages: []anthropic.BetaMessageParam{
  		anthropic.NewBetaUserMessage(anthropic.NewBetaTextBlock("Hello, Claude")),
  	},
  	Betas:         []anthropic.AnthropicBeta{"user-profiles-billing-2026-10-01"},
  	UserProfileID: anthropic.String("uprof_01HV9Z"),
  }
  params.SetExtraFields(map[string]any{
  	"billing_policy": map[string]string{
  		"type":    "billing_policy",
  		"bill_to": "user_profile",
  	},
  })

  message, err := client.Beta.Messages.New(context.Background(), params)
  if err != nil {
  	log.Fatal(err)
  }

  fmt.Printf("%+v\n", message.Content)
  ```

  ```java Java
  import com.anthropic.core.JsonValue;
  import com.anthropic.models.beta.messages.MessageCreateParams;
  import com.anthropic.models.messages.Model;
  import java.util.Map;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      var params = MessageCreateParams.builder()
          .model(Model.CLAUDE_SONNET_5_5)
          .maxTokens(1024)
          .addUserMessage("Hello, Claude")
          .addBeta("user-profiles-billing-2026-10-01")
          .userProfileId("uprof_01HV9Z")
          .putAdditionalBodyProperty("billing_policy", JsonValue.from(Map.of(
              "type", "billing_policy",
              "bill_to", "user_profile")))
          .build();
      var message = client.beta().messages().create(params);

      IO.println(message.content());
  }
  ```

  ```php PHP
  use Anthropic\Messages\Model;

  $client = new Client();

  $message = $client->beta->messages->create(
      maxTokens: 1024,
      messages: [['role' => 'user', 'content' => 'Hello, Claude']],
      model: Model::CLAUDE_SONNET_5_5,
      betas: ['user-profiles-billing-2026-10-01'],
      userProfileID: 'uprof_01HV9Z',
      requestOptions: [
          'extraBodyParams' => [
              'billing_policy' => ['type' => 'billing_policy', 'bill_to' => 'user_profile'],
          ],
      ],
  );

  echo $message;
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  message = client.beta.messages.create(
    model: Anthropic::Model::CLAUDE_SONNET_5_5,
    max_tokens: 1024,
    messages: [{ role: "user", content: "Hello, Claude" }],
    betas: ["user-profiles-billing-2026-10-01"],
    user_profile_id: "uprof_01HV9Z",
    request_options: {
      extra_body: { billing_policy: { type: "billing_policy", bill_to: "user_profile" } }
    }
  )

  puts(message.content)
  ```
</CodeGroup>

If the request is refused, see [Expected errors](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections#expected-errors).

### You pay

To pay yourself, either omit the `billing_policy` entirely (in which case the billing beta header is optional):

<CodeGroup>
  ```bash cURL
  curl https://api.anthropic.com/v1/messages \
    -H "Authorization: Bearer $ACCESS_TOKEN" \
    -H "anthropic-version: 2026-10-21" \
    -H "anthropic-user-profile-id: uprof_01HV9Z" \
    -H "content-type: application/json" \
    -d '{
      "model": "claude-opus-5-5",
      "max_tokens": 1024,
      "messages": [{"role": "user", "content": "Hello, Claude"}]
    }'
  ```

  ```bash CLI
  ant messages create \
    --user-profile-id uprof_01HV9Z \
    --model claude-sonnet-5-5 \
    --max-tokens 1024 \
    --message '{role: user, content: "Hello, Claude"}'
  ```

  ```python Python
  def message_billed_to_you(user_profile_id: str, prompt: str) -> Message:
      return client.messages.create(
          model="claude-opus-5-5",
          max_tokens=1024,
          messages=[{"role": "user", "content": prompt}],
          user_profile_id=user_profile_id,
      )
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const message = await client.messages.create({
    model: "claude-sonnet-5-5",
    max_tokens: 1024,
    messages: [{ role: "user", content: "Hello, Claude" }],
    user_profile_id: "uprof_01HV9Z"
  });

  console.log(message.content);
  ```

  ```csharp C#
  AnthropicClient client = new();

  var message = await client.Messages.Create(
      new MessageCreateParams
      {
          Model = Model.ClaudeSonnet5_5,
          MaxTokens = 1024,
          Messages = [new UserMessageParam { Content = "Hello, Claude" }],
          UserProfileID = "uprof_01HV9Z",
      }
  );

  Console.WriteLine(string.Join("\n", message.Content));
  ```

  ```go Go
  client := anthropic.NewClient()

  message, err := client.Messages.New(context.Background(), anthropic.MessageNewParams{
  	Model:     anthropic.ModelClaudeSonnet5_5,
  	MaxTokens: 1024,
  	Messages: []anthropic.MessageParam{
  		anthropic.NewUserMessage(anthropic.NewTextBlock("Hello, Claude")),
  	},
  	UserProfileID: anthropic.String("uprof_01HV9Z"),
  })
  if err != nil {
  	log.Fatal(err)
  }

  fmt.Printf("%+v\n", message.Content)
  ```

  ```java Java
  import com.anthropic.models.messages.MessageCreateParams;
  import com.anthropic.models.messages.Model;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      var params = MessageCreateParams.builder()
          .model(Model.CLAUDE_SONNET_5_5)
          .maxTokens(1024)
          .addUserMessage("Hello, Claude")
          .userProfileId("uprof_01HV9Z")
          .build();
      var message = client.messages().create(params);

      IO.println(message.content());
  }
  ```

  ```php PHP
  use Anthropic\Messages\Model;

  $client = new Client();

  $message = $client->messages->create(
      maxTokens: 1024,
      messages: [['role' => 'user', 'content' => 'Hello, Claude']],
      model: Model::CLAUDE_SONNET_5_5,
      userProfileID: 'uprof_01HV9Z',
  );

  echo $message;
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  message = client.messages.create(
    model: Anthropic::Model::CLAUDE_SONNET_5_5,
    max_tokens: 1024,
    messages: [{ role: "user", content: "Hello, Claude" }],
    user_profile_id: "uprof_01HV9Z"
  )

  puts(message.content)
  ```
</CodeGroup>

or use `bill_to: "self"`:

<CodeGroup>
  ```bash cURL
  curl https://api.anthropic.com/v1/messages \
    -H "Authorization: Bearer $ACCESS_TOKEN" \
    -H "anthropic-version: 2026-10-21" \
    -H "anthropic-beta: user-profiles-billing-2026-10-01" \
    -H "anthropic-user-profile-id: uprof_01HV9Z" \
    -H "content-type: application/json" \
    -d '{
      "model": "claude-sonnet-5-5",
      "max_tokens": 1024,
      "messages": [{"role": "user", "content": "Hello, Claude"}],
      "billing_policy": {"type": "billing_policy", "bill_to": "self"}
    }'
  ```

  ```bash CLI
  ant beta:messages create \
    --beta user-profiles-billing-2026-10-01 \
    --user-profile-id uprof_01HV9Z \
    --model claude-sonnet-5-5 \
    --max-tokens 1024 \
    --message '{role: user, content: "Hello, Claude"}' <<'YAML'
  billing_policy:
    type: billing_policy
    bill_to: self
  YAML
  ```

  ```python Python
  def message_billed_to_self(user_profile_id: str, prompt: str) -> BetaMessage:
      return client.beta.messages.create(
          model="claude-opus-5-5",
          max_tokens=1024,
          messages=[{"role": "user", "content": prompt}],
          betas=[BILLING_BETA],
          extra_headers={"anthropic-user-profile-id": user_profile_id},
          extra_body={"billing_policy": {"type": "billing_policy", "bill_to": "self"}},
      )
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const message = await client.beta.messages.create({
    model: "claude-sonnet-5-5",
    max_tokens: 1024,
    messages: [{ role: "user", content: "Hello, Claude" }],
    betas: ["user-profiles-billing-2026-10-01"],
    user_profile_id: "uprof_01HV9Z",
    billing_policy: { type: "billing_policy", bill_to: "self" }
  });

  console.log(message.content);
  ```

  ```csharp C#
  using Anthropic.Models.Beta.Messages;
  using System.Text.Json;
  using Model = Anthropic.Models.Messages.Model;

  AnthropicClient client = new();

  var parameters = new MessageCreateParams
  {
      Model = Model.ClaudeSonnet5_5,
      MaxTokens = 1024,
      Messages = [new BetaUserMessageParam { Content = "Hello, Claude" }],
      Betas = ["user-profiles-billing-2026-10-01"],
      UserProfileID = "uprof_01HV9Z",
  };
  var body = new Dictionary<string, JsonElement>(parameters.RawBodyData)
  {
      ["billing_policy"] = JsonSerializer.SerializeToElement(
          new { type = "billing_policy", bill_to = "self" }
      ),
  };

  var message = await client.Beta.Messages.Create(
      MessageCreateParams.FromRawUnchecked(parameters.RawHeaderData, parameters.RawQueryData, body)
  );

  Console.WriteLine(string.Join("\n", message.Content));
  ```

  ```go Go
  client := anthropic.NewClient()

  params := anthropic.BetaMessageNewParams{
  	Model:     anthropic.ModelClaudeSonnet5_5,
  	MaxTokens: 1024,
  	Messages: []anthropic.BetaMessageParam{
  		anthropic.NewBetaUserMessage(anthropic.NewBetaTextBlock("Hello, Claude")),
  	},
  	Betas:         []anthropic.AnthropicBeta{"user-profiles-billing-2026-10-01"},
  	UserProfileID: anthropic.String("uprof_01HV9Z"),
  }
  params.SetExtraFields(map[string]any{
  	"billing_policy": map[string]string{
  		"type":    "billing_policy",
  		"bill_to": "self",
  	},
  })

  message, err := client.Beta.Messages.New(context.Background(), params)
  if err != nil {
  	log.Fatal(err)
  }

  fmt.Printf("%+v\n", message.Content)
  ```

  ```java Java
  import com.anthropic.core.JsonValue;
  import com.anthropic.models.beta.messages.MessageCreateParams;
  import com.anthropic.models.messages.Model;
  import java.util.Map;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      var params = MessageCreateParams.builder()
          .model(Model.CLAUDE_SONNET_5_5)
          .maxTokens(1024)
          .addUserMessage("Hello, Claude")
          .addBeta("user-profiles-billing-2026-10-01")
          .userProfileId("uprof_01HV9Z")
          .putAdditionalBodyProperty("billing_policy", JsonValue.from(Map.of(
              "type", "billing_policy",
              "bill_to", "self")))
          .build();
      var message = client.beta().messages().create(params);

      IO.println(message.content());
  }
  ```

  ```php PHP
  use Anthropic\Messages\Model;

  $client = new Client();

  $message = $client->beta->messages->create(
      maxTokens: 1024,
      messages: [['role' => 'user', 'content' => 'Hello, Claude']],
      model: Model::CLAUDE_SONNET_5_5,
      betas: ['user-profiles-billing-2026-10-01'],
      userProfileID: 'uprof_01HV9Z',
      requestOptions: [
          'extraBodyParams' => [
              'billing_policy' => ['type' => 'billing_policy', 'bill_to' => 'self'],
          ],
      ],
  );

  echo $message;
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  message = client.beta.messages.create(
    model: Anthropic::Model::CLAUDE_SONNET_5_5,
    max_tokens: 1024,
    messages: [{ role: "user", content: "Hello, Claude" }],
    betas: ["user-profiles-billing-2026-10-01"],
    user_profile_id: "uprof_01HV9Z",
    request_options: {
      extra_body: { billing_policy: { type: "billing_policy", bill_to: "self" } }
    }
  )

  puts(message.content)
  ```
</CodeGroup>

## OAuth tokens for each connection

Your back end calls the Claude API as your app’s operator service account (Step 3). By default, any authenticated request as that service account can bill every linked customer, by passing a user profile ID header and including `bill_to` in Messages API requests. This default is called operator-only tokenless authentication.

To handle single-tenant deployments of your product, or customer-controlled sandbox environments, you can obtain connection-bound OAuth access and refresh tokens instead of using operator-only tokenless authentication.

For each connection, the code exchange in Step 8 returns that connection’s own access token. The token authenticates as your operator service account, but it can bill only that connection’s customer. It expires within 1 hour.

To authenticate each connection separately:

* **Use offline access.** Turn on [**Offline access**](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections#settings-for-a-connections-oauth-tokens) for your app, and request `offline_access` in Step 5. Each connection then also gets a refresh token, which your back end uses to request new access tokens. Without it, the customer must approve again to give you a new access token: run Steps 5 to 8 again with the same `scope`.
* **Set a default workspace.** [Choose a workspace](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections#settings-for-a-connections-oauth-tokens) in your organization for requests with these tokens to run in.
* **Optionally, turn off operator-only tokenless authentication.** By default, you can still bill a linked customer as your operator service account (by passing a user profile header and `bill_to`), even after the customer’s access token expires. After you [turn off operator-only authentication](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections#turn-off-operator-only-authentication), every request that bills a customer must authenticate with that customer’s access token.
* **Use `billing:attribution`.** Only this scope gives a connection its own tokens. You can still bill a linked customer as your operator service account, as with `org:billing_attribution`, which is deprecated. See [Scopes for a billing connection](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections#scopes-for-a-billing-connection).

### Set up your app

Requests with a connection’s access token run in one workspace of your organization. Every app needs one, even if you don’t use these tokens: while your app has no workspace, the code exchange in Step 8 is refused with `unauthorized_client`.

A member of your organization with the Admin role opens the app’s **Client authentication** tab in the Console. Under the operator service account, find **Default workspace for platform auth mode OAuth tokens** (the app’s `connection_token_workspace_id` setting) and click **Choose workspace**. Select a workspace that the operator service account (Step 3) is a member of. The workspace must not be archived.

To get refresh tokens, turn on **Offline access** on the app’s **Permissions** tab. A change to the app’s scopes takes a few minutes to reach `auth.claude.com`.

<Note>
  Archiving the default workspace revokes every token that runs in it, and it can’t be undone. To move to another workspace, set the new one and wait a few minutes. A refresh before the change reaches `auth.claude.com` can return tokens that still run in the earlier workspace. Then, refresh every connection that has a refresh token, and only then archive the earlier workspace. If you archive a workspace first, stop refreshing its connections before you set another one: a later refresh ends the connection.

  Don’t change or archive the app’s operator service account while a customer is linked. After you change or archive it, `auth.claude.com` refuses every refresh, and the tokens that you hold soon stop billing customers. Each customer whose tokens you use must then link again: for help, [contact support](https://support.claude.com/en/articles/9015913-how-to-get-support).
</Note>

### Scopes for a billing connection

In Step 5, send `scope` as `billing:attribution`. To also get a refresh token, send `billing:attribution offline_access`.

To change the scopes of a customer who is already linked, for example to add `offline_access`, run Steps 5 to 8 again with the customer’s existing user profile and the new `scope`. You don’t unlink first. The code exchange returns a new `connection_id`, and the new connection replaces the earlier one. See the note in Step 8.

An app can have `billing:attribution` and the deprecated `org:billing_attribution` at once. You add `billing:attribution` under **Billing** on the app’s **Permissions** tab. If you remove `org:billing_attribution` there, you can’t add it again. A connection that a customer approved with `org:billing_attribution` keeps billing through your operator service account until the connection ends or you [turn off operator-only authentication](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections#turn-off-operator-only-authentication).

### Store the tokens

The code exchange returns the tokens only once, so store them in Step 8. The response contains `access_token`, `expires_in` (at most 1 hour, in seconds), and `connection_id`. If the customer approved `offline_access`, it also contains `refresh_token` and `refresh_token_expires_in`. A refresh token lasts at most 1 year, and a refresh doesn’t extend that. After that, [link the customer again](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections#connect-a-customer-again).

Store the tokens and their expiry times in a secret store that only the service that refreshes can read.

If the exchange is refused with `unauthorized_client`, `error_description` gives the cause, such as a missing or archived workspace. The code isn’t used up: correct the cause, and send the same code again before it expires.

### Call Claude with a connection’s access token

<Note>
  During the beta, ask your Anthropic account team whether Claude API requests with a connection’s access token are enabled for your organization. While they aren’t, every such request fails, whatever it sends. Also ask whether the `anthropic-user-profile-id` header and `billing_policy` are optional. While they aren’t, send every `/v1/messages` and `/v1/chat/completions` request that uses a connection’s access token as [Your customer pays](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections#your-customer-pays) shows, with the header, `bill_to: "user_profile"`, and the billing beta header.
</Note>

Send the connection’s access token as a bearer token in the `Authorization` header, in place of your operator service account’s own credential. Don’t send an `x-api-key` header. In the Anthropic SDK, pass the token as `auth_token` (typescript, php: `authToken`; java: `.authToken()`; csharp: `AuthToken`; go: `option.WithAuthToken()`), or set the `ANTHROPIC_AUTH_TOKEN` environment variable.

On `/v1/messages` and `/v1/chat/completions`, the request is billed to that connection’s customer. The `anthropic-user-profile-id` header and `billing_policy` are optional. You need the billing beta header only with `billing_policy`.

On these two endpoints, you can’t pay for a request with this token. Use the token only on these two endpoints, `/v1/messages/count_tokens`, and the Models endpoints. Send every other request, and every request that you pay for, as your operator service account, from your own back end. That includes a request that uses [billable code execution features](https://platform.claude.com/docs/en/about-claude/pricing#code-execution-tool), which can’t bill a customer.

The Claude API refuses these requests:

* `400 invalid_request_error`, with no error code: the request named another user profile or set `bill_to: "self"`.
* `403 permission_error`, with no error code: the request went to a [Message Batches](https://platform.claude.com/docs/en/build-with-claude/batch-processing) endpoint.
* `401 authentication_error`: the token expired, a refresh replaced it, or its connection ended. After a connection ends, the response can also be `403 user_profile_not_billable`.

### Refresh the tokens

To renew a connection’s access token, send its refresh token to the token endpoint, `https://auth.claude.com/v1/oauth/token`, with your app’s [client authentication](https://platform.claude.com/docs/en/manage-claude/oauth-apps/oauth-reference#client-authentication). Don’t send a `scope` parameter.

<CodeGroup exclude="shell:CLI, typescript, csharp, go, java, php, ruby">
  ```bash cURL
  curl https://auth.claude.com/v1/oauth/token \
    -H "content-type: application/json" \
    -d @- <<JSON
  {
    "grant_type": "refresh_token",
    "refresh_token": "$CONNECTION_REFRESH_TOKEN",
    "client_id": "YOUR_CLIENT_ID",
    "client_assertion_type": "urn:ietf:params:oauth:client-assertion-type:jwt-bearer",
    "client_assertion": "$CLIENT_ASSERTION"
  }
  JSON
  ```

  ```python Python
  connection_locks: defaultdict[str, threading.Lock] = defaultdict(threading.Lock)


  def error_body(response: httpx.Response) -> dict:
      try:
          body = response.json()
      except ValueError:
          return {}
      return body if isinstance(body, dict) else {}


  def is_lost(response: httpx.Response) -> bool:
      """True for a 5xx response that can follow a refresh that took effect."""
      if response.status_code < 500:
          return False
      # A 503 in the Claude API's format with a retry-after header is a refusal
      # that doesn't use the refresh token. Every other 5xx response counts as lost.
      paused = (
          response.status_code == 503
          and error_body(response).get("type") == "error"
          and "retry-after" in response.headers
      )
      return not paused


  def hold_error(connection_id: str, reason: str) -> RefreshOnHold:
      return RefreshOnHold(
          f"Connection {connection_id} is on hold. {reason} Don't send its refresh token"
          ' again: that can end the connection. See "Link a customer again" in the'
          " Linked billing guide."
      )


  def refresh_connection(connection_id: str, *, force: bool = False) -> tuple[str, int]:
      """Refreshes the connection if its access token is close to its expiry.

      Returns the current access token and its expiry time in Unix seconds. Call
      this from your schedule, and pass force=True to refresh a token that isn't
      close to its expiry. Raises RefreshOnHold when the refresh token can't be sent
      again, now and on every later call, and httpx.HTTPStatusError for a refusal
      that keeps the refresh token. After RefreshOnHold for a lost refresh, pause
      your schedule. Resume with one connection, and resume the others only after
      that refresh succeeds or gets a 4xx.
      """
      # This lock works inside one process. If the service has replicas, use a lock
      # that all of them share.
      with connection_locks[connection_id]:
          tokens = load_tokens(connection_id)
          if tokens.on_hold:
              raise hold_error(
                  connection_id, "An earlier refresh might have used its refresh token."
              )
          if not force and tokens.expires_at - time.time() > REFRESH_MARGIN_SECONDS:
              return tokens.access_token, tokens.expires_at  # not close to expiry
          request = {
              "grant_type": "refresh_token",
              "refresh_token": tokens.refresh_token,
              "client_id": CLIENT_ID,
              "client_assertion_type": JWT_BEARER,
              "client_assertion": client_assertion(),
          }
          url = f"{AUTH}/v1/oauth/token"
          # Put the connection on hold before the refresh token leaves this process.
          # If the process stops before the new tokens are saved, the hold stays.
          save_tokens(connection_id, replace(tokens, on_hold=True))
          issued_at = int(time.time())
          started = time.monotonic()
          # httpx doesn't retry by itself. Don't add retries: a late retry ends the
          # connection.
          try:
              response = httpx.post(url, json=request, timeout=REQUEST_TIMEOUT)
              lost = is_lost(response)
          except (httpx.ConnectError, httpx.ConnectTimeout):
              # No connection was made, so the refresh token never left this process.
              save_tokens(connection_id, tokens)
              raise
          except httpx.TransportError:
              lost = True
          if lost:
              # The first request might have used the refresh token. A second request
              # is safe only inside the limit above, so send one at once or not at
              # all.
              if time.monotonic() - started > SECOND_REQUEST_DEADLINE_SECONDS:
                  raise hold_error(connection_id, "A refresh got no usable answer.")
              try:
                  response = httpx.post(url, json=request, timeout=REQUEST_TIMEOUT)
              except httpx.TransportError:
                  raise hold_error(
                      connection_id, "Two refreshes got no answer."
                  ) from None
              if response.status_code != 200:
                  # After any answer but new tokens you can't tell whether the
                  # first request took effect, and a later request isn't safe.
                  raise hold_error(connection_id, "The second refresh failed.")
          if error_body(response).get("error") == "invalid_grant":
              # Expired, already used, or the connection ended. Sending it again
              # can end the connection.
              raise hold_error(connection_id, "The refresh returned invalid_grant.")
          if response.status_code != 200:
              # A refusal that keeps the refresh token, so take the hold off.
              save_tokens(connection_id, tokens)
              response.raise_for_status()
          body = response.json()
          tokens = ConnectionTokens(
              refresh_token=body["refresh_token"],
              access_token=body["access_token"],
              expires_at=issued_at + body["expires_in"],
              refresh_expires_at=issued_at + body["refresh_token_expires_in"],
          )
          # If the write fails, try the write again. Don't refresh again.
          for attempt in range(5):
              try:
                  save_tokens(connection_id, tokens)
                  return tokens.access_token, tokens.expires_at
              except OSError:  # your secret store's error type
                  if attempt < 4:
                      time.sleep(2**attempt)
          # The new tokens exist only in this process, and the stored refresh token
          # is used up. The stored record is still on hold. The error carries the new
          # tokens, so that the caller can store them when the secret store is back.
          error = hold_error(
              connection_id,
              "The refresh succeeded, but the new tokens could not be saved.",
          )
          error.new_tokens = tokens
          raise error
  ```
</CodeGroup>

The response contains a new `access_token` and a new `refresh_token`. The refresh token that you sent is replaced: don’t send it again, except as the list of failures that follows says. The earlier access token stops working within a few minutes. [OAuth token snippet initialization](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections#oauth-token-snippet-initialization) defines the functions that the example calls.

* Store the new refresh token before you use the new access token.
* Refresh each connection’s tokens from one service, one refresh at a time. If the service has replicas, use a lock that all of them share. A used refresh token that arrives again more than 30 seconds after its first use ends the connection. Every token is revoked, the customer displays as **Unlinked**, and no credential can bill them until they link again.
* Turn off automatic retries for the refresh request, in your HTTP client and in any proxy.

If the first request with a refresh token fails:

* The request couldn’t connect: the refresh token wasn’t sent. Try again later.

* A dropped connection, or any 5xx response other than the `503` in this list: you can’t tell whether the request took effect, so send the same refresh token one more time.

  1. Send it at once, and only if less than 30 seconds have passed since you sent the first request.
  2. If it returns new tokens, store them and use only them. If the first request did take effect, its tokens, which never reached you, are revoked.
  3. If it returns anything else or gets no answer, or if the 30 seconds have passed, don’t send that refresh token again. Stop refreshing that connection, and [link the customer again](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections#connect-a-customer-again).

* A timeout: the request might still be running. Don’t send that refresh token again. Stop refreshing that connection, and [link the customer again](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections#connect-a-customer-again).

* `429`, or `503` with a `retry-after` header and `"type": "error"` at the top level of its body: nothing is revoked. Wait at least as long as the header says, and send the same refresh token again.

* `unauthorized_client` or `invalid_client`: nothing is revoked. `error_description` gives the cause, such as a missing workspace, `offline_access` no longer registered for your app, or a failed client assertion. Correct it, and send the same refresh token again.

* `invalid_scope`: the request sent a `scope` parameter, or `billing:attribution` is no longer registered for your app. Nothing is revoked. Correct the cause, and send the same refresh token again.

* `invalid_grant`: the refresh token expired or was already used, the connection ended, or the customer’s organization is suspended. Stop refreshing that connection, and follow [Link a customer again](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections#connect-a-customer-again), which starts with a check for a suspension.

If a dropped connection, a 5xx response, or a timeout has made you stop refreshing a connection, also pause the refreshes of your other connections. When you resume, refresh one connection first, and resume the others only after that refresh succeeds or gets a 4xx response.

### Run an agent in a sandbox

Give a sandbox only the access token, never the refresh token. Your back end refreshes, and it sends each new access token to the sandbox. It decides which customer a sandbox serves from the sandbox’s own identity, such as its pod identity, and never from a value that the sandbox sends. It sends a sandbox only that customer’s token. The sandbox must not be able to get a JWT that matches one of your federation rules or your app’s client authentication. Give it no mounted identity token and no access to a cloud metadata server.

Claude Code, the [Claude Agent SDK](https://code.claude.com/docs/en/agent-sdk/overview), and the Anthropic SDK can read the token from a credentials file in a configuration profile (see [Profile configuration file](https://platform.claude.com/docs/en/manage-claude/wif-reference#profile-configuration-file)). In the sandbox, create a configuration directory with this profile. Don’t add a `client_id` to it: with one, the SDK tries to refresh the token itself.

```json configs/customer.json
{
  "version": "1.0",
  "authentication": {
    "type": "user_oauth"
  }
}
```

Write the access token as `credentials/customer.json` in the same directory, before the agent starts and after each refresh. `expires_at` is the expiry time in Unix seconds. Write a new file with mode `0600`, and rename it over the old one:

```json credentials/customer.json
{
  "type": "oauth_token",
  "access_token": "sk-ant-oat01-...",
  "expires_at": 1793635200
}
```

Set `ANTHROPIC_CONFIG_DIR` to the configuration directory and `ANTHROPIC_PROFILE` to `customer`. Unset every other credential in the sandbox, such as `ANTHROPIC_API_KEY`, `ANTHROPIC_AUTH_TOKEN`, `CLAUDE_CODE_OAUTH_TOKEN`, and Claude Code’s `apiKeyHelper` setting, because each can take precedence over the profile. The agent reads the file again in the last 2 minutes before `expires_at`, and after a 401 response.

```python
def write_credentials_file(
    config_dir: Path, profile: str, token: str, expires_at: int
) -> None:
    credentials_dir = config_dir / "credentials"
    credentials_dir.mkdir(mode=0o700, parents=True, exist_ok=True)
    body = {"type": "oauth_token", "access_token": token, "expires_at": expires_at}
    # Rename a finished file into place, so that the agent never reads half a file.
    # mkstemp sets mode 0600 with the current user as owner, so run this as the
    # agent's user.
    handle, temporary_path = tempfile.mkstemp(dir=credentials_dir)
    with os.fdopen(handle, "w") as temporary_file:
        json.dump(body, temporary_file)
    os.replace(temporary_path, credentials_dir / f"{profile}.json")
```

### Link a customer again

Link a customer again in these cases:

* A refresh returned `invalid_grant`.
* You lost a refresh token, or one leaked.
* You lost the response in Step 8 for `billing:attribution offline_access`, or Step 8 returned `invalid_grant` for such a connection.
* A refresh token is close to its expiry.

Follow these steps:

1. On your [User profiles](https://platform.claude.com/user-profiles) page, check whether the customer displays as **Linked**. After `invalid_grant`, first ask your Anthropic account team whether the customer’s organization is suspended: after a suspension ends, the refresh token that you hold works again. If every connection returns `invalid_grant` at the same time, look for a cause on your side, such as an archived workspace, before you unlink anyone.
2. If the customer displays as **Linked**, unlink them, as [Unlinking a customer](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections#disconnecting-a-customer) describes. Unlinking revokes the connection’s tokens. Do it when an administrator of the customer’s organization is ready to approve, because billing through the connection stops until they do.
3. Run Steps 5 to 8 again with the customer’s existing user profile. Store the new connection ID and the new tokens in place of the earlier ones.

### Turn off operator-only authentication

<Note>
  During the beta, ask your Anthropic account team whether this setting is available for your organization. While it isn’t, you can’t turn it on.
</Note>

To stop requests that authenticate only as your operator service account from billing customers, turn on **Disable operator-only tokenless authentication** (the app’s `disable_operator_only_auth` setting). It is on the app’s **Client authentication** tab, under the operator service account. Your app must have the `billing:attribution` and `offline_access` scopes and a [workspace for its OAuth tokens](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections#settings-for-a-connections-oauth-tokens). Before you turn it on, make sure that every linked customer has approved `billing:attribution offline_access` and that your requests with their access tokens work. While it is on, only the access token of a `billing:attribution` connection can bill that connection’s customer. A request that authenticates as the service account alone and sets `bill_to: "user_profile"` is refused with `403 user_profile_not_billable`. The customer still displays as **Linked**, so watch for this error in your logs. The service account can still manage user profiles and send the requests that you pay for. You can turn the setting off again.

### OAuth token snippet initialization

The examples in this section share the following setup. It defines:

* the imports, which include the `httpx` package
* your app’s client ID and the client assertion type
* `ConnectionTokens`, which holds a connection’s tokens, their expiry times, and its `on_hold` mark
* `RefreshOnHold`, the error that `refresh_connection()` raises when a refresh token must not be sent again: it might already have been used, or the token endpoint answered `invalid_grant`. `refresh_connection()` raises it on every later call too, until you clear `on_hold` in the stored tokens, for example after a suspension ends. When a refresh succeeded and only your secret store refused the write, its `new_tokens` holds the tokens to store.
* `client_assertion()`, which reads your identity provider’s JWT from the file that `ANTHROPIC_IDENTITY_TOKEN_FILE` names. The JWT’s `aud` claim must be the audience in your app’s client authentication settings.
* `load_tokens()` and `save_tokens()`, which you write for your own secret store

```python
import json
import os
import tempfile
import threading
import time
from collections import defaultdict
from dataclasses import dataclass, field, replace
from pathlib import Path

import httpx

AUTH = "https://auth.claude.com"
# copy from platform.claude.com after you register your OAuth app.
CLIENT_ID = "YOUR_CLIENT_ID"
JWT_BEARER = "urn:ietf:params:oauth:client-assertion-type:jwt-bearer"
REFRESH_MARGIN_SECONDS = 600
# A refresh that times out here loses its new tokens, so allow 10 seconds for the
# answer. A connection that can't be made fails within 2.
REQUEST_TIMEOUT = httpx.Timeout(10, connect=2)
# A second request must start this soon after the first, or not at all. The
# page gives 30 seconds, but keep this under REQUEST_TIMEOUT's read timeout: a
# request that timed out must not be sent again.
SECOND_REQUEST_DEADLINE_SECONDS = 4


@dataclass
class ConnectionTokens:
    refresh_token: str = field(repr=False)
    access_token: str = field(repr=False)
    expires_at: int  # the access token's expiry time, in Unix seconds
    refresh_expires_at: int  # the refresh token's expiry time, in Unix seconds
    # True: the refresh token might have been used. Don't send it again.
    on_hold: bool = False


class RefreshOnHold(Exception):
    """The refresh token might have been used, so a person decides what to do next.

    Don't catch this to try again. If new_tokens is set, the refresh succeeded and
    only the write failed: store those tokens.
    """

    new_tokens: ConnectionTokens | None = None


def client_assertion() -> str:
    """Reads your identity provider's JWT on every call, because its file rotates."""
    return Path(os.environ["ANTHROPIC_IDENTITY_TOKEN_FILE"]).read_text().strip()


def load_tokens(connection_id: str) -> ConnectionTokens:
    """Reads the connection's newest tokens from your secret store."""
    raise NotImplementedError("Read the tokens from your secret store.")


def save_tokens(connection_id: str, tokens: ConnectionTokens) -> None:
    """Writes the connection's newest tokens to your secret store."""
    raise NotImplementedError("Write the tokens to your secret store.")
```

## Managing your connections

### Viewing customers in Console

Besides the OAuth apps page, you can view all your user profiles on the [User profiles](https://platform.claude.com/user-profiles) page in the Console. On that list and on each user profile’s detail page, **Your spend** is your own cost for that user profile’s requests. It is the cost before Anthropic applies any credits. These pages call a connection a link: a user profile with an active connection reads **Linked**, and one whose connection has ended reads **Unlinked**.

Click a user profile for a more detailed view of its usage over the last 7, 28, or 90 days.

### Monitoring each customer’s usage

The Claude Console and the [Usage and Cost Analytics API](https://platform.claude.com/docs/en/manage-claude/usage-cost-analytics-api) both report usage for each user profile. Both count the requests that you pay for and the requests that your customer pays for. Neither shows what the customer paid or the customer’s rates.

In the Console, the [User profiles](https://platform.claude.com/user-profiles) page lists **Requests**, **Tokens**, and **Your spend** for each user profile over the last 28 days. A request that your customer pays for adds to the profile’s **Requests** and **Tokens** and adds nothing to **Your spend**.

Call the API with an [Admin API credential](https://platform.claude.com/docs/en/manage-claude/admin-api#authentication), such as an OAuth access token with the `org:admin` scope or an Admin API key. Don’t use your operator service account (Step 3). Its federation rule grants `workspace:developer` by default, not `org:admin`. The `org:admin` scope covers the whole Admin API, so don’t add it to the operator service account.

To report by user profile through the API, call its [usage endpoint](https://platform.claude.com/docs/en/manage-claude/usage-cost-analytics-api#usage-endpoint) or its [cost endpoint](https://platform.claude.com/docs/en/manage-claude/usage-cost-analytics-api#cost-endpoint). To get one row for each user profile, group by `user_profile_id` alone and leave out `time_bucket_width`. Only a user profile that has usage in the time range that you request gets a row. One more row has a null `user_profile_id`. It holds usage that named no profile and usage that is metered outside requests, such as code execution container time.

On the cost endpoint, a request that your customer pays for adds 0 to `amount` and its list price to `list_amount`. The `amount` field is the same measure as **Your spend**. The API has no field, filter, or `group_by[]` value for who paid. A row with an `amount` of 0 and a `list_amount` above 0 usually means that the customer paid for every request in that row.

Don’t use these figures to stop a customer’s usage at an amount that you choose. Neither the Console nor the API reports in real time. The Console’s figures refresh about once an hour, and a request can take a few hours to appear. For the API’s delay, see [Data freshness](https://platform.claude.com/docs/en/manage-claude/usage-cost-analytics-api#data-freshness). [Spend caps](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections#spend-caps) says what the customer’s own limits do.

### Reading a customer’s link status

To read a customer’s link status from your back end, request their user profile with your app’s client ID in `oauth_app_id`, and send the `user-profiles-search-2026-08-30` beta header. Authenticate as your operator service account (Step 3), with its access token or an API key bound to it. The access token must come from a federation rule with the `workspace:developer` scope, which is the default.

<CodeGroup exclude="shell:CLI, python, typescript, csharp, go, java, php, ruby">
  ```bash cURL
  curl "https://api.anthropic.com/v1/user_profiles/uprof_01HV9Z?oauth_app_id=YOUR_CLIENT_ID" \
    -H "Authorization: Bearer $ACCESS_TOKEN" \
    -H "anthropic-version: 2026-10-21" \
    -H "anthropic-beta: user-profiles-search-2026-08-30"
  ```
</CodeGroup>

In the response, `connection_status` describes the user profile’s link to your app:

| `connection_status.type` | Meaning |
| ----- | ----- |
| `connected` | At least one connection between the user profile and your app is active. |
| `disconnected` | The user profile was linked, and every connection has ended. `last_revoked_at` says when the last one ended. `last_revoked_reason.type` says why, for example `revoked_by_admin` (an administrator of the customer’s organization) or `revoked_by_app_owner` (your organization, including your back end). |
| `not_connected` | The user profile has never been linked to your app. |

Treat a `connection_status` of `null`, or a `type` you don’t recognize, as unknown. Treat a reason you don’t recognize as `other`. `oauth_connections.data` lists the connections themselves.

`connected` doesn’t promise that a request will succeed. It says only that a connection is active. The Claude API still checks each request that sets `bill_to: "user_profile"`. It can refuse the request, for example because the customer’s organization isn’t an [eligible customer](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections#eligible-customers-and-endpoints) or has reached a spend limit. So handle the [expected errors](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections#expected-errors) on every request, even for a user profile that reads `connected`.

A 400 means that the beta header is missing or `oauth_app_id` isn’t in the form of a client ID. A 403 means that the caller isn’t the operator service account of the app in `oauth_app_id`. A 404 means that the user profile doesn’t exist. On a 503, retry with backoff.

### Unlinking a customer

To unlink a customer in the Console, use the list on the [User profiles page](https://platform.claude.com/user-profiles) or the **Unlink** button at the top right of a user profile’s detail page.

To unlink a customer from your back end, send the connection ID that you stored in Step 8 to the [revocation endpoint](https://platform.claude.com/docs/en/manage-claude/oauth-apps/oauth-reference#revocation), with the same client authentication as the code exchange. To name the connection by its user profile instead, send `user_profile_id` in place of `connection_id`.

<CodeGroup exclude="shell:CLI">
  ```bash cURL
  curl https://auth.claude.com/v1/oauth/revoke \
    -H "content-type: application/json" \
    -d @- <<'JSON'
  {
    "connection_id": "ocon_01HV9Z",
    "client_id": "YOUR_CLIENT_ID",
    "client_assertion_type": "urn:ietf:params:oauth:client-assertion-type:jwt-bearer",
    "client_assertion": "YOUR_CLIENT_ASSERTION_JWT"
  }
  JSON
  ```

  ```python Python
  def revoke_connection(connection_id: str) -> list[str]:
      response = httpx.post(
          f"{AUTH}/v1/oauth/revoke",
          json={
              "connection_id": connection_id,
              "client_id": CLIENT_ID,
              "client_assertion_type": JWT_BEARER,
              "client_assertion": client_assertion(),
          },
      )
      response.raise_for_status()
      # IDs of the connections this request ended. The list is empty if the
      # connection had already ended or the ID is unknown.
      return response.json()["revoked_connection_ids"]
  ```

  ```typescript TypeScript
  // No SDK covers auth.claude.com, so this example calls it directly.
  import { readFile } from "node:fs/promises";

  // The connection ID that you stored in Step 8.
  const connectionId = "ocon_01HV9Z";

  // The client assertion: the JWT in the identity token file. Read it for each request, because the file rotates.
  // If your app's client authentication expects a different audience from the one that JWT has, use a second token file.
  const clientAssertion = (
    await readFile(process.env.ANTHROPIC_IDENTITY_TOKEN_FILE!, "utf8")
  ).trim();

  const response = await fetch("https://auth.claude.com/v1/oauth/revoke", {
    method: "POST",
    redirect: "error",
    headers: { "content-type": "application/json" },
    body: JSON.stringify({
      connection_id: connectionId,
      client_id: "YOUR_CLIENT_ID",
      client_assertion_type: "urn:ietf:params:oauth:client-assertion-type:jwt-bearer",
      client_assertion: clientAssertion
    })
  });
  if (!response.ok) {
    throw new Error(`revoke failed: ${response.status}`);
  }

  const { revoked_connection_ids: revokedConnectionIds } = (await response.json()) as {
    revoked_connection_ids: string[];
  };
  console.log(revokedConnectionIds); // IDs of the connections this request ended. The list is empty if the connection had already ended or the ID is unknown.
  ```

  ```csharp C#
  // No SDK covers auth.claude.com, so this example calls it directly.
  using System.Net.Http.Json;
  using System.Text.Json;

  // The connection ID that you stored in Step 8.
  var connectionId = "ocon_01HV9Z";

  // The client assertion: the JWT in the identity token file. Read it for each request, because the file rotates.
  // If your app's client authentication expects a different audience from the one that JWT has, use a second token file.
  var tokenFile = Environment.GetEnvironmentVariable("ANTHROPIC_IDENTITY_TOKEN_FILE")!;
  var clientAssertion = (await File.ReadAllTextAsync(tokenFile)).Trim();

  using var http = new HttpClient();
  using var response = await http.PostAsJsonAsync(
      "https://auth.claude.com/v1/oauth/revoke",
      new Dictionary<string, string>
      {
          ["connection_id"] = connectionId,
          ["client_id"] = "YOUR_CLIENT_ID",
          ["client_assertion_type"] = "urn:ietf:params:oauth:client-assertion-type:jwt-bearer",
          ["client_assertion"] = clientAssertion,
      }
  );
  response.EnsureSuccessStatusCode();

  var result = await response.Content.ReadFromJsonAsync<JsonElement>();
  Console.WriteLine(result.GetProperty("revoked_connection_ids")); // IDs of the connections this request ended. The list is empty if the connection had already ended or the ID is unknown.
  ```

  ```go Go
  // No SDK covers auth.claude.com, so this example calls it directly.

  import (
  	"bytes"
  	"encoding/json"
  	"fmt"
  	"net/http"
  	"os"
  	"strings"
  )

  func main() {
  	// The connection ID that you stored in Step 8.
  	connectionID := "ocon_01HV9Z"

  	// The client assertion: the JWT in the identity token file. Read it for each request, because the file rotates.
  	// If your app's client authentication expects a different audience from the one that JWT has, use a second token file.
  	token, err := os.ReadFile(os.Getenv("ANTHROPIC_IDENTITY_TOKEN_FILE"))
  	if err != nil {
  		panic(err)
  	}

  	body, err := json.Marshal(map[string]string{
  		"connection_id":         connectionID,
  		"client_id":             "YOUR_CLIENT_ID",
  		"client_assertion_type": "urn:ietf:params:oauth:client-assertion-type:jwt-bearer",
  		"client_assertion":      strings.TrimSpace(string(token)),
  	})
  	if err != nil {
  		panic(err)
  	}

  	response, err := http.Post("https://auth.claude.com/v1/oauth/revoke", "application/json", bytes.NewReader(body))
  	if err != nil {
  		panic(err)
  	}
  	defer response.Body.Close()
  	if response.StatusCode < 200 || response.StatusCode > 299 {
  		panic(fmt.Sprintf("revoke failed: %d", response.StatusCode))
  	}

  	var result struct {
  		RevokedConnectionIDs []string `json:"revoked_connection_ids"`
  	}
  	if err := json.NewDecoder(response.Body).Decode(&result); err != nil {
  		panic(err)
  	}
  	fmt.Println(result.RevokedConnectionIDs) // IDs of the connections this request ended. The list is empty if the connection had already ended or the ID is unknown.
  }
  ```

  ```java Java
  // No SDK covers auth.claude.com, so this example calls it directly. The Java SDK brings in Jackson.
  import com.fasterxml.jackson.databind.ObjectMapper;
  import java.net.URI;
  import java.net.http.HttpClient;
  import java.net.http.HttpRequest;
  import java.net.http.HttpResponse;
  import java.nio.file.Files;
  import java.nio.file.Path;

  void main() throws Exception {
      // The connection ID that you stored in Step 8.
      String connectionId = "ocon_01HV9Z";

      // The client assertion: the JWT in the identity token file. Read it for each request, because the file rotates.
      // If your app's client authentication expects a different audience from the one that JWT has, use a second token file.
      String clientAssertion = Files.readString(
          Path.of(System.getenv("ANTHROPIC_IDENTITY_TOKEN_FILE"))).strip();

      var mapper = new ObjectMapper();
      String body = mapper.createObjectNode()
          .put("connection_id", connectionId)
          .put("client_id", "YOUR_CLIENT_ID")
          .put("client_assertion_type", "urn:ietf:params:oauth:client-assertion-type:jwt-bearer")
          .put("client_assertion", clientAssertion)
          .toString();

      var request = HttpRequest.newBuilder(URI.create("https://auth.claude.com/v1/oauth/revoke"))
          .header("content-type", "application/json")
          .POST(HttpRequest.BodyPublishers.ofString(body))
          .build();
      var response = HttpClient.newHttpClient().send(request, HttpResponse.BodyHandlers.ofString());
      if (response.statusCode() / 100 != 2) {
          throw new IllegalStateException("revoke failed: " + response.statusCode());
      }

      // IDs of the connections this request ended. The list is empty if the connection had already ended or the ID is unknown.
      IO.println(mapper.readTree(response.body()).get("revoked_connection_ids"));
  }
  ```

  ```php PHP
  // No SDK covers auth.claude.com, so this example calls it directly.

  // The connection ID that you stored in Step 8.
  $connectionId = 'ocon_01HV9Z';

  // The client assertion: the JWT in the identity token file. Read it for each request, because the file rotates.
  // If your app's client authentication expects a different audience from the one that JWT has, use a second token file.
  $clientAssertion = trim(
      file_get_contents((string) getenv('ANTHROPIC_IDENTITY_TOKEN_FILE'))
          ?: throw new \RuntimeException('the file named by ANTHROPIC_IDENTITY_TOKEN_FILE cannot be read or is empty')
  );

  $body = json_encode([
      'connection_id' => $connectionId,
      'client_id' => 'YOUR_CLIENT_ID',
      'client_assertion_type' => 'urn:ietf:params:oauth:client-assertion-type:jwt-bearer',
      'client_assertion' => $clientAssertion,
  ], JSON_THROW_ON_ERROR);

  $context = stream_context_create(['http' => [
      'method' => 'POST',
      'header' => 'content-type: application/json',
      'content' => $body,
  ]]);
  $response = file_get_contents('https://auth.claude.com/v1/oauth/revoke', context: $context);
  if ($response === false) {
      throw new \RuntimeException('revoke failed');
  }

  /** @var array{revoked_connection_ids: list<string>} $result */
  $result = json_decode($response, associative: true, flags: JSON_THROW_ON_ERROR);
  // IDs of the connections this request ended. The list is empty if the connection had already ended or the ID is unknown.
  echo implode(', ', $result['revoked_connection_ids']), PHP_EOL;
  ```

  ```ruby Ruby
  # No SDK covers auth.claude.com, so this example calls it directly.
  require "json"
  require "net/http"

  # The connection ID that you stored in Step 8.
  connection_id = "ocon_01HV9Z"

  # The client assertion: the JWT in the identity token file. Read it for each request, because the file rotates.
  # If your app's client authentication expects a different audience from the one that JWT has, use a second token file.
  client_assertion = File.read(ENV.fetch("ANTHROPIC_IDENTITY_TOKEN_FILE")).strip

  response = Net::HTTP.post(
    URI("https://auth.claude.com/v1/oauth/revoke"),
    {
      connection_id: connection_id,
      client_id: "YOUR_CLIENT_ID",
      client_assertion_type: "urn:ietf:params:oauth:client-assertion-type:jwt-bearer",
      client_assertion: client_assertion
    }.to_json,
    "content-type" => "application/json"
  )
  response.value # raises on an error

  # IDs of the connections this request ended. The list is empty if the connection had already ended or the ID is unknown.
  puts(JSON.parse(response.body).fetch("revoked_connection_ids"))
  ```
</CodeGroup>

`auth.claude.com` responds with HTTP 200 and `revoked_connection_ids`, the IDs of the connections that this request ended. The list is empty if the connection has already ended, so you can safely repeat a request that sends `connection_id`. It is also empty if the ID is unknown, so an empty list doesn’t prove that the connection existed. See [Revocation](https://platform.claude.com/docs/en/manage-claude/oauth-apps/oauth-reference#revocation) for the other parameters and [Errors from the revocation endpoint](https://platform.claude.com/docs/en/manage-claude/oauth-apps/oauth-reference#errors-from-the-revocation-endpoint).

To unlink a customer through the Claude API instead, send your app’s client ID in `oauth_app_id` to `POST /v1/user_profiles/{id}/unlink`. This ends the same connections as the revocation endpoint with `user_profile_id`. The two requests differ as follows:

|  | Revocation endpoint | Unlink |
| ----- | ----- | ----- |
| **Host** | `auth.claude.com` | `api.anthropic.com` |
| **Authentication** | Your app’s client authentication (Step 2) | Your operator service account (Step 3): its access token, or an API key bound to it. The access token must come from a federation rule with the `workspace:developer` scope, which is the default. |
| **Beta header** | None | `user-profiles-search-2026-08-30` |
| **What it ends** | One connection, or all of your app’s connections on a user profile | All of your app’s connections on a user profile |

<CodeGroup exclude="shell:CLI, python, typescript, csharp, go, java, php, ruby">
  ```bash cURL
  curl https://api.anthropic.com/v1/user_profiles/uprof_01HV9Z/unlink \
    -H "Authorization: Bearer $ACCESS_TOKEN" \
    -H "anthropic-version: 2026-10-21" \
    -H "anthropic-beta: user-profiles-search-2026-08-30" \
    -H "content-type: application/json" \
    -d '{"oauth_app_id": "YOUR_CLIENT_ID"}'
  ```
</CodeGroup>

The response has `revoked_connection_ids`, the IDs of the connections that this request ended. The list is empty if no connection was active. A 400 means that `oauth_app_id` is missing or isn’t in the form of a client ID. A 403 means that the caller isn’t the operator service account of the app in `oauth_app_id`. A 404 means that the user profile doesn’t exist or the beta header is missing.

After the connection ends, the user profile displays as **Unlinked**, and a request that sets `bill_to: "user_profile"` for this customer receives `user_profile_not_billable`. You can still serve the customer at your own cost with `bill_to: "self"`. [After linking](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections#after-connecting) says what your customer sees, and [Emails about linking and unlinking](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections#emails-to-your-customer) says which way of unlinking sends them an email.

If the unlink request returns a 503, it might have ended only some of the connections. Within a day of the first request, repeat it with backoff until you get a 200. After a day, send each `connection_id` that you stored before the first request to the revocation endpoint instead. That ends what’s left, even if `revoked_connection_ids` is empty. A repeat that late can return a 200 with an empty list and skip connections that ended with tokens or billing access left. Also send `connection_id` this way if the customer might have linked again since the first request, because a repeat ends the new connection too.

### Linking a customer to a different Claude organization

To link a customer’s user profile to a different Claude organization, unlink the customer and then link them again.

After you unlink, requests that you bill to this customer are refused. That lasts until a user approves for the other organization and you exchange the code in Step 8. Follow these steps when that user is ready to approve:

1. Skip this step if your customer has already unlinked your app on their [Linked platforms](https://platform.claude.com/linked-platforms) page. Otherwise, unlink the customer, as [Unlinking a customer](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections#disconnecting-a-customer) describes. The user profile then displays as **Unlinked** on your [User profiles](https://platform.claude.com/user-profiles) page.
2. Run [Steps 5 to 8](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections#runtime-step-2) again with the same user profile. For [Step 7](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections#the-administrator-approves), the user needs an account that has the Admin or Billing role in the other organization. Have the user approve for that organization.
3. Store the new connection ID in place of the earlier one. If you use the connection’s tokens, do the same with the new tokens.

Until the customer is unlinked, the approval page lets a user approve only for the organization that is already linked.

A spend cap belongs to one customer organization and your app, so the first organization’s cap doesn’t carry over. [Spend caps](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections#spend-caps) has the rules.

## Expected errors

When a request sets `bill_to: "user_profile"`, Anthropic either bills your customer or refuses the request. It never silently bills you instead. On `/v1/messages` the code in the following list is in `error.details.error_code`. On `/v1/chat/completions` you get the same HTTP status and message in OpenAI format, without the code:

* `403 permission_error, user_profile_not_billable`: Anthropic can’t bill this customer for this request, and the response doesn’t say why. Not retryable, except in the first 10 seconds after a new connection. Before you ask the customer to link again, see [Causes of `user_profile_not_billable`](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections#user-profile-not-billable): linking again fixes only some of them. You can still serve the customer at your own cost by resending with `bill_to: "self"`. In the Anthropic SDK, handle `user_profile_not_billable` by the [error class](https://platform.claude.com/docs/en/api/errors#sdk-error-types) for the 403 status, which is `PermissionDeniedError` (java, php: `PermissionDeniedException`; csharp: `AnthropicForbiddenException`; go: `apierr.StatusCode == http.StatusForbidden`). This also matches other 403 errors, so check the error code too.

* `402 billing_error, linked_organization_billing_unavailable`: Anthropic can’t currently bill the customer’s organization (for example, it’s suspended, or its credit runs out after Claude has started a reply). The response doesn’t say why. A customer that has no credit when the request arrives gets `linked_organization_spend_limit_reached` instead. Not retryable. Tell the customer to check their Claude Platform account. You can still serve them at your own cost by resending with `bill_to: "self"`.

* `402 billing_error, linked_organization_spend_limit_reached`: the customer’s organization has reached a spend limit that it set. The limit is either the [spend cap](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections#spend-caps) that applies to your app or the monthly spend limit for the whole organization. The Claude API sends the same code when the organization has no credit that can pay for the request. The response doesn’t say which. The request was refused before Claude started a reply. Not retryable. You can still serve the customer at your own cost by resending with `bill_to: "self"`. Ask the customer to check these in the Claude Console:

  * **The spend cap for your app:** On the page for your app under [Linked platforms](https://platform.claude.com/linked-platforms), they can set or raise the spend cap. A cap set there replaces any default cap that they set for all linked platforms.
  * **The organization’s Monthly spend limit:** Under [Spend limits](https://platform.claude.com/settings/billing#spend-limits), they can raise it.
  * **The credit balance:** On their [Billing](https://platform.claude.com/settings/billing) page, they can see their credit balance and buy credits. A purchase can take some time to apply, so a request sent soon after it can still get this 402. If so, try again later. Some credits can’t pay for these requests: see [Which credits can pay](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections#which-credits-can-pay).

* `503 overloaded_error`: Anthropic couldn’t confirm right now whether the customer can be billed. Retry with backoff and honor the `retry-after` header. The request wasn’t served or billed.

* `400 invalid_request_error, user_profile_required`: you set `bill_to: "user_profile"` without the `anthropic-user-profile-id` header. Such a request needs the header unless it uses a connection’s access token and the header is optional. To find out whether the header is optional, see the note in [Call Claude with a connection’s access token](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections#call-claude-with-a-connections-access-token).

* `400 invalid_request_error`, with no error code: the `anthropic-user-profile-id` header holds an ID that is malformed or isn’t a user profile of your organization.

* `400 invalid_request_error`, with no error code: the request authenticated with a connection’s access token, and either set `bill_to: "self"` or named a user profile other than the one that the token is limited to. See [Call Claude with a connection’s access token](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections#call-claude-with-a-connections-access-token).

On `/v1/messages` and `/v1/chat/completions`, a connection’s access token can’t send a request that you pay for. To resend a refused request with `bill_to: "self"`, authenticate from your own back end with your operator service account’s own credential. [Call Claude with a connection’s access token](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections#call-claude-with-a-connections-access-token) lists the refusals of the token itself.

A successful response doesn’t say who was billed, so keep your own record of which requests you sent with `bill_to: "user_profile"`.

### Causes of `user_profile_not_billable`

Check these in order:

* **Your request.** The request must authenticate as your OAuth app’s operator service account (Step 3). A [connection’s access token](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections#oauth-tokens-for-each-connection) also authenticates as that service account. A request that authenticates any other way is refused. Examples are a different service account and an API key that isn’t bound to that service account. If the `anthropic-user-profile-id` header names one of your profiles that isn’t linked, the request is refused. If the credential or the header is wrong, correct the request. A new connection doesn’t help.
* **The connection.** The customer hasn’t linked through this app, or the connection has ended: an administrator of their organization or of yours ended it, or your back end did. An ended connection displays as **Unlinked** on your [User profiles](https://platform.claude.com/user-profiles) page. A profile linked only through your test app isn’t linked to your production app. Stop billing that customer until they link. A connection’s access token is limited to that connection, so after the customer links again, use the access token of the new connection. If your app has [turned off operator-only authentication](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections#turn-off-operator-only-authentication), you can bill a customer only with their connection’s access token. Then a customer for whom you hold no working token of a `billing:attribution` connection displays as **Linked**, but must approve again, as [Link a customer again](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections#connect-a-customer-again) describes.
* **The customer’s organization.** It must be an [eligible customer](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections#eligible-customers-and-endpoints). You can’t see the organization’s status from your side. A customer’s new organization can link before it has billing set up. Until then, requests that bill it get this 403, not the out-of-credit 402. Ask the customer to buy credits on their [Billing](https://platform.claude.com/settings/billing) page in the Claude Console, and then send the request again. A purchase can take some time to apply, so if you still get this 403 or that out-of-credit 402 (`linked_organization_spend_limit_reached`), try again later. If that doesn’t help, ask your Anthropic account team.

A new connection usually works at once, but it can take about 10 seconds after the exchange in Step 8. If a request is refused with `user_profile_not_billable` in those 10 seconds, send it again. After that, waiting or retrying doesn’t change the result until the cause is fixed. Log the whole `error.message` and the `request-id` response header of each refused request. If a customer whose connection displays as **Linked** is still refused and your request is correct, send a refused request’s `request-id` to your Anthropic account team, so that Anthropic can look up why it was refused.

## Your customer’s view

### Linking

Your user approves on `auth.claude.com` after your app redirects them in Step 6. [Step 7](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections#the-administrator-approves) lists the approval page’s screens. Each screen shows your app’s name and has a **Cancel** button. What the user does on each screen:

* **Select an organization:** The user picks which of their Claude organizations to link. The page shows this screen only if the user has a choice of organization.
* **How billing works:** The user reads the screen and clicks **Continue**.
* **Set a monthly spend limit:** The user enters a limit for your app in whole US dollars and clicks **Continue**. The amount field starts empty, so the page doesn’t choose a limit for the user. **Continue without a limit** saves no new limit, and a cap or default that the customer saved earlier still applies. The limit that the user enters is the spend cap that [Spend caps](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections#spend-caps) describes. This screen differs while your app is in testing: see [While your app is in testing](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections#while-your-app-is-in-testing).
* **The last screen:** This screen lists what your app will be able to do, including the limit that the user chose. The user clicks **Link and authorize**.

The approval page uses whichever Claude account is signed in to the browser and offers only that account’s Claude organizations. That account might not be the one that your user expects, for example a personal account instead of a work account. Your app can’t choose the account. The `prompt=select_account` and `login_hint` parameters don’t change which account the page uses.

### After linking

Your customers manage their connections on the [Linked platforms](https://platform.claude.com/linked-platforms) page in the Claude Console. They can unlink your app at any time. Anthropic doesn’t notify you when they do: you get no webhook event and no email. To check a customer’s status, see [Reading a customer’s link status](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections#reading-link-status).

After a customer unlinks, requests that you bill to that customer are refused with 403 `user_profile_not_billable` (see [Causes of `user_profile_not_billable`](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections#user-profile-not-billable)). The customer’s user profile displays as **Unlinked** on your [User profiles](https://platform.claude.com/user-profiles) page in the Console. To link again, run [Steps 5 to 8](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections#runtime-step-2) again with the customer’s existing user profile.

### Emails about linking and unlinking

Anthropic’s emails about linking and unlinking go to the members of your customer’s organization who have the Admin or Billing role. Each email links to the customer’s Linked platforms page. Whether Anthropic sends an email depends on the event:

* **When the customer links your app:** Anthropic sends an email when you exchange the code in Step 8. It sends nothing for an approval whose code you never exchange. It also sends nothing when a user approves again while the customer is still linked.
* **When the customer unlinks your app:** Anthropic sends an email. It doesn’t name the person who unlinked your app.
* **When you unlink the customer from your back end:** Anthropic sends an email.
* **When you unlink the customer in the Console:** Anthropic sends no email.

Anthropic doesn’t guarantee that an email is sent or delivered. Tell your customer yourself when you unlink them. Don’t rely on these emails to tell a customer that they are linked.

### Spend caps

Your customer can set a monthly spend cap for your app in US dollars (USD). The approval page calls this cap a monthly spend limit, and the user who links can set it there (see [Linking](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections#connecting)). It is separate from the organization’s **Monthly spend limit**, which applies to the whole organization. You can’t read a customer’s cap or how much of it they have used.

When the customer’s spend through your app reaches the cap, the Claude API refuses the requests that you bill to them with a 402. See [Expected errors](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections#expected-errors). The refusals last until 00:00 UTC on the first day of the next month or until the customer raises or removes the cap. A change to the cap can take about a minute to apply.

After linking, a member of the customer’s organization with the Admin or Billing role manages caps on the [Linked platforms](https://platform.claude.com/linked-platforms) page in the Console:

* **Set or change a cap:** They click your app, then **Set spend cap** or **Edit spend cap**.
* **Set a default:** Under **Default spend cap**, they click **Set default** or **Edit**. Each linked app that has no cap of its own can spend up to the default each month. The apps don’t share it.
* **Remove a cap:** They click your app, **Edit spend cap**, and then **Remove cap**. Your app then uses the default. If there is no default, your app has no cap.

The smallest cap is $0 USD, which refuses every request that you bill to that customer. The Console accepts whole dollars and has no practical maximum. The cap counts token costs and web search fees at list prices before any negotiated discount. The customer’s bill can differ from the amount that the cap counts.

A cap can be higher than the organization’s **Monthly spend limit**, which the customer sets under [Spend limits](https://platform.claude.com/settings/billing#spend-limits). The Claude API refuses the requests that you bill to the customer when either one is reached.

#### While your app is in testing

These limits apply whenever someone links your app or changes its cap while the app is in testing, in review, or not approved:

|  | In testing, in review, or not approved | After the app is live |
| ----- | ----- | ----- |
| A monthly spend limit on the approval page | Required, $50 USD or less | Optional |
| The amount field on the approval page | Starts at $50 USD | Starts empty |
| **Continue without a limit** on the approval page | Not offered | Offered |
| Removing the cap in the Console | Not possible | Possible |
| The largest cap that a customer can set | $50 USD | No practical maximum |

Once your app is live, a cap that a customer saved before then stays in place. The customer can then raise or remove it.

### Supporting your customers

You support your customers for everything about your app, including the Claude usage you bill to them. Anthropic gives your customers the approval page and the Linked platforms page in the Claude Console. On the Linked platforms page, a member with the Admin or Billing role can see what your app has cost the organization this month. They can also set a monthly [spend cap](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections#spend-caps) for your app and unlink it. All other questions about your app should come to you, so tell your customers how to reach you.

## Code snippet initialization

The Python examples on this page share the following setup, which you write once. It defines:

* the imports
* your app’s client ID and redirect URI
* the billing beta header value
* a Claude API client that authenticates as your service account
* `client_assertion`, which returns the client assertion that your back end sends to `auth.claude.com`

```python
# The Python examples assume the following initialization and variables
import secrets
from urllib.parse import urlencode

import anthropic
import httpx
from anthropic.lib.credentials import IdentityTokenFile
from anthropic.types import Message
from anthropic.types.beta import BetaMessage
from authlib.oauth2.rfc7636 import create_s256_code_challenge

AUTH = "https://auth.claude.com"
# copy from platform.claude.com after you register your OAuth app.
CLIENT_ID = "YOUR_CLIENT_ID"
REDIRECT_URI = "https://app.example.com/claude/billing/callback"
JWT_BEARER = "urn:ietf:params:oauth:client-assertion-type:jwt-bearer"
BILLING_BETA = "user-profiles-billing-2026-10-01"

# API client. The SDK exchanges your workload's identity JWT for an access
# token and refreshes it, so you never handle "Bearer <access token>" yourself.
client = anthropic.Anthropic()

# Client assertion for auth.claude.com: the identity JWT itself, read fresh on
# every call because the file rotates. If your app's client authentication
# settings name a different audience than your federation rule, point this at
# a second token file: IdentityTokenFile("/path/to/other/token").
client_assertion = IdentityTokenFile()
```
