# Ping Identity SSO/SCIM email mismatch

Claude uses email as the primary identifier to match SSO logins to provisioned seats. Ping Identity products (PingOne and PingFederate) have flexible, layered attribute configuration. When SCIM provisioning and SAML/OIDC SSO pull from different user attributes, a mismatch blocks access.

**Applies to:** Enterprise plans and Console organizations using SCIM provisioning. Team plans don't have SCIM provisioning, so this mismatch scenario doesn't apply—see **[Set up JIT or SCIM provisioning](https://support.claude.com/en/articles/13133195)** for what's available on each plan.

---

## Symptoms

People may experience one or more of the following when attempting to access your organization via SSO:

- **"Account creation is blocked"** — The person authenticates via SSO but Claude cannot find a matching provisioned account.

- **Landing on a free personal account** — If organization creation is not restricted, the person bypasses your organization entirely.

- **"Please confirm your email" mismatch** — The SSO callback shows a different email than the one the person entered at login.

- **Claude Code authentication failure** — The Claude Code CLI shows an email mismatch error during the authentication flow.

---

## How this happens

Ping Identity products allow granular attribute mapping at multiple levels (directory, IdP adapter, SP connector, application). SCIM and SSO can each traverse different paths through these layers, resulting in different email values reaching Claude:

| **Ping attribute**                   | **Typical value**                              | **Commonly used by**                            |
| ------------------------------------ | ---------------------------------------------- | ----------------------------------------------- |
| `email` (PingOne)                    | `test.user.one@example.com`                    | Recommended for both SCIM and SAML/OIDC         |
| `username` (PingOne)                 | `testuser1` or `testuser1@example.com`         | Default login identifier; may differ from email |
| IdP adapter attribute (PingFederate) | Varies by adapter type (LDAP, HTML Form, etc.) | PingFederate identity sources                   |
| LDAP `mail` attribute                | `test.user.one@example.com`                    | Directory-sourced email in PingFederate         |
| LDAP `sAMAccountName` or uid         | May be employee ID or short username           | Sometimes mapped to email by mistake            |
| Custom population attributes         | Custom fields defined per environment          | Advanced PingOne configurations                 |

Claude requires an exact string match between the SCIM-provisioned email and the SSO-asserted email.

**PingFederate note:** PingFederate's attribute contract system is especially complex—email can pass through multiple layers (LDAP → IdP adapter → adapter contract → SP connector → assertion). A mismatch at any layer will cause the wrong value to reach Claude. Trace the value end-to-end.

---

## Diagnostic steps

### Step 1 — Confirm the mismatch (PingOne)

1. **Check SCIM attribute mapping:** In PingOne Admin, go to **Connections → Applications → [Claude app] → Attribute Mappings**. Find the attribute mapped to emails[primary].value or email. Note the PingOne user attribute used as the source.

2. **Check SSO attribute mapping:** In the same app, go to the **SAML** or **OIDC** tab and find the attribute or claim mapped to email. Note its source attribute.

3. If SCIM and SSO reference different PingOne attributes, you've confirmed the mismatch.

### Step 1 (alternate) — Confirm the mismatch (PingFederate)

1. In the PingFederate Admin console, locate the **SP Connection** for Claude.

2. In **Attribute Contract Fulfillment**, find the email attribute and trace its source back to the IdP adapter or LDAP data store.

3. Separately, check the SCIM provisioning connector or outbound provisioning channel for Claude and trace the source of the email attribute being sent.

4. If the two traces lead to different directory attributes, you've confirmed the mismatch.

### Step 2 — Identify the scope of the problem

- If **most or all** provisioned people share the same email format mismatch, this is a **systemic attribute mapping problem**. The fix is in your IdP's SCIM attribute mapping.

- If only **one or two people** are affected, the issue is likely specific to those accounts. Check their profile directly.

### Step 3 — Check attribute values for a specific person

1. **PingOne:** Go to **Identities → Users → [User]** and compare the Username and Email field values.

2. **PingFederate with LDAP:** Check the person's LDAP record and compare mail, userPrincipalName, sAMAccountName, and any other attributes being used in your adapter mapping.

---

## Resolution

### PingOne — Align both mappings to the email attribute

1. In **Connections → Applications → [Claude app]**, open **Attribute Mappings**.

2. For SCIM: Ensure emails[primary].value maps to PingOne's **Email Address** attribute.

3. For SAML/OIDC: Ensure the email attribute or claim also maps to PingOne's **Email Address** attribute.

4. Save changes.

### PingFederate — Align attribute contract across all layers

1. In the SP Connection for Claude, go to **Attribute Contract Fulfillment**.

2. Find the email attribute. Ensure its source is the same LDAP or data store attribute used in your SCIM outbound provisioning channel.

3. If using a custom IdP adapter, ensure the adapter's contract includes the canonical email attribute and that it's correctly mapped through to the SP connection.

4. Update SCIM provisioning to use the same source attribute.

### Trigger a full re-sync

**Critical — Full sync required:** An incremental sync will not update existing records after you change an attribute mapping. You must trigger a **full restart** of the provisioning cycle.

1. **PingOne:** In the app's provisioning settings, trigger a full provisioning cycle. You may need to disable and re-enable provisioning to force a complete re-push.

2. **PingFederate:** Trigger a full sync in your outbound provisioning channel. Check your provisioning logs to confirm the updated email values are being sent.

3. Verify that updated email values appear in provisioning logs before asking people to retry login.

---

## Post-fix cleanup

After correcting the attribute mapping and completing the full sync:

- **Rogue free accounts:** If organization creation was not restricted before the fix, some people may have inadvertently created free personal Claude accounts. Contact **[our Support team](https://support.claude.com/en/articles/9015913-how-to-get-support)** to have these removed.

- **Ghost accounts (wrong-email seats):** Contact our Support team to deprovision these.

- **Seat availability:** If ghost accounts are occupying all contracted seats, new logins will fail. Contact our Support team.

- **Re-adding affected people:** After ghost accounts are removed, people may need to be re-invited or re-provisioned.

- **Prevent future occurrences:** Enable "Restrict organization creation" in your organization's Identity and access settings.

---

## Verification

1. Check a sample of provisioned people—confirm their email in the provisioning log matches the email format that SSO sends.

2. Ask an affected person to clear browser cookies for claude.ai, then log in via SSO.

3. Confirm people aren't creating free accounts.

4. If Claude Code was affected, have the person re-run `claude auth login --enterprise` and confirm the email matches their provisioned seat.

---

## Common issues

| **Issue**                                                                 | **Solution**                                                                                                   |
| ------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| PingOne `username` field used instead of `email`                          | Switch the SCIM mapping to PingOne's **Email Address** attribute.                                              |
| PingFederate attribute mismatch across contract layers                    | Trace the email attribute end-to-end: LDAP source → IdP adapter → adapter contract → SP connector → assertion. |
| LDAP `sAMAccountName` or `uid` mapped as email source                     | Use the LDAP `mail` attribute instead.                                                                         |
| Incremental provisioning sync doesn't update existing records             | A full re-sync is required after changing attribute mappings.                                                  |
| Attribute contract updated in PingFederate but SCIM connector not updated | Both SP connection and outbound SCIM provisioning channel must be updated independently.                       |
| Emails updated in SCIM but person still can't log in                      | Check for rogue free orgs or ghost accounts. Clear browser cookies and retry.                                  |

---

## **When to contact Support**

Contact **[our Support team](https://support.claude.com/en/articles/9015913-how-to-get-support)** with your organization's domain, the affected person's email, and screenshots of your attribute mappings when:

- SCIM and SSO attributes appear identical but people still cannot access their seats.

- You need confirmation of the email Claude recorded during SCIM provisioning for specific people.

- You need help cleaning up ghost accounts or rogue free orgs.

- People are hitting an out-of-seats error despite available contracted seats.