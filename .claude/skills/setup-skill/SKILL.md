---
name: setup
description: Initialize a new full-stack project repo with the standard Wiki intelligence layer, CLAUDE.md agent workflow, and top-level folder structure (Examples/, Experiments/, web/, Wiki/). Use this skill at the very start of a new project — before any code is written — to bootstrap the documentation scaffolding that every subsequent change will hook into. Trigger this skill whenever the user says they want to "start a new project", "set up a new repo", "bootstrap a new app", "initialize a project with the wiki", "create a fresh project folder structure", or any similar phrasing — even if they don't explicitly name this skill. Also trigger when the user describes a brand-new product idea and signals they want to begin building (e.g., "let's start building X", "I want to set up the repo for Y") — these are setup moments. Stack-agnostic: this skill scaffolds documentation only, not code. The user picks the stack later and populates web/ at that point.
---

# Setup

Initialize a new full-stack project with the standard scaffolding: top-level folders (`Examples/`, `Experiments/`, `web/`, `Wiki/`), the `CLAUDE.md` agent workflow file, and the full `Wiki/` intelligence layer (`system-overview.md`, `CHANGELOG.md`, and the three sub-areas `codebase/`, `database/`, `deployment/` each pre-populated with their overview pages and inventory scaffolds).

This skill produces an empty-but-well-structured repo. **No code, no stack decisions, no plan is written.** Those come after.

## When to use this skill

Use this skill at the **very start of a new project**, before any production code is written. Specifically when:

- The user says "let's start a new project", "set up a new repo", "scaffold a new app", "bootstrap the repo", "initialize the project folder", or similar.
- The user has described a product idea and is ready to begin building — even if they don't use the word "setup".
- The user is starting in an empty directory and wants the standard project skeleton in place.

Do NOT use this skill if:

- The repo already has a populated `Wiki/` folder — it's already been set up. (Confirm by listing the directory first.)
- The user is in the middle of building features and just wants to add a single page or table. That's a normal change, not a setup.
- The user wants to write `PLAN.md` or do product discovery — that's a separate concern. This skill scaffolds; planning is its own activity that the user does either before or after.

## What this skill does — phases

### Phase 1: Interview (brief)

Ask the user for two things, conversationally:

1. **Project name** — the brand / product name. This goes into the README, CLAUDE.md, and Wiki headers. (Example: `Aspirants.io`.) If the user has a folder name that differs from the brand name, ask which one to use in user-facing copy.

2. **One-sentence product summary** — a short description of what this product is and who it's for. This goes into `system-overview.md` and the README. Don't ask for a long product description; one sentence is plenty for scaffolding. The user can flesh out detail later as the wiki populates.

That's it. **Don't ask about stack, framework, database, or any specifics.** This skill is intentionally stack-agnostic — the user makes those decisions when they start populating `web/`. Asking now creates premature lock-in.

### Phase 2: Confirm target directory

Confirm with the user where to scaffold:

- If they're already in an empty directory in Claude Code (check with `ls` or `pwd`), default to scaffolding in the current working directory.
- If the directory is not empty, surface this and ask if they want to scaffold elsewhere or if they want to proceed (with `--force`).
- If they want a new subdirectory, create it first.

### Phase 3: Run the scaffold

Run the scaffold script:

```bash
python <skill-path>/scaffold.py <target-dir> \
  --project-name "<name>" \
  --project-summary "<one-sentence summary>"
```

The script copies every file from the `templates/` folder into the target directory, substituting `{{PROJECT_NAME}}` and `{{PROJECT_SUMMARY}}` placeholders along the way.

If `<skill-path>` isn't obvious, find the skill's location first (the path that contains this `SKILL.md`).

### Phase 4: Report back and hand off

After the scaffold runs, show the user the resulting tree (`ls -la <target>` and `find <target> -type f | sort`) so they can see what was created. Then explicitly hand off:

> The scaffolding is in place. From here, the next moves are yours:
>
> 1. **Initialize git** in the directory if you haven't already: `git init && git add . && git commit -m "Initial scaffold"`.
> 2. **Edit the empty templates** — `system-overview.md`, the `overview.md` pages in each sub-folder, `codebase/conventions.md`, etc. — as you start making concrete decisions. Don't fill them speculatively; fill them as decisions are made.
> 3. **When you're ready to start product planning** (entities, views, flows, non-goals), write that into a `PLAN.md` at the repo root. This skill deliberately does not create `PLAN.md` — the plan is yours to author.
> 4. **When you start writing code in `web/`**, follow the 4-step workflow in `CLAUDE.md`: read the wiki first, make the change, update the wiki, log the changelog.

