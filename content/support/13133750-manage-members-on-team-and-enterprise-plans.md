# Manage members on Team and Enterprise plans

This guide covers how to add, remove, and manage the people on your Team or Enterprise plan.

**Permissions note:** Organization Admins can manage members in **[Organization settings > Members](http://claude.ai/admin-settings/members)**, but only Owners and Primary Owners can access **[Organization](https://claude.ai/admin-settings/organization)[settings > Billing](https://claude.ai/admin-settings/billing)**. For more information, see our article about **[roles and permissions](https://support.claude.com/en/articles/9267276-roles-and-permissions)**.

For information on purchasing seats or adjusting your plan's seat allocation, see our guides for **[Team plans](https://support.claude.com/en/articles/12004354-purchasing-and-managing-seats)** and **[Enterprise plans](https://support.claude.com/en/articles/13393991-purchasing-and-managing-seats-on-enterprise-plans)**.

---

## Add members

### Add members by invitation

**Note:** Pending invitations occupy your available seats immediately; a new member does not need to accept the invite to take up a seat.

Admins and above can add members by following these steps:

1. Navigate to **[Organization settings > Members](http://claude.ai/admin-settings/members)** and click “Add member.”

2. Enter the person's email address (it must use one of your organization's **[allowed email domains](https://support.claude.com/en/articles/13325567-account-management-faqs#h_b54c41c86c)**).

3. Select the appropriate seat type.

4. Set the role and permissions for the member.

  1. **Note:** On Enterprise plans, you can also select “Custom” as a member’s role. Members set to this role have their access controlled through group memberships and custom roles. To see exactly what a custom role member can access, open the “**⋮**” menu on the right side of their row and select "View effective role." For details, see **[Manage custom roles on Enterprise plans](https://support.claude.com/en/articles/13930452-manage-custom-roles-on-enterprise-plans)**.

5. Click “Add members.”

This sends an email invitation to the person. The invitation expires after 21 days, so you'll need to re-invite them if they don't accept within that time period.

**Add multiple members at once:** You can invite multiple members by clicking "Bulk add" and typing or pasting email addresses separated by commas or new lines.

**Note:** The seat type selector only shows seat types your plan already owns. If all seats of the selected type are assigned, you'll be prompted to purchase one. See our guides for **[Team plans](https://support.claude.com/en/articles/12004354)** and **[Enterprise plans](https://support.claude.com/en/articles/13393991)** for more information.

### Add members via organization discovery

Members can also join your organization on their own through organization discovery. When you enable discoverability, colleagues with a matching email domain can find your organization during signup and request to join—no invitation needed. You can configure whether they're added automatically or require your approval. See **[Find and join a Team or Enterprise organization](https://support.claude.com/en/articles/13566435-organization-discovery)** for details.

### Share an invite link

Admins and above can generate a shareable invite link and distribute it to teammates—for example, by posting it in a Slack channel, email thread, or team wiki—without needing to enter individual email addresses.

**Availability:**

- **Team plans:** Invite links are enabled by default for new organizations.

- **Enterprise plans (non-SSO):** Invite links are disabled by default. Admins can enable them in **[Organization settings > Organization and access](https://claude.ai/admin-settings/organization)**.

- **SSO organizations:** Invite links are not available. Member provisioning is managed through your Identity Provider.

To find and copy your invite link, navigate to **[Organization settings > Organization and access](https://claude.ai/admin-settings/organization)**. New members who join via link are assigned to the lowest available seat tier, defaulting to a standard seat if none are available.

Admins can disable the link at any time—this immediately invalidates all existing links. Regenerating the link also invalidates the previous one.

For more details on how the joining flow works, see **[Join an organization via invite link](https://support.claude.com/en/articles/13776697-join-an-organization-via-invite-link)**.

### Automated provisioning with SSO

Organizations with single sign-on (SSO) configured can automate member provisioning. Learn more about **[setting up SSO](https://support.claude.com/en/articles/13132885-setting-up-single-sign-on-sso-for-claude-and-claude-console)**.

- **Just-in-time (JIT) provisioning:** Members assigned to the Anthropic app in your Identity Provider will have accounts created automatically the first time they log in. On plans with multiple seat types, users are assigned to the highest-available seat type upon first login. On single-seat Enterprise plans, users are automatically assigned the Enterprise seat. Admins and above can manually reassign seat types afterward in **[Organization settings > Organization and access](https://claude.ai/admin-settings/organization)**.

- **SCIM provisioning (Enterprise plan only):** With SCIM directory sync enabled, members assigned to the Anthropic app in your Identity Provider are provisioned automatically, up to the number of total seats on your plan. On plans with multiple seat types, seat types are distributed from highest to lowest available. On single-seat Enterprise plans, all users are automatically assigned the Enterprise seat. Primary Owners and Owners can reassign seat types afterward in **[Organization settings > Organization and access](https://claude.ai/admin-settings/organization)**.

**Important:** An Owner or Primary Owner must ensure seats are available before new users can be provisioned. We recommend monitoring your seat usage and adding seats proactively to ensure uninterrupted access for your team. You can **[enable group mappings with JIT or SCIM](https://support.claude.com/en/articles/13133195-setting-up-jit-or-scim-provisioning#h_adee31eeba) to provision users directly to a specific role and seat tier**.

---

## Member-to-member invites

Organization members can invite teammates by email, even if they aren't admins. This makes it easier for your team to grow organically without requiring admin involvement for every new member.

### How it works

Any member can access the invite flow from the account selector in Claude. They enter a teammate's email address and submit the invite. What happens next depends on your organization's new member approval setting:

- **Approve one-by-one (default):** The invite request goes to an admin for review. The invite is only sent to the teammate after an admin approves it.

- **Approve automatically:** The invite is sent right away and the invitee can join immediately.

Invites sent by members follow the same domain restrictions as other join methods — the invitee's email must match one of your organization's allowed domains.

### Availability

- **Team plans:** Member-to-member invites are enabled by default for new organizations.

- **Enterprise plans:** Member-to-member invites are disabled by default. Admins can enable them from Admin settings.

### Admin controls

Admins can enable or disable member-to-member invites from the admin settings. When disabled, only admins can send invitations. Invitees added through member invites are assigned the default member role and placed in the lowest available seat tier.

---

## Remove members

You can remove a member by navigating to **[Organization settings > Members](http://claude.ai/admin-settings/members)**, clicking the menu button to the right of the member, then selecting "Remove from team."

For Enterprise organizations using SCIM provisioning, members are automatically removed from Claude when they are removed from your Identity Provider.

When a member is removed:

- They lose access to the organization immediately.

- The seat they occupied becomes available to assign to another user.

- If you re-add the member later using the same email address, their account history will be maintained.

Removing a member frees up their seat for reassignment, but does not automatically reduce your plan's total seat count. See our guides for **[Team plans](https://support.claude.com/en/articles/12004354-purchasing-and-managing-seats)** and **[Enterprise plans](https://support.claude.com/en/articles/13393991-purchasing-and-managing-seats-on-enterprise-plans)** for information on reducing seats.

**Note:** You cannot remove yourself as a Primary Owner or Owner. Another Primary Owner or Owner must remove you from the team.

---

## Export member data

Admins and above can export a CSV of your organization's current member list from your organization settings.

The export includes member details such as name, email address, role, and seat type. This is useful for auditing membership, reconciling seat usage, or maintaining an external record of your team.

To export:

1. Navigate to **[Organization settings > Members](http://claude.ai/admin-settings/members)**.

2. Click the "Export CSV" button at the top of the **Members** section.

3. A CSV file will download to your device.

---

## Manage invitations

### Resend an expired invitation

You can resend an invite from **[Organization settings > Members](http://claude.ai/admin-settings/members)**. Click the “Pending” tab, find the member, and select to resend the invite.

### Revoke a pending invitation

You can revoke a pending invite from **[Organization settings > Members](http://claude.ai/admin-settings/members)**. Click the “Pending” tab, find the member, and select "Remove from team."

---

## Frequently asked questions

### Can I invite someone who already uses Claude personally with their work email?

Yes. Once they join your team, they'll have both a personal account and a Team or Enterprise plan account. They can toggle between accounts through the menu by clicking their initials or name in the lower left corner.

### How do I add a member that I previously removed?

To add a member that you previously removed, follow the same steps as adding a new member. Their account history will be maintained.

### How do I change the Primary Owner?

The current Primary Owner can transfer ownership by:

1. Navigate to **[Organization settings > Members](http://claude.ai/admin-settings/members)**.

2. Click the Role dropdown next to the new user and select "Primary Owner."

3. Type the new Primary Owner's email address in the modal to confirm and transfer ownership.

**Important:** There can only be one Primary Owner per organization. Following these steps transfers the role to a different user.

### What happens to the initial invitation for a new Enterprise organization?

When Anthropic provides a new Enterprise organization and invites the Primary Owner, the same 21-day expiration period applies to that initial invitation. If your invitation has expired, please reach out to your account manager.