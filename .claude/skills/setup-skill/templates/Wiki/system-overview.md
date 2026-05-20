# System overview

The bird's-eye view of {{PROJECT_NAME}}. **Read this first** when starting a task — then drill into the page that's relevant to what you're doing.

## What {{PROJECT_NAME}} is

{{PROJECT_SUMMARY}}

## Map of the Wiki

Three areas, one folder each:

- **`codebase/`** — repo structure, file index, code conventions, architecture decisions.
- **`database/`** — tables, functions, and data layer.
- **`deployment/`** — hosting, environments, and deployment configuration.

The areas are kept separate so a task that only touches one of them doesn't drag in context from the others.

## Drill-down: pages

| Page | What it covers |
|------|----------------|
| [`codebase/overview.md`](codebase/overview.md) | Repo structure, file index, code conventions, architecture |
| [`database/overview.md`](database/overview.md) | Tables, functions, and data layer |
| [`deployment/overview.md`](deployment/overview.md) | Hosting and deployment configuration |

## Which page to read

- **Editing a file or adding code** → start with `codebase/overview.md`.
- **Touching data, schemas, or storage** → `database/overview.md`.
- **Shipping, infra, monitoring, environments** → `deployment/overview.md`.
- **Cross-cutting** (a feature that touches code + DB + deploy) → read all three before acting.

If a relevant page is empty, that area hasn't been documented yet — note it and create the entry as part of your change (per the core workflow in `CLAUDE.md`).
