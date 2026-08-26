> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Restrict where Claude Tag operates

> Claude Tag responds only where it has been added and addressed. See who can invoke it, what changes in guest and Slack Connect channels, the per-scope version setting, how to limit it to chosen channels, how to delegate a channel's setup, and how to quiet or remove it.

export const BetaNote = () => <Info>Claude Tag is in public beta. Features and behavior described here may change before general availability.</Info>;

<BetaNote />

In channels, Claude Tag responds only where it's been added and addressed, and the controls on this page narrow that further. DMs are a separate surface that runs on the user's own account; see [how DMs differ from channels](/docs/claude-tag/concepts/agent-identity#direct-message-channels).

<Note>Most controls on this page require the Owner role in your Claude organization; the [permissions table](#permissions-by-role) below lists which actions a channel manager or a channel member can take.</Note>

## Control who can invoke Claude Tag

In channels where the app has been added, an @-mention guarantees a response; Claude may also respond to a message that doesn't mention it when it judges a reply is warranted, and once a thread is active it follows replies in that thread. By default, anyone in such a channel can address it. A single toggle narrows that to people in your Claude organization.

<a id="members" />

### Restrict who can use Claude

Open **Manage** on the Slack entry under **Where Claude Tag works** at [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag). The dialog shows a toggle that controls who in your Slack workspace can use Claude at all; its label depends on your plan. You must be an Owner of your Claude organization to change it.

| Plan       | Toggle                                       | Off (default)                                                                         | On                                                                                   |
| :--------- | :------------------------------------------- | :------------------------------------------------------------------------------------ | :----------------------------------------------------------------------------------- |
| Enterprise | **Restrict to roles with Claude Tag access** | Anyone in the connected Slack workspace can use Claude, even without a Claude account | Only members whose role grants the **Claude Tag in Slack** capability can use Claude |
| Team       | **Restrict to your organization**            | Anyone in the connected Slack workspace can use Claude, even without a Claude account | Only Slack users with a Claude account in your organization can use Claude           |

The toggle applies to channels and DMs alike.

<Info>
  You may see the earlier three-option **Members** dropdown instead of the toggle. The dialog keeps the dropdown while your organization's stored choice matches neither toggle state. That happens for an Enterprise organization that previously chose **Open to any organization member** (now marked deprecated), and for a Team organization still restricted by role from an earlier Enterprise plan. Switch to one of the toggle's two states. The dropdown is then replaced by the toggle, and the deprecated option is no longer offered.
</Info>

#### Restrict by role on Enterprise

Role restriction requires an Enterprise plan. Team plans don't have role-level control; turning on **Restrict to your organization** is the only restriction available there.

Restricting by role spans three console pages.

1. On [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag), turn on **Restrict to roles with Claude Tag access**.
2. On [`claude.ai/admin-settings/groups`](https://claude.ai/admin-settings/groups), create groups and add the relevant members.
3. On [`claude.ai/admin-settings/roles`](https://claude.ai/admin-settings/roles), create a custom role with the **Claude Tag in Slack** capability turned on or off, and choose which groups hold the role in the role editor.

Three rules govern how role restrictions resolve.

* **The toggle gates the capability.** The **Claude Tag in Slack** capability on a role has no effect until **Restrict to roles with Claude Tag access** is on. While the toggle is off, every member can use Claude regardless of what their role grants.
* **Built-in roles always grant access.** Every built-in role, including User, Owner, and Primary owner, grants **Claude Tag in Slack** automatically, so the restriction only blocks members on a custom role that doesn't grant it.
* **Any grant wins.** A member in more than one group keeps access if any of their roles grants it.

A member whose roles don't grant the capability is excluded everywhere Claude works, in three ways:

* **@-mentions and DMs get a private notice.** Claude doesn't act on the request. The member sees a notice only they can see, saying their role doesn't allow Claude Tag and to ask their admin for access.
* **Automatic replies skip them.** In channels where Claude responds without being tagged, a restricted member's messages never trigger a response.
* **Their thread replies aren't read.** In a thread an allowed member started, a restricted member's replies don't reach Claude as content. Claude sees that a message arrived, but the message body is withheld.

<Warning>On a Slack Enterprise Grid whose workspaces are paired to different Claude organizations, one organization's access settings govern the entire grid, so your restrictions may not be enforced in your own workspaces.</Warning>

### Restrict who can link a Claude account by email domain

On Enterprise plans, if your organization belongs to a parent enterprise organization, you see one more toggle in the same **Manage** dialog, **Restrict to your verified domains**. It needs an Owner to change and is disabled while Claude Tag is off for the organization. The check uses the enterprise's verified domains, which every organization under the enterprise shares.

When the toggle is on, a Slack user whose profile email isn't on one of the enterprise's verified domains can't link a Claude account to this organization; the sign-in is refused.

<Warning>Turning this on in any one organization also stops Slack users on a verified domain from linking a Claude account to any organization outside the enterprise.</Warning>

## Control where Claude Tag operates

The restriction toggle decides who can use Claude. The controls in this section decide where it works at all, from one channel up to a workspace, and which generation answers in each scope (a scope is a channel, a workspace, or your whole organization).

### Quiet or remove Claude Tag

Six ways to stop Claude Tag from responding, ordered from quietest to most complete:

1. **Ask it to stay quiet.** Saying "stay quiet in this thread unless tagged" stops Claude following an active thread.
2. **Remove it from the channel.** Run `/remove @Claude`. It can no longer read or post there.
3. **Set the scope's Claude Tag version to Off.** Claude stops responding in that scope even if someone invites it back; an @-mention gets a disabled notice instead of a reply. The control is on the scope's panel at [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag), and only an Owner can change it.
4. **Detach the scope.** The channel loses its elevated access and falls back to inherited baselines.
5. **Delete the bundle.** This revokes its credentials everywhere it was attached (the credentials are removed; memory, routines, and transcripts are not). Running sessions may keep a revoked credential for a short window before the change propagates.
6. **Uninstall the app.** This removes Claude from the workspace and deletes the workspace's Claude data the same way [disconnecting the workspace](/docs/claude-tag/admins/workspaces#revoke-a-pairing) does.

To keep Claude out of channels by name ahead of time, add a [blocked channel pattern](#block-or-auto-join-channels-by-name) instead.

Steps 1–4 do not delete any data. Step 5 (deleting a bundle) removes the credentials in that bundle; memory, routines, and session transcripts are unaffected. Removing Claude from a channel stops it responding there; the channel's memory and routines remain on record, and re-adding it restores them. To delete data without uninstalling, use the dedicated controls at [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag).

### Limit Claude Tag to specific channels

To let Claude respond only in channels you choose, for example during a pilot confined to one channel, turn the [version setting](/docs/claude-tag/admins/workspaces#set-the-version-for-a-scope) **Off** everywhere and switch the chosen channels back to **New**. Both changes happen in the **Claude Tag's access** section at [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag). DMs, guest channels, and shared channels need more than the version setting; each gets its own treatment after the steps.

<Note>**Off** silences the earlier Claude in Slack too. If you're in the middle of migrating from the earlier app, decide which scopes stay on **Legacy** before you start; the earlier app keeps answering in those channels.</Note>

<Steps>
  <Step title="Turn Claude Tag off everywhere">
    Set the **Claude Tag version** on [**Default Slack access**](/docs/claude-tag/admins/attach-to-scope) to **Off**. Then set any workspace or channel scope whose version is something other than **Inherit** to **Off** or **Inherit** too, leaving alone the scopes you're keeping on **Legacy**.
  </Step>

  <Step title="Switch the chosen channels back on">
    Set each chosen channel's version to **New**. A channel's own setting wins over the **Off** above it, so Claude responds in the chosen channels and nowhere else. Channels Claude was added to already appear in the **Claude Tag's access** section, and the version control is on each channel scope's panel; use **Search channels** to find each one. For a channel that isn't listed, create a scope with **Add channel** as described in [Attach to a channel](/docs/claude-tag/admins/attach-to-scope#attach-to-a-channel).
  </Step>
</Steps>

If someone invites the app into another channel afterward, Claude stays silent there. Mentioning `@Claude` in that channel gets a notice that Claude is disabled in the channel, not a reply.

DMs, guest channels, and shared channels sit outside the version setting:

* **DMs.** The version setting doesn't cover them. To close those off too, turn off [Allow direct messages](#allow-or-disable-direct-messages).
* **Guest channels.** By default Claude is off in any channel that includes a Slack guest. If a chosen channel has guests, also set [Allow Claude to work in channels with guests](#restrict-guest-channels) to **Allow** or **Channel only** on its scope.
* **Shared channels.** A [channel shared across workspaces in your Enterprise Grid](#channels-shared-across-workspaces-in-your-enterprise-grid) takes its settings from **Default Slack access** only and can't serve as a chosen channel. In a [Slack Connect channel](#externally-shared-channels), Claude replies only where the guest setting allows it.

To control who can use Claude in the allowed channels, turn on the [restriction toggle](#restrict-who-can-use-claude); to cap what a channel spends, [set a per-channel spend limit](#set-spend-limits).

### Block or auto-join channels by name

**Channel name rules** steer where Claude works by channel name instead of channel by channel. The rules sit in the **Advanced** section of the **Default Slack access** panel and of each workspace scope's panel at [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag), as two pattern lists:

* **Blocked channel patterns**: Claude won't read or respond in a channel whose name matches, even if someone invites it there. When it's added to such a channel or @-mentioned in one, it posts a notice that an admin has blocked it there, and otherwise stays silent.
* **Auto-join channel patterns**: Claude joins a public channel whose name matches when the channel is created or renamed. Private channels still need an invite. To add Claude to an existing channel, invite it as usual.

A pattern is written in lowercase, like Slack channel names, plus two wildcards: `*` matches any run of characters and `?` matches exactly one. `inc-*` matches every channel whose name starts with `inc-`, and `*-confidential-*` matches any name containing `-confidential-`. Each list holds up to 50 patterns of up to 80 characters.

A channel that matches a blocked pattern stays off-limits even when it also matches an auto-join pattern. Patterns on **Default Slack access** apply in every connected workspace. A workspace scope can add its own patterns but can't remove the organization's.

### Restrict guest channels

By default, Claude is disabled in any channel that includes a Slack guest. The **Allow Claude to work in channels with guests** setting changes that per scope. It's at [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag), on the **Slack** tab under **Claude Tag's access**, in the scope's collapsed **Advanced** section, and it has three values:

| Value                  | What Claude does in a channel that includes a guest                                                                                                                                                                                                                                                                                           |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Restrict** (default) | Doesn't reply. When someone mentions it, Claude posts a short notice that it doesn't respond in channels that include guests, with a link to this setting.                                                                                                                                                                                    |
| **Channel only**       | Replies, but while a guest is present it runs with channel-only access. Bundles, connectors, and instructions from the workspace or from **Default Slack access** don't reach the channel, and neither do repositories, memory, or skills. The channel's own instructions and any access bundle attached directly to the channel still apply. |
| **Allow**              | Replies with the full access the scope gives it, as in any other channel.                                                                                                                                                                                                                                                                     |

A channel without its own value shows **Inherit** and takes the value from its workspace, or from **Default Slack access**. Changing this setting requires an organization owner. The setting applies to every guest channel the scope covers; to open one channel rather than a whole workspace, set it on the channel's own scope.

Under every value, guests in the channel can read what Claude posts there. In any channel that includes a guest, even under **Allow**, Claude won't search the workspace, look up people or channels, or read channels other than the one it's in, because the results could include content the guests can't see in Slack. That is the same reason Claude doesn't search private channels. To do any of that, ask from a channel without guests.

#### How Channel only works

**Channel only** lets a team keep using Claude in a channel shared with contractors, clients, or agency partners without exposing the rest of the organization's setup to that conversation. While a guest is in the channel, Claude keeps what is set on the channel itself and drops what it would inherit:

* No [access bundles](/docs/claude-tag/admins/attach-to-scope) from the workspace or from **Default Slack access**. A bundle attached directly to this channel's scope still applies, with its connections, instructions, and plugins, so attach to a guest channel only what you're comfortable having used in front of guests.
* No repositories, including any in a bundle attached to the channel, and no connectors set directly on the channel.
* No instructions set on the workspace or the organization. Instructions set on the channel itself still apply.
* No memory, including this channel's own, and no skills.

Claude decides this when a conversation starts. When no guest is in the channel, new conversations get its usual full access, as under **Allow**. A guest can talk to Claude by mentioning `@Claude` or by replying in a thread Claude started after a guest was in the channel, and Claude answers them. In a thread Claude began before the first guest joined, Claude stops replying while a guest is present, and a guest who writes there gets the same notice as under **Restrict**; start a new thread instead. While a guest is present, Claude replies only to mentions and to threads it's already part of; it doesn't pick up other channel messages on its own, even where [**Respond automatically**](/docs/claude-tag/users/when-claude-responds#turn-automatic-replies-on-or-off) is on. A guest can't approve a tool or permission request, or restart, mute, fork, or stop the session. If a guest clicks approve, nothing is granted and a workspace member has to ask Claude again.

Treat a channel's instructions, and the instructions in any bundle attached to the channel, as visible to everyone in that channel, including guests. Under **Channel only** they shape replies that guests read and take part in.

**Channel only** takes effect where the **New** version answers. On a scope where **Legacy** answers, a channel that includes a guest is treated as **Restrict**.

<a id="externally-shared-channels" />

### Slack Connect channels

In a Slack Connect channel, one shared with another company, Claude treats everyone from the other company as a guest, and the [guest setting](#restrict-guest-channels), **Allow Claude to work in channels with guests**, decides whether it replies. Under **Restrict**, the default, Claude stays silent and posts no notice, unlike in a channel with a Slack guest. To let Claude answer, set the guest setting to **Channel only** on the channel's scope, or on a scope it inherits from; **Allow** behaves the same there, because in a Slack Connect channel Claude only ever runs with [channel-only access](#how-channel-only-works).

When Claude replies in a Slack Connect channel:

* People from the other company can ask it by mentioning `@Claude` or replying in a thread it's already in. When the [restriction toggle](#restrict-who-can-use-claude) that limits Claude to your organization's members is on, Claude doesn't answer them. Whether or not the toggle is on, they can't approve a tool or permission request.
* Claude doesn't search your workspace, look up people or channels, read other channels, or use memory. Of the [commands](/docs/claude-tag/users/commands), your organization's members can use only `!help`, `!mute`, and `!unmute`; restarting or forking a session isn't available, and neither are routines.
* Claude replies only to mentions and to threads it's already in, even where [**Respond automatically**](/docs/claude-tag/users/when-claude-responds#turn-automatic-replies-on-or-off) is on. It reads the rest of the channel as context, including what the other company's people and apps post, but never answers their apps or bots.
* You can't create a scope for a channel that's already shared; the console refuses it. A scope created before the channel was shared still applies, with its instructions and any bundle attached directly to it, so treat both as visible to the other company.
* Everyone in the channel reads what Claude posts.
* Claude stops replying in a thread it was in before the channel was shared, and posts a notice asking for a mention in a new thread.

The guest setting controls only your organization's Claude. If the other company also uses Claude Tag, their settings decide whether their Claude answers in the channel, and you can't turn theirs off from your side. Claude never answers the other company's Claude.

On Enterprise Grid, when Claude is installed at the organization level rather than per workspace, it replies only in Slack Connect channels that one of your own workspaces created. In a channel the other company created, it stays silent and posts no notice.

### Channels shared across workspaces in your Enterprise Grid

What happens in a channel shared across more than one workspace inside your Enterprise Grid depends on whether every workspace in it is connected to the same Claude organization.

When the workspaces all belong to your one Claude organization, Claude replies in the channel, but only with the access and settings on your organization's [Default Slack access](/docs/claude-tag/admins/attach-to-scope) scope. Bundles, instructions, and memory set on a workspace or on that channel don't reach it. Claude posts a notice in the thread explaining this, about once a month per channel at most rather than on every reply. Where guest access is **Restrict** or **Channel only**, the [guest check](#restrict-guest-channels) still runs first and can refuse the reply.

When the workspaces belong to different Claude organizations, each with its own settings and plan, Claude won't reply and posts a refusal message instead.

There is no per-channel override for either case.

### Migrate from the earlier Claude in Slack

If your organization used the earlier Claude in Slack app, the **Claude Tag version** setting on each scope chooses which generation answers `@Claude` there. Access bundles only apply where the New version answers. See [Set the version for a scope](/docs/claude-tag/admins/workspaces#set-the-version-for-a-scope) for the values and [Migrate from the earlier Claude in Slack](/docs/claude-tag/admins/migrate-from-earlier) for the switch.

### Allow or disable direct messages

The **Allow direct messages** toggle controls whether members can message Claude directly. When it's off, Claude is reachable only in channels. The default is on, and you must be an Owner of your Claude organization to change it.

On [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag), the toggle appears in one of two places: directly on the Claude Tag settings page, or in the **Manage** dialog on the Slack entry under **Where Claude Tag works**. It's the same setting in both places, so change it wherever it appears for your organization.

### Set spend limits

Spend limits live at [`claude.ai/admin-settings/usage/claude-tag`](https://claude.ai/admin-settings/usage/claude-tag), a different page than the main Claude Tag settings. Spend trends and per-channel reports live on a separate analytics page; see [Usage analytics](#usage-analytics) below.

A spend limit is a cap on how much of your organization's usage balance Claude Tag can draw each billing period. Setting a limit doesn't fund the balance; on a Team plan, [fund the usage balance first](/docs/claude-tag/admins/set-spend-limit) or Claude won't respond in channels regardless of the limit.

* **Organization-wide limit.** Caps total Claude Tag spend across every channel.
* **Default spend limit.** A default limit applied to each channel that doesn't have its own.
* **Per-channel limits.** Set on any channel from its row in the per-channel spend table, in addition to the organization limit. A channel doesn't need its own scope to take a limit.
* **Per-channel spend.** How much each channel has spent against its limit in the current billing period, at list price, on the same page.

Work that would exceed a limit is declined rather than silently truncated. A user blocked by a limit can request more usage from their admin in Slack, and the admin notification names whether the usage balance or the limit caused the block.

### Usage analytics

Spend trends live at [`claude.ai/analytics/claude-tag`](https://claude.ai/analytics/claude-tag), the Claude Tag section of the Analytics dashboard. It shows total and projected month-end spend for the period you pick, spend by channel with a CSV export, DM versus channel spend, [spend by kind of work](/docs/claude-tag/admins/set-spend-limit#see-spend-by-kind-of-work), and any promotional credit, as billed after your discount. Anyone with permission to view your organization's Analytics dashboard can open it; it has no controls, so use the usage page to change a limit. The two pages link to each other.

## Delegate channel setup to channel managers

A channel manager is a member of your Claude organization who can set up Claude in specific channels without the Owner role. Channel managers are available on the Enterprise plan, and you must be an Owner to add or remove them.

You name channel managers one channel at a time. For that channel, a channel manager adds repositories and credentials, sets the default model, and edits channel instructions. Every other setting at [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag) stays with Owners.

### What a channel manager can do on the Configure page

A channel manager has to be a member of the channel in Slack. The channel's [Configure page](/docs/claude-tag/users/good-habits#configure-claude-for-a-channel), reached from the **Configure** link in any Claude reply, is split into tabs. In a channel you assigned to them, a channel manager sees the **Default model** card on the **General** tab and the repository and access bundle cards on the **Tools and access** tab. Members without the role don't see those cards. Owners and Admins also see an **Admin** tab, whose **Channel settings** card holds some of the channel scope's settings from admin settings.

| Setting            | What a channel manager can do                                                                                                                                                                                                                                   |
| :----------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Default model**  | Choose the model new threads in the channel start on, from the models your organization allows. **Inherit** keeps the workspace or organization default                                                                                                         |
| **Repositories**   | Add repositories beyond the ones your bundles already grant the channel. They can add only repositories their own GitHub account can write to                                                                                                                   |
| **Access bundles** | Add, rotate, test, and remove credentials in the bundle Claude created for the channel and in any bundle they created for it. If the channel has no bundle yet, they can create one. They can't edit a bundle you created or a bundle that other channels share |

When a channel manager adds a credential, Claude also allows the host that credential uses. Channel managers can't change the bundle's domains or rules in any other way. Credentials that use Claude's own identity (mutual TLS, AWS or GCP service identity, and IAP) stay Owner-only: a channel manager can't add, change, or rotate one, but can delete one from the channel's bundle, including one an Owner added. If that happens, Claude loses access to that service until an Owner adds the credential back.

If you detach the channel's own bundle from the channel, its channel managers can't save settings for the channel; they see an error saying the channel's configuration was suspended by an administrator. They don't get a new bundle. Attach the bundle again to restore their access.

A channel manager can edit channel instructions even when the scope's [Channel member edits](/docs/claude-tag/admins/attach-to-scope#restrict-who-can-set-channel-instructions) setting is **Block**.

Channel managers see their assigned channels at [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag); organization and workspace settings are read-only for them. Tell them when you add them.

### Add a channel manager

Channel managers are built on [custom roles](https://claude.ai/admin-settings/roles). When you add the first manager to a channel, you create a custom role for it, named **Channel managers** plus the channel's name and ID, with the **Claude Tag channel setup** permission. A custom role works only for members on the **Custom roles** access level, so the last step below checks each manager's level.

<Steps>
  <Step title="Open the channel's panel">
    At [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag), select the channel's row on the **Slack** tab under **Claude Tag's access**. The channel must be a public or private channel. If it isn't listed, [add Claude to the channel](/docs/claude-tag/users/getting-started#add-claude-to-a-channel) in Slack first.
  </Step>

  <Step title="Add people or a group">
    In the panel's header, select the people-icon button labeled **Add channel managers who can add connections and repos to this channel**. In the popup, select **Add users** to add people, which also creates a group named after the channel, or **Add groups** to add a group from [`claude.ai/admin-settings/groups`](https://claude.ai/admin-settings/groups). The same group can manage several channels.
  </Step>

  <Step title="Check each manager's access level">
    When you add a member on the User or Claude Code user level, you move them to the **Custom roles** level in the same step; if they already hold other custom roles, you confirm the move first. For a member on any other level, you see **Not in effect** until you change their level on the Members page. Adding a group changes nobody's level; group members who aren't on the **Custom roles** level show **Not in effect** too.

    If your identity provider manages access levels, you can't change a level on the Members page, and the move doesn't happen. Put the channel managers in an identity provider group and map that group to the **Custom roles** level instead. If you turn on identity provider management after adding channel managers, the next sync sets every member's level from your group mappings, so managers you moved by hand show **Not in effect** until a mapped group covers them. The role and its group are kept; you don't need to add the managers again.
  </Step>
</Steps>

Owners and Admins can already configure every channel, so you see them as **Already has full access** and can't add them.

Leave the role as it was created: assigned to its channel, with **Claude Tag channel setup** as its only permission. If the role's permissions are changed on the Roles page, the channel's channel-managers popup stops recognizing the role and refuses to add or remove any, with a notice that points you to the Roles page. To recover, set the role's permissions back to exactly **Claude Tag channel setup**; the group and its members are kept. To give channel managers any other permission, create a separate role for it.

### Remove a channel manager

To remove a channel manager, open the same popup from the people-icon button on the channel's panel. The current managers are listed under **Channel managers**. Remove a member you added directly, or detach a group you added. The member keeps their access level and any other custom roles. The manager cards on the channel's Configure page disappear for them.

### Verify a channel manager's access

The popup behind the people-icon button on the channel's panel shows each manager's status under **Channel managers**. A member whose access level doesn't support the role appears as **Not in effect**; the role works only on the **Custom roles** access level, so change the member's level on the Members page to put it into effect. An active manager sees the **Default model**, repository, and access bundle cards on the channel's [Configure page](/docs/claude-tag/users/good-habits#configure-claude-for-a-channel), so asking them to open that page confirms the setup.

### Audit channel manager activity

Channel manager activity is recorded in your organization's audit log, which you read through the [Compliance API](https://platform.claude.com/docs/en/api/compliance). The log records:

* **Role channel assignments.** When a channel is assigned to a channel manager role or removed from it, with the role and the number of channels before and after.
* **Credential changes.** Each credential a channel manager creates, updates, rotates, or deletes, with the Slack workspace and channel it was for and the roles that granted the permission, so you can tell a channel manager's change from an Owner's. Secrets are never included.
* **Configure page changes.** Which settings a channel manager saved from the Configure page, such as the default model, repositories, or channel instructions. The log records which fields changed, not the values entered.

The [Audit page](/docs/claude-tag/admins/audit) at [`claude.ai/admin-settings/claude-tag/audit`](https://claude.ai/admin-settings/claude-tag/audit) doesn't list these events; it covers scheduled work, memory, and network events.

## Permissions by role

Creating bundles, binding them to scopes, and pairing workspaces need an Owner. A [channel manager](#delegate-channel-setup-to-channel-managers) configures only the channels assigned to them. Everything else happens inside the channel and is open to its members. The table lists each action and who can take it.

| Action                                                                | Owner               | Channel manager                                                   | Channel member                                                                                                                                 |
| :-------------------------------------------------------------------- | :------------------ | :---------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------- |
| Pair a workspace                                                      | Yes                 | No                                                                | No                                                                                                                                             |
| Create, rename, delete, or bind an Access bundle                      | Yes                 | Only to create a bundle for an assigned channel                   | No                                                                                                                                             |
| Edit a bundle's Repositories, Plugins, or Instructions tab            | Yes                 | No                                                                | No                                                                                                                                             |
| Edit a bundle's Credentials or Domains tab                            | Yes                 | Credentials tab only, in a bundle created for an assigned channel | No                                                                                                                                             |
| Add a channel manager                                                 | Yes                 | No                                                                | No                                                                                                                                             |
| Set a channel's default model or repositories from the Configure page | Yes                 | Yes, in assigned channels                                         | No                                                                                                                                             |
| Write channel memory                                                  | Yes, in the channel | Yes, in the channel                                               | Yes                                                                                                                                            |
| Set channel instructions from the Configure link                      | Yes                 | Yes, in assigned channels                                         | Yes, unless the scope's [Channel member edits](/docs/claude-tag/admins/attach-to-scope#restrict-who-can-set-channel-instructions) setting blocks it |
| Create, list, or disable a scheduled job in the channel               | Yes, in the channel | Yes, in the channel                                               | Yes                                                                                                                                            |
| Remove Claude from a channel                                          | Yes                 | Yes, with `/remove`, unless your Slack admin restricts it         | Yes, with `/remove`, unless your Slack admin restricts it                                                                                      |

Scheduled jobs run with the channel's credentials, so a member creating one can't reach anything the channel itself can't.

## Controls that aren't available

These are controls an admin might look for that Claude Tag doesn't have.

* **Third-party deployment.** Sessions run on Anthropic's first-party infrastructure; Claude Tag isn't available through third-party deployments.
* **Renaming or rebranding the app.** The Claude app's name, @-handle, and avatar in Slack are fixed; there is no per-workspace rename setting.
* **Per-user spend caps on channel work.** Spend limits apply at the organization and channel level. There's no way to cap what one member can spend in channels; DM usage bills to that member's own seat and follows the seat's usual limits.
* **Per-channel responder allowlist.** The restriction toggle governs who can invoke Claude across the workspace; you can't narrow it to a list of people for one channel only.
* **An open-internet switch in Claude Tag settings.** A channel sandbox reaches only allowed hosts. To let Claude reach a public site or API, an Owner adds that hostname on a [bundle's Domains tab](/docs/claude-tag/admins/add-connections#allow-a-host-without-a-credential); for broad web access, they pin an [environment](/docs/claude-tag/concepts/glossary#environment) whose network access level is Full access on the scope. [Allow-all egress](/docs/claude-tag/admins/add-connections#allow-all-hosts), a `*` entry on the Domains tab, is off by default and enabled per organization by Anthropic.
* **A web search toggle for channels.** No setting turns web search off for channel sessions; the web search capability setting in claude.ai admin settings governs claude.ai chat, not channels. Web search runs on Anthropic's servers rather than from the channel sandbox, so Domains entries and egress settings don't govern it, and a search opens no new path out of the sandbox; search requests travel to Anthropic the same way the session's model traffic already does. See [Web search vs. network requests](/docs/claude-tag/concepts/agent-identity#web-search-vs-network-requests).
* **Read-scope confinement.** Claude can search public channels by keyword the same way any Slack user can; it can't read a channel's full history unless it's been added there. There's no setting to disable workspace search, and no setting to enable it in [channels that include guests](#restrict-guest-channels), where search is unavailable.
* **Session length enforcement.** Your organization's Slack session-length policy is not enforced on this surface.

## Related resources

* [Configure per-channel access](/docs/claude-tag/admins/attach-to-scope): change the scopes these controls apply to
* [How agent identity works](/docs/claude-tag/concepts/agent-identity): the model these controls operate on
* [Security and data handling](/docs/claude-tag/concepts/security-and-data): what these controls don't cover (data flow, retention, where credentials are stored)
* [Data lifecycle and deletion](/docs/claude-tag/concepts/data-lifecycle): which of these controls delete data and which only stop Claude responding
