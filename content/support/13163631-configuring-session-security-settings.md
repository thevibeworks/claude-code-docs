# Configuring session security settings

This feature is available to Admins and Owners of Enterprise plans and Console Admins.

Session duration controls allow Enterprise and Console Admins to set a maximum session length for all users in their organization. When enabled, users will need to sign in again after the specified period, even if they've been actively using Claude. This helps protect your organization by limiting how long a compromised session could remain valid.

## Enabling session length settings

### For Enterprise Admins

1. Log in to your Enterprise organization as an Admin or above.

2. Navigate to **[Organization settings > Organization and access](https://claude.ai/admin-settings/organization)**.

3. Locate the **Session security** section.

4. Click “Enable” next to **Shortened session length**, then select a duration from the dropdown: 1 day, 7 days, 14 days, or 28 days.

5. Confirm your selection by clicking “Enable.”

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/1888469436/1725e63ea1a2615948faecf4ec73/9bd276a1-7329-414d-87a1-d04dac93fff7?expires=1787053500&amp;signature=4b46803de8984b030eaca332a42da6639ec7fa313294ab51c0d5d71ab9a62e55&amp;req=dSgvHs14lIVcX%2FMW1HO4zQNx6%2BUnRllVg%2F6XaftFnjxTKKeFy4O%2B%2BObp9EHX%0AeWrVvGIOzslmlmtRyw0%3D%0A)

### For Console Admins

1. Log in to your Console account as an Admin.

2. Navigate to **[Settings > Organization and access](http://platform.claude.com/settings/organization)**.

3. Locate the **Session security** section.

4. Click “Enable” next to **Shortened session length**, then select a duration from the dropdown: 1 day, 3 days, or 7 days.

5. Confirm your selection by clicking “Enable.”

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/1888469435/7a766bbe02e61c7d8f05deb5b8f0/b0bda400-47c6-43dd-9907-131ebe180b36?expires=1787053500&amp;signature=791cdcd716c9c98d53b92623601b3a6df674d2ab186bbaf02e306084e5a5a07c&amp;req=dSgvHs14lIVcXPMW1HO4zWzx2L42InwkXZ5D7eVpMtcwnwUj5FdaYhn%2BLkNs%0ARrQSuQRD8GA87zJ%2FUJQ%3D%0A)

### What happens after enabling shortened session length?

- Existing sessions older than the selected duration will expire immediately.

- Other active sessions will expire no later than the selected duration.

- Users whose sessions expire will be directed to sign in again.

## Updating session duration

You can change the session duration at any time by selecting a new value from the dropdown. If you select a shorter duration:

- Sessions older than the new duration will expire immediately.

- Sessions scheduled to expire beyond the new duration will have their expiration shortened accordingly.

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/1888469437/46ac5bc55484ca01556d87a5ade7/b01a7651-ad65-4b32-93ff-16dbc9ca97c0?expires=1787053500&amp;signature=ca2aabef3cb3f2ce5058ce0e634bae42a26dda09b802e6bf1f537b71efdbb262&amp;req=dSgvHs14lIVcXvMW1HO4zZ7mWs%2Bb4jqmA00cbyPOLDWUyQdv88ExWmM45lHw%0A1ocr63DRJhK9rhjuOic%3D%0A)

## Disabling session length settings

To disable session duration, select "Disable" next to **Shortened session length**. Existing active sessions will continue to expire at their scheduled time. New sessions will return to default behavior, where sessions remain active as long as the user stays active.

## Users in multiple organizations

If a user belongs to multiple organizations with different session duration settings, the shortest duration will be applied. For example, if a user is a member of Organization A (7-day limit) and Organization B (28-day limit), their sessions will expire after seven days. This is because a single session is used across all their organizations, so the most restrictive setting takes precedence.