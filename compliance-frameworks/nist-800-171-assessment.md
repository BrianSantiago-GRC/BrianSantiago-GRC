# NIST SP 800-171 Rev 2 Self-Assessment

**Standard:** NIST Special Publication 800-171, Protecting Controlled Unclassified Information in Nonfederal Systems and Organizations

**Applicability:** Organizations handling CUI, including K-12 districts managing student records (FERPA), employee PII, and grant/contract data from federal agencies

**Assessment Date:** 2026-03-15

**Assessor:** Brian Santiago

---

## Scoring Methodology

Using the DoD NIST SP 800-171 Assessment Methodology:

- **Met:** The security requirement is implemented and operating as intended
- **Not Met:** The security requirement is not implemented or not operating as intended
- **N/A:** The requirement does not apply to the assessed scope

**SPRS Score Calculation:** Start at 110 points. Subtract weighted values for each unmet requirement per the DoD Assessment Methodology.

---

## 3.1 Access Control (22 requirements)

| ID | Requirement | Status | Evidence / Notes |
|----|------------|--------|-----------------|
| 3.1.1 | Limit system access to authorized users | Met | AD group policies, RBAC model documented |
| 3.1.2 | Limit system access to authorized transactions and functions | Met | Role-based permissions in SIS, EHR, and file shares |
| 3.1.3 | Control the flow of CUI in accordance with approved authorizations | Met | DLP rules on email, USB restrictions via GPO |
| 3.1.4 | Separate the duties of individuals to reduce risk | Met | SoD matrix documented, enforced in AD |
| 3.1.5 | Employ the principle of least privilege | Met | Quarterly access reviews, privilege escalation requires approval |
| 3.1.6 | Use non-privileged accounts for non-security functions | Met | Admin staff use separate admin accounts for elevated tasks |
| 3.1.7 | Prevent non-privileged users from executing privileged functions | Met | UAC enforced, admin rights removed from standard accounts |
| 3.1.8 | Limit unsuccessful logon attempts | Met | Account lockout after 5 failed attempts, 30-min lockout |
| 3.1.9 | Provide privacy and security notices consistent with CUI rules | Met | Login banners on all systems |
| 3.1.10 | Use session lock with pattern-hiding displays | Met | GPO: 10-minute screen lock, password required |
| 3.1.11 | Terminate sessions after defined conditions | Met | GPO: 30-minute idle timeout for remote sessions |
| 3.1.12 | Monitor and control remote access sessions | Met | VPN with MFA, session logging enabled |
| 3.1.13 | Employ cryptographic mechanisms for remote access | Met | TLS 1.2+ required for VPN and web apps |
| 3.1.14 | Route remote access via managed access control points | Met | All remote access routes through VPN concentrator |
| 3.1.15 | Authorize remote execution of privileged commands | Met | PAM solution for remote admin sessions |
| 3.1.16 | Authorize wireless access prior to allowing connections | Met | 802.1X with certificate-based auth for staff SSID |
| 3.1.17 | Protect wireless access using authentication and encryption | Met | WPA3-Enterprise on staff network, WPA2 on guest (isolated) |
| 3.1.18 | Control connection of mobile devices | Met | MDM enrollment required, conditional access policies |
| 3.1.19 | Encrypt CUI on mobile devices | Met | BitLocker on laptops, MDM encryption on mobile |
| 3.1.20 | Verify and control connections to external systems | Not Met | External connections not formally catalogued or reviewed |
| 3.1.21 | Limit use of portable storage devices | Met | USB storage blocked via GPO except approved devices |
| 3.1.22 | Control CUI posted or processed on publicly accessible systems | Met | Public web content review process documented |

**Access Control Score: 21/22 Met**

---

## 3.2 Awareness and Training (3 requirements)

| ID | Requirement | Status | Evidence / Notes |
|----|------------|--------|-----------------|
| 3.2.1 | Ensure personnel are aware of security risks associated with their activities | Met | Annual security awareness training via LMS |
| 3.2.2 | Ensure personnel are trained to carry out assigned security responsibilities | Met | Role-based training for IT staff, data custodians |
| 3.2.3 | Provide security awareness training on recognizing social engineering | Met | Quarterly phishing simulations, targeted training for failures |

