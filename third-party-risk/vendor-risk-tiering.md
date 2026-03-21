# Vendor Risk Tiering Framework

**Framework:** ISO 27001:2022 (A.5.19-5.22) / NIST SP 800-161

**Purpose:** Classify vendors by risk level to determine the appropriate depth of security assessment and ongoing monitoring

**Last Updated:** 2026-02-01

---

## Tiering Criteria

Vendors are tiered based on two factors: **data sensitivity** and **access level**.

### Data Sensitivity

| Level | Description | Examples |
|-------|-------------|---------|
| High | Vendor accesses or stores Restricted data (ePHI, student records, PII) | EHR vendor, SIS vendor, cloud storage for student data |
| Medium | Vendor accesses Confidential data but not Restricted | HR SaaS platform, financial system, IT management tools |
| Low | Vendor has no access to sensitive data; provides commoditized services | Office supplies, janitorial, marketing |

### Access Level

| Level | Description | Examples |
|-------|-------------|---------|
| High | Direct access to production systems or data | SaaS platform hosting our data, managed service provider |
| Medium | Indirect access (network connectivity, support access) | IT support vendor, HVAC vendor with network access |
| Low | No system or network access | Consulting, training, physical-only services |

---

## Tier Matrix

|  | Access: High | Access: Medium | Access: Low |
|--|-------------|---------------|-------------|
| **Data: High** | Tier 1 (Critical) | Tier 1 (Critical) | Tier 2 (High) |
| **Data: Medium** | Tier 2 (High) | Tier 2 (High) | Tier 3 (Standard) |
| **Data: Low** | Tier 3 (Standard) | Tier 3 (Standard) | Tier 4 (Low) |

---

## Assessment Requirements by Tier

| Requirement | Tier 1 (Critical) | Tier 2 (High) | Tier 3 (Standard) | Tier 4 (Low) |
|------------|-------------------|---------------|-------------------|-------------|
| Full security questionnaire | Yes | Yes | Abbreviated | No |
| SOC 2 or ISO 27001 report required | Yes | Preferred | No | No |
| BAA required | Yes (if ePHI) | If applicable | No | No |
| On-site or virtual assessment | If no SOC 2/ISO cert | No | No | No |
| Contractual security clauses | Detailed | Standard | Basic | Standard terms |
| Incident notification SLA | 24 hours | 48 hours | 72 hours | N/A |
| Right to audit clause | Required | Required | Preferred | N/A |
| Reassessment frequency | Annual | Annual | Every 2 years | At renewal |
| Continuous monitoring | Yes (if available) | Recommended | No | No |

---

## Current Vendor Inventory (Sample)

| Vendor | Service | Data Sensitivity | Access Level | Tier | BAA | Last Assessment | Next Due |
|--------|---------|-----------------|-------------|------|-----|----------------|----------|
| EHR Vendor | Electronic health records | High | High | 1 | Yes | 2025-11-01 | 2026-11-01 |
| SIS Platform | Student information system | High | High | 1 | N/A (FERPA) | 2025-09-15 | 2026-09-15 |
| Cloud Email (M365) | Email and collaboration | High | High | 1 | Yes | 2025-10-01 | 2026-10-01 |
| Qualys | Vulnerability management | Medium | Medium | 2 | No | 2025-08-01 | 2026-08-01 |
| NinjaOne | Endpoint management | Medium | High | 2 | No | 2025-07-15 | 2026-07-15 |
| Splunk Cloud | SIEM | Medium | Medium | 2 | No | 2025-09-01 | 2026-09-01 |
| Copier Vendor | Print services | Low | Low | 4 | No | N/A | At renewal |

---

## Reassessment Triggers

Beyond the scheduled reassessment cycle, reassess a vendor when:

- The vendor reports a security incident or breach
- The vendor changes their subprocessors
- The scope of data shared with the vendor changes
- A significant vulnerability is reported in the vendor's platform
- Contract renewal (always reassess at renewal)

---

## References

- ISO 27001:2022 Annex A (5.19-5.22)
- NIST SP 800-161 Rev. 1 - Supply Chain Risk Management
- HIPAA Security Rule (164.308(b))
