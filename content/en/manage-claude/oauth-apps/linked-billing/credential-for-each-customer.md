---
title: Use a separate credential for each customer
url: https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/credential-for-each-customer
description: Call Claude with each customer's own OAuth access token, so that code you don't fully control can bill only that customer.
---

<Warning>
  Claude Platform OAuth is a Beta Service: prerelease software provided under your agreement with Anthropic, such as the [Commercial Terms of Service](https://www.anthropic.com/legal/commercial-terms), and the [Service Specific Terms](https://www.anthropic.com/legal/service-specific-terms). Endpoints, parameters, and behavior can change during the beta. It might not be suitable for production use.
</Warning>

Each customer you link with [Linked billing](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing) comes with their own credential: an OAuth access token that can bill only that customer. Use it when code that you don’t fully control calls Claude for one customer, for example in an agent’s sandbox or a single-tenant deployment. A bug or a leak in that code can then bill only that customer.

If every request that bills a customer comes from your own back end, you don’t need these credentials. [Bill customers as your operator service account](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/link-and-bill-a-customer#bill-a-request), and skip this page.

## Before you begin

* **The customer’s OAuth tokens and connection ID:** The code exchange returned them when you [linked the customer](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/link-and-bill-a-customer#save-the-connection-and-its-tokens). A connection is the record that ties the customer’s Claude organization to one of your [user profiles](https://platform.claude.com/docs/en/manage-claude/user-profiles).
* **A refresh token:** [**Offline access**](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/set-up-your-app#choose-whether-to-get-refresh-tokens) is on for your app, and the customer approved `billing:attribution offline_access`. A customer who approved without `offline_access` gets a refresh token by [approving again](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/link-and-bill-a-customer#if-a-customer-approves-again), which replaces their connection without an unlink.
* **For the refresh samples:** A client assertion: a JWT from your identity provider for your app’s **Expected audience**, set up as your app’s [client authentication](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/set-up-your-app#set-up-client-authentication). The samples read it from the file that the `CLIENT_ASSERTION_FILE` environment variable names or from the `CLIENT_ASSERTION` shell variable.

## Keep the OAuth tokens secret

Store each customer’s access token, refresh token, and their expiry times in a secret store that only the refreshing service can read. Anyone who holds an access token can bill that customer until the token expires. If a token leaks, [unlink the customer](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/manage-customers#unlink-a-customer) first, then link them again. If you lose a refresh token, [link the customer again](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/manage-customers#link-a-customer-again).

## Call Claude with a customer’s access token

Send the customer’s access token in place of your operator service account’s credential:

* **In the Anthropic SDK:** Pass the customer’s access token as the client’s authentication token when you build the client.
* **In the `ant` CLI:** Set `ANTHROPIC_AUTH_TOKEN` to the token for the command.
* **In an HTTP request:** Send it as a bearer token in the `Authorization` header. Don’t send an `x-api-key` header.

<Warning>
  Unset `ANTHROPIC_API_KEY` wherever you use a customer’s access token: some clients send the key instead, and Anthropic can bill you.
</Warning>

Those clients are the `ant` CLI and an SDK client that reads the token from `ANTHROPIC_AUTH_TOKEN`. For the reason and a guard against it, see [If an API key can reach the process](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/credential-for-each-customer#if-an-api-key-can-reach-the-process). If your lookup finds no token for the customer, stop before you build the client. Given a null token, the SDK might fall back to your own credential and bill you.

<CodeGroup>
  ```bash cURL
  curl https://api.anthropic.com/v1/messages \
    -H "authorization: Bearer $CUSTOMER_ACCESS_TOKEN" \
    -H "anthropic-version: 2026-10-21" \
    -H "content-type: application/json" \
    -d '{
      "model": "claude-opus-5-5",
      "max_tokens": 1024,
      "messages": [{"role": "user", "content": "Hello, Claude"}]
    }'
  ```

  ```bash CLI
  ANTHROPIC_AUTH_TOKEN="$CUSTOMER_ACCESS_TOKEN" ant messages create \
    --model claude-opus-5-5 \
    --max-tokens 1024 \
    --message '{role: user, content: "Hello, Claude"}'
  ```

  ```python Python
  client = anthropic.Anthropic(auth_token=customer_access_token)

  message = client.messages.create(
      model="claude-opus-5-5",
      max_tokens=1024,
      messages=[{"role": "user", "content": "Hello, Claude"}],
  )

  for block in message.content:
      if block.type == "text":
          print(block.text)
  ```

  ```typescript TypeScript
  const client = new Anthropic({ authToken: customerAccessToken });

  const message = await client.messages.create({
    model: "claude-opus-5-5",
    max_tokens: 1024,
    messages: [{ role: "user", content: "Hello, Claude" }]
  });

  for (const block of message.content) {
    if (block.type === "text") {
      console.log(block.text);
    }
  }
  ```

  ```csharp C#
  AnthropicClient client = new() { AuthToken = customerAccessToken };

  var message = await client.Messages.Create(
      new MessageCreateParams
      {
          Model = Model.ClaudeOpus5_5,
          MaxTokens = 1024,
          Messages = [new UserMessageParam { Content = "Hello, Claude" }],
      }
  );

  foreach (var block in message.Content)
  {
      if (block.TryPickText(out var textBlock))
      {
          Console.WriteLine(textBlock.Text);
      }
  }
  ```

  ```go Go
  client := anthropic.NewClient(option.WithAuthToken(customerAccessToken))

  message, err := client.Messages.New(context.Background(), anthropic.MessageNewParams{
  	Model:     anthropic.ModelClaudeOpus5_5,
  	MaxTokens: 1024,
  	Messages: []anthropic.MessageParam{
  		anthropic.NewUserMessage(anthropic.NewTextBlock("Hello, Claude")),
  	},
  })
  if err != nil {
  	log.Fatal(err)
  }

  for _, block := range message.Content {
  	if textBlock, ok := block.AsAny().(anthropic.TextBlock); ok {
  		fmt.Println(textBlock.Text)
  	}
  }
  ```

  ```java Java
  AnthropicClient client = AnthropicOkHttpClient.builder()
      .authToken(customerAccessToken)
      .build();
  // ...

  var params = MessageCreateParams.builder()
      .model(Model.CLAUDE_OPUS_5_5)
      .maxTokens(1024)
      .addUserMessage("Hello, Claude")
      .build();
  var message = client.messages().create(params);

  for (var block : message.content()) {
      block.text().ifPresent(textBlock -> IO.println(textBlock.text()));
  }
  ```

  ```php PHP
  $client = new Client(authToken: $customerAccessToken);

  $message = $client->messages->create(
      maxTokens: 1024,
      messages: [['role' => 'user', 'content' => 'Hello, Claude']],
      model: Model::CLAUDE_OPUS_5_5,
  );

  foreach ($message->content as $block) {
      if ($block instanceof \Anthropic\Messages\TextBlock) {
          echo $block->text, PHP_EOL;
      }
  }
  ```

  ```ruby Ruby
  client = Anthropic::Client.new(auth_token: customer_access_token)

  message = client.messages.create(
    model: Anthropic::Model::CLAUDE_OPUS_5_5,
    max_tokens: 1024,
    messages: [{ role: "user", content: "Hello, Claude" }]
  )

  message.content.each do |block|
    puts(block.text) if block.is_a?(Anthropic::Models::TextBlock)
  end
  ```
</CodeGroup>

A customer’s access token works on these endpoints only:

* `/v1/messages` and `/v1/chat/completions`
* `/v1/messages/count_tokens`
* the Models endpoints

On `/v1/messages` and `/v1/chat/completions`, the access token alone bills the customer. You don’t need the `anthropic-user-profile-id` header or [`billing_policy`](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/link-and-bill-a-customer#bill-a-request).

Send every other request and every request that you pay for as your operator service account. That includes requests that use billable code execution, which [can’t bill a customer](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing#if-you-use-code-execution).

Requests with the token run in the workspace that you set as your app’s default. Archiving it revokes every token in it: see [If you move to another workspace](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/set-up-your-app#if-you-move-to-another-workspace). If a request with the token is refused, see [Linked billing errors](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/errors).

## Refresh the OAuth tokens

A customer’s access token lasts at most 1 hour. Before it expires, send the customer’s refresh token to the token endpoint for a new pair of tokens. Each refresh token works once, apart from a single repeat within 30 seconds to recover an answer that you lost.

<Warning>
  A refresh token sent again more than 30 seconds after its first use ends the customer’s connection, and you have to link them again.
</Warning>

To make sure that you never send a used token late:

* Turn off automatic retries for the refresh request in your HTTP client and in any proxy.
* Refresh each customer’s OAuth tokens from one service, one refresh at a time for each customer. If the service has replicas, give them a shared lock. Hold it from reading a customer’s stored tokens until the new ones are stored.
* Store the new refresh token before you use the new access token.

The request is a `refresh_token` grant to `auth.claude.com`. It carries the refresh token and your app’s [client authentication](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/set-up-your-app#set-up-client-authentication): `client_id` and a client assertion. No SDK covers `auth.claude.com`, so the samples call it over HTTP. They show the plain call with no failure handling:

<CodeGroup exclude="shell:CLI">
  ```bash cURL
  curl https://auth.claude.com/v1/oauth/token \
    -H "content-type: application/json" \
    -d @- <<JSON
  {
    "grant_type": "refresh_token",
    "refresh_token": "$CUSTOMER_REFRESH_TOKEN",
    "client_id": "clid_01ABcDeFgHiJkLmNoPqRsTuV",
    "client_assertion_type": "urn:ietf:params:oauth:client-assertion-type:jwt-bearer",
    "client_assertion": "$CLIENT_ASSERTION"
  }
  JSON
  ```

  <CodeGroupItem language="CLI">
    The `ant` CLI has no command for `auth.claude.com`. Send the refresh with cURL or in your application’s language.
  </CodeGroupItem>

  ```python Python
  import os
  from pathlib import Path

  import httpx2  # comes with the Anthropic SDK


  def refresh_tokens(refresh_token: str) -> dict:
      assertion_file = Path(os.environ["CLIENT_ASSERTION_FILE"])

      response = httpx2.post(
          "https://auth.claude.com/v1/oauth/token",
          json={
              "grant_type": "refresh_token",
              "refresh_token": refresh_token,
              "client_id": "clid_01ABcDeFgHiJkLmNoPqRsTuV",
              "client_assertion_type": "urn:ietf:params:oauth:client-assertion-type:jwt-bearer",
              "client_assertion": assertion_file.read_text().strip(),
          },
          timeout=10,
      )
      if not response.is_success:
          raise RuntimeError(f"Refresh failed: {response.status_code} {response.text}")
      return response.json()  # the new access_token and refresh_token
  ```

  ```typescript TypeScript
  import { readFile } from "node:fs/promises";

  async function refreshTokens(refreshToken: string) {
    const jwt = await readFile(process.env.CLIENT_ASSERTION_FILE!, "utf8");

    const response = await fetch("https://auth.claude.com/v1/oauth/token", {
      method: "POST",
      redirect: "error",
      signal: AbortSignal.timeout(10_000),
      headers: { "content-type": "application/json" },
      body: JSON.stringify({
        grant_type: "refresh_token",
        refresh_token: refreshToken,
        client_id: "clid_01ABcDeFgHiJkLmNoPqRsTuV",
        client_assertion_type: "urn:ietf:params:oauth:client-assertion-type:jwt-bearer",
        client_assertion: jwt.trim()
      })
    });
    if (!response.ok) {
      throw new Error(`Refresh failed: ${response.status} ${await response.text()}`);
    }
    return response.json(); // the new access_token and refresh_token
  }
  ```

  ```csharp C#
  using System.Net.Http.Json;
  using System.Text.Json;

  using var http = new HttpClient { Timeout = TimeSpan.FromSeconds(10) };

  async Task<JsonElement> RefreshTokens(string refreshToken)
  {
      var assertionFile = Environment.GetEnvironmentVariable("CLIENT_ASSERTION_FILE")!;
      var jwt = await File.ReadAllTextAsync(assertionFile);

      using var response = await http.PostAsJsonAsync(
          "https://auth.claude.com/v1/oauth/token",
          new Dictionary<string, string>
          {
              ["grant_type"] = "refresh_token",
              ["refresh_token"] = refreshToken,
              ["client_id"] = "clid_01ABcDeFgHiJkLmNoPqRsTuV",
              ["client_assertion_type"] = "urn:ietf:params:oauth:client-assertion-type:jwt-bearer",
              ["client_assertion"] = jwt.Trim(),
          }
      );
      if (!response.IsSuccessStatusCode)
      {
          var details = await response.Content.ReadAsStringAsync();
          throw new HttpRequestException($"Refresh failed: {(int)response.StatusCode} {details}");
      }

      // The new access_token and refresh_token
      return await response.Content.ReadFromJsonAsync<JsonElement>();
  }
  ```

  ```go Go
  import (
  	"bytes"
  	"encoding/json"
  	"fmt"
  	"io"
  	"net/http"
  	"os"
  	"strings"
  	"time"
  )

  var httpClient = &http.Client{Timeout: 10 * time.Second}

  func refreshTokens(refreshToken string) (map[string]any, error) {
  	jwt, err := os.ReadFile(os.Getenv("CLIENT_ASSERTION_FILE"))
  	if err != nil {
  		return nil, err
  	}

  	body, err := json.Marshal(map[string]string{
  		"grant_type":            "refresh_token",
  		"refresh_token":         refreshToken,
  		"client_id":             "clid_01ABcDeFgHiJkLmNoPqRsTuV",
  		"client_assertion_type": "urn:ietf:params:oauth:client-assertion-type:jwt-bearer",
  		"client_assertion":      strings.TrimSpace(string(jwt)),
  	})
  	if err != nil {
  		return nil, err
  	}

  	endpoint := "https://auth.claude.com/v1/oauth/token"
  	response, err := httpClient.Post(endpoint, "application/json", bytes.NewReader(body))
  	if err != nil {
  		return nil, err
  	}
  	defer response.Body.Close()
  	if response.StatusCode/100 != 2 {
  		details, _ := io.ReadAll(response.Body)
  		return nil, fmt.Errorf("refresh failed: %d %s", response.StatusCode, details)
  	}

  	var tokens map[string]any // the new access_token and refresh_token
  	err = json.NewDecoder(response.Body).Decode(&tokens)
  	return tokens, err
  }
  ```

  ```java Java
  import module java.base;
  import module java.net.http;
  import com.fasterxml.jackson.databind.JsonNode;
  import com.fasterxml.jackson.databind.ObjectMapper; // Jackson comes with the Anthropic SDK

  final HttpClient http = HttpClient.newHttpClient();
  final ObjectMapper mapper = new ObjectMapper();

  JsonNode refreshTokens(String refreshToken) throws Exception {
      var jwt = Files.readString(Path.of(System.getenv("CLIENT_ASSERTION_FILE")));

      var body = mapper.createObjectNode()
          .put("grant_type", "refresh_token")
          .put("refresh_token", refreshToken)
          .put("client_id", "clid_01ABcDeFgHiJkLmNoPqRsTuV")
          .put("client_assertion_type", "urn:ietf:params:oauth:client-assertion-type:jwt-bearer")
          .put("client_assertion", jwt.strip());

      var request = HttpRequest.newBuilder(URI.create("https://auth.claude.com/v1/oauth/token"))
          .header("content-type", "application/json")
          .timeout(Duration.ofSeconds(10))
          .POST(HttpRequest.BodyPublishers.ofString(body.toString()))
          .build();
      var response = http.send(request, HttpResponse.BodyHandlers.ofString());
      if (response.statusCode() / 100 != 2) {
          throw new IOException("Refresh failed: " + response.statusCode() + " " + response.body());
      }
      return mapper.readTree(response.body()); // the new access_token and refresh_token
  }
  ```

  ```php PHP
  function refreshTokens(string $refreshToken): mixed
  {
      $jwt = file_get_contents((string) getenv('CLIENT_ASSERTION_FILE'))
          ?: throw new \RuntimeException('Cannot read the client assertion file');

      $body = json_encode([
          'grant_type' => 'refresh_token',
          'refresh_token' => $refreshToken,
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
      $response = file_get_contents('https://auth.claude.com/v1/oauth/token', context: $context);
      $status = http_get_last_response_headers()[0] ?? '';
      if ($response === false || !preg_match('{^HTTP/\S+ 2}', $status)) {
          throw new \RuntimeException("Refresh failed: {$status} {$response}");
      }

      // The new access_token and refresh_token
      return json_decode($response, associative: true, flags: JSON_THROW_ON_ERROR);
  }
  ```

  ```ruby Ruby
  require "json"
  require "net/http"

  def refresh_tokens(refresh_token)
    jwt = File.read(ENV.fetch("CLIENT_ASSERTION_FILE"))

    body = {
      grant_type: "refresh_token",
      refresh_token:,
      client_id: "clid_01ABcDeFgHiJkLmNoPqRsTuV",
      client_assertion_type: "urn:ietf:params:oauth:client-assertion-type:jwt-bearer",
      client_assertion: jwt.strip
    }
    response = Net::HTTP.start("auth.claude.com", 443, use_ssl: true, read_timeout: 10) do |http|
      http.post("/v1/oauth/token", body.to_json, "content-type" => "application/json")
    end
    unless response.is_a?(Net::HTTPSuccess)
      raise "Refresh failed: #{response.code} #{response.body}"
    end

    JSON.parse(response.body) # the new access_token and refresh_token
  end
  ```
</CodeGroup>

The response holds a new access token and a new refresh token. `expires_in` and `refresh_token_expires_in` give their lifetimes in seconds. The new refresh token replaces the one you sent, and the earlier access token stops working within a few minutes.

Before you send a token again after a failed refresh, read [what to do if a refresh fails](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/credential-for-each-customer#if-a-refresh-fails). Some retries end the connection, and some failures mean that you pause every customer’s refreshes. The [full refresh sample](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/credential-for-each-customer#full-refresh-sample) handles those failures.

A refresh token lasts at most 1 year from the code exchange, and a refresh doesn’t extend that. Before it expires, [link the customer again](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/manage-customers#link-a-customer-again).

## Run an agent in a sandbox

Before you use this section, read section 4.1(b) of the [Linked Billing Beta Terms](https://www.anthropic.com/legal/linked-billing-terms). If you have a question about it, ask your Anthropic account team.

When an agent works for one customer in a sandbox, follow these rules:

* Give the sandbox only the access token, never the refresh token. Your back end refreshes the tokens and sends each new access token to the sandbox.
* Decide which customer a sandbox serves from the sandbox’s own identity, such as its pod identity. Never decide from a value that the sandbox sends.
* Send a sandbox only the token of the customer it serves.
* Give the sandbox no mounted identity token and no access to a cloud metadata server.

That last rule keeps the sandbox from getting a JWT that matches your app’s client authentication or one of your [federation rules](https://platform.claude.com/docs/en/manage-claude/workload-identity-federation). With such a JWT, code in the sandbox could authenticate as your app or as one of your service accounts.

The Anthropic SDK, Claude Code, and the [Claude Agent SDK](https://code.claude.com/docs/en/agent-sdk/overview) can read the access token from a credentials file in a configuration profile. For the file’s format, see [Profile configuration file](https://platform.claude.com/docs/en/manage-claude/wif-reference#profile-configuration-file). To set up the sandbox:

<Steps>
  <Step title="Add a profile">
    In the sandbox, create a configuration directory. Inside it, add a profile at `configs/customer.json` whose authentication type is `user_oauth`. Don’t give the profile a `client_id`: with one, the SDK expects a refresh token in the file and refreshes the token itself.

    <File filename="configs/customer.json">
      ```json
      {
        "version": "1.0",
        "authentication": {
          "type": "user_oauth"
        }
      }
      ```
    </File>
  </Step>

  <Step title="Write the access token">
    Before the agent starts, write the access token to `credentials/customer.json` in the same configuration directory, so that `configs` and `credentials` sit side by side. Write it again right after each refresh. `expires_at` is the token’s expiry time in Unix seconds. For code that writes it safely, see [When you write each new access token to a sandbox](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/credential-for-each-customer#when-you-write-each-new-token-to-a-sandbox).

    ```json credentials/customer.json
    {
      "type": "oauth_token",
      "access_token": "sk-ant-oat01-...",
      "expires_at": 1793635200
    }
    ```
  </Step>

  <Step title="Point the client at the profile">
    Set `ANTHROPIC_CONFIG_DIR` to the configuration directory and `ANTHROPIC_PROFILE` to `customer`.
  </Step>

  <Step title="Remove every other credential">
    Unset every other credential in the sandbox, because each can take precedence over the profile. These include:

    * the `ANTHROPIC_API_KEY` and `ANTHROPIC_AUTH_TOKEN` environment variables
    * Claude Code’s `CLAUDE_CODE_OAUTH_TOKEN` environment variable and `apiKeyHelper` setting
  </Step>
</Steps>

The SDK picks up each new token without a restart: see [When you write each new access token to a sandbox](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/credential-for-each-customer#when-you-write-each-new-token-to-a-sandbox).

## Check the result

To confirm that a request billed the customer, see [where a billed request appears](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/link-and-bill-a-customer#check-the-result). To confirm that a token is limited to its customer:

* A request with the token that names another of your user profiles gets `400 invalid_request_error`.
* A few minutes after a refresh, a request with the earlier access token gets `401 authentication_error`.

## Decide whether to turn off operator-only authentication

By default, your operator service account can bill any linked customer without the customer’s access token. It names the customer’s user profile and sets `bill_to: "user_profile"` in [`billing_policy`](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/link-and-bill-a-customer#bill-a-request). This default is called operator-only authentication, and it keeps working after a customer’s access token expires.

Once every customer’s requests use their own access token, you can turn off operator-only authentication. Then, only a customer’s own access token can bill them, so a bug that names the wrong user profile can’t bill the wrong customer.

Every customer’s requests then depend on refreshes. If you lose a customer’s refresh token, you can’t bill them until they [link again](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/manage-customers#link-a-customer-again). Anything that stops refreshes, such as turning off **Offline access** or clearing the [default workspace](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/set-up-your-app#default-workspace), makes every customer’s requests fail as their access tokens expire.

The Claude Console checks only that your app has `billing:attribution`, `offline_access`, and a default workspace. Before you turn off operator-only authentication, check these yourself:

* Your store holds a refresh token for every linked customer.
* Your requests with their access tokens work.

To turn off operator-only authentication:

1. Open the app’s **Client authentication** tab in the Console.
2. Under the operator service account, turn on **Disable operator-only tokenless authentication** and confirm in the dialog box. Its name in the API is `disable_operator_only_auth`.

These rules then apply:

* A request from the service account alone that sets `bill_to: "user_profile"` for a linked customer gets `403 user_profile_not_billable`. The customer still shows as **Linked**, so watch your logs for this error.
* The service account can still manage user profiles and send the requests that you pay for.
* To go back to the default, turn the same setting off.

## Implementation details, rules, and special cases

The rest of this page is the detail behind the steps. It covers failed refreshes, a full refresh sample, and how an API key or a refresh affects a running client. A customer who approved only the deprecated scope has no access token of their own: see [If you still use the deprecated scope](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/set-up-your-app#if-you-still-use-the-deprecated-scope).

### If a refresh fails

A refresh replaces the refresh token that you sent. What happens when the replaced token arrives again depends on when it arrives:

* **Within 30 seconds, the first time:** It returns a new pair of tokens and revokes the pair that you never received. This lets you repeat a refresh whose answer you lost.
* **Within 30 seconds, the first time, if the token that you sent was under 30 seconds old when it was replaced:** It gets `invalid_grant`, and the connection stays.
* **Within 30 seconds, any later time:** It gets `invalid_grant`, and the connection stays.
* **After 30 seconds:** It gets `invalid_grant` and ends the connection. Every token is revoked, the customer shows as **Unlinked**, and nothing can bill them until they link again.

After a failed refresh, what to do depends on whether the refresh token reached `auth.claude.com` and was used:

| What the refresh got | What it means | What to do |
| ----- | ----- | ----- |
| The request couldn’t reach `auth.claude.com`, including a connect timeout | The token wasn’t sent | Send it again later |
| `429` | Nothing was revoked | Wait, then send it again |
| A `503` refusal: a `retry-after` header and `"type": "error"` at the top level of the body | Nothing was revoked | Wait, then send it again |
| Any other `4xx`, except `invalid_grant` | Nothing was revoked | Fix the cause, then send it again |
| Any other `5xx` or a network drop after the request went out | It might have worked | Send it once more, right away |
| No answer in time (a read timeout) | It might still be running | Don’t send it again |
| `invalid_grant` | The token can’t be used now | Stop sending it |

**Wait, then send it again:** Wait at least as long as `retry-after` says. If a `429` has no `retry-after` header, back off before you send it again. A `503` that lacks either mark counts as any other `5xx`.

**Fix the cause, then send it again:**

* `unauthorized_client`: `error_description` usually names the cause, such as a missing default workspace or `offline_access` no longer on your app.
* `invalid_client`: your client assertion failed. Check it against [Client assertion claims](https://platform.claude.com/docs/en/manage-claude/oauth-apps/endpoints-and-parameters#client-assertion-claims).
* `invalid_scope`: the request sent a `scope` parameter, or `billing:attribution` is no longer on your app.
* Any other `4xx`, such as `invalid_request`: correct the request.

If you changed or archived the operator service account, every refresh of a working token gets `unauthorized_client`, and sending again can’t help. See [If you change the service account](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/set-up-your-app#if-you-change-the-service-account).

**Send it once more, right away:** `auth.claude.com` must receive the second request within 30 seconds of replacing the token. You can’t see when that was, so count from when you sent the first request, and leave time for the second to arrive. Then:

* If the second request returns new tokens, store them and use only them.
* If it returns anything else, gets no answer, or can’t go out in time, don’t send the token again.

**Don’t send it again:** After a read timeout or a lost answer that you can’t recover, stop refreshing that customer and [link them again](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/manage-customers#link-a-customer-again).

**Stop sending it:** Stop refreshing that customer. `invalid_grant` usually means one of these, and the response doesn’t say which, so check the first two before you link anyone again:

* The customer’s organization is suspended. Don’t unlink the customer, and keep the refresh token: it works again after the suspension ends. To find out, ask [Anthropic support](https://support.claude.com/en/articles/9015913-how-to-get-support) or your Anthropic account team if you have one.
* Every customer’s refresh got `invalid_grant` at the same time. Look for a cause on your side, such as an [archived workspace](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/set-up-your-app#if-you-move-to-another-workspace).
* The token expired or was already used, the connection ended, or its workspace was archived. [Link the customer again](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/manage-customers#link-a-customer-again).

A lost network connection, a `5xx` response, or a timeout can mean that `auth.claude.com` has a fault. If one made you stop refreshing a customer, keep the fault from costing you more connections:

1. Pause the refreshes of your other customers.
2. Refresh one customer.
3. Resume the rest only after that refresh succeeds or gets a `4xx` response.

### Full refresh sample

This version of the refresh follows [If a refresh fails](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/credential-for-each-customer#if-a-refresh-fails). It adds these safeguards to the plain call:

* It refreshes when the access token has less than 10 minutes left.
* It holds a lock for each customer from reading the stored tokens until the new ones are stored.
* Before the refresh token leaves the process, it marks the stored tokens `on_hold` (typescript, java, php: `onHold`; csharp, go: `OnHold`), so that a crash can’t lead to a second send.
* It waits up to 2 seconds to reach `auth.claude.com` and 10 seconds for an answer.
* It sends a second request only within 4 seconds of the first. That leaves time for the second to arrive within the 30 seconds. It also keeps the second inside the 10-second wait, so that a request that timed out is never sent again.
* If only the write to your secret store fails, it tries the write again and doesn’t refresh again.

The sample leaves three things to you:

* a lock that all your replicas share, because its own lock doesn’t reach your other replicas
* waiting and sending again after a `429` or a `503` refusal, which it reports as an error
* pausing the refreshes of your other customers after a lost refresh, on every replica

Call the refresh function for each customer more often than every 10 minutes, so that it always runs inside that margin.

`refresh_connection()` (typescript, go, java, php: `refreshConnection()`; csharp: `Connections.RefreshConnection()`) fails with `RefreshOnHoldError` (csharp, java, php: `RefreshOnHoldException`) when a refresh token must not be sent again. It also fails on every later call for that customer. The stored record keeps `on_hold` (typescript, java, php: `onHold`; csharp, go: `OnHold`) and `hold_reason` (typescript, java, php: `holdReason`; csharp, go: `HoldReason`), so that you can tell later why the hold was set. When only the write failed, the error’s `new_tokens` (typescript, java, php: `newTokens`; csharp, go: `NewTokens`) holds the tokens to store.

The following setup defines the shared names. You write `load_tokens()` (typescript, go, java, php: `loadTokens()`; csharp: `LoadTokens()`) and `save_tokens()` (typescript, go, java, php: `saveTokens()`; csharp: `SaveTokens()`) for your own secret store.

<CodeGroup exclude="shell:cURL, shell:CLI">
  <CodeGroupItem language="cURL">
    This setup goes with the refresh function that follows, which needs more logic than a single shell command. Write both in your application’s language.
  </CodeGroupItem>

  <CodeGroupItem language="CLI">
    This setup goes with the refresh function that follows, which needs more logic than a single shell command. Write both in your application’s language.
  </CodeGroupItem>

  ```python Python
  import os
  import threading
  import time
  from collections import defaultdict
  from dataclasses import dataclass, field, replace
  from pathlib import Path

  import httpx2  # comes with the Anthropic SDK

  TOKEN_URL = "https://auth.claude.com/v1/oauth/token"
  CLIENT_ID = "clid_01ABcDeFgHiJkLmNoPqRsTuV"
  JWT_BEARER = "urn:ietf:params:oauth:client-assertion-type:jwt-bearer"
  REFRESH_MARGIN_SECONDS = 600
  REQUEST_TIMEOUT = httpx2.Timeout(10, connect=2)
  SECOND_REQUEST_DEADLINE_SECONDS = 4  # keep this under the 10-second read timeout


  @dataclass
  class ConnectionTokens:
      refresh_token: str = field(repr=False)
      access_token: str = field(repr=False)
      expires_at: int  # Unix seconds
      refresh_expires_at: int  # Unix seconds
      on_hold: bool = False  # True: the refresh token might have been used
      hold_reason: str | None = None  # "lost" or "invalid_grant"


  class RefreshOnHoldError(Exception):
      """The refresh token must not be sent again. Don't catch this to try again.

      If new_tokens is set, only the write failed: store those tokens.
      """

      new_tokens: ConnectionTokens | None = None


  def client_assertion() -> str:
      """Reads the JWT that authenticates your app to auth.claude.com."""
      return Path(os.environ["CLIENT_ASSERTION_FILE"]).read_text().strip()


  def load_tokens(connection_id: str) -> ConnectionTokens:
      """Reads the connection's newest tokens from your secret store."""
      raise NotImplementedError("Read the tokens from your secret store.")


  def save_tokens(connection_id: str, tokens: ConnectionTokens) -> None:
      """Writes the connection's newest tokens to your secret store."""
      raise NotImplementedError("Write the tokens to your secret store.")
  ```

  ```typescript TypeScript
  import { readFile } from "node:fs/promises";
  import type { IncomingHttpHeaders } from "node:http";
  import { request } from "node:https";

  const TOKEN_URL = "https://auth.claude.com/v1/oauth/token";
  const CLIENT_ID = "clid_01ABcDeFgHiJkLmNoPqRsTuV";
  const JWT_BEARER = "urn:ietf:params:oauth:client-assertion-type:jwt-bearer";
  const REFRESH_MARGIN_SECONDS = 600;
  const SECOND_REQUEST_DEADLINE_MS = 4_000; // keep this under the 10-second timeout

  interface ConnectionTokens {
    refreshToken: string;
    accessToken: string;
    expiresAt: number; // Unix seconds
    refreshExpiresAt: number; // Unix seconds
    onHold?: boolean; // true: the refresh token might have been used
    holdReason?: "lost" | "invalid_grant";
  }

  /** The refresh token must not be sent again. Don't catch this to try again. */
  class RefreshOnHoldError extends Error {
    override name = "RefreshOnHoldError";
    readonly #newTokens?: ConnectionTokens; // private, so that printing the error doesn't show them

    constructor(message: string, newTokens?: ConnectionTokens) {
      super(message);
      this.#newTokens = newTokens;
    }

    /** If set, only the write failed: store these tokens. */
    get newTokens() {
      return this.#newTokens;
    }
  }

  /** Reads the JWT that authenticates your app to auth.claude.com. */
  async function clientAssertion(): Promise<string> {
    return (await readFile(process.env.CLIENT_ASSERTION_FILE!, "utf8")).trim();
  }

  /** Reads the connection's newest tokens from your secret store. */
  async function loadTokens(connectionId: string): Promise<ConnectionTokens> {
    throw new Error("Read the tokens from your secret store.");
  }

  /** Writes the connection's newest tokens to your secret store. */
  async function saveTokens(connectionId: string, tokens: ConnectionTokens): Promise<void> {
    throw new Error("Write the tokens to your secret store.");
  }
  ```

  ```csharp C#
  using System.Collections.Concurrent;
  using System.Diagnostics;
  using System.Text;
  using System.Text.Json;

  record ConnectionTokens(
      string RefreshToken,
      string AccessToken,
      long ExpiresAt, // Unix seconds
      long RefreshExpiresAt, // Unix seconds
      bool OnHold = false, // true: the refresh token might have been used
      string? HoldReason = null // "lost" or "invalid_grant"
  )
  {
      // Keeps the tokens out of logs.
      public override string ToString() =>
          $"ConnectionTokens {{ ExpiresAt = {ExpiresAt}, OnHold = {OnHold}, HoldReason = {HoldReason} }}";
  }

  /// <summary>The refresh token must not be sent again. Don't catch this to try again.</summary>
  class RefreshOnHoldException(string message) : Exception(message)
  {
      /// <summary>If set, only the write failed: store these tokens.</summary>
      public ConnectionTokens? NewTokens { get; init; }
  }

  static partial class Connections
  {
      const string TokenUrl = "https://auth.claude.com/v1/oauth/token";
      const string ClientId = "clid_01ABcDeFgHiJkLmNoPqRsTuV";
      const string JwtBearer = "urn:ietf:params:oauth:client-assertion-type:jwt-bearer";
      const int RefreshMarginSeconds = 600;
      static readonly TimeSpan SecondRequestDeadline = TimeSpan.FromSeconds(4); // keep this under the 10-second timeout

      /// <summary>Reads the JWT that authenticates your app to auth.claude.com.</summary>
      static string ClientAssertion() =>
          File.ReadAllText(Environment.GetEnvironmentVariable("CLIENT_ASSERTION_FILE")!).Trim();

      /// <summary>Reads the connection's newest tokens from your secret store.</summary>
      static Task<ConnectionTokens> LoadTokens(string connectionId) =>
          throw new NotImplementedException("Read the tokens from your secret store.");

      /// <summary>Writes the connection's newest tokens to your secret store.</summary>
      static Task SaveTokens(string connectionId, ConnectionTokens tokens) =>
          throw new NotImplementedException("Write the tokens to your secret store.");
  }
  ```

  ```go Go
  import (
  	"bytes"
  	"encoding/json"
  	"errors"
  	"fmt"
  	"io"
  	"net"
  	"net/http"
  	"net/http/httptrace"
  	"os"
  	"strings"
  	"sync"
  	"time"
  )

  const (
  	tokenURL              = "https://auth.claude.com/v1/oauth/token"
  	clientID              = "clid_01ABcDeFgHiJkLmNoPqRsTuV"
  	jwtBearer             = "urn:ietf:params:oauth:client-assertion-type:jwt-bearer"
  	refreshMargin         = 10 * time.Minute
  	secondRequestDeadline = 4 * time.Second // keep this under the 10-second timeout
  )

  var httpClient = &http.Client{
  	Timeout: 10 * time.Second,
  	Transport: &http.Transport{
  		Proxy:               http.ProxyFromEnvironment,
  		DialContext:         (&net.Dialer{Timeout: 2 * time.Second}).DialContext,
  		TLSHandshakeTimeout: 2 * time.Second,
  	},
  	CheckRedirect: func(*http.Request, []*http.Request) error { return http.ErrUseLastResponse },
  }

  type ConnectionTokens struct {
  	RefreshToken     string
  	AccessToken      string
  	ExpiresAt        int64  // Unix seconds
  	RefreshExpiresAt int64  // Unix seconds
  	OnHold           bool   // true: the refresh token might have been used
  	HoldReason       string // "lost" or "invalid_grant"
  }

  // String keeps the tokens out of logs.
  func (t ConnectionTokens) String() string {
  	return fmt.Sprintf("ConnectionTokens{ExpiresAt: %d, OnHold: %t, HoldReason: %q}", t.ExpiresAt, t.OnHold, t.HoldReason)
  }

  // RefreshOnHoldError means the refresh token must not be sent again. Don't try again.
  type RefreshOnHoldError struct {
  	Message   string
  	NewTokens *ConnectionTokens // if set, only the write failed: store these tokens
  }

  func (e *RefreshOnHoldError) Error() string { return e.Message }

  // clientAssertion reads the JWT that authenticates your app to auth.claude.com.
  func clientAssertion() (string, error) {
  	jwt, err := os.ReadFile(os.Getenv("CLIENT_ASSERTION_FILE"))
  	return strings.TrimSpace(string(jwt)), err
  }

  // loadTokens reads the connection's newest tokens from your secret store.
  func loadTokens(connectionID string) (ConnectionTokens, error) {
  	return ConnectionTokens{}, errors.New("read the tokens from your secret store")
  }

  // saveTokens writes the connection's newest tokens to your secret store.
  func saveTokens(connectionID string, tokens ConnectionTokens) error {
  	return errors.New("write the tokens to your secret store")
  }
  ```

  ```java Java
  import module java.base;
  import module java.net.http;
  import com.fasterxml.jackson.databind.JsonNode;
  import com.fasterxml.jackson.databind.ObjectMapper; // Jackson comes with the Anthropic SDK

  static final URI TOKEN_URL = URI.create("https://auth.claude.com/v1/oauth/token");
  static final String CLIENT_ID = "clid_01ABcDeFgHiJkLmNoPqRsTuV";
  static final String JWT_BEARER = "urn:ietf:params:oauth:client-assertion-type:jwt-bearer";
  static final long REFRESH_MARGIN_SECONDS = 600;
  static final Duration SECOND_REQUEST_DEADLINE = Duration.ofSeconds(4); // keep this under the 10-second read timeout

  record ConnectionTokens(
      String refreshToken,
      String accessToken,
      long expiresAt, // Unix seconds
      long refreshExpiresAt, // Unix seconds
      boolean onHold, // true: the refresh token might have been used
      String holdReason // "lost" or "invalid_grant"
  ) {
      @Override // keeps the tokens out of logs
      public String toString() {
          return "ConnectionTokens[expiresAt=" + expiresAt + ", onHold=" + onHold + ", holdReason=" + holdReason + "]";
      }

      ConnectionTokens withHold(String reason) {
          return new ConnectionTokens(refreshToken, accessToken, expiresAt, refreshExpiresAt, true, reason);
      }
  }

  record AccessToken(String value, long expiresAt /* Unix seconds */) {
      @Override // keeps the token out of logs
      public String toString() {
          return "AccessToken[expiresAt=" + expiresAt + "]";
      }
  }

  /** The refresh token must not be sent again. Don't catch this to try again. */
  static class RefreshOnHoldException extends RuntimeException {
      /** If set, only the write failed: store these tokens. */
      ConnectionTokens newTokens;

      RefreshOnHoldException(String message) {
          super(message);
      }
  }

  /** Reads the JWT that authenticates your app to auth.claude.com. */
  String clientAssertion() throws IOException {
      return Files.readString(Path.of(System.getenv("CLIENT_ASSERTION_FILE"))).strip();
  }

  /** Reads the connection's newest tokens from your secret store. */
  ConnectionTokens loadTokens(String connectionId) throws IOException {
      throw new UnsupportedOperationException("Read the tokens from your secret store.");
  }

  /** Writes the connection's newest tokens to your secret store. */
  void saveTokens(String connectionId, ConnectionTokens tokens) throws IOException {
      throw new UnsupportedOperationException("Write the tokens to your secret store.");
  }
  ```

  ```php PHP
  const TOKEN_URL = 'https://auth.claude.com/v1/oauth/token';
  const CLIENT_ID = 'clid_01ABcDeFgHiJkLmNoPqRsTuV';
  const JWT_BEARER = 'urn:ietf:params:oauth:client-assertion-type:jwt-bearer';
  const REFRESH_MARGIN_SECONDS = 600;
  const SECOND_REQUEST_DEADLINE_SECONDS = 4; // keep this under the 10-second timeout

  final class ConnectionTokens
  {
      public function __construct(
          public readonly string $refreshToken,
          public readonly string $accessToken,
          public readonly int $expiresAt, // Unix seconds
          public readonly int $refreshExpiresAt, // Unix seconds
          public readonly bool $onHold = false, // true: the refresh token might have been used
          public readonly ?string $holdReason = null, // 'lost' or 'invalid_grant'
      ) {}

      /** Keeps the tokens out of var_dump and print_r. */
      public function __debugInfo(): array
      {
          return ['expiresAt' => $this->expiresAt, 'onHold' => $this->onHold, 'holdReason' => $this->holdReason];
      }

      public function withHold(string $reason): self
      {
          return new self(
              refreshToken: $this->refreshToken,
              accessToken: $this->accessToken,
              expiresAt: $this->expiresAt,
              refreshExpiresAt: $this->refreshExpiresAt,
              onHold: true,
              holdReason: $reason,
          );
      }
  }

  /** The refresh token must not be sent again. Don't catch this to try again. */
  final class RefreshOnHoldException extends \RuntimeException
  {
      /** If set, only the write failed: store these tokens. */
      public ?ConnectionTokens $newTokens = null;
  }

  /** Reads the JWT that authenticates your app to auth.claude.com. */
  function clientAssertion(): string
  {
      $jwt = file_get_contents((string) getenv('CLIENT_ASSERTION_FILE'))
          ?: throw new \RuntimeException('Cannot read the client assertion file');
      return trim($jwt);
  }

  /** Reads the connection's newest tokens from your secret store. */
  function loadTokens(string $connectionId): ConnectionTokens
  {
      throw new \LogicException('Read the tokens from your secret store.');
  }

  /** Writes the connection's newest tokens to your secret store. */
  function saveTokens(string $connectionId, ConnectionTokens $tokens): void
  {
      throw new \LogicException('Write the tokens to your secret store.');
  }
  ```

  ```ruby Ruby
  require "json"
  require "net/http"

  TOKEN_URL = URI("https://auth.claude.com/v1/oauth/token")
  CLIENT_ID = "clid_01ABcDeFgHiJkLmNoPqRsTuV"
  JWT_BEARER = "urn:ietf:params:oauth:client-assertion-type:jwt-bearer"
  REFRESH_MARGIN_SECONDS = 600
  SECOND_REQUEST_DEADLINE_SECONDS = 4 # keep this under the 10-second read timeout

  ConnectionTokens = Data.define(
    :refresh_token,
    :access_token,
    :expires_at, # Unix seconds
    :refresh_expires_at, # Unix seconds
    :on_hold, # true: the refresh token might have been used
    :hold_reason # "lost" or "invalid_grant"
  ) do
    def initialize(on_hold: false, hold_reason: nil, **) = super

    # Keeps the tokens out of logs.
    def inspect = "#<data ConnectionTokens expires_at=#{expires_at} on_hold=#{on_hold} hold_reason=#{hold_reason.inspect}>"
    alias_method :to_s, :inspect
  end

  # The refresh token must not be sent again. Don't rescue this to try again.
  # If new_tokens is set, only the write failed: store those tokens.
  class RefreshOnHoldError < StandardError
    attr_accessor :new_tokens
  end

  # Reads the JWT that authenticates your app to auth.claude.com.
  def client_assertion = File.read(ENV.fetch("CLIENT_ASSERTION_FILE")).strip

  # Reads the connection's newest tokens from your secret store.
  def load_tokens(connection_id)
    raise NotImplementedError, "Read the tokens from your secret store."
  end

  # Writes the connection's newest tokens to your secret store.
  def save_tokens(connection_id, tokens)
    raise NotImplementedError, "Write the tokens to your secret store."
  end
  ```
</CodeGroup>

The following refresh function uses that setup:

<CodeGroup exclude="shell:cURL, shell:CLI">
  <CodeGroupItem language="cURL">
    This refresh needs more logic than a single shell command. Write it in your application’s language.
  </CodeGroupItem>

  <CodeGroupItem language="CLI">
    This refresh needs more logic than a single shell command. Write it in your application’s language.
  </CodeGroupItem>

  ```python Python
  connection_locks: defaultdict[str, threading.Lock] = defaultdict(threading.Lock)


  def error_body(response: httpx2.Response) -> dict:
      try:
          body = response.json()
      except ValueError:
          return {}
      return body if isinstance(body, dict) else {}


  def is_lost(response: httpx2.Response) -> bool:
      """True for a 5xx response that can follow a refresh that took effect."""
      if response.status_code < 500:
          return False
      refused = (
          response.status_code == 503
          and error_body(response).get("type") == "error"
          and "retry-after" in response.headers
      )
      return not refused


  def hold_error(connection_id: str, reason: str) -> RefreshOnHoldError:
      return RefreshOnHoldError(
          f"Connection {connection_id} is on hold. {reason} Don't send its refresh token"
          " again: that can end the customer's link. See"
          ' "If a refresh fails" in the Linked billing docs.'
      )


  def refresh_connection(connection_id: str, *, force: bool = False) -> tuple[str, int]:
      """Returns a current access token and its expiry time in Unix seconds.

      Call this from your schedule. Pass force=True to refresh a token that isn't
      close to its expiry. Raises RefreshOnHoldError when the refresh token must not be
      sent again, and httpx2.HTTPStatusError for a refusal that keeps it.
      """
      # This lock works inside one process only.
      with connection_locks[connection_id]:
          tokens = load_tokens(connection_id)
          if tokens.on_hold:
              raise hold_error(connection_id, f"Reason: {tokens.hold_reason}.")
          if not force and tokens.expires_at - time.time() > REFRESH_MARGIN_SECONDS:
              return tokens.access_token, tokens.expires_at
          request = {
              "grant_type": "refresh_token",
              "refresh_token": tokens.refresh_token,
              "client_id": CLIENT_ID,
              "client_assertion_type": JWT_BEARER,
              "client_assertion": client_assertion(),
          }
          # Hold first, so that the hold stays if the process stops mid-refresh.
          held = replace(tokens, on_hold=True, hold_reason="lost")
          save_tokens(connection_id, held)
          issued_at = int(time.time())
          started = time.monotonic()
          # Don't add retries: a late retry ends the customer's link.
          try:
              response = httpx2.post(TOKEN_URL, json=request, timeout=REQUEST_TIMEOUT)
              lost = is_lost(response)
          except (httpx2.ConnectError, httpx2.ConnectTimeout):
              # The refresh token never left this process, so take the hold off.
              save_tokens(connection_id, tokens)
              raise
          except httpx2.TransportError:
              lost = True
          if lost:
              if time.monotonic() - started > SECOND_REQUEST_DEADLINE_SECONDS:
                  raise hold_error(connection_id, "A refresh got no usable answer.")
              try:
                  response = httpx2.post(TOKEN_URL, json=request, timeout=REQUEST_TIMEOUT)
              except httpx2.TransportError:
                  raise hold_error(
                      connection_id, "Two refreshes got no answer."
                  ) from None
              if response.status_code != 200:
                  raise hold_error(connection_id, "The second refresh failed.")
          if error_body(response).get("error") == "invalid_grant":
              save_tokens(connection_id, replace(held, hold_reason="invalid_grant"))
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
          # Retry only the write. Don't refresh again.
          for attempt in range(5):
              try:
                  save_tokens(connection_id, tokens)
                  return tokens.access_token, tokens.expires_at
              except OSError:  # your secret store's error type
                  if attempt < 4:
                      time.sleep(2**attempt)
          error = hold_error(
              connection_id,
              "The refresh succeeded, but the new tokens could not be saved.",
          )
          error.new_tokens = tokens
          raise error
  ```

  ```typescript TypeScript
  const connectionLocks = new Map<string, Promise<unknown>>();

  function withConnectionLock<T>(connectionId: string, work: () => Promise<T>): Promise<T> {
    const result = (connectionLocks.get(connectionId) ?? Promise.resolve()).then(work, work);
    connectionLocks.set(
      connectionId,
      result.catch(() => {})
    );
    return result;
  }

  class NotSent extends Error {}

  interface TokenResponse {
    status: number;
    headers: IncomingHttpHeaders;
    text: string;
  }

  function post(body: string): Promise<TokenResponse> {
    return new Promise((resolve, reject) => {
      let connected = false;
      const req = request(
        TOKEN_URL,
        {
          method: "POST",
          agent: false, // a new connection for each request
          headers: { "content-type": "application/json" },
          signal: AbortSignal.timeout(10_000)
        },
        (response) => {
          let text = "";
          response.setEncoding("utf8");
          response.on("data", (chunk: string) => (text += chunk));
          response.on("end", () =>
            resolve({ status: response.statusCode!, headers: response.headers, text })
          );
          response.on("error", reject);
        }
      );
      const connectTimer = setTimeout(
        () => req.destroy(new Error("No connection in 2 seconds")),
        2_000
      );
      req.on("socket", (socket) =>
        socket.once("secureConnect", () => {
          connected = true;
          clearTimeout(connectTimer);
        })
      );
      req.on("error", (error) => {
        clearTimeout(connectTimer);
        reject(connected ? error : new NotSent(error.message, { cause: error }));
      });
      req.end(body);
    });
  }

  function errorBody(response: TokenResponse): Record<string, unknown> {
    try {
      const body: unknown = JSON.parse(response.text);
      return typeof body === "object" && body !== null ? (body as Record<string, unknown>) : {};
    } catch {
      return {};
    }
  }

  /** True for a 5xx response that can follow a refresh that took effect. */
  function isLost(response: TokenResponse): boolean {
    if (response.status < 500) {
      return false;
    }
    const refused =
      response.status === 503 &&
      errorBody(response).type === "error" &&
      "retry-after" in response.headers;
    return !refused;
  }

  function holdError(
    connectionId: string,
    reason: string,
    newTokens?: ConnectionTokens
  ): RefreshOnHoldError {
    return new RefreshOnHoldError(
      `Connection ${connectionId} is on hold. ${reason} Don't send its refresh token again: ` +
        'that can end the customer\'s link. See "If a refresh fails" in the Linked billing docs.',
      newTokens
    );
  }

  /**
   * Returns a current access token and its expiry time in Unix seconds.
   *
   * Call this from your schedule. Pass force: true to refresh a token that isn't
   * close to its expiry. Throws RefreshOnHoldError when the refresh token must not be
   * sent again, and an Error for a refusal that keeps it.
   */
  function refreshConnection(connectionId: string, { force = false } = {}) {
    // This lock works inside one process only.
    return withConnectionLock(connectionId, async () => {
      const tokens = await loadTokens(connectionId);
      if (tokens.onHold) {
        throw holdError(connectionId, `Reason: ${tokens.holdReason}.`);
      }
      if (!force && tokens.expiresAt - Date.now() / 1000 > REFRESH_MARGIN_SECONDS) {
        return { accessToken: tokens.accessToken, expiresAt: tokens.expiresAt };
      }
      const body = JSON.stringify({
        grant_type: "refresh_token",
        refresh_token: tokens.refreshToken,
        client_id: CLIENT_ID,
        client_assertion_type: JWT_BEARER,
        client_assertion: await clientAssertion()
      });
      // Hold first, so that the hold stays if the process stops mid-refresh.
      const held: ConnectionTokens = { ...tokens, onHold: true, holdReason: "lost" };
      await saveTokens(connectionId, held);
      const issuedAt = Math.floor(Date.now() / 1000);
      const started = performance.now();
      // Don't add retries: a late retry ends the customer's link.
      let response: TokenResponse | undefined;
      try {
        response = await post(body);
      } catch (error) {
        if (error instanceof NotSent) {
          // The refresh token never left this process, so take the hold off.
          await saveTokens(connectionId, tokens);
          throw error;
        }
      }
      if (!response || isLost(response)) {
        if (performance.now() - started > SECOND_REQUEST_DEADLINE_MS) {
          throw holdError(connectionId, "A refresh got no usable answer.");
        }
        try {
          response = await post(body);
        } catch {
          throw holdError(connectionId, "Two refreshes got no answer.");
        }
        if (response.status !== 200) {
          throw holdError(connectionId, "The second refresh failed.");
        }
      }
      if (errorBody(response).error === "invalid_grant") {
        await saveTokens(connectionId, { ...held, holdReason: "invalid_grant" });
        throw holdError(connectionId, "The refresh returned invalid_grant.");
      }
      if (response.status !== 200) {
        // A refusal that keeps the refresh token, so take the hold off.
        await saveTokens(connectionId, tokens);
        throw new Error(`Refresh failed: ${response.status} ${response.text}`);
      }
      const answer = JSON.parse(response.text);
      const newTokens: ConnectionTokens = {
        refreshToken: answer.refresh_token,
        accessToken: answer.access_token,
        expiresAt: issuedAt + answer.expires_in,
        refreshExpiresAt: issuedAt + answer.refresh_token_expires_in
      };
      // Retry only the write. Don't refresh again.
      for (let attempt = 0; attempt < 5; attempt++) {
        try {
          await saveTokens(connectionId, newTokens);
          return { accessToken: newTokens.accessToken, expiresAt: newTokens.expiresAt };
        } catch {
          // the write failed
          if (attempt < 4) {
            await new Promise((wake) => setTimeout(wake, 2 ** attempt * 1000));
          }
        }
      }
      throw holdError(
        connectionId,
        "The refresh succeeded, but the new tokens could not be saved.",
        newTokens
      );
    });
  }
  ```

  ```csharp C#
  static partial class Connections
  {
      static readonly ConcurrentDictionary<string, SemaphoreSlim> ConnectionLocks = new();

      static readonly HttpClient Http = new(new SocketsHttpHandler
      {
          ConnectTimeout = TimeSpan.FromSeconds(2),
          AllowAutoRedirect = false,
          PooledConnectionLifetime = TimeSpan.Zero, // a new connection for each request
      })
      { Timeout = Timeout.InfiniteTimeSpan }; // Post sets the 10-second timeout

      static async Task<(HttpResponseMessage? Response, string Body, Exception? Error, bool Connected)> Post(
          string body)
      {
          using var request = new HttpRequestMessage(HttpMethod.Post, TokenUrl)
          {
              Content = new StringContent(body, Encoding.UTF8, "application/json"),
          };
          using var timeout = new CancellationTokenSource(TimeSpan.FromSeconds(10));
          try
          {
              var response = await Http.SendAsync(request, timeout.Token);
              return (response, await response.Content.ReadAsStringAsync(timeout.Token), null, true);
          }
          catch (HttpRequestException e) when (e.HttpRequestError is HttpRequestError.ConnectionError
              or HttpRequestError.NameResolutionError or HttpRequestError.SecureConnectionError)
          {
              return (null, "", e, false);
          }
          catch (TaskCanceledException e) when (!timeout.IsCancellationRequested)
          {
              return (null, "", e, false); // the 2-second connect timeout
          }
          catch (Exception e) when (e is HttpRequestException or TaskCanceledException)
          {
              return (null, "", e, true); // a dropped connection or a timeout
          }
      }

      static JsonElement ErrorBody(string body)
      {
          try
          {
              using var document = JsonDocument.Parse(body);
              var parsed = document.RootElement;
              return parsed.ValueKind == JsonValueKind.Object ? parsed.Clone() : default;
          }
          catch (JsonException)
          {
              return default;
          }
      }

      static string? ErrorField(string body, string name) =>
          ErrorBody(body) is { ValueKind: JsonValueKind.Object } error && error.TryGetProperty(name, out var value)
              ? value.ToString()
              : null;

      /// <summary>True for a 5xx response that can follow a refresh that took effect.</summary>
      static bool IsLost(HttpResponseMessage response, string body)
      {
          if ((int)response.StatusCode < 500) return false;
          var refused = (int)response.StatusCode == 503
              && ErrorField(body, "type") == "error"
              && response.Headers.Contains("retry-after");
          return !refused;
      }

      static RefreshOnHoldException HoldError(string connectionId, string reason) => new(
          $"Connection {connectionId} is on hold. {reason} Don't send its refresh token again: " +
          "that can end the customer's link. See \"If a refresh fails\" in the Linked billing docs.");

      /// <summary>
      /// Returns a current access token and its expiry time in Unix seconds.
      /// Call this from your schedule. Pass force: true to refresh a token that isn't
      /// close to its expiry. Throws RefreshOnHoldException when the refresh token must not be
      /// sent again, and HttpRequestException for a refusal that keeps it.
      /// </summary>
      public static async Task<(string AccessToken, long ExpiresAt)> RefreshConnection(
          string connectionId, bool force = false)
      {
          // This lock works inside one process only.
          var connectionLock = ConnectionLocks.GetOrAdd(connectionId, _ => new SemaphoreSlim(1, 1));
          await connectionLock.WaitAsync();
          try
          {
              var tokens = await LoadTokens(connectionId);
              if (tokens.OnHold) throw HoldError(connectionId, $"Reason: {tokens.HoldReason}.");
              if (!force && tokens.ExpiresAt - DateTimeOffset.UtcNow.ToUnixTimeSeconds() > RefreshMarginSeconds)
              {
                  return (tokens.AccessToken, tokens.ExpiresAt);
              }
              var request = JsonSerializer.Serialize(new Dictionary<string, string>
              {
                  ["grant_type"] = "refresh_token",
                  ["refresh_token"] = tokens.RefreshToken,
                  ["client_id"] = ClientId,
                  ["client_assertion_type"] = JwtBearer,
                  ["client_assertion"] = ClientAssertion(),
              });
              // Hold first, so that the hold stays if the process stops mid-refresh.
              var held = tokens with { OnHold = true, HoldReason = "lost" };
              await SaveTokens(connectionId, held);
              var issuedAt = DateTimeOffset.UtcNow.ToUnixTimeSeconds();
              var started = Stopwatch.StartNew();
              // Don't add retries: a late retry ends the customer's link.
              var (response, body, error, connected) = await Post(request);
              if (!connected)
              {
                  // The refresh token never left this process, so take the hold off.
                  await SaveTokens(connectionId, tokens);
                  throw new HttpRequestException("Couldn't connect to auth.claude.com.", error);
              }
              if (response is null || IsLost(response, body))
              {
                  if (started.Elapsed > SecondRequestDeadline)
                      throw HoldError(connectionId, "A refresh got no usable answer.");
                  (response, body, _, _) = await Post(request);
                  if (response is null) throw HoldError(connectionId, "Two refreshes got no answer.");
                  if ((int)response.StatusCode != 200) throw HoldError(connectionId, "The second refresh failed.");
              }
              if (ErrorField(body, "error") == "invalid_grant")
              {
                  await SaveTokens(connectionId, held with { HoldReason = "invalid_grant" });
                  throw HoldError(connectionId, "The refresh returned invalid_grant.");
              }
              if ((int)response.StatusCode != 200)
              {
                  // A refusal that keeps the refresh token, so take the hold off.
                  await SaveTokens(connectionId, tokens);
                  throw new HttpRequestException($"Refresh failed: {(int)response.StatusCode} {body}",
                      null, response.StatusCode);
              }
              using var document = JsonDocument.Parse(body);
              var answer = document.RootElement;
              var newTokens = new ConnectionTokens(
                  RefreshToken: answer.GetProperty("refresh_token").GetString()!,
                  AccessToken: answer.GetProperty("access_token").GetString()!,
                  ExpiresAt: issuedAt + answer.GetProperty("expires_in").GetInt64(),
                  RefreshExpiresAt: issuedAt + answer.GetProperty("refresh_token_expires_in").GetInt64());
              // Retry only the write. Don't refresh again.
              for (var attempt = 0; attempt < 5; attempt++)
              {
                  try
                  {
                      await SaveTokens(connectionId, newTokens);
                      return (newTokens.AccessToken, newTokens.ExpiresAt);
                  }
                  catch (IOException) // your secret store's error type
                  {
                      if (attempt < 4) await Task.Delay(TimeSpan.FromSeconds(1 << attempt));
                  }
              }
              throw new RefreshOnHoldException(HoldError(connectionId,
                  "The refresh succeeded, but the new tokens could not be saved.").Message)
              { NewTokens = newTokens };
          }
          finally
          {
              connectionLock.Release();
          }
      }
  }
  ```

  ```go Go
  var connectionLocks sync.Map

  type tokenResponse struct {
  	status int
  	header http.Header
  	body   []byte
  }

  // post sends the refresh. connected is false if the request never left.
  func post(body []byte) (response *tokenResponse, connected bool, err error) {
  	request, err := http.NewRequest(http.MethodPost, tokenURL, bytes.NewReader(body))
  	if err != nil {
  		return nil, false, err
  	}
  	request.Header.Set("content-type", "application/json")
  	trace := &httptrace.ClientTrace{GotConn: func(httptrace.GotConnInfo) { connected = true }}
  	request = request.WithContext(httptrace.WithClientTrace(request.Context(), trace))
  	answer, err := httpClient.Do(request)
  	if err != nil {
  		return nil, connected, err
  	}
  	defer answer.Body.Close()
  	data, err := io.ReadAll(answer.Body)
  	if err != nil {
  		return nil, true, err
  	}
  	return &tokenResponse{answer.StatusCode, answer.Header, data}, true, nil
  }

  func errorBody(response *tokenResponse) map[string]any {
  	var body map[string]any
  	if json.Unmarshal(response.body, &body) != nil {
  		return map[string]any{}
  	}
  	return body
  }

  // isLost is true for a 5xx response that can follow a refresh that took effect.
  func isLost(response *tokenResponse) bool {
  	if response.status < 500 {
  		return false
  	}
  	refused := response.status == 503 &&
  		errorBody(response)["type"] == "error" &&
  		response.header.Get("retry-after") != ""
  	return !refused
  }

  func holdError(connectionID, reason string) *RefreshOnHoldError {
  	return &RefreshOnHoldError{Message: fmt.Sprintf("connection %s is on hold. %s Don't send its refresh token "+
  		"again: that can end the customer's link. See \"If a refresh fails\" in the Linked billing docs.",
  		connectionID, reason)}
  }

  // refreshConnection returns a current access token and its expiry time in Unix
  // seconds. Call it from your schedule. Pass force=true to refresh a token that
  // isn't close to its expiry. It returns a *RefreshOnHoldError when the refresh
  // token must not be sent again, and another error for a refusal that keeps it.
  func refreshConnection(connectionID string, force bool) (string, int64, error) {
  	// This lock works inside one process only.
  	lock, _ := connectionLocks.LoadOrStore(connectionID, &sync.Mutex{})
  	lock.(*sync.Mutex).Lock()
  	defer lock.(*sync.Mutex).Unlock()

  	tokens, err := loadTokens(connectionID)
  	if err != nil {
  		return "", 0, err
  	}
  	if tokens.OnHold {
  		return "", 0, holdError(connectionID, "Reason: "+tokens.HoldReason+".")
  	}
  	if !force && time.Until(time.Unix(tokens.ExpiresAt, 0)) > refreshMargin {
  		return tokens.AccessToken, tokens.ExpiresAt, nil
  	}
  	assertion, err := clientAssertion()
  	if err != nil {
  		return "", 0, err
  	}
  	body, err := json.Marshal(map[string]string{
  		"grant_type":            "refresh_token",
  		"refresh_token":         tokens.RefreshToken,
  		"client_id":             clientID,
  		"client_assertion_type": jwtBearer,
  		"client_assertion":      assertion,
  	})
  	if err != nil {
  		return "", 0, err
  	}
  	// Hold first, so that the hold stays if the process stops mid-refresh.
  	held := tokens
  	held.OnHold, held.HoldReason = true, "lost"
  	if err := saveTokens(connectionID, held); err != nil {
  		return "", 0, err
  	}
  	issuedAt := time.Now().Unix()
  	started := time.Now()
  	// Don't add retries: a late retry ends the customer's link.
  	response, connected, err := post(body)
  	if err != nil && !connected {
  		// The refresh token never left this process, so take the hold off.
  		if saveErr := saveTokens(connectionID, tokens); saveErr != nil {
  			return "", 0, saveErr
  		}
  		return "", 0, err
  	}
  	if err != nil || isLost(response) {
  		if time.Since(started) > secondRequestDeadline {
  			return "", 0, holdError(connectionID, "A refresh got no usable answer.")
  		}
  		if response, _, err = post(body); err != nil {
  			return "", 0, holdError(connectionID, "Two refreshes got no answer.")
  		}
  		if response.status != 200 {
  			return "", 0, holdError(connectionID, "The second refresh failed.")
  		}
  	}
  	if errorBody(response)["error"] == "invalid_grant" {
  		held.HoldReason = "invalid_grant"
  		if err := saveTokens(connectionID, held); err != nil {
  			return "", 0, err
  		}
  		return "", 0, holdError(connectionID, "The refresh returned invalid_grant.")
  	}
  	if response.status != 200 {
  		// A refusal that keeps the refresh token, so take the hold off.
  		if err := saveTokens(connectionID, tokens); err != nil {
  			return "", 0, err
  		}
  		return "", 0, fmt.Errorf("refresh failed: %d %s", response.status, response.body)
  	}
  	var answer struct {
  		AccessToken           string `json:"access_token"`
  		RefreshToken          string `json:"refresh_token"`
  		ExpiresIn             int64  `json:"expires_in"`
  		RefreshTokenExpiresIn int64  `json:"refresh_token_expires_in"`
  	}
  	if err := json.Unmarshal(response.body, &answer); err != nil {
  		return "", 0, holdError(connectionID, "The refresh answer could not be read.")
  	}
  	tokens = ConnectionTokens{
  		RefreshToken:     answer.RefreshToken,
  		AccessToken:      answer.AccessToken,
  		ExpiresAt:        issuedAt + answer.ExpiresIn,
  		RefreshExpiresAt: issuedAt + answer.RefreshTokenExpiresIn,
  	}
  	// Retry only the write. Don't refresh again.
  	for attempt := range 5 {
  		if err := saveTokens(connectionID, tokens); err == nil {
  			return tokens.AccessToken, tokens.ExpiresAt, nil
  		}
  		if attempt < 4 {
  			time.Sleep(time.Second << attempt)
  		}
  	}
  	hold := holdError(connectionID, "The refresh succeeded, but the new tokens could not be saved.")
  	hold.NewTokens = &tokens
  	return "", 0, hold
  }
  ```

  ```java Java
  final Map<String, ReentrantLock> connectionLocks = new ConcurrentHashMap<>();
  final ObjectMapper mapper = new ObjectMapper();
  final HttpClient http = HttpClient.newBuilder()
      .connectTimeout(Duration.ofSeconds(2))
      .followRedirects(HttpClient.Redirect.NEVER)
      .build();

  HttpResponse<String> post(String body) throws IOException, InterruptedException {
      var request = HttpRequest.newBuilder(TOKEN_URL)
          .header("content-type", "application/json")
          .timeout(Duration.ofSeconds(10))
          .POST(HttpRequest.BodyPublishers.ofString(body))
          .build();
      return http.send(request, HttpResponse.BodyHandlers.ofString());
  }

  JsonNode errorBody(HttpResponse<String> response) {
      try {
          return mapper.readTree(response.body());
      } catch (IOException _) {
          return mapper.createObjectNode();
      }
  }

  /** True for a 5xx response that can follow a refresh that took effect. */
  boolean isLost(HttpResponse<String> response) {
      if (response.statusCode() < 500) {
          return false;
      }
      boolean refused = response.statusCode() == 503
          && errorBody(response).path("type").asText().equals("error")
          && response.headers().firstValue("retry-after").isPresent();
      return !refused;
  }

  RefreshOnHoldException holdError(String connectionId, String reason) {
      return new RefreshOnHoldException("Connection " + connectionId + " is on hold. " + reason
          + " Don't send its refresh token again: that can end the customer's link."
          + " See \"If a refresh fails\" in the Linked billing docs.");
  }

  /**
   * Returns a current access token and its expiry time in Unix seconds.
   * Call this from your schedule. Pass force = true to refresh a token that isn't
   * close to its expiry. Throws RefreshOnHoldException when the refresh token must not be
   * sent again, and IOException for a refusal that keeps it.
   */
  AccessToken refreshConnection(String connectionId, boolean force)
          throws IOException, InterruptedException {
      // This lock works inside one process only.
      var lock = connectionLocks.computeIfAbsent(connectionId, id -> new ReentrantLock());
      lock.lock();
      try {
          var tokens = loadTokens(connectionId);
          if (tokens.onHold()) {
              throw holdError(connectionId, "Reason: " + tokens.holdReason() + ".");
          }
          if (!force && tokens.expiresAt() - Instant.now().getEpochSecond() > REFRESH_MARGIN_SECONDS) {
              return new AccessToken(tokens.accessToken(), tokens.expiresAt());
          }
          var request = mapper.createObjectNode()
              .put("grant_type", "refresh_token")
              .put("refresh_token", tokens.refreshToken())
              .put("client_id", CLIENT_ID)
              .put("client_assertion_type", JWT_BEARER)
              .put("client_assertion", clientAssertion())
              .toString();
          // Hold first, so that the hold stays if the process stops mid-refresh.
          var held = tokens.withHold("lost");
          saveTokens(connectionId, held);
          long issuedAt = Instant.now().getEpochSecond();
          long started = System.nanoTime();
          // Don't add retries: a late retry ends the customer's link.
          HttpResponse<String> response = null;
          try {
              response = post(request);
          } catch (ConnectException | HttpConnectTimeoutException | SSLHandshakeException e) {
              // The refresh token never left this process, so take the hold off.
              saveTokens(connectionId, tokens);
              throw e;
          } catch (IOException _) {
              // The connection dropped, or no answer came in time.
          }
          if (response == null || isLost(response)) {
              if (Duration.ofNanos(System.nanoTime() - started).compareTo(SECOND_REQUEST_DEADLINE) > 0) {
                  throw holdError(connectionId, "A refresh got no usable answer.");
              }
              try {
                  response = post(request);
              } catch (IOException _) {
                  throw holdError(connectionId, "Two refreshes got no answer.");
              }
              if (response.statusCode() != 200) {
                  throw holdError(connectionId, "The second refresh failed.");
              }
          }
          if (errorBody(response).path("error").asText().equals("invalid_grant")) {
              saveTokens(connectionId, held.withHold("invalid_grant"));
              throw holdError(connectionId, "The refresh returned invalid_grant.");
          }
          if (response.statusCode() != 200) {
              // A refusal that keeps the refresh token, so take the hold off.
              saveTokens(connectionId, tokens);
              throw new IOException("Refresh failed: " + response.statusCode() + " " + response.body());
          }
          var answer = mapper.readTree(response.body());
          var newTokens = new ConnectionTokens(
              answer.get("refresh_token").asText(),
              answer.get("access_token").asText(),
              issuedAt + answer.get("expires_in").asLong(),
              issuedAt + answer.get("refresh_token_expires_in").asLong(),
              false,
              null);
          // Retry only the write. Don't refresh again.
          for (int attempt = 0; attempt < 5; attempt++) {
              try {
                  saveTokens(connectionId, newTokens);
                  return new AccessToken(newTokens.accessToken(), newTokens.expiresAt());
              } catch (IOException _) { // your secret store's error type
                  if (attempt < 4) {
                      Thread.sleep(Duration.ofSeconds(1L << attempt));
                  }
              }
          }
          var error = holdError(connectionId, "The refresh succeeded, but the new tokens could not be saved.");
          error.newTokens = newTokens;
          throw error;
      } finally {
          lock.unlock();
      }
  }
  ```

  ```php PHP
  /**
   * Sends the refresh. Returns a string, curl's error, when the request never left this process.
   *
   * @return array{status: int, headers: list<string>, body: string}|false|string false: no answer
   */
  function post(string $body): array|false|string
  {
      $headers = [];
      $curl = curl_init(TOKEN_URL);
      curl_setopt_array($curl, [
          CURLOPT_POST => true,
          CURLOPT_POSTFIELDS => $body,
          CURLOPT_HTTPHEADER => ['content-type: application/json'],
          CURLOPT_RETURNTRANSFER => true,
          CURLOPT_CONNECTTIMEOUT => 2,
          CURLOPT_TIMEOUT => 10,
          CURLOPT_FOLLOWLOCATION => false,
          CURLOPT_FORBID_REUSE => true, // a new connection for each request
          CURLOPT_HEADERFUNCTION => function ($curl, string $line) use (&$headers): int {
              $headers[] = strtolower(trim($line));
              return strlen($line);
          },
      ]);
      $text = curl_exec($curl);
      if (!is_string($text)) {
          // No TLS connection yet means that nothing was sent.
          return curl_getinfo($curl, CURLINFO_APPCONNECT_TIME_T) > 0 ? false : curl_error($curl);
      }
      return ['status' => curl_getinfo($curl, CURLINFO_RESPONSE_CODE), 'headers' => $headers, 'body' => $text];
  }

  /**
   * @param array{status: int, headers: list<string>, body: string} $response
   * @return array<mixed>
   */
  function errorBody(array $response): array
  {
      $body = json_decode($response['body'], associative: true);
      return is_array($body) ? $body : [];
  }

  /**
   * True for a 5xx response that can follow a refresh that took effect.
   *
   * @param array{status: int, headers: list<string>, body: string} $response
   */
  function isLost(array $response): bool
  {
      if ($response['status'] < 500) {
          return false;
      }
      $refused = $response['status'] === 503
          && (errorBody($response)['type'] ?? null) === 'error'
          && preg_grep('/^retry-after:/', $response['headers']);
      return !$refused;
  }

  function holdError(string $connectionId, string $reason): RefreshOnHoldException
  {
      return new RefreshOnHoldException(
          "Connection {$connectionId} is on hold. {$reason} Don't send its refresh token again: "
          . "that can end the customer's link. See \"If a refresh fails\" in the Linked billing docs."
      );
  }

  /**
   * Returns a current access token and its expiry time in Unix seconds.
   *
   * Call this from your schedule. Pass force: true to refresh a token that isn't
   * close to its expiry. Throws RefreshOnHoldException when the refresh token must not be
   * sent again, and \RuntimeException for a refusal that keeps it.
   *
   * @return array{string, int}
   */
  function refreshConnection(string $connectionId, bool $force = false): array
  {
      // This lock works on one machine only.
      $lock = fopen(sys_get_temp_dir() . '/refresh-' . hash('sha256', $connectionId) . '.lock', 'c')
          ?: throw new \RuntimeException('Cannot open the lock file');
      flock($lock, LOCK_EX);
      try {
          $tokens = loadTokens($connectionId);
          if ($tokens->onHold) {
              throw holdError($connectionId, "Reason: {$tokens->holdReason}.");
          }
          if (!$force && $tokens->expiresAt - time() > REFRESH_MARGIN_SECONDS) {
              return [$tokens->accessToken, $tokens->expiresAt];
          }
          $request = json_encode([
              'grant_type' => 'refresh_token',
              'refresh_token' => $tokens->refreshToken,
              'client_id' => CLIENT_ID,
              'client_assertion_type' => JWT_BEARER,
              'client_assertion' => clientAssertion(),
          ], JSON_THROW_ON_ERROR);
          // Hold first, so that the hold stays if the process stops mid-refresh.
          $held = $tokens->withHold('lost');
          saveTokens($connectionId, $held);
          $issuedAt = time();
          $started = hrtime(true);
          // Don't add retries: a late retry ends the customer's link.
          $response = post($request);
          if (is_string($response)) {
              // The refresh token never left this process, so take the hold off.
              saveTokens($connectionId, $tokens);
              throw new \RuntimeException("Could not connect to auth.claude.com: {$response}");
          }
          if ($response === false || isLost($response)) {
              if ((hrtime(true) - $started) / 1e9 > SECOND_REQUEST_DEADLINE_SECONDS) {
                  throw holdError($connectionId, 'A refresh got no usable answer.');
              }
              $response = post($request);
              if (!is_array($response)) {
                  throw holdError($connectionId, 'Two refreshes got no answer.');
              }
              if ($response['status'] !== 200) {
                  throw holdError($connectionId, 'The second refresh failed.');
              }
          }
          if ((errorBody($response)['error'] ?? null) === 'invalid_grant') {
              saveTokens($connectionId, $held->withHold('invalid_grant'));
              throw holdError($connectionId, 'The refresh returned invalid_grant.');
          }
          if ($response['status'] !== 200) {
              // A refusal that keeps the refresh token, so take the hold off.
              saveTokens($connectionId, $tokens);
              throw new \RuntimeException("Refresh failed: {$response['status']} {$response['body']}");
          }
          /**
           * @var array{
           *     access_token: string,
           *     refresh_token: string,
           *     expires_in: int,
           *     refresh_token_expires_in: int,
           * } $answer
           */
          $answer = json_decode($response['body'], associative: true, flags: JSON_THROW_ON_ERROR);
          $newTokens = new ConnectionTokens(
              refreshToken: $answer['refresh_token'],
              accessToken: $answer['access_token'],
              expiresAt: $issuedAt + $answer['expires_in'],
              refreshExpiresAt: $issuedAt + $answer['refresh_token_expires_in'],
          );
          // Retry only the write. Don't refresh again.
          for ($attempt = 0; $attempt < 5; $attempt++) {
              try {
                  saveTokens($connectionId, $newTokens);
                  return [$newTokens->accessToken, $newTokens->expiresAt];
              } catch (\RuntimeException) { // your secret store's error type
                  if ($attempt < 4) {
                      sleep(2 ** $attempt);
                  }
              }
          }
          $error = holdError($connectionId, 'The refresh succeeded, but the new tokens could not be saved.');
          $error->newTokens = $newTokens;
          throw $error;
      } finally {
          flock($lock, LOCK_UN);
          fclose($lock);
      }
  }
  ```

  ```ruby Ruby
  CONNECTION_LOCKS = Hash.new { |locks, connection_id| locks[connection_id] = Mutex.new }
  LOCKS_GUARD = Mutex.new

  # Raises before the request leaves if it can't connect.
  def open_connection
    Net::HTTP.start(TOKEN_URL.host, TOKEN_URL.port, use_ssl: true,
      open_timeout: 2, read_timeout: 10, write_timeout: 10, max_retries: 0)
  end

  def post(http, body)
    http.post(TOKEN_URL.path, body, "content-type" => "application/json")
  ensure
    http.finish
  end

  def error_body(response)
    body = JSON.parse(response.body.to_s)
    body.is_a?(Hash) ? body : {}
  rescue JSON::ParserError
    {}
  end

  # True for a 5xx response that can follow a refresh that took effect.
  def lost?(response)
    return false if response.code.to_i < 500

    refused = response.code == "503" &&
      error_body(response)["type"] == "error" &&
      response.key?("retry-after")
    !refused
  end

  def hold_error(connection_id, reason)
    RefreshOnHoldError.new(
      "Connection #{connection_id} is on hold. #{reason} Don't send its refresh token again: " \
      "that can end the customer's link. See \"If a refresh fails\" in the Linked billing docs."
    )
  end

  # Returns a current access token and its expiry time in Unix seconds.
  #
  # Call this from your schedule. Pass force: true to refresh a token that isn't
  # close to its expiry. Raises RefreshOnHoldError when the refresh token must not be
  # sent again, and RuntimeError for a refusal that keeps it.
  def refresh_connection(connection_id, force: false)
    # This lock works inside one process only.
    LOCKS_GUARD.synchronize { CONNECTION_LOCKS[connection_id] }.synchronize do
      tokens = load_tokens(connection_id)
      raise hold_error(connection_id, "Reason: #{tokens.hold_reason}.") if tokens.on_hold
      if !force && tokens.expires_at - Time.now.to_i > REFRESH_MARGIN_SECONDS
        return tokens.access_token, tokens.expires_at
      end

      request = {
        grant_type: "refresh_token",
        refresh_token: tokens.refresh_token,
        client_id: CLIENT_ID,
        client_assertion_type: JWT_BEARER,
        client_assertion:
      }.to_json
      # Hold first, so that the hold stays if the process stops mid-refresh.
      held = tokens.with(on_hold: true, hold_reason: "lost")
      save_tokens(connection_id, held)
      issued_at = Time.now.to_i
      started = Process.clock_gettime(Process::CLOCK_MONOTONIC)
      # Don't add retries: a late retry ends the customer's link.
      begin
        http = open_connection
      rescue
        # The refresh token never left this process, so take the hold off.
        save_tokens(connection_id, tokens)
        raise
      end
      begin
        response = post(http, request)
        lost = lost?(response)
      rescue
        lost = true
      end
      if lost
        if Process.clock_gettime(Process::CLOCK_MONOTONIC) - started > SECOND_REQUEST_DEADLINE_SECONDS
          raise hold_error(connection_id, "A refresh got no usable answer.")
        end
        begin
          response = post(open_connection, request)
        rescue
          raise hold_error(connection_id, "Two refreshes got no answer.")
        end
        raise hold_error(connection_id, "The second refresh failed.") unless response.code == "200"
      end
      if error_body(response)["error"] == "invalid_grant"
        save_tokens(connection_id, held.with(hold_reason: "invalid_grant"))
        raise hold_error(connection_id, "The refresh returned invalid_grant.")
      end
      unless response.code == "200"
        # A refusal that keeps the refresh token, so take the hold off.
        save_tokens(connection_id, tokens)
        raise "Refresh failed: #{response.code} #{response.body}"
      end
      body = JSON.parse(response.body)
      tokens = ConnectionTokens.new(
        refresh_token: body.fetch("refresh_token"),
        access_token: body.fetch("access_token"),
        expires_at: issued_at + body.fetch("expires_in"),
        refresh_expires_at: issued_at + body.fetch("refresh_token_expires_in")
      )
      # Retry only the write. Don't refresh again.
      5.times do |attempt|
        save_tokens(connection_id, tokens)
        return tokens.access_token, tokens.expires_at
      rescue IOError, SystemCallError # your secret store's error types
        sleep(2**attempt) if attempt < 4
      end
      error = hold_error(connection_id, "The refresh succeeded, but the new tokens could not be saved.")
      error.new_tokens = tokens
      raise error
    end
  end
  ```
</CodeGroup>

### If an API key can reach the process

This section is only for a process where `ANTHROPIC_API_KEY` might be set beside a customer’s access token. These clients send the key in place of the token:

* the `ant` CLI
* an SDK client that reads the token from `ANTHROPIC_AUTH_TOKEN`

An SDK client given the token when you build it sends only the token. Other clients can send both. The key still wins, except on the Models endpoints, where the request can be refused. When the key goes out, the Claude API authenticates the request with it, so the request isn’t limited to that customer.

As a guard in such a process, send each request with the `anthropic-user-profile-id` header, `billing_policy` with `bill_to: "user_profile"`, and the `user-profiles-billing-2026-10-01` beta header. Then, a request that goes out with the key has one of these outcomes:

* **With the header and `bill_to: "user_profile"`:** It fails, or it bills the customer the header names.
* **With the header alone, or with neither:** Anthropic bills it to you.

### When you write each new access token to a sandbox

Your back end sends each new token to code in the sandbox, over a channel that you build. That code runs as the agent’s user and writes the token into a `credentials` directory with mode `0700`. It writes a new file with mode `0600` and renames it over the old one, so that the agent never reads half a file. This function does that:

<CodeGroup exclude="shell:cURL, shell:CLI">
  <CodeGroupItem language="cURL">
    Write the file with your application’s code, running in the sandbox as the agent’s user.
  </CodeGroupItem>

  <CodeGroupItem language="CLI">
    Write the file with your application’s code, running in the sandbox as the agent’s user.
  </CodeGroupItem>

  ```python Python
  import json
  import os
  import tempfile
  from pathlib import Path


  def write_credentials_file(
      config_dir: Path, profile: str, token: str, expires_at: int
  ) -> None:
      """Run this in the sandbox, as the agent's user."""
      credentials_dir = config_dir / "credentials"
      credentials_dir.mkdir(mode=0o700, parents=True, exist_ok=True)
      body = {"type": "oauth_token", "access_token": token, "expires_at": expires_at}
      handle, temporary_path = tempfile.mkstemp(dir=credentials_dir)  # mode 0600
      with os.fdopen(handle, "w") as temporary_file:
          json.dump(body, temporary_file)
      os.replace(temporary_path, credentials_dir / f"{profile}.json")
  ```

  ```typescript TypeScript
  import { mkdir, rename, writeFile } from "node:fs/promises";
  import { join } from "node:path";

  /** Run this in the sandbox, as the agent's user. */
  async function writeCredentialsFile(
    configDir: string,
    profile: string,
    token: string,
    expiresAt: number
  ) {
    const credentialsDir = join(configDir, "credentials");
    await mkdir(credentialsDir, { mode: 0o700, recursive: true });
    const body = { type: "oauth_token", access_token: token, expires_at: expiresAt };
    const temporaryPath = join(credentialsDir, `.${crypto.randomUUID()}.tmp`);
    await writeFile(temporaryPath, JSON.stringify(body), { mode: 0o600, flag: "wx" });
    await rename(temporaryPath, join(credentialsDir, `${profile}.json`));
  }
  ```

  ```csharp C#
  using System.Text.Json;

  /// <summary>Run this in the sandbox, as the agent's user.</summary>
  static void WriteCredentialsFile(string configDir, string profile, string token, long expiresAt)
  {
      var credentialsDir = Path.Combine(configDir, "credentials");
      Directory.CreateDirectory(credentialsDir, UnixFileMode.UserRead | UnixFileMode.UserWrite | UnixFileMode.UserExecute);
      var body = new Dictionary<string, object>
      {
          ["type"] = "oauth_token",
          ["access_token"] = token,
          ["expires_at"] = expiresAt,
      };
      var temporaryPath = Path.Combine(credentialsDir, $".{Guid.NewGuid()}.tmp");
      using (var temporaryFile = new FileStream(temporaryPath, new FileStreamOptions
      {
          Mode = FileMode.CreateNew,
          Access = FileAccess.Write,
          UnixCreateMode = UnixFileMode.UserRead | UnixFileMode.UserWrite,
      }))
      {
          JsonSerializer.Serialize(temporaryFile, body);
      }
      File.Move(temporaryPath, Path.Combine(credentialsDir, $"{profile}.json"), overwrite: true);
  }
  ```

  ```go Go
  import (
  	"encoding/json"
  	"os"
  	"path/filepath"
  )

  // writeCredentialsFile runs in the sandbox, as the agent's user.
  func writeCredentialsFile(configDir, profile, token string, expiresAt int64) error {
  	credentialsDir := filepath.Join(configDir, "credentials")
  	if err := os.MkdirAll(credentialsDir, 0o700); err != nil {
  		return err
  	}
  	body, err := json.Marshal(map[string]any{"type": "oauth_token", "access_token": token, "expires_at": expiresAt})
  	if err != nil {
  		return err
  	}
  	temporaryFile, err := os.CreateTemp(credentialsDir, ".tmp-*") // mode 0600
  	if err != nil {
  		return err
  	}
  	defer os.Remove(temporaryFile.Name()) // does nothing once the rename is done
  	if _, err := temporaryFile.Write(body); err != nil {
  		temporaryFile.Close()
  		return err
  	}
  	if err := temporaryFile.Close(); err != nil {
  		return err
  	}
  	return os.Rename(temporaryFile.Name(), filepath.Join(credentialsDir, profile+".json"))
  }
  ```

  ```java Java
  import module java.base;
  import com.fasterxml.jackson.databind.ObjectMapper; // Jackson comes with the Anthropic SDK

  /** Run this in the sandbox, as the agent's user. */
  void writeCredentialsFile(Path configDir, String profile, String token, long expiresAt) throws IOException {
      var credentialsDir = Files.createDirectories(configDir.resolve("credentials"),
          PosixFilePermissions.asFileAttribute(PosixFilePermissions.fromString("rwx------")));
      var body = Map.of("type", "oauth_token", "access_token", token, "expires_at", expiresAt);
      var temporaryPath = Files.createTempFile(credentialsDir, ".", ".tmp"); // mode 0600
      Files.writeString(temporaryPath, new ObjectMapper().writeValueAsString(body));
      Files.move(temporaryPath, credentialsDir.resolve(profile + ".json"),
          StandardCopyOption.ATOMIC_MOVE, StandardCopyOption.REPLACE_EXISTING);
  }
  ```

  ```php PHP
  /** Run this in the sandbox, as the agent's user. */
  function writeCredentialsFile(string $configDir, string $profile, string $token, int $expiresAt): void
  {
      $credentialsDir = "{$configDir}/credentials";
      if (!is_dir($credentialsDir) && !mkdir($credentialsDir, 0700, recursive: true)) {
          throw new \RuntimeException("Cannot create {$credentialsDir}");
      }
      $credentials = ['type' => 'oauth_token', 'access_token' => $token, 'expires_at' => $expiresAt];
      $body = json_encode($credentials, JSON_THROW_ON_ERROR);
      $temporaryPath = tempnam($credentialsDir, '.tmp'); // mode 0600
      if ($temporaryPath === false || dirname($temporaryPath) !== realpath($credentialsDir)) {
          throw new \RuntimeException("Cannot create a file in {$credentialsDir}"); // tempnam can fall back to /tmp
      }
      $finalPath = "{$credentialsDir}/{$profile}.json";
      if (file_put_contents($temporaryPath, $body) === false || !rename($temporaryPath, $finalPath)) {
          throw new \RuntimeException("Cannot write the credentials for {$profile}");
      }
  }
  ```

  ```ruby Ruby
  require "fileutils"
  require "json"
  require "tempfile"

  # Run this in the sandbox, as the agent's user.
  def write_credentials_file(config_dir, profile, token, expires_at)
    credentials_dir = File.join(config_dir, "credentials")
    FileUtils.mkdir_p(credentials_dir, mode: 0o700)
    body = { type: "oauth_token", access_token: token, expires_at: }
    temporary_file = Tempfile.create(".tmp", credentials_dir) # mode 0600
    temporary_file.write(body.to_json)
    temporary_file.close
    File.rename(temporary_file.path, File.join(credentials_dir, "#{profile}.json"))
  end
  ```
</CodeGroup>

Within a few minutes of a refresh, a request with the earlier token gets a `401`. The client can then read the file again and send the request with the new token. With the TypeScript or C# SDK on its own, that one request fails instead. Send it once more: the next request uses the new token. The SDK also reads the file again in the last 2 minutes before `expires_at`, or in the last 30 seconds in Java.

### For agents

* When you refresh, don’t send a `scope` parameter.
* For every refresh, read the client assertion again from its file.
* When you store new tokens, count their expiry times from when you sent the refresh, using `expires_in` and `refresh_token_expires_in`.
* When a suspension ends, clear `on_hold` (typescript, java, php: `onHold`; csharp, go: `OnHold`) only if its `hold_reason` (typescript, java, php: `holdReason`; csharp, go: `HoldReason`) is `invalid_grant`.
* When you write a sandbox’s credentials file, write a token that has more than 30 seconds left before its `expires_at`.

## Next steps

<CardGroup cols={2}>
  <Card title="Test and publish your app" icon="rocket" href="https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/test-and-publish">
    Add test users, publish your app, and change or delete it
  </Card>

  <Card title="What your customers see" icon="browser" href="https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/what-your-customers-see">
    The approval page, spend caps, and emails that your customers see, so that you can support them
  </Card>
</CardGroup>
