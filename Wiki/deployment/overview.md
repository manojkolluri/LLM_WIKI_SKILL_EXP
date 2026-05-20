# Deployment overview

This folder is the knowledge layer for how this project gets to production: hosting, environments, environment variables, build configuration, and any monitoring or analytics integrations.

## What lives here

_Fill in as deployment specifics are decided. Sections worth documenting:_

### Hosting

- Where the project is hosted (Vercel / Netlify / Cloudflare / self-hosted / etc.)
- The project's URL(s) — production, preview, staging
- Any platform-specific configuration (e.g., "Root Directory" setting, build command overrides)

### Environments

- Which environments exist (production, preview, development)
- How they differ (different env vars, different databases, different feature flags)

### Environment variables

- What env vars are required
- Which are client-visible vs server-only
- Where the canonical list lives (typically `.env` in the project's working directory — gitignored)
- Where they're configured in the hosting dashboard

### Build process

- The build command and where it runs from
- Build artifacts and where they end up
- Any pre-build or post-build steps

### Monitoring / analytics

- What's wired in (analytics, error tracking, performance monitoring)
- Where the data shows up

### Domains and DNS

- Custom domain configuration
- DNS records and where they're managed

## Tracking convention

When deployment configuration changes (new env var, new analytics integration, new domain, change in hosting provider), update this file in the same change. Append a CHANGELOG entry. Drift between deployed reality and these docs is the failure mode this folder exists to prevent.
