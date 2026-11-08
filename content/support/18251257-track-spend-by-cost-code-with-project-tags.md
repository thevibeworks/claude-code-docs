# Track spend by cost code with project tags

This article explains how to tag projects with the codes your organization already uses, such as a work breakdown structure (WBS) code, charge code, or client-matter number. You can then see most spend in those projects by tag, in your organization settings or through the API.

Project tags are available in beta on Claude Enterprise plans. They aren't available to organizations with a HIPAA configuration, customer-managed encryption keys (CMEK), zero data retention (ZDR), including ZDR for Claude Code, minimal data retention, or data stored outside the US. They also aren't available to organizations that route Claude Desktop through their own model provider.

**Important:** Project tags only work inside projects. Work outside a project doesn't get a tag.

## How project tags work

Project tags use two pieces:

- **Tag:** The category you report on, like `cost_code` or `client_matter`.

- **Value:** The code itself, like `CC-1042`.

An owner creates the tag and its values, and anyone who can edit a project can set the value for that project. Each tag holds one value per project, and a project can have up to 16 tags.

## Before you begin

- **Role required to create tags and manage their values:** Primary Owner, Owner, or a custom role with Owner access

- **Role required to set a project's tags:** "Can edit" access to the project

- **Role required to view spend by tag:** Primary Owner, Owner, or a custom role with Analytics view and Billing view access

- **Role required to create API keys:** Primary Owner

## Where project tags apply

