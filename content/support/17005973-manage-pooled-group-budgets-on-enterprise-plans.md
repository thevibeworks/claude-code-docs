# Manage pooled group budgets on Enterprise plans

A pooled group budget gives a group one shared monthly amount that all its members draw from, on top of each user's own monthly spend limit. This article explains how pooled budgets work and how to set, prioritize, and monitor them.

Pooled group budgets are in beta for Enterprise plan organizations. Primary Owners, Owners, Admins, and custom roles with the **Billing** permission set to "Can manage" can set pooled budgets in **[Organization settings > Usage](https://claude.ai/admin-settings/usage)**. To share feedback on the beta, contact your Anthropic account team.

## How pooled budgets work

A group spend limit applies to each group member separately, so every member gets the same monthly limit. A pooled budget adds one shared amount for the whole group.

Every request counts against both the user's own monthly spend limit and the group's pooled budget, and the user stops at whichever runs out first. Usage can go slightly over a limit before it pauses. When the pooled budget is used up, usage pauses for every member of the group until you raise the budget or it resets for the new month. After you raise it, group members can send messages again right away.

**Note:** A pooled budget isn't an equal share for each person. If you set the member monthly limit to the pooled budget divided by the number of group members, you're back to one-person limits and lose the benefit of a shared budget. Set the member monthly limit as a guard rail against unusually high use by one person.

## Before you start

Check the following before you set a pooled budget:

- The group exists in **[Organization settings > Groups](https://claude.ai/admin-settings/groups)**. Learn more about **[managing groups and group spend limits on Enterprise plans](https://support.claude.com/en/articles/13799932)**.

- The group has a monthly spend limit. A pooled budget sits on top of this limit.

- You've picked a group to start with. A single team with a clear owner is a good first choice.

## Choose starting amounts

Base your first amounts on last month's actual spend, not an estimate. You need two numbers for the group. Editing limits for a group suggests these automatically, alternatively you can verify these numbers in **Analytics**:

- **Last month's spend for the group:** In **Analytics**, filter the members table to the group and add up the spend.

- **The group's top spender:** The first row when you sort that table by spend.

A good starting point is a pooled budget of about three times last month's group spend, and a member monthly limit of about three times the top spender's spend.

For example, if a group spent $1450 last month and its top spender used $310, set the pooled budget to $2900 and the member monthly limit to about $950. With these amounts, requests for more should be rare and the pooled budget should last the month.

## Set a pooled budget

Set the pooled budget and the member monthly limit together from the group's row in the spend limits table.

1. Navigate to **[Organization settings > Usage](https://claude.ai/admin-settings/usage)**.

2. Scroll to **Spend limits** and select the "By group/tier" tab.

3. Find the group, click the menu button to the right, and select "Edit limits."

4. Under **Pooled monthly budget**, select "Set amount." A suggested amount based on the group's recent usage is filled in, and you can change it.

5. Under **Member monthly limit**, click "Use" to apply the suggested limit, or enter your own.

6. Click "Save."

If the member monthly limit is too low for the pooled budget, you'll see a warning with an option to raise it.

## Change, freeze, or turn off a pooled budget

- **Change the amount:** Select "Edit limits" in the group's row menu and enter a new amount.

- **Freeze the group:** Set the pooled budget to $0. Every group member stops until you raise it.

- **Pause the pooled budget**: select Paused. The amount is kept but not enforced until you select Set amount again. To remove the pool, select **No pooled budget**

- **Remove the group's spend limit:** This also removes the group's pooled budget.

## Set the budget priority for users in several groups

If a user belongs to more than one group with a pooled budget, the largest pooled budget pays first by default. To choose the order yourself:

1. Navigate to **[Organization settings > Usage](https://claude.ai/admin-settings/usage)**.

2. In the **Pooled budget priority** card, select "Custom order."

3. Use the arrows to put the groups in order, with the most specific team first.

4. Click "Save order."

With a custom order, the first available pooled budget with remaining usage in your list pays first.

**Note:** Budget priority only decides which pooled budget pays. To choose which group's member monthly limit applies to a user in more than one group, use the **Member limit from groups** setting under **Spending defaults**.

## Monitor pooled budgets

Check pooled budget usage at any time in the **Pooled budget** column on the "By group/tier" tab in **[Organization settings > Usage](https://claude.ai/admin-settings/usage)**. The column shows each group's pooled budget and how much of it has been used this month. The bar turns amber at 75% and red at 90%., and a dash means the group has no pooled budget.

When a pooled budget reaches 50%, 75%, 95%, and 100% of its monthly amount, every admin with billing permissions gets an email, and a notice for the group appears on the admin home page. Click "View group" in the notice to go to the group's row, then dismiss the notice once you've acted on it.

To tell whether your amounts are right, also check the number of requests under **Review requests**. If a pooled budget is 75% used before the 20th of the month, consider raising it by 50%. If users keep requesting more, raise the member monthly limit.

## What users see

Nothing changes for users until they reach their own monthly spend limit or the group's pooled budget runs out. At that point, a message appears in the message box with a "Request more" button. If the pooled budget is used up, the message says their team's shared budget has run out.

Requests from users appear under **Review requests**. Users never see the group's name or the pooled budget amount.

## Beta limitations

- The **Billing** permission applies across your whole organization, so anyone who can edit one group's pooled budget can edit every group's pooled budget.

- Pooled budgets can only be managed in **Organization settings**. They aren't available through the Admin API.