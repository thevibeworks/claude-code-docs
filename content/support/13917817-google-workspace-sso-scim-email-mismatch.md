# Google Workspace SSO/SCIM email mismatch

Claude uses email as the primary identifier to match SSO logins to provisioned seats. In Google Workspace, SCIM auto-provisioning and SAML SSO can send different email values—especially when people have email aliases—causing a mismatch that blocks access.

**Applies to:** Enterprise plans and Console organizations using SCIM provisioning. Team plans don't have SCIM provisioning, so this mismatch scenario doesn't apply — see **[Set up JIT or SCIM provisioning](https://support.claude.com/en/articles/13133195)** for what's available on each plan.

---

## Symptoms

People may experience one or more of the following when attempting to access your organization via SSO:

- **"Account creation is blocked"** — The person authenticates via SSO but Claude cannot find a matching provisioned account. If your organization has organization creation restricted (recommended), the person is blocked entirely.

- **Landing on a free personal account** — If organization creation is not restricted, the person bypasses your organization entirely and creates or lands on a free personal account instead of their provisioned seat.

- **"Please confirm your email" mismatch** — The SSO callback shows a different email than the one the person entered at login.

- **Claude Code authentication failure** — The Claude Code CLI shows an email mismatch error during the authentication flow, preventing the person from connecting to your organization.

---

## How this happens

Google Workspace accounts have a primary email and may have multiple aliases. SCIM provisioning and SAML SSO are configured separately in the Google Admin console and can pull from different address fields:

| **Google attribute**    | **Typical value**                                | **Commonly used by**                |
| ----------------------- | ------------------------------------------------ | ----------------------------------- |
| `primaryEmail`          | `test.user.one@example.com`                      | Recommended for both SCIM and SAML  |
| Email aliases           | `testuser1@example.com`, `t.userone@example.com` | Sometimes mapped by mistake in SCIM |
| Custom schema fields    | Custom attributes defined per org                | Advanced attribute mappings         |
| Organization unit email | OU-derived address variants                      | Rarely, in complex org structures   |

The most common mismatch: SCIM is configured to send an alias address while SAML sends the primary email (or vice versa). Since aliases and primary emails are different strings, Claude cannot match them. Claude requires an **exact string match**.

**Common confusion:** In Google Admin, SCIM auto-provisioning settings and SAML attribute mapping are on separate tabs within the same app. Admins sometimes update one and miss the other. Verify both locations.

---

## Diagnostic steps

### Step 1 — Confirm the mismatch

1. **Check the SCIM email:** In the **Google Admin console**, go to **Apps → Web and mobile apps → [Claude app] → Auto-provisioning**. Check which attribute is mapped to the email field being sent to Claude.

2. **Check the SAML email:** In the same app, go to the **SAML attribute mapping** section. Find the attribute mapped to email and note its source.

3. **Check a specific person:** In **Directory → Users → [User]**, compare the **Primary email** with any listed **Alias emails**.

### Step 2 — Identify the scope of the problem

- If **most or all** provisioned people share the same email format mismatch, this is a **systemic attribute mapping problem**. The fix is in your IdP's SCIM attribute mapping.

- If only **one or two people** are affected, the issue is likely specific to those accounts. Check their profile directly.

### Step 3 — Check Name ID in SAML configuration

1. In the app settings, go to **SAML → Service provider details**.

2. Confirm that the **Name ID** is set to **Basic Information → Primary email**.

3. If Name ID is set to a custom schema field or alias, it may send a different value than SCIM.

---

## Resolution

### Align both mappings to primaryEmail

Google Workspace's primaryEmail is the most reliable source for both SCIM and SAML.

1. **Update SCIM provisioning:** In **Apps → Web and mobile apps → [Claude app] → Auto-provisioning → Attribute mapping**, ensure the email attribute maps to primaryEmail.

2. **Update SAML Name ID:** In **SAML → Service provider details**, set **Name ID** to **Basic Information → Primary email**.

3. **Update SAML attribute mapping:** In the **Attribute mapping** step, ensure the email attribute is mapped to **Basic Information → Primary email**.

4. Save all changes.

### Trigger a full re-sync

**Critical — Full sync required:** An incremental sync will *not* update existing records after you change an attribute mapping. You must trigger a **full restart** of the provisioning cycle.

1. In the Google Admin console, go to the app's **Auto-provisioning** settings.

2. Temporarily suspend provisioning, then re-enable it. This triggers a full sync of everyone assigned.

3. Alternatively, remove and re-add affected people from the app assignment to force their individual records to re-provision.

4. Monitor the provisioning logs for errors and confirm emails updated to match the SAML format before asking people to retry.

---

## Post-fix cleanup

After correcting the attribute mapping and completing the full sync:

- **Rogue free accounts:** If organization creation was not restricted before the fix, some people may have inadvertently created free personal Claude accounts. Contact **[our Support team](https://support.claude.com/en/articles/9015913)** to have these removed.

- **Ghost accounts (wrong-email seats):** The originally provisioned accounts with the incorrect email may still exist in your organization, occupying seats. Contact our Support team to deprovision these.

- **Seat availability:** If ghost accounts are occupying all contracted seats, new logins will fail with an out-of-seats error. Deprovisioning the ghost accounts frees those seats.

- **Re-adding affected people:** After ghost accounts are removed, people with the corrected email may need to be re-invited or re-provisioned.

- **Prevent future occurrences:** Enable "Restrict organization creation" in your organization's Identity and access settings. This prevents people who aren't yet provisioned from accidentally creating free personal accounts.

---

## Verification

1. Check a sample of provisioned people—confirm their email in the provisioning log matches the email format that SSO sends.

2. Ask an affected person to clear browser cookies for claude.ai, then log in via SSO. They should land directly in your organization's workspace without any error.

3. Confirm people aren't creating free accounts—with organization creation restricted, blocked people see a clear error rather than landing on a personal account.

4. If Claude Code was affected, have the person re-run `claude auth login --enterprise` and confirm the email matches their provisioned seat.

---

## Common issues

| **Issue**                                                                 | **Solution**                                                                                                           |
| ------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| SCIM sends an alias while SAML sends the primary email                    | Always use `primaryEmail` for both.                                                                                    |
| Name ID in SAML settings was not checked                                  | The Name ID field determines the email sent at login. This is separate from the attribute mapping section. Check both. |
| Custom schema field is blank for some people                              | Stick to standard Google attributes like `primaryEmail`.                                                               |
| Reprovisioning doesn't trigger automatically after mapping change         | You may need to manually suspend and re-enable provisioning to force a full sync.                                      |
| Someone's primary email changed but the old email still appears in Claude | A full re-sync is needed after primary email changes.                                                                  |
| Emails updated in SCIM but person still can't log in                      | Check for rogue free orgs or ghost accounts. Clear browser cookies and retry.                                          |

---

## When to contact Support

Contact **[our Support team](https://support.claude.com/en/articles/9015913)** with your organization's domain, the affected person's email, and screenshots of your attribute mappings when:

- SCIM and SSO attributes appear identical but people still cannot access their seats.

- You need confirmation of the email Claude recorded during SCIM provisioning for specific people.

- You need help cleaning up ghost accounts or rogue free orgs.

- People are hitting an out-of-seats error despite available contracted seats.