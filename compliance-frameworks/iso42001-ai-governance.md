# ISO/IEC 42001:2023 AI Governance Assessment

**Standard:** ISO/IEC 42001:2023 — Artificial Intelligence Management System (AIMS)

**Purpose:** Assess organizational readiness for responsible AI governance, identify risks from AI systems, and establish controls for AI use in a regulated environment (K-12 / HIPAA / FERPA)

**Assessment Date:** 2026-03-22

**Assessor:** Brian Santiago

---

## Why AI Governance Matters for GRC

AI tools are entering regulated environments faster than policies can keep up. In K-12 and healthcare, AI systems handle student data, assist with clinical decisions, generate content, and automate workflows. Without governance:

- **FERPA risk:** AI tools that process student records may expose data to third parties without proper agreements
- **HIPAA risk:** AI assistants processing ePHI may train on or store data outside BAA scope
- **Bias risk:** AI-driven decisions about students or employees may produce discriminatory outcomes with no audit trail
- **Shadow AI risk:** Staff adopt AI tools without IT or compliance review

ISO 42001 provides the framework to manage these risks systematically.

---

## Scope

AI systems and AI-assisted tools used within the organization:

| AI System Category | Examples | Data Sensitivity |
|-------------------|---------|-----------------|
| Generative AI assistants | ChatGPT, Copilot, Claude | May process student/employee data |
| Learning management AI | Adaptive learning platforms, AI tutoring | Student PII, learning records |
| Administrative AI | Document generation, email drafting, scheduling | Employee PII, operational data |
| IT operations AI | Threat detection, anomaly detection, log analysis | Security events, system data |
| Accessibility AI | Speech-to-text, translation, alt text generation | Student accommodations data |

---

## Clause 4: Context of the Organization

### 4.1 Understanding the Organization and Its Context

| Factor | Assessment | Notes |
|--------|-----------|-------|
| Regulatory environment | High complexity | HIPAA, FERPA, state student privacy laws, upcoming AI regulations |
| Stakeholder expectations | High sensitivity | Parents, school board, OCR, and HHS expect responsible AI use |
| AI maturity | Early adoption | Some AI tools in use, no formal governance program |
| Risk appetite for AI | Conservative | Regulated data requires strict controls on AI processing |

### 4.2 Interested Parties

| Stakeholder | AI-Related Concerns |
|------------|-------------------|
| Students and parents | Data privacy, fairness in AI-driven decisions, transparency |
| Staff | Job impact, appropriate use guidance, training |
| School board | Liability, policy compliance, public trust |
| OCR / HHS | FERPA and HIPAA compliance when AI processes regulated data |
| State education department | Student data privacy law compliance |
| AI vendors | Data usage terms, model training policies |

### 4.3 Scope of the AI Management System

The AIMS applies to all AI systems that:
- Process, store, or have access to student education records (FERPA)
- Process, store, or have access to protected health information (HIPAA)
- Make or assist with decisions affecting students or employees
- Are used by staff in the course of their professional duties

---

## Clause 5: Leadership

### 5.1 AI Governance Structure

| Role | Responsibility | Current Status |
|------|---------------|---------------|
| AI Governance Lead | Owns AI policy, coordinates risk assessments | Not assigned — recommend IT Security lead |
| Data Protection Officer | Ensures AI use complies with HIPAA/FERPA | Existing role covers this |
| AI Risk Reviewer | Evaluates new AI tools before deployment | Not established |
| Department Heads | Approve AI use within their teams | Informal process only |

**Gap:** No formal AI governance committee or designated AI governance lead.

### 5.2 AI Policy

**Status:** Not yet created. Draft framework below.

**Proposed AI Responsible Use Policy — Key Elements:**

1. **Approved AI tools list** — Only AI tools that have been vetted by IT Security and Compliance may be used with organizational data
2. **Data classification for AI** — No Restricted or Confidential data (ePHI, student records, HR records) may be entered into AI tools unless the tool has a BAA/DPA and is on the approved list
3. **Human oversight requirement** — AI-generated outputs that affect students, employees, or compliance decisions must be reviewed by a qualified human before action
4. **Transparency** — Staff must disclose when AI tools are used to generate content for official communications, reports, or decisions
5. **Prohibited uses** — AI may not be used for: student discipline decisions, employment decisions, medical diagnoses, or grading without human review
6. **Vendor assessment** — AI vendors must complete the standard vendor risk assessment plus AI-specific addendum (see Section 8 below)
7. **Incident reporting** — AI-related incidents (bias, data exposure, hallucination causing harm) must be reported through the standard IR process

