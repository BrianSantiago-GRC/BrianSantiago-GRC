# GRC Key Performance Indicators and Key Risk Indicators

**Purpose:** Define measurable metrics for tracking the effectiveness of the security and compliance program

**Audience:** IT Security, Compliance, IT Leadership

**Review Cycle:** Monthly reporting, quarterly trending

**Last Updated:** 2026-03-01

---

## KPI vs KRI

- **KPI (Key Performance Indicator):** Measures how well a control or process is performing. Tells you if you are doing things right.
- **KRI (Key Risk Indicator):** Measures changes in risk exposure. Tells you if risk is increasing or decreasing.

Both are needed. A control can be performing well (KPI green) while the threat landscape shifts and risk increases (KRI yellow).

---

## Vulnerability Management

| Metric | Type | Target | Red Threshold | Source | Frequency |
|--------|------|--------|--------------|--------|-----------|
| Critical/High patch compliance within SLA | KPI | >= 95% | < 80% | Qualys + NinjaOne | Monthly |
| Mean time to remediate (critical) | KPI | < 14 days | > 30 days | Qualys | Monthly |
| Open critical vulnerabilities | KRI | 0 | > 3 | Qualys | Weekly |
| Total open vulnerabilities | KRI | Trend decreasing | Trend increasing for 3+ months | Qualys | Monthly |
| CISA KEV findings open past deadline | KRI | 0 | > 0 | Qualys + CISA KEV | Weekly |
| Patch exception count | KRI | < 5 active | > 10 active | Exception log | Monthly |

---

## Access Control

| Metric | Type | Target | Red Threshold | Source | Frequency |
|--------|------|--------|--------------|--------|-----------|
| Access review completion rate | KPI | 100% on schedule | < 90% | Review records | Quarterly |
| Orphan accounts found per quarter | KRI | < 5 | > 10 | AD audit | Quarterly |
| Time to revoke terminated employee access | KPI | < 24 hours | > 48 hours | HR-AD sync logs | Monthly |
| Privileged accounts as % of total accounts | KRI | < 5% | > 10% | Azure AD | Quarterly |
| MFA enrollment rate | KPI | 100% for Restricted data access | < 95% | Azure AD | Monthly |
| Failed login attempts (anomalous) | KRI | Baseline normal | > 2x baseline | Splunk | Weekly |

---

## Incident Response

| Metric | Type | Target | Red Threshold | Source | Frequency |
|--------|------|--------|--------------|--------|-----------|
| Mean time to detect (MTTD) | KPI | < 24 hours | > 72 hours | SIEM + incident log | Monthly |
| Mean time to contain (MTTC) | KPI | < 4 hours (SEV-1/2) | > 12 hours | Incident log | Per incident |
| Incidents by severity | KRI | Trend stable or decreasing | Increasing SEV-1/2 trend | Incident log | Monthly |
| Tabletop exercises completed | KPI | 4 per year (quarterly) | < 2 per year | Exercise records | Quarterly |
| Post-incident review completion rate | KPI | 100% for SEV-1/2 | < 100% | IR records | Per incident |
| Repeat incidents (same root cause) | KRI | 0 | > 1 | Incident log | Quarterly |

---

## Compliance

| Metric | Type | Target | Red Threshold | Source | Frequency |
|--------|------|--------|--------------|--------|-----------|
| Policy review currency (% reviewed within 12 months) | KPI | 100% | < 90% | Policy register | Quarterly |
| Open audit findings | KRI | Trend decreasing | Increasing or stale findings | Audit tracker | Monthly |
| Audit finding closure within SLA | KPI | >= 90% | < 75% | Audit tracker | Monthly |
| HIPAA training completion rate | KPI | 100% | < 95% | LMS | Quarterly |
| BAA coverage for ePHI vendors | KPI | 100% | < 100% | Vendor inventory | Quarterly |
| Regulatory change items unaddressed | KRI | 0 past due | > 0 past 30 days | Regulatory tracker | Monthly |

---

## Third-Party Risk

| Metric | Type | Target | Red Threshold | Source | Frequency |
|--------|------|--------|--------------|--------|-----------|
| Tier 1 vendor assessments current | KPI | 100% | < 100% | TPRM tracker | Quarterly |
| Tier 2 vendor assessments current | KPI | 100% | < 80% | TPRM tracker | Quarterly |
| Vendor incidents reported | KRI | Track trend | Increasing trend | Vendor notifications | Monthly |
| Vendors without current SOC 2 (Tier 1) | KRI | 0 | > 0 | TPRM tracker | Annually |

---

## Security Awareness

| Metric | Type | Target | Red Threshold | Source | Frequency |
|--------|------|--------|--------------|--------|-----------|
| Phishing simulation click rate | KRI | < 5% | > 15% | Phishing platform | Quarterly |
| Phishing report rate | KPI | > 50% | < 25% | Phishing platform | Quarterly |
| Security training completion rate | KPI | >= 95% within 30 days | < 85% | LMS | Quarterly |
| Reported security events by users | KPI | Trend increasing (means people are reporting) | Sudden drop | Help desk | Monthly |

---

## Risk Management

| Metric | Type | Target | Red Threshold | Source | Frequency |
|--------|------|--------|--------------|--------|-----------|
| Average residual risk score | KRI | Trend stable or decreasing | Increasing for 2+ quarters | Risk register | Quarterly |
| Risks at Critical level (residual) | KRI | 0 | > 0 | Risk register | Quarterly |
| Risk treatment plans overdue | KPI | 0 | > 2 | Risk register | Monthly |
| Risk assessment completion | KPI | Annual + event-driven | Overdue | Risk register | Annually |
| Overall risk reduction % | KPI | >= 25% | < 15% | Risk scoring tool | Quarterly |

---

## Reporting

### Monthly Report (to IT Director)
- Vulnerability management KPIs and KRIs
- Incident summary (count, severity, MTTD, MTTC)
- Access control metrics
- Any red-threshold items with action plans

### Quarterly Report (to Leadership)
- Full KPI/KRI dashboard across all areas
- Trend analysis (this quarter vs. previous 2 quarters)
- Risk register summary (critical and high risks)
- Compliance program status
- Recommendations and resource requests

---

## How to Use These Metrics

1. Collect data from source systems on the defined frequency
2. Compare against targets and red thresholds
3. Investigate any metric that crosses the red threshold
4. Report trends, not just snapshots. A single bad month is different from a 3-month trend.
5. Use metrics to justify resource requests. "Our MTTR for critical patches is 22 days against a 14-day target because we have one person patching 400 endpoints" is more effective than "we need more staff."
