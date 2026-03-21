# Cross-Framework Control Mapping Matrix

**Purpose:** Map security controls across NIST CSF 2.0, NIST SP 800-53, ISO 27001:2022, and HIPAA Security Rule to demonstrate compliance coverage and identify gaps across frameworks.

**Scope:** K-12 environment with HIPAA and FERPA obligations

**Last Updated:** 2026-03-01

---

## How to Use This Matrix

Each row represents a security control area. Columns show the corresponding requirement in each framework. This mapping helps:

- Demonstrate that one control can satisfy multiple compliance requirements
- Identify gaps where a framework has a requirement but no control is mapped
- Support audit evidence collection across multiple standards
- Reduce duplicate effort when managing multi-framework compliance

---

## Access Control

| Control Area | NIST CSF 2.0 | NIST 800-53 | ISO 27001:2022 | HIPAA | Implementation Status |
|-------------|-------------|-------------|----------------|-------|---------------------|
| Access control policy | PR.AA-03 | AC-1 | A.5.15 | 164.312(a)(1) | Implemented |
| Account management | PR.AA-01 | AC-2 | A.5.16 | 164.308(a)(4) | Implemented |
| Least privilege | PR.AA-03 | AC-6 | A.5.18 | 164.312(a)(1) | Implemented |
| Separation of duties | PR.AA-03 | AC-5 | A.5.3 | 164.312(a)(1) | Implemented |
| MFA | PR.AA-02 | IA-2(1) | A.5.17 | 164.312(d) | Implemented |
| Remote access | PR.AA-03 | AC-17 | A.6.7 | 164.312(e)(1) | Implemented |
| Session management | PR.AA-03 | AC-12 | A.8.5 | 164.312(a)(2)(iii) | Implemented |
| Privileged access management | PR.AA-01 | AC-6(5) | A.8.2 | 164.308(a)(4) | Implemented |

## Risk Management

| Control Area | NIST CSF 2.0 | NIST 800-53 | ISO 27001:2022 | HIPAA | Implementation Status |
|-------------|-------------|-------------|----------------|-------|---------------------|
| Risk assessment | ID.RA-04 | RA-3 | Clause 6.1.2 | 164.308(a)(1)(ii)(A) | Implemented |
| Risk treatment | ID.RA-04 | RA-7 | Clause 6.1.3 | 164.308(a)(1)(ii)(B) | Implemented |
| Vulnerability management | ID.RA-01 | RA-5 | A.8.8 | 164.308(a)(1) | Implemented |
| Threat intelligence | ID.RA-02 | RA-3(1) | A.5.7 | - | Partial |
| Risk register | ID.RA-04 | RA-3 | Clause 6.1.2 | 164.308(a)(1) | Implemented |

## Incident Response

| Control Area | NIST CSF 2.0 | NIST 800-53 | ISO 27001:2022 | HIPAA | Implementation Status |
|-------------|-------------|-------------|----------------|-------|---------------------|
| IR plan | RS.MA-01 | IR-1 | A.5.24 | 164.308(a)(6)(i) | Implemented |
| IR procedures | RS.MA-01 | IR-4 | A.5.26 | 164.308(a)(6)(ii) | Implemented |
| IR reporting | RS.CO-01 | IR-6 | A.6.8 | 164.308(a)(6)(ii) | Implemented |
| Incident analysis | RS.AN-01 | IR-4 | A.5.25 | 164.308(a)(6) | Partial |
| Lessons learned | RS.AN-01 | IR-4(1) | A.5.27 | 164.308(a)(6) | Partial |
| Breach notification | RS.CO-01 | IR-6 | A.5.26 | 164.408-414 | Implemented |

## Data Protection

| Control Area | NIST CSF 2.0 | NIST 800-53 | ISO 27001:2022 | HIPAA | Implementation Status |
|-------------|-------------|-------------|----------------|-------|---------------------|
| Data classification | ID.AM-03 | RA-2 | A.5.12 | 164.312(a)(1) | Implemented |
| Encryption at rest | PR.DS-01 | SC-28 | A.8.24 | 164.312(a)(2)(iv) | Implemented |
| Encryption in transit | PR.DS-02 | SC-8 | A.8.24 | 164.312(e)(1) | Implemented |
| Data loss prevention | PR.DS-01 | SC-7(10) | A.8.12 | 164.312(c)(1) | Implemented |
| Data retention | PR.DS-01 | SI-12 | A.5.33 | 164.316(b)(1) | Implemented |
| Media disposal | PR.DS-01 | MP-6 | A.7.14 | 164.310(d)(1) | Implemented |
| Backup | RC.RP-01 | CP-9 | A.8.13 | 164.308(a)(7)(ii)(A) | Implemented |

