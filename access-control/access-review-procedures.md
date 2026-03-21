# Access Review Procedures

**Framework:** NIST SP 800-53 (AC-2) / ISO 27001:2022 (A.5.18)

**Purpose:** Define the procedures for conducting periodic access reviews to verify that user access remains appropriate and aligned with job responsibilities

**Owner:** IT Security

**Last Updated:** 2026-02-15

---

## Review Schedule

| Review Type | Frequency | Reviewer | Scope | Tool |
|------------|-----------|----------|-------|------|
| Privileged access review | Quarterly | IT Security | All accounts with admin, PIM, or elevated roles | Azure AD PIM report |
| Application access review | Quarterly | System/data owners | Users with access to Restricted data systems (EHR, SIS) | Application user export |
| General access review | Semi-annually | Department managers | All user accounts in their department | AD group membership report |
| Orphan account audit | Quarterly | IT Security | Accounts with no login in 90+ days | AD last logon report |
| Service account review | Semi-annually | IT Operations | All service accounts and their permissions | AD service account inventory |
| Third-party/contractor access | Quarterly | Compliance | All active vendor and contractor accounts | Contractor account list |

---

## Privileged Access Review Procedure

### Preparation (IT Security)
1. Export Azure AD PIM role assignments (active and eligible)
2. Export local admin group memberships from all servers
3. Export domain admin, enterprise admin, and schema admin group membership
4. Compile into a review spreadsheet with: username, role, assignment date, last activation (PIM), justification

### Review (IT Security + IT Director)
1. For each privileged account, verify:
   - Is the user still employed and in a role that requires this access?
   - Has the account been used in the past 90 days?
   - Is there documented justification for the privilege level?
   - Are separate admin and standard accounts maintained?
2. Flag any account that fails any of the above checks
3. Decision for flagged accounts: revoke, downgrade, or document justification for retention

### Follow-up
1. Revoke or modify flagged accounts within 5 business days
2. Document all review decisions and actions
3. Store review evidence (spreadsheet + decisions) for audit

---

## Application Access Review Procedure (Restricted Data Systems)

### Preparation (IT Security)
1. Request user access report from EHR system administrator
2. Request user access report from SIS administrator
3. Cross-reference with HR active employee list
4. Cross-reference with role-based access matrix

### Review (System/Data Owners)
1. For each user with access to the application:
   - Confirm the user's current role still requires access
   - Confirm the access level is appropriate (read-only vs. read/write vs. admin)
   - Verify that terminated or transferred employees have been removed
2. Flag users with access that exceeds their job function
3. Flag any accounts not tied to an active employee record

### Follow-up
1. Remove or modify flagged access within 5 business days
2. Investigate how inappropriate access was granted (process gap or manual override?)
3. Document findings and corrective actions

---

## Orphan Account Audit Procedure

### Identification (IT Security)
1. Query Active Directory for accounts with last logon date > 90 days
2. Exclude known exceptions: service accounts, break-glass accounts, seasonal staff
3. Cross-reference with HR termination list for the past 6 months
4. Cross-reference with long-term leave list (FMLA, sabbatical)

### Action
| Finding | Action | Timeline |
|---------|--------|----------|
| Terminated employee, account still active | Disable immediately | Same day |
| Account inactive 90+ days, employee still active | Contact manager to verify need | 5 business days |
| Account inactive 90+ days, no HR match | Disable and investigate | Same day |
| Seasonal/temporary account past expected end date | Disable | Same day |

### Documentation
- Record all orphan accounts found, action taken, and date
- Track trends: are orphan accounts increasing? Is the HR-AD sync working?

---

## Review Evidence Template

Each review cycle produces the following evidence package:

```
access-review-[date]/
  review-scope.txt              (what was reviewed and why)
  user-access-export.csv        (raw data from system)
  review-decisions.csv          (approved/revoked/modified for each account)
  remediation-actions.csv       (what was changed and when)
  reviewer-signoff.txt          (reviewer name, date, signature)
```

---

## Metrics

| Metric | Target | Measured |
|--------|--------|----------|
| Review completion rate | 100% on schedule | Quarterly |
| Accounts flagged for removal | Track trend | Quarterly |
| Orphan accounts found | <5 per quarter | Quarterly |
| Time to remediate flagged accounts | <5 business days | Per review |
| Percentage of reviews with documented evidence | 100% | Quarterly |

---

## References

- NIST SP 800-53 Rev. 5 (AC-2 - Account Management)
- ISO 27001:2022 Annex A (5.18 - Access Rights)
- HIPAA Security Rule (164.308(a)(3) - Workforce Security, 164.308(a)(4) - Information Access Management)
- FERPA (34 CFR 99.31)
