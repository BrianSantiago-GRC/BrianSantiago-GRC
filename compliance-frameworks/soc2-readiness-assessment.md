# SOC 2 Type II Readiness Assessment

**Standard:** AICPA Trust Services Criteria (TSC) 2017

**Report Type:** SOC 2 Type II (operating effectiveness over a period)

**Scope:** Information systems supporting the organization's services, including systems that process ePHI and student education records

**Assessment Date:** 2026-03-15

**Assessor:** Brian Santiago

---

## What This Assessment Covers

SOC 2 Type II evaluates whether controls are designed properly AND operating effectively over a review period (typically 6-12 months). This readiness assessment identifies where the organization currently stands against each Trust Services Criteria category and what needs to happen before engaging an external auditor.

This assessment maps existing controls (many already documented in this portfolio) to SOC 2 requirements and identifies gaps.

---

## Trust Services Criteria Overview

| Category | Code | Description | In Scope |
|----------|------|-------------|----------|
| Security | CC | Protection against unauthorized access (required for all SOC 2) | Yes |
| Availability | A | System uptime and operational accessibility | Yes |
| Processing Integrity | PI | Data processing is complete, accurate, and authorized | No |
| Confidentiality | C | Protection of confidential information | Yes |
| Privacy | P | Collection, use, retention, and disposal of personal information | Yes |

Processing Integrity is excluded because the organization does not provide data processing services to external customers.

---

## CC Series: Common Criteria (Security)

### CC1 - Control Environment

| Ref | Criteria | Status | Evidence | Gap |
|-----|----------|--------|----------|-----|
| CC1.1 | Organization demonstrates commitment to integrity and ethical values | Ready | Employee handbook, code of conduct, sanction policy | - |
| CC1.2 | Board/management exercises oversight of internal controls | Ready | Quarterly risk reviews, leadership meeting minutes | - |
| CC1.3 | Management establishes structure, authority, and responsibility | Ready | Org chart, RACI matrix, security policy | - |
| CC1.4 | Organization demonstrates commitment to attract, develop, and retain competent individuals | Ready | Job descriptions, training program, performance reviews | - |
| CC1.5 | Organization holds individuals accountable for internal control responsibilities | Ready | Security policy enforcement clause, sanction policy | - |

**CC1 Status: Ready**

### CC2 - Communication and Information

| Ref | Criteria | Status | Evidence | Gap |
|-----|----------|--------|----------|-----|
| CC2.1 | Organization obtains or generates relevant, quality information | Ready | Risk register, vulnerability reports, SIEM dashboards | - |
| CC2.2 | Organization internally communicates information about internal controls | Ready | Policy library on SharePoint, security awareness training | - |
| CC2.3 | Organization communicates with external parties about internal controls | Partial | BAAs include security clauses; no formal external communication plan | Need external communication procedure for control changes |

**CC2 Status: Partial (1 gap)**

### CC3 - Risk Assessment

| Ref | Criteria | Status | Evidence | Gap |
|-----|----------|--------|----------|-----|
| CC3.1 | Organization specifies objectives clearly enough to identify risks | Ready | Risk assessment methodology, risk appetite statement | - |
| CC3.2 | Organization identifies risks and analyzes them to determine management approach | Ready | Risk register (14 risks), NIST 800-30 methodology | - |
| CC3.3 | Organization considers potential for fraud | Partial | Insider threat in risk register; no formal fraud risk assessment | Add fraud risk assessment section |
| CC3.4 | Organization identifies and assesses changes that could significantly impact internal controls | Partial | Change management process exists; no formal change risk assessment | Link change management to control impact assessment |

**CC3 Status: Partial (2 gaps)**

### CC4 - Monitoring Activities

| Ref | Criteria | Status | Evidence | Gap |
|-----|----------|--------|----------|-----|
| CC4.1 | Organization selects, develops, and performs ongoing evaluations | Partial | Quarterly access reviews, monthly vuln reports; no formal monitoring plan for all controls | Create control monitoring schedule |
| CC4.2 | Organization evaluates and communicates internal control deficiencies in a timely manner | Ready | Audit findings tracked with SLAs, reported monthly to IT Director | - |

**CC4 Status: Partial (1 gap)**

### CC5 - Control Activities

| Ref | Criteria | Status | Evidence | Gap |
|-----|----------|--------|----------|-----|
| CC5.1 | Organization selects and develops control activities that mitigate risks | Ready | Controls mapped in risk register, control mapping matrix | - |
| CC5.2 | Organization selects and develops technology-based control activities | Ready | EDR, SIEM, MFA, DLP, encryption documented | - |
| CC5.3 | Organization deploys control activities through policies and procedures | Ready | Policy library (information security, access control, patch management, data classification) | - |

