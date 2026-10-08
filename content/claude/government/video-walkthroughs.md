> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Video walkthroughs for administrators

> Watch short narrated walkthroughs of setting up and running Claude for Government for your agency.

> **Who this is for:** Tenant administrators, organization owners, and IT administrators who set up and run Claude for Government. If you use Claude Desktop but don't administer it, see [Video walkthroughs for Claude Desktop](/docs/government/desktop/video-walkthroughs) instead.

Each video is one to three minutes long and narrated, with on-screen captions.

## Admin series

The videos follow the order of a first setup.

### Finding your way around

How a tenant, its organizations, and their users fit together, how administrators sign in to the web portal, and how to move between the admin, tenant, and account views. Read more: [The three views](/docs/government/overview#the-three-views).

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

### Verify your domain and connect single sign-on

Claiming and verifying your agency's email domain, then connecting your identity provider with OIDC or SAML in the setup wizard. Read more: [Step 2: Domains](/docs/government/tenant-admin/setup-wizard#step-2-domains) and [Single sign-on](/docs/government/tenant-admin/identity-and-access#single-sign-on).

<Frame caption="Video: Verify your domain and connect single sign-on (2 min 24 s). Narrated with an AI-generated voice, with on-screen captions.">
  <video controls preload="metadata" playsInline className="w-full aspect-video" src="https://mintcdn.com/claude-ai/gGFKuNSbKYs4JMmK/images/government/videos/admin-02-verify-your-domain-and-connect-single-sign-on.mp4?fit=max&auto=format&n=gGFKuNSbKYs4JMmK&q=85&s=bf307a4d18d646cbce35d3c269be51b7" aria-label="Video walkthrough: Verify your domain and connect single sign-on" data-path="images/government/videos/admin-02-verify-your-domain-and-connect-single-sign-on.mp4" />
</Frame>

<Accordion title="Transcript">
  Before your members can sign in, your tenant needs a verified email domain and a connection to your identity provider.

  Until single sign-on is connected, tenant administrators sign in with a link sent by email.

  Enter your email, select Email me a sign-in link, and open the link from your inbox. Confirm with Sign in, then acknowledge the system-use notification.

  Select Switch to tenant view in the footer, then Resume setup at the top, then Next.

  Sign-in finds your tenant by email domain. Unless Anthropic already verified it, type your agency's domain and select Claim. The page shows a TXT record that proves ownership.

  Your DNS administrator publishes the record. It can take a few minutes to an hour to appear.

  Once the record is live, select Verify now. The domain now shows as Verified.

  Next is Single sign-on. Copy the Redirect URI and the SP Entity ID. You will paste them into your provider.

  In your provider, create an application and paste in those values. In return, OIDC gives you a client ID, a secret, and four endpoints. SAML gives one metadata file.

  First, in another window, confirm you can sign in to your provider. This change applies to everyone, including you. Then enter the values and select Connect. The badge reads Connected. Administrators keep the emailed link as a fallback.

  If your provider uses SAML instead, paste its metadata XML on the SAML tab. Saving one replaces the other.

  Sign-in starts from Claude Desktop or the web portal. Starting from the app's tile in your provider's portal is not supported.

  Both steps are now ticked. New people cannot sign in until a routing rule places them in an organization. That is the wizard's Routing step.
</Accordion>

### Organizations, seats, and routing rules

Adding a sign-in routing rule that places new people in the right organization, adding an organization, and giving it seats. Read more: [Routing rules](/docs/government/tenant-admin/identity-and-access#routing-rules).

<Frame caption="Video: Organizations, seats, and routing rules (2 min 14 s). Narrated with an AI-generated voice, with on-screen captions.">
  <video controls preload="metadata" playsInline className="w-full aspect-video" src="https://mintcdn.com/claude-ai/gGFKuNSbKYs4JMmK/images/government/videos/admin-03-organizations-seats-and-routing-rules.mp4?fit=max&auto=format&n=gGFKuNSbKYs4JMmK&q=85&s=3b4fdf17a38f17ace0a31daff24dd678" aria-label="Video walkthrough: Organizations, seats, and routing rules" data-path="images/government/videos/admin-03-organizations-seats-and-routing-rules.mp4" />
</Frame>

<Accordion title="Transcript">
  Routing rules decide which organization each person lands in. Organizations hold users, seats, and settings, and their seats come from a billing account.

  Marcus, a tenant administrator, signs in and opens the tenant view from the footer.

  A new colleague, Rosa, tries to sign in. No routing rule covers Rosa yet, so the page says Almost there. The attempt is recorded for tenant administrators.

  On Identity and access, Rejected sign-ins lists the attempt. Select Test in preview to check whether any rule covers Rosa.

  The preview says refused at sign-in, because no rule matches Rosa yet.

  Under Sign-in routing, add the first rule. Set If to Anyone with email domain, and choose example.gov. Set Then place in to Operations Bureau, and select Add rule. Rules run top to bottom, and the first match wins.

  Run the preview again. Rosa would now be placed in Operations Bureau.

  Rosa selects Try again and signs in once more. Rosa lands in Operations Bureau and gets a seat, because one was free.

  On Organizations, expand Add organization. Enter a name and the Primary Owner's email, choose the billing account, then select Add. The owner does not automatically become a tenant administrator.

  On Seats, the billing account shows its pool and the organizations it funds. Give Research Office seats and select Save. Its first seats also seat its Primary Owner, and the setup banner clears.

  To send people to Research Office, add an identity provider group rule for them and drag it above the domain rule. Each person belongs to exactly one organization.
</Accordion>

### Directory sync (SCIM) and group mappings

Connecting SCIM provisioning, routing directory groups to organizations, and mapping groups to seat tiers and roles. Read more: [SCIM provisioning](/docs/government/tenant-admin/identity-and-access#scim-provisioning) and [Group mappings](/docs/government/org-admin/provisioning).

<Frame caption="Video: Directory sync (SCIM) and group mappings (2 min 3 s). Narrated with an AI-generated voice, with on-screen captions.">
  <video controls preload="metadata" playsInline className="w-full aspect-video" src="https://mintcdn.com/claude-ai/gGFKuNSbKYs4JMmK/images/government/videos/admin-04-directory-sync-scim-and-group-mappings.mp4?fit=max&auto=format&n=gGFKuNSbKYs4JMmK&q=85&s=e254e02786c5f309b5c5c240c7752c4e" aria-label="Video walkthrough: Directory sync (SCIM) and group mappings" data-path="images/government/videos/admin-04-directory-sync-scim-and-group-mappings.mp4" />
</Frame>

<Accordion title="Transcript">
  Directory sync is optional, and without it accounts are created at first sign-in. With it, your identity provider pushes users and groups, provisioning rules place them in organizations, and each organization maps groups to seat tiers and roles.

  On Identity and access, open SCIM provisioning. Copy the SCIM base URL, which your provider may call the Tenant URL, and select Generate token.

  The token is shown once. Copy it for your provider's secret token field, then select Done. You can revoke a token here at any time.

  In your provider's provisioning settings, paste both values, assign the groups you want to sync, and turn provisioning on.

  After the first sync, your groups appear under Directory groups with member counts, and people not yet placed wait under Synced, not routed.

  Under Provisioning rules, route groups to organizations. Send research-staff to Research Office, and claude-users to Operations Bureau. The first match wins, so add the narrower group first or drag it to the top.

  Once a rule covers them, they are placed in its organization, and the list clears on its own.

  In the organization's admin view, People now includes Group mappings. Map claude-users to a seat tier, here Standard, and claude-owners to the Owner role. Each change is applied right away.

  On Users, the provisioned members now hold their mapped seat tier and role.

  While sync is connected, your directory is the source of truth. Change groups in your provider, because role or seat tier edits made by hand are overwritten by the group mappings.
</Accordion>

### Users, seat tiers, and Readiness for organization owners

Checking the **Readiness** page, assigning seat tiers and roles on the **Users** page, and reviewing the **Tiers** page. Read more: [Organization administration](/docs/government/org-admin/overview).

<Frame caption="Video: Organization owners: users, seat tiers, and Readiness (1 min 48 s). Narrated with an AI-generated voice, with on-screen captions.">
  <video controls preload="metadata" playsInline className="w-full aspect-video" src="https://mintcdn.com/claude-ai/gGFKuNSbKYs4JMmK/images/government/videos/admin-05-organization-owners-users-seat-tiers-and-readiness.mp4?fit=max&auto=format&n=gGFKuNSbKYs4JMmK&q=85&s=d235ae566a0056c409a1b59b2a9623e7" aria-label="Video walkthrough: Organization owners: users, seat tiers, and Readiness" data-path="images/government/videos/admin-05-organization-owners-users-seat-tiers-and-readiness.mp4" />
</Frame>

<Accordion title="Transcript">
  In an organization, a member's role decides what they can manage, and their seat tier decides which models they can use and how much. Readiness shows what still blocks your members.

  Marcus, a Primary Owner, signs in and lands on the organization admin view.

  Under Settings, Readiness lists what blocks members. Every required step is done, but one optional item remains, Assign seat tiers to members. Select Open Users.

  Users lists every member with their role, seat tier, usage against the five-hour and seven-day limits, and last login.

  Wen is Unassigned. Wen can sign in, but Claude Desktop offers no models. Choose a tier from the Seat tier dropdown. The change applies at once, and the models appear the next time Wen starts Claude Desktop.

  Roles are User, Owner, and Primary Owner. Keep at least two Primary Owners, so one can always promote a replacement. From Priya's Role dropdown, Marcus chooses Primary Owner.

  Tiers lists the seat tiers available to your organization. Anthropic-managed tiers are read-only, and your tenant can let you create your own.

  Model access comes from the seat tier, never from the role. Tenant administrator is separate from these roles. If directory groups set roles or tiers, change the group in your provider, because the group mappings overwrite edits made by hand.
</Accordion>

### Config essentials

Editing settings on the **Config** page for an organization or for one directory group, turning on web search, reviewing the session idle timeout, and locking a value for every organization from the tenant. Read more: [How Config works](/docs/government/config/overview).

<Frame caption="Video: Config essentials (2 min 23 s). Narrated with an AI-generated voice, with on-screen captions.">
  <video controls preload="metadata" playsInline className="w-full aspect-video" src="https://mintcdn.com/claude-ai/gGFKuNSbKYs4JMmK/images/government/videos/admin-06-config-essentials.mp4?fit=max&auto=format&n=gGFKuNSbKYs4JMmK&q=85&s=8624805f501e6ca7e01e12e6e94602ab" aria-label="Video walkthrough: Config essentials" data-path="images/government/videos/admin-06-config-essentials.mp4" />
</Frame>

<Accordion title="Transcript">
  Config sets product behavior for the people you manage. The tenant and each organization share the same page, and each level starts from the one above it.

  In the admin view, open Config under Settings. Settings are grouped on the left, and the scope bar at the top shows which level you are editing.

  Product availability has a switch for each product and feature. Chat, Cowork, and Code in Claude Desktop are on by default. Here the organization turns Code in Claude Desktop off and saves.

  To treat one directory group differently, choose it in the scope bar. The same editor appears for that group, and Code in Claude Desktop is turned back on for its members, unless a higher-priority group has settings for them.

  Under Integrations, Web search is off by default. Turning it on asks you to acknowledge how search works. Require approval for each search stays on, so members approve every search.

  Under Sessions and access, Session idle timeout signs out inactive members after 24 hours by default. Lower levels can only shorten it, and lowering it applies from the next sign-in.

  In the tenant view, open the same page and set the Claude Desktop banner for everyone. Choose Must use this value, open Preview impact, then save. Every organization now uses this value.

  Back in the organization's Config, the banner shows Locked by your tenant and cannot be changed there.

  You do not need to push anything. Claude Desktop checks for changes at launch and about every 10 minutes while it runs, or every 30 minutes on older versions, and prompts members to relaunch when something changed.
</Accordion>

### Connectors and plugins

Setting up the Microsoft 365 connector, adding a connector of your own with a tool policy, and adding a plugin. Read more: [Connectors](/docs/government/connectors/overview) and [Manage plugins and connectors](/docs/government/config/plugins-and-connectors).

<Frame caption="Video: Connectors and plugins (2 min 8 s). Narrated with an AI-generated voice, with on-screen captions.">
  <video controls preload="metadata" playsInline className="w-full aspect-video" src="https://mintcdn.com/claude-ai/gGFKuNSbKYs4JMmK/images/government/videos/admin-07-connectors-and-plugins.mp4?fit=max&auto=format&n=gGFKuNSbKYs4JMmK&q=85&s=43f78d15928eea46d27229f8dbc04db6" aria-label="Video walkthrough: Connectors and plugins" data-path="images/government/videos/admin-07-connectors-and-plugins.mp4" />
</Frame>

<Accordion title="Transcript">
  A connector lets Claude reach another service, such as Microsoft 365 or a system of your own. A plugin packages skills and commands for Claude Desktop.

  Microsoft 365 setup starts in Microsoft Entra. An Entra administrator registers an application, approves its Microsoft Graph permissions, and sends you two values, the tenant ID and the client ID.

  On Config, under Integrations, expand Microsoft 365. Paste the Tenant ID and the Client ID, keep Azure cloud on Commercial unless your Microsoft tenant is in GCC High or DoD. Check that Access matches what Entra approved, and save.

  Members then connect Microsoft 365 in Claude Desktop with their own work account, and Claude reaches only what each member can already open.

  For a system of your own, open Add connector on the Connectors card. Name it, enter the server's address, and choose how Claude authenticates, for example a shared secret or member sign-in. Select Next.

  Discover tools asks the server which tools it offers. If the server cannot be reached from your browser, add tool names by hand on the next step.

  Under Apply to, choose the products that receive it, here Claude Desktop only. Under Tool policy, switch off any tool you do not want, then save the connector. Members are still asked before Claude uses an allowed tool.

  On the Plugins card, select Add plugins and drop a zip file. The preview shows its name and version. Choose Auto-install for everyone, or Members choose, then add it.

  You do not need to push anything. Claude Desktop picks up the connector and the plugin when it next checks for changes. Members find plugins under Customize, Plugins.
</Accordion>

### Pilot Claude Desktop on one machine

Connecting one copy of Claude Desktop to Claude for Government with the bootstrap address, signing in, and exporting the configuration for your fleet. Read more: [Configure a single machine](/docs/government/deploy-desktop/configure#configure-a-single-machine).

<Frame caption="Video: Pilot Claude Desktop on one machine (1 min 34 s). Narrated with an AI-generated voice, with on-screen captions.">
  <video controls preload="metadata" playsInline className="w-full aspect-video" src="https://mintcdn.com/claude-ai/gGFKuNSbKYs4JMmK/images/government/videos/admin-08-pilot-claude-desktop-on-one-machine.mp4?fit=max&auto=format&n=gGFKuNSbKYs4JMmK&q=85&s=753d21fb976775a19f3cca9521b738b3" aria-label="Video walkthrough: Pilot Claude Desktop on one machine" data-path="images/government/videos/admin-08-pilot-claude-desktop-on-one-machine.mp4" />
</Frame>

<Accordion title="Transcript">
  A fresh install connects to claude.ai. One setting, the bootstrap address on your Claude for Government host, points it at Claude for Government. Everything else arrives at sign-in.

  First confirm your test account has a seat tier, the device and browser can reach your host and identity provider, and you have administrator rights.

  Open the app and stay on the sign-in screen. Enable Developer Mode from Help, Troubleshooting, then open Developer, Configure Third-Party Inference.

  The window opens on Connection. Change nothing there. In Source, enter the bootstrap address, leave Trust bootstrap-delivered settings off, and select Apply Changes.

  After the relaunch, choose Sign in with your organization. The app shows a pairing code, and you finish sign-in in your browser.

  Then a small window, Apply settings from your organization, lists a Gateway base URL. Confirm it is on your host and select Allow.

  For your fleet, turn on Disable Claude.ai sign-in under Workspace, keep the trust switch off, and use Export for the macOS, Jamf, Intune, or Group Policy files.

  One end-to-end check is a short Claude Desktop banner on the Config page. If it appears in the app after sign-in, per-user delivery works.
</Accordion>

### Deploy to your fleet

Delivering the bootstrap address and the setting that hides the claude.ai sign-in option as device policy, installing the Windows package, enabling the **Virtual Machine Platform** feature that Cowork needs, allowing network access, and deciding on automatic updates. Read more: [Deploy to your fleet](/docs/government/deploy-desktop/configure#deploy-to-your-fleet).

<Frame caption="Video: Deploy to your fleet (1 min 31 s). Narrated with an AI-generated voice, with on-screen captions.">
  <video controls preload="metadata" playsInline className="w-full aspect-video" src="https://mintcdn.com/claude-ai/gGFKuNSbKYs4JMmK/images/government/videos/admin-09-deploy-to-your-fleet.mp4?fit=max&auto=format&n=gGFKuNSbKYs4JMmK&q=85&s=bde163c8a3661fd5393106756950713c" aria-label="Video walkthrough: Deploy to your fleet" data-path="images/government/videos/admin-09-deploy-to-your-fleet.mp4" />
</Frame>

<Accordion title="Transcript">
  Push two values as device policy, the bootstrap address and the setting that hides the claude.ai sign-in option. On macOS they live in a configuration profile, on Windows in machine policy. Deliver them before the app, and note they carry no secrets.

  On Windows, deploy the MSIX package machine-wide. Anthropic publishes Intune install and detection scripts, and an offline installer for networks that cannot reach downloads.claude.ai.

  Cowork needs the Virtual Machine Platform feature, enabled with a restart before rollout. Run the Cowork readiness check on one device per hardware model.

  Allow the app to reach your host, and browsers to reach the host, its sign-in service, and your identity provider. Cowork and Code also download components from downloads.claude.ai.

  Decide on updates. If your agency distributes app updates itself, turn on Block automatic updates on the Config page, lock it, and add the disableAutoUpdates value to the profile. Otherwise, leave updates on.

  With the configuration delivered first, users land directly on the organization sign-in screen, and the configuration window becomes read-only. After a profile change, fully quit and reopen the app.
</Accordion>

### Verify a managed device and spot common failures

What a correctly managed device shows, and the usual causes of an empty model picker, a claude.ai sign-in screen, a repeated settings prompt, and an expired session. Read more: [Confirm it worked](/docs/government/deploy-desktop/configure#confirm-it-worked) and [Troubleshooting](/docs/government/deploy-desktop/configure#troubleshooting).

<Frame caption="Video: Verify a managed device and spot common failures (1 min 40 s). Narrated with an AI-generated voice, with on-screen captions.">
  <video controls preload="metadata" playsInline className="w-full aspect-video" src="https://mintcdn.com/claude-ai/gGFKuNSbKYs4JMmK/images/government/videos/admin-10-verify-a-managed-device-and-spot-common-failures.mp4?fit=max&auto=format&n=gGFKuNSbKYs4JMmK&q=85&s=3a725133f700322bdfcf0d684f9fd1c8" aria-label="Video walkthrough: Verify a managed device and spot common failures" data-path="images/government/videos/admin-10-verify-a-managed-device-and-spot-common-failures.mp4" />
</Frame>

<Accordion title="Transcript">
  On a managed device, the sign-in screen offers only Sign in with your organization, and the configuration window is read-only. Under Help, Troubleshooting, Generate Diagnostic Report saves a report that shows what the app read.

  Sign in as a test user with a seat tier. Chat should work, the picker should list that user's models, and your Config page banner should appear in the app.

  If the picker is empty, nothing is wrong with the device. Most often the user has no seat tier, and an organization owner assigns one on the Users page.

  Only the claude.ai sign-in means the configuration did not reach the app. Check delivery and the diagnostic report, then quit and reopen.

  A prompt to apply settings at every launch means the address was set per user. Have the user check the address and select Allow, and deliver it machine-wide to stop the prompt.

  A Microsoft page saying you cannot access this right now comes from a Conditional Access policy, which your identity team resolves. Nothing in the app changes it.

  On current app versions, Your session has expired with Sign in again is expected after the idle timeout your tenant sets, 24 hours by default. Signing in again reconnects the app. Older versions may call it a configuration sync issue, so update them.
</Accordion>
