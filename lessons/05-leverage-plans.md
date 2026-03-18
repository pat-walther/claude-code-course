# 5. Leverage Plans to Improve Quality

> **Magic Moment:** You see the difference between asking Claude to "just build it" vs. planning first — and realize that 30 seconds of planning prevents 30 minutes of rebuilding.

## Instructions for Claude

CRITICAL RULES:
- **ONE step per message.** Never combine two steps into one response.
- **STOP and wait** after every step. Do not continue until the student responds.
- **Keep each message SHORT** — 3-5 sentences max.
- Never use technical jargon. Write plans in plain language.
- Use the AskUserQuestion tool whenever you need more info.

---

### Step 1: What Do You Want to Build?

> "Today we're going to plan before we build. What feature or page do you want to add to your product?"
>
> **A)** A new page or section
> **B)** A feature that helps your users
> **C)** Something you've been putting off

**STOP. Wait for their response.**

---

### Step 2: Sketch It

> "Before we build anything, let me sketch it out."

Generate 3 different ASCII wireframe layouts for their feature. Each should take a genuinely different approach. Keep sketches small (5-8 lines each). Label what each prioritizes.

> "Which feels closest? Or mix and match — like 'the header from A but the flow from C.'"

**STOP. Wait for their choice.**

If they want changes, update the sketch and show it again. Repeat until they're happy.

---

### Step 3: Plan It

> "Now press **Shift + Tab** until you see **Plan** at the bottom of your screen. This puts me in planning mode — I'll think through how to build this without actually doing it yet."

**STOP. Wait for them to confirm they're in Plan mode.**

Write an implementation plan and save it to `plan.md`:
- **What we're building** — one sentence
- **Approach** — steps in plain language
- **What could go wrong** — risks
- **How big this is** — quick or involved?

> "Here's the plan. Does this match what you had in mind? Now is the cheap moment to change direction."

**STOP. Wait for their feedback.** Update `plan.md` if needed.

---

### Step 4: Build It

> "Press **Shift + Tab** to switch back to **Normal** mode. Time to build."

**STOP. Wait for them to switch.**

Build the feature following the plan and their chosen sketch. Open in browser.

> "There it is. What do you think?"

**STOP. Wait for their reaction.** Do one round of changes if needed.

---

### Wrap Up

> "That's the workflow: **sketch → plan → build.** Each step prevents building the wrong thing."
>
> **What would you like to do next?**
> - **A)** Move on to Lesson 6 — brainstorm features and build prototypes
> - **B)** Add another feature using this workflow
> - **C)** Publish your updated project

**Share prompt:** What feature did you plan and build? Was the planning step worth it?

---

## Reference Material

**ASCII wireframe examples (for Claude's reference when generating sketches):**

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

```
┌──────────────────────────────┐
│  Logo        Nav   Nav   Nav │
├──────────────────────────────┤
│   Big headline here          │
│   [ Get Started ]            │
├───────┬───────┬──────────────┤
│ Card  │ Card  │ Card         │
└───────┴───────┴──────────────┘
```

```
┌──────────────────────────────┐
│         Logo + Nav           │
├──────────────────────────────┤
│    [ Search bar         🔍 ] │
│    ┌────────────────────┐    │
│    │ Item 1        ►    │    │
│    │ Item 2        ►    │    │
│    │ Item 3        ►    │    │
│    └────────────────────┘    │
└──────────────────────────────┘
```

**The discovery prompt template:**
"I want to make _____. This is for _____, who are trying to _____."

**Pro tip:** Start a fresh chat after big milestones. Long conversations make Claude less sharp. Your CLAUDE.md means you don't lose context.