**CC5 Status: Ready**

### CC6 - Logical and Physical Access Controls

| Ref | Criteria | Status | Evidence | Gap |
|-----|----------|--------|----------|-----|
| CC6.1 | Organization implements logical access security over protected information assets | Ready | RBAC, MFA, access control policy, Azure AD PIM | - |
| CC6.2 | Organization controls access credentials (registration, issuance, management) | Ready | HR-AD sync, password policy, MFA enrollment | - |
| CC6.3 | Organization authorizes, modifies, and removes access based on roles | Ready | Access review procedures, quarterly reviews, offboarding checklist | - |
| CC6.4 | Organization restricts physical access to facilities and protected information assets | Ready | Badge access, server room restrictions, visitor policy | - |
| CC6.5 | Organization discontinues logical and physical protections over assets no longer needed | Ready | Asset disposal (NIST 800-88), orphan account audits | - |
| CC6.6 | Organization implements logical access security over externally managed data | Ready | Vendor risk assessments, BAAs, contractual security requirements | - |
| CC6.7 | Organization restricts transmission, movement, and removal of information | Ready | DLP policies, encryption in transit, USB controls | - |
| CC6.8 | Organization implements controls to prevent or detect unauthorized or malicious software | Ready | EDR, application whitelisting, admin rights restricted | - |

**CC6 Status: Ready**

### CC7 - System Operations

| Ref | Criteria | Status | Evidence | Gap |
|-----|----------|--------|----------|-----|
| CC7.1 | Organization uses detection and monitoring procedures to identify configuration changes resulting in new vulnerabilities | Partial | Qualys scans weekly; no automated configuration drift detection | Implement configuration baseline monitoring |
| CC7.2 | Organization monitors system components for anomalies | Ready | SIEM (Splunk), EDR alerts, failed login monitoring | - |
| CC7.3 | Organization evaluates identified events to determine if they are security incidents | Ready | IR plan with triage procedures, severity classification | - |
| CC7.4 | Organization responds to identified security incidents | Ready | IR plan, playbooks (ransomware, phishing, data breach) | - |
| CC7.5 | Organization identifies, develops, and implements activities to recover from incidents | Ready | Recovery procedures in IR plan, backup/restore process | - |

**CC7 Status: Partial (1 gap)**

### CC8 - Change Management

| Ref | Criteria | Status | Evidence | Gap |
|-----|----------|--------|----------|-----|
| CC8.1 | Organization authorizes, designs, develops, configures, documents, tests, approves, and implements changes | Ready | Change management process, change tickets, approval workflow | - |

**CC8 Status: Ready**

### CC9 - Risk Mitigation

| Ref | Criteria | Status | Evidence | Gap |
|-----|----------|--------|----------|-----|
| CC9.1 | Organization identifies, selects, and develops risk mitigation activities | Ready | Risk treatment plans in risk register | - |
| CC9.2 | Organization assesses and manages risks associated with vendors and business partners | Ready | Vendor risk tiering, questionnaires, BAAs, annual reassessment | - |

**CC9 Status: Ready**

---

## A Series: Availability

| Ref | Criteria | Status | Evidence | Gap |
|-----|----------|--------|----------|-----|
| A1.1 | Organization maintains, monitors, and evaluates current processing capacity and usage | Ready | NinjaOne monitoring, capacity dashboards | - |
| A1.2 | Organization authorizes, designs, develops, implements, and monitors environmental protections | Ready | UPS, fire suppression, generator, climate control | - |
| A1.3 | Organization tests recovery plan procedures supporting system recovery | Partial | Monthly backup restore tests; no full DR test | Conduct annual full DR exercise |

**Availability Status: Partial (1 gap)**

---

## C Series: Confidentiality

| Ref | Criteria | Status | Evidence | Gap |
|-----|----------|--------|----------|-----|
| C1.1 | Organization identifies and maintains confidential information | Ready | Data classification policy (4 levels), handling requirements | - |
| C1.2 | Organization disposes of confidential information | Ready | NIST 800-88 media sanitization, disposal certificates | - |

**Confidentiality Status: Ready**

---

## P Series: Privacy

