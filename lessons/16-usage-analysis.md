# 16. Data Analysis Without SQL

> **Magic Moment:** You hand Claude a CSV export and it produces charts, trends, and actionable insights — no SQL, no Jupyter, no data science degree required.

## Why This Matters

Every PM has a moment where they need to answer a data question and the analytics team is booked for two weeks. You know the data exists — maybe in a CSV export, a Google Analytics dump, or a Mixpanel report — but turning raw numbers into "here's what we should do" requires tools you don't use daily. Claude eliminates that gap. Give it data, ask questions in plain English, get answers with visualizations.

## Before You Start

- Claude Code open in your terminal
- A CSV or data export from any tool you use (see Step 1 for how to get one)
- 15 minutes

## Do This Now

### Step 1: Export your data

You need a CSV. Here's how to get one from common tools:

| Tool | How to export |
|------|--------------|
| **Google Analytics** | Reports → Export → CSV |
| **Mixpanel** | Insights → Download CSV |
| **Amplitude** | Any chart → Export → CSV |
| **PostHog** | Trends → Export CSV |
| **Stripe** | Payments → Export |
| **App Store Connect** | Sales and Trends → Download |
| **Spreadsheet** | File → Download → CSV |

Save the file somewhere you can find it. If you're already in a project directory, drop it there.

💡 **No data to export?** No problem. You can ask Claude to generate a realistic sample dataset:

**Paste this into Claude Code:**
```
Create a sample product usage CSV with 200 rows. Include columns for: user_id, signup_date, last_active_date, plan_type (free/pro/enterprise), sessions_last_30_days, features_used, country, referral_source. Make the data realistic — include some churned users, power users, and everything in between. Save it as usage-data.csv
```

### Step 2: Run the analysis

**Paste this into Claude Code:**
```
Read the file usage-data.csv (or whatever your file is named).

Analyze this data and tell me:
1. Which features are getting the most use?
2. Where do users seem to drop off or disengage?
3. What does the data suggest about what users actually care about vs. what we think they care about?
4. What's the one metric I should be watching most closely?

Visualize the key findings using ASCII charts directly in this chat. Do not generate code or open external tools.
```

**What you should see:** Something like this:

```
═══════════════════════════════════════════════
          USAGE ANALYSIS — KEY FINDINGS
═══════════════════════════════════════════════

📊 SESSIONS BY PLAN TYPE (last 30 days)
Enterprise  ██████████████████████ 22.4 avg
Pro         ████████████░░░░░░░░░ 12.1 avg
Free        ████░░░░░░░░░░░░░░░░░  4.3 avg

📉 DROP-OFF PATTERN
Week 1      ████████████████████ 100% active
Week 2      ████████████████░░░░  78%
Week 3      ██████████░░░░░░░░░░  52%
Week 4      ███████░░░░░░░░░░░░░  34%
             ↑ Biggest drop: Week 2→3 (-26%)

🌍 TOP ENGAGEMENT BY COUNTRY
US          ████████████████████ 45%
UK          ████████░░░░░░░░░░░░ 18%
Canada      █████░░░░░░░░░░░░░░░ 12%
Germany     ████░░░░░░░░░░░░░░░░  9%
```

Three visualizations, key insight at the top, all in your terminal. No chart library required.

### Step 3: Ask follow-up questions

This is where it gets powerful. You don't need to re-export or re-query — just keep talking:

**Try these follow-ups:**
```
Compare usage from this month vs. last month. What changed?
```

```
Which user segment is most engaged? What do they have in common?
```

```
If I had to cut 3 features based on usage data, which would you cut and why?
```

```
What does the data say about our free-to-paid conversion? What's the typical journey?
```

**What you should see:** Claude digs deeper into the same dataset, cross-references different dimensions, and gives you increasingly specific insights. Each follow-up builds on the context of the conversation.

### Step 4: Turn insights into a recommendation

**Paste this into Claude Code:**
```
Based on everything we've analyzed, write a 1-page data brief I could share with my team. Include:

1. Executive summary (3 sentences)
2. Key metrics with trends (up/down arrows)
3. The one thing we should start doing
4. The one thing we should stop doing
5. The one thing we should investigate further

Keep it tight — no fluff, just signal.
```

**What you should see:** A crisp, stakeholder-ready summary that turns your raw CSV into a document you'd actually share in a team meeting.

## 🎉 What Just Happened

You just did a full data analysis cycle — import, explore, visualize, and recommend — without opening a single analytics tool. Claude read your CSV, understood the structure, identified patterns across dimensions (time, segments, features), and produced both visualizations and recommendations.

The important part: you asked questions in plain English. "Where do users drop off?" is a natural question. Normally answering it requires SQL, a BI tool, and 30 minutes of query-building. With Claude, it's a conversation.

## Go Deeper

- **Connect to live analytics:** If you have PostHog, Amplitude, or Mixpanel MCP servers installed, Claude can query your data directly — no CSV export needed. Ask: `analyze my usage data from PostHog`
- **Cohort analysis:** Ask Claude to compare user cohorts: "How do users who signed up in January behave differently from March signups?"
- **Funnel analysis:** Describe your funnel steps and ask Claude to calculate conversion rates between each step
- **Predictive questions:** "Based on these trends, what does next month look like?" — Claude won't predict the future, but it can extrapolate patterns and flag risks

## Share

**Bring back:** One finding from your usage data that surprised you or confirmed something you suspected but couldn't prove until now.
