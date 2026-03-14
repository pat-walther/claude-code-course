# 20. Prioritize With Data, Not Gut

> **Magic Moment:** Claude takes your messy backlog — a mix of feature requests, bugs, tech debt, and half-baked ideas — and produces a scored, ranked list with reasoning you can defend in a planning meeting.

## Why This Matters

Every PM has a backlog that's part strategy, part wishlist, part graveyard. You know you should prioritize it more rigorously, but frameworks like RICE and ICE take forever to score manually, and the inputs are always a little made up anyway. Claude doesn't fix the subjectivity problem — but it does force rigor, surfaces your assumptions, and does the math in seconds so you can focus on the judgment calls.

## Before You Start

- Claude Code open in your terminal
- Your backlog — exported from Jira/Linear, or just a list you type out
- Any context on your users, goals, or strategy (the more Claude knows, the better the output)
- 15 minutes

## Do This Now

### Step 1: Feed Claude your backlog

The easiest path: just paste it.

**Paste this into Claude Code:**
```
Here is my current product backlog:

[Paste your backlog items — titles are fine, descriptions are better. Even a rough list works:]

1. Dark mode
2. Fix checkout crash on Android
3. Add CSV export to reports
4. Redesign onboarding flow
5. Implement SSO for enterprise
6. Performance improvements for large accounts
7. In-app feedback widget
8. Notification preferences page
9. API rate limiting
10. Multi-language support

Here's context about our product and users:
[Paste any context — who your users are, what your goals are, what you've heard in user interviews]
```

💡 **Have Jira or Linear connected?** Use MCP instead:

```
Using the Jira MCP server, fetch all issues in the [PROJECT_KEY] backlog. Analyze the distribution by priority, component, and labels. Show me what we're working with before we prioritize.
```

**What you should see:** Claude acknowledges the backlog and may ask clarifying questions about your goals and users. This is a good sign — it means the prioritization will be more contextual.

### Step 2: Apply a scoring framework

**Paste this into Claude Code:**
```
Score each backlog item using the RICE framework:
- Reach: How many users will this impact per quarter? (estimate)
- Impact: How much will this move the needle per user? (3=massive, 2=high, 1=medium, 0.5=low, 0.25=minimal)
- Confidence: How sure are we about the estimates? (100%=high, 80%=medium, 50%=low)
- Effort: How many person-weeks to build? (estimate)

RICE Score = (Reach × Impact × Confidence) / Effort

Show me:
1. A scored table sorted by RICE score (highest first)
2. A 2x2 matrix of Impact vs. Effort (the quick wins quadrant)
3. Your top 5 recommendation with reasoning

Be opinionated. I don't want a neutral spreadsheet — I want a recommendation.
```

**What you should see:** Something like:

```
═══════════════════════════════════════════════════════════
                    RICE PRIORITIZATION
═══════════════════════════════════════════════════════════

 #  │ Item                    │ Reach │ Impact │ Conf │ Effort │ RICE
────┼─────────────────────────┼───────┼────────┼──────┼────────┼──────
 1  │ Fix checkout crash      │ 5000  │  3.0   │ 100% │  1 wk  │ 15000
 2  │ Redesign onboarding     │ 8000  │  2.0   │  80% │  4 wk  │  3200
 3  │ CSV export              │ 2000  │  2.0   │ 100% │  1 wk  │  4000
 4  │ Performance (lg accts)  │  500  │  3.0   │  80% │  3 wk  │   400
 5  │ SSO for enterprise      │  200  │  3.0   │  80% │  4 wk  │   120
 ...

═══════════════════════════════════════════════════════════
              IMPACT vs. EFFORT MATRIX
═══════════════════════════════════════════════════════════

           HIGH IMPACT
               │
  🎯 DO FIRST  │  📋 PLAN CAREFULLY
  Checkout fix │  Onboarding redesign
  CSV export   │  Enterprise SSO
               │
 ──────────────┼──────────────────
               │
  ❓ MAYBE     │  ❌ DEPRIORITIZE
  Feedback     │  Multi-language
  widget       │  (low reach now)
               │
           LOW IMPACT
    LOW EFFORT ─────── HIGH EFFORT
```

