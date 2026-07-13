# Recruiter Portfolio Redesign Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build and publish a recruiter-first portfolio where visitors can identify Brian's strongest role, inspect relevant evidence, open the correct resume, and contact him within 30 seconds.

**Architecture:** Keep the site dependency-free and compatible with GitHub Pages. Split the current monolithic page into semantic HTML, a dedicated stylesheet, a small role-state controller, and a standard-library Python verifier so structure, copy boundaries, links, and role behavior are independently testable.

**Tech Stack:** HTML5, CSS3, vanilla JavaScript, Python 3 standard library, GitHub Pages.

## Global Constraints

- IT Support is the primary professional lane; SOC and GRC are one-click specialist paths.
- Professional experience, hands-on lab work, and synthetic portfolio artifacts must be labeled accurately.
- Do not claim retained telemetry, production SOC ownership, malware containment, live audit authority, or deployed controls when the repositories do not support those claims.
- No external frontend dependencies, build system, tracking script, or form submission service.
- No horizontal overflow at 390 CSS pixels.
- Certification content must be static by default; no auto-scrolling marquee.
- Preserve the existing PDFs, privacy page, hero visual, and Git history.

---

### Task 1: Add A Portfolio Contract Verifier

**Files:**
- Create: `tests/verify_portfolio.py`
- Inspect: `docs/index.html`

**Interfaces:**
- Consumes: `docs/index.html`, `docs/assets/site.css`, `docs/assets/site.js`, resume PDFs, hero image, privacy page.
- Produces: a command-line verifier that exits `0` with `PORTFOLIO_VERIFY_OK` or exits nonzero with explicit failed assertions.

- [ ] **Step 1: Write the failing verifier**

Create a Python script using `html.parser.HTMLParser`, `pathlib.Path`, and `urllib.parse.urlparse`. Track start tags, IDs, headings, links, buttons, project article attributes, and visible text. Assert:

```python
required_ids = {
    "overview", "snapshot", "experience", "projects", "skills",
    "credentials", "resumes", "contact", "role-title", "role-summary",
    "role-resume", "role-tools", "role-proof"
}
required_role_values = {"it", "soc", "grc"}
required_repo_urls = {
    "https://github.com/BrianSantiago-GRC/entra-identity-security-review",
    "https://github.com/BrianSantiago-GRC/Microsoft-Sentinel-SIEM",
    "https://github.com/BrianSantiago-GRC/microsoft-defender-endpoint-investigation",
    "https://github.com/BrianSantiago-GRC/grc-access-review-audit-evidence-pack",
    "https://github.com/BrianSantiago-GRC/iam-jml-access-workflow-pack",
    "https://github.com/BrianSantiago-GRC/grc-portfolio",
}
required_resumes = {
    "assets/resumes/Brian_Santiago_IT.pdf",
    "assets/resumes/Brian_Santiago_SOC.pdf",
    "assets/resumes/Brian_Santiago_GRC.pdf",
}
forbidden_copy = {
    "contained endpoint alert",
    "8 KQL detection rules",
    "false-positive reduction around 35%",
    "route plan",
    "event log",
}
```

Also assert one `h1`, at least three role buttons, six project articles, local asset existence, external-link HTTPS, nonempty accessible names, and the presence of `site.css` and `site.js` references.

- [ ] **Step 2: Run the verifier and confirm the old page fails**

Run:

```powershell
& 'C:\Users\brian\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' .\tests\verify_portfolio.py
```

Expected: nonzero exit with missing `docs/assets/site.css`, missing `docs/assets/site.js`, missing section IDs, and forbidden-copy failures.

- [ ] **Step 3: Commit the test contract**

```powershell
git add tests/verify_portfolio.py
git commit -m "Add recruiter portfolio contract verifier"
```

---

### Task 2: Rebuild The Semantic Recruiter Experience

**Files:**
- Modify: `docs/index.html`
- Preserve: `docs/assets/resumes/*.pdf`
- Preserve: `docs/privacy/index.html`
- Preserve: `docs/recruiter_portfolio_hero_visual.png`

**Interfaces:**
- Consumes: the role values `it`, `soc`, and `grc`; repository-backed project copy; professional resume evidence.
- Produces: stable section IDs and data attributes consumed by `site.js` and verified by `verify_portfolio.py`.

- [ ] **Step 1: Replace the monolithic document shell**

Use one `h1`, semantic landmarks, external CSS/JS, canonical metadata, Open Graph metadata, and Person JSON-LD. The navigation contract is:

```html
<nav aria-label="Primary navigation">
  <a href="#overview">Overview</a>
  <a href="#experience">Experience</a>
  <a href="#projects">Projects</a>
  <a href="#skills">Skills</a>
  <a href="#credentials">Credentials</a>
  <a href="#resumes">Resumes</a>
  <a href="#contact">Contact</a>
</nav>
```

- [ ] **Step 2: Build the first-screen role router**

Place the role controls before the primary hero copy:

