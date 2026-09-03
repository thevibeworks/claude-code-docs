# Create surveys for your organization

Surveys let admins ask users short, in-product questions about how they're using Claude and review the aggregated answers in the Admin console. This article explains how to create a survey, choose who sees it, and review the results.

Surveys are available in beta for Enterprise plans. Primary Owners, Owners, and Admins can create and view surveys, along with users on **[custom roles that grant Analytics view access](https://support.claude.com/en/articles/13930452-manage-custom-roles-on-enterprise-plans#h_536123d968)**. While the feature is in beta, organizations using **[customer-managed encryption keys (CMEK)](https://support.claude.com/en/articles/15505325)** can't use surveys.

## How surveys work

Surveys appear in the **Analytics** section. Usage analytics show how much your team uses Claude; surveys tell you what people are doing with it and what's getting in their way.

Users see a survey as a small card in Cowork or chat at a natural break in their work. The card shows your organization's name, and each user sees a given survey once. A survey takes about 90 seconds to complete.

## Create a survey

To create and schedule a survey:

1. Navigate to **[Analytics > Surveys](https://claude.ai/analytics/surveys)**.

2. Click the “New survey” button in the upper right corner.

3. Name your survey. The name is internal only, so users never see it.

4. Set a start and end date. The survey runs for that window and closes automatically.

5. Choose your audience: all members, or one or more groups. Groups are how you narrow a survey to a specific department or team: select the group that matches the department you want to hear from. You can select more than one. Click "Manage groups" to open your organization's group settings.

6. Choose where the survey appears: Cowork, Chat, or both.

7. Review the questions. You can add or remove questions before the survey goes live.

8. Check the preview and the estimated reach panel, which shows how many users are in your selected audience, how many are active in Cowork or chat, and the expected number of responses.

9. Schedule the survey, or save it as a draft.

The following questions are included by default:

1. “What’s the most valuable thing you’ve done with Claude recently? How could you tell the outcome was better than it would have been without Claude?” (text)

2. “For the work you described, what (if anything) did Claude change about the time it took?” (multi-select)

3. “What’s one way you use Claude that a teammate should copy? Describe it so they could start tomorrow: the setup, habit, or way of prompting they wouldn’t know to do.” (text)

4. “If your team lost access to Claude tomorrow, what would break or slow down first?” (text)

## What users see

When a survey is live, users in the audience see a card at a natural break in their work: between tasks in Cowork, or after a reply in chat. A survey never interrupts a running task.

- The card shows your organization's name and explains that answers go to your organization's admins, not to Anthropic.

- Users answer one question at a time.

- Dismissing the card declines the survey.

## Review results

The **Surveys** table lists every survey by status (Live, Scheduled, or Closed), along with its audience, window, response count, and response rate.

Open a survey to see results, which aggregate while the survey is live:

- Total responses and response rate

- The split between Cowork and chat responses

- Bar charts for multi-select questions

- A feed of written responses tagged by group, surface, and date. Filter the feed by group to read the responses from a single department or team.

You can also close a survey early from the results page.

## Export responses

Each survey can be exported as a CSV file from **[Analytics > Surveys](https://claude.ai/analytics/surveys)**. The export includes one row per response, with the submission time, the user's email, their group, the surface where they responded, and one column per question. Multi-select answers are separated by semicolons.

## Privacy and data handling

Surveys run under your organization's name, and responses go to your organization's admins. Your surveys are treated as your data so Anthropic accesses them only as necessary to operate the service. CMEK protections are coming soon, but while this feature is in beta, CMEK customers cannot use it. Regulated customers, including HIPAA customers, should not put regulated data, such as PHI, into survey responses.

Learn more about **[viewing usage analytics for Team and Enterprise plans](https://support.claude.com/en/articles/12883420)**.