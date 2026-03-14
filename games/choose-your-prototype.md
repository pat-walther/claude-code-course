# 🎮 Choose Your Own Prototype

> **Magic Moment:** You build a fully working prototype in under 15 minutes — and survive a last-minute "can it also do X?" curveball from the CEO.

```
    ╔═══════════════════════════════════════════╗
    ║                                           ║
    ║   📱  INCOMING CALL: Board of Directors   ║
    ║                                           ║
    ║   "The board meeting moved up."           ║
    ║   "You have 2 hours."                     ║
    ║   "We need something to show."            ║
    ║                                           ║
    ║           [ Accept Call 📞 ]               ║
    ║                                           ║
    ╚═══════════════════════════════════════════╝
```

## The Setup

You're a PM at a Series A startup called **Stackwise**. It's 10:00 AM on a Tuesday. You just got the Slack message every PM dreads:

> **@CEO:** Board meeting moved to noon. They want to see the product direction. Can you throw something together? Doesn't need to be perfect. Just needs to be real.

Two hours. No engineering sprint. No design handoff. Just you and Claude Code.

**What are you going to build?**

## Before You Start

- Claude Code installed and running (complete [Lesson 1](../lessons/01-setup.md) first if you haven't)
- Create a fresh folder for this game: ask Claude to `create a folder called "board-demo" and navigate into it`
- 10–15 minutes of uninterrupted time

## Choose Your Path

You stare at Slack. The cursor blinks. You need to pick a direction — fast.

| Path | What You'll Build | Time | Skills |
|------|-------------------|------|--------|
| **[Path A](#path-a-the-dashboard)** | Customer Analytics Dashboard | ~12 min | Data viz, layout, interactivity |
| **[Path B](#path-b-the-landing-page)** | Product Launch Page | ~10 min | Design, copywriting, responsive layout |
| **[Path C](#path-c-the-internal-tool)** | Team Productivity Tool | ~12 min | Forms, data handling, CRUD |

**Pick one and jump to that section. You can always come back and try the others.**

---

# Path A: The Dashboard

*You decide to show the board that you know your numbers. A customer analytics dashboard will prove the team understands the data — and has the tooling to act on it.*

> **Slack to CEO:** "I'll have a customer analytics dashboard ready by noon."
>
> **CEO:** "👍 Make it look like we know what we're doing."

---

### A1: The Foundation

**Context for Claude:** You're building a customer analytics dashboard for a SaaS startup. It needs to look real enough for a board meeting.

**Paste this into Claude Code:**
```
Build a customer analytics dashboard as a single HTML file. Include:
- A header with the company name "Stackwise" and today's date
- 4 metric cards at the top: Total Customers (2,847), MRR ($142,350), Churn Rate (3.2%), NPS Score (72)
- A line chart showing monthly revenue growth over the past 12 months (make up realistic SaaS numbers starting around $80k and growing to $142k)
- A table of the top 10 customers by revenue with columns: Company Name, Plan, MRR, Status
- Use a clean, modern design with a white background and blue accent color
- Use Chart.js loaded from a CDN for the chart
Make it look polished — this is for a board meeting. Open it in my browser.
```

**What you should see:** A complete dashboard opens in your browser. Metric cards up top, chart in the middle, table at the bottom. It should look like a real product.

⚠️ **If the chart doesn't render:** This sometimes happens if Chart.js CDN is slow. Ask Claude: "The chart isn't showing. Can you check the Chart.js import and fix it?" — this is a real debugging moment.

---

### A2: Make It Interactive

The static dashboard is good. But boards love clicking things.

**Paste this into Claude Code:**
```
Update the dashboard to add interactivity:
- Make the metric cards clickable — when you click one, it highlights and shows a small tooltip with a trend (e.g., "↑ 12% from last month")
- Add a dropdown filter above the customer table that lets you filter by plan type (Starter, Growth, Enterprise)
- Make the table rows highlight on hover
- Add a subtle animation when the page loads (cards fade in one by one)
```

**What you should see:** Refresh the page. Click a metric card — you should see a tooltip. Use the dropdown — the table filters. Hover over table rows — they highlight. The cards should fade in on load.

---

### A3: The Plot Twist 🔀

Your phone buzzes. It's the CEO again.

> **CEO:** "Actually, the lead investor is really into cohort analysis. Can you add a cohort retention chart? You know, the triangle-shaped one where each row is a monthly cohort and the cells show retention percentages? Color-coded would be 🔥"
>
> *Read: 10:47 AM*

Classic. Scope creep, 73 minutes before the meeting.

**Paste this into Claude Code:**
```
The CEO wants a cohort retention analysis added to the dashboard. Add a new section below the revenue chart with:
- A title "Cohort Retention Analysis"
- A triangular cohort retention table showing 6 monthly cohorts
- Each row is a cohort (Jan 2025 through Jun 2025), columns are Month 0 through Month 5
- Month 0 is always 100%, then realistic SaaS retention numbers (dropping to around 70-80% by Month 5)
- Color-code the cells: green for >80%, yellow for 60-80%, red for <60%
- Make it look like it belongs with the rest of the dashboard
```

**What you should see:** A color-coded cohort retention table appears below the revenue chart. Green, yellow, and red cells forming the classic triangular pattern. This is the kind of thing that takes hours in a spreadsheet — you just added it in one prompt.

---

### A4: The Polish

The board will see this on a projector. Time to make sure it's presentation-ready.

**Paste this into Claude Code:**
```
Final polish for the board meeting:
- Add a subtle dark mode toggle in the top-right corner (boards love dark mode on projectors)
- Put a "Last updated: [today's date and time]" footer
- Make sure everything is responsive — it should look good on a laptop screen and a projector
- Add the Stackwise tagline under the logo: "Data-driven growth for modern teams"
```

**What you should see:** A polished, professional dashboard with dark mode toggle. Click it. Everything should look great in both modes. This is board-ready.

---

### A5: Present It

**The board meeting is starting. Open your dashboard in the browser. Full screen it.**

Take a screenshot. You just built a presentation-ready analytics dashboard from scratch. No Figma. No engineering ticket. No sprint planning.

**How long did that take?** Check the time.

**➡️ Now jump to [The Debrief](#the-debrief)**

---

# Path B: The Landing Page

*You decide to show the board where the product is headed. A new landing page will demonstrate vision, positioning, and that you can execute without waiting for the design team.*

> **Slack to CEO:** "I'll have a product landing page ready. New positioning, new look."
>
> **CEO:** "Ooh. Bold. Do it."

---

### B1: The Foundation

**Context for Claude:** You're building a landing page for Stackwise, a SaaS analytics platform. This needs to look like a real startup's website.

**Paste this into Claude Code:**
```
Build a product landing page for "Stackwise" as a single HTML file. Stackwise is a SaaS analytics platform that helps growing startups understand their customers.

Include these sections:
- Hero section with a bold headline "Stop Guessing. Start Growing.", a subtitle explaining the product, and a "Start Free Trial" CTA button
- Social proof bar: "Trusted by 500+ startups" with fake logos (use styled text as placeholders: "TechCorp", "ScaleUp", "DataFlow", "CloudBase", "GrowthKit")
- 3-column features section with icons (use emoji): 📊 Real-time Analytics, 🎯 Customer Segmentation, 🔮 Predictive Insights
- Each feature gets a short paragraph description
- A pricing section with 3 tiers: Starter ($29/mo), Growth ($99/mo), Enterprise (Custom)
- A footer with fake links

Use a modern gradient hero (dark blue to purple), clean white sections, and professional typography. Open it in my browser.
```

**What you should see:** A full landing page that looks like it was designed by a professional. Hero with gradient, social proof bar, feature cards, pricing table, footer. If you showed this to someone, they'd think it was a real product page.

---

### B2: Make It Scroll

Good landing pages tell a story. Let's add storytelling.

**Paste this into Claude Code:**
```
Enhance the landing page:
- Add smooth scroll animations — sections should fade in as you scroll down to them
- Add a "How It Works" section between features and pricing with 3 numbered steps: 1) Connect your data, 2) Get instant insights, 3) Act on recommendations
- Add a testimonial section with 3 fake customer quotes in cards, each with a name, title, and company
- Make the "Start Free Trial" button have a subtle pulse animation to draw attention
- Add a sticky navigation bar at the top that appears when you scroll past the hero
```

**What you should see:** Scroll down the page. Sections fade in. The nav sticks to the top. The CTA pulses gently. Testimonials look real. This is conversion-optimized design — built from a text prompt.

---

### B3: The Plot Twist 🔀

Your phone buzzes. It's the CEO.

> **CEO:** "The board's been talking about AI. EVERYTHING has to be about AI now. Can you make the page more... AI-forward? Maybe add a demo section that shows a fake AI chat interface? Something interactive. Don't worry about it actually working — it just needs to LOOK like it works."
>
> *Read: 10:52 AM*

Every PM has lived this moment. The strategy pivot, 68 minutes before the meeting.

**Paste this into Claude Code:**
```
The CEO wants the landing page to be more AI-focused. Make these changes:
- Update the hero headline to: "Your AI-Powered Growth Engine"
- Update the subtitle to mention AI-driven analytics
- Add a new section called "See the AI in Action" that contains a fake chat interface:
  - A dark chat window with rounded corners
  - 3 pre-written messages showing a conversation:
    - User: "Why did churn spike last month?"
    - AI (with a ✨ icon): "Churn increased 2.1% in March, primarily driven by the Starter plan segment. 73% of churned users hadn't used the segmentation feature. Recommendation: trigger an onboarding email for Starter users in week 2."
    - User: "Create a segment of at-risk users"
    - AI: "Done. Created segment 'At-Risk Starter Users' with 142 accounts. Want me to draft a re-engagement email?"
  - A fake input field at the bottom with placeholder text "Ask your data anything..."
  - Make it look like a real chat interface
- Rename the "Predictive Insights" feature to "AI Copilot" with a new description
```

**What you should see:** The page now screams "AI-first product." The fake chat demo looks convincing. If the board squints at the projector, they'll think it's real. That's all you need.

---

### B4: Mobile Check

Board members will pull this up on their phones. Let's make sure it doesn't look broken.

**Paste this into Claude Code:**
```
Make sure the landing page is fully responsive:
- On mobile, stack the feature columns vertically
- Make the pricing cards stack on small screens
- Ensure the fake chat interface looks good on mobile
- Make the sticky nav collapse into a hamburger menu on mobile
- Test by making the browser window narrow — everything should reflow cleanly
Add a subtle "Built with ❤️ by the Stackwise team" at the very bottom.
```

**What you should see:** Resize your browser window narrow. Everything stacks and reflows. The hamburger menu appears. It looks like a real responsive website.

---

### B5: Present It

**The board meeting is starting. Open your landing page in the browser. Full screen it.**

Scroll through it top to bottom. Take a screenshot of the hero section. You just built a complete, responsive, AI-focused product landing page.

**How long did that take?** Check the time.

**➡️ Now jump to [The Debrief](#the-debrief)**

---

# Path C: The Internal Tool

*You decide to show the board that the team is operationally excellent. An internal productivity tool proves you're building systems, not just features.*

> **Slack to CEO:** "I'll have an internal tool ready — something the team can actually use starting today."
>
> **CEO:** "Practical. I like it. What kind of tool?"
>
> **You:** "Feature request tracker. We get requests from everywhere — Slack, email, support tickets. This puts them all in one place."
>
> **CEO:** "Ship it."

---

### C1: The Foundation

**Context for Claude:** You're building a feature request tracker that the team can use to collect, prioritize, and manage product feature requests.

**Paste this into Claude Code:**
```
Build a feature request tracker as a single HTML file with embedded JavaScript. This is an internal tool for a product team.

Include:
- A header with "Stackwise Feature Tracker" and a "New Request" button
- A form that appears when you click "New Request" with fields: Title, Description, Requested By (dropdown: Customer, Sales, Engineering, Support, CEO), Priority (dropdown: Low, Medium, High, Critical), and a Submit button
- A table showing all submitted requests with columns: Title, Requested By, Priority, Status (New/In Review/Planned/Done), Date Added
- Pre-populate 5 fake feature requests so it doesn't look empty
- Store all data in the browser's localStorage so it persists across refreshes
- Clean, professional design — this should look like a real internal tool
Open it in my browser.
```

**What you should see:** A working feature tracker with 5 pre-loaded requests. Click "New Request" and the form appears. Fill it out and submit — it shows up in the table. Refresh the page — your data is still there. That's persistence, built from a single prompt.

---

### C2: Make It Useful

A table is fine. A useful table is better.

**Paste this into Claude Code:**
```
Enhance the feature tracker:
- Add a status dropdown in each table row so you can change a request's status directly in the table (New → In Review → Planned → Done)
- Color-code the priority: Critical = red, High = orange, Medium = yellow, Low = gray
- Add sorting — click any column header to sort by that column
- Add a search bar that filters the table in real-time as you type
- Add a count at the top: "Showing X of Y requests"
- When status changes to "Done", the row should get a subtle strikethrough and fade slightly
```

**What you should see:** Click column headers — the table sorts. Type in the search bar — it filters. Change a status dropdown to "Done" — the row fades. This is a real, functional CRUD app.

---

### C3: The Plot Twist 🔀

Your phone buzzes. It's the CEO. Of course it is.

> **CEO:** "Love the tracker. Quick question though. Can you add voting? Like, people can upvote feature requests? And maybe a chart that shows which category has the most requests? The board loves charts. LOVES them."
>
> *Read: 10:49 AM*

"Quick question" that's two features. Classic.

**Paste this into Claude Code:**
```
The CEO wants voting and charts added. Update the feature tracker:
- Add a 👍 upvote button to each row. Clicking it increments a vote count. Store votes in localStorage too
- Sort by votes by default (most voted at top)
- Add a sidebar (or section above the table) with two small charts:
  1. A bar chart showing request count by source (Customer, Sales, Engineering, Support, CEO)
  2. A pie chart showing requests by priority level
- Use Chart.js from CDN for the charts
- The charts should update automatically when new requests are added
```

**What you should see:** Vote buttons on each row. Click them — the count goes up and the row reorders. Two charts appear showing the distribution. Add a new request — the charts update. This is genuinely useful software.

---

### C4: The Export

Board members will want data, not just a demo. Let's make it exportable.

**Paste this into Claude Code:**
```
Add data management features:
- An "Export CSV" button that downloads all feature requests as a spreadsheet
- An "Export Report" button that generates a clean summary page showing: total requests, breakdown by priority, breakdown by source, top 5 most-voted features, and the charts — formatted for printing
- A "Clear Done" button that removes all completed requests (with a confirmation dialog)
- Add keyboard shortcuts: Ctrl+N for new request, Ctrl+E for export
```

**What you should see:** Click "Export CSV" — a file downloads. Click "Export Report" — a clean summary page opens. Try the keyboard shortcuts. This tool has more features than some production SaaS apps.

---

### C5: Present It

**The board meeting is starting. Open your feature tracker in the browser. Full screen it.**

Add a feature request live: "Board Presentation Tool — build prototypes faster." Upvote it. Watch the charts update. Take a screenshot.

**How long did that take?** Check the time.

**➡️ Now jump to [The Debrief](#the-debrief)**

---

# The Debrief

## ⏱️ How'd You Do?

| Your Time | Rating |
|-----------|--------|
| Under 8 min | 🏆 **Shipped It Before The Meeting** |
| 8–12 min | 🥇 **Board-Ready** |
| 12–18 min | 🥈 **Made the Deadline** |
| 18+ min | 🥉 **Better Than a Slide Deck** |

## 🎉 What Just Happened

No matter which path you chose, you just built a **working prototype from scratch** using only plain English prompts. Let's break down what you actually learned:

### Skills Every Path Taught You

| Skill | What It Looked Like |
|-------|-------------------|
| **Generating complete apps** | You described what you wanted, Claude built the whole thing — HTML, CSS, JavaScript, all in one go. |
| **Iterating on existing code** | You didn't start over each time. You told Claude to *modify* what it already built. It remembered the context. |
| **Handling scope changes** | The CEO threw a curveball. You didn't panic. You just described the new requirement and Claude adapted. |
| **Progressive enhancement** | You started simple and added complexity step by step. Each prompt built on the last. |
| **Describing UI in words** | You learned to translate visual ideas into text descriptions. This is the core skill of working with AI. |

### The PM Superpower

Here's what really happened today: you experienced the future of product management. The gap between "I have an idea" and "here's a working prototype" just collapsed from weeks to minutes.

You didn't need to:
- ❌ File a Jira ticket
- ❌ Wait for a design sprint
- ❌ Schedule an engineering review
- ❌ Attend a standup about it

You just... **built it.**

## Path-Specific Takeaways

**If you did Path A (Dashboard):** You learned that data visualization — the thing that usually requires a BI tool, a data team, and 3 meetings — can be prototyped from a text description. Next time someone asks "can you pull some metrics together?", you know the answer is yes, and it takes 12 minutes.

**If you did Path B (Landing Page):** You learned that marketing pages — the thing that usually requires a designer, a copywriter, and a developer — can be prototyped end-to-end by describing what you want. Next time marketing needs a quick page, you're the one who builds it.

**If you did Path C (Internal Tool):** You learned that internal tools — the things that "never get prioritized" because engineering is busy with customer features — can be built by you, right now. Next time your team needs a tracker, a calculator, or a dashboard, you don't need to beg for engineering time.

## Try Another Path

**That was just one path. There are two more.**

Go back to the [path selection](#choose-your-path) and pick a different letter. Each path teaches different skills and builds a completely different prototype. All three together take about 35 minutes.

## Go Deeper

- **Combine paths:** Ask Claude to merge two of your prototypes into one mega-app
- **Make it real:** Take one of your prototypes and iterate on it until it's actually usable by your team
- **Get ambitious:** Ask Claude to add user authentication, a database backend, or API integration to any prototype
- **Break things:** Intentionally make a bad prompt and see how Claude handles ambiguity. Then learn to give better prompts.

## Share

**Bring back:** A screenshot of your prototype. Tell the cohort which path you chose and how long it took. Bonus: share the "plot twist" prompt and what Claude did with it.
