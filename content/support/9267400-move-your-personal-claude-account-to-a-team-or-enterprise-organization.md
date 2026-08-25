# Move your personal Claude account to a Team or Enterprise organization

If you're using Claude with a personal account (Free, Pro, or Max) tied to your work email, you may be able to move that account into your organization's Team or Enterprise workspace. There are two paths: you can start a migration yourself (Team and Enterprise) or your admin can claim accounts on your domain (Enterprise only).

**Note:** Enterprise organizations that have turned on HIPAA readiness or customer-managed encryption keys (CMEK) can't receive data from a personal account. If your organization uses either, you won't be offered the option to bring your data with you, and a domain claim won't offer to merge your account. You can export your data first if you want a copy. Learn more about **[HIPAA-ready Enterprise plans](https://support.claude.com/en/articles/13296973)** and **[customer-managed encryption keys](https://support.claude.com/en/articles/15505325)**.

---

## What moves when you migrate

Both paths move the same content for each person.

### What moves

- Chats

- Artifacts within chats

- Projects, project instructions, and files, including projects created through or used with Cowork

- Uploaded files and attachments

- Project sync configurations (which Drive folders and repositories a project syncs)

- Claude's memory from chats and projects, unless your organization has memory turned off

- Claude Code memory and personal settings such as tool settings, notification preferences, and consents, unless your organization account already has its own values set

- Claude Design systems and projects migrated since 14 August 2026

### What doesn't move

- Custom skills.  There's no migration path for skills. Export any you want to keep before you migrate.

- Sign-ins to connected apps and services**.** All authorizations are revoked. You'll reconnect each app from your organization account.

- Custom connectors you added yourself. You'll need to add them again in your organization account, and your organization's policy may not allow them.

- Published artifacts. Publishing isn't available on Team and Enterprise plans.

- Public share links to chats. These stop working permanently.

- Pending share invites

- Cowork sessions in the desktop app. Desktop sessions and the folders you've connected are stored locally, not in the cloud, so they stay on your computer. Copy anything you want to keep after you migrate.

- Cowork cloud sessions (web and mobile). Download any files or outputs you want to keep before you migrate.

- Claude Code cloud sessions (web, scheduled tasks, and mobile)

- Claude Design systems and projects migrated before 14 August 2026

### Before you migrate

1. Export any custom skills you want to keep.

2. Save a copy of anything you've published as an artifact, since published artifacts won't be available afterward.

3. Share any content you've sent out as a public link another way, because those links will break.

4. Make a note of the apps you've connected so you can reconnect them.

---

## Voluntary migration

Voluntary migration is supported on Team and Enterprise plans.

If you have a personal Claude account on the same email address as your organization, you can choose how to handle it when you join a Team or Enterprise organization:

- **Keep both accounts:** Your personal account stays active. You can switch between it and your organization account from your account menu.

- **Use your organization account only:** You'll see two migration options after selecting this.

  - **Bring your data with you:** Your personal data moves into the organization's workspace, as described above in **[What moves when you migrate](#h_4e63ef6e87)**. Your personal account closes, and active Pro or Max subscriptions are canceled and refunded depending on how you purchased the plan.

  - **Delete your data:** Your personal account closes (with a prorated refund if you had a paid subscription), but no content moves into the organization. You start with a clean account. You can choose to download your account data before deleting it.

If your organization has turned on HIPAA readiness or CMEK, **Bring your data with you** isn't offered.

### How do refunds work for migrated accounts?

What happens to your Pro or Max plan after migrating depends on where you bought it:

- **Directly (not through a mobile app):** Your Pro or Max subscription is canceled automatically when your personal account closes, and you receive a prorated refund for unused time.

- **Google Play Store:** Your Pro or Max subscription is canceled automatically when your personal account closes, and you receive a prorated refund for unused time. Refunds for Google Play purchases can take a few days to appear.

