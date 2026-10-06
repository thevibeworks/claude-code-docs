# Use Claude Code \(local mode\) and Claude Cowork \(local mode\) on a HIPAA-ready Enterprise plan

The HIPAA configuration is an organization setting on Enterprise plans. It brings local Claude Code and Claude Cowork sessions, as opposed to cloud sessions such as Claude Code on the web, under your Business Associate Agreement (BAA) with Anthropic. This article calls them Claude Code (local mode) and Cowork (local mode). They run in one of these places:

- Claude Code in the terminal

- Claude Code in the Code section of Claude Desktop

- Cowork in Claude Desktop

With the configuration applied, members can use both products with protected health information (PHI), on the conditions in **[Check what your BAA covers](#h_eba343b314)**. Applying it also turns off certain features across your organization.

Available on Enterprise plans only. Only the Primary Owner can apply the HIPAA configuration.

This article is for the Primary Owner, who applies the configuration, and for any Owner who helps decide whether to apply it, prepare for it, and confirm it.

"HIPAA-ready" means the product is configured to support your HIPAA obligations under the BAA. Compliance remains your organization's responsibility.

**Note:**

- If your organization hasn't enabled HIPAA, start with **[HIPAA-ready Enterprise plans](https://support.claude.com/en/articles/13296973-hipaa-ready-enterprise-plans)**. Enabling HIPAA brings chat under your BAA. That step alone doesn't bring Claude Code (local mode) or Cowork (local mode) under your BAA.

- If you prepare members' computers, see **[Set up Claude Code (local mode) for a HIPAA-ready organization](https://code.claude.com/docs/en/hipaa-setup)** and **[Set up Cowork (local mode) for a HIPAA-ready organization](https://claude.com/docs/cowork/hipaa-setup)**.

- If you want to check whether a specific feature is covered under your BAA, see the list of Eligible Services in the **[Implementation Guide for HIPAA Entities](https://trust.anthropic.com/resources?s=l1wrssd9hsbi4gak0tp5a6&name=%5Banthropic%5D-hipaa-ready-offering-implementation-guide)** and **[Business Associate Agreements (BAA) for Commercial Customers](https://support.claude.com/en/articles/8114513-business-associate-agreements-baa-for-commercial-customers)**.

## Check what your BAA covers

After you apply the HIPAA configuration, your BAA covers each product in the table, on the condition in the second column. Applying the configuration turns off Cowork and the Code section of Claude Desktop, even if they were on, so an Owner has to turn each one on afterward.

| **Product**                                       | **Covered under your BAA when**                                                                                                               |
| ------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| Claude Code in the terminal                       | Members sign in with their Claude Enterprise account, and Claude Code connects directly to Anthropic, not through a cloud provider or gateway |
| Claude Code in the Code section of Claude Desktop | An Owner has turned on the "Desktop" toggle in **Organization settings > Claude Code**                                                        |
| Cowork in Claude Desktop                          | An Owner has turned on the "Enable for your organization" toggle in **Organization settings > Cowork**                                        |

You don't need zero data retention (ZDR) to apply the configuration. If your organization has ZDR for Claude Code, see **[Replace ZDR with the configuration](#h_a6b761685a)**.

### Products and features your BAA doesn't cover

Keep PHI out of these products and features. Your BAA doesn't cover them, even with the configuration applied:

- The Claude Code extensions for VS Code and JetBrains, which keep working after you apply the configuration

- Any feature labeled beta or research preview

- Claude Code sessions that connect through a cloud provider such as Amazon Bedrock, an LLM gateway, or a custom base URL

- Claude Code sessions that use a Claude Console API key, unless the Claude Console organization has ZDR enabled

- Connectors, MCP servers, plugins, desktop extensions, Claude in Chrome, and skills, including after an Owner turns them on

- Cloud and remote features such as Claude Code on the web, which the configuration makes unavailable

Ask your IT team to **[deploy managed settings](https://code.claude.com/docs/en/hipaa-setup#deploy-managed-settings)**, a policy file on each computer that directs members to sign in with a Claude Enterprise account and refuses cloud providers and gateways. For a full list of Eligible Services, please review the **[Implementation Guide](https://trust.anthropic.com/resources?s=l1wrssd9hsbi4gak0tp5a6&name=%5Banthropic%5D-hipaa-ready-offering-implementation-guide)** and **[Business Associate Agreements (BAA) for Commercial Customers](https://support.claude.com/en/articles/8114513-business-associate-agreements-baa-for-commercial-customers)**.

## Ask Anthropic to turn on the HIPAA configuration

You apply the configuration with the "Apply HIPAA configuration" button in **Organization settings > Data and privacy**. The button is grayed out until Anthropic turns it on for your organization. Ask your Anthropic account team to turn it on.

If your organization doesn't have an account team, you can't apply the configuration. See **[Coverage until you apply the configuration](#h_415ff36247)** and **[Business Associate Agreements (BAA) for Commercial Customers](https://support.claude.com/en/articles/8114513-business-associate-agreements-baa-for-commercial-customers)** for what your BAA covers if you haven't applied it.

### Coverage until you apply the configuration

Until you apply the configuration, members can still use Claude Code (local mode) and Cowork (local mode) where an Owner has them turned on, but your BAA may not cover their use. Coverage differs for organizations with and without zero data retention (ZDR) for Claude Code:

- **Without ZDR for Claude Code:** Your BAA doesn't cover Claude Code or Cowork, so don't use them to process PHI.

- **With ZDR for Claude Code:** Your BAA covers Claude Code through ZDR. It doesn't cover Cowork, so don't use Cowork to process PHI.

Your account team can tell you whether your organization has ZDR for Claude Code.

### Replace ZDR with the configuration

The configuration is meant to replace ZDR for Claude Code (local mode). Applying it doesn't turn ZDR off. Don't apply the configuration if you wish to keep your existing access through ZDR.

If you have ZDR enabled for Claude Code within Claude for Enterprise, email your account team for help switching to the HIPAA configuration.

Once ZDR is removed, Anthropic keeps Claude Code data under standard retention, as it does for your organization's chat data.

## Prepare your organization

Complete these tasks before you apply the configuration.

### Review what changes for members

The table shows the changes members are most likely to notice, and what to do about each one before you apply the configuration. The **[Implementation Guide for HIPAA Entities](https://trust.anthropic.com/resources?s=l1wrssd9hsbi4gak0tp5a6&name=%5Banthropic%5D-hipaa-ready-offering-implementation-guide)** and **[Business Associate Agreements (BAA) for Commercial Customers](https://support.claude.com/en/articles/8114513-business-associate-agreements-baa-for-commercial-customers)** list the Eligible Services under your BAA.

| **What changes**                                                                                                                                                         | **What to do before you apply**                                                                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------- |
| Cowork, the Code section of Claude Desktop, skills, and Claude in Chrome turn off, even if an Owner had turned them on                                                   | List the ones you want back and who approves each one                                                |
| Every other setting that enabling HIPAA turns off by default turns off again, including chat settings                                                                    | List the settings an Owner has turned on since you enabled HIPAA                                     |
| Each connector turns off, and its tool permissions change to **Blocked**, unless an Owner accepted the terms when they added or enabled it                               | Record each connector's tool permissions, because turning the connector back on doesn't restore them |
| The built-in GitHub integration turns off                                                                                                                                | Note whether you want it back                                                                        |
| Each desktop extension is removed from your organization's allowlist, unless an Owner accepted the terms when they added it                                              | List the extensions you want to add again                                                            |
| Within minutes, members can't start sessions in Claude Code on the web or Cowork in the cloud. Sessions that are already running stop. Members will lose access to them. | Ask members to finish that work and save what they need                                              |
| Remote Control and Claude Tag aren't available. Claude Design turns off until an Owner turns it on                                                                       | Ask members who use them to finish that work                                                         |
| Approvals that members gave to scheduled tasks in Cowork and the Code section of Claude Desktop expire                                                                   | Tell members to expect to approve their scheduled tasks again                                        |

Chat uses the same connectors, skills, and Claude in Chrome settings, so when these turn off, they turn off in chat too.

### Have your team review the terms

When you apply the configuration, you accept the BAA and confirm that you reviewed the **[Implementation Guide for HIPAA Entities](https://trust.anthropic.com/resources?s=l1wrssd9hsbi4gak0tp5a6&name=%5Banthropic%5D-hipaa-ready-offering-implementation-guide)**, which includes a list of Eligible Services under your BAA. Ask your legal and compliance teams to review both documents before you apply the configuration.

### Ask your IT team to prepare computers

Ask your IT team to follow **[Set up Claude Code (local mode) for a HIPAA-ready organization](https://code.claude.com/docs/en/hipaa-setup)**. If members use Cowork, ask the team to follow **[Set up Cowork (local mode) for a HIPAA-ready organization](https://claude.com/docs/cowork/hipaa-setup)** too. They update Claude Code and Claude Desktop to the latest versions, allow network access to Anthropic's servers, and deploy managed settings and the Claude Desktop policy.

The update matters because once the configuration is applied, Anthropic's servers reject requests from versions older than the minimum.

### Choose a time and tell members

Apply the configuration at a quiet time for your organization because Cowork, the Code section of Claude Desktop, and some connectors stay off until an Owner turns them on. Keep an Owner available afterward, and plan time to turn on each connector separately.

Tell members the date and time, which features turn off, and which ones you plan to turn back on.

## Apply the HIPAA configuration

To apply the configuration, you must be the Primary Owner and have a verified email address. Other Owners and Admins can't apply it, because applying it includes accepting the BAA for your organization.

The configuration applies to your existing Claude Enterprise organization, the same one your members use for chat, not to a separate account. It applies to Claude Code and Cowork together, and to every member.

**Warning:** When you apply the HIPAA configuration, certain features start turning off across your organization as soon as you confirm. An Owner can turn some features back on, but cloud features such as Claude Code on the web stay unavailable.

To apply the configuration:

1. Sign in to Claude as the Primary Owner and go to **[Organization settings > Data and privacy](https://claude.ai/admin-settings/data-privacy-controls)**.

2. In the "Compliance" section, find the row for Claude Code (local mode) and Cowork (local mode).

3. Select "Apply HIPAA configuration." A dialog opens.

4. In the dialog, review what changes, then download the Implementation Guide for HIPAA Entities, and the BAA if your organization has none on file. The "Apply HIPAA configuration" button in the dialog stays grayed out until you download them. Selecting it accepts Anthropic's updated BAA.

5. Select "Apply HIPAA configuration" to confirm. A message confirms that the configuration is applied.

If the button is grayed out, check that you're signed in as the Primary Owner and that your email address is verified. If it's still grayed out, **[ask Anthropic to turn it on](#h_a54ff1eb7a)**.

## Turn features back on

Cowork, the Code section of Claude Desktop, skills, and Claude in Chrome are off after you apply the configuration, and so is each connector whose terms no Owner had accepted. An Owner turns on the ones your organization approved. The **[Implementation Guide for HIPAA Entities](https://trust.anthropic.com/resources?s=l1wrssd9hsbi4gak0tp5a6&name=%5Banthropic%5D-hipaa-ready-offering-implementation-guide)** and **[Business Associate Agreements (BAA) for Commercial Customers](https://support.claude.com/en/articles/8114513-business-associate-agreements-baa-for-commercial-customers)** list the Eligible Services under your BAA.

Turning a feature on doesn't change whether your BAA covers it.

Connectors take more steps, because you turn on each one separately. Go to **Organization settings > Connectors**, open the connector, select "Enable" in the banner, select the checkbox to accept the terms, and click "Continue." Then set the connector's tool permissions again.

## Confirm the configuration is applied

Ask members to restart Claude Code and Claude Desktop, so that both get the configuration right away. Without a restart, a running Claude Code session gets it within about an hour. Claude Desktop might not get it until a member restarts or reloads the app.

Organization settings, Claude Code, and Claude Desktop each show the configuration once it's applied:

- **Organization settings:** Go to **[Organization settings > Data and privacy](https://claude.ai/admin-settings/data-privacy-controls)**. Confirm that the row for Claude Code (local mode) and Cowork (local mode) says they're HIPAA configured for this organization, and shows the date you applied the configuration.

- **Claude Code:** Ask a member to run `/status` in a session. Confirm that the **Status** tab lists `HIPAA` on the `Organization configuration` line.

- **Claude Desktop:** Confirm that the title bar shows a **HIPAA configured** label. On a Mac, open the sidebar to see it.

Tell members not to process PHI until they see `HIPAA` in `/status`, or the **HIPAA configured** label, on their own computer.

If either one is missing on a member's computer, ask your IT team to follow **[Confirm the configuration on a computer](https://code.claude.com/docs/en/hipaa-setup#confirm-the-configuration-on-a-computer)**, which lists the likely causes in order. For the Claude Desktop label, see **[The HIPAA configured label is missing](https://claude.com/docs/cowork/hipaa-setup#the-hipaa-configured-label-is-missing)**. If it's still missing, contact your account team.

## Manage data on members' computers

Claude Code (local mode) and Cowork (local mode) store session data, such as transcripts, on each member's computer. Securing and deleting that data is your organization's responsibility.

Removing a member from your organization deletes nothing on their computer, so wipe the computer when a member leaves. Keep full-disk encryption turned on.

**[Manage local session data](https://code.claude.com/docs/en/hipaa-setup#manage-local-session-data)** lists where the data is stored, what Claude Code (local mode) and Claude Desktop delete automatically, and how to delete the rest. For Cowork data, see **[Manage Cowork data on each computer](https://claude.com/docs/cowork/hipaa-setup#manage-cowork-data-on-each-computer)**.

## Monitor sessions

These tools show what happens in Claude Code (local mode) and Cowork (local mode). They differ in whether they include session content:

- **Compliance API:** With the **[Compliance API](https://support.claude.com/en/articles/13015708)** turned on for your organization, Anthropic captures session activity and content from both products so that your organization can read it through the API. Sessions are readable for 30 days, or for your organization's retention period if it's shorter. While your organization has ZDR for Claude Code, Anthropic doesn't capture Claude Code sessions.

- **Audit logs and data exports:** Audit logs and data exports don't include session content. The audit log records administrative changes, such as enabling HIPAA and applying the configuration.

- **OpenTelemetry:** You can send events from both products to your own monitoring tools. The data you export is your organization's responsibility. Set the destination for Cowork in **Organization settings > Data and privacy > Monitoring**. Your IT team sets the destination for Claude Code in **[managed settings](https://code.claude.com/docs/en/monitoring-usage#administrator-configuration)**.

**Important:** By default, Cowork's OpenTelemetry events include prompt text, Claude's responses, and tool inputs, so PHI in a session may reach your monitoring tools. No organization setting turns that content off. Your IT team turns it off on each computer, as described in **[Content capture](https://claude.com/docs/cowork/monitoring#content-capture)**.

## Get help

For questions about the BAA, the Implementation Guide for HIPAA Entities, or the configuration, contact your Anthropic account team. Do not include PHI in a support request.