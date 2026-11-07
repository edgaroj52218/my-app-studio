# App Studio decisions

The durable agreement between learner and AI. Update only agreed decisions and
actual evidence; pending is a valid state. Keep explanations/help in
[LEARNING.md](LEARNING.md), not a second copy here.

## Current stage

- **Current feature:** APP-001.
- **Status:** Portfolio homepage kept by learner for its responsive, clean layout; summary reviewed. Normal full check after marker update passed; GitHub cycle pending.
- **Next step:** Commit/push and open the APP-001 PR for CI review.
- **Implementation marker:** `studio.json` now declares `implemented_through: 1` after verified full APP-001 success. Normal full check passed after the marker update.

This repository owns application code. Server/proxy changes and production
deployment are outside these three local-development lessons. Prepared helpers
are reusable foundations, not evidence that unfinished routes are implemented.

## APP-001 · Branded homepage

**Scope:** make the neutral FastAPI homepage express one chosen identity with
a simple original SVG mark, coherent copy, navigation and shared style tokens.
Keep account actions honest about their unfinished state.

| Decision | Agreement |
|---|---|
| Visitor and concrete use situation | Employers reviewing Edgar's résumé, work and projects for IT opportunities. |
| Reused IS117 brand, or name / promise / primary archetype | New identity: Edgar Steven Ojeda. Sage; technical learning and problem-solving. Promise: make the thinking behind the work clear. |
| One visible choice and visitor benefit | Problem → approach → result shows complexity, technical choices and outcomes. Calm navy/teal, clear wording, original ESO SVG, shared style tokens. |
| Own issue / branch / PR | [Issue #1](https://github.com/edgaroj52218/my-app-studio/issues/1); `codex/app-001-portfolio`; PR pending. |

Résumé and specific project evidence have not been supplied. The homepage labels
them as unavailable/planned, with no fabricated experience or download links.
Signup/login remain unfinished. Deployment is outside this assignment.

**Keep when:** the agreed identity is visible and usable at desktop/narrow widths;
full foundation + APP-001 checks pass; AI review and the learner's actual check
interpretation/browser observation/keep reason are recorded; reviewed evidence
and verified GitHub state are linked below.

## APP-002 · Signup, login and logout

**Scope:** add browser forms and REST behavior for member signup, login, a private
dashboard and logout backed by SQLite. Reuse the prepared password/JWT/CSRF/session
helpers; keep data local. New accounts cannot choose their role.

| Decision | Agreement |
|---|---|
| Expected public/private behavior and account flow | Pending |
| Valid and rejected cases to demonstrate | Pending |
| Own issue / branch / PR | Pending |

**Keep when:** the agreed forms/API work; duplicate/invalid signup and wrong
credentials are rejected; passwords are hashed; authentication uses validated,
expiring JWTs with protected cookies and CSRF; private requests require a live
session and logout revokes it. Full cumulative checks, AI review, actual learner
contributions and GitHub state are recorded. This is not a production-security certification.

## APP-003 · Server-enforced roles

**Scope:** enforce a small member/admin boundary in the API and browser. Assign
roles only through the trusted local terminal command; use current server-side
permissions, including for an existing session after a role change.

| Visitor | Homepage | Member area | Admin area/API |
|---|---|---|---|
| Anonymous | Allowed | Login required | Login required |
| Member | Allowed | Allowed | Forbidden |
| Admin | Allowed | Allowed | Allowed |

| Decision | Agreement |
|---|---|
| Intended admin-only result | Pending |
| Actual allowed/denied request evidence | Pending |
| Own issue / branch / PR | Pending |

**Keep when:** a direct request cannot bypass the role boundary, role changes
take effect as specified, new signup remains member-only, and full cumulative
checks plus AI review pass. Link the learner's actual interpretation/observation,
reviewed record and verified GitHub result. Hidden navigation alone is insufficient.

## Evidence

Link actual files/checks and the student's own issues/PRs. No fabricated URLs,
customer research or claims that a timestamp proves learning.

| Feature | Files / own issue / PR | Actual checks and learner observations | Kept / GitHub state |
|---|---|---|---|
| APP-001 | `app/brand.json`, `app/templates/base.html`, `app/templates/home.html`, `app/static/site.css`, `app/static/logo.svg`; [issue #1](https://github.com/edgaroj52218/my-app-studio/issues/1) | `python studio.py check --lesson APP-001`: Black/Pylint passed; foundation 96 passed, 2 skipped (learner reran in administrator PowerShell; saved passing receipt matched source before marker update); APP-001 contracts 2 passed; Chromium 2 passed. AI inspected 1440px desktop and 390px narrow layout. Learner identified fixed widths, excessive spacing and missing responsive design as potential overflow causes; learner observed content stacking at 390px without sideways scrolling and connected it to demonstrating responsive design to employers. | Learner keeps the responsive, clean layout and approved the summary. Local and unstaged; no PR/commit/push. Marker advanced to 1; normal full check passed after marker change (96 foundation, 2 contract and 2 Chromium tests passed; 2 skipped). PR/CI/merge pending. |
| APP-002 | Pending | Unfinished; explicit contracts not yet passed | Pending |
| APP-003 | Pending | Unfinished; explicit contracts not yet passed | Pending |

The instructor's reference branches show possible implementations. They do not
establish this repository's completion or the learner's own reasoning.
