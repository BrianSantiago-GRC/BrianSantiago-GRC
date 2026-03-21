# Patch Management Policy

**Framework:** NIST SP 800-40 Rev. 4 / ISO 27001:2022 (Annex A 8.8)

**Version:** 1.0

**Effective Date:** 2026-01-15

**Review Cycle:** Annual

**Owner:** IT Operations

---

## 1. Purpose

Establish requirements for the timely identification, testing, and deployment of security patches across all organizational systems to reduce exposure to known vulnerabilities.

---

## 2. Scope

All operating systems, applications, firmware, and network device software managed by the organization, including on-premises infrastructure, cloud-hosted systems, and endpoints.

---

## 3. Patching Timelines

| Severity (CVSS) | Classification | Patching SLA | Testing Required |
|-----------------|---------------|--------------|-----------------|
| Critical (9.0-10.0) | Emergency | 14 days | Abbreviated (24-48 hours) |
| High (7.0-8.9) | Urgent | 30 days | Standard |
| Medium (4.0-6.9) | Routine | 60 days | Standard |
| Low (0.1-3.9) | Scheduled | 90 days | Standard or bundled |
| Zero-day (actively exploited) | Emergency | 72 hours | Emergency testing or compensating control |

---

## 4. Patch Management Process

### 4.1 Identification
- Vulnerability scans run weekly via Qualys
- Vendor security advisories monitored daily (Microsoft, Linux distros, network vendors)
- CISA Known Exploited Vulnerabilities (KEV) catalog reviewed weekly
- NinjaOne patch status dashboard reviewed daily by IT Operations

### 4.2 Assessment
- IT Operations reviews scan results and assigns severity
- Patches affecting Restricted data systems are prioritized
- Dependencies and potential conflicts documented before deployment

### 4.3 Testing
- Patches tested on a representative subset of systems before broad deployment
- Emergency patches may use abbreviated testing with documented risk acceptance
- Test results documented with pass/fail and any issues noted

### 4.4 Deployment
- Patches deployed via automated tools (NinjaOne for endpoints, WSUS/SCCM for servers)
- Deployment windows:
  - Endpoints: automated deployment during maintenance window (weekends)
  - Servers: scheduled change window with change management approval
  - Network devices: manual deployment with change ticket

### 4.5 Verification
- Post-deployment scan confirms patch application
- Failed patches are flagged for manual remediation
- Compliance metrics reported monthly

---

## 5. Exceptions

If a patch cannot be applied within the SLA:

1. Document the business justification
2. Identify and implement compensating controls
3. Obtain IT Director approval
4. Set a revised remediation date (maximum 30 days beyond original SLA)
5. Track in the vulnerability management exception log

---

## 6. Metrics

| Metric | Target | Measured |
|--------|--------|----------|
| Critical/High patch compliance within SLA | 95% | Monthly |
| Mean time to patch (critical) | < 14 days | Monthly |
| Systems with outstanding critical patches | 0 | Weekly |
| Exception count | < 5 active | Monthly |

---

## 7. References

- NIST SP 800-40 Rev. 4 - Guide to Enterprise Patch Management Planning
- ISO 27001:2022 Annex A (8.8 - Management of Technical Vulnerabilities)
- HIPAA Security Rule (45 CFR 164.308(a)(5)(ii)(B))
- CISA Known Exploited Vulnerabilities Catalog
