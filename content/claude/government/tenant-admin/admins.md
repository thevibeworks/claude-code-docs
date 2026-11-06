> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Admins

> Tenant administrator access: what it grants, who can be added, how to add or remove an administrator, and the safeguards on the list.

> **Who this is for:** Tenant administrators who manage who else has tenant-level administrative access.

## How tenant admin access works

**Tenant administrator** is a specific membership list, separate from any role someone holds inside an organization. Being on this list grants access to every page in the tenant admin portal: creating organizations, configuring sign-in and provisioning, writing routing rules, distributing seats, setting spend caps, and setting tenant-wide configuration. It also lets the person open any organization's admin view and act on that organization's behalf.

Adding someone here doesn't make them an owner of any organization, and making someone an organization owner doesn't put them on this list. A tenant administrator doesn't have to belong to any organization or hold a seat. An administrator in no organization shows as **No organization** here and can't use Claude until they [join one](https://claude.com/docs/government/tenant-admin/identity-and-access.md#accounts-in-no-organization).

## Adding a tenant administrator

In the **Add admin** section, start typing a name or email address and select the person from the results, then click **Grant admin**. The change takes effect immediately; the next time that person loads the portal, the tenant admin view is available to them. Adding tenant administrators is self-service and does not require any action from Anthropic.

The search covers organization owners across every organization in your tenant, plus people in your tenant who don't belong to an organization. To add someone with the User role, make them an [Owner](https://claude.com/docs/government/org-admin/users.md#change-a-role) first. If their organization [maps directory groups to roles](https://claude.com/docs/government/org-admin/provisioning.md#group-to-role), add them to the group mapped to Owner in your directory instead.

## Removing a tenant administrator

Click **Remove** next to a name to revoke their tenant admin access. The change takes effect immediately. The person keeps their account and whatever organization role they have, but loses access to this portal. Unless they are an organization's [Primary Owner](https://claude.com/docs/government/org-admin/users.md#understanding-roles), they can also no longer use an [emailed sign-in link](https://claude.com/docs/government/tenant-admin/identity-and-access.md#emailed-sign-in-link).

* You can't remove the last remaining tenant administrator. This protects your tenant from losing all administrative access.
* You cannot remove yourself from the list. If your own access needs to be removed, ask another tenant administrator to do it.
* If the only person on this list leaves your agency or loses account access, contact Anthropic to have a new tenant administrator appointed.
