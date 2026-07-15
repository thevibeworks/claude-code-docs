# Set up JIT or SCIM provisioning

This guide covers how to configure user provisioning and role assignment for your Claude or Claude Console organization.

JIT provisioning is available for Team plans, Enterprise plans, and Console organizations. SCIM provisioning is available for Enterprise and Console organizations only.

**Before you begin:** This guide assumes you have already completed the steps in **[Set up single sign-on (SSO)](https://support.claude.com/en/articles/13132885-setting-up-single-sign-on-sso)**, including domain verification and SSO configuration with your Identity Provider (IdP), and you have an Admin (Console) or Owner (Claude) role.

---

## Step 1: Choose your provisioning mode

Once SSO is configured, you need to decide how users will be provisioned to your organization. This is controlled via the **User provisioning** section in **[Organization settings > Organization and access](https://claude.ai/admin-settings/organization)**.

### Provisioning options

**Invite only** is the default. Users are added and removed directly in Claude or Console settings.

**Just-in-time (JIT):** Users assigned to your Anthropic IdP app are automatically provisioned when they first log in. This option is available to all plans.

**SCIM directory sync:** Users are automatically provisioned and deprovisioned based on assignments in your IdP, without requiring them to log in first. SCIM is available for Enterprise plans and Console organizations with their own parent organization or joined to an Enterprise parent organization. SCIM is not available for Team plans or Console organizations joined to a Team plan's parent organization.

### Provisioning behavior overview

Use this table to help decide which provisioning mode is right for your organization:

| **Mode**              | **Provisioning**                                                                                                                                                | **Role and seat type changes**                                                | **Removal**                                                                                                                                            |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Invite only           | Users are manually added                                                                                                                                        | Roles and seat types are manually changed                                     | Users are manually removed                                                                                                                             |
| Just-in-time (JIT)    | Users assigned to your IdP app are provisioned at login with the User role                                                                                      | Roles and seat types are manually changed                                     | Manual removal required: users removed from your IdP app can no longer log in, but remain in the user list until they attempt to log in or are removed |
| JIT + group mappings  | Users in at least one mapped group are provisioned at login with the highest-permissioned role from their group memberships                                     | Roles and seat types update on next login based on group membership           | Users without group access can't log in but remain in the list until login attempt or manual removal                                                   |
| SCIM directory sync   | Users assigned to your IdP app are automatically provisioned to all organizations joined to your parent org.                                                    | Roles and seat types are manually changed                                     | Users removed from your IdP app are automatically removed                                                                                              |
| SCIM + group mappings | Users in at least one mapped group are automatically provisioned, with appropriate role, to just the org(s) joined to the parent org where that group is added. | Role and seat types changes automatically propagate based on group membership | Automatic removal when group access is revoked                                                                                                         |

Both JIT and SCIM can be combined with **Enable group mappings** to control role or seat tier assignment based on IdP group membership. If you select either of these options for your provisioning mode, **Enable group mappings** will appear within the **User provisioning** section:

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2312706099/35d5d3ec149880a96bb7acec59f6/a4cfce55-86bf-40b0-b455-c8f412d48e9e?expires=1784143800&amp;signature=3ad8ddaca4293bd4ff61b1c6de92a969f2441a0e416373d899507acaf6a769e0&amp;req=diMmFM5%2Bm4FWUPMW1HO4zXBDQ69VCVl%2BxFMG%2BIEvQSc1lr6KYvQjqeyxHE4L%0A4F%2Fm7XU7RaE%2BfZg1%2BIY%3D%0A)

### Available roles and seat tiers

| **Product**                                       | **Roles**                                                            | **Seat types**           |
| ------------------------------------------------- | -------------------------------------------------------------------- | ------------------------ |
| Team plan                                         | Owner, Admin, User                                                   | Premium, Standard        |
| Seat-based Enterprise plan                        | Owner, Admin, User, Custom                                           | Premium, Standard        |
| Usage-based Enterprise plan (with two seat types) | Owner, Admin, User, Custom                                           | Chat, Chat + Claude Code |
| Usage-based Enterprise plan (single seat type)    | Owner, Admin, User, Custom                                           | Enterprise               |
| Console                                           | Admin, Developer, Limited Developer, Billing, Claude Code User, User | —                        |

For information on purchasing seats or adjusting your plan's seat allocation, see our guides for **[Team plans](https://support.claude.com/en/articles/12004354-purchasing-and-managing-seats)** and **[Enterprise plans](https://support.claude.com/en/articles/13393991-purchasing-and-managing-seats-on-enterprise-plans)**.

---

## Step 2: Set up SCIM directory sync (if using SCIM)

**Note:** Skip this step if you're using Invite only or JIT provisioning.

If you chose SCIM as your provisioning mode, you need to establish the connection between your Identity Provider and Anthropic before enabling it.

1. Navigate to your **Organization and access** settings in Claude (**[claude.ai/admin-settings/organization](http://claude.ai/admin-settings/organization)**) or your **Identity and access** settings in Console (**[platform.claude.com/settings/identity](http://platform.claude.com/settings/identity)**)

2. In the **User provisioning** section, click “Setup SCIM” (or “Manage SCIM”)next to **SCIM directory sync**.

3. Follow the WorkOS setup guide to configure SCIM in your Identity Provider. You'll need to copy values from WorkOS into your IdP's Anthropic application.

**‼️ When you reach the IdP Group step, pause to review Steps 3 and 4 of this guide, alongside the other guides.**

For IdP-specific JIT / SCIM setup instructions, see:

- **[Okta SAML](https://workos.com/docs/integrations/okta-saml)** / **[OKTA SCIM](https://workos.com/docs/integrations/okta-scim)**

- **[Entra ID SAML](https://workos.com/docs/integrations/entra-id-saml)** / **[Entra ID SCIM](https://workos.com/docs/integrations/entra-id-scim)**

- **[Google SAML](https://workos.com/docs/integrations/google-saml)** / **[Directory Sync](https://workos.com/docs/integrations/google-directory-sync)**

- **[OneLogin SAML](https://workos.com/docs/integrations/onelogin-saml)** / **[OneLogin SCIM](https://workos.com/docs/integrations/onelogin-scim)**

- **[JumpCloud SAML](https://workos.com/docs/integrations/jumpcloud-saml)** / **[JumpCloud SCIM](https://workos.com/docs/integrations/jumpcloud-scim)**

- See additional IdPs **[here](https://workos.com/docs/integrations)**

Once your IdP is connected, continue to Step 3.

---

## Step 3: Configure provisioning mode and enable group mappings

1. Find the **User provisioning** section of your settings.

2. Select your chosen option:

  1. **Invite only**: New members can only join if manually invited by an existing member. SSO access alone won't add them to your org.

  2. **Just-in-time (JIT)**: Allow people with SSO access to join when they first log in. Each new member uses one of your available seats.

  3. **SCIM directory sync**: Add or remove members automatically as your directory changes. Your org always stays current.

3. If you selected “Just-in-time (JIT)” or “SCIM directory sync,” do NOT click “Save changes” immediately. You must first ensure all users are assigned to your Anthropic application in your IdP.

4. Once you’ve confirmed all users are assigned in your IdP you can either:

  1. Click “Save changes” to complete the set up and trigger the initial provisioning, or

  2. Toggle on **Enable group mappings** and move to Step 4.

**Important**: Saving before users are properly assigned will result in those users being deprovisioned from the organization. Where it's available, the admin console shows a preview of what the sync will change, including how many members will be removed, before it applies. Review it before you confirm, and cancel if the removal count is higher than you expect. Learn more about **[how SCIM sync works](https://support.claude.com/en/articles/14499648-how-scim-sync-works-for-enterprise-organizations)**.

---

## Step 4: Configure groups in your Identity Provider and map groups to roles and seat types

1. Create groups in your IdP for each role you want to assign. Unless you're on the single-seat Enterprise plan, create groups for each seat type as well.

  1. While there are no longer naming requirements for these groups, we recommend including something in the group name (e.g., `anthropic-claude-` or `anthropic-console-`) to make them easier to identify.

2. Add users to the groups you created, ensuring at least one user (including yourself) is in a group that will be mapped to an Admin (Console) or Owner (Claude) role.

3. Return to your **Organization and access** or **Identity and access** settings in Claude or Console, and find **User provisioning**.

4. Toggle **Enable group mappings** on (if it’s not already):

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2312714635/b57870b51e6511c8293637bceee2/da1ceabc-b6bc-451b-9cda-24ff6aa90d02?expires=1784143800&amp;signature=ea1543a7d1a663071f0affcda830c642d5e8235dc969a71f675536035efdfb89&amp;req=diMmFM5%2FmYdcXPMW1HO4zeBEbsHZk%2FlAyb72rapuHpNEATnSWeN9%2BjFygvLH%0AR5Lt%0A)

5. In the **Enable group mappings** section, click “Add” next to each role and select the corresponding group from your IdP in the dropdown.

  1. When using group mappings, you *must* assign all users to a role-based group in order to ensure they’re provisioned an account. Assigning users to seat-tier based groups is optional.

  2. You can map an IdP group to the “Custom” role. Members assigned this role have no default permissions—their access is determined entirely by the custom roles assigned to their groups in Claude.

6. **For all plans except single-seat Enterprise:** In the **Assign seat tiers to IdP groups** section (optional), click "Add" next to each seat type and select the corresponding group from your IdP. If a user isn't assigned to a seat type group, they will be assigned to the highest available type by default.

  1. **For single-seat Enterprise:** Seat type mapping does not apply. All provisioned users are automatically assigned an Enterprise seat, provided one is available in your organization.

7. Verify all necessary groups are mapped to the appropriate roles and seat types.

8. Click “Save changes.”

  1. **Note:** Microsoft Entra only pushes SCIM changes every 40 minutes, so there may be a delay before changes appear. You can check which users are synced from your IdP by clicking "Manage SCIM" and viewing the Directory. Those users in the Directory will be provisioned to Claude / Console.

**Important:** All users who need access must be assigned to the appropriate groups before you save your group mappings configuration. These users should already be assigned to your Anthropic application in your IdP from when you enabled SSO.

### How the Primary Owner role works with SCIM

- Your organization's Primary Owner is exempt from SCIM reconciliation. If the Primary Owner account is not present in the IdP directory, or is not a member of any group mapped to a role, it will be skipped when SCIM syncs. The Primary Owner's membership and role are preserved.

- This exemption applies only to the single Primary Owner role. Owner and Admin roles are **not** exempt and **must** be in a group mapped to a role, or they will be removed when SCIM group mappings are enabled.

- The Primary Owner role cannot be assigned via SCIM group mappings. It can only be transferred manually from **[Organization settings > Members](https://claude.ai/admin-settings/members)**. Set your intended Primary Owner before enabling SCIM.

- The Primary Owner is not exempt from SSO sign-in enforcement. SSO enforcement is applied by email domain; if the Primary Owner's email is on an enforced domain, they must authenticate through SSO.

---

## Troubleshooting

### Users assigned correctly and showing in the directory but aren’t being added to the Claude as members?

Verify you have enough seats purchased and available to add members to your org.

1. Check the number of available seats shown in **[Organization settings > Organization and access](https://claude.ai/admin-settings/organization)** and purchase additional seats if needed (see our guides for **[Team plans](https://support.claude.com/en/articles/12004354-purchasing-and-managing-seats)** and **[Enterprise plans](https://support.claude.com/en/articles/13393991-purchasing-and-managing-seats-on-enterprise-plans)**).

2. Once you have available seats, go back to the Organization and access page and click “Sync now,” next to **Directory sync (SCIM)**. This will trigger a sync to provision accounts for those users not yet added as members.

### Users aren't being provisioned with the correct role

1. Verify the user is assigned to the correct group in your IdP.

2. Verify the group is mapped to the correct role in your **Organization and access** settings.

3. **For JIT:** The user needs to log out and log back in for role changes to take effect.

4. **For SCIM:** Click "Sync" to prompt an immediate sync, or wait for the automatic sync cycle:

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2312717421/c97fce49ad17d4660880a05fbaaf/59fbfa2a-1072-4662-8ca5-102970d5a795?expires=1784143800&amp;signature=39fef561775472a9bf5176a312d37ef9e8a9b1b94f42e74fca71534a71130b90&amp;req=diMmFM5%2FmoVdWPMW1HO4zZ9La1msHcnK5hujYvMis4dxb0gl0yEf621z34%2Bl%0Ab88v%0A)

### I lost Admin/Owner access after enabling group mappings

This happens when the person configuring group mappings isn't assigned to a group mapped to an Admin or Owner role, causing their permissions to be downgraded to User.

To fix this:

**Option 1: Have another Admin/Owner reinstate your role**

1. Contact another Admin or Owner of your organization.

2. Ask them to navigate to **[Organization settings > Organization](https://claude.ai/admin-settings/organization)** (for Claude) or **[Settings > Members](https://platform.claude.com/settings/members)** (for Console).

3. Have them change your role back to Admin or Owner.

**Option 2: Fix via your Identity Provider**

1. In your IdP, assign yourself to a group with the correct prefix that maps to an Admin or Owner role.

2. **For JIT:** Log out and log back in to regain access.

3. **For SCIM:** Ask another Admin or Owner to click "Sync" in the **Organization and access** settings, or wait for the automatic sync cycle.