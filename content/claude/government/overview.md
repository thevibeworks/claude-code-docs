> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Claude for Government administrator guide

> Set up and manage Claude for Government for your agency: how tenants, organizations, users, seats, and credits fit together.

> **Who this guide is for:** Administrators who set up and manage Claude for Government for their agency.

> **Find your section:**
>
> | If you are… | Start with |
> | - | - |
> | A tenant administrator | [Tenant administration](/docs/government/tenant-admin/overview) |
> | An organization owner | [Organization administration](/docs/government/org-admin/overview) |
> | Any user | [Your account](/docs/government/account/overview) |
> | Anyone using Claude Desktop | [Use Claude Desktop](/docs/government/desktop/plugins) |

This guide covers the portals used to manage Claude for Government: how access, seats, and usage are organized, and who is responsible for each part.

If you just want to use Claude for Government, you don't need this guide. You can simply sign in and start a conversation, and come back here when you need to manage other people's access or understand why something is configured the way it is.

## How your deployment is organized

Claude for Government is organized as a three-level hierarchy:

**Tenant** → **Organizations** → **Users**

### Tenant

The tenant is the top level, and it represents your agency's overall deployment. There is exactly one tenant per agency, and it holds the things that are shared across everyone: your connection to your identity provider for single sign-on, automatic user provisioning (where your directory system creates and updates accounts for you), the list of verified email domains, and the pool of credits and seats issued to you by Anthropic.

The tenant is managed by a short list of **tenant administrators**. They create organizations, decide how seats are divided among them and what spend caps are set, and set policies that apply across the whole agency.

### Organizations

An organization is a group of users who share a pool of seats and a set of policies, with its own spend caps. You might create one organization for each bureau, office, or program, or you might run the whole agency as a single organization.

Most agencies start with a single organization. You would create more when you need any of the following:

* Separate billing accounts so one group's usage never draws down another group's balance.
* Separate usage reporting for each bureau or program.
* Different product settings, seat tiers, or access rules for different parts of your agency.

Each organization has its own owners, its own members, its own seat assignments, and its own configuration. The organizations all share the tenant's single sign-on connection, so you configure identity once and every organization uses it.

### Users

A user is a single person. Every user belongs to exactly one organization, and two properties control what they can do:

* A user's **role** determines what they can manage. Most people have the **User** role, which means they use Claude but don't administer anything. **Owners** and **Primary Owners** manage the organization: they manage members' roles and seats, and adjust organization-level settings.
* A user's **seat tier** determines how much they can use Claude. A seat tier is a named bundle of usage limits (for example, how much Claude usage a person gets in a given period). A user with no seat assigned can sign in and see their account, but they can't send messages until an owner assigns them a seat.

A user never belongs to more than one organization at a time. Moving a person between organizations keeps the same account; their role and seat assignment are managed separately in the new organization.

## Billing accounts

A **billing account** is where your agency's credits and seats live. Anthropic sets up one or more billing accounts with your agency, and each one holds a prepaid credit balance (a dollar amount that is drawn down as people use Claude) and a pool of seats (a fixed number of seats in each tier).

Every organization is linked to exactly one billing account, and usage by that organization draws directly from the account's balance. Several organizations can share the same billing account, or each organization can have its own. Tenant administrators divide each billing account's seat pool among the organizations it funds, and can set per-organization spend caps to control how much any one organization draws from a shared balance.

## The three views

<Frame caption="Video: Finding your way around (2 min 23 s). Narrated with an AI-generated voice, with on-screen captions.">
  <video controls preload="metadata" playsInline className="w-full aspect-video" src="https://mintcdn.com/claude-ai/gGFKuNSbKYs4JMmK/images/government/videos/admin-01-finding-your-way-around.mp4?fit=max&auto=format&n=gGFKuNSbKYs4JMmK&q=85&s=e815e7d6b488de1c9629bfaa2f1354ab" aria-label="Video walkthrough: Finding your way around" data-path="images/government/videos/admin-01-finding-your-way-around.mp4" />
</Frame>

