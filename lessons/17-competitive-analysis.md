# 17. Research Competitors Systematically

> **Magic Moment:** Claude analyzes a competitor's entire public presence — website, app store, reviews, docs — and produces a structured competitive brief that would take you hours to compile manually.

## Why This Matters

You know you should be tracking competitors more closely. But competitive analysis always gets deprioritized because it's tedious: visit five websites, read their pricing pages, scan their changelogs, check their reviews, piece it all together. By the time you finish, it's already stale. Claude can do this research in minutes, and you can re-run it anytime the market shifts.

## Before You Start

- Claude Code open in your terminal
- The name(s) of 3-5 competitors you want to analyze
- 15 minutes

## Do This Now

### Step 1: Identify your competitors

**Paste this into Claude Code:**
```
I'm building [describe your product in one sentence].

Get my top 3-5 direct competitors. For each one, find:
- Website URL
- App store link (if applicable)
- Public product documentation or help center
- Release notes or changelog (if public)
- Review sites (G2, Capterra, App Store reviews)
- Any community forums or discussions

List them in a table.
```

**What you should see:** A clean table with your competitive landscape mapped out. Claude will use web search to find these — you'll likely discover competitors you weren't tracking.

💡 **Already know your competitors?** Skip this step and just list them directly in Step 2.

### Step 2: Analyze their positioning

**Paste this into Claude Code:**
```
Visit these competitor sites and analyze their positioning:
[list your competitor URLs]

For each competitor, extract:
- Value proposition (the one-sentence version: "[BRAND] is a [DIFFERENTIATOR] for [SEGMENT]")
- Target customer segment
- Key features they emphasize
- What pain points they lead with
- Pricing model (if public)

Then visualize the competitive landscape using ASCII:
- A 2x2 positioning matrix (you pick the best axes)
- A feature comparison table
- Where each competitor is strong vs. weak
```

**What you should see:** Something like this:

```
═══════════════════════════════════════════════
         COMPETITIVE POSITIONING MAP
═══════════════════════════════════════════════

              HIGH PRICE
                 │
    Enterprise   │   Premium
    Player       │   Specialist
    (Comp C) ●   │        ● (Comp A)
                 │
 ─────────────── ┼ ─────────────── BROAD
  NARROW         │              FEATURES
                 │
           ●     │   ● (Comp B)
     (You)       │
    Focused &    │   Freemium
    Affordable   │   Generalist
                 │
              LOW PRICE

═══════════════════════════════════════════════
         FEATURE COMPARISON MATRIX
═══════════════════════════════════════════════
Feature          You   A    B    C
─────────────────────────────────────
Core workflow     ✅   ✅   ✅   ✅
AI features       ✅   ❌   ✅   ✅
Mobile app        ✅   ✅   ❌   ✅
API access        ❌   ✅   ✅   ✅
SSO/Enterprise    ❌   ✅   ❌   ✅
Free tier         ✅   ❌   ✅   ❌
```

### Step 3: Analyze competitor reviews

This is where you find gold — what their customers complain about is your opportunity.

**Paste this into Claude Code:**
```
Find and analyze reviews for [Competitor A] on the App Store, G2, or Capterra. What are their users complaining about most? What do they praise? What unmet needs can you identify?

Visualize the key complaint themes using ASCII bar charts, and highlight:
- Complaints we could solve better
- Praise we should match or beat
- Gaps in the market nobody is filling
```

**What you should see:** A breakdown of competitor weaknesses backed by their own users' words. This is ammunition for positioning, feature planning, and sales enablement.

### Step 4: Generate the competitive brief

**Paste this into Claude Code:**
```
Create a one-page competitive brief I can share with my team. Structure it as:

## Market Overview
[2-3 sentences on the competitive landscape]

## Competitor Profiles
[One paragraph each — who they are, who they serve, what they're good at]

## Our Advantages
[Where we win and why — be specific]

## Our Vulnerabilities
[Where competitors beat us — be honest]

## Strategic Recommendations
[3 concrete actions based on this analysis]

## Key Quotes from Competitor Reviews
[Pull the most insightful competitor user quotes]

Be direct. No marketing fluff — this is for internal strategy.
```

**What you should see:** A structured competitive brief you'd actually share with your leadership team. The kind of document that usually takes a half-day of research compressed into a 15-minute conversation.

## 🎉 What Just Happened

You just ran a systematic competitive analysis without opening a single browser tab yourself. Claude searched the web, visited competitor sites, analyzed their positioning, and synthesized everything into a structured brief. The 2x2 matrix, feature comparison, and review analysis are the same frameworks consultants charge thousands to produce — you got them in minutes.

The real power: you can re-run this quarterly. Markets shift, competitors launch new features, reviews accumulate. A competitive analysis that's 6 months old is nearly useless. One you can regenerate in 15 minutes? That's a strategic advantage.

## Go Deeper

- **Deep dive on one competitor:** Pick your scariest competitor and ask Claude to analyze their last 6 months of changelog/release notes. What direction are they heading?
- **Pricing analysis:** Ask Claude to map all competitor pricing tiers and identify where there's pricing power or whitespace
- **Win/loss analysis:** Paste notes from recent sales calls and ask Claude to identify patterns in why you win or lose deals against specific competitors
- **Porter's Five Forces:** Ask Claude to run a full Porter's analysis on your market — it's a classic framework that's tedious to do manually but perfect for AI

## Share

**Bring back:** Your 2x2 positioning map. Where did Claude place you vs. competitors — and do you agree with the axes it chose?
