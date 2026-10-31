# Get started with smart reports

Smart reports analyze how a team uses Claude and report on the work getting done, what it costs at list price, where sessions run into friction, and which repeated patterns are worth packaging as shared skills. This guide explains how smart reports work, what appears in a smart report, and how to create, share, and delete them.

Each organization can run up to 10 reports per month at no charge. Reports that are queued or in progress count toward this limit, and reports that fail don't.

When your organization reaches its limit, you can’t create new reports. The smart reports page shows the date your limit resets, which is the first day of the next calendar month. If you need more reports before then, contact your account team.

Smart reports are available on Claude Enterprise plans and are off by default, so they must be turned on in your organization's settings.

Claude Enterprise organizations can’t use smart reports if they use customer-managed encryption keys (CMEK), a HIPAA configuration, or a hybrid deployment that runs inference on their own cloud provider. If your organization uses zero data retention for Claude Code, smart reports cover chat and Claude Cowork and leave out Claude Code.

**Important:** Smart reports help you understand adoption and plan your investment in Claude. They aren't designed and should not be used for evaluating individual performance or making employment decisions.

## How smart reports work

First, a Primary Owner, Owner, Admin, or someone with a custom role with analytics view access chooses what the report covers: a team, a time range of up to the last 28 days, one or more products (chat, Claude Code, Claude Cowork, or the unified chat and Cowork experience), the focus areas for the analysis, and any custom questions you’d like Claude to answer while analyzing the transcripts.

Claude then reads a sample of transcripts in that scope, groups them into workstreams and types of outputs, attaches spend to each group, and writes up what it found. Every chart is interactive. Click a workstream to open the sessions inside it, ranked by cost, each with a one-paragraph summary, the product used, the date, and the output type. You can filter by subcategory and download the report as HTML with drilldowns intact.

Sessions that Claude identifies as involving restricted topics, including personal conversations, are used only for aggregate analysis and don’t include summaries (see **[Privacy guardrails](#h_7b22bb48c1)**). Personal conversations also don’t include individual sessions or names. Admins can delete any report (see **[Delete smart reports](#h_765fe12f41)**).

## Information included in smart reports

Each report includes the following sections:

### Workstreams

Workstreams shows what the group used Claude for most, by sessions and by spend, side by side.

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2671030907/7b62b605189fe8e9474a20c1eaf2/image.png?expires=1793476800&amp;signature=2cbd4cd452744f371a679cfca5e10542a344f1e23303dae003723064ae5aaf64&amp;req=diYgF8l9nYhfXvMW1HO4zZse%2BmGYTA4EVa%2FWhnGS4Gm6JPGfaDsFZGqlKYRk%0ADjjtKZgE%2Bn8vGOh0zug%3D%0A)

### Deliverables produced

Deliverables produced groups sessions by the type of output that was produced. For example, analysis, documentation, content drafts, and code.

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2671035220/2a582bc047a6ba46e7dbd6f05d9f/e17881ac-874c-4747-94ca-8679e0301455?expires=1793476800&amp;signature=82b1e9b432ca40ec221e9dd30a1006fa42d71d77dedc37d5e72d77f4eaf8a14b&amp;req=diYgF8l9mINdWfMW1HO4zelj06RflNv6YDEFlKbF9Y9KxmkU63txhlp0PEJF%0Aalm7ZC6XspxW%2B1%2FsSHk%3D%0A)

### Cost per session by type of output

Cost per session by type of output  shows the average spend per session for each kind of output so you can see what's cheap or expensive to produce.

### Task outcomes

Task outcomes  shows what each session produced.

### Most common pain points

Most common pain points shows what got in the way, by category. For example, a connector that wasn’t set up, output that didn’t match the ask, approval or sign-in gating, tool failures, or rework loops.

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2671052365/b69f22b75729e5587563e7ab6830/b1647659-a7ea-403b-89fc-0b150ee97675?expires=1793476800&amp;signature=a97a4c9b3bb36509cb75908e889b6c38fb868157147b48091be9c8d0d3fb3b34&amp;req=diYgF8l7n4JZXPMW1HO4zdDitrkxU9tZjFK5P3Uf7Rg4yBSI2aq7dJRokAsz%0AjjTcdwwsTgRg8LzzNk8%3D%0A)

Click into a category to see more information:

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2671053199/b68936dd5d590c5fbcbbc092b332/5ec247b2-cd67-4f3f-97b5-23479b87a5c6?expires=1793476800&amp;signature=bfe1c582c6ae5230a83d12bcc39554e0781fe036cdff347460a4705ecdc3f870&amp;req=diYgF8l7noBWUPMW1HO4zbuGO4gsIb8UodOVMLl17PVYK7KaLAhCqniPLWk4%0AY%2FbKfUcRjAw0dy6psXg%3D%0A)

### Inefficiencies

Inefficiencies counts sessions that produced nothing usable and sessions that were personal or off-topic, with their cost (shown only as an aggregate count and cost, with no summaries or drilldown).

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2671036122/90dc848a7adf371a872bd89a2f5e/de86945b-ccfe-4e0f-892d-abacc475c5c4?expires=1793476800&amp;signature=fd86b229bee12753ecd6577aca16196d895341d7236e0e8c64d8b1489e8cfc9b&amp;req=diYgF8l9m4BdW%2FMW1HO4zcYfhgySCvISBas8rgXn%2Fb3md6gAwY3Ffu3unWCP%0AX9uSrD6LWsxvbzfBV4E%3D%0A)

