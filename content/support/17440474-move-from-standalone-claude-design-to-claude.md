# Move from standalone Claude Design to Claude

Claude Design now lives in Claude. The standalone Claude Design site (claude.ai/design) will close on December 14, 2026, and you can still access it until that date. This article explains what's changing and when, how to move your design systems today, and what happens to your projects.

Claude Design is available on Free, Pro, Max, Team, and Enterprise plans.

## What's changing and when

You can keep using the standalone version until it closes on December 14, 2026. After that, it's read-only, and you can't start new projects there.

When you start a new design, design system, or slide deck in Claude, it's created as an artifact.

## What happens to your work

When you move a design system, the original stays in the standalone version. Your chats and comments can't move to Claude, so they stay in the standalone version until it closes.

**Important:** Design systems that have already moved become read-only for everyone in the standalone version as soon as Move to Claude is available to your organization. If you've kept editing one there, those changes didn't move, so make them again in Claude.

## What you need to do

- Move your design systems now.

- On Team and Enterprise plans, ask your organization's owner to set a default design system to get the most out of artifacts.

- Moving projects to Claude is rolling out gradually to paid plans. Once you can, move the projects you want to keep. See What happens to your projects.

- If you're a Team or Enterprise owner, check that artifacts and design systems are turned on. On Enterprise plans, design systems are off by default.

---

## Move your design systems

**Note:** Once **Move to Claude** is available to your organization, design systems no longer have their own move. They move the same way as projects. Each design system's owner can move it, or an owner of your organization can move everything at once. See **[What happens to your projects](#h_1d425b60a1)**.

### Before you start

- One move brings over every design system in your organization, including other people's, so it only needs to be started once.

- Anyone who can use Claude Design can start it, not just your organization's owners.

- Each design system keeps its owner and the people it's shared with. If the owner has left your organization, the Primary Owner becomes its owner.

- Empty design systems aren't moved, and neither are ones made from a built-in starter theme, even if you've edited them.

**Important:** Published design systems that aren't private will be shared with everyone in your organization and appear in their design system menu. On individual plans, nothing is shared.

### Start the move

1. Open the **Artifacts** page in Claude.

2. Click "Move team design systems" in the "Claude Design lives here now" banner. If you've closed the banner, choose it from the Claude Design menu. To open the menu, click the "…" button on the Design tile under "Make something new." If there's no Design tile, click the "…" button at the top right of the page.

3. Click "Move" to confirm. On individual plans, there's no confirmation step, and the move starts right away.

4. Wait for the move to finish. If you close the window, it keeps running.

5. Check the results. Under Moved, the window lists each design system with its owner's name and an "Open" link. You'll see only the design systems you have access to, unless you're an owner of your organization.

## After the move

Your moved design systems appear in the design system menu when you make designs and slide decks in Claude. To see them all, choose "View design systems" from the Claude Design menu on the Artifacts page. The list opens in Settings.

Owners can set your organization's default design system here. Open a design system's menu and choose "Set as default." Click a design system's name to open it.

A moved design system keeps its files as they were, and you can't edit it yourself on its page yet. Its editors see a note at the top saying that it was moved and that they can ask Claude to make changes.