```html
<div class="role-switcher" aria-label="Choose a recruiter view">
  <button type="button" data-role="it" aria-pressed="true">IT Support</button>
  <button type="button" data-role="soc" aria-pressed="false">SOC</button>
  <button type="button" data-role="grc" aria-pressed="false">GRC</button>
</div>
```

Expose `#role-title`, `#role-summary`, `#role-tools`, `#role-proof`, and `#role-resume`. The default IT copy must identify 3+ years of Tier 1-3 support, regulated healthcare and education environments, Microsoft 365, Active Directory/Entra ID, endpoint management, ITSM, and documentation.

- [ ] **Step 3: Add a recruiter snapshot and professional experience**

The snapshot must expose Ocala, Florida; remote-first preference; earned certifications; 400+ monthly tickets; 99% SLA; 500+ users; and 200+ endpoints. Add three chronological experience entries:

```text
IT Support Specialist | Ina A. Colen Academy | Jul 2025 - Jun 2026
Tier 3 IT Support Specialist | Sanitas Medical Center | Jan 2025 - May 2025
Help Desk Technician | KM New Living Society | May 2023 - Aug 2024
```

Each entry must show scope, tools, and two or three defensible outcomes. Do not repeat the full resume.

- [ ] **Step 4: Add six evidence-rich project cards**

Each `.project-card` must include `data-project`, `data-roles`, and `data-rank-it`, `data-rank-soc`, `data-rank-grc`. Each card must render labels for `Problem`, `Action`, `Tools`, `Result`, and `Scope` plus a direct GitHub link. Use repository-backed facts:

```text
Entra review: sanitized tenant review; evidence collection and recommendations; no claim every policy was deployed.
Sentinel casebook: Event IDs 4625/4624, five reusable KQL query files, validation suite; raw telemetry/screenshots not retained.
Defender review: Windows Security, Get-MpComputerStatus, Event Viewer, timeline and checklist; no active threat was found.
Access review: 15 synthetic records; 10 Keep, 2 Modify, 3 Remove; synthetic exercise.
IAM JML: sample request-to-removal workflow, approval matrix, offboarding checklist; sample process design.
GRC portfolio: synthetic policy, risk, control, audit, vendor, and incident artifacts; no audit opinion or employer program.
```

- [ ] **Step 5: Add skills, credentials, resumes, and contact**

Use role-tagged skill groups, static credential rows, three labeled resume links, email, LinkedIn, GitHub, and a copy-email button. Earned credentials are CompTIA A+, Network+, Security+, Google Cybersecurity Certificate, ISO 27001 Lead Auditor, GRC Mastery, and MediClear HIPAA Compliance. Label CySA+ as `In progress - target Q4 2026`.

- [ ] **Step 6: Run the verifier**

Expected at this stage: failures only for missing CSS/JS or behavior-specific tokens; all semantic HTML, copy, links, and asset checks pass.

- [ ] **Step 7: Commit semantic markup**

```powershell
git add docs/index.html
git commit -m "Rebuild portfolio around recruiter role paths"
```

---

### Task 3: Build The Responsive Visual System

**Files:**
- Create: `docs/assets/site.css`

**Interfaces:**
- Consumes: classes and IDs from `docs/index.html`.
- Produces: desktop and mobile layouts with no overflow and visible focus states.

- [ ] **Step 1: Define the palette and layout primitives**

Use CSS custom properties:

```css
:root {
  --ink: #0d1619;
  --muted: #53636a;
  --paper: #f7f9f8;
  --surface: #ffffff;
  --line: #d7e0df;
  --teal: #087f78;
  --teal-dark: #075e5a;
  --amber: #b66b09;
  --focus: #006ee6;
  --max: 1180px;
}
```

Use an unframed full-width hero, restrained section bands, project cards with at most `8px` radius, and no decorative nested cards.

- [ ] **Step 2: Implement desktop hierarchy**

At `min-width: 900px`, the first viewport must show the role switcher, title, summary, three actions, proof strip, and role evidence panel. Use a two-column hero with a `minmax(0, 1.3fr) minmax(320px, 0.7fr)` grid and cap hero vertical padding so the next section remains visible.

- [ ] **Step 3: Implement mobile hierarchy**

At `max-width: 720px`, use one column, a compact two-row navigation, three equal role buttons, stacked actions, two-column proof metrics, and a hidden decorative hero image. Keep the hero below `760px` tall at 390x844 and prevent horizontal overflow with `min-width: 0`, wrapping, and responsive grids.

- [ ] **Step 4: Add interaction and accessibility states**

Add `:focus-visible`, hover, pressed, filtered, and reduced-motion styles. Use `[hidden] { display: none !important; }`. Disable all nonessential transitions under `prefers-reduced-motion: reduce`.

- [ ] **Step 5: Run the verifier and inspect CSS statically**

Run the verifier and `git diff --check`. Expected: verifier still fails only if JavaScript behavior is absent; whitespace check passes.

- [ ] **Step 6: Commit the visual system**

```powershell
git add docs/assets/site.css
git commit -m "Add responsive recruiter portfolio visual system"
```

---

### Task 4: Implement Role-Specific Behavior

