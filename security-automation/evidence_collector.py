"""
GRC Evidence Collection Automation Tool
Generates an organized evidence package for audit preparation.
Simulates collecting evidence from common GRC data sources and
produces a structured output ready for auditor review.

In a production environment, this would connect to AD, SIEM, and
endpoint management APIs. This version works with CSV data files
to demonstrate the workflow and output format.

Framework: HIPAA Security Rule / ISO 27001:2022
Author: Brian Santiago
"""

import csv
import os
import sys
from datetime import datetime, timedelta
import json


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# -----------------------------------------------------------------------
# Sample data generators (replace with API calls in production)
# -----------------------------------------------------------------------

def generate_sample_users():
    """Sample user access data simulating an AD export."""
    return [
        {"username": "jsmith", "display_name": "John Smith", "department": "Nursing", "role": "Clinical Staff", "mfa_enabled": True, "last_login": "2026-03-19", "status": "Active", "privileged": False, "data_access": "ePHI"},
        {"username": "mjones", "display_name": "Mary Jones", "department": "Registrar", "role": "Records Clerk", "mfa_enabled": True, "last_login": "2026-03-20", "status": "Active", "privileged": False, "data_access": "Student Records"},
        {"username": "admin.tbrown", "display_name": "Tom Brown (Admin)", "department": "IT", "role": "System Admin", "mfa_enabled": True, "last_login": "2026-03-20", "status": "Active", "privileged": True, "data_access": "Full"},
        {"username": "kwilson", "display_name": "Karen Wilson", "department": "HR", "role": "HR Manager", "mfa_enabled": True, "last_login": "2026-03-18", "status": "Active", "privileged": False, "data_access": "HR Records"},
        {"username": "rgarcia", "display_name": "Robert Garcia", "department": "IT", "role": "Help Desk", "mfa_enabled": True, "last_login": "2026-03-20", "status": "Active", "privileged": False, "data_access": "Standard"},
        {"username": "ldavis", "display_name": "Lisa Davis", "department": "Teaching", "role": "Teacher", "mfa_enabled": True, "last_login": "2026-03-17", "status": "Active", "privileged": False, "data_access": "Student Records"},
        {"username": "pmartin", "display_name": "Paul Martin", "department": "IT", "role": "Network Admin", "mfa_enabled": True, "last_login": "2026-03-20", "status": "Active", "privileged": True, "data_access": "Full"},
        {"username": "jlee_old", "display_name": "James Lee", "department": "Teaching", "role": "Former Teacher", "mfa_enabled": False, "last_login": "2025-11-30", "status": "Active", "privileged": False, "data_access": "Student Records"},
        {"username": "svc_backup", "display_name": "Backup Service", "department": "IT", "role": "Service Account", "mfa_enabled": False, "last_login": "2026-03-20", "status": "Active", "privileged": True, "data_access": "Full"},
        {"username": "awhite", "display_name": "Amy White", "department": "Administration", "role": "Principal", "mfa_enabled": True, "last_login": "2026-03-19", "status": "Active", "privileged": False, "data_access": "Student Records"},
    ]


def generate_sample_training():
    """Sample training completion data."""
    return [
        {"username": "jsmith", "training": "HIPAA Security Awareness", "completed": "2026-01-15", "due": "2026-01-31", "status": "Completed"},
        {"username": "mjones", "training": "HIPAA Security Awareness", "completed": "2026-01-22", "due": "2026-01-31", "status": "Completed"},
        {"username": "admin.tbrown", "training": "HIPAA Security Awareness", "completed": "2026-01-10", "due": "2026-01-31", "status": "Completed"},
        {"username": "kwilson", "training": "HIPAA Security Awareness", "completed": "2026-01-28", "due": "2026-01-31", "status": "Completed"},
        {"username": "rgarcia", "training": "HIPAA Security Awareness", "completed": "2026-02-05", "due": "2026-01-31", "status": "Overdue"},
        {"username": "ldavis", "training": "HIPAA Security Awareness", "completed": "2026-01-20", "due": "2026-01-31", "status": "Completed"},
        {"username": "pmartin", "training": "HIPAA Security Awareness", "completed": "2026-01-12", "due": "2026-01-31", "status": "Completed"},
        {"username": "jlee_old", "training": "HIPAA Security Awareness", "completed": "", "due": "2026-01-31", "status": "Not Completed"},
        {"username": "awhite", "training": "HIPAA Security Awareness", "completed": "2026-01-25", "due": "2026-01-31", "status": "Completed"},
    ]


