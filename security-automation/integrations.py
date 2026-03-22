"""
Live Integration Module for GRC Automation Tools
Demonstrates how the sample-data scripts connect to real data sources
in a production environment.

Each integration class shows the API calls, authentication, and data
transformation needed to feed into the existing audit and compliance tools.

These use only the Python standard library so they work on any system
without pip installs. For production, you would add error handling,
retry logic, and credential management (e.g., environment variables
or a secrets manager).

Author: Brian Santiago
"""

import json
import csv
import os
import sys
import subprocess
from datetime import datetime
from urllib.request import Request, urlopen
from urllib.parse import urlencode
from urllib.error import URLError


# -----------------------------------------------------------------------
# Active Directory integration via PowerShell (Windows environments)
# -----------------------------------------------------------------------

class ActiveDirectoryExporter:
    """
    Exports user access data from Active Directory for use with
    access_review_audit.py. Runs PowerShell commands to query AD.

    Usage:
        exporter = ActiveDirectoryExporter()
        exporter.export_users("ad_users.csv")
        # Then: python3 access_review_audit.py ad_users.csv
    """

    # PowerShell command to pull user attributes needed for access review
    PS_COMMAND = """
    Import-Module ActiveDirectory
    Get-ADUser -Filter {Enabled -eq $true} -Properties `
        DisplayName, Department, Title, MemberOf, `
        LastLogonDate, PasswordLastSet, Created `
    | Select-Object `
        SamAccountName,
        DisplayName,
        Department,
        Title,
        @{N='last_login';E={$_.LastLogonDate.ToString('yyyy-MM-dd')}},
        @{N='privileged';E={
            ($_.MemberOf | Where-Object {
                $_ -match 'Domain Admins|Enterprise Admins|Schema Admins'
            }).Count -gt 0
        }},
        @{N='mfa_enabled';E={
            # Check for Azure AD MFA registration
            # In hybrid environments, query MSOL or Graph API instead
            $true  # Placeholder - replace with actual MFA check
        }},
        Enabled
    | Export-Csv -Path '{output_path}' -NoTypeInformation
    """

    def export_users(self, output_path):
        """Run the AD export and save to CSV."""
        cmd = self.PS_COMMAND.format(output_path=output_path)
        print(f"[AD Export] Running PowerShell AD query...")
        try:
            result = subprocess.run(
                ["powershell", "-Command", cmd],
                capture_output=True, text=True, timeout=120
            )
            if result.returncode == 0:
                print(f"[AD Export] Exported to {output_path}")
                return True
            else:
                print(f"[AD Export] Error: {result.stderr}")
                return False
        except FileNotFoundError:
            print("[AD Export] PowerShell not available (Linux/macOS)")
            print("[AD Export] Use 'ldapsearch' or Microsoft Graph API instead")
            return False
        except subprocess.TimeoutExpired:
            print("[AD Export] Query timed out after 120 seconds")
            return False


# -----------------------------------------------------------------------
# Microsoft Graph API integration (Azure AD / Entra ID)
# -----------------------------------------------------------------------

