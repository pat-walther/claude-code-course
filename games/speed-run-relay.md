# 🏁 Speed Run Relay — Ship a Product in 22 Minutes

> **Magic Moment:** Your team goes from a blank folder to a polished, documented product prototype — in a relay race where every handoff teaches a new Claude Code skill.

---

## The Race at a Glance

| | Role | Time | What They Build |
|---|---|---|---|
| 🏗️ Leg 1 | **The Architect** | 5 min | Project structure + CLAUDE.md + ASCII wireframe |
| 🔨 Leg 2 | **The Builder** | 7 min | Working HTML prototype |
| 🎨 Leg 3 | **The Designer** | 5 min | Polished, responsive UI |
| 📋 Leg 4 | **The PM** | 5 min | Release notes + product docs + v2 roadmap |

**Total relay time: ~22 minutes**
**Total session time with setup + judging: ~45 minutes**

---

## How This Works

You're a relay team. Each person runs one leg — building one piece of the product using Claude Code — then passes their output to the next runner. No one sees the full picture until the end. The team that ships fastest with the best result wins.

**The rules are simple:**
1. Only one person works at a time (no parallel running — this is a relay, not a free-for-all)
2. You can only use what the previous person gave you (plus the original brief)
3. Every handoff goes through your team channel — post files, screenshots, or code
4. The clock is always running ⏱️

---

# 📋 FACILITATOR GUIDE

*Print this section or keep it on your screen. You're the race official.*

## Pre-Race Setup (10 minutes before go time)

### 1. Split Into Teams
- **Ideal team size:** 4 people (one per leg)
- **3-person teams:** Person 1 doubles back as the PM in Leg 4
- **Odd numbers:** Facilitator joins a team or one team gets a wildcard — they pick their own brief
- **Tip:** Mix experience levels. Pair someone comfortable in the terminal with someone brand new.

### 2. Set Up Team Channels
Pick one sharing method per session:

| Method | Best For | Setup |
|--------|----------|-------|
| **Slack/Discord** | Remote or hybrid sessions | Create channels: `#team-alpha`, `#team-bravo`, `#team-charlie` |
| **GitHub** | Technical cohorts | Each team forks a template repo, pushes between legs |
| **AirDrop/USB** | In-person sessions | Sit teams together, share files directly |
| **Copy-paste** | Minimum setup | Paste CLAUDE.md content and code directly into group chat |

### 3. Assign Briefs
Distribute one brief per team. Use different briefs so teams aren't copying each other:

- **Team Alpha** → `brief-a.md` (Habit Tracker)
- **Team Bravo** → `brief-b.md` (Team Standup Bot)
- **Team Charlie** → `brief-c.md` (Customer Feedback Wall)

Briefs are in `games/speed-run-files/`. Print them or share the file.

### 4. Assign Roles
Each team assigns roles before the race:

| Role | Who Should Run This Leg |
|------|------------------------|
| 🏗️ The Architect | Someone who's comfortable with project setup |
| 🔨 The Builder | The most adventurous prompt writer |
| 🎨 The Designer | The person with the strongest design eye |
| 📋 The PM | The natural writer/strategist |

