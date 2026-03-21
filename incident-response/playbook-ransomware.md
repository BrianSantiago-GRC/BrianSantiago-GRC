# Playbook PB-001: Ransomware

**Severity:** SEV-1 (Critical)

**Framework:** NIST SP 800-61 / CISA Ransomware Guide

**Last Updated:** 2026-02-01

---

## Trigger Conditions

- EDR alert for ransomware or encryption behavior
- User reports files encrypted or ransom note displayed
- Unusual mass file modification detected in SIEM
- Backup system alerts for unexpected deletion or modification

---

## Immediate Actions (First 30 Minutes)

| Step | Action | Who |
|------|--------|-----|
| 1 | Confirm alert is a true positive (check EDR console, user report) | Technical Lead |
| 2 | Isolate affected system(s) from network immediately (disconnect cable, disable Wi-Fi, or isolate via EDR) | Technical Lead |
| 3 | Do NOT power off affected systems (preserve volatile evidence) | Technical Lead |
| 4 | Notify IR Lead and activate incident response team | First responder |
| 5 | Begin incident log with timestamp, affected systems, and initial observations | Documentation |
| 6 | Determine scope: how many systems are affected or showing indicators | Technical Lead |
| 7 | Check if ePHI or student records are on affected systems | Compliance |

---

## Containment (First 4 Hours)

| Step | Action | Who |
|------|--------|-----|
| 8 | Block known ransomware indicators (IPs, domains, hashes) at firewall and email gateway | Technical Lead |
| 9 | Disable affected user accounts and reset credentials | IT Security |
| 10 | Isolate network segments with affected systems | IT Operations |
| 11 | Verify backup integrity: confirm backups are not infected and offline copies are accessible | IT Operations |
| 12 | Preserve evidence: capture memory dumps and disk images of affected systems | Technical Lead |
| 13 | Identify ransomware variant (check ransom note, file extensions, ID Ransomware) | Technical Lead |
| 14 | Determine initial access vector (phishing email, RDP, vulnerability) | IT Security |
| 15 | Check for lateral movement indicators across the network | IT Security |

---

## Eradication

| Step | Action | Who |
|------|--------|-----|
| 16 | Remove ransomware from all affected systems using EDR or clean boot media | Technical Lead |
| 17 | Patch the vulnerability or close the access vector used for initial compromise | IT Operations |
| 18 | Scan all systems in the affected network segment for indicators of compromise | IT Security |
| 19 | Reset all credentials in affected domain if Active Directory was compromised | IT Security |
| 20 | Verify no persistence mechanisms remain (scheduled tasks, services, registry keys) | Technical Lead |

---

## Recovery

| Step | Action | Who |
|------|--------|-----|
| 21 | Restore affected systems from verified clean backups | IT Operations |
| 22 | Validate restored data integrity | IT Operations + Data Owners |
| 23 | Reconnect systems to network in phases with enhanced monitoring | IT Security |
| 24 | Monitor restored systems for 72 hours for signs of re-infection | IT Security |
| 25 | Confirm business operations are restored and users can access needed systems | IT Operations |

---

## Notification and Compliance

| Condition | Action | Timeline |
|-----------|--------|----------|
| ePHI potentially accessed or encrypted | Engage Privacy Officer for breach assessment | Within 4 hours |
| Breach confirmed (ePHI of >500 individuals) | Notify HHS, affected individuals, and media (if required) | Within 60 days |
| Student records potentially affected | Notify FERPA compliance office | Within 24 hours |
| Criminal activity suspected | Contact local FBI field office or CISA | Within 24 hours |
| Ransom demand received | Do NOT pay without legal and leadership approval; report to CISA | Immediately |

---

## Post-Incident

| Step | Action | Timeline |
|------|--------|----------|
| 26 | Conduct post-incident review with all team members | Within 5 business days |
| 27 | Document root cause, timeline, and lessons learned | Within 10 business days |
| 28 | Update detection rules based on indicators from this incident | Within 5 business days |
| 29 | Update risk register with new or modified risk entries | Within 10 business days |
| 30 | Schedule targeted training if phishing was the initial vector | Within 30 days |

---

## Decision Tree

```
Ransomware Alert Received
    |
    +-- Validate alert (true/false positive?)
         |
         +-- FALSE POSITIVE --> Document and close
         |
         +-- TRUE POSITIVE --> Isolate system immediately
              |
              +-- Single system? --> Contain, eradicate, restore
              |
              +-- Multiple systems? --> Activate full IR team
                   |
                   +-- ePHI involved? --> Engage Privacy Officer
                   |
                   +-- AD compromised? --> Full credential reset
                   |
                   +-- Backups intact? --> Restore from clean backup
                   |
                   +-- Backups compromised? --> Engage vendor for decryption options
```

---

## Key Contacts

| Role | Contact Method |
|------|---------------|
| IR Lead | Security team phone tree |
| IT Director | Direct phone |
| Privacy Officer | Direct phone + email |
| Legal Counsel | On retainer - direct phone |
| FBI IC3 | ic3.gov or local field office |
| CISA | cisa.gov/report |
