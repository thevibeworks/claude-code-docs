Title: How SCIM sync works for Enterprise organizations

URL Source: https://support.claude.com/en/articles/14499648-how-scim-sync-works-for-enterprise-organizations

Markdown Content:
# How SCIM sync works for Enterprise organizations | Claude Help Center

[Skip to main content](https://support.claude.com/en/articles/14499648-how-scim-sync-works-for-enterprise-organizations#main-content)

[![Image 1: Claude Help Center](https://downloads.intercomcdn.com/i/o/lupk8zyo/787776/ade321b9d8ff06050cb06ac0049d/d7ef4b66df4ff3851b5de741185c97ab.png)](https://support.claude.com/en/)

[API Docs](https://docs.claude.com/en/docs/intro)[Release Notes](https://support.claude.com/en/articles/12138966-release-notes)[How to Get Support](https://support.claude.com/en/articles/9015913-how-to-get-support)

English

[API Docs](https://docs.claude.com/en/docs/intro)[Release Notes](https://support.claude.com/en/articles/12138966-release-notes)[How to Get Support](https://support.claude.com/en/articles/9015913-how-to-get-support)

English

Search for articles... 

1.   [All Collections](https://support.claude.com/en/) 
2.   [Identity management (SSO, JIT, SCIM)](https://support.claude.com/en/collections/17270717-identity-management-sso-jit-scim) 
3.   How SCIM sync works for Enterprise organizations

# How SCIM sync works for Enterprise organizations

April 23, 2026

Table of contents

[What gets synced](https://support.claude.com/en/articles/14499648-how-scim-sync-works-for-enterprise-organizations#h_aa80c4d36f)[Automatic syncing](https://support.claude.com/en/articles/14499648-how-scim-sync-works-for-enterprise-organizations#h_c8b5139d9c)[Manual syncing](https://support.claude.com/en/articles/14499648-how-scim-sync-works-for-enterprise-organizations#h_bf49a0e7f2)[How to manually trigger a sync](https://support.claude.com/en/articles/14499648-how-scim-sync-works-for-enterprise-organizations#h_beada82363)[Member sync vs. group sync](https://support.claude.com/en/articles/14499648-how-scim-sync-works-for-enterprise-organizations#h_6bbaf2ee87)[How long manual syncs take](https://support.claude.com/en/articles/14499648-how-scim-sync-works-for-enterprise-organizations#h_ca176e5a00)[Verifying your sync status](https://support.claude.com/en/articles/14499648-how-scim-sync-works-for-enterprise-organizations#h_849bc20f61)[Risks to watch for when resyncing](https://support.claude.com/en/articles/14499648-how-scim-sync-works-for-enterprise-organizations#h_dea2998e58)

SCIM provisioning keeps your Enterprise organization's membership and groups in sync with your identity provider. This article covers what gets synced, how syncs are triggered, and what to watch for when resyncing.

Available on the Enterprise plan. For setup instructions, see **[Set up JIT or SCIM provisioning](https://support.claude.com/en/articles/13133195-set-up-jit-or-scim-provisioning)**.

## What gets synced

When you connect your identity provider (IdP) to your Enterprise organization through the WorkOS integration, two things sync from your IdP:

*   **Members** from your SCIM directory 
*   **SCIM groups** that you've pushed from your IdP to WorkOS 

Group membership in your organization determines which capabilities members with custom roles can access, along with group spend limits.

## Automatic syncing

Your Enterprise organization receives changes from your IdP automatically whenever your IdP pushes member or group updates (adds, removes, or edits) to WorkOS.

Behind the scenes, your organization polls WorkOS for update events every minute and processes them in a queue. This method is eventually consistent—syncs typically complete within minutes, but can take several hours during periods of high system traffic.

## Manual syncing

Some actions trigger a manual sync immediately, and you can also run one on demand.

### Actions that trigger a manual sync

*   **Changing the provisioning mode to SCIM.** Any member not in your IdP directory is removed, and any member in your IdP directory is added. You'll need to wait for this initial resync before configuring group mappings. 
*   **Enabling group mappings.** The full list of members and groups updates. New and existing members' roles and seat tiers are enforced by the group mapping and can't be overridden manually. After saving a new mapping, click "Sync." 
*   **Sync now** to recompute roles and seat tiers for existing members. 

    *   Using the "Check for updates" button at **[Organization settings > Groups](https://claude.ai/admin-settings/groups)**. 
    *   Using the "Sync" button at **[Organization settings > Organization and access](https://claude.ai/admin-settings/organization)** under **User provisioning**. 

**Note:**When you update seat provisioning or seat roles through group mappings, existing members aren't resynced automatically. Trigger a manual sync to apply the changes.

When you disable group mappings, you regain the ability to manually assign member roles and seat tiers. Existing members keep their current roles. New members are assigned the User role—change their role to "Custom Roles" if you want to enable custom role permissions.

## How to manually trigger a sync

You can trigger a manual sync from two places in your admin settings.

**From the Groups page**

1.   Go to **[Organization settings > Groups](https://claude.ai/admin-settings/groups)**. 
2.   Click "Check for updates" under **SCIM sync**:  [![Image 2](https://downloads.intercomcdn.com/i/o/lupk8zyo/2312613548/44cd5970ee3c3b2c7f8dcd592d71/image+%2824%29.png?expires=1781156700&signature=f38057f9d312f0bb5f5316a573dfb96b9e7c3861c74e6fed826a8f227b5cd068&req=diMmFM9%2FnoRbUfMW1HO4zW4gbDSsMMuzrgfl7PnOium97p6Frm2zUDyf2xJi%0ATRlQ%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/2312613548/44cd5970ee3c3b2c7f8dcd592d71/image+%2824%29.png?expires=1781156700&signature=f38057f9d312f0bb5f5316a573dfb96b9e7c3861c74e6fed826a8f227b5cd068&req=diMmFM9%2FnoRbUfMW1HO4zW4gbDSsMMuzrgfl7PnOium97p6Frm2zUDyf2xJi%0ATRlQ%0A)  
3.   Select whether to sync members, groups, or both. 

**From the Manage SCIM page**

1.   Go to **[Organization settings > Organization and access](https://claude.ai/admin-settings/organization)** and scroll to the **User provisioning** section. 
2.   Click "Sync." 
3.   Select whether to sync members, groups, or both:  [![Image 3](https://downloads.intercomcdn.com/i/o/lupk8zyo/2312608119/e4b0ef4f309f3c4eac8311a6ef47/image.png?expires=1781156700&signature=364b34a7eaaa93468e048e1a88d4610706a3f20c4b40cd907b3f198e45f9223a&req=diMmFM9%2BlYBeUPMW1HO4zX%2F4frvxzj0Y43OpyTHzM9RAWbxAEzxJWEUNH%2B8j%0Afyx%2B%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/2312608119/e4b0ef4f309f3c4eac8311a6ef47/image.png?expires=1781156700&signature=364b34a7eaaa93468e048e1a88d4610706a3f20c4b40cd907b3f198e45f9223a&req=diMmFM9%2BlYBeUPMW1HO4zX%2F4frvxzj0Y43OpyTHzM9RAWbxAEzxJWEUNH%2B8j%0Afyx%2B%0A) 

**Note:**If you trigger a manual sync while background changes are processing, your organization takes the most recent change for each member or group. If multiple changes are queued for the same member or group, you may need to resync again to make sure everything applies correctly.

## Member sync vs. group sync

When you trigger a manual sync, you can choose to sync members, groups, or both. Here's what each does:

*   **Member sync** updates your organization's record of which members are mapped to seats, seat tiers, and seat roles (Custom Roles, User, Admin, Owner). This can affect members' login access to Claude. 
*   **Group sync** updates your organization's record of which SCIM groups exist and who belongs to them. Group membership determines which capabilities members with custom roles can use, along with group spend limits.  

## How long manual syncs take

Manual syncs rescan WorkOS for the full list of members and groups to establish an up-to-date baseline. Expect roughly one minute per 100 members in your organization—so a 1,000-member organization takes about 10 minutes to fully resync.

## Verifying your sync status

To check whether your organization's membership and groups are current, you have two options:

*   **Export your member list.** Go to **[Organization settings > Members](http://claude.ai/admin-settings/members)** and click "Export CSV" to download the current view of your membership. 
*   **View the WorkOS integration's record.** Go to **[Organization settings > Organization and access](https://claude.ai/admin-settings/organization)** and click "Manage SCIM" to see what WorkOS currently holds for your organization.  

## Risks to watch for when resyncing

Before you trigger a manual resync, keep these in mind:

*   **Changing the provisioning mode to SCIM removes members not in your IdP directory.** Confirm that all existing members are in your IdP directory before changing provisioning mode. 
*   **Updating a member's email creates a new member record.** The member with the old email is removed, and a new member with the new email is created. 
*   **Resyncing cascades to child organizations.** If you have multiple organizations with SCIM provisioning under the same **parent organization**, resyncing one triggers resyncing in the others. This includes sandbox organizations sharing the same parent. 
*   **Incomplete group mappings remove members from the organization.** When enabling group mapping for SCIM, finish assigning all groups before saving. Any member not included in a role group mapping is removed from the organization. If you enable seat tier mapping, any member not in a seat tier group mapping is also removed. 

* * *

Related Articles

[Set up JIT or SCIM provisioning](https://support.claude.com/en/articles/13133195-set-up-jit-or-scim-provisioning)[Ping Identity SSO/SCIM email mismatch](https://support.claude.com/en/articles/13917875-ping-identity-sso-scim-email-mismatch)[Google Workspace SSO setup](https://support.claude.com/en/articles/13917884-google-workspace-sso-setup)[Set up role-based permissions on Enterprise plans](https://support.claude.com/en/articles/13930458-set-up-role-based-permissions-on-enterprise-plans)[Set up SCIM in Claude for Government](https://support.claude.com/en/articles/14503643-set-up-scim-in-claude-for-government)

Did this answer your question?

😞😐😃

Table of contents

[What gets synced](https://support.claude.com/en/articles/14499648-how-scim-sync-works-for-enterprise-organizations#h_aa80c4d36f)[Automatic syncing](https://support.claude.com/en/articles/14499648-how-scim-sync-works-for-enterprise-organizations#h_c8b5139d9c)[Manual syncing](https://support.claude.com/en/articles/14499648-how-scim-sync-works-for-enterprise-organizations#h_bf49a0e7f2)[How to manually trigger a sync](https://support.claude.com/en/articles/14499648-how-scim-sync-works-for-enterprise-organizations#h_beada82363)[Member sync vs. group sync](https://support.claude.com/en/articles/14499648-how-scim-sync-works-for-enterprise-organizations#h_6bbaf2ee87)[How long manual syncs take](https://support.claude.com/en/articles/14499648-how-scim-sync-works-for-enterprise-organizations#h_ca176e5a00)[Verifying your sync status](https://support.claude.com/en/articles/14499648-how-scim-sync-works-for-enterprise-organizations#h_849bc20f61)[Risks to watch for when resyncing](https://support.claude.com/en/articles/14499648-how-scim-sync-works-for-enterprise-organizations#h_dea2998e58)

[![Image 4: Claude Help Center](https://downloads.intercomcdn.com/i/o/487548/17213f6a445c8e6e874b1f4b/fad85208982e639d11b9108df895a293.png)](https://support.claude.com/en/)

*   [Product](https://www.anthropic.com/product)
*   [Research](https://www.anthropic.com/research)
*   [Company](https://www.anthropic.com/company)
*   [News](https://www.anthropic.com/news)
*   [Careers](https://www.anthropic.com/careers)

*   [Terms of Service - Consumer](https://www.anthropic.com/terms)
*   [Terms of Service - Commercial](https://www.anthropic.com/legal/commercial-terms)
*   [Privacy Policy](https://www.anthropic.com/privacy)
*   [Usage Policy](https://www.anthropic.com/aup)
*   [Responsible Disclosure Policy](https://www.anthropic.com/responsible-disclosure-policy)
*   [Compliance](https://trust.anthropic.com/)
