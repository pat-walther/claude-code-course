# 📋 Product Brief C: EchoWall — Customer Feedback Wall

## The Problem
Customer feedback is scattered across Intercom, email, Twitter, support tickets, and Slack. PMs spend hours every week hunting for patterns. By the time they find a theme ("everyone hates the new navigation"), they've already shipped three more things nobody asked for. Teams need a single wall where all feedback is visible, sortable, and actionable.

## The Product
**EchoWall** — a visual feedback board where customer quotes get pinned like sticky notes, tagged by theme, and voted on by the team. Think of it as a "voice of the customer" dashboard that lives in one place.

## Target User
Product managers and customer success teams at B2B SaaS companies who receive 50+ pieces of feedback per week and struggle to prioritize what to build next.

## Core Features
1. **Feedback cards** — Each card shows: customer quote, customer name/company, source (email/chat/Twitter), date, and sentiment tag (😍 Love / 😐 Meh / 😤 Frustrated)
2. **Theme tags** — Color-coded tags like "Onboarding," "Pricing," "Mobile," "Performance" that you can filter by
3. **Upvote system** — Team members can upvote feedback cards to signal "we're hearing this a lot"
4. **Add new feedback** — A form to paste in a new customer quote with source and sentiment
5. **Filter bar** — Filter by sentiment, theme, or date range. Show a count: "Showing 12 of 47 items"

## Design Direction
- Masonry / Pinterest-style card grid layout
- Colorful — each sentiment gets a distinct color (green for love, yellow for meh, red for frustrated)
- Slight tilt/rotation on cards for a "sticky note on a wall" feel
- Big, readable customer quotes — the words are the hero, not the UI chrome
- Vibe: "Design thinking workshop wall, but digital"

## Out of Scope (for this prototype)
- Real data or API connections
- User authentication
- Export to CSV/Jira
- AI-powered theme detection
- Comments or threading on cards

## Sample Data (use these)
Pre-populate with 8-10 realistic feedback cards:
- Mix of sentiments (4 frustrated, 3 love, 3 meh)
- Different sources (email, Intercom, Twitter, Slack)
- Different themes (at least 3 different tags)
- Real-sounding customer quotes (not "Lorem ipsum")

## Success Criteria
A PM should be able to:
1. Scan the wall and immediately see the dominant sentiment
2. Filter to "frustrated" feedback and spot patterns
3. Add a new quote from a customer call they just had
...in under 30 seconds.

---

*Build the wall your PM team wishes they'd had six months ago.* 🧱
