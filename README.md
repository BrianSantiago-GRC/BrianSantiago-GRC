# Brian Santiago

Entry-level GRC professional based in Ocala, FL. ISO 27001 Lead Auditor. CompTIA Security+.

[LinkedIn](https://linkedin.com/in/briansantiago-grc) · briand.santiago@gmail.com · Open to junior GRC and compliance roles

---

I got into GRC through IT operations. Spent a few years doing hands-on IT work in HIPAA and FERPA environments before I realized the compliance side was where I wanted to focus. That background actually helps -- I know what the systems look like behind the policies, not just what the frameworks say about them.

Right now I work in a K-12 school managing compliance under HIPAA and FERPA. Audit evidence, SOPs, identity lifecycle, endpoint management. Real work, regulated environment.

Everything below is built from actual methodology. I structured this portfolio the way I would organize a working GRC program, not as a collection of disconnected documents.

---

## Portfolio

This repo is organized by GRC domain. Each folder contains artifacts that connect to each other the way they would in a real compliance program -- the risk register feeds into the maturity assessment, the policies reference the controls, the playbooks tie back to the risk scenarios, and the automation scripts work with the data in the artifacts.

### Risk Assessment

Artifacts for identifying, scoring, and managing information security risks.

| Document | Framework |
|----------|-----------|
| [Risk Register](risk-assessment/risk-register.md) -- 14 risks with inherent/residual scoring and treatment plans | NIST SP 800-30 |
| [Risk Assessment Methodology](risk-assessment/risk-assessment-methodology.md) -- scoring criteria, risk matrix, treatment options | NIST SP 800-30 / ISO 27005 |

### Policies and Procedures

Organizational policies that define security requirements and acceptable behavior.

| Document | Framework |
|----------|-----------|
| [Information Security Policy](policies-and-procedures/information-security-policy.md) -- data classification, encryption, awareness, enforcement | ISO 27001 / HIPAA |
| [Access Control Policy](policies-and-procedures/access-control-policy.md) -- RBAC, MFA, least privilege, access reviews, remote access | NIST SP 800-53 / ISO 27001 |
| [Data Classification Policy](policies-and-procedures/data-classification-policy.md) -- classification levels, handling requirements, roles | NIST SP 800-60 / ISO 27001 |
| [Patch Management Policy](policies-and-procedures/patch-management-policy.md) -- patching SLAs by severity, exception process, metrics | NIST SP 800-40 |

### Compliance Frameworks

Assessments and mappings that show current compliance posture across multiple standards.

| Document | Framework |
|----------|-----------|
| [NIST CSF 2.0 Maturity Assessment](compliance-frameworks/nist-csf-maturity-assessment.md) -- all 6 functions scored with gap analysis | NIST CSF 2.0 |
| [HIPAA Security Rule Audit Checklist](compliance-frameworks/hipaa-security-rule-checklist.md) -- 50 controls across all safeguard categories | 45 CFR Parts 160/164 |
| [ISO 27001:2022 Gap Analysis](compliance-frameworks/iso27001-gap-analysis.md) -- full Annex A assessment (93 controls) | ISO 27001:2022 |
| [SOC 2 Type II Readiness Assessment](compliance-frameworks/soc2-readiness-assessment.md) -- 47 Trust Services Criteria assessed, 87% ready, remediation plan | AICPA TSC 2017 |
| [NIST 800-171 Self-Assessment](compliance-frameworks/nist-800-171-assessment.md) -- all 110 requirements, SPRS scoring (77/110), POA&M | NIST SP 800-171 Rev 2 |
| [ISO 42001 AI Governance Assessment](compliance-frameworks/iso42001-ai-governance.md) -- AI risk assessment, responsible use policy, governance controls | ISO 42001:2023 |
| [Cross-Framework Control Mapping](compliance-frameworks/control-mapping-matrix.md) -- maps controls across NIST CSF, 800-53, 800-171, ISO 27001, HIPAA | Multi-framework |

### Incident Response

IR plan, playbooks for specific scenarios, and tabletop exercise scripts.

| Document | Framework |
|----------|-----------|
| [Incident Response Plan](incident-response/incident-response-plan.md) -- 6-phase plan with severity levels, communication plan, evidence handling | NIST SP 800-61 |
| [Playbook: Ransomware](incident-response/playbook-ransomware.md) -- step-by-step with decision tree and notification requirements | NIST SP 800-61 / CISA |
| [Playbook: Phishing](incident-response/playbook-phishing.md) -- triage, containment, investigation, and escalation triggers | NIST SP 800-61 |
| [Playbook: Data Breach](incident-response/playbook-data-breach.md) -- HIPAA 4-factor test, FERPA assessment, notification timelines | HIPAA / FERPA |
| [Tabletop Exercise Scenarios](incident-response/tabletop-exercises.md) -- 3 scenarios with injects and discussion prompts | NIST SP 800-84 |

### Vulnerability Management

Lifecycle documentation for identifying, prioritizing, and remediating vulnerabilities.

| Document | Framework |
|----------|-----------|
| [Vulnerability Management Lifecycle](vulnerability-management/vulnerability-management-lifecycle.md) -- 6-phase lifecycle, SLAs, exception process, metrics | NIST SP 800-40 / ISO 27001 |

### Third-Party Risk

Vendor assessment questionnaire and risk tiering framework.

| Document | Framework |
|----------|-----------|
| [Vendor Risk Assessment Questionnaire](third-party-risk/vendor-risk-assessment-questionnaire.md) -- 38 questions across 8 security domains | ISO 27001 / HIPAA |
| [Vendor Risk Tiering Framework](third-party-risk/vendor-risk-tiering.md) -- tier matrix, assessment requirements by tier, sample inventory | ISO 27001 / NIST SP 800-161 |

### Access Control

Procedures for managing and reviewing user access to systems and data.

| Document | Framework |
|----------|-----------|
| [Access Review Procedures](access-control/access-review-procedures.md) -- review types, procedures, evidence templates, metrics | NIST SP 800-53 / ISO 27001 |

### Audit Artifacts

Guides and metrics for audit preparation and program measurement.

| Document | Framework |
|----------|-----------|
| [Audit Evidence Collection Guide](audit-artifacts/audit-evidence-guide.md) -- maps every common audit request to evidence source and location | HIPAA / ISO 27001 |
| [KPI and KRI Metrics](audit-artifacts/kpi-kri-metrics.md) -- measurable indicators across vuln mgmt, access control, IR, compliance, TPRM | Multi-framework |

### Security Automation

Python scripts that automate common GRC tasks. Zero external dependencies.

| Script | What It Does | Framework |
|--------|-------------|-----------|
| [risk_scorer.py](security-automation/risk_scorer.py) | Calculates inherent/residual risk scores from CSV, generates heat map and prioritized report | NIST SP 800-30 |
| [evidence_collector.py](security-automation/evidence_collector.py) | Collects and analyzes access, training, and patch evidence for audit prep | HIPAA / ISO 27001 |
| [access_review_audit.py](security-automation/access_review_audit.py) | Audits user access for orphan accounts, MFA gaps, privilege ratios, and SoD violations | NIST SP 800-53 |
| [compliance_checker.py](security-automation/compliance_checker.py) | Maps controls across 5 frameworks and reports implementation gaps by framework and owner | Multi-framework |
| [integrations.py](security-automation/integrations.py) | Live integration module that connects scripts to AD, Microsoft Graph, Qualys, Splunk, and n8n | Multi-platform |

---

## Certifications

- ISO 27001 Certified Lead Auditor
- CompTIA Security+ (2024)
- CompTIA Network+ (2024)
- Microsoft SC-900 Security, Compliance and Identity Fundamentals
- Qualys Vulnerability Management Foundation
- ITIL Foundation (2024)
- Google Cybersecurity Certificate (2024)

---

## Skills

Frameworks: HIPAA, FERPA, NIST CSF, ISO 27001, SOC 1/2, NIST 800-171, ISO 42001

Audit and compliance: gap analysis, control testing, evidence collection, audit coordination, policy and SOP authoring

Risk: risk register development, CAPA planning, third-party risk assessments, treatment planning

IAM: provisioning and deprovisioning, MFA, access governance, access reviews, RCA

Tools: Splunk, Wireshark, NinjaOne, Qualys, Confluence, Microsoft 365, Azure AD, Active Directory, n8n

---

## What I am working on

- CISA exam prep
- Deepening ISO 42001 AI governance work -- AI risk is showing up in more GRC programs and I want to be ahead of it
- Building automation workflows with n8n -- I use it to handle repetitive operational tasks and it has changed how I think about process efficiency
- Connecting GRC automation scripts to live data sources (AD, Qualys, Splunk) for production use

---

Currently preparing for CISA. If you are hiring for a junior GRC, compliance, or IT audit role feel free to reach out.