class MicrosoftGraphIntegration:
    """
    Pulls user data and MFA status from Microsoft Entra ID via the
    Graph API. Works on any OS.

    Requires:
        - Azure AD App Registration with User.Read.All permission
        - Client credentials (app ID + secret) stored in environment vars

    Usage:
        graph = MicrosoftGraphIntegration()
        users = graph.get_users_with_mfa_status()
        graph.export_for_access_review(users, "graph_users.csv")
    """

    GRAPH_BASE = "https://graph.microsoft.com/v1.0"

    def __init__(self):
        self.tenant_id = os.environ.get("AZURE_TENANT_ID", "")
        self.client_id = os.environ.get("AZURE_CLIENT_ID", "")
        self.client_secret = os.environ.get("AZURE_CLIENT_SECRET", "")
        self._token = None

    def _get_token(self):
        """Get OAuth2 token using client credentials flow."""
        if self._token:
            return self._token

        url = f"https://login.microsoftonline.com/{self.tenant_id}/oauth2/v2.0/token"
        data = urlencode({
            "grant_type": "client_credentials",
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "scope": "https://graph.microsoft.com/.default",
        }).encode()

        req = Request(url, data=data, method="POST")
        resp = urlopen(req, timeout=30)
        result = json.loads(resp.read())
        self._token = result["access_token"]
        return self._token

    def _graph_get(self, endpoint):
        """Make an authenticated GET request to Graph API."""
        token = self._get_token()
        url = f"{self.GRAPH_BASE}{endpoint}"
        req = Request(url, headers={"Authorization": f"Bearer {token}"})
        resp = urlopen(req, timeout=30)
        return json.loads(resp.read())

    def get_users(self):
        """Get all enabled users with relevant attributes."""
        users = []
        endpoint = "/users?$filter=accountEnabled eq true&$select=displayName,userPrincipalName,department,jobTitle,signInActivity,assignedLicenses&$top=999"
        data = self._graph_get(endpoint)
        users.extend(data.get("value", []))

        # Handle pagination
        while "@odata.nextLink" in data:
            next_url = data["@odata.nextLink"].replace(self.GRAPH_BASE, "")
            data = self._graph_get(next_url)
            users.extend(data.get("value", []))

        return users

    def get_mfa_status(self):
        """Get MFA registration status for all users."""
        endpoint = "/reports/authenticationMethods/userRegistrationDetails"
        data = self._graph_get(endpoint)
        mfa_map = {}
        for entry in data.get("value", []):
            upn = entry.get("userPrincipalName", "")
            methods = entry.get("methodsRegistered", [])
            mfa_map[upn] = len(methods) > 1  # More than just password
        return mfa_map

    def get_directory_roles(self):
        """Get users assigned to privileged directory roles."""
        privileged_roles = [
            "Global Administrator", "Privileged Role Administrator",
            "Security Administrator", "Exchange Administrator",
            "SharePoint Administrator", "User Administrator",
        ]
        privileged_users = set()

        for role_name in privileged_roles:
            endpoint = f"/directoryRoles?$filter=displayName eq '{role_name}'"
            try:
                data = self._graph_get(endpoint)
                for role in data.get("value", []):
                    role_id = role["id"]
                    members = self._graph_get(f"/directoryRoles/{role_id}/members")
                    for member in members.get("value", []):
                        privileged_users.add(member.get("userPrincipalName", ""))
            except URLError:
                continue

        return privileged_users

    def export_for_access_review(self, output_path):
        """
        Pull users, MFA status, and roles, then export a CSV
        compatible with access_review_audit.py.
        """
        print("[Graph API] Fetching users from Entra ID...")
        users = self.get_users()
        print(f"[Graph API] Found {len(users)} active users")

        print("[Graph API] Checking MFA registration...")
        mfa_map = self.get_mfa_status()

        print("[Graph API] Checking privileged roles...")
        priv_users = self.get_directory_roles()

        rows = []
        for user in users:
            upn = user.get("userPrincipalName", "")
            sign_in = user.get("signInActivity", {})
            last_sign_in = sign_in.get("lastSignInDateTime", "")
            if last_sign_in:
                last_sign_in = last_sign_in[:10]  # Just the date part

            rows.append({
                "username": upn.split("@")[0],
                "display_name": user.get("displayName", ""),
                "department": user.get("department", ""),
                "role": user.get("jobTitle", ""),
                "mfa_enabled": str(mfa_map.get(upn, False)),
                "last_login": last_sign_in,
                "status": "Active",
                "privileged": str(upn in priv_users),
                "data_access": "Standard",  # Map from your data classification
            })

        with open(output_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=rows[0].keys())
            writer.writeheader()
            writer.writerows(rows)

        print(f"[Graph API] Exported {len(rows)} users to {output_path}")
        return output_path


# -----------------------------------------------------------------------
# Qualys Vulnerability Scanner integration
# -----------------------------------------------------------------------

class QualysIntegration:
    """
    Pulls vulnerability and patch data from the Qualys API for use with
    evidence_collector.py patch compliance checks.

    Requires:
        - Qualys API credentials in environment variables
        - API access enabled on your Qualys subscription

    Usage:
        qualys = QualysIntegration()
        qualys.export_patch_compliance("patch_data.csv")
    """

    def __init__(self):
        self.api_url = os.environ.get("QUALYS_API_URL", "https://qualysapi.qualys.com")
        self.username = os.environ.get("QUALYS_USERNAME", "")
        self.password = os.environ.get("QUALYS_PASSWORD", "")

    def _qualys_request(self, endpoint, params=None):
        """Make an authenticated request to the Qualys API."""
        import base64
        url = f"{self.api_url}{endpoint}"
        if params:
            url += "?" + urlencode(params)

        credentials = base64.b64encode(
            f"{self.username}:{self.password}".encode()
        ).decode()

        req = Request(url, headers={
            "Authorization": f"Basic {credentials}",
            "X-Requested-With": "Python GRC Automation",
        })
        resp = urlopen(req, timeout=60)
        return resp.read().decode()

    def get_host_detections(self, severity_filter="3,4,5"):
        """
        Get vulnerability detections at specified severity levels.
        Severity: 1=Info, 2=Low, 3=Medium, 4=High, 5=Critical
        """
        print(f"[Qualys] Fetching detections (severity >= {severity_filter})...")
        # In production, use the Qualys VMDR API:
        # POST /api/2.0/fo/asset/host/vm/detection/
        # with: action=list, severities=3,4,5, status=New,Active,Re-Opened
        #
        # The response is XML. Parse with xml.etree.ElementTree.
        # Each HOST_LIST/HOST has IP, DNS, and DETECTION_LIST entries.
        print("[Qualys] API call would go here - see inline comments for endpoint details")
        return []

    def export_patch_compliance(self, output_path):
        """
        Export patch compliance data in the format expected by
        evidence_collector.py patch compliance checks.
        """
        # In production, this would call get_host_detections() and
        # transform the results into the expected CSV format:
        #
        # hostname,os,critical_patches,high_patches,last_scan,compliant,data_type
        #
        # The data_type column maps to your asset inventory / CMDB
        # to identify systems handling ePHI, Student Records, etc.
        print("[Qualys] Would export patch compliance data to:", output_path)
        print("[Qualys] Format: hostname,os,critical_patches,high_patches,last_scan,compliant,data_type")


