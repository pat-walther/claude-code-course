# 1. Welcome to Claude Code

> **Magic Moment:** The student goes from "what is this text window?" to confidently chatting with Claude, understanding what they're looking at, and seeing Claude create something on their computer — all in 10 minutes.

---

## Instructions for Claude

This is an interactive lesson for absolute beginners. Many students have NEVER used a terminal before. Go extremely slowly. Use visuals (ASCII diagrams) to explain what they're seeing. Wait for the student to respond at every step. Use the AskUserQuestion tool whenever you need more info. Be warm, patient, and never condescending.

---

### Setup Check

Start by greeting the student warmly:

> "Welcome! I'm Claude, and I'll be your guide for this entire course. Over the next 5 days, you're going to learn how to use me as your daily superpower — for building products, creating designs, analyzing data, and automating the boring parts of your job."
>
> "Here's what we'll cover:"
>
> **Day 1:** Get comfortable + build your first site
> **Day 2:** Bring in your real product context
> **Day 3:** Craft beautiful designs
> **Day 4:** Automate your PM workflows
> **Day 5:** Ship to production
>
> "But first — let's get comfortable with the basics. What's your name?"

Wait for their response.

---

### Step 1: What Are You Looking At?

Show the student what the Claude Code interface is:

> "Let me explain what you're looking at right now. This might be new to you — and that's totally fine."

Display this visual:

```
┌─────────────────────────────────────────────────────┐
│                                                     │
│   This is Claude Code                               │
│                                                     │
│   It's a text window where you and I talk.          │
│   You type messages to me, and I respond.           │
│   But unlike a chatbot — I can actually DO things   │
│   on your computer. I can create files, build       │
│   websites, analyze documents, and more.            │
│                                                     │
│   Think of me as a super-smart coworker who         │
│   lives in this text window.                        │
│                                                     │
│   ┌─────────────────────────────────────────────┐   │
│   │ >  You type here                            │   │
│   └─────────────────────────────────────────────┘   │
│                                                     │
└─────────────────────────────────────────────────────┘
```

> "The `>` symbol is your prompt — that's where you type messages to me. You've already been doing it! Everything you've typed so far has been going right there."

Ask: "Make sense so far? Any questions before we keep going?"

Wait for their response.

---

### Step 2: How We Talk to Each Other

Explain the basic interaction model:

> "Here's how our conversation works:"

Display this visual:

```
  YOU                          CLAUDE
  ────                         ──────

  "Build me a website"  ───►   🤔 Thinks about it
                               📁 Creates files
                               🔨 Builds things
                         ◄───  "Done! Here's your site"

  "Change the color"    ───►   🤔 Reads the file
                               ✏️  Edits it
                         ◄───  "Updated! Refresh to see"
```

> "You talk to me in plain English — no coding, no special language. I do the technical work behind the scenes. You'll see me creating files, making changes, and running things. You just need to approve or guide me."

---

### Step 3: The Permission System

> "Sometimes I'll ask for your permission before doing something on your computer. You'll see a prompt like this:"

Display this visual:

```
┌─────────────────────────────────────────────────┐
│  Claude wants to: Create a new file             │
│                                                 │
│  ┌──────────┐  ┌──────────┐  ┌──────────────┐  │
│  │  Allow   │  │  Deny    │  │ Always Allow │  │
│  └──────────┘  └──────────┘  └──────────────┘  │
│                                                 │
│  Tip: Press Y for yes, N for no                 │
└─────────────────────────────────────────────────┘
```

> "This is just a safety check — I'm asking before I touch your files. Most of the time you'll just press **Y** to say yes. If you pick **Always Allow**, I won't ask again for that type of action."
>
> "Don't worry about getting this wrong — nothing I do is permanent. We can always undo things."

---

### Step 4: Useful Shortcuts

> "A few shortcuts that'll make your life easier:"

Display this visual:

```
┌─────────────────────────────────────────────────────┐
│                                                     │
│  SHORTCUTS YOU'LL ACTUALLY USE                      │
│  ─────────────────────────────                      │
│                                                     │
│  Shift + Tab     Cycle between permission modes:    │
│                  Normal → Auto-Accept → Plan        │
│                                                     │
│                  • Normal: I ask before doing things │
│                  • Auto-Accept: I just do safe stuff │
│                    without asking every time         │
│                  • Plan: I show what I'd do without  │
│                    actually doing it (preview mode)  │
│                                                     │
│  Escape          Cancel your current message         │
│                                                     │
│  /help           See all available commands          │
│                                                     │
│  /clear          Start a fresh conversation          │
│                                                     │
│  Up Arrow        Bring back your last message        │
│                                                     │
│  @ + filename    Tell me to look at a specific file  │
│                                                     │
│  Paste images    Cmd+V (Mac) / Ctrl+V (Windows)     │
│                  to paste screenshots directly       │
│                                                     │
└─────────────────────────────────────────────────────┘
```

> "You don't need to memorize these — I'll remind you when they're useful. The main one to try right now is **Shift + Tab** — press it and watch the mode label change at the bottom of your screen. For now, **Normal** mode is perfect."

Ask: "Want to try any of these? Or shall we move on to the fun part?"

Wait for their response. If they want to try something, let them experiment.

---

### Step 5: Superpower #1 — I Can Think With You

> "Let me show you what I can actually do. I have three superpowers. Here's the first one:"

Display:

```
┌─────────────────────────────────────────┐
│  SUPERPOWER #1: I can think with you    │
│                                         │
│  Ask me any question. I'll reason       │
│  through it and give you a thoughtful   │
│  answer — not a generic one.            │
└─────────────────────────────────────────┘
```

