> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Admins

> Use this page to view, add, and remove the people who can use the tenant admin portal.

> **Who this is for:** Tenant administrators who manage who else has tenant-level administrative access.

Use this page to view, add, and remove the people who can use the tenant admin portal.

## How tenant admin access works

**Tenant administrator** is a specific membership list, separate from any role someone holds inside an organization. Being on this list grants access to every page in the tenant admin portal: creating organizations, configuring sign-in and provisioning, writing routing rules, distributing seats, setting spend caps, and setting tenant-wide configuration. It also lets the person open any organization's admin view and act on that organization's behalf.

Tenant admin membership is not tied to any organization role. Adding someone here doesn't make them an owner of any organization, and making someone an organization owner doesn't put them on this list.

> **For organization owners:** Being an organization's owner does not make you a tenant administrator, and being a tenant administrator doesn't grant any particular role inside an organization. The two are independent.

## The admin list

The table lists every current tenant administrator with their email and which organization they belong to. A tenant administrator doesn't have to belong to any organization; those rows show *No organization*. This is common for the initial administrator Anthropic sets up during onboarding.

## Adding a tenant administrator

In the **Add admin** section, start typing a name or email address and select the person from the results, then click **Grant admin**. The change takes effect immediately; the next time that person loads the portal, the tenant admin view is available to them.

The search covers organization owners across every organization in your tenant, plus any existing tenant staff who don't belong to an organization. The person must already exist in your tenant, meaning they have signed in at least once or have been provisioned through your directory.

## Removing a tenant administrator

Click **Remove** next to a name to revoke their tenant admin access. The change takes effect immediately. The person keeps their account and whatever organization role they have; only the ability to open this portal is removed.

<Warning>
  You can't remove the last remaining tenant administrator. The button is disabled when only one is left. This protects your tenant from losing all administrative access.
</Warning>

## Things to know

* Adding tenant administrators is self-service and does not require any action from Anthropic. See [Adding a tenant administrator](#adding-a-tenant-administrator) above.
* You cannot remove yourself from the list. If your own access needs to be removed, ask another tenant administrator to do it.
* There is no upper limit on the number of tenant administrators, but because the access is broad, keep the list as short as your operational needs allow.
* If the only person on this list leaves your agency or loses account access, contact Anthropic to have a new tenant administrator appointed.
