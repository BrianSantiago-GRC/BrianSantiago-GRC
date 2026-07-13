# Signal Path Cinematic Portfolio Enhancement

## Objective

Add cinematic visual storytelling to Brian Santiago's recruiter portfolio while preserving its proof-first structure, fast role selection, honest evidence boundaries, and static GitHub Pages deployment. The result should earn attention in the first few seconds, sustain curiosity through the project section, and remain easy for a recruiter to scan.

## Approved Direction

The approved direction is **Signal Path**. It uses controlled motion, a live-feeling route motif, role-specific transitions, and authentic artifact previews. It must feel polished and technically confident without becoming a splash page, game interface, or simulated security dashboard.

The existing IT Support default and one-click SOC and GRC recruiter paths remain unchanged in purpose. Motion supports those paths instead of competing with them.

## Experience Sequence

### Initial Reveal

The page must be readable immediately. There is no blocking loader or intro screen.

During the first 1.2 seconds:

1. The background visual settles into place with a short opacity and scale transition.
2. The identity line, role selector, headline, summary, actions, proof strip, and role panel appear in a restrained stagger.
3. A signal line sweeps once through the hero and then becomes a quiet ambient element.
4. The first below-hero content remains partially visible on standard desktop and mobile viewports.

The reveal runs once per page load. It does not replay on ordinary scrolling.

### Role Changes

Selecting IT Support, SOC, or GRC must remain immediate. The active role state changes first, followed by a short crossfade of the role-specific headline, summary, tools, proof statement, project order, and resume state.

Each role receives a restrained accent treatment:

- IT Support: teal signal accent.
- SOC: coral alert accent paired with teal.
- GRC: amber evidence accent paired with teal.

The palette remains balanced and does not turn the page into a single-hue theme. Role transitions must not change element dimensions or cause visible layout jumps.

### Scroll Progression

A thin progress line at the top of the viewport shows movement through the page. It is decorative and receives no focus.

Major sections reveal with short opacity and vertical-position transitions when they first enter the viewport. Individual experience rows, project cards, skill groups, credentials, resumes, and contact links may stagger within their section, but animation must remain under 600 milliseconds per item.

The project section is the visual high point. Motion becomes quieter after the project section so the resume and contact actions remain calm and direct.

## Authentic Project Visuals

Each project card will receive a stable visual region above its written evidence. These visuals are lightweight semantic HTML and CSS previews built from the actual project scope and artifact types. They are not screenshots of production systems, live telemetry, or claims of deployed controls.

The six previews are:

1. **Microsoft Entra ID Security Review**: identity nodes, access state, and review checkpoints.
2. **Microsoft Sentinel Authentication Casebook**: an authentication timeline, compact KQL excerpt, and investigation markers.
3. **Windows Defender Endpoint Review**: endpoint posture rows and documented review findings.
4. **Access Review and Audit Evidence Pack**: reviewer, disposition, evidence, and closure fields.
5. **IAM Joiner-Mover-Leaver Workflow Pack**: lifecycle stages and approval handoffs.
6. **GRC Documentation Portfolio**: risk, control, owner, evidence, and status relationships.

Every preview will carry a visible `Artifact preview` label. The preview content must be traceable to the matching repository README or artifact files and must not invent metrics, incidents, malware, audit conclusions, or production ownership.

## Visual System

The existing hero bitmap remains the primary visual asset. It will be reframed with CSS overlays rather than replaced with a generic stock image.

The cinematic layer consists of:

- A subtle background drift using transform only.
- One route-line sweep on initial load.
- Small pulsing evidence nodes with low opacity.
- A restrained scan texture created with CSS, not a large additional image.
- Role-specific accent changes controlled by CSS custom properties.
- Fixed-height artifact preview regions so animations cannot move surrounding content.
- A top scroll progress line updated through a CSS custom property.

No decorative orbs, bokeh blobs, looping video, canvas dependency, WebGL, fake terminal feed, or autoplay audio will be added.

