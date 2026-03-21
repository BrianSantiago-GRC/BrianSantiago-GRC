# Access Control Policy

**Framework:** NIST SP 800-53 Rev. 5 / ISO 27001:2022 (Annex A 5.15-5.18)

**Version:** 1.0

**Effective Date:** 2026-01-15

**Review Cycle:** Annual

**Owner:** IT Security

---

## 1. Purpose

Define requirements for managing logical and physical access to organizational information systems and data, ensuring that access is granted based on business need and least privilege.

---

## 2. Scope

Applies to all systems, applications, and data repositories across the organization, including on-premises infrastructure, cloud services (Azure AD, M365), and third-party platforms.

---

## 3. Access Control Requirements

### 3.1 Account Management (AC-2)

| Event | Requirement | Timeline |
|-------|-------------|----------|
| New hire | Provisioned based on role via HR-to-AD sync | Within 24 hours of start date |
| Role change | Access modified to match new role; old access revoked | Within 48 hours |
| Termination | All access disabled | Within 24 hours (same day for involuntary) |
| Contractor onboarding | Time-limited account with defined expiration | Before access is needed |
| Orphan accounts | Identified and disabled via quarterly audit | Quarterly |

### 3.2 Least Privilege (AC-6)

- Users receive the minimum access necessary for their job function
- Administrative/privileged access requires separate accounts
- Privileged access is managed through Azure AD Privileged Identity Management (PIM) with just-in-time activation
- Standing admin access is not permitted for systems containing ePHI or student records

### 3.3 Role-Based Access Control (AC-3)

Access is assigned through predefined roles rather than individual permissions:

| Role Category | Access Level | Approval |
|--------------|-------------|----------|
| Standard user | Email, office apps, department file share | Automatic via HR sync |
| Clinical/health staff | EHR system, ePHI | Manager + Privacy Officer |
| Student records staff | SIS, FERPA-protected data | Manager + Registrar |
| IT operations | Infrastructure systems, admin tools | IT Director |
| IT security | SIEM, EDR, vulnerability scanner | CISO/Security Lead |

### 3.4 Authentication (IA-2, IA-5)

- Multi-factor authentication (MFA) is required for:
  - All remote access
  - All access to systems containing Restricted data
  - All administrative/privileged access
  - All cloud service access
- Passwords must meet the following requirements:
  - Minimum 14 characters
  - Not found in common password lists
  - Changed immediately if compromised
  - No forced periodic rotation (per NIST SP 800-63B)
- Service accounts must use managed identities or certificate-based authentication where possible

### 3.5 Access Reviews (AC-2(j))

| Review Type | Frequency | Reviewer | Scope |
|------------|-----------|----------|-------|
| Privileged access | Quarterly | IT Security | Admin accounts, PIM roles |
| Application access | Quarterly | System owners | Users with access to Restricted data |
| General access | Semi-annually | Department managers | All user accounts in their department |
| Orphan account audit | Quarterly | IT Security | Accounts with no recent login (90+ days) |
| Third-party access | Annually | Compliance | Vendor and contractor accounts |

### 3.6 Remote Access (AC-17)

- Remote access requires VPN or approved zero-trust network access (ZTNA)
- Split tunneling is disabled for VPN connections
- Remote sessions to systems with Restricted data have a 15-minute idle timeout
- Personal devices are not permitted to access Restricted data unless enrolled in MDM

### 3.7 Separation of Duties (AC-5)

- No single individual can both approve and execute privileged changes
- Password resets for privileged accounts require identity verification by a second team member
- Firewall rule changes require approval from IT Security before implementation by IT Operations
- User provisioning is handled automatically via HR system; manual overrides require IT Director approval

---

## 4. Monitoring and Logging

- All access to systems containing Restricted data is logged
- Authentication events (success and failure) are forwarded to SIEM (Splunk)
- Failed login attempts trigger alerting after 5 consecutive failures
- Access logs are retained for a minimum of 90 days
- Privileged access usage is reviewed monthly

---

## 5. Non-Compliance

Unauthorized access attempts are treated as security incidents and handled per the Incident Response Plan. Intentional policy violations may result in disciplinary action.

---

## 6. References

- NIST SP 800-53 Rev. 5 (AC family)
- NIST SP 800-63B (Digital Identity Guidelines)
- ISO 27001:2022 Annex A (5.15 - Access Control, 5.16 - Identity Management, 5.17 - Authentication, 5.18 - Access Rights)
- HIPAA Security Rule (45 CFR 164.312(a) - Access Control)
- FERPA (34 CFR 99.31 - Disclosure without consent)