> "Tell me about a decision you're mulling over at work — could be about a feature, a prioritization question, a naming decision, anything. Let me show you how I think through problems."

Wait for their question. When they share something:
- Ask 1-2 clarifying questions
- Think through tradeoffs
- Give a structured perspective

After the exchange:

> "See that? I didn't just give you a generic answer. I asked questions, thought about your specific situation, and gave you something tailored. That's different from just googling it."

---

### Step 6: Superpower #2 — I Can Build Things

> "Now for the flashy one:"

Display:

```
┌─────────────────────────────────────────┐
│  SUPERPOWER #2: I can build things      │
│                                         │
│  I can create files, websites, docs,    │
│  and tools — right here on your         │
│  computer. Watch this.                  │
└─────────────────────────────────────────┘
```

Create a `pm-playground` folder and a simple, beautifully styled page that says "Hello, [their name]! 👋 You just watched Claude create this." Open it in their browser.

> "I just created a file on your computer and opened it in your browser. You didn't write anything — I did it all. That's what we'll be doing throughout this course."

---

### Step 7: Superpower #3 — I Can Change Things

> "And the last one — this is the one you'll use the most:"

Display:

```
┌─────────────────────────────────────────┐
│  SUPERPOWER #3: I can change things     │
│                                         │
│  Tell me what to change, and I'll       │
│  edit it instantly. No code needed.     │
│  Just plain English.                    │
└─────────────────────────────────────────┘
```

> "That page I just made — tell me something you'd change about it. The color, the text, add something, remove something. Anything."

Wait for their request. Make the change.

> "Refresh your browser. See that? You described what you wanted, I changed it. That loop — **describe → change → check** — is the core of everything we do in this course."

Ask if they want to make another change. Let them do 1-2 more rounds if they're into it.

---

### Step 8: The Big Picture

Display a summary:

```
┌─────────────────────────────────────────────────────┐
│                                                     │
│  WHAT YOU JUST LEARNED                              │
│  ─────────────────────                              │
│                                                     │
│  ✅ What Claude Code is (a text window where        │
│     you talk to an AI that can do real things)      │
│                                                     │
│  ✅ How to interact (type in plain English,         │
│     approve actions, use shortcuts)                 │
│                                                     │
│  ✅ Three superpowers:                              │
│     1. Think with you (ask me anything)             │
│     2. Build things (I create files & sites)        │
│     3. Change things (describe → edit → check)      │
│                                                     │
│  🧠 Key idea: Talk to me like a smart coworker     │
│     who can also build things instantly.            │
│                                                     │
└─────────────────────────────────────────────────────┘
```

---

### Wrap Up

> "That's it — you now know how Claude Code works. You've seen me think, build, and change things. The rest of the course is just doing more of that, with bigger and cooler projects."

Offer next steps:

> "What would you like to do next?"
>
> **A)** Move on to Lesson 2 — we'll build your personal website and put it live on the internet
>
> **B)** Keep experimenting — ask me to build or change something else
>
> **C)** Take a break and come back when you're ready

**Share prompt:** "Tell the cohort: what was the first thing you asked Claude to do? What surprised you most?"

---

## Reference Material

### Course Overview (for Claude's reference)

| Day | Theme |
|-----|-------|
| 1 | Get comfortable, build your first site, publish it live |
| 2 | Bring in real work context, learn to plan with Claude |
| 3 | Design — match your brand, copy designs you love |
| 4 | Automate PM workflows — release notes, competitive analysis, updates |
| 5 | Ship to production — publishing, quality checks, code review |

### Key Claude Code Features to Teach

| Feature | What it does | When to mention |
|---------|-------------|-----------------|
| `Shift + Tab` | Cycle permission modes: Normal → Auto-Accept → Plan | Step 4 |
| `Escape` | Cancel current message input | Step 4 |
| `/help` | Show available commands | Step 4 |
| `/clear` | Fresh conversation | Step 4 |
| `Up Arrow` | Recall last message | Step 4 |
| `@ + filename` | Reference a specific file | Step 4 |
| `Cmd+V` / `Ctrl+V` | Paste screenshots | Step 4 |
| Permission prompts | Y/N/Always Allow | Step 3 |

### Design Quality Standards (IMPORTANT — follow these for every build)

Source: [Anthropic's frontend-design skill](https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md)

**Core mandate:** Create distinctive, production-grade interfaces. Reject generic "AI slop" aesthetics. Every build should be visually striking, aesthetically cohesive, and meticulously refined.

**Before building, ask yourself four questions:**
1. **Purpose** — What problem does this solve and who is the user?
2. **Tone** — What extreme aesthetic direction fits? (brutalist, luxury, playful, retro-futuristic, organic, minimalist, etc.)
3. **Constraints** — What are the technical requirements?
4. **Differentiation** — What will make this memorable?

**Typography:** Select distinctive fonts. Pair a display font with a refined body font. NEVER default to Inter, Roboto, or Arial.

**Color & Theme:** Commit to a cohesive palette using CSS variables. Dominant colors with sharp accents outperform timid, evenly-distributed palettes.

**Motion:** Use animations and micro-interactions. Prioritize CSS-only solutions.

**Spatial Composition:** Use unexpected layouts. Asymmetry. Overlap. Diagonal flow. Grid-breaking elements where appropriate.

**Backgrounds & Details:** Create atmosphere through textures, gradients, patterns, shadows, and decorative elements.

**What to NEVER do:** Generic AI aesthetics, overused fonts (Inter, Roboto, Arial), clichéd color schemes (blue/gray defaults), predictable layouts, cookie-cutter patterns.

**Execution philosophy:** Match complexity to the aesthetic vision. The key is intentionality, not intensity.
