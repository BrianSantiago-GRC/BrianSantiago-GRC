# Risk Register

**Framework:** NIST SP 800-30 Rev. 1 (Guide for Conducting Risk Assessments)

**Scope:** Information systems supporting HIPAA and FERPA regulated data in a K-12 environment

**Last Updated:** 2026-03-21

**Risk Owner:** IT Security / Compliance

---

## Scoring Methodology

Risks are scored using the methodology defined in the [Risk Assessment Methodology](../risk-assessment/risk-assessment-methodology.md). In brief: **Inherent Risk** = Likelihood (1-5) x Impact (1-5), scored on a 1-25 scale. **Residual Risk** = Inherent Risk adjusted by control effectiveness. Risk levels: Low (1-4), Medium (5-9), High (10-16), Critical (17-25).

---

## Risk Register

| ID | Risk | Category | Threat Source | Asset | L | I | Inherent | Controls | Eff. | Residual | Level | Owner |
|----|------|----------|---------------|-------|---|---|----------|----------|------|----------|-------|-------|
| RISK-001 | Unauthorized access to ePHI | Confidentiality | External attacker | EHR System | 4 | 5 | 20 | MFA on all ePHI accounts; RBAC implemented | High | 12 | High | IT Security |
| RISK-002 | Ransomware infection on endpoints | Integrity | External attacker | Workstations/servers | 4 | 5 | 20 | EDR on all endpoints; daily backups with offline copy | Medium | 15 | High | IT Operations |
| RISK-003 | Insider threat - data exfiltration | Confidentiality | Insider (malicious) | Student records DB | 2 | 5 | 10 | DLP on email/USB; quarterly access reviews | Medium | 8 | Medium | IT Security |
| RISK-004 | Unpatched critical vulnerabilities | Integrity | External attacker | Network infrastructure | 3 | 4 | 12 | Monthly Qualys scans; 30-day critical patching SLA | Medium | 9 | Medium | IT Operations |
| RISK-005 | Phishing - credential compromise | Confidentiality | External attacker | Email/credentials | 4 | 4 | 16 | Quarterly security awareness; email anti-phishing rules | Medium | 12 | High | IT Security |
| RISK-006 | Loss of backup data | Availability | System failure | Backup infrastructure | 2 | 5 | 10 | Geo-redundant backups; monthly restore testing | High | 6 | Medium | IT Operations |
| RISK-007 | Third-party vendor breach | Confidentiality | Third party | Vendor-hosted SIS | 3 | 4 | 12 | Annual vendor risk assessments; BAA; contractual controls | Medium | 9 | Medium | Compliance |
| RISK-008 | Misconfigured cloud permissions | Confidentiality | Insider (accidental) | Azure AD / M365 | 3 | 4 | 12 | Quarterly access reviews; least privilege; Azure AD PIM | Medium | 9 | Medium | IT Security |
| RISK-009 | Physical theft of devices | Confidentiality | External attacker | Laptops/mobile | 3 | 3 | 9 | Full disk encryption; MDM remote wipe | High | 5 | Medium | IT Operations |
| RISK-010 | Denial of service attack | Availability | External attacker | Public-facing web apps | 2 | 3 | 6 | WAF deployed; cloud DDoS mitigation | High | 4 | Low | IT Security |
| RISK-011 | Non-compliance with FERPA audit | Compliance | Regulatory body | Student education records | 2 | 4 | 8 | Annual FERPA training; need-to-know access; audit logging | High | 5 | Medium | Compliance |
| RISK-012 | Identity lifecycle failures | Confidentiality | Insider (accidental) | Active Directory | 3 | 3 | 9 | Automated provisioning via HR sync; orphan account audits | Medium | 7 | Medium | IT Security |
| RISK-013 | Insufficient logging/monitoring | Integrity | Internal gap | SIEM infrastructure | 2 | 4 | 8 | Splunk with 1-year retention; critical event alerting | Medium | 6 | Medium | IT Security |
| RISK-014 | Social engineering - help desk | Confidentiality | External attacker | Help desk staff | 3 | 4 | 12 | Identity verification for resets; help desk security training | Low | 11 | High | IT Operations |

---

## Summary

- **Total risks:** 14
- **Critical (inherent):** 2 (RISK-001, RISK-002)
- **High (residual):** 4 risks requiring 30-day treatment plans
- **Average inherent score:** 11.7
- **Average residual score:** 8.4
- **Overall risk reduction from controls:** 28.0%

---

## Treatment Plan Priorities

1. **RISK-002** (Ransomware) - Residual 15: Upgrade EDR to include behavioral detection; implement network segmentation; test backup restoration weekly
2. **RISK-001** (ePHI access) - Residual 12: Add conditional access policies in Azure AD; implement session timeouts; deploy CASB
3. **RISK-005** (Phishing) - Residual 12: Increase training to monthly phishing simulations; deploy DMARC/DKIM/SPF; implement URL sandboxing
4. **RISK-014** (Social engineering) - Residual 11: Implement callback verification for privileged resets; add help desk MFA for admin actions

---

## Notes

- Risks are reviewed quarterly and after any significant incident; full risk assessment conducted annually per the Risk Assessment Methodology
- Risk register feeds into the NIST CSF 2.0 maturity assessment (ID.RA)
- Automated scoring available via `security-automation/risk_scorer.py`
