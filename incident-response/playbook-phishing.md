# Playbook PB-002: Phishing with Credential Compromise

**Severity:** SEV-2 (High) or SEV-3 (Medium) depending on impact

**Framework:** NIST SP 800-61

**Last Updated:** 2026-02-01

---

## Trigger Conditions

- User reports clicking a suspicious link or entering credentials on an unknown site
- Email gateway detects phishing email after delivery
- SIEM alert for impossible travel or unusual sign-in activity
- MFA push notification that user did not initiate
- Help desk receives password reset request from user who suspects compromise

---

## Triage (First 15 Minutes)

| Step | Action | Who |
|------|--------|-----|
| 1 | Interview the user: what did they click, what did they enter, when did it happen | Help Desk / IT Security |
| 2 | Determine if credentials were actually entered on a phishing page | IT Security |
| 3 | Check Azure AD / AD sign-in logs for the user account (look for unusual locations, devices, or MFA bypasses) | IT Security |
| 4 | Check if the phishing email was sent to multiple users (search email logs for sender/subject/URL) | IT Security |
| 5 | Assign severity: SEV-2 if credentials confirmed compromised, SEV-3 if link clicked but no creds entered | IR Lead |

---

## Containment

| Step | Action | Who |
|------|--------|-----|
| 6 | Force password reset for the affected user immediately | IT Security |
| 7 | Revoke all active sessions (Azure AD: "Revoke sessions") | IT Security |
| 8 | Verify MFA is enabled and not bypassed (check for added MFA methods by attacker) | IT Security |
| 9 | Block the phishing URL and sender domain at email gateway and web filter | IT Operations |
| 10 | If email sent to multiple users, quarantine the message from all mailboxes | IT Operations |
| 11 | Check for mail forwarding rules added to the compromised mailbox | IT Security |
| 12 | Check for OAuth app consents granted by the compromised account | IT Security |

---

## Investigation

| Step | Action | Who |
|------|--------|-----|
| 13 | Review mailbox audit log for suspicious activity (forwarding rules, delegate access, sent items) | IT Security |
| 14 | Check if the user had access to ePHI, student records, or other Restricted data | Compliance |
| 15 | Review file access logs (SharePoint, OneDrive) for the compromised account | IT Security |
| 16 | Look for lateral movement: did the attacker use the account to send internal phishing? | IT Security |
| 17 | Document indicators of compromise (sender, URL, IP addresses, timestamps) | Documentation |

---

## Eradication

| Step | Action | Who |
|------|--------|-----|
| 18 | Remove any mail forwarding rules or OAuth apps added by the attacker | IT Security |
| 19 | Delete any phishing emails sent from the compromised account to internal users | IT Operations |
| 20 | Add phishing indicators to blocklists (email gateway, firewall, web filter) | IT Operations |
| 21 | Scan the user's endpoint for malware if they downloaded any attachments | IT Security |

---

## Recovery

| Step | Action | Who |
|------|--------|-----|
| 22 | Confirm the user can access their account with new credentials and MFA | Help Desk |
| 23 | Monitor the account for 30 days for unusual activity | IT Security |
| 24 | Provide the user with targeted security awareness follow-up | IT Security |

---

## Escalation Triggers

Escalate to SEV-1 if any of the following are true:

- Attacker accessed ePHI or student records
- Attacker sent internal phishing that resulted in additional compromises
- Attacker modified admin settings or elevated privileges
- Data exfiltration is detected

---

## Post-Incident

| Step | Action | Timeline |
|------|--------|----------|
| 25 | Document the full incident timeline and root cause | Within 5 business days |
| 26 | Update email filtering rules based on this phishing campaign | Within 48 hours |
| 27 | If data exposure occurred, initiate breach assessment | Per IR plan |
| 28 | Report phishing indicators to relevant sharing communities | Within 48 hours |
| 29 | Add scenario to next quarterly tabletop exercise if applicable | Next cycle |
