# App Studio decisions

The durable agreement between learner and AI. Update only agreed decisions and
actual evidence; pending is a valid state. Keep explanations/help in
[LEARNING.md](LEARNING.md), not a second copy here.

## Current stage

- **Current feature:** APP-002.
- **Status:** APP-001 merged and verified; APP-002 full cumulative checks passed; learner inspected the redirect after logout, interpreted HTTP 200 and chose to keep the account flow.
- **Next step:** Review the latest checks on PR #4 before deciding whether to merge.
- **Implementation marker:** `implemented_through: 2` after verified full APP-002 success; the normal full check passed at stage 2.

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
| Own issue / branch / PR | [Issue #1](https://github.com/edgaroj52218/my-app-studio/issues/1); `codex/app-001-portfolio`; [PR #2](https://github.com/edgaroj52218/my-app-studio/pull/2). |

Résumé and specific project evidence have not been supplied. The homepage labels
them as unavailable/planned, with no fabricated experience or download links.
Signup/login are being implemented in APP-002. Deployment is outside this assignment.

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
| Expected public/private behavior and account flow | Public portfolio; member signup, login, private dashboard and POST logout. Anonymous dashboard requests redirect to login; private API returns 401. Sessions persist between requests via a protected cookie and server validation. |
| Valid and rejected cases to demonstrate | Valid signup/login; duplicate/invalid signup, role injection, wrong credentials, missing CSRF, excessive/duplicate form fields, expired sessions and copied-token replay after logout. |
| Own issue / branch / PR | [Issue #3](https://github.com/edgaroj52218/my-app-studio/issues/3); `codex/app-002-accounts`; [PR #4](https://github.com/edgaroj52218/my-app-studio/pull/4). |

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
| APP-001 | `app/brand.json`, `app/templates/base.html`, `app/templates/home.html`, `app/static/site.css`, `app/static/logo.svg`; [issue #1](https://github.com/edgaroj52218/my-app-studio/issues/1) | `python studio.py check --lesson APP-001`: Black/Pylint passed; foundation 96 passed, 2 skipped (learner reran in administrator PowerShell; saved passing receipt matched source before marker update); APP-001 contracts 2 passed; Chromium 2 passed. AI inspected 1440px desktop and 390px narrow layout. Learner identified fixed widths, excessive spacing and missing responsive design as potential overflow causes; learner observed content stacking at 390px without sideways scrolling and connected it to demonstrating responsive design to employers. | Learner keeps the responsive, clean layout and approved the summary. Implementation committed as `4ea0c1a` and pushed; [PR #2](https://github.com/edgaroj52218/my-app-studio/pull/2) merged as `a73fa5d`; issue #1 closed. Marker advanced to 1; normal full check passed after marker change (96 foundation, 2 contract and 2 Chromium tests passed; 2 skipped). [CI run](https://github.com/edgaroj52218/my-app-studio/actions/runs/42320637714) passed both `check` and `windows` for implementation commit `4ea0c1a`; both latest PR jobs and [main jobs](https://github.com/edgaroj52218/my-app-studio/actions/runs/42321124327) also passed; local main was synced and rechecked. |
| APP-002 | `app/features/accounts.py`, `app/templates/account.html`, `app/templates/dashboard.html`, `app/static/site.css`, `contracts/test_accounts.py`; issue #3 above | Initial cumulative contracts: 14 passed; Chromium: 2 passed; Black/Pylint passed. Foundation: 95 passed, 2 skipped, 1 Windows symlink privilege failure. All 15 account tests passed separately. Learner then ran the full cumulative check: 96 foundation tests, 17 contracts and 2 Chromium tests passed; 2 skipped. AI verified the saved receipt matched current source. AI inspected signup at 1440/390px and login at 390px. | Learner kept the account flow and approved the summary. The normal full check after the marker update passed (96 foundation, 17 contracts, 2 Chromium tests, 2 skipped). Both GitHub jobs passed for the [APP-002 implementation at 67d7d74](https://github.com/edgaroj52218/my-app-studio/actions/runs/42325633695). Merge pending. |
| APP-003 | Pending | Unfinished; explicit contracts not yet passed | Pending |

The instructor's reference branches show possible implementations. They do not
establish this repository's completion or the learner's own reasoning.
