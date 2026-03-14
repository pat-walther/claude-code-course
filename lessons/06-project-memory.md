# 6. Make Claude Remember Everything

> **Magic Moment:** You create a CLAUDE.md file, start a brand new session, and Claude already knows your product — without you saying a word.

## Why This Matters

Remember the movie *50 First Dates*? The woman wakes up every day with no memory. Her partner has to re-introduce himself and their entire relationship from scratch. That's what using Claude Code without a CLAUDE.md file is like — every session starts from zero. CLAUDE.md is the "morning video" that brings Claude up to speed instantly.

Right now, Claude knows nothing about your product until you tell it. After this lesson, it will — permanently.

## Before You Start

- [ ] Claude Code open in your project folder
- [ ] You've already explored your codebase with Claude (Lesson 4)
- [ ] You know what your product does and who it's for

## Do This Now

### Step 1: Let Claude learn your project and create its memory file

This is the one-prompt version. Claude reads everything, understands it, and writes its own onboarding doc.

**Paste this into Claude Code:**
```
Tell me about my project files, including:
- What this product does and who it's for
- How it's built (explain it simply — I'm a PM, not an engineer)
- How to run it locally
- Any important setup steps

Then save your findings in a file called CLAUDE.md
```

**What you should see:** Claude reads through your project, then creates a `CLAUDE.md` file in your project root. You'll see it write the file with sections covering what the product does, the tech stack, and how to run it.

### Step 2: Add the human context Claude can't infer

Claude can figure out your tech stack and folder structure by reading files. But it can't know your strategy, your users, or your roadmap. That's your job.

**Paste this into Claude Code:**
```
Add these sections to CLAUDE.md:

## Target Users
[Your answer: Who uses this product? What's their biggest pain point?]

## Product Vision
[Your answer: What problem are you solving? Where is this product headed?]

## Current Priorities
[Your answer: What are the top 3 things on your roadmap right now?]

## What We Don't Do
[Your answer: What have you explicitly decided NOT to build?]
```

⚠️ **Important:** Replace the `[Your answer: ...]` placeholders with your actual product info before sending. This is the stuff only you know.

**What you should see:** CLAUDE.md gets updated with your human context layered on top of what Claude discovered automatically.

### Step 3: Add coding principles

Tell Claude how you want it to work on your project.

**Paste this into Claude Code:**
```
Add principles on what good coding practice looks like into CLAUDE.md, focusing on simplicity, readability, incremental building, using standard libraries, and no premature optimization under a section called: HOW TO CODE.
```

**What you should see:** A `HOW TO CODE` section gets appended to CLAUDE.md with clear, practical principles.

### Step 4: The magic test — start fresh

This is the moment of truth. Quit Claude Code completely, then start a brand new session:

```bash
# Press Ctrl+C to exit Claude Code, then:
claude
```

Now test whether it remembers:

**Paste this into Claude Code:**
```
What do you know about this project? What am I building and who is it for?
```

**What you should see:** 🎉 Claude already knows. It read your CLAUDE.md automatically when the session started. No re-explaining. No context dump. It just... knows.

Try a follow-up to really test it:

```
Based on our current priorities, what should I work on next?
```

**What you should see:** Claude references the priorities YOU wrote in CLAUDE.md and gives you a relevant answer. It's like picking up a conversation with a teammate who reviewed the brief before the meeting.

## 🎉 What Just Happened

You created a `CLAUDE.md` file — a project memory file that Claude reads automatically at the start of every session. Think of it as a README for your AI: a dedicated, predictable place to give Claude the context it needs.

Here's how Claude's memory works:
- **Short-term memory** = the current conversation (gone when you close the session)
- **Medium-term memory** = files in your project directory that Claude can read on demand
- **CLAUDE.md** = the bridge — it gets loaded automatically at session start, like a briefing document

The less you put in CLAUDE.md, but the more specific and correct it is, the better Claude performs. Don't dump everything — just the salient ideas. If you need more context, put it in other `.md` files and reference them from CLAUDE.md.

## Go Deeper

- **Template for a great CLAUDE.md:**
  ```markdown
  # CLAUDE.md

  ## What This Is
  [One-line product description]

  ## Who It's For
  [Target users and their core problem]

  ## Tech Stack
  [Keep it brief: frameworks, languages, databases]

  ## How to Run
  [The commands to get it running locally]

  ## Current Priorities
  [Top 3 things you're working on]

  ## How to Code
  [Your coding principles and conventions]
  ```
- **Add more context without bloating CLAUDE.md:** Create a `specs/` folder for feature specs, a `docs/` folder for deeper documentation. Reference them from CLAUDE.md: `"See specs/ for feature specifications."`
- Read: [Writing a Good CLAUDE.md](https://www.humanlayer.dev/blog/writing-a-good-claude-md) — excellent deep dive
- Read: [AGENTS.md spec](https://agents.md/#examples) — the open format for guiding coding agents
- Read: [Claude's Memory Tool docs](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool) — how memory works under the hood
- Browse: [claude.ai/directory](https://claude.ai/directory) — one-click integrations for Claude
- Browse: [skills.sh](https://skills.sh) — community skills directory

## Share

**Bring back:** Show the CLAUDE.md Claude created. What did it get right? What did it miss that you'll add manually?
