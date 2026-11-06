> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Readiness

> Readiness checks for your tenant and its organizations: what the checks on domains, routing rules, sign-in failures, and billing mean, and who clears them.

> **Who this is for:** Tenant administrators who are setting up a deployment, or who need to find out why users in any organization are unable to use Claude.

The **Readiness** page shows what is blocking your organizations from using Claude and where each item is resolved. To open it, go to **Settings > Readiness** in the tenant admin portal. You would normally work through it once during initial setup and then return whenever the **Settings** menu shows a notification dot. The dot means a required step is unfinished.

An open step shows why it is blocked, and either offers a button that takes you to the page where the fix is made or names who it is waiting on. A step that isn't required doesn't raise the dot, but people can still be stuck until it is done.

When a step is something only Anthropic can do, such as adding credits or reactivating an organization, the page shows **Waiting on Anthropic**. Contact your Anthropic representative to move it forward.

## Tenant-level checks

These checks cover the things every organization in your tenant depends on. The table shows what a check means when it is unfinished, and who can clear it.

| Check | What it means | Who clears it |
| - | - | - |
| **Register a domain** | Until at least one domain is verified, only tenant administrators can sign in, by [emailed link](https://claude.com/docs/government/tenant-admin/identity-and-access.md#emailed-sign-in-link). | You, under [Domains](https://claude.com/docs/government/tenant-admin/identity-and-access.md#domains) |
| **Add a routing rule** | Until at least one rule points at an active organization, people who don't yet have an account are turned away. | You, under [Routing rules](https://claude.com/docs/government/tenant-admin/identity-and-access.md#routing-rules). If your tenant has no active organization, create one on the [Organizations](https://claude.com/docs/government/tenant-admin/organizations.md) page first |
| **Fund the billing account** | No billing account linked to an active organization has a positive balance. | Funding is arranged with Anthropic |
| **Configure the seat pool** | No billing account has a seat pool yet, so the [Seats](https://claude.com/docs/government/tenant-admin/seats.md) page has no seats on Anthropic-managed tiers for you to distribute. Organizations can still give their users seats on any [self-managed seat tiers](https://claude.com/docs/government/org-admin/seat-tiers.md) they create themselves. | The pool is configured by Anthropic |
| **Set up SCIM provisioning** | No directory is connected. Connecting one is optional. | You, under [SCIM provisioning](https://claude.com/docs/government/tenant-admin/identity-and-access.md#scim-provisioning) |
| **Review sign-in failures** | People tried to sign in and were turned away. | You, under [Unplaced users](https://claude.com/docs/government/tenant-admin/identity-and-access.md#unplaced-users) |
| **Fix the identity provider's email attribute** | Sign-in attempts were refused because your identity provider didn't send an email address. | You, in your identity provider's sign-in configuration or under [Attribute mapping](https://claude.com/docs/government/tenant-admin/identity-and-access.md#attribute-mapping-advanced) |

If your tenant has a single active organization, checks from [that organization's Readiness page](https://claude.com/docs/government/org-admin/readiness.md#what-the-checks-mean) appear in the same list.

**Connect single sign-on** shows only on the [setup wizard](https://claude.com/docs/government/tenant-admin/setup-wizard.md)'s Finish step. Until you connect it under [Single sign-on](https://claude.com/docs/government/tenant-admin/identity-and-access.md#single-sign-on), only Primary Owners and tenant administrators can sign in, by [emailed link](https://claude.com/docs/government/tenant-admin/identity-and-access.md#emailed-sign-in-link).

## Organizations

When your tenant has more than one active organization, a card lists each one as **Ready** or with the step that blocks it.

Expanding a row loads that organization's full checklist inline. The steps are the same ones described on the [organization Readiness page](https://claude.com/docs/government/org-admin/readiness.md), and any buttons you click here act on that organization, not the one you are currently viewing in the organization admin portal.

Deactivated organizations appear here with their reactivation status. An organization whose billing account is retired must be assigned a new one by Anthropic before it can be reactivated.
