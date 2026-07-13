# Security Automation Toolkit

Four small Python tools that turn clearly labeled synthetic security and GRC data into repeatable review output. The project demonstrates readable logic, consistent evidence handling, and tests without implying production deployment.

## Problem, Action, Result

**Problem:** Access reviews, risk scoring, evidence collection, and control-gap checks are repetitive and easy to perform inconsistently.

**Action:** I wrote standard-library Python tools that parse structured data, apply documented rules, prioritize findings, and generate reviewer-friendly output.

**Result:** The same inputs now produce repeatable findings that can be tested, reviewed, and discussed. No external packages or live-system access are required.

## Tools

| Tool | Input | Output | Key logic |
|---|---|---|---|
| `risk_scorer.py` | Synthetic risk-register CSV | Inherent/residual scores, heat map, priorities | Likelihood x impact with documented control reductions |
| `access_review_audit.py` | Synthetic user-access CSV | Orphan, MFA, privilege, service-account, and separation-of-duties findings | Policy thresholds with a reproducible review date |
| `evidence_collector.py` | Built-in synthetic access, training, and patch records | Console report plus optional JSON/CSV evidence package | Normalization, severity ranking, and audit packaging |
| `compliance_checker.py` | Built-in or CSV control mappings | Multi-framework status and gap report | NIST CSF, NIST 800-53, ISO 27001, and HIPAA mapping summaries |

## Run It

From this directory:

```powershell
python risk_scorer.py sample_risk_register.csv outputs/risk-report.txt
python access_review_audit.py sample_users.csv --as-of 2026-04-01
python evidence_collector.py outputs --as-of 2026-04-01
python compliance_checker.py
python -m unittest discover -s tests -v
```

The explicit `--as-of` date keeps portfolio results reproducible. When it is omitted for a custom access export, the tools use the current date.

## Verification

Automated tests cover:

- Risk classification and control-effectiveness calculations.
- Orphan-account, MFA, privilege, separation-of-duties, and service-account checks.
- Access, training, and patch evidence summaries.
- Compliance gap and framework counts.

GitHub Actions runs the same standard-library test suite on every push and pull request.

## Scope

This is portfolio code using synthetic people, systems, controls, and findings. It has no live API connections and has not been deployed in a production environment. The value is the review logic, readable output, tests, and the ability to explain how the workflow could connect to AD/Entra, ticketing, endpoint-management, or SIEM exports.
