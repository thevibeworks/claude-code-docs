> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Answer when Claude asks to fetch a web page

> Which links Claude fetches without asking in a Cowork task that runs on your computer, and when it asks you first.

In a Cowork task that runs on your computer, Claude can fetch a web page to read it. Claude fetches some links without asking. Before it fetches any other link, it asks you. This page describes the latest version of Claude Desktop. Earlier versions and tasks that run in the cloud can differ, and not every account has this prompt.

## Links that Claude fetches without asking

In **Manually approve** mode, Claude fetches these links without asking:

* **Links you type or paste**: links in the message box when you send your message, up to 100 in each message.
* **Links in a scheduled task's prompt**: the links in the task's own instructions. Claude can write or change this prompt for you, so check its links each time it does.
* **Links in a message from your phone or the web**: all the links in the text of a message that you send from another device to a task on this computer.
* **Links on a page that Claude fetched**: only links to the same site as the address that Claude fetched, and none if that address redirected to another site.
* **Web search results**: in some tasks, the pages that Claude's own web search found.

In **Skip all approvals** mode, Claude fetches any link without asking. In **Automatically approve** mode, an automatic check reviews each fetch, and it can block the fetch or ask you. If you leave either of these modes during a task, Claude can ask again about links that it could fetch before, including links you typed.

## Links that Claude asks about

Claude asks before it fetches a link that reached the task in another way. These are examples from messages that you send on this computer:

* A link that is only in a connected document whose text is part of your message.
* A link that is only in a quote, a comment, or page data added to your message.
* A link that is only in a message that failed to send, if you send it again with **Retry**.
* A link in a message whose text an app or a web address put in the message box, even if you edited the text before you sent it.

The prompt shows the address in full. Check it before you answer, because an address can carry information from your task to the site. A site can redirect Claude to another site, and Claude doesn't ask again.

* **Allow once**: Claude fetches this link.
* **Allow all for this website**: Claude fetches this link and later links to the same host name in this task, until Claude Desktop restarts. A subdomain counts as a different website. Some prompts don't have this button.
* **Deny**: Claude doesn't fetch this link, and continues without the page.

## When Claude can't ask

When a scheduled task starts on its schedule, Claude can't ask you, even if you're at your computer. Unless the task runs in **Skip all approvals** mode, Claude doesn't fetch the link, and continues without the page. To let a scheduled task fetch a page, add the page's full address to the task's prompt. Claude can ask in a run that you start with **Run now**, and in any run after you reply in it.

## Organization settings

In some organizations, web fetch isn't available, and Claude fetches no links. An admin can also require a prompt before each fetch. **Allow all for this website** might then cover only the current link.

If your organization deploys Claude Desktop with its own model provider, this page doesn't apply. Your admin's [list of allowed hosts](https://claude.com/docs/third-party/claude-desktop/web-tools.md#web-fetch) decides which pages Claude can fetch.

## Related

These pages cover related topics.

* [Network access for shell commands](https://claude.com/docs/cowork/guide/network-access.md) for the hosts that a task's shell commands can reach
* [Cowork overview](https://claude.com/docs/cowork/overview.md) for an introduction to Cowork
