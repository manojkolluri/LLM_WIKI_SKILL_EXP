# Database overview

This folder is the knowledge layer for the database. Everything that's true about tables, indexes, RLS policies (if applicable), and database functions / triggers (and how they're accessed) lives here.

## Pages in this folder

| Page | What it covers |
|------|----------------|
| [`table-inventory.md`](table-inventory.md) | Brief description of every custom table + pointer to its detailed context file |
| [`table-context/`](table-context/) | One context file per custom table — schema, indexes, policies, triggers, consumers, gotchas |
| [`function-inventory.md`](function-inventory.md) | Brief description of every database function |
| [`function-context/`](function-context/) | One context file per database function — purpose, signature, callers, gotchas |

## Tracking convention

**Every database object we create — tables, policies, functions, triggers — gets recorded here.**

- **Tables** get a row in `table-inventory.md` and a context file at `table-context/<name>.context.md`. The context file has dedicated sections for schema, indexes, **policies**, **triggers**, consumers, and gotchas.
- **Functions** get a row in `function-inventory.md` and a context file at `function-context/<name>.context.md`. Includes signature, language, purpose, callers, and gotchas.

When we add or change anything, the Wiki update happens in the same change as the database change — drift between the database state and these files is the failure mode this folder exists to prevent.

## Which page to read

- **Looking for a specific table** → `table-inventory.md`, then drill to its context file.
- **Looking for a function** → `function-inventory.md`, then drill to its context file.
- **Adding a new table or modifying a schema** → start with `table-inventory.md`'s template; update the context file in the same commit as the schema change.
- **Auditing security** → drill into individual table context files; each has a policies section.

## What lives outside this folder

- **The actual schema, indexes, policies, and functions** live in **the database itself**, not in this repo. This folder is documentation of that state — not source-of-truth. If reality and the docs diverge, reality wins; update the docs to match.

## Current state

_Fill in once tables exist._

- **Custom tables:** _none yet_
- **Database functions:** _none yet_
- **Triggers:** _none yet_

Everything custom we add from here on out gets tracked in the appropriate inventory + context file.
