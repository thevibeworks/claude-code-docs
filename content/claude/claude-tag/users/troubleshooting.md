> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Troubleshoot Claude Tag in channels and DMs

> Fixes for common Claude Tag problems in Slack. See no reply after a reaction, queued or failed sessions, lost work, missing connections, blocked links and websites, and DM or account errors.

export const BetaNote = () => <Info>Claude Tag is in public beta. Features and behavior described here may change before general availability.</Info>;

<BetaNote />

When something goes wrong mid-conversation, the cause is usually one of a small set. Each entry below has the same three parts: what you see, what it means, and how to resolve it. For setup and credential errors, see the [admin troubleshooting page](/docs/claude-tag/admins/troubleshooting).

Many fixes end with something to send your admin. On this page that means whoever manages your organization's Claude account at claude.ai, and it's often not the same person as your Slack administrator. If you don't know who that is, ask whoever set Claude up in your workspace.

## No response or silence

### Mentioning @Claude does nothing at all

**What you see**

`@Claude` gets no reaction and no reply.

**What it means**

Total silence has several possible causes, from the app not being installed to the channel being turned off, and the checks below separate them.

**How to resolve**

Work through these in order. Each step says what success looks like and where to go if it fails.

1. **Is the Claude app installed in this workspace?** Start typing `@Claude` in any channel. **Works**: Slack autocompletes to a Claude app with an app badge; if more than one Claude app appears, check with your admin which one to use. **Fails**: nothing autocompletes, or only a person named Claude appears. The app isn't installed; this needs your admin (send them the [setup overview](/docs/claude-tag/admins/setup-overview)).
2. **Is Claude in this channel?** Type `/invite @Claude` in the channel's message box, not in a thread reply. Slack rejects `/invite` inside threads ("/invite is not supported in threads. Sorry!"). **Works**: Slack posts "Claude was added to #channel" (or "is already in this channel"). Mention it again. **Fails**: Slack says you can't add apps to this channel (a Slack Connect or guest-restricted channel); try an internal channel instead.
3. **Is Claude Tag turned on for this channel?** Mention it again now that it's invited. **Works**: it reacts and replies. **Fails**: it replies "Claude is disabled in this channel" (the channel is set to **Off**), or it replies but behaves like the earlier Claude in Slack, with no channel memory and pull requests opening under your name rather than Claude's (the channel is set to **Legacy**). Either way this needs your admin (send them [Migrate from the earlier Claude in Slack](/docs/claude-tag/admins/restrict-access#migrate-from-the-earlier-claude-in-slack)).

If `@Claude` still gets no reaction and no reply after all three, send your admin [the admin entries for a silent workspace](/docs/claude-tag/admins/troubleshooting#nothing-responds). If the silence covers every channel across an Enterprise Grid, the fix needs a Slack organization admin rather than your Claude admin, so send the link to them.

### Claude replies to me but not to a teammate

**What you see**

Claude answers your mentions in a channel, and a teammate's mentions in the same channel get silence or a refusal.

**What it means**

Mentioning Claude in a channel doesn't require the sender to have a Claude account or seat, so by default anyone in the workspace can use it. Your organization can restrict that with the [member access setting](/docs/claude-tag/admins/restrict-access#restrict-who-can-use-claude), in which case members outside the restriction are declined.

**How to resolve**

Have the teammate mention `@Claude` themselves and report the exact text of any reply; the reply is the diagnosis.

* No reaction and no reply at all: unusual when it works for you in the same channel; send your admin the exact channel and person.
* A message about guests: see [the guest entry below](#claude-doesn%E2%80%99t-respond-in-channels-that-include-guests).
* A message about permissions or access: your organization restricts who can use Claude; send your admin [the member access setting](/docs/claude-tag/admins/restrict-access#restrict-who-can-use-claude).

### Claude reacted or started thinking, then never replied

**What you see**

Claude added a reaction to your message, or an "is thinking…" line appeared under it, but no reply arrived.

**What it means**

A reaction or an "is thinking…" line without a reply usually means Claude is still working, not that your message was dropped.

**How to resolve**

1. @-mention Claude in the same thread to ask for a status check.
2. If the silence has stretched well past what the task should need, send [`@Claude !restart`](/docs/claude-tag/users/commands#restart-a-stuck-or-wrong-context-session) in the thread; it archives the session and starts a fresh one that still reads the thread. Starting a new thread and restating the request also works.

<Warning>Restarting abandons whatever the session was midway through, and there's no way to resume it. A silent session may still be working through a long task, so treat `!restart` as a last resort.</Warning>

### Claude says my session is queued or failed to start

**What you see**

Claude posts in the thread:

> Still waiting for available capacity — your request is queued and will start automatically. Replies in this thread are picked up automatically.

Or, if the session never started:

> Session failed to start: the session container never connected — please try again

**What it means**

The first message means compute capacity is temporarily busy; the session starts on its own once capacity frees up. The second means the session didn't start at all, which is transient.

**How to resolve**

* For the capacity message, wait a few minutes; no action is needed. To add context while waiting, @-mention Claude in the same thread rather than starting a new one. A new thread only queues a second session behind the first.
* For the failed-start message, mention Claude in the same thread to retry. If the retry worked, the session starts and Claude begins the task.

### Claude didn't react to a message I edited

**What you see**

You edited a sent message to add `@Claude`, and nothing happened.

**What it means**

Editing a sent message to add a mention doesn't trigger a response; Claude only picks up mentions from new messages.

**How to resolve**

Send a new message with the mention included.

### Claude never responds in a channel shared with another company

**What you see**

Mentions in a Slack Connect channel, one shared with another company, get no answer, and usually no notice.

**What it means**

By default, Claude is off in Slack Connect channels, and it posts no notice there. A Claude organization Owner turns it on with the [guest setting](/docs/claude-tag/admins/restrict-access#restrict-guest-channels), after which Claude replies with [channel-only access](/docs/claude-tag/admins/restrict-access#how-channel-only-works). If the setting is already **Allow** or **Channel only** and Claude still doesn't answer, one of two things is likely:

* The organization that runs Claude restricts it to its own members, and you're on the other side of the channel.
* That organization installed Claude at the Enterprise Grid organization level, and the other company's workspace created the channel.

See [Slack Connect channels](/docs/claude-tag/admins/restrict-access#externally-shared-channels).

If the mention gets the notice "This channel is now shared with another organization through Slack Connect, so this thread's earlier session can't continue here," the thread started before the channel was shared. Mention `@Claude` in a new thread.

A channel shared across workspaces inside your Enterprise Grid isn't silent; what happens there depends on how those workspaces connect to Claude. When every workspace in the channel belongs to your one Claude organization, Claude answers, but with only your organization's default access and settings, so a repository or an instruction set up for that channel doesn't apply. A notice in the thread points this out from time to time. When the workspaces are connected to different Claude organizations, you see "This channel is shared among several Claude workspaces, so Claude cannot respond here" instead of an answer.

Where guest access is restricted, you may first see "This channel is shared across multiple workspaces, and Claude can't verify whether it includes guests, so Claude can't respond here." If you ask Claude from another conversation to act in one of these channels, such as posting a message there, you see a reply that ends "Claude isn't available in channels shared across your Enterprise Grid".

Each of these messages means the channel spans more than one workspace. The [admin entries on these messages](/docs/claude-tag/admins/troubleshooting#this-channel-is-shared-across-multiple-workspaces) explain what causes each one and what an admin can change.

**How to resolve**

Move the conversation to an internal channel that belongs to a single workspace, or to a DM, and mention Claude there.

### Couldn't check this channel just now

**What you see**

Claude replies in the channel:

> Couldn't check this channel just now. Please try again in a moment.

**What it means**

When your organization restricts Claude in channels that include guests (the default), Claude checks each channel for guests before replying. That check briefly failed, so Claude declined this reply rather than guess.

**How to resolve**

Mention Claude again; the check usually passes on retry. If the same channel hits this repeatedly, send your admin [the admin entry on this message](/docs/claude-tag/admins/troubleshooting#couldn%E2%80%99t-check-this-channel-just-now).

### Claude doesn't respond in channels that include guests

**What you see**

Claude replies in the channel:

> Claude doesn't respond in channels that include guests. You can remove the guests from this channel (Channel details -> Members -> filter by "guests"), or a claude.ai organization owner can allow it in Claude Tag settings under Advanced -> "Allow Claude to work in channels with guests".

**What it means**

The channel includes at least one Slack guest account, and your organization restricts Claude in channels that include guests (the default).

**How to resolve**

Any of these fixes works:

* Remove the guests from the channel. In Slack, open **Channel details** → **Members** and filter by "guests"; guests show a **guest** badge on their Slack profile.
* Move the conversation to a channel with no guests.
* Ask an admin of your Claude organization to change the guest setting for this channel, and send them [the guest access setting](/docs/claude-tag/admins/restrict-access#restrict-guest-channels). They can let Claude reply with only the channel's own setup, or with full access. If you don't know who your organization's admins are, ask whoever set Claude up in your workspace.

The guest access setting restores replies, not workspace search. Claude can't search the workspace from a channel that includes guests, even when it's allowed to respond there. Removing the guests or moving the conversation to a channel with no guests restores search as well.

If the fix worked, a mention in the channel gets a reply.

## Too many or wrong responses

### Claude gave me a confident but wrong answer

**What you see**

Claude answered with certainty, and the answer is wrong or incomplete.

**What it means**

Claude can be wrong, including when it sounds certain. The most common wrong answer in Slack is an incomplete one, where Claude queried one source or one date range and reported the result as if it were the whole picture.

**How to resolve**

Before you share or act on a result, check the source links it posted, and ask it to show its work ("which channels did you search?" or "show me the query you ran"). If the answer is wrong, say so in the same thread with the correct answer; correcting it there is also how you steer the next attempt.

For numbers and facts that matter, the [definition-of-done habit](/docs/claude-tag/users/good-habits#give-every-task-a-definition-of-done) helps. Make "include the source for every figure" or "show me the query" part of the ask.

### Claude replies to every message in a thread

**What you see**

Claude answers messages in the thread that weren't addressed to it.

**What it means**

Once Claude is mentioned in a thread, it follows the whole conversation there and may reply to messages that weren't addressed to it.

**How to resolve**

Reply in the thread with an instruction such as "only respond when I @-mention you"; Claude follows that instruction for the rest of the thread.

### I want to take back something I sent

**What you see**

You edited or deleted a message, and Claude still acts on the original.

**What it means**

Claude has already read the original. An edit reaches it as a new update in the thread, so it may or may not act on the change, and it never undoes work already in progress. A deleted reply doesn't reach Claude at all.

**How to resolve**

Say so in a new reply ("ignore that, do X instead"), or start a fresh thread for a clean session.

### This conversation is too long for me to process

**What you see**

Claude posts in the thread:

> This conversation is too long for me to process and I couldn't finish this turn — please start a new thread to continue.

In a DM it ends with "Click *New Chat* in the top right to start a fresh session" instead.

**What it means**

The thread has grown past what one session can hold, and it stays too long forever; retrying there can't work.

**How to resolve**

Start a new thread. You can paste a summary of where the previous one left off.

## Claude stopped mid-task

The messages in this section mean a session started and then stopped partway through. In most cases the work isn't lost, and the same thread picks up where it stopped. Each entry says whether anything needs redoing.

### I hit repeated API server errors

**What you see**

Claude posts in the thread:

> I hit repeated API server errors. I'll retry automatically in about 2 minutes — no need to do anything. Mention me to retry sooner.

The related messages that start "Claude is over capacity right now" and "I hit API rate limits" behave the same way. The wait Claude names grows with each retry.

If the retries run out, or the session isn't a thread session, the message ends "and stopped after retrying. Mention me to continue." instead. "The API request timed out and I stopped after retrying. Mention me to continue." and "An API server error cut my last response short, so it may be incomplete. Mention me to continue." always take that form.

**What it means**

The API serving the session returned repeated errors. The work isn't lost. When the message says Claude will retry automatically, the same conversation wakes again on its own, up to three times; a newer message from you in the thread cancels the pending retry.

**How to resolve**

Nothing, when the message says Claude will retry automatically; wait for it. Mention Claude in the same thread to retry sooner, or when the message asks you to.

### I hit API rate limits

**What you see**

Claude posts in the thread:

> I hit API rate limits. I'll retry automatically in about 2 minutes — no need to do anything. Mention me to retry sooner.

When the retries run out, the message is "I hit API rate limits and stopped after retrying. Wait a moment, then mention me to continue."

**What it means**

The Claude API rate-limited your organization's traffic partway through the turn. The work isn't lost. Rate limits are about momentary request rate, not accumulated usage: a single task makes many API requests in short bursts, so this can appear on an organization's very first request. It isn't the channel spend limit, and it doesn't mean anything is misconfigured.

**How to resolve**

Wait for the automatic retry, or wait a moment and mention Claude in the same thread; it picks up where it stopped. If it recurs constantly across channels, the organization's sustained traffic is above its rate limits; an admin can stagger heavy use or contact their account team about limits.

If your message mentions a spend limit instead, that's a different problem; see [You've reached a Claude Tag spend limit](#you%E2%80%99ve-reached-a-claude-tag-spend-limit).

### This request needs usage credits that aren't available

**What you see**

Claude posts in the thread:

> This request needs usage credits that aren't available and I couldn't finish this turn. Enable or purchase usage credits in claude.ai, then mention me to retry.

**What it means**

Your organization's usage credit balance can't cover the request, so the turn stopped. The session is still there.

**How to resolve**

An admin enables or purchases usage credits in claude.ai for your organization. Once that's done, mention Claude in the same thread to retry (adding credits doesn't restart the work on its own). The retry continues with the thread's conversation and context. [What survives between replies](/docs/claude-tag/concepts/how-it-works#what-survives-between-replies) covers what else carries over.

### Claude couldn't clone a repository for this session

**What you see**

Claude posts in the thread:

> Claude couldn't clone a repository for this session. This can be temporary (for example a GitHub rate limit) — mention Claude in this thread to retry in a few minutes. If it keeps happening, this session may lack access to a repository it needs, or its credentials or integration may need to be reconnected.

**What it means**

The clone failed when the session started. A one-off failure is transient; the same repository failing every time usually means it isn't granted for this channel, or the connection it depends on needs to be reconnected.

**How to resolve**

Wait a few minutes, then mention Claude in the same thread to retry. If the same repository fails every time, send your admin [the GitHub access entry](/docs/claude-tag/admins/troubleshooting#github-doesn%E2%80%99t-work-in-this-channel).

### I got disconnected partway through

**What you see**

Claude posts in the thread:

> I got disconnected partway through and may not have finished. Reconnecting and resuming automatically — usually within a few minutes, though a slow recovery can take much longer. Mention me if I don't follow up.

When Claude reconnects, it edits that message to "I reconnected and I'm carrying on where I left off. No need to mention me." When automatic recovery isn't armed, the message is "I got disconnected partway through and may not have finished. Mention me to pick up where I left off." instead.

You can see it in a thread where you're working with Claude, including a direct-message thread; Claude doesn't post it in a channel it's only watching or from a routine.

**What it means**

The sandbox running this thread's session stopped partway through a turn, so the step Claude was on may not have finished. The thread's conversation is intact.

**How to resolve**

Wait for the reconnect message, or mention Claude in the same thread when the message asks you to. Claude resumes there and continues from the conversation; ask it to check on the step it was working on and redo anything that didn't finish. If the same notice comes back, the underlying problem hasn't cleared yet. Wait a few minutes and mention Claude again.

### Something went wrong and I couldn't finish this turn

**What you see**

Claude posts in the thread:

> Something went wrong and I couldn't finish this turn. Mention me to retry.

The related message "The API rejected the request as invalid, so I couldn't finish this turn. Mention me to retry." behaves the same way.

**What it means**

This is the catch-all for a turn that stopped mid-task. The error didn't match any of the more specific messages in this section, so the cause varies. If the message says "Something went wrong starting a session. Try again in a moment." instead, the session never started; the retry is the same either way.

**How to resolve**

Mention Claude in the same thread to retry; it picks up where it stopped. If the message repeats on every retry, [give feedback](https://support.claude.com) from the thread where it happened.

## Lost or stale work

### Claude lost work it created earlier

**What you see**

Claude can't find files or drafts it made earlier in the thread.

**What it means**

The isolated workspace where Claude works on a thread is recycled after a period of inactivity. Work that was pushed to a branch, opened as a pull request, or posted into the thread survives. Files that existed only inside that workspace don't, and Claude will need to recreate them.

**How to resolve**

Ask Claude to recreate the file, and for long-running work, ask it to commit and push early, or to post drafts into the thread as it goes, so nothing lives only in that workspace. The [definition-of-done habit](/docs/claude-tag/users/good-habits#give-every-task-a-definition-of-done) helps here. Make "push the branch" or "post the file" part of the task.

### My old thread stopped working, but new threads are fine

**What you see**

A thread created a while ago fails the same way on every retry, while new threads work.

**What it means**

A thread keeps the skills, plugins, and custom instructions it started with, so a thread created weeks ago can fall out of step with your organization's current setup, even though new threads work. Retrying in the same thread will usually keep failing the same way.

**How to resolve**

Send [`@Claude !restart`](/docs/claude-tag/users/commands#restart-a-stuck-or-wrong-context-session) in the thread. It archives the stuck session and starts a fresh one with your organization's current configuration, and the fresh session still reads the thread.

Starting a new thread and restating your request also works; paste a link to the old thread so Claude picks up the context.

### Claude picked the wrong repository

**What you see**

Claude started working in a repository you didn't mean.

**What it means**

The request didn't name a repository, so Claude picked one from the channel's grants.

**How to resolve**

Start a new thread with the right one named in your first message, for example "in `acme/data-pipeline`, fix the failing import." Naming the repository up front is also how you prevent this. If you need another repository mid-thread, ask Claude to add it ("add acme/data-pipeline") and confirm with the **Confirm** button it posts; if the repository isn't allowed for this channel, Claude tells you after you confirm.

### Claude forgot instructions I gave it before

**What you see**

Something you told Claude earlier doesn't stick in later threads.

**What it means**

Channel memory is a small, curated note, not a transcript, and Claude decides what's worth saving, so passing details usually aren't kept.

**How to resolve**

To make an instruction stick, say so explicitly, as in `remember for this channel: always post reports as a table`. Keep saved instructions short; the per-channel memory budget is limited, and long entries crowd out everything else. For longer playbooks, store them in a repository Claude can read.

Verify what stuck by asking what it remembers about the channel. See [What Claude Tag remembers](/docs/claude-tag/users/memory).

### A session link Claude posted shows a not-found page

**What you see**

You open a link to a session on claude.ai that Claude posted in Slack, such as the "open the session" link in a routine's completion message, and claude.ai shows a not-found page instead of the session.

**What it means**

A session Claude ran from a channel belongs to Claude's own identity rather than to the person who asked, so claude.ai shows it only to accounts in the Claude organization paired with the workspace, and then only to people who could see the conversation in Slack. Any workspace member can open a session from a public channel; a session from a private channel opens only for members of that channel and the person who started it. Anyone else sees not-found rather than a permission error.

**How to resolve**

Sign in to claude.ai with the account that belongs to the organization paired with your workspace. claude.ai matches you to your Slack identity through a connected Slack account or, failing that, through the email address on your Claude account, so if your Claude email differs from your Slack email, connect your Slack account first; DM `@Claude` and it prompts you. If the session came from a private channel, ask to be added to the channel.

## Access and connections

### A connection my admin added isn't showing up

**What you see**

Your admin added a connection, and Claude in your thread says it doesn't have it.

**What it means**

Claude isn't told about a connection added after its session started, so it doesn't list or offer the new service, even though the connection is usable.

**How to resolve**

Ask Claude to use the service by name; the connection works even though Claude didn't announce it. Or start a new thread, which picks up the connection on its own. For a scheduled job that's missing a connection, edit or recreate the schedule. If the fix worked, asking `@Claude what can you access from this channel?` in a new thread lists the connection.

### Claude says it can't access a channel it read before

**What you see**

One reply surfaces findings from a channel, and a later one says "I can't access that channel." Or Claude says it can't read a private channel it's a member of when you ask from another channel.

**What it means**

This usually doesn't mean access changed.

For a public channel, Claude can search it without being a member, but it can't read the channel directly without being invited, so search results and direct reads come and go differently.

For a private channel, membership isn't the issue. A private channel is readable only from inside it. Even when Claude is a member, it can't read that channel from any other channel or DM.

**How to resolve**

For a public channel Claude needs to read directly, invite it with `/invite @Claude` in that channel, then ask again in a new thread.

For a private channel, ask in that channel itself, inviting Claude there first if it isn't a member. An invite lets Claude work inside the private channel, but doesn't make the channel readable from anywhere else.

### Claude says it can't reach a tool or service

**What you see**

Claude says it has no connection for a service you expected it to reach.

**What it means**

The channel likely hasn't been given a connection for that service; see [what each connection adds](/docs/claude-tag/admins/add-connections).

**How to resolve**

Ask your admin to add one for this channel and send them [the connection scope entry](/docs/claude-tag/admins/troubleshooting#a-connection-works-in-one-channel-but-not-another). Once they have, ask Claude to use the service by name, or start a new thread, which picks up the connection on its own. If the fix worked, asking `@Claude what can you access from this channel?` in a new thread lists the service.

### A connector works on claude.ai but not in Slack

**What you see**

A connector you use on claude.ai is missing when you work with Claude in Slack, or Claude says it has no access to that service.

**What it means**

Where you message Claude determines which connectors apply. A channel uses only the connections an admin attached to it, and personal connectors never apply there. A DM runs on your own claude.ai account and uses that account's connectors.

You set up and authenticate connectors on claude.ai under **Customize > Connectors**; Slack has no connector settings of its own. The [settings map](/docs/claude-tag/concepts/settings-map) covers every settings surface.

**How to resolve**

For a channel, ask your admin to [add a connection](/docs/claude-tag/admins/add-connections) for the service.

For a DM, work through these in order:

1. Check that your Claude account is connected. DM `@Claude` and it prompts you to connect if it isn't.
2. Check that the connector shows as connected under **Customize > Connectors** on claude.ai.
3. For a custom connector on a Team or Enterprise plan, an Owner adds it to the organization before you can connect it; see [third party connectors with remote MCP](/docs/connectors/custom/remote-mcp).
4. After connecting or reconnecting the connector on claude.ai, send Claude a new top-level direct message. A session loads its connectors when it starts, so your existing DM threads keep the set they started with and don't pick up the change.

### Claude says it has no internet access or can't open a link

**What you see**

You paste a URL or ask Claude to read a page, and it says the website isn't allowed, the request was blocked, or it lacks internet access. It may find the same page with web search and still not open the link.

**What it means**

Searching and opening a page take different paths. Web search runs on Anthropic's servers and needs no setup, and a search brings back content from the pages it matches, so Claude can often answer from what the search returned. Opening a URL happens from the channel's sandbox, the isolated workspace where Claude runs, and the sandbox reaches only websites your organization's setup allows; the web search setting has no effect on that.

**How to resolve**

Send your admin the link you tried to open along with [the blocked host entry](/docs/claude-tag/admins/troubleshooting#claude-says-a-host-isn%E2%80%99t-allowed-or-it-can%E2%80%99t-reach-the-internet). While you wait, ask Claude to search for the page instead; a search often brings back enough of the content to answer. Once your admin has allowed the website, retry; if it's still blocked, start a fresh thread.

### Claude can't connect over SSH

**What you see**

Claude reports it can't reach a host over SSH, or a database's native protocol times out.

**What it means**

Every request Claude makes from a channel passes through [Agent Proxy](/docs/claude-tag/concepts/agent-identity#agent-proxy), which carries HTTP and HTTPS only. A protocol that isn't HTTP, such as SSH or a database's native wire protocol, can't cross the proxy to any host, so this isn't a connection your admin can add.

**How to resolve**

If the service exposes an HTTP API, ask your admin to [add a connection](/docs/claude-tag/admins/add-connections) for that instead.

### You've reached a Claude Tag spend limit

**What you see**

Claude posts in the thread:

> You've reached a Claude Tag spend limit. A Claude.ai organization owner can raise it in Claude.ai admin settings. Once the limit is raised, mention me to retry.

You may also see a heads-up before you hit the limit. It starts "Heads up — your organization has used *N%* of its monthly Claude Tag spend limit." for the organization limit, or "Heads up — this channel has used *N%* of its monthly Claude Tag spend limit." for a channel limit.

**What it means**

Usage hit a cap an admin set, either for the whole organization or for this channel. A rate limit looks similar but is a different problem, and raising the spend limit doesn't clear it. If your message says "Hit the session rate limit — try again in a few seconds." (or "in about Ns" when Claude knows the wait), too many sessions started at once. Wait a moment, then mention Claude again.

**How to resolve**

Ask your admin to raise the limit; they do so at [`claude.ai/admin-settings/usage/claude-tag`](https://claude.ai/admin-settings/usage/claude-tag). Your admin here is whoever manages your organization's Claude account at claude.ai, not necessarily your Slack administrator. Once the limit is raised, mention Claude in the same thread to retry.

## DMs aren't working

DMs run on your own Claude account rather than the organization's agent. They need a seat that includes Claude Code, and they use your personal connectors rather than the channel connections. If channels work but DMs don't, first check that your Claude account is connected; DM `@Claude` and it prompts you to connect if it isn't.

### I get an environment error in a DM

**What you see**

Claude replies in the DM:

> I couldn't find a Claude Code environment for your account. Set one up at claude.ai/code and try again.

**What it means**

DMs run on your own claude.ai account rather than the organization's setup, which is why this appears there and not in channels. It's usually a brief lookup failure rather than a missing environment.

**How to resolve**

1. Mention Claude again; the retry usually clears it.
2. If it keeps happening, the environment your account is set to use may no longer be available; check it at [`claude.ai/code`](https://claude.ai/code).

If a channel (not a DM) shows session-start failures that mention an environment, send your admin [the environment scope entry](/docs/claude-tag/admins/troubleshooting#channel-sessions-use-the-wrong-environment-or-can%E2%80%99t-find-one).

### Your Claude account is connected, but it doesn't have access in this organization

**What you see**

Claude replies in the DM:

> Your Claude account is connected, but it doesn't have access in this organization yet, usually because it needs a seat that includes Claude Code. A Claude admin can add one in your organization's settings. Once they do, mention me here and I'll pick this back up.

The Claude app's **Messages** tab and Slack's assistant panel both count as DMs even though neither looks like one, so this message can appear when you thought you were using a channel.

**What it means**

Your seat type doesn't include the Claude Code engine that powers DMs. Mentioning `@Claude` in a real channel doesn't depend on your seat type and keeps working.

**How to resolve**

Channels keep working while you wait, so mention `@Claude` there if you need an answer now. Then ask your admin (whoever manages your organization's Claude account at claude.ai) about your seat assignment; the [admin entry on this message](/docs/claude-tag/admins/troubleshooting#your-claude-account-is-connected-but-it-doesn%E2%80%99t-have-access-in-this-organization) covers the fix.

### Your Claude admin has disabled sending direct messages to Claude

**What you see**

Claude replies when you DM it:

> Your Claude admin has disabled sending direct messages to Claude.

**What it means**

DMs are turned off organization-wide.

**How to resolve**

Use a channel instead, or ask your admin about enabling DMs.

### Group DMs aren't supported

**What you see**

Claude replies in the group DM:

> Group DMs aren't supported yet. Try a channel or a 1:1 DM instead.

**What it means**

Claude works in channels and one-to-one DMs only.

**How to resolve**

Start a private channel with the same members instead.

## Related resources

* [How Claude Tag works](/docs/claude-tag/concepts/how-it-works): why behavior differs by channel and thread
* [Give feedback](https://support.claude.com): report a bug from the thread where it happened
