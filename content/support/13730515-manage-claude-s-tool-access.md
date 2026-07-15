# Manage Claude’s tool access

When you connect many services to Claude, you can control how those connectors are loaded into your conversations. This helps Claude work more accurately and efficiently, especially if you've added 10 or more connectors.

Tool access modes are available for all users on Claude, Cowork, Claude Desktop, and Claude Mobile (iOS and Android).

## Why tool access matters

Each connector takes up space in a conversation. With a small number of connected services, this is rarely noticeable. But as your connector library grows, the combined overhead can limit how much room is left for your actual work: documents, code, and conversation history.

To address this, Claude supports three tool access modes that control when and how your connectors are loaded.

---

## Tool access modes

You can manage Claude’s access to your connectors per conversation using the **Tool access** setting in your chat.

Choose from three options:

- **Auto** *(default)*: Claude decides dynamically which connectors to load based on what you're working on. This is the best starting point for most users.

- **Always available**: All your connectors are loaded at the start of every conversation. Claude can use any of them immediately, without any extra steps.

  - Best for: Fewer than 10 connectors you use constantly.

  - Trade-off: Uses more conversation space upfront.

- **On demand:** Connectors aren't loaded until Claude searches for the right one based on your request. Claude finds the most relevant connectors and loads only those.

  - Best for: Large connector libraries (10 or more), or when you're running into conversation length issues.

  - Trade-off: Claude may take an extra step to find the right connector before using it.

---

## Which mode should I use?

| **Your situation**                                         | **Recommended mode** |
| ---------------------------------------------------------- | -------------------- |
| Fewer than 10 connectors, all used frequently              | Always available     |
| 10–30 tools with mixed usage                               | Auto                 |
| 30+ tools or multiple connectors connected                 | On demand or Auto    |
| A specific connector needs to work every time without fail | Always available     |
| Conversations are hitting length limits                    | On demand            |

---

## How to change your tool access setting

You can set your tool access mode per conversation by following these steps:

1. Open a chat with Claude.

2. Click the “+”  button in the lower left corner of your chat, or type "/" to open the menu.

3. Mouse over “Connectors,” then “Tool access.”

4. Select your preferred mode from the three options.

Your selection only applies to that conversation. You can change it at any time.

---

## Frequently asked questions

### Will “On demand” mode miss the connectors I need?

Claude searches for the most relevant connectors based on your request, so it works well for most tasks. For connectors that need to be available every time, use “Always available” or set that connector's access individually.

### Why does Claude sometimes add an extra message to use a connector?

In “On demand” mode, Claude searches for the right tool before using it. This search step adds one interaction, but keeps your conversation from hitting length limits when you have many tools connected.