# Usage limit best practices

The number of messages you can send will vary based on your Claude plan. For more information on your plan’s usage, refer to the following resources.

- **[Free Claude](https://support.claude.com/en/articles/8114491-getting-started-with-claude#h_57262af5ae)**

- **[Pro plan](https://support.claude.com/en/articles/8325606-what-is-the-pro-plan#h_62ccc00135)**

- **[Max plan](https://support.claude.com/en/articles/11049741-what-is-the-max-plan#h_cfd2904008)**

- **[Team plan](https://support.claude.com/en/articles/9266767-what-is-the-team-plan#h_b59203dff2)**

- **[Enterprise plan](https://support.claude.com/en/articles/9797531-what-is-the-enterprise-plan#h_8294bce903)**

Additional factors that affect your usage limits include:

- Message length

- File attachment size

- Current conversation length

- Tool usage (e.g., Research, web search)

- Model choice

- Effort level

- Artifact creation and usage

Our system also includes caching that helps you optimize your limits:

- Content in projects is cached and doesn't count against your limits when reused.

- Similar prompts you use frequently are partially cached.

- Claude remembers context from earlier in the conversation.

---

## 1. Start by planning your conversations

Before starting a conversation with Claude, consider the following:

- What specific information or assistance do you need?

- Can you combine multiple related questions into a single message?

- Is there any background information you can provide upfront?

Planning helps reduce the number of back-and-forth messages needed.

## 2. Be specific and concise

- Provide clear, detailed instructions or questions in each message.

- Avoid vague queries that may require clarification.

- Include relevant context to help Claude understand your needs better.

## 3. Use Claude's chat search and memory capabilities

- All users can follow these guidelines to take advantage of Claude's memory within a single chat:

  - Refer back to previous information instead of repeating it.

  - Use phrases like "As mentioned earlier" to build on earlier parts of the conversation.

- Users with paid plans (Pro, Max, Team, and Enterprise) can prompt Claude to search through previous conversations and reference relevant information in new chats. Giving Claude access to additional context prevents you from needing to provide the same information repeatedly.

  - Learn more here: **[Searching past chats with Claude](https://support.claude.com/en/articles/11817273-using-claude-s-chat-search-and-memory-to-build-on-previous-context#h_89b670b004)**

- Users with paid plans (Pro, Max, Team, and Enterprise) can use Claude's memory and project summaries to build context across conversations.

  - Learn more here: **[What is Claude's memory?](https://support.claude.com/en/articles/11817273-using-claude-s-chat-search-and-memory-to-build-on-previous-context#h_c1c0b33879)**

## 4. Batch similar requests in one message

If you have multiple related tasks or questions, group them in a single message. For example, instead of sending separate messages for each math problem, send them all in one message.

## 5. Review and edit your prompt before sending

Take a moment to review your message for clarity and completeness to reduce the need for follow-up messages.

## 6. Use project knowledge bases effectively

Projects offer significant caching benefits:

- When you upload documents to a project, they're cached for future use.

- Every time you reference that content, only new/uncached portions count against your limits.

- This means you can work with the same documents repeatedly without using up your messages as quickly.

- Example: If you're working on a research paper and add all your reference materials to a project, you can ask multiple questions about those materials while using fewer messages than if you uploaded them each time.

- Projects offer a Retrieval Augmented Generation (RAG) mode allowing for expanded project knowledge capacity.

  - Learn more here: **[Retrieval Augmented Generation (RAG) for projects](https://support.claude.com/en/articles/11473015-retrieval-augmented-generation-rag-for-projects)**

## 7. Monitor your consumption in Usage settings

- If you're using a Pro, Max, Team, or seat-based Enterprise plan, you can navigate to **[Settings > Usage](https://claude.ai/settings/usage)** to view progress bars showing how much of your five-hour session and weekly usage limits you’ve consumed.

- The **Plan usage limits** section at the top shows your progress towards both your session limit and weekly limits.

  - **Current session:** How much of your plan’s five-hour session limit you’ve used thus far, plus the amount of time remaining in the session.

  - **Weekly limits:** Check when your plan’s weekly usage limit resets for Opus only and all other models.

- **Usage credits:** If you are using a Pro, Max, Team, or seat-based Enterprise plan, your usage settings page will also show how much of your plan's limit you've used. Refer to these articles for more information about enabling usage credits depending on your plan:

  - **[Manage usage credits for paid Claude plans](https://support.claude.com/en/articles/12429409-)**

  - **[Manage usage credits for Team and seat-based Enterprise plans](https://support.claude.com/en/articles/12005970-)**

- If your organization is on a usage-based Enterprise plan, you won’t have specific usage limits, but will be charged based on consumption. You can also track this in **[Settings > Usage](https://claude.ai/settings/usage)**.

## 8. Quick caching tips

- Use projects for anything you'll reference multiple times.

- Upload your core working documents to the project knowledge section when starting a project.

- The more you use the same content, the more benefit you get from caching.

---

## Best practices for specific use cases

### For coding tasks

- Provide complete context about your coding environment in your initial message.

- Include entire relevant code snippets in one message for reviews or debugging.

### For writing assistance

- Outline requirements, target audience, and key points comprehensively.

- Send entire texts for editing in one message rather than breaking them up.

### For research and analysis

- Clearly define your research question and focus areas initially.

- Provide all relevant data in a single, well-structured message.

By following these best practices, you can make the most efficient use of your Claude plan's message allocation.