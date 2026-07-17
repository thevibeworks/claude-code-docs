# Claude Code usage analytics

This feature allows Console users and owners of Team and Enterprise plans to monitor how their organization uses Claude Code, tracking productivity metrics and adoption patterns across teams.

Claude Code usage analytics are available to:

- **Team plans:** Owners and Primary Owners

- **Enterprise plans:** Owners, Primary Owners, and Admins (requires a Chat + Claude Code seat for usage-based plans or Premium seat for seat-based plans)

- **API Console:** Admin, Billing, and Developer roles

## Access Claude Code analytics

### Team and Enterprise plans

1. Log in to your Owner or Primary Owner account.

2. Click your initials or name in the lower left corner.

3. Navigate to **[Analytics > Claude Code](https://claude.ai/analytics/claude-code)**.

4. Select the “Usage” or “Value”  tab.

### API Console users

1. Log in to your **[Claude Console account](https://platform.claude.com)**.

2. Expand the left side panel.

3. Click “Claude Code” under **Analytics**.

4. View Claude Code usage analytics on **[Settings > Claude Code](https://platform.claude.com/claude-code)**.

---

## Usage tab

The **Usage** tab displays the following metrics for your organization. Data on this tab refreshes daily.

### Organization-level metrics

- **Lines of code accepted**: Total lines of code your team has accepted from Claude Code suggestions.

- **Suggestion accept rate**: Percentage of Claude Code suggestions that your team accepts.

- **Activity trends**: Daily view of active users and sessions over time.

- **Lines accepted over time**: Daily breakdown of accepted code lines.

- **Top commands**: The Claude Code commands used most often across your organization.

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/1717579277/46c512f4b3ed05c359cecd78ed5c/e0ce2c19-39e2-411f-9a1f-cb1d46439a42?expires=1784276100&amp;signature=3b2877cc381d50d9dfd34e44955bed7a11fd3517da27229de959d7e7185a5485&amp;req=dScmEcx5lINYXvMW1HO4zfiEP6JSiH%2FPCX9h5MbdDjNvypRZTInuauaK2J%2Be%0AfzAKglnJ4HGJOn%2B0KBg%3D%0A)

### User-level metrics

**Individual usage**: View each team member's email address and their total lines of code accepted for the current month. You can search for specific users or click the “Export” button to generate a CSV of members’ email addresses and total lines of code.

---

## Value tab

The **Value** tab summarizes usage and cost data to help you understand what Claude Code is returning to your organization at a glance.

- **Estimated productivity lift**

- **Cost per commit**

- **Estimated annual value**

Every formula used on this tab is shown inline. Click any input to adjust it to match your organization's assumptions, and the estimates recalculate.

---

## Contribution metrics (beta)

Contribution metrics are a new feature in public beta that helps Team and Enterprise organizations measure how Claude Code affects engineering velocity. By connecting to your organization's GitHub account, these metrics track code shipping activity with and without Claude Code, so you can see where it's making a difference.

Contribution metrics require GitHub Cloud and are not available to Console users at this time.

For a more in-depth look at contribution metrics, see **[our Claude Code docs](https://code.claude.com/docs/en/analytics#enable-contribution-metrics)**.

### Set up contribution metrics

Contribution metrics require a few steps beyond the base analytics setup:

1. Install the **[Claude GitHub App](https://github.com/apps/claude)** on your organization's GitHub account.

2. Log in with an Owner or Primary Owner account.

3. Navigate to **[Organization settings > Claude Code](https://claude.ai/admin-settings/claude-code)**.

4. Enable the Claude Code analytics feature if you haven't already.

5. Toggle on **GitHub analytics**.

6. Select the GitHub organization(s) you want included in the comparison.

After setup, metrics begin populating automatically. Allow up to 24 hours for data to appear. The dashboard currently processes data once daily.

If you see "GitHub app required. Install the GitHub app to view analytics," the GitHub App hasn't been installed yet. If the app is authenticated but no data appears, confirm the GitHub App is installed and that your team has started using Claude Code.

### Available contribution metrics

Once enabled, the following metrics appear in your Claude Code analytics dashboard:

1. **Pull requests merged**: Total PRs merged with and without Claude Code assistance, at both the organization and user level.

2. **Lines of code committed**: Total lines committed with and without Claude Code assistance, at both the organization and user level.

3. **Pull requests opened per user**: Individual PR activity across your team.

Data is collected by correlating Claude Code session activity with GitHub commits and pull requests.

---

## Data reset and availability

Usage metrics display data for the current calendar month and reset at the beginning of each month. Historical data visualization shows daily granularity for tracking trends over time.

## Use analytics to optimize Claude Code adoption

Review your organization's code acceptance rate to understand if teams are finding Claude Code's suggestions valuable. If rates are lower than expected, consider providing additional training on effective prompting techniques.

Monitor individual usage patterns to identify power users who can share best practices with the broader team, or to spot team members who might benefit from additional support.

Track activity trends to understand when your team uses Claude Code most effectively and ensure adequate seat allocation during peak periods.

---

## Frequently asked questions

### I'm using an individual paid plan; how can I access usage analytics for Claude Code?

Claude Code usage analytics are not available to individual Pro or Max plans at this time.

### I'm looking for a specific user but they're missing from the reports.

If you notice that a specific user isn't showing up in your analytics, you should have them update Claude Code to the most recent version. The first Claude Code version to support this feature is **version 2.0.28**, so users should run `claude update` to manually update Claude Code if needed.

### Where can I find more information?

See **[Analytics](https://code.claude.com/docs/en/analytics)** in our Claude Code docs for more information.