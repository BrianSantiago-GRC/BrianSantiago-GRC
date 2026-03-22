"""
Compliance Control Checker
Reads a control mapping CSV and generates a compliance status report
showing implementation gaps across multiple frameworks (NIST CSF,
NIST 800-53, NIST 800-171, ISO 27001, HIPAA).

Useful for tracking multi-framework compliance and identifying
controls that satisfy requirements across multiple standards.

Framework: Multi-framework (NIST CSF 2.0, NIST 800-53, NIST 800-171, ISO 27001, HIPAA)
Author: Brian Santiago
"""

import csv
import sys
import os
from datetime import datetime


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


def generate_sample_controls():
    """Generate sample control data for demonstration."""
    return [
        {"control_area": "Access control policy", "nist_csf": "PR.AA-03", "nist_800_53": "AC-1", "nist_800_171": "3.1.1", "iso_27001": "A.5.15", "hipaa": "164.312(a)(1)", "status": "Implemented", "evidence": "Access control policy document", "owner": "IT Security", "last_reviewed": "2026-01-15"},
        {"control_area": "Multi-factor authentication", "nist_csf": "PR.AA-02", "nist_800_53": "IA-2(1)", "nist_800_171": "3.5.3", "iso_27001": "A.5.17", "hipaa": "164.312(d)", "status": "Implemented", "evidence": "Azure AD MFA report", "owner": "IT Security", "last_reviewed": "2026-03-01"},
        {"control_area": "Account management", "nist_csf": "PR.AA-01", "nist_800_53": "AC-2", "nist_800_171": "3.1.1", "iso_27001": "A.5.16", "hipaa": "164.308(a)(4)", "status": "Implemented", "evidence": "HR-AD sync configuration, access review records", "owner": "IT Security", "last_reviewed": "2026-02-15"},
        {"control_area": "Risk assessment", "nist_csf": "ID.RA-04", "nist_800_53": "RA-3", "nist_800_171": "3.11.1", "iso_27001": "Clause 6.1.2", "hipaa": "164.308(a)(1)(ii)(A)", "status": "Implemented", "evidence": "Risk register, risk assessment methodology", "owner": "IT Security", "last_reviewed": "2026-01-20"},
        {"control_area": "Vulnerability management", "nist_csf": "ID.RA-01", "nist_800_53": "RA-5", "nist_800_171": "3.11.2", "iso_27001": "A.8.8", "hipaa": "164.308(a)(1)", "status": "Implemented", "evidence": "Qualys scan reports, patching metrics", "owner": "IT Operations", "last_reviewed": "2026-03-15"},
        {"control_area": "Incident response plan", "nist_csf": "RS.MA-01", "nist_800_53": "IR-1", "nist_800_171": "3.6.1", "iso_27001": "A.5.24", "hipaa": "164.308(a)(6)(i)", "status": "Implemented", "evidence": "IR plan document, playbooks", "owner": "IT Security", "last_reviewed": "2026-02-01"},
        {"control_area": "Security awareness training", "nist_csf": "PR.AT-01", "nist_800_53": "AT-2", "nist_800_171": "3.2.1", "iso_27001": "A.6.3", "hipaa": "164.308(a)(5)(i)", "status": "Implemented", "evidence": "Training completion records, LMS export", "owner": "IT Security", "last_reviewed": "2026-01-31"},
        {"control_area": "Encryption at rest", "nist_csf": "PR.DS-01", "nist_800_53": "SC-28", "nist_800_171": "3.13.16", "iso_27001": "A.8.24", "hipaa": "164.312(a)(2)(iv)", "status": "Implemented", "evidence": "BitLocker compliance report, DB encryption config", "owner": "IT Operations", "last_reviewed": "2026-02-20"},
        {"control_area": "Encryption in transit", "nist_csf": "PR.DS-02", "nist_800_53": "SC-8", "nist_800_171": "3.13.8", "iso_27001": "A.8.24", "hipaa": "164.312(e)(1)", "status": "Implemented", "evidence": "TLS configuration scan results", "owner": "IT Operations", "last_reviewed": "2026-02-20"},
        {"control_area": "Audit logging", "nist_csf": "DE.CM-01", "nist_800_53": "AU-2", "nist_800_171": "3.3.1", "iso_27001": "A.8.15", "hipaa": "164.312(b)", "status": "Implemented", "evidence": "Splunk deployment config, retention policy", "owner": "IT Security", "last_reviewed": "2026-03-01"},
        {"control_area": "Log monitoring and alerting", "nist_csf": "DE.AE-01", "nist_800_53": "AU-6", "nist_800_171": "3.3.5", "iso_27001": "A.8.16", "hipaa": "164.312(b)", "status": "Partial", "evidence": "Splunk alert rules (basic)", "owner": "IT Security", "last_reviewed": "2026-03-01"},
        {"control_area": "Data backup", "nist_csf": "RC.RP-01", "nist_800_53": "CP-9", "nist_800_171": "3.8.9", "iso_27001": "A.8.13", "hipaa": "164.308(a)(7)(ii)(A)", "status": "Implemented", "evidence": "Backup schedules, restore test logs", "owner": "IT Operations", "last_reviewed": "2026-02-10"},
        {"control_area": "Vendor risk assessment", "nist_csf": "GV.SC-01", "nist_800_53": "SA-9", "nist_800_171": "", "iso_27001": "A.5.19", "hipaa": "164.308(b)(1)", "status": "Implemented", "evidence": "Vendor questionnaires, risk tier matrix", "owner": "Compliance", "last_reviewed": "2026-02-01"},
        {"control_area": "Threat intelligence", "nist_csf": "ID.RA-02", "nist_800_53": "RA-3(1)", "nist_800_171": "", "iso_27001": "A.5.7", "hipaa": "", "status": "Partial", "evidence": "CISA alerts reviewed manually", "owner": "IT Security", "last_reviewed": "2026-03-10"},
        {"control_area": "Supply chain risk management", "nist_csf": "GV.SC-01", "nist_800_53": "SR-1", "nist_800_171": "", "iso_27001": "A.5.21", "hipaa": "", "status": "Not Implemented", "evidence": "None", "owner": "Compliance", "last_reviewed": ""},
        {"control_area": "Configuration management", "nist_csf": "PR.PS-01", "nist_800_53": "CM-6", "nist_800_171": "3.4.1", "iso_27001": "A.8.9", "hipaa": "164.310(d)(1)", "status": "Partial", "evidence": "Baselines documented, not fully enforced", "owner": "IT Operations", "last_reviewed": "2026-01-20"},
        {"control_area": "Data classification", "nist_csf": "ID.AM-03", "nist_800_53": "RA-2", "nist_800_171": "3.8.4", "iso_27001": "A.5.12", "hipaa": "164.312(a)(1)", "status": "Implemented", "evidence": "Data classification policy", "owner": "Compliance", "last_reviewed": "2026-01-15"},
        {"control_area": "Business continuity testing", "nist_csf": "RC.RP-02", "nist_800_53": "CP-4", "nist_800_171": "", "iso_27001": "A.5.30", "hipaa": "164.308(a)(7)(ii)(D)", "status": "Partial", "evidence": "Monthly backup restore tests only", "owner": "IT Operations", "last_reviewed": "2026-02-28"},
    ]