### Complex, autonomous work

Complex, autonomous work shows  sessions scoring highest on task complexity, time saved, how long Claude worked on its own, and the expertise required.

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2771304819/746adaaa5ae3196304f0af43cbdd/image.png?expires=1793476800&amp;signature=e990d583f44cef6c8e249228a8f344c670dd5bab78d6d2075acde228b44499a5&amp;req=dicgF8p%2BmYleUPMW1HO4zRKi0HWHikhuhdMrWDTaChUBv%2FH63fEpH9fVDjNj%0AMvmpPBFIC1N98S3Ag6M%3D%0A)

### New to the organization

This section shows work that was new to your organization.

### Automating their own work

This section shows work that people have automated for themselves.

### Most expensive sessions

Most expensive sessions lists where spend concentrates.

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2671032083/2b075387a4a3473f884a8ba26436/image.png?expires=1793476800&amp;signature=4fa9f9f0b8926f81d5818db88993c88d2784891cf42fe2e80908d455efff1bd0&amp;req=diYgF8l9n4FXWvMW1HO4zdLkImyh7UAhnUoxuhUXEhhs%2Bc19T0T69L%2FZr7j2%0A1EooABty%2BVPykeViwss%3D%0A)

### Answers to custom questions

Before running a smart report, you can select a pre-built template or one you’ve saved to steer the analysis towards those questions, and customize those questions to your specific requirements. If you added custom questions, the answers appear in their own section with the sessions that informed them. You can't ask questions about restricted topics (see **[Privacy guardrails](#h_7b22bb48c1)**).

### Custom insights

Custom insights shows the answers to the questions your organization added, which Claude answers for every analyzed session. Each answer shows its share of sessions and spend. Select a bar to see its sessions.

### Recommendations

Recommendations brings the report's suggestions together in one list, including recurring workflows to turn into skills, examples of complex work from across the team, and rules to add to your code repository. To send a finding to the people who can act on it, share it as an artifact.

This section also identifies people whose work is being held back by their spend limit. If you have billing permission and you're using the report's attributed view, you can raise their spend limit from the report.

## Before you begin

- **Role required to enable smart reports for your Enterprise organization:** Primary Owner or Owner

- **Role required to create and view reports:** Primary Owner, Owner, Admin, or a custom role with Analytics view access

- **Role required to delegate access to smart reports to specific team leads or department heads without making them admins:** Primary Owner, Owner, or a custom role with both Analytics and Identity & Access permissions

## Enable smart reports for your organization

An Owner or Primary Owner can take the following steps to enable smart reports for their organization:

1. Navigate to **[Organization settings > Capabilities](https://claude.ai/admin-settings/capabilities).**

2. Find the **Analytics** section.

3. Turn on the "Smart reports" toggle, which is off by default. This makes smart reports available to your organization’s admins with analytics access.

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

1. Navigate to **[Analytics > Smart reports](https://claude.ai/analytics/insights)**.

2. Click "New report."

3. Type a name for your report.

4. Select a specific team or department. Note that this option is only available if you have at least one RBAC group or your organization is in SCIM provisioning and the user payload contains department or cost center fields.

5. Select a date range.

6. Select the products to include in your report.

7. Preview how many sessions will be sampled in your report.

8. Click "Add files" to add documents to help Claude tailor the report.

9. Choose who you want to share the report with.

10. (Optional) Turn on the "Allow attributed view for people you share with" toggle. Note that this option is only available when the org-level "Allow attribution to individual users" toggle is on.

11. Choose a report template, the questions Claude will answer, and any custom insights. You can customize these to your specific requirements.

12. Click "Create report."

Reports usually take a few hours to generate, and they can take longer at busy times. You’ll get an email when the report is ready, and reports also appear in the "Smart reports" list in **[Analytics > Smart reports](https://claude.ai/analytics/insights)**.

## Create custom insights and templates

Custom insights are questions Claude answers for every analyzed session, and the report counts the answers. Custom templates save your questions and custom insights so you can reuse them in future reports.

To add a custom insight while creating a report:

1. Under **Your custom insights**, click "Add custom insight."

2. Enter a name.

3. Under **What should Claude look for in each session?**, describe what Claude should check.

4. Under **Answer**, select "Categories," "Yes or no," or "Scale."

5. Click "Save."

To save your questions and custom insights as a template, click "Save as template" under **Report template**.

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

1. Navigate to **[Analytics > Smart reports](https://claude.ai/analytics/insights)**.

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

## Privacy guardrails

Smart reports have two guardrails for restricted topics. Both are always on, and you can't turn them off:

- **You can’t ask custom questions on restricted topics.** This applies to template questions you customize and to questions you write yourself.

- **Sessions that Claude identifies as involving restricted topics are used only for aggregate analysis.** The report doesn't show a session summary for them.

Restricted topics are:

- **Protected characteristics:** race, ethnicity, national origin, religion, gender identity, age, disability, immigration status

- **Health and medical:** physical or mental health, pregnancy, medical leave, medication, therapy, substance use

- **Union activity:** organizing, collective bargaining, coworkers discussing pay or working conditions

- **Harassment, whistleblower, or legal:** harassment or discrimination complaints, whistleblower reports, privileged legal content about the workplace

- **Political or religious views**

- **Personal life:** family, relationships, personal finances, personal legal troubles, other non-work life

- **Sentiment about people:** feelings about a specific named person, or that person's morale