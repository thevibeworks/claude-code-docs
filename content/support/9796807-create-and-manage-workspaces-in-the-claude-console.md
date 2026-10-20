# Create and manage Workspaces in the Claude Console

This guide will walk you through the process of creating, editing, and managing Workspaces in your Claude Console organization.

## What are Workspaces?

Workspaces are collaborative spaces within Console organizations where teams can separate API resources by use case.

If you need to create a fully separate organization with its own members, billing, and Workspaces, see **[Creating a separate Console organization](#h_816b6c2559)** below.

## How to create a new Workspace

**Note:** Only Organization Admins can create new Workspaces.

1. Log in to your **[Claude Console account](https://platform.claude.com/login)**.

2. Go to the **Workspaces** page (platform.claude.com/settings/workspaces).

3. Click "Create workspace." The **Create workspace** page opens (platform.claude.com/settings/workspaces/new).

4. Enter a name for your new Workspace, and select a color. The color helps you identify your Workspace in the Claude Console.

5. Click "Create workspace" to finalize the new Workspace.

Your new Workspace will now appear in the list of Workspaces.

**Note:** You are limited to 100 workspaces per organization.

## Edit Workspace settings

1. From the **Workspaces** list, click on the ellipsis next to the Workspace you want to edit.

2. Select “Edit details."

3. You can modify the following settings:

  - Workspace Name

  - Color

4. After making your changes, click "Save" to apply them.

**Note:** The default Workspace is not editable and cannot be removed.

## Add members to a Workspace

**Note:** You must add members to your Console organization by following **[these instructions](https://support.claude.com/en/articles/13443764-inviting-members-to-the-claude-console)** before you can add them to a Workspace.

1. Go to the **Members** page (platform.claude.com/settings/members).

2. Click "Add to workspace."

3. Select the Workspace, the organization member to add, and their Workspace role.

4. Click "Add to workspace" to confirm.

**Note:** Organization Admins are automatically added as Workspace Admin to every Workspace. Organization Billing role holders are automatically granted ability to see cost, usage, and limit values for all Workspaces, but can be upgraded to the Organization Admin role.

## Delete members from a Workspace

1. Go to the **Members** page (platform.claude.com/settings/members) and select the Workspace from the **Workspace** dropdown menu. If the menu shows "All," removing a member removes them from your organization instead.

2. At the end of the member's row, open the "More actions" menu (three dots) and select "Remove member."

3. Click "Remove" to confirm.

**Note:** Organization members with Admin and Billing roles are automatically granted permissions on all Workspaces and cannot be removed from Workspaces.

## Manage API Keys in a Workspace

1. Go to the **API keys** page (platform.claude.com/settings/keys).

2. Select the Workspace from the **Workspace** dropdown menu to list only its keys.

3. To create a new API key for this Workspace:

  - Click "Create key"

  - Give the key a descriptive name

  - Click "Create key"

4. To revoke an existing API key:

  - Find the key in the list

  - Click the ellipsis next to it

  - Select "Disable API key" or “Delete API key”

    - **Note:** Deleting an API key is a permanent action and cannot be undone.

  - Confirm the action

**Note:** API keys are tied to the Workspace they're created in and cannot be moved between Workspaces.

## Set Workspace rate limits

1. Go to the **Rate limits** page (platform.claude.com/usage/limits) and select the Workspace from the **Workspace** dropdown menu.

2. Click "Edit" next to a model to set its limits.

3. Set a limit for each model tier and limit type by clicking "Edit" next to each option.

4. Workspace limits can be reset to the organization rate limit by selecting a model, leaving all the fields blank in the **Edit workspace rate limits** modal, and clicking "Save."

**Note:** Anthropic always evaluates all applicable limiters—at the Workspace and Organization level—for every request. In other words, if the Workspace limits are unset, Organization limits still apply.

## Set Workspace spend limits or notifications

1. Go to the **Workspaces** page (platform.claude.com/settings/workspaces) and select the Workspace.

2. In the panel that opens, click "Spend limits."

3. Choose one of the following:

  - Select "Change limit" under **Monthly limit** to set a specific spend limit for this Workspace.

    - **Note:** You can only set a spend limit that is lower than your organization’s limit. If unset, your spend limit defaults to the organization’s limit.

  - Select "+ Add notification" under **Email notification** to set up an email notification when the Workspace spend reaches a specific amount.

## View Workspace usage and costs

Go to the **Usage** page (platform.claude.com/usage) or the **Cost** page (platform.claude.com/cost).

## Archive a Workspace

If you no longer need a Workspace but want to retain its historical data:

1. Navigate to the **Workspaces** page.

2. Click the ellipsis next to the Workspace you would like to archive.

3. Confirm that you want to archive the Workspace.

**Note:** Archiving a Workspace will archive all API keys in the Workspace. This action cannot be undone.

## Manage the Default Workspace

Go to the **API keys** page (platform.claude.com/settings/keys) and select "Default" from the **Workspace** dropdown menu.

**Note:** You can view your default Workspace’s limits on the **Rate limits** page (platform.claude.com/usage/limits).

---

## Create a separate Console organization

A single email address can create only one Console organization. If you've already created an organization with your email, signing up again routes you back to that organization instead of starting a new one. You can still be invited to other organizations and switch between them on the same email, but you can only create one yourself.

### When you need a separate organization

You might need a fully separate organization for a different legal entity or for separate billing. A separate organization is independent of your existing one, with its own members, billing, and Workspaces.

To create a new organization, sign up with a work email address that isn't already registered with Anthropic.

### How to create a new organization

The person who will own the new organization should complete these steps. Whoever signs up becomes the organization's Primary Owner.

1. Go to **[Claude Console](https://platform.claude.com/)**.

2. Sign up with a work email address using Google or Microsoft single sign-on (SSO), or an email and password.

3. Verify the email address using the link sent to that inbox.

4. Complete the organization details form, including organization name, entity type, country, and intended use, then choose "Complete setup."

The new organization is created automatically with a default Workspace, and the person who signed up is taken to the Console for that organization.

### After setup

The Primary Owner can:

- Invite members and assign roles (such as Admin, Billing, and Developer) on the **Members** page (platform.claude.com/settings/members).

- Add a payment method on the **Billing** page (platform.claude.com/settings/billing).