| Ref | Criteria | Status | Evidence | Gap |
|-----|----------|--------|----------|-----|
| P1.1 | Organization provides notice about privacy practices | Ready | Privacy notices (HIPAA Notice of Privacy Practices) | - |
| P2.1 | Organization obtains consent for collection, use, and disclosure of personal information | Ready | Consent forms, directory information opt-out (FERPA) | - |
| P3.1 | Organization collects personal information only for identified purposes | Ready | Data minimization in classification policy | - |
| P4.1 | Organization limits the use of personal information | Ready | Need-to-know access, RBAC, DLP | - |
| P5.1 | Organization retains personal information per retention schedule | Ready | Retention schedule (6-year HIPAA minimum) | - |
| P5.2 | Organization disposes of personal information per retention schedule | Ready | Disposal procedures, certificates | - |
| P6.1 | Organization provides data subjects access to their personal information | Ready | HIPAA right of access procedures | - |
| P7.1 | Organization communicates personal information to third parties only for identified purposes | Ready | BAAs, FERPA disclosure exceptions documented | - |
| P8.1 | Organization informs data subjects of privacy incidents | Ready | Breach notification procedures (HIPAA 60-day, state laws) | - |

**Privacy Status: Ready**

---

## Readiness Summary

| TSC Category | Total Criteria | Ready | Partial | Not Ready |
|-------------|---------------|-------|---------|-----------|
| CC1 - Control Environment | 5 | 5 | 0 | 0 |
| CC2 - Communication | 3 | 2 | 1 | 0 |
| CC3 - Risk Assessment | 4 | 2 | 2 | 0 |
| CC4 - Monitoring | 2 | 1 | 1 | 0 |
| CC5 - Control Activities | 3 | 3 | 0 | 0 |
| CC6 - Access Controls | 8 | 8 | 0 | 0 |
| CC7 - System Operations | 5 | 4 | 1 | 0 |
| CC8 - Change Management | 1 | 1 | 0 | 0 |
| CC9 - Risk Mitigation | 2 | 2 | 0 | 0 |
| A - Availability | 3 | 2 | 1 | 0 |
| C - Confidentiality | 2 | 2 | 0 | 0 |
| P - Privacy | 9 | 9 | 0 | 0 |
| **Total** | **47** | **41** | **6** | **0** |

**Readiness Rate: 87% Ready / 13% Partial / 0% Not Ready**

---

## Remediation Plan (6 Gaps to Close Before Audit)

| Priority | Gap | TSC Ref | Owner | Target Date | Effort |
|----------|-----|---------|-------|-------------|--------|
| 1 | Conduct full DR exercise | A1.3 | IT Operations | Q2 2026 | Medium |
| 2 | Create control monitoring schedule covering all TSC areas | CC4.1 | IT Security | Q2 2026 | Medium |
| 3 | Add fraud risk assessment to risk program | CC3.3 | Compliance | Q2 2026 | Low |
| 4 | Link change management to control impact assessment | CC3.4 | IT Operations | Q2 2026 | Low |
| 5 | Implement configuration baseline drift detection | CC7.1 | IT Operations | Q3 2026 | Medium |
| 6 | Document external communication procedure for control changes | CC2.3 | Compliance | Q2 2026 | Low |

**Estimated time to audit-ready: 3-4 months**

---

## Mapping to Existing Portfolio Artifacts

Many SOC 2 requirements are already satisfied by artifacts in this portfolio:

| SOC 2 Area | Existing Artifact |
|------------|------------------|
| CC3 (Risk Assessment) | `risk-assessment/risk-register.md`, `risk-assessment/risk-assessment-methodology.md` |
| CC5 (Control Activities) | `compliance-frameworks/control-mapping-matrix.md` |
| CC6 (Access Controls) | `policies-and-procedures/access-control-policy.md`, `access-control/access-review-procedures.md` |
| CC7 (System Operations) | `vulnerability-management/vulnerability-management-lifecycle.md`, `incident-response/` |
| CC9 (Vendor Risk) | `third-party-risk/vendor-risk-assessment-questionnaire.md`, `third-party-risk/vendor-risk-tiering.md` |
| A (Availability) | `incident-response/playbook-ransomware.md` (recovery section) |
| C (Confidentiality) | `policies-and-procedures/data-classification-policy.md` |
| P (Privacy) | `compliance-frameworks/hipaa-security-rule-checklist.md` |

---

## References

- AICPA Trust Services Criteria (2017)
- AICPA SOC 2 Reporting on an Examination of Controls at a Service Organization
- NIST SP 800-53 Rev. 5 (control mapping)
- ISO 27001:2022 (control mapping)
