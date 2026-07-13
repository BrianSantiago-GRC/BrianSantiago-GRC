"""
Access Review Audit Automation Tool
Reads a user access export (CSV) and flags accounts that violate
access control policies: orphan accounts, missing MFA, excessive
privileges, and separation of duties violations.

Designed for quarterly access reviews per NIST SP 800-53 (AC-2)
and HIPAA Security Rule (164.308(a)(3-4)).

Author: Brian Santiago
"""

import argparse
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
DEMO_AS_OF_DATE = datetime(2026, 4, 1)

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


def check_orphan_accounts(users, as_of=None):
    """Find accounts with no login activity past the threshold."""
    findings = []
    today = as_of or datetime.now()

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


def run_audit(filepath, as_of=None):
    """Run all access review checks and produce a report."""
    users = load_users(filepath)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    review_date = as_of or datetime.now()

    all_findings = []
    all_findings.extend(check_orphan_accounts(usersvâÚ$z{-®éÜj×\Èˆ‹›\İÜØØ[ˆˆŒŒ‹LËLN‹˜ÛÛ\X[ˆ˜[ÙK™]Wİ\Hˆ“Z^YŸKBˆÈšÜİ˜[YHˆ”Ô•‹TÔS’ËLH‹›ÜÈˆ•X[HŒ‹Œ‹˜Üš]XØ[Ü]Ú\ÈˆšYÚÜ]Ú\Èˆ›\İÜØØ[ˆˆŒŒ‹LËLN‹˜ÛÛ\X[ˆYK™]Wİ\Hˆ“ÙÜÈŸKBˆÈšÜİ˜[YHˆ‘•ËQQÑKLH‹›ÜÈˆ‘›ÜSÔÈË‹˜Üš]XØ[Ü]Ú\ÈˆšYÚÜ]Ú\ÈˆK›\İÜØØ[ˆˆŒŒ‹LËLMH‹˜ÛÛ\X[ˆYK™]Wİ\Hˆ’[™œ˜\İXİ\™HŸKBˆÈšÜİ˜[YHˆ•ÔËS•T”ÑKLH‹›ÜÈˆ•Ú[™İÜÈLH‹˜Üš]XØ[Ü]Ú\ÈˆšYÚÜ]Ú\Èˆ›\İÜØØ[ˆˆŒŒ‹LËLŒ‹˜ÛÛ\X[ˆYK™]Wİ\Hˆ™THŸKBˆÈšÜİ˜[YHˆ•ÔËSÑ‘’PÑKLLˆ‹›ÜÈˆ•Ú[™İÜÈLH‹˜Üš]XØ[Ü]Ú\ÈˆšYÚÜ]Ú\ÈˆK›\İÜØØ[ˆˆŒŒ‹LËLŒ‹˜ÛÛ\X[ˆYK™]Wİ\Hˆ”İ[™\™ŸKBˆCBƒBƒBˆÈKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKCBˆÈ]šY[˜ÙHÛÛXİ[Ûˆ[˜İ[ÛœÃBˆÈKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKCBƒB™YˆÛÛXİØXØÙ\Ü×Ù]šY[˜ÙJ\Ù\œË\×ÛÙS›Û™JN‚ˆˆˆ[˜[^™H\Ù\ˆXØÙ\ÜÈ]H[™›YÈ\ÜİY\ËˆˆˆƒBˆš[™[™ÜÈH×CBˆİ]ÈHÃBˆİ[İ\Ù\œÈˆ[Š\Ù\œÊKBˆ›Y˜WÙ[˜X›YˆBˆœš]š[YÙYØXØÛİ[ÈˆBˆ›Üœ[—ØXØÛİ[ÈˆBˆœ™\İšXİYÙ]Wİ\Ù\œÈˆBˆCBƒBˆÙ^HH\×ÛÙˆÜˆ]][YK››İÊ
BƒBˆ›Üˆ\Ù\ˆ[ˆ\Ù\œÎƒBˆYˆ\Ù\–È›Y˜WÙ[˜X›Y—NƒBˆİ]ÖÈ›Y˜WÙ[˜X›Y—H
ÏHCBˆYˆ\Ù\–Èœš]š[YÙY—NƒBˆİ]ÖÈœš]š[YÙYØXØÛİ[È—H
ÏHCBˆYˆ\Ù\–È™]WØXØÙ\ÜÈ—H[ˆ
™TH‹”İY[™XÛÜ™È‹‘[ŠNƒBˆİ]ÖÈœ™\İšXİYÙ]Wİ\Ù\œÈ—H
ÏHCBƒBˆÈÚXÚÈ›ÜˆÜœ[ˆXØÛİ[È
›ÈÙÚ[ˆ[ˆL
È^\ÊCBˆYˆ\Ù\–È›\İÛÙÚ[ˆ—NƒBˆ\İÛÙÚ[ˆH]][YKœİœ[YJ\Ù\–È›\İÛÙÚ[ˆ—K‰VKI[KIYŠCBˆ^\×Ú[˜Xİ]™HH
Ù^HH\İÛÙÚ[ŠK™^\ÃBˆYˆ^\×Ú[˜Xİ]™HˆLƒBˆİ]ÖÈ›Üœ[—ØXØÛİ[È—H
ÏHCBˆš[™[™ÜË˜\[™
ÃBˆ\Hˆ“Ô”S—ĞPĞÓÕS•‹BˆœÙ]™\š]Hˆ’YÚ‹Bˆ\Ù\ˆˆ\Ù\–È\Ù\›˜[YH—KBˆ™]Z[ˆˆ“›ÈÙÚ[ˆ›ÜˆÙ^\×Ú[˜Xİ]™_H^\Ëˆ\İÙÚ[ˆİ\Ù\–ÉÛ\İÛÙÚ[‰×_Kˆ]HXØÙ\ÜÎˆİ\Ù\–ÉÙ]WØXØÙ\ÜÉ×_H‹Bˆœ™XÛÛ[Y[™][Ûˆˆ‘\ØX›HXØÛİ[[[YYX][H[™[™\İYØ]HÚ]ˆ‹BˆJCBƒBˆÈÚXÚÈ›Üˆš]š[YÙYXØÛİ[ÈÚ]İ]QCBˆYˆ\Ù\–Èœš]š[YÙY—H[™›İ\Ù\–È›Y˜WÙ[˜X›Y—NƒBˆš[™[™ÜË˜\[™
ÃBˆ\Hˆ”’U—Ó“×ÓQH‹BˆœÙ]™\š]HˆÜš]XØ[‹Bˆ\Ù\ˆˆ\Ù\–È\Ù\›˜[YH—KBˆ™]Z[ˆˆ”š]š[YÙYXØÛİ[Ú]İ]QKˆ›ÛNˆİ\Ù\–ÉÜ›ÛI×_H‹Bˆœ™XÛÛ[Y[™][Ûˆˆ‘[˜X›HQH[[YYX][HÜˆÛÛ™\ÈX[˜YÙYY[]H‹BˆJCBƒBˆÈÚXÚÈ›Üˆ›Û‹\š]š[YÙY™\İšXİY]HXØÙ\ÜÈÚ]İ]QCBˆYˆ\Ù\–È™]WØXØÙ\ÜÈ—H[ˆ
™TH‹”İY[™XÛÜ™ÈŠH[™›İ\Ù\–È›Y˜WÙ[˜X›Y—NƒBˆš[™[™ÜË˜\[™
ÃBˆ\Hˆ”‘TÕ’PÕQÓ“×ÓQH‹BˆœÙ]™\š]Hˆ’YÚ‹Bˆ\Ù\ˆˆ\Ù\–È\Ù\›˜[YH—KBˆ™]Z[ˆˆXØÙ\ÜÈÈİ\Ù\–ÉÙ]WØXØÙ\ÜÉ×_HÚ]İ]QH[˜X›Y‹Bˆœ™XÛÛ[Y[™][Ûˆˆ‘[˜X›HQH\ˆTPKÑ‘T”HXØÙ\ÜÈÛÛ›Û™\]Z\™[Y[È‹BˆJCBƒBˆİ]ÖÈ›Y˜WÜ˜]H—HHˆÜİ]ÖÉÛY˜WÙ[˜X›Y	×HÈİ]ÖÉİİ[İ\Ù\œÉ×H
ˆL‹ŒYŸIHƒBˆİ]ÖÈœš]—Ü˜]H—HHˆÜİ]ÖÉÜš]š[YÙYØXØÛİ[É×HÈİ]ÖÉİİ[İ\Ù\œÉ×H
ˆL‹ŒYŸIHƒBƒBˆ™]\›ˆİ]Ëš[™[™ÜÃBƒBƒB™YˆÛÛXİİ˜Z[š[™×Ù]šY[˜ÙJ˜Z[š[™×Ü™XÛÜ™ÊNƒBˆˆˆ[˜[^™H˜Z[š[™ÈÛÛ\][Ûˆ]KˆˆˆƒBˆİ]ÈHÃBˆİ[Ø\ÜÚYÛ™Yˆ[Š˜Z[š[™×Ü™XÛÜ™ÊKBˆ˜ÛÛ\]YÛÛ—İ[YHˆBˆ˜ÛÛ\]YÛ]HˆBˆ››İØÛÛ\]YˆBˆCBˆš[™[™ÜÈH×CBƒBˆ›Üˆ™XÛÜ™[ˆ˜Z[š[™×Ü™XÛÜ™ÎƒBˆYˆ™XÛÜ™Èœİ]\È—HOHÛÛ\]YƒBˆİ]ÖÈ˜ÛÛ\]YÛÛ—İ[YH—H
ÏHCBˆ[Yˆ™XÛÜ™Èœİ]\È—HOH“İ™\™YHƒBˆİ]ÖÈ˜ÛÛ\]YÛ]H—H
ÏHCBˆš[™[™ÜË˜\[™
ÃBˆ\Hˆ“UWÕRS’S‘È‹BˆœÙ]™\š]Hˆ“YY][H‹Bˆ\Ù\ˆˆ™XÛÜ™È\Ù\›˜[YH—KBˆ™]Z[ˆˆÛÛ\]Y˜Z[š[™ÈÛˆÜ™XÛÜ™ÉØÛÛ\]Y	×_H
YHÜ™XÛÜ™ÉÙYI×_JH‹Bˆœ™XÛÛ[Y[™][Ûˆˆ“[Ûš]Üˆ›Üˆ[Y[HÛÛ\][Ûˆ™^ŞXÛH‹BˆJCBˆ[ÙNƒBˆİ]ÖÈ››İØÛÛ\]Y—H
ÏHCBˆš[™[™ÜË˜\[™
ÃBˆ\Hˆ“RTÔÒS‘×ÕRS’S‘È‹BˆœÙ]™\š]Hˆ’YÚ‹Bˆ\Ù\ˆˆ™XÛÜ™È\Ù\›˜[YH—KBˆ™]Z[ˆˆ•˜Z[š[™È›İÛÛ\]YˆYH]NˆÜ™XÛÜ™ÉÙYI×_H‹Bˆœ™XÛÛ[Y[™][Ûˆˆ\ÜÚYÛˆ˜Z[š[™È[[YYX][H[™\ØØ[]HÈX[˜YÙ\ˆ‹BˆJCBƒBˆÛÛ\][ÛˆHİ]ÖÈ˜ÛÛ\]YÛÛ—İ[YH—H
Èİ]ÖÈ˜ÛÛ\]YÛ]H—CBˆİ]ÖÈ˜ÛÛ\][Û—Ü˜]H—HHˆØÛÛ\][ÛˆÈİ]ÖÉİİ[Ø\ÜÚYÛ™Y	×H
ˆL‹ŒYŸIHƒBˆİ]ÖÈ›Û—İ[YWÜ˜]H—HHˆÜİ]ÖÉØÛÛ\]YÛÛ—İ[YI×HÈİ]ÖÉİİ[Ø\ÜÚYÛ™Y	×H
ˆL‹ŒYŸIHƒBƒBˆ™]\›ˆİ]Ëš[™[™ÜÃBƒBƒB™YˆÛÛXİÜ]ÚÙ]šY[˜ÙJ]Ú\ÊNƒBˆˆˆ[˜[^™H]ÚÛÛ\X[˜ÙH]KˆˆˆƒBˆİ]ÈHÃBˆİ[ÜŞ\İ[\Èˆ[Š]Ú\ÊKBˆ˜ÛÛ\X[ˆBˆ››Û—ØÛÛ\X[ˆBˆİ[ØÜš]XØ[ˆBˆİ[ÚYÚˆBˆœ™\İšXİYÜŞ\İ[\×ØÛÛ\X[ˆBˆœ™\İšXİYÜŞ\İ[\×İİ[ˆBˆCBˆš[™[™ÜÈH×CBƒBˆ›ÜˆŞ\İ[H[ˆ]Ú\ÎƒBˆYˆŞ\İ[VÈ˜ÛÛ\X[—NƒBˆİ]ÖÈ˜ÛÛ\X[—H
ÏHCBˆ[ÙNƒBˆİ]ÖÈ››Û—ØÛÛ\X[—H
ÏHCBˆİ]ÖÈİ[ØÜš]XØ[—H
ÏHŞ\İ[VÈ˜Üš]XØ[Ü]Ú\È—CBˆİ]ÖÈİ[ÚYÚ—H
ÏHŞ\İ[VÈšYÚÜ]Ú\È—CBƒBˆYˆŞ\İ[VÈ™]Wİ\H—H[ˆ
™TH‹”İY[™XÛÜ™ÈŠNƒBˆİ]ÖÈœ™\İšXİYÜŞ\İ[\×İİ[—H
ÏHCBˆYˆŞ\İ[VÈ˜ÛÛ\X[—NƒBˆİ]ÖÈœ™\İšXİYÜŞ\İ[\×ØÛÛ\X[—H
ÏHCBƒBˆYˆŞ\İ[VÈ˜Üš]XØ[Ü]Ú\È—HˆƒBˆš[™[™ÜË˜\[™
ÃBˆ\HˆÔ’UPĞSÔUÒÓRTÔÒS‘È‹BˆœÙ]™\š]HˆÜš]XØ[‹BˆœŞ\İ[HˆŞ\İ[VÈšÜİ˜[YH—KBˆ™]Z[ˆˆÜŞ\İ[VÉØÜš]XØ[Ü]Ú\É×_HÜš]XØ[]Ú\ÈZ\ÜÚ[™Ëˆ]H\NˆÜŞ\İ[VÉÙ]Wİ\I×_H‹Bˆœ™XÛÛ[Y[™][Ûˆˆ”]ÚÚ][ˆMY^HÓH
Ìˆİ\œÈYˆ[ˆÒTĞHÑUŠH‹BˆJCBƒBˆİ]ÖÈ˜ÛÛ\X[˜ÙWÜ˜]H—HHˆÜİ]ÖÉØÛÛ\X[	×HÈİ]ÖÉİİ[ÜŞ\İ[\É×H
ˆL‹ŒYŸIHƒBƒBˆ™]\›ˆİ]Ëš[™[™ÜÃBƒBƒBˆÈKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKCBˆÈ™\ÜÙ[™\˜][ÛƒBˆÈKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKCBƒB™YˆÙ[™\˜]WÙ]šY[˜ÙWÜ™\Ü
İ]]Ù\S›Û™K\×ÛÙS›Û™JN‚ˆˆˆ‘Ù[™\˜]HH[]šY[˜ÙHÛÛXİ[Ûˆ™\ÜˆˆˆƒBˆ[Y\İ[\H]][YK››İÊ
Kœİ™[YJ‰VKI[KIY	R‰SN‰TÈŠCBƒBˆ\Ù\œÈHÙ[™\˜]WÜØ[\Wİ\Ù\œÊ
CBˆ˜Z[š[™ÈHÙ[™\˜]WÜØ[\Wİ˜Z[š[™Ê
CBˆ]Ú\ÈHÙ[™\˜]WÜØ[\WÜ]Ú\Ê
CBƒBˆ™]šY]×Ù]HH\×ÛÙˆÜˆSS×ĞT×ÓÑ—ÑUBˆXØÙ\Ü×Üİ]ËXØÙ\Ü×Ùš[™[™ÜÈHÛÛXİØXØÙ\Ü×Ù]šY[˜ÙJ\Ù\œË™]šY]×Ù]JBˆ˜Z[š[™×Üİ]Ë˜Z[š[™×Ùš[™[™ÜÈHÛÛXİİ˜Z[š[™×Ù]šY[˜ÙJ˜Z[š[™ÊCBˆ]ÚÜİ]Ë]ÚÙš[™[™ÜÈHÛÛXİÜ]ÚÙ]šY[˜ÙJ]Ú\ÊCBƒBˆ[Ùš[™[™ÜÈHXØÙ\Ü×Ùš[™[™ÜÈ
È˜Z[š[™×Ùš[™[™ÜÈ
È]ÚÙš[™[™ÜÃBˆÜš]XØ[ØÛİ[Hİ[JH›Üˆˆ[ˆ[Ùš[™[™ÜÈYˆ–ÈœÙ]™\š]H—HOHÜš]XØ[ŠCBˆYÚØÛİ[Hİ[JH›Üˆˆ[ˆ[Ùš[™[™ÜÈYˆ–ÈœÙ]™\š]H—HOH’YÚŠCBˆYY][WØÛİ[Hİ[JH›Üˆˆ[ˆ[Ùš[™[™ÜÈYˆ–ÈœÙ]™\š]H—HOH“YY][HŠCBƒBˆÈš[™\ÜBˆš[
ˆ—ÉÏIÊHŠCBˆš[
ˆˆÔÈU’QSÑHÓÓPÕSÓˆ‘TÔ•ŠCBˆš[
ˆˆÙ[™\˜]Yˆİ[Y\İ[\HŠBˆš[
ˆˆ™]šY]È]NˆÜ™]šY]×Ù]Kœİ™[YJ	ÉVKI[KIY	Ê_HŠBˆš[
ˆˆØÛÜNˆTPHÙXİ\š]H[HÈTÓÈÌH]Y]™\\˜][ÛˆŠCBˆš[
ˆÉÏIÊHŠCBƒBˆš[
ˆ—ˆVPÕUU‘HÕSSPT–HŠCBˆš[
ˆˆÉËIÊÌHŠCBˆš[
ˆˆİ[š[™[™ÜÎˆÛ[Š[Ùš[™[™ÜÊ_HŠCBˆš[
ˆˆÜš]XØ[ˆØÜš]XØ[ØÛİ[HŠCBˆš[
ˆˆYÚˆÚYÚØÛİ[HŠCBˆš[
ˆˆYY][NˆÛYY][WØÛİ[HŠCBƒBˆš[
ˆ—ˆPĞÑTÔÈÓÓ•“ÓU’QSÑHŠCBˆš[
ˆˆÉËIÊÌHŠCBˆ›ÜˆÙ^K˜[[ˆXØÙ\Ü×Üİ]Ëš][\Ê
NƒBˆš[
ˆˆÚÙ^_Nˆİ˜[HŠCBƒBˆš[
ˆ—ˆRS’S‘ÈÓÓTPSÑHU’QSÑHŠCBˆš[
ˆˆÉËIÊÌHŠCBˆ›ÜˆÙ^K˜[[ˆ˜Z[š[™×Üİ]Ëš][\Ê
NƒBˆš[
ˆˆÚÙ^_Nˆİ˜[HŠCBƒBˆš[
ˆ—ˆUÒÓÓTPSÑHU’QSÑHŠCBˆš[
ˆˆÉËIÊÌHŠCBˆ›ÜˆÙ^K˜[[ˆ]ÚÜİ]Ëš][\Ê
NƒBˆš[
ˆˆÚÙ^_Nˆİ˜[HŠCBƒBˆYˆ[Ùš[™[™ÜÎƒBˆš[
ˆ—ˆ’S‘S‘ÔÈ‘TURT’S‘ÈPÕSÓˆŠCBˆš[
ˆˆÉËIÊÌHŠCBˆ›ÜˆKˆ[ˆ[[Y\˜]JÛÜY
[Ùš[™[™ÜËÙ^O[[X™HˆÈÜš]XØ[ˆ’YÚˆK“YY][HˆŸK™Ù]
ÈœÙ]™\š]H—KÊJKJNƒBˆ\Ù\—ÛÜ—ÜŞ\İ[HH‹™Ù]
\Ù\ˆ‹‹™Ù]
œŞ\İ[H‹“‹ĞHŠJCBˆš[
ˆˆÚ_KˆŞÙ–ÉÜÙ]™\š]I×_WHÙ–Éİ\I×_HHİ\Ù\—ÛÜ—ÜŞ\İ[_HŠCBˆš[
ˆˆÙ–ÉÙ]Z[	×_HŠCBˆš[
ˆˆXİ[ÛˆÙ–ÉÜ™XÛÛ[Y[™][Û‰×_HŠCBˆš[

CBƒBˆš[
ˆÉÏIÊHŠCBƒBˆÈÜš]HÔÕˆ^ÜÈYˆİ]]\™XİÜHÜXÚYšYYBˆYˆİ]]Ù\ƒBˆÜË›XZÙY\œÊİ]]Ù\‹^\İÛÚÏUYJCBˆ]WÜİˆH]][YK››İÊ
Kœİ™[YJ‰VI[IYŠCBƒBˆÈ\Ù\ˆXØÙ\ÜÈ^ÜBˆXØÙ\Ü×Ü]HÜËœ]š›Ú[Šİ]]Ù\‹ˆ˜XØÙ\ÜË\™]šY]Ë^Ù]WÜİŸK˜ÜİˆŠCBˆÚ]Ü[ŠXØÙ\Ü×Ü]È‹™]Û[™OHˆ‹[˜ÛÙ[™ÏH]‹NŠH\ÈƒBˆÜš]\ˆHÜİ‹‘XİÜš]\Š‹šY[˜[Y\Ï]\Ù\œÖÌKšÙ^\Ê
JCBˆÜš]\‹Üš]ZXY\Š
CBˆÜš]\‹Üš]\›İÜÊ\Ù\œÊCBˆš[
ˆ—ˆ^ÜYˆØXØÙ\Ü×Ü]HŠCBƒBˆÈ˜Z[š[™È^ÜBˆ˜Z[š[™×Ü]HÜËœ]š›Ú[Šİ]]Ù\‹ˆ˜Z[š[™ËXÛÛ\X[˜ÙK^Ù]WÜİŸK˜ÜİˆŠCBˆÚ]Ü[Š˜Z[š[™×Ü]È‹™]Û[™OHˆ‹[˜ÛÙ[™ÏH]‹NŠH\ÈƒBˆÜš]\ˆHÜİ‹‘XİÜš]\Š‹šY[˜[Y\Ï]˜Z[š[™ÖÌKšÙ^\Ê
JCBˆÜš]\‹Üš]ZXY\Š
CBˆÜš]\‹Üš]\›İÜÊ˜Z[š[™ÊCBˆš[
ˆˆ^ÜYˆİ˜Z[š[™×Ü]HŠCBƒBˆÈ]Ú^ÜBˆ]ÚÜ]HÜËœ]š›Ú[Šİ]]Ù\‹ˆœ]ÚXÛÛ\X[˜ÙK^Ù]WÜİŸK˜ÜİˆŠCBˆÚ]Ü[Š]ÚÜ]È‹™]Û[™OHˆ‹[˜ÛÙ[™ÏH]‹NŠH\ÈƒBˆÜš]\ˆHÜİ‹‘XİÜš]\Š‹šY[˜[Y\Ï\]Ú\ÖÌKšÙ^\Ê
JCBˆÜš]\‹Üš]ZXY\Š
CBˆÜš]\‹Üš]\›İÜÊ]Ú\ÊCBˆš[
ˆˆ^ÜYˆÜ]ÚÜ]HŠCBƒBˆÈš[™[™ÜÈ^ÜBˆš[™[™Ü×Ü]HÜËœ]š›Ú[Šİ]]Ù\‹ˆ™š[™[™ÜË^Ù]WÜİŸKšœÛÛˆŠCBˆÚ]Ü[Šš[™[™Ü×Ü]È‹[˜ÛÙ[™ÏH]‹NŠH\ÈƒBˆœÛÛ‹™[\
ÃBˆœ™\ÜÙ]Hˆ[Y\İ[\Bˆœİ[[X\HˆÃBˆİ[Ùš[™[™ÜÈˆ[Š[Ùš[™[™ÜÊKBˆ˜Üš]XØ[ˆÜš]XØ[ØÛİ[BˆšYÚˆYÚØÛİ[Bˆ›YY][HˆYY][WØÛİ[BˆKBˆ˜XØÙ\Ü×Üİ]ÈˆXØÙ\Ü×Üİ]ËBˆ˜Z[š[™×Üİ]Èˆ˜Z[š[™×Üİ]ËBˆœ]ÚÜİ]Èˆ]ÚÜİ]ËBˆ™š[™[™ÜÈˆ[Ùš[™[™ÜËBˆK‹[™[LŠCBˆš[
ˆˆ^ÜYˆÙš[™[™Ü×Ü]HŠCBƒBƒB™YˆXZ[Š
N‚ˆ\œÙ\ˆH\™Ü\œÙK\™İ[Y[\œÙ\Š\ØÜš\[ÛH‘Ù[™\˜]HHŞ[]XÈ]Y]]šY[˜ÙHXÚØYÙKˆŠBˆ\œÙ\‹˜YØ\™İ[Y[
›İ]]Ù\ˆ‹˜\™ÜÏHÈ‹[H“Ü[Û˜[İ]]\™XİÜHŠBˆ\œÙ\‹˜YØ\™İ[Y[
‹KX\Ë[Ùˆ‹\İH˜\×ÛÙˆ‹Y˜][HŒŒ‹LLH‹[H”™]šY]È]H[ˆVVVKSSKQ›Ü›X]ŠBˆ\™ÜÈH\œÙ\‹œ\œÙWØ\™ÜÊ
B‚ˆN‚ˆ\×ÛÙˆH]][YKœİœ[YJ\™ÜË˜\×ÛÙ‹‰VKI[KIYŠBˆ^Ù\˜[YQ\œ›Ü‚ˆ\œÙ\‹™\œ›ÜŠ‹KX\Ë[Ùˆ]\İ\ÙHVVVKSSKQŠB‚ˆÙ[™\˜]WÙ]šY[˜ÙWÜ™\Ü
\™ÜË›İ]]Ù\‹\×ÛÙX\×ÛÙŠBƒBƒBšYˆ×Û˜[YW×ÈOH—×ÛXZ[—×ÈƒBˆXZ[Š
CB