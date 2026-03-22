# ISO 27001:2022 Gap Analysis - Annex A Controls

**Standard:** ISO 27001:2022

**Scope:** Information security management for a K-12 organization

**Assessment Date:** 2026-01-25

**Assessor:** Brian Santiago

---

## Assessment Key

| Status | Definition |
|--------|-----------|
| Conforming | Control is fully implemented and operating effectively |
| Partially Conforming | Control exists but has gaps in design or operation |
| Non-Conforming | Control is missing or not effective |
| N/A | Control is not applicable (with justification) |

---

## Annex A Assessment Summary

### A.5 - Organizational Controls

| Control | Title | Status | Gap | Remediation |
|---------|-------|--------|-----|-------------|
| A.5.1 | Policies for information security | Conforming | - | Policy library in place |
| A.5.2 | Information security roles | Conforming | - | RACI documented |
| A.5.3 | Segregation of duties | Conforming | - | SoD in access control policy |
| A.5.4 | Management responsibilities | Conforming | - | Leadership reviews risks quarterly |
| A.5.5 | Contact with authorities | Partially | Need formal contact list | Build regulatory contact register |
| A.5.6 | Contact with special interest groups | Partially | Informal only | Document ISAC and peer group memberships |
| A.5.7 | Threat intelligence | Partially | Basic CISA feed only | Add structured TI ingestion |
| A.5.8 | Information security in project management | Non-Conforming | No formal process | Add security review gate to project lifecycle |
| A.5.9 | Inventory of information and other assets | Partially | Endpoints tracked, software gaps | Complete CMDB |
| A.5.10 | Acceptable use of information | Conforming | - | AUP in policy library |
| A.5.11 | Return of assets | Conforming | - | Offboarding checklist |
| A.5.12 | Classification of information | Conforming | - | Data classification policy |
| A.5.13 | Labelling of information | Partially | Not consistently applied | Implement email/document labels |
| A.5.14 | Information transfer | Conforming | - | Encryption in transit enforced |
| A.5.15 | Access control | Conforming | - | RBAC with MFA |
| A.5.16 | Identity management | Conforming | - | AD lifecycle management |
| A.5.17 | Authentication information | Conforming | - | Password policy, MFA |
| A.5.18 | Access rights | Conforming | - | Quarterly reviews |
| A.5.19 | Information security in supplier relationships | Partially | Assessments done; no formal program | Build TPRM program document |
| A.5.20 | Information security in supplier agreements | Conforming | - | BAAs and security clauses |
| A.5.21 | Managing information security in ICT supply chain | Non-Conforming | No supply chain risk process | Develop ICT supply chain assessment |
| A.5.22 | Monitoring, review of supplier services | Partially | Annual review; no continuous | Add SLA monitoring cadence |
| A.5.23 | Information security for cloud services | Partially | Some controls; no cloud policy | Draft cloud security policy |
| A.5.24 | Incident management planning | Conforming | - | IR plan with playbooks |
| A.5.25 | Assessment and decision on events | Conforming | - | Triage procedure in IR plan |
| A.5.26 | Response to incidents | Conforming | - | Playbooks per incident type |
| A.5.27 | Learning from incidents | Partially | Ad hoc lessons learned | Formalize post-incident review process |
| A.5.28 | Collection of evidence | Partially | Basic; no chain of custody | Add evidence handling procedure |
| A.5.29 | Information security during disruption | Partially | DR plan exists, not tested | Annual DR test |
| A.5.30 | ICT readiness for business continuity | Partially | Backup tested; no full BCM | Develop BCP |
| A.5.31 | Legal, statutory, regulatory requirements | Conforming | - | HIPAA/FERPA mapped |
| A.5.32 | Intellectual property rights | Conforming | - | Software licensing tracked |
| A.5.33 | Protection of records | Conforming | - | Retention schedule |
| A.5.34 | Privacy and protection of PII | Conforming | - | Privacy procedures align to HIPAA |
| A.5.35 | Independent review of information security | Non-Conforming | No external review | Plan for annual independent assessment |
| A.5.36 | Compliance with policies and standards | Conforming | - | Internal reviews conducted |
| A.5.37 | Documented operating procedures | Conforming | - | SOPs documented |

### A.6 - People Controls

| Control | Title | Status | Gap | Remediation |
|---------|-------|--------|-----|-------------|
| A.6.1 | Screening | Conforming | - | Background checks pre-hire |
| A.6.2 | Terms and conditions of employment | Conforming | - | Security clauses in contracts |
| A.6.3 | Information security awareness, education, training | Conforming | - | Quarterly training program |
| A.6.4 | Disciplinary process | Conforming | - | HR policy |
| A.6.5 | Responsibilities after termination | Conforming | - | NDA, offboarding process |
| A.6.6 | Confidentiality or NDA | Conforming | - | Signed at hire |
| A.6.7 | Remote working | Conforming | - | VPN + MFA required |
| A.6.8 | Information security event reporting | Conforming | - | Reporting procedure in IR plan |

### A.7 - Physical Controls

