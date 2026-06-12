Title: How SCIM sync works for Enterprise organizations

URL Source: https://support.claude.com/en/articles/14499648-how-scim-sync-works-for-enterprise-organizations

Markdown Content:
1.   [All Collections](https://support.claude.com/en/)
2.   [Identity management (SSO, JIT, SCIM)](https://support.claude.com/en/collections/17270717-identity-management-sso-jit-scim)
3.   How SCIM sync works for Enterprise organizations

April 23, 2026

Table of contents

SCIM provisioning keeps your Enterprise organization's membership and groups in sync with your identity provider. This article covers what gets synced, how syncs are triggered, and what to watch for when resyncing.

## What gets synced

When you connect your identity provider (IdP) to your Enterprise organization through the WorkOS integration, two things sync from your IdP:

Group membership in your organization determines which capabilities members with custom roles can access, along with group spend limits.

## Automatic syncing

Your Enterprise organization receives changes from your IdP automatically whenever your IdP pushes member or group updates (adds, removes, or edits) to WorkOS.

Behind the scenes, your organization polls WorkOS for update events every minute and processes them in a queue. This method is eventually consistent—syncs typically complete within minutes, but can take several hours during periods of high system traffic.

## Manual syncing

Some actions trigger a manual sync immediately, and you can also run one on demand.

### Actions that trigger a manual sync

## How to manually trigger a sync

You can trigger a manual sync from two places in your admin settings.

**From the Groups page**

**From the Manage SCIM page**

## Member sync vs. group sync

When you trigger a manual sync, you can choose to sync members, groups, or both. Here's what each does:

## How long manual syncs take

Manual syncs rescan WorkOS for the full list of members and groups to establish an up-to-date baseline. Expect roughly one minute per 100 members in your organization—so a 1,000-member organization takes about 10 minutes to fully resync.

## Verifying your sync status

To check whether your organization's membership and groups are current, you have two options:

## Risks to watch for when resyncing

Before you trigger a manual resync, keep these in mind:

* * *

Related Articles

[Set up JIT or SCIM provisioning](https://support.claude.com/en/articles/13133195-set-up-jit-or-scim-provisioning)[Ping Identity SSO/SCIM email mismatch](https://support.claude.com/en/articles/13917875-ping-identity-sso-scim-email-mismatch)[Google Workspace SSO setup](https://support.claude.com/en/articles/13917884-google-workspace-sso-setup)[Set up role-based permissions on Enterprise plans](https://support.claude.com/en/articles/13930458-set-up-role-based-permissions-on-enterprise-plans)[Set up SCIM in Claude for Government](https://support.claude.com/en/articles/14503643-set-up-scim-in-claude-for-government)
