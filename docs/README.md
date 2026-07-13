# Brian Santiago Recruiter Portfolio

Updated: 2026-07-13

This folder is the GitHub Pages source for Brian Santiago's recruiter portfolio. The page leads with professional IT Support experience and provides one-click SOC and GRC views backed by accurately labeled professional, hands-on, sample, and synthetic evidence.

## Recruiter Experience

- IT Support is the default professional lane.
- SOC and GRC buttons update the headline, tools, evidence level, project order, and resume.
- Professional experience appears before portfolio projects.
- Every project shows its Problem, Action, Tools, Result, Scope, and direct GitHub proof.
- Desktop and mobile layouts expose role selection and a clear next action without a long introductory scroll.

## Files

- `index.html` - semantic recruiter portfolio structure and content
- `assets/site.css` - responsive visual system
- `assets/site.js` - role routing, project ordering, resume selection, and contact feedback
- `assets/resumes/` - IT Support, SOC, and GRC resume PDFs
- `recruiter_portfolio_hero_visual.png` - local brand visual used behind the desktop hero
- `privacy/index.html` - lightweight privacy page for OAuth and app references
- `.nojekyll` - publishes the folder directly through GitHub Pages
- `../tests/verify_portfolio.py` - portfolio structure, copy, link, asset, and evidence-boundary verifier

## Public URL

```text
https://briansantiago-grc.github.io/BrianSantiago-GRC/
```

Optional role-specific URLs:

```text
https://briansantiago-grc.github.io/BrianSantiago-GRC/?role=it
https://briansantiago-grc.github.io/BrianSantiago-GRC/?role=soc
https://briansantiago-grc.github.io/BrianSantiago-GRC/?role=grc
```

## Verify Before Publishing

From the repository root:

```powershell
& 'C:\Users\brian\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' .\tests\verify_portfolio.py
```

Expected output:

```text
PORTFOLIO_VERIFY_OK
```

Then confirm:

- The page and all local assets return HTTP 200.
- IT Support, SOC, and GRC controls update the correct content and resume.
- The first two projects change for each role.
- Desktop and 390x844 mobile layouts have no horizontal overflow.
- Browser console output has no relevant errors or warnings.
- All six GitHub repositories and all three resume PDFs open correctly.

## Evidence Boundary

The site distinguishes professional support and compliance-support work from hands-on security labs, sample workflows, and synthetic GRC exercises. It does not claim senior SOC ownership, production audit authority, retained telemetry that is not in the repositories, malware containment that did not occur, or controls that were not deployed.