**Files:**
- Create: `docs/assets/site.js`

**Interfaces:**
- Consumes: role buttons with `data-role`, role content IDs, project ranking attributes, role-tagged skill groups, and resume paths.
- Produces: `applyRole(role: "it" | "soc" | "grc"): void` and `copyEmail(): Promise<void>`.

- [ ] **Step 1: Define truthful role data**

```javascript
const roleData = {
  it: {
    label: "IT Support Specialist",
    resume: "assets/resumes/Brian_Santiago_IT.pdf",
    tools: ["Microsoft 365", "Active Directory", "Entra ID", "ServiceNow", "NinjaOne", "Windows 10/11"],
    proof: "3+ years of Tier 1-3 support across education and regulated healthcare."
  },
  soc: {
    label: "SOC Analyst - Support-to-Security Path",
    resume: "assets/resumes/Brian_Santiago_SOC.pdf",
    tools: ["Microsoft Sentinel", "KQL", "Defender", "Event Viewer", "Splunk", "MITRE ATT&CK"],
    proof: "Professional endpoint and identity investigation plus documented SOC lab evidence."
  },
  grc: {
    label: "GRC Analyst - Audit and Evidence Path",
    resume: "assets/resumes/Brian_Santiago_GRC.pdf",
    tools: ["NIST CSF", "ISO 27001", "HIPAA", "SOX ITGC", "Access Reviews", "TPRM"],
    proof: "Professional compliance-support evidence plus clearly labeled synthetic GRC artifacts."
  }
};
```

- [ ] **Step 2: Implement one role state transition**

`applyRole` must validate the role, update `aria-pressed`, replace the role title/summary/tools/proof/resume, update `document.title`, set `?role=<role>` with `history.replaceState`, sort project cards by the matching rank attribute, and hide role-irrelevant skill groups without hiding cross-role evidence.

- [ ] **Step 3: Initialize from the URL and bind controls**

Read `new URLSearchParams(location.search).get("role")`; use `it` for invalid or absent values. Bind each role button once. Support browser history with a `popstate` listener.

- [ ] **Step 4: Implement copy-email feedback**

Use `navigator.clipboard.writeText` when available and a selectable-text fallback when it is not. Update `#copy-status` to `Email copied` or `Select the email address above`.

- [ ] **Step 5: Run the complete verifier**

Expected output:

```text
PORTFOLIO_VERIFY_OK
```

- [ ] **Step 6: Commit behavior**

```powershell
git add docs/assets/site.js
git commit -m "Add recruiter role routing and portfolio interactions"
```

---

### Task 5: Render, Exercise, Publish, And Verify

**Files:**
- Modify only if QA finds defects: `docs/index.html`, `docs/assets/site.css`, `docs/assets/site.js`, `tests/verify_portfolio.py`

**Interfaces:**
- Consumes: completed static site and verifier.
- Produces: a pushed GitHub commit and verified production URL.

- [ ] **Step 1: Start the local site**

Run the repository's available Python runtime with `python -m http.server 8778 --directory docs --bind 127.0.0.1`. Verify `http://127.0.0.1:8778/` returns HTTP 200.

- [ ] **Step 2: Run desktop browser QA**

Flow: page loads -> IT Support view is active -> click SOC -> SOC headline, tools, project order, and SOC resume appear -> click GRC -> corresponding GRC state appears -> click IT Support -> default state returns.

Check page identity, nonblank DOM, no framework overlay, console warnings/errors, screenshot evidence, visible next section, all navigation targets, and copy-email feedback.

- [ ] **Step 3: Run 390x844 mobile QA**

Set the browser viewport to `390x844`. Verify no horizontal overflow, role selector visibility, hero height below `760px`, readable actions, nonoverlapping proof metrics, mobile navigation, project cards, and role-state interactions. Reset the viewport afterward.

- [ ] **Step 4: Verify links and assets**

Use HTTP GET requests for the page, privacy page, hero image, three PDFs, six GitHub repositories, LinkedIn profile, and mailto syntax. Expected: HTTP 200 for public HTTPS resources and correct PDF/image content types.

- [ ] **Step 5: Fix any QA defects and rerun all checks**

Run:

```powershell
& 'C:\Users\brian\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' .\tests\verify_portfolio.py
git diff --check
```

Expected: `PORTFOLIO_VERIFY_OK`, no diff-check output, no relevant browser console warnings/errors, and passing desktop/mobile screenshots.

- [ ] **Step 6: Commit and push**

```powershell
git add docs/index.html docs/assets/site.css docs/assets/site.js tests/verify_portfolio.py
git commit -m "Revamp portfolio for recruiter-first role discovery"
git push origin HEAD:main
```

- [ ] **Step 7: Verify GitHub Pages production**

Poll `https://briansantiago-grc.github.io/BrianSantiago-GRC/` until it serves the pushed commit's site. Repeat desktop/mobile browser QA and HTTP asset checks against production.

- [ ] **Step 8: Leave production open**

Open the canonical production URL in the user's visible browser and retain it as the deliverable tab.
