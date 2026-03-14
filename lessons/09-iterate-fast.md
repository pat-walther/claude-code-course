# 9. The Screenshot-Feedback Loop

> **Magic Moment:** You screenshot something that looks wrong, paste it into Claude Code with "fix the spacing here," and Claude fixes exactly what you pointed at — no lengthy descriptions required.

## Why This Matters

Building v1 is the easy part. The real work is the 20 iterations that turn "this is close" into "this is right." Most PMs waste time writing detailed change requests: "increase the padding between the header and the card container from 16px to 24px, and reduce the font-weight on the subtitle from semibold to medium." That's slow, and you have to know CSS to do it. The screenshot-feedback loop is faster: point at the problem, describe it like a human, and Claude fixes it. You iterate at the speed of conversation, not the speed of tickets.

## Before You Start

- [ ] Claude Code open in your project folder
- [ ] A prototype you've built (from Lesson 7 or 8)
- [ ] The prototype open in your browser so you can screenshot it
- [ ] Know how to take a screenshot (Mac: Cmd+Shift+4 to select a region)

## Do This Now

### Step 1: Review before you build

Before we iterate visually, learn the habit that saves the most time: **review Claude's plan before it writes code.**

**Paste this into Claude Code:**
```
I want to add a sidebar navigation to my prototype. Before writing any code:
- Read my project files
- Write a plan for how you'd build this
- Include: what files you'd change, what components you'd add, and any tradeoffs
- Don't write code yet — just the plan

I want to review it first.
```

**What you should see:** A clear, readable plan — not code. Read it. Does the approach match what you imagined? This is your chance to course-correct before Claude spends 2 minutes building the wrong thing.

**Now respond with your edits:**
```
Change the plan: make the sidebar collapsible on mobile (hamburger icon), and use icons-only mode on smaller screens instead of hiding it completely. Now build it.
```

**What you should see:** Claude builds the sidebar following your modified plan. The habit of reviewing first prevents the "undo" loop where Claude builds something, you don't like it, and you spend 10 minutes getting back to where you started.

### Step 2: Your first screenshot iteration

Open your prototype in the browser. Find something that looks off — wrong spacing, weird alignment, color that doesn't feel right, text that's too big or too small. You'll find something. There's always something.

**Take a screenshot of that specific area** (Cmd+Shift+4 on Mac, Snipping Tool on Windows). Then:

**Paste the screenshot into Claude Code with this prompt:**
```
Look at this screenshot. Fix these issues:
1. The spacing between the cards is too tight — add more breathing room
2. The header text looks too heavy — make it lighter
3. The filter buttons don't look clickable enough — add a subtle border or background
```

**What you should see:** Claude reads your screenshot, identifies exactly what you're pointing at, and makes targeted changes to the code. No guessing, no "which card do you mean?" — it sees what you see.

### Step 3: The point-and-describe method

This is the most natural way to give design feedback. You don't need to know CSS property names. Just describe what's wrong the way you'd tell a designer sitting next to you.

**Take another screenshot and try these styles of feedback:**

**Vague but effective:**
```
This doesn't feel right. The whole page feels cramped. Give everything more space to breathe.
```

**Pointing at specifics:**
```
See the gap between the metrics bar and the card list? Make that bigger. And the cards — they need slightly rounded corners, like 12px radius instead of whatever they are now.
```

**Comparative:**
```
This looks okay, but the sidebar feels heavier than the main content. It's drawing too much attention. Make the sidebar more subtle — lighter background, thinner text — so the eye goes to the main content first.
```

**What you should see:** 🎉 **This is the magic moment.** Claude interprets your natural language feedback and makes precisely the right CSS/layout changes. You didn't say "change padding-top from 1rem to 1.5rem" — you said "give it more space to breathe" and Claude figured out the implementation. Refresh your browser, and it looks exactly like what you meant.

### Step 4: The rapid iteration loop

Now do this 3-4 more times. Each cycle should take under a minute:

1. **Look** at the prototype in your browser
2. **Screenshot** the part that bugs you
3. **Paste + describe** what's wrong in plain English
4. **Refresh** your browser to see the fix
5. **Repeat** until it feels right

**Try these prompts for common iteration needs:**

**Layout problems:**
```
[screenshot] The layout breaks on narrow screens. The cards should stack vertically on mobile instead of overflowing.
```

**Visual hierarchy:**
```
[screenshot] Everything on this page has the same visual weight. Make the primary action (the big blue button) stand out more. Dim everything else slightly.
```

**Polish:**
```
[screenshot] This is 90% there. Add the small details that make it feel finished: subtle hover transitions, a focus ring on inputs, and better spacing in the empty state message.
```

### Step 5: Know when to start fresh

Sometimes iterating won't get you there. If you've gone through 5+ rounds of feedback and it still doesn't feel right, the foundation might be off.

**Paste this into Claude Code:**
```
I've been iterating on this prototype but something fundamental isn't working. Instead of more tweaks: start a new chat, re-read design.md, and rebuild this screen from scratch with a completely different layout approach. Keep the same features but rethink the visual structure.
```

⚠️ **Key habit:** After you finish a significant round of iteration, start a new Claude Code chat. Long conversations accumulate context that can confuse Claude. A fresh chat with your CLAUDE.md and design.md gives you a clean slate without losing your design system.

## 🎉 What Just Happened

You learned the most powerful iteration pattern in Claude Code: screenshot → describe → fix → repeat. This loop replaces the old way of iterating on design (write a detailed ticket → wait for a developer → review → write another ticket). You're giving feedback the way you think — "this feels cramped," "that's too heavy," "make this pop more" — and Claude translates that into precise code changes.

The two key habits: **review the plan before building** (prevents building the wrong thing) and **start fresh chats after major features** (keeps Claude sharp). Together, these habits make your iteration cycles dramatically faster.

## Go Deeper

- **Design review prompt:** Use Julie Zhuo's framework — paste your prototype screenshot and ask: `"You are an expert product designer. Review this screen: What is the objective? Who is it for? What do we want users to feel? What can we remove and have it work just as well?"`
- **User persona feedback:** Ask Claude to roleplay as your user: `"You are a [busy PM at a startup]. Look at this prototype screenshot. What confuses you? What would you click first? What would make you leave?"`
- **Audit for consistency:** After multiple iterations: `"Review all the screens in my prototype for visual consistency. Are button styles, spacing, typography, and colors consistent across pages? List any inconsistencies."`
- **Keyboard shortcut:** On Mac, Cmd+Shift+4 lets you select a specific region to screenshot — use this instead of full-screen captures so Claude focuses on the area you care about.

## Share

**Bring back:** A before and after — your screenshot feedback to Claude and the fixed result. What did you say in plain English, and how close was Claude's fix to what you meant?
