> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Migrate from the earlier Claude in Slack

> Claude Tag replaces the earlier per-user Claude in Slack app in place. See what changes, what stays, how the version is chosen per channel, and what existing users notice.

export const BetaNote = () => <Info>Claude Tag is in public beta. Features and behavior described here may change before general availability.</Info>;

<BetaNote />

If your organization already used the earlier Claude in Slack, including [Claude Code in Slack](https://code.claude.com/docs/en/slack), Claude Tag replaces it. Your existing Slack app and `@Claude` handle stay, and no data migrates. What changes is who Claude acts as and who sets it up.

## Switch your workspace to Claude Tag

<Steps>
  <Step title="Connect the workspace in the Claude console">
    Open [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag). If your workspace isn't paired, run [setup](/docs/claude-tag/admins/setup-overview); otherwise you're already on Claude Tag. Once paired, channels and linked-user DMs answer with the New version by default; no per-channel action is needed.
  </Step>

  <Step title="Check for channels still on Legacy">
    In the **Claude Tag's access** section, look at the **Claude Tag version** on each scope. Pairing defaults every scope to New, so this is usually empty; set any showing **Legacy** to **New**.
  </Step>

  <Step title="Give Claude its connections">
    The New version starts with no access of its own. GitHub repositories and other connections do not carry over from individual users' linked accounts, so code requests in a switched channel have nothing to clone until you configure them. Follow the [setup overview](/docs/claude-tag/admins/setup-overview) to add connections, and [GitHub access](/docs/claude-tag/admins/configure-github) for code work specifically.

    If your teams keep custom skills in a repository's `.claude/skills/` folder, those skills apply only in threads that have the repository. Grant the repository in an [Access bundle](/docs/claude-tag/admins/add-connections#your-first-access-bundle) and have users name it in the first message. To give skills to every channel under a scope, add them through a [skills repository](/docs/claude-tag/admins/skills-repo).
  </Step>

  <Step title="Tell your users">
    Send them [Get started](/docs/claude-tag/users/getting-started). The visible change is that work now belongs to the channel; see [What existing users notice after the switch](#what-existing-users-notice-after-the-switch) below.
  </Step>
</Steps>

**You'll see:** the workspace appears under **Where Claude Tag works**, and the **Claude Tag version** on each scope shows **New**.

### If `@Claude` doesn't respond at all

On Enterprise Grid, an earlier install can lose its connection and stop responding in every workspace. Don't uninstall the app. Have a Slack Org Owner or Org Admin, while signed in to one of the workspaces (not the org-level admin page), open [claude.com/claude-for-slack](https://claude.com/claude-for-slack), select **Add to Slack**, and choose **Install to entire organization**. This refreshes the connection in place. Then send `@Claude connect` again in a channel of that workspace and continue with step 1 above.

<Warning>The earlier Claude in Slack app, shown as **Legacy** in admin settings, is being deprecated; check with your account team for the cutover date. After that date, channels still set to Legacy stop responding until the scope's Claude Tag version is set to New.</Warning>

## What stays the same

* The Slack app and the `@Claude` handle. Your existing Claude in Slack settings (allowed users, verified-domain restriction) carry over. If your earlier install predates a permission Claude now uses, `@Claude connect` says so when you pair; a Slack admin clicks the install link in that reply and approves the consent screen, which installs over the existing app. Otherwise no app-side action is needed.
* Direct messages still run on the user's own claude.ai account, the same way they did before. The shift to a shared identity applies to channels.
* Users who already linked their claude.ai account keep that connection. It is what powers their DMs.

## How Claude Tag differs from the earlier app

The earlier app linked each user's own claude.ai account, so it answered as that person and used their connectors. Claude Tag has one identity for the team, provisioned by an admin who also sets what it can reach in each channel.

|                | Legacy (the earlier Claude in Slack)        | New (Claude Tag)                                           |
| :------------- | :------------------------------------------ | :--------------------------------------------------------- |
| Identity       | Each user links their own claude.ai account | One agent identity with org-level service credentials      |
| Sessions       | Spawned per request                         | One persistent session per thread, shared with the channel |
| Memory         | None                                        | Shared workspace memory plus private-channel memory        |
| Standing work  | None                                        | Routines and channel watching                              |
| Who sets it up | Each user, individually                     | An Owner, once                                             |

The **Claude Tag version** setting on each scope lets you pin a channel or workspace to **Off**, **Legacy**, or **New**, or **Inherit** the organization default. Use it to hold specific channels on the Legacy behavior while you finish provisioning, then switch them when ready. Access bundles only apply where the New version answers. See [the version setting](/docs/claude-tag/admins/restrict-access#migrate-from-the-earlier-claude-in-slack) for the control.

## Two versions of the same Slack app

The earlier Claude in Slack and Claude Tag are two versions of the same `@Claude` Slack app, not two apps, so there is nothing to uninstall. You choose which version answers per scope with the **Claude Tag version** setting (**Off**, **Legacy**, **New**, or **Inherit**), so one workspace can run both during a phased switch. Setting a scope to **Off** turns off both versions there; to keep the earlier behavior in a scope, set it to **Legacy**.

To tell which version answered in a channel, look at who authored the work. The New version authors code as the Claude GitHub App and keeps work in the channel's thread; if `@Claude` still opens pull requests under the asker's name, that channel is answering with the Legacy version.

## What existing users notice after the switch

In channels, the visible difference is that work belongs to the channel, not to whoever asked. Anyone can reply in a thread to steer it, and the result stays where the team can see and pick it up. Code work is authored by the Claude GitHub App rather than as the requesting user.

A user who never linked a claude.ai account can now hand Claude work in channels, by default. Whether that stays open or narrows to organization members is the admin's [access restriction](/docs/claude-tag/admins/restrict-access#restrict-who-can-use-claude) setting.

## Related resources

* [Glossary: the earlier Claude in Slack](/docs/claude-tag/concepts/glossary#the-earlier-claude-in-slack): what each term meant in the old app versus now
* [Set up Claude Tag](/docs/claude-tag/admins/setup-overview): the new admin-side setup, since per-user setup no longer applies
* [Restrict where Claude Tag operates](/docs/claude-tag/admins/restrict-access): keep specific channels on the old version during a phased switch
