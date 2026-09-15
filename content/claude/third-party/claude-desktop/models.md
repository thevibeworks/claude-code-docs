> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Models and effort levels

> Which models Claude Desktop on 3P offers, the default model and its starting effort level, per-model effort caps, display names, and 1M-context variants

Claude Desktop on third-party (3P) builds the model picker in Chat, Cowork, and Code from your configuration. Your configuration decides which models the picker offers, which model and effort level each new conversation starts with, and which effort levels users can choose. You control all three with the keys under **Models** in the [in-app configuration window](/docs/third-party/claude-desktop/in-app-configuration). The [configuration reference](/docs/third-party/claude-desktop/configuration#models) lists every field.

## Model list and default model

[`inferenceModels`](/docs/third-party/claude-desktop/configuration#inferencemodels) lists the models the picker offers. Write each entry with the exact model ID your provider expects, such as `us.anthropic.claude-sonnet-5` on Amazon Bedrock or `claude-sonnet-5` on Google Cloud's Agent Platform. The first entry is the default model. New Chat conversations, Cowork sessions, and Code sessions start on the default model until a user picks another model. To control whether a user's choice carries over to later conversations and sessions, see [Start every conversation on the default model](#start-every-conversation-on-the-default-model).

If you leave `inferenceModels` unset and your provider supports [model discovery](/docs/third-party/claude-desktop/configuration#modeldiscoveryenabled), Claude Desktop fills the picker from the provider's model list at launch. The first discovered model is then the default model.

Each entry is either a model ID string or an object. In an object, `name` holds the model ID and every other field is optional. Two of the optional fields change how the picker shows the model:

* `labelOverride` sets the display name for an ID the picker can't turn into a readable name, such as a gateway routing alias or an Amazon Bedrock application inference profile ARN. Claude Desktop still sends `name` to your provider.
* `supports1m: true` adds a second entry that shows the same name with **1M context window** beneath it. Set it only when your deployment accepts 1M-token requests for that model. Otherwise, requests from the 1M entry fail at the provider. Add `prefer1m: true` to the default model's entry to make its 1M entry the default selection. Users can still choose the standard entry.

## Effort levels

An effort level sets how much thinking Claude puts into each response. Higher levels give more thorough answers but take longer and use more tokens. Users choose the level with the **Effort** control in the model picker.

Each model starts at Anthropic's recommended level unless you configure otherwise. The **Effort** control marks the recommended level **Default**.

### Per-model effort cap

[`maxEffort`](/docs/third-party/claude-desktop/configuration#inferencemodels) on an `inferenceModels` entry sets the highest effort level Claude Desktop offers for that model in Chat, Cowork, and Code. Set it to `low`, `medium`, `high`, `xhigh`, or `max`. The picker shows `xhigh` as **Extra**. The **Effort** control doesn't offer levels above the cap.

In Code sessions, the cap also limits Claude Code's own effort settings, such as a `CLAUDE_CODE_EFFORT_LEVEL` environment variable or the `/effort` command. If a model's recommended level is above its cap, the model starts at the cap. If Claude Desktop doesn't recognize the `maxEffort` value, it caps the model at low.

### Starting effort level for the default model

[`defaultModelEffort`](/docs/third-party/claude-desktop/configuration#defaultmodeleffort) sets the effort level the default model starts at, in place of its recommended level. Other models keep their recommended level. If you set a level the default model doesn't offer, or one above its `maxEffort`, the default model starts at the nearest lower level it offers.

`defaultModelEffort` also applies when [model discovery](/docs/third-party/claude-desktop/configuration#modeldiscoveryenabled) fills the picker instead of an `inferenceModels` list.

### Models without an Effort control

Some model IDs, such as a gateway routing alias, don't name a specific Claude model. For such a model, the picker shows no **Effort** control, so users can't change its effort level. Its conversations and sessions never run above the `maxEffort` on its entry. When such a model is the default model, its conversations and sessions run at [`defaultModelEffort`](/docs/third-party/claude-desktop/configuration#defaultmodeleffort), up to that cap. With only `maxEffort` set, they run at that cap.

## Start every conversation on the default model

Set [`alwaysStartWithDefaultModel`](/docs/third-party/claude-desktop/configuration#alwaysstartwithdefaultmodel) to `true` to start every new Chat conversation, Cowork session, and Code session on the [default model](#model-list-and-default-model) at its [starting effort level](#effort-levels), not on the user's last choice. When the user picks a model or effort level, it applies only for that conversation or session.

If you leave `alwaysStartWithDefaultModel` unset, the default model and its starting effort level apply until a user picks a different model or effort level. Claude Desktop remembers that choice and starts the user's new conversations and sessions from it.

When you turn the setting on, Claude Desktop keeps the choices users saved earlier. If you later turn it off, those choices apply again.

`alwaysStartWithDefaultModel` also applies when [model discovery](/docs/third-party/claude-desktop/configuration#modeldiscoveryenabled) fills the picker instead of an `inferenceModels` list.

## Example configuration

The following configuration offers Claude Sonnet 5, with a 1M-context variant, and Claude Opus 5. It makes Claude Sonnet 5 the default model at medium effort, caps both models at high effort, and starts every new conversation and session from those defaults:

```json theme={null}
{
  "inferenceModels": [
    { "name": "claude-sonnet-5", "supports1m": true, "maxEffort": "high" },
    { "name": "claude-opus-5", "maxEffort": "high" }
  ],
  "defaultModelEffort": "medium",
  "alwaysStartWithDefaultModel": true
}
```

With this configuration, a user who starts a new Cowork session sees Claude Sonnet 5 selected at medium effort. The **Effort** control offers low, medium, and high for every entry.

In that session, the user can switch to Claude Opus 5, which starts at its recommended high effort, or raise Claude Sonnet 5 to high. The session keeps either choice. The user's next new conversation or session opens on Claude Sonnet 5 at medium effort again.

The example is plain JSON, which is the form a [bootstrap server](/docs/third-party/claude-desktop/bootstrap) response and the Linux managed file use. For a macOS profile or the Windows registry, encode the same values as the [Value types](/docs/third-party/claude-desktop/configuration#value-types) section describes.