| Control | Title | Status | Gap | Remediation |
|---------|-------|--------|-----|-------------|
| A.7.1 | Physical security perimeters | Conforming | - | Badge access, locked rooms |
| A.7.2 | Physical entry | Conforming | - | Badge + visitor policy |
| A.7.3 | Securing offices, rooms, facilities | Conforming | - | Server room secured |
| A.7.4 | Physical security monitoring | Partially | Badge logs only | Add camera integration |
| A.7.5 | Protecting against physical and environmental threats | Conforming | - | UPS, fire suppression |
| A.7.6 | Working in secure areas | Conforming | - | Escort policy |
| A.7.7 | Clear desk and clear screen | Conforming | - | Policy enforced via GPO |
| A.7.8 | Equipment siting and protection | Conforming | - | Data center standards |
| A.7.9 | Security of assets off-premises | Conforming | - | Encryption, MDM |
| A.7.10 | Storage media | Conforming | - | Encrypted, disposal tracked |
| A.7.11 | Supporting utilities | Conforming | - | UPS, generator |
| A.7.12 | Cabling security | Conforming | - | Structured cabling |
| A.7.13 | Equipment maintenance | Conforming | - | Maintenance tracked |
| A.7.14 | Secure disposal or re-use of equipment | Conforming | - | NIST 800-88 |

### A.8 - Technological Controls

| Control | Title | Status | Gap | Remediation |
|---------|-------|--------|-----|-------------|
| A.8.1 | User endpoint devices | Conforming | - | MDM, encryption, EDR |
| A.8.2 | Privileged access rights | Conforming | - | PIM, separate accounts |
| A.8.3 | Information access restriction | Conforming | - | RBAC enforced |
| A.8.4 | Access to source code | N/A | - | No in-house development |
| A.8.5 | Secure authentication | Conforming | - | MFA everywhere |
| A.8.6 | Capacity management | Conforming | - | Monitored via NinjaOne |
| A.8.7 | Protection against malware | Conforming | - | EDR on all endpoints |
| A.8.8 | Management of technical vulnerabilities | Conforming | - | Qualys, patching SLAs |
| A.8.9 | Configuration management | Partially | Baselines not fully enforced | Automate baseline compliance |
| A.8.10 | Information deletion | Conforming | - | Retention + disposal |
| A.8.11 | Data masking | N/A | - | No dev/test environments |
| A.8.12 | Data leakage prevention | Conforming | - | DLP on email/USB |
| A.8.13 | Information backup | Conforming | - | Daily, geo-redundant |
| A.8.14 | Redundancy of information processing facilities | Partially | Single site | Evaluate cloud DR |
| A.8.15 | Logging | Conforming | - | Splunk, 1-year retention |
| A.8.16 | Monitoring activities | Partially | Basic alerting | Tune SIEM correlation rules |
| A.8.17 | Clock synchronization | Conforming | - | NTP configured |
| A.8.18 | Use of privileged utility programs | Conforming | - | Restricted to admins |
| A.8.19 | Installation of software on operational systems | Conforming | - | Admin rights restricted |
| A.8.20 | Networks security | Conforming | - | Firewall, segmentation |
| A.8.21 | Security of network services | Conforming | - | SLA with ISP |
| A.8.22 | Segregation of networks | Conforming | - | VLANs, zones |
| A.8.23 | Web filtering | Conforming | - | Content filter deployed |
| A.8.24 | Use of cryptography | Conforming | - | AES-256, TLS 1.2+ |
| A.8.25 | Secure development lifecycle | N/A | - | No in-house development |
| A.8.26 | Application security requirements | N/A | - | No in-house development |
| A.8.27 | Secure system architecture and engineering | Conforming | - | Hardened configurations |
| A.8.28 | Secure coding | N/A | - | No in-house development |
| A.8.29 | Security testing in development and acceptance | N/A | - | No in-house development |
| A.8.30 | Outsourced development | N/A | - | No outsourced development |
| A.8.31 | Separation of development, test, production | N/A | - | No development environments |
| A.8.32 | Change management | Conforming | - | Change management process |
| A.8.33 | Test information | N/A | - | No test environments |
| A.8.34 | Protection of information systems during audit testing | Conforming | - | Audit controls in place |

---

## Summary

| Section | Total | Conforming | Partial | Non-Conforming | N/A |
|---------|-------|-----------|---------|----------------|-----|
| A.5 Organizational | 37 | 26 | 8 | 3 | 0 |
| A.6 People | 8 | 8 | 0 | 0 | 0 |
| A.7 Physical | 14 | 13 | 1 | 0 | 0 |
| A.8 Technological | 34 | 23 | 3 | 0 | 8 |
| **Total** | **93** | **70** | **12** | **3** | **8** |

**Applicable Controls: 85 | Conformance Rate: 82% (70/85)**

---

## Top 5 Remediation Priorities

1. **A.5.8** - Add security review requirement to project management
2. **A.5.21** - Develop ICT supply chain risk assessment process
3. **A.5.35** - Plan independent security review (external or internal audit)
4. **A.8.9** - Automate configuration baseline compliance checking
5. **A.5.23** - Draft and approve cloud security policy
