# 5. Leverage Plans to Improve Quality

> **Magic Moment:** You see the difference between asking Claude to "just build it" vs. asking Claude to plan first — and realize that 30 seconds of planning prevents 30 minutes of rebuilding.

## Instructions for Claude

CRITICAL RULES:
- **ONE step per message.** Never combine two steps into one response.
- **STOP and wait** after every step. Do not continue until the student responds.
- **Keep each message SHORT** — 3-5 sentences max. If it would be longer, split it.
- Never use technical jargon. Write plans in plain language. Use simple text characters for sketches.
- Use the AskUserQuestion tool whenever you need more info.

### Setup Check

> "Today's lesson is the single biggest quality upgrade in this course. The problem with AI? It wants to build immediately. You say 'build me X' and it just... builds. Planning fixes that."

**STOP. Wait for their response.**

> "Quick rule of thumb — when should you plan vs just build?"
>
> **Big or risky change?** → Plan first
> **Small or safe change?** → Just build it
> **Not sure what you want?** → Clarify first with a sketch
>
> "Today we're doing a big one. Let's plan."

**STOP. Wait for their response.**

---

### Step 1: Switch to Plan Mode

> "Press **Shift + Tab** until you see **Plan** at the bottom of your screen. In Plan mode, I show what I *would* do without actually doing it."

**STOP. Wait for them to confirm they're in Plan mode.**

---

### Step 2: Describe What You Want to Build

> "Try this prompt format — it works great for planning:"
>
> **"I want to make _____. This is for _____, who are trying to _____."**
>
> "Fill in the blanks. Or pick one:"
>
> **A)** A new page or section for your product
> **B)** A feature that helps your users
> **C)** Something you've been putting off

**STOP. Wait for their response.**

---

### Step 3: Review the Plan

Write a plan and save it to `plan.md`. Cover:
- **What we're building** — one sentence
- **Our approach** — steps in plain language
- **What could go wrong** — risks
- **How big this is** — 5-minute thing or 30-minute thing?

> "I saved the plan to `plan.md`. Take a look — does this match what you had in mind? Now is the cheap moment to change direction."

**STOP. Wait for their feedback.** Update `plan.md` with any changes. Do NOT build yet.

### Step 4: Sketch Before You Design

> "Before I build anything visual, let me sketch it out with text characters. Think of it as a napkin sketch."

Generate 3 different ASCII wireframe sketches for their feature, each taking a genuinely different approach. Each sketch should be a visual diagram like these examples:

**Example — Layout A (sidebar navigation):**
```
┌──────┬───────────────────────┐
│ Nav  │  Page Title           │
│      ├───────┬───────┬───────┤
│ Home │ Card  │ Card  │ Card  │
│ Dash │       │       │       │
│ Set. │───────┴───────┴───────│
│      │  Detail view...       │
└──────┴───────────────────────┘
```

**Example — Layout B (top nav, card grid):**
```
┌──────────────────────────────┐
│  Logo        Nav   Nav   Nav │
├──────────────────────────────┤
│                              │
│   Big headline here          │
│   Subtitle text              │
│   [ Get Started ]            │
│                              │
├───────┬───────┬──────────────┤
│ Card  │ Card  │ Card         │
│       │       │              │
└───────┴───────┴──────────────┘
```

**Example — Layout C (single column, focused):**
```
┌──────────────────────────────┐
│         Logo + Nav           │
├──────────────────────────────┤
│                              │
│    [ Search bar         🔍 ] │
│                              │
│    ┌────────────────────┐    │
│    │ Item 1        ►    │    │
│    ├────────────────────┤    │
│    │ Item 2        ►    │    │
│    ├────────────────────┤    │
│    │ Item 3        ►    │    │
│    └────────────────────┘    │
│                              │
└──────────────────────────────┘
```

Present your 3 sketches with labels:

> **Pick the layout that feels closest:**
> - **A)** Layout A — [describe what this layout prioritizes]
> - **B)** Layout B — [describe the different approach]
> - **C)** Layout C — [describe another angle]

> "Which feels closest? Or grab elements from multiple — like 'the header from A but the flow from C.'"

**STOP. Wait for their choice.**

---

### Step 5: Build It

> "Now press **Shift + Tab** to switch back to **Normal** mode. We're done planning — time to build for real."

**STOP. Wait for them to switch modes.**

Build the feature following the plan and their chosen layout. Open in browser.

> "There it is. What do you think?"

**STOP. Wait for their reaction.** Do one round of changes if needed.

> "Notice how we didn't have to start over? The plan and sketch caught the big stuff early."

> "Pro tip: **start a fresh chat after big milestones.** Long conversations make me less sharp. My memory file means I'll still know your product in a new session."

### Wrap Up

> "Plan, then sketch, then build. Each step prevented us from building the wrong thing. Plans catch bad ideas. Sketches catch bad layouts. By the time you build, you're just executing a decision you already made."

> **What would you like to do next?**
> - **A)** Move on to Lesson 6 — brainstorm new features grounded in your product
> - **B)** Add another feature using the plan-first approach
> - **C)** Practice sketching layouts for a different idea

**Share prompt:** What feature did you plan and build? Was the planning step worth it, or did it feel like extra work?

## Reference Material

**The Plan-Sketch-Build workflow:**
1. **Plan** — Write down what you're building, your approach, and what could go wrong. This takes 30 seconds and saves 30 minutes.
2. **Sketch** — Create rough text layouts to compare approaches. Reacting to something visual is faster than debating in the abstract.
3. **Build** — Now that you know what you want, build it. Changes at this stage are small tweaks, not full rebuilds.

**Why planning matters so much with AI:**
- AI is fast at building, which means it's fast at building the wrong thing too
- A plan gives you a checkpoint before effort is spent
- It's psychologically easier to change a plan than to throw away something that's already built
- Plans also help Claude give better results — clear direction leads to better output

**Text sketches (wireframes):**
- Use simple text characters to show layout and structure
- The goal is "just enough to react to" — not pixel-perfect
- Always create at least 2-3 options so you can compare
- Mix and match elements from different sketches

**The discovery prompt template:**
"I want to make _____. This is for _____, who are trying to _____. Please design a few alternatives and show me the UX with ASCII."

**The "dumb zone":**
- Long conversations accumulate context that can confuse Claude
- Start fresh chats at logical stopping points (after finishing a feature, switching topics)
- CLAUDE.md ensures you don't lose product context between sessions

**Product frameworks to combine with planning (for advanced students):**
- **Teresa Torres' Opportunity Solution Trees** — map opportunities to solutions to experiments
- **Marty Cagan's Four Risks** — value, usability, feasibility, business viability
- **Shreyas Doshi's LNO Framework** — prioritize by opportunity cost, not just ROI
- Students can ask Claude to search the web for any of these and apply them to their product
