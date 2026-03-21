# HIPAA Security Rule Audit Checklist

**Regulation:** 45 CFR Parts 160 and 164

**Scope:** Administrative, Physical, and Technical Safeguards

**Assessment Date:** 2026-02-01

**Assessor:** Brian Santiago

---

## How to Read This Checklist

- **Status:** Implemented / Partially Implemented / Not Implemented / N/A
- **Evidence:** Type of documentation that supports the control
- Organized by HIPAA Security Rule safeguard category

---

## Administrative Safeguards (164.308)

| # | Requirement | Standard | Status | Evidence | Notes |
|---|------------|----------|--------|----------|-------|
| 1 | Risk analysis conducted | 164.308(a)(1)(ii)(A) | Implemented | Risk register, methodology doc | Annual + event-driven |
| 2 | Risk management program | 164.308(a)(1)(ii)(B) | Implemented | Risk treatment plans | Tracked in risk register |
| 3 | Sanction policy for violations | 164.308(a)(1)(ii)(C) | Implemented | Employee handbook, HR policy | Referenced in security policy |
| 4 | Information system activity review | 164.308(a)(1)(ii)(D) | Implemented | Splunk dashboards, access logs | Monthly review |
| 5 | Security officer designated | 164.308(a)(2) | Implemented | Org chart, job description | IT Security lead |
| 6 | Workforce access authorization | 164.308(a)(3)(ii)(A) | Implemented | RBAC matrix, access request forms | Role-based via AD |
| 7 | Workforce clearance procedures | 164.308(a)(3)(ii)(B) | Implemented | Background check policy | Pre-employment screening |
| 8 | Termination procedures | 164.308(a)(3)(ii)(C) | Implemented | Offboarding checklist, HR-AD sync | 24-hour revocation SLA |
| 9 | Access authorization | 164.308(a)(4)(ii)(B) | Implemented | Access request workflow | Manager + data owner approval |
| 10 | Access modification | 164.308(a)(4)(ii)(C) | Partially Implemented | AD group changes | Manual for some apps |
| 11 | Security awareness training | 164.308(a)(5)(i) | Implemented | Training records, completion logs | Quarterly |
| 12 | Security reminders | 164.308(a)(5)(ii)(A) | Implemented | Email newsletters | Monthly security tips |
| 13 | Log-in monitoring | 164.308(a)(5)(ii)(C) | Implemented | Splunk alerts | Failed login alerting |
| 14 | Password management | 164.308(a)(5)(ii)(D) | Implemented | AD password policy | 14-char minimum, no rotation |
| 15 | Security incident procedures | 164.308(a)(6)(i) | Implemented | IR plan, playbooks | NIST 800-61 aligned |
| 16 | Security incident response | 164.308(a)(6)(ii) | Implemented | IR plan, incident log | Tested via tabletop exercises |
| 17 | Contingency plan | 164.308(a)(7)(i) | Implemented | DR plan, backup procedures | Annual review |
| 18 | Data backup plan | 164.308(a)(7)(ii)(A) | Implemented | Backup schedules, restore logs | Daily backups, geo-redundant |
| 19 | Disaster recovery plan | 164.308(a)(7)(ii)(B) | Partially Implemented | DR plan draft | Needs full DR test |
| 20 | Emergency mode operations | 164.308(a)(7)(ii)(C) | Partially Implemented | Emergency procedures | Documented, not fully tested |
| 21 | Testing and revision | 164.308(a)(7)(ii)(D) | Partially Implemented | Restore test results | Need annual DR exercise |
| 22 | BAA with business associates | 164.308(b)(1) | Implemented | Signed BAAs | All ePHI vendors covered |
| 23 | BAA content requirements | 164.308(b)(4) | Implemented | BAA template | Reviewed by legal |

---

## Physical Safeguards (164.310)

