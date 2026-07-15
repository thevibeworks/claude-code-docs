# Microsoft Entra ID SSO/SCIM email mismatch

Claude uses email as the primary identifier to match SSO logins to provisioned seats. In Microsoft Entra ID, SCIM provisioning and SSO authentication are configured in *separate places* and can pull email from different user attributes—causing a mismatch that blocks access. This guide walks through how to identify the problem, fix the attribute mapping, and clean up any side effects.

**Applies to:** Enterprise plans and Console organizations using SCIM provisioning. Team plans don't have SCIM provisioning, so this mismatch scenario doesn't apply — see **[Set up JIT or SCIM provisioning](https://support.claude.com/en/articles/13133195)** for what's available on each plan.

---

## Symptoms

People may experience one or more of the following when attempting to access your organization via SSO:

- **"Account creation is blocked"** — The person authenticates via SSO but Claude cannot find a matching provisioned account. If organization creation is restricted (recommended), the person is blocked entirely.

- **Landing on a free personal account** — If organization creation is not restricted, the person bypasses your organization and creates or lands on a free personal account.

- **"Please confirm your email" mismatch** — The SSO callback shows a different email than the one the person entered at login.

- **Claude Code authentication failure** — The Claude Code CLI shows an email mismatch error during the authentication flow.

---

## How this happens

Microsoft Entra ID user accounts have multiple email-like attributes that can hold *different values*. SCIM provisioning and SSO authentication are configured in separate admin areas and each can pull from a different attribute:

| **Entra attribute** | **Typical value**                                   | **Commonly used by**            |
| ------------------- | --------------------------------------------------- | ------------------------------- |
| `userPrincipalName` | `testuser1@example.com` (may be employee ID format) | Default SCIM userName mapping   |
| `mail`              | `test.user.one@example.com` (standard email)        | OIDC / SAML email claim         |
| `proxyAddresses`    | `SMTP:test.user.one@example.com`                    | Exchange / M365 primary address |
| `otherMails`        | May contain aliases or secondary addresses          | Alternative contact emails      |

The mismatch occurs when SCIM pulls email from one attribute while SSO sends the email from another. Even a subtle difference blocks access—Claude requires an **exact string match**.

**Common confusion:** Entra has two separate admin areas. The **SCIM provisioning app** lives under **Enterprise applications** (Microsoft's term for integrated apps—unrelated to your Claude plan). The **SSO/OIDC app** lives under **App registrations**. IT admins frequently navigate to the wrong location.

---

## Diagnostic steps

### Step 1 — Confirm the mismatch

1. **Check the SCIM email:** In Entra Admin Center → **Enterprise applications → [Claude SCIM app] → Provisioning → Provisioning logs**, find a recently provisioned person and inspect **Modified attributes**. The value mapped to emails[type eq "work"].value is what SCIM sent to Claude.

2. **Check the SSO email:** In **Enterprise applications → [Claude app] → Single sign-on → Attributes & Claims**, find the email claim. For OIDC apps, check **App registrations → [Claude app] → Token configuration**.

3. If the two source attributes point to **different fields**, you've confirmed the mismatch.

### Step 2 — Identify the scope

- If **most or all** provisioned people share the same format mismatch, this is a **systemic attribute mapping problem**. The fix is in the SCIM attribute mapping config.

- If only **one or two people** are affected, check their user profile directly in Entra.

### Step 3 — Check the OIDC token claims (OIDC apps only)

1. In Entra Admin Center, go to **App registrations** (not Enterprise applications).

2. Find the Claude OIDC app and click "Token configuration."

3. Check the email optional claim.

4. Cross-reference with your SCIM attribute mapping to confirm whether they match.

---

## Resolution

### Fix the SCIM attribute mapping

Navigate to the **SCIM provisioning app** — not the SSO/OIDC app:

1. Go to **Entra Admin Center → Enterprise applications**.

2. Search for the Claude SCIM app. Look for the app with a **Provisioning** section.

3. Click **Provisioning → Edit provisioning → Attribute mappings**.

4. Find the row where the SCIM attribute is emails[type eq "work"].value. Click it to edit.

5. Change the **Source attribute** to match what SSO sends — typically mail.

6. Also check the userName mapping and update if needed.

7. Click "Save."

### Trigger a full provisioning sync

**Full sync required — incremental won't work.** You must trigger a **full restart** of the provisioning cycle.

1. Go to the **Provisioning** overview page.

2. Click **Restart provisioning**.

3. Wait for the sync to complete.

4. Verify in provisioning logs that emails have updated to the correct format.

---

## Post-fix cleanup

After correcting the attribute mapping and completing the full sync:

- **Rogue free accounts:** If organization creation wasn't restricted before the fix, some people may have created free personal Claude accounts. Contact **[our Support team](https://support.claude.com/en/articles/9015913-how-to-get-support)** for removal.

- **Ghost accounts (wrong-email seats):** The originally provisioned accounts with the incorrect email may still exist in your organization, occupying seats that can never be used. Contact our Support team to deprovision these.

- **Seat availability:** If ghost accounts are occupying all contracted seats, new logins will fail with an out-of-seats error even after the mapping is fixed.

- **Re-adding affected people:** After ghost accounts are removed, people with the corrected email may need to be re-invited or re-provisioned.

- **Prevent future occurrences:** Enable "Restrict organization creation" in your organization's Identity and access settings.

---

## Verification

1. Check a sample of provisioned people—confirm their email in the provisioning log matches the email format that SSO sends.

2. Ask an affected person to clear browser cookies for claude.ai, then log in via SSO. They should land directly in your organization's workspace.

3. Confirm people aren't creating free accounts—with organization creation restricted, blocked people see a clear error instead of landing on a personal account.

4. If Claude Code was affected, have the person re-run `claude auth login --enterprise` and confirm the email matches their provisioned seat.

---

## Common issues

| **Issue**                                                      | **Solution**                                                                                                                                                                           |
| -------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SCIM mapping updated but SSO claim not checked (or vice versa) | Both must be updated. SCIM under **Enterprise applications → Provisioning**; SSO claims under **Single sign-on → Attributes & Claims** or **App registrations → Token configuration**. |
| userPrincipalName is in employee-ID format, not a real email   | Switch SCIM to use the mail attribute instead.                                                                                                                                         |
| Incremental sync runs but emails don't update                  | **Restart provisioning** is required after an attribute mapping change.                                                                                                                |
| OIDC app email claim not configured as an optional claim       | Add email under **App registrations → Token configuration**.                                                                                                                           |
| Emails updated but person still can't log in                   | Look for rogue free orgs or ghost accounts. Clear browser cookies and retry.                                                                                                           |

---

## When to contact Support

Contact **[our Support team](https://support.claude.com/en/articles/9015913)** with your organization's domain, the affected person's email, and attribute mapping screenshots when:

- SCIM and SSO attributes appear identical but people still cannot access their seats.

- You need confirmation of the email Claude recorded during SCIM provisioning for specific people.

- You need help cleaning up ghost accounts or rogue free orgs.

- People are hitting an out-of-seats error despite available contracted seats.