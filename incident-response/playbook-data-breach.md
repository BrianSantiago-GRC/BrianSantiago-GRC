# Playbook PB-004: Data Breach Involving Regulated Data

**Severity:** SEV-1 (Critical)

**Framework:** NIST SP 800-61 / HIPAA Breach Notification Rule / FERPA

**Last Updated:** 2026-02-01

---

## Trigger Conditions

- Confirmed unauthorized access to, disclosure of, or exfiltration of ePHI or student education records
- Ransomware incident where regulated data was accessible to the attacker
- Lost or stolen device containing unencrypted regulated data
- Third-party vendor notifies of a breach involving our data
- Insider access violation involving Restricted data

---

## Triage (First 1 Hour)

| Step | Action | Who |
|------|--------|-----|
| 1 | Confirm that regulated data was involved (ePHI, student records, PII) | IT Security + Compliance |
| 2 | Determine the type of data exposed and volume of records | IT Security |
| 3 | Identify the population affected (patients, students, employees) | Compliance |
| 4 | Determine if the breach is ongoing or contained | Technical Lead |
| 5 | Activate full IR team and notify IT Director | IR Lead |
| 6 | Engage Privacy Officer immediately | IR Lead |

---

## Containment

| Step | Action | Who |
|------|--------|-----|
| 7 | Stop the breach (isolate systems, disable accounts, block access paths) | Technical Lead |
| 8 | Preserve all evidence (logs, disk images, email records) | Technical Lead |
| 9 | If vendor-caused, contact the vendor's security team and request their IR report | Compliance |
| 10 | Document the chain of custody for all evidence | Documentation |

---

## Breach Assessment (HIPAA 4-Factor Test)

For ePHI breaches, evaluate using the HIPAA breach assessment factors:

| Factor | Question | Assessment |
|--------|----------|-----------|
| 1. Nature and extent of PHI | What types of identifiers and clinical data were involved? | [Document] |
| 2. Unauthorized person | Who accessed or received the data? Were they authorized for any access? | [Document] |
| 3. Was PHI actually acquired or viewed? | Is there evidence the data was opened, downloaded, or read? | [Document] |
| 4. Extent of risk mitigation | What steps were taken to reduce harm (e.g., data retrieved, recipient confirmed deletion)? | [Document] |

If the assessment cannot demonstrate a "low probability of compromise," the event is a reportable breach.

---

## FERPA Assessment

For student education records:

| Question | Assessment |
|----------|-----------|
| Was the disclosure to an authorized party under FERPA exceptions (34 CFR 99.31)? | [Document] |
| Were the records de-identified or did they contain directory information only? | [Document] |
| Has the disclosure been documented in the student's record per 34 CFR 99.32? | [Document] |

---

## Notification Requirements

### HIPAA (ePHI Breach)

| Condition | Notification | Timeline | Method |
|-----------|-------------|----------|--------|
| Breach affecting <500 individuals | HHS annual report | Within 60 days of calendar year end | HHS breach portal |
| Breach affecting >=500 individuals | HHS, affected individuals, media | Within 60 days of discovery | HHS portal, written notice, media outlet |
| All confirmed breaches | Affected individuals | Within 60 days of discovery | Written notice (first class mail) |

Individual notification must include:
- Description of the breach
- Types of information involved
- Steps individuals can take to protect themselves
- What the organization is doing in response
- Contact information for questions

### FERPA

- Record the unauthorized disclosure in the student's education record
- Notify the Family Policy Compliance Office (FPCO) if a systemic failure
- Notify affected parents/students if appropriate

### State Notification

- Check applicable state breach notification laws (varies by state)
- Florida: notify individuals within 30 days (FL Stat. 501.171)

---

## Recovery

| Step | Action | Who |
|------|--------|-----|
| 11 | Remediate the vulnerability or access path that caused the breach | Technical Lead |
| 12 | Implement additional controls to prevent recurrence | IT Security |
| 13 | Monitor affected systems and accounts for 90 days | IT Security |
| 14 | Provide credit monitoring or identity protection if PII/SSN exposed | Compliance + Legal |

---

## Post-Incident

| Step | Action | Timeline |
|------|--------|----------|
| 15 | Complete post-incident review | Within 5 business days |
| 16 | File all required regulatory notifications | Per timelines above |
| 17 | Update risk register | Within 10 business days |
| 18 | Update policies and procedures if gaps contributed | Within 30 days |
| 19 | Conduct targeted training for staff involved | Within 30 days |
| 20 | Brief leadership on root cause and corrective actions | Within 10 business days |

---

## Documentation Checklist

- [ ] Incident log with full timeline
- [ ] Evidence inventory with chain of custody
- [ ] Breach assessment (HIPAA 4-factor test and/or FERPA analysis)
- [ ] List of affected individuals and data types
- [ ] Notification letters (drafts reviewed by legal)
- [ ] Regulatory filings (HHS, state AG, FPCO as applicable)
- [ ] Post-incident review report
- [ ] Corrective action plan with owners and deadlines