def load_controls(filepath):
    """Load controls from CSV file."""
    controls = []
    with open(filepath, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            controls.append(row)
    return controls


def analyze_controls(controls):
    """Analyze control implementation status across frameworks."""
    frameworks = ["nist_csf", "nist_800_53", "nist_800_171", "iso_27001", "hipaa"]
    framework_labels = {
        "nist_csf": "NIST CSF 2.0",
        "nist_800_53": "NIST 800-53",
        "nist_800_171": "NIST 800-171",
        "iso_27001": "ISO 27001",
        "hipaa": "HIPAA",
    }

    stats = {
        "total": len(controls),
        "implemented": 0,
        "partial": 0,
        "not_implemented": 0,
        "by_framework": {},
        "by_owner": {},
        "stale_reviews": [],
        "gaps": [],
    }

    today = datetime.now()

    for fw in frameworks:
        stats["by_framework"][fw] = {"total": 0, "implemented": 0, "partial": 0, "not_implemented": 0}

    for ctrl in controls:
        status = ctrl.get("status", "").strip()
        owner = ctrl.get("owner", "Unknown")

        if status == "Implemented":
            stats["implemented"] += 1
        elif status == "Partial":
            stats["partial"] += 1
        else:
            stats["not_implemented"] += 1

        # Count by framework (only if framework has a mapping for this control)
        for fw in frameworks:
            if ctrl.get(fw, "").strip():
                stats["by_framework"][fw]["total"] += 1
                if status == "Implemented":
                    stats["by_framework"][fw]["implemented"] += 1
                elif status == "Partial":
                    stats["by_framework"][fw]["partial"] += 1
                else:
                    stats["by_framework"][fw]["not_implemented"] += 1

        # Count by owner
        if owner not in stats["by_owner"]:
            stats["by_owner"][owner] = {"total": 0, "implemented": 0, "gaps": 0}
        stats["by_owner"][owner]["total"] += 1
        if status == "Implemented":
            stats["by_owner"][owner]["implemented"] += 1
        else:
            stats["by_owner"][owner]["gaps"] += 1

        # Check for stale reviews (>12 months)
        last_reviewed = ctrl.get("last_reviewed", "").strip()
        if last_reviewed:
            try:
                review_date = datetime.strptime(last_reviewed, "%Y-%m-%d")
                days_since = (today - review_date).days
                if days_since > 365:
                    stats["stale_reviews"].append({
                        "control": ctrl["control_area"],
                        "last_reviewed": last_reviewed,
                        "days_since": days_since,
                    })
            except ValueError:
                pass

        # Track gaps
        if status != "Implemented":
            gap_frameworks = []
            for fw in frameworks:
                if ctrl.get(fw, "").strip():
                    gap_frameworks.append(framework_labels[fw])
            stats["gaps"].append({
                "control": ctrl["control_area"],
                "status": status,
                "frameworks_affected": gap_frameworks,
                "owner": owner,
                "evidence": ctrl.get("evidence", ""),
            })

    return stats, framework_labels


def generate_report(controls, stats, framework_labels):
    """Print the compliance report."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"\n{'='*80}")
    print(f"  COMPLIANCE CONTROL STATUS REPORT")
    print(f"  Generated: {timestamp}")
    print(f"  Frameworks: NIST CSF 2.0, NIST 800-53, NIST 800-171, ISO 27001, HIPAA")
    print(f"{'='*80}")

    # Overall status
    total = stats["total"]
    impl_pct = stats["implemented"] / total * 100 if total else 0
    print(f"\n  OVERALL STATUS")
    print(f"  {'-'*60}")
    print(f"  Total controls mapped:  {total}")
    print(f"  Implemented:            {stats['implemented']} ({impl_pct:.1f}%)")
    print(f"  Partially implemented:  {stats['partial']}")
    print(f"  Not implemented:        {stats['not_implemented']}")

    # By framework
    print(f"\n  STATUS BY FRAMEWORK")
    print(f"  {'-'*60}")
    print(f"  {'Framework':<20} {'Total':>6} {'Impl':>6} {'Partial':>8} {'Gap':>6} {'Rate':>8}")
    print(f"  {'-'*60}")
    for fw, label in framework_labels.items():
        fw_stats = stats["by_framework"][fw]
        if fw_stats["total"] > 0:
            rate = fw_stats["implemented"] / fw_stats["total"] * 100
            print(f"  {label:<20} {fw_stats['total']:>6} {fw_stats['implemented']:>6} {fw_stats['partial']:>8} {fw_stats['not_implemented']:>6} {rate:>7.1f}%")

    # By owner
    print(f"\n  STATUS BY OWNER")
    print(f"  {'-'*60}")
    for owner, owner_stats in stats["by_owner"].items():
        rate = owner_stats["implemented"] / owner_stats["total"] * 100 if owner_stats["total"] else 0
        print(f"  {owner:<20} {owner_stats['total']:>3} controls | {owner_stats['implemented']:>2} implemented | {owner_stats['gaps']:>2} gaps | {rate:.0f}%")

    # Gaps
    if stats["gaps"]:
        print(f"\n  COMPLIANCE GAPS (requires action)")
        print(f"  {'-'*60}")
        for i, gap in enumerate(stats["gaps"], 1):
            frameworks_str = ", ".join(gap["frameworks_affected"])
            print(f"  {i}. {gap['control']}")
            print(f"     Status: {gap['status']} | Owner: {gap['owner']}")
            print(f"     Frameworks affected: {frameworks_str}")
            print(f"     Current evidence: {gap['evidence']}")
            print()

    # Stale reviews
    if stats["stale_reviews"]:
        print(f"\n  STALE CONTROL REVIEWS (>12 months since last review)")
        print(f"  {'-'*60}")
        for item in stats["stale_reviews"]:
            print(f"  - {item['control']} (last reviewed: {item['last_reviewed']}, {item['days_since']} days ago)")

    print(f"\n{'='*80}")


def main():
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
        if not os.path.exists(filepath):
            print(f"Error: File not found: {filepath}")
            sys.exit(1)
        controls = load_controls(filepath)
    else:
        # Use built-in sample data
        controls = generate_sample_controls()
        print("  Using built-in sample control data (pass a CSV path for your own data)")

    stats, framework_labels = analyze_controls(controls)
    generate_report(controls, stats, framework_labels)


if __name__ == "__main__":
    main()
