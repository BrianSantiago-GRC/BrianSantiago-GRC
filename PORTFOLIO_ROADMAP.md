# Cybersecurity / GRC Portfolio Roadmap

Date updated: 2026-05-15
Status: active execution roadmap

## Portfolio Objective

Build a focused cybersecurity/GRC portfolio that proves practical security operations, Microsoft security, compliance operations, and documentation maturity.

The portfolio should make recruiters think:

> This candidate has real operational exposure, practical project work, and strong growth potential.

It should not look like fake enterprise engineering, senior security architecture, or AI-generated filler.

## Portfolio Rules

- Keep the portfolio to 6 total projects.
- Finish depth before adding quantity.
- Every project must be explainable in an interview.
- Every project must include a README, screenshots or evidence, lessons learned, and a LinkedIn-ready summary.
- Do not claim production ownership, enterprise SOC work, threat hunting, detection engineering, or senior GRC authority.
- Use grounded language: built, practiced, documented, reviewed, analyzed, mapped, learned, supported.

## Final Portfolio Set

| Order | Project | Category | Status | Priority |
|---:|---|---|---|---|
| 1 | Phishing Analysis Workflow | Operational Security / Security Operations | Completed documentation; screenshot polish pending | Complete proof |
| 2 | Microsoft Sentinel Honeypot SIEM Lab | Security Operations | Completed documentation; screenshots not captured | Complete proof |
| 3 | Entra ID Identity Security Review | Microsoft Security / GRC | Completed with redacted evidence | Complete proof |
| 4 | Microsoft Defender Endpoint Investigation Walkthrough | Microsoft Security / Security Operations | Completed with sanitized evidence | Complete proof |
| 5 | GRC Access Review and Audit Evidence Pack | GRC / Compliance | Completed and published | Complete proof |
| 6 | Vulnerability Remediation Workflow | Operational Security / GRC | Planned | Medium |

## Execution Order

1. Finish phishing screenshots and evidence polish.
2. Use completed Microsoft Sentinel Honeypot SIEM Lab in resume, LinkedIn, and interviews. Recreate screenshots only if needed.
3. Use completed Entra ID Identity Security Review in GitHub, LinkedIn, resume bullets, and interviews.
4. Use completed Microsoft Defender Endpoint Investigation Walkthrough in GitHub, LinkedIn, resume bullets, and interviews.
5. Use completed GRC Access Review and Audit Evidence Pack in GitHub, LinkedIn, resume bullets, and interviews.
6. Build Vulnerability Remediation Workflow after the completed projects are integrated into applications.

Do not start more than one new project at a time.

---

## Project 1: Phishing Analysis Workflow

**Purpose:** Show a realistic junior SOC phishing triage workflow using Microsoft 365 context, user reporting, header review, IOC extraction, risk classification, containment recommendations, and incident notes.

**Skills Demonstrated:**
- Phishing triage
- Email header review concepts
- Suspicious link and attachment review
- IOC extraction
- Incident documentation
- Escalation criteria
- Microsoft 365 security operations awareness

**Tools Used:**
- Microsoft 365 phishing investigation context
- Sanitized phishing scenario
- Header analyzer
- URL/hash reputation lookup
- IOC checklist
- Markdown documentation

**Screenshots Needed:**
- Sanitized suspicious email scenario
- Email header/authentication result
- URL reputation review
- Completed IOC checklist
- Completed incident notes

**Interview Value:** Strong. Gives a concrete story for phishing triage, evidence handling, documentation, escalation, and user reporting.

**LinkedIn Value:** Strong. Supports posts about phishing indicators, analyst timeline, lessons learned, and completed project evidence.

**GitHub Value:** Strong. Already readable and completed as documentation; screenshots make it stronger.

**Realism Score:** 9/10

**Difficulty Level:** Beginner to junior SOC

**Estimated Completion Time:** Core project complete. Evidence polish: 2-4 hours.

---

## Project 2: Microsoft Sentinel Honeypot SIEM Lab

**Purpose:** Document a completed Microsoft Sentinel honeypot lab focused on failed logon review, basic KQL, SIEM triage thinking, and junior SOC incident notes.

This project shows how a junior analyst reviews authentication activity, organizes evidence, documents limitations, and writes clear follow-up notes without pretending to own a production SOC.

**Skills Demonstrated:**
- SIEM basics
- Basic KQL queries
- Sign-in and audit log review
- Alert triage thinking
- Incident notes
- Evidence-based escalation
- Microsoft identity log awareness

**Tools Used:**
- Microsoft Sentinel
- Azure Log Analytics Workspace
- Windows Security Events
- KQL
- Markdown documentation

**Screenshots Needed If Recreated Later:**
- Sentinel workspace overview
- Log Analytics query screen
- Basic KQL query results
- Example alert or incident view
- Investigation summary or incident notes

Note: screenshots were not captured during the completed lab. Do not fake screenshots. Add them only if the lab is recreated or the original environment can be safely revisited.

**Interview Value:** Strong. Supports SOC Analyst I and Security Analyst interviews without pretending to be a detection engineer.

**LinkedIn Value:** Strong. Useful for posts on learning SIEM basics, alert context, and incident documentation.

**GitHub Value:** Strong. Published as `Microsoft-Sentinel-SIEM` and functions as a completed SOC anchor project through written evidence, KQL, analyst timeline, incident notes, and lessons learned. Screenshots remain a future polish item.

**Realism Score:** 8/10

**Difficulty Level:** Junior security operations

**Estimated Completion Time:** Core documentation complete. Screenshot recreation only if useful: 2-4 hours.

---

## Project 3: Entra ID Identity Security Review

**Purpose:** Document a Microsoft Entra ID identity security review showing how Security Defaults, authentication methods, admin roles, sign-in logs, user access, and Conditional Access concepts support operational security and GRC.

The project is completed with redacted evidence and should be presented as a review and recommendation project, not an enterprise identity ownership claim.

**Skills Demonstrated:**
- Identity and access management
- MFA review
- Sign-in log review
- Conditional Access concepts
- Access control documentation
- GRC evidence thinking
- Microsoft security operations awareness

**Tools Used:**
- Microsoft Entra ID
- Microsoft 365 admin context
- Sign-in logs if available
- MFA status review
- Conditional Access templates or documentation
- Markdown checklist

**Screenshots / Evidence Included:**
- Entra admin overview
- Active users / test accounts
- Authentication methods
- Security Defaults
- Roles and administrators
- Sign-in logs
- Conditional Access overview
- Access review checklist
- Findings and recommendations

**Interview Value:** Very strong. Identity is the cleanest bridge from IT support into security operations and GRC.

**LinkedIn Value:** Strong. Good for posts on MFA, risky sign-ins, access reviews, and operational identity security.

**GitHub Value:** Strong. Published as `entra-identity-security-review` with sanitized screenshots, review notes, findings, recommendations, and evidence documentation.

**Realism Score:** 9/10

**Difficulty Level:** Junior to intermediate Microsoft security / GRC

**Estimated Completion Time:** Complete. Future polish only if a lab Conditional Access policy design is added.

---

## Project 4: Microsoft Defender Endpoint Investigation Walkthrough

**Purpose:** Document a realistic endpoint investigation workflow using Microsoft Defender and Windows evidence.

The project focuses on reviewing endpoint context, checking Defender status, collecting basic evidence, documenting findings, and recommending containment or remediation.

**Skills Demonstrated:**
- Endpoint security awareness
- Alert or suspicious activity review
- Device/user context review
- Windows Event Viewer review
- Defender status validation
- Containment recommendation writing
- Incident timeline documentation

**Tools Used:**
- Microsoft Defender concepts
- Windows Security
- Windows Event Viewer
- PowerShell commands such as `Get-MpComputerStatus`
- Microsoft Defender portal or evaluation lab if available
- Markdown documentation

**Screenshots / Evidence Included:**
- Windows Security / Defender status
- PowerShell Defender status output
- Event Viewer Security log
- Event Viewer System log
- Endpoint investigation timeline
- Containment and remediation recommendations

**Interview Value:** Strong. Helps explain how IT support troubleshooting transfers into endpoint security investigation.

**LinkedIn Value:** Medium to strong. Useful for posts about endpoint visibility, containment thinking, and clear notes.

**GitHub Value:** Strong. Published as `microsoft-defender-endpoint-investigation` with sanitized screenshots, evidence notes, investigation timeline, lessons learned, and remediation recommendations.

**Realism Score:** 8/10

**Difficulty Level:** Junior to intermediate security operations

**Estimated Completion Time:** Complete. Future polish only if a Microsoft Defender portal/evaluation screenshot is added later.

---

## Project 5: GRC Access Review and Audit Evidence Pack

**Purpose:** Build a practical evidence pack showing how an access review can be documented for audit readiness.

The project connects user access, review evidence, exceptions, control mapping, and remediation follow-up.

**Skills Demonstrated:**
- Access review documentation
- Audit evidence organization
- Control mapping
- Risk and exception tracking
- HIPAA / NIST CSF awareness
- Compliance operations support
- Clear evidence labeling

**Tools Used:**
- Sanitized user access export
- Microsoft 365 / Entra ID context
- Sanitized spreadsheet or CSV practice data
- NIST CSF concepts
- HIPAA safeguard concepts
- Markdown documentation

**Screenshots / Evidence Included:**
- Completed access review tracker
- Evidence checklist
- Control mapping table
- Exception/remediation log
- Final audit-ready summary

**Interview Value:** Very strong. Gives GRC and compliance interviews a concrete example of audit support, access review, and evidence handling.

**LinkedIn Value:** Medium to strong. Good for posts about audit readiness, evidence quality, and access reviews.

**GitHub Value:** Strong. Published as `grc-access-review-audit-evidence-pack` so recruiters can quickly understand the GRC value.

**Realism Score:** 9/10

**Difficulty Level:** Junior GRC / compliance operations

**Estimated Completion Time:** Complete. Future polish only if screenshots or visuals improve recruiter scanning.

---

## Project 6: Vulnerability Remediation Workflow

**Purpose:** Document a realistic vulnerability remediation process from finding intake to prioritization, ownership, remediation notes, validation, and closure.

The focus is operational follow-through, not exploitation or advanced vulnerability research.

**Skills Demonstrated:**
- Vulnerability management basics
- CVSS/severity interpretation
- Asset ownership tracking
- Remediation planning
- Exception documentation
- Validation and closure notes
- IT/security communication

**Tools Used:**
- Nessus Essentials, OpenVAS, Defender vulnerability context, or sanitized training finding
- NVD / CVE references
- Windows Update or configuration evidence
- Markdown remediation workflow
- Simple tracker table

**Screenshots Needed:**
- Sanitized vulnerability finding
- Severity/CVSS reference
- Affected asset example
- Remediation or patch evidence
- Closure/validation notes

**Interview Value:** Strong. Connects IT support, patching, risk, and security follow-up.

**LinkedIn Value:** Medium. Good for practical posts about remediation workflow and why scanning is not the same as closure.

**GitHub Value:** Medium to strong. Best when it shows before/after evidence and clean documentation.

**Realism Score:** 8/10

**Difficulty Level:** Junior to intermediate operational security

**Estimated Completion Time:** 8-12 hours

---

## Deferred Projects

Do not start these until at least four roadmap projects are complete with evidence:

- Splunk detection lab
- Security automation workflow
- Large Microsoft hardening project
- Large dashboard system
- Multi-tool SOC architecture

Reason: these can become shallow, overbuilt, or hard to defend in interviews.

## Completion Standard

Each project is complete only when it has:

- README
- Clear purpose
- Tools used
- Steps performed
- Screenshots or evidence
- Lessons learned
- Future improvements
- LinkedIn-ready summary
- Interview talking point

## Next 30-Day Priorities

1. Add completed GRC project to LinkedIn Projects and Featured.
2. Add one GRC project bullet to the GRC resume variant.
3. Use completed Entra, Defender, and GRC projects in applications, LinkedIn, resume bullets, and interviews.
4. Submit the next 10 targeted applications using the updated portfolio proof.
5. Build Vulnerability Remediation Workflow only after the completed projects are integrated into career materials.

## Anti-Overengineering Rule

Do not expand this portfolio until at least four projects are complete with screenshots and interview notes.

More projects will not help if the existing ones are unfinished.