**Do not start writing code or filling in wiki content beyond what was scaffolded.** This skill's job ends at scaffolding. The next steps are the user's calls, made in subsequent conversations or follow-on requests.

## What gets created

The scaffold produces this exact tree:

```
<target>/
├── .gitignore
├── CLAUDE.md                        # 4-step agent workflow, generalized from Aspirants.io
├── README.md                        # Minimal — project name + summary + layout pointers
├── Examples/
│   └── .gitkeep                     # Explains the folder's purpose; delete when populated
├── Experiments/
│   └── .gitkeep
├── web/
│   └── .gitkeep                     # Production code lands here; stack chosen later
└── Wiki/
    ├── CHANGELOG.md                 # Audit log; populated with format header + empty
    ├── system-overview.md           # Bird's-eye view; pre-populated with project name + summary
    ├── codebase/
    │   ├── overview.md              # Index page for codebase wiki
    │   ├── architecture.md          # Empty scaffold for architectural decisions
    │   ├── conventions.md           # Universal in-file-commentary + sandbox-folder rules
    │   ├── file-inventory.md        # Empty catalog; ready to fill as files land
    │   ├── workflows.md             # Empty; populate when patterns emerge
    │   └── file-context/
    │       └── .gitkeep
    ├── database/
    │   ├── overview.md              # Index page for database wiki
    │   ├── table-inventory.md       # Empty table catalog
    │   ├── function-inventory.md    # Empty function catalog
    │   ├── table-context/
    │   │   └── .gitkeep
    │   └── function-context/
    │       └── .gitkeep
    └── deployment/
        └── overview.md              # Sections to fill as hosting choices are made
```

## Design philosophy of this scaffold

A few things worth knowing about why the scaffold is shaped this way — so the user can edit or extend the templates confidently.

**The Wiki is the intelligence layer; CLAUDE.md is the contract.** Every code change must be preceded by reading the wiki, followed by updating the wiki, and logged in the CHANGELOG. This is enforced by the 4-step workflow in `CLAUDE.md` — the most important file in the scaffold. Don't water it down without thinking carefully about what you're trading off.

**Three wiki sub-folders, separate concerns.** `codebase/`, `database/`, and `deployment/` are kept apart because a code change usually doesn't need DB context, and vice versa. Mixing them creates ambient noise that makes the wiki feel like a wall of text.

**Inventories and context files: same shape across all three areas.** `file-inventory` + `file-context/` mirrors `table-inventory` + `table-context/` mirrors `function-inventory` + `function-context/`. Once the user learns one pattern, they know all three.

**Examples/ and Experiments/ are explicitly NOT tracked in the wiki.** Sandbox files have throwaway-or-graduate lifecycle; tracking each one creates documentation churn without payoff. The `conventions.md` codifies this rule.

**Empty scaffolds, not pre-filled content.** Most files in this scaffold are deliberately stubs. Pre-filling them with speculative content (e.g., "the auth flow uses Supabase") locks in decisions the user hasn't made yet and rots when they make different ones. Stubs invite the user to populate as decisions emerge.

**Stack-agnostic for code, opinionated about documentation structure.** The `web/` folder is empty because every project picks its own stack. The Wiki structure is opinionated because that part *is* transferable across projects. This is the core insight that justifies the skill: the documentation methodology is the reusable asset; the code stack is per-project.

## Editing the templates

If the user wants the scaffold to be different — different default folder names, additional template files, stack-specific scaffolds — edit `templates/` inside this skill's directory. The scaffold script copies whatever's in `templates/` verbatim (with placeholder substitution). Adding a new file to the scaffold is as simple as dropping it into `templates/`.

Be careful changing the structure of `CLAUDE.md` or the wiki overviews — downstream wiki content references them by path. If you rename `codebase/overview.md`, you have to update the references in `system-overview.md` and the other overview pages.

## What this skill does not do

- **Does not create `PLAN.md`.** Product planning is a separate activity. The user authors `PLAN.md` themselves, either before invoking this skill (and pastes the content in afterwards) or after.
- **Does not initialize git.** The user runs `git init` themselves. Leaving git uninitialized lets the user decide where the repo lives and whether to push to GitHub immediately.
- **Does not install dependencies, scaffold a Next.js app, or create any production code.** Those are subsequent steps, taken when the user has decided on a stack.
- **Does not configure Supabase, Vercel, or any external service.** External services are configured manually by the user as the project progresses.
- **Does not assume the user wants Next.js + Supabase + Vercel.** The wiki shape supports those choices well (the database folder is shaped for SQL with policies), but it works for any stack the user picks. If the project ends up not needing a database, the user can ignore `Wiki/database/` or delete it.
