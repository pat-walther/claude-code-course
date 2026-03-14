# 4. Introduce Your Product to Claude

> **Magic Moment:** Claude reads your actual codebase and tells you something specific and insightful about your product that a generic chatbot never could.

## Why This Matters

Every time you ask ChatGPT for product advice, you spend the first 10 minutes explaining what you're building. Claude Code skips all of that — it reads your files, understands your architecture, and meets you where your product actually is. This is the difference between a generic consultant and one who's been embedded on your team for months.

## Before You Start

- [ ] Claude Code installed and working (you tested it in Day 1)
- [ ] A codebase to work with — either your own product repo, or one of the course projects:
  - **Beginner:** [github.com/exiao/weekly-date-night](http://github.com/exiao/weekly-date-night) — a date planning service landing page
  - **Intermediate:** [github.com/exiao/subscription-tracker](http://github.com/exiao/subscription-tracker) — an app that parses credit card data to find subscriptions to cancel
  - **Advanced:** [github.com/exiao/second-opinion](http://github.com/exiao/second-opinion) — a decision-making app with AI as its core feature
- [ ] Terminal open and ready

## Do This Now

### Step 1: Clone a project (skip if using your own repo)

If you don't have your own codebase ready, pick one of the course projects and clone it:

```bash
git clone https://github.com/exiao/weekly-date-night.git
cd weekly-date-night
```

(Replace with whichever repo you chose.)

**What you should see:** A local copy of the project with its files and folders.

### Step 2: Open Claude Code in your project

Navigate to your project folder and launch Claude Code:

```bash
cd your-project-folder
claude
```

**What you should see:** Claude Code starts up with a `>` prompt, ready for your input.

### Step 3: Ask Claude to learn your product

This is the moment. You're about to see the difference between "an AI that knows coding" and "an AI that knows YOUR product."

**Paste this into Claude Code:**
```
Tell me about this codebase. I'm a PM, not an engineer, so explain it to me like I'm smart but non-technical:

1. What does this product do and who is it for?
2. How is it built? (explain the tech stack simply)
3. What are the key features you can see in the code?
4. What's the folder structure and why is it organized that way?
5. How would someone run this locally?
```

**What you should see:** Claude will read through your files — package.json, README, source code, config files — and give you a product-aware summary. Not generic fluff. Specific observations about YOUR code.

💡 **Pay attention:** Claude will likely mention specific file names, function names, or patterns it found. This is context-aware understanding — something ChatGPT can't do without you manually pasting every file.

### Step 4: Go deeper — test its understanding

Now push Claude to show you it really gets your product:

**Paste this into Claude Code:**
```
Based on what you just learned about this codebase:

1. What's the most interesting technical decision the developers made?
2. What's one thing that seems incomplete or could be improved?
3. If I told you our #1 user complaint was [pick something relevant], where in the code would you look to fix it?
```

**What you should see:** Claude references specific files and lines of code. It connects product decisions to technical implementation. It's not guessing — it's reading.

### Step 5: Get a product-level insight

**Paste this into Claude Code:**
```
Looking at this codebase as a product person: what's the biggest gap between what this product currently does and what it could do? What's the lowest-hanging fruit feature that would make the biggest difference for users?
```

**What you should see:** 🎉 This is where it clicks. Claude suggests something specific to YOUR product — not "add better onboarding" generic advice, but something grounded in the actual code, data structures, and user flows it can see.

## 🎉 What Just Happened

Claude Code read your entire project directory — every file, every config, every piece of code — and built a mental model of your product. When you asked questions, it didn't just pattern-match against generic advice. It referenced actual files, identified real architectural decisions, and gave you insights grounded in your specific codebase.

This is the superpower: Claude Code has the context that ChatGPT never will. From this point forward, every prompt you write is grounded in what your product actually is, not what you remember to tell it.

## Go Deeper

- Try asking: `"What would break if we removed [specific file]?"` — test how well it understands dependencies
- Try: `"Explain the data flow when a user [does key action]"` — see if it can trace through your code
- Try: `"What questions would a new engineer ask on their first day working on this project?"` — great for finding documentation gaps
- Read: [Claude Code Overview](https://docs.anthropic.com/en/docs/claude-code/overview)

## Share

**Bring back:** What was the most specific, surprising thing Claude said about your codebase? Something a generic AI would never have known.
