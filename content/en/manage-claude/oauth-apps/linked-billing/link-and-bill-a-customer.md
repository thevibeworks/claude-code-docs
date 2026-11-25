---
title: Link and bill a customer
url: https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/link-and-bill-a-customer
description: Send a customer to approve your OAuth app, save the connection, and bill Claude API requests to their Claude organization.
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

This page shows how to build Linked billing into your product. A customer approves your app once, which creates a connection between their Claude organization and one of your user profiles. After that, your back end bills the customer by sending requests as your own [operator service account](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/set-up-your-app#service-account), naming the customer’s [user profile](https://platform.claude.com/docs/en/manage-claude/user-profiles). You try the flow first on a test customer, a second organization of your own. For how the feature works and whether it fits your product, see [Linked billing](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing).

## Before you begin

You need these:

* **An app set up for Linked billing:** It needs client authentication, an operator service account, and a default workspace: see [Set up your app for Linked billing](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/set-up-your-app).
* **A test customer:** A second Claude organization of yours, because the organization that owns your app can’t link to it. It must pay Anthropic directly, through invoiced billing or [credit that can pay for these requests](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing#which-credits-can-pay).
* **A test user:** A person with the Admin or Billing role in the test customer’s organization, who approves for it. Until your app is live, only people on its **Test users** list can link it. [Add this person’s Claude email address](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/test-and-publish#add-test-users) to that list.

### Sample setup

The samples read these values:

| Samples | What they need | Where it comes from |
| ----- | ----- | ----- |
| SDK and CLI | Your operator service account’s federation settings, in environment variables, including the federation JWT’s file in `ANTHROPIC_IDENTITY_TOKEN_FILE` | [Construct the SDK client](https://platform.claude.com/docs/en/manage-claude/workload-identity-federation#construct-the-sdk-client) |
| cURL requests to the Claude API | Your service account’s access token, in `ANTHROPIC_AUTH_TOKEN` | [Authenticate from your workload](https://platform.claude.com/docs/en/manage-claude/workload-identity-federation#authenticate-from-your-workload) |
| Requests to `auth.claude.com` | A client assertion: a JWT for your app’s **Expected audience**, in the file that `CLIENT_ASSERTION_FILE` names or in place of `YOUR_CLIENT_ASSERTION_JWT` | Your identity provider |
| All | Your app’s client ID and redirect URI, in place of the sample’s client ID and redirect URI | Your app’s page in the Claude Console |

Set `ANTHROPIC_AUTH_TOKEN` only where the cURL samples run. Where the SDK and CLI samples run, unset it and `ANTHROPIC_API_KEY`, because [each one takes priority over federation](https://platform.claude.com/docs/en/manage-claude/workload-identity-federation#credential-precedence).

The client assertion and the federation JWT usually need different audiences, so keep them in separate files: see [when the two audiences differ](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/link-and-bill-a-customer#if-the-audiences-differ). The samples that use `CLIENT_ASSERTION_FILE` read it for each request, because the JWT in it rotates.

## Choose the user profile

A [user profile](https://platform.claude.com/docs/en/manage-claude/user-profiles) is a record in your own organization that stands for one of your customers. A request that bills the customer carries the profile’s ID, which tells Anthropic whom to bill. You can link a profile that you already have, unless it’s archived, and linking doesn’t change its ID or usage history.

Within one app, a customer’s Claude organization can link to only one of your profiles, and a profile can link to only one organization. Decide which profile stands for which organization before you link your first customer. The organization is the one that your customer selects when they approve, so ask them how their teams use Claude organizations:

* **Several teams share one Claude organization:** Use one profile for all of the teams.
* **Each team has its own Claude organization:** Use one profile for each organization.

If the customer selects an organization that’s already linked to another of your profiles, the approval is refused: see [`user_profile_already_linked` in Linked billing errors](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/errors#user-profile-already-linked).

Two cases change the profile that you create: [If you have a profile for each person](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/link-and-bill-a-customer#if-you-have-a-profile-for-each-person) and [If you resell API access](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/link-and-bill-a-customer#if-you-resell-api-access).

## Link the customer

<Frame>
  ![Sequence diagram: the customer approves at auth.claude.com, then your back end gets a connection and OAuth tokens](https://platform.claude.com/docs/images/linked-billing-link-flow.svg)
</Frame>

### Create the user profile

Create one user profile for each Claude organization that will link, as you mapped them in [Choose the user profile](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/link-and-bill-a-customer#choose-the-user-profile). Skip this step for a profile that you already have. Send a name and your own ID for the customer (`reference_id`). Create the profile once, and store its ID with the customer’s record: each create request makes a new profile, even with the same `reference_id`.

<CodeGroup>
  ```bash cURL
  curl https://api.anthropic.com/v1/user_profiles \
    -H "authorization: Bearer $ANTHROPIC_AUTH_TOKEN" \
    -H "anthropic-version: 2026-10-21" \
    -H "content-type: application/json" \
    -d '{
      "name": "Example Customer Inc.",
      "external_user_details": {"reference_id": "cust_2abc3def"}
    }'
  ```

  ```bash CLI
  ant user-profiles create \
    --name "Example Customer Inc." \
    --external-user-details.reference-id cust_2abc3def
  ```

  ```python Python
  client = anthropic.Anthropic()

  profile = client.user_profiles.create(
      name="Example Customer Inc.",
      external_user_details={"reference_id": "cust_2abc3def"},
  )

  print(profile.id)
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const profile = await client.userProfiles.create({
    name: "Example Customer Inc.",
    external_user_details: { reference_id: "cust_2abc3def" }
  });

  console.log(profile.id);
  ```

  ```csharp C#
  AnthropicClient client = new();

  var profile = await client.UserProfiles.Create(
      new()
      {
          Name = "Example Customer Inc.",
          ExternalUserDetails = new() { ReferenceID = "cust_2abc3def" },
      }
  );

  Console.WriteLine(profile.ID);
  ```

  ```go Go
  client := anthropic.NewClient()

  profile, err := client.UserProfiles.New(context.Background(), anthropic.UserProfileNewParams{
  	Name: anthropic.String("Example Customer Inc."),
  	ExternalUserDetails: anthropic.UserProfileExternalUserDetailsParams{
  		ReferenceID: anthropic.String("cust_2abc3def"),
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
              .referenceId("cust_2abc3def")
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
      externalUserDetails: ['referenceID' => 'cust_2abc3def'],
  );

  echo $profile->id, PHP_EOL;
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  profile = client.user_profiles.create(
    name: "Example Customer Inc.",
    external_user_details: { reference_id: "cust_2abc3def" }
  )

  puts(profile.id)
  ```
</CodeGroup>

The response holds the profile’s `id`, such as `uprof_01HV9Z`.

### Send the customer to approve

Add a [Link your Claude organization button](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/link-button) to your product, where your customers manage billing or integrations. Its HTML, colors, and logo are ready to copy.

The approval page offers only the organizations of the signed-in Claude account, and the organization that the customer selects pays. For what to show beside the button, see [What to tell your customers](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/link-and-bill-a-customer#what-to-tell-your-customers).

When the customer clicks the button, do these three things in your back end:

1. **Create a `state` value and a PKCE code verifier,** a random secret that proves your back end started this approval. Store both on your back end, tied to the browser session and the customer’s record.
2. **Send a pushed authorization request** to `auth.claude.com`, which passes the approval’s details from your back end instead of through the browser.
3. **Redirect the browser** to `https://auth.claude.com/oauth/authorize` with your `client_id` and the `request_uri` from the response. A `request_uri` works once and expires after 10 minutes, so send a new pushed authorization request for each click.

No SDK covers `auth.claude.com`, so the samples for these steps call it over HTTP:

<CodeGroup exclude="shell:CLI">
  ```bash cURL
  curl https://auth.claude.com/v1/oauth/par \
    -H "content-type: application/json" \
    -d @- <<'JSON'
  {
    "response_type": "code",
    "client_id": "clid_01ABcDeFgHiJkLmNoPqRsTuV",
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
  }
  JSON
  ```

  <CodeGroupItem language="CLI">
    The `ant` CLI has no command for `auth.claude.com`. Send the request with cURL or in your application’s language.
  </CodeGroupItem>

  ```python Python
  import base64
  import hashlib
  import os
  import secrets
  from pathlib import Path
  from urllib.parse import urlencode

  import httpx2  # comes with the Anthropic SDK

  CLIENT_ID = "clid_01ABcDeFgHiJkLmNoPqRsTuV"


  def push_authorization_request(user_profile_id: str) -> dict[str, str]:
      state = secrets.token_urlsafe(32)
      code_verifier = secrets.token_urlsafe(64)
      digest = hashlib.sha256(code_verifier.encode()).digest()
      assertion_file = Path(os.environ["CLIENT_ASSERTION_FILE"])

      response = httpx2.post(
          "https://auth.claude.com/v1/oauth/par",
          json={
              "response_type": "code",
              "client_id": CLIENT_ID,
              "redirect_uri": "https://app.example.com/claude/billing/callback",
              "scope": "billing:attribution",
              "connection_type": "organization_shared",
              "connection_auth_target": "platform",
              "user_profile_id": user_profile_id,
              "state": state,
              "code_challenge": base64.urlsafe_b64encode(digest).rstrip(b"=").decode(),
              "code_challenge_method": "S256",
              "client_assertion_type": "urn:ietf:params:oauth:client-assertion-type:jwt-bearer",
              "client_assertion": assertion_file.read_text().strip(),
          },
          timeout=10,
      )
      if not response.is_success:
          raise RuntimeError(f"Request failed: {response.status_code} {response.text}")

      query = {"client_id": CLIENT_ID, "request_uri": response.json()["request_uri"]}
      return {
          "approval_url": f"https://auth.claude.com/oauth/authorize?{urlencode(query)}",
          "state": state,
          "code_verifier": code_verifier,
      }
  ```

  ```typescript TypeScript
  import { createHash, randomBytes } from "node:crypto";
  import { readFile } from "node:fs/promises";

  const CLIENT_ID = "clid_01ABcDeFgHiJkLmNoPqRsTuV";

  async function pushAuthorizationRequest(userProfileId: string) {
    const state = randomBytes(32).toString("base64url");
    const codeVerifier = randomBytes(64).toString("base64url");
    const jwt = await readFile(process.env.CLIENT_ASSERTION_FILE!, "utf8");

    const response = await fetch("https://auth.claude.com/v1/oauth/par", {
      method: "POST",
      redirect: "error",
      signal: AbortSignal.timeout(10_000),
      headers: { "content-type": "application/json" },
      body: JSON.stringify({
        response_type: "code",
        client_id: CLIENT_ID,
        redirect_uri: "https://app.example.com/claude/billing/callback",
        scope: "billing:attribution",
        connection_type: "organization_shared",
        connection_auth_target: "platform",
        user_profile_id: userProfileId,
        state,
        code_challenge: createHash("sha256").update(codeVerifier).digest("base64url"),
        code_challenge_method: "S256",
        client_assertion_type: "urn:ietf:params:oauth:client-assertion-type:jwt-bearer",
        client_assertion: jwt.trim()
      })
    });
    if (!response.ok) {
      throw new Error(`Request failed: ${response.status} ${await response.text()}`);
    }

    const { request_uri } = (await response.json()) as { request_uri: string };
    const query = new URLSearchParams({ client_id: CLIENT_ID, request_uri });
    return {
      approvalUrl: `https://auth.claude.com/oauth/authorize?${query}`,
      state,
      codeVerifier
    };
  }
  ```

  ```csharp C#
  using System.Buffers.Text;
  using System.Net.Http.Json;
  using System.Security.Cryptography;
  using System.Text;
  using System.Text.Json;

  const string ClientId = "clid_01ABcDeFgHiJkLmNoPqRsTuV";
  using var http = new HttpClient { Timeout = TimeSpan.FromSeconds(10) };

  async Task<(string ApprovalUrl, string State, string CodeVerifier)> PushAuthorizationRequest(
      string userProfileId
  )
  {
      var state = Base64Url.EncodeToString(RandomNumberGenerator.GetBytes(32));
      var codeVerifier = Base64Url.EncodeToString(RandomNumberGenerator.GetBytes(64));
      var digest = SHA256.HashData(Encoding.ASCII.GetBytes(codeVerifier));
      var assertionFile = Environment.GetEnvironmentVariable("CLIENT_ASSERTION_FILE")!;
      var jwt = await File.ReadAllTextAsync(assertionFile);

      using var response = await http.PostAsJsonAsync(
          "https://auth.claude.com/v1/oauth/par",
          new Dictionary<string, string>
          {
              ["response_type"] = "code",
              ["client_id"] = ClientId,
              ["redirect_uri"] = "https://app.example.com/claude/billing/callback",
              ["scope"] = "billing:attribution",
              ["connection_type"] = "organization_shared",
              ["connection_auth_target"] = "platform",
              ["user_profile_id"] = userProfileId,
              ["state"] = state,
              ["code_challenge"] = Base64Url.EncodeToString(digest),
              ["code_challenge_method"] = "S256",
              ["client_assertion_type"] = "urn:ietf:params:oauth:client-assertion-type:jwt-bearer",
              ["client_assertion"] = jwt.Trim(),
          }
      );
      if (!response.IsSuccessStatusCode)
      {
          var details = await response.Content.ReadAsStringAsync();
          throw new HttpRequestException($"Request failed: {(int)response.StatusCode} {details}");
      }

      var result = await response.Content.ReadFromJsonAsync<JsonElement>();
      var requestUri = Uri.EscapeDataString(result.GetProperty("request_uri").GetString()!);
      var query = $"client_id={ClientId}&request_uri={requestUri}";
      return ($"https://auth.claude.com/oauth/authorize?{query}", state, codeVerifier);
  }
  ```

  ```go Go
  import (
  	"bytes"
  	"crypto/rand"
  	"crypto/sha256"
  	"encoding/base64"
  	"encoding/json"
  	"fmt"
  	"io"
  	"net/http"
  	"net/url"
  	"os"
  	"strings"
  	"time"
  )

  const clientID = "clid_01ABcDeFgHiJkLmNoPqRsTuV"

  var httpClient = &http.Client{Timeout: 10 * time.Second}

  type approval struct{ URL, State, CodeVerifier string }

  func pushAuthorizationRequest(userProfileID string) (*approval, error) {
  	state := rand.Text()
  	codeVerifier := rand.Text() + rand.Text() // PKCE needs at least 43 characters
  	digest := sha256.Sum256([]byte(codeVerifier))
  	jwt, err := os.ReadFile(os.Getenv("CLIENT_ASSERTION_FILE"))
  	if err != nil {
  		return nil, err
  	}

  	body, err := json.Marshal(map[string]string{
  		"response_type":          "code",
  		"client_id":              clientID,
  		"redirect_uri":           "https://app.example.com/claude/billing/callback",
  		"scope":                  "billing:attribution",
  		"connection_type":        "organization_shared",
  		"connection_auth_target": "platform",
  		"user_profile_id":        userProfileID,
  		"state":                  state,
  		"code_challenge":         base64.RawURLEncoding.EncodeToString(digest[:]),
  		"code_challenge_method":  "S256",
  		"client_assertion_type":  "urn:ietf:params:oauth:client-assertion-type:jwt-bearer",
  		"client_assertion":       strings.TrimSpace(string(jwt)),
  	})
  	if err != nil {
  		return nil, err
  	}

  	endpoint := "https://auth.claude.com/v1/oauth/par"
  	response, err := httpClient.Post(endpoint, "application/json", bytes.NewReader(body))
  	if err != nil {
  		return nil, err
  	}
  	defer response.Body.Close()
  	if response.StatusCode/100 != 2 {
  		details, _ := io.ReadAll(response.Body)
  		return nil, fmt.Errorf("request failed: %d %s", response.StatusCode, details)
  	}

  	var result struct {
  		RequestURI string `json:"request_uri"`
  	}
  	if err := json.NewDecoder(response.Body).Decode(&result); err != nil {
  		return nil, err
  	}
  	query := url.Values{"client_id": {clientID}, "request_uri": {result.RequestURI}}
  	approvalURL := "https://auth.claude.com/oauth/authorize?" + query.Encode()
  	return &approval{approvalURL, state, codeVerifier}, nil
  }
  ```

  ```java Java
  import module java.base;
  import module java.net.http;
  import com.fasterxml.jackson.databind.ObjectMapper; // Jackson comes with the Anthropic SDK

  static final String CLIENT_ID = "clid_01ABcDeFgHiJkLmNoPqRsTuV";
  static final Base64.Encoder BASE64_URL = Base64.getUrlEncoder().withoutPadding();
  final HttpClient http = HttpClient.newHttpClient();
  final ObjectMapper mapper = new ObjectMapper();

  record Approval(String url, String state, String codeVerifier) {}

  String randomValue(int size) {
      var bytes = new byte[size];
      new SecureRandom().nextBytes(bytes);
      return BASE64_URL.encodeToString(bytes);
  }

  Approval pushAuthorizationRequest(String userProfileId) throws Exception {
      var state = randomValue(32);
      var codeVerifier = randomValue(64);
      var digest = MessageDigest.getInstance("SHA-256")
          .digest(codeVerifier.getBytes(StandardCharsets.US_ASCII));
      var jwt = Files.readString(Path.of(System.getenv("CLIENT_ASSERTION_FILE")));

      var body = mapper.createObjectNode()
          .put("response_type", "code")
          .put("client_id", CLIENT_ID)
          .put("redirect_uri", "https://app.example.com/claude/billing/callback")
          .put("scope", "billing:attribution")
          .put("connection_type", "organization_shared")
          .put("connection_auth_target", "platform")
          .put("user_profile_id", userProfileId)
          .put("state", state)
          .put("code_challenge", BASE64_URL.encodeToString(digest))
          .put("code_challenge_method", "S256")
          .put("client_assertion_type", "urn:ietf:params:oauth:client-assertion-type:jwt-bearer")
          .put("client_assertion", jwt.strip());

      var request = HttpRequest.newBuilder(URI.create("https://auth.claude.com/v1/oauth/par"))
          .header("content-type", "application/json")
          .timeout(Duration.ofSeconds(10))
          .POST(HttpRequest.BodyPublishers.ofString(body.toString()))
          .build();
      var response = http.send(request, HttpResponse.BodyHandlers.ofString());
      if (response.statusCode() / 100 != 2) {
          throw new IOException("Request failed: " + response.statusCode() + " " + response.body());
      }

      var requestUri = mapper.readTree(response.body()).get("request_uri").asText();
      var query = "client_id=%s&request_uri=%s"
          .formatted(CLIENT_ID, URLEncoder.encode(requestUri, StandardCharsets.UTF_8));
      return new Approval("https://auth.claude.com/oauth/authorize?" + query, state, codeVerifier);
  }
  ```

  ```php PHP
  const CLIENT_ID = 'clid_01ABcDeFgHiJkLmNoPqRsTuV';

  function base64Url(string $bytes): string
  {
      return rtrim(strtr(base64_encode($bytes), '+/', '-_'), '=');
  }

  /** @return array{approvalUrl: string, state: string, codeVerifier: string} */
  function pushAuthorizationRequest(string $userProfileId): array
  {
      $state = base64Url(random_bytes(32));
      $codeVerifier = base64Url(random_bytes(64));
      $jwt = file_get_contents((string) getenv('CLIENT_ASSERTION_FILE'))
          ?: throw new \RuntimeException('Cannot read the client assertion file');

      $body = json_encode([
          'response_type' => 'code',
          'client_id' => CLIENT_ID,
          'redirect_uri' => 'https://app.example.com/claude/billing/callback',
          'scope' => 'billing:attribution',
          'connection_type' => 'organization_shared',
          'connection_auth_target' => 'platform',
          'user_profile_id' => $userProfileId,
          'state' => $state,
          'code_challenge' => base64Url(hash('sha256', $codeVerifier, binary: true)),
          'code_challenge_method' => 'S256',
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
      $response = file_get_contents('https://auth.claude.com/v1/oauth/par', context: $context);
      $status = http_get_last_response_headers()[0] ?? '';
      if ($response === false || !preg_match('{^HTTP/\S+ 2}', $status)) {
          throw new \RuntimeException("Request failed: {$status} {$response}");
      }

      /** @var array{request_uri: string} $result */
      $result = json_decode($response, associative: true, flags: JSON_THROW_ON_ERROR);
      $query = http_build_query(['client_id' => CLIENT_ID, 'request_uri' => $result['request_uri']]);

      return [
          'approvalUrl' => "https://auth.claude.com/oauth/authorize?{$query}",
          'state' => $state,
          'codeVerifier' => $codeVerifier,
      ];
  }
  ```

  ```ruby Ruby
  require "base64"
  require "digest"
  require "json"
  require "net/http"
  require "securerandom"

  CLIENT_ID = "clid_01ABcDeFgHiJkLmNoPqRsTuV"

  def push_authorization_request(user_profile_id)
    state = SecureRandom.urlsafe_base64(32)
    code_verifier = SecureRandom.urlsafe_base64(64)
    digest = Digest::SHA256.digest(code_verifier)
    jwt = File.read(ENV.fetch("CLIENT_ASSERTION_FILE"))

    body = {
      response_type: "code",
      client_id: CLIENT_ID,
      redirect_uri: "https://app.example.com/claude/billing/callback",
      scope: "billing:attribution",
      connection_type: "organization_shared",
      connection_auth_target: "platform",
      user_profile_id:,
      state:,
      code_challenge: Base64.urlsafe_encode64(digest, padding: false),
      code_challenge_method: "S256",
      client_assertion_type: "urn:ietf:params:oauth:client-assertion-type:jwt-bearer",
      client_assertion: jwt.strip
    }
    response = Net::HTTP.start("auth.claude.com", 443, use_ssl: true, read_timeout: 10) do |http|
      http.post("/v1/oauth/par", body.to_json, "content-type" => "application/json")
    end
    unless response.is_a?(Net::HTTPSuccess)
      raise "Request failed: #{response.code} #{response.body}"
    end

    request_uri = JSON.parse(response.body).fetch("request_uri")
    query = URI.encode_www_form(client_id: CLIENT_ID, request_uri:)
    { approval_url: "https://auth.claude.com/oauth/authorize?#{query}", state:, code_verifier: }
  end
  ```
</CodeGroup>

The pushed authorization request carries your client ID and a client assertion, the customer’s user profile ID, and the scope. It also carries your registered redirect URI, the `state`, and a code challenge made from the verifier. `connection_type` and `connection_auth_target` mark it as a Linked billing request. For each field and its value, see [OAuth endpoints and parameters](https://platform.claude.com/docs/en/manage-claude/oauth-apps/endpoints-and-parameters#authorization-requests).

The scope is `billing:attribution`. To also get a refresh token, ask for `billing:attribution offline_access`, which needs **Offline access** turned on for your app. Whether you need one depends on [how your back end bills](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/set-up-your-app#choose-whether-to-get-refresh-tokens). Adding `offline_access` for a customer who is already linked makes a new connection that replaces the earlier one: see [If a customer approves again](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/link-and-bill-a-customer#if-a-customer-approves-again).

On the approval page, the customer signs in to Claude if needed, selects the organization to link, and approves. Until your app is live, the person who approves must also set a spend cap for your app: see [Caps while testing](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/test-and-publish#caps-while-testing).

### Save the connection and its OAuth tokens

After the customer approves, `auth.claude.com` sends the browser to your redirect URI. Then, do these things in your back end:

1. **Check the callback.** Check that its `state` matches the one you stored, which shows that the same browser came back. Check that its `iss` is `https://identity.anthropic.com/users`, which shows that the callback came from Claude. If either is missing or doesn’t match, stop.
2. **Check for an error.** If the callback carries an `error` parameter instead of a code, no connection was made. For the causes, see [Linked billing errors](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/errors#while-linking).
3. **Exchange the code at once.** Send it with the PKCE code verifier, the redirect URI from your pushed authorization request, and a client assertion. The code expires after 5 minutes.
4. **Store what the response returns.** The exchange returns the OAuth tokens only once.

These samples send the code exchange to `auth.claude.com` over HTTP:

<CodeGroup exclude="shell:CLI">
  ```bash cURL
  curl https://auth.claude.com/v1/oauth/token \
    -H "content-type: application/json" \
    -d @- <<'JSON'
  {
    "grant_type": "authorization_code",
    "code": "AUTH_CODE",
    "code_verifier": "ORIGINAL_CODE_VERIFIER",
    "redirect_uri": "https://app.example.com/claude/billing/callback",
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
  import secrets
  from pathlib import Path

  import httpx2  # comes with the Anthropic SDK


  def handle_callback(params: dict[str, str], state: str, code_verifier: str) -> dict:
      if not secrets.compare_digest(params.get("state", "").encode(), state.encode()):
          raise ValueError("state does not match")
      if params.get("iss") != "https://identity.anthropic.com/users":
          raise ValueError("iss does not match")
      if "error" in params:
          raise PermissionError(params["error"])

      assertion_file = Path(os.environ["CLIENT_ASSERTION_FILE"])

      response = httpx2.post(
          "https://auth.claude.com/v1/oauth/token",
          json={
              "grant_type": "authorization_code",
              "code": params["code"],
              "code_verifier": code_verifier,
              "redirect_uri": "https://app.example.com/claude/billing/callback",
              "client_id": "clid_01ABcDeFgHiJkLmNoPqRsTuV",
              "client_assertion_type": "urn:ietf:params:oauth:client-assertion-type:jwt-bearer",
              "client_assertion": assertion_file.read_text().strip(),
          },
          timeout=10,
      )
      if not response.is_success:
          raise RuntimeError(f"Exchange failed: {response.status_code} {response.text}")
      return response.json()  # connection_id and the tokens
  ```

  ```typescript TypeScript
  import { timingSafeEqual } from "node:crypto";
  import { readFile } from "node:fs/promises";

  async function handleCallback(params: URLSearchParams, state: string, codeVerifier: string) {
    const received = new TextEncoder().encode(params.get("state") ?? "");
    const expected = new TextEncoder().encode(state);
    if (received.length !== expected.length || !timingSafeEqual(received, expected)) {
      throw new Error("state does not match");
    }
    if (params.get("iss") !== "https://identity.anthropic.com/users") {
      throw new Error("iss does not match");
    }
    if (params.has("error")) {
      throw new Error(`Linking failed: ${params.get("error")}`);
    }

    const jwt = await readFile(process.env.CLIENT_ASSERTION_FILE!, "utf8");

    const response = await fetch("https://auth.claude.com/v1/oauth/token", {
      method: "POST",
      redirect: "error",
      signal: AbortSignal.timeout(10_000),
      headers: { "content-type": "application/json" },
      body: JSON.stringify({
        grant_type: "authorization_code",
        code: params.get("code"),
        code_verifier: codeVerifier,
        redirect_uri: "https://app.example.com/claude/billing/callback",
        client_id: "clid_01ABcDeFgHiJkLmNoPqRsTuV",
        client_assertion_type: "urn:ietf:params:oauth:client-assertion-type:jwt-bearer",
        client_assertion: jwt.trim()
      })
    });
    if (!response.ok) {
      throw new Error(`Exchange failed: ${response.status} ${await response.text()}`);
    }
    return response.json(); // connection_id and the tokens
  }
  ```

  ```csharp C#
  using System.Net.Http.Json;
  using System.Security.Cryptography;
  using System.Text;
  using System.Text.Json;

  using var http = new HttpClient { Timeout = TimeSpan.FromSeconds(10) };

  async Task<JsonElement> HandleCallback(
      Dictionary<string, string> parameters,
      string state,
      string codeVerifier
  )
  {
      var received = Encoding.UTF8.GetBytes(parameters.GetValueOrDefault("state", ""));
      if (!CryptographicOperations.FixedTimeEquals(received, Encoding.UTF8.GetBytes(state)))
      {
          throw new InvalidOperationException("state does not match");
      }
      if (parameters.GetValueOrDefault("iss") != "https://identity.anthropic.com/users")
      {
          throw new InvalidOperationException("iss does not match");
      }
      if (parameters.TryGetValue("error", out var error))
      {
          throw new InvalidOperationException($"Linking failed: {error}");
      }

      var assertionFile = Environment.GetEnvironmentVariable("CLIENT_ASSERTION_FILE")!;
      var jwt = await File.ReadAllTextAsync(assertionFile);

      using var response = await http.PostAsJsonAsync(
          "https://auth.claude.com/v1/oauth/token",
          new Dictionary<string, string>
          {
              ["grant_type"] = "authorization_code",
              ["code"] = parameters["code"],
              ["code_verifier"] = codeVerifier,
              ["redirect_uri"] = "https://app.example.com/claude/billing/callback",
              ["client_id"] = "clid_01ABcDeFgHiJkLmNoPqRsTuV",
              ["client_assertion_type"] = "urn:ietf:params:oauth:client-assertion-type:jwt-bearer",
              ["client_assertion"] = jwt.Trim(),
          }
      );
      if (!response.IsSuccessStatusCode)
      {
          var details = await response.Content.ReadAsStringAsync();
          throw new HttpRequestException($"Exchange failed: {(int)response.StatusCode} {details}");
      }

      // connection_id and the tokens
      return await response.Content.ReadFromJsonAsync<JsonElement>();
  }
  ```

  ```go Go
  import (
  	"bytes"
  	"crypto/subtle"
  	"encoding/json"
  	"errors"
  	"fmt"
  	"io"
  	"net/http"
  	"net/url"
  	"os"
  	"strings"
  	"time"
  )

  var httpClient = &http.Client{Timeout: 10 * time.Second}

  func handleCallback(params url.Values, state, codeVerifier string) (map[string]any, error) {
  	if subtle.ConstantTimeCompare([]byte(params.Get("state")), []byte(state)) != 1 {
  		return nil, errors.New("state does not match")
  	}
  	if params.Get("iss") != "https://identity.anthropic.com/users" {
  		return nil, errors.New("iss does not match")
  	}
  	if params.Has("error") {
  		return nil, fmt.Errorf("linking failed: %s", params.Get("error"))
  	}

  	jwt, err := os.ReadFile(os.Getenv("CLIENT_ASSERTION_FILE"))
  	if err != nil {
  		return nil, err
  	}

  	body, err := json.Marshal(map[string]string{
  		"grant_type":            "authorization_code",
  		"code":                  params.Get("code"),
  		"code_verifier":         codeVerifier,
  		"redirect_uri":          "https://app.example.com/claude/billing/callback",
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
  		return nil, fmt.Errorf("exchange failed: %d %s", response.StatusCode, details)
  	}

  	var connection map[string]any // connection_id and the tokens
  	err = json.NewDecoder(response.Body).Decode(&connection)
  	return connection, err
  }
  ```

  ```java Java
  import module java.base;
  import module java.net.http;
  import com.fasterxml.jackson.databind.JsonNode;
  import com.fasterxml.jackson.databind.ObjectMapper; // Jackson comes with the Anthropic SDK

  final HttpClient http = HttpClient.newHttpClient();
  final ObjectMapper mapper = new ObjectMapper();

  JsonNode handleCallback(Map<String, String> params, String state, String codeVerifier)
          throws Exception {
      var received = params.getOrDefault("state", "").getBytes(StandardCharsets.UTF_8);
      if (!MessageDigest.isEqual(received, state.getBytes(StandardCharsets.UTF_8))) {
          throw new IllegalStateException("state does not match");
      }
      if (!"https://identity.anthropic.com/users".equals(params.get("iss"))) {
          throw new IllegalStateException("iss does not match");
      }
      if (params.containsKey("error")) {
          throw new IllegalStateException("Linking failed: " + params.get("error"));
      }

      var jwt = Files.readString(Path.of(System.getenv("CLIENT_ASSERTION_FILE")));

      var body = mapper.createObjectNode()
          .put("grant_type", "authorization_code")
          .put("code", params.get("code"))
          .put("code_verifier", codeVerifier)
          .put("redirect_uri", "https://app.example.com/claude/billing/callback")
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
          throw new IOException("Exchange failed: " + response.statusCode() + " " + response.body());
      }
      return mapper.readTree(response.body()); // connection_id and the tokens
  }
  ```

  ```php PHP
  /** @param array<string, string> $params */
  function handleCallback(array $params, string $state, string $codeVerifier): mixed
  {
      if (!hash_equals($state, $params['state'] ?? '')) {
          throw new \RuntimeException('state does not match');
      }
      if (($params['iss'] ?? '') !== 'https://identity.anthropic.com/users') {
          throw new \RuntimeException('iss does not match');
      }
      if (isset($params['error'])) {
          throw new \RuntimeException("Linking failed: {$params['error']}");
      }

      $jwt = file_get_contents((string) getenv('CLIENT_ASSERTION_FILE'))
          ?: throw new \RuntimeException('Cannot read the client assertion file');

      $body = json_encode([
          'grant_type' => 'authorization_code',
          'code' => $params['code'],
          'code_verifier' => $codeVerifier,
          'redirect_uri' => 'https://app.example.com/claude/billing/callback',
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
          throw new \RuntimeException("Exchange failed: {$status} {$response}");
      }

      // connection_id and the tokens
      return json_decode($response, associative: true, flags: JSON_THROW_ON_ERROR);
  }
  ```

  ```ruby Ruby
  require "json"
  require "net/http"
  require "openssl"

  def handle_callback(params, state, code_verifier)
    raise "state does not match" unless OpenSSL.secure_compare(params["state"].to_s, state)
    raise "iss does not match" unless params["iss"] == "https://identity.anthropic.com/users"
    raise "Linking failed: #{params["error"]}" if params.key?("error")

    jwt = File.read(ENV.fetch("CLIENT_ASSERTION_FILE"))

    body = {
      grant_type: "authorization_code",
      code: params.fetch("code"),
      code_verifier:,
      redirect_uri: "https://app.example.com/claude/billing/callback",
      client_id: "clid_01ABcDeFgHiJkLmNoPqRsTuV",
      client_assertion_type: "urn:ietf:params:oauth:client-assertion-type:jwt-bearer",
      client_assertion: jwt.strip
    }
    response = Net::HTTP.start("auth.claude.com", 443, use_ssl: true, read_timeout: 10) do |http|
      http.post("/v1/oauth/token", body.to_json, "content-type" => "application/json")
    end
    unless response.is_a?(Net::HTTPSuccess)
      raise "Exchange failed: #{response.code} #{response.body}"
    end

    JSON.parse(response.body) # connection_id and the tokens
  end
  ```
</CodeGroup>

The response holds these values:

| Value | What it is | What to do with it |
| ----- | ----- | ----- |
| `connection_id` | The connection’s ID | Store it with the customer’s record, to end the connection from your back end later |
| `access_token` | The customer’s own token, separate from your service account’s: it can bill only this customer, for up to 1 hour | Store it as a secret |
| `refresh_token` | A token that gets new access tokens, if you asked for `offline_access` | Store it as a secret |

The response doesn’t say which organization the customer linked.

The requests on this page bill as your service account, so they don’t need the OAuth tokens. Store them anyway: you need them to [use a separate credential for each customer](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/credential-for-each-customer). If you asked for a refresh token, you can’t get it again unless you unlink the customer and they link again.

If the exchange fails, what you do depends on how:

* **The exchange returns `unauthorized_client`:** Usually, your app has no operator service account or default workspace, or the workspace is archived. See [how to fix `unauthorized_client`](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/errors#code-exchange-unauthorized-client).
* **The exchange returns `invalid_grant`:** The redirect URI or the verifier was wrong, or the code expired or was already used. A wrong redirect URI or verifier uses up the code, so the customer has to approve again. For a customer who is already linked, see [If a customer approves again](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/link-and-bill-a-customer#if-a-customer-approves-again).
* **The exchange timed out:** [Send the same code once more](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/link-and-bill-a-customer#if-the-code-exchange-times-out).

## Bill a request

Send every request for this customer as your operator service account, and put the customer’s user profile ID in the `anthropic-user-profile-id` header. The SDK sends that header for you from its user profile parameter. The header makes the request count in that profile’s usage, whoever pays. Then, choose on each request whether the customer or you pays.

### Your customer pays

To bill a request to the customer, name the profile that holds their connection in that header, and also send:

* [`billing_policy`](https://platform.claude.com/docs/en/api/beta/messages/create) in the request body, set to `{"type": "billing_policy", "bill_to": "user_profile"}`
* the `user-profiles-billing-2026-10-01` beta header

<Warning>
  If a request names another linked customer’s profile, Anthropic bills that customer’s organization, and no error tells you.
</Warning>

Check each request’s profile ID. Your test customer pays real money for these requests, as any customer would.

<CodeGroup>
  ```bash cURL
  curl https://api.anthropic.com/v1/messages \
    -H "authorization: Bearer $ANTHROPIC_AUTH_TOKEN" \
    -H "anthropic-version: 2026-10-21" \
    -H "anthropic-beta: user-profiles-billing-2026-10-01" \
    -H "anthropic-user-profile-id: uprof_01HV9Z" \
    -H "content-type: application/json" \
    -d '{
      "model": "claude-opus-5-5",
      "max_tokens": 1024,
      "messages": [{"role": "user", "content": "Hello, Claude"}],
      "billing_policy": {"type": "billing_policy", "bill_to": "user_profile"}
    }'
  ```

  ```bash CLI
  ant beta:messages create \
    --beta user-profiles-billing-2026-10-01 \
    --user-profile-id uprof_01HV9Z \
    --model claude-opus-5-5 \
    --max-tokens 1024 \
    --message '{role: user, content: "Hello, Claude"}' \
    --billing-policy '{type: billing_policy, bill_to: user_profile}'
  ```

  ```python Python
  client = anthropic.Anthropic()

  message = client.beta.messages.create(
      model="claude-opus-5-5",
      max_tokens=1024,
      messages=[{"role": "user", "content": "Hello, Claude"}],
      betas=["user-profiles-billing-2026-10-01"],
      user_profile_id="uprof_01HV9Z",
      billing_policy={"type": "billing_policy", "bill_to": "user_profile"},
  )

  for block in message.content:
      if block.type == "text":
          print(block.text)
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const message = await client.beta.messages.create({
    model: "claude-opus-5-5",
    max_tokens: 1024,
    messages: [{ role: "user", content: "Hello, Claude" }],
    betas: ["user-profiles-billing-2026-10-01"],
    user_profile_id: "uprof_01HV9Z",
    billing_policy: { type: "billing_policy", bill_to: "user_profile" }
  });

  for (const block of message.content) {
    if (block.type === "text") {
      console.log(block.text);
    }
  }
  ```

  ```csharp C#
  using Anthropic.Models.Beta.Messages;
  using Model = Anthropic.Models.Messages.Model;

  AnthropicClient client = new();

  var message = await client.Beta.Messages.Create(
      new MessageCreateParams
      {
          Model = Model.ClaudeOpus5_5,
          MaxTokens = 1024,
          Messages = [new BetaUserMessageParam { Content = "Hello, Claude" }],
          Betas = ["user-profiles-billing-2026-10-01"],
          UserProfileID = "uprof_01HV9Z",
          BillingPolicy = new() { BillTo = BetaBillTo.UserProfile },
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
  client := anthropic.NewClient()

  message, err := client.Beta.Messages.New(context.Background(), anthropic.BetaMessageNewParams{
  	Model:     anthropic.ModelClaudeOpus5_5,
  	MaxTokens: 1024,
  	Messages: []anthropic.BetaMessageParam{
  		anthropic.NewBetaUserMessage(anthropic.NewBetaTextBlock("Hello, Claude")),
  	},
  	Betas:         []anthropic.AnthropicBeta{"user-profiles-billing-2026-10-01"},
  	UserProfileID: anthropic.String("uprof_01HV9Z"),
  	BillingPolicy: anthropic.BetaBillingPolicyParam{BillTo: anthropic.BetaBillToUserProfile},
  })
  if err != nil {
  	log.Fatal(err)
  }

  for _, block := range message.Content {
  	if textBlock, ok := block.AsAny().(anthropic.BetaTextBlock); ok {
  		fmt.Println(textBlock.Text)
  	}
  }
  ```

  ```java Java
  import com.anthropic.models.beta.messages.BetaBillTo;
  import com.anthropic.models.beta.messages.BetaBillingPolicy;
  import com.anthropic.models.beta.messages.MessageCreateParams;
  import com.anthropic.models.messages.Model;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      var params = MessageCreateParams.builder()
          .model(Model.CLAUDE_OPUS_5_5)
          .maxTokens(1024)
          .addUserMessage("Hello, Claude")
          .addBeta("user-profiles-billing-2026-10-01")
          .userProfileId("uprof_01HV9Z")
          .billingPolicy(BetaBillingPolicy.builder()
              .billTo(BetaBillTo.USER_PROFILE)
              .build())
          .build();
      var message = client.beta().messages().create(params);

      for (var block : message.content()) {
          block.text().ifPresent(textBlock -> IO.println(textBlock.text()));
      }
  }
  ```

  ```php PHP
  use Anthropic\Beta\Messages\BetaBillingPolicy;
  use Anthropic\Beta\Messages\BetaBillTo;
  use Anthropic\Beta\Messages\BetaTextBlock;
  use Anthropic\Messages\Model;

  $client = new Client();

  $message = $client->beta->messages->create(
      maxTokens: 1024,
      messages: [['role' => 'user', 'content' => 'Hello, Claude']],
      model: Model::CLAUDE_OPUS_5_5,
      betas: ['user-profiles-billing-2026-10-01'],
      userProfileID: 'uprof_01HV9Z',
      billingPolicy: BetaBillingPolicy::with(billTo: BetaBillTo::USER_PROFILE),
  );

  foreach ($message->content as $block) {
      if ($block instanceof BetaTextBlock) {
          echo $block->text, PHP_EOL;
      }
  }
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  message = client.beta.messages.create(
    model: Anthropic::Model::CLAUDE_OPUS_5_5,
    max_tokens: 1024,
    messages: [{ role: "user", content: "Hello, Claude" }],
    betas: ["user-profiles-billing-2026-10-01"],
    user_profile_id: "uprof_01HV9Z",
    billing_policy: { type: :billing_policy, bill_to: :user_profile }
  )

  message.content.each do |block|
    puts(block.text) if block.is_a?(Anthropic::Beta::BetaTextBlock)
  end
  ```
</CodeGroup>

The Claude API either bills the customer or refuses the request. It never bills you instead. On `/v1/messages`, a refused request carries its code in `error.details.error_code`. It can have these causes:

* **A new connection:** A new connection can take about 10 seconds to work after the code exchange. If your first request is refused with `user_profile_billing_not_authorized` within those 10 seconds, send it again after they pass. If it’s still refused, see [how to fix `user_profile_billing_not_authorized`](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/errors#user-profile-billing-not-authorized).
* **A customer who can’t be billed:** `user_profile_not_billable` can mean that the customer’s organization can’t be billed, for example because it has no billing set up. See [how to fix `user_profile_not_billable`](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/errors#user-profile-not-billable).
* **A spend limit or no credit:** Requests are refused with `linked_organization_spend_limit_reached` when the customer’s spend through your app reaches their cap or their organization reaches its own monthly spend limit. The same happens when no credit on their account can pay.
* **Anything else:** See [Linked billing errors while billing](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/errors#while-billing).

### You pay

To pay for a request yourself, keep sending the customer’s user profile ID in the header. Then, either leave `billing_policy` out or set its `bill_to` to `"self"`.

Without `billing_policy`, the beta header is optional:

<CodeGroup>
  ```bash cURL
  curl https://api.anthropic.com/v1/messages \
    -H "authorization: Bearer $ANTHROPIC_AUTH_TOKEN" \
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
    --model claude-opus-5-5 \
    --max-tokens 1024 \
    --message '{role: user, content: "Hello, Claude"}'
  ```

  ```python Python
  client = anthropic.Anthropic()

  message = client.messages.create(
      model="claude-opus-5-5",
      max_tokens=1024,
      messages=[{"role": "user", "content": "Hello, Claude"}],
      user_profile_id="uprof_01HV9Z",
  )

  for block in message.content:
      if block.type == "text":
          print(block.text)
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const message = await client.messages.create({
    model: "claude-opus-5-5",
    max_tokens: 1024,
    messages: [{ role: "user", content: "Hello, Claude" }],
    user_profile_id: "uprof_01HV9Z"
  });

  for (const block of message.content) {
    if (block.type === "text") {
      console.log(block.text);
    }
  }
  ```

  ```csharp C#
  using Anthropic.Models.Messages;

  AnthropicClient client = new();

  var message = await client.Messages.Create(
      new MessageCreateParams
      {
          Model = Model.ClaudeOpus5_5,
          MaxTokens = 1024,
          Messages = [new UserMessageParam { Content = "Hello, Claude" }],
          UserProfileID = "uprof_01HV9Z",
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
  client := anthropic.NewClient()

  message, err := client.Messages.New(context.Background(), anthropic.MessageNewParams{
  	Model:     anthropic.ModelClaudeOpus5_5,
  	MaxTokens: 1024,
  	Messages: []anthropic.MessageParam{
  		anthropic.NewUserMessage(anthropic.NewTextBlock("Hello, Claude")),
  	},
  	UserProfileID: anthropic.String("uprof_01HV9Z"),
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
  import com.anthropic.models.messages.MessageCreateParams;
  import com.anthropic.models.messages.Model;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      var params = MessageCreateParams.builder()
          .model(Model.CLAUDE_OPUS_5_5)
          .maxTokens(1024)
          .addUserMessage("Hello, Claude")
          .userProfileId("uprof_01HV9Z")
          .build();
      var message = client.messages().create(params);

      for (var block : message.content()) {
          block.text().ifPresent(textBlock -> IO.println(textBlock.text()));
      }
  }
  ```

  ```php PHP
  use Anthropic\Messages\Model;
  use Anthropic\Messages\TextBlock;

  $client = new Client();

  $message = $client->messages->create(
      maxTokens: 1024,
      messages: [['role' => 'user', 'content' => 'Hello, Claude']],
      model: Model::CLAUDE_OPUS_5_5,
      userProfileID: 'uprof_01HV9Z',
  );

  foreach ($message->content as $block) {
      if ($block instanceof TextBlock) {
          echo $block->text, PHP_EOL;
      }
  }
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  message = client.messages.create(
    model: Anthropic::Model::CLAUDE_OPUS_5_5,
    max_tokens: 1024,
    messages: [{ role: "user", content: "Hello, Claude" }],
    user_profile_id: "uprof_01HV9Z"
  )

  message.content.each do |block|
    puts(block.text) if block.is_a?(Anthropic::Models::TextBlock)
  end
  ```
</CodeGroup>

With `bill_to` set to `"self"`, the request needs the beta header:

<CodeGroup>
  ```bash cURL
  curl https://api.anthropic.com/v1/messages \
    -H "authorization: Bearer $ANTHROPIC_AUTH_TOKEN" \
    -H "anthropic-version: 2026-10-21" \
    -H "anthropic-beta: user-profiles-billing-2026-10-01" \
    -H "anthropic-user-profile-id: uprof_01HV9Z" \
    -H "content-type: application/json" \
    -d '{
      "model": "claude-opus-5-5",
      "max_tokens": 1024,
      "messages": [{"role": "user", "content": "Hello, Claude"}],
      "billing_policy": {"type": "billing_policy", "bill_to": "self"}
    }'
  ```

  ```bash CLI
  ant beta:messages create \
    --beta user-profiles-billing-2026-10-01 \
    --user-profile-id uprof_01HV9Z \
    --model claude-opus-5-5 \
    --max-tokens 1024 \
    --message '{role: user, content: "Hello, Claude"}' \
    --billing-policy '{type: billing_policy, bill_to: self}'
  ```

  ```python Python
  client = anthropic.Anthropic()

  message = client.beta.messages.create(
      model="claude-opus-5-5",
      max_tokens=1024,
      messages=[{"role": "user", "content": "Hello, Claude"}],
      betas=["user-profiles-billing-2026-10-01"],
      user_profile_id="uprof_01HV9Z",
      billing_policy={"type": "billing_policy", "bill_to": "self"},
  )

  for block in message.content:
      if block.type == "text":
          print(block.text)
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const message = await client.beta.messages.create({
    model: "claude-opus-5-5",
    max_tokens: 1024,
    messages: [{ role: "user", content: "Hello, Claude" }],
    betas: ["user-profiles-billing-2026-10-01"],
    user_profile_id: "uprof_01HV9Z",
    billing_policy: { type: "billing_policy", bill_to: "self" }
  });

  for (const block of message.content) {
    if (block.type === "text") {
      console.log(block.text);
    }
  }
  ```

  ```csharp C#
  using Anthropic.Models.Beta.Messages;
  using Model = Anthropic.Models.Messages.Model;

  AnthropicClient client = new();

  var message = await client.Beta.Messages.Create(
      new MessageCreateParams
      {
          Model = Model.ClaudeOpus5_5,
          MaxTokens = 1024,
          Messages = [new BetaUserMessageParam { Content = "Hello, Claude" }],
          Betas = ["user-profiles-billing-2026-10-01"],
          UserProfileID = "uprof_01HV9Z",
          BillingPolicy = new() { BillTo = BetaBillTo.Self },
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
  client := anthropic.NewClient()

  message, err := client.Beta.Messages.New(context.Background(), anthropic.BetaMessageNewParams{
  	Model:     anthropic.ModelClaudeOpus5_5,
  	MaxTokens: 1024,
  	Messages: []anthropic.BetaMessageParam{
  		anthropic.NewBetaUserMessage(anthropic.NewBetaTextBlock("Hello, Claude")),
  	},
  	Betas:         []anthropic.AnthropicBeta{"user-profiles-billing-2026-10-01"},
  	UserProfileID: anthropic.String("uprof_01HV9Z"),
  	BillingPolicy: anthropic.BetaBillingPolicyParam{BillTo: anthropic.BetaBillToSelf},
  })
  if err != nil {
  	log.Fatal(err)
  }

  for _, block := range message.Content {
  	if textBlock, ok := block.AsAny().(anthropic.BetaTextBlock); ok {
  		fmt.Println(textBlock.Text)
  	}
  }
  ```

  ```java Java
  import com.anthropic.models.beta.messages.BetaBillTo;
  import com.anthropic.models.beta.messages.BetaBillingPolicy;
  import com.anthropic.models.beta.messages.MessageCreateParams;
  import com.anthropic.models.messages.Model;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      var params = MessageCreateParams.builder()
          .model(Model.CLAUDE_OPUS_5_5)
          .maxTokens(1024)
          .addUserMessage("Hello, Claude")
          .addBeta("user-profiles-billing-2026-10-01")
          .userProfileId("uprof_01HV9Z")
          .billingPolicy(BetaBillingPolicy.builder()
              .billTo(BetaBillTo.SELF)
              .build())
          .build();
      var message = client.beta().messages().create(params);

      for (var block : message.content()) {
          block.text().ifPresent(textBlock -> IO.println(textBlock.text()));
      }
  }
  ```

  ```php PHP
  use Anthropic\Beta\Messages\BetaBillingPolicy;
  use Anthropic\Beta\Messages\BetaBillTo;
  use Anthropic\Beta\Messages\BetaTextBlock;
  use Anthropic\Messages\Model;

  $client = new Client();

  $message = $client->beta->messages->create(
      maxTokens: 1024,
      messages: [['role' => 'user', 'content' => 'Hello, Claude']],
      model: Model::CLAUDE_OPUS_5_5,
      betas: ['user-profiles-billing-2026-10-01'],
      userProfileID: 'uprof_01HV9Z',
      billingPolicy: BetaBillingPolicy::with(billTo: BetaBillTo::SELF),
  );

  foreach ($message->content as $block) {
      if ($block instanceof BetaTextBlock) {
          echo $block->text, PHP_EOL;
      }
  }
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  message = client.beta.messages.create(
    model: Anthropic::Model::CLAUDE_OPUS_5_5,
    max_tokens: 1024,
    messages: [{ role: "user", content: "Hello, Claude" }],
    betas: ["user-profiles-billing-2026-10-01"],
    user_profile_id: "uprof_01HV9Z",
    billing_policy: { type: :billing_policy, bill_to: :self }
  )

  message.content.each do |block|
    puts(block.text) if block.is_a?(Anthropic::Beta::BetaTextBlock)
  end
  ```
</CodeGroup>

## Check the result

First, check in the Claude Console that the customer is linked:

* Your User profiles page displays the customer’s profile as **Linked**. Only members with the Admin role see this status.
* Your app’s **Overview** tab lists the customer under **Linked customers**, with the connection ID that you stored.

Then, check the bill in the Console, because a billed request that succeeds returns a normal response that doesn’t say who paid. The test customer’s [Linked platforms](https://platform.claude.com/linked-platforms) page is open to members of that organization with the Admin or Billing role.

| Where | What it displays | How soon |
| ----- | ----- | ----- |
| The test customer’s [Linked platforms](https://platform.claude.com/linked-platforms) page | Your app’s spend this month, against the cap | Within about a minute |
| The test customer’s Linked platforms page | Your app’s cost and usage this month | Every few hours |
| Your [User profiles](https://platform.claude.com/user-profiles) page | **Requests** and **Tokens** count the request. **Your spend** doesn’t. | About once an hour, though a request can take a few hours to appear |

When the test works, [publish your app](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/test-and-publish#publish-the-app) so that your customers can link it.

## What to tell your customers

Before real customers link, tell them these things in your product:

* **Who can approve:** A person with the Admin or Billing role in their Claude organization.
* **Which account in your product they’re linking:** Show it beside the button.
* **Which Claude account they’re using:** Ask them to check the account that the approval page displays.
* **That they’re linked:** After the code exchange, say that the customer is linked, not that billing is active. A customer’s organization can link before Anthropic can bill it, for example before it has billing set up.
* **What you bill them for:** Only the Claude usage that they and their users cause in your product. For the full rule, see [What you may bill](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing#what-you-may-bill).

## Rules and special cases

These sections give the rules behind the earlier steps and what to do in particular cases.

### If your federation rule and client authentication expect different audiences

Your back end sends a JWT from your identity provider in two places:

* **To federation, for the Claude API:** The JWT must have your federation rule’s audience. A rule that leaves its audience blank expects `https://api.anthropic.com`.
* **To `auth.claude.com`, as the client assertion:** The JWT must have exactly one audience, your app’s **Expected audience**, from its **Client authentication** tab.

With a rule that leaves its audience blank, the two usually differ, so get a JWT for each audience from your identity provider. The SDK and CLI read the federation JWT from the file that `ANTHROPIC_IDENTITY_TOKEN_FILE` names. The client assertion goes in the file that `CLIENT_ASSERTION_FILE` names.

### If the code exchange times out

A code works once, but a retry after a timeout is safe. If the first try never reached `auth.claude.com`, a retry within the code’s 5 minutes succeeds. If it got through, the retry returns `invalid_grant` and changes nothing. In that case, [check whether the customer is linked](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/manage-customers#check-a-links-status):

* **Not linked:** Start again from the pushed authorization request.
* **Linked:** You don’t have the connection ID or OAuth tokens that the lost response held. If you asked for `billing:attribution` alone, send the customer to approve again with the same scope. That returns the same connection ID and a new access token. If you also asked for `offline_access`, follow [Link a customer again](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/manage-customers#link-a-customer-again).

### If you have a profile for each person

You might already have a user profile for each person who uses your product, and several of them might work for one customer. Only one profile can link each organization, so Anthropic recommends that you create one more profile for the customer’s organization and link that one. Then, the profile ID that you send depends on who pays:

* **Requests that the customer pays for:** Send the ID of the customer’s profile. To also tell Anthropic which person a request comes from, send an opaque ID for the person in `metadata.user_id`, never a name, email address, or phone number. See [Identify one person within a company](https://platform.claude.com/docs/en/manage-claude/user-profiles#identify-individual-users-within-a-company).
* **Requests that you pay for:** You can keep sending the person’s own profile ID.

### If you resell API access

If your organization resells API access, also send `"access_type": "passthrough"` when you create the customer’s profile. The samples leave `access_type` out, which creates an `application` profile. For the two types, see [Decide who gets a profile](https://platform.claude.com/docs/en/manage-claude/user-profiles#decide-who-gets-a-profile).

### If a customer approves again

A customer approves again when you send them to approve for a profile that already has a connection. What the code exchange does depends on the connection’s scopes and the scopes of the new approval:

| The customer approves | What the code exchange does | What you do |
| ----- | ----- | ----- |
| `billing:attribution` again | Returns the same connection ID and a new access token | Store the new access token |
| `billing:attribution offline_access` again | Returns `invalid_grant`, and the connection stays as it was | To get new OAuth tokens, [unlink the customer and have them link again](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/manage-customers#link-a-customer-again) |
| Other scopes, such as `offline_access` added to `billing:attribution` | Ends the earlier connection and its OAuth tokens and makes a new one with a new ID | Store the new connection ID and OAuth tokens |

If the exchange for a change of scopes fails with a 5xx response, the earlier connection might have ended already. Requests that you bill to the customer are refused until a new exchange succeeds. To recover:

1. Send the customer to approve again with the new scopes.
2. If that exchange returns `invalid_grant`, [unlink the customer and have them link again](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/manage-customers#link-a-customer-again).

### For agents

* If the pushed authorization request fails, don’t redirect the browser.
* When you send a request with `bill_to: "user_profile"`, record it in your own logs: no response says who paid.

## Next steps

<CardGroup cols={1}>
  <Card title="What your customers see" icon="browser" href="https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/what-your-customers-see">
    The approval page, spend caps, and emails that your customers see, so that you can support them
  </Card>
</CardGroup>
