> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Readiness

> Use this page to see everything that is blocking your organizations from using Claude, and to find the one place where each blocker is resolved.

> **Who this is for:** Tenant administrators who are setting up a deployment, or who need to find out why users in any organization are unable to use Claude.

Use this page to see everything that is blocking your organizations from using Claude, and to find the one place where each blocker is resolved.

A deployment is ready when a user in each organization can sign in, be placed in that organization, hold a seat, and send a message to a model. This page runs that check for the whole tenant and lists every step that is complete, blocked, or waiting on someone. You would normally work through it once during initial setup and then return whenever the **Settings** menu shows a notification dot, which appears whenever anything on this page needs attention.

## How the checklist is presented

Each step sits on a vertical track with a status marker.

* A **green check** means the step is complete. The label is struck through and you can ignore it.
* A **filled circle** marks the step you should act on next. It expands to show why it is blocked and offers an **Open** button that takes you to the page where the fix is made.
* A **clock** means the step is blocked but you are not the person who can clear it. A line underneath tells you whether it is waiting on Anthropic, on an organization owner, or on the owner of a shared billing account.
* A **hollow circle** is a step still to come. It stays collapsed until the steps ahead of it are cleared.

Below a divider is an **Optional** section. These items do not stop anyone from using Claude, but the page surfaces them because they usually matter, such as setting up SCIM provisioning or reviewing sign-in attempts that were turned away.

Use **Refresh** at the top right after you make a change elsewhere to see the updated state without leaving the page.

## Tenant-level checks

These are the items that appear in the top card. They cover the things every organization in your tenant depends on.

* **Activate the tenant** appears on its own when Anthropic has not yet finished provisioning your tenant, or when the tenant has been deactivated. Nothing else can be configured until this clears, and only Anthropic can clear it, so the page shows a waiting state.
* **Fund the billing account** checks that at least one billing account linked to an active organization has a positive balance. This is advisory because the blocking state is shown on each organization's own readiness check. Funding is arranged with Anthropic.
* **Configure the seat pool** checks that at least one billing account has a seat pool set. This is also advisory. Until a pool is set, the [Seats](/docs/government/tenant-admin/seats) page has no seats on Anthropic-managed tiers for you to distribute. Organizations can still give their users seats on any [self-managed seat tiers](/docs/government/org-admin/seat-tiers) they create themselves. The pool is configured by Anthropic as part of your contract.
* **Register a domain** is required. Claude for Government routes users to your tenant by the domain of their email address, so until at least one domain is registered nobody can start a new sign-in. Use **Open Identity and access** to go to the [Identity and access](/docs/government/tenant-admin/identity-and-access) page and add one.
* **Set up SCIM provisioning** is optional. SCIM lets your directory push users and groups into Claude for Government automatically. If you plan to use it, generate a provisioning token on the [Identity and access](/docs/government/tenant-admin/identity-and-access) page.
* **Add a routing rule** is required. Routing rules decide which organization each user joins when they sign in. Until at least one rule points at an active organization, every new sign-in is turned away. Use **Open Identity and access** to add a rule. If your tenant has no active organizations yet, the button instead opens the [Organizations](/docs/government/tenant-admin/organizations) page so you can create one first.
* **Review sign-in failures** is an optional summary of people who tried to sign in and were turned away. The description tells you how many need a routing rule, how many need their email domain registered, and how many conflict with an existing account. Use **Open Identity and access** to resolve them.

If your tenant has a single organization, that organization's own checks (credits, spend caps, seats, seat tiers, and products) appear directly in this card below the tenant-level items, so you can work through the whole deployment from one list.

## Organizations

When your tenant has more than one organization, a second card lists each one with a one-line summary: **Ready**, a named blocker with **(fix available)**, or a named blocker with who it is waiting on. The marker beside each row uses the same colors as the checklist above.

Expanding a row loads that organization's full checklist inline. The steps are the same ones described on the [organization Readiness page](/docs/government/org-admin/readiness), and any buttons you click here act on that organization, not the one you are currently viewing in the organization admin portal. This lets you clear an organization's blockers without switching context.

Deactivated organizations appear here with their reactivation status. An organization whose billing account is retired cannot be reactivated until the account has settled and Anthropic has assigned a new one, so those rows show a waiting state instead of a button.

## Things to know

* Every **Open** button goes to the page where the fix belongs, with the right organization already selected when one applies. You make the change there and return here to see it reflected.
* When a step is something only Anthropic can do, such as funding a billing account or reactivating an organization, the page shows **Waiting on Anthropic**. Contact your Anthropic representative to move it forward.
* Hover the help icon next to any step's label for a one-line explanation of what the check looks for.
