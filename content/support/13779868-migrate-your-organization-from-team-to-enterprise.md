# Migrate your organization from Team to Enterprise

When upgrading from a Team plan to an Enterprise plan, we recommend you keep the same Team organization and follow the upgrade path to change it to Enterprise. This will allow you to preserve your data (memberships/roles, conversations, and projects) and some of the settings from your Team plan organization. If you create a brand new Enterprise organization, then you'll need to set up everything from scratch.

There are two ways to upgrade: upgrade using the self-serve flow, or follow the sales-assisted flow if you’re working with an Anthropic account executive on an invoiced or contracted agreement. The steps and timing differ, so use the section that matches your situation.

## What's retained (same organization upgrade)

- All chat history and conversations

- Projects and shared content

- User memberships and roles

## Before you migrate

If you previously set a spend limit on your Team plan, consider increasing it before your go-live date so users aren’t locked out. Once the org-level spend limit is reached, all users lose access immediately until the spend limit is raised or the new month begins.

## Migrate from Team to self-serve Enterprise

You can migrate from a Team plan to a self-serve Enterprise plan by following these steps:

1. Navigate to **[claude.ai/upgrade](https://claude.ai/upgrade)** and click "Get Enterprise plan."

2. When prompted, choose "Upgrade an existing organization" and select your Team plan organization.

3. Add the number of seats needed for all your team members (Enterprise organizations have a 20 seat minimum).

4. Set a per-user spend limit and a starting usage balance for the whole team.

5. Your payment information will be saved from previous Team plan payments, but you can click the pencil icon to change it if needed.

  1. When you migrate from a Team to a self-serve Enterprise plan, we only support credit card payments. After you migrate to a self-serve Enterprise plan, you can choose to use a credit card, debit card, or bank transfer. For more information, see **[Self-serve vs. sales-assisted Enterprise](https://support.claude.com/en/articles/9797531-what-is-the-enterprise-plan#h_3058c781c5)**.

6. Review your order summary and click "Confirm upgrade."

**Important:** Migrating an organization from Team to Enterprise via this pathway is not reversible. Please ensure that an Enterprise plan is the right fit for your organization before initiating this change.

## Migrate from Team to sales-assisted Enterprise

You can migrate from a Team plan to a sales-assisted Enterprise plan through the Anthropic **[sales team](https://claude.com/contact-sales?utm_source=support&utm_medium=article&utm_content=enterprise-plan_contact-sales_intro)**. If your organization is migrating to a sales-assisted Enterprise plan, review the following before your go-live date:

- **Plan your activation timing:** Work with your account executive to agree on a go-live time before your contract is countersigned. Once your agreement is countersigned, your organization is provisioned on your contracted start date. Activation may not complete until later that day, so plan your internal rollout for the next business morning to avoid disruption mid-workday.

- **Expect a brief disruption at cutover:** Your users won’t be able to access Claude while provisioning is in progress. After the migration is complete, all users, including admins and standard users, should log out and log back in to refresh their session and clear any cached legacy settings.

## After you migrate

After your self-serve or sales-assisted migration is complete, we recommend reviewing the following settings.

### Capabilities

Some features that are turned on by default on Team plans may be turned off by default on Enterprise plans, so it's worth checking that your configuration matches your preferences.

Your underlying data is preserved even when a capability is turned off. For example, if your Team plan had skills enabled and members had created custom skills, those skills are not deleted during the migration—they're retained in your organization. When an admin re-enables skills on the Enterprise plan, any previously created custom skills will be available again. The same applies to other default-off capabilities: turning the setting back on restores access to existing content rather than starting from scratch.

The following capabilities are default-off for Enterprise plans:

- Skills and by dependency, Skill creation and Skill sharing (both public and within the organization)

- Code execution and file creation

- Interactive content in artifacts

- Claude Design

- Claude in Chrome

### Per-user spend limits

Go to **[Organization settings > Usage](https://claude.ai/admin-settings/usage)** and review per-user spend limits for all members. Clear or adjust any that are no longer appropriate for your Enterprise plan configuration.

### Seat assignments

During migration, some users may appear as **No seat assigned** rather than being automatically mapped to seat tiers. Admins should verify all users have correct seat assignments after the cutover. Pay attention to your highest-usage members, and note that users without a seat won't have access until an admin corrects their seat assignment.

For detailed guidance, refer to **[Purchase and manage seats on Enterprise plans](https://support.claude.com/en/articles/13393991)**.

### Role-based access controls

After migrating your organization from a Team plan to an Enterprise plan, an Owner or Primary Owner can follow the instructions to configure custom roles, groups, and group spend limits: **[Set up role-based permissions on Enterprise plans](https://support.claude.com/en/articles/13930458-set-up-role-based-permissions-on-enterprise-plans)**.

Read more about groups, group spend limits, and custom roles:

- **[Manage groups and group spend limits on Enterprise plans](https://support.claude.com/en/articles/13799932-manage-groups-and-group-spend-limits-on-enterprise-plans)**

- **[Manage custom roles on Enterprise plans](https://support.claude.com/en/articles/13930452-manage-custom-roles-on-enterprise-plans)**

---

## Additional information

### SSO and identity setup timeline

- **Domain verification (DNS):** Allow 24–48 hours for DNS changes to propagate globally, though many changes take effect within 10 minutes.

- **SCIM provisioning sync:** Microsoft Entra ID pushes changes approximately every 40 minutes. Okta syncs more frequently.

For detailed setup instructions, refer to **[Set up single sign-on (SSO)](https://support.claude.com/en/articles/13132885)** and **[Set up JIT or SCIM provisioning](https://support.claude.com/en/articles/13133195).**

**Note:** Once you turn on SSO, existing users will be forced to log out and log back in.

### Billing and usage configuration

For usage-based Enterprise plans, usage is billed based on actual consumption. For more detailed information, refer to **[How am I billed for my Enterprise plan?](https://support.claude.com/en/articles/11526368-how-am-i-billed-for-my-enterprise-plan)**

If you had purchased usage credits for your Team plan, any unused balance will roll over and become available on your new usage-based Enterprise plan.

### Provisioning process

On the start date, you'll be provisioned and able to use the new features by the end of the day. After initial setup, Owners and Primary Owners can self-serve additional seats by navigating to **[Organization settings > Organization and access](https://claude.ai/admin-settings/organization)** and clicking "Manage" under **Total seats**.

---

## Helpful resources

- **[Set up single sign-on (SSO)](https://support.claude.com/en/articles/13132885-set-up-single-sign-on-sso)**

- **[Set up JIT or SCIM provisioning](https://support.claude.com/en/articles/13133195-set-up-jit-or-scim-provisioning)**

- **[Purchase and manage seats on Enterprise plans](https://support.claude.com/en/articles/13393991-purchase-and-manage-seats-on-enterprise-plans)**

- **[Manage members on Team and Enterprise plans](https://support.claude.com/en/articles/13133750-manage-members-on-team-and-enterprise-plans)**

- **[Enterprise billing information](https://support.claude.com/en/articles/11526368-how-am-i-billed-for-my-enterprise-plan)**

- **[Use Claude Code with your Team or Enterprise plan](https://support.claude.com/en/articles/11845131-use-claude-code-with-your-team-or-enterprise-plan)**