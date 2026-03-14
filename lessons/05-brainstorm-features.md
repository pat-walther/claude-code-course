# 5. Brainstorm Features With Your AI Co-PM

> **Magic Moment:** Claude suggests a feature idea that's specific to YOUR product — something you hadn't considered but makes total sense given your codebase and users.

## Why This Matters

We all know AI can brainstorm. Ask ChatGPT "give me feature ideas for a dating app" and you'll get the same 10 generic suggestions everyone else gets. The game changes when your brainstorming partner has already read your code, understands your architecture, and knows what's actually feasible to build. That's Claude Code — it's like having a product partner who's read every file in your repo before the meeting starts.

This lesson is inspired by the [Design Sprint](https://www.youtube.com/live/4u94juYwLLM) playbook. Pre-AI, a design sprint takes a week to go from idea to tested mockup. We're going from idea to actionable feature spec in minutes.

## Before You Start

- [ ] Claude Code open in your project folder (from Lesson 4)
- [ ] Claude has already explored your codebase (or you've completed `Tell me about this codebase...`)

## Do This Now

### Step 1: Get context-aware feature ideas

This is the prompt that separates Claude Code from ChatGPT. You're not describing your product — Claude already knows it.

**Paste this into Claude Code:**
```
Look at my project files and tell me:

1. What are the top 3 pain points users of this product probably have?
2. What features do competitors offer that we don't? (Search the web to find out.)
3. What's the highest-leverage thing we could ship in the next sprint?

Be specific. Reference actual parts of the product you can see in my files.
```

**What you should see:** Claude identifies pain points grounded in your actual code — not generic "improve the UX" advice, but things like "your checkout flow has 5 steps when it could have 2" or "you collect email but never use it for re-engagement." It names files. It references functions.

### Step 2: Apply structured brainstorming frameworks

Generic brainstorming produces generic ideas. Use structured frameworks to push Claude into unexpected territory.

**Pick one and paste it into Claude Code:**

**SCAMPER Framework:**
```
Apply the SCAMPER framework to our product's core feature:
- What can we SUBSTITUTE?
- What can we COMBINE with another feature?
- What can we ADAPT from other industries?
- How can we MAGNIFY the best part?
- What other PURPOSE could this serve?
- What can we ELIMINATE to simplify?
- How can we REVERSE or REARRANGE the flow?

Ground every suggestion in what you see in my actual codebase.
```

**Constraint Manipulation:**
```
Generate feature ideas under these constraints:
1. We can ONLY use push notifications (no app open required)
2. We have ONLY 5 seconds of user attention
3. The feature must work with NO internet connection

Now generate 3 ideas if we REMOVE the constraint that users need to sign up first.

Base all ideas on what our product actually does — reference specific files.
```

**Persona-Based Ideation:**
```
Look at my codebase and imagine these 4 people evaluating our product:
- A UX designer focused on delight
- A growth PM focused on virality
- A technical PM worried about feasibility
- An executive focused on revenue

What feature would each of them push for? Be specific to our product.
```

**What you should see:** Ideas that feel like they came from someone who's been working on your product for months. Not "add gamification" — more like "your data model already supports X, so you could expose Y to users with minimal effort."

### Step 3: Go deeper on the best idea

AI's first response is a starting point, not the answer. The magic is in the follow-up.

**Paste this into Claude Code:**
```
Go deeper on idea #3. Show me:
- 5 variations of how we could implement it
- What are the hidden assumptions?
- What could go wrong? Give me 5 failure modes.
- What's the absolute simplest version we could ship this week?
- Looking at our codebase, what would need to change to build this?
```

**What you should see:** 🎉 This is the magic moment. Claude connects the feature idea to your actual code — showing you which files to modify, what the data model already supports, and what the minimum viable version looks like. It's not just ideation anymore, it's a buildable plan.

### Step 4: Rank and commit

**Paste this into Claude Code:**
```
Take all the feature ideas from this conversation and rank them using ICE scoring (Impact, Confidence, Ease).

Then tell me:
- Top 3 for immediate testing
- Which idea validates our riskiest assumption?
- What's the one thing we should build first and why?

Save this analysis to a file called feature-brainstorm.md
```

**What you should see:** A ranked list saved to a file you can share with your team. Each idea is grounded in your actual product, not theoretical.

## 🎉 What Just Happened

You just ran a compressed design sprint with an AI that knows your product inside and out. The ideas Claude generated weren't generic — they referenced your actual files, data models, and user flows. When you said "go deeper on #3," Claude didn't just elaborate on the concept — it showed you where in your codebase to make it happen.

This is the difference between brainstorming with ChatGPT (generic + requires context dump) and brainstorming with Claude Code (specific + already has context). Your product context is the moat.

## Go Deeper

- 📺 **Watch:** [Design Sprint in 90 Minutes](https://www.youtube.com/live/4u94juYwLLM) — the methodology behind structured ideation
- Try the emotional journey mapping prompt: `"Map the user's emotional journey through [key flow]. What do they feel at each step? Where's the biggest emotional drop? What would turn frustration into delight?"`
- Try designing for extreme users: `"Design for someone who uses our product 50 times a day. What features would they need? Now design for someone who uses it once a month. What's different?"`
- Read: [AGENTS.md examples](https://agents.md/#examples) for how other projects structure context

## Share

**Bring back:** Your top 3 feature ideas from Claude — and whether any of them genuinely surprised you.