## Security Operations

| Control Area | NIST CSF 2.0 | NIST 800-53 | ISO 27001:2022 | HIPAA | Implementation Status |
|-------------|-------------|-------------|----------------|-------|---------------------|
| Audit logging | DE.CM-01 | AU-2, AU-3 | A.8.15 | 164.312(b) | Implemented |
| Log monitoring | DE.AE-01 | AU-6 | A.8.16 | 164.312(b) | Partial |
| Malware protection | PR.DS-01 | SI-3 | A.8.7 | 164.308(a)(5)(ii)(B) | Implemented |
| Patch management | PR.DS-01 | SI-2 | A.8.8 | 164.308(a)(5)(ii)(B) | Implemented |
| Configuration management | PR.PS-01 | CM-6 | A.8.9 | 164.310(d)(1) | Partial |
| Change management | PR.PS-01 | CM-3 | A.8.32 | 164.308(a)(8) | Implemented |

## Awareness and Training

| Control Area | NIST CSF 2.0 | NIST 800-53 | ISO 27001:2022 | HIPAA | Implementation Status |
|-------------|-------------|-------------|----------------|-------|---------------------|
| Security awareness training | PR.AT-01 | AT-2 | A.6.3 | 164.308(a)(5)(i) | Implemented |
| Role-based training | PR.AT-01 | AT-3 | A.6.3 | 164.308(a)(5)(i) | Implemented |
| Phishing awareness | PR.AT-01 | AT-2(1) | A.6.3 | 164.308(a)(5)(ii)(A) | Implemented |

## Third-Party Risk

| Control Area | NIST CSF 2.0 | NIST 800-53 | ISO 27001:2022 | HIPAA | Implementation Status |
|-------------|-------------|-------------|----------------|-------|---------------------|
| Vendor assessment | GV.SC-01 | SA-9 | A.5.19 | 164.308(b)(1) | Implemented |
| Vendor agreements | GV.SC-01 | SA-9 | A.5.20 | 164.308(b)(4) | Implemented |
| Ongoing monitoring | GV.SC-01 | SA-9(2) | A.5.22 | 164.308(b)(1) | Partial |
| Supply chain risk | GV.SC-01 | SR-1 | A.5.21 | - | Not Implemented |

## Physical Security

| Control Area | NIST CSF 2.0 | NIST 800-53 | ISO 27001:2022 | HIPAA | Implementation Status |
|-------------|-------------|-------------|----------------|-------|---------------------|
| Facility access | PR.AA-03 | PE-2 | A.7.2 | 164.310(a)(1) | Implemented |
| Visitor management | PR.AA-03 | PE-3 | A.7.2 | 164.310(a)(2)(iii) | Implemented |
| Environmental protection | PR.AA-03 | PE-13, PE-15 | A.7.5 | 164.310(a)(2)(ii) | Implemented |
| Equipment disposal | PR.DS-01 | MP-6 | A.7.14 | 164.310(d)(1) | Implemented |

---

## Coverage Summary

| Framework | Total Controls Mapped | Implemented | Partial | Not Implemented |
|-----------|---------------------|-------------|---------|-----------------|
| NIST CSF 2.0 | 42 | 36 | 5 | 1 |
| NIST 800-53 | 42 | 36 | 5 | 1 |
| ISO 27001:2022 | 42 | 36 | 5 | 1 |
| HIPAA Security Rule | 40 | 35 | 4 | 1 |

**Overall Implementation Rate: 86%**

---

## Key Findings

1. Strong coverage across access control, data protection, and physical security
2. Gaps in threat intelligence, supply chain risk, and continuous monitoring map across all frameworks
3. HIPAA has the highest implementation rate since the environment is already HIPAA-regulated
4. ISO 27001 A.5.21 (supply chain) is the primary gap with no compensating control
