"""
Access Review Audit Automation Tool
Reads a user access export (CSV) and flags accounts that violate
access control policies: orphan accounts, missing MFA, excessive
privileges, and separation of duties violations.

Designed for quarterly access reviews per NIST SP 800-53 (AC-2)
and HIPAA Security Rule (164.308(a)(3-4)).

Author: Brian Santiago
"""

import csv
import sys
import os
from datetime import datetime


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# -----------------------------------------------------------------------
# Policy thresholds
# -----------------------------------------------------------------------

INACTIVE_THRESHOLD_DAYS = 90
MFA_REQUIRED_DATA_TYPES = ["ePHI", "Student Records", "Full", "HR Records"]
MAX_PRIVILEGED_PERCENT = 10.0

# Departments where a user should NOT have access to certain data types
# (simplified separation of duties check)
SOD_RULES = [
    {"department": "Teaching", "forbidden_access": "HR Records", "reason": "Teachers should not access HR records"},
    {"department": "HR", "forbidden_access": "ePHI", "reason": "HR staff should not access clinical ePHI"},
    {"department": "Administration", "forbidden_access": "Full", "reason": "Admins should not have full system access"},
]


def load_users(filepath):
    """Load user data from CSV."""
    users = []
    with open(filepath, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["mfa_enabled"] = row.get("mfa_enabled", "").lower() in ("true", "yes", "1")
            row["privileged"] = row.get("privileged", "").lower() in ("true", "yes", "1")
            users.append(row)
    return users


def check_orphan_accounts(users):
    """Find accounts with no login activity past the threshold."""
    findings = []
    today = datetime.now()

    for user in users:
        if user.get("status", "").lower() != "active":
            continue
        last_login = user.get("last_login", "")
        if not last_login:
            findings.append({
                "check": "Orphan Account",
                "severity": "High",
                "username": user["username"],
                "detail": "No last login date recorded",
                "action": "Investigate with HR and disable if not needed",
            })
            continue

        try:
            login_date = datetime.strptime(last_login, "%Y-%m-%d")
            days_inactive = (today - login_date).days
            if days_inactive > INACTIVE_THRESHOLD_DAYS:
                findings.append({
                    "check": "Orphan Account",
                    "severity": "High",
                    "username": user["username"],
                    "detail": f"Inactive for {days_inactive} days (last login: {last_login})",
                    "action": "Disable account and verify employment status with HR",
                })
        except ValueError:
            findings.append({
                "check": "Orphan Account",
                "severity": "Medium",
                "username": user["username"],
                "detail": f"Cannot parse last login date: {last_login}",
                "action": "Fix data quality issue in source system",
            })

    return findings


def check_mfa_compliance(users):
    """Find users who access restricted data without MFA."""
    findings = []

    for user in users:
        if user.get("status", "").lower() != "active":
            continue
        data_access = user.get("data_access", "")
        if data_access in MFA_REQUIRED_DATA_TYPES and not user["mfa_enabled"]:
            sev = "Critical" if user["privileged"] else "High"
            findings.append({
                "check": "MFA Not Enabled",
                "severity": sev,
                "username": user["username"],
                "detail": f"Accesses {data_access} without MFA. Privileged: {user['privileged']}",
                "action": "Enable MFA immediately per access control policy",
            })

    return findings


def check_privilege_ratio(users):
    """Check if privileged accounts exceed the threshold."""
    findings = []
    active_users = [u for u in users if u.get("status", "").lower() == "active"]
    priv_users = [u for u in active_users if u["privileged"]]

    if not active_users:
        return findings

    priv_pct = len(priv_users) / len(active_users) * 100

    if priv_pct > MAX_PRIVILEGED_PERCENT:
        findings.append({
            "check": "Excessive Privileged Accounts",
            "severity": "Medium",
            "username": "N/A (systemic)",
            "detail": f"{len(priv_users)} of {len(active_users)} accounts are privileged ({priv_pct:.1f}%, threshold: {MAX_PRIVILEGED_PERCENT}%)",
            "action": "Review privileged accounts and downgrade where possible",
        })

    return findings


def check_separation_of_duties(users):
    """Check for SoD violations based on department/data access rules."""
    findings = []

    for user in users:
        if user.get("status", "").lower() != "active":
            continue
        for rule in SOD_RULES:
            if user.get("department", "") == rule["department"] and user.get("data_access", "") == rule["forbidden_access"]:
                findings.append({
                    "check": "Separation of Duties",
                    "severity": "High",
                    "username": user["username"],
                    "detail": f"{rule['reason']}. Department: {user['department']}, Access: {user['data_access']}",
                    "action": "Review access with department manager and remove if not justified",
                })

    return findings


def check_service_accounts(users):
    """Flag service accounts that may need review."""
    findings = []

    for user in users:
        role = user.get("role", "").lower()
        if "service" in role:
            if user["privileged"]:
                findings.append({
                    "check": "Service Account Review",
                    "severity": "Medium",
                    "username": user["username"],
                    "detail": f"Privileged service account: {user.get('display_name', user['username'])}",
                    "action": "Verify service account is still needed and uses managed identity or certificate auth",
                })

    return findings


def run_audit(filepath):
    """Run all access review checks and produce a report."""
    users = load_users(filepath)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    all_findings = []
    all_findings.extend(check_orphan_accounts(users))
    all_findings.extend(check_mfa_compliance(users))
    all_findings.extend(check_privilege_ratio(users))
    all_findings.extend(check_separation_of_duties(users))
    all_findings.extend(check_service_accounts(users))

    severity_order = {"Critical": 0, "High": 1, "Medium": 2, "Low": 3}
    all_findings.sort(key=lambda x: severity_order.get(x["severity"], 99))

    # Stats
    active_count = sum(1 for u in users if u.get("status", "").lower() == "active")
    priv_count = sum(1 for u in users if u["privileged"] and u.get("status", "").lower() == "active")
    mfa_count = sum(1 for u in users if u["mfa_enabled"] and u.get("status", "").lower() == "active")
    restricted_count = sum(1 for u in users if u.get("data_access", "") in MFA_REQUIRED_DATA_TYPES and u.get("status", "").lower() == "active")

    critical = sum(1 for f in all_findings if f["severity"] == "Critical")
    high = sum(1 for f in all_findings if f["severity"] == "High")
    medium = sum(1 for f in all_findings if f["severity"] == "Medium")

    # Output
    print(f"\n{'='*80}")
    print(f"  ACCESS REVIEW AUDIT REPORT")
    print(f"  Generated: {timestamp}")
    print(f"  Source: {filepath}")
    print(f"  Framework: NIST SP 800-53 (AC-2) / HIPAA 164.308(a)(3-4)")
    print(f"{'='*80}")

    print(f"\n  ACCOUNT STATISTICS")
    print(f"  {'-'*60}")
    print(f"  Total accounts reviewed:    {len(users)}")
    print(f"  Active accounts:            {active_count}")
    print(f"  Privileged accounts:        {priv_count} ({priv_count/active_count*100:.1f}% of active)")
    print(f"  MFA enabled:                {mfa_count} ({mfa_count/active_count*100:.1f}% of active)")
    print(f"  Restricted data access:     {restricted_count}")

    print(f"\n  AUDIT FINDINGS")
    print(f"  {'-'*60}")
    print(f"  Total findings:  {len(all_findings)}")
    print(f"    Critical:  {critical}")
    print(f"    High:      {high}")
    print(f"    Medium:    {medium}")

    if all_findings:
        print(f"\n  DETAILED FINDINGS")
        print(f"  {'-'*60}")
        for i, f in enumerate(all_findings, 1):
            print(f"  {i}. [{f['severity']}] {f['check']} - {f['username']}")
            print(f"     {f['detail']}")
            print(f"     Action: {f['action']}")
            print()

    # Pass/fail assessment
    print(f"  AUDIT RESULT")
    print(f"  {'-'*60}")
    if critical > 0:
        print(f"  Result: FAIL - {critical} critical finding(s) require immediate remediation")
    elif high > 0:
        print(f"  Result: CONDITIONAL PASS - {high} high finding(s) require remediation within 5 business days")
    else:
        print(f"  Result: PASS - No critical or high findings")

    print(f"\n{'='*80}")

    return all_findings


def main():
    if len(sys.argv) < 2:
        # Use built-in sample data for demonstration
        sample_path = os.path.join(SCRIPT_DIR, "sample_users.csv")
        if not os.path.exists(sample_path):
            # Generate sample file
            users = [
                {"username": "jsmith", "display_name": "John Smith", "department": "Nursing", "role": "Clinical Staff", "mfa_enabled": "True", "last_login": "2026-03-19", "status": "Active", "privileged": "False", "data_access": "ePHI"},
                {"username": "mjones", "display_name": "Mary Jones", "department": "Registrar", "role": "Records Clerk", "mfa_enabled": "True", "last_login": "2026-03-20", "status": "Active", "privileged": "False", "data_access": "Student Records"},
                {"username": "admin.tbrown", "display_name": "Tom Brown (Admin)", "department": "IT", "role": "System Admin", "mfa_enabled": "True", "last_login": "2026-03-20", "status": "Active", "privileged": "True", "data_access": "Full"},
                {"username": "kwilson", "display_name": "Karen Wilson", "department": "HR", "role": "HR Manager", "mfa_enabled": "True", "last_login": "2026-03-18", "status": "Active", "privileged": "False", "data_access": "HR Records"},
                {"username": "rgarcia", "display_name": "Robert Garcia", "department": "IT", "role": "Help Desk", "mfa_enabled": "True", "last_login": "2026-03-20", "status": "Active", "privileged": "False", "data_access": "Standard"},
                {"username": "ldavis", "display_name": "Lisa Davis", "department": "Teaching", "role": "Teacher", "mfa_enabled": "True", "last_login": "2026-03-17", "status": "Active", "privileged": "False", "data_access": "Student Records"},
                {"username": "pmartin", "display_name": "Paul Martin", "department": "IT", "role": "Network Admin", "mfa_enabled": "True", "last_login": "2026-03-20", "status": "Active", "privileged": "True", "data_access": "Full"},
                {"username": "jlee_old", "display_name": "James Lee", "department": "Teaching", "role": "Former Teacher", "mfa_enabled": "False", "last_login": "2025-11-30", "status": "Active", "privileged": "False", "data_access": "Student Records"},
                {"username": "svc_backup", "display_name": "Backup Service", "department": "IT", "role": "Service Account", "mfa_enabled": "False", "last_login": "2026-03-20", "status": "Active", "privileged": "True", "data_access": "Full"},
                {"username": "awhite", "display_name": "Amy White", "department": "Administration", "role": "Principal", "mfa_enabled": "True", "last_login": "2026-03-19", "status": "Active", "privileged": "False", "data_access": "Student Records"},
            ]
            with open(sample_path, "w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=users[0].keys())
                writer.writeheader()
                writer.writerows(users)
            print(f"  Generated sample data: {sample_path}")

        filepath = sample_path
    else:
        filepath = sys.argv[1]

    if not os.path.exists(filepath):
        print(f"Error: File not found: {filepath}")
        sys.exit(1)

    run_audit(filepath)


if __name__ == "__main__":
    main()