**Awareness and Training Score: 3/3 Met**

---

## 3.3 Audit and Accountability (9 requirements)

| ID | Requirement | Status | Evidence / Notes |
|----|------------|--------|-----------------|
| 3.3.1 | Create and retain system audit logs | Met | Splunk deployment, 1-year retention |
| 3.3.2 | Ensure actions can be traced to individual users | Met | Unique user IDs, no shared accounts policy |
| 3.3.3 | Review and update logged events | Met | Annual log source review, quarterly tuning |
| 3.3.4 | Alert in the event of an audit logging process failure | Not Met | No automated alerting for log collection failures |
| 3.3.5 | Correlate audit review, analysis, and reporting | Not Met | Manual correlation only, no SIEM correlation rules |
| 3.3.6 | Provide audit record reduction and report generation | Met | Splunk dashboards and saved searches |
| 3.3.7 | Provide a system capability for time synchronization | Met | NTP configured to NIST time servers |
| 3.3.8 | Protect audit information and tools from unauthorized access | Met | Splunk access restricted to security team |
| 3.3.9 | Limit management of audit logging to authorized individuals | Met | Role-based access in Splunk, change log enabled |

**Audit and Accountability Score: 7/9 Met**

---

## 3.4 Configuration Management (9 requirements)

| ID | Requirement | Status | Evidence / Notes |
|----|------------|--------|-----------------|
| 3.4.1 | Establish and maintain baseline configurations | Not Met | Baselines documented but not enforced via automation |
| 3.4.2 | Establish and enforce security configuration settings | Not Met | Settings documented but compliance scanning not in place |
| 3.4.3 | Track, review, approve changes to organizational systems | Met | Change advisory board, ServiceNow tickets required |
| 3.4.4 | Analyze the security impact of changes prior to implementation | Met | Security review step in change management process |
| 3.4.5 | Define, document, approve physical and logical access restrictions | Met | Network segmentation diagram, firewall rule reviews |
| 3.4.6 | Employ the principle of least functionality | Met | Unnecessary services disabled per hardening checklist |
| 3.4.7 | Restrict, disable, or prevent nonessential programs | Met | Application allowlisting on CUI systems |
| 3.4.8 | Apply deny-by-exception policy for unauthorized software | Met | Software installation requires admin approval |
| 3.4.9 | Control and monitor user-installed software | Met | SCCM inventory, monthly review of installed software |

**Configuration Management Score: 7/9 Met**

---

## 3.5 Identification and Authentication (11 requirements)

| ID | Requirement | Status | Evidence / Notes |
|----|------------|--------|-----------------|
| 3.5.1 | Identify system users, processes, or devices | Met | AD for users, SCCM for devices, service accounts documented |
| 3.5.2 | Authenticate users, processes, or devices as a prerequisite | Met | AD authentication required for all system access |
| 3.5.3 | Use multifactor authentication for local and network access | Met | Azure AD MFA for all staff, conditional access policies |
| 3.5.4 | Employ replay-resistant authentication mechanisms | Met | Kerberos and SAML tokens with replay protection |
| 3.5.5 | Prevent reuse of identifiers for a defined period | Met | AD policy: no reuse of usernames for 2 years |
| 3.5.6 | Disable identifiers after a defined period of inactivity | Met | 90-day inactivity disables account via automated script |
| 3.5.7 | Enforce minimum password complexity | Met | 12-char minimum, complexity requirements via GPO |
| 3.5.8 | Prohibit password reuse for a specified number of generations | Met | 24-password history enforced |
| 3.5.9 | Allow temporary password use with immediate change | Met | Temporary passwords require change at first login |
| 3.5.10 | Store and transmit only cryptographically-protected passwords | Met | NTLM disabled, Kerberos AES encryption |
| 3.5.11 | Obscure feedback of authentication information | Met | Password masking on all login interfaces |

**Identification and Authentication Score: 11/11 Met**

---

## 3.6 Incident Response (3 requirements)

