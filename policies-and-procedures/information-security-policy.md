# Information Security Policy

**Framework:** ISO 27001:2022 / HIPAA Security Rule

**Version:** 1.0

**Effective Date:** 2026-01-15

**Review Cycle:** Annual

**Owner:** Information Security

---

## 1. Purpose

Establish the organization's commitment to protecting the confidentiality, integrity, and availability of information assets, including electronic protected health information (ePHI) and student education records.

---

## 2. Scope

This policy applies to:
- All employees, contractors, and third-party users with access to organizational systems
- All information assets including hardware, software, data, and network resources
- All locations where organizational data is processed, stored, or transmitted

---

## 3. Policy Statements

### 3.1 Information Classification

All data must be classified according to the four-level scheme (Restricted, Confidential, Internal, Public) defined in the Data Classification Policy. That policy is the authoritative source for classification levels, data type mappings, and handling requirements.

### 3.2 Access Control

- Access is granted based on the principle of least privilege
- Role-based access control (RBAC) is required for all systems containing Restricted or Confidential data
- Multi-factor authentication (MFA) is required for access to systems containing ePHI or student records
- Access is reviewed quarterly by system owners
- Access is revoked within 24 hours of role change or termination

Reference: Access Control Policy (separate document)

### 3.3 Acceptable Use

- Organizational systems are for authorized business purposes only
- Users must not attempt to access data or systems beyond their authorization
- Personal use of organizational systems is permitted only if it does not interfere with job duties or security
- Users must not install unauthorized software on organizational devices
- Users must lock workstations when unattended

### 3.4 Encryption

- ePHI and student records must be encrypted at rest using AES-256 or equivalent
- All data in transit must use TLS 1.2 or higher
- Full disk encryption is required on all laptops and mobile devices
- Encryption keys must be managed through a documented key management process

### 3.5 Incident Response

- All suspected security incidents must be reported to IT Security immediately
- Incident response follows the procedures in the Incident Response Plan (NIST SP 800-61)
- Breach notification timelines follow HIPAA (60 days) and state requirements
- Post-incident reviews are conducted for all confirmed incidents

Reference: Incident Response Plan (separate document)

### 3.6 Third-Party Security

- All vendors with access to Restricted data must complete a risk assessment before onboarding
- Business Associate Agreements (BAAs) are required for any vendor handling ePHI
- Vendor security posture is reassessed annually
- Contractual security requirements must address access controls, encryption, incident notification, and audit rights

Reference: Third-Party Risk Assessment Questionnaire (separate document)

### 3.7 Physical Security

- Server rooms and network closets require badge access with logging
- Visitor access to secure areas requires escort and sign-in
- Clean desk policy applies to all areas where Restricted data is handled
- Devices containing Restricted data must not be left unattended in public areas

### 3.8 Security Awareness

- All employees complete security awareness training within 30 days of hire
- Refresher training is required quarterly
- Phishing simulation exercises are conducted quarterly
- Role-specific training is required for IT staff and users with elevated privileges

---

## 4. Enforcement

Violations of this policy may result in disciplinary action up to and including termination. Violations involving regulatory data may also result in legal or regulatory consequences.

---

## 5. Exceptions

Exceptions to this policy require written approval from the CISO or designee with:
- Description of the exception and business justification
- Risk assessment of the exception
- Compensating controls in place
- Defined expiration date (maximum 12 months)

---

## 6. References

- ISO 27001:2022 (Clause 5.2 - Information Security Policy)
- HIPAA Security Rule (45 CFR 164.306 - Security Standards)
- FERPA (34 CFR Part 99)
- NIST SP 800-53 Rev. 5 (PL-1: Policy and Procedures)
