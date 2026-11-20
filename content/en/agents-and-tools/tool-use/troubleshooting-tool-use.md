---
title: Troubleshooting tool use
url: https://platform.claude.com/docs/en/agents-and-tools/tool-use/troubleshooting-tool-use
description: Fix the most common tool-use errors with symptom-to-fix diagnostic tables.
---

Find the symptom or error you see, and then apply the fix listed for it.

## Claude calls the wrong tool

| Symptom | Likely cause | Fix |
| ----- | ----- | ----- |
| Claude calls tool A when you wanted tool B | Description ambiguity | Sharpen descriptions. Differentiate tools by WHEN to use them, not only WHAT they do. See [Define tools](https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools). |
| Claude never calls your tool | Tool name collision or overly generic schema | Check for duplicate names across your tool list. Add `input_examples` to make the intended use concrete. |
| Claude calls with wrong parameter types | Ambiguous schema | Add `strict: true` (if your schema is in the supported subset) or add `input_examples`. |

## Claude invents tool parameters

| Symptom | Likely cause | Fix |
| ----- | ----- | ----- |
| Parameter that doesn’t exist in your schema | Model over-generation without strict mode | Add `strict: true` if your schema is in the [supported subset](https://platform.claude.com/docs/en/agents-and-tools/tool-use/strict-tool-use). |
| Parameter values outside your enum | Missing strict mode or too-large enum | Shrink the enum or add `input_examples` showing valid choices. |

## Parallel tool calls don’t work

| Symptom | Likely cause | Fix |
| ----- | ----- | ----- |
| Claude calls tools sequentially when parallel would be better | Message history formatting | Send multiple `tool_result` blocks in ONE user message, not one per turn. See [Parallel tool use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/parallel-tool-use). |
| `disable_parallel_tool_use` seems ignored | Set too late in the conversation | Set it on the request that returns `tool_use`. Setting it on a later request has no effect on earlier tool calls. |

## Cache keeps invalidating

| Symptom | Likely cause | Fix |
| ----- | ----- | ----- |
| Every request is a cache miss | `tool_choice`, the thinking configuration, or `output_config.effort` varying between requests | Keep `tool_choice` stable or place the `cache_control` breakpoint before the variation point; hold the thinking configuration and effort level constant for the life of a cached conversation. See [Tool use with prompt caching](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-use-with-prompt-caching) and [Thinking and prompt caching](https://platform.claude.com/docs/en/build-with-claude/thinking#thinking-and-prompt-caching). |
| Adding a tool mid-conversation breaks cache | Tool prepended to the tools array | Declare the tool with `defer_loading: true` from the first request and let tool search load it inline, instead of adding it to the array later. |

## Errors at request time

The Error column shows part of each message, and `...` stands for text that varies.

| Error | Cause | Fix |
| ----- | ----- | ----- |
| `tool_use ids were found without tool_result blocks immediately after` | Missing `tool_result` for some `tool_use` IDs, or `tool_result` is not the first content block in the user message | Return one `tool_result` for every `tool_use` block in the assistant response. Put `tool_result` blocks before any text. See [Handle tool calls](https://platform.claude.com/docs/en/agents-and-tools/tool-use/handle-tool-calls) and [Parallel tool use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/parallel-tool-use). |
| `was found without a corresponding ... block` | The follow-up request keeps a waiting server tool from running | See [A server tool call has no result block](https://platform.claude.com/docs/en/agents-and-tools/tool-use/troubleshooting-tool-use#a-server-tool-call-has-no-result-block). |
| `Unsupported regex feature in pattern field: ...` | A strict tool’s `pattern` uses a regex feature that strict mode can’t compile, such as a backreference, a word boundary, or a large `{n,m}` range | Simplify the pattern. See [JSON Schema limitations](https://platform.claude.com/docs/en/build-with-claude/structured-outputs#json-schema-limitations). |
| `Invalid regex in pattern field: ...` | A strict tool’s `pattern` has a lookahead, a lookbehind, or a syntax error | Remove any lookahead or lookbehind and fix any syntax errors. See [JSON Schema limitations](https://platform.claude.com/docs/en/build-with-claude/structured-outputs#json-schema-limitations). |
| `All tools have defer_loading: true` | No tools visible to the model | At least one tool must be immediately loaded. The tool search tool itself must never have `defer_loading: true`. |

### A server tool call has no result block

A [server tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/server-tools) is still waiting to run when its `server_tool_use` or `mcp_tool_use` block has no result block. The error `was found without a corresponding ... block` means the follow-up request keeps the waiting tool from running. The error message and the previous `stop_reason` show why. Use the first case that matches:

* **The message ends with ``but no `<name>` tool was provided`` or `is not available after the last message`:** Here, `<name>` is the tool’s name, such as `web_search`. The request no longer defines the tool. Send the same `tools` array as before, and the same `mcp_servers` for an MCP tool.
* **The previous `stop_reason` was `tool_use`:** Your user message had content after the `tool_result` blocks. Send only the `tool_result` blocks, one for each client `tool_use` block.
* **The previous `stop_reason` was `pause_turn`:** You added a user message. Remove it so that the request ends with the paused response as an `assistant` message.

For the full steps, see [When a server tool is still waiting](https://platform.claude.com/docs/en/build-with-claude/handling-stop-reasons#when-a-server-tool-is-still-waiting) and the [`pause_turn` stop reason](https://platform.claude.com/docs/en/build-with-claude/handling-stop-reasons#pause-turn).

## Error: thinking blocks cannot be modified

If a request fails with a 400 `invalid_request_error` whose message contains `` `thinking` or `redacted_thinking` blocks in the latest assistant message cannot be modified `` when continuing a conversation after a tool call, your application is altering the assistant’s thinking blocks before sending them back. Send the entire assistant message back unchanged, then append your `tool_result`.

See [Thinking blocks cannot be modified](https://platform.claude.com/docs/en/api/errors#thinking-blocks-cannot-be-modified) for the full error and fix steps.

## Claude flags tool results as prompt injection

| Symptom | Likely cause | Fix |
| ----- | ----- | ----- |
| Claude refuses to act on a tool result, or asks the user to confirm instructions that came from it | Your own instructions are being delivered inside the `tool_result` content | Claude is trained to treat instructions inside tool results as potentially untrusted third-party content. Move your instructions out of the tool result: send them in a `user` turn after the `tool_result` block, or, on supported models, in a [mid-conversation system message](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages). Keep the tool result to just the data. See [Mitigate jailbreaks and prompt injections](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks#indirect-prompt-injection). |

## JSON escaping differences between model versions

| Symptom | Cause | Fix |
| ----- | ----- | ----- |
| String comparison on tool inputs fails with newer models | Unicode and forward-slash escaping differs between model versions | Parse with `json.loads()` or `JSON.parse()`. Never do raw string matching on serialized input. |

## Next steps

<CardGroup cols={3}>
  <Card title="Define tools" href="https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools">
    Write schemas and descriptions that steer Claude toward the right tool.
  </Card>

  <Card title="Handle tool calls" href="https://platform.claude.com/docs/en/agents-and-tools/tool-use/handle-tool-calls">
    Run tools and return results in the required message format.
  </Card>

  <Card title="Tool reference" href="https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-reference">
    Full directory of Anthropic-provided tools and their version strings.
  </Card>
</CardGroup>
