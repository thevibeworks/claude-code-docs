# Cyber Verification Program Security Requirements

Customer must meet and maintain the following security requirements for each Cyber Verification Program access level that Customer holds (“**Access Level**”). These requirements apply to Approved Users and to Granted Workspaces.

## 1. All Access Levels.

1. **Security Contact.** Customer must provide Anthropic with a named security contact who may receive security and misuse alerts and is able to act on them.

2. **Incident Reporting.** Customer must report suspected breaches or misuse involving the grant to Anthropic within 72 hours, or within 24 hours for a security incident. Reporting can be done at <security@anthropic.com> or your Account team contact.

3. **Cooperation.** Customer must investigate any abuse that Anthropic identifies within 48 hours, work with Anthropic to remediate it, and respond to misuse inquiries within seven (7) days.

4. **Personal Access.** Each Approved User must sign in as themselves. Shared sign-ins, seats, sessions, and workload identities, and browser extensions or proxy tools that expose a session to other people that are not explicitly an Approved User meeting all the requirements below, are not permitted.

5. **Usage Attribution.** User profiles must remain enabled on the Granted Workspace so that requests can be attributed to a named user or workload identity.

6. **Notice of Changes.** Customer must notify Anthropic within thirty (30) days of a material change to its security posture, ownership, headquarters, or security contact.

7. **Ongoing Review.** Anthropic may request that Customer provide evidence of compliance with these Cyber Verification Program Security Requirements.

## 2. Defense Access.

1. **Multi-Factor Authentication.** At the time of Customer’s access to the CVP, all accounts that can sign in to the Granted Workspace, or hold credentials for it, must have multi-factor authentication enabled. By December 15, 2026 (the "Cutoff Date"), all such accounts must use phishing-resistant multi-factor authentication as defined in the CISA fact sheet "Implementing Phishing-Resistant MFA" and with NIST SP 800-63B-4, meaning (i) a FIDO2/WebAuthn security key, (ii) a passkey, on the device or in a password manager, or (iii) a smartcard/PIV, and email magic-link sign-in must be disabled. SMS, voice, emailed codes, authenticator-app codes, and push approvals do not qualify.

2. **Credential Management.** By the Cutoff Date, downloaded, exported, or otherwise long-lived static credentials, including API keys, must not be used to access the model. The following requirements apply to Customer based on the deployment platform(s) through which Customer accesses the model. For each applicable platform, all Approved Users and all workloads must authenticate using short-lived credentials issued and managed by that platform's native identity service.

  1. **Anthropic (first-party API and Console).** Static or long-lived API keys are not permitted, including for interactive access to Claude Console, Claude for Enterprise, Claude Code, and other Anthropic application surfaces.

  2. **Google Vertex.** Downloaded service account JSON key files are not permitted.

  3. **Amazon Web Services (Amazon Bedrock).** IAM user access key pairs (access key ID and secret access key) are not permitted, with the exception of short-term Bedrock API keys that expire within 12 hours or the length of the Bedrock session, whichever is shorter.

  4. **Microsoft Azure (Azure AI Foundry).** API keys and exported service principal client secrets or certificates are not permitted.

3. **Interim API Keys.** Until the Cutoff Date, API keys are permitted under a Defense Access grant only if each key is (i) stored in a secrets manager or password manager, (ii) assigned to a single person or workload, (iii) kept out of source code, and (iv) replaced at least every 7 days. Anthropic may limit the lifetime of API keys under a Defense Access grant to 7 days, and may disable API keys on the Granted Workspace from the Cutoff Date.

4. **Approved Users.** There is no default limit on the number of Approved Users at this Access Level.

## 3. Defense Access for Individuals.

1. Individuals are eligible for Defense Access only. Where the grant is held by an individual this section applies

  1. **Multi-Factor Authentication.** The individual must sign in to the Anthropic account that holds the grant only through Google or an equivalent identity provider. From the date access is granted, that account must have multi-factor authentication enabled. By December 15, 2026 (the "Cutoff Date"), that account must use phishing-resistant multi-factor authentication, meaning a security key, a passkey, or a smartcard/PIV, and the individual must not use email magic-link sign-in. SMS, voice, emailed codes, authenticator-app codes, and push approvals do not qualify.

  2. **Credential Management.** By the Cutoff Date, static or long-lived credentials, including API keys, must not be used to access the model. Claude Code, Claude Console, and claude.ai authenticate through OAuth. Programmatic access for workloads, where offered, must use Workload Identity Federation. Until the Cutoff Date, one API key is permitted only if it is (i) stored in a password manager or local secrets store, (ii) never shared or placed in source code, and (iii) replaced at least every 7 days. Anthropic may limit the lifetime of API keys under the grant to 7 days, and may disable API keys from the Cutoff Date.

  3. **Personal Access.** The individual is the only person who may use the access. Shared sign-ins or sessions, and browser extensions or proxy tools that expose the session to others, are not permitted.

  4. **Monitoring.** All traffic under the grant is retained and monitored. Zero data retention is not available.

  5. Of the All Access Levels requirements, Incident Reporting, Cooperation, and Ongoing Review apply to an individual.