## Architecture

The enhancement remains dependency-free and uses the current files:

- `docs/index.html`: adds semantic decorative layers, reveal hooks, and six artifact preview regions.
- `docs/assets/site.css`: defines the signal motif, role accent variables, reveal states, artifact visuals, responsive behavior, and reduced-motion fallbacks.
- `docs/assets/site.js`: extends the existing role controller with motion initialization, role-transition state, scroll progress, and viewport reveal behavior.
- `tests/verify_portfolio.py`: adds structural checks for artifact labels, preview count, motion hooks, and reduced-motion support.

No build system or third-party animation library is introduced.

## Interaction Flow

On page load:

1. Read and validate the `role` query parameter.
2. Apply role-specific content before initializing visible motion states.
3. Detect `prefers-reduced-motion`.
4. If motion is allowed, attach reveal observers and a requestAnimationFrame-throttled scroll progress handler.
5. If motion is not allowed or an observer is unavailable, render all content in its final visible state.

On role selection:

1. Set the active role and accent variables immediately.
2. Mark the dynamic role content as transitioning.
3. Reuse the existing content, URL, skill, resume, and project-order updates.
4. Remove the transition state after the short crossfade.

The existing clipboard, navigation, resume, GitHub, LinkedIn, email, and project interactions remain independent from the animation layer.

## Accessibility And Failure Behavior

- `prefers-reduced-motion: reduce` removes transforms, sweeps, pulses, stagger delays, and smooth scrolling while keeping every element visible.
- Decorative signal layers use `aria-hidden="true"` and cannot receive focus.
- Artifact previews use meaningful labels and do not communicate required information through color alone.
- Keyboard focus remains visible and role buttons retain accurate `aria-pressed` states.
- If JavaScript fails, the document remains readable, role-default content stays visible, and no element is permanently hidden by an animation class.
- If `IntersectionObserver` is unavailable, all reveal targets are shown immediately.
- Scroll and pointer handlers do not perform layout reads and writes in an unthrottled loop.

## Responsive And Performance Requirements

- No horizontal overflow at 390 CSS pixels.
- At 390x844, the hero must leave a visible hint of the recruiter snapshot below it.
- The role selector, primary proof action, and resume action remain available without an oversized mobile introduction.
- Artifact previews use stable aspect ratios and collapse detail at narrow widths without clipped text.
- Motion uses opacity and transform where possible to avoid layout shift.
- The site adds no external runtime dependency and no autoplay media.
- The existing hero image remains the only large bitmap unless verification proves that a repository-sourced image materially improves the experience.

## Verification

Automated checks will verify:

- Existing role data, project ordering, resume links, and asset paths remain valid.
- Exactly six project artifact previews exist and each is labeled.
- Motion hooks and reduced-motion CSS are present.
- The page includes no external animation library.
- All current portfolio tests pass.

Browser verification will cover:

- Desktop at 1440x900 and mobile at 390x844.
- IT Support, SOC, and GRC query paths and role-button transitions.
- First viewport composition, artifact preview legibility, scroll progress, and section reveal behavior.
- No overlapping text, horizontal overflow, blank visual regions, console errors, or warning-level application failures.
- Reduced-motion behavior renders all content without cinematic movement.
- Resume, project, LinkedIn, email, and internal navigation links remain usable.

Production verification will confirm GitHub Pages returns HTTP 200 for the page and all local assets, then the finished live portfolio will be opened in Brian's browser.

## Success Criteria

The enhancement is successful when:

- The first viewport communicates identity, role choice, proof, and action immediately.
- Motion creates a memorable first impression without delaying recruiter tasks.
- Each featured project has a credible, role-relevant visual derived from real portfolio evidence.
- A recruiter can move from overview to relevant proof, resume, and contact in under 30 seconds.
- Desktop, mobile, reduced-motion, and role-specific paths all remain stable and readable.
