# NIST CSF 2.0 Maturity Assessment

**Framework:** NIST Cybersecurity Framework 2.0

**Scope:** K-12 organization processing HIPAA and FERPA regulated data

**Assessment Date:** 2026-01-20

**Assessor:** Brian Santiago

---

## Assessment Methodology

Each subcategory is rated on a 1-5 maturity scale:

| Level | Label | Description |
|-------|-------|-------------|
| 1 | Initial | Ad hoc; no formal process |
| 2 | Developing | Some processes documented but inconsistently applied |
| 3 | Defined | Processes documented, standardized, and communicated |
| 4 | Managed | Processes measured and monitored with metrics |
| 5 | Optimizing | Continuous improvement based on data and lessons learned |

---

## Assessment Results

### GOVERN (GV)

| Subcategory | Control Area | Current | Target | Gap | Notes |
|------------|-------------|---------|--------|-----|-------|
| GV.OC-01 | Organizational context understood | 3 | 4 | 1 | Mission and stakeholder needs documented |
| GV.OC-02 | Internal stakeholders understood | 3 | 3 | 0 | Roles defined; RACI in place |
| GV.OC-03 | Legal/regulatory requirements | 3 | 4 | 1 | HIPAA and FERPA mapped; need formal regulatory tracking |
| GV.RM-01 | Risk management objectives | 3 | 4 | 1 | Risk appetite defined; needs leadership revalidation |
| GV.RM-02 | Risk appetite determined | 2 | 3 | 1 | Informal; needs formal documentation |
| GV.SC-01 | Supply chain risk program | 2 | 3 | 1 | Vendor assessments exist; no formal program |
| GV.RR-01 | Roles and responsibilities | 3 | 3 | 0 | Documented in policies |

**GV Average: 2.7 / Target: 3.4**

### IDENTIFY (ID)

| Subcategory | Control Area | Current | Target | Gap | Notes |
|------------|-------------|---------|--------|-----|-------|
| ID.AM-01 | Hardware asset inventory | 3 | 4 | 1 | NinjaOne for endpoints; network devices tracked manually |
| ID.AM-02 | Software asset inventory | 2 | 3 | 1 | Partial; needs centralized CMDB |
| ID.AM-03 | Data flow mapping | 2 | 3 | 1 | ePHI flows documented; other data flows incomplete |
| ID.RA-01 | Vulnerabilities identified | 3 | 4 | 1 | Qualys scans monthly; need continuous scanning |
| ID.RA-02 | Threat intelligence received | 2 | 3 | 1 | CISA alerts reviewed; no formal TI feed |
| ID.RA-03 | Threats identified | 3 | 3 | 0 | Risk register includes threat sources |
| ID.RA-04 | Risk assessment performed | 3 | 4 | 1 | NIST 800-30 methodology in place |
| ID.IM-01 | Improvement opportunities | 2 | 3 | 1 | Post-incident reviews done; no formal program |

**ID Average: 2.5 / Target: 3.4**

### PROTECT (PR)

| Subcategory | Control Area | Current | Target | Gap | Notes |
|------------|-------------|---------|--------|-----|-------|
| PR.AA-01 | Identity management | 3 | 4 | 1 | AD with HR sync; PIM for privileged roles |
| PR.AA-02 | Authentication | 3 | 4 | 1 | MFA deployed; need conditional access policies |
| PR.AA-03 | Access control | 3 | 3 | 0 | RBAC implemented; quarterly reviews |
| PR.AT-01 | Security awareness training | 3 | 4 | 1 | Quarterly training; need phishing sim metrics |
| PR.DS-01 | Data-at-rest protection | 3 | 3 | 0 | Full disk encryption; database encryption |
| PR.DS-02 | Data-in-transit protection | 3 | 3 | 0 | TLS 1.2+ enforced |
| PR.PS-01 | Configuration management | 2 | 3 | 1 | Baselines exist but not consistently enforced |
| PR.IR-01 | Audit log management | 3 | 4 | 1 | Splunk deployed; need longer retention |

**PR Average: 2.9 / Target: 3.5**

### DETECT (DE)

| Subcategory | Control Area | Current | Target | Gap | Notes |
|------------|-------------|---------|--------|-----|-------|
| DE.CM-01 | Network monitoring | 2 | 3 | 1 | Basic monitoring; SIEM alerting for critical events |
| DE.CM-02 | Physical environment monitoring | 2 | 3 | 1 | Badge access logging; no camera integration |
| DE.CM-03 | Personnel activity monitoring | 2 | 3 | 1 | Admin activity logged; need user behavior analytics |
| DE.AE-01 | Anomaly/event analysis | 2 | 3 | 1 | Manual review; need automated correlation rules |
| DE.AE-02 | Event correlation | 2 | 3 | 1 | Splunk rules basic; need tuning |

**DE Average: 2.0 / Target: 3.0**

### RESPOND (RS)

| Subcategory | Control Area | Current | Target | Gap | Notes |
|------------|-------------|---------|--------|-----|-------|
| RS.MA-01 | Incident management | 3 | 4 | 1 | IR plan documented; playbooks in place |
| RS.MA-02 | Incident reporting | 3 | 3 | 0 | Reporting procedures defined |
| RS.AN-01 | Incident analysis | 2 | 3 | 1 | Basic analysis; need formal forensics capability |
| RS.CO-01 | Incident communication | 3 | 3 | 0 | Notification procedures in place |
| RS.MI-01 | Incident mitigation | 3 | 3 | 0 | Containment procedures documented |

**RS Average: 2.8 / Target: 3.2**

### RECOVER (RC)

| Subcategory | Control Area | Current | Target | Gap | Notes |
|------------|-------------|---------|--------|-----|-------|
| RC.RP-01 | Recovery planning | 3 | 3 | 0 | Backup and recovery procedures documented |
| RC.RP-02 | Recovery execution | 2 | 3 | 1 | Monthly restore tests; need full DR test |
| RC.CO-01 | Recovery communication | 2 | 3 | 1 | Informal; need formal communication plan |

**RC Average: 2.3 / Target: 3.0**

---

## Summary

| Function | Current Avg | Target Avg | Gap |
|----------|------------|------------|-----|
| GOVERN | 2.7 | 3.4 | 0.7 |
| IDENTIFY | 2.5 | 3.4 | 0.9 |
| PROTECT | 2.9 | 3.5 | 0.6 |
| DETECT | 2.0 | 3.0 | 1.0 |
| RESPOND | 2.8 | 3.2 | 0.4 |
| RECOVER | 2.3 | 3.0 | 0.7 |
| **Overall** | **2.5** | **3.3** | **0.7** |

---

## Priority Improvement Areas

1. **DETECT** (Gap: 1.0) - Deploy automated correlation rules in Splunk; add user behavior analytics; integrate network monitoring with SIEM
2. **IDENTIFY** (Gap: 0.9) - Build centralized software inventory; complete data flow mapping for all Restricted data; implement continuous vulnerability scanning
3. **GOVERN** (Gap: 0.7) - Formalize risk appetite documentation; establish regulatory change tracking process; build supply chain risk management program
4. **RECOVER** (Gap: 0.7) - Conduct annual full DR test; document recovery communication plan with stakeholder contact list

---

## References

- NIST Cybersecurity Framework 2.0 (February 2024)
- NIST SP 800-53 Rev. 5 (supporting control references)
