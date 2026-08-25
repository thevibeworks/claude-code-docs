> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Code in Claude Desktop on 3P

> How Claude Desktop on 3P configuration applies to the embedded Claude Code engine

Code in Claude Desktop on third-party (3P) is the embedded [Claude Code](https://code.claude.com/docs/en/overview) interface. It runs the same Claude Code engine as the standalone CLI, with a graphical session manager, and it inherits your Claude Desktop on 3P configuration automatically.

## How configuration propagates

When the app starts a Code session, it translates your Claude Desktop on 3P [configuration keys](/docs/third-party/claude-desktop/configuration) into the equivalent Claude Code settings and passes them to the session. You configure one profile, and Cowork and Code both honor it.

Each key reaches Claude Code through one of two mechanisms, and the distinction matters if you also deploy Claude Code's own managed settings (see [the next section](#interaction-with-claude-code%E2%80%99s-own-managed-settings)).

### Always applied

These keys are passed directly to the Claude Code process as environment variables or launch options. They take effect on every Code session and cannot be overridden by user-level Claude Code settings or by a separately deployed `managed-settings.json`.

| Claude Desktop on 3P key                                                                                                                                               | Effect in Code sessions                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `inferenceProvider` and all provider credential keys (`inferenceGateway*`, `inferenceVertex*`, `inferenceBedrock*`, `inferenceFoundry*`, `inferenceCredentialHelper*`) | Selects the inference backend and supplies credentials. Code sessions use the same provider, endpoint, and credentials as Cowork sessions.                                                                               |
| `inferenceModels`                                                                                                                                                      | Populates the model picker. The first entry is the default for new Code sessions.                                                                                                                                        |
| `autoModeEnabled`                                                                                                                                                      | Offers **Auto mode** in the Code session's permission selector. A separately deployed Claude Code managed-settings file that sets `disableAutoMode` to `"disable"` overrides this and keeps Auto mode hidden; see below. |
| `disabledBuiltinTools`                                                                                                                                                 | Removes the listed tools from Code sessions. Tools your provider does not support, such as WebSearch on Amazon Bedrock, are removed automatically in addition to your list.                                              |
| `builtinToolPolicy`                                                                                                                                                    | Tools set to `"ask"` require approval on each call in Code sessions, enforced via a PreToolUse hook and Claude Code `permissions.ask` rules.                                                                             |
| `managedMcpServers`                                                                                                                                                    | Makes the same managed MCP servers available in Code sessions. The app handles the connection and authentication; the Code session sees only the resulting tool list.                                                    |
| `otlpEndpoint`, `otlpProtocol`, `otlpHeaders`, `otlpResourceAttributes`                                                                                                | Routes Claude Code's OpenTelemetry metrics and logs to your collector. See [Telemetry](/docs/third-party/claude-desktop/telemetry).                                                                                           |
| `disableEssentialTelemetry`, `disableNonessentialTelemetry`                                                                                                            | Disables Claude Code's crash reporting and usage telemetry to Anthropic, mirroring Cowork.                                                                                                                               |
| `disableAutoUpdates`                                                                                                                                                   | The embedded Claude Code engine never self-updates regardless of this key; its version is managed by the app's own updater.                                                                                              |
| `inferenceMaxTokensPerWindow`, `inferenceTokenWindowHours`                                                                                                             | The token budget is shared across Cowork and Code sessions and enforced before each turn.                                                                                                                                |

### Applied as managed policy

These keys are translated into Claude Code [managed settings](https://code.claude.com/docs/en/settings#settings-files) and supplied to the session as policy. They take precedence over user and project settings, but they participate in Claude Code's managed-settings precedence if you have also deployed a separate Claude Code policy.

| Claude Desktop on 3P key   | Claude Code policy it produces                                                                                                                                                                                                                                                                                                                               |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `coworkEgressAllowedHosts` | A network sandbox restricted to your hosts plus the inference and telemetry endpoints, `WebFetch` permission rules for the same hosts, and `allowManagedDomainsOnly`.                                                                                                                                                                                        |
| `allowedWorkspaceFolders`  | A filesystem sandbox (`sandbox.filesystem.allowRead` with `allowManagedReadPathsOnly`) scoped to your allowed roots. The roots are also passed as `additionalDirectories` at launch, which is always applied independent of managed-settings precedence. The app also refuses to start a Code session outside an allowed root.                               |
| `managedMcpServers`        | An `allowedMcpServers` list containing only your managed servers, with `allowManagedMcpServersOnly` set so users cannot add their own from Claude Code's side. Per-tool `toolPolicy` values on each server are emitted as `permissions.deny` (for `blocked`) or `permissions.ask` (for `ask`) rules against the corresponding `mcp__<server>__<tool>` names. |

## Interaction with Claude Code's own managed settings

Claude Code can also be configured directly by deploying a [`managed-settings.json` file](https://code.claude.com/docs/en/settings#settings-files), an OS configuration profile for Claude Code, or (with Anthropic authentication) server-managed settings. If a device has any of these, Claude Code treats it as the administrator policy and, by default, **ignores** the policy values Claude Desktop supplies from the [Applied as managed policy](#applied-as-managed-policy) table. The [Always applied](#always-applied) keys are unaffected.

To have Claude Desktop's restrictions apply on top of your Claude Code policy, set `parentSettingsBehavior` to `"merge"` in the Claude Code managed settings you deploy:

```json managed-settings.json theme={null}
{
  "parentSettingsBehavior": "merge"
}
```

With `"merge"`, Claude Desktop's policy values are layered under your Claude Code policy. Your values win any conflict, deny and allow lists are unioned, and Claude Desktop's values are filtered so they can only tighten policy, never loosen it. See [`parentSettingsBehavior`](https://code.claude.com/docs/en/settings-reference#parentsettingsbehavior) in the Claude Code settings reference. Requires Claude Code v2.1.133 or later, which ships with Claude Desktop on 3P.

<Note>
  In a third-party deployment there is no Anthropic authentication, so Claude Code's server-managed settings tier is never present. If you have not separately deployed a Claude Code `managed-settings.json` or OS profile, Claude Desktop's policy applies automatically and you do not need to set `parentSettingsBehavior`.
</Note>

## Further reading

* [Claude Code settings reference](https://code.claude.com/docs/en/settings-reference)
* [Claude Code sandboxing](https://code.claude.com/docs/en/sandboxing)
* [Settings precedence](https://code.claude.com/docs/en/settings#settings-precedence)

## Disabling Code

To turn off Code, set `isClaudeCodeForDesktopEnabled` to `false` in your Claude Desktop on 3P configuration. Users can no longer open Code. Cowork is unaffected, and so is [Chat](/docs/third-party/claude-desktop/chat#configuration) if you have enabled it.
