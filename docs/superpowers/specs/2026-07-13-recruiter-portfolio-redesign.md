# Recruiter Portfolio Redesign

## Objective

Turn Brian Santiago's portfolio into a recruiter-first decision surface where a visitor can understand his strongest fit, inspect role-relevant proof, open the correct resume, and contact him without hunting through the page.

## Positioning

- Lead with IT Support because it has the strongest professional evidence.
- Present SOC and GRC as one-click specialist paths backed by hands-on labs and documented portfolio work.
- Clearly distinguish professional experience, hands-on lab work, and synthetic practice artifacts.
- Use direct recruiting language and searchable role/tool keywords without overstating production security experience.

## First-Screen Experience

The first viewport must answer five questions:

1. Who is Brian?
2. What role is he strongest for?
3. What tools and outcomes support that claim?
4. Where is the proof?
5. How can a recruiter contact him or open the correct resume?

The hero will contain:

- Name, location, remote preference, and availability.
- A direct IT Support headline and concise support-to-security positioning.
- IT Support, SOC, and GRC role controls visible without scrolling.
- Primary actions for role proof, role resume, and contact.
- A compact proof strip using defensible professional metrics.
- A role-specific evidence panel instead of the decorative route dashboard and simulated event log.

## Information Architecture

The page will use this order:

1. Overview and role selector
2. Recruiter snapshot
3. Professional experience
4. Featured proof projects
5. Tools and skills
6. Certifications and education
7. Role-specific resumes
8. Contact

A compact sticky header will expose Overview, Experience, Projects, Skills, Credentials, Resumes, and Contact. On mobile, navigation will remain compact and the role selector will stay near the top rather than appearing after an oversized hero.

## Role Paths

The role selector changes the following content without sending the visitor to another page:

- Headline and role summary
- Primary tools
- Recruiter talking points
- Featured project order
- Resume link and label
- Relevance badges on project cards

### IT Support

Lead with Microsoft 365, Active Directory, Entra ID, ServiceNow, NinjaOne, endpoint support, ticket ownership, SLA discipline, user communication, and identity administration.

### SOC

Lead with Microsoft Sentinel, KQL, Windows event IDs, Microsoft Defender, alert triage, incident documentation, escalation, and MITRE ATT&CK mapping. Label this evidence as lab and portfolio work where appropriate.

### GRC

Lead with access reviews, control evidence, risk registers, policies, third-party risk, HIPAA, SOX, NIST, ISO 27001 concepts, audit trails, remediation ownership, and documented exceptions. Label synthetic exercises explicitly.

## Experience Presentation

Professional experience will appear before projects and will communicate:

- Role and employer context
- Scale of support
- Tools used
- Responsibilities and outcomes
- Transferable operational discipline

The driving background will remain concise supporting context rather than the site's visual or verbal theme.

## Project Presentation

Each project card will show:

- Project name and evidence type
- Problem
- Action
- Tools
- Result
- Scope boundary
- Direct GitHub proof link

The six current repositories remain in scope:

- Microsoft Entra ID Security Review
- Microsoft Sentinel Authentication Casebook
- Windows Defender Endpoint Review
- Access Review and Audit Evidence Pack
- IAM Joiner-Mover-Leaver Workflow Pack
- GRC Documentation Portfolio

Project descriptions must match the repository READMEs and must not invent retained telemetry, production ownership, malware findings, audit authority, or deployed controls.

## Visual Direction

- Quiet, high-contrast professional interface suitable for repeated recruiter scanning.
- White and near-black surfaces with teal as the primary action color and amber reserved for proof/status accents.
- Minimal route-line motif retained only as subtle brand texture.
- No simulated dashboards, fake event feeds, decorative metric panels, or oversized mobile hero.
- Cards used only for individual projects, credentials, and genuinely grouped proof.
- Clear type hierarchy with compact headings inside panels.

## Interaction And Accessibility

- Role controls use buttons with accurate `aria-pressed` state.
- Project visibility and resume destination update together.
- Keyboard focus states remain visible.
- Reduced-motion preferences disable nonessential animation.
- The certification section will not auto-scroll by default.
- Internal links use scroll offsets that keep headings visible.
- All interactive controls have unique accessible names.

## Responsive Requirements

- No horizontal overflow at 390 CSS pixels.
- Role selector and primary action must be reachable in the first mobile viewport or immediately below a compact hero.
- Desktop first viewport must show identity, role choice, proof, and a next action.
- Text, buttons, metrics, and navigation must not overlap at desktop or mobile breakpoints.

## Verification

Before publication:

- Validate HTML structure and local asset paths.
- Verify every GitHub, LinkedIn, email, privacy, and resume link.
- Check desktop and 390x844 mobile rendering.
- Confirm no browser console errors or warning-level application failures.
- Exercise all role controls and verify content, project ordering, and resume changes.
- Confirm keyboard-accessible navigation and visible focus.
- Confirm production GitHub Pages returns HTTP 200 for the page, image, privacy page, and all three resumes.
- Open the production page in the user's browser after deployment.

## Success Criteria

A recruiter can identify Brian's strongest lane, choose IT Support, SOC, or GRC, understand the evidence level, inspect a relevant project, open the correct resume, and find contact information in under 30 seconds on desktop or mobile.
