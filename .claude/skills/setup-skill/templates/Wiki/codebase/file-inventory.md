# File inventory

Every committed source file in the repo gets one row in the table below: a brief description and a pointer to its detailed context file in [`file-context/`](file-context/). Three exclusions:

- **`Wiki/`** — documentation about the repo (already self-describing).
- **`CLAUDE.md`** — instructions for the agent, not a code artifact.
- **Files inside `Examples/` and `Experiments/`** — sandbox / reference material with throwaway-or-graduate lifecycle. Tracking each one would create churn without payoff.

## How to use this

- **Looking for what a file does** → find its row, read the description, drill to its context file for detail.
- **Adding a new file to the repo** → add a row here, create its context file in `file-context/` (mirroring the source path), and link them.

## Context-file template

Each context file in `file-context/` follows this shape:

```
# Context: <relative path to source file>

## Purpose
What this file is and why it exists.

## Key sections / entry points
For code files: main functions, exported APIs, important constants.
For data files: schema overview, ID conventions.
For docs: what topics it covers.

## Dependencies
What this file depends on. What depends on it.

## Gotchas / things to know
Hidden constraints, surprises, or "do not change without checking X" notes.
```

## Inventory

### Repo root

| File | Brief description | Context file |
|------|-------------------|--------------|
| _No files tracked yet._ | | |

### Sandbox / reference folders (intentionally not tracked file-by-file)

| Folder | Purpose |
|--------|---------|
| `Examples/` | Reference snippets the user provides for the agent to use as canonical examples when building production code. |
| `Experiments/` | Agent-created prototypes built on user request, iterated on before approval and integration into production folders. |

Files inside these folders are **not** listed in this inventory and **don't** get context files in `file-context/`.