<Accordion title="Transcript">
  Your tenant is your agency's deployment and holds its organizations. Each user belongs to one, run by Owners and Primary Owners. Tenant administrators manage the tenant.

  This video shows the web portal, which you open in a browser. Members use Claude in the Claude Desktop app, with Chat, Cowork, and Code.

  In a browser, open your agency's Claude for Government address and enter your work email.

  Select Continue, and your agency's usual sign-in page opens.

  After your agency's single sign-on, acknowledge the system-use notification.

  As an organization owner, Marcus lands on the admin view. With several organizations, tenant administrators pick one from the organization menu at the top of the page.

  Under People, Users lists each member's role and seat tier. Owners and Primary Owners manage these.

  Under Settings, Readiness lists anything blocking members from using Claude. Every step here is complete.

  The footer holds the view links. Select Switch to user view.

  The Account view shows your profile, usage, and sessions. Members who are not owners land here. Marcus is a Primary Owner and, separately, a tenant administrator.

  Switch to admin view takes you back.

  Tenant administrators also get Switch to tenant view.

  The tenant view covers every organization, with identity, seats, settings, and admins. Select an organization's name to open its admin view.

  Until setup is complete, Resume setup sits above the navigation.

  The dot on Settings flags Readiness. Its second card lists each organization, and Research Office still needs seats. Expand the row for its checklist, then follow Open to fix it.

  Admins, under Settings, lists the tenant administrators. Keep at least two.

  Switch to org view returns to the organization admin view.
</Accordion>

The portal has three views. Which ones you can reach depends on your role, and you switch between them using the link in the page footer.

| View | Who has it | What it's for |
| - | - | - |
| [**Tenant**](/docs/government/tenant-admin/overview) | Tenant administrators | Creating organizations, configuring identity and access (single sign-on, provisioning, and routing rules), distributing seats, setting spend caps, and managing who else is a tenant administrator. |
| [**Organization admin**](/docs/government/org-admin/overview) | Organization owners and tenant administrators | Managing users and seats, setting usage tiers, viewing analytics, and configuring organization-level settings. |
| [**Account**](/docs/government/account/overview) | Everyone | Viewing your own profile, checking your usage limits, and managing where you're signed in. |

When you sign in, you land on the most relevant view for you. Organization owners land on the organization admin view, and everyone else lands on their account view. This includes tenant administrators who are not also an organization owner; they start on their account view and can use the **Switch to admin view** link in the page footer, and from there switch to the tenant view.

### A note on tenant administrators

Being a tenant administrator is separate from the role you hold inside an organization. Roles (User, Owner, and Primary Owner) control what you can do within a single organization, while tenant administrator status is granted by adding someone to the tenant's **Admins** list and controls access to the settings that sit above every organization. The two are independent: an organization owner is not automatically a tenant administrator, and a tenant administrator does not automatically hold any particular role inside any organization.

> **For tenant administrators:** Because the tenant sits above every organization, you can also open the organization admin view and act on behalf of any organization in the tenant, even ones you don't belong to. When the tenant has more than one organization, an organization switcher appears at the top of the admin view so you can choose which one you're managing.

## How people get access

Users reach your deployment in one of two ways, both of which are configured by a tenant administrator on the [Identity and access](/docs/government/tenant-admin/identity-and-access) page:

* **Single sign-on.** The user enters their agency email address and is redirected to your identity provider (for example, Microsoft Entra, Okta, or ADFS). When they return authenticated, Claude for Government evaluates your tenant's routing rules to decide which organization they belong in.
* **Directory provisioning.** If your identity provider supports SCIM, which is a standard way for directory systems to keep accounts in sync with other applications, you can connect it so that your directory pushes users and group memberships to Claude for Government automatically. Routing rules then place each provisioned user in an organization based on their group membership.

Routing rules are the only way in. A new person who does not match any rule cannot sign in until a rule is added that covers them. Routing rules are also re-evaluated each time an existing member signs in, so a rule change can move someone to a different organization the next time they sign in.

## Where to go next

* Read [**Tenant administration**](/docs/government/tenant-admin/overview) if you're a tenant administrator managing the overall deployment.
* Read [**Organization administration**](/docs/government/org-admin/overview) if you're an owner managing a single organization.
* Read [**Your account**](/docs/government/account/overview) if you want to understand your own profile, usage, and sessions.
