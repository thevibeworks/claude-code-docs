---
title: Migrating to API version 2026-10-21
url: https://platform.claude.com/docs/en/api/migration-2026-10-21
description: "Upgrade a Claude API integration from API version 2023-06-01 to 2026-10-21: the SDK version to install and the code changes to make."
---

This guide lists the code changes for moving from API version `2023-06-01` to `2026-10-21`. The [upgrade steps](https://platform.claude.com/docs/en/api/migration-2026-10-21#migration-checklist) say what to do, in order.

## Upgrade steps

<Steps>
  <Step title="Switch to 2026-10-21">
    If you use an SDK, your requests use the API version that was current when your SDK's major version was released. The versions shown for your language are the first to use `2026-10-21`, so upgrade to them. If you call the API without an SDK, set the `anthropic-version` header to `2026-10-21`.

    <Tabs>
      <Tab title="cURL">
        Set the `anthropic-version` header to `2026-10-21`:

        ```bash
        curl https://api.anthropic.com/v1/messages \
          -H "x-api-key: $ANTHROPIC_API_KEY" \
          -H "anthropic-version: 2026-10-21" \
          -H "content-type: application/json" \
          -d '{
            "model": "claude-opus-5-5",
            "max_tokens": 1024,
            "messages": [{"role": "user", "content": "Hello, Claude"}]
          }'
        ```
      </Tab>

      <Tab title="CLI">
        Upgrade the `ant` CLI to version 2.0.0. The Homebrew command and the release downloads stay the same.

        Go requires the path of a module at major version 2 or later to end in that version, so the CLI's module path is now `github.com/anthropics/anthropic-cli/v2`. If you install with `go install`, add `/v2` to the path:

        ```bash
        # Before
        go install 'github.com/anthropics/anthropic-cli/cmd/ant@latest'

        # After
        go install 'github.com/anthropics/anthropic-cli/v2/cmd/ant@latest'
        ```

        The old path keeps installing the latest v1 release, with no error or warning.
      </Tab>

      <Tab title="Python">
        Upgrade the `anthropic` package to version 2.0.0.
      </Tab>

      <Tab title="TypeScript">
        Upgrade the `@anthropic-ai/sdk` package to version 1.0.0.

        v1 of `@anthropic-ai/bedrock-sdk`, `@anthropic-ai/vertex-sdk`, `@anthropic-ai/foundry-sdk`, `@anthropic-ai/aws-sdk`, and `@anthropic-ai/google-cloud-sdk` needs v1 of `@anthropic-ai/sdk`, and their earlier versions need a version below 1. If you use one of them, move it to v1 in the same upgrade. Otherwise your package manager installs a second, older copy of `@anthropic-ai/sdk` for it.
      </Tab>

      <Tab title="C#">
        Upgrade the `Anthropic` package to version 13.0.0.
      </Tab>

      <Tab title="Go">
        Upgrade to version 2.0.0 of the Go SDK, whose module path is `github.com/anthropics/anthropic-sdk-go/v2`. A new major version of a Go module has a new import path, so change each import of `github.com/anthropics/anthropic-sdk-go`, and of its packages such as `github.com/anthropics/anthropic-sdk-go/option`, to start with `github.com/anthropics/anthropic-sdk-go/v2`. Then run `go get github.com/anthropics/anthropic-sdk-go/v2`.
      </Tab>

      <Tab title="Java">
        Upgrade the `com.anthropic:anthropic-java` artifact to version 3.0.0.
      </Tab>

      <Tab title="PHP">
        Run `composer require "anthropic-ai/sdk"` to upgrade the package to version 1.0.0. `composer update` alone stays within your current version constraint.
      </Tab>

      <Tab title="Ruby">
        Upgrade the `anthropic` gem to version 2.0.0.
      </Tab>
    </Tabs>

    <Warning>
      On Amazon Bedrock, `2026-10-21` is available only for Claude 4.7 and later models. If you call an older model on Bedrock, listed in [Claude on Amazon Bedrock (Opus 4.6 and earlier)](https://platform.claude.com/docs/en/build-with-claude/claude-on-amazon-bedrock-legacy), stay on the SDK version you use today, or, if you set the API version yourself, keep sending the version you send today. To move those calls to `2026-10-21`, first switch them to a Claude 4.7 or later model.
    </Warning>

    Release the upgrade together with your fixes from the next step.
  </Step>

  <Step title="Update your code for the breaking changes">
    Go through the [breaking changes](https://platform.claude.com/docs/en/api/migration-2026-10-21#breaking-changes), and update your code for each one that affects you. Also make the [code changes that the new SDK or CLI version needs](https://platform.claude.com/docs/en/api/migration-2026-10-21#sdk-changes).
  </Step>

  <Step title="Test against 2026-10-21">
    Test your integration against `2026-10-21` before you release.
  </Step>
</Steps>

## Breaking changes

### Messages API

These changes apply to requests to the Messages API (`POST /v1/messages`), to [token counting](https://platform.claude.com/docs/en/build-with-claude/token-counting), and to each request in a [Message Batch](https://platform.claude.com/docs/en/build-with-claude/batch-processing) created with `2026-10-21`.

#### Document blocks in assistant messages return an error

Affects you if you send `document` blocks directly in `assistant` messages.

In `2026-10-21`, a request that places a `document` block directly in an `assistant` message returns a 400 error. Send documents in `user` messages instead. A document nested inside another block, such as a web fetch tool result that Claude returned, is still accepted.

#### Citations in user messages return an error

Affects you if you send `citations` on `text` blocks in `user` messages, including inside `search_result` blocks.

In `2026-10-21`, a request that sends a `text` block with a non-empty `citations` array in a `user` message returns a 400 error. Remove `citations` from those blocks. Citations on `text` blocks in `assistant` messages, such as Claude's earlier replies that you send back, are still accepted, and so is the `"citations": {"enabled": true}` setting on documents and search results.

#### Sampling parameters are removed

Affects you if you send `temperature`, `top_p`, or `top_k` in Messages requests or Message Batch requests.

In `2026-10-21`, a request that sends `temperature`, `top_p`, or `top_k` returns a 400 error, even at the parameter's default value.

Remove the three parameters from your requests.

As of the latest major versions, the SDK and the CLI no longer have the three parameters.

Without these parameters, a request samples with their defaults, including a `temperature` of 1.0, the same as a `2023-06-01` request that leaves them out. Models that already accept only the defaults, such as Claude 4.7 and later models, sample as before. On models that accept other values, such as Claude Sonnet 4.6, a request that lowered `temperature` for more consistent output loses that effect. No other setting replaces it. If a request relies on a non-default value, either stop sending the parameter, or keep that request on `2023-06-01`.

### Admin API and Claude Enterprise Analytics API

Affects you if your code reads the Admin API or Claude Enterprise Analytics API response fields in the following tables.

In `2026-10-21`, responses from the Admin API and the [Claude Enterprise Analytics API](https://platform.claude.com/docs/en/manage-claude/analytics-api) no longer include the old names of renamed fields. Use the new names instead.

Admin API:

| Endpoints                                                                                                                                                                                                                                                        | Old name       | New name                                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| [RBAC groups](https://platform.claude.com/docs/en/api/beta/organization/rbac_groups/list): create, list, retrieve, and update                                                                                                                                    | `roles`        | `role_ids`                                                                                                                                      |
| [RBAC group members](https://platform.claude.com/docs/en/api/beta/organization/rbac_groups/members/list): list and add, and the response to [removing a member](https://platform.claude.com/docs/en/api/beta/organization/rbac_groups/members/remove)            | `group_id`     | `rbac_group_id`                                                                                                                                 |
| [RBAC roles](https://platform.claude.com/docs/en/api/beta/organization/rbac_roles/list): list and retrieve                                                                                                                                                       | `name`         | `display_name`                                                                                                                                  |
| [Organization](https://platform.claude.com/docs/en/api/organization/rate_limits/list) and [workspace](https://platform.claude.com/docs/en/api/organization/workspaces/rate_limits/list) rate limits: list, and the response to setting a workspace's rate limits | `group_type`   | `group.type`                                                                                                                                    |
| [API keys](https://platform.claude.com/docs/en/api/organization/api_keys/list): list, retrieve, and update                                                                                                                                                       | `workspace_id` | `scope` (different values; see [`workspace_id` on API keys](https://platform.claude.com/docs/en/api/migration-2026-10-21#api-key-workspace-id)) |

Claude Enterprise Analytics API:

| Endpoints                                                                                                                                                                                                                  | Old name      | New name              |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- | --------------------- |
| Per-user [usage](https://platform.claude.com/docs/en/api/beta/organization/analytics/user_usage_report/list) and [cost](https://platform.claude.com/docs/en/api/beta/organization/analytics/user_cost_report/list) reports | `actor.email` | `actor.email_address` |
| [Activity summaries](https://platform.claude.com/docs/en/api/beta/organization/analytics/summaries/list)                                                                                                                   | `summaries`   | `data`                |

The `group_type` query parameter on the rate-limit list endpoints and the `workspace_id` filter on the API key list endpoint are unchanged.

#### `workspace_id` on API keys

Affects you if your code reads `workspace_id` on API keys.

In `2023-06-01`, an API key's `workspace_id` is the ID of the workspace the key is bound to, or `null` for a key bound to the Default Workspace and for a key that isn't bound to one workspace (an all-workspaces key).

In `2026-10-21`, `workspace_id` is removed. Read `scope` instead: for a key bound to a workspace, including the Default Workspace, `scope.workspace_id` is that workspace's real ID, and an all-workspaces key has a `scope` of `{"type": "organization"}`, with no `workspace_id`.

If your code treated a `null` `workspace_id` as the Default Workspace, compare `scope.workspace_id` with your Default Workspace's ID instead. To find that ID, call [List Workspaces](https://platform.claude.com/docs/en/api/organization/workspaces/list) with `include_default=true` and take the workspace named `"Default"`.

## SDK and CLI changes

Earlier SDK and CLI versions sent `anthropic-version: 2023-06-01` with every request. The versions under [Switch to 2026-10-21](https://platform.claude.com/docs/en/api/migration-2026-10-21#upgrade) send `2026-10-21`, including their Amazon Bedrock and Google Cloud clients. The changes in [Breaking changes](https://platform.claude.com/docs/en/api/migration-2026-10-21#breaking-changes) apply to them too: the removed parameters and the old field names are also gone from the SDK's types and from the CLI's flags and output.

### `MessageParam` is a union with one type per role

In earlier versions, `MessageParam` was one type for every role. Each role now has a type of its own: `UserMessageParam`, `AssistantMessageParam`, and `SystemMessageParam`. `BetaMessageParam` is split the same way, into `BetaUserMessageParam`, `BetaAssistantMessageParam`, and `BetaSystemMessageParam`. The requests that the SDK sends have the same fields and values as before.

<Tabs exclude="shell">
  <Tab title="Python">
    A message written as a dict literal, such as `{"role": "user", "content": "Hello"}`, needs no change.

    In v1, `anthropic.types.MessageParam` was one `TypedDict`. In v2 it is a union of the three types, and `anthropic.types.beta.BetaMessageParam` is a union of its three. Both names still work in annotations, such as `list[MessageParam]`.

    Calling either name now raises a `TypeError`, and a type checker flags it. Write the message as a dict:

    ```python
    # Before
    message = MessageParam(role="user", content="Hello")

    # After
    message: MessageParam = {"role": "user", "content": "Hello"}
    ```

    Subclassing either name also raises a `TypeError`. Subclass the type for the role, such as `UserMessageParam`.

    The remaining changes affect type checking only. A dict whose `role` is a variable that can hold more than one role matches no type in the union, so build the dict for one role at a time:

    ```python
    # Before
    def to_message(role: Literal["user", "assistant"], text: str) -> MessageParam:
        return {"role": role, "content": text}


    # After
    def to_message(role: Literal["user", "assistant"], text: str) -> MessageParam:
        if role == "user":
            return {"role": "user", "content": text}
        return {"role": "assistant", "content": text}
    ```

    Two more apply to `BetaMessageParam` only:

    * `clear_at` and `output_config` are keys of `BetaSystemMessageParam`, so a user or assistant message can't have them.
    * `content` is optional in `BetaSystemMessageParam`, so pyright reports `message["content"]`. Read it with `message.get("content")`, or check first that `message["role"]` is not `"system"`.
  </Tab>

  <Tab title="TypeScript">
    `MessageParam` was one interface. It is now `UserMessageParam | AssistantMessageParam | SystemMessageParam`, and `BetaMessageParam` is the same union of its three types. Only the types changed. A message literal that names its role, such as `{ role: "user", content: "Hello, Claude" }`, type-checks as it did, so most code needs no change.

    The system type differs from the other two. Its `content` is a string or text blocks, plus `tool_addition` and `tool_removal` blocks in `beta`, so an image block there no longer compiles. In `beta`, only it has `clear_at` and `output_config`, and its `content` is optional.

    Code that handles a message of any role has to check `role` before it replaces or adds content blocks, and before it reads `clear_at` or `output_config`:

    ```typescript
    // Before
    const copy: Anthropic.MessageParam = { ...message, content: blocks };

    // After
    const copy: Anthropic.MessageParam =
      message.role === "system" ? message : { ...message, content: blocks };
    ```

    The `content` of a `BetaMessageParam` can be `undefined`:

    ```typescript
    // Before
    const types =
      typeof message.content === "string" ? [] : message.content.map((block) => block.type);

    // After
    const types = Array.isArray(message.content) ? message.content.map((block) => block.type) : [];
    ```

    The type `BetaMessageParam["content"]` includes `undefined` too. For the content of a user or assistant message, use `BetaMessageContentParam`.

    An interface can't extend a union, and a class can't implement one. Use a type alias, or name the type of one role instead.

    ```typescript
    // Before
    interface StoredMessage extends Anthropic.MessageParam {
      id: string;
    }

    // After
    type StoredMessage = Anthropic.MessageParam & { id: string };
    ```
  </Tab>

  <Tab title="C#">
    In v12, `MessageParam` and `BetaMessageParam` were classes whose `Role` and `Content` you set. In v13 each is a union of the three classes for its roles, and the `Role` enums in `Anthropic.Models.Messages` and `Anthropic.Models.Beta.Messages` are gone.

    When you build a message, name the class for its role and delete `Role`. Each class converts to the union implicitly:

    ```csharp
    // Before
    Messages = [new() { Role = Role.User, Content = "Hello, Claude" }],

    // After
    Messages = [new UserMessageParam { Content = "Hello, Claude" }],
    ```

    `new UserMessageParam("Hello, Claude")` works too.

    The classes that hold `Content` change as well:

    * `MessageParamContent` is now `MessageContentParam`, and `BetaMessageParamContent` is now `BetaMessageContentParam`.
    * A system message has a content class of its own. A `SystemMessageParamContent` holds a string or a list of `TextBlockParam`, and a `BetaSystemMessageParamContent` holds a string or a list of `SystemMessageContentBlock`. A `List<ContentBlockParam>` or a `List<BetaContentBlockParam>` no longer converts to it.
    * `ClearAt` and `OutputConfig` are on `BetaSystemMessageParam` only.

    When you read a message, the union still has `Role` and `Content`, but you can't set them, so a `with` expression goes on the class for the role. `Role` now holds a `MessageParamRole` or a `BetaMessageParamRole`. `BetaMessageParam.Content` can be `null`, because `Content` is optional on `BetaSystemMessageParam`.

    ```csharp
    // Before
    if (message.Role.Value() == Role.Assistant) { }

    // After
    if (message.Role.Value() == MessageParamRole.Assistant) { }
    ```

    `TryPickUser`, `TryPickAssistant`, `TryPickSystem`, `Switch`, and `Match` give you the class for the role.
  </Tab>

  <Tab title="Go">
    In v1, `MessageParam` was one struct with a `Role` and a `Content` field. In v2 it is a union: `OfUser` holds a `*UserMessageParam`, `OfAssistant` an `*AssistantMessageParam`, and `OfSystem` a `*SystemMessageParam`. `BetaMessageParam` changes in the same way. The SDK sends the same JSON as before, apart from the order of the keys in a beta system message.

    `NewUserMessage`, `NewAssistantMessage`, `NewBetaUserMessage`, and the `ToParam` methods of `Message` and `BetaMessage` work as before, so code that builds its messages with them needs no change.

    A struct literal names the type for its role. Leave `Role` out, because each type marshals its own:

    ```go
    // Before
    anthropic.MessageParam{
    	Role:    anthropic.MessageParamRoleAssistant,
    	Content: blocks,
    }

    // After
    anthropic.MessageParam{OfAssistant: &anthropic.AssistantMessageParam{
    	Content: blocks,
    }}
    ```

    Code that reads a message checks which field is set:

    ```go
    // Before
    if message.Role == anthropic.MessageParamRoleUser {
    	blocks = message.Content
    }

    // After
    if message.OfUser != nil {
    	blocks = message.OfUser.Content
    }
    ```

    * The `MessageParamRole` and `BetaMessageParamRole` types and their constants are gone. `message.GetRole()` returns a pointer to the role as a `string`, or `nil` when no field is set.
    * `ClearAt` and `OutputConfig` moved from `BetaMessageParam` to `BetaSystemMessageParam`. The names of the `BetaMessageParamClearAt` type and its constants now start with `BetaSystemMessageParamClearAt`.
    * `SystemMessageParam.Content` is a `[]TextBlockParam`. `BetaSystemMessageParam.Content` is a `[]BetaSystemMessageParamContentUnion`, which holds `text`, `tool_addition`, and `tool_removal` blocks. `NewBetaSystemMessage` takes blocks of that type, so `anthropic.NewBetaTextBlock("Be brief.")` becomes `anthropic.BetaSystemMessageParamContentUnion{OfText: &anthropic.BetaTextBlockParam{Text: "Be brief."}}`.
    * A copy of a `MessageParam` points to the same message as the original. Setting `duplicate.OfUser.Content` changes both, where setting `duplicate.Content` in v1 changed only the copy.
    * `mcp.ToMessage` returns an `*mcp.UnsupportedValueError` for a role other than `user` or `assistant`. v1 copied any role into the message.
  </Tab>

  <Tab title="Java">
    In v2, `MessageParam` was a single class with a `role` and a `content`. In v3 it is a union of the three classes, and `MessageParam.Content` is now the top-level `MessageContentParam`. `BetaMessageParam` changes the same way, and its classes have the same names with a `Beta` prefix. The JSON that the SDK sends is the same, except that a beta system message now has `role` before `content`.

    `addUserMessage`, `addAssistantMessage`, and `addSystemMessage` with a `String`, `addMessage` with a `Message` or a `MessageParam`, and `Message.toParam()` don't change.

    `MessageParam.builder()` and `toBuilder()` are gone. Call the factory method for the role, which is `ofUser`, `ofAssistant`, or `ofSystem`:

    ```java
    // Before
    MessageParam message = MessageParam.builder()
        .role(MessageParam.Role.USER)
        .content("Hello, Claude")
        .build();

    // After
    MessageParam message = MessageParam.ofUser("Hello, Claude");
    ```

    The methods that take a list of content blocks have new names on the builders of `MessageCreateParams`, `StructuredMessageCreateParams`, `MessageCountTokensParams`, and `BatchCreateParams.Request.Params`:

    | v2                                 | v2 beta                                       | v3                                        |
    | ---------------------------------- | --------------------------------------------- | ----------------------------------------- |
    | `addUserMessageOfBlockParams`      | `addUserMessageOfBetaContentBlockParams`      | `addUserMessageOfContentBlockParams`      |
    | `addAssistantMessageOfBlockParams` | `addAssistantMessageOfBetaContentBlockParams` | `addAssistantMessageOfContentBlockParams` |
    | `addSystemMessageOfBlockParams`    | `addSystemMessageOfBetaContentBlockParams`    | `addSystemMessageOfBlocks`                |

    On the content class, `BlockParams` (`BetaContentBlockParams` in beta) becomes `ContentBlockParams` in `ofBlockParams`, `blockParams()`, `isBlockParams()`, `asBlockParams()`, and the visitor's `visitBlockParams`.

    A system message has its own content class, `SystemMessageParam.Content`, which `addSystemMessage` now takes. Its blocks are `TextBlockParam`, not `ContentBlockParam`. In beta they are `BetaSystemMessageParam.Content.SystemMessageContentBlock`, which has `ofText`, `ofToolAddition`, and `ofToolRemoval`.

    ```java
    // Before
    builder.addSystemMessageOfBlockParams(List.of(ContentBlockParam.ofText(textBlock)));

    // After
    builder.addSystemMessageOfBlocks(List.of(textBlock));
    ```

    When you read a message, `role()` doesn't change. `content()` returns a `MessageContentParam`, or an `Optional<BetaMessageContentParam>` in beta, where a system message can have no content. `_role()`, `_content()`, and `_additionalProperties()` are now on the class for the role, which `asUser()`, `asAssistant()`, or `asSystem()` returns.
  </Tab>

  <Tab title="PHP">
    The classes are in `Anthropic\Messages`, and the beta classes in `Anthropic\Beta\Messages`. Messages you write as arrays don't change, and still need their `'role'`.

    `MessageParam::with()` and `BetaMessageParam::with()` remain, and return the class that goes with `role`. A call with named arguments needs no change. `role` is now the first parameter, so in a positional call swap `content` and `role`, or call `with()` on the role's class, which takes no `role`. For arguments in the old order PHP throws `UnhandledMatchError`, which PHPStan does not warn about, or a `TypeError` if `content` is a list or `role` is an enum case.

    ```php
    // Before
    MessageParam::with('Hello, Claude', 'user');

    // After
    UserMessageParam::with('Hello, Claude');
    ```

    No object is a `MessageParam` any more: `instanceof MessageParam` is false, and PHP throws a `TypeError` where a parameter or return type names it. Name the three classes instead:

    ```php
    // Before
    function send(MessageParam $message): void {}

    // After
    function send(UserMessageParam|AssistantMessageParam|SystemMessageParam $message): void {}
    ```

    * `MessageParam::fromArray()` and `(new MessageParam)->withContent()` throw "Call to undefined method". Call them on the role's class, which sets `role` itself.
    * `withRole()` takes only the string now: PHP throws a `TypeError` for a `Role` case. To give a message another role, build that role's class.
    * `clearAt` and `outputConfig` exist only on `BetaSystemMessageParam`, and `BetaMessageParam::with()` drops them for the other two roles. The `BetaMessageParam\ClearAt` enum is now `BetaSystemMessageParam\ClearAt`.
    * `MessageParam\Content` is now `MessageContentParam`, and `BetaMessageParam\Content` is now `BetaMessageContentParam`. Their PHPStan types take the new name too: `ContentShape` is now `MessageContentParamShape`.
    * An array whose `'role'` is a `Role` case still works, but PHPStan now reports it. Write the string.
  </Tab>

  <Tab title="Ruby">
    Messages you write as hashes don't change.

    In v2, `Anthropic::MessageParam` is a union of `Anthropic::UserMessageParam`, `Anthropic::AssistantMessageParam`, and `Anthropic::SystemMessageParam`. In the same way, `Anthropic::Beta::BetaMessageParam` is a union of its three classes.

    `Anthropic::MessageParam.new(role: :user, content: "Hello, Claude")` still works, and returns an instance of the class for that role. You can also build that class yourself, with no `role:`, as `Anthropic::UserMessageParam.new(content: "Hello, Claude")`. Four things change for code that builds or inspects these instances:

    * `MessageParam.new` takes keywords only, so pass a hash as `MessageParam.new(**hash)`. It raises an `ArgumentError` when `role:` is missing or isn't one of the three roles.
    * `message.is_a?(Anthropic::MessageParam)` is `false`. A `when Anthropic::MessageParam` branch and `messages.grep(Anthropic::MessageParam)` still match.
    * An instance built with `.new` has no `:role` in its `to_h`, and `message[:role]` is `nil`. `message.role` still returns the role.
    * Only `BetaSystemMessageParam` has `clear_at` and `output_config`. On a user or assistant message they returned `nil`, and now raise a `NoMethodError`.

    ```ruby
    # Before
    typed = messages.select { _1.is_a?(Anthropic::MessageParam) }
    roles = typed.map { _1[:role] }

    # After
    typed = messages.grep(Anthropic::MessageParam)
    roles = typed.map(&:role)
    ```

    The `Role` enum modules stay. These constants moved. The names that start with `Beta` are under `Anthropic::Beta`, and the others are under `Anthropic`:

    | Removed                     | Use instead                                                                          |
    | --------------------------- | ------------------------------------------------------------------------------------ |
    | `MessageParam::Content`     | `MessageContentParam`, or `SystemMessageParam::Content` for a system message         |
    | `BetaMessageParam::Content` | `BetaMessageContentParam`, or `BetaSystemMessageParam::Content` for a system message |
    | `BetaMessageParam::ClearAt` | `BetaSystemMessageParam::ClearAt`                                                    |

    If you type-check with Sorbet, `MessageParam::OrHash` is gone, and `Anthropic::MessageParam` as a type no longer accepts an instance. Use `Anthropic::MessageParam::Variants` for the three classes, each of which has its own `OrHash`. In RBS, a value typed `Anthropic::MessageParam` has no `role` or `content`. Use the `Anthropic::Models::message_param` alias, which was the hash form of a message and is now the union of the three classes. The beta names are `BetaMessageParam::Variants` and `Anthropic::Models::Beta::beta_message_param`.
  </Tab>
</Tabs>

### One-value enums are constants

This affects the C#, Go, Java, PHP, and Ruby SDKs and one CLI flag. In earlier versions, a required field that can hold only one value had an enum type of its own with a single member. These fields are now constants, and the enum types are gone. The JSON that the SDK sends and reads is the same.

<Tabs exclude="shell:cURL, python, typescript">
  <Tab title="CLI">
    `--type` is optional on `ant beta:sessions:resources add`. `file` is the only value `--type` can take there, so v2 sends it for you. Commands that still pass `--type file` keep working, so there is nothing to change.
  </Tab>

  <Tab title="C#">
    In v12, such a `required` property had an enum with a single member, such as `BetaManagedAgentsTextBlockType.Text`. Nearly all of them are the `Type` property of a class under `Anthropic.Models.Beta`: `Agents`, `DeploymentRuns`, `Deployments`, `Dreams`, `Environments`, `MemoryStores`, `Sessions`, `UserProfiles`, and `Vaults`. In v13 these properties are a `JsonElement` that the constructor fills in, as `TextBlockParam.Type` already was.

    An optional property, such as `BetaManagedAgentsGlobToolConfigParams.Type`, keeps its enum. Two of those enums have a new name:

    | v12                                         | v13                                       |
    | ------------------------------------------- | ----------------------------------------- |
    | `BetaManagedAgentsBashToolConfigParamsType` | `Anthropic.Models.Beta.Agents.Type`       |
    | `BetaPackagesType`                          | `Anthropic.Models.Beta.Environments.Type` |

    When you build an object, delete the property:

    ```csharp
    // Before
    new BetaManagedAgentsTextBlock
    {
        Type = BetaManagedAgentsTextBlockType.Text,
        Text = "Hello Claude!",
    };

    // After
    new BetaManagedAgentsTextBlock { Text = "Hello Claude!" };
    ```

    A class that is left with one required property also gains a constructor that takes it, so `new BetaManagedAgentsTextBlock("Hello Claude!")` works too. A class that is left with none is built with `new BetaManagedAgentsAlwaysAllowPolicy()`.

    When you read one, compare the string:

    ```csharp
    // Before
    if (message.Type.Value() == BetaManagedAgentsAgentMessageEventType.AgentMessage) { }

    // After
    if (message.Type.GetString() == "agent.message") { }
    ```

    To tell the variants of a union apart, keep using its `TryPick*`, `Switch`, and `Match` methods, which don't change.
  </Tab>

  <Tab title="Go">
    An example of such an enum type and its constant is `BetaManagedAgentsTextBlockType` and `BetaManagedAgentsTextBlockTypeText`. Nearly all of them are the `Type` field of a struct under `client.Beta`: Agents, Deployments, Deployment Runs, Dreams, Environments, Memory Stores, Sessions, User Profiles, and Vaults. In v2 these fields use a type from the `shared/constant` package, as `TextBlockParam.Type` already did. An optional field, such as `BetaManagedAgentsBashToolConfigParams.Type`, keeps its enum.

    In a request, delete the field. It marshals as its one value when you leave it out:

    ```go
    // Before
    anthropic.BetaManagedAgentsTextBlockParam{
    	Type: anthropic.BetaManagedAgentsTextBlockTypeText,
    	Text: "Hello Claude!",
    }

    // After
    anthropic.BetaManagedAgentsTextBlockParam{
    	Text: "Hello Claude!",
    }
    ```

    A struct whose only field was that `Type` now has a constructor, such as `NewBetaManagedAgentsAlwaysAllowPolicyParam()`. As a union member, a pointer to the empty struct works too: `OfAlwaysAllow: &anthropic.BetaManagedAgentsAlwaysAllowPolicyParam{}`.

    In a response, compare with the string:

    ```go
    // Before
    switch event.Type {
    case string(anthropic.BetaManagedAgentsAgentMessageEventTypeAgentMessage):
    }

    // After
    switch event.Type {
    case "agent.message":
    }
    ```

    A variable, field, or parameter of yours that was declared with one of the removed types takes the new type of the field, such as `constant.AgentMessage`. `constant.ValueOf[constant.AgentMessage]()` returns its value.

    The union constructors change with the fields. These five lose their `type_` argument:

    * `BetaManagedAgentsEventParamsOfUserToolConfirmation`
    * `BetaManagedAgentsEventParamsOfUserDefineOutcome`
    * `BetaManagedAgentsDeploymentInitialEventParamsOfUserDefineOutcome`
    * `BetaManagedAgentsMultiagentRosterEntryParamsOfBetaManagedAgentsAgents`
    * `BetaManagedAgentsMultiagentRosterEntryParamsOfBetaManagedAgentsAdvisors`

    These four took no other argument, so they are gone. Set the union's field to a pointer to the empty struct, such as `BetaManagedAgentsEventParamsUnion{OfUserInterrupt: &anthropic.BetaManagedAgentsUserInterruptEventParams{}}`:

    * `BetaManagedAgentsEventParamsOfUserInterrupt`
    * `BetaManagedAgentsMultiagentRosterEntryParamsOfBetaManagedAgentsMultiagentSelfs`
    * `BetaManagedAgentsCredentialNetworkingParamsOfUnrestricted`
    * `BetaOutputBehaviorParamOfCreateNew`
  </Tab>

  <Tab title="Java">
    An example of such an enum is the nested class `BetaManagedAgentsTextBlock.Type`, with its one member `TEXT`. Nearly all of them are the `type` of a class under `com.anthropic.models.beta`: `agents`, `deploymentruns`, `deployments`, `dreams`, `environments`, `memorystores`, `sessions`, `userprofiles`, and `vaults`. In v3 these fields are a `JsonValue` that the builder fills in, as `TextBlockParam`'s already was. An optional field, such as the `type` of `BetaManagedAgentsBashToolConfigParams`, keeps its enum.

    When you build an object, delete the call:

    ```java
    // Before
    BetaManagedAgentsTextBlock block = BetaManagedAgentsTextBlock.builder()
        .type(BetaManagedAgentsTextBlock.Type.TEXT)
        .text("Hello Claude!")
        .build();

    // After
    BetaManagedAgentsTextBlock block = BetaManagedAgentsTextBlock.builder()
        .text("Hello Claude!")
        .build();
    ```

    A class that is left with one required field also gains a factory method that takes it, so `BetaManagedAgentsTextBlock.of("Hello Claude!")` works too. A class that is left with none loses `of(type)`, and its unions lose the overload that took the enum, such as `ofAlwaysAllow(type)`. Build it with `BetaManagedAgentsAlwaysAllowPolicy.builder().build()`.

    When you read one, `type()` is gone and `_type()` returns the `com.anthropic.core.JsonValue`:

    ```java
    // Before
    if (message.type().equals(BetaManagedAgentsAgentMessageEvent.Type.AGENT_MESSAGE)) {}

    // After
    if (message._type().equals(JsonValue.from("agent.message"))) {}
    ```

    To tell the variants of a union apart, keep using its `is*()` and `as*()` methods and its visitor, which don't change.
  </Tab>

  <Tab title="PHP">
    An example of such an enum case is `Anthropic\Beta\Sessions\Events\ManagedAgentsTextBlock\Type::TEXT`. Nearly all of them are the `type` of a Managed Agents class under `Anthropic\Beta`. These properties are now a string with that one value as their default, as the `type` of `Anthropic\Messages\TextBlockParam` already was. An optional property, such as the `type` of `Anthropic\Beta\Environments\BetaPackages`, keeps its enum.

    `with()` no longer takes `type`. Remove it: PHP throws "Unknown named parameter" for a leftover `type:`, and in a positional call the arguments after it move up by one.

    ```php
    // Before
    ManagedAgentsTextBlock::with(text: 'Hello Claude!', type: Type::TEXT);

    // After
    ManagedAgentsTextBlock::with(text: 'Hello Claude!');
    ```

    Where you compared with an enum case, compare with the string:

    ```php
    // Before
    $event->type === Type::AGENT_MESSAGE->value;

    // After
    $event->type === 'agent.message';
    ```

    * `withType()` and the `type` argument of `$client->beta->sessions->resources->add()` take only the string now. In `add()` it defaults to `'file'`, so you can leave it out.
    * Requests you write as arrays don't change, and still need their `'type'`.
  </Tab>

  <Tab title="Ruby">
    An example of such an enum constant is `Anthropic::Beta::Sessions::BetaManagedAgentsTextBlock::Type::TEXT`. Nearly all of them are the `type` of a Managed Agents class under `Anthropic::Beta`. In v2 these fields are declared as a constant, as the `type` of `Anthropic::TextBlockParam` already was. An optional field, such as the `type` of `Anthropic::Beta::BetaManagedAgentsGlobToolConfigParams`, keeps its enum.

    Replace a removed constant with its symbol:

    ```ruby
    # Before
    event.type == Anthropic::Beta::Sessions::BetaManagedAgentsAgentMessageEvent::Type::AGENT_MESSAGE

    # After
    event.type == :"agent.message"
    ```

    Requests you write as hashes don't change, and still need their `type`:

    ```ruby
    client.beta.sessions.events.send_(
      session.id,
      events: [{type: "user.message", content: [{type: "text", text: "Hello Claude!"}]}]
    )
    ```

    When you build a model instance, `type:` now has a default, so you can leave it out: `Anthropic::Beta::Sessions::BetaManagedAgentsTextBlock.new(text: "Hello Claude!")`. The same goes for the `type:` keyword of `client.beta.sessions.resources.add`.

    If you type-check with Sorbet, the `Type::OrSymbol` and `Type::TaggedSymbol` aliases of these modules are gone with them, and the fields are a `Symbol`. `OrSymbol` also allowed a `String`, so `.new(type: "text")` no longer type-checks. Drop the keyword or pass `:text`. In RBS, the `type_` alias of each class is gone, and the field is the literal, such as `:text`.
  </Tab>
</Tabs>

### Client-side compaction is removed from the tool runner

This affects the TypeScript and Ruby SDKs. Client-side compaction in the tool runner has been removed in favor of server-side compaction, which summarizes the conversation inside the API instead of with an extra request from the client.

<Tabs exclude="shell, python, csharp, go, java, php">
  <Tab title="TypeScript">
    The `compactionControl` option and the `@anthropic-ai/sdk/lib/tools/CompactionControl` module are gone. The option stopped working in v0.129.0, where passing it threw an `AnthropicError`. It isn't in the params type, so TypeScript reports it as an unknown property.

    To keep compacting automatically at a token threshold:

    ```typescript
    // Before
    const runner = client.beta.messages.toolRunner({
      // ...
      compactionControl: { enabled: true, contextTokenThreshold: 100_000 }
    });

    // After
    const runner = client.beta.messages.toolRunner({
      // ...
      betas: ["compact-2026-01-12"],
      context_management: {
        edits: [{ type: "compact_20260112", trigger: { type: "input_tokens", value: 100_000 } }]
      }
    });
    ```

    To decide yourself when the conversation is compacted, call [`runner.compactBeforeNextTurn()`](https://github.com/anthropics/anthropic-sdk-typescript/blob/main/helpers.md#compaction).
  </Tab>

  <Tab title="Ruby">
    The `compaction_control:` option is gone. It stopped working in v1.74.0, where passing it raised an `ArgumentError`.

    To keep compacting automatically at a token threshold:

    ```ruby
    # Before
    runner = client.beta.messages.tool_runner(
      # ...
      compaction_control: {enabled: true, context_token_threshold: 100_000}
    )

    # After
    runner = client.beta.messages.tool_runner(
      # ...
      betas: ["compact-2026-01-12"],
      context_management: {
        edits: [{type: :compact_20260112, trigger: {type: :input_tokens, value: 100_000}}]
      }
    )
    ```

    To decide yourself when the conversation is compacted, call [`#compact_before_next_turn`](https://github.com/anthropics/anthropic-sdk-ruby/blob/main/helpers.md#compact_before_next_turn---compact-the-conversation) on the runner.
  </Tab>
</Tabs>

The trigger threshold must be at least 50,000 tokens. See [compaction](https://platform.claude.com/docs/en/build-with-claude/compaction-threshold) for the other options (`pause_after_compaction`, custom `instructions`).

### Text Completions is removed

The legacy Text Completions API is removed from the TypeScript, Go, Java, and Ruby SDKs and from the CLI. Newer models and features don't support it. Use the [Messages API](https://platform.claude.com/docs/en/api/messages) instead.

<Tabs exclude="shell:cURL, python, csharp, php">
  <Tab title="CLI">
    The `ant completions create` command is gone.

    ```bash
    # Before
    ant completions create \
      --model "$MODEL" \
      --max-tokens-to-sample 1024 \
      --prompt $'\n\nHuman: Hello, Claude\n\nAssistant:'

    # After
    ant messages create \
      --model "$MODEL" \
      --max-tokens 1024 \
      --message '{role: user, content: "Hello, Claude"}'
    ```

    The reply text moves from the `completion` field to `content.0.text`, so a script that passed `--transform completion` passes `--transform content.0.text` instead.

    `ant messages create` also takes `--stream`, but its events have another shape: the text arrives in `delta.text` of `content_block_delta` events, so `--transform content.0.text` does not apply to a stream.
  </Tab>

  <Tab title="TypeScript">
    `client.completions` is gone, along with the `Completions` resource class and the `Completion`, `CompletionCreateParams`, `CompletionCreateParamsNonStreaming`, and `CompletionCreateParamsStreaming` types. `AnthropicBedrock` no longer has a `completions` property either. The `HUMAN_PROMPT` and `AI_PROMPT` constants, which only Text Completions prompts used, are gone too, both as exports and as static properties of the client.

    ```typescript
    // Before
    const completion = await client.completions.create({
      model,
      max_tokens_to_sample: 1024,
      prompt: "\n\nHuman: Hello, Claude\n\nAssistant:"
    });
    console.log(completion.completion);

    // After
    const message = await client.messages.create({
      model,
      max_tokens: 1024,
      messages: [{ role: "user", content: "Hello, Claude" }]
    });
    console.log(message.content);
    ```

    `client.completions.create({ ..., stream: true })` becomes `client.messages.create({ ..., stream: true })` or `client.messages.stream({ ... })`.
  </Tab>

  <Tab title="Go">
    `client.Completions` is gone, along with `CompletionService`, `NewCompletionService`, `CompletionNewParams`, and `Completion`. `aws.Client` no longer has a `Completions` field either. `bedrock.DefaultEndpoints` no longer lists `/v1/complete`.

    ```go
    // Before
    completion, err := client.Completions.New(ctx, anthropic.CompletionNewParams{
    	Model:             model,
    	MaxTokensToSample: 1024,
    	Prompt:            "\n\nHuman: Hello, Claude\n\nAssistant:",
    })
    fmt.Println(completion.Completion)

    // After
    message, err := client.Messages.New(ctx, anthropic.MessageNewParams{
    	Model:     model,
    	MaxTokens: 1024,
    	Messages: []anthropic.MessageParam{
    		anthropic.NewUserMessage(anthropic.NewTextBlock("Hello, Claude")),
    	},
    })
    fmt.Println(message.Content[0].Text)
    ```

    `client.Completions.NewStreaming` becomes `client.Messages.NewStreaming`.
  </Tab>

  <Tab title="Java">
    `client.completions()` is gone from `AnthropicClient` and `AnthropicClientAsync`, along with `CompletionService`, `CompletionServiceAsync`, and the `com.anthropic.models.completions` package (`CompletionCreateParams` and `Completion`).

    ```java
    // Before
    CompletionCreateParams params = CompletionCreateParams.builder()
        .model(model)
        .maxTokensToSample(1024)
        .prompt("\n\nHuman: Hello, Claude\n\nAssistant:")
        .build();

    System.out.println(client.completions().create(params).completion());

    // After
    MessageCreateParams params = MessageCreateParams.builder()
        .model(model)
        .maxTokens(1024)
        .addUserMessage("Hello, Claude")
        .build();

    client.messages().create(params).content().stream()
        .flatMap(contentBlock -> contentBlock.text().stream())
        .forEach(textBlock -> System.out.println(textBlock.text()));
    ```

    `client.completions().createStreaming` becomes `client.messages().createStreaming`.
  </Tab>

  <Tab title="Ruby">
    `client.completions` is gone, along with `Anthropic::Resources::Completions`, `Anthropic::CompletionCreateParams`, and `Anthropic::Completion`. `Anthropic::BedrockClient` no longer has a `completions` reader either. On `Anthropic::BedrockMantleClient` and `Anthropic::GoogleCloudClient`, where `completions` raised `NotImplementedError`, the method no longer exists.

    ```ruby
    # Before
    completion = client.completions.create(
      model: model,
      max_tokens_to_sample: 1024,
      prompt: "\n\nHuman: Hello, Claude\n\nAssistant:"
    )
    puts(completion.completion)

    # After
    message = client.messages.create(
      model: model,
      max_tokens: 1024,
      messages: [{role: "user", content: "Hello, Claude"}]
    )
    puts(message.content)
    ```

    `client.completions.create_streaming` becomes `client.messages.stream`.
  </Tab>
</Tabs>

### `betas` is removed from the non-beta Models methods

The non-beta Models methods no longer take `betas` (csharp, go: `Betas`; java: `.addBeta()`), and the `ant models` commands no longer take `--beta`. To send beta headers, call the same methods on `client.beta.models` (csharp, go: `client.Beta.Models`; java: `client.beta().models()`; php: `$client->beta->models`), or `ant beta:models` in the CLI. In the SDK, those methods return `BetaModelInfo` (ruby: `Anthropic::Beta::BetaModelInfo`) where the non-beta ones return `ModelInfo` (ruby: `Anthropic::ModelInfo`).

<Tabs exclude="shell:cURL">
  <Tab title="CLI">
    ```bash
    # Before
    ant models list --beta "$BETA"

    # After
    ant beta:models list --beta "$BETA"
    ```
  </Tab>

  <Tab title="Python">
    `client.models.retrieve()` and `client.models.list()` no longer take `betas` (passing it is a `TypeError`, and a type checker flags it), and `anthropic.types.ModelListParams` no longer has a `betas` key.

    ```python
    # Before
    page = client.models.list(betas=[beta])

    # After
    page = client.beta.models.list(betas=[beta])
    ```
  </Tab>

  <Tab title="TypeScript">
    `Anthropic.ModelRetrieveParams` and `Anthropic.ModelListParams` no longer have a `betas` property.

    ```typescript
    // Before
    const page = await client.models.list({ betas: [beta] });

    // After
    const page = await client.beta.models.list({ betas: [beta] });
    ```
  </Tab>

  <Tab title="C#">
    `ModelRetrieveParams` and `ModelListParams` in `Anthropic.Models.Models` no longer have a `Betas` property. The methods on `client.Beta.Models` take the classes of the same names in `Anthropic.Models.Beta.Models`.

    ```csharp
    // Before
    using Anthropic.Models.Models;

    var page = await client.Models.List(new ModelListParams { Betas = [beta] });

    // After
    using Anthropic.Models.Beta.Models;

    var page = await client.Beta.Models.List(new ModelListParams { Betas = [beta] });
    ```
  </Tab>

  <Tab title="Go">
    `ModelGetParams` and `ModelListParams` no longer have a `Betas` field.

    ```go
    // Before
    page, err := client.Models.List(ctx, anthropic.ModelListParams{
    	Betas: []anthropic.AnthropicBeta{beta},
    })

    // After
    page, err := client.Beta.Models.List(ctx, anthropic.BetaModelListParams{
    	Betas: []anthropic.AnthropicBeta{beta},
    })
    ```
  </Tab>

  <Tab title="Java">
    `ModelRetrieveParams` and `ModelListParams` in `com.anthropic.models.models` no longer have `betas()`, and their builders no longer have `betas` and `addBeta`. The methods on `client.beta().models()` take the classes of the same names in `com.anthropic.models.beta.models`.

    ```java
    // Before
    import com.anthropic.models.models.ModelListPage;
    import com.anthropic.models.models.ModelListParams;

    ModelListPage page = client.models().list(ModelListParams.builder().addBeta(beta).build());

    // After
    import com.anthropic.models.beta.models.ModelListPage;
    import com.anthropic.models.beta.models.ModelListParams;

    ModelListPage page = client.beta().models().list(ModelListParams.builder().addBeta(beta).build());
    ```
  </Tab>

  <Tab title="PHP">
    `$client->models->retrieve()` and `$client->models->list()` no longer take `betas` (passing it throws `Error: Unknown named parameter $betas`), and `Anthropic\Models\ModelRetrieveParams` and `Anthropic\Models\ModelListParams` no longer have a `betas` property.

    ```php
    // Before
    $page = $client->models->list(betas: [$beta]);

    // After
    $page = $client->beta->models->list(betas: [$beta]);
    ```

    If you pass arguments by position, `workspaceID` and `requestOptions` each move up one place in both methods.
  </Tab>

  <Tab title="Ruby">
    `client.models.retrieve` and `client.models.list` no longer take `betas:`, and `Anthropic::ModelRetrieveParams` and `Anthropic::ModelListParams` no longer have a `betas` field.

    ```ruby
    # Before
    page = client.models.list(betas: [beta])

    # After
    page = client.beta.models.list(betas: [beta])
    ```

    Passing `betas:` to `client.models` does not raise, but it no longer sets the `anthropic-beta` header.
  </Tab>
</Tabs>

### API keys are sent as `Authorization: Bearer`

The SDK and the CLI send your API key as `Authorization: Bearer <key>` instead of in the `X-Api-Key` header, so change any proxy or gateway that reads or sets `X-Api-Key` to use `Authorization`, or [send the key in `X-Api-Key` yourself](https://platform.claude.com/docs/en/api/migration-2026-10-21#sdk-proxy-x-api-key). The Claude API accepts a key in either header, so a program that talks to the API directly needs no change.

```text wrap
# Before
X-Api-Key: <key>

# After
Authorization: Bearer <key>
```

<Tabs>
  <Tab title="CLI">
    This applies to a key in `ANTHROPIC_API_KEY` and to one piped to `--api-key-stdin`.

    With `--debug`, the request log now shows `Authorization: Bearer <REDACTED>` where it showed `X-Api-Key: <REDACTED>`.
  </Tab>

  <Tab title="Python">
    `Authorization` is the header `auth_token` already uses.

    This applies to the `api_key` argument and the `ANTHROPIC_API_KEY` environment variable of `Anthropic` and `AsyncAnthropic`, and to `api_key` and `ANTHROPIC_AWS_API_KEY` of `AnthropicAWS`. `AnthropicFoundry` still sends its key as `x-api-key`, and `AnthropicBedrockMantle` already sent a bearer token.
  </Tab>

  <Tab title="TypeScript">
    `Authorization` is the header the `authToken` option already uses.

    This applies to the `apiKey` option, the `ANTHROPIC_API_KEY` environment variable, and `apiKey` and `ANTHROPIC_AWS_API_KEY` in `@anthropic-ai/aws-sdk`. `apiKey` in `@anthropic-ai/foundry-sdk` still goes out as `X-Api-Key`, and `apiKey` in `@anthropic-ai/bedrock-sdk` was already a bearer token.

    Middleware or a custom `fetch` that reads the key from the `x-api-key` request header needs to read `authorization` instead, where the key follows `Bearer `.
  </Tab>

  <Tab title="C#">
    `Authorization` is the header `AuthToken` already uses.

    This applies to `ApiKey` on `AnthropicClient` and `ClientOptions` and to the `ANTHROPIC_API_KEY` environment variable. In the `Anthropic.Aws` release that depends on v13, it also applies to `ApiKey` in `AwsClientOptions` and to `ANTHROPIC_AWS_API_KEY`. `AnthropicFoundryApiKeyCredentials` still sends its key as `x-api-key`, and `ApiKey` in `MantleAwsClientOptions` was already a bearer token.
  </Tab>

  <Tab title="Go">
    This applies to `option.WithAPIKey`, the `ANTHROPIC_API_KEY` environment variable, and `APIKey` in `aws.ClientConfig` (or `ANTHROPIC_AWS_API_KEY`). `APIKey` in `foundry.ClientConfig` (or `ANTHROPIC_FOUNDRY_API_KEY`) still goes out as `X-Api-Key`, and `APIKey` in `bedrock.MantleClientConfig` was already a bearer token.
  </Tab>

  <Tab title="Java">
    `Authorization` is the header `authToken` already uses.

    This applies to `apiKey` on the `AnthropicOkHttpClient`, `AnthropicOkHttpClientAsync`, and `AnthropicBackend` builders, the `ANTHROPIC_API_KEY` environment variable, and the `anthropic.apiKey` system property. `apiKey` on the `FoundryBackend` builder still goes out as `x-api-key`. `apiKey` on the `AwsBackend`, `BedrockBackend`, and `BedrockMantleBackend` builders was already a bearer token.

    An interceptor now sees the key in `Authorization` instead of `X-Api-Key`.
  </Tab>

  <Tab title="PHP">
    `Authorization` is the header `authToken` already uses.

    This applies to the `apiKey` argument and the `ANTHROPIC_API_KEY` environment variable of `Anthropic\Client`, and to `apiKey` and `ANTHROPIC_AWS_API_KEY` of `Anthropic\Aws\Client`. `Anthropic\Foundry\Client` still sends its key as `x-api-key`, and `Anthropic\Bedrock\MantleClient` already sent a bearer token.
  </Tab>

  <Tab title="Ruby">
    `Authorization` is the header `auth_token:` already uses.

    This applies to the `api_key:` argument and the `ANTHROPIC_API_KEY` environment variable of `Anthropic::Client`, and to `api_key:` and `ANTHROPIC_AWS_API_KEY` of `Anthropic::AWSClient`. `Anthropic::BedrockMantleClient` already sent a bearer token.

    The SDK drops `Authorization` when it follows a redirect to another origin, which includes a redirect from `http` to `https` on the same host. The key is now dropped there too.
  </Tab>
</Tabs>

#### If a proxy or gateway reads `X-Api-Key`

<Tabs exclude="shell:cURL">
  <Tab title="CLI">
    If `--base-url` or `ANTHROPIC_BASE_URL` points `ant` at a proxy or gateway that reads `X-Api-Key`, change it to read the key from `Authorization`. `ant` has no flag or environment variable for adding a header of your own, so it can't send `X-Api-Key`.
  </Tab>

  <Tab title="Python">
    Move the key back with an `auth` function on the HTTP client. It runs on every request the client sends, including retries:

    ```python
    import httpx2
    from anthropic import Anthropic, DefaultHttpxClient


    def send_x_api_key(request: httpx2.Request) -> httpx2.Request:
        if request.headers.get("Authorization") == f"Bearer {api_key}":
            del request.headers["Authorization"]
            request.headers["X-Api-Key"] = api_key
        return request


    client = Anthropic(api_key=api_key, http_client=DefaultHttpxClient(auth=send_x_api_key))
    ```

    `AsyncAnthropic` takes the same function, in `http_client=DefaultAsyncHttpxClient(auth=send_x_api_key)`.
  </Tab>

  <Tab title="TypeScript">
    Set the header yourself. `Authorization: null` stops the key from going out there as well:

    ```typescript
    const client = new Anthropic({
      apiKey,
      defaultHeaders: { "X-Api-Key": apiKey, Authorization: null }
    });
    ```

    If the proxy adds the credential and your client has none, v0 let you say so with either `"X-Api-Key": null` or `Authorization: null` in `defaultHeaders`. v1 accepts only `Authorization: null`.

    The environment work poller and worker are given their own key, so they leave `X-Api-Key` and `Authorization` default headers out of their own requests.
  </Tab>

  <Tab title="C#">
    Set the header yourself with `ExtraHeaders`. Setting `ApiKey` and `AuthToken` to `null` stops a credential found in `ANTHROPIC_API_KEY` or `ANTHROPIC_AUTH_TOKEN` from going out as well:

    ```csharp
    AnthropicClient client = new(
        new ClientOptions
        {
            ApiKey = null,
            AuthToken = null,
            ExtraHeaders = new Dictionary<string, string> { ["X-Api-Key"] = apiKey },
        }
    );
    ```
  </Tab>

  <Tab title="Go">
    Set the header yourself. `option.WithHeaderDel` stops a key found in `ANTHROPIC_API_KEY` from going out as well:

    ```go
    client := anthropic.NewClient(
    	option.WithHeader("X-Api-Key", apiKey),
    	option.WithHeaderDel("Authorization"),
    )
    ```

    `environments.WorkPoller` and `environments.EnvironmentWorker` are given their own key, so they leave a hand-set `X-Api-Key` out of their own requests.
  </Tab>

  <Tab title="Java">
    Set the header yourself instead of calling `apiKey`:

    ```java
    AnthropicClient client = AnthropicOkHttpClient.builder()
        .putHeader("X-Api-Key", apiKey)
        .build();
    ```
  </Tab>

  <Tab title="PHP">
    Move the key back with a middleware:

    ```php
    use Anthropic\Client;
    use Psr\Http\Message\RequestInterface;
    use Psr\Http\Message\ResponseInterface;

    $sendXApiKey = fn (RequestInterface $request, callable $next): ResponseInterface => $next(
        $request->withoutHeader('Authorization')->withHeader('X-Api-Key', $apiKey)
    );

    $client = new Client(apiKey: $apiKey, requestOptions: ['middleware' => [$sendXApiKey]]);
    ```

    Do not use the client's `extraHeaders` for this. A request that has `extraHeaders` of its own replaces the client's, and every endpoint under `$client->beta` that needs a beta header has them.
  </Tab>

  <Tab title="Ruby">
    Move the key back with a middleware:

    ```ruby
    send_x_api_key = lambda do |req, nxt|
      next nxt.call(req) unless req.headers["authorization"] == "Bearer #{api_key}"
      nxt.call(req.with(headers: {**req.headers.except("authorization"), "x-api-key" => api_key}))
    end

    client = Anthropic::Client.new(api_key: api_key, middleware: send_x_api_key)
    ```

    The first line leaves a request alone when it doesn't carry the key, such as one that was redirected to another origin.

    `Anthropic::AWSClient` takes no `middleware:` argument. Pass the middleware with each request instead, as `request_options: {middleware: send_x_api_key}`.
  </Tab>
</Tabs>

#### If you set or removed `X-Api-Key` on a request

This affects the Python, TypeScript, Go, PHP, and Ruby SDKs.

If you removed `X-Api-Key` so that a request sent only an auth token, delete that code instead of changing it, because removing `Authorization` would remove the token. [A client holds one credential](https://platform.claude.com/docs/en/api/migration-2026-10-21#sdk-one-credential), so make sure that it's the token: with none passed in code and both `ANTHROPIC_API_KEY` and `ANTHROPIC_AUTH_TOKEN` set, the client uses the key.

<Tabs exclude="shell, csharp, java">
  <Tab title="Python">
    Code that passes `extra_headers={"X-Api-Key": omit}` to keep the key off a request no longer does that. Pass `extra_headers={"Authorization": omit}` instead.

    `extra_headers={"X-Api-Key": other_key}` no longer replaces the client's key: both keys go out. To send another key with one request, pass `extra_headers={"Authorization": f"Bearer {other_key}"}`.
  </Tab>

  <Tab title="TypeScript">
    `headers: { "X-Api-Key": otherKey }` in a request's options no longer replaces the client's key: both keys go out. To send another key with one request, pass ``headers: { Authorization: `Bearer $\{otherKey}` }``.
  </Tab>

  <Tab title="Go">
    `option.WithHeaderDel("X-Api-Key")` no longer keeps the key off a request. Delete `Authorization` instead:

    ```go
    // Before
    client.Messages.New(ctx, params, option.WithHeaderDel("X-Api-Key"))

    // After
    client.Messages.New(ctx, params, option.WithHeaderDel("Authorization"))
    ```

    `option.WithHeader("X-Api-Key", otherKey)` no longer replaces the client's key: both keys go out. To send another key with one request, pass `option.WithAPIKey(otherKey)`.
  </Tab>

  <Tab title="PHP">
    `'extraHeaders' => ['X-Api-Key' => null]` no longer keeps the key off a request. To send a request with no credential, set `Authorization` to `null` instead, or remove it in a middleware if you did this for the whole client.

    `'extraHeaders' => ['X-Api-Key' => $otherKey]` no longer replaces the client's key: both keys go out. To send another key with one request, set `Authorization` to `"Bearer {$otherKey}"`.
  </Tab>

  <Tab title="Ruby">
    `extra_headers: {"x-api-key" => nil}` no longer keeps the key off a request. Set `"authorization"` to `nil` instead. To send another key with one request, set `"authorization"` to `"Bearer #{other_key}"`, not `"x-api-key"`.
  </Tab>
</Tabs>

### A client holds one credential

An API key and an auth token now share a header, so an SDK client holds one credential. With none passed in code, it follows the [credential precedence](https://platform.claude.com/docs/en/manage-claude/wif-reference#credential-precedence) order.

<Tabs exclude="shell">
  <Tab title="Python">
    v1 sent both an API key and an auth token when the client had both, each in its own header. The credential is one of `api_key`, `auth_token`, `credentials`, `config`, or `profile`.

    * **Pass at most one.** Two or more in the constructor, or in one `copy()` or `with_options()` call, raise `ValueError`. `None` doesn't count. v1 raised `TypeError`, and only for two of `credentials`, `config`, and `profile`.
    * **The one you pass is the only one.** As in v1, the client does not look for another in the environment or on disk.
    * **With none passed, only the first of these that is set is used:** `ANTHROPIC_API_KEY`, `ANTHROPIC_AUTH_TOKEN`, the profile that `ANTHROPIC_PROFILE` names, the workload identity federation variables, the active profile on disk (the one the `active_config` file names, otherwise `default`). When both of the first two are set, the client logs a warning once. v1 used the active profile ahead of the federation variables when `ANTHROPIC_CONFIG_DIR` was set or an `active_config` file existed; set `ANTHROPIC_PROFILE` to keep using it.
    * **`copy()` and `with_options()` replace.** A credential you pass replaces the client's own, whichever kind either one is. A base URL and headers that came from the old credential's config or profile go with it, and the new credential's are used. A base URL you passed stays.

    ```python
    client = Anthropic(api_key=key, auth_token=token)

    # Before: sent `X-Api-Key: <key>` and `Authorization: Bearer <token>`
    # After:  raises `ValueError`
    ```

    The platform clients keep their own rules. `AnthropicAWS` takes `auth_token` next to `api_key` without an error, and sends the key.

    The docstrings of `Anthropic.__init__` and `Anthropic.copy` in [`_client.py`](https://github.com/anthropics/anthropic-sdk-python/blob/main/src/anthropic/_client.py) have the details.

    If you relied on sending both, for example a token for a gateway and a key for the API behind it, pass the token as `auth_token` and set `X-Api-Key` in `default_headers`. Have the gateway remove its `Authorization` header before it forwards the request. The Claude API expects one credential per request.
  </Tab>

  <Tab title="TypeScript">
    In v0 a client that had both an API key and an auth token sent both, each in its own header. The credential is one of `apiKey`, `authToken`, `credentials`, `config`, or `profile`.

    * **Pass at most one.** Two or more in `new Anthropic()`, or in one `withOptions()` call, throw a `TypeError`. `null` and `undefined` don't count.
    * **The one you pass is the only one.** The client does not look for another in the environment or on disk.
    * **With none passed, the first of these is used:** `ANTHROPIC_API_KEY`, `ANTHROPIC_AUTH_TOKEN`, the profile that `ANTHROPIC_PROFILE` names, the workload identity federation variables, the active profile on disk (the one the `active_config` file names, otherwise `default`). When both of the first two are set, the client logs a warning once. In v0 the active profile came before the federation variables. An `ANTHROPIC_PROFILE` that names a missing profile was skipped in v0, and now the first request throws an `AnthropicError`. `loadConfig()` with no argument follows the same order and throws the same error.
    * **`withOptions` replaces.** A credential you pass replaces the one of the client you copy, so `client.withOptions({ authToken })` no longer needs `apiKey: null` next to it.
    * **A platform client takes only its platform's credentials.** The AWS, Bedrock, and Foundry clients and `AnthropicVertex` throw an `AnthropicError` for a credential option they don't authenticate with, as `AnthropicGoogleCloud` already did. On the AWS and Bedrock clients `apiKey: null` now clears the key, so the client signs with AWS credentials. `AnthropicBedrock` keeps its key in `client.apiKey`, where v0 kept it in `client.authToken`.

    ```typescript
    // Before: sent the API key and ignored `credentials`
    const client = new Anthropic({ apiKey, credentials });

    // After: the line above throws a TypeError
    const client = new Anthropic({ credentials });
    ```

    The doc comments on [`ClientOptions`](https://github.com/anthropics/anthropic-sdk-typescript/blob/main/src/client.ts) say how each option behaves, and the doc comment on each of those platform clients' constructors lists the options it rejects.

    If you relied on sending both, for example a token for a gateway and a key for the API behind it, set `X-Api-Key` in `defaultHeaders` and keep `authToken`. Have the gateway remove its `Authorization` header before it forwards the request. The Claude API expects one credential per request.
  </Tab>

  <Tab title="C#">
    In v12 a client that had both an API key and an auth token sent both, each in its own header. The credential is one of `ApiKey`, `AuthToken`, or `ClientOptions.Credentials`.

    * **Passing two is an error.** Setting a second one throws an `ArgumentException`. `null` doesn't count, so to swap the credential in `ClientOptions` that you built yourself, set the old one to `null` first.
    * **Passing one uses it and ignores the environment.** No credential environment variable or profile on disk is read. In the same way, `AnthropicCredentials.Resolve(profile: "name")` now returns that profile's credentials when `ANTHROPIC_API_KEY` or `ANTHROPIC_AUTH_TOKEN` is set.
    * **Passing none uses the first match in the environment:** `ANTHROPIC_API_KEY`, `ANTHROPIC_AUTH_TOKEN`, `ANTHROPIC_PROFILE`, the workload identity federation variables, then the active profile on disk. An empty `ANTHROPIC_API_KEY` or `ANTHROPIC_AUTH_TOKEN` counts as unset. When both of the first two are set, a warning goes to stderr once. The client looks when it is first used, so an `ANTHROPIC_PROFILE` that doesn't exist now throws from the first request instead of the constructor.
    * **`WithOptions` replaces.** A credential you pass in the modifier replaces the client's, whichever kind that was, so `AuthToken = token` no longer needs `ApiKey = null` next to it. With none passed, the copy keeps the client's credential, `BaseUrl`, and `ExtraHeaders`, even when the modifier returns new `ClientOptions`.

    ```csharp
    // Before: sent both, each in its own header
    AnthropicClient client = new() { ApiKey = apiKey, AuthToken = token };

    // After: the line above throws an ArgumentException
    AnthropicClient client = new() { AuthToken = token };
    ```

    The XML docs on those three properties of [`ClientOptions`](https://github.com/anthropics/anthropic-sdk-csharp/blob/main/src/Anthropic/Core/ClientOptions.cs) have the details.

    Cloud platform clients keep the credentials they were built with. The Bedrock, Bedrock Mantle, Foundry, Google Cloud, and AWS clients and `AnthropicVertexClient` decide how to authenticate when you build them, and most of them use the `Authorization` header for it. The releases of these packages that depend on v13 ignore an `ApiKey` or `AuthToken` that you set through `WithOptions`. To use another key with `AnthropicAwsClient`, build a new client with `ApiKey` in `AwsClientOptions`.

    If you relied on sending both, for example a token for a gateway and a key for the API behind it, set `X-Api-Key` with `ExtraHeaders` and keep `AuthToken`. Have the gateway remove its `Authorization` header before it forwards the request. The Claude API expects one credential per request.
  </Tab>

  <Tab title="Go">
    In v1 a client that had both an API key and an auth token sent both, each in its own header. The credential comes from `option.WithAPIKey`, `option.WithAuthToken`, `option.WithConfig`, `option.WithProfile`, or `option.WithFederationTokenProvider`.

    * **Two of them passed to `anthropic.NewClient` are an error.** `NewClient` returns no error, so every request the client makes fails with it. `NewClient` already applies `anthropic.DefaultClientOptions()`, so don't pass its result as well: the credential it finds in the environment then counts as one you passed.
    * **One of them is used as it is.** No credential is read from the environment or from a profile on disk. In v1 `ANTHROPIC_API_KEY` and `ANTHROPIC_AUTH_TOKEN` won over the last three.
    * **With none of them, the first of these that is set is used,** in the same order as v1: `ANTHROPIC_API_KEY`, `ANTHROPIC_AUTH_TOKEN`, `ANTHROPIC_PROFILE`, the workload identity federation variables, the active profile on disk. When both of the first two are set, the SDK logs a warning once.
    * **One of them on a request replaces the client's credential for that request,** so `option.WithAuthToken` no longer needs `option.WithHeaderDel("X-Api-Key")` next to it.

    ```go
    // Before: the API key was sent and a warning was logged
    client := anthropic.NewClient(
    	option.WithAPIKey(apiKey),
    	option.WithProfile("work"),
    )

    // After: every request of the client above fails, so pass the one you want
    client := anthropic.NewClient(option.WithAPIKey(apiKey))
    ```

    The warning that v1 logged is gone, so `option.WithConfigQuiet`, which suppressed it, now does what `option.WithConfig` does and is deprecated.

    The doc comments on `anthropic.NewClient` and `anthropic.DefaultClientOptions` in [`client.go`](https://github.com/anthropics/anthropic-sdk-go/blob/main/client.go) have the details.

    If you relied on sending both, for example a token for a gateway and a key for the API behind it, set `X-Api-Key` with `option.WithHeader` and keep `option.WithAuthToken`. Have the gateway remove its `Authorization` header before it forwards the request. The Claude API expects one credential per request.

    `ANTHROPIC_CUSTOM_HEADERS` and `ANTHROPIC_WEBHOOK_SIGNING_KEY` now apply to every client that `anthropic.NewClient` builds. In v1 they were read only when neither the environment nor a profile on disk held a credential.
  </Tab>

  <Tab title="Java">
    In v2 a client that had both an API key and an auth token sent both, each in its own header. The credential is one of `apiKey`, `authToken`, or `configurationProvider` on the `AnthropicOkHttpClient`, `AnthropicOkHttpClientAsync`, and `AnthropicBackend` builders.

    * **Set at most one.** With two on one builder, `build()` throws an `IllegalStateException` that names them. `null` or an empty `Optional` does not count.
    * **The one you set is the only one.** `fromEnv()`, called before or after, takes no credential from the environment or from a profile on disk. In v2, a key or token that `fromEnv()` found could be sent as well, or instead.
    * **With none set, `fromEnv()` uses the first of these that it finds:** `ANTHROPIC_API_KEY`, `ANTHROPIC_AUTH_TOKEN`, `ANTHROPIC_PROFILE`, the workload identity federation variables, the active profile on disk. When both of the first two are set, a warning goes to `System.err` once. The `anthropic.apiKey` and `anthropic.authToken` system properties count as the environment. An empty key or token, in a variable or a system property, counts as unset. In v2, `fromEnv()` used the empty value as the key or token.

    ```java
    // Before: both were sent. In v3, build() throws an IllegalStateException
    AnthropicClient client = AnthropicOkHttpClient.builder()
        .apiKey(apiKey)
        .authToken(authToken)
        .build();

    // After
    AnthropicClient client = AnthropicOkHttpClient.builder()
        .apiKey(apiKey)
        .build();
    ```

    The documentation of `fromEnv()` on those builders has the details.

    If you relied on sending both, for example a token for a gateway and a key for the API behind it, set both headers yourself:

    ```java
    AnthropicClient client = AnthropicOkHttpClient.builder()
        .putHeader("Authorization", "Bearer " + gatewayToken)
        .putHeader("X-Api-Key", apiKey)
        .build();
    ```

    Have the gateway remove its `Authorization` header before it forwards the request. The Claude API expects one credential per request.
  </Tab>

  <Tab title="PHP">
    Earlier versions sent both an API key and an auth token when the client had both, each in its own header. `Anthropic\Client` takes one credential, from `apiKey`, `authToken`, or `credentials`:

    * Passing more than one of them throws `\InvalidArgumentException`. Only `null` counts as not passed. An empty string counts as passed, so `new Client(apiKey: '')` sends no credential.
    * Passing one uses it, and no credential is read from the environment or from a profile on disk. With `ANTHROPIC_API_KEY` set, `new Client(authToken: $token)` sends the token. Earlier versions sent the environment's key with it.
    * Passing none uses the first of these that is set: `ANTHROPIC_API_KEY`, `ANTHROPIC_AUTH_TOKEN`, the profile named by `ANTHROPIC_PROFILE`, the workload identity federation variables, the active profile on disk (the one the `active_config` file names, otherwise `default`). Earlier versions used the active profile before the federation variables, and used no profile when there was no `active_config` file. They also skipped an `ANTHROPIC_PROFILE` that named a missing or invalid profile. For that, `new Client()` now throws `Anthropic\Core\Exceptions\AnthropicException`. With both `ANTHROPIC_API_KEY` and `ANTHROPIC_AUTH_TOKEN` set, the client sends the key and its `authToken` property is empty. The first client built that way also writes a warning with `error_log()`, once per process, which on a web server means once per request: `Anthropic: ANTHROPIC_API_KEY and ANTHROPIC_AUTH_TOKEN are both set. Using ANTHROPIC_API_KEY.` To stop it, unset the variable you don't use.

    ```php
    // Before: sent the key as X-Api-Key and the token as Authorization.
    // After: throws "Pass at most one of `apiKey`, `authToken`, or `credentials`. Received `apiKey`, `authToken`."
    $client = new Client(apiKey: $key, authToken: $token);
    ```

    If you relied on sending both, for example a token for a gateway and a key for the API behind it, pass the token as `authToken` and add `X-Api-Key` in a middleware like the one under [If a proxy or gateway reads `X-Api-Key`](https://platform.claude.com/docs/en/api/migration-2026-10-21#sdk-proxy-x-api-key), without the `withoutHeader` call. Have the gateway remove its `Authorization` header before it forwards the request. The Claude API expects one credential per request.
  </Tab>

  <Tab title="Ruby">
    The credential arguments of `Anthropic::Client.new` are `api_key:`, `auth_token:`, `credentials:`, and `config:`. A `nil` argument counts as not passed. The platform clients keep their own rules.

    * **Two or more passed:** `Anthropic::Client.new` raises `ArgumentError`. Earlier versions raised only for `credentials:` with `config:`, and otherwise sent the key if there was one, then the token.
    * **One passed:** The client uses it, and does not fall back to a credential from the environment or from a profile on disk.
    * **None passed:** The client uses the first of these it finds: `ANTHROPIC_API_KEY`, `ANTHROPIC_AUTH_TOKEN`, `ANTHROPIC_PROFILE`, the workload identity federation variables, the active profile on disk. The order has not changed, but with both `ANTHROPIC_API_KEY` and `ANTHROPIC_AUTH_TOKEN` set, `client.auth_token` is now `nil`. An empty `ANTHROPIC_API_KEY` or `ANTHROPIC_AUTH_TOKEN` now counts as unset, where earlier versions let an empty `ANTHROPIC_API_KEY` hide the token and everything after it.

    When no credential is passed and both `ANTHROPIC_API_KEY` and `ANTHROPIC_AUTH_TOKEN` are set, the SDK also warns once per process, on standard error through `Kernel#warn`: `Anthropic: ANTHROPIC_API_KEY and ANTHROPIC_AUTH_TOKEN are both set. Using ANTHROPIC_API_KEY.` Unset the variable you don't use to silence it.

    ```ruby
    # Before: sent the key and ignored the token.
    # After: ArgumentError, "Pass at most one of `api_key:`, `auth_token:`, `credentials:`, or `config:`. Received `api_key:`, `auth_token:`."
    Anthropic::Client.new(api_key: api_key, auth_token: auth_token)

    # Pass the one you want sent.
    Anthropic::Client.new(api_key: api_key)
    ```
  </Tab>
</Tabs>

### Changes in one SDK or the CLI

These changes each affect one SDK or the CLI.

<Tabs exclude="shell:cURL, python, typescript">
  <Tab title="CLI">
    **`--api-key` and `--auth-token` are removed.** `ant` no longer takes an API key or auth token as a flag value, because a value on the command line is visible in shell history and process listings. Both flags have printed a deprecation warning since v1.27.0. A command that still passes one stops with `flag provided but not defined`.

    | Removed                | Use instead                                                 |
    | ---------------------- | ----------------------------------------------------------- |
    | `--api-key <key>`      | `ANTHROPIC_API_KEY`, `--api-key-stdin`, or `ant auth login` |
    | `--auth-token <token>` | `ANTHROPIC_AUTH_TOKEN` or `--auth-token-stdin`              |

    ```bash
    # Before
    ant --api-key "$KEY" models list

    # After, from the environment
    export ANTHROPIC_API_KEY="$KEY"
    ant models list

    # After, from a secret manager
    op read op://vault/anthropic/api-key | ant --api-key-stdin models list
    ```

    `--api-key-stdin` and `--auth-token-stdin` read all of standard input, so a command that uses one takes its request body from flags.

    `ant auth status`, the first-run prompt of `ant apply`, and the note about multiple auth sources now call these credentials `ANTHROPIC_API_KEY` and `ANTHROPIC_AUTH_TOKEN`, where they printed `--api-key / ANTHROPIC_API_KEY` and `--auth-token / ANTHROPIC_AUTH_TOKEN`.
  </Tab>

  <Tab title="C#">
    **A union's `Type` is an enum.** In v12, the `Type` property of a union class, such as `ContentBlock.Type` or `RawMessageStreamEvent.Type`, was a `JsonElement`. In v13 it is an `ApiEnum<string, T>`, where `T` is a new enum with one member for each variant, such as `ContentBlockType`. A few unions are told apart by `Name` or `Command` instead, such as `BetaMemoryTool20250818Command.Command`, and those properties change in the same way. The `Type` of a variant class, such as `TextBlock.Type`, is still a `JsonElement`.

    ```csharp
    // Before
    if (block.Type.GetString() == "tool_use") { }

    // After
    if (block.Type.Value() == ContentBlockType.ToolUse) { }
    ```

    `block.Type.Raw()` returns the string, including one that this version of the SDK has no enum member for.

    **`IChatClient` ignores sampling options.** The `IChatClient` adapters (`AsIChatClient()`) now ignore `ChatOptions.Temperature`, `ChatOptions.TopK`, and `ChatOptions.TopP`. See [Sampling parameters are removed](https://platform.claude.com/docs/en/api/migration-2026-10-21#sampling-parameters).
  </Tab>

  <Tab title="Go">
    **`vertex.DefaultVersion` and `bedrock.DefaultVersion` are removed.**
  </Tab>

  <Tab title="Java">
    **Getters that now return an `Optional`.** `apiKey()` and `authToken()` on `AnthropicBackend` now return an `Optional<String>`, as `apiKey()` on `AwsBackend` and `BedrockMantleBackend` already did. In v2 each returned a `String`, which was `null` when the backend had no credential of that kind.

    ```java
    // Before
    String apiKey = backend.apiKey();
    if (apiKey != null) {}

    // After
    Optional<String> apiKey = backend.apiKey();
    if (apiKey.isPresent()) {}
    ```

    These getters now return an `Optional` too. In v2 each returned the value itself, which was `null` when there was none:

    * `apiKey()` and `awsCredentialsProvider()` on `BedrockBackend`
    * `filename()` and `mimeType()` on `McpResourceFile`
    * `detail()` on `CredentialSource`
    * `body()` on `HttpRequest`
    * `resource()` on `FoundryBackend`, which was `getResource()`
    * `responseValidation()`, `timeout()`, `followRedirects()`, `fallbackState()`, and `openTelemetry()` on `RequestOptions`, which were `getResponseValidation()`, `getTimeout()`, `getFollowRedirects()`, `getFallbackState()`, and `getOpenTelemetry()`

    ```java
    // Before
    String filename = file.filename();
    if (filename != null) {}
    String resource = backend.getResource();

    // After
    Optional<String> filename = file.filename();
    if (filename.isPresent()) {}
    Optional<String> resource = backend.resource();
    ```

    `getBaseUrl()` on `FoundryBackend` is removed. Call `baseUrl()`, which returns the URL that requests go to. That is the base URL you set, or the one built from the resource, and it ends in `/anthropic`.

    `getBaseUrl()` on `AnthropicBackend` is removed too. Call `baseUrl()`, which returns the same value.

    **`HttpRequest` requires a base URL.** If you build an `HttpRequest` yourself, such as in a test of an interceptor, set its base URL. Without one, `build()` now throws an `IllegalStateException`. In v2 it returned a request whose `baseUrl()` was `null`. The requests that the SDK builds already had one.

    ```java
    // Before
    HttpRequest request = HttpRequest.builder()
        .method(HttpMethod.GET)
        .build();

    // After
    HttpRequest request = HttpRequest.builder()
        .method(HttpMethod.GET)
        .baseUrl("https://api.anthropic.com")
        .build();
    ```

    `baseUrl()` still returns a `String`, which is now never `null`. On the builder, `baseUrl(Optional<String>)` is removed and `baseUrl(String)` no longer accepts `null`.

    **Interceptors see `anthropic-version`.** The client now adds the default `anthropic-version` header before interceptors run. In v2, the backend added it after them. If your interceptor sets its own version, call `replaceHeaders`, because `putHeader` now adds a second value:

    ```java
    // Before
    request.toBuilder().putHeader("anthropic-version", version).build();

    // After
    request.toBuilder().replaceHeaders("anthropic-version", version).build();
    ```
  </Tab>

  <Tab title="PHP">
    **Enum cases you pass are read back as their values.** `with()` and setters such as `withAllowedCallers()` still take an enum case or its value. Earlier versions kept a case as you passed it. v1 keeps the case's value, which is what the property types already declare. Objects that the SDK builds from a response don't change, and the JSON that the SDK sends is the same. If you read a property back and compare it with a case, the comparison is now false and nothing throws, so compare it with the case's value:

    ```php
    $tool = CodeExecutionTool20250825::with(allowedCallers: [AllowedCaller::DIRECT]);

    // Before
    in_array(AllowedCaller::DIRECT, $tool->allowedCallers, true);

    // After
    in_array(AllowedCaller::DIRECT->value, $tool->allowedCallers, true);
    ```
  </Tab>

  <Tab title="Ruby">
    **`Anthropic::VertexClient::DEFAULT_VERSION` and `Anthropic::BedrockClient::DEFAULT_VERSION` are removed.**
  </Tab>
</Tabs>

### The license is Apache 2.0

Starting with these versions, the SDK and the CLI are licensed under the Apache License, Version 2.0. Earlier versions remain under the MIT License. No code changes are needed. If you track the licenses of your dependencies, update their entries.

* **TypeScript:** The platform packages (`@anthropic-ai/bedrock-sdk`, `@anthropic-ai/vertex-sdk`, `@anthropic-ai/foundry-sdk`, `@anthropic-ai/aws-sdk`, and `@anthropic-ai/google-cloud-sdk`) change license in their own 1.0.0 releases.
* **C#:** The other packages (`Anthropic.Bedrock`, `Anthropic.Vertex`, `Anthropic.Foundry`, `Anthropic.Aws`, `Anthropic.GoogleCloud`, and `Anthropic.Mcp`) change license in their own 1.0.0 releases.
* **Java:** The change covers every `com.anthropic` artifact.