def generate_sample_patches():
    """Sample patch compliance data."""
    return [
        {"hostname": "SRV-EHR-01", "os": "Windows Server 2022", "critical_patches": 0, "high_patches": 1, "last_scan": "2026-03-18", "compliant": True, "data_type": "ePHI"},
        {"hostname": "SRV-SIS-01", "os": "Windows Server 2022", "critical_patches": 0, "high_patches": 0, "last_scan": "2026-03-18", "compliant": True, "data_type": "Student Records"},
        {"hostname": "SRV-AD-01", "os": "Windows Server 2022", "critical_patches": 0, "high_patches": 0, "last_scan": "2026-03-18", "compliant": True, "data_type": "Infrastructure"},
        {"hostname": "SRV-FILE-01", "os": "Windows Server 2022", "critical_patches": 1, "high_patches": 2, "last_scan": "2026-03-18", "compliant": False, "data_type": "Mixed"},
        {"hostname": "SRV-SPLUNK-01", "os": "Ubuntu 22.04", "critical_patches": 0, "high_patches": 0, "last_scan": "2026-03-18", "compliant": True, "data_type": "Logs"},
        {"hostname": "FW-EDGE-01", "os": "FortiOS 7.4", "critical_patches": 0, "high_patches": 1, "last_scan": "2026-03-15", "compliant": True, "data_type": "Infrastructure"},
        {"hostname": "WS-NURSE-01", "os": "Windows 11", "critical_patches": 0, "high_patches": 0, "last_scan": "2026-03-20", "compliant": True, "data_type": "ePHI"},
        {"hostname": "WS-OFFICE-12", "os": "Windows 11", "critical_patches": 0, "high_patches": 1, "last_scan": "2026-03-20", "compliant": True, "data_type": "Standard"},
    ]


# -----------------------------------------------------------------------
# Evidence collection functions
# -----------------------------------------------------------------------

def collect_access_evidence(users):
    """Analyze user access data and flag issues."""
    findings = []
    stats = {
        "total_users": len(users),
        "mfa_enabled": 0,
        "privileged_accounts": 0,
        "orphan_accounts": 0,
        "restricted_data_users": 0,
    }

    today = datetime.now()

    for user in users:
        if user["mfa_enabled"]:
            stats["mfa_enabled"] += 1
        if user["privileged"]:
            stats["privileged_accounts"] += 1
        if user["data_access"] in ("ePHI", "Student Records", "Full"):
            stats["restricted_data_users"] += 1

        # Check for orphan accounts (no login in 90+ days)
        if user["last_login"]:
            last_login = datetime.strptime(user["last_login"], "%Y-%m-%d")
            days_inactive = (today - last_login).days
            if days_inactive > 90:
                stats["orphan_accounts"] += 1
                findings.append({
                    "type": "ORPHAN_ACCOUNT",
                    "severity": "High",
                    "user": user["username"],
                    "detail": f"No login for {days_inactive} days. Last login: {user['last_login']}. Data access: {user['data_access']}",
                    "recommendation": "Disable account immediately and investigate with HR",
                })

        # Check for privileged accounts without MFA
        if user["privileged"] and not user["mfa_enabled"]:
            findings.append({
                "type": "PRIV_NO_MFA",
                "severity": "Critical",
                "user": user["username"],
                "detail": f"Privileged account without MFA. Role: {user['role']}",
                "recommendation": "Enable MFA immediately or convert to managed identity",
            })

        # Check for non-privileged restricted data access without MFA
        if user["data_access"] in ("ePHI", "Student Records") and not user["mfa_enabled"]:
            findings.append({
                "type": "RESTRICTED_NO_MFA",
                "severity": "High",
                "user": user["username"],
                "detail": f"Access to {user['data_access']} without MFA enabled",
                "recommendation": "Enable MFA per HIPAA/FERPA access control requirements",
            })

    stats["mfa_rate"] = f"{stats['mfa_enabled'] / stats['total_users'] * 100:.1f}%"
    stats["priv_rate"] = f"{stats['privileged_accounts'] / stats['total_users'] * 100:.1f}%"

    return stats, findings


def collect_training_evidence(training_records):
    """Analyze training completion data."""
    stats = {
        "total_assigned": len(training_records),
        "completed_on_time": 0,
        "completed_late": 0,
        "not_completed": 0,
    }
    findings = []

    for record in training_records:
        if record["status"] == "Completed":
            stats["completed_on_time"] += 1
        elif record["status"] == "Overdue":
            stats["completed_late"] += 1
            findings.append({
                "type": "LATE_TRAINING",
                "severity": "Medium",
                "user": record["username"],
                "detail": f"Completed training on {record['completed']} (due {record['due']})",
                "recommendation": "Monitor for timely completion next cycle",
            })
        else:
            stats["not_completed"] += 1
            findings.append({
                "type": "MISSING_TRAINING",
                "severity": "High",
                "user": record["username"],
                "detail": f"Training not completed. Due date: {record['due']}",
                "recommendation": "Assign training immediately and escalate to manager",
            })

    completion = stats["completed_on_time"] + stats["completed_late"]
    stats["completion_rate"] = f"{completion / stats['total_assigned'] * 100:.1f}%"
    stats["on_time_rate"] = f"{stats['completed_on_time'] / stats['total_assigned'] * 100:.1f}%"

    return stats, findings


