# Okta SSO/SCIM email mismatch

Claude uses email as the primary identifier to match SSO logins to provisioned seats. In Okta, SCIM provisioning and SSO are configured separately and can pull email from different user profile fields. This guide explains how to identify and resolve the mismatch.

**Applies to:** Enterprise plans and Console organizations using SCIM provisioning. Team plans don't have SCIM provisioning, so this mismatch scenario doesn't apply—see **[Set up JIT or SCIM provisioning](https://support.claude.com/en/articles/13133195)** for what's available on each plan.

---

## Symptoms

People may experience one or more of the following when attempting to access your organization via SSO:

- **"Account creation is blocked"** — SSO authentication succeeds but Claude cannot locate a matching provisioned account. If your organization has organization creation restricted (recommended), the person is blocked entirely.

- **Landing on a free personal account** — If organization creation is not restricted, the person bypasses your organization entirely and creates or lands on a free personal account instead of their provisioned seat.

- **"Please confirm your email" mismatch** — The SSO callback shows a different email than the one the person entered at login.

- **Claude Code authentication failure** — The Claude Code CLI shows an email mismatch error during the authentication flow.

---

## How this happens

Okta user profiles contain multiple fields that represent identity. SCIM provisioning (under **Provisioning → To App**) and SAML/OIDC SSO (under **Sign On**) are configured independently.

| **Okta attribute** | **Typical value**                      | **Commonly used by**                            |
| ------------------ | -------------------------------------- | ----------------------------------------------- |
| `user.login`       | `testuser1` or <testuser1@example.com> | Default SCIM userName mapping; sometimes NameID |
| `user.email`       | <test.user.one@example.com>            | SAML/OIDC email claim (recommended)             |
| `appuser.email`    | App-level override of user email       | Custom app-level attribute mapping              |

A common mismatch: SCIM uses `user.login` while SAML sends `user.email`. Claude requires an exact string match.

**Common confusion:** Okta's SCIM attribute mappings and SAML attribute statements live in two different tabs — **Provisioning → To App** for SCIM, and **Sign On** for SSO.

---

## Diagnostic steps

### Step 1 — Confirm the mismatch

1. **Check SCIM email:** Navigate to **Applications → [Claude App] → Provisioning → To App → Attribute Mappings**. Locate the `email` (or `userName`) row. The **Value** column shows the Okta expression being sent.

2. **Check SSO email (SAML):** Go to **Applications → [Claude App] → Sign On → SAML Settings → Edit → Attribute Statements**. Find the `email` attribute. The **Value** column indicates which Okta field is asserted.

3. **Check SSO email (OIDC):** Go to **Applications → [Claude App] → Sign On → OpenID Connect ID Token** and review the **Claims** section for email.

4. If SCIM and SSO values reference different Okta fields, the mismatch is confirmed.

### Step 2 — Identify the scope of the problem

- **Most or all provisioned people affected:** This is a systemic attribute mapping problem. The fix is in your IdP's SCIM attribute mapping.

- **One or two people affected:** The issue is specific to those accounts. Check their user profile directly.

### Step 3 — Verify Okta user profiles directly

1. Go to **Directory → People → [User] → Profile**.

2. Compare the Login and Email field values. Differences between these fields will produce mapping mismatches.

---

## Resolution

### Align both mappings to the same Okta field

The safest fix is to use `user.email` for both SCIM and SSO, as this field contains the canonical email address in Okta.

1. **Update SCIM mapping:** In **Provisioning → To App → Attribute Mappings**, change the `email` (or `userName`) source to `user.email`.

2. **Update SSO claim (SAML):** In **Sign On → SAML Settings → Attribute Statements**, change the email attribute value to user.email.

3. **Update SSO claim (OIDC):** In **Sign On → OpenID Connect ID Token → Claims**, update the email claim to map to `user.email`.

4. Click “Save.”

### Force a full re-sync

**Critical — Full sync required:** An incremental sync will not update existing records after you change an attribute mapping.

1. In **Provisioning → To App**, click “Force Sync” to trigger a full re-evaluation of everyone assigned.

2. Alternatively, for specific people: **Provisioning → Push Users → select affected people → Push Now**.

3. Check Okta System Log (**Reports → System Log**) for provisioning errors.

4. Verify updated email values appear in provisioning logs before people retry login.

---

## Post-fix cleanup

After correcting the attribute mapping and completing the full sync:

- **Rogue free accounts:** If organization creation wasn't restricted before the fix, some people may have created free personal Claude accounts. Contact **[our Support team](https://support.claude.com/en/articles/9015913)** for removal.

- **Ghost accounts (wrong-email seats):** The originally provisioned accounts with the incorrect email may still exist in your organization, occupying seats that can never be used. Contact our Support team for deprovisioning.

- **Seat availability:** If ghost accounts are occupying all contracted seats, new logins will fail with an out-of-seats error even after the mapping is fixed.

- **Re-adding affected people:** After ghost account removal, people with the corrected email may need to be re-invited or re-provisioned.

- **Prevent future occurrences:** Enable "Restrict organization creation" in your organization's Identity and access settings to prevent unprovisioned people from creating free accounts.

---

## Verification

After completing the fix and any cleanup:

1. Check a sample of provisioned people—confirm their email in the provisioning log matches the email format that SSO sends.

2. Ask an affected person to clear browser cookies for claude.ai, then log in via SSO. They should land directly in your organization's workspace without error.

3. Confirm people aren't creating free accounts—with organization creation restricted, blocked people see a clear error instead of landing on a personal account.

4. If Claude Code was affected, have the person re-run `claude auth login --enterprise` and confirm the email matches their provisioned seat.

---

## Common issues

| **Issue**                                                                              | **Solution**                                                                                                        |
| -------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| Admin updates SAML claims but forgets SCIM attribute mappings (or vice versa)          | Both must be updated. SCIM mappings under **Provisioning → To App**; SAML claims under **Sign On → SAML Settings**. |
| `user.login` contains a username (not email) for some people                           | Switch both to `user.email` and verify email fields are populated for everyone.                                     |
| Incremental sync runs but emails don't update                                          | **Force Sync** or **Push Users** is required after an attribute mapping change.                                     |
| App-level profile attribute (`appuser.email`) differs from user profile (`user.email`) | Check if app-level attribute mappings override user profile values.                                                 |
| Emails updated but person still can't log in                                           | Look for rogue free orgs or ghost accounts. Clear browser cookies and retry. Contact Support if it persists.        |
| OIDC and SAML apps are separate Okta apps for Claude                                   | Some organizations configure both. Ensure attribute alignment in both apps.                                         |

---

## When to contact Support

Contact **[our Support team](https://support.claude.com/en/articles/9015913)** with your organization's domain, the affected person's email, and attribute mapping screenshots when:

- SCIM and SSO attributes appear identical but people still cannot access their seats.

- You need confirmation of the email Claude recorded during SCIM provisioning for specific people.

- You need help cleaning up ghost accounts or rogue free organizations.

- People are hitting an out-of-seats error despite available contracted seats.