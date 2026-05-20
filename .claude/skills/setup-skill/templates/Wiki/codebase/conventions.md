# Conventions

Rules to follow when creating or editing files in this repo. These are deliberate constraints — don't quietly violate them. If a change requires breaking one, surface it and ask first.

## Stack

_Fill in once the stack is chosen._

- **Framework:** _e.g., Next.js (App Router) + React + TypeScript_
- **Styling:** _e.g., Tailwind CSS + global stylesheet for tokens_
- **Database:** _e.g., Supabase (Postgres)_
- **Hosting:** _e.g., Vercel_
- **Build:** _e.g., `npm run build` from inside `web/`_

## Where code lives

_Fill in once the project structure is established._

The website lives entirely under `web/` (or whichever folder you settle on). The repo root is for `Wiki/`, sandbox folders (`Examples/`, `Experiments/`), and project meta (`README.md`, `LICENSE`, `CLAUDE.md`, `.gitignore`).

- **Don't add new top-level directories** without surfacing why.
- **Don't add framework source files to the repo root.** Production code lives in its dedicated folder.

## In-file documentation (extensive commentary) — required

Every code file must carry **extensive in-file commentary** so a human or AI reading the file alone — without consulting the Wiki — can understand WHAT it does, WHY it's shaped this way, and WHERE the gotchas are. The Wiki (`Wiki/codebase/`) is the index; the file itself is the source of truth, and its comments are first-class.

### Required elements in any code file

1. **File header banner** — multi-line comment at the top covering:
   - **FILE / PROJECT / ROLE / PURPOSE** lines of identity.
   - **WHAT THIS FILE IS** — one paragraph on purpose.
   - **WHY [KEY DECISION]** — paragraphs for each important decision the file embodies.
   - **STRUCTURE / SECTIONS** — top-to-bottom sketch.
   - **EXTERNAL DEPENDENCIES** — what this file pulls in from outside.
   - **WHEN YOU EDIT THIS FILE** — concrete reminders (which Wiki pages to update, fragility warnings, smoke-test instructions).

2. **Section dividers** — mark major sections with a row of `═` characters inside a comment.

3. **Pre-block descriptive comments** — before each non-trivial function, effect, or subtree, write a comment explaining **WHY**, not just WHAT.

4. **Inline annotations** — for specific values that aren't self-explanatory (timing values, magic numbers, color choices, threshold values), add a short trailing comment.

5. **Fragility warnings** — when code is brittle or has hidden coupling, lead with `FRAGILITY WARNING:` so future editors notice it before they break it.

### Voice and depth

- Authoritative but informal — "We deliberately do not polyfill" not "polyfilling is not implemented."
- Honest about limitations, alternatives considered, and the reason this approach won.
- Cross-reference siblings: "see `<sibling-file>` for the related variant."
- Prefer explanation over jargon — write for a senior dev who hasn't seen this codebase before.

## Sandbox folders — `Experiments/` and `Examples/`

Two top-level folders sit outside the production code:

- **`Experiments/`** — agent-created prototypes built on user request. Initial-design artifacts for things we're iterating on before deciding what to build for real.
- **`Examples/`** — reference snippets the user provides for the agent to use as canonical examples when producing actual production code.

**Files inside these folders are NOT tracked in the Wiki.** No row in `Wiki/codebase/file-inventory.md`. No context file in `Wiki/codebase/file-context/`. Their lifecycle is "drop in or generate, iterate, then port into production or discard" — file-level Wiki coverage would create churn without payoff. CHANGELOG entries may note creation events for these files (event records ≠ file docs), but anything more granular is reserved for production code.

When a prototype or example graduates to production, the port goes into the production code folder, and **that** new file gets full Wiki coverage (inventory row + context file) per the normal rules.

## Project-specific conventions

_Add sections here as the project's specific patterns emerge: naming, env vars, hygiene rules, etc. Below are common ones worth filling in early._

### Naming and consistency

_Add brand name rules, file naming patterns, any "do not change" idioms here._

### Env vars

_Add rules for client-visible vs server-only env vars, where `.env` lives, what's in `.gitignore`._

### Hygiene

_Add anything that should stay out of the repo: `.DS_Store`, `node_modules/`, build artifacts, secrets._

## When in doubt

If a change would break any of the above, surface it first. The constraints exist for reasons that aren't always written next to the constraint.
