# Share artifacts

This article explains how to share an artifact, who can open it, and what people see when they do. It covers every plan and every place you make artifacts: in a chat, from a template, and in Claude Code.

Artifacts start private to you. Nothing is shared until you share it.

| **Sharing option**                                                 | **Free** | **Pro** | **Max** | **Team** | **Enterprise** |
| ------------------------------------------------------------------ | -------- | ------- | ------- | -------- | -------------- |
| Share with anyone who has the link                                 |          | ✅       | ✅       | ✅        | ✅              |
| Share with everyone, or with specific people, in your organization |          |         |         | ✅        | ✅              |
| Share with groups                                                  |          |         |         |          | ✅              |
| Invite specific people by email (beta)                             |          | ✅       | ✅       | ✅        | ✅              |
| Publish a legacy artifact (made in a chat)                         | ✅        | ✅       | ✅       |          |                |
| Share a legacy artifact with "Share & copy link"                   |          |         |         | ✅        | ✅              |

On Team and Enterprise plans, artifacts stay inside your organization by default. An owner decides whether users can share outside it. Learn more in the **[Artifacts admin guide for Team and Enterprise plans](https://support.claude.com/en/articles/16994751-artifacts-admin-guide-for-team-and-enterprise-plans#h_fd0c095985)**.

**Note:** Live artifacts, which are Cowork artifacts made before August 19, 2026, have their own sharing rules. Learn more about **[using live artifacts in Claude Cowork](https://support.claude.com/en/articles/14729249)**.

**Note:** Legacy artifacts show "Publish" or "Share & copy link" instead of "Share." To share those, see **[Publish or share a legacy artifact](#h_a5750b9176)**.

---

## Share an artifact

1. Open the artifact and click "Share."

2. On Team and Enterprise plans, add people from your organization, and choose each one's access level. Enterprise plans can also add groups.

3. Under **Who has access**, choose who else can open the artifact.

4. Copy the link and send it.

**Note:** You can't change sharing settings in Claude for iOS or Claude for Android. Use Claude on the web or Claude Desktop.

### Choose who has access

- **Pro and Max plans:** "Only you" or "Anyone with the link." To give specific people access, invite them by email.

- **Team and Enterprise plans:** "Only people invited," "Anyone at [your organization's name]," or "Anyone with the link." "Only you" shows when you haven't added anyone. "Anyone with the link" is available only when an Owner has turned on **External sharing** or has allowed that artifact individually. If it's grayed out, ask an Owner or Primary Owner.

### Choose an access level

| **Access**    | **What people can do**                                                                    |
| ------------- | ----------------------------------------------------------------------------------------- |
| **Can view**  | Open the artifact and read its comments.                                                  |
| **Commenter** | Everything in **Can view**, plus add comments and download any files the artifact offers. |
| **Can edit**  | Everything in **Commenter**, plus make changes.                                           |

The levels you can choose depend on the artifact. **Can view** or **Can edit**. Every other type of artifact offers all three levels.

---

## Invite people by email

Available in beta on Pro, Max, Team, and Enterprise plans.

You can invite specific people by email to access an artifact. They sign in to Claude with the email address you used and open the artifact with the access you give them. Unlike "Anyone with the link," an invitation works only for the person you invite.

### Before you invite someone

- **Who can invite:** The artifact's owner. On Team and Enterprise plans, anyone in your organization who can edit the artifact can also invite people. The owner gets an email when someone else sends an invitation.

- **Team and Enterprise plans:** **Email invitations outside your organization** needs to be on in **[Organization settings > Artifacts](https://claude.ai/admin-settings/artifacts)**. It's on by default on Team plans and off on Enterprise plans. If you don't see the option, ask an Owner or Primary Owner.

- **The invitee needs a Claude account** with the email address you invited. If they don't have one, they need to create one with that address before they can open the artifact. Claude doesn't tell you whether or not they have an account.

- **Some artifacts can't be shared this way.** The "Share" menu tells you when this applies:

  - Documents made with Claude Docs

  - Artifacts that connect to other websites

  - Artifacts with an uploaded file that's still being checked or didn't pass the check

### Send an invitation

1. Open the artifact and click "Share."

2. In the field at the top of the **Share** menu (**Add people**, or **Invite people by email** on Pro and Max plans), type the person's email address.

3. Select the **Invite** option that shows their address.

4. Under **Their access**, choose "Can view," "Commenter," or "Can edit."

5. Click "Invite."

On Team and Enterprise plans, if you type the address of someone in your organization, they're added to the artifact directly instead of getting an invitation.

### What people you invite can do

People you invite from outside your organization can't invite others or change sharing settings. Parts of the artifact that use Claude or your connectors don't work for them. People with “Can edit” access can't delete the artifact, and they can upload only images and videos to it.

People you invite with “Commenter” or “Can edit” access can comment, but they can't mention people or ask Claude in a comment, and they don't get email notifications about comments. They can't comment on an artifact that's also shared with "Anyone with the link."

If the artifact is also shared with "Anyone with the link," the people you invited have the same access as anyone with the link, whatever level you gave them.

### Manage people you've invited

In the artifact's **Share** menu, people you've invited appear under **Invited from outside your organization**, and pending invitations show when they expire. From there, you can change someone's access or remove them. Removing someone takes away their access right away.

If someone didn't get an invitation email because they didn't have a Claude account yet, ask them to create one with that address. Then remove the invitation and invite them again.

### When access changes

- **Pending invitations expire after 30 days.** Accepted invitations don't expire.

- **If you change who can open the artifact to "Only you":** On Team and Enterprise plans, everyone you invited from outside your organization loses access, and their invitations are removed. On Pro and Max plans, people you invited keep their access.

- **If you delete the artifact:** Everyone you invited loses access.

- **If the person who sent an invitation leaves your organization or loses edit access:** Their pending invitations stop working. People who already accepted keep access until someone removes them.

- **If an owner turns off email invitations:** People you invited can't open the artifact until the setting is turned back on. Accepted invitations aren't deleted, and pending ones still expire 30 days after they were sent.

### Limits

- You can invite up to 50 people from outside your organization per artifact, counting pending and accepted invitations.

- Invitation emails are in English.

---

## Who can open a shared artifact

- **Everyone needs a Claude account.** People without one can't open a shared artifact, even with the link. The only exception is a legacy artifact published from a chat.

- **Everyone in your organization:** Only people signed in to your organization can open it.

- **Anyone with the link:** Anyone signed in to Claude who has the link can open it. On Team and Enterprise plans, if an owner turns off **External sharing**, these links stop working until it's turned back on, unless an owner has allowed that artifact individually.

### Artifacts that can't be shared outside your organization

- **By link:** Artifacts that connect to your apps or use Claude can't use "Anyone with the link." On Team and Enterprise plans, docs can't use it yet either.

- **By email invitation:** See the list in **[Before you invite someone](#h_4abce57435)**.

### What people see when they open your artifact

- **Viewers use their own access.** An **[artifact that pulls from connected apps](https://support.claude.com/en/articles/9487310-what-are-artifacts-and-how-do-i-use-them#h_1a161da210)** uses the viewer's connections, not yours. If a viewer can't access a data source, that part of the artifact shows an error instead of your data.

- **Stored information can be shared.** Some artifacts save information that everyone who opens them can see, like items in a shared tracker. Before you enter sensitive information, check whether the **[artifact uses shared storage](https://support.claude.com/en/articles/9487310-what-are-artifacts-and-how-do-i-use-them#h_135477d2e6)**.

**Important:** Only open shared artifacts from people you trust. Treat someone else's artifact the way you'd treat a file from an unknown sender.

---

## Stop sharing an artifact

To stop sharing an artifact, open it, click "Share," and under **Who has access**, choose "Only you" (Pro and Max) or "Only people invited" (Team and Enterprise). To remove someone you added, open their access level and select "Remove."

On Team and Enterprise plans, owners can also remove outside access to individual artifacts. Learn more in the **[Artifacts admin guide for Team and Enterprise plans](https://support.claude.com/en/articles/16994751-artifacts-admin-guide-for-team-and-enterprise-plans#h_929aa51571)**.

---

## Open an artifact you were invited to

1. Open the email from Claude (<no-reply-claude@mail.anthropic.com>). It shows the email address of the person who invited you and what access you'll have.

2. Click "View invitation" and sign in to Claude in a web browser with the address the invitation was sent to.

3. Click "Accept and open."

To come back to the artifact later, open the link in the invitation email again or bookmark the artifact.

### Report an invitation you didn't expect

Click "Report this invitation" in the email, or "Didn't expect this? Report this invitation" on the invitation page. Reporting declines the invitation, and the person who sent it isn't notified. After you report an invitation, that person can't invite you by email again.

---

## Publish or share a legacy artifact

Legacy artifacts show "Publish" (Free, Pro, and Max plans) or "Share & copy link" (Team and Enterprise plans) instead of "Share." Use the steps in this section for those artifacts.

### Publish a legacy artifact on Free, Pro, and Max plans

1. Open the artifact you want to publish.

2. Click "Publish."

3. Copy the public link and send it.

Publishing adds the artifact to **[Artifacts](https://claude.ai/artifacts)** in your sidebar, so you can find it again outside the original chat.

**Who can open a published chat artifact:**

- Anyone with the link can view and use it without a Claude account. They're asked to sign up only for features that use Claude.

- People signed in on Free, Pro, or Max plans can also copy and save it. Features that use Claude count toward their own usage limits.

### Embed a published chat artifact

After you publish, click "Get embed code" to get code you can paste into another website. In the **Allowed domains** field, enter the websites that can embed your artifact, separated by commas.

### Unpublish a chat artifact

Click "Unpublish" to revoke access to a published artifact.

**Important:** You can't publish an artifact again after you unpublish it. To share it later, you'll need to create a new artifact. Unpublishing also permanently deletes any personal and shared storage data the artifact used.

### Share a chat artifact on Team and Enterprise plans

1. Open the artifact you want to share.

2. Click "Share."

3. Click "Share & copy link."

**Who can open it:**

- Users in your organization, signed in with their Team or Enterprise account.

- Anyone with the link, if an owner has turned on **External sharing** and you chose "Anyone with the link." They need a Claude account.

- If the artifact was made in a project, viewers also need access to that project.

**Important:** When you share an artifact made in a chat, viewers also get access to the attachments and files in that chat. Check for sensitive documents before you share.

**To unshare a chat artifact:**

1. Click "Share" in the upper right corner of the artifact.

2. In the **Artifact shared** modal, click "Unshare."

---

## Learn more

Learn more about **[creating and working with artifacts](https://support.claude.com/en/articles/9487310)**. For organization settings that control sharing, see the **[Artifacts admin guide for Team and Enterprise plans](https://support.claude.com/en/articles/16994751)**. For Claude Code, see the **[artifacts documentation on Claude Code Docs](https://code.claude.com/docs/en/artifacts)**.