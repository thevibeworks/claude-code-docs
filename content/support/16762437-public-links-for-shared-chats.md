# Public links for shared chats

When you share a chat with a public link, anyone who has the link can view a snapshot of that chat. This article covers who can see it, what's included, and how public links interact with search engines like Google.

Public links are available on Free, Pro, and Max plans. Team and Enterprise members can only share chats inside their organization. For how to share and unshare, see **[Share and unshare chats](https://support.claude.com/en/articles/10593882)**.

## What a public link does

- It shares a snapshot of the chat as of the moment you shared it. Messages you send afterward stay private unless you update the snapshot.

- Anyone with the link can open it. No Claude account is required.

- It's view only. Viewers can't continue the chat.

- Files you attached to the chat are not included.

- You can turn it off at any time from the "Share" menu, or from **[Settings > Privacy](https://claude.ai/settings/data-privacy-controls)** under **Shared chats**. Once it's off, the link stops working.

## Can Google or other search engines index my shared chat?

We ask them not to. Every shared chat page carries a "noindex" instruction, which is the standard way to tell Google and other search engines not to show a page in search results. We also don't publish a directory or sitemap of shared chats, and each link is a long random string that can't be guessed.

There are things we can't control:

- **Where the link gets posted.** If you (or someone you sent it to) post the link on a public site like a forum, social feed, or blog, anyone who finds it there can open it.

- **Copies.** Anyone who can view the page can copy, screenshot, or repost what's in it. Third-party archive and scraping services may save their own copy, and those copies aren't governed by our noindex instruction.

- **Every search engine.** Major search engines honor noindex. We can't guarantee every crawler on the internet does.

The simple rule: treat a public link as public. If you wouldn't post the contents on the open web, don't put them behind a public link.

## Frequently asked questions

### Does someone need a Claude account to open a public link?

No. Anyone with the link can view the snapshot.

### I only sent the link to one person. Is it still public?

Yes. A link sent privately won't land in search results on its own, but whoever has it can forward or post it, and there's no way to limit a public link to specific people.

### One of my shared chats showed up in search results. What should I do?

Turn off sharing for that chat (Share menu > set to Private, or Settings > Privacy > Shared chats). The link stops working immediately, so nobody can click through and read it. Search engines drop dead and noindexed pages on their own recrawl schedule, which can take some time. For Google, you can speed this up with their **[Remove outdated content](https://support.google.com/websearch/answer/6349986)** tool. If a third-party site saved a copy, you'll need to contact that site directly.

### If I turn off a public link, are copies deleted too?

No. Turning it off disables the link on claude.ai. It can't remove copies, screenshots, or archives someone else already made.

### Can Team or Enterprise members create public links?

No. On Team and Enterprise plans, shared chats are only visible to signed-in members of the same organization.