## 4. Red Team Access.

1. **Credential Management.** The following requirements apply to Customer based on the deployment platform(s) through which Customer accesses the model. For each applicable platform, all Approved Users and all workloads must authenticate using short-lived credentials issued and managed by that platform's native identity service.

  1. **Anthropic (first-party API and Console).** Static or long-lived API keys are not permitted, including for interactive access to Claude Console, Claude for Enterprise, Claude Code, and other Anthropic application surfaces.

  2. **Google Vertex.** Downloaded service account JSON key files are not permitted.

  3. **Amazon Web Services (Amazon Bedrock).** IAM user access key pairs (access key ID and secret access key) are not permitted, with the exception of short-term Bedrock API keys that expire within 12 hours or the length of the Bedrock session, whichever is shorter.

  4. **Microsoft Azure (Azure AI Foundry).** API keys and exported service principal client secrets or certificates are not permitted.

2. **Multi-Factor Authentication.** At the time of Customer’s access to the CVP, phishing-resistant multi-factor authentication must protect (i) all accounts that can sign in to the Granted Workspace or hold credentials for it, (ii) Approved Users' accounts at Customer's identity provider, (iii) AWS, Google Cloud, or Azure identities that can call the model, (iv) administrative access to anything that issues or stores model credentials, and (v) any virtual desktop or enclave used to meet these requirements. Phishing-resistant multi-factor authentication means (i) a FIDO2/WebAuthn security key, (ii) a passkey, on the device or in a password manager, or (iii) a smartcard/PIV, consistent with the CISA fact sheet "Implementing Phishing-Resistant MFA" and NIST SP 800-63B-4. SMS, voice, emailed codes, authenticator-app codes, and push approvals do not qualify, and email magic-link sign-in must be disabled.

3. **Organization Accounts.** Approved Users must sign in with accounts on Customer's domain. Personal and webmail accounts are not permitted.

4. **Approved Users.** The Granted Workspace is limited to twenty-five (25) Approved Users who personally perform or directly supervise the work for which the grant was approved. Workload identities do not count toward that number. Customer may request additional Approved Users seats in writing (email sufficing). Only named administrators may add members, change roles, or create workload identities or credentials on the Granted Workspace.

5. **Gateways.** If Customer operates a gateway or proxy in front of the model, it must admit only Approved Users or their workload identities, use a short-lived credential of its own, and keep its logs and transcripts restricted to Approved Users and Customer's security, IT-administration, or trust-and-safety teams.

6. **Customer-Operated Credential Systems.** Credentials issued by Customer's own systems must expire within 12 hours, must be issued only after phishing-resistant multi-factor authentication (for people) or a verified workload identity (for services), and must leave no static credential on endpoints, in source code, or in shared stores. The keys and secrets that can issue model credentials must be kept in a secrets manager or key management service with access logging.

7. **Revocation.** Customer must be able to revoke any compromised credential or identity within 24 hours.

8. **Offboarding.** Customer must remove departed or reassigned Approved Users, and their workload identities, from the Granted Workspace within three (3) business days.

9. **Network Egress.** Wherever the model performs offensive or agentic work, outbound traffic must be limited to an allow-list enforced off the host, and must be logged. Workstations used only for interactive prompting may use an on-host allow-list if the agentic work itself runs in a sandbox that cannot change that list.

10. **Managed Devices.** Approved Users must reach the Granted Workspace only from devices that Customer controls that receive automatic or regularly scheduled operating-system updates, not personal devices.

11. **Background Checks.** Every Approved User, including contractors, must have passed an identity check and, where lawful, a criminal-history check. Where local law restricts criminal checks, identity, right-to-work, or employment verification is accepted. Government vetting or a clearance satisfies this requirement.

12. **Incident Procedure.** Customer must maintain a documented procedure for suspected compromise or misuse of the grant that covers credential revocation and seat suspension.

13. **Government Entities.** A FISMA Authority to Operate with an annual independent Inspector General assessment against NIST SP 800-53, or an equivalent national scheme, satisfies the Managed Devices, Background Checks, and Incident Procedure requirements. All other requirements continue to apply.

