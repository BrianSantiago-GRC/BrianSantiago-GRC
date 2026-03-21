# Third-Party Vendor Risk Assessment Questionnaire

**Framework:** ISO 27001:2022 (A.5.19-5.22) / HIPAA Security Rule

**Purpose:** Evaluate the security posture of vendors who will access, process, or store organizational data, including ePHI and student records

**Version:** 1.0

**Last Updated:** 2026-02-01

---

## Instructions

This questionnaire should be completed by the vendor's security or compliance team. Responses will be evaluated as part of the vendor onboarding process and annual review cycle.

**Scoring:**
- Each response is rated: Meets Requirement / Partially Meets / Does Not Meet / N/A
- Vendors must score "Meets" on all critical controls (marked with *) to be approved
- Vendors with "Partially Meets" on critical controls require a remediation plan before contract execution

---

## Section 1: Organization and Governance

| # | Question | Response | Notes |
|---|----------|----------|-------|
| 1.1 | Do you have a documented information security policy? | | |
| 1.2 | Is there a designated security officer or equivalent role? | | |
| 1.3 | Do you conduct annual risk assessments? | | |
| 1.4* | Do you hold any security certifications (SOC 2, ISO 27001, HITRUST)? If yes, provide the most recent report or certificate. | | |
| 1.5 | Do you carry cyber insurance? If yes, provide coverage amounts. | | |

## Section 2: Data Protection

| # | Question | Response | Notes |
|---|----------|----------|-------|
| 2.1* | How is our data classified and segregated from other customers' data? | | |
| 2.2* | Is data encrypted at rest? If yes, what algorithm and key length? | | |
| 2.3* | Is data encrypted in transit? What TLS version is enforced? | | |
| 2.4* | In what geographic locations is our data stored and processed? | | |
| 2.5* | Do you retain our data after contract termination? If yes, for how long and how is it disposed of? | | |
| 2.6 | Do you have a data loss prevention (DLP) program? | | |
| 2.7* | How do you handle data subject access requests and data deletion requests? | | |

## Section 3: Access Control

| # | Question | Response | Notes |
|---|----------|----------|-------|
| 3.1* | Is multi-factor authentication required for accessing systems that store our data? | | |
| 3.2* | How is access to our data restricted (RBAC, least privilege)? | | |
| 3.3 | Do you conduct regular access reviews? How often? | | |
| 3.4* | How are accounts deprovisioned when employees leave your organization? What is the timeline? | | |
| 3.5 | Do you use privileged access management (PAM) for administrative access? | | |

## Section 4: Security Operations

| # | Question | Response | Notes |
|---|----------|----------|-------|
| 4.1 | Do you perform regular vulnerability scans? What is the frequency? | | |
| 4.2 | Do you conduct penetration testing? How often? Who performs it? | | |
| 4.3 | What is your patch management process and SLA for critical vulnerabilities? | | |
| 4.4 | Do you have a SIEM or equivalent monitoring capability? | | |
| 4.5 | Do you deploy endpoint detection and response (EDR) on systems that access our data? | | |

## Section 5: Incident Response

| # | Question | Response | Notes |
|---|----------|----------|-------|
| 5.1* | Do you have a documented incident response plan? | | |
| 5.2* | Within what timeframe will you notify us of a security incident affecting our data? | | |
| 5.3 | Have you experienced a data breach in the past 3 years? If yes, provide details on what happened and remediation. | | |
| 5.4 | Do you conduct incident response testing (tabletop exercises, simulations)? | | |

## Section 6: Business Continuity

| # | Question | Response | Notes |
|---|----------|----------|-------|
| 6.1 | Do you have a business continuity / disaster recovery plan? | | |
| 6.2 | What is your RTO (Recovery Time Objective) and RPO (Recovery Point Objective)? | | |
| 6.3 | How often do you test your DR plan? | | |
| 6.4 | What is your guaranteed uptime SLA? | | |

## Section 7: Compliance

| # | Question | Response | Notes |
|---|----------|----------|-------|
| 7.1* | Are you willing to sign a Business Associate Agreement (BAA) per HIPAA requirements? | | |
| 7.2 | Do you comply with FERPA requirements for handling student education records? | | |
| 7.3* | Do you allow audit rights for your customers (right to audit clause)? | | |
| 7.4 | Can you provide your most recent SOC 2 Type II report? | | |
| 7.5 | Do you have a process for tracking and complying with regulatory changes? | | |

## Section 8: Subprocessors

| # | Question | Response | Notes |
|---|----------|----------|-------|
| 8.1* | Do you use subprocessors or subcontractors who will have access to our data? If yes, list them. | | |
| 8.2 | How do you assess the security of your subprocessors? | | |
| 8.3* | Will you notify us before adding or changing subprocessors? | | |

---

## Risk Rating Criteria

| Rating | Definition | Action |
|--------|-----------|--------|
| Low Risk | Vendor meets all critical controls and most others | Approve, standard annual review |
| Medium Risk | Vendor partially meets some controls; no critical gaps | Approve with remediation plan, 6-month review |
| High Risk | Vendor does not meet one or more critical controls | Do not approve until remediated, or seek alternative vendor |
| Critical Risk | Vendor has significant security gaps and handles Restricted data | Do not approve |

---

## Assessment Workflow

1. **Pre-assessment:** Compliance sends questionnaire to vendor
2. **Vendor completes:** Allow 15 business days for response
3. **Review:** IT Security reviews technical responses; Compliance reviews regulatory responses
4. **Risk rating:** Assign overall vendor risk rating
5. **Decision:** Approve, approve with conditions, or reject
6. **Contract:** Include security requirements, BAA, audit rights, and incident notification clause
7. **Ongoing:** Annual reassessment; request updated SOC 2 reports annually

---

## References

- ISO 27001:2022 Annex A (5.19 - Information Security in Supplier Relationships)
- HIPAA Security Rule (164.308(b) - Business Associate Contracts)
- NIST SP 800-53 Rev. 5 (SA-9 - External Information System Services)
- NIST SP 800-161 - Supply Chain Risk Management
