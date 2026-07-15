# How do usage and length limits work?

When working with Claude, you may encounter two different types of limits that work in distinct ways: **usage limits** and **length limits**. Understanding the difference between these can help you use Claude more effectively.

## What are usage limits?

Usage limits control how much you can interact with Claude over a specific time period. Think of this as your "conversation budget" that determines how many messages you can send to Claude, or how long you can work with Claude Code, before needing to wait for your limit to reset.

Your usage is affected by several factors, including the length and complexity of your conversations, the features you use, which Claude model you're chatting with, and the effort level you've selected. Different subscription plans (Pro, Max, Team, etc.) have different usage allowances, with paid plans offering higher limits.

Note that your usage of all different Claude product surfaces (claude.ai, Claude Code, Claude Desktop) counts towards the same usage limit.

Learn more about **[changing the model, effort, and thinking settings](https://support.claude.com/en/articles/8664678)**.

## How can I get unlimited usage?

There are a couple of different ways to increase your usage depending on your plan:

- If you're using a paid plan, including Pro, Max, Team, or seat-based Enterprise plans, see these articles for details about purchasing usage credits:

  - **[Manage usage credits for paid Claude plans](https://support.claude.com/en/articles/12429409-)**

  - **[Manage usage credits for Team and seat-based Enterprise plans](https://support.claude.com/en/articles/12005970-)**

- If your organization has a usage-based Enterprise plan, your usage is based on consumption. See this article for additional information: **[How am I billed for my Enterprise plan?](https://support.claude.com/en/articles/11526368-how-am-i-billed-for-my-enterprise-plan)**

For strategies to maximize your message allotment, see **[Usage limit best practices](https://support.claude.com/en/articles/9797557-usage-limit-best-practices)**.

## What are length limits?

Length limits relate to Claude's context window—the amount of information Claude can work with in a single chat. Think of the context window as Claude's working memory that determines how much content it can process and remember at once.

**Note**: The context window size depends on which model you're using. On paid plans, the newest models support up to a 1M token context window, while others support 500K or 200K tokens. A portion of the context window is always reserved for Claude's response, so the longest possible conversation is slightly smaller than the full window. For the current per-model breakdown, refer to **[How large is the context window on paid Claude plans?](https://support.claude.com/en/articles/8606394-how-large-is-the-context-window-on-paid-claude-plans)**

## Automatic context management

For users with code execution enabled, Claude now automatically manages long conversations. When your conversation approaches the context window limit, Claude summarizes earlier messages to continue the conversation seamlessly. This means you can have longer, more natural conversations with fewer interruptions.

Your full chat history is preserved so Claude can reference it even after summarization. You may occasionally see that Claude is "organizing its thoughts" during long conversations—this indicates automatic context management is working.

Longer conversations that trigger automatic context management consume more of your usage limit. Try starting a new conversation if you're approaching your usage limit in a longer chat.

**Note:** **[Code execution must be enabled](https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude#h_1c99382190)** for automatic context management. Rare edge cases (such as very large first messages) may still encounter context limits.

## How can I increase the size of Claude’s context window?

While you can't increase the fixed context window size for your plan, you can use these strategies to maximize available context space and optimize both your context window and usage limits:

- **Utilize projects effectively:** Projects use retrieval-augmented generation (RAG), which allows Claude to work with larger amounts of information more efficiently by only loading relevant content into the context window.

- **Shorten project instructions:** Keep your project instructions concise and focused on essential information. Claude performs best when you use project instructions for general context around your project, key guidelines, and Claude's role. Reserve task-specific instructions for the chat itself.

- **Remove unused project files:** Regularly clean up files you're no longer actively using in your projects.

- **Toggle extended thinking off:** Turn off this feature when you don't need Claude's enhanced reasoning for a particular task.

- **Lower the effort level:** Choose a lower effort level for routine tasks that don't need Claude's most thorough responses. Higher effort uses more tokens.

- **Temporarily disable non-critical tools and connectors:** Disable web search, Research, and MCP connectors from your "Search and tools" settings when they're not needed for specific conversations.

**Note:** Tools and connectors are token-intensive, so managing them helps both maximize your available context window and optimize your usage limits.

## Key differences

The main distinction is that usage limits control *how much* you can use Claude across all your conversations, while length limits control *how long* any single conversation can become. Usage limits are about quantity over time, while length limits are about the depth and complexity of individual conversations.

If you hit your usage limit, you'll need to wait for it to reset, upgrade your plan, or purchase usage credits. If you hit a length limit, you can start a new conversation or use **[features like projects](https://support.claude.com/en/articles/9517075-what-are-projects)** to work with larger amounts of information more efficiently.