## 5. Specialized Access.

1. **Multi-Factor Authentication.** At the time of Customer’s access to the CVP, phishing-resistant multi-factor authentication must protect (i) all accounts that can sign in to the Granted Workspace or hold credentials for it, (ii) Approved Users' accounts at Customer's identity provider, (iii) AWS, Google Cloud, or Azure identities that can call the model, (iv) administrative access to anything that issues or stores model credentials, and (v) any virtual desktop or enclave used to meet these requirements. Phishing-resistant multi-factor authentication means (i) a FIDO2/WebAuthn security key, (ii) a passkey, on the device or in a password manager, or (iii) a smartcard/PIV, consistent with the CISA fact sheet "Implementing Phishing-Resistant MFA" and NIST SP 800-63B-4. SMS, voice, emailed codes, authenticator-app codes, and push approvals do not qualify, and email magic-link sign-in must be disabled.

2. **Credential Management.** The following requirements apply to Customer based on the deployment platform(s) through which Customer accesses the model. For each applicable platform, all Approved Users and all workloads must authenticate using short-lived credentials issued and managed by that platform's native identity service.

  1. **Anthropic (first-party API and Console).** Static or long-lived API keys are not permitted, including for interactive access to Claude Console, Claude for Enterprise, Claude Code, and other Anthropic application surfaces.

  2. **Google Vertex.** Downloaded service account JSON key files are not permitted.

  3. **Amazon Web Services (Amazon Bedrock).** IAM user access key pairs (access key ID and secret access key) are not permitted, with the exception of short-term Bedrock API keys that expire within 12 hours or the length of the Bedrock session, whichever is shorter.

  4. **Microsoft Azure (Azure AI Foundry).** API keys and exported service principal client secrets or certificates are not permitted.

3. **Single Sign-On and Organization Accounts.** Approved Users must sign in with accounts on Customer's own domain. Approved Users must sign in with organization-domain identities federated through Customer's single sign-on. Personal, webmail, and non-federated accounts are not permitted.

4. **Approved Users.** The Granted Workspace is limited to 25 Approved Users who personally perform or directly supervise the work for which the grant was approved. Workload identities do not count toward that number. Customer may request additional Approved Users seats in writing (email sufficing). Only named administrators may add members, change roles, or create workload identities or credentials on the Granted Workspace.

5. **Gateways.** If Customer operates a gateway or proxy in front of the model, it must admit only Approved Users or their workload identities, use a short-lived credential of its own, and keep its logs and transcripts restricted to Approved Users and Customer's security, IT-administration, or trust-and-safety teams.

6. **Customer-Operated Credential Systems.** Credentials issued by Customer's own systems must expire within 12 hours, must be issued only after phishing-resistant multi-factor authentication (for people) or a verified workload identity (for services), and must leave no static credential on endpoints, in source code, or in shared stores. The keys and secrets that can issue model credentials must be kept in a secrets manager or key management service with access logging.

7. **Revocation.** Customer must be able to revoke any compromised credential or identity within 24 hours.

8. **Offboarding.** Customer must remove departed or reassigned Approved Users, and their workload identities, from the Granted Workspace within 3 business days.

9. **Network Egress.** Wherever the model performs offensive or agentic work, outbound traffic must be limited to an allow-list enforced off the host, and must be logged. Workstations used only for interactive prompting may use an on-host allow-list if the agentic work itself runs in a sandbox that cannot change that list.

10. **Managed Devices and Malware Protection.** Approved Users must reach the Granted Workspace only from devices that Customer controls, not personal devices, and that receive automatic or regularly scheduled operating-system updates. Every device an Approved User uses to reach the Granted Workspace must be managed by Customer and must run application allow-listing or deny-listing in enforce mode, or an endpoint detection and response agent in block or prevent mode. A managed virtual desktop or enclave that meets this standard also qualifies.

11. **Background Checks.** Every Approved User, including contractors, must have passed an identity check and, where lawful, a criminal-history check. Where local law restricts criminal checks, identity, right-to-work, or employment verification is accepted. Government vetting or a clearance satisfies this requirement.

12. **Incident Procedure.** Customer must maintain a documented procedure for suspected compromise or misuse of the grant that covers credential revocation, seat suspension, and notifying Anthropic.

13. **Government Entities.** A FISMA Authority to Operate with an annual independent Inspector General assessment against NIST SP 800-53, or an equivalent national scheme, satisfies the Managed Devices and Malware Protection, Background Checks, and Incident Procedure requirements. All other requirements continue to apply.