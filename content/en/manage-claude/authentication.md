---
title: Authentication
url: https://platform.claude.com/docs/en/manage-claude/authentication
description: Authenticate to the Claude API with API keys, Workload Identity Federation, or App Attest.
---

The Claude API supports three ways to authenticate requests:

| Method                                                                                                                        | Credential                                                                                              | Best for                                                                                                                                        |
| ----------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| [API key](https://platform.claude.com/docs/en/manage-claude/authentication#api-keys)                                          | Static `sk-ant-api...` secret sent as a bearer token in the `Authorization` header                      | Local development, prototyping, scripts, and servers where you control secret storage                                                           |
| [Workload Identity Federation](https://platform.claude.com/docs/en/manage-claude/authentication#workload-identity-federation) | Short-lived bearer token exchanged from your identity provider's identity token                         | Production workloads on cloud platforms (AWS, Google Cloud, Azure), CI/CD pipelines, and Kubernetes, where you want to eliminate static secrets |
| [App Attest](https://platform.claude.com/docs/en/manage-claude/authentication#app-attest)                                     | Short-lived access token issued to a genuine, attested installation of your registered iOS or macOS app | iOS and macOS apps distributed to end users, where the app calls the Claude API directly with no back end or proxy                              |

API keys and Workload Identity Federation grant the same access to Claude API endpoints. Choose API keys to get started quickly: a personal key for your own development, or a service account key for anything shared. Move to Workload Identity Federation when your workload already has a platform-issued identity you can federate. Use App Attest for iOS and macOS apps you distribute to end users.

## API keys

API keys are static secrets that you generate in the Claude Console and send on every request as a bearer token in the `Authorization` header.

### Key types

When you create a key, you choose its type, which determines what the key can do, where it works, and when it stops working:

| Key type                   | Acts as                                                                                                              | Works in                                                                                                                                                                                              | Stops working when                                                                                                                                                                                                                   |
| -------------------------- | -------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Personal key**           | You, the user, with your roles and permissions                                                                       | Either a single workspace or the workspaces where your role allows API use, chosen when the key is created                                                                                            | You lose access to the organization or, for a single-workspace key, to that workspace. Personal keys are archived when you are removed from the organization. If you are re-invited, create new keys; archived keys are not restored |
| **Service account key**    | A [service account](https://platform.claude.com/docs/en/manage-claude/workload-identity-federation#service-accounts) | Either a single workspace or anything the service account has access to, chosen when the key is created. A service account has access to the Default Workspace and to workspaces it has been added to | The service account is archived or, for a single-workspace key, is removed from that workspace                                                                                                                                       |
| **Workspace key** (legacy) | No one: it belongs to the workspace it was created in                                                                | That workspace                                                                                                                                                                                        | It expires, is disabled or deleted, or its workspace is archived, regardless of whether its creator leaves the organization                                                                                                          |

Personal keys and service account keys are identity-backed: each belongs to a user or service account your organization already manages, and every request acts as that identity. When that identity is removed from the organization, the key stops working. This means that keys won't accidentally outlive the people or workloads that own them. Prefer them over workspace keys for new integrations.

Use a personal key for your own development and scripts. A shared personal key acts as one person and breaks when they leave. For shared or automated workloads (CI, production services), have an organization admin create a service account so the workload has its own identity.

Workspace API keys still work but should be considered legacy; identity-backed keys or [Workload Identity Federation](https://platform.claude.com/docs/en/manage-claude/workload-identity-federation) are preferred. To migrate, see [Replacing workspace API keys](https://platform.claude.com/docs/en/manage-claude/authentication#replacing-workspace-api-keys).

### Create and use a key

* **Create a key:** Go to [Settings → API keys](https://platform.claude.com/settings/keys) in the Claude Console and click **Create key**. Name the key and choose an [expiration](https://platform.claude.com/docs/en/manage-claude/authentication#key-expiration). Set **Linked account** to yourself for a personal key, or to a service account for a key shared across multiple users. You can also scope the key to a specific workspace, which lets you skip setting a workspace ID manually in future requests.
* **Use the key:** Send it as `Authorization: Bearer <key>` on direct HTTP requests, or set the `ANTHROPIC_API_KEY` environment variable and the [client SDKs](https://platform.claude.com/docs/en/cli-sdks-libraries/overview) pick it up automatically.

```http
POST /v1/messages
Authorization: Bearer YOUR_API_KEY
anthropic-version: 2023-06-01
content-type: application/json
```

The legacy `x-api-key: YOUR_API_KEY` header is still supported in place of `Authorization`.

Store API keys in a secrets manager, rotate them periodically, and disable or delete any key you suspect has leaked. On the [API keys page](https://platform.claude.com/settings/keys), **Disable** is reversible (the Admin API reports the key's `status` as `"inactive"`, and **Re-enable** returns it to `"active"`), while **Delete** is permanent: the key is archived and still appears in [List API Keys](https://platform.claude.com/docs/en/api/admin/api_keys/list) with `status: "archived"`. Expired keys can only be deleted. You can also set an [expiration](https://platform.claude.com/docs/en/manage-claude/authentication#key-expiration) when you create a key to limit how long a leaked credential stays usable.

<CodeGroup>
  ```bash cURL
  curl https://api.anthropic.com/v1/messages \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "content-type: application/json" \
    -d '{
      "model": "claude-opus-5",
      "max_tokens": 1024,
      "messages": [{"role": "user", "content": "Hello, Claude"}]
    }'
  ```

  ```python Python
  client = Anthropic(api_key="my-anthropic-api-key")
  # or, with ANTHROPIC_API_KEY set in the environment:
  client = Anthropic()
  ```

  ```typescript TypeScript
  const client = new Anthropic({ apiKey: "my-anthropic-api-key" });
  // or, with ANTHROPIC_API_KEY set in the environment:
  // const client = new Anthropic();
  ```

  ```go Go
  client := anthropic.NewClient(
  	option.WithAPIKey("sk-ant-api03-..."), // defaults to os.LookupEnv("ANTHROPIC_API_KEY")
  )
  ```

  ```java Java
  import com.anthropic.client.AnthropicClient;
  import com.anthropic.client.okhttp.AnthropicOkHttpClient;

  // Explicit
  AnthropicClient client = AnthropicOkHttpClient.builder()
    .apiKey("my-anthropic-api-key")
    .build();

  // From ANTHROPIC_API_KEY (or anthropic.apiKey system property)
  AnthropicClient clientFromEnv = AnthropicOkHttpClient.fromEnv();
  ```

  ```csharp C#
  using Anthropic;

  AnthropicClient client = new() { ApiKey = "my-anthropic-api-key" };
  // Or, with ANTHROPIC_API_KEY set in the environment:
  // AnthropicClient client = new();
  ```

  ```php PHP
  // Reads ANTHROPIC_API_KEY from the environment
  $client = new Client();
  // Or pass the key explicitly:
  $client = new Client(apiKey: 'my-anthropic-api-key');
  ```

  ```ruby Ruby
  anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")
  # or, with ANTHROPIC_API_KEY set in the environment:
  anthropic = Anthropic::Client.new
  ```

  ```bash CLI
  # See /docs/en/cli-sdks-libraries/cli/authentication#api-key for zsh, bash, and Windows variants
  export ANTHROPIC_API_KEY=sk-ant-api03-...
  ```
</CodeGroup>

### Select a workspace

API keys that are created for a specific workspace only work in that workspace, and API requests using these keys can omit the workspace ID.

If your API key isn't scoped to a workspace, you must specify the workspace ID in the `anthropic-workspace-id` header for each request. See the following example for how to set this header in a request or in SDKs.

The [Admin API](https://platform.claude.com/docs/en/manage-claude/admin-api) accepts a personal key or service account key only if the key isn't scoped to a specific workspace.

You can find a workspace's ID in the **ID** column of [Settings → Workspaces](https://platform.claude.com/settings/workspaces) in the Claude Console, or by calling the [List Workspaces](https://platform.claude.com/docs/en/api/admin/workspaces/list) endpoint. List Workspaces omits the Default Workspace; its ID is in the `anthropic-workspace-id` [response header](https://platform.claude.com/docs/en/manage-claude/workspaces#identify-the-workspace-behind-an-api-response) of any request that runs there.

<CodeGroup>
  ```bash cURL
  # Required on every request for a multi-workspace key.
  # Omit the anthropic-workspace-id header for a single-workspace key.
  curl https://api.anthropic.com/v1/messages \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-workspace-id: wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ" \
    -H "content-type: application/json" \
    -d '{
      "model": "claude-opus-5",
      "max_tokens": 1024,
      "messages": [{"role": "user", "content": "Hello, Claude"}]
    }'
  ```

  ```bash CLI
  # Required on every command for a multi-workspace key.
  # Omit --workspace-id for a single-workspace key.
  ant messages create \
    --workspace-id wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ \
    --model claude-opus-5 \
    --max-tokens 1024 \
    --message '{role: user, content: "Hello, Claude"}'
  ```

  ```python Python
  client = Anthropic()  # reads ANTHROPIC_API_KEY

  # Required on every request for a multi-workspace key.
  # Omit extra_headers for a single-workspace key.
  message = client.messages.create(
      model="claude-opus-5",
      max_tokens=1024,
      messages=[{"role": "user", "content": "Hello, Claude"}],
      extra_headers={"anthropic-workspace-id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"},
  )
  print(message.content)

  # Or set it once for every request from this client:
  workspace_client = Anthropic(
      default_headers={"anthropic-workspace-id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"},
  )
  ```

  ```typescript TypeScript
  const client = new Anthropic(); // reads ANTHROPIC_API_KEY

  // Required on every request for a multi-workspace key.
  // Omit the second argument for a single-workspace key.
  const message = await client.messages.create(
    {
      model: "claude-opus-5",
      max_tokens: 1024,
      messages: [{ role: "user", content: "Hello, Claude" }]
    },
    { headers: { "anthropic-workspace-id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ" } }
  );
  console.log(message.content);

  // Or set it once for every request from this client:
  const workspaceClient = new Anthropic({
    defaultHeaders: { "anthropic-workspace-id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ" }
  });
  ```

  ```csharp C#
  AnthropicClient client = new(); // reads ANTHROPIC_API_KEY

  MessageCreateParams parameters = new()
  {
      Model = Model.ClaudeOpus5,
      MaxTokens = 1024,
      Messages = [new() { Role = Role.User, Content = "Hello, Claude" }],
  };

  // Required on every request for a multi-workspace key.
  // Call client.Messages.Create(parameters) directly for a single-workspace key.
  var message = await client
      .WithOptions(options =>
          options with
          {
              ExtraHeaders = new Dictionary<string, string>
              {
                  ["anthropic-workspace-id"] = "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
              },
          }
      )
      .Messages.Create(parameters);
  Console.WriteLine(message);

  // Or set it once for every request from this client:
  AnthropicClient workspaceClient = new(new ClientOptions
  {
      ExtraHeaders = new Dictionary<string, string>
      {
          ["anthropic-workspace-id"] = "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
      },
  });
  ```

  ```go Go
  client := anthropic.NewClient() // reads ANTHROPIC_API_KEY

  // Required on every request for a multi-workspace key.
  // Omit the option for a single-workspace key.
  message, err := client.Messages.New(context.TODO(), anthropic.MessageNewParams{
  	Model:     anthropic.ModelClaudeOpus5,
  	MaxTokens: 1024,
  	Messages: []anthropic.MessageParam{
  		anthropic.NewUserMessage(anthropic.NewTextBlock("Hello, Claude")),
  	},
  }, option.WithHeader("anthropic-workspace-id", "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"))
  if err != nil {
  	log.Fatal(err)
  }
  fmt.Println(message.Content)

  // Or set it once for every request from this client:
  workspaceClient := anthropic.NewClient(
  	option.WithHeader("anthropic-workspace-id", "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"),
  )
  ```

  ```java Java
  AnthropicClient client = AnthropicOkHttpClient.fromEnv(); // reads ANTHROPIC_API_KEY

  // Required on every request for a multi-workspace key.
  // Omit putAdditionalHeader for a single-workspace key.
  Message message = client.messages().create(MessageCreateParams.builder()
      .model(Model.CLAUDE_OPUS_5)
      .maxTokens(1024)
      .addUserMessage("Hello, Claude")
      .putAdditionalHeader("anthropic-workspace-id", "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ")
      .build());

  IO.println(message.content());

  // Or set it once for every request from this client:
  AnthropicClient workspaceClient = AnthropicOkHttpClient.builder()
      .fromEnv()
      .putHeader("anthropic-workspace-id", "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ")
      .build();
  ```

  ```php PHP
  $client = new Client(); // reads ANTHROPIC_API_KEY

  // Required on every request for a multi-workspace key.
  // Omit requestOptions for a single-workspace key.
  $message = $client->messages->create(
      model: Model::CLAUDE_OPUS_5,
      maxTokens: 1024,
      messages: [['role' => 'user', 'content' => 'Hello, Claude']],
      requestOptions: [
          'extraHeaders' => ['anthropic-workspace-id' => 'wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ'],
      ],
  );

  echo json_encode($message->content), PHP_EOL;
  ```

  ```ruby Ruby
  client = Anthropic::Client.new # reads ANTHROPIC_API_KEY

  # Required on every request for a multi-workspace key.
  # Omit request_options for a single-workspace key.
  message = client.messages.create(
    model: Anthropic::Model::CLAUDE_OPUS_5,
    max_tokens: 1024,
    messages: [{role: "user", content: "Hello, Claude"}],
    request_options: {extra_headers: {"anthropic-workspace-id" => "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"}}
  )

  puts message.content
  ```
</CodeGroup>

If a request made with a key that isn't scoped to a workspace omits the header, the API returns a 400 `invalid_request_error`:

```json JSON
{
  "type": "error",
  "error": {
    "type": "invalid_request_error",
    "message": "anthropic-workspace-id is required when authenticating with an identity-linked API key; send the id of the workspace this request acts in."
  },
  "request_id": "req_011CSHoEeqs5C35K2UUqR7Fy"
}
```

A header value that isn't a valid workspace ID returns a 400 `invalid_request_error` with the message `anthropic-workspace-id header must be a valid workspace ID.` If the workspace doesn't exist, or the key's user or service account doesn't have access to it, the API returns a 404 `not_found_error` with the message ``Workspace `<id>` not found.``, the same response as for any unknown workspace.

Workload Identity Federation selects a workspace at token exchange instead; see the [WIF reference](https://platform.claude.com/docs/en/manage-claude/wif-reference) for details.

### Key expiration

When you create an API key from the [API keys page](https://platform.claude.com/settings/keys) in the Claude Console, you choose an expiration: a preset (3 hours, 1 day, 7 days, or 30 days), a custom duration, or **Never** for keys you store in a secrets manager and rotate yourself. If your organization has a maximum expiration policy, the Console limits presets and custom durations to the policy maximum, and **Never** is unavailable. Existing keys keep their current behavior; expiration is set at creation time and cannot be changed afterward. The same expiration choice applies when you [create an Admin API key](https://platform.claude.com/docs/en/manage-claude/admin-api-keys) in the Claude Console.

Anthropic emails the key's creator as the expiration approaches: 7 days before expiration for keys created with a lifetime of at least 14 days, and 1 day before for keys with a lifetime of at least 7 days. Keys with shorter lifetimes expire without a warning email.

After a key expires, requests made with it return a `401 authentication_error`. Create a new key to restore access; expired keys cannot be reactivated.

The Console API keys table shows each key's expiration, and the Admin API reports each key's `expires_at` timestamp on the [List API Keys](https://platform.claude.com/docs/en/api/admin/api_keys/list) and [Retrieve API Key](https://platform.claude.com/docs/en/api/admin/api_keys/retrieve) endpoints, so you can audit and rotate keys before they expire. The field is `null` for keys without an expiration.

Expiration limits the lifetime of a leaked credential, but it is not a substitute for secret hygiene. Regardless of expiration, store keys in a secrets manager and disable or delete any key you suspect has leaked.

### Replacing workspace API keys

If you have a workspace key, you may want to replace it with [Workload Identity Federation](https://platform.claude.com/docs/en/manage-claude/wif-reference) or a personal or service account key. This provides better security and observability.

See [Workload Identity Federation](https://platform.claude.com/docs/en/manage-claude/wif-reference) for details on configuring Workload Identity Federation, which is preferred over long-lived keys.

To replace a workspace key with a personal or service account key:

1. **Decide the key type.** Your own tooling should use a personal key. A shared or unattended workload should use a service account key.
2. **Create a service account** if necessary. You may have to ask an organization admin to create one in [Settings → Service accounts](https://platform.claude.com/settings/service-accounts) and add it to the relevant workspace.
3. **Create the new key.** Create it specifically for the integration's workspace unless multiple workspaces are needed.
4. **Deploy the new key.** Replace the old key wherever the integration reads it, typically the `ANTHROPIC_API_KEY` environment variable or a secrets manager entry. For a multi-workspace key, also send the `anthropic-workspace-id` header as shown in [Select a workspace](https://platform.claude.com/docs/en/manage-claude/authentication#select-a-workspace).
5. **Delete the old key.** Confirm that requests succeed, then delete the workspace key on the [API keys page](https://platform.claude.com/settings/keys).

## Workload Identity Federation

Workload Identity Federation (WIF) lets a workload authenticate with a short-lived identity token issued by an identity provider (IdP) you already trust, such as AWS IAM, Google Cloud, or any standards-compliant OIDC issuer (such as GitHub Actions, Kubernetes service accounts, SPIFFE, Microsoft Entra ID, or Okta). The workload exchanges its IdP-issued JWT at `POST /v1/oauth/token` for a short-lived Claude API access token, and the SDK refreshes that token automatically before it expires. There is no `sk-ant-api...` string to mint, distribute, or rotate.

Federation removes long-lived Claude API keys from your environment, which shrinks the blast radius of a leaked credential and lets you manage access with the same IdP controls you already use for cloud resources. It does not, on its own, guarantee end-to-end security: the trust chain is only as strong as your identity provider's configuration, and a long-lived secret one hop upstream (for example, a static cloud credential that can mint IdP tokens) can still undermine it. Pair federation with your provider's controls, such as IP allowlists, MFA, and audit logging.

To configure federation, you create three resources in the Claude Console (a service account, a federation issuer, and a federation rule) and then point your SDK at the rule. See [Workload Identity Federation](https://platform.claude.com/docs/en/manage-claude/workload-identity-federation) for the full setup walkthrough.

## App Attest

App Attest authenticates iOS and macOS apps that call the Claude API directly from the device. Each installation proves that it is a genuine, unmodified build of an app you registered in the Claude Console, using Apple's App Attest service. Anthropic then issues the device a short-lived access token that bills usage to your workspace. Tokens are scoped to your workspace, expire after one hour, and authorize only [Messages API](https://platform.claude.com/docs/en/api/messages/create) calls.

To register your app and get a client ID, see [App Attest for iOS and macOS apps](https://platform.claude.com/docs/en/manage-claude/app-attest).

## Next steps

<CardGroup cols={2}>
  <Card title="Set up Workload Identity Federation" icon="lock" href="https://platform.claude.com/docs/en/manage-claude/workload-identity-federation">
    Configure issuers, rules, and service accounts, then exchange tokens
  </Card>

  <Card title="Identity provider guides" icon="cloud" href="https://platform.claude.com/docs/en/manage-claude/workload-identity-federation#identity-providers">
    Step-by-step guides for AWS, Google Cloud, Azure, GitHub Actions, Kubernetes, SPIFFE, and Okta
  </Card>

  <Card title="WIF reference" icon="book" href="https://platform.claude.com/docs/en/manage-claude/wif-reference">
    Environment variables, validation rules, profile configuration, and error reference
  </Card>

  <Card title="App Attest for iOS and macOS apps" icon="fingerprint" href="https://platform.claude.com/docs/en/manage-claude/app-attest">
    Let genuine installations of your app call the Claude API without shipping an API key
  </Card>

  <Card title="Client SDKs" icon="code" href="https://platform.claude.com/docs/en/cli-sdks-libraries/overview">
    Python, TypeScript, C#, Go, Java, PHP, Ruby, and the CLI
  </Card>
</CardGroup>
