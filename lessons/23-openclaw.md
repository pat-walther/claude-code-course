# 23. OpenClaw — Your 24/7 AI Chief of Staff

> **Magic Moment:** You realize Claude Code can run 24/7 on your machine, controlled from your phone via Signal or WhatsApp, with full memory of who you are — and see what that actually looks like in practice.

## Why This Matters

Right now, you're the middleware. You open Claude, load context, run prompts, copy results somewhere else, close your laptop, and the work stops. OpenClaw removes you from the loop for the parts that don't need you. It runs Claude on your machine around the clock, remembers everything, browses the web, runs your skills automatically, and reports back to your phone. Imagine texting your AI "what happened with our competitor's pricing page today?" and getting an answer — because it already checked.

## Before You Start

- Everything from lessons 21 and 22 (USER.md, SOUL.md, and at least one skill)
- A Mac (OpenClaw currently runs on macOS)
- Signal, WhatsApp, or Telegram installed on your phone
- An Anthropic API key (for Claude Code access)
- 20 minutes for setup (or just read through to understand what's possible)

⚠️ **Honest note:** OpenClaw is an advanced setup. Most students in this cohort won't install it today — and that's fine. This lesson is about understanding what's possible so you know where you're headed. If you do want to set it up, the steps are here.

## Do This Now

### Step 1: Understand what OpenClaw actually is

OpenClaw is open-source software that wraps Claude Code into a persistent service. Instead of opening a terminal, you message it from your phone. Instead of re-explaining your context, it reads your USER.md and memory files automatically. Instead of closing when you close your laptop, it keeps running.

Here's what it replaces:

| Before (you as middleware) | After (OpenClaw) |
|---|---|
| Open laptop → open Claude → explain context → get answer → paste somewhere | Text from your phone → get answer with full context |
| Close laptop → work stops | Work continues 24/7 |
| "Remember that thing from last week?" → re-explain | Already remembers — it wrote it down |
| Run the same analysis every Monday | Scheduled to run automatically, results sent to your phone |

📱 Real example: Eric runs his entire company through chat messages — deploys, code reviews, content pipelines. All from Signal, no laptop required.

### Step 2: The four capabilities

OpenClaw gives Claude four superpowers that regular Claude Code doesn't have:

**1. Remember everything**
It loads your full history at the start of every conversation. Your product, your team, your decisions, your writing style. Set it up once — it stays set up. This is your USER.md, SOUL.md, and AGENTS.md from Lesson 21, plus a `memory/` folder that grows over time.

**2. Use the web**
It controls a real browser. Visit pages, fill out forms, click buttons, scrape data, take screenshots. Ask it to monitor a competitor's pricing page and tell you when it changes. It will.

**3. Run skills automatically**
Your skills from Lesson 22 work here too. When you ask OpenClaw to "write release notes" or "analyze this feedback," it loads the right skill automatically. Every time, same quality.

**4. Work while you sleep**
Schedule anything on a timer. Morning competitive digest delivered to your phone. Weekly analytics summary every Monday. OpenClaw wakes up, does the work, and reports back.

### Step 3: Control it from chat

No app to open. No config to edit. Everything from the chat window.

- `/new` — fresh conversation, full memory intact
- `/compact` — clears working memory when it gets too full, keeps the important stuff
- `/model opus` — switch to the most powerful model for hard problems
- `/think high` — turns on deeper reasoning before it answers
- `/status` — see what model you're on, how much you've used, session cost

### Step 4: The three config files

OpenClaw is configured with the same files you already built:

- **SOUL.md** — its personality and writing style. This is what kills AI slop: no filler phrases, no corporate speak. You define the voice.
- **USER.md** — who you are. Name, job, timezone, communication style, tech stack. Loaded every session so it never asks twice.
- **AGENTS.md** — workspace rules. How it handles decisions, when to ask for approval, what it's allowed to do on its own.

You already wrote these in Lesson 21. They work identically in OpenClaw.

### Step 5: Getting started (if you want to install it today)

1. **Clone the repo:** Visit [github.com/clawdbot/clawdbot](https://github.com/clawdbot/clawdbot) and follow the setup instructions
2. **Connect your messaging app:** Link Signal, WhatsApp, or Telegram so you can chat from your phone
3. **Add your config files:** Copy your USER.md, SOUL.md, and AGENTS.md into the workspace
4. **Write your first skill:** Or copy one from the [ClawdHub skills library](https://clawdhub.com)
5. **Set up one cron job:** Even just a daily summary to see the magic of scheduled work

**Paste this into Claude Code (once OpenClaw is running):**
```
Set up a daily cron job that runs every morning at 8am. It should:
1. Check my calendar for today's meetings
2. Summarize any unread important emails
3. List my top 3 priorities based on what I was working on yesterday

Send the summary to me via chat.
```

**What you should see:** A cron job created that will run every morning and message you a daily briefing — before you even open your laptop.

## 🎉 What Just Happened

You've seen the full picture of where personal AI is headed. OpenClaw turns Claude Code from a tool you use into an employee that works for you. The key insight: everything you've learned this week — context files, skills, memory, prompting — compounds. Each piece makes the others more powerful. USER.md + SOUL.md + Skills + 24/7 runtime = an AI that works like a senior team member who never forgets, never sleeps, and gets better every week.

## Go Deeper

- **OpenClaw repo:** [github.com/clawdbot/clawdbot](https://github.com/clawdbot/clawdbot)
- **Skills marketplace:** [clawdhub.com](https://clawdhub.com) — browse and share community-built skills
- **Start small:** You don't need to go full 24/7 on day one. Start with USER.md + SOUL.md in regular Claude Code, add skills when you find repeating workflows, and graduate to OpenClaw when you're ready for persistent operation.
- **Security matters:** OpenClaw runs on your machine with your permissions. Review the AGENTS.md security patterns from Lesson 21 — define what it can do autonomously vs. what needs your approval.

## Share

Bring back: If you had a 24/7 AI chief of staff, what's the first task you'd hand off? What would it do every morning before you wake up?
