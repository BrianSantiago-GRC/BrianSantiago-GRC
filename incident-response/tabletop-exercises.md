# Tabletop Exercise Scenarios

**Framework:** NIST SP 800-61 / NIST SP 800-84

**Purpose:** Test incident response procedures and identify gaps in a low-stakes discussion format

**Frequency:** Quarterly

**Facilitator:** IT Security Lead

**Participants:** IR team, IT Operations, Compliance, Help Desk, Management

---

## How to Run These Exercises

1. Select a scenario based on current risk priorities (check the risk register)
2. Distribute the scenario to participants 30 minutes before the session
3. Walk through each inject in order, pausing for discussion after each one
4. Use the discussion prompts to guide conversation
5. Document decisions made, gaps identified, and action items
6. Update IR procedures and playbooks based on findings

Expected duration: 60-90 minutes per exercise

---

## Scenario 1: Ransomware Attack on School Network

**Date:** Q1 Exercise

**Relates to:** RISK-002 (Ransomware infection on endpoints)

### Background

It is Tuesday at 7:45 AM. Staff are arriving and logging in for the day. The school nurse needs to access student health records in the EHR system for a scheduled medication administration.

### Inject 1 (7:50 AM)

The help desk receives three calls within 10 minutes from staff who cannot open files on the shared drive. One teacher reports seeing a text file on their desktop that says "Your files have been encrypted. Contact us at [email address] for the decryption key."

**Discussion:**
- Who receives this initial report and what is their first action?
- How do we confirm this is ransomware vs. a different issue?
- At what point do we classify this as SEV-1 vs. SEV-2?

### Inject 2 (8:15 AM)

The IT team confirms that files on two file servers are encrypted. The ransomware appears to be spreading via SMB. The EDR console shows alerts on 12 endpoints. The EHR system is on a separate network segment but shares Active Directory authentication.

**Discussion:**
- What systems do we isolate first?
- How do we determine if the EHR system and ePHI are affected?
- Who do we notify at this point?
- Do we shut down the entire network or isolate segments?

### Inject 3 (9:00 AM)

The principal calls IT asking when systems will be back. Teachers cannot access lesson plans, attendance, or the student information system. A parent calls asking why the school's website is down.

**Discussion:**
- How do we communicate with staff and parents?
- What is our message to the public?
- Who is authorized to speak externally?
- How do we maintain school operations without IT systems?

### Inject 4 (10:30 AM)

IT confirms that the EHR system was not encrypted, but the attacker's lateral movement logs show they accessed the server. The ransom demand is $50,000 in cryptocurrency.

**Discussion:**
- Does accessing the EHR server constitute a HIPAA breach even if data was not exfiltrated?
- What is our position on paying the ransom?
- When do we engage law enforcement?
- When do we engage the Privacy Officer for breach assessment?

### Inject 5 (End of Day)

Systems have been isolated. Backups from last night are confirmed clean. Estimated recovery time is 48 hours to restore all file servers and verify integrity.

**Discussion:**
- What is our recovery priority order?
- How do we verify that the threat is fully eradicated before reconnecting systems?
- What do we communicate to staff about the timeline?
- What regulatory notifications are needed?

---

## Scenario 2: Phishing Campaign Targeting Staff Credentials

**Date:** Q2 Exercise

**Relates to:** RISK-005 (Phishing leading to credential compromise)

### Background

It is Thursday afternoon. The school district recently announced a new benefits enrollment period, and staff are expecting emails from HR about open enrollment.

### Inject 1 (2:00 PM)

A staff member forwards a suspicious email to the help desk. The email claims to be from HR with a link to "update your benefits selections." The link goes to a site that looks like the M365 login page but is hosted on a different domain.

**Discussion:**
- How do we determine if other staff received this email?
- What is our process for searching and quarantining the email across all mailboxes?
- How quickly can we block the phishing domain?

### Inject 2 (2:30 PM)

Email log analysis shows the phishing email was sent to 150 staff members. Click tracking from the email gateway shows 23 users clicked the link. We do not know yet how many entered credentials.

**Discussion:**
- Do we reset passwords for all 23 users or just those who entered credentials?
- How do we determine who actually submitted credentials?
- What is the fastest way to force password resets and revoke sessions?

### Inject 3 (3:15 PM)

Azure AD logs show that one compromised account had a sign-in from an IP address in another country 20 minutes after the phishing email was clicked. The account belongs to a staff member with access to the student information system (FERPA data).

**Discussion:**
- How do we assess whether student records were accessed?
- What logs do we check in the student information system?
- At what point does this become a FERPA incident?
- Do we need to notify parents?

### Inject 4 (4:00 PM)

Further investigation shows the attacker added a mail forwarding rule on the compromised account sending all incoming email to an external address. The rule was active for approximately 90 minutes before being detected.

**Discussion:**
- What types of data could have been forwarded during that window?
- How do we determine the content of forwarded emails?
- Does this change our breach assessment?

---

## Scenario 3: Insider Threat / Unauthorized Data Access

**Date:** Q3 Exercise

**Relates to:** RISK-003 (Insider threat - data exfiltration)

### Background

A quarterly access review reveals that a staff member in the registrar's office has been accessing student records that are outside their normal job function.

### Inject 1

The access review shows the employee accessed records for 47 students in a different department over the past 60 days. These students have no connection to the employee's assigned responsibilities.

**Discussion:**
- How do we determine if this was accidental or intentional?
- Who needs to be involved in this investigation (HR, legal, compliance)?
- Do we confront the employee immediately or investigate further first?
- What logs do we pull to understand the scope?

### Inject 2

Further log review shows the employee also downloaded several student records as PDFs. USB access logs show a USB device was connected to their workstation on three occasions during the same period.

**Discussion:**
- At what point do we consider this a FERPA violation?
- Do we disable the employee's access during the investigation?
- How do we preserve evidence while maintaining the employee's rights?
- What is the role of HR vs. IT Security in this situation?

### Inject 3

The employee claims they were "just curious" and did not share the records with anyone. DLP logs show no email transmission of the files, but we cannot confirm whether data was copied to the USB device because USB content logging was not enabled.

**Discussion:**
- Can we accept the employee's explanation?
- What is our obligation to notify the affected students/parents under FERPA?
- What controls should we implement to prevent this in the future?
- How does this feed back into the risk register?

---

## After-Action Report Template

Use this template after each exercise:

```
Exercise:         [Scenario name]
Date:             [Date]
Participants:     [Names and roles]
Duration:         [Minutes]

Key Findings:
1. [Finding]
2. [Finding]
3. [Finding]

Gaps Identified:
1. [Gap] - Severity: [High/Medium/Low]
2. [Gap] - Severity: [High/Medium/Low]

Action Items:
| # | Action | Owner | Due Date | Status |
|---|--------|-------|----------|--------|
| 1 | [Action] | [Owner] | [Date] | Open |
| 2 | [Action] | [Owner] | [Date] | Open |

Procedures to Update:
- [Procedure or playbook]
- [Procedure or playbook]
```
