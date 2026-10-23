---
title: User profiles for end-customer attribution
url: https://platform.claude.com/docs/en/manage-claude/user-profiles
description: Attribute API requests to the end customers your platform serves, so a safety enforcement action can apply to one profile instead of your whole organization.
---

User profiles ("profiles") tell Anthropic which of your end customers each API request is for. A safety enforcement action, such as a restriction or a ban, can then apply to one end customer instead of your whole organization. When it does, the rest of your traffic is unaffected.

If you operate a platform or gateway, or resell API access, the requests you send for your end customers arrive under your organization. Anthropic runs automated safety classifiers over API traffic. Without a profile on the request, one end customer can trigger an enforcement action that applies to your whole organization.

You register each end customer once with `POST /v1/user_profiles` and store the `uprof_` ID it returns. Then you send that ID in the `anthropic-user-profile-id` header on every request you make on that end customer's behalf.

Profiles aren't billable and don't affect pricing.

## Decide who gets a profile

What a profile stands for depends on how you sell Claude: a person who uses your product, or a company you resell API access to. These two cases cover most platforms. The profile's `access_type` field says which one applies.

| Who the traffic is for                                       | Profile                                                                                                                                                                                                | `access_type`                                                     |
| ------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------- |
| A signed-up user of your product                             | One for each user, created when they sign up.                                                                                                                                                          | `application` (the default, set when you leave `access_type` out) |
| A company you resell API access to, for example as a gateway | One for each company, not for each person within it.                                                                                                                                                   | `passthrough` (not the default, so you have to send it)           |
| Your own organization                                        | None. Anthropic counts a request with no profile ID as your own usage. Keep that usage in a [separate organization](https://platform.claude.com/docs/en/manage-claude/user-profiles#before-you-begin). | Not applicable                                                    |
| A workspace in your organization                             | No separate profile. A profile belongs to your organization, and its ID works on requests through any workspace in it.                                                                                 | Not applicable                                                    |

## What a profile contains and how Anthropic uses it

A profile contains only what you send about the end customer, plus any [program status](https://platform.claude.com/docs/en/manage-claude/user-profiles-verification-portal#after-the-end-customer-links-the-profile) or enforcement status that Anthropic sets. It doesn't contain conversation content. Anthropic uses the details you send to attribute requests, to monitor for abuse, for enforcement of the [Usage Policy](https://www.anthropic.com/legal/aup), and to enable application and access to trusted access programs. Anthropic doesn't verify the details.

Anthropic processes profiles in accordance with the [Privacy Policy](https://www.anthropic.com/legal/privacy).

## Before you start

You create and manage profiles in one of the following:

* An organization on the Claude API.
* An organization on [Claude Platform on AWS](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws). The calling principal needs the [user profile IAM actions](https://platform.claude.com/docs/en/api/claude-platform-on-aws-iam-actions#user-profiles).
* A [Microsoft Foundry](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry) deployment [hosted on Anthropic](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry#hosting-options), not one hosted on Azure. You don't need an organization on the Claude API or Claude Platform on AWS. Use your Foundry endpoint, with the same base URL and authentication that you use for inference.

Amazon Bedrock and Claude Models on Google Cloud (Google managed) don't have the `/v1/user_profiles` endpoints. If your inference runs there, create your profiles in an organization on the Claude API or Claude Platform on AWS. On Amazon Bedrock, profiles work only with [Claude in Amazon Bedrock](https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock). See [Attribute requests on Amazon Bedrock and Claude Models on Google Cloud (Google managed)](https://platform.claude.com/docs/en/manage-claude/user-profiles#attribute-requests-on-amazon-bedrock-and-google-cloud).

Keep the traffic you send for your end customers in one organization and your own internal usage in another. Profiles belong to an organization, not a workspace, so separate workspaces in one organization aren't enough. Only the organization for end-customer traffic needs user profiles. To create another organization on the Claude API, see the "How to create a new organization" section of [Creating and managing Workspaces in the Claude Console](https://support.claude.com/en/articles/9796807) in the Claude Help Center.

The examples call the Claude API with an API key. You don't need an [Admin API key](https://platform.claude.com/docs/en/manage-claude/admin-api-keys). On Claude Platform on AWS, use its base URL and authentication.

## Create a profile for each end customer

Create one profile for each end customer whose traffic you send to Claude. Create it once, in your customer-onboarding flow. `POST /v1/user_profiles` isn't idempotent, so every call creates a new profile, even when `reference_id` matches an existing one. If you already have end customers without profiles, see the guidance on registering an existing customer base later in this section.

The following example registers a company that buys API access through a gateway, so it sets `access_type` to `passthrough`. For an `application` profile, leave out `access_type`, and describe one end user in `name` and `external_user_details` instead of a company. [Decide who gets a profile](https://platform.claude.com/docs/en/manage-claude/user-profiles#decide-who-gets-a-profile) compares the two access types.

<CodeGroup>
  ```bash cURL
  curl https://api.anthropic.com/v1/user_profiles \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "content-type: application/json" \
    -d '{
      "name": "Acme Analytics, Inc.",
      "access_type": "passthrough",
      "external_user_details": {
        "reference_id": "cust-8f2a1c",
        "country": "US"
      }
    }'
  ```

  ```bash CLI
  ant user-profiles create \
    --name "Acme Analytics, Inc." \
    --access-type passthrough \
    --external-user-details '{reference_id: cust-8f2a1c, country: US}'
  ```

  ```python Python
  client = anthropic.Anthropic()

  profile = client.user_profiles.create(
      name="Acme Analytics, Inc.",
      access_type="passthrough",
      external_user_details={"reference_id": "cust-8f2a1c", "country": "US"},
  )

  print(profile.id)
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const profile = await client.userProfiles.create({
    name: "Acme Analytics, Inc.",
    access_type: "passthrough",
    external_user_details: { reference_id: "cust-8f2a1c", country: "US" }
  });

  console.log(profile.id);
  ```

  ```csharp C#
  AnthropicClient client = new();

  var profile = await client.UserProfiles.Create(new()
  {
      Name = "Acme Analytics, Inc.",
      AccessType = UserProfileAccessType.Passthrough,
      ExternalUserDetails = new()
      {
          ReferenceID = "cust-8f2a1c",
          Country = "US"
      }
  });

  Console.WriteLine(profile.ID);
  ```

  ```go Go
  client := anthropic.NewClient()

  profile, err := client.UserProfiles.New(context.Background(), anthropic.UserProfileNewParams{
  	Name:       anthropic.String("Acme Analytics, Inc."),
  	AccessType: anthropic.UserProfileAccessTypePassthrough,
  	ExternalUserDetails: anthropic.UserProfileExternalUserDetailsParams{
  		ReferenceID: anthropic.String("cust-8f2a1c"),
  		Country:     anthropic.String("US"),
  	},
  })
  if err != nil {
  	log.Fatal(err)
  }

  fmt.Println(profile.ID)
  ```

  ```java Java
  import com.anthropic.models.userprofiles.UserProfileAccessType;
  import com.anthropic.models.userprofiles.UserProfileCreateParams;
  import com.anthropic.models.userprofiles.UserProfileExternalUserDetailsParams;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      var params = UserProfileCreateParams.builder()
          .name("Acme Analytics, Inc.")
          .accessType(UserProfileAccessType.PASSTHROUGH)
          .externalUserDetails(UserProfileExternalUserDetailsParams.builder()
              .referenceId("cust-8f2a1c")
              .country("US")
              .build())
          .build();
      var profile = client.userProfiles().create(params);

      IO.println(profile.id());
  // ...
  }
  ```

  ```php PHP
  $client = new Client();

  $profile = $client->userProfiles->create(
      name: 'Acme Analytics, Inc.',
      accessType: 'passthrough',
      externalUserDetails: ['referenceID' => 'cust-8f2a1c', 'country' => 'US'],
  );

  echo $profile->id, PHP_EOL;
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  profile = client.user_profiles.create(
    name: "Acme Analytics, Inc.",
    access_type: :passthrough,
    external_user_details: { reference_id: "cust-8f2a1c", country: "US" }
  )

  puts profile.id
  ```
</CodeGroup>

The response is the new profile:

```json
{
  "type": "user_profile",
  "id": "uprof_011CZkZCu8hGbp5mYRQgUmz9",
  "name": "Acme Analytics, Inc.",
  "access_type": "passthrough",
  "external_user_details": {
    "reference_id": "cust-8f2a1c",
    "onboarded_at": null,
    "account_status": null,
    "entity_type": null,
    "country": "US",
    "name_hash": null,
    "email_hash": null
  },
  "metadata": {},
  "programs": {
    "cyber": null,
    "efs": null
  },
  "created_at": "2026-03-15T10:00:00Z",
  "updated_at": "2026-03-15T10:00:00Z"
}
```

Store the `id` on your customer record, and have your service instances read it from there instead of creating their own profile. You retrieve, update, and delete a profile by that `id`. The `programs` field is read-only, and attribution doesn't use it. It holds the end customer's status in each program that Anthropic runs. For what its values mean, see [which programs apply to a profile](https://platform.claude.com/docs/en/manage-claude/user-profiles-verification-portal#after-the-end-customer-links-the-profile). [Check whether Anthropic has restricted or banned a profile](https://platform.claude.com/docs/en/manage-claude/user-profiles#check-whether-anthropic-has-restricted-or-banned-a-profile) explains the `enforcement_status` and `enforcement_actions` fields.

There's no cap on the number of profiles in an organization, but profile creation is rate limited. Before you register an existing customer base in bulk, contact your Anthropic account team.

### What to tell Anthropic about an end customer

Every field is optional. You can send `name`, `metadata`, and these fields in `external_user_details`: `entity_type`, `country`, `reference_id`, `onboarded_at`, `account_status`, `name_hash`, and `email_hash`. The [Create a profile](https://platform.claude.com/docs/en/api/user_profiles/create) reference describes each field, with its type, format, and length limit.

Follow these rules when you set the fields:

* **Unknown values:** If you don't know a value, leave it out instead of sending a placeholder. You can replace a value in `external_user_details` later, but you can't clear it.
* **Company names:** For a `passthrough` profile, send the company's legal name in `name` if you know it.
* **Country:** In `country`, send the end customer's country, not yours.
* **Your own ID:** In `reference_id`, send your own stable identifier for the end customer. It doesn't have to be unique.
* **Names and email addresses you can't share:** Leave out `name` and send `external_user_details.name_hash` instead. For the email address, send `external_user_details.email_hash`. A profile has no field for the address itself.
* **Hashes:** Compute the hashes yourself, with a function you choose. They show Anthropic which of your profiles share a name or an email address. Use the same function and the same case and whitespace normalization for every profile, because only values computed the same way match.

## Attribute each request

Send the profile ID in the `anthropic-user-profile-id` header on every request you make on the end customer's behalf. The SDK and the CLI have an argument that sends the header for you: `user_profile_id` (java: `userProfileId`; php: `userProfileID`; csharp, go: `UserProfileID`; cli: `--user-profile-id`).

<CodeGroup>
  ```bash cURL
  curl https://api.anthropic.com/v1/messages \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-user-profile-id: $PROFILE_ID" \
    -H "content-type: application/json" \
    -d '{
      "model": "claude-opus-5-5",
      "max_tokens": 1024,
      "messages": [
        {"role": "user", "content": "Hello, Claude"}
      ]
    }'
  ```

  ```bash CLI
  ant messages create \
    --model claude-opus-5-5 \
    --max-tokens 1024 \
    --message '{role: user, content: "Hello, Claude"}' \
    --user-profile-id "$PROFILE_ID"
  ```

  ```python Python
  client = anthropic.Anthropic()

  message = client.messages.create(
      model="claude-opus-5-5",
      max_tokens=1024,
      messages=[{"role": "user", "content": "Hello, Claude"}],
      user_profile_id=profile_id,
  )

  print(message)
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const message = await client.messages.create({
    model: "claude-opus-5-5",
    max_tokens: 1024,
    messages: [{ role: "user", content: "Hello, Claude" }],
    user_profile_id: profileId
  });

  console.log(message);
  ```

  ```csharp C#
  AnthropicClient client = new();

  var parameters = new MessageCreateParams
  {
      Model = Model.ClaudeOpus5_5,
      MaxTokens = 1024,
      Messages = [new UserMessageParam { Content = "Hello, Claude" }],
      UserProfileID = profileId
  };
  var message = await client.Messages.Create(parameters);

  Console.WriteLine(message);
  ```

  ```go Go
  client := anthropic.NewClient()

  message, err := client.Messages.New(context.Background(), anthropic.MessageNewParams{
  	Model:     anthropic.ModelClaudeOpus5_5,
  	MaxTokens: 1024,
  	Messages: []anthropic.MessageParam{
  		anthropic.NewUserMessage(anthropic.NewTextBlock("Hello, Claude")),
  	},
  	UserProfileID: anthropic.String(profileID),
  })
  if err != nil {
  	log.Fatal(err)
  }

  fmt.Println(message)
  ```

  ```java Java
  import com.anthropic.models.messages.MessageCreateParams;
  import com.anthropic.models.messages.Model;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      var params = MessageCreateParams.builder()
          .model(Model.CLAUDE_OPUS_5_5)
          .maxTokens(1024L)
          .addUserMessage("Hello, Claude")
          .userProfileId(profileId)
          .build();
      var message = client.messages().create(params);

      IO.println(message);
  }
  ```

  ```php PHP
  $client = new Client();

  $message = $client->messages->create(
      maxTokens: 1024,
      messages: [['role' => 'user', 'content' => 'Hello, Claude']],
      model: Model::CLAUDE_OPUS_5_5,
      userProfileID: $profileId,
  );

  echo json_encode($message, JSON_PRETTY_PRINT), PHP_EOL;
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  message = client.messages.create(
    model: Anthropic::Model::CLAUDE_OPUS_5_5,
    max_tokens: 1024,
    messages: [{ role: "user", content: "Hello, Claude" }],
    user_profile_id: profile_id
  )

  puts message
  ```
</CodeGroup>

The header works the same way on [token counting](https://platform.claude.com/docs/en/build-with-claude/token-counting), [Message Batches](https://platform.claude.com/docs/en/build-with-claude/batch-processing), and [OpenAI SDK compatibility](https://platform.claude.com/docs/en/cli-sdks-libraries/libraries/openai-sdk) requests. On a batch, it applies to every request in the batch.

The Claude API, Claude Platform on AWS, and Microsoft Foundry deployments hosted on Anthropic check the ID on every request. If the ID is malformed or doesn't belong to the organization that sends the request, the API returns a `400` `invalid_request_error`. By default, these platforms accept a profile ID only on requests from the organization that created the profile. This means that if you send traffic under more than one organization, for example one on the Claude API and one on Claude Platform on AWS, a request from an organization that didn't create the profile gets the same `400`.

Message Batches is the exception: creating a batch checks only the ID's format. If a well-formed ID doesn't belong to the organization that sends the batch, the batch is still created, and each request in it then fails with an `errored` result that contains the same `invalid_request_error`.

### Attribute requests on Amazon Bedrock and Claude Models on Google Cloud (Google managed)

A profile ID of either access type also works on [Claude in Amazon Bedrock](https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock) and on Claude Models on Google Cloud (Google managed). It doesn't work with the [earlier Amazon Bedrock integration](https://platform.claude.com/docs/en/build-with-claude/claude-on-amazon-bedrock-legacy) that you call with `InvokeModel` or `Converse`. You use your Anthropic organization's credentials only to create and manage profiles. Inference stays on your existing AWS or Google Cloud credentials.

| Platform                                                                                                                                             | Create profiles                                              | Send the profile ID in                      |
| ---------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------- |
| Claude API                                                                                                                                           | Yes                                                          | `anthropic-user-profile-id` header          |
| [Claude Platform on AWS](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws)                                               | Yes                                                          | `anthropic-user-profile-id` header          |
| [Microsoft Foundry](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry), deployments hosted on Anthropic              | Yes                                                          | `anthropic-user-profile-id` header          |
| [Claude Models on Google Cloud (Google managed)](https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/google-managed) | No. Create them on the Claude API or Claude Platform on AWS. | `anthropic-user-profile-id` header          |
| [Claude in Amazon Bedrock](https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock)                                           | No. Create them on the Claude API or Claude Platform on AWS. | `user_profile_id` field in the request body |

On Claude in Amazon Bedrock, put the ID at the top level of the request body:

```json
{
  "model": "anthropic.claude-opus-5-5",
  "max_tokens": 1024,
  "user_profile_id": "uprof_011CZkZCu8hGbp5mYRQgUmz9",
  "messages": [{ "role": "user", "content": "Hello, Claude" }]
}
```

Link each AWS account that sends requests to Claude in Amazon Bedrock, and each Google Cloud project that sends requests to Claude Models on Google Cloud (Google managed), to the Anthropic organization that creates your profiles:

1. An admin or owner of that organization starts the link in the Verification Portal at `portal.anthropic.com`, under **Linked accounts**.
2. Someone who can manage IAM in the AWS account or Google Cloud project runs a command that the portal provides.
3. The admin or owner completes the verification in the portal.

Programs that apply to a profile apply to an account's requests only after the account is linked and the portal shows it as **Linked**. Those programs include the ones an end customer's organization is approved for after the end customer [links the profile to that organization](https://platform.claude.com/docs/en/manage-claude/user-profiles-verification-portal) and, for Cyber Verification Program access levels, turns them on for the profile in the portal.

Claude in Amazon Bedrock and Claude Models on Google Cloud (Google managed) check the format of the ID but don't look the profile up. They reject a malformed ID with a `400`. They accept any well-formed ID, so a successful response doesn't confirm that the ID matches a profile. A request with no ID goes through unattributed, and if it triggers an enforcement action, the action applies to your whole organization.

### Identify individual users within a company

A `passthrough` profile identifies a company, not the person making the request. If a request comes from one identifiable person, also send an identifier for that person in the [`metadata.user_id`](https://platform.claude.com/docs/en/api/messages/create) field of the Messages request. This is the request's own `metadata` object, not the profile's `metadata` field. The identifier is optional, and it helps Anthropic detect misuse by one person.

## Check whether Anthropic has restricted or banned a profile

A profile's `enforcement_status` and `enforcement_actions` fields report the enforcement actions that Anthropic has open on the end customer. An enforcement action is a restriction or a ban. Every response that returns a profile includes both fields: create, retrieve, update, and each profile in a list. Send these requests with no `user-profiles-` value in the `anthropic-beta` header, because `user-profiles-2026-09-04` and earlier values leave the fields out. The following example shows the fields on a retrieved profile, with the other fields left out:

```json
{
  "type": "user_profile",
  "id": "uprof_011CZkZCu8hGbp5mYRQgUmz9",
  "enforcement_status": "restricted",
  "enforcement_actions": [
    {
      "type": "restriction",
      "id": "enac_011CZkZEq4TnWb7xLfRgPm2v",
      "reason": "fraud_or_abuse",
      "action": null,
      "opened_at": "2026-10-02T19:30:00Z",
      "expires_at": null
    }
  ]
}
```

`enforcement_status` summarizes the open actions in one value:

* `unrestricted`: No action is open.
* `restricted`: At least one action is open and none of them is a ban.
* `banned`: A ban is open.

While an action is open, Anthropic refuses some or all inference requests that carry the profile's ID.

`enforcement_actions` lists the open actions and is empty when there are none. An action that ends leaves the list. Each action has these fields:

* `type`: `restriction` or `ban`.
* `id`: The action's ID, which starts with `enac_`.
* `reason`: Why Anthropic opened the action. It's one of `unsupported_region`, `fraud_or_abuse`, `high_harm`, `usage_policy_violation`, `account_compromise`, or `unspecified`.
* `action`: What the end customer can do to clear the action, or `null` when there's nothing they can do.
* `opened_at`: When Anthropic opened the action.
* `expires_at`: When the action ends by itself, or `null` when it has no end date.

To check a profile, retrieve it with [`GET /v1/user_profiles/{id}`](https://platform.claude.com/docs/en/api/user_profiles/retrieve). To find the profiles that have an open action, [list your profiles](https://platform.claude.com/docs/en/api/user_profiles/list) with `enforcement_status[]=restricted` and `enforcement_status[]=banned`. To get an event when an action opens or ends, see [Organization webhooks](https://platform.claude.com/docs/en/manage-claude/organization-webhooks). Without events, compare both fields with the values you last saw. A change doesn't reliably move `updated_at`.

Anthropic sets both fields. If a create or update request includes either one, the API returns a `400`. `enforcement_status` is separate from `external_user_details.account_status`, which records your own decision about the account.

Anthropic can add values. Treat an `enforcement_status` you don't recognize as `restricted`, a `type` you don't recognize as `restriction`, a `reason` you don't recognize as `unspecified`, and an `action` you don't recognize as `null`.

On Claude Platform on AWS, the two fields don't report enforcement actions: `enforcement_status` is always `unrestricted`, and `enforcement_actions` is always empty. Anthropic doesn't refuse requests there because of an open action.

## Keep profiles current

Update a profile when the end customer's details or account status change, and delete it when they close their account or ask you to erase their data.

### Update a profile

[`POST /v1/user_profiles/{id}`](https://platform.claude.com/docs/en/api/user_profiles/update) changes only the fields you send. For example, use it when a company rebrands or you suspend an account.

* `name` and `access_type` replace the stored value.
* Each field you send in `external_user_details` replaces the stored value. You can't clear a value. The API rejects `null` with a `400`.
* `metadata` merges key by key. A key you send overwrites the stored value, an empty string deletes the key, and keys you leave out stay as they are.

The following example marks the account as suspended and deletes a `trial_cohort` metadata key.

<CodeGroup>
  ```bash cURL
  curl "https://api.anthropic.com/v1/user_profiles/$PROFILE_ID" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "content-type: application/json" \
    -d '{
      "external_user_details": {"account_status": "suspended"},
      "metadata": {"trial_cohort": ""}
    }'
  ```

  ```bash CLI
  ant user-profiles update \
    --user-profile-id "$PROFILE_ID" \
    --external-user-details '{account_status: suspended}' \
    --metadata '{trial_cohort: ""}'
  ```

  ```python Python
  client = anthropic.Anthropic()

  profile = client.user_profiles.update(
      profile_id,
      external_user_details={"account_status": "suspended"},
      metadata={"trial_cohort": ""},
  )

  print(profile)
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const profile = await client.userProfiles.update(profileId, {
    external_user_details: { account_status: "suspended" },
    metadata: { trial_cohort: "" }
  });

  console.log(profile);
  ```

  ```csharp C#
  AnthropicClient client = new();

  var profile = await client.UserProfiles.Update(profileId, new()
  {
      ExternalUserDetails = new()
      {
          AccountStatus = UserProfileExternalUserAccountStatus.Suspended
      },
      Metadata = new Dictionary<string, string> { ["trial_cohort"] = "" }
  });

  Console.WriteLine(profile);
  ```

  ```go Go
  client := anthropic.NewClient()

  profile, err := client.UserProfiles.Update(
  	context.Background(),
  	profileID,
  	anthropic.UserProfileUpdateParams{
  		ExternalUserDetails: anthropic.UserProfileExternalUserDetailsParams{
  			AccountStatus: anthropic.UserProfileExternalUserAccountStatusSuspended,
  		},
  		Metadata: map[string]string{"trial_cohort": ""},
  	},
  )
  if err != nil {
  	log.Fatal(err)
  }

  fmt.Println(profile)
  ```

  ```java Java
  import com.anthropic.core.JsonValue;
  import com.anthropic.models.userprofiles.UserProfileExternalUserAccountStatus;
  import com.anthropic.models.userprofiles.UserProfileExternalUserDetailsParams;
  import com.anthropic.models.userprofiles.UserProfileUpdateParams;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      var params = UserProfileUpdateParams.builder()
          .userProfileId(profileId)
          .externalUserDetails(UserProfileExternalUserDetailsParams.builder()
              .accountStatus(UserProfileExternalUserAccountStatus.SUSPENDED)
              .build())
          .metadata(UserProfileUpdateParams.Metadata.builder()
              .putAdditionalProperty("trial_cohort", JsonValue.from(""))
              .build())
          .build();
      var profile = client.userProfiles().update(params);

      IO.println(profile);
  }
  ```

  ```php PHP
  $client = new Client();

  $profile = $client->userProfiles->update(
      $profileId,
      externalUserDetails: ['accountStatus' => 'suspended'],
      metadata: ['trial_cohort' => ''],
  );

  echo json_encode($profile, JSON_PRETTY_PRINT), PHP_EOL;
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  profile = client.user_profiles.update(
    profile_id,
    external_user_details: { account_status: :suspended },
    metadata: { trial_cohort: "" }
  )

  puts profile
  ```
</CodeGroup>

### Delete a profile

[`DELETE /v1/user_profiles/{id}`](https://platform.claude.com/docs/en/api/user_profiles/delete) permanently deletes a profile and everything you supplied for it, including `name`, `external_user_details`, and `metadata`. It doesn't remove the trust and safety records that Anthropic keeps about that profile ID.

Delete a profile when an end customer closes their account or asks you to erase their data. Before you delete a profile, stop sending its ID on that end customer's requests. If the end customer stays with you after an erasure request, create a new profile and switch to its ID. Then delete the old one.

<CodeGroup>
  ```bash cURL
  curl -X DELETE "https://api.anthropic.com/v1/user_profiles/$PROFILE_ID" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01"
  ```

  ```bash CLI
  ant user-profiles delete --user-profile-id "$PROFILE_ID"
  ```

  ```python Python
  client = anthropic.Anthropic()

  deleted = client.user_profiles.delete(profile_id)

  print(deleted.id)
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const deleted = await client.userProfiles.delete(profileId);

  console.log(deleted.id);
  ```

  ```csharp C#
  AnthropicClient client = new();

  var deleted = await client.UserProfiles.Delete(profileId);

  Console.WriteLine(deleted.ID);
  ```

  ```go Go
  client := anthropic.NewClient()

  deleted, err := client.UserProfiles.Delete(
  	context.Background(),
  	profileID,
  	anthropic.UserProfileDeleteParams{},
  )
  if err != nil {
  	log.Fatal(err)
  }

  fmt.Println(deleted.ID)
  ```

  ```java Java
  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      var deleted = client.userProfiles().delete(profileId);

      IO.println(deleted.id());
  }
  ```

  ```php PHP
  $client = new Client();

  $deleted = $client->userProfiles->delete($profileId);

  echo $deleted->id, PHP_EOL;
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  deleted = client.user_profiles.delete(profile_id)

  puts deleted.id
  ```
</CodeGroup>

The response repeats the ID with `"type": "user_profile_deleted"`. If a delete returns a server error, retry it. A `404` on the retry means the first delete went through.

After a delete, the profile endpoints return a `404` for that ID. For up to about 10 minutes, inference requests that carry the deleted ID can still succeed. After that, the platforms that check the ID on every request reject the request with a `400`. Claude in Amazon Bedrock and Claude Models on Google Cloud (Google managed) don't look profiles up, so they still accept it.

## Next steps

The API reference has each endpoint's fields, types, and limits: [Create a profile](https://platform.claude.com/docs/en/api/user_profiles/create), [Retrieve a profile](https://platform.claude.com/docs/en/api/user_profiles/retrieve), [Update a profile](https://platform.claude.com/docs/en/api/user_profiles/update), [Delete a profile](https://platform.claude.com/docs/en/api/user_profiles/delete), and [List profiles](https://platform.claude.com/docs/en/api/user_profiles/list).

If an end customer's program approvals should apply when they use Claude through your platform, see [Send an end customer a link to the Verification Portal](https://platform.claude.com/docs/en/manage-claude/user-profiles-verification-portal).

To get an event when Anthropic restricts or bans one of your end customers, or when the restriction or ban ends, see [Organization webhooks](https://platform.claude.com/docs/en/manage-claude/organization-webhooks).

<CardGroup cols={2}>
  <Card title="Authentication" href="https://platform.claude.com/docs/en/manage-claude/authentication">
    Choose how your services authenticate to the Claude API.
  </Card>

  <Card title="Usage and Cost API" href="https://platform.claude.com/docs/en/manage-claude/usage-cost-api">
    Track API token usage and costs for your organization.
  </Card>

  <Card title="Data residency" href="https://platform.claude.com/docs/en/manage-claude/data-residency">
    Manage where model inference runs and where data is stored.
  </Card>

  <Card title="Compliance API" href="https://platform.claude.com/docs/en/manage-claude/compliance-api">
    Audit activity across your organization.
  </Card>
</CardGroup>
