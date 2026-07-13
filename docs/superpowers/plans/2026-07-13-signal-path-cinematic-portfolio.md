# Signal Path Cinematic Portfolio Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Turn the approved Signal Path design into the live recruiter portfolio with visible motion, role-aware cinematics, and six honest artifact previews.

**Architecture:** Keep the existing dependency-free GitHub Pages structure. Extend the contract verifier first, then add semantic preview markup, CSS-only preview visuals and motion states, and small vanilla-JavaScript controllers for reveal, progress, and role transitions.

**Tech Stack:** HTML5, CSS3, vanilla JavaScript, Python standard-library verifier, GitHub Pages.

## Global Constraints

- Preserve IT Support as the default role and keep SOC/GRC one click away.
- Keep every project preview traceable to the matching repository evidence and visibly labeled `Artifact preview`.
- Add no external frontend or animation dependency.
- Keep the first screen immediately readable with no loader, autoplay media, canvas, or WebGL.
- Support `prefers-reduced-motion: reduce` and no horizontal overflow at 390 CSS pixels.
- Preserve existing resume, project, navigation, email, LinkedIn, and GitHub behavior.

---

### Task 1: Extend The Portfolio Contract

**Files:**
- Modify: `tests/verify_portfolio.py`

**Interfaces:**
- Consumes: `docs/index.html`, `docs/assets/site.css`, and `docs/assets/site.js`.
- Produces: assertions for six artifact previews, motion hooks, scroll progress, role-transition hooks, and reduced-motion CSS.

- [ ] Add parser support for `artifact-preview` regions and visible `Artifact preview` labels.
- [ ] Assert exactly six previews, one per project card, plus `#scroll-progress` and `.signal-path` hooks.
- [ ] Assert `IntersectionObserver`, `requestAnimationFrame`, role transition state, and reduced-motion tokens.
- [ ] Run the verifier and confirm it fails because cinematic markup and behavior are absent.
- [ ] Commit the failing contract.

### Task 2: Add Semantic Cinematic And Artifact Markup

**Files:**
- Modify: `docs/index.html`

**Interfaces:**
- Consumes: existing six `.project-card` elements and role-router IDs.
- Produces: `#scroll-progress`, `.signal-path`, reveal hooks, and six labeled `.artifact-preview` regions.

- [ ] Add the decorative progress bar and hero signal-path layers with `aria-hidden="true"`.
- [ ] Add reveal hooks to major sections and repeated items without hiding content when JavaScript fails.
- [ ] Add one fixed-height, labeled artifact preview to each project card using evidence-backed semantic rows, nodes, timelines, or workflow steps.
- [ ] Run the verifier and confirm only CSS/JavaScript behavior assertions still fail.
- [ ] Commit the semantic cinematic markup.

### Task 3: Build The Signal Path Visual System

**Files:**
- Modify: `docs/assets/site.css`

**Interfaces:**
- Consumes: cinematic and artifact classes from `docs/index.html`.
- Produces: initial reveal, route sweep, role accents, artifact preview styling, stable dimensions, responsive layout, and reduced-motion fallbacks.

- [ ] Add balanced role accent variables for IT, SOC, and GRC.
- [ ] Add the one-time signal sweep, low-opacity node pulse, and subtle bitmap drift using opacity and transform only.
- [ ] Style six artifact preview types with fixed aspect ratios and no text clipping.
- [ ] Add reveal, role-transition, hover, and scroll-progress states.
- [ ] Add 390px responsive and reduced-motion rules that leave all content visible.
- [ ] Run the verifier and `git diff --check`.
- [ ] Commit the cinematic visual system.

### Task 4: Implement Motion And Role-State Behavior

**Files:**
- Modify: `docs/assets/site.js`

**Interfaces:**
- Consumes: existing `applyRole(role, options)` behavior and new motion hooks.
- Produces: `initializeCinematics()`, progress updates, reveal observation, and a stable role crossfade.

- [ ] Add a validated role accent update before dynamic copy replacement.
- [ ] Add a short `.is-role-transitioning` state with timer cleanup and no layout mutation.
- [ ] Add requestAnimationFrame-throttled scroll progress.
- [ ] Add IntersectionObserver reveal behavior with a visible fallback.
- [ ] Disable nonessential motion when reduced motion is requested.
- [ ] Run the verifier and confirm `PORTFOLIO_VERIFY_OK`.
- [ ] Commit the cinematic behavior.

### Task 5: Verify, Publish, And Prove Production

**Files:**
- Modify only if QA finds defects: `docs/index.html`, `docs/assets/site.css`, `docs/assets/site.js`, `tests/verify_portfolio.py`.

**Interfaces:**
- Consumes: completed static site.
- Produces: a tested commit on `main` and verified production screenshots.

- [ ] Start the site locally and verify HTTP 200.
- [ ] Run desktop QA at 1440x900 for IT, SOC, and GRC role paths, console health, progress, reveal, and project previews.
- [ ] Run mobile QA at 390x844 for overflow, first-viewport composition, role controls, and preview legibility.
- [ ] Capture desktop and mobile screenshots and inspect them visually.
- [ ] Run `tests/verify_portfolio.py`, `git diff --check`, and repository tests.
- [ ] Commit remaining QA fixes and push `HEAD:main`.
- [ ] Poll GitHub Pages until the new assets are live, repeat production QA, and leave the production URL open.
