# Troubleshoot Claude error messages

This article explains common error messages and warnings you may encounter when using Claude and provides guidance on how to address them.

## Usage limit warnings and errors

Your plan has a five-hour session limit and a weekly limit. Some plans have an additional weekly limit that applies specifically to Fable. Usage limit warnings appear when you’re approaching any of your plan's limits: *“Approaching session limit”* or "Approaching weekly limit." When the percentage is available, the warning shows how much of your limit you've used instead, for example "You've used X% of your weekly limit."

If you reach a limit and don’t have usage credits enabled, you’ll see an error message letting you know when you can use Claude again: "5-hour limit reached - resets [time]" or "You've reached your weekly limit. It resets [day] at [time]."

Looking for ways to maximize your Claude usage? Refer to **[Usage limit best practices](https://support.claude.com/en/articles/9797557-usage-limit-best-practices)**.

### Usage credits

If you’re on a paid Claude plan with usage credits enabled in Usage settings, reaching your five-hour session limit or any of your weekly limits doesn’t stop your work. Your requests switch to pay-as-you-go pricing on usage credits and keep working until you reach your monthly spend limit or your usage credit balance runs out with auto-reload off. Instead of the error above, you’ll see "5-hour limit resets [time] - continuing with usage credits" or "Now using credits. Your plan limit resets [day] at [time]".

**Note:** The warning that you’re approaching your limit may still be showing at the moment your usage switches to usage credits. It can look like you’ve been cut off, but your work continues, and the message changes to “Now using credits” once your next request goes through.

Refer to these articles for more information about this feature depending on your plan:

- **[Manage usage credits for paid Claude plans](https://support.claude.com/en/articles/12429409-)**

- **[Manage usage credits for Team and seat-based Enterprise plans](https://support.claude.com/en/articles/12005970-)**

## Length limit errors

You may encounter a length limit error when your message to Claude exceeds the maximum input length allowed: "Your message will exceed the length limit for this chat. Try attaching fewer or smaller files or starting a new conversation." This error indicates that your message is too long and needs to be shortened before sending it to Claude.

For users on paid plans with code execution enabled, Claude automatically manages long conversations by summarizing earlier messages when context limits are approached. This means most users will rarely encounter length limit errors during normal use. Your full chat history is preserved so Claude can reference it even after summarization. In rare cases where you still encounter this error (such as when sending a very large first message), you can:

- Break your content into smaller chunks and process them separately

- Summarize or extract key sections before sending to Claude

- Use Claude to first identify the most relevant portions of your content

- Start a new conversation

## Login errors

If you see a generic error message when attempting to log in to your Claude account (e.g, "There was an error logging you in"), try the following troubleshooting steps:

- Ensure you’re not using a VPN when accessing Claude.

- Disable any browser extensions that you currently have active.

- Clear your browser’s cache and cookies.

If you're still seeing an error, check **[our status page](http://status.claude.com)** for active incidents.

## Capacity constraints

Capacity issues occur when Claude’s infrastructure experiences high demand system-wide. When capacity is constrained, you may see this message when chatting with Claude: *"Due to unexpected capacity constraints, Claude is unable to respond to your message. Please try again soon."*

**Important:** Capacity constraints are not outages. The system is functioning normally but managing high demand across all users. These issues are temporary and typically resolve as demand patterns shift throughout the day. If you encounter this message, try again in a few minutes.

Capacity issues will not appear on our status page because they represent normal load management rather than technical problems.

## Service incidents and outages

Service incidents are disruptions where Claude is unavailable or significantly degraded for all or most users. These represent actual technical problems with our systems. To check for confirmed incidents, visit status.claude.com, where you'll find real-time updates on scope, impact, and resolution progress for any active incidents.

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/1753796247/e6a8c6ef8653b229c5758e881242/c2fc6fc0-d163-4119-93e0-394104d86bc9?expires=1791615600&amp;signature=428a62262cca98766cb063d951d127d3253dd9c723bf8b04da3e56a70167bf16&amp;req=dSciFc53m4NbXvMW1HO4za4BX64l07fC7y68oYp%2BYg%2FFUxKg8w2AKThlVAFp%0ALnoXUteowYdalbx%2Bnes%3D%0A)