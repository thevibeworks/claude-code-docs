> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Troubleshoot Claude Tag setup

> Error messages from Claude Tag setup and what fixes each. Covers permission mismatches, GitHub access gaps, session start failures, and account errors.

export const BetaNote = () => <Info>Claude Tag is in public beta. Features and behavior described here may change before general availability.</Info>;

<BetaNote />

This page covers errors you might hit setting up and administering Claude Tag: Slack app permissions, guest and shared channels, console errors, channels and threads where nothing responds, access and connections, and session starts. Each entry has the same three parts: what you see, what it means, and how to resolve it.

<Note>For problems people can resolve on their own in a channel, like a missing reply or a thread that lost its work, see [Troubleshoot Claude Tag in channels and DMs](/docs/claude-tag/users/troubleshooting).</Note>

If someone reports that Claude can't reach a service you connected, check two things before anything else:

* The connection is in a [bundle attached to that channel's scope](/docs/claude-tag/admins/attach-to-scope).
* The test ran in a new thread; an existing thread isn't told about a connection added after it started, though the connection works there if the request names the service.

## Slack app permissions

Most errors in this section appear when Claude needs a Slack permission that wasn't part of the app when your workspace approved it. For those, the fix is a Slack workspace admin re-approving the Claude app from [Claude for Slack](https://claude.com/claude-for-slack), which grants the current permission set. Nothing else changes, and existing settings carry over.

### This workspace's Claude app installation is out of date

**What you see**

Claude replies to `@Claude connect`:

> This workspace's Claude app installation is out of date — it hasn't granted the \[permission name] permission(s). I can't create a link code until a Slack admin reinstalls the Claude app or approves its updated permissions. Once that's done, ask me to link again.

Two phrases in the message are links:

* **reinstalls the Claude app** opens the reinstall flow. The fix below starts from this link.
* **approves its updated permissions** opens Slack's Manage apps page for the workspace.

On Enterprise Grid the message names "this Slack organization's Claude app installation" and asks a Slack organization admin to reinstall the org-wide app. The org-wide reinstall works from inside one of the Grid's workspaces with **Install to entire organization**, following the steps in [Claude is silent everywhere on Enterprise Grid](#claude-is-silent-everywhere-on-enterprise-grid).

Sometimes the reply issues a code anyway, with a footnote that the install "is out of date". The reinstall steps below clear the footnote too.

**What it means**

Claude needs a Slack permission that wasn't part of the app when your workspace approved it, so the app was never granted it. Claude can't issue a link code until the updated permission set is approved.

**How to resolve**

A Slack workspace admin runs these three steps:

1. Click the **reinstalls the Claude app** link in the reply, or open [Claude for Slack](https://claude.com/claude-for-slack) and click **Add to Slack**. Don't uninstall first; this installs over the existing app, so your settings carry over.
2. Approve the consent screen Slack shows; it lists each permission being added. If Slack shows **Unapproved permissions requested** instead of completing, see [Unapproved permissions requested](#unapproved-permissions-requested).
3. Run `@Claude connect` again. If the reinstall worked, the reply contains a pairing code (the link code the original message said it couldn't create) instead of this message.

Send that pairing code to whoever runs Claude setup in the console; it expires after 15 minutes. Slack's **Manage apps** page lists the permissions the app requests, not the permissions your workspace has granted, so seeing the missing permission listed there doesn't mean it's approved. The grant happens on the consent screen. For the app's permissions in one place, see [What the Claude Slack app can access](/docs/claude-tag/admins/for-slack-admins).

### Unapproved permissions requested

**What you see**

**Unapproved permissions requested** is a message from Slack, not a Claude reply. It appears in either of two places:

* On the consent screen after **Add to Slack**, including for a workspace admin who approved the app before
* As the pending status on the Claude entry under **Settings & administration** → **Manage apps** → **App requests**, in workspaces that require admin approval for apps

**What it means**

The permissions the Claude app requests have changed since your workspace approved it, and Slack requires a fresh approval for the additions. The consent screen lists each permission being added, so you can review exactly what you're granting before approving; approval applies only to the Claude app already installed in your workspace.

**How to resolve**

A Slack workspace admin approves the Claude app's updated permissions in either place:

* In Slack, go to **Settings & administration** → **Manage apps** → **App requests** and approve the Claude request.
* Or open [Claude for Slack](https://claude.com/claude-for-slack), click **Add to Slack**, and approve the consent screen.

Both paths grant the same permissions, and neither requires uninstalling first.

If the approval worked, `@Claude connect` returns a pairing code without mentioning the installation again.

### Only Slack workspace admins or Grid org admins can link this workspace

**What you see**

Claude replies to `@Claude connect`:

> Only Slack workspace admins (or Enterprise Grid org admins) can link this workspace to a Claude organization. Please ask a workspace admin to mention me with `@Claude connect`.

**What it means**

Slack reports that the person who ran `@Claude connect` doesn't hold the workspace admin role, so no pairing code was issued. This reply is itself the signal, and there's nothing else to check. The Claude Owner role doesn't satisfy the check; it's the Slack-side role that matters.

**How to resolve**

Have a Slack workspace admin run `@Claude connect` instead. On Enterprise Grid, a Grid organization admin works too. If the fix worked, their reply contains a pairing code.

### Missing the required Slack permission (users:read)

**What you see**

Claude replies in the channel:

> Claude can't check this channel for guests because it's missing the required Slack permission (users:read). A workspace admin needs to reinstall Claude to grant it.

If the failure happens while Claude is posting a message rather than replying, there's no fixed message; Claude describes the problem in its own words, and the underlying error it relays reads "message not delivered: Claude can't check this channel for guests because the Slack app is missing a permission (users:read); a workspace admin must reinstall Claude to grant it."

**What it means**

**Allow Claude to work in channels with guests** is set to **Restrict** or **Channel only** for this channel's [scope](/docs/claude-tag/concepts/glossary#scope), so Claude checks the channel for guests before replying, and this install predates the `users:read` permission that check needs.

**How to resolve**

Re-approve the app from [Claude for Slack](https://claude.com/claude-for-slack). Don't uninstall first; the re-approval installs over the existing app. If the fix worked, a mention in the affected channel gets a reply instead of the permission message.

### The audit log shows Claude joining channels no one invited it to

**What you see**

Slack's audit log shows Claude joining a channel with no inviter recorded, and no one in the workspace remembers adding it.

**What it means**

Either a member selected **Add to channel** on a channel Claude suggested in a direct message, or the channel's name matches an [auto-join channel pattern](/docs/claude-tag/admins/restrict-access#block-or-auto-join-channels-by-name) an admin set, and Claude joined the public channel when it was created or renamed. Claude's welcome message, the introduction it posts when a member first opens a direct message with it, suggests a few public channels, each with an **Add to channel** button. Selecting one directs Claude to add itself to that channel.

Claude performs that join with its own `channels:join` permission, so Slack's audit log records the join as the Claude app and shows no inviter; the member's selection is not visible in Slack's log. Outside those two paths, Claude never joins a channel unprompted. [What the Claude Slack app can access](/docs/claude-tag/admins/for-slack-admins) covers how members add it.

**How to resolve**

Nothing is misconfigured. If an auto-join pattern brought Claude in, review the patterns in the scope's **Advanced** section. If Claude shouldn't be in the channel, remove it with `/remove @Claude`, or [set the scope's Claude Tag version to Off](/docs/claude-tag/admins/restrict-access#quiet-or-remove-claude-tag) so it stops responding there even if it's added again. If you want every join in the audit log attributed to a person, ask members to add Claude with `/invite @Claude` rather than the buttons; Slack records an invite as the inviting member's action.

## Guest and shared channels

Claude checks a channel for guests and for sharing across workspaces before it replies there. The messages those checks post look alike, but most are refusals and one is a notice on a reply Claude goes on to give. Match the exact message text before changing anything; each message has a different cause and a different fix.

A channel created at the Enterprise Grid organization level rather than inside a single workspace counts as shared across workspaces even when it appears in only one workspace's sidebar, so a channel can hit the shared-channel messages below despite looking like an ordinary single-workspace channel.

### Claude doesn't respond in channels that include guests

**What you see**

Claude replies in the channel:

> Claude doesn't respond in channels that include guests. You can remove the guests from this channel (Channel details -> Members -> filter by "guests"), or a claude.ai organization owner can allow it in Claude Tag settings under Advanced -> "Allow Claude to work in channels with guests".

In the message, "Claude Tag settings" is a link to the admin page where the guest setting described below lives. The role it names is a claude.ai organization owner, not a Slack admin.

**What it means**

The channel includes at least one Slack guest account, and **Allow Claude to work in channels with guests** is set to **Restrict** for this channel's scope. **Restrict** is the default.

**How to resolve**

Either fix works:

* Remove the guests from the channel, or move the conversation to a channel with no guests; this changes no settings, so no other channel is affected.
* Or change **Allow Claude to work in channels with guests** for the scope covering this channel; changing it needs an organization owner. **Channel only** restores replies while keeping Claude to the channel's own instructions and access. **Allow** gives guests the full access the scope has. The setting is at [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag), on the **Slack** tab under **Claude Tag's access**, in the scope's collapsed **Advanced** section. Either value applies to every guest channel that scope covers; to limit it to one channel, set it on the channel's own scope. See [restrict guest channels](/docs/claude-tag/admins/restrict-access#restrict-guest-channels) for what each value exposes.

Either value restores replies, not workspace search. Claude can't search the workspace from a channel that includes guests, even under **Allow**. Removing the guests restores search as well.

If the fix worked, a mention in the channel gets a reply.

### Couldn't check this channel just now

**What you see**

Claude replies in the channel:

> Couldn't check this channel just now. Please try again in a moment.

**What it means**

Claude couldn't complete its check for guests in this channel; either the guest-policy lookup or the Slack membership check briefly failed, so Claude declined this reply rather than risk posting where a guest might see it. This isn't a configuration error.

**How to resolve**

1. Mention Claude again; the retry usually clears it.
2. If one channel hits this repeatedly, the membership check may be failing on an unusually large channel. Setting **Allow Claude to work in channels with guests** to **Allow** on the channel's scope removes the guest check for every channel that scope covers, which usually stops the message from recurring; weigh [what Allow exposes](#claude-doesn%E2%80%99t-respond-in-channels-that-include-guests) first.

### This channel is shared across multiple workspaces

**What you see**

Claude replies in the channel:

> This channel is shared across multiple workspaces, and Claude can't verify whether it includes guests, so Claude can't respond here.

The same check also refuses requests made from another conversation, such as asking Claude to post a message in the channel, with a message ending "shared across multiple workspaces and Claude can't verify whether it includes guests".

**What it means**

This message comes from the guest check, not from workspace sharing. **Allow Claude to work in channels with guests** is set to **Restrict** or **Channel only** for this channel's scope, and the channel's membership can't be verified, most often because the channel is shared across an Enterprise Grid organization, so Claude declines.

**How to resolve**

Use a channel that belongs to a single workspace. Setting the scope's guest setting to **Allow** removes the guest check that posts this message, but a Grid-shared channel still doesn't behave like a single-workspace one. When its workspaces connect to different Claude organizations, Claude posts the refusal in [This channel is shared among several Claude workspaces](#this-channel-is-shared-among-several-claude-workspaces) instead of replying. When they all share your one Claude organization, Claude replies with only your organization's default access and settings, described in [This channel is shared across several Slack workspaces](#this-channel-is-shared-across-several-slack-workspaces).

### This channel is shared among several Claude workspaces

**What you see**

Claude replies in the channel:

> This channel is shared among several Claude workspaces, so Claude cannot respond here.

The reply appears only when someone mentions Claude directly, or addresses it in a thread it already joined. Other messages in the channel get no reply at all.

**What it means**

The channel is shared across more than one Slack workspace in your Enterprise Grid, and those workspaces are paired to different Claude organizations. No single organization's settings cover the channel, so Claude declines regardless of the guest policy or any scope setting. Claude also declines when it can't confirm that the workspaces share one Claude organization.

Two similar messages come from different situations. [This channel is shared across multiple workspaces](#this-channel-is-shared-across-multiple-workspaces) is the guest case, and [This channel is shared across several Slack workspaces](#this-channel-is-shared-across-several-slack-workspaces) is the case where every workspace belongs to your one Claude organization, so Claude replies.

**How to resolve**

Move the conversation to a channel that belongs to a single workspace, or to a DM.

### This channel is shared across several Slack workspaces

**What you see**

Claude posts a notice in the thread, then answers the request:

> This channel is shared across several Slack workspaces, so Claude is using only your organization's default Slack access and settings here — not any workspace- or channel-specific repos, instructions, or memory you've configured.

**What it means**

The channel is shared across more than one Slack workspace, and every one of those workspaces belongs to your Claude organization. Claude works there, but only with the access and settings on your [**Default Slack access**](/docs/claude-tag/admins/attach-to-scope) scope. Bundles, instructions, and memory attached to a workspace or to this channel don't apply.

The notice posts at most about once a month per channel, so replies in this channel run under the same defaults even when no notice accompanies them.

**How to resolve**

Nothing is broken. To use a channel's own repositories, connections, or instructions, work in a channel that belongs to a single workspace, or add what the channel needs to the **Default Slack access** scope. In a single-workspace channel, requests use that channel's own configuration and the notice doesn't appear.

### Claude isn't available in channels shared across your Enterprise Grid

**What you see**

You ask Claude to do something that involves a channel shared across your Enterprise Grid, and the refusal names the request it declined and ends:

> Claude isn't available in channels shared across your Enterprise Grid

**What it means**

The request needed Claude to act in a channel that's shared across more than one workspace in your Enterprise Grid. The message appears in whichever conversation you made the request; the entries above cover the replies Claude posts in the shared channel itself.

This refusal covers both sharing cases. Even when the shared channel's workspaces all belong to your one Claude organization and Claude answers direct mentions there, Claude still declines requests made from another conversation.

**How to resolve**

Point the request at a channel that belongs to a single workspace, or move the conversation to one.

### This channel is now shared across multiple workspaces

**What you see**

Claude posts in the thread:

> This channel is now shared across multiple workspaces, so this thread's earlier session can't continue here. Please @-mention me in a new thread.

**What it means**

The channel became shared after this thread's session started, so the session is still bound to one workspace's configuration and can't continue in front of every workspace that now sees the channel.

**How to resolve**

Mention Claude in a new thread; new threads start under the channel's current sharing.

## Console errors

### Couldn't load Slack scopes

**What you see**

A banner at [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag), on the **Slack** tab under **Claude Tag's access**, reads:

> Couldn't load Slack scopes. Reload the page to try again.

**What it means**

The request that loads your scope list from Claude's backend failed; it isn't a Slack permissions problem, and your configuration is intact. The page shows the error instead of an empty list so that a failed load doesn't look like an unconfigured workspace.

**How to resolve**

1. Reload the page. If the reload worked, the scope list renders. That's the usual outcome.
2. If the banner persists across reloads, check [`status.anthropic.com`](https://status.anthropic.com) for an active incident and try again in a few minutes.
3. If it continues with no incident posted, contact [Anthropic support](https://support.claude.com) with the time it occurred.

### The page shows your plan as Free

**What you see**

You open the admin console expecting your organization's settings and land on your personal account settings instead, showing the **Free plan** and no Claude Tag section anywhere.

**What it means**

You're signed into a personal claude.ai account, which is a separate workspace from your organization. claude.ai sends a personal account to its own settings page rather than to the admin console, so the **Free** you see is your personal account's plan, not a broken admin page.

**How to resolve**

Use the workspace switcher in claude.ai to switch to your organization, then reopen [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag). If the switch worked, the page shows your organization's plan and the Claude Tag settings.

## Nothing responds

Most of the silence problems in this section span a whole workspace or channel and come down to configuration. When a single thread goes quiet and Claude answers everywhere else, the cause is a stuck session rather than a setting; see [Claude went silent in one thread, but responds elsewhere](#claude-went-silent-in-one-thread-but-responds-elsewhere).

### Claude went silent in one thread, but responds elsewhere

**What you see**

In one thread, an "is thinking…" line appeared under a request and no reply followed, while Claude kept answering normally in other channels and threads.

**What it means**

The session behind that thread is stuck: it hasn't replied and hasn't posted an error. Because Claude responds everywhere else, the problem is confined to that one session, and none of the configuration fixes in the entries below apply.

**How to resolve**

Have someone in the thread send [`@Claude !restart`](/docs/claude-tag/users/commands#restart-a-stuck-or-wrong-context-session). The command archives the stuck session and starts a fresh one that rereads the thread, so a follow-up message in the same thread gets an answer. Starting a new thread and restating the request also works.

<Warning>Restarting abandons whatever the session was midway through, and there's no way to resume it. A silent session may still be working through a long task, so treat `!restart` as a last resort.</Warning>

If the same request stalls again on the fresh session, send [feedback](/docs/claude-tag/users/commands#send-feedback) from that thread so Anthropic can investigate.

### Claude is silent everywhere on Enterprise Grid

**What you see**

Mentions get no reaction and no reply in every channel and DM across the Grid, and nothing was changed on the Claude side.

**What it means**

On Enterprise Grid, the Claude app's organization-level authorization can be revoked on Slack's side without anything changing in Claude. When it is, Claude never receives the mentions at all.

**How to resolve**

Reinstall over the existing app. Don't uninstall first; installing over the top is what carries your existing settings over.

1. As a Slack org owner or org admin, sign into one of the Grid's workspaces, not the organization-level admin page. The install option only appears from inside a workspace.
2. Open [Claude for Slack](https://claude.com/claude-for-slack), select **Add to Slack**, and choose **Install to entire organization**.
3. Mention `@Claude` anywhere. If the reinstall worked, the mention gets a reaction and a reply. The pairing survives the reinstall, so a normal reply means you're done. A reply that says the workspace isn't set up means the pairing needs to be redone; see [This workspace isn't set up for Claude Tag yet](#this-workspace-isn%E2%80%99t-set-up-for-claude-tag-yet).

See [If `@Claude` doesn't respond at all](/docs/claude-tag/admins/pair-workspace#if-@claude-doesn%E2%80%99t-respond-at-all).

### This workspace isn't set up for Claude Tag yet

**What you see**

Claude replies to a mention:

> This workspace isn't set up for Claude Tag yet. A workspace admin can run `@Claude connect`, or set it up here.

The reply varies with the sender: someone who isn't a Slack workspace admin is told to ask their Claude workspace owner to run `@Claude connect`, without the settings link.

**What it means**

The Slack workspace hasn't been paired with a Claude organization.

**How to resolve**

Run [the pairing flow](/docs/claude-tag/admins/pair-workspace). If the fix worked, a mention in the workspace gets a reply.

### Using the legacy Claude in Slack bot. Ask your Claude workspace owner to enable Claude Tag.

**What you see**

Claude posts "Using the legacy Claude in Slack bot. Ask your Claude workspace owner to enable Claude Tag." as a short notice in the thread just before its first reply.

**What it means**

The earlier per-user Claude in Slack app answered the message instead of the new version. That happens when the Slack workspace isn't paired with a Claude organization that has Claude Tag turned on, or when the channel's or workspace's **Claude Tag version** is set to **Legacy**. Turning Claude Tag on needs an Owner of your Claude organization, not a Slack workspace owner.

**How to resolve**

The fix is in claude.ai admin settings, not in Slack. An Owner turns Claude Tag on at [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag) and [pairs the workspace](/docs/claude-tag/admins/pair-workspace). If the workspace is already paired, check the **Claude Tag version** on the channel's scope, then on its workspace's, and set it to **New** or **Inherit**; see [Migrate from the earlier Claude in Slack](/docs/claude-tag/admins/migrate-from-earlier). Once Claude Tag is on and the workspace is paired, the notice stops appearing.

### Claude Tag is turned off for your organization

**What you see**

Claude replies to a mention:

> Claude Tag has been turned off for your Claude organization (the one this Slack workspace is connected to). A Claude admin for that organization can turn it back on in Claude admin settings.

The same reply appears on every surface: channel mentions, DMs, and `@Claude connect`. In a DM, the parenthetical instead names the organization your connected claude.ai account belongs to, because that's the organization whose setting failed the check.

**What it means**

The **Enable Claude Tag for your organization** toggle is off in admin settings, or your organization isn't enabled for Claude Tag. The toggle that matters is the one in the Claude organization the reply's parenthetical points to.

**How to resolve**

1. An Owner switches the toggle on at [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag). If the toggle was the problem, a mention in Slack now gets a normal reply.
2. If the message persists, check which Claude organization the workspace is paired to. If your company has more than one (a trial organization alongside the main one, for example), an Owner in the wrong organization can [revoke the pairing](/docs/claude-tag/admins/workspaces#revoke-a-pairing) so you can pair the workspace to the right one.
3. If the right organization has the toggle on and the message persists, contact your account team to confirm Claude Tag is enabled for it.

### Claude Tag is unavailable because Routines are not enabled

**What you see**

Claude replies to a mention or a DM:

> Claude Tag is unavailable because Routines aren't enabled for your organization. Admins can manage Routines at claude.ai → Admin settings → Claude Code.

In the message, "claude.ai → Admin settings → Claude Code" is a link to that settings page. When Claude can't check the setting in the moment, the reply reads "Couldn't verify your organization's settings right now. Please try again in a moment." instead.

**What it means**

Your organization doesn't have Routines enabled, which Claude Tag requires. Anyone who mentions Claude in a channel or DMs it gets this reply, and Claude does no work. The "Couldn't verify" reply means the check couldn't complete rather than that Routines is off.

**How to resolve**

An admin enables Routines from the Claude Code page in admin settings, at [`claude.ai/admin-settings/claude-code`](https://claude.ai/admin-settings/claude-code). Once Routines is enabled for your organization, mention Claude again; a normal reply means the setting took effect. For the "Couldn't verify" reply, wait a moment and mention Claude again.

### Restricted compliance settings block Claude Tag

**What you see**

Claude replies to a mention in a channel:

> Claude isn't available for organizations with restricted compliance settings.

In a DM with Claude, on the Claude app's **Home** tab, and in Slack's assistant panel, the message reads instead:

> Claude in Slack is not available for your organization

In a DM and in the assistant panel, that message is shown only to you and isn't kept in the conversation, while the **Home** tab continues to show it.

Other Claude Tag actions in the same organization return similar messages that end with "not available for organizations with restricted compliance settings."

**What it means**

Your Claude organization has a restricted compliance configuration, such as Zero Data Retention (ZDR). Claude Tag retains channel memory and session transcripts, so it isn't available to organizations under that configuration; see [what Claude Tag retains](/docs/claude-tag/concepts/security-and-data).

**How to resolve**

There's no setting that lifts this; Claude Tag isn't available to these organizations. Contact your account team with questions about your organization's compliance configuration.

### Claude is disabled in this channel

**What you see**

Claude replies in the channel:

> Claude is disabled in this channel. Your admin can re-enable it here.

Only the first sentence is fixed. A sender who isn't a Slack workspace admin is told to ask their Claude workspace owner to re-enable it, with a link to the Claude Tag product page instead of admin settings.

**What it means**

This channel's scope has **Claude Tag version** set to **Off**.

**How to resolve**

An Owner changes the scope's version setting at [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag) on the **Slack** tab under **Claude Tag's access**. If the fix worked, a mention in the channel gets a reply.

## Access and connections

Access and connection errors usually mean Claude responded but couldn't reach a connected service, a repository, or a capability the sender's seat doesn't include. A scope left on **Legacy** only looks like an access problem; there, the earlier Claude in Slack answers instead of Claude Tag, so bundles and connections never apply.

### Claude says a host isn't allowed or it can't reach the internet

**What you see**

Claude in a channel says a host isn't allowed, a network request was blocked, or it can't fetch a page, even though the request was ordinary HTTP.

**What it means**

A channel session's outbound network access is deny-by-default. A host is reachable when a bundle's connection or [Domains list](/docs/claude-tag/admins/add-connections#allow-a-host-without-a-credential) allows it, or when the network access setting of the environment the scope's sessions run on allows it; anything else is blocked. Web search is separate and works regardless, so Claude can answer from search while being unable to fetch the same page; enabling web search in claude.ai admin settings doesn't open network access for channels. See [Web search vs. network requests](/docs/claude-tag/concepts/agent-identity#web-search-vs-network-requests).

**How to resolve**

* For specific hosts, add them to the bundle's [Domains list](/docs/claude-tag/admins/add-connections#add-a-domain); if the channel's scope has no bundle attached, [attach one](/docs/claude-tag/admins/attach-to-scope) first. A credential-bearing service belongs in a connection instead.
* For broad access, pin an organization-scoped environment whose network access level is Full access on the scope; see [the environment entry below](#channel-sessions-use-the-wrong-environment-or-can%E2%80%99t-find-one).

Test in a new thread. If the fix worked, the fetch that failed succeeds there.

### A connection works in one channel but not another

**What you see**

Claude uses a connected service without trouble in one channel, and in another channel says it has no access to the same service.

**What it means**

Bundles attach per scope. The working channel's scope has the bundle; the failing one likely doesn't.

**How to resolve**

Attach the bundle to the failing channel's scope, or move the work to a channel under a covered scope. Test in a new thread, or ask Claude to use the service by name in the existing one. If the fix worked, asking `@Claude what can you access from this channel?` in a new thread lists the service.

### GitHub doesn't work in this channel

**What you see**

In the channel, Claude says it has no GitHub access, can't find a repository, or opens pull requests under the asker's name instead of its own.

**What it means**

The most likely cause is a channel whose scope still has **Claude Tag version** set to **Legacy**, so the earlier Claude in Slack answers instead of Claude Tag. The other causes are a missing bundle attachment, a stale thread, an ungranted repository, or a repository the GitHub App installation doesn't cover.

**How to resolve**

Go through these checks in order; the same checks, in the same order, apply when GitHub worked in a channel and then stopped.

1. **Which version answers the channel**: if `@Claude` opens pull requests under the asker's name, the channel is on **Legacy**, and bundles only apply where Claude Tag answers. Switch the scope's **Claude Tag version** setting per [Migrate from the earlier Claude in Slack](/docs/claude-tag/admins/restrict-access#migrate-from-the-earlier-claude-in-slack). You're on the right version when pull requests open under the Claude GitHub App.
2. **A bundle with GitHub access on this channel's scope**: bundles attach per scope, so the bundle that carries GitHub access must be attached to a scope that covers this channel; [Attach the bundle to a scope](/docs/claude-tag/admins/attach-to-scope) covers attachment and inheritance. If the bundle is attached, asking `@Claude what can you access from this channel?` in a new thread lists GitHub.
3. **A fresh thread**: a new thread picks up every configuration change, so test in one before checking anything further.
4. **The repository granted in the bundle**: the repository must be listed in the bundle's **Repositories** tab, per [Grant repository access](/docs/claude-tag/admins/configure-github#grant-repository-access). If the repository is granted, asking Claude to read a file from it works in a new thread. Granting makes the repository available to clone, but the code doesn't enter a session until a request names it.
5. **The GitHub App installation covers the repository**: if Claude reports a repository isn't available, isn't configured, or returned a 403, check the installation, since the app's repository selection is upstream of the bundle grant. At [`claude.ai/admin-settings/github`](https://claude.ai/admin-settings/github), the organization that owns the repository should show **Connected** under **Connected GitHub accounts**. If it appears under **Unlinked accounts** with a **Needs permissions** status instead, the install is waiting on a GitHub organization owner. Click **Review permissions** to approve it on github.com. If you aren't a GitHub organization owner, use **Copy message** under **Not a GitHub account owner?** on that settings page to send the request to someone who is. If the organization isn't listed at all, install the app with **Install on another organization**; [Link your GitHub organization](/docs/claude-tag/admins/configure-github#link-your-github-organization) covers both.

For GitHub Enterprise Server repositories, confirm [the GHE host is registered](/docs/claude-tag/admins/configure-github#github-enterprise-server) instead. The github.com App install doesn't cover them.

### I hit an authentication error and couldn't finish this turn

**What you see**

Claude posts in the thread:

> I hit an authentication error and couldn't finish this turn. This can be temporary (for example a GitHub rate limit) — mention me to retry in a few minutes. If it keeps happening, this session may lack access to a repository it needs, or its credentials or integration may need to be reconnected.

**What it means**

Claude's own request failed an authentication check partway through the turn, so it stopped, keeping the work done so far. The cause is usually temporary, such as a GitHub rate limit on the session's requests, and a retry a few minutes later clears it. When the message repeats, the session likely can't reach a repository it needs.

This message doesn't point at a service you connected. When a connected service's credential fails, Claude reports that as a tool error inside its reply, not with this notice. A DM sender whose seat doesn't include Claude Code gets [Your Claude account is connected, but it doesn't have access in this organization](#your-claude-account-is-connected-but-it-doesn%E2%80%99t-have-access-in-this-organization) instead.

**How to resolve**

Have the requester mention Claude in the same thread after a few minutes; the session picks up where it stopped. If the message repeats on every retry, check the repository access for that channel with the steps in [GitHub doesn't work in this channel](#github-doesn%E2%80%99t-work-in-this-channel), then start a new thread. If access checks out and the message still recurs, contact [Anthropic support](https://support.claude.com) with the channel and the time it happened.

### Your Claude account is connected, but it doesn't have access in this organization

**What you see**

Claude replies in the DM:

> Your Claude account is connected, but it doesn't have access in this organization yet, usually because it needs a seat that includes Claude Code. A Claude admin can add one in your organization's settings. Once they do, mention me here and I'll pick this back up.

**What it means**

DMs run on the user's own claude.ai account and need a seat that includes Claude Code; this user's seat doesn't include it. Mentioning `@Claude` in a channel doesn't depend on the sender's seat.

**How to resolve**

Assign the user a seat that includes Claude Code on the **Members** page at [`claude.ai/admin-settings/members`](https://claude.ai/admin-settings/members), then have them mention Claude in the same DM thread. If the fix worked, the DM gets a reply instead of this message.

## Session start errors

Session start errors appear before any work begins. Some are transient and clear on retry; the rest point to capacity or environment configuration rather than credentials.

### Still waiting for available capacity

**What you see**

Claude posts in the thread:

> Still waiting for available capacity — your request is queued and will start automatically. Replies in this thread are picked up automatically.

**What it means**

Compute capacity is temporarily busy. The session starts on its own once capacity frees up.

**How to resolve**

Wait; no action is needed. Users should reply in the same thread if they have more to add, since starting a new thread only queues a second session behind the first.

### Session failed to start: the session container never connected

**What you see**

Claude posts in the thread:

> Session failed to start: the session container never connected — please try again

**What it means**

The session's compute container didn't come up in time. This is transient.

**How to resolve**

Mention Claude in the same thread to retry. If the retry worked, the session starts and Claude begins the task.

### Something went wrong starting a session

**What you see**

Claude posts in the thread:

> Something went wrong starting a session. Try again in a moment.

When Claude can name the cause, it posts one of these instead:

| Message                                                                                                  | Cause                                                                                                                                                                |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| "Hit the session rate limit — try again in a few seconds." (or "in about Ns" when Claude knows the wait) | Too many sessions started at once; wait, then mention Claude again                                                                                                   |
| A message naming a specific repository that isn't available or isn't configured                          | The repository isn't granted for this channel; see [GitHub doesn't work in this channel](#github-doesn%E2%80%99t-work-in-this-channel)                               |
| "That environment or repo isn't configured for Claude Code. Check claude.ai/code and try again."         | The scope's pinned environment isn't set up; see [Channel sessions use the wrong environment](#channel-sessions-use-the-wrong-environment-or-can%E2%80%99t-find-one) |
| "Claude is having trouble starting sessions right now. Try again in a minute."                           | The service that runs sessions is briefly unavailable; retry                                                                                                         |
| "You don't have permission to start a session here."                                                     | A permission check refused to start the session; when Claude knows which check failed, the message names it                                                          |

**What it means**

This is the catch-all for session-start failures that don't map to a more specific message, so the cause varies. It's usually transient.

**How to resolve**

Mention Claude again in the same thread before changing any configuration; the retry usually clears it. If a specific message from the table above appears instead, follow its row.

### Channel sessions use the wrong environment, or can't find one

**What you see**

Sessions in a channel start on an environment you didn't expect, or session starts fail with the environment message from the table above.

**What it means**

Each scope at [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag), on the **Slack** tab under **Claude Tag's access**, has an **Environment** picker (in the scope's **Advanced** section) that pins the Claude Code environment or runner pool that sessions in that scope use. A channel with no pin of its own inherits the nearest pin above it; with nothing pinned anywhere, sessions use the **Organization default**. The picker only lists environments scoped to the organization; an environment created under an individual account doesn't appear, because channel sessions run with no user account attached.

**How to resolve**

If the environment you want isn't in the picker, create it as an [organization-shared environment](https://code.claude.com/docs/en/cloud-environments#organization-shared-environments) from the **Cloud environments** page in [admin settings](https://claude.ai/admin-settings), then pin it on the scope. Don't create it at [`claude.ai/code`](https://claude.ai/code): environments you create there belong to your individual account, so they never appear in the picker. If the fix worked, a new thread's session runs on the pinned environment. See the [glossary entry on environments](/docs/claude-tag/concepts/glossary#environment).

## Related resources

* [Setup overview](/docs/claude-tag/admins/setup-overview): re-walk the setup steps if the failure points to one you skipped
* [User troubleshooting](/docs/claude-tag/users/troubleshooting): for problems people hit in channels
* [Give feedback](https://support.claude.com): when it's a bug, not a configuration issue