| # | Requirement | Standard | Status | Evidence | Notes |
|---|------------|----------|--------|----------|-------|
| 24 | Facility access controls | 164.310(a)(1) | Implemented | Badge access system logs | Server room restricted |
| 25 | Contingency operations access | 164.310(a)(2)(i) | Partially Implemented | Emergency access procedures | Need testing |
| 26 | Facility security plan | 164.310(a)(2)(ii) | Implemented | Physical security policy | Annual review |
| 27 | Access control and validation | 164.310(a)(2)(iii) | Implemented | Visitor logs, escort policy | Sign-in required |
| 28 | Maintenance records | 164.310(a)(2)(iv) | Implemented | Maintenance logs | Tracked in NinjaOne |
| 29 | Workstation use policy | 164.310(b) | Implemented | Acceptable use policy | Clean desk policy |
| 30 | Workstation security | 164.310(c) | Implemented | MDM enrollment, screen lock | Auto-lock 5 minutes |
| 31 | Device and media disposal | 164.310(d)(1) | Implemented | Disposal certificates | NIST 800-88 compliant |
| 32 | Media reuse | 164.310(d)(2)(i) | Implemented | Sanitization procedures | Verified before reuse |
| 33 | Device movement accountability | 164.310(d)(2)(iii) | Implemented | Asset tracking | NinjaOne inventory |

---

## Technical Safeguards (164.312)

| # | Requirement | Standard | Status | Evidence | Notes |
|---|------------|----------|--------|----------|-------|
| 34 | Unique user identification | 164.312(a)(2)(i) | Implemented | AD accounts | No shared accounts |
| 35 | Emergency access procedure | 164.312(a)(2)(ii) | Partially Implemented | Break-glass procedure | Needs regular testing |
| 36 | Automatic logoff | 164.312(a)(2)(iii) | Implemented | Group Policy settings | 15-min idle timeout |
| 37 | Encryption and decryption | 164.312(a)(2)(iv) | Implemented | BitLocker, TLS configs | AES-256 at rest |
| 38 | Audit controls | 164.312(b) | Implemented | Splunk deployment | 90-day retention |
| 39 | Integrity controls | 164.312(c)(1) | Implemented | File integrity monitoring | EDR-based |
| 40 | Authentication of entity | 164.312(d) | Implemented | MFA configuration | All ePHI access |
| 41 | Transmission encryption | 164.312(e)(1) | Implemented | TLS 1.2+ enforcement | Tested with SSL scan |
| 42 | Transmission integrity | 164.312(e)(2)(i) | Implemented | TLS, checksums | Standard protocols |

---

## Organizational Requirements (164.314)

| # | Requirement | Standard | Status | Evidence | Notes |
|---|------------|----------|--------|----------|-------|
| 43 | BAA contracts | 164.314(a)(1) | Implemented | Signed BAAs on file | All covered entities |
| 44 | BAA required content | 164.314(a)(2) | Implemented | BAA template | Legal reviewed |
| 45 | Group health plan safeguards | 164.314(b)(1) | N/A | | Not applicable |

---

## Policies, Procedures, and Documentation (164.316)

| # | Requirement | Standard | Status | Evidence | Notes |
|---|------------|----------|--------|----------|-------|
| 46 | Policies and procedures | 164.316(a) | Implemented | Policy library | Reviewed annually |
| 47 | Documentation retention | 164.316(b)(1) | Implemented | Retention schedule | 6-year minimum |
| 48 | Documentation updates | 164.316(b)(2)(i) | Implemented | Version control, review dates | Annual review cycle |
| 49 | Documentation availability | 164.316(b)(2)(ii) | Implemented | SharePoint, Confluence | Accessible to workforce |
| 50 | Time limit on retention | 164.316(b)(2)(iii) | Implemented | Retention schedule | From date of creation |

---

## Summary

| Category | Total | Implemented | Partial | Not Implemented | N/A |
|----------|-------|------------|---------|-----------------|-----|
| Administrative (164.308) | 23 | 19 | 4 | 0 | 0 |
| Physical (164.310) | 10 | 10 | 0 | 0 | 0 |
| Technical (164.312) | 9 | 8 | 1 | 0 | 0 |
| Organizational (164.314) | 3 | 2 | 0 | 0 | 1 |
| Documentation (164.316) | 5 | 5 | 0 | 0 | 0 |
| **Total** | **50** | **44** | **5** | **0** | **1** |

**Compliance Rate: 88% Implemented / 10% Partially / 0% Not Implemented**

---

## Remediation Priorities

1. Disaster recovery plan testing (164.308(a)(7)(ii)(D)) - Schedule annual DR exercise
2. Emergency access procedure testing (164.312(a)(2)(ii)) - Test break-glass accounts quarterly
3. Access modification automation (164.308(a)(4)(ii)(C)) - Extend HR-AD sync to all applications
4. Emergency mode operations (164.308(a)(7)(ii)(C)) - Conduct emergency mode drill
5. Contingency operations access (164.310(a)(2)(i)) - Test physical access during emergency scenario
