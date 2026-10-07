# Assign a program to workspaces in Claude Console

This article explains how to apply grants and enable programs for the Anthropic Console and API.

Anthropic offers several verification programs, such as the Cyber Verification Program (CVP), or access to models that might not be generally available. In order to gain access to these programs, go to our **[Verification Portal](https://portal.anthropic.com/)** to see what programs are available to you, and apply.

Once you’ve applied and been approved for a program, Anthropic issues a “program” or “grant” to your organization. To use the program or grant, you must assign it to a group of people within the organization. In the Claude Console, a program applies only to the workspaces you assign it to. This article shows you how to assign one.

## Before you start

- Your organization must already have a grant. Grants appear only after Anthropic issues one to your organization. To apply to a specific program, your Organization Admin or Owner goes to our **[Verification Portal](https://portal.anthropic.com/)** to see what programs are available.

- In the Console, you need to be an organization Admin or Owner. Other roles cannot view or manage grants.

## Give a Console workspace access

In the Console, programs are issued to your organization and apply to workspaces. Some programs, such as the Cyber Verification Program, apply automatically to every workspace that meets their requirements. Others need workspaces assigned. A program only applies to API traffic from workspaces that meet its requirements.

Follow these steps:

1. **[Sign in to the Console](https://platform.claude.com/)** as an organization Admin.

2. Go to **[Organization settings > Programs](https://platform.claude.com/settings/organization/programs)**.

3. Select the program to open its page. The **Workspaces** table shows each workspace's status. A workspace marked with an issue does not meet a requirement yet.

4. Hover over the issue to see which requirement is not met.

5. Open the workspace, select "Manage," then "Programs," and check the **Qualifications** panel.

Unmet requirements are flagged with remediation steps.

## Assigning Programs to a workspace

Programs apply only to the workspaces you assign them to.

### 1. Create a new Workspace and add users

Some programs can’t be assigned to the default workspace. If your program is one of them, create a dedicated workspace first.

1. **[Sign in to the Console](https://platform.claude.com/)** as an organization Admin.

2. Go to **[Settings > Workspaces](https://platform.claude.com/settings/workspaces)**.

3. Click "Add Workspace" (you cannot use the default workspace for accessing the model).

4. Enter a name for your new Workspace, and select a color assignment. This color assignment will be used to help visually identify your workspace in the Claude Console.

5. Click "Create.”

6. Add the approved users to the new Workspace.

**Important:** Some programs have a seat cap. If your organization goes over the cap, assigned workspaces lose access until it’s back under the limit.

Learn more about **[creating and managing Workspaces in the Claude Console](https://support.claude.com/en/articles/9796807-creating-and-managing-workspaces-in-the-claude-console)**.

**Note:** If support asks for your workspace ID, go to **[Settings > Workspaces](https://platform.claude.com/settings/workspaces)** and select your workspace. Workspace IDs start with `wrkspc_`. Your organization ID is under **Settings > Organization**.

### 2. Enable access in your organization

You add the grant to a workspace in your existing Anthropic organization. For API organizations, access is enabled on a workspace within your existing Anthropic organization. You don’t need a new organization or a separate organization.

1. **[Sign in to the Console](https://platform.claude.com/)** as an organization Admin.

2. Go to **[Settings > Programs](https://platform.claude.com/settings/programs)** or **Settings > Grants**, and you’ll see the approved access Grants available for your organization and the model’s codename.

3. Navigate to the new workspace you set up in Step 1 above by going to **[Settings > Workspaces and clicking](https://platform.claude.com/settings/workspaces)**on the new workspace you created.

4. In the workspace, navigate to the **Programs** or **Grants** tab in the Manage section (the label will depend on whether you have existing grants in your provisioned org).

5. Click “Add grant.”

6. Select the program or grant to attach it to the workspace.

7. Make sure the grant is set to **Active**.

After the grant is active, you can use the program through the API with that workspace. If Anthropic sent you setup instructions for your program, follow those next.

## Troubleshooting

- **The Grants page is missing.** Your organization does not have a grant yet, or you are not an organization Admin. Contact your Anthropic account team or your admin.

- **You don’t see your program, the Other grants section is empty, or the Programs tab is missing.** Your organization may not have a program yet, or you might not be an organization Admin. Contact your Anthropic account team or your organization Admin.

- **The workspace shows as inactive.** Open the workspace, select "Manage," then "Programs," and check the **Qualifications** panel for an unmet requirement. Fix each unmet requirement and try again.

- **The grant is over its seat limit.** Some programs have a seat cap. Assigned workspaces lose access until your organization is back under the limit. Reduce the number of members counted toward the grant, then check again.

- **You are trying to use the default Console workspace.** Some programs don't allow the program to be assigned to the default workspace. If the default workspace isn’t working, assign a different workspace or create a new one.

- **You can’t assign the program to a workspace.** Confirm that you’re an organization Admin and that you aren’t selecting the default workspace. Some programs can’t be assigned to the default workspace, so create a dedicated workspace if you need one.

- **The API returns a 401 error.** Confirm your SSO session is active (interactive) or your federated token hasn't expired (workload), and that your credential is scoped to the workspace.

- **The API returns a 404 error for the model.** Double-check the model string and confirm your request is scoped to the workspace, not the default workspace.