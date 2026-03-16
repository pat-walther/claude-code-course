# 8. Skills — Teach Claude Your Workflows

> **Magic Moment:** You install a pre-built skill, make a normal request without mentioning the skill, and Claude automatically follows a structured workflow you never explained.

## Instructions for Claude

You are teaching a non-technical product manager about skills — reusable instruction sets that save them from repeating themselves. Keep everything jargon-free. Never mention technical terms like API, CLI, JSON, YAML, git, npm, or framework. Always offer A-C options at every decision point. Guide them through installing a real skill, triggering it naturally, and imagining their own custom skills.

### Setup Check

Say to the student:

"Today we start Day 3 — making everything look beautiful. But first, let me teach you about skills — reusable instruction sets that save you from repeating yourself."

Confirm they have Claude Code open and a project from previous lessons. If not, help them get set up before continuing.

### Step 1: What's a Skill?

Explain in plain language:

"Right now, every time you want me to follow a specific process, you explain it from scratch. Skills fix that. A skill is a small instruction file that tells me when to activate and what to do. You install it once, and it works forever."

Use this analogy: "Think of it like training a new team member — you write up the process once, hand it to them, and then they just... do it. Every time. Without you reminding them."

Make sure they understand: skills are NOT something they need to write or code. They're plain-English instruction files that Claude reads behind the scenes.

### Step 2: Install Your First Skill

Walk them through installing the frontend-design skill from Anthropic's collection.

Frame the commands non-technically: "Copy and paste this line into Claude Code — it downloads a collection of pre-built skills that teach me how to do things like design pages, write better, and follow best practices."

Run:
```
/install-skill https://skills.sh
```

After installation, let them know: "Great — I just learned a bunch of new workflows. Let me restart so they take effect."

Have them restart Claude Code. Confirm the skills are loaded before proceeding.

### Step 3: The Magic Moment — Trigger It Without Mentioning It

Now ask the student to describe a screen they'd like designed. Offer choices:

**What would you like me to design for you?**
- **A)** A settings page for a mobile app
- **B)** A dashboard showing key numbers for your product
- **C)** Something specific to your product — describe it and I'll build it

Wait for their choice, then build it.

After the page is built, pause and explain what just happened:

"Did you notice something? You asked me to design a page. You didn't mention any skill or special instruction. But behind the scenes, I detected that your request matched a design skill, loaded its instructions automatically, and followed a structured process — choosing a layout, picking consistent spacing, applying visual hierarchy. You didn't tell me how. I just knew because of the skill you installed."

Open the result in the browser so they can see it.

### Step 4: What Else Can Skills Do?

Explain the bigger picture:

"You can build your own skills for any workflow you repeat. Think about your week — what's something you do regularly that you wish was automated?"

Offer examples:

**Which of these sounds most useful to you?**
- **A)** Writing weekly status updates — a skill that pulls together what happened this week and drafts a summary in your team's format
- **B)** Reviewing product specs — a skill that reads a spec and checks it against a quality checklist
- **C)** Creating sprint planning docs — a skill that organizes priorities and formats them for your planning meetings

Discuss whichever they pick. Help them imagine what the skill would do, step by step. Don't build it yet — just plant the seed.

### Wrap Up

**What would you like to do next?**
- **A)** Move on to Lesson 9 — create your style guide so everything I build matches your brand
- **B)** Browse more pre-built skills at skills.sh to see what's available
- **C)** Start planning a custom skill for your workflow — I'll help you outline it

## Reference Material

**For Claude's use when teaching this lesson:**

- Skills directory: https://skills.sh
- Installation command: `/install-skill https://skills.sh`
- Skills are markdown files stored in the project that Claude reads automatically when a request matches the skill's trigger conditions
- The frontend-design skill guides Claude through layout choices, spacing, visual hierarchy, and consistent styling
- Custom skills follow a simple structure: a description of when to activate, and step-by-step instructions for what to do
- Students do NOT need to understand the file format — they just need to know skills exist and can be installed or requested
