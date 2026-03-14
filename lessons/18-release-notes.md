# 18. Generate Release Notes From Git History

> **Magic Moment:** Claude reads your git log — a wall of cryptic commit messages — and writes customer-facing release notes that actually sound good, complete with categories, highlights, and the right tone.

## Why This Matters

Nobody reads commit messages except engineers. But your users, your stakeholders, and your marketing team all need to know what shipped. The gap between `fix: handle null ref in checkout flow (#847)` and "We fixed a bug that could cause checkout to freeze — sorry about that!" is the gap between a git log and a product update. Claude bridges it instantly.

## Before You Start

- Claude Code open in your terminal
- A git repository (your product's repo, or any repo you have access to)
- 10 minutes

## Do This Now

### Step 1: Look at the raw material

First, let's see what we're working with. Navigate to your project repo.

**Paste this into Claude Code:**
```
Run git log --oneline --since="2 weeks ago" and show me the last 30 commits. Don't summarize — show the raw output.
```

**What you should see:** Something like this beautiful mess:

```
a3f2c1d fix: resolve race condition in payment processing
b7e4a9f chore: update dependencies
c1d8f3e feat: add dark mode toggle to settings
d4a2b6c refactor: extract auth middleware
e9f1c7d fix: prevent duplicate notification sends
f2b8d4e feat: implement CSV export for reports
g6c3a1f docs: update API documentation
h8d5e2g fix: correct timezone handling in scheduler
i1f7b9h chore: bump node to v20
j3g8c4i feat: add bulk action toolbar to list view
k5h2d6j test: add e2e tests for onboarding flow
```

A PM can maybe squint at this and figure out what matters. But your users? No chance.

### Step 2: Transform commits into release notes

**Paste this into Claude Code:**
```
Based on the git history from the last 2 weeks, generate customer-facing release notes. 

Rules:
- Only include user-facing changes (skip chores, refactors, tests, dependency updates)
- Group into: ✨ New Features, 🐛 Bug Fixes, 💪 Improvements
- Write each item in plain English — no technical jargon
- Lead with the benefit, not the implementation
- Keep each item to 1-2 sentences max

Format it ready to paste into an email, blog post, or in-app notification.
```

**What you should see:** The transformation:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
       What's New — March 2026
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✨ NEW FEATURES

Dark Mode
  Finally! Toggle dark mode in Settings → 
  Appearance. Your eyes will thank you.

CSV Export for Reports
  Download any report as a CSV file. Perfect
  for when you need to slice data in a 
  spreadsheet.

Bulk Actions
  Select multiple items and act on them at 
  once — edit, archive, or delete in bulk.

🐛 BUG FIXES

- Fixed a payment processing issue that could
  cause occasional delays at checkout
- Notifications no longer send duplicates 
  (sorry about that!)
- Times and dates now display correctly 
  regardless of your timezone
```

That's the same commits. Same information. Completely different impact.

### Step 3: Customize the tone

Different audiences need different tones. Try these variations:

**Paste this into Claude Code:**
```
Rewrite those release notes in three different tones:

1. **Casual/fun** — like a startup talking to early adopters
2. **Professional** — like an enterprise SaaS company talking to IT buyers
3. **Internal** — like a PM updating the executive team on what shipped

Keep the same content, just shift the voice.
```

**What you should see:** Three versions of the same release notes, each appropriate for a different audience. Pick the one that matches your brand, or mix and match.

### Step 4: Set up the GitHub Action (advanced, optional)

Want this to happen automatically every time code merges to main? Claude can set that up too.

**Paste this into Claude Code:**
```
Create a GitHub Action workflow that:
1. Triggers on push to main branch
2. Analyzes recent merged PRs
3. Generates release notes in our style
4. Creates a PR with the updated CHANGELOG.md

Use the anthropics/claude-code-action@v1 action. Save the workflow file.
```

**What you should see:** A `.github/workflows/update-docs.yml` file that automates the entire process. Every merge to main triggers Claude to write release notes and submit them as a PR for your review.

⚠️ **This requires a Claude Code OAuth token as a GitHub secret.** Claude will explain the setup steps.

## 🎉 What Just Happened

You turned a wall of developer shorthand into polished, customer-ready communication. Claude filtered out the noise (dependency updates, refactors, test changes), translated technical descriptions into user benefits, and organized everything into a format your users will actually read.

The before/after is stark: commit messages are written for developers tracking changes; release notes are written for users who want to know "what's new and why should I care." Claude understands both audiences and bridges the gap.

## Go Deeper

- **No git repo?** Just describe what shipped: paste a bullet list of what your team built this sprint and ask Claude to write release notes from that
- **Screenshots included:** Ask Claude to open your app in a browser, navigate to new features, and take screenshots to include with the release notes
- **Changelog maintenance:** Have Claude maintain a running CHANGELOG.md that accumulates release notes over time
- **Multi-format output:** Ask for the same notes formatted for email, Slack, in-app banner, and app store "What's New" — all at once

## Share

**Bring back:** Your release notes draft. Read them aloud — would a non-technical user understand every item? If not, ask Claude to simplify further.
