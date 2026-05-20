# Table inventory

Every custom table in the database gets one row below: a brief description and a pointer to its detailed context file in [`table-context/`](table-context/).

## Context-file template

Each context file in `table-context/` follows this shape:

```
# Context: <table_name>

## Purpose
What this table stores and why it exists.

## Schema
| Column | Type | Constraints | Notes |
|--------|------|-------------|-------|
| ...    | ...  | ...         | ...   |

## Indexes
List of indexes, what each is for.

## Policies
RLS / access-control rules (if applicable). Document each policy: name, operation (SELECT/INSERT/UPDATE/DELETE), the USING / WITH CHECK predicate, and what it enforces.

## Triggers
Any triggers on this table or that fire because of it. Document trigger name, event, and what it does.

## Used by
Files in the codebase that read from or write to this table.

## Gotchas / things to know
Hidden constraints, surprising behavior, or "do not change without checking X" notes.

## How to verify
Steps to confirm the table is in the expected state (e.g., dashboard checks, sample SQL queries).

## Maintenance
Procedure to follow when schema or policies change — including which Wiki pages to update.
```

## Onboarding a new table

When adding a new table to the database:

1. Create the table in the database (migration / SQL / dashboard).
2. Add a row to the inventory below.
3. Create `table-context/<name>.context.md` from the template above.
4. If the table introduces new policies or triggers, document them in the context file's relevant section.
5. Append a CHANGELOG entry.

## Inventory

| Table | Brief description | Context file |
|-------|-------------------|--------------|
| _No custom tables yet._ | | |
