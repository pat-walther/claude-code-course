# 📋 Product Brief B: StandupBot — Async Team Standup Tool

## The Problem
Daily standup meetings waste 15 minutes of everyone's morning. Half the team zones out while one person talks. Remote teams do them over Zoom, which is even worse — awkward silences, "you're on mute," and no one remembers what was said. We need async standups that take 60 seconds to post and 2 minutes to read.

## The Product
**StandupBot** — an async standup board where team members post their daily update (yesterday / today / blockers) and everyone can read the whole team's status at a glance. No meetings required.

## Target User
Engineering and product teams (5-15 people) at startups who are tired of daily standup meetings but still need visibility into what everyone's working on.

## Core Features
1. **Standup form** — Three simple text fields: "What I did yesterday," "What I'm doing today," "Any blockers?" with a Submit button
2. **Team board** — A card-based view showing everyone's standup for today, newest first
3. **Team member avatars** — Each update shows a name, avatar (emoji or initials), and timestamp
4. **Blocker highlight** — If someone has a blocker, their card gets a red border and a 🚨 icon so it's immediately visible
5. **Status indicator** — Show who has posted today vs. who hasn't yet (green dot / gray dot next to names)

## Design Direction
- Professional but not boring — think Notion or Linear aesthetics
- Dark mode preferred (developers love it)
- Dense information display — this is a dashboard, not a landing page
- Clean typography, monospace accents for timestamps
- Vibe: "The anti-meeting" — efficient, respectful of everyone's time

## Out of Scope (for this prototype)
- Real user accounts or authentication
- Backend/database (hardcode 3-4 sample team members with realistic data)
- Slack/Teams integration
- Historical standup archives
- Comments or reactions on standups

## Success Criteria
A team lead should be able to:
1. See the whole team's status for today in one glance
2. Immediately spot who has blockers
3. Know who hasn't posted yet
...without scrolling.

---

*Ship the thing that kills the meeting. Your team's mornings depend on it.* ☕