# -----------------------------------------------------------------------
# Splunk integration for log evidence
# -----------------------------------------------------------------------

class SplunkIntegration:
    """
    Queries Splunk for audit evidence needed by compliance checks.
    Demonstrates how to pull login events, failed authentications,
    and privileged actions for audit evidence packages.

    Requires:
        - Splunk REST API access
        - Authentication token in environment variable

    Usage:
        splunk = SplunkIntegration()
        results = splunk.search_failed_logins(days=30)
        results = splunk.search_privileged_actions(days=7)
    """

    def __init__(self):
        self.base_url = os.environ.get("SPLUNK_URL", "https://splunk.example.com:8089")
        self.token = os.environ.get("SPLUNK_TOKEN", "")

    def _splunk_search(self, query, earliest="-30d"):
        """Run a Splunk search and return results."""
        url = f"{self.base_url}/services/search/v2/jobs/export"
        data = urlencode({
            "search": f"search {query}",
            "earliest_time": earliest,
            "output_mode": "json",
        }).encode()

        req = Request(url, data=data, headers={
            "Authorization": f"Bearer {self.token}",
        })
        try:
            resp = urlopen(req, timeout=120)
            return json.loads(resp.read())
        except URLError as e:
            print(f"[Splunk] Connection error: {e}")
            return {"results": []}

    def search_failed_logins(self, days=30):
        """
        Search for failed login events. Evidence for NIST 800-53 AC-7
        and HIPAA 164.312(d).
        """
        query = f"""index=wineventlog EventCode=4625 earliest=-{days}d
        | stats count by Account_Name, src_ip, Workstation_Name
        | where count > 5
        | sort -count"""
        print(f"[Splunk] Searching failed logins (last {days} days)...")
        return self._splunk_search(query, f"-{days}d")

    def search_privileged_actions(self, days=7):
        """
        Search for privileged account activity. Evidence for NIST 800-53 AU-2
        and HIPAA 164.312(b).
        """
        query = f"""index=wineventlog
        (EventCode=4672 OR EventCode=4688 OR EventCode=4720 OR EventCode=4726)
        earliest=-{days}d
        | stats count by EventCode, Account_Name, ComputerName
        | sort -count"""
        print(f"[Splunk] Searching privileged actions (last {days} days)...")
        return self._splunk_search(query, f"-{days}d")

    def search_account_changes(self, days=30):
        """
        Search for account creation, deletion, and modification.
        Evidence for NIST 800-53 AC-2 and HIPAA 164.308(a)(4).
        """
        query = f"""index=wineventlog
        (EventCode=4720 OR EventCode=4722 OR EventCode=4725 OR EventCode=4726
         OR EventCode=4738 OR EventCode=4740 OR EventCode=4767)
        earliest=-{days}d
        | stats count by EventCode, Account_Name, src_user
        | sort -EventCode"""
        print(f"[Splunk] Searching account changes (last {days} days)...")
        return self._splunk_search(query, f"-{days}d")

    def export_evidence_package(self, output_dir, days=30):
        """
        Export a complete audit evidence package from Splunk.
        Maps to audit-artifacts/audit-evidence-guide.md.
        """
        os.makedirs(output_dir, exist_ok=True)
        date_str = datetime.now().strftime("%Y%m%d")

        searches = {
            f"failed-logins-{date_str}.json": self.search_failed_logins(days),
            f"privileged-actions-{date_str}.json": self.search_privileged_actions(7),
            f"account-changes-{date_str}.json": self.search_account_changes(days),
        }

        for filename, results in searches.items():
            path = os.path.join(output_dir, filename)
            with open(path, "w", encoding="utf-8") as f:
                json.dump(results, f, indent=2)
            print(f"[Splunk] Exported: {path}")


# -----------------------------------------------------------------------
# n8n Webhook integration for workflow automation
# -----------------------------------------------------------------------