⚠️ **The RICE numbers are estimates.** Claude is making educated guesses based on the context you gave it. The value isn't in the exact scores — it's in the relative ranking and the reasoning behind it. If a score looks wrong, challenge it (see Step 4).

### Step 3: Try a different framework

Don't love RICE? Swap it.

**Paste this into Claude Code:**
```
Now re-score the same backlog using ICE instead:
- Impact: How much will this affect our key metric? (1-10)
- Confidence: How sure are we? (1-10)
- Ease: How easy is this to implement? (1-10)

ICE Score = Impact × Confidence × Ease

Show me how the ranking changes. What moves up? What moves down? Which framework tells a more useful story for our situation?
```

**What you should see:** A different ranking that reveals different priorities. Some items stay at the top regardless of framework (those are your clear winners). Items that shift a lot are the judgment calls worth discussing with your team.

### Step 4: Challenge the prioritization

This is the most valuable step. Push back.

**Paste this into Claude Code:**
```
I want you to challenge this prioritization. Play devil's advocate:

1. What context am I missing that would change the ranking?
2. Which items might be ranked wrong because of bad assumptions?
3. Is there a dependency I'm ignoring? (Something that needs to ship before something else can work?)
4. What's the contrarian case? If a smart PM disagreed with this ranking, what would they argue?
5. If we could only ship 3 things this quarter, which 3 and why?
```

**What you should see:** Claude pokes holes in its own analysis. It might surface dependencies ("SSO is ranked low, but your top 3 sales prospects require it"), hidden assumptions ("the reach estimate for onboarding assumes current traffic, but what if you're launching a campaign?"), or strategic considerations the framework misses.

### Step 5: Create the final recommendation

**Paste this into Claude Code:**
```
Based on everything — both frameworks, the challenges, and the analysis — create a final prioritized list I can bring to sprint planning.

Format it as:

## 🔴 Must Do (This Sprint)
[Items with clear justification — 2-3 max]

## 🟡 Should Do (Next Sprint)  
[Items that are important but can wait — 3-5 items]

## 🟢 Nice to Have (This Quarter)
[Items for when there's bandwidth]

## 🔵 Revisit Later
[Items to park — with a note on what would change the priority]

For each item, include one sentence on WHY it's in that tier.
```

**What you should see:** A clean, defensible prioritization document. Not a spreadsheet of scores — a recommendation with reasoning that you can walk into a meeting and explain.

## 🎉 What Just Happened

You applied a rigorous prioritization framework to your entire backlog in about 10 minutes. Normally this takes a PM a half-day with a spreadsheet, and the results are often biased by the anchoring effect (whatever you score first sets the baseline for everything else). Claude scores everything independently, applies the math consistently, and then challenges its own assumptions when you ask.

The real magic was Step 4 — the challenge. Frameworks give you structure, but they don't replace judgment. By asking Claude to argue against its own ranking, you surface the assumptions and trade-offs that make prioritization hard. That's the conversation your team should be having.

## Go Deeper

- **Add customer voice:** Paste customer feedback alongside your backlog and ask Claude to map requests to backlog items. "Which backlog items address the most customer complaints?"
- **Pricing analysis:** Ask Claude to research competitor pricing and identify which features are commonly gated behind paid tiers — this informs what to build for conversion vs. retention
- **Quarterly roadmap:** After prioritizing, ask Claude to arrange the top items into a quarterly roadmap with dependencies and milestones
- **Re-score monthly:** Save your scored backlog and re-run the analysis each month with updated context. Watch how priorities shift as you learn more

## Share

**Bring back:** Your top 3 priorities and Claude's reasoning. Do you agree with the ranking? If not, what would you change and why?
