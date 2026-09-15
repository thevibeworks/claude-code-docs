# Let team members run smart reports for specific groups

Smart reports show how your organization uses Claude. By default, only Primary Owners, Owners, Admins, and custom roles with analytics view access can create and view smart reports. With delegated access, you can let team leads or department heads run smart reports without making them admins. They can only report on the groups, departments, or cost centers you choose, and they see only the reports they ran or that others share with them.

Smart reports are available in beta on Claude Enterprise plans and aren’t available for organizations using customer-managed encryption keys (CMEK), HIPAA configurations, or **[Access Transparency](https://platform.claude.com/docs/en/manage-claude/access-transparency)**. Smart reports are also unavailable for Claude Code for Claude Enterprise organizations that use zero data retention.

**Important:** Smart reports help you understand adoption and plan your investment in Claude. They aren't designed and should not be used for evaluating individual performance or making employment decisions.

## Who can manage access for smart reports

To manage access to smart reports, you must be an Owner or Primary Owner, or in a custom role with both the **Analytics** permission and the **Identity & Access** permission. If you don’t have one of these roles, you won’t see the **Manage access** button.

## Before you begin

- Your organization must be on a Claude Enterprise plan with "Smart Reports (beta)" turned on in **Organization settings > Capabilities > Analytics**.

- The people you add must be on the **Custom roles** access level, which is set per member in **Organization settings > Members**.

## Step 1: Open Manage access

Go to **[Analytics > Smart reports (beta)](https://claude.ai/analytics/insights)** and click "Manage access." The **Who can run reports** screen opens.

The line at the top tells you which roles can run reports. Admins and owners can always run reports.

## Step 2: Add a person

Under **Add people**, type a name or email and pick the person.

Some users appear greyed out with the label **Not on Custom roles**. Change their access level in **[Organization settings > Members](https://claude.ai/admin-settings/members)**, then close and reopen **Manage access** and add them.

## Step 3: Choose what they can report on

The person appears under **People with access**, with the columns **Person** and **Can run reports on**. Nothing is saved for them until you choose a scope.

1. If your organization has more than one kind of scope, select **Group**, **Department**, or **Cost center** in the first dropdown menu.

  1. Groups come from **[Organization settings > Groups](https://claude.ai/admin-settings/groups)**.

  2. Departments and cost centers are offered only if your identity provider provisions members through SCIM with those attributes.

2. Select the group, department, or cost center values in the second dropdown menu.

Each change is saved as soon as you make it and will say "Saved."
​

If you click "Close" while someone still has no scope, or their last change couldn't be saved, the screen asks "Close without saving?" and explains that their access isn't saved.

Keep in mind:

- You can select up to 50 groups, departments, or cost centers of each kind per person.

- A delegate can only run a report on what you assign here. They never get a whole-organization option.

**Note:** People you give access to aren’t notified. They can view smart reports by clicking on their name in the lower left corner in Claude, then going to **Analytics > Smart reports (beta)**.

## What happens automatically

The first time you save a delegate, smart reports creates two things in your organization:

- A group named **Smart Reports delegates**

- A custom role named **Smart Reports delegates**, assigned to that group, with the **Smart Reports delegated admin** permission

Every person you add is placed in this group, which is how they get permission to run reports. We recommend that you don’t edit these roles manually.

The following badges can appear on a person's row:

- **Not on Custom roles**: the person's access level changed after you added them. Change it back in **[Organization settings > Members](https://claude.ai/admin-settings/members)**.

- **Needs the permission**: this person doesn’t have access to any roles that grant permission to run smart reports (for example, they were removed from the smart reports delegates group). Click **Add to the Smart Reports delegates role** on their row to add them back. If the automatic role itself lost the permission, restore it in **[Organization settings > Roles](https://claude.ai/admin-settings/roles)** first.

## What a delegate sees and can do

- In **Analytics**, delegates see only **Smart Reports**. Their list is titled **Your reports** and contains only the reports they ran.

- When they click "New report," the **People in scope** menu offers only the groups, departments, or cost centers you assigned. All of them are selected to start, and the delegate can narrow the selection.

- Delegates can share their reports with other members of your organization and download them, the same way admins can.

- The attributed view, which shows user emails and session IDs, only appears when your organization's **Allow attribution to individual users** setting is on.

- Reports run by delegates count toward your organization's monthly smart reports limit and share the same limit on reports running at once.

Delegates cannot:

- Run a report on the whole organization, or on anything outside their assigned scope

- See reports other people ran, unless someone shares the report with them

- Rename, archive, or delete reports

- Open **Manage access** or change who can run reports

## Change or remove access

- **To change what someone can report on**, open **Manage access** and change their selections. The new selection replaces their previous scope. Reports they already ran stay available to them.

- **To remove someone**, click the "✕" (**Remove**) button on their row. Their access is removed right away, and you'll see a confirmation that they can no longer run reports. If the smart reports delegates group is used only by the automatic role, they are also taken out of it. Otherwise, remove them from the group in **Organization settings > Groups**. Once they no longer hold the permission, they can't open smart reports, including the reports they ran. Reports they already downloaded aren't affected.

- **When a user is removed from your organization**, they can no longer run reports. Their saved scope is usually removed at the same time. If your identity provider removes users through SCIM, remove them in **Manage access** first so their old scope isn't kept if they're added back later.

- **When a group is deleted, or a department or cost center value no longer exists**, it disappears from the person's row and from their selections. If a delegate tries to run a report with a selection that no longer exists, the report is refused and they can pick again. You can also open their row and choose new values.

## FAQ

### Can I grant the permission through my own roles instead of the automatic one?

Yes. In **Organization settings > Roles**, the **Smart Reports delegated admin** permission appears under **Product controls**. Adding it to a role isn't enough on its own: each person still needs a scope. Open **Manage access** on the smart reports page, add each person, and choose what they can report on.

### Why is someone greyed out when I try to add them?

They aren't on the **Custom roles** access level, which custom roles (including the automatic one) require. Change it in **Organization settings > Members**, or in your identity provider if it sets access levels.

### Can a delegate see individual users' names or emails?

Only if your organization's **Allow attribution to individual users** setting is on. It is off by default.