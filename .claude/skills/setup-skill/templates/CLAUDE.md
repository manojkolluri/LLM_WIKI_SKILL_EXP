# {{PROJECT_NAME}}

{{PROJECT_SUMMARY}}

## The `Wiki/` folder

The `Wiki/` folder is the intelligence layer for the LLM. It's where the model should look first to find context about any file in this repo or any process in the surrounding environment, so it can make informed decisions instead of guessing.

Whenever you need information about a file, a workflow, or how a piece of the system fits together, check `Wiki/` before acting.

## Core workflow — required for every change

Whenever the user asks you to do something that changes the repo, you must follow these steps **in order**:

1. **Read the `Wiki/` first, starting with [`Wiki/system-overview.md`](Wiki/system-overview.md).** That's the bird's-eye-view entry point. From there, drill into the relevant page (`codebase/overview.md`, `database/overview.md`, or `deployment/overview.md`) and any specific wiki pages for the file or area you're about to change. Use that context to understand what exists, what conventions apply, and what the change should look like. If no wiki page exists for what you're updating, note it — you'll create one in step 3.

2. **Make the change.**

3. **Update the `Wiki/`** so the docs stay in sync with the code. If you edit a code file, update its context file. If you add a new dependency or workflow, add or update a wiki entry for it. If the relevant wiki page doesn't exist yet, create it. Drift between code and wiki is the failure mode this folder exists to prevent.

4. **Log the change** by adding an entry to `Wiki/CHANGELOG.md`. Use this exact format, **newest at the top**:

   ```
   ### YYYY-MM-DD HH:MM AM/PM TZ
   - **Asked:** <precise summary of what the user requested, in their words where useful>
   - **Done:** <precise summary of what the agent actually implemented>
   - **Files:** <comma-separated paths touched>
   ```

   The date and time must come from the environment (run `date '+%Y-%m-%d %I:%M %p %Z'` for 12-hour format), never guessed. The **Asked** and **Done** lines must be precise — not a vague "updated CLAUDE.md" but specifically what was requested and what was changed. If the two diverge (you implemented something different from what was asked), say so explicitly.

Do all four in the same response, not as a follow-up. If a request is purely a question and no files change, no wiki/log update is needed — but you should still consult the wiki to inform your answer.

## Sandbox folders

- **`Examples/`** — Reference snippets the user provides for the agent to use as canonical examples when building production code. Files here are NOT tracked file-by-file in the Wiki.
- **`Experiments/`** — Agent-created prototypes built on user request, iterated on before approval and integration into `web/`. Files here are NOT tracked file-by-file in the Wiki.

When a prototype or example graduates to production, the port goes into the production code folder (e.g., `web/`), and **that** new file gets full Wiki coverage (inventory row + context file) per the normal rules.
