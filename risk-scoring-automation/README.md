# Risk Scoring Automation Tool

Python-based tool that automates GRC risk scoring using the **NIST SP 800-30** methodology. Reads a risk register from CSV, calculates inherent and residual risk scores, and generates a prioritized report with a risk heat map.

Built to demonstrate how GRC processes can be automated to improve consistency and reduce manual effort in risk assessment workflows.

## What It Does

- Parses a risk register CSV with likelihood, impact, and control effectiveness data
- Calculates **inherent risk** (likelihood x impact) on a 1-25 scale
- Applies **control effectiveness reduction** to compute residual risk scores
- Classifies risks into Low / Medium / High / Critical tiers
- Generates a **5x5 risk heat map** showing residual risk distribution
- Outputs a **prioritized top-risks list** for treatment planning
- Produces summary statistics including overall risk reduction percentage

## Scoring Methodology

| Rating | Likelihood | Impact |
|--------|-----------|--------|
| 1 | Very Low | Very Low |
| 2 | Low | Low |
| 3 | Moderate | Moderate |
| 4 | High | High |
| 5 | Very High | Very High |

**Inherent Risk** = Likelihood x Impact (range: 1-25)

**Residual Risk** = Inherent Risk x (1 - Control Effectiveness Reduction)

| Control Effectiveness | Reduction |
|----------------------|-----------|
| High | 40% |
| Medium | 25% |
| Low | 10% |
| None | 0% |

**Risk Levels:**
- **Low**: 1-4
- **Medium**: 5-9
- **High**: 10-16
- **Critical**: 17-25

## Usage

```bash
# Run with the included sample risk register
python3 risk_scorer.py

# Run with your own CSV
python3 risk_scorer.py your_risk_register.csv

# Save report to a file
python3 risk_scorer.py your_risk_register.csv output_report.txt
```

## CSV Format

Your risk register CSV needs these columns:

| Column | Description | Values |
|--------|-------------|--------|
| risk_id | Unique identifier | e.g. RISK-001 |
| risk_name | Short description of the risk | Free text |
| category | CIA triad category | Confidentiality, Integrity, Availability, Compliance |
| threat_source | Who or what causes the risk | e.g. External attacker, Insider |
| affected_asset | System or asset at risk | Free text |
| likelihood | Probability rating | 1-5 |
| impact | Impact severity rating | 1-5 |
| control_description | Existing mitigating controls | Free text |
| control_effectiveness | How effective the controls are | High, Medium, Low, None |
| status | Current risk status | Open, Closed, Accepted |
| owner | Risk owner | Free text |

## Sample Output

The tool generates a report with:
- Scored risk table with inherent and residual ratings
- Summary statistics (average scores, risk reduction percentage)
- 5x5 residual risk heat map
- Top 5 prioritized risks for treatment

## Frameworks

- **NIST SP 800-30** - Risk assessment methodology and scoring
- **NIST SP 800-37** - Risk Management Framework alignment
- **ISO 27005** - Information security risk management

## No Dependencies

Uses only Python standard library (csv, sys, os, datetime). No pip install required.
