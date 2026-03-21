# Security Automation Scripts

Python tools that automate common GRC tasks. Built to show how repetitive compliance and risk processes can be scripted for consistency and efficiency. All scripts use only the Python standard library -- no pip install required.

---

## Tools

### risk_scorer.py
Reads a risk register CSV, calculates inherent and residual risk scores using NIST SP 800-30 methodology, and generates a prioritized report with a 5x5 risk heat map.

```bash
python3 risk_scorer.py                          # uses sample data
python3 risk_scorer.py risks.csv                # your own data
python3 risk_scorer.py risks.csv report.txt     # save to file
```

**Framework:** NIST SP 800-30

---

### evidence_collector.py
Simulates an audit evidence collection run. Pulls user access data, training records, and patch compliance, then analyzes them for policy violations and produces a findings report. In production, this would connect to Active Directory, your LMS, and vulnerability scanner APIs.

```bash
python3 evidence_collector.py                   # report to console
python3 evidence_collector.py ./output/         # export CSVs and findings JSON
```

**Frameworks:** HIPAA Security Rule, ISO 27001:2022

---

### access_review_audit.py
Reads a user access export (CSV) and runs policy checks: orphan accounts, MFA compliance, privilege ratios, separation of duties violations, and service account review. Produces a pass/fail audit result.

```bash
python3 access_review_audit.py                  # uses sample data
python3 access_review_audit.py users.csv        # your own AD export
```

**Frameworks:** NIST SP 800-53 (AC-2), HIPAA 164.308(a)(3-4)

---

### compliance_checker.py
Reads a control mapping (or uses built-in sample data) and generates a compliance status report across NIST CSF, NIST 800-53, ISO 27001, and HIPAA. Shows implementation rates by framework and by owner, highlights gaps, and flags stale control reviews.

```bash
python3 compliance_checker.py                   # uses sample data
python3 compliance_checker.py controls.csv      # your own control mapping
```

**Frameworks:** NIST CSF 2.0, NIST 800-53, ISO 27001, HIPAA

---

## CSV Formats

Each tool documents its expected CSV format in the script header or generates sample data when run without arguments. Run any script with no arguments to see the output format.

---

## Why Automate GRC Tasks

- Risk scoring by hand is slow and inconsistent. A script applies the same formula every time.
- Access reviews that run quarterly on 500 accounts need automation, not spreadsheets.
- Evidence collection before an audit is usually the most stressful part. Scripting the export and analysis cuts that down significantly.
- Compliance mapping across 4+ frameworks by hand is where mistakes happen. A tool catches the gaps.

These are the kinds of tasks I have automated or plan to automate using n8n and Python in my day-to-day work.
