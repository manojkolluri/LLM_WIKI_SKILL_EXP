# Codebase overview

This folder is the knowledge layer for the codebase. Everything you need to know about the files in this repo (excluding the `Wiki/` folder itself) — what they are, how they fit together, and the rules for changing them — lives here.

## Pages in this folder

| Page | What it covers |
|------|----------------|
| [`file-inventory.md`](file-inventory.md) | Brief description of every file in the repo + pointer to its detailed context file |
| [`architecture.md`](architecture.md) | High-level architecture and the reasoning behind every important architectural decision |
| [`conventions.md`](conventions.md) | Coding rules to follow when creating or editing files in this repo |
| [`workflows.md`](workflows.md) | Repeated workflows (populate as patterns emerge) |
| [`file-context/`](file-context/) | One context file per repo file — purpose, key sections, dependencies, gotchas |

## Which page to read

- **Looking for a specific file** → `file-inventory.md`, then drill to its context file in `file-context/`.
- **Need to understand why the system is shaped this way** → `architecture.md`.
- **About to write or edit code** → `conventions.md` first.
- **Doing something you've done before** → `workflows.md`.
