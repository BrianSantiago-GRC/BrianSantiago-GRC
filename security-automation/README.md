# Security Automation Practice

Small Python scripts for practicing security, GRC, and compliance operations workflows.

These are completed practice scripts. They use sanitized practice data and are meant to show how repetitive documentation or review tasks can be made more consistent. They do not represent live deployment work or organization-wide tooling.

---

## Project Purpose

The purpose of this folder is to practice simple automation concepts that support operational security and GRC work.

The focus is on repeatable logic, readable output, and documentation discipline rather than advanced engineering.

---

## Tools Used

- Python standard library
- Sanitized CSV practice data
- Markdown documentation
- Sanitized GRC/security operations scenarios

No external Python packages are required.

---

## What I Practiced

- Reading sanitized CSV practice data.
- Applying simple risk scoring logic.
- Reviewing sanitized access data for common issues.
- Generating basic compliance or evidence reports.
- Thinking through how scripts can reduce repetitive manual review work.

---

## Scripts

| Script | Purpose | Practice Area |
|---|---|---|
| `risk_scorer.py` | Reads a sanitized risk register and calculates basic inherent/residual risk scores | Risk management basics |
| `evidence_collector.py` | Simulates collecting access, training, and patch evidence from sanitized practice data | Audit evidence support |
| `access_review_audit.py` | Reviews sanitized user access data for common access review issues | IAM / access review practice |
| `compliance_checker.py` | Reviews sanitized control mapping data and highlights control gaps | GRC control tracking |

---

## Example Usage

```bash
python3 risk_scorer.py
python3 evidence_collector.py ./output/
python3 access_review_audit.py
python3 compliance_checker.py
```

---

## Skills Demonstrated

- Basic Python scripting.
- CSV parsing and structured output.
- Risk scoring logic.
- Access review support concepts.
- Evidence collection thinking.
- Control gap documentation.
- Practical process improvement.

---

## Lessons Learned

- Automation is most useful when the manual process is already understood.
- Small scripts can make review work more consistent.
- Output should be easy for another person to understand.
- Practice data should be clearly labeled so it is not confused with real evidence.

---

## Screenshots / Evidence

Screenshots are not included yet.

Planned additions:

- Script output.
- Example risk scoring report.
- Example access review findings.
- Example compliance summary output.

---

## Future Improvements

- Add completed output files.
- Add screenshots of each script run.
- Add clearer input CSV examples.
- Add short notes explaining how each script could support IT security, GRC, or compliance operations.

---

## Limitations

- Sanitized practice data only.
- No live system connections.
- No production deployment.
- No claim of advanced automation engineering.
