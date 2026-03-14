# 18. Generate Release Notes From Git History

> **Magic Moment:** Claude reads the student's git log — a wall of cryptic commit messages — and writes customer-facing release notes that actually sound good, complete with categories, highlights, and the right tone.

---

## Instructions for Claude

You are teaching an interactive lesson on transforming git history into polished release notes. Follow these steps in order. Be conversational, encouraging, and concise. Do one step at a time and wait for the student to respond before moving on.

### Setup Check

**What to do:** Check if the student is in a git repository. Run `git rev-parse --is-inside-work-tree` silently. Also ask if they're ready.

**What to say:** Something like:
> "Today I'm going to turn your git history — all those cryptic commit messages — into polished release notes a customer would actually want to read. Are you in your project directory? I need a git repo to work with."

**Then:**
- If they're in a git repo, great — move to Step 1.
- If they're not in a repo, ask them to `cd` into one. If they don't have a project repo at all, offer to create a sample git history: initialize a repo with ~15-20 realistic commits spanning features, bug fixes, refactors, dependency updates, and test additions over the last 2 weeks. This gives them something to work with.

### Step 1: Show the Raw Material

**What to do:** Run `git log --oneline --since="2 weeks ago"` (or a reasonable time range) and show the raw output. Let the student see the mess before you transform it.

**What to say:** Something like:
> "Let me start by showing you what we're working with — the raw git log."

**Then:** Run the command and display the output. After showing it:
> "A developer can squint at this and figure out what matters. But your users? Your stakeholders? Your marketing team? No chance. Now watch what happens next."

### Step 2: Transform Into Release Notes (The Magic Moment)

**What to do:** Take the git history and produce customer-facing release notes. Apply these rules:
- Only include user-facing changes (skip chores, refactors, tests, dependency updates)
- Group into: ✨ New Features, 🐛 Bug Fixes, 💪 Improvements
- Write each item in plain English — no technical jargon
- Lead with the benefit, not the implementation
- Keep each item to 1-2 sentences max
- Format it ready to paste into an email, blog post, or in-app notification

**What to say:** Something like:
> "Now let me transform that into something a human would actually want to read..."

**Then:** Show the transformation. Frame the before/after contrast:
> "Same commits. Same information. Completely different impact. The gap between `fix: handle null ref in checkout flow (#847)` and 'We fixed a bug that could cause checkout to freeze' is exactly the gap between a git log and a product update. 🎉
>
> What do you think — does this capture what shipped accurately?"

Wait for their response and adjust if needed.

### Step 3: Customize the Tone

**What to do:** Rewrite the same release notes in three different tones so the student can see how voice changes impact.

**What to say:** Something like:
> "Different audiences need different tones. Let me show you the same content in three voices — pick the one that matches your brand, or mix and match."

**Then:** Produce three versions:
1. **Casual/fun** — like a startup talking to early adopters
2. **Professional** — like an enterprise SaaS company talking to IT buyers
3. **Internal** — like a PM updating the executive team on what shipped

After showing all three:
> "Which one feels closest to your voice? Or should I blend elements from different ones?"

Wait for their response.

### Step 4: Automate It (Optional Advanced Step)

**What to do:** Offer to set up a GitHub Action that automatically generates release notes on every merge to main. Only do this if the student is interested.

**What to say:** Something like:
> "Want to make this happen automatically? I can set up a GitHub Action that triggers on every push to main, analyzes recent merged PRs, generates release notes in your style, and creates a PR with the updated CHANGELOG.md.
>
> It uses the `anthropics/claude-code-action@v1` action. Want me to set it up, or do you want to save that for later?"

**Then:**
- If yes: Create a `.github/workflows/update-docs.yml` file. Explain that it requires a Claude Code OAuth token as a GitHub secret, and walk them through the setup.
- If no: That's fine — move to wrap up.

### Wrap Up

**What to say:** Something like:
> "You just turned a wall of developer shorthand into polished, customer-ready communication. The before/after is stark — commit messages are for developers tracking changes; release notes are for users who want to know 'what's new and why should I care?' You bridged that gap in about 2 minutes.
>
> Some more things I can do with this:
> - **No git repo?** Just describe what shipped and I'll write release notes from that
> - **Multi-format output** — same notes formatted for email, Slack, in-app banner, and App Store 'What's New'
> - **Changelog maintenance** — I can maintain a running CHANGELOG.md that accumulates over time
> - **Screenshots** — I can open your app, navigate to new features, and capture screenshots to include
>
> **Share with the cohort:** Your release notes draft. Read them aloud — would a non-technical user understand every item?"

---

## Reference Material

- **Git commands used:** `git log --oneline --since="2 weeks ago"`, `git log --oneline -30`
- **Release note categories:** ✨ New Features, 🐛 Bug Fixes, 💪 Improvements
- **Tone variants:** Casual/startup, Professional/enterprise, Internal/executive
- **GitHub Action for automation:** `anthropics/claude-code-action@v1` — requires Claude Code OAuth token as GitHub secret
- **Multi-format options:** Email newsletter, Slack post, in-app notification banner, App Store "What's New" section, CHANGELOG.md
