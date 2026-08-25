> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Turn threads into docs and tickets

> Claude Tag turns a Slack discussion into the artifact you name. See replies you can send, decision docs, status memos, filed tickets, hosted web pages, and a capture-channel pattern.

export const BetaNote = () => <Info>Claude Tag is in public beta. Features and behavior described here may change before general availability.</Info>;

<BetaNote />

## How artifact prompts work

An artifact here is a generated document, page, chart, or file Claude posts or links in the thread for the team to use, as opposed to a chat reply.

Each prompt below is a Slack message. You paste it in the thread or channel you want turned into something, Claude reads the discussion and posts progress in that thread, and the draft lands there too. What the draft is depends on the prompt, and each one below names the artifact it returns, like a decision doc, a customer reply, a filed ticket, a planning outline, or a hosted web page.

## Check the channel's connections

Check that the channel has the connections below. Ask `@Claude what can you access from this channel?` to check; an admin can [add a connection](/docs/claude-tag/admins/add-connections) the channel is missing.

| Connection     | Examples            | Why it matters here                    |
| :------------- | :------------------ | :------------------------------------- |
| None           | —                   | Works on Slack content alone           |
| Issue tracking | Linear, Jira, Asana | Optional. Files tickets from the draft |

## Prompts to paste

### Draft from one thread

The thread settled the question, and what's missing is the doc, the customer reply, or the ticket. Name the artifact in the thread where the discussion happened.

```text wrap theme={null}
@Claude turn this thread into a one-page decision doc: what we decided, the options we rejected, and why.
```

```text wrap theme={null}
@Claude draft a reply I can send to the customer based on this discussion. Keep it under 150 words.
```

```text wrap theme={null}
@Claude file this thread as a ticket, assign it to the owner we discussed above, and post the link here.
```

Name the format and the length; "a doc" gets you a guess, "a one-pager with a decision section" gets you the artifact.

### Ask for a hosted page

When the deliverable is a page people open, like a dashboard or a status page, ask for one. Claude publishes it as a web page hosted on claude.ai, posts the link in the thread, and updates it when you ask in the same thread.

```text wrap theme={null}
@Claude build a status page from the open items in this channel and post the link here.
```

Anyone with access to this channel can open the page; [artifact visibility](/docs/claude-tag/concepts/security-and-data#artifact-visibility) covers the access model.

### Keep a capture channel

Planning inputs arrive over a month, not in one sitting. Forward messages and ideas to one channel as you find them, then ask for a synthesis when you need the artifact.

```text wrap theme={null}
@Claude go through everything posted in this channel this month and synthesize it into an outline for the planning doc.
```

## Related resources

<CardGroup cols={2}>
  <Card title="Catch up" href="/docs/claude-tag/users/use-cases/catch-up" horizontal arrow>
    When you need the summary, not the artifact
  </Card>

  <Card title="Good habits" href="/docs/claude-tag/users/good-habits" horizontal arrow>
    How to specify outputs that come back right
  </Card>
</CardGroup>
