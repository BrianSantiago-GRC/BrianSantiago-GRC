# Risk Assessment Methodology

**Framework:** NIST SP 800-30 Rev. 1 / ISO 27005:2022

**Scope:** K-12 organization processing HIPAA and FERPA regulated data

**Version:** 1.0

---

## 1. Purpose

This document defines the methodology used to identify, assess, and prioritize information security risks across the organization. It provides a repeatable, consistent process that aligns with NIST SP 800-30 and ISO 27005.

---

## 2. Risk Assessment Process

### 2.1 Step 1: System Characterization

Identify the systems, data flows, and assets in scope:

- Hardware, software, and network components
- Data types (ePHI, student education records, PII)
- System boundaries and interconnections
- User roles and access levels

**Output:** Asset inventory with data classification labels

### 2.2 Step 2: Threat Identification

Identify threat sources applicable to the environment:

| Threat Source | Examples |
|--------------|----------|
| External adversary | Hackers, nation-state actors, hacktivists |
| Insider (malicious) | Disgruntled employees, contractors |
| Insider (accidental) | Misconfiguration, misdirected email |
| Environmental | Power failure, natural disaster |
| System failure | Hardware malfunction, software bugs |
| Third party | Vendor compromise, supply chain risk |

**Source:** NIST SP 800-30 Table D-2

### 2.3 Step 3: Vulnerability Identification

Identify weaknesses that could be exploited:

- Vulnerability scan results (Qualys)
- Configuration audit findings
- Gap analysis outputs (ISO 27001, NIST CSF)
- Previous audit findings and POA&Ms
- Penetration test results (if available)

### 2.4 Step 4: Likelihood Determination

| Rating | Label | Description |
|--------|-------|-------------|
| 1 | Very Low | Unlikely to occur; strong controls in place |
| 2 | Low | Could occur but not expected within 2 years |
| 3 | Moderate | Reasonably expected within 1-2 years |
| 4 | High | Expected to occur within 1 year |
| 5 | Very High | Almost certain; has occurred recently or controls are weak |

### 2.5 Step 5: Impact Determination

| Rating | Label | Description |
|--------|-------|-------------|
| 1 | Very Low | Negligible effect on operations or compliance |
| 2 | Low | Minor disruption; no regulatory impact |
| 3 | Moderate | Noticeable disruption; possible minor regulatory finding |
| 4 | High | Significant disruption; regulatory investigation likely |
| 5 | Very High | Severe disruption; breach notification required; potential fines |

Impact considers: operational disruption, financial loss, regulatory penalty, reputational harm, and harm to individuals.

### 2.6 Step 6: Risk Scoring

**Inherent Risk** = Likelihood x Impact

| | Impact 1 | Impact 2 | Impact 3 | Impact 4 | Impact 5 |
|---|---|---|---|---|---|
| **Likelihood 5** | 5 (M) | 10 (H) | 15 (H) | 20 (C) | 25 (C) |
| **Likelihood 4** | 4 (L) | 8 (M) | 12 (H) | 16 (H) | 20 (C) |
| **Likelihood 3** | 3 (L) | 6 (M) | 9 (M) | 12 (H) | 15 (H) |
| **Likelihood 2** | 2 (L) | 4 (L) | 6 (M) | 8 (M) | 10 (H) |
| **Likelihood 1** | 1 (L) | 2 (L) | 3 (L) | 4 (L) | 5 (M) |

L = Low (1-4) | M = Medium (5-9) | H = High (10-16) | C = Critical (17-25)

### 2.7 Step 7: Control Assessment

Evaluate existing controls and their effectiveness:

| Effectiveness | Reduction | Criteria |
|--------------|-----------|----------|
| High | 40% | Controls are well-designed, consistently applied, and tested |
| Medium | 25% | Controls exist but have gaps in design or implementation |
| Low | 10% | Controls are minimal or inconsistently applied |
| None | 0% | No controls in place |

**Residual Risk** = Inherent Risk x (1 - Reduction %)

### 2.8 Step 8: Risk Treatment

| Risk Level | Response | Timeline |
|------------|----------|----------|
| Critical | Immediate action; escalate to leadership | Within 72 hours |
| High | Develop treatment plan; assign owner | Within 30 days |
| Medium | Schedule remediation; monitor | Within 90 days |
| Low | Accept or monitor; document rationale | Next review cycle |

Treatment options (ISO 27005):
- **Mitigate:** Implement additional controls
- **Transfer:** Insurance or contractual transfer
- **Accept:** Formally accept with documented rationale and management sign-off
- **Avoid:** Eliminate the activity or system creating the risk

---

## 3. Assessment Frequency

| Trigger | Type |
|---------|------|
| Quarterly | Scheduled review of full risk register |
| After significant incident | Targeted reassessment of affected risks |
| System change | Assessment of new or modified systems |
| Annual | Full risk assessment aligned with audit cycle |
| Regulatory change | Assess impact of new requirements (HIPAA, FERPA updates) |

---

## 4. Roles and Responsibilities

| Role | Responsibility |
|------|---------------|
| Risk Owner | Accepts or escalates risk; owns treatment plan |
| IT Security | Conducts assessments; maintains risk register |
| Compliance | Validates regulatory alignment; supports audit readiness |
| Leadership | Reviews critical/high risks; approves risk acceptance |

---

## 5. References

- NIST SP 800-30 Rev. 1 - Guide for Conducting Risk Assessments
- NIST SP 800-37 Rev. 2 - Risk Management Framework
- ISO/IEC 27005:2022 - Information Security Risk Management
- HIPAA Security Rule (45 CFR 164.308(a)(1))
- FERPA (34 CFR Part 99)
