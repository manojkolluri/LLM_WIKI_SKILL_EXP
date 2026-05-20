# Function inventory

Every custom database function gets one row below: a brief description and a pointer to its detailed context file in [`function-context/`](function-context/).

## Context-file template

Each context file in `function-context/` follows this shape:

```
# Context: <function_name>

## Purpose
What this function does and why it exists.

## Signature
Language (plpgsql / sql / etc.), arguments, return type, volatility (STABLE / IMMUTABLE / VOLATILE), security context (SECURITY DEFINER vs SECURITY INVOKER).

## Body
The actual function body (or a faithful summary). Annotate non-obvious logic.

## Security model
Who can EXECUTE this function. If SECURITY DEFINER, who owns it and what privileges that grants. Include the EXECUTE grants table.

## Callers
Where this function is invoked from — triggers, RPC calls from the client, other functions.

## Gotchas / things to know
Mutability surprises, security pitfalls, ordering dependencies.

## How to verify
Steps to confirm the function is in the expected state (e.g., dashboard checks, SQL queries against system catalogs).
```

## Onboarding a new function

When adding a new database function:

1. Create the function (migration / SQL / dashboard).
2. **For `SECURITY DEFINER` functions, REVOKE EXECUTE from PUBLIC by default.** Only grant to the specific role(s) that need it. The default grant of EXECUTE to PUBLIC is a common security pitfall.
3. Add a row to the inventory below.
4. Create `function-context/<name>.context.md` from the template above.
5. Append a CHANGELOG entry.

## Inventory

| Function | Brief description | Context file |
|----------|-------------------|--------------|
| _No custom functions yet._ | | |