def collect_patch_evidence(patches):
    """Analyze patch compliance data."""
    stats = {
        "total_systems": len(patches),
        "compliant": 0,
        "non_compliant": 0,
        "total_critical": 0,
        "total_high": 0,
        "restricted_systems_compliant": 0,
        "restricted_systems_total": 0,
    }
    findings = []

    for system in patches:
        if system["compliant"]:
            stats["compliant"] += 1
        else:
            stats["non_compliant"] += 1
        stats["total_critical"] += system["critical_patches"]
        stats["total_high"] += system["high_patches"]

        if system["data_type"] in ("ePHI", "Student Records"):
            stats["restricted_systems_total"] += 1
            if system["compliant"]:
                stats["restricted_systems_compliant"] += 1

        if system["critical_patches"] > 0:
            findings.append({
                "type": "CRITICAL_PATCH_MISSING",
                "severity": "Critical",
                "system": system["hostname"],
                "detail": f"{system['critical_patches']} critical patches missing. Data type: {system['data_type']}",
                "recommendation": "Patch within 14-day SLA (72 hours if in CISA KEV)",
            })

    stats["compliance_rate"] = f"{stats['compliant'] / stats['total_systems'] * 100:.1f}%"

    return stats, findings


# -----------------------------------------------------------------------
# Report generation
# -----------------------------------------------------------------------

def generate_evidence_report(output_dir=None):
    """Generate a full evidence collection report."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    users = generate_sample_users()
    training = generate_sample_training()
    patches = generate_sample_patches()

    access_stats, access_findings = collect_access_evidence(users)
    training_stats, training_findings = collect_training_evidence(training)
    patch_stats, patch_findings = collect_patch_evidence(patches)

    all_findings = access_findings + training_findings + patch_findings
    critical_count = sum(1 for f in all_findings if f["severity"] == "Critical")
    high_count = sum(1 for f in all_findings if f["severity"] == "High")
    medium_count = sum(1 for f in all_findings if f["severity"] == "Medium")

    # Print report
    print(f"\n{'='*80}")
    print(f"  GRC EVIDENCE COLLECTION REPORT")
    print(f"  Generated: {timestamp}")
    print(f"  Scope: HIPAA Security Rule / ISO 27001 Audit Preparation")
    print(f"{'='*80}")

    print(f"\n  EXECUTIVE SUMMARY")
    print(f"  {'-'*70}")
    print(f"  Total findings: {len(all_findings)}")
    print(f"    Critical: {critical_count}")
    print(f"    High:     {high_count}")
    print(f"    Medium:   {medium_count}")

    print(f"\n  ACCESS CONTROL EVIDENCE")
    print(f"  {'-'*70}")
    for key, val in access_stats.items():
        print(f"    {key}: {val}")

    print(f"\n  TRAINING COMPLIANCE EVIDENCE")
    print(f"  {'-'*70}")
    for key, val in training_stats.items():
        print(f"    {key}: {val}")

    print(f"\n  PATCH COMPLIANCE EVIDENCE")
    print(f"  {'-'*70}")
    for key, val in patch_stats.items():
        print(f"    {key}: {val}")

    if all_findings:
        print(f"\n  FINDINGS REQUIRING ACTION")
        print(f"  {'-'*70}")
        for i, f in enumerate(sorted(all_findings, key=lambda x: {"Critical": 0, "High": 1, "Medium": 2}.get(x["severity"], 3)), 1):
            user_or_system = f.get("user", f.get("system", "N/A"))
            print(f"  {i}. [{f['severity']}] {f['type']} - {user_or_system}")
            print(f"     {f['detail']}")
            print(f"     Action: {f['recommendation']}")
            print()

    print(f"{'='*80}")

    # Write CSV exports if output directory specified
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
        date_str = datetime.now().strftime("%Y%m%d")

        # User access export
        access_path = os.path.join(output_dir, f"access-review-{date_str}.csv")
        with open(access_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=users[0].keys())
            writer.writeheader()
            writer.writerows(users)
        print(f"\n  Exported: {access_path}")

        # Training export
        training_path = os.path.join(output_dir, f"training-compliance-{date_str}.csv")
        with open(training_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=training[0].keys())
            writer.writeheader()
            writer.writerows(training)
        print(f"  Exported: {training_path}")

        # Patch export
        patch_path = os.path.join(output_dir, f"patch-compliance-{date_str}.csv")
        with open(patch_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=patches[0].keys())
            writer.writeheader()
            writer.writerows(patches)
        print(f"  Exported: {patch_path}")

        # Findings export
        findings_path = os.path.join(output_dir, f"findings-{date_str}.json")
        with open(findings_path, "w", encoding="utf-8") as f:
            json.dump({
                "report_date": timestamp,
                "summary": {
                    "total_findings": len(all_findings),
                    "critical": critical_count,
                    "high": high_count,
                    "medium": medium_count,
                },
                "access_stats": access_stats,
                "training_stats": training_stats,
                "patch_stats": patch_stats,
                "findings": all_findings,
            }, f, indent=2)
        print(f"  Exported: {findings_path}")


def main():
    output_dir = sys.argv[1] if len(sys.argv) > 1 else None
    generate_evidence_report(output_dir)


if __name__ == "__main__":
    main()
