---
title: Manage linked customers
url: https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/manage-customers
description: "Check and manage linked customers: see their usage, unlink them or link them again, and move them to another organization or off their API key."
---

<Warning>
  Claude Platform OAuth is a Beta Service: prerelease software provided under your agreement with Anthropic, such as the [Commercial Terms of Service](https://www.anthropic.com/legal/commercial-terms), and the [Service Specific Terms](https://www.anthropic.com/legal/service-specific-terms). Endpoints, parameters, and behavior can change during the beta. It might not be suitable for production use.
</Warning>

After customers link, you manage them from the Claude Console and from your back end. Each customer has a [user profile](https://platform.claude.com/docs/en/manage-claude/user-profiles) in your organization, which you created to link them. Linking creates a connection, the record that ties the customer’s Claude organization to that profile.

## Before you begin

* **The customer’s IDs:** the user profile ID (`uprof_…`) and the `connection_id` (`ocon_…`) that you stored when you [linked the customer](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/link-and-bill-a-customer#save-the-connection-and-its-tokens).
* **To check a customer’s status or use the unlink endpoint:** your app’s [operator service account](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/set-up-your-app#service-account) with an access token from [Workload Identity Federation](https://platform.claude.com/docs/en/manage-claude/workload-identity-federation). The token must come from a federation rule with the `workspace:developer` scope, which is the default.
* **To unlink through `auth.claude.com`:** your app’s [client authentication](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/set-up-your-app#set-up-client-authentication). The samples read a client assertion from the file that the `CLIENT_ASSERTION_FILE` environment variable names, or you paste one in place of `YOUR_CLIENT_ASSERTION_JWT`. It’s a JWT for your app’s **Expected audience**.
* **To read usage from your back end:** an [Admin API credential](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/manage-customers#if-you-read-usage-from-your-back-end).

## View customers and usage

Open the [User profiles](https://platform.claude.com/user-profiles) page in the Console. Your app’s **Overview** tab also lists its linked customers. For each user profile, the User profiles page lists **Requests**, **Tokens**, and **Your spend** over the last 28 days. Click a profile to see its usage over the last 7, 28, or 90 days.

* A profile with an active connection reads **Linked**, one whose connection has ended reads **Unlinked**, and one never linked reads **Not linked**. Only members with the Admin role see these statuses and **Unlink**.
* **Your spend** is your own cost for the profile’s requests, before Anthropic applies any credits.
* A request that the customer pays for adds to **Requests** and **Tokens** and adds nothing to **Your spend**.
* The page doesn’t display what the customer paid or the customer’s rates.

The figures refresh about once an hour, and a request can take a few hours to appear.

Don’t use these figures to stop a customer’s usage at an amount that you choose. The customer’s own [spend caps](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/what-your-customers-see#spend-caps) do that.

## Check whether a customer is linked

From your back end, call `GET /v1/user_profiles/{id}` with the customer’s user profile ID. Send your app’s client ID in `oauth_app_id`, and send the `user-profiles-search-2026-08-30` beta header. Authenticate as your operator service account. The SDK doesn’t send `oauth_app_id`, so the sample calls the endpoint over HTTP.

In this sample, `ANTHROPIC_AUTH_TOKEN` holds the service account’s access token, which you [get from your workload](https://platform.claude.com/docs/en/manage-claude/workload-identity-federation#authenticate-from-your-workload). Set the variable only where you run cURL: the SDK and CLI would use it in place of federation.

<CodeGroup exclude="shell:CLI, python, typescript, csharp, go, java, php, ruby">
  ```bash cURL
  curl "https://api.anthropic.com/v1/user_profiles/uprof_01HV9Z?oauth_app_id=clid_01ABcDeFgHiJkLmNoPqRsTuV" \
    -H "authorization: Bearer $ANTHROPIC_AUTH_TOKEN" \
    -H "anthropic-version: 2026-10-21" \
    -H "anthropic-beta: user-profiles-search-2026-08-30"
  ```
</CodeGroup>

In the response, `connection_status.type` describes the profile’s connection to your app:

| `connection_status.type` | In the Console | Meaning |
| ----- | ----- | ----- |
| `connected` | **Linked** | A connection to your app is active |
| `disconnected` | **Unlinked** | The profile was linked, and its connections have ended |
| `not_connected` | **Not linked** | The profile has never been linked to your app |

A `connected` status doesn’t promise that a request bills the customer. On every request that bills a customer, handle both `403` codes and the two `402` [billing errors](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/errors#while-billing).

For a `disconnected` profile, these fields say more. The reasons listed are examples:

| Field | What it says |
| ----- | ----- |
| `last_revoked_at` | When the last connection ended |
| `last_revoked_reason.type` | Why. `revoked_by_admin`: a member of the customer’s organization with the Admin or Billing role unlinked your app. `revoked_by_app_owner`: your organization or your back end unlinked the customer. |

For any status, `oauth_connections.data` lists the profile’s connections to your app, up to 100, with `truncated` set when the list might be incomplete.

## Unlink a customer

<Warning>
  Unlinking stops new requests that bill the customer until you exchange the code of a new approval.
</Warning>

In the Console, you can unlink a customer in two places:

* **Your app’s Overview tab:** Under **Linked customers**, **Unlink** in the customer’s row menu ends their connection to that app only.
* **The User profiles page:** **Unlink** is in a profile’s row menu and at the top right of its page. It ends the profile’s connections to all of your apps, test apps included.

From your back end, send a revocation request to `auth.claude.com` with your app’s client authentication and one of these:

* **`connection_id`:** Ends that one connection. Use it when you have it.
* **`user_profile_id`:** Sent in place of `connection_id`, it ends every connection of your app on that profile. That includes one the customer made after you stored your IDs.

<CodeGroup exclude="shell:CLI">
  ```bash cURL
  curl https://auth.claude.com/v1/oauth/revoke \
    -H "content-type: application/json" \
    -d @- <<'JSON'
  {
    "connection_id": "ocon_01HV9Z",
    "client_id": "clid_01ABcDeFgHiJkLmNoPqRsTuV",
    "client_assertion_type": "urn:ietf:params:oauth:client-assertion-type:jwt-bearer",
    "client_assertion": "YOUR_CLIENT_ASSERTION_JWT"
  }
  JSON
  ```

  <CodeGroupItem language="CLI">
    The `ant` CLI has no command for `auth.claude.com`. Send the request with cURL or in your application’s language.
  </CodeGroupItem>

  ```python Python
  import os
  from pathlib import Path

  import httpx2  # comes with the Anthropic SDK

  # The connection ID that you stored when you linked the customer
  connection_id = "ocon_01HV9Z"

  assertion_file = Path(os.environ["CLIENT_ASSERTION_FILE"])

  response = httpx2.post(
      "https://auth.claude.com/v1/oauth/revoke",
      json={
          "connection_id": connection_id,
          "client_id": "clid_01ABcDeFgHiJkLmNoPqRsTuV",
          "client_assertion_type": "urn:ietf:params:oauth:client-assertion-type:jwt-bearer",
          "client_assertion": assertion_file.read_text().strip(),
      },
      timeout=10,
  )
  if not response.is_success:
      raise RuntimeError(f"Revoke failed: {response.status_code} {response.text}")

  print(response.json()["revoked_connection_ids"])
  ```

  ```typescript TypeScript
  import { readFile } from "node:fs/promises";

  // The connection ID that you stored when you linked the customer
  const connectionId = "ocon_01HV9Z";

  const jwt = await readFile(process.env.CLIENT_ASSERTION_FILE!, "utf8");

  const response = await fetch("https://auth.claude.com/v1/oauth/revoke", {
    method: "POST",
    redirect: "error",
    signal: AbortSignal.timeout(10_000),
    headers: { "content-type": "application/json" },
    body: JSON.stringify({
      connection_id: connectionId,
      client_id: "clid_01ABcDeFgHiJkLmNoPqRsTuV",
      client_assertion_type: "urn:ietf:params:oauth:client-assertion-type:jwt-bearer",
      client_assertion: jwt.trim()
    })
  });
  if (!response.ok) {
    throw new Error(`Revoke failed: ${response.status} ${await response.text()}`);
  }

  const result = (await response.json()) as { revoked_connection_ids: string[] };
  console.log(result.revoked_connection_ids);
  ```

  ```csharp C#
  using System.Net.Http.Json;
  using System.Text.Json;

  // The connection ID that you stored when you linked the customer
  var connectionId = "ocon_01HV9Z";

  var assertionFile = Environment.GetEnvironmentVariable("CLIENT_ASSERTION_FILE")!;
  var jwt = await File.ReadAllTextAsync(assertionFile);

  using var http = new HttpClient { Timeout = TimeSpan.FromSeconds(10) };
  using var response = await http.PostAsJsonAsync(
      "https://auth.claude.com/v1/oauth/revoke",
      new Dictionary<string, string>
      {
          ["connection_id"] = connectionId,
          ["client_id"] = "clid_01ABcDeFgHiJkLmNoPqRsTuV",
          ["client_assertion_type"] = "urn:ietf:params:oauth:client-assertion-type:jwt-bearer",
          ["client_assertion"] = jwt.Trim(),
      }
  );
  if (!response.IsSuccessStatusCode)
  {
      var details = await response.Content.ReadAsStringAsync();
      throw new HttpRequestException($"Revoke failed: {(int)response.StatusCode} {details}");
  }

  var result = await response.Content.ReadFromJsonAsync<JsonElement>();
  Console.WriteLine(result.GetProperty("revoked_connection_ids"));
  ```

  ```go Go
  import (
  	"bytes"
  	"encoding/json"
  	"fmt"
  	"io"
  	"log"
  	"net/http"
  	"os"
  	"strings"
  	"time"
  )

  func main() {
  	// The connection ID that you stored when you linked the customer
  	connectionID := "ocon_01HV9Z"

  	jwt, err := os.ReadFile(os.Getenv("CLIENT_ASSERTION_FILE"))
  	if err != nil {
  		log.Fatal(err)
  	}

  	body, err := json.Marshal(map[string]string{
  		"connection_id":         connectionID,
  		"client_id":             "clid_01ABcDeFgHiJkLmNoPqRsTuV",
  		"client_assertion_type": "urn:ietf:params:oauth:client-assertion-type:jwt-bearer",
  		"client_assertion":      strings.TrimSpace(string(jwt)),
  	})
  	if err != nil {
  		log.Fatal(err)
  	}

  	httpClient := &http.Client{Timeout: 10 * time.Second}
  	endpoint := "https://auth.claude.com/v1/oauth/revoke"
  	response, err := httpClient.Post(endpoint, "application/json", bytes.NewReader(body))
  	if err != nil {
  		log.Fatal(err)
  	}
  	defer response.Body.Close()
  	if response.StatusCode/100 != 2 {
  		details, _ := io.ReadAll(response.Body)
  		log.Fatalf("revoke failed: %d %s", response.StatusCode, details)
  	}

  	var result struct {
  		RevokedConnectionIDs []string `json:"revoked_connection_ids"`
  	}
  	if err := json.NewDecoder(response.Body).Decode(&result); err != nil {
  		log.Fatal(err)
  	}
  	fmt.Println(result.RevokedConnectionIDs)
  }
  ```

  ```java Java
  import module java.base;
  import module java.net.http;
  import com.fasterxml.jackson.databind.ObjectMapper; // Jackson comes with the Anthropic SDK

  void main() throws Exception {
      // The connection ID that you stored when you linked the customer
      var connectionId = "ocon_01HV9Z";

      var jwt = Files.readString(Path.of(System.getenv("CLIENT_ASSERTION_FILE")));

      var mapper = new ObjectMapper();
      var body = mapper.createObjectNode()
          .put("connection_id", connectionId)
          .put("client_id", "clid_01ABcDeFgHiJkLmNoPqRsTuV")
          .put("client_assertion_type", "urn:ietf:params:oauth:client-assertion-type:jwt-bearer")
          .put("client_assertion", jwt.strip());

      var request = HttpRequest.newBuilder(URI.create("https://auth.claude.com/v1/oauth/revoke"))
          .header("content-type", "application/json")
          .timeout(Duration.ofSeconds(10))
          .POST(HttpRequest.BodyPublishers.ofString(body.toString()))
          .build();
      var response = HttpClient.newHttpClient().send(request, HttpResponse.BodyHandlers.ofString());
      if (response.statusCode() / 100 != 2) {
          throw new IOException("Revoke failed: " + response.statusCode() + " " + response.body());
      }

      IO.println(mapper.readTree(response.body()).get("revoked_connection_ids"));
  }
  ```

  ```php PHP
  // The connection ID that you stored when you linked the customer
  $connectionId = 'ocon_01HV9Z';

  $jwt = file_get_contents((string) getenv('CLIENT_ASSERTION_FILE'))
      ?: throw new \RuntimeException('Cannot read the client assertion file');

  $body = json_encode([
      'connection_id' => $connectionId,
      'client_id' => 'clid_01ABcDeFgHiJkLmNoPqRsTuV',
      'client_assertion_type' => 'urn:ietf:params:oauth:client-assertion-type:jwt-bearer',
      'client_assertion' => trim($jwt),
  ], JSON_THROW_ON_ERROR);

  $context = stream_context_create(['http' => [
      'method' => 'POST',
      'header' => 'content-type: application/json',
      'content' => $body,
      'timeout' => 10,
      'ignore_errors' => true, // keep the body of an error response
  ]]);
  $response = file_get_contents('https://auth.claude.com/v1/oauth/revoke', context: $context);
  $status = http_get_last_response_headers()[0] ?? '';
  if ($response === false || !preg_match('{^HTTP/\S+ 2}', $status)) {
      throw new \RuntimeException("Revoke failed: {$status} {$response}");
  }

  /** @var array{revoked_connection_ids: list<string>} $result */
  $result = json_decode($response, associative: true, flags: JSON_THROW_ON_ERROR);
  echo implode(', ', $result['revoked_connection_ids']), PHP_EOL;
  ```

  ```ruby Ruby
  require "json"
  require "net/http"

  # The connection ID that you stored when you linked the customer
  connection_id = "ocon_01HV9Z"

  jwt = File.read(ENV.fetch("CLIENT_ASSERTION_FILE"))

  body = {
    connection_id:,
    client_id: "clid_01ABcDeFgHiJkLmNoPqRsTuV",
    client_assertion_type: "urn:ietf:params:oauth:client-assertion-type:jwt-bearer",
    client_assertion: jwt.strip
  }
  response = Net::HTTP.start("auth.claude.com", 443, use_ssl: true, read_timeout: 10) do |http|
    http.post("/v1/oauth/revoke", body.to_json, "content-type" => "application/json")
  end
  raise "Revoke failed: #{response.code} #{response.body}" unless response.is_a?(Net::HTTPSuccess)

  puts(JSON.parse(response.body).fetch("revoked_connection_ids"))
  ```
</CodeGroup>

The response’s `revoked_connection_ids` lists the connections that the request ended. An empty list means that it found none to end: usually the connection had already ended, or the ID was unknown. This means that you can safely repeat a request that sends `connection_id`. To confirm, [check whether the customer is linked](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/manage-customers#check-a-links-status). To unlink through the Claude API instead, see [If you unlink through the Claude API](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/manage-customers#if-you-unlink-through-the-claude-api).

After you unlink, these things happen:

* The profile shows as **Unlinked**. Unlinking doesn’t delete it.
* The connection’s OAuth tokens stop working, so you can delete them from your secret store.
* New requests that bill the customer typically stop within about 10 seconds, whoever unlinked. Requests that are already running finish and are billed to the customer.
* A request that bills the customer gets [`403 user_profile_billing_not_authorized`](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/errors#user-profile-billing-not-authorized). One sent with the customer’s access token can get a [`401 authentication_error`](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/errors#authentication-error) instead.
* Anthropic emails the customer’s Admin and Billing members when you unlink from your back end by either route. It doesn’t email them when you unlink in the Console. See [which emails your customers get](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/what-your-customers-see#emails).

You can still serve the customer at your own cost with [`bill_to: "self"`](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/link-and-bill-a-customer#you-pay). Tell the customer yourself whenever you unlink them, because Anthropic doesn’t guarantee that an email is sent or delivered.

## Link a customer again

If the customer’s connection has ended (**Unlinked**), [send them to approve](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/link-and-bill-a-customer#send-them-to-approve) again with their existing user profile. There’s nothing to unlink, and a new profile would split their usage history.

While the connection is active, what you do depends on whether it has a refresh token, which it has if the customer approved `offline_access`:

* **The connection has no refresh token:** Don’t unlink. Send them to approve again with the same `scope`, which [gives you a new access token](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/link-and-bill-a-customer#if-a-customer-approves-again). If an access token leaked, [unlink the customer](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/manage-customers#unlink-a-customer) first, because approving again doesn’t revoke it.
* **The connection has a refresh token, even one that you lost:** Unlink the customer, then have them approve again, as the following steps describe.

When a customer’s connection has a refresh token, link the customer again in these cases:

* A refresh returned `invalid_grant`, or a failed refresh made you stop refreshing the customer. First, [rule out a suspension and a cause on your side](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/credential-for-each-customer#if-a-refresh-fails).
* You lost a refresh token, a refresh token leaked, or you lost the code exchange’s response.
* The refresh token is close to its 1-year expiry.
* You changed the operator service account, and you use this customer’s OAuth tokens.

Billing through the connection stops from the unlink until your new code exchange succeeds. First, agree on a time with a person who has the Admin or Billing role in the customer’s organization. Then:

1. If the profile shows as **Linked**, [unlink the customer](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/manage-customers#unlink-a-customer).
2. [Send the customer to approve](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/link-and-bill-a-customer#send-them-to-approve) again with their existing user profile and the same scope, which includes `offline_access`.
3. Store the new `connection_id` and the new OAuth tokens in place of the earlier ones. The profile then shows as **Linked** again.

## Move a customer to another organization

To bill a customer through a different Claude organization of theirs, unlink them and link them again. Until you unlink, the approval page offers only the organization that’s already linked. From the unlink until you exchange the code of an approval for the other organization, requests that bill the customer are refused.

Start when a person with the Admin or Billing role in the other organization is ready to approve. Then:

1. Unless the customer has already unlinked your app on their [Linked platforms](https://platform.claude.com/linked-platforms) page, [unlink the customer](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/manage-customers#unlink-a-customer).
2. [Send them to approve](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/link-and-bill-a-customer#send-them-to-approve) again with the same user profile and scope, and have the person approve for the other organization.
3. Store the new `connection_id` in place of the earlier one, and store the new OAuth tokens if you use them. The profile then shows as **Linked** again, through the other organization.

The first organization’s spend cap for your app doesn’t carry over. For the cap that applies to the other organization, see [Spend caps in What your customers see](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/what-your-customers-see#spend-caps).

## Move a customer from their API key to Linked billing

Before you move a customer off their own API key, weigh two costs:

* **You pay for what can’t bill a customer:** [Message Batches](https://platform.claude.com/docs/en/build-with-claude/batch-processing), Claude Managed Agents, and billable code execution.
* **The requests run in your organization:** Your rate limits and data terms apply. The customer’s zero data retention, business associate agreement (BAA), customer-managed encryption keys (CMEK), and IP allowlist don’t. See [Whose terms and limits apply](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing#whose-data-terms-and-rate-limits-apply).

To move a customer:

1. [Link the customer](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/link-and-bill-a-customer), and store their `connection_id`.
2. Instead of their key, bill their requests as your operator service account, and set `bill_to: "user_profile"` in [`billing_policy`](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/link-and-bill-a-customer#bill-a-request).
3. Delete the stored API key, and tell the customer that you did.

Their requests then add to their profile’s **Requests** on your [User profiles](https://platform.claude.com/user-profiles) page. They add nothing to **Your spend**.

## Decide how often to check whether customers are linked

A customer can unlink your app at any time on their [Linked platforms](https://platform.claude.com/linked-platforms) page, and Anthropic doesn’t tell you. Decide when your product finds out:

* **When a request is refused:** Find [the cause of the refusal](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/errors#while-billing), and [check whether the customer is still linked](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/manage-customers#check-a-links-status).
* **Before you bill:** Check when the customer starts something in your product that bills them.
* **On a schedule:** Check every customer, and keep your product’s view of who’s linked up to date.

Checking more often shows an unlink sooner, at the cost of more requests.

## Implementation details, rules, and special cases

The rest of this page covers the API details behind these tasks. It also covers special cases, such as a failed unlink.

### If you unlink through the Claude API

You can unlink through the Claude API’s unlink endpoint instead: send your app’s client ID in `oauth_app_id` to `POST /v1/user_profiles/{id}/unlink`. It ends the same connections as a revocation request with `user_profile_id`.

| Detail | Revocation request | Unlink endpoint |
| ----- | ----- | ----- |
| Host | `auth.claude.com` | `api.anthropic.com` |
| Authentication | Your app’s client authentication | Your operator service account |
| Beta header | None | `user-profiles-search-2026-08-30` |
| What it ends | One connection or every connection of your app on a profile | Every connection of your app on a profile |

In this sample, `ANTHROPIC_AUTH_TOKEN` holds your operator service account’s access token, as in [Check whether a customer is linked](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/manage-customers#check-a-links-status).

<CodeGroup exclude="shell:CLI, python, typescript, csharp, go, java, php, ruby">
  ```bash cURL
  curl https://api.anthropic.com/v1/user_profiles/uprof_01HV9Z/unlink \
    -H "authorization: Bearer $ANTHROPIC_AUTH_TOKEN" \
    -H "anthropic-version: 2026-10-21" \
    -H "anthropic-beta: user-profiles-search-2026-08-30" \
    -H "content-type: application/json" \
    -d '{"oauth_app_id": "clid_01ABcDeFgHiJkLmNoPqRsTuV"}'
  ```
</CodeGroup>

The response has `revoked_connection_ids`, which is empty if no connection was active.

### If the unlink endpoint returns a 503

A `503` from the unlink endpoint means that it might have ended only some of the connections. Send a revocation request for each `connection_id` that you had stored before the request that failed. That works at any time. It ends what’s left and doesn’t touch a connection the customer made since.

Repeating the unlink with backoff also works within a day of the first request, but it ends a connection the customer made since, too. After a day, a repeat can return a `200` with an empty list. That later repeat also doesn’t revoke what’s left of the connections that the failed request ended, so they can keep OAuth tokens or billing access.

### If a status check or the unlink endpoint refuses a request

| Status | Status check | Unlink endpoint |
| ----- | ----- | ----- |
| `400` | `oauth_app_id` isn’t in the form of a client ID, or the beta header is missing | `oauth_app_id` is missing or isn’t in the form of a client ID |
| `401` | The credential is missing or invalid, or its federation rule doesn’t grant `workspace:developer` | The same |
| `403` | The caller isn’t the operator service account of the app in `oauth_app_id`, or it uses a token of that account that’s limited to one session | The same |
| `404` | The user profile doesn’t exist | The user profile doesn’t exist, or the beta header is missing |
| `503` | Retry with backoff | See [If the unlink endpoint returns a 503](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/manage-customers#if-an-unlink-returns-a-503) |

The revocation request’s own errors are in [Errors from the revocation endpoint](https://platform.claude.com/docs/en/manage-claude/oauth-apps/endpoints-and-parameters#errors-from-the-revocation-endpoint).

### If you read usage from your back end

The [Usage and Cost Analytics API](https://platform.claude.com/docs/en/manage-claude/usage-cost-analytics-api) reports usage for each user profile. Like the Console, it counts both the requests that you pay for and those that your customer pays for.

Call it with an Admin API credential, such as an OAuth access token with the `org:admin` scope or an [Admin API key](https://platform.claude.com/docs/en/manage-claude/admin-api#authentication). Don’t use your operator service account: its federation rule grants `workspace:developer` by default, not `org:admin`. Don’t add `org:admin` to it, because that scope covers the whole Admin API.

To get one row for each user profile, call the [usage endpoint](https://platform.claude.com/docs/en/manage-claude/usage-cost-analytics-api#usage-endpoint) or the [cost endpoint](https://platform.claude.com/docs/en/manage-claude/usage-cost-analytics-api#cost-endpoint). Group by `user_profile_id` alone, and leave out `time_bucket_width`. Only a profile with usage in the time range gets a row. A row with a null `user_profile_id` holds usage that named no profile, and usage that’s metered outside requests, such as code execution container time.

On the cost endpoint, you can tell who paid from two fields:

| Field | A request you pay for | A request your customer pays for |
| ----- | ----- | ----- |
| `amount` | Its cost, the same measure as **Your spend** | 0 |
| `list_amount` | Its list price | Its list price |

The API has no field or filter for who paid. A row whose `amount` is 0 and whose `list_amount` is above 0 usually means that the customer paid for all of it. For how late the data can be, see [Data freshness](https://platform.claude.com/docs/en/manage-claude/usage-cost-analytics-api#data-freshness).

### For agents

* Treat a `connection_status` of `null` or a `type` that you don’t recognize as unknown.
* Treat a `last_revoked_reason.type` that you don’t recognize as `other`.

## Next steps

<CardGroup cols={1}>
  <Card title="Test and publish your app" icon="rocket" href="https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/test-and-publish">
    Add test users, publish your app, and change or delete it
  </Card>
</CardGroup>
