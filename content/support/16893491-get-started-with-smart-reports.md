# Get started with smart reports

Smart reports analyze how a team uses Claude and report on the work getting done, what it costs, where sessions run into friction, and which repeated patterns are worth packaging as shared skills. This guide explains how smart reports work, what appears in a smart report, and how to create, share, and delete them.

During beta, each organization can run up to 10 reports per month for free, and the limit resets on the first day of every calendar month. If you need more reports during beta, please reach out to your account team or submit a request in the smart report page once you've hit the 10 report limit.

Smart reports are available in beta on Claude Enterprise plans and aren’t available for organizations using customer-managed encryption keys (CMEK), HIPAA configurations, or **[Access Transparency](https://platform.claude.com/docs/en/manage-claude/access-transparency)**. Smart reports are also unavailable for Claude Code for Claude Enterprise organizations that use zero data retention.

**Important:** Smart reports help you understand adoption and plan your investment in Claude. They aren't designed and should not be used for evaluating individual performance or making employment decisions.

## How smart reports work

First, a Primary Owner, Owner, Admin, or someone with a custom role with analytics view access chooses what the report covers: a team, a time range of up to the last 28 days, one or more products (chat, Claude Code, or Claude Cowork), the focus areas for the analysis, and any custom questions you’d like Claude to answer while analyzing the transcripts.

Claude then reads a sample of transcripts in that scope, groups them into workstreams and types of outputs, attaches spend to each group, and writes up what it found. Every chart is interactive. Click a workstream to open the sessions inside it, ranked by cost, each with a one-paragraph summary, the product used, the date, and the output type. You can filter by subcategory and download the report as HTML with drilldowns intact.

Personal conversations appear only in aggregate, with no summaries, individual sessions, or names. Admins can delete any report (see **[Delete smart reports](#h_765fe12f41)**).

## Information included in smart reports

Each report includes the following sections:

### Workstreams

Workstreams shows what the group used Claude for most, by sessions and by spend, side by side.

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2671030907/7b62b605189fe8e9474a20c1eaf2/image.png?expires=1789828200&amp;signature=a86e50f31a1522eaa5953ada7035639aa13bc193fc6892e66c5e12b98d26ec17&amp;req=diYgF8l9nYhfXvMW1HO4zZse%2B2uUSQAOVa%2FWhnGS4GnDfnWBftCIiXCBPOlB%0ALNp%2FAn6wlvgAExFwEkE%3D%0A)

### Deliverables produced

Deliverables produced groups sessions by the type of output that was produced. For example, analysis, documentation, content drafts, and code.

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2671035220/2a582bc047a6ba46e7dbd6f05d9f/e17881ac-874c-4747-94ca-8679e0301455?expires=1789828200&amp;signature=5f15f7ff784fb07ae72bf170e4f62b7b138ea5ff62eb3fe30000e24a6d1cbb22&amp;req=diYgF8l9mINdWfMW1HO4zelj0q5TkdXwYDEFlKbF9Y8w3tuJ2W1neRjig8Iw%0AOlVQDWENipSdlACbEZQ%3D%0A)

### Cost per session by type of output

Cost per session by type of output  shows the average spend per session for each kind of output so you can see what's cheap or expensive to produce.

### Task outcomes

Task outcomes  shows what each session produced.

### Most common frictions

Most common frictions shows what got in the way, by category. For example, a connector that wasn’t set up, output that didn’t match the ask, approval or sign-in gating, tool failures, or rework loops.

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2671052365/b69f22b75729e5587563e7ab6830/b1647659-a7ea-403b-89fc-0b150ee97675?expires=1789828200&amp;signature=d64f1a86bcd8a5f0d2c5ddf6be057c6624af2ef3a72bb3c49aa013d91da09e5e&amp;req=diYgF8l7n4JZXPMW1HO4zdDit7M9VtVTjFK5P3Uf7RhYb%2F%2FBZe3viJpxqKix%0Asf%2BS2EMydEnRym7ugMI%3D%0A)

Click into a category to see more information:

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2671053199/b68936dd5d590c5fbcbbc092b332/5ec247b2-cd67-4f3f-97b5-23479b87a5c6?expires=1789828200&amp;signature=ddee222ebb4a57b64aae903b3bcaa19b638db7388f6752ec87645ef9921b4ba6&amp;req=diYgF8l7noBWUPMW1HO4zbuGOoIgJLEeodOVMLl17PXGPl%2BwhE%2FxCppkLR1v%0A29EN%2BWhVUXqsGlL7RNg%3D%0A)