### 5. Set Up the Timer
Use any visible timer — project it on screen if possible:
- [TimerTab.com](https://www.timertab.com/) — full-screen browser timer
- Phone timer on a stand works too
- See `speed-run-files/timer-instructions.md` for the exact sequence

### 6. The Pre-Race Briefing (say this out loud)

> "Alright, racers. Here's what's about to happen.
>
> You're building a real product in 22 minutes. Each of you runs one leg of the relay. When the whistle blows, Leg 1 starts — The Architect has 5 minutes to set up the project. When their time is up, they post their work to the team channel, and Leg 2 picks it up. No stopping. No going back.
>
> You'll be scored on three things: **Speed** — did you finish? **Quality** — does it actually work? **Creativity** — did you surprise us?
>
> This is not a drill. This is a race. Ready?"

---

## Running the Race

### 🟢 START — Leg 1: The Architect (5:00)
- Announce: *"ARCHITECTS — GO! You have 5 minutes!"*
- Start the 5-minute timer
- At 1:00 remaining: *"One minute! Start sharing your output!"*
- At 0:00: *"TIME! Architects, post everything to your channel NOW."*

### 🟡 Transition (30 seconds)
- *"Builders — grab the CLAUDE.md and wireframe from your channel. You're up in 30 seconds."*
- Confirm all teams have received their Leg 1 handoff

### 🟢 Leg 2: The Builder (7:00)
- Announce: *"BUILDERS — GO! You have 7 minutes!"*
- Start the 7-minute timer
- At 2:00 remaining: *"Two minutes! Your prototype should be working!"*
- At 0:00: *"TIME! Post your prototype NOW."*

### 🟡 Transition (30 seconds)

### 🟢 Leg 3: The Designer (5:00)
- Announce: *"DESIGNERS — GO! You have 5 minutes!"*
- At 1:00 remaining: *"One minute! Take your before/after screenshots!"*
- At 0:00: *"TIME! Post your polished version NOW."*

### 🟡 Transition (30 seconds)

### 🟢 Leg 4: The PM (5:00)
- Announce: *"PMs — GO! You have 5 minutes! This is the final leg!"*
- At 1:00 remaining: *"One minute! Package it up!"*
- At 0:00: *"TIME! The race is over! Hands off the keyboard!"*

### 🏁 Finish Line
- *"Alright, let's see what you built. Each team gets 30 seconds to present."*

---

## Scoring

Use the scorecard in `speed-run-files/scorecard.md`. Score each team out of 100:

| Category | Weight | What to Look For |
|----------|--------|-----------------|
| ⏱️ **Speed** | 40% | Did they finish all 4 legs? Did each leg finish on time? Partial legs count for partial credit. |
| ✅ **Quality** | 30% | Does the prototype work? Is the code clean? Do the docs make sense? |
| 🧠 **Creativity** | 30% | Did they add unexpected features? Is the design distinctive? Did the PM write something compelling? |

### Awards
- 🥇 **Fastest Ship** — Finished first with all legs complete
- 🎨 **Best Design** — Highest marks on visual polish and UX
- 🧠 **Most Creative** — Most surprising or ambitious interpretation
- 🏆 **Overall Winner** — Highest combined score

---

## The Twist Round (Optional — 5 extra minutes)

*Only run this if energy is high and time allows.*

After all teams finish, announce:

> "Great work. But we're not done. A customer just submitted a critical bug report. Your entire team works together this time. First team to fix it and post proof gets 10 bonus points."

**The Bug Report** (share with all teams):

```
BUG REPORT #001
Priority: P0 — Critical
Reporter: Alex Chen, beta tester

Summary: The main page crashes when I click the primary action button.

Steps to reproduce:
1. Open the prototype
2. Click the main CTA button
3. Nothing happens — no response, no error message

Expected: Something should happen when I click the button
Actual: Dead click. The button is just decoration.

Additional context: "I love the design but I literally can't use it.
Please fix ASAP."
```

*This is intentionally vague — it forces teams to diagnose before they fix. First team to post a working prototype where the button does something meaningful wins.*

---

# 🎮 PLAYER GUIDE

*This is what each player sees during the race. Share the relevant leg with each person.*

---

## 🏗️ LEG 1: The Architect

**Your role:** You're laying the foundation. Everything your team builds depends on what you set up in the next 5 minutes.

**Par time:** 5 minutes
**Your handoff:** CLAUDE.md file + ASCII wireframe → post both to your team channel

### Before the Whistle
- Open your terminal
- Create a new folder for the project: `mkdir relay-project && cd relay-project`
- Launch Claude Code: `claude`
- Have your product brief open (your facilitator gave you one)

### When the Clock Starts

**Step 1: Set up the project (1 min)**

Paste this into Claude Code (customize the bracketed parts from your brief):

```
Create a project structure for [PRODUCT NAME FROM YOUR BRIEF]. Set up:
1. A CLAUDE.md file that describes what this product is, who it's for, and the core features
2. An index.html file (empty for now, just boilerplate)
3. A README.md with a one-line description

In the CLAUDE.md, include:
- Product name and one-sentence pitch
- Target user
- Core features (3-5 bullet points from the brief)
- Tech stack: single HTML file with inline CSS and JS
- Design direction: modern, clean, mobile-first
```

**What you should see:** Claude creates 3 files. The CLAUDE.md should read like a mini product spec.

**Step 2: Create the wireframe (3 min)**

```
Create an ASCII wireframe of the main screen for this product. Show:
- The header/nav area
- The main content area with the key UI elements
- The primary call-to-action
- The overall layout structure

Make it detailed enough that a developer could build from it. Use box-drawing characters.
Save it as wireframe.txt
```

**What you should see:** A text-based layout that looks something like:

```
┌──────────────────────────────────┐
│  🟢 HabitFlow          [+ Add]  │
├──────────────────────────────────┤
│                                  │
│  Today's Habits                  │
│  ┌────────────────────────────┐  │
│  │ ☐ Morning meditation  5m  │  │
│  │ ☐ Read 20 pages      15m  │  │
│  │ ☐ Exercise           30m  │  │
│  └────────────────────────────┘  │
│                                  │
│  ══════════════════════════════  │
│  Streak: 🔥 7 days              │
│                                  │
└──────────────────────────────────┘
```

**Step 3: Share your output (1 min)**

Post to your team channel:
1. The **CLAUDE.md** file (copy-paste the full text or share the file)
2. The **wireframe.txt** or a screenshot of it
3. A one-line note: *"Here's the foundation — [any context about design choices]"*

### ✅ You're Done When
- [ ] CLAUDE.md exists with product name, target user, features, and tech notes
- [ ] ASCII wireframe shows the main screen layout clearly
- [ ] Both are posted to the team channel

### What You Just Learned
- **CLAUDE.md** is your product spec for the AI — the better you write it, the better your team's code will be
- Claude can wireframe faster than any whiteboard session
- Setting up structure before code saves everyone time downstream

---

## 🔨 LEG 2: The Builder

**Your role:** You're turning a wireframe into a working prototype. The Architect gave you the blueprint — now make it real.

**Par time:** 7 minutes
**Your handoff:** A working HTML prototype → post the file (or a live URL) to your team channel

### Before the Whistle
- Grab the CLAUDE.md and wireframe from your team channel
- Create the same project folder: `mkdir relay-project && cd relay-project`
- Save the CLAUDE.md file into this folder (paste it in or download it)
- Launch Claude Code: `claude`

### When the Clock Starts

**Step 1: Feed Claude the context (1 min)**

```
Read the CLAUDE.md in this folder. Then read wireframe.txt.
I need you to build a working HTML prototype based on this wireframe.
Summarize what you understand about the product before we start building.
```

**What you should see:** Claude reads both files and summarizes the product. This confirms it has the right context. If something's off, correct it now — you don't have time to fix misunderstandings later.

**Step 2: Build the prototype (5 min)**

```
Build a complete, working single-page HTML prototype based on the wireframe.

Requirements:
- Everything in one index.html file (HTML + CSS + JS inline)
- The UI should match the wireframe layout
- All buttons and interactive elements should do something (even if it's just a console.log or alert for now)
- Use modern CSS (flexbox/grid, good spacing, readable fonts)
- Add realistic sample data (don't use "Lorem ipsum")
- Make sure it looks decent — this is going to a designer next

Don't overthink the design — focus on WORKING functionality first.
```

**What you should see:** Claude generates a full HTML file with working interactions. It should look like a real app, not a homework assignment.

**Step 3: Verify it works (30 sec)**

```
Open index.html in my browser so I can verify it works
```

Click around. Does it load? Do buttons do things? If something's broken:

```
The [specific thing] isn't working. Fix it quickly — I'm on a timer.
```

**Step 4: Share your output (30 sec)**

Post to your team channel:
1. The **index.html** file
2. A **screenshot** of the working prototype in the browser
3. One-line note: *"Prototype is working — [any known issues or notes]"*

### ✅ You're Done When
- [ ] index.html opens in a browser without errors
- [ ] The layout matches the wireframe from Leg 1
- [ ] Interactive elements actually respond to clicks
- [ ] Posted to team channel with a screenshot

### What You Just Learned
- Claude reads CLAUDE.md automatically — good project memory means better code
- Translating a wireframe to code is Claude's superpower
- "Make it work first, make it pretty later" — prototyping speed matters

---

## 🎨 LEG 3: The Designer

**Your role:** The Builder gave you a working prototype that probably looks... okay. You have 5 minutes to make it look *great*.

**Par time:** 5 minutes
**Your handoff:** Before/after screenshots + polished HTML file → post to your team channel

### Before the Whistle
- Grab the index.html from your team channel
- Save it to your project folder
- Open it in your browser — take a SCREENSHOT now (this is your "before")
- Launch Claude Code: `claude`

### When the Clock Starts

**Step 1: Take stock and screenshot (30 sec)**

Open the prototype in your browser. Take a screenshot. This is your "before."

**Step 2: Create a design system (2 min)**

```
Read the index.html file in this folder. I need to polish this prototype's design.

Apply a cohesive design system:
1. Pick a color palette — a primary color, a secondary color, and a neutral scale (grays)
2. Set up typography — use Google Fonts or system fonts, with clear hierarchy (h1, h2, body, caption sizes)
3. Add consistent spacing — use 8px grid spacing throughout
4. Round corners on cards/containers (border-radius: 12px)
5. Add subtle shadows for depth (box-shadow on cards)
6. Make sure the contrast ratio is accessible (dark text on light backgrounds)

Make it feel premium, not generic.
```

**What you should see:** The same page, but now it looks like a real product, not a hackathon project.

**Step 3: Add polish and motion (2 min)**

```
Now add the finishing touches:
1. Smooth hover transitions on buttons and interactive elements (0.2s ease)
2. A subtle fade-in animation on page load for the main content
3. Make it fully responsive — looks good on mobile (375px) and desktop (1200px)
4. Add a favicon emoji in the title
5. If there's a list, add a subtle stagger animation so items appear one by one

Keep it tasteful — we want "Apple website", not "MySpace page".
```

**Step 4: Screenshot the "after" (30 sec)**

Open the updated file in your browser. Take another screenshot. Post both to your team channel.

```
Open the updated index.html in my browser
```

### ✅ You're Done When
- [ ] The page has a clear color palette, good typography, and consistent spacing
- [ ] Hover effects and animations are working
- [ ] It looks good on both mobile and desktop
- [ ] Before/after screenshots are posted to team channel
- [ ] Updated index.html file is posted

### What You Just Learned
- Design iteration with Claude is addictive — "make it look better" is a valid prompt
- A design system prompt transforms amateur code into professional-looking UI
- The screenshot-feedback loop: take a screenshot → describe what to change → repeat
- You can create a `design.md` file to codify your design decisions for future work

---

## 📋 LEG 4: The PM

**Your role:** The product is built and polished. Now you need to ship it. Write the docs that make this thing launchable.

**Par time:** 5 minutes
**Your handoff:** The final package (prototype + all docs) → post to your team channel. This is the finish line.

### Before the Whistle
- Grab the polished index.html from your team channel
- Grab the CLAUDE.md from Leg 1 (for context)
- Save both to your project folder
- Launch Claude Code: `claude`

### When the Clock Starts

**Step 1: Write release notes (2 min)**

```
Read the CLAUDE.md and index.html files in this folder.

Write release notes for v1.0 of this product. Include:
1. A catchy one-line headline for the launch
2. What's new (3-5 bullet points describing the features)
3. Known limitations (be honest — 2-3 things we know aren't perfect)
4. What's coming next (tease v2)

Write it in markdown. Tone: confident but not corporate. Like a cool indie dev shipping their first product.
Save it as RELEASE-NOTES.md
```

**What you should see:** A markdown file that feels like a real product launch post.

**Step 2: Write the product description (1.5 min)**

```
Write a 1-paragraph product description for this app. This is the "About" text you'd put on Product Hunt or an app store listing. Max 3 sentences.

Then write a tagline — one line, max 10 words.

Save both in a file called PRODUCT.md
```

**Step 3: Generate v2 feature ideas (1.5 min)**

```
Based on everything you know about this product, brainstorm 3 feature ideas for v2. For each one:
1. Feature name
2. One-sentence description
3. Why it matters for the target user
4. Rough complexity estimate (Small / Medium / Large)

Be creative — think about what would make users tell their friends about this product.

Add these to the PRODUCT.md file under a "## V2 Roadmap" section.
```

**Step 4: Post the final package (0 sec — you're at the finish line)**

Post to your team channel:
1. The final **index.html** (the polished version from the Designer)
2. **RELEASE-NOTES.md**
3. **PRODUCT.md** (with description, tagline, and v2 ideas)
4. A victory message: *"🏁 [Team Name] HAS SHIPPED! Here's our product."*

### ✅ You're Done When
- [ ] RELEASE-NOTES.md has a headline, features, limitations, and next steps
- [ ] PRODUCT.md has a product description, tagline, and 3 v2 feature ideas
- [ ] Everything is posted to the team channel
- [ ] You've announced your team has finished

### What You Just Learned
- Claude is an exceptional writing partner for PM tasks — release notes, product copy, and feature ideation
- Having CLAUDE.md context means Claude already understands the product — no re-explaining
- The best PMs ship with documentation, not just code

---

# 🏆 The Finish Line

## Presentations (5 minutes)

Each team gets **30 seconds** to present:
1. Show the final prototype (open it in a browser)
2. Read the tagline
3. Share one v2 feature idea

**Facilitator:** Time them strictly. 30 seconds. A buzzer sound helps.

## Awards Ceremony

Score each team using the scorecard, then announce:

> "And the results are in..."

| Award | Meaning |
|-------|---------|
| 🥇 **Fastest Ship** | Finished all legs with time to spare |
| 🎨 **Best Design** | Most polished, professional-looking prototype |
| 🧠 **Most Creative** | Biggest "wow, I didn't expect that" moment |
| 🏆 **Overall Winner** | Highest total score across all categories |

*Tip: If possible, have small prizes — stickers, bragging rights, or "First Place" Slack emoji react on their post.*

---

## 🔄 Sharing Mechanics — Quick Reference

How to hand off between legs. Pick ONE method for your session:

### Option 1: Slack/Discord (Recommended for remote)
- Each team has a channel: `#team-alpha`, `#team-bravo`, etc.
- Each runner posts files and screenshots when their leg is done
- Next runner downloads files and drops them into their project folder

### Option 2: GitHub (For technical cohorts)
- Create a template repo with just a README
- Each team forks it
- Each runner commits and pushes when done
- Next runner pulls before starting

### Option 3: AirDrop / USB (For in-person)
- Teams sit together
- AirDrop files directly between laptops
- Fast and frictionless — best for co-located teams

### Option 4: Copy-Paste (Minimum setup)
- Paste the full CLAUDE.md text and HTML code into a group DM
- Next person copies it into a file locally
- Works everywhere, zero setup — just messy for large files

---

## Debrief Questions (5 minutes after awards)

Ask the group:

1. **"What was the hardest handoff?"** — This reveals where documentation was lacking
2. **"Did the CLAUDE.md actually help the Builder?"** — Demonstrates the value of project memory
3. **"What would you do differently on a second run?"** — Surfaces process improvements
4. **"Who discovered a Claude Code trick they want to share?"** — Crowdsources tips

---

## Variations for Future Sessions

| Variation | Change |
|-----------|--------|
| **Reverse Relay** | Start from PM docs and work backward to code |
| **Blind Relay** | No one sees the original brief except the Architect |
| **Speed Round** | Cut all times in half — 2.5 / 3.5 / 2.5 / 2.5 |
| **Solo Relay** | Each person does all 4 legs — race against each other |
| **Tag Team** | 2-person teams, alternating every 3 minutes |

---

## Share

**Bring back:** Your team's final prototype URL or screenshot, plus the winning tagline. Post it in the main cohort channel with the hashtag `#SpeedRunRelay`.