---

## Clause 6: Planning

### 6.1 AI Risk Assessment

| Risk ID | AI Risk | Likelihood | Impact | Risk Level | Mitigation |
|---------|---------|-----------|--------|------------|-----------|
| AI-001 | Staff enter ePHI into unapproved AI tools | High | High | Critical | Approved tools list, DLP on AI domains, training |
| AI-002 | AI vendor trains models on organizational data | Medium | High | High | Contractual restrictions, BAA/DPA review, data processing addendum |
| AI-003 | AI-generated content contains inaccurate information used in official capacity | High | Medium | High | Human review requirement, disclosure policy |
| AI-004 | AI tool produces biased recommendations affecting students | Medium | High | High | Bias testing before deployment, human oversight |
| AI-005 | Shadow AI adoption without security review | High | Medium | High | Approved tools list, network monitoring, user training |
| AI-006 | AI chatbot exposes student data through prompt injection | Medium | High | High | Input validation, output filtering, approved tools only |
| AI-007 | Over-reliance on AI reduces staff critical thinking for compliance decisions | Medium | Medium | Medium | Training on AI limitations, human-in-the-loop policy |
| AI-008 | AI-generated IEP or accommodation content is inappropriate | Low | High | Medium | Prohibited use policy, human review required |
| AI-009 | AI tool vendor suffers data breach exposing org data | Low | High | Medium | Vendor risk assessment, incident response plan |
| AI-010 | Regulatory change restricts current AI usage | Medium | Medium | Medium | Monitor AI legislation, maintain flexibility in vendor contracts |

### 6.2 AI Risk Treatment Plan

| Risk | Treatment | Owner | Target Date |
|------|-----------|-------|-------------|
| AI-001 | Deploy approved AI tools list, configure web filtering for unapproved AI sites, conduct training | IT Security | Q2 2026 |
| AI-002 | Add AI data processing addendum to vendor contracts, review existing AI vendor terms | Compliance | Q2 2026 |
| AI-003 | Publish AI responsible use policy with human review requirements | Compliance | Q2 2026 |
| AI-004 | Require bias impact assessment for AI tools that make recommendations about students | Compliance | Q3 2026 |
| AI-005 | Add AI tool discovery to quarterly access reviews, monitor for unapproved AI domains | IT Security | Q2 2026 |

---

## Clause 7: Support

### 7.1 AI Competence and Training

| Training Topic | Audience | Status | Priority |
|---------------|---------|--------|----------|
| AI responsible use policy | All staff | Not started | High |
| Data classification for AI inputs | All staff | Not started | High |
| AI tool security review process | IT team | Not started | High |
| AI bias awareness | Administrators, counselors | Not started | Medium |
| Prompt engineering basics | Staff using approved AI tools | Not started | Low |

### 7.2 AI-Specific Documentation Needed

| Document | Purpose | Status |
|----------|---------|--------|
| AI Responsible Use Policy | Define acceptable AI use | Draft framework above |
| Approved AI Tools Register | Track vetted AI systems | Not started |
| AI Vendor Assessment Addendum | AI-specific vendor risk questions | See Section 8 |
| AI Incident Response Procedures | Handle AI-specific incidents | Not started |
| AI Impact Assessment Template | Evaluate new AI deployments | Not started |

---

## Clause 8: Operation

### 8.1 AI Vendor Risk Assessment Addendum

These questions supplement the standard vendor risk assessment questionnaire for vendors providing AI-powered services:

