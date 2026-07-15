# Purchase and manage seats on Enterprise plans

This article covers how to add seats, manage your seat allocation, and handle member access on Enterprise plans. For pricing and billing details, see **[How am I billed for my Enterprise plan?](https://support.claude.com/en/articles/11526368-usage-based-enterprise-plans)**

**Permissions note:** Only Owners and Primary Owners can purchase seats and access **[Organization settings > Organization and access](https://claude.ai/admin-settings/organization)**. Admins and above can reassign seat types for members in **[Organization settings > Members](https://claude.ai/admin-settings/members)**. To check your role, click your name or initials in the lower left corner—your role is listed next to your organization's plan type.

For information on adding and removing members from your organization, see **[Manage members on Team and Enterprise plans](https://support.claude.com/en/articles/13133750-managing-members-on-team-and-enterprise-plans)**.

**Important:** The main sections of this article describe the current Enterprise seat model, which applies to all new Enterprise plans.

- If your organization was provisioned before the transition to the single Enterprise seat and you see **Chat** and **Chat + Claude Code** seat types in **[Organization settings > Members](https://claude.ai/admin-settings/members)**, refer to **[Information for Chat and Chat + Claude Code plans](#h_2673e097fb)**.

  - **[HIPAA-ready Enterprise organizations](https://support.claude.com/en/articles/13296973-hipaa-ready-enterprise-plans)** are an exception: they are provisioned with separate Chat and Chat + Claude Code seat types and are not eligible for the single Enterprise seat billing model.

- If you see **Standard** and **Premium** seat types, refer to **[Information for seat-based Enterprise plans](#h_6a78e30e26)**.

- Chat-only seats and Standard/Premium seats are no longer available for new contracts—both legacy plan types are transitioning to the single Enterprise seat at their next renewal.

---

## Your seat type

Usage-based Enterprise plans use a single seat type: the **Enterprise seat**, priced per user per month (billed annually). This seat includes access to Claude on web, desktop, and mobile, as well as Claude Code.

Enterprise plans require a minimum of 20 seats.

---

## Purchase new seats

You can add seats to your Enterprise plan at any time during your annual term. New seats are prorated for the remainder of your billing cycle and charged immediately.

1. Log in with your Owner or Primary Owner account.

2. Go to **[Organization settings > Organization and access](https://claude.ai/admin-settings/organization)**.

3. Click "Manage" under **Total seats**.

4. Click "Add or change seats."

5. Enter the number of seats you'd like to add.

6. Review your changes and the prorated charge before confirming.

7. Click "Confirm & purchase" to finalize.

**Note:** You can also purchase a seat while adding a new member. If you don't have an available seat when inviting someone, you'll be prompted to purchase one.

For details on how seat additions are billed, see **[How am I billed for my Enterprise plan?](https://support.claude.com/en/articles/11526368-how-am-i-billed-for-my-enterprise-plan)**

---

## Remove seats

**Self-serve Enterprise plans:** Seats cannot be removed during your annual term. You can add seats at any time, but reductions to your seat count only take effect at renewal. If you need to make an exception, contact **[our Sales team](https://claude.com/contact-sales)** to discuss converting to a sales-assisted plan.

**Sales-assisted Enterprise plans:** Contact your account manager to discuss changes to your seat allocation.

Removing a member from your organization is different from reducing your seat count. When you remove a member, their seat becomes available to assign to someone else, so your total seat allocation and bill don't change. To reduce your bill, you'll need to reduce your total seat allocation. See **[Manage members on Team and Enterprise plans](https://support.claude.com/en/articles/13133750-managing-members-on-team-and-enterprise-plans)** for instructions on removing members.

---

## Temporarily remove a member's access

The **No seat assigned** option lets you temporarily remove a member's access to Claude without removing them from your organization. This is useful for contractors or team members who need intermittent access.

To unassign a member:

1. Go to **[Organization settings > Members](https://claude.ai/admin-settings/members)**.

2. Find the member you want to unassign.

3. Click the dropdown under **Tier**.

4. Select "No seat assigned."

To restore their access, repeat the process and select “Enterprise seat.”

**Note:** Members with no seat assigned remain part of your organization but can't use Claude until you reassign them a seat.

---

## Seat assignment with JIT or SCIM provisioning

**[Users provisioned via JIT or SCIM](https://support.claude.com/en/articles/13133195-setting-up-jit-or-scim-provisioning-to-manage-user-assignments-on-team-or-enterprise-plans)** are automatically assigned an Enterprise seat when they're added, provided one is available in your allocation. If no seat is available, provisioning will not complete until an owner purchases an additional seat.

Admins and above can manually adjust a member's status (e.g., remove their seat assignment) afterward in **[Organization settings > Members](https://claude.ai/admin-settings/members)**.

---

## Cancel your Enterprise plan

**Self-serve Enterprise plans:** An Owner or Primary Owner can cancel your plan from **[Organization settings > Billing](https://claude.ai/admin-settings/billing)**. Cancellation takes effect at the end of your current annual billing cycle—your organization will continue to have access until then.

**Sales-assisted Enterprise plans:** Reach out to your Anthropic Contact or **[our Sales team](https://claude.com/contact-sales)** to discuss cancellation.

---

## Information for Chat and Chat + Claude Code plans

**Important:** Chat and Chat + Claude Code are legacy seat types that are no longer available for new Enterprise contracts. This section only applies to organizations that were provisioned with these seat types before the transition to the single Enterprise seat. If you recently signed a new Enterprise contract, the main sections of this article apply to you—your plan uses the single Enterprise seat, which includes Claude Code access for all members.

Some existing usage-based Enterprise organizations currently have two seat types: **Chat** and **Chat + Claude Code**. If you see these seat types in **[Organization settings > Members](https://claude.ai/admin-settings/members)**, this section applies to you. Your plan will transition to the single Enterprise seat model at your next contract renewal—see below for more information.

### Seat types

| **Seat type**      | **What's included**                         |
| ------------------ | ------------------------------------------- |
| Chat               | Claude on web, desktop, and mobile apps     |
| Chat + Claude Code | Everything in Chat, plus Claude Code access |

You can mix and match seat types based on your team's needs. Assign Chat + Claude Code seats to team members who need coding workflows, while keeping others on Chat seats.

### Reassign users between seat types

You can move users between Chat and Chat + Claude Code seats within your existing allocation.

1. Go to **[Organization settings > Members](https://claude.ai/admin-settings/members)**.

2. Find the member you want to reassign.

3. Click the dropdown under **Tier**.

4. Select "Chat" or "Chat + Claude Code."

Members moved from Chat + Claude Code to Chat will lose Claude Code access, and vice versa.

The **Tier** dropdown only shows seat types your plan already owns. If your plan includes Chat + Claude Code seats but they're all assigned, you'll be prompted to purchase one. If your plan has no seats of that type, see **[Purchase new seats](#h_91344d9191)** above to add one first.

### Swap users between seat types

If all your Chat + Claude Code seats are assigned and you need to move one user to that type while moving another off it, use **No seat assigned** to free up a seat first.

**Example:** You have ten Chat + Claude Code seats, all assigned. You want to move User A (currently on Chat + Claude Code) to Chat, and move User B (currently on Chat) to Chat + Claude Code — without purchasing an additional seat.

1. Go to **[Organization settings > Members](https://claude.ai/admin-settings/members)**.

2. Find User A and change their seat type to "No seat assigned." This frees up one Chat + Claude Code seat.

3. Find User B and change their seat type to "Chat + Claude Code." They now occupy the freed seat.

4. Find User A and change their seat type to "Chat."

### Seat assignment with JIT or SCIM provisioning

Users provisioned via JIT or SCIM are automatically assigned to the highest-available seat type (Chat + Claude Code, if available) when they're added. Admins and above can manually reassign seat types afterward in **[Organization settings > Members](https://claude.ai/admin-settings/members)**.

You can also use Advanced Group Mappings with JIT or SCIM to provision users directly to a specific seat type.

### Transition to the single Enterprise seat

**Note: [HIPAA-ready organizations](https://support.claude.com/en/articles/13296973-hipaa-ready-enterprise-plans)** are provisioned with separate Chat and Chat + Claude Code seat types and are not eligible for the unified seat type.

At your next renewal, you will switch to the single Enterprise seat model upon signing a new contract. This seat includes Claude Code, Cowork, Chat and more.

Reach out to your Anthropic Contact or **[our Sales team](https://claude.com/contact-sales)** with questions about your upcoming renewal.

---

## Information for seat-based Enterprise plans

**Important:** Standard and Premium are legacy seat types that are no longer available for new Enterprise contracts. This section only applies to organizations that were provisioned with these seat types before the transition to usage-based billing. If you recently signed a new Enterprise contract, the main sections of this article apply to you.

Some Enterprise organizations are on older seat-based plans with a different billing structure than the usage-based model described above. If you see **Standard** and **Premium** seats in **[Organization settings > Members](https://claude.ai/admin-settings/members)**, this section applies to you.

### Seat types

| **Seat type** | **What's included**                              |
| ------------- | ------------------------------------------------ |
| Standard      | Core Enterprise features and usage limits        |
| Premium       | Everything in Standard, plus higher usage limits |

### Reassign users between seat types

You can move users between Standard and Premium seats within your existing allocation.

1. Go to **[Organization settings > Members](https://claude.ai/admin-settings/members)**.

2. Find the member you want to reassign.

3. Click the dropdown under **Tier**.

4. Select "Standard" or "Premium."

Members moved from Premium to Standard will have lower usage limits, and vice versa.

The **Tier** dropdown only shows seat types your plan already owns. If your plan includes Premium seats but they're all assigned, reassigning another user to Premium will prompt you to purchase an additional seat. If your plan has no seats of that type, see **[Purchase new seats](#h_91344d9191)** above to add one first.

### Swap users between seat types

If all your Premium seats are assigned and you need to move one user to Premium while moving another to Standard, use **No seat assigned** to free up a seat first.

**Example:** You have ten Premium seats, all assigned. You want to move User A (currently on Premium) to Standard, and move User B (currently on Standard) to Premium—without purchasing an additional seat.

1. Go to **[Organization settings > Members](https://claude.ai/admin-settings/members)**.

2. Find User A and change their seat type to "No seat assigned." This frees up one Premium seat.

3. Find User B and change their seat type to "Premium." They now occupy the freed seat.

4. Find User A and change their seat type to "Standard."

### Billing and usage credits

Seat-based Enterprise plans charge a flat monthly fee per seat that includes usage limits. Owners can enable usage credits to allow team members to continue working after reaching their seat's usage limits. For details, see **[Manage usage credits for Team and seat-based Enterprise plans](https://support.claude.com/en/articles/12005970-)**.

For specific information about seat-based Enterprise pricing, reach out to your Anthropic Contact or **[our Sales team](https://claude.com/contact-sales)**.

### Transition to the single Enterprise seat

At your next contract renewal, your plan will transition to the usage-based single Enterprise seat model described in the main sections of this article. If you'd like to migrate before your renewal, reach out to your Anthropic Contact or **[our Sales team](https://claude.com/contact-sales)**.