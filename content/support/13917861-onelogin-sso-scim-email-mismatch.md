# OneLogin SSO/SCIM email mismatch

Claude uses email as the primary identifier to match SSO logins to provisioned seats. In OneLogin, SCIM provisioning and SAML SSO are configured in separate tabs of the app and can reference different user profile fields, causing a mismatch that blocks access.

**Applies to:** Enterprise plans and Console organizations using SCIM provisioning. Team plans don't have SCIM provisioning, so this mismatch scenario doesn't apply—see **[Set up JIT or SCIM provisioning](https://support.claude.com/en/articles/13133195)** for what's available on each plan.

---

## Symptoms

People may experience one or more of the following when attempting to access your organization via SSO:

- **"Account creation is blocked"** — The person authenticates via SSO but Claude cannot find a matching provisioned account. If your organization has organization creation restricted (recommended), the person is blocked entirely.

- **Landing on a free personal account** — If organization creation is not restricted, the person bypasses your organization entirely and creates or lands on a free personal account instead of their provisioned seat.

- **"Please confirm your email" mismatch** — The SSO callback shows a different email than the one the person entered at login.

- **Claude Code authentication failure** — The Claude Code CLI shows an email mismatch error during the authentication flow.

---

## How this happens

OneLogin user profiles contain distinct fields for username and email, which may hold different values. SCIM provisioning parameters and SAML attribute statements are configured independently and can each pull from a different field:

| **OneLogin field** | **Typical value**                                         | **Commonly used by**                    |
| ------------------ | --------------------------------------------------------- | --------------------------------------- |
| `Username`         | `testuser1` or <testuser1@example.com>                    | Sometimes used in SCIM userName mapping |
| `Email`            | <test.user.one@example.com>                               | Recommended for both SCIM and SAML      |
| `Login Name`       | May differ from email if SSO is used for non-email logins | Legacy or custom configurations         |
| Custom user fields | Custom attributes defined per org                         | Advanced attribute mappings             |

A common mismatch: the SCIM parameters tab maps the email attribute to Username (which may be an employee ID or short name) while the SAML attribute statement sends the Email field. Claude requires an **exact string match**.

**Common confusion:** OneLogin's SCIM parameters and SAML attribute statements are in different tabs of the same app — **Parameters** for SCIM and **SSO** (or **Parameters** with SAML-specific fields) for SSO. Both must be checked and aligned.

---

## Diagnostic steps

## Step 1 — Confirm the mismatch

1. **Check the SCIM email:** In the OneLogin Admin portal, go to **Applications → [Claude app] → Parameters**. Find the field mapped to the email Claude receives. Note the **OneLogin value** column — this shows which user field is sent.

2. **Check the SAML email:** In the same app, go to the **SSO** tab. Click **More Actions → Edit SAML Response** or check the **SAML Attribute Statements** section. Find the attribute for email and note its source field.

3. **Check a specific person:** In **Users → [User]**, compare the **Username** and **Email** fields. If they differ, any mapping using one vs. the other will cause a mismatch.

## Step 2 — Identify the scope of the problem

- If **most or all** provisioned people share the same email format mismatch, this is a **systemic attribute mapping problem**. The fix is in your IdP's SCIM attribute mapping.

- If only **one or two people** are affected, the issue is likely specific to those accounts. Check their profile directly.

## Step 3 — Review user field values

1. Go to **Users → [Affected User] → User Info**.

2. Check both the **Username** and **Email** fields.

3. If Username is in a format that doesn't match a valid email, SCIM may be sending an invalid or non-matching value.

---

## Resolution

## Align both mappings to the Email field

OneLogin's Email field is the most reliable source for both SCIM and SAML, as it's designed to hold a valid email address.

1. **Update SCIM parameter:** In **Applications → [Claude app] → Parameters**, find the row for the email attribute Claude receives. Change the **Value** to **Email** (the OneLogin Email field).

2. **Update SAML attribute statement:** In the **SSO** tab (or **Parameters** for SAML attributes), update the email attribute value to use the same **Email** field.

3. Click "Save."

## Trigger a full re-sync

**Critical — Full sync required:** An incremental sync will *not* update existing records after you change an attribute mapping. You must trigger a **full restart** of the provisioning cycle.

1. In the app's **Provisioning** tab, look for a **Re-sync** or **Sync All** option and run it.

2. To reprovision individual people: Go to **Users → [User] → Applications**, find the Claude app, and use **Re-provision**.

3. Check the OneLogin provisioning activity log for errors.

4. Verify updated email values appear in the log before asking people to retry login.

---

## Post-fix cleanup

After correcting the attribute mapping and completing the full sync:

- **Rogue free accounts:** If organization creation was not restricted before the fix, some people may have inadvertently created free personal Claude accounts. Contact **[our Support team](https://support.claude.com/en/articles/9015913)** to have these removed.

- **Ghost accounts (wrong-email seats):** The originally provisioned accounts with the incorrect email may still exist in your organization, occupying seats that can never be used. Contact our Support team to deprovision these.

- **Seat availability:** If ghost accounts are occupying all contracted seats, new logins will fail with an out-of-seats error even after the mapping is fixed.

- **Re-adding affected people:** After ghost accounts are removed, people with the corrected email may need to be re-invited or re-provisioned.

- **Prevent future occurrences:** Enable "Restrict organization creation" in your organization's Identity and access settings.

---

## Verification

1. Check a sample of provisioned people—confirm their email in the provisioning log matches the email format that SSO sends.

2. Ask an affected person to clear browser cookies for claude.ai, then log in via SSO.

3. Confirm people aren't creating free accounts.

4. If Claude Code was affected, have the person re-run `claude auth login --enterprise` and confirm the email matches their provisioned seat.

---

## Common issues

| **Issue**                                                      | **Solution**                                                                                  |
| -------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| Username field holds a short name or employee ID, not an email | Switch SCIM to use the **Email** field.                                                       |
| SAML attributes updated but SCIM parameters were not changed   | Both the Parameters tab (for SCIM) and the SSO/SAML attributes must be updated independently. |
| Re-sync doesn't appear to trigger                              | Try removing and re-assigning affected people from the app.                                   |
| Custom user fields are mapped but blank for some people        | Switch to the standard **Email** field.                                                       |
| Emails updated in SCIM but person still can't log in           | Check for rogue free orgs or ghost accounts. Clear browser cookies and retry.                 |
| "Invite domain not allowed" when trying to re-add people       | Your organization's domain may not be verified in Claude. Contact Support.                    |

---

## When to contact Support

Contact **[our Support team](https://support.claude.com/en/articles/9015913)** with your organization's domain, the affected person's email, and screenshots of your attribute mappings when:

- SCIM and SSO attributes appear identical but people still cannot access their seats.

- You need confirmation of the email Claude recorded during SCIM provisioning for specific people.

- You need help cleaning up ghost accounts or rogue free orgs.

- People are hitting an out-of-seats error despite available contracted seats.