| **Where the work happens**                          | **Is spend reported by project?**                                                                                                                |
| --------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| Chat in a project                                   | Yes                                                                                                                                              |
| The unified chat and Cowork experience in a project | Yes                                                                                                                                              |
| Cowork task on your computer                        | Yes. Update to Claude Desktop 3.6556.1 or later and pick one project for the task.                                                               |
| Claude Code in your terminal or on desktop          | Yes, after you **[set the project for Claude Code](#h_7e7b25dba6)**. Requires Claude Code 2.1.305 or later, or Claude Desktop 3.6556.1 or later. |

Project tags don't apply to:

- Claude Code on the web

- Claude for Office

- Claude in Chrome

- Claude Design

- Claude in Slack and Microsoft Teams

- Artifacts

- Voice mode

- The Claude API or the Claude Console

- Claude Code through Amazon Bedrock, Google Cloud Vertex AI, a gateway, or an API key

## Set up project tags

Project tags are on automatically for eligible organizations, with no setting to turn on. To get started, create a tag.

## Create a tag and add its values

Owners can follow these steps to create a tag:

1. Navigate to **[Organization settings > Organization > Project tags](https://claude.ai/admin-settings/tags)**.

2. Click "Create tag."

3. Enter a name, like `cost_code`. Names are lowercase with no spaces, and you can't change a name later.

4. Under **Allowed values**, select "Predefined values only" to have users choose from your list, or "Any value" to let them enter their own.

5. If you selected "Predefined values only," add your list under **Values**. Enter one value per line, or add a CSV file with a single column with `value` as the header.

6. (Optional) Turn on the "Required" toggle to make users set a value on new projects.

7. Click "Continue."

To add values later, open the tag on the **Project tags** page and click "Add values" or "Import CSV."

**Note:** Tag names and values are visible to all users in your organization, so keep sensitive information out of them.

## Add a tag to a project

Anyone with "Can edit" access can add a tag to a project:

1. Open the project.

2. Under **Tags**, click "Add tag."

3. Select the tag, then pick or enter a value.

**Note:** Tag names and values are visible to all users in your organization, so keep sensitive information out of them.

## Set the project for Claude Code

Claude Code doesn't have a project picker, so users set the project in a settings file. If no project is set, Claude Code usage isn't tagged and there's no warning, so let your users know.

1. Open the project in Claude and copy its ID, which is the last part of the URL: claude.ai/project/**this-part**.

2. Open `.claude/settings.json` in a repository, or `~/.claude/settings.json` to apply it across repositories.

3. Add the line below, using your project ID.

4. If you used a repository's settings file, trust the folder when Claude Code asks. The setting takes effect after that.

```
{ "attributionProject": "PROJECT_ID" }
```

**Warning:** Make sure the file stays valid JSON. A stray comma can break Claude Code on that computer.

## View spend by tag

Primary Owners, Owners, and custom roles with Analytics view and Billing view access can view spend by tag:

1. Navigate to **Organization settings > Usage > Spend by project**.

2. Use the "Group by" menu to select your tag.

3. Use the "Period" and "Product" menus to narrow the results.

Data runs through the end of yesterday (UTC). To download the results, click "Export CSV."

**Note:** The names of private projects are shown as “Private project” on this page and in the CSV. The Analytics dashboard, the Analytics API, and the Compliance API still show their real names.

Keep these points in mind when you read the numbers:

- **Add tags before work starts.** Spend only counts toward a tag once the tag takes effect, which takes about two hours. Earlier spend in that project doesn’t count toward it.

- **Projects with no usage won’t appear.** A project shows up after it’s been used in the dates you pick.

- **Reporting starts when project tags become available to your organization.** Don't treat earlier dates as the full history.

- **New tags take about two hours to show up.** Usage during that window may stay under the previous tag or no tag.

- **Changing a tag doesn't change past spend.** Usage stays under whatever tag the project had at the time.

- **Spend outside a project shows as "Not in a project."** This includes Claude Code sessions with no project set. Spend in a project with no value for the tag shows as "No tag value."

- **Amounts may not match your invoice.** They're shown after your discount and before credits, and recent numbers can change until about a week after month end.

- **Usage covered by seats isn't counted.** A project used mostly on seats may show little or no spend.

## Manage tags and pull spend with the APIs

You can set tags and pull spend from your own systems. Both APIs are in beta, so paths and names may change. Your Primary Owner creates API keys in **[Organization settings > Organization > API](https://claude.ai/admin-settings/api-access)**.

### Set tags with the Admin API

Create a key with the read:project_tags and write:project_tags scopes. The Admin API can list your tags, add values to a tag's list, and set a project's tags. It can't create tags, archive values, or create projects.

```
POST /v1/organizations/apps/projects/claude_proj_.../tags

Header: anthropic-beta: ce-project-tags-2026-10-09

Body: {"tags": {"cost_code": "CC-1042"}}
```

The Admin API uses the `claude_proj_` ID, not the ID in the project's URL. To list IDs, call `GET /v1/organizations/analytics/apps/chat/projects?date=YYYY-MM-DD` with a date at least one day old. It only returns projects that had chat activity on that date. This call needs the `read:analytics` scope, so turn on the Analytics API and add that scope to your key.

### Pull spend with usage and cost reports

Turn on the Analytics API and create a key with the `read:analytics` scope. Daily buckets cover up to 31 days per call, so use them to pull a full month.

```
GET /v1/organizations/analytics/cost?starting_at=...&ending_at=...&time_bucket_width=1d&group_by[]=tags.claude_project[cost_code]&limit=1000

Header: anthropic-beta: analytics-usage-cost-2026-08-24
```

- Amounts are in cents, can include fractions of a cent, and already include your discount, but may not match your invoice.

- Each call returns up to 1000 rows. If `has_more` is true, keep paging or your totals will come up short.

- Tag filter text travels in the URL, so it may appear in request logs.

## Current limitations

- **Sharing:** Tag names and values are visible to all users in your organization, so keep sensitive information out of them.

- **Editing:** Anyone who can edit a project can change its tags, and can clear one unless it's required. You can't lock a tag.

- **Required tags:** These only apply to new projects created on the web, so existing projects aren't affected. On the web, a required tag's value can be changed but not removed. The Admin API can still remove it.

- **Characters:** Values can be up to 256 characters and can include spaces and commas. Values that rely on invisible characters, like combined emoji or some Persian or Sinhala words, are rejected.

- **Not included in this beta:** Tags on a single chat or session, splitting spend across tags, renaming tags or values, and spend limits by tag.

## Frequently asked questions

### Can a project have more than one tag?

Yes, using separate tags like `cost_center` and `client_matter`, up to 16 per project. Each tag holds one value, so a project's spend can't be split across two values of the same tag.

### Does Claude check our tag values?

No. A list limits what users can pick, but values aren't checked against your finance systems.

### How do I turn off project tags?

Project tags don't change anything until an Owner creates a tag. To turn them off, reach out to your account team.