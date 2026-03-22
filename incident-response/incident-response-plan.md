# Incident Response Plan

**Framework:** NIST SP 800-61 Rev. 2 (Computer Security Incident Handling Guide)

**Scope:** All information systems and data managed by the organization

**Version:** 1.0

**Effective Date:** 2026-01-15

**Review Cycle:** Annual and after every significant incident

**Owner:** IT Security

---

## 1. Purpose

Provide a structured approach to detecting, responding to, containing, and recovering from security incidents. This plan covers incidents involving ePHI (HIPAA), student education records (FERPA), and general IT security events.

---

## 2. Incident Severity Levels

| Level | Name | Description | Example | Response Time |
|-------|------|-------------|---------|---------------|
| SEV-1 | Critical | Active breach of regulated data; business operations severely impacted | Ransomware encrypting production systems; confirmed ePHI exfiltration | Immediate (within 1 hour) |
| SEV-2 | High | Confirmed unauthorized access; potential for regulated data exposure | Compromised admin account; malware on server with ePHI access | Within 4 hours |
| SEV-3 | Medium | Suspicious activity; no confirmed data exposure | Phishing email clicked; unauthorized software installed | Within 24 hours |
| SEV-4 | Low | Minor policy violation; no security impact | Failed login attempts; AUP violation | Within 72 hours |

---

## 3. Incident Response Phases

### Phase 1: Preparation

- Maintain and test this IR plan annually
- Train IR team members on procedures and tools
- Maintain forensic toolkit (write blockers, imaging tools, chain of custody forms)
- Keep up-to-date contact lists for internal teams, vendors, and regulators
- Conduct tabletop exercises quarterly (see tabletop scenarios)
- Maintain incident log and evidence storage

**Tools:**
- SIEM: Splunk (log aggregation and alerting)
- EDR: Endpoint detection and response
- Email filtering: Anti-phishing and anti-malware
- Forensic workstation: Dedicated system for evidence analysis

### Phase 2: Detection and Analysis

**Detection sources:**
- SIEM alerts (Splunk)
- EDR alerts
- User reports (email to security@, phone to help desk)
- Vulnerability scan findings (Qualys)
- Third-party notification (vendor, law enforcement)
- Anomalous activity during access reviews

**Triage steps:**
1. Validate the alert (true positive vs. false positive)
2. Determine incident severity level
3. Identify affected systems and data types
4. Check if regulated data (ePHI, FERPA records) is potentially involved
5. Document initial findings in incident log
6. Escalate to IR lead if SEV-1 or SEV-2

### Phase 3: Containment

**Short-term containment (stop the bleeding):**
- Isolate affected systems from the network
- Disable compromised accounts
- Block malicious IPs/domains at firewall
- Preserve volatile evidence (memory dumps, running processes) before changes

**Long-term containment:**
- Apply patches or workarounds to affected systems
- Reset credentials for affected accounts
- Implement additional monitoring on affected systems
- Stand up clean replacement systems if needed

### Phase 4: Eradication

- Remove malware, unauthorized tools, or backdoors
- Patch the vulnerability that was exploited
- Verify removal using EDR and antivirus scans
- Review logs to confirm no persistence mechanisms remain
- Validate that root cause has been addressed

### Phase 5: Recovery

- Restore systems from clean backups (verify backup integrity)
- Monitor restored systems closely for 72 hours
- Validate that business operations are functioning normally
- Re-enable user access incrementally
- Confirm that regulated data integrity is intact

### Phase 6: Post-Incident Activity

- Conduct post-incident review within 5 business days
- Document lessons learned and root cause
- Update IR procedures, playbooks, and detection rules as needed
- Update the risk register if new risks were identified
- File the complete incident report with all evidence and timeline

---

## 4. Communication Plan

| Audience | When | Method | Who Communicates |
|----------|------|--------|-----------------|
| IR team | Immediately on detection | Secure chat channel or phone tree | IR lead |
| IT leadership | SEV-1/SEV-2 within 1 hour | Phone + email | IR lead |
| Executive leadership | SEV-1 within 2 hours | Briefing call | IT Director |
| Legal counsel | When regulated data involved | Phone + email | IT Director |
| HHS (HIPAA breach) | Within 60 days if >500 individuals | Online portal | Privacy Officer |
| Affected individuals | Per HIPAA/state requirements | Written notification | Privacy Officer + Legal |
| FERPA compliance office | When student records involved | Internal escalation | Compliance |
| Law enforcement | If criminal activity suspected | Phone | IT Director + Legal |

---

## 5. Incident Response Team

| Role | Responsibility | Primary | Backup |
|------|---------------|---------|--------|
| IR Lead | Coordinates response; makes containment decisions | IT Security Lead | IT Director |
| Technical Lead | Performs forensics and technical analysis | Senior IT staff | IT Security |
| Communications | Manages internal/external notifications | IT Director | Compliance |
| Compliance/Privacy | Determines regulatory notification requirements | Privacy Officer | Compliance |
| Documentation | Maintains incident log and evidence chain | Assigned per incident | IR Lead |

---

## 6. Evidence Handling

- All evidence is documented with date, time, source, and handler
- Digital evidence is imaged before analysis (never analyze original)
- Chain of custody form completed for each piece of evidence
- Evidence stored in access-controlled location (physical or encrypted digital)
- Evidence retained for minimum 6 years (HIPAA) or per legal hold requirements

---

## 7. Playbook Index

Detailed response playbooks are maintained for the following scenarios:

| Playbook | Scenario | Severity |
|----------|----------|----------|
| PB-001 | [Ransomware](playbook-ransomware.md) | SEV-1 |
| PB-002 | [Phishing with credential compromise](playbook-phishing.md) | SEV-2/SEV-3 |
| PB-003 | [Data breach involving regulated data](playbook-data-breach.md) | SEV-1 |

See the other files in this directory for full playbooks.

---

## 8. References

- NIST SP 800-61 Rev. 2 - Computer Security Incident Handling Guide
- HIPAA Breach Notification Rule (45 CFR 164.400-414)
- FERPA (34 CFR Part 99)
- NIST SP 800-86 - Guide to Integrating Forensic Techniques into Incident Response
