# 15. Turn Raw Reviews Into Product Strategy

> **Magic Moment:** You paste 20+ messy, unstructured app reviews and Claude produces a prioritized product strategy — with themes, severity scores, and specific recommendations — in under 60 seconds.

## Why This Matters

You have feedback. Probably too much of it. App store reviews, support tickets, survey responses, Slack messages from the sales team — it's everywhere, and nobody has time to read all of it, let alone synthesize it into something actionable. Claude turns that pile of raw signal into a structured strategy you can bring to your next planning session.

## Before You Start

- Claude Code open in your terminal
- Either: your own customer feedback (reviews, tickets, survey responses), OR the Walmart dataset we'll download below
- 15 minutes

## Do This Now

### Step 1: Get some feedback data

**Option A — Use the Walmart dataset (recommended for practice):**

Download a public dataset of Walmart app reviews from Kaggle. This gives you thousands of real reviews to work with.

**Paste this into Claude Code:**
```
Search for and download the Walmart app reviews dataset from Kaggle. If you can't download it directly, find a publicly available app review CSV dataset and save it to this directory. Name it walmart-reviews.csv
```

**What you should see:** Claude downloads or creates a CSV file with columns like review text, rating, date, etc.

**Option B — Use your own data:**

Grab your last 20+ reviews, support tickets, or survey responses. Raw is fine — don't clean them up. Copy-paste them directly into the next step.

💡 **Where to find your reviews:** App Store Connect → Ratings and Reviews, Google Play Console → Reviews, Zendesk → export tickets, Intercom → export conversations, or even just copy-paste from your app's store page.

### Step 2: Run the initial analysis

**Paste this into Claude Code (use ask mode so it doesn't defer to writing code):**
```
Help me analyze this dataset. I want to see the data visualized in 3 different ways using ASCII with a summary of takeaways at the top, within this chat. Do not generate code.

From this data, tell me:
1. Top 3 themes — what are people praising?
2. Top 3 complaints — what keeps coming up as problems?
3. Any surprising patterns you didn't expect?
4. What should I prioritize fixing based on this?

Quote specific pieces of feedback to support each finding.
```

If you're using your own feedback instead of the CSV, paste it right after the prompt.

**What you should see:** Claude produces something like this:

```
═══════════════════════════════════════════════
           CUSTOMER FEEDBACK ANALYSIS
═══════════════════════════════════════════════

📊 SENTIMENT DISTRIBUTION
██████████████████░░ 72% Negative (1-2 stars)
████░░░░░░░░░░░░░░░ 15% Neutral  (3 stars)
███░░░░░░░░░░░░░░░░ 13% Positive (4-5 stars)

🔥 TOP COMPLAINTS BY FREQUENCY
App crashes/freezing  ████████████████ 34%
Login issues          ██████████░░░░░░ 22%
Slow performance      ████████░░░░░░░░ 18%
Missing features      ████░░░░░░░░░░░░ 11%

💚 TOP PRAISE THEMES
Easy to use           ████████████░░░░ 45%
Good deals/savings    ████████░░░░░░░░ 32%
Wide selection        ██████░░░░░░░░░░ 23%
```

Three different ASCII visualizations, right in your terminal. No Jupyter. No Tableau. No data science degree.

### Step 3: Go deeper — build a product strategy

Now ask Claude to turn insights into action:

**Paste this into Claude Code:**
```
Based on this analysis, create a product strategy brief. For each theme:

1. Severity (Critical / High / Medium / Low)
2. Estimated user impact (what % of users are affected)
3. Specific recommendation (what would you build/fix)
4. Evidence (quote 2-3 actual reviews)
5. Quick win vs. strategic investment

Format it as a prioritized table I could bring to a sprint planning meeting.
```

**What you should see:** A structured table with actionable recommendations, severity levels, and direct quotes from your users backing up each recommendation. This is the kind of output that usually takes a PM a full afternoon to compile.

### Step 4: Challenge it with your roadmap

Here's where it gets really interesting. Follow up with:

**Paste this into Claude Code:**
```
Here's what's currently on our roadmap: [paste your roadmap items, or describe your top 3-5 priorities]

Compare what customers are asking for vs. what we're building. Are we working on the right things? What's on the roadmap that nobody asked for? What are customers screaming about that we're ignoring?
```

**What you should see:** Claude maps customer demand against your planned work and highlights the gaps. This is the conversation you should be having with your team — and now you have the data to back it up.

## 🎉 What Just Happened

You just did in 5 minutes what normally takes a PM half a day: read through dozens (or hundreds) of reviews, identified patterns, categorized by severity, and produced a strategy brief with evidence. Claude processed the unstructured text, found semantic patterns across reviews (not just keyword matching), and organized them into a framework you can actually use in a meeting.

The key insight: you didn't need to clean the data, export to a spreadsheet, or tag anything manually. Raw feedback in, prioritized strategy out.

## Go Deeper

- **Sentiment over time:** Ask Claude to chart sentiment trends by week/month — is your product getting better or worse?
- **Competitor comparison:** Paste your competitor's reviews alongside yours — where are they beating you?
- **Auto-categorize:** Have Claude create tags for each review, then export as a CSV you can import back into your tracking tool
- **The "so what" test:** After every analysis, ask "If I showed this to my CEO, what would they ask next?" Then answer that question too

## Share

**Bring back:** The #1 complaint theme Claude found in your feedback. Is it already on your roadmap? If not — should it be?