class N8nWebhookIntegration:
    """
    Sends GRC automation results to n8n webhooks to trigger
    downstream workflows: Slack alerts, Jira ticket creation,
    email notifications, or dashboard updates.

    Usage:
        n8n = N8nWebhookIntegration()
        n8n.send_findings(findings, workflow="access-review")
        n8n.send_compliance_alert(control="MFA", status="FAIL")
    """

    def __init__(self):
        self.base_url = os.environ.get("N8N_WEBHOOK_URL", "https://n8n.example.com/webhook")

    def _post_webhook(self, path, payload):
        """Send a POST request to an n8n webhook."""
        url = f"{self.base_url}/{path}"
        data = json.dumps(payload).encode()
        req = Request(url, data=data, headers={
            "Content-Type": "application/json",
        }, method="POST")
        try:
            resp = urlopen(req, timeout=30)
            print(f"[n8n] Webhook triggered: {path} (status {resp.status})")
            return True
        except URLError as e:
            print(f"[n8n] Webhook failed: {e}")
            return False

    def send_findings(self, findings, workflow="grc-findings"):
        """
        Send audit findings to n8n for automated triage.
        Workflow can route to Slack, Jira, or email based on severity.
        """
        payload = {
            "timestamp": datetime.now().isoformat(),
            "source": "grc-automation",
            "workflow": workflow,
            "summary": {
                "total": len(findings),
                "critical": sum(1 for f in findings if f.get("severity") == "Critical"),
                "high": sum(1 for f in findings if f.get("severity") == "High"),
            },
            "findings": findings,
        }
        return self._post_webhook(workflow, payload)

    def send_compliance_alert(self, control, status, details=""):
        """
        Send a compliance status alert. Use for real-time notifications
        when a control check fails (e.g., MFA rate drops below threshold).
        """
        payload = {
            "timestamp": datetime.now().isoformat(),
            "alert_type": "compliance_status",
            "control": control,
            "status": status,
            "details": details,
        }
        return self._post_webhook("compliance-alert", payload)


# -----------------------------------------------------------------------
# CLI demo: show available integrations and how to use them
# -----------------------------------------------------------------------

def main():
    print("\n" + "=" * 70)
    print("  GRC AUTOMATION - LIVE INTEGRATION MODULE")
    print("  Shows how to connect scripts to real data sources")
    print("=" * 70)

    integrations = [
        {
            "name": "Active Directory (PowerShell)",
            "class": "ActiveDirectoryExporter",
            "env_vars": ["(none - uses AD module directly)"],
            "feeds_into": "access_review_audit.py",
            "example": "exporter = ActiveDirectoryExporter()\nexporter.export_users('ad_users.csv')",
        },
        {
            "name": "Microsoft Graph / Entra ID",
            "class": "MicrosoftGraphIntegration",
            "env_vars": ["AZURE_TENANT_ID", "AZURE_CLIENT_ID", "AZURE_CLIENT_SECRET"],
            "feeds_into": "access_review_audit.py",
            "example": "graph = MicrosoftGraphIntegration()\ngraph.export_for_access_review('graph_users.csv')",
        },
        {
            "name": "Qualys Vulnerability Scanner",
            "class": "QualysIntegration",
            "env_vars": ["QUALYS_API_URL", "QUALYS_USERNAME", "QUALYS_PASSWORD"],
            "feeds_into": "evidence_collector.py (patch compliance)",
            "example": "qualys = QualysIntegration()\nqualys.export_patch_compliance('patches.csv')",
        },
        {
            "name": "Splunk SIEM",
            "class": "SplunkIntegration",
            "env_vars": ["SPLUNK_URL", "SPLUNK_TOKEN"],
            "feeds_into": "evidence_collector.py (audit logs)",
            "example": "splunk = SplunkIntegration()\nsplunk.export_evidence_package('./evidence/')",
        },
        {
            "name": "n8n Workflow Automation",
            "class": "N8nWebhookIntegration",
            "env_vars": ["N8N_WEBHOOK_URL"],
            "feeds_into": "All scripts (sends results to Slack, Jira, email)",
            "example": "n8n = N8nWebhookIntegration()\nn8n.send_findings(findings)",
        },
    ]

    for i, integ in enumerate(integrations, 1):
        print(f"\n  {i}. {integ['name']}")
        print(f"     Class: {integ['class']}")
        print(f"     Env vars: {', '.join(integ['env_vars'])}")
        print(f"     Feeds into: {integ['feeds_into']}")
        print(f"     Example:")
        for line in integ["example"].split("\n"):
            print(f"       {line}")

    print(f"\n{'=' * 70}")
    print("  Set the required environment variables, then import this module")
    print("  in your scripts or use the classes directly.")
    print(f"{'=' * 70}\n")


if __name__ == "__main__":
    main()