| # | Question | Risk Area |
|---|---------|-----------|
| 1 | Does the AI system process, store, or have access to student records or ePHI? | Data privacy |
| 2 | Does the vendor use customer data to train or improve AI models? If yes, can this be disabled? | Data usage |
| 3 | Where is customer data processed? Is it sent to third-party AI providers (OpenAI, Google, etc.)? | Data residency |
| 4 | Does the vendor have a BAA/DPA that explicitly covers AI processing? | Compliance |
| 5 | What safeguards prevent prompt injection or data extraction attacks? | Security |
| 6 | Does the AI system make or recommend decisions about individuals? If yes, how is bias tested? | Fairness |
| 7 | Can the organization export or delete all data provided to the AI system? | Data rights |
| 8 | What is the vendor's incident response process for AI-specific incidents (hallucination, bias, data leak)? | Incident response |
| 9 | Does the vendor provide transparency into how the AI model generates outputs? | Explainability |
| 10 | What happens to data in the AI system if the contract is terminated? | Data retention |

### 8.2 AI System Lifecycle Controls

| Phase | Control | ISO 42001 Ref |
|-------|---------|--------------|
| Procurement | AI vendor risk assessment with addendum | Clause 8.2 |
| Deployment | AI impact assessment, approved tools register update | Clause 8.3 |
| Operation | Monitoring, human oversight, incident reporting | Clause 8.4 |
| Review | Annual AI system inventory review, bias audit | Clause 9 |
| Retirement | Data deletion verification, contract termination checklist | Clause 8.5 |

---

## Clause 9: Performance Evaluation

### 9.1 Proposed AI Governance KPIs

| KPI | Target | Measurement Frequency |
|-----|--------|---------------------|
| % of AI tools on approved list | 100% | Quarterly |
| AI responsible use training completion | > 95% | Annual |
| AI vendor assessments completed (with AI addendum) | 100% of AI vendors | Annual |
| AI-related incidents reported | Track trend | Monthly |
| Time to review new AI tool requests | < 10 business days | Per request |
| Shadow AI detection rate | Track discovery count | Quarterly |

---

## Clause 10: Improvement

### 10.1 AI Governance Maturity Roadmap

| Phase | Timeline | Activities | Maturity Level |
|-------|----------|-----------|---------------|
| **Phase 1: Foundation** | Q2 2026 | AI policy, approved tools list, staff training, vendor addendum | Initial |
| **Phase 2: Operationalize** | Q3-Q4 2026 | AI impact assessments, shadow AI monitoring, bias testing framework | Developing |
| **Phase 3: Measure** | Q1 2027 | KPI tracking, AI incident response procedures, governance committee | Defined |
| **Phase 4: Optimize** | Q2-Q4 2027 | Automated AI compliance checks, continuous monitoring, maturity review | Managed |

---

## Assessment Summary

| ISO 42001 Clause | Status | Key Gap |
|------------------|--------|---------|
| 4 - Context | Partial | AI-specific context documented; formal scope statement needed |
| 5 - Leadership | Not Ready | No AI governance lead or committee assigned |
| 6 - Planning | Partial | AI risk assessment completed; treatment plan needs execution |
| 7 - Support | Not Ready | AI training program not yet developed |
| 8 - Operation | Partial | Vendor addendum drafted; lifecycle controls need implementation |
| 9 - Performance | Not Ready | KPIs defined but not yet measured |
| 10 - Improvement | Partial | Roadmap created; execution begins Q2 2026 |

**Overall AI Governance Readiness: Early Stage — Foundation in place, execution needed**

---

## Mapping to Existing GRC Program

ISO 42001 does not replace existing frameworks — it layers AI-specific governance on top of them:

| Existing Artifact | AI Governance Extension |
|------------------|----------------------|
| Risk register | Add AI risks (AI-001 through AI-010 above) |
| Vendor risk assessment | Add AI addendum questions |
| Access control policy | Add AI tool access requirements |
| Data classification policy | Add guidance for AI data inputs |
| Incident response plan | Add AI-specific incident types |
| Security awareness training | Add AI responsible use module |
| Control mapping matrix | Add ISO 42001 references where applicable |

---

## References

- ISO/IEC 42001:2023 — Artificial Intelligence Management System
- NIST AI Risk Management Framework (AI RMF 1.0)
- UNESCO Recommendation on the Ethics of Artificial Intelligence
- Executive Order 14110 — Safe, Secure, and Trustworthy AI (2023)
- FERPA and AI: Student Privacy Policy Office Guidance