### Inefficiencies

Inefficiencies counts sessions that produced nothing usable and sessions that were personal or off-topic, with their cost (shown only as an aggregate count and cost, with no summaries or drilldown).

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2671036122/90dc848a7adf371a872bd89a2f5e/de86945b-ccfe-4e0f-892d-abacc475c5c4?expires=1789828200&amp;signature=d9ec3d41b4f805213f641ce45f918c188be87a4e7adb61d2c1a59cac445bd68a&amp;req=diYgF8l9m4BdW%2FMW1HO4zcYfhwaeD%2FwYBas8rgXn%2Fb3CoKQI%2F8Dj2a%2BGNYra%0ACisj%2BxxlRU2g%2FBUZ0U8%3D%0A)

### Reusable skills and workflows to build

Reusable skills and workflows to build identifies repeated patterns that could be packaged as a shared skill so the whole team gets the same result faster. For example, turning call notes into follow-ups, building account briefs, and drafting QBR outlines. Each card includes a suggested prompt you can copy to set up the skill.

### Most expensive sessions

Most expensive sessions lists where spend concentrates.

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2671032083/2b075387a4a3473f884a8ba26436/image.png?expires=1789828200&amp;signature=8c1749a46200133bc7a5b2a37fa670386f3b484840b09f2bcc48aba30320a219&amp;req=diYgF8l9n4FXWvMW1HO4zdLkI2at6E4rnUoxuhUXEhi13S1UGXs05UeG2q%2FR%0Ax5x%2BlHu%2BEt4QSKrKgKk%3D%0A)

### Complex, autonomous work

Complex, autonomous work shows  sessions scoring highest on task complexity, time saved, how long Claude worked on its own, and the expertise required.

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2671031695/3781b98c5cb9cdc069439aa3d9ab/image.png?expires=1789828200&amp;signature=b32c8458ad98d0ea1bdaf8a805028d0bd999660626c2df38bf38d5f17bbe2114&amp;req=diYgF8l9nIdWXPMW1HO4zcPtgzv5CdfGtjDEKfEvx0MdZJqC%2FfHMFPAL8RQW%0A32mSOIoIVz4oDpPrjSE%3D%0A)

### Answers to custom questions

Before running a smart report, you can select specific pre-built templates to steer the analysis towards those questions, and customize those questions to your specific requirements. If you added custom questions, the answers appear in their own section with the sessions that informed them.

## Before you begin

- **Role required to enable smart reports for your Enterprise organization:** Primary Owner or Owner

- **Role required to create and view reports:** Primary Owner, Owner, Admin, or a custom role with Analytics view access

- **Role required to delegate access to smart reports to specific team leads or department heads without making them admins:** Primary Owner, Owner, or a custom role with both Analytics and Identity & Access permissions

## Enable smart reports for your organization

An Owner or Primary Owner can take the following steps to enable smart reports for their organization:

1. Navigate to **[Organization settings > Capabilities](https://claude.ai/admin-settings/capabilities).**

2. Find the **Analytics** section.

3. Turn on the "Smart reports (beta)" toggle, which is off by default. This makes smart reports available to your organization’s admins with analytics access.

4. (Optional) Turn on the "Allow attribution to individual users" toggle, which is off by default. This toggle controls whether report viewers can ever see who ran a given session, and each time a viewer reveals names, that action is logged.

  1. **If the toggle is off:** every drilldown shows "User" in place of a name and hides session IDs.

  2. **If the toggle is on:** drilldowns still show "User" by default. The person viewing the report gets an in-report control to reveal member names and session IDs. Unveils are logged.

After you've successfully completed these steps, smart reports are enabled for your Enterprise organization.

You can manage access to let team leads or department heads run smart reports without making them admins. Learn how to **[let team members run smart reports for specific groups](https://support.claude.com/en/articles/16948886)**.

## Scope smart reports to specific teams

Smart reports are more useful when they’re scoped to a functional team rather than the whole organization. For example, you can scope your report to sales, finance, marketing, or engineering. Team-level reports produce clusters specific enough to act on and keep the analysis on spend and adoption: what kinds of tasks, which surfaces and connectors, what it costs.

You can scope by:

- **Groups:** You can filter reports by groups that use role-based permissions. Groups can be created manually in **Organization settings > Groups**, or you can sync groups from your identity provider (IdP) if you use SCIM directory sync.

- **Department or cost center:** If your identity provider groups don’t map cleanly to functional teams, pass department and cost center from your IdP and filter on those instead. See the **[Pass department and cost center via SCIM](#h_cde3c2c758)** section for setup instructions.

## Create a smart report

Once smart reports have been turned on for your organization, Primary Owners, Owners, Admins, and custom roles with analytics view access can create and view reports. Delegates with scoped access can also create and view reports, limited to the groups, departments, or cost centers assigned to them. See **[Let team members run smart reports for specific groups](https://support.claude.com/en/articles/16948886)**.

To create a smart report:

1. Navigate to **[Analytics > Smart reports (beta)](https://claude.ai/analytics/insights)**.

2. Click "New report."

3. Type a name for your report.

4. Select a specific team or department. Note that this option is only available if you have at least one RBAC group or your organization is in SCIM provisioning and the user payload contains department or cost center fields.

5. Select a date range.

6. Select the products to include in your report.

7. Click "Add files" to add documents to help Claude tailor the report.

8. Choose who you want to share the report with.

9. (Optional) Turn on the "Allow attributed view for people you share with" toggle. Note that this option is only available when the org-level "Allow attribution to individual users" toggle is on.

10. Choose a report template and the questions Claude will answer. You can customize the questions to your specific requirements.

11. Click "Create report."

Generating a report takes a few hours. You’ll get an email when the report is ready, and reports also appear in the "Smart reports" list in **[Analytics > Smart reports (beta)](https://claude.ai/analytics/insights)**.

## Pass department and cost center via SCIM

If your identity provider groups don’t map to functional teams, you can push the department and cost center as SCIM attributes and filter smart reports on them.

### Which value is used

The value you send in the attribute is what appears in the filter. Send a name (for example, "Finance") rather than a code unless you want the code shown.

### Attribute paths

Use the SCIM enterprise extension:

- Department: `urn:ietf:params:scim:schemas:extension:enterprise:2.0:User:department`

- Cost center: `urn:ietf:params:scim:schemas:extension:enterprise:2.0:User:costCenter`

### Example PATCH request

User creation and updates use the same structure as today, with the new attributes added:

```
{
  "schemas": ["urn:ietf:params:scim:api:messages:2.0:PatchOp"],
  "Operations": [
    { "op": "replace", "path": "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User:department", "value": "Finance" },
    { "op": "replace", "path": "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User:costCenter", "value": "CC-1234" }
  ]
}
```

Most IdPs can map their department and cost center user attributes to these paths in the SCIM app configuration. Once values are flowing, they appear as filter options when you create a new report.

## Share smart reports

Smart reports can be shared to individual users in your organization. To share a report:

1. Click "Share."

2. Add people to share with.

3. (Optional) Turn on the "Allow attributed view for people you share with" toggle. Note that this option is only available when the org-level "Allow attribution to individual users" toggle is on.

The report only opens through the sharing link. Only the people it's shared with, and admins who can already view reports, can open that link. You can also pre-share a report while you’re creating it or while it’s still generating, so those people can open the report as soon as it’s ready without the admin having to set up sharing again.

## Delete smart reports

To delete a smart report:

1. Navigate to **[Analytics > Smart reports (beta)](https://claude.ai/analytics/insights)**.

2. Click on the three-dot menu for your smart report.

3. Select "Archive."

4. Toggle on "Show archived" at the top of the page.

5. Click on the three-dot menu for your smart report.

6. Select "Delete."

7. Click "Delete report."

## Use cases

- **Attach cost to the work.** See which kinds of work a team does with Claude and what each costs.

- **Find the integration you haven't enabled.** When the same friction shows up across many sessions, the report names it. The fix is often a connector or setting an admin can turn on in minutes.

- **Turn repeated work into a shared skill.** The report identifies the patterns a team keeps reinventing and gives you a starting prompt to package them.

- **Share examples.** Point the rest of the team to sessions that produced a complete pipeline digest or a batch of account briefs so they can follow the same pattern.

- **Bring evidence to renewals.** Walk into a budget conversation with a per-team view of adoption, cost, and output instead of a blended usage number.