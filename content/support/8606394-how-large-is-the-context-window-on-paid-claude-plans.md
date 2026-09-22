# How large is the context window on paid Claude plans?

This article explains how large the context window is on paid Claude plans (Pro, Max, Team, Enterprise) when you chat with Claude, or use Claude Code or Claude Cowork.

## Chatting with Claude

| **Model**         | **Context window** |
| ----------------- | ------------------ |
| Claude Fable 5.1  | 1M tokens          |
| Claude Fable 5    | 500K tokens        |
| Claude Opus 5.5   | 1M tokens          |
| Claude Opus 5     | 1M tokens          |
| Claude Opus 4.8   | 500K tokens        |
| Claude Opus 4.7   | 500K tokens        |
| Claude Opus 4.6   | 500K tokens        |
| Claude Sonnet 5   | 1M tokens          |
| Claude Sonnet 4.6 | 500K tokens        |

Outside of these models, Claude’s context window size is 200K, meaning it can ingest 200K+ tokens (about 500 pages of text or more) when using a paid Claude plan to chat with Claude.

## Claude Code

| **Model**         | **Context window**                                                                                                                                                                       |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Claude Fable 5.1  | 1M tokens                                                                                                                                                                                |
| Claude Fable 5    | 1M tokens                                                                                                                                                                                |
| Claude Opus 5.5   | 1M tokens                                                                                                                                                                                |
| Claude Opus 5     | 1M tokens                                                                                                                                                                                |
| Claude Opus 4.8   | 1M tokens                                                                                                                                                                                |
| Claude Opus 4.7   | 1M tokens                                                                                                                                                                                |
| Claude Opus 4.6   | 1M tokens<br>**Note:** 1M context window available by selecting `claude-opus-4-6[1m]` with `/model`; on Pro, usage credits must be enabled to access                                     |
| Claude Sonnet 5   | 1M tokens                                                                                                                                                                                |
| Claude Sonnet 4.6 | 1M tokens<br>**Note:** 1M context window available by selecting `claude-sonnet-4-6[1m]` with `/model`; usage credits must be enabled to access (except for usage-based Enterprise plans) |

## Claude Cowork

| **Model**         | **Context window**                                                                     |
| ----------------- | -------------------------------------------------------------------------------------- |
| Claude Fable 5.1  | 1M tokens                                                                              |
| Claude Fable 5    | 1M tokens                                                                              |
| Claude Opus 5.5   | 1M tokens                                                                              |
| Claude Opus 5     | 1M tokens                                                                              |
| Claude Opus 4.8   | 1M tokens                                                                              |
| Claude Opus 4.7   | 1M tokens                                                                              |
| Claude Opus 4.6   | 200K tokens                                                                            |
| Claude Sonnet 5   | 1M tokens<br>**Note:** Sonnet 5 automatically compacts the conversation at 500K tokens |
| Claude Sonnet 4.6 | 200K tokens                                                                            |
| Haiku 4.5         | 200K tokens                                                                            |

## Automatic context management

For users on paid plans with code execution enabled, Claude automatically manages your conversation context. When your conversation approaches the context window limit, Claude summarizes earlier messages to make room for new content. This allows conversations to continue indefinitely in most cases. Longer conversations that trigger automatic context management use more of your usage limit.

Your full chat history is preserved so Claude can reference it, even after earlier portions have been summarized. You may occasionally notice Claude "organizing its thoughts" during long conversations—this is the automatic context management at work.

**Note:** Code execution must be enabled for automatic context management to work. In rare edge cases (such as very large first messages or system errors), you may still encounter context window limits.

## Maximizing your context window

While context is managed automatically for most conversations, you can still optimize how you use your available context space:

- **Utilize projects effectively:** Projects use retrieval-augmented generation (RAG), which allows Claude to work with larger amounts of information by only loading relevant content into the context window.

- **Keep project instructions concise:** Claude performs best when you use project instructions for general context around your project, key guidelines, and Claude's role.

- **Manage tools and connectors:** These features are token-intensive, so being mindful of how many you have active helps maximize your available context.