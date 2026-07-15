# How large is the context window on paid Claude plans?

Claude Sonnet 5 supports a 1M token context window on all paid plans when chatting with Claude. Claude Opus 4.8, Opus 4.7, Opus 4.6, and Sonnet 4.6 support a 500K token context window on all paid plans when chatting with Claude. Outside of these models, Claude’s context window size is 200K, meaning it can ingest 200K+ tokens (about 500 pages of text or more) when using a paid Claude plan.

When using Claude Code with a Pro, Max, Team, or Enterprise plan, Claude Sonnet 5, Fable 5, Opus 4.8, Opus 4.7, and Opus 4.6 support a 1M token context window. Pro users need to enable usage credits to access the 1M token context window for Opus models. Sonnet 4.6 also supports a 1M context window for all paid Claude plans on Claude Code, but usage credits must be enabled to access it (except for usage-based Enterprise plans).

## Automatic context management

For users on paid plans with code execution enabled, Claude automatically manages your conversation context. When your conversation approaches the context window limit, Claude summarizes earlier messages to make room for new content. This does not count towards your usage limit, and allows conversations to continue indefinitely in most cases.

Your full chat history is preserved so Claude can reference it, even after earlier portions have been summarized. You may occasionally notice Claude "organizing its thoughts" during long conversations—this is the automatic context management at work.

**Note:** Code execution must be enabled for automatic context management to work. In rare edge cases (such as very large first messages or system errors), you may still encounter context window limits.

## Maximizing your context window

While context is managed automatically for most conversations, you can still optimize how you use your available context space:

- **Utilize projects effectively:** Projects use retrieval-augmented generation (RAG), which allows Claude to work with larger amounts of information by only loading relevant content into the context window.

- **Keep project instructions concise:** Claude performs best when you use project instructions for general context around your project, key guidelines, and Claude's role.

- **Manage tools and connectors:** These features are token-intensive, so being mindful of how many you have active helps maximize your available context.