Learn more about **[getting started with Claude Design](https://support.claude.com/en/articles/14604416-get-started-with-claude-design)**.

### If a design system can't move

The window lists it under **Didn't move**, with its name, owner, and a short reason, such as "it's too large."

To reopen the results later, click the count in the banner on the Artifacts page, such as "6 of your 11 design systems couldn't move."

Anyone who can edit the design system can fix problems with its own files or size. If you can't edit it, you won't be able to run the check, so ask its owner, who's named in the row.

**To fix a design system:**

1. Click "Fix in Claude Design Standalone" in its row.

2. Click "Check" on the **Check whether this design system can move to Claude** card.

3. Fix the files the check lists, using the table below.

4. Click "Check again" until it says "Nothing found in the way."

5. Move again from the **Artifacts** page in Claude.

| **What the check says**              | **What to do**                    |
| ------------------------------------ | --------------------------------- |
| Too large for an artifact            | Shrink or remove them             |
| With a name an artifact can't use    | Rename them                       |
| A kind an artifact can't hold        | Convert or remove them            |
| Can't go in a design system artifact | Remove them                       |
| Can't be opened                      | Save them again, or remove them   |
| With characters that can't be read   | Fix or remove them                |
| Contents missing                     | Upload them again, or remove them |

If the whole design system is too large, the card says "It's too large. Make it smaller." instead of listing files. Remove files you don't need, then check again.

**Note:** The `uploads` folder often contains duplicate files, so it's an easy place to start trimming down a design system.

Some reasons need your organization's owner to fix them: "design systems are turned off for your team," "your team can't publish artifacts," or "its owner's role doesn't include design systems." The first two stop the move, and any design systems it hadn't started are listed under **Not started**. Once they're fixed, move again.

Sometimes the card says "Can't move this design system" without saying why. If this happens, click "Download design system" to keep a copy of its files. You can click "Check again" later, and if it still can't move, let us know. See **[Get help](#h_5acf964297)**.

### Move again

**Note:** Once **Move to Claude** is available to your organization, this section no longer applies. A later move doesn't update a design system that has already moved. To replace it with a fresh copy, its owner deletes it in Claude, then moves it again from the standalone version.

To move new, changed, or fixed design systems, choose "Move again" from the Claude Design menu on the Artifacts page. To reopen your last results, choose "View last move," just below it.

**When you move again:**

| **If the design system is**                                   | **What happens**                                                                                                  |
| ------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| New, or changed in the standalone version since the last move | It's moved                                                                                                        |
| Unchanged in both places                                      | It's left alone and marked "already moved"                                                                        |
| Changed in Claude since it was moved                          | It's listed under Skipped as "changed on claude.ai, left as they are," so your edits in Claude aren't overwritten |

To replace a moved design system with a fresh copy, delete it in Claude, then move again. To keep any changes you've made to it, duplicate it first.

## What happens to your projects

Until they're moved, your projects stay in the standalone version and keep working until it closes. The **Artifacts** page in Claude also lists up to 60 of them, and they open in the standalone version.

Moving a project to Claude, where it becomes an artifact, is rolling out gradually to paid plans.

- On Team and Enterprise plans, artifacts also need to be on for your organization. On Enterprise plans with custom roles, your role needs them too.

- Organizations with customer-managed encryption keys (CMEK) can move one project at a time, but can't yet move lists of projects, design systems, or everything at once. Standalone Claude Design doesn't support CMEK, so its data won't be encrypted under your key until you move. Once a project moves to Claude, it's encrypted under your key.

- Organizations with the HIPAA-ready configuration can't move projects right now.

- Organizations with zero data retention (ZDR) can't move projects, so download your projects before the standalone version closes.

To move a project:

1. Open the project in the standalone version at claude.ai/design. Only the project's owner can move it.

2. Start the review from the pop-up or from the banner at the top of the project.

3. Read the review. It lists what moves, anything that will work differently, and what stays behind. You can also download a copy as a .zip file. Then confirm the move.

4. Keep the tab open until the move finishes.

5. Open the project in Claude. It's now an artifact on the Artifacts page.

After the move, the copy in the standalone version is read-only for everyone, and this can't be undone. Your chats and comments stay in that copy, where you can read them until the standalone version closes. Sharing carries over where Claude supports it.

You can also move all of your own projects at once, or only the ones you choose. On Team and Enterprise plans, your organization's owners can move everyone's projects at once with "Move everything."

"Move everything" is on the Artifacts page in Claude, and it moves templates and design systems too. Only an Owner or the Primary Owner can start it, not an Admin.

Most projects keep their owner, and private projects stay private. If a project's owner has left your organization, it goes to an owner of your organization, usually the Primary Owner, and Claude shows that person a list called "Projects moved to you." Anything that can't move stays in the standalone version, and the results say why. As with any move, the standalone copies of moved projects become read-only for everyone.

**Important:** If your organization has a retention period that covers artifacts, a project or design system that moves, or has already moved, to Claude can be permanently deleted if nobody opens it for that period. The period starts on the day of the move and restarts when someone opens or edits the artifact. Learn more in **[Configure custom data retention controls for Enterprise plans](https://support.claude.com/en/articles/10440198)**.

## What isn't carried over

These stay in the standalone version and are deleted some time after it closes, per our **[data retention practices](https://privacy.claude.com/en/articles/10023548-how-long-do-you-store-my-data)**:

- Your chats with Claude

- Comments on your projects and design systems

Public links to projects in the standalone version will no longer work after it closes.

**Important:** Save anything you need from your chats and comments before the standalone version closes.

---

## For Team and Enterprise owners

Claude Design in Claude depends on artifacts. If artifacts are off for your organization, people can't create designs in Claude or move anything, and they won't see the "Claude Design lives here now" banner.

To check your settings, navigate to **[Organization settings](https://claude.ai/admin-settings/artifacts)**[> **Artifacts**](https://claude.ai/admin-settings/artifacts):

| **Setting**                                    | **What it's for**                              | **Default**                                 |
| ---------------------------------------------- | ---------------------------------------------- | ------------------------------------------- |
| **Artifacts**                                  | Everything below depends on it                 | On                                          |
| **Design systems**, under **Templates**        | Moving design systems and creating new ones    | On for Team plans, off for Enterprise plans |
| **Design** and **Slides**, under **Templates** | Creating new designs and slide decks in Claude | On                                          |

On Enterprise plans with custom roles, each role also needs these permissions, which the role editor lists under **Artifacts**. This lets you turn on artifacts for just the people who use Claude Design. A design system can't move if its owner's role doesn't include design systems.

While **Design systems** is off, owners who click "Move team design systems" see "Design systems are off for your organization" and an "Open Organization settings" button. Everyone else sees the button grayed out, with the reason "Design systems are turned off in your organization's Artifacts settings."

If your organization's default design system moves, it becomes the default in Claude too, unless you've already set one there.

Organizations with zero data retention (ZDR) can't turn on artifacts, so they can't move. If that's your organization, download your projects before the standalone version closes. See **[Can I download all my projects?](#h_a676b76d76)**

---

## Frequently asked questions

### What happens to my originals after the standalone version closes?

Your originals stay in the standalone version, and moved ones are read-only. After it closes on December 14, 2026, the rest become read-only too, with one exception. The owner of a project that hasn't moved can still change its files, so they can fix it and move it to Claude. Originals are deleted some time later, per our **[data retention practices](https://privacy.claude.com/en/articles/10023548-how-long-do-you-store-my-data)**.

### What if the owner of a design system or project has left my organization?

When it moves to Claude, your organization's Primary Owner becomes its owner.

### Can I download all my projects?

A download of all the projects you own is rolling out together with **Move to Claude**. Once you have it, you'll find it on the home page of the standalone version. It includes your files, not your chats or comments. It isn't available to organizations with the HIPAA-ready configuration. If you don't have it, you can download your projects one at a time:

1. Open the project in the standalone version.

2. Click "Share," then choose "Project HTML." For a slide deck, it's under "More formats and apps."

3. Keep "Project archive" selected and click "Export."

You get a .zip file with every file in the project. It's free and doesn't count toward your usage limits.

## Get help

If something didn't come over right, your original is still in the standalone version. Please let us know if your design system can't move and there's no way for you to fix it. Learn more about **[how to get support](https://support.claude.com/en/articles/9015913-how-to-get-support)**.