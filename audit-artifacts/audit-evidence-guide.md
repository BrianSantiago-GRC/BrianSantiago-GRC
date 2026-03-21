# Audit Evidence Collection Guide

**Purpose:** Define what evidence is needed for each control area during internal and external audits, where to find it, and how to organize it for auditor review

**Audience:** IT Security, Compliance, IT Operations

**Last Updated:** 2026-03-01

---

## Why This Guide Exists

Auditors ask for evidence. If you cannot produce it quickly, it looks like the control does not exist, even if it does. This guide maps every common audit request to the system where the evidence lives and the format auditors expect.

This is organized by control area, not by framework, because most audit requests map across multiple frameworks (HIPAA, ISO 27001, NIST CSF) and the evidence is the same.

---

## Access Control Evidence

| Auditor Request | Evidence Source | Format | Location |
|----------------|---------------|--------|----------|
| Access control policy | Policy library | PDF/Markdown | SharePoint > Policies |
| User access list for [system] | System admin console or AD export | CSV | Generated on request |
| Quarterly access review records | Review spreadsheet + signoff | CSV + PDF | SharePoint > Access Reviews > [Date] |
| Terminated employee access revocation | HR-AD sync logs + offboarding tickets | Export + tickets | NinjaOne / AD logs |
| Privileged access list | Azure AD PIM export | CSV | Generated on request |
| MFA enrollment status | Azure AD MFA report | CSV | Azure AD portal |
| Password policy configuration | AD Group Policy screenshot | Screenshot | AD Group Policy |
| Orphan account audit results | AD query results + remediation log | CSV | SharePoint > Access Reviews |

---

## Risk Management Evidence

| Auditor Request | Evidence Source | Format | Location |
|----------------|---------------|--------|----------|
| Risk register | Risk register document | Markdown/CSV | This repo: risk-assessment/ |
| Risk assessment methodology | Methodology document | PDF/Markdown | This repo: risk-assessment/ |
| Risk treatment plans | Treatment plans in risk register | Markdown | This repo: risk-assessment/ |
| Risk acceptance documentation | Risk acceptance forms | Signed PDF | SharePoint > Risk |
| Board/leadership risk review | Meeting minutes | PDF | SharePoint > Governance |

---

## Vulnerability Management Evidence

| Auditor Request | Evidence Source | Format | Location |
|----------------|---------------|--------|----------|
| Vulnerability scan reports | Qualys | PDF/CSV export | Qualys console |
| Patch compliance report | NinjaOne | Dashboard export | NinjaOne portal |
| Patching SLA compliance metrics | Monthly vuln report | PDF | SharePoint > Vuln Management |
| Exception log for unpatched systems | Exception tracker | CSV | SharePoint > Vuln Management |
| Penetration test report (if available) | External vendor | PDF | SharePoint > Security Assessments |

---

## Incident Response Evidence

| Auditor Request | Evidence Source | Format | Location |
|----------------|---------------|--------|----------|
| Incident response plan | IR plan document | PDF/Markdown | This repo: incident-response/ |
| Incident log | Incident tracking system | CSV/export | Ticketing system |
| Post-incident review reports | After-action reports | PDF | SharePoint > Incidents |
| Tabletop exercise records | Exercise reports + attendance | PDF | SharePoint > Exercises |
| Breach notification records | Notification letters, HHS filings | PDF | Compliance files |

---

## Security Awareness Evidence

| Auditor Request | Evidence Source | Format | Location |
|----------------|---------------|--------|----------|
| Training policy | Policy library | PDF | SharePoint > Policies |
| Training completion records | LMS / training platform | CSV export | Training platform |
| Phishing simulation results | Email security platform | Report export | Email security console |
| New hire training completion | LMS enrollment report | CSV | Training platform |

---

## Data Protection Evidence

| Auditor Request | Evidence Source | Format | Location |
|----------------|---------------|--------|----------|
| Data classification policy | Policy library | PDF/Markdown | This repo: policies-and-procedures/ |
| Encryption configuration (at rest) | BitLocker compliance report + DB encryption settings | Screenshot / report | NinjaOne / DB admin |
| Encryption configuration (in transit) | TLS scan results | Report | SSL Labs or internal scan |
| DLP policy configuration | Email/endpoint DLP settings | Screenshot | M365 compliance center |
| Backup configuration and test results | Backup schedules + restore test logs | Screenshot + log | Backup system |
| Media disposal records | Disposal certificates | Signed PDF | IT Operations files |

---

## Third-Party Risk Evidence

| Auditor Request | Evidence Source | Format | Location |
|----------------|---------------|--------|----------|
| Vendor inventory | Vendor list with risk tiers | CSV | SharePoint > TPRM |
| Vendor risk assessments | Completed questionnaires + ratings | PDF | SharePoint > TPRM > [Vendor] |
| BAA inventory | Signed BAAs | PDF | Legal / Compliance files |
| SOC 2 / ISO 27001 reports from vendors | Vendor-provided | PDF | SharePoint > TPRM > [Vendor] |
| Vendor contract security clauses | Contract excerpts | PDF | Legal files |

---

## Physical Security Evidence

| Auditor Request | Evidence Source | Format | Location |
|----------------|---------------|--------|----------|
| Physical access logs (server room) | Badge access system | Export | Physical security system |
| Visitor logs | Sign-in sheets | Scanned PDF | Front desk records |
| Equipment disposal records | Disposal certificates | Signed PDF | IT Operations |
| Environmental controls | UPS, fire suppression inspection reports | PDF | Facilities |

---

## Tips for Audit Preparation

1. **Start collecting 30 days before the audit.** Do not wait for the auditor to ask.
2. **Use consistent naming.** Follow the pattern: `[ControlArea]-[EvidenceType]-[Date].pdf`
3. **Screenshots need context.** Include the system name, date, and what the screenshot shows. A screenshot without a label is useless.
4. **Exports should be complete.** Full user list, not a filtered view. Auditors want to see what you did not filter out.
5. **Keep a running evidence folder.** After every quarterly review, access audit, or tabletop exercise, drop the evidence into the audit folder immediately. Scrambling before an audit is how things get missed.
6. **If a control changed mid-year, show both.** Auditors want to see the control was in place for the full audit period, not just at the time of the audit.

---

## Audit Readiness Checklist

Run this checklist 30 days before any scheduled audit:

- [ ] All access reviews completed for the audit period
- [ ] Vulnerability scan reports exported for each month in scope
- [ ] Patch compliance metrics compiled
- [ ] Incident log exported with all incidents in scope period
- [ ] Training completion records pulled from LMS
- [ ] Phishing simulation reports generated
- [ ] BAA inventory updated and all BAAs accounted for
- [ ] Vendor risk assessments current for Tier 1 and Tier 2 vendors
- [ ] Policy review dates verified (all policies reviewed within 12 months)
- [ ] Risk register updated with current scores and treatment plans
- [ ] Physical access logs exported for the audit period
- [ ] Evidence organized in shared folder with consistent naming