- **Apple App Store:** Your Pro or Max subscription isn't canceled. Apple doesn't allow third-party cancellation, so you'll need to cancel it yourself through your Apple ID settings. If you don't, Apple keeps charging you after your personal account closes.

For cancellation instructions, see **[Cancel your Pro or Max subscription](https://support.claude.com/en/articles/8325617)**.

### How to start a migration

Start from your organization account, not your personal account. If you're signed in to your personal account, switch first by clicking your initials or name in the lower left corner and selecting your organization.

On a Team plan, you'll be prompted to choose when you accept an invite to your organization. If you don't pick an option right away, you'll see a reminder banner for about seven days. You can also go to **[Settings > Account > Close your personal account](https://claude.ai/settings/account)** at any time to initiate the migration.

On an Enterprise plan, you won't see a prompt when you join. To start the migration, go to **[Settings > Account > Close your personal account](https://claude.ai/settings/account)**.

### If you own both accounts

Owning the Team organization doesn't change where you start the migration. If you created the organization from your personal account, you may still be signed in to the personal one, and **Close your personal account** won't appear there. Switch to your organization account first, then go to **[Settings > Account](https://claude.ai/settings/account)**.

**Important:** Bringing your work into a Team or Enterprise workspace is one-way. Once content has been moved, it can't be moved back to a personal account.

### Apple App Store subscribers

If you subscribed to the Pro or Max plan through the Apple App Store, **Keep both accounts** is your only option. Apple doesn't allow third-party cancellation of App Store subscriptions, so we can't auto-cancel your iOS plan as part of the migration. If you'd rather move your work into the Team, **[cancel your iOS subscription](https://support.claude.com/en/articles/8325617-cancel-your-pro-or-max-subscription#h_54384c9962)** through your Apple ID settings first, then start the migration from the reminder banner or **[Settings > Account](https://claude.ai/settings/account)**.

---

## Domain claiming

Domain claiming is supported on Claude Enterprise plans only.

Enterprise admins can claim all existing personal accounts on their organization's verified domain and move them into the Enterprise workspace. If your admin initiates a domain claim, you'll receive an email and in-product notification with a deadline (at least 30 days out) to choose between merging your data into a new Enterprise account or starting fresh. If your organization has turned on HIPAA readiness or CMEK, you'll still get the notification and deadline, but merging isn't offered. Export anything you want to keep before the deadline, then start fresh.

For the full walkthrough of your options, deadlines, and what happens to your subscription, see **[Respond to an Enterprise domain claim on your Claude account](https://support.claude.com/en/articles/14625626-respond-to-an-enterprise-domain-claim-on-your-claude-account)**.

---

## Manage personal and organization accounts

You may have both a personal account and an organization account tied to the same email address. You can switch between them by clicking your initials or name in the lower left corner of the screen.

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2312193347/712f763fc290b2488c103849f20c/0c135a6f-3442-4ee1-9ab7-98673f03ef6e?expires=1787640300&amp;signature=35187f37523ff4f00780eaeadb4849578aa75b20428ad2fb3383c5db800ce666&amp;req=diMmFMh3noJbXvMW1HO4zXhPndcwzB9iufhmlOXMdYYgv07xNbm1dnEuck9T%0A27YQw4Zcp2%2BQMVfIH24%3D%0A)

A blue checkmark shows which account you're currently using. Click the other account to switch to it and access its separate conversations and projects.

---

## Discontinue your personal account manually

If you want to close your personal account without moving any of your work into an organization:

1. **[Cancel your individual paid plan](https://support.claude.com/en/articles/8325617-how-do-i-cancel-my-paid-claude-subscription)** if applicable.

2. **[Export your data](https://support.claude.com/en/articles/9450526-how-can-i-export-my-claude-data)** while you still have access.

3. Navigate to **[Settings > Account](https://claude.ai/settings/account)** and click "Delete" to **[delete your account](https://support.claude.com/en/articles/9028421-how-can-i-delete-my-claude-account)**.