| ID | Requirement | Status | Evidence / Notes |
|----|------------|--------|-----------------|
| 3.6.1 | Establish incident handling capability | Met | IR plan, playbooks for ransomware, phishing, data breach |
| 3.6.2 | Track, document, and report incidents | Met | ServiceNow incident tracking, severity classification |
| 3.6.3 | Test the organizational incident response capability | Met | Bi-annual tabletop exercises documented |

**Incident Response Score: 3/3 Met**

---

## 3.7 Maintenance (6 requirements)

| ID | Requirement | Status | Evidence / Notes |
|----|------------|--------|-----------------|
| 3.7.1 | Perform maintenance on organizational systems | Met | Monthly patching schedule, NinjaOne for endpoint mgmt |
| 3.7.2 | Provide controls on tools used for maintenance | Met | Maintenance tools restricted to IT team |
| 3.7.3 | Ensure equipment removed for off-site maintenance is sanitized | Met | Data wipe procedure before off-site repair |
| 3.7.4 | Check media containing diagnostic programs for malware | Met | AV scan required before connecting external media |
| 3.7.5 | Require MFA for nonlocal maintenance sessions | Met | VPN + MFA required for remote maintenance |
| 3.7.6 | Supervise maintenance activities of personnel without required access | Met | Escort policy for vendors, access logs maintained |

**Maintenance Score: 6/6 Met**

---

## 3.8 Media Protection (9 requirements)

| ID | Requirement | Status | Evidence / Notes |
|----|------------|--------|-----------------|
| 3.8.1 | Protect system media containing CUI | Met | Locked storage for physical media, encryption for digital |
| 3.8.2 | Limit access to CUI on system media to authorized users | Met | Access controls on file shares and databases |
| 3.8.3 | Sanitize or destroy system media before disposal or reuse | Met | NIST 800-88 media sanitization procedure, certificates of destruction |
| 3.8.4 | Mark media with necessary CUI markings and distribution limitations | Not Met | No formal CUI marking program in place |
| 3.8.5 | Control access to media containing CUI and maintain accountability | Met | Media inventory for removable storage |
| 3.8.6 | Implement cryptographic mechanisms to protect CUI during transport | Met | Encrypted USB drives for authorized transfers |
| 3.8.7 | Control the use of removable media on system components | Met | USB restrictions via GPO |
| 3.8.8 | Prohibit the use of portable storage devices with no identifiable owner | Met | Only district-issued USB drives permitted |
| 3.8.9 | Protect the confidentiality of backup CUI at storage locations | Met | Encrypted backups, offsite storage with access controls |

**Media Protection Score: 8/9 Met**

---

## 3.9 Personnel Security (2 requirements)

| ID | Requirement | Status | Evidence / Notes |
|----|------------|--------|-----------------|
| 3.9.1 | Screen individuals prior to authorizing access to CUI | Met | Background checks for all employees, HR verification |
| 3.9.2 | Ensure CUI is protected during and after personnel actions | Met | Termination checklist, same-day access revocation |

**Personnel Security Score: 2/2 Met**

---

## 3.10 Physical Protection (6 requirements)

| ID | Requirement | Status | Evidence / Notes |
|----|------------|--------|-----------------|
| 3.10.1 | Limit physical access to authorized individuals | Met | Badge access for server rooms and data centers |
| 3.10.2 | Protect and monitor the physical facility and infrastructure | Met | Security cameras, visitor logs, alarm systems |
| 3.10.3 | Escort visitors and monitor visitor activity | Met | Visitor badge and escort policy enforced |
| 3.10.4 | Maintain audit logs of physical access | Met | Badge reader logs retained 1 year |
| 3.10.5 | Control and manage physical access devices | Met | Badge issuance/revocation tracked in access management system |
| 3.10.6 | Enforce safeguarding measures for CUI at alternate work sites | Met | Remote work policy requires encrypted devices, VPN |

**Physical Protection Score: 6/6 Met**

---

## 3.11 Risk Assessment (3 requirements)

| ID | Requirement | Status | Evidence / Notes |
|----|------------|--------|-----------------|
| 3.11.1 | Periodically assess the risk to operations and assets | Met | Annual risk assessment, quarterly reviews |
| 3.11.2 | Scan for vulnerabilities periodically and when new vulnerabilities are identified | Met | Weekly Qualys scans, patch Tuesday response |
| 3.11.3 | Remediate vulnerabilities in accordance with risk assessments | Met | SLA-based remediation: Critical 72hr, High 7d, Medium 30d |

**Risk Assessment Score: 3/3 Met**

---

## 3.12 Security Assessment (4 requirements)

| ID | Requirement | Status | Evidence / Notes |
|----|------------|--------|-----------------|
| 3.12.1 | Periodically assess security controls to determine effectiveness | Met | Annual control assessment, quarterly spot checks |
| 3.12.2 | Develop and implement plans of action to correct deficiencies | Met | POA&M maintained in compliance tracker |
| 3.12.3 | Monitor security controls on an ongoing basis | Not Met | Continuous monitoring program not fully established |
| 3.12.4 | Develop, document, and update system security plans | Met | SSP maintained, annual review cycle |

**Security Assessment Score: 3/4 Met**

---

## 3.13 System and Communications Protection (16 requirements)

| ID | Requirement | Status | Evidence / Notes |
|----|------------|--------|-----------------|
| 3.13.1 | Monitor, control, and protect communications at external boundaries | Met | Firewall with IPS, DMZ architecture |
| 3.13.2 | Employ architectural designs that promote effective security | Met | Network segmentation, CUI systems in separate VLAN |
| 3.13.3 | Separate user functionality from system management functionality | Met | Management interfaces on separate network segment |
| 3.13.4 | Prevent unauthorized and unintended information transfer | Met | DLP on email, web filtering, USB controls |
| 3.13.5 | Implement subnetworks for publicly accessible system components | Met | DMZ for public-facing services, isolated from internal |
| 3.13.6 | Deny network communications by default and allow by exception | Met | Default deny firewall rules, documented exceptions |
| 3.13.7 | Prevent remote devices from establishing non-remote connections simultaneously | Not Met | Split tunneling allowed on VPN for performance |
| 3.13.8 | Implement cryptographic mechanisms to prevent unauthorized disclosure during transmission | Met | TLS 1.2+ enforced for all CUI transmissions |
| 3.13.9 | Terminate network connections at the end of sessions | Met | Session timeouts configured on all services |
| 3.13.10 | Establish and manage cryptographic keys for required cryptography | Met | Key management procedures documented |
| 3.13.11 | Employ FIPS-validated cryptography when used to protect CUI | Not Met | Not all systems use FIPS-validated modules |
| 3.13.12 | Prohibit remote activation of collaborative computing devices | Met | Camera/mic activation requires user consent |
| 3.13.13 | Control and monitor the use of mobile code | Met | Browser security policies, script execution controls |
| 3.13.14 | Control and monitor the use of VoIP technologies | Met | VoIP on segmented VLAN, encrypted SIP |
| 3.13.15 | Protect the authenticity of communications sessions | Met | Certificate-based authentication for web services |
| 3.13.16 | Protect the confidentiality of CUI at rest | Met | BitLocker on endpoints, DB-level encryption |

**System and Communications Protection Score: 14/16 Met**

---

## 3.14 System and Information Integrity (7 requirements)

| ID | Requirement | Status | Evidence / Notes |
|----|------------|--------|-----------------|
| 3.14.1 | Identify, report, and correct system flaws in a timely manner | Met | Patch management policy with SLAs |
| 3.14.2 | Provide protection from malicious code at designated locations | Met | Endpoint protection on all systems, email gateway filtering |
| 3.14.3 | Monitor system security alerts and advisories | Met | CISA alerts, vendor advisories reviewed weekly |
| 3.14.4 | Update malicious code protection mechanisms when new releases are available | Met | Automated AV updates, daily signature updates |
| 3.14.5 | Perform periodic scans and real-time scans of files from external sources | Met | Real-time scanning enabled, weekly full scans |
| 3.14.6 | Monitor organizational systems to detect attacks and indicators of potential attacks | Not Met | Basic monitoring only, no behavioral analytics |
| 3.14.7 | Identify unauthorized use of organizational systems | Not Met | No automated detection of unauthorized access patterns |

**System and Information Integrity Score: 5/7 Met**

---

## Assessment Summary

| Control Family | Requirements | Met | Not Met | Score |
|---------------|-------------|-----|---------|-------|
| 3.1 Access Control | 22 | 21 | 1 | 95% |
| 3.2 Awareness and Training | 3 | 3 | 0 | 100% |
| 3.3 Audit and Accountability | 9 | 7 | 2 | 78% |
| 3.4 Configuration Management | 9 | 7 | 2 | 78% |
| 3.5 Identification and Authentication | 11 | 11 | 0 | 100% |
| 3.6 Incident Response | 3 | 3 | 0 | 100% |
| 3.7 Maintenance | 6 | 6 | 0 | 100% |
| 3.8 Media Protection | 9 | 8 | 1 | 89% |
| 3.9 Personnel Security | 2 | 2 | 0 | 100% |
| 3.10 Physical Protection | 6 | 6 | 0 | 100% |
| 3.11 Risk Assessment | 3 | 3 | 0 | 100% |
| 3.12 Security Assessment | 4 | 3 | 1 | 75% |
| 3.13 System and Communications Protection | 16 | 14 | 2 | 88% |
| 3.14 System and Information Integrity | 7 | 5 | 2 | 71% |
| **Total** | **110** | **99** | **11** | **90%** |

**Estimated SPRS Score: 77/110**

---

## Top Priority Remediation Items

| Priority | Requirement | Gap | Remediation Plan | Estimated Effort |
|----------|------------|-----|-----------------|-----------------|
| 1 | 3.14.6 - Attack monitoring | No behavioral analytics | Deploy EDR with behavioral detection, configure SIEM correlation rules | Medium |
| 2 | 3.14.7 - Unauthorized use detection | No automated detection | Implement UEBA or baseline anomaly detection in Splunk | Medium |
| 3 | 3.3.5 - Audit correlation | Manual correlation only | Build Splunk correlation searches for key attack patterns | Low |
| 4 | 3.3.4 - Audit failure alerting | No automated alerting | Configure Splunk alerts for log source health monitoring | Low |
| 5 | 3.4.1 - Baseline configurations | Not enforced via automation | Implement GPO compliance scanning or CIS-CAT tool | Medium |
| 6 | 3.4.2 - Security configuration enforcement | No compliance scanning | Deploy configuration compliance tool (CIS Benchmarks) | Medium |
| 7 | 3.13.11 - FIPS-validated cryptography | Not all systems validated | Audit cryptographic modules, enable FIPS mode where supported | Medium |
| 8 | 3.13.7 - Split tunneling | Allowed for performance | Evaluate full-tunnel VPN impact, implement for CUI users | Low |
| 9 | 3.12.3 - Continuous monitoring | Not fully established | Define continuous monitoring strategy, automate control checks | High |
| 10 | 3.8.4 - CUI marking | No marking program | Develop CUI marking guide, implement header/footer templates | Low |
| 11 | 3.1.20 - External connections | Not catalogued | Create external connection inventory, review annually | Low |

---

## Plan of Action and Milestones (POA&M)

| ID | Weakness | Milestone | Target Date | Status |
|----|---------|-----------|-------------|--------|
| POA-001 | 3.14.6, 3.14.7 - Advanced monitoring | Deploy EDR and UEBA | 2026-Q3 | Planned |
| POA-002 | 3.3.4, 3.3.5 - Audit automation | Implement Splunk correlation and alerting | 2026-Q2 | In Progress |
| POA-003 | 3.4.1, 3.4.2 - Configuration compliance | Deploy CIS-CAT or equivalent | 2026-Q3 | Planned |
| POA-004 | 3.13.11 - FIPS cryptography | Audit and enable FIPS modules | 2026-Q3 | Planned |
| POA-005 | 3.12.3 - Continuous monitoring | Establish ISCM program | 2026-Q4 | Planned |
| POA-006 | 3.8.4 - CUI marking | Develop marking program | 2026-Q2 | Planned |
