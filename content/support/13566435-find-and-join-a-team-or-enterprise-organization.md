# Find and join a Team or Enterprise organization

Organization discovery allows you to find and join your company's existing Team or Enterprise plan organization when you start the sign-up flow with a work email address. Instead of creating a separate personal account, you can request to join—or be added automatically—depending on your organization's configuration.

Organization discovery must be enabled by an admin before the capability is available. It’s unavailable for organizations that have **[single sign-on (SSO) enabled](https://support.claude.com/en/articles/13132885-setting-up-single-sign-on-sso)**. If your organization uses SSO, your existing provisioning settings remain in effect.

---

## Admin setup

### Enable discoverability

Admins and above can manage organization discovery from **[Organization settings > Organization and access](https://claude.ai/admin-settings/organization)**.

- **New organizations:**

  - **Team plans:** Discoverability is on by default. Admins see the option during plan onboarding with it pre-selected.

  - **Enterprise plans:** Discoverability is off by default. Admins will see the option disabled on the Organization and access page.

- **Existing organizations:** Discoverability is off by default. Admins can turn it on from settings at any time.

To enable discoverability:

1. Log in as an Admin, Owner, Primary Owner.

2. Navigate to **[Organization settings > Organization and access](https://claude.ai/admin-settings/organization)**.

3. Your organization’s domains are listed at the top of the page.

4. Find the domain you want users to search for and click the toggle under **Discoverable**.

5. Find **New member approval** under **User provisioning** and choose either “Approve automatically” or “Require admin approval.”

### Configure allowed domains

Admins can specify which email domains are allowed to discover and join the organization by clicking “+ Add domain” under **Domains** on the organization and access page. The organization owner’s domain will appear on the **Domains** list automatically, but admins can configure additional allowed domains by adding them here, verifying them, and toggling **Discoverable** on. Personal email domains (like Gmail) and .edu domains can't be added to the allowed list.

### Choose an approval mode

Admins select how join requests are handled:

**Approve automatically:** Users are added to the organization’s lowest available seat tier automatically when they ask to join. Billing begins as soon as a user joins—if the organization has no available seats, billing auto-expands and a new seat is purchased immediately.

**Require admin approval:** The admin reviews and approves each join request individually. Users aren't added to the organization until the admin approves. Billing begins when the request is approved—if no seats are available at that point, a new seat is purchased.

This approval mode also applies to invitations sent by existing members of your organization. For additional details, see **[Manage members on Team and Enterprise plans](https://support.claude.com/en/articles/13133750-managing-members-on-team-and-enterprise-plans)**.

---

## How to find and join an organization

When someone signs up for Claude with a work email address that matches a discoverable organization, they'll see the option to join during the signup flow. They can choose to join or continue with a personal account.

- If the organization uses **instant approval**, they're added right away.

- If the organization uses **request + approve**, a request is sent to the admin. The requester can choose to continue with a personal account (as long as "Restrict organization creation" is disabled) until the request is approved or denied.

If multiple organizations share the same email domain and are all discoverable, users will see all of them and can choose which one to join. You can be a member of multiple Team or Enterprise organizations at the same time.

---

## Join when you already have a personal Claude account

If you have a Free, Pro, or Max account on the same email address as the organization you're joining, you can choose what to do with it: keep both accounts or bring your work into the organization. On Team plans, you're prompted when you accept the invite. On Team and Enterprise plans, you can start the migration from **[Settings > Account](https://claude.ai/settings/account)** at any time after joining.

For details on each option, refund handling, and Apple App Store limitations, see **[Move your personal Claude account to a Team or Enterprise organization](https://support.claude.com/en/articles/9267400-move-your-personal-claude-account-to-a-team-or-enterprise-organization)**.

---

## Other ways to join an organization

In addition to organization discovery, there are a few other ways to join a Team or Enterprise organization:

- **Invite link:** Your admin may share an invite link that lets you join directly. See **[Join an organization via invite link](https://support.claude.com/en/articles/13776697-join-an-organization-via-invite-link#h_af9f6b7825)**.

  - **Note:** If the invite link has been disabled or regenerated by your admin, it will no longer work. Ask your admin to share a new link.

- **Email invitation:** An admin or existing member of the organization may send you an email invitation to join.

- **Admin invitation:** An admin can add you directly from admin settings. See **[Manage members on Team and Enterprise plans](https://support.claude.com/en/articles/13133750-managing-members-on-team-and-enterprise-plans)**.

---

## SSO and organization discovery

Organization discovery is not available for organizations with single sign-on enabled. If your organization uses SSO, the feature doesn't apply—your existing provisioning settings (including any just-in-time provisioning) remain unchanged.

If you'd like to enable organization discovery, SSO must be turned off first.