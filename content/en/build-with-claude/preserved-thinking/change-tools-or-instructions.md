---
title: Change tools or instructions without failing the prefix check
url: https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/change-tools-or-instructions
description: Send an instruction, tool, reminder, or summary, resume a saved conversation, or pass on other people's requests, so that Claude keeps its earlier thinking.
featureMetadata:
  status: stable
  supportedModels:
    - claude-fable-5-2
    - claude-mythos-5-2
    - claude-fable-5-1
    - claude-mythos-5-1
    - claude-opus-5-5
    - claude-sonnet-5-5
    - claude-haiku-5-5
  supportedPlatforms:
    Claude API: stable
    Amazon Bedrock: stable
    Amazon Bedrock (bedrock-runtime): stable
    Claude Platform on AWS: stable
    Claude Models on Google Cloud (Anthropic managed): stable
    Claude Models on Google Cloud (Google managed): stable
    Microsoft Foundry: stable
---

To update tools, instructions, or other context, leave everything you sent as it was, and add the update at the end, where it stays. On models with preserved thinking, changing what you sent can make the thinking after it invalid, and [the request can fail](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/prefix-checks#outcomes).

The models with preserved thinking are Claude Fable 5.2, Claude Mythos 5.2, Claude Fable 5.1, Claude Mythos 5.1, Claude Opus 5.5, Claude Sonnet 5.5, and Claude Haiku 5.5.

## Send assistant turns back exactly

Send back the whole `content` array of each response, in order, including thinking blocks whose text is empty. A block with empty text is complete, because its `signature` holds the reasoning, encrypted. A turn that holds a [`fallback` block](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback#continuing-the-conversation) has its own rule.

[Serializers, filters, and stream parsers](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/change-tools-or-instructions#append-assistant-turns-exactly-as-returned-details) can break this.

## Change instructions

Keep `system` the same on every request. Put your own instructions in a `role: "system"` message at the end, and send one only when something has changed. Claude treats it as an instruction from you, the operator. Leave it for the rest of the conversation, because deleting or rewording it later makes the thinking after it invalid. [Your user’s words](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/change-tools-or-instructions#user-words) have their own rule.

A reminder that must come with every turn is different: [send one that clears itself](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/change-tools-or-instructions#per-turn-reminders).

The system message goes after the newest user message, even one with [tool results](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/change-tools-or-instructions#new-instructions-details). A system message with text or tool blocks gets a 400 error right after Claude’s turn or right before a user message. So when Claude’s turn is last, wait until the next user message is in place.

A system message doesn’t guarantee that Claude follows an instruction, so apply limits such as read-only mode in the code that runs your tools. Some models [don’t accept system messages](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages).

## Text that other people can edit

Ask whether your user would expect Claude to trust a file, such as an `AGENTS.md` or `CLAUDE.md` that other people can edit, or stored memory. If not, send its text only in a `tool_result` block, the first version included. For why, see [Indirect prompt injection](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks#indirect-prompt-injection).

Don’t put such text in a system message or in the text of a user message, and in new conversations, don’t put it in `system`.

When you load such a file or it changes, tell Claude to read it with a tool, and don’t include its text. Or, after the next user message, append the tool call and its result yourself: an `assistant` message with a `tool_use` block, then a `user` message whose `tool_result` block holds the text. For the steps, see [Write the tool call yourself](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/change-tools-or-instructions#write-the-tool-call).

A file that your user expects Claude to follow can go in a user message. An instruction file that only you control can go in a system message: load it once, and append each updated version.

## Update the date, files, or other context

Build `system` and the first message once, and send them unchanged on every request.

Put an updated value in its own text block of the user message you’re about to send, [after any tool results](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/change-tools-or-instructions#user-words):

```json
{
  "role": "user",
  "content": [
    { "type": "text", "text": "Environment update: the current branch is now release-2." },
    { "type": "text", "text": "Run the tests again." }
  ]
}
```

State it only when it changes, and leave it there.

Store any context that your code adds to a message with that message. Otherwise the next request sends something different before the same thinking.

## Add, remove, or turn off tools

Keep `tools` the same on every request. Adding, changing, or removing a tool there, other than [a deferred one](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/change-tools-or-instructions#deferred-tools), makes the thinking already in the conversation invalid, because `tools` comes before all of it. One reworded sentence in a description is enough.

To add or remove a tool, append a system message with a `tool_addition` or `tool_removal` block and [the beta header for your case](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/change-tools-or-instructions#tool-changes-details). Do the same when an MCP server or plugin connects.

To turn tools off for one request, set `tool_choice: {"type": "none"}`, and keep `tools` as it was.

## Trim or summarize older turns

To keep recent turns with their thinking, let the API write the summary with [on-demand compaction](https://platform.claude.com/docs/en/build-with-claude/compaction-on-demand#request-a-summary), under the [conditions for kept thinking](https://platform.claude.com/docs/en/build-with-claude/compaction-thinking-blocks#conditions-for-kept-thinking-to-stay-valid). Start `messages` with the compaction block it returns, and remove the messages it summarizes.

If your own code writes the summary, or cuts older turns without one, [remove the kept turns’ thinking or send `"drop_block"`](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/change-tools-or-instructions#server-side-trimming-details). Each new cut makes the kept turns’ thinking invalid again, so cut rarely, in large steps. To clear old tool results instead, [use context editing](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/change-tools-or-instructions#clear-old-content).

## Save, resume, or fork a conversation

Store what you sent and what you received, and send exactly that. A resumed conversation is an ordinary next request: `system`, `tools`, and earlier `messages` must have the values they had. For a fork, put the branch’s instruction in its first new user message, or in a system message after that. Thinking can’t move to a conversation with a different history: start that conversation from a summary instead.

A release that changes your system prompt or tools is a change in conversations already running. The fix that makes your code append-only can be one too. Keep sending each running conversation the `system` and `tools` of its last successful request, because its newest thinking was produced after that version. Going back to an earlier version would make that thinking invalid.

Use the updated `system` and `tools` in new conversations. If the release removes a tool or changes an instruction for safety, apply it to running conversations too. Append [a `tool_removal` block](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/change-tools-or-instructions#tool-changes) or [a system message](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/change-tools-or-instructions#new-instructions).

## Remove secrets, personal data, or injected text

Safety and privacy come before keeping thinking valid. If a message holds a secret or personal data you must delete, remove that text. Remove it from every message and summary that repeats it, too.

For a tool result with injected instructions, replace its content with a short note such as “Removed.” Keep the `tool_result` block itself, because its `tool_use` needs one. If a [compaction block](https://platform.claude.com/docs/en/build-with-claude/compaction) holds the text, delete the block, and start from your own summary.

Then delete every `thinking` and `redacted_thinking` block after the first place the text appeared. If it was in `system` or `tools`, that’s all of them. Each block can repeat the text, and you can’t read or edit what’s inside. Sending `"drop_block"` isn’t enough here, because it leaves those blocks in your stored history. The conversation carries on without that reasoning.

After an injected result, later turns might already have acted on it. Check the tool calls made since, and undo what you need to.

## Technical details

### Ways code changes assistant turns

* A serializer drops block types it doesn’t know, or reorders, merges, or splits blocks. That changes what came before every later block.
* Code skips thinking blocks that look empty. If it skips all of them, Claude loses that reasoning. If it skips only some, the gap makes the thinking after it invalid.
* A stream parser of your own drops a thinking block that got no text. The SDK’s stream helpers keep it.

### Leave out thinking

Claude loses the reasoning you leave out. Leave out the oldest blocks, the newest, or all of them, but none in between. Each block records the one it was produced after, so a gap makes the blocks after it invalid. Thinking blocks with no other block between them in a turn are checked together, so leave out all of them or none. Once a block is out, keep it out.

While a tool call is open, [send that turn’s thinking back](https://platform.claude.com/docs/en/build-with-claude/thinking#preserving-thinking-blocks), so that Claude finishes the round with its reasoning.

### Your instructions in a tool loop

The messages go in this order:

```json
[
  {
    "role": "assistant",
    "content": [
      { "type": "thinking", "thinking": "", "signature": "..." },
      {
        "type": "tool_use",
        "id": "toolu_01",
        "name": "run_tests",
        "input": { "path": "tests/" }
      }
    ]
  },
  {
    "role": "user",
    "content": [
      { "type": "tool_result", "tool_use_id": "toolu_01", "content": "2 failed, 48 passed" }
    ]
  },
  {
    "role": "system",
    "content": "Plan mode is off. You can edit files."
  }
]
```

### Write the tool call yourself

Declare a tool that reads files on the first request, or [add it later in a system message](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/change-tools-or-instructions#tool-changes), and have your code answer Claude’s calls to it. After the next user message, append an `assistant` message with a `tool_use` block for that tool. Directly after it, append a `user` message whose `tool_result` block has the matching `tool_use_id` and holds the file’s text. Claude answers after that:

```json
[
  { "role": "user", "content": "Run the tests again." },
  {
    "role": "assistant",
    "content": [
      {
        "type": "tool_use",
        "id": "toolu_app_agents_md_1",
        "name": "read_file",
        "input": { "path": "AGENTS.md" }
      }
    ]
  },
  {
    "role": "user",
    "content": [
      {
        "type": "tool_result",
        "tool_use_id": "toolu_app_agents_md_1",
        "content": "The file's text"
      }
    ]
  }
]
```

Leave both in place, and append a new pair, with a new `id`, for each new version.

### Your user’s words, and updated values, in a tool loop

If you pass on what your user typed while Claude was working, add it before you send the user message that carries the `tool_result` blocks. Make it a text block after the last `tool_result`.

A value that comes from you can go in a system message instead. After tool results, Claude Sonnet 5.5 and Claude Haiku 5.5 can ignore a user’s words in a system message as a prompt injection. Claude Sonnet 5.5 can do the same with your own instructions and reminders if they come after every tool result.

The user message with the tool results must hold only `tool_result` blocks when the turn also called a [server tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/handle-tool-calls) that has no result yet, or used programmatic tool calling. Then add the text to the next user message.

### Models that don’t accept system messages

On the Claude API, every model with preserved thinking accepts system messages. For a model that doesn’t, see [When a model doesn’t accept system messages](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking#unchosen-switches-details).

### Send a reminder for one turn

Send a reminder as a [turn-scoped system message](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages#turn-scoped-system-messages): set `clear_at: "next_user_message"`, and send the beta header `mid-conversation-system-clear-at-2026-08-21`. It goes after the user message that carries the `tool_result` blocks:

```json
{
  "role": "system",
  "clear_at": "next_user_message",
  "content": "Run the linter before you report that a task is done."
}
```

At the next user message, even one with only `tool_result` blocks, the API clears it, so Claude stops reading it. On Claude Sonnet 5.5, [don’t send one after every tool result](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/change-tools-or-instructions#user-words). Keep every reminder in your `messages`, cleared or not, unless it [holds something you must remove](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/change-tools-or-instructions#remove-sensitive-content). Removing or rewording one makes the thinking after it invalid.

Without the header, send a plain system message and leave it in place. It never clears, so reminders pile up. On a model that takes no system messages, use a text block in the user message.

### Which block and beta header a tool change needs

For the platforms that take each header, see [Mid-conversation system messages and tool changes](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages).

* **If you know every tool at the start:** Declare them all on the first request, with `defer_loading: true` on those you offer later. Then name the tool in a `tool_addition` or `tool_removal` block of a system message. Beta header: `inline-tools-2026-09-15` or `mid-conversation-tool-changes-2026-07-01`.
* **If you learn of a tool later, or have one whose schema changes:** Define the tool in a `tool_addition` block of a system message. Beta header: `inline-tools-2026-09-15`.
* **If you learn of a tool later, on a platform without the `inline-tools-2026-09-15` header:** Add the tool to the end of `tools` with `defer_loading: true`, which isn’t a change, then offer it by name. Beta header: `mid-conversation-tool-changes-2026-07-01`.
* **If you connect an MCP server through the MCP connector late, on the Claude API:** Define its `mcp_toolset` in a `tool_addition` block. Beta headers: `inline-tools-2026-09-15` and `mcp-client-2026-09-15`.

If an MCP server’s tool list can change, see [Pin an MCP server’s tool list](https://platform.claude.com/docs/en/agents-and-tools/mcp-connector#pin-mcp-tool-list).

This system message offers a declared tool by name and defines another, which needs `inline-tools-2026-09-15`:

```json
{
  "role": "system",
  "content": [
    {
      "type": "tool_addition",
      "tool": { "type": "tool_reference", "name": "search_tickets" }
    },
    {
      "type": "tool_addition",
      "tool": {
        "type": "tool_definition",
        "definition": {
          "name": "get_weather",
          "description": "Get the current weather in a city.",
          "input_schema": {
            "type": "object",
            "properties": { "city": { "type": "string" } },
            "required": ["city"]
          }
        }
      }
    }
  ]
}
```

### Tools with `defer_loading`, and the 400 error that names it

A tool with `defer_loading: true` stays out of Claude’s context and the prefix check until a message or tool search result refers to it. Until then, adding, updating, or removing it isn’t a change. Afterward it is. Turning `defer_loading` on or off counts as changing `tools`, too.

Declare at least one tool that isn’t deferred, or the request can get a 400 error that names `defer_loading`.

### Shorten or clear old results and images

Shorten or downscale a tool result or image before you first send it. If your code clears, shortens, or re-encodes something it already sent, the thinking after it becomes invalid. To clear old tool results later, including any images inside them, use context editing. Send `context_management` with an edit of type `clear_tool_uses_20250919`, and the beta header `context-management-2025-06-27`. For the full request and its options, see [Context editing](https://platform.claude.com/docs/en/build-with-claude/context-editing#tool-result-clearing).

### Files you send by URL

For a file by URL, the API compares the bytes it fetched. So when a signed URL expires, a fresh one for the same file is fine. If the content behind a URL can change, send a `file_id` or base64 from the first request.

### If your own code summarizes or cuts older turns

After your own summary or cut, a kept turn’s thinking fails the [prefix check](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/prefix-checks#prefix-check), because the messages it followed are gone. Remove that thinking, or [send `"drop_block"`](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/prefix-checks#preserved-thinking-controls). Claude still reads the turn without it.

### Libraries, proxies, and gateways

If other people’s requests pass through your code, your rewrites change their history, and they might not be able to see or fix those changes. Don’t hide the 400 error. If you recover for the caller, say so, because their history still holds the change.

* Pass `anthropic-beta` values and `thinking.block_binding` through as sent. If your gateway allows only known fields, add `thinking.block_binding` and the header value `thinking-binding-controls-2026-08-01`, or your users can’t choose `"drop_block"`.
* Don’t remove the beta header and forward the setting. That request gets a 400 error.
* Return thinking blocks whose text is empty, and the `input_transformations` array, to the caller.
* Leave a `role: "system"` message where it is. Moving it into `system` makes the thinking already in the conversation invalid.
* Test with [`prefix_mismatch_behavior`](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/prefix-checks#preserved-thinking-controls) set to `"error"`, which gives the error on every model with preserved thinking.

## Next steps

<CardGroup cols={2}>
  <Card title="Preserved thinking" icon="book" href="https://platform.claude.com/docs/en/build-with-claude/preserved-thinking">
    What preserved thinking is, what a thinking block is tied to, and switching models or accounts.
  </Card>

  <Card title="Fix a thinking block bound to a different conversation" icon="wrench" href="https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/fix-bound-to-a-different-conversation">
    Recover a failing conversation, and see what dropping thinking costs.
  </Card>

  <Card title="Mid-conversation system messages and tool changes" icon="message" href="https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages">
    Where system messages and tool changes go, and which models and platforms take them.
  </Card>
</CardGroup>
