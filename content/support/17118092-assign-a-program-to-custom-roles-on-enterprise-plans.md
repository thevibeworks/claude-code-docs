# Assign a program to custom roles on Enterprise plans

This article explains how to assign an Anthropic-issued program to users through custom roles on Enterprise plans.

Anthropic offers several verification programs, such as the Cyber Verification Program (CVP), or access to models that might not be generally available. To gain access to these programs, go to our **[Verification Portal](https://portal.anthropic.com/)** to see what programs are available to you, and apply.

Once you’ve applied and been approved for a program, Anthropic issues a "program" or "grant" to your organization. To use the program or grant, you must assign it to a group of people within the organization. In Claude Enterprise, a program applies to members through a custom role: you add the grant to a role, and assign the role to groups of members.

Available on Claude Enterprise plans.

## Before you begin

- Your organization must already have a grant. You’ll see grants only after Anthropic issues one to your organization. To apply to a specific program, go to our **[Verification Portal](https://portal.anthropic.com/)** to see what programs are available.

- You need to be an Owner or Primary Owner in a Claude Enterprise organization to assign grants.

- Members who should get access need the role type "Custom" on the **Members** page. Owners and Admins who keep their built-in role are not covered by custom roles.

## Give members access with a custom role

In Claude Enterprise, Programs and Grants are issued to your organization and apply to members through roles. For some programs, Anthropic creates a role for you: you can’t change its grants, but you can assign groups to it. For others, you add the grant to a role of your own.

To assign a program or grant to a custom role:

1. Navigate to **[Organization settings > Roles](https://claude.ai/admin-settings/roles)** on claude.ai or in the Claude Desktop app.

2. Create a new role by selecting “Add role.” Edit an existing role by opening the three-dot menu at the end of its row and selecting “Edit role.”

3. Select the **Details** tab, then enter a **Role name**. Under **Groups**, choose the groups whose members should get access.

4. Select the **Models** tab and scroll to the **Grants** section.

5. Check the box for each grant this role should have, then select “Save.”

To check that you’ve successfully given members access to your program:

1. Navigate to **[Organization settings > Grants](https://claude.ai/admin-settings/grants)**. The section for your grant lists its requirements (for example, data retention or a member cap, depending on the grant).

2. Navigate to **[Organization settings > Roles](https://claude.ai/admin-settings/roles)**. The role shows **Grant role**.

To remove access, clear the box in the **Grants** section in the custom role and save. To remove one person, take them out of the role's groups.

## Troubleshooting

### The Grants page, or the Grants section in the Models tab of the role, is missing

Your organization doesn’t have a grant yet, or your role can’t view it. These pages are only available for Enterprise plans. Contact your Anthropic account team or an Owner of your organization.

### The checkboxes are grey

Hovering over a box shows "Only organization owners can change which grants this role has." Ask an Owner or Primary Owner.

### The role says "Granted by Anthropic and managed centrally. These grants are read-only."

Anthropic created this role. Assign your groups to it to give them access to your program.

### The role shows "Grant withheld", or the Grants page shows "Action required."

The grant isn’t in effect for a role, or is on hold. Open **Grants** and fix the requirements that aren’t met. If there’s nothing to fix, contact your Anthropic account team.

### The grant is over its member cap

Some grants have a member cap. The role editor shows a warning message: "This role will exceed the member cap of … for the … grant. Everyone in this role will lose access until the member cap is restored." Reduce the members in the groups of the roles that have this grant.