# 19. Weekly Updates That Write Themselves

> **Magic Moment:** Claude reads your recent work — git commits, ticket statuses, docs — and drafts a stakeholder update you'd actually send, formatted for whatever audience needs it.

## Why This Matters

Every PM spends 30-60 minutes every week collecting what happened, formatting it for different audiences, and writing some version of "here's what we shipped, here's what's next." It's important work — stakeholder trust is built on consistent communication — but it's also entirely synthesizable. Claude can gather the context and write the first draft in minutes. Your job becomes editing, not authoring.

## Before You Start

- Claude Code open in your terminal
- Knowledge of what your team shipped/worked on this week (or access to a git repo, project board, or notes)
- 15 minutes

## Do This Now

### Step 1: Gather context

The quality of the update depends on the quality of the input. Give Claude everything.

**Paste this into Claude Code:**
```
I need to write a stakeholder update. Here's my context:

What shipped this week:
[paste bullet list — or say "check git log for the last week"]

What's in progress:
[paste current sprint items, or describe what's being worked on]

Key metrics that moved:
[paste any numbers — signups, revenue, DAU, whatever you track]

Blockers or risks:
[anything stakeholders should know about]

Generate a stakeholder update from this. Lead with impact, not activity.
```

💡 **Have integrations?** If you have Linear, Jira, or GitHub connected via MCP, Claude can pull this data directly:

```
Using the Linear MCP server, get all completed and in-progress issues for the last week. Then check the git log for what was merged. Combine both into a stakeholder update.
```

**What you should see:** Claude synthesizes multiple data sources into a single coherent narrative.

### Step 2: Generate the update

**Paste this into Claude Code:**
```
Write a weekly product update email. Structure it as:

## Executive Summary
[2-3 sentences — the headline version. If they read nothing else, they get the point.]

## 🚀 Shipped This Week
[List completed work with brief descriptions and user impact]

## 🔨 In Progress
[Current work with progress indicators and expected completion]

## 📊 Key Metrics
[Numbers with trend arrows — up is ▲, down is ▼, flat is ▬]

## 🎯 Next Week
[Top 3 priorities]

## 🚧 Blockers & Decisions Needed
[Anything that requires stakeholder input — frame as a clear ask]

Keep it under 300 words. No jargon. Confident tone.
End with one specific ask — a decision, a resource, or an unblock.
```

**What you should see:** A polished update that looks like this:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
            WEEKLY PRODUCT UPDATE
            Week of March 10-14, 2026
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

EXECUTIVE SUMMARY
Strong week — shipped the new onboarding flow
that drove a 23% improvement in Day-1 retention.
Mobile performance work unblocked by completing
the API migration ahead of schedule.

🚀 SHIPPED
✅ New onboarding flow → +23% Day-1 retention
✅ CSV export for all reports
✅ Performance: 40% faster page loads

🔨 IN PROGRESS
AI search        [████████░░] 80% — ships Mar 21
Mobile redesign  [██████░░░░] 60% — ships Mar 28

📊 KEY METRICS
DAU:        12,400  ▲ 8% WoW
Signups:       340  ▲ 12% WoW
Retention D7:  54%  ▬ flat
Revenue:     $47K   ▲ 5% MoM

🎯 NEXT WEEK
1. Ship AI-powered search
2. Begin user interviews for Q2 planning
3. Launch referral program beta

🚧 NEED FROM YOU
Design contractor approval — we're bottlenecked
on the mobile redesign. Approve Y/N?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Step 3: Adapt for different audiences

The same information, three different formats:

**Paste this into Claude Code:**
```
Take that update and create 3 versions:

1. **Executive version** (for CEO/leadership) — 5 bullet points max. Only outcomes and decisions needed. No implementation details.

2. **Team version** (for engineering/design) — More detailed. Include technical context, shoutouts, and what's coming next sprint.

3. **Board version** (for investors/board) — Focus on metrics, growth trajectory, and strategic milestones. Quarterly framing.
```

**What you should see:** Three distinct versions, each pitched at the right altitude. The exec version is 5 lines. The team version has detail and personality. The board version connects this week's work to the bigger picture.

### Step 4: Make it shorter

The final test — can Claude compress without losing substance?

**Paste this into Claude Code:**
```
Take the executive version and make it 50% shorter. Every word must earn its place.
```

**What you should see:** A brutally tight update that proves you don't need length to communicate impact. This is the version busy stakeholders will actually read.

## 🎉 What Just Happened

You automated the most repetitive part of your week. Claude gathered context from multiple sources (git, tickets, your brain), synthesized it into a narrative, and formatted it for different audiences — all in a few minutes.

The key is the format flexibility. A CEO doesn't need the same update as your engineering lead. Instead of writing three separate emails, you write zero — Claude drafts all three from the same source material, and you spend your time editing instead of starting from scratch.

## Go Deeper

- **Automate it:** Set up a weekly cron job or scheduled task that runs Claude against your git log and Linear/Jira board every Friday at 3pm, drops the draft in a Google Doc, and pings you to review
- **Thread the narrative:** Ask Claude to reference last week's update and highlight progress on items you mentioned before — stakeholders love continuity
- **Add metrics automatically:** If you have PostHog or analytics MCP servers connected, Claude can pull real numbers directly instead of you pasting them
- **OKR alignment:** Include your quarterly OKRs and ask Claude to map each shipped item to the relevant objective

## Share

**Bring back:** Your update draft. Read the first sentence of the executive summary. Does it tell a stakeholder exactly why they should care? If not, rewrite it until it does.
