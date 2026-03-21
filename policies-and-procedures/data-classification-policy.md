# Data Classification Policy

**Framework:** NIST SP 800-60 / ISO 27001:2022 (Annex A 5.12-5.13)

**Version:** 1.0

**Effective Date:** 2026-01-15

**Review Cycle:** Annual

**Owner:** Compliance / IT Security

---

## 1. Purpose

Define a data classification scheme to ensure information is protected according to its sensitivity and regulatory requirements. This policy supports compliance with HIPAA and FERPA by establishing clear handling rules for each data type.

---

## 2. Scope

Applies to all data created, received, stored, processed, or transmitted by the organization in any format (digital or physical).

---

## 3. Classification Levels

| Level | Label | Definition | Regulatory Driver |
|-------|-------|------------|-------------------|
| 1 | **Restricted** | Data that would cause severe harm if disclosed; subject to legal or regulatory protection | HIPAA (ePHI), FERPA (education records), PCI DSS (cardholder data) |
| 2 | **Confidential** | Sensitive business data not intended for public disclosure | Employment records, financial data, IT infrastructure details |
| 3 | **Internal** | General business data for internal use | Policies, procedures, internal communications |
| 4 | **Public** | Information approved for unrestricted access | Published content, marketing materials, public notices |

---

## 4. Data Types and Classification

| Data Type | Classification | Regulatory Basis | Examples |
|-----------|---------------|------------------|----------|
| Electronic Protected Health Information (ePHI) | Restricted | HIPAA | Student health records, immunization records, nurse visit notes |
| Student Education Records | Restricted | FERPA | Grades, transcripts, disciplinary records, IEPs |
| Personally Identifiable Information (PII) | Restricted | State privacy laws | SSNs, dates of birth, addresses (when combined with name) |
| Employee HR Records | Confidential | Employment law | Performance reviews, salary data, background checks |
| Financial Records | Confidential | Internal policy | Budgets, vendor contracts, purchase orders |
| IT Configuration Data | Confidential | Security best practice | Network diagrams, firewall rules, system credentials |
| Policies and Procedures | Internal | N/A | SOPs, training materials, meeting agendas |
| Public Communications | Public | N/A | Website content, board meeting minutes (approved), press releases |

---

## 5. Handling Requirements

| Requirement | Restricted | Confidential | Internal | Public |
|------------|-----------|--------------|----------|--------|
| Encryption at rest | Required (AES-256) | Required | Recommended | Not required |
| Encryption in transit | Required (TLS 1.2+) | Required | Recommended | Not required |
| Access control | RBAC + MFA | RBAC | Authentication | None |
| Logging | All access logged | Modification logged | Not required | Not required |
| Sharing (internal) | Need-to-know only | Need-to-know | Available to staff | Available to all |
| Sharing (external) | Prohibited without authorization + BAA/DUA | Prohibited without approval | Not recommended | Permitted |
| Retention | Per retention schedule + regulatory minimum | Per retention schedule | Per retention schedule | No limit |
| Disposal | Secure deletion (NIST SP 800-88) | Secure deletion | Standard deletion | Standard deletion |
| Labeling | Required on documents and systems | Recommended | Optional | Not required |
| Backup | Encrypted backups required | Encrypted backups required | Standard backup | Not required |

---

## 6. Roles and Responsibilities

| Role | Responsibility |
|------|---------------|
| Data Owner | Classifies data; approves access; reviews classification annually |
| Data Custodian | Implements technical controls per classification requirements |
| Data User | Handles data according to its classification; reports mishandling |
| Compliance | Validates classification against regulatory requirements |
| IT Security | Monitors compliance with handling requirements; investigates incidents |

---

## 7. Classification Review

- Data owners must review classifications annually or when:
  - Regulatory requirements change
  - Data use changes
  - A security incident involves the data
  - An audit finding relates to data handling

---

## 8. References

- NIST SP 800-60 Vol. 1 - Guide for Mapping Types of Information and Information Systems to Security Categories
- NIST SP 800-88 Rev. 1 - Guidelines for Media Sanitization
- ISO 27001:2022 Annex A (5.12 - Classification of Information, 5.13 - Labelling of Information)
- HIPAA Security Rule (45 CFR 164.312)
- FERPA (34 CFR Part 99)
