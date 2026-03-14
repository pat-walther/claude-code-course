# 22. Build Your Own Reusable Skills

> **Magic Moment:** You build a custom skill for a workflow you repeat every week, and Claude automatically loads it the next time you mention that workflow — without you asking it to.

## Why This Matters

You probably explain the same process to Claude every few days. "Use our PRD format." "Follow our release notes template." "Here's how we do sprint planning." Skills let you explain it once. From then on, Claude loads the right workflow automatically when it recognizes what you're doing. You're not just using AI — you're teaching it to work your way.

## Before You Start

- Claude Code open (or Claude.ai with Skills enabled)
- Think about one workflow you repeat at least weekly — you'll build a skill for it today
- Install the `skill-creator` skill from [github.com/anthropics/skills](https://github.com/anthropics/skills) (instructions in Step 1)

## Do This Now

### Step 1: Install the skill-creator

Before building your own skill, install the tool that builds skills for you.

**Paste this into Claude Code:**
```
Download the skill-creator skill from https://github.com/anthropics/skills and install it in my skills directory. Show me where it was installed.
```

**If you're using Claude.ai instead:** Go to [github.com/anthropics/skills](https://github.com/anthropics/skills), download the `skill-creator` folder, then upload it via Settings → Capabilities → Skills → Upload skill. Toggle it on.

**What you should see:** Claude confirms the skill is installed and shows you the file path. You now have a skill that builds other skills. Very meta.

### Step 2: See a skill in action

Before building your own, watch one trigger automatically.

**Paste this into Claude Code:**
```
Help me build a skill for writing weekly status updates.
```

**What you should see:** Claude automatically loads the `skill-creator` skill (you didn't ask it to!) and starts walking you through the process — asking about your use case, what the output should look like, what triggers it. That automatic loading? That's the description field at work.

### Step 3: Pick your workflow

Now it's your turn. Think about what you repeat every week.

**Ask yourself:** *What workflow do I repeat every week? What's the thing where I keep explaining the same process to Claude?*

Common PM examples:
- Writing PRDs in your team's format
- Summarizing customer feedback into themes
- Creating sprint planning docs
- Drafting release notes from changelogs
- Competitive analysis reports

**Paste this into Claude Code (fill in your workflow):**
```
Use the skill-creator skill to help me build a skill for [YOUR WORKFLOW HERE].

Here's what I want it to do:
- When I say "[YOUR TRIGGER PHRASE]", it should automatically kick in
- The output should include [WHAT YOU WANT]
- It should follow this process: [YOUR STEPS]

Ask me clarifying questions, then generate the SKILL.md file.
```

**What you should see:** Claude interviews you about your workflow, then generates a properly formatted SKILL.md file with YAML frontmatter, trigger phrases, step-by-step instructions, and examples.

### Step 4: Understand the SKILL.md structure

Here's what a good skill looks like under the hood:

```yaml
---
name: your-skill-name
description: [What it does]. Use when user [trigger phrases]. Use for [key tasks].
---

# Your Skill Name

## Quick Start
[Most important thing Claude should do first]

## Step 1: [First Major Step]
[Clear explanation of what happens]

## Step 2: [Second Major Step]
[etc.]

## Examples
**Example 1: [common scenario]**
User says: "[example request]"
Actions: [what Claude does]
Result: [what the user gets]

## Troubleshooting
**Error: [Common error]**
Cause: [Why it happens]
Solution: [How to fix]
```

⚠️ **The description field is everything.** This is how Claude decides whether to load your skill. Structure it as: `[What it does] + [When to use it] + [Key capabilities]`. Include specific trigger phrases the user would naturally say.

### Step 5: Run the three-test validation

Your skill isn't done until it passes three tests. Start a new session and run each one.

**Test 1 — Triggering:** Does it load when it should?

```
[Say something that should naturally trigger your skill — don't mention the skill name]
```

If it doesn't load: your description is too vague. Add more trigger phrases.

**Test 2 — Functional:** Does it produce correct outputs?

Run the same request 3 times. Is the output structurally consistent? Do you need to redirect or clarify?

**Test 3 — Performance:** Is it better than no skill?

Ask Claude to do the same task with and without the skill enabled. Compare the quality, number of corrections needed, and how many follow-up messages you send.

**Debugging tip:** If your skill isn't triggering, ask Claude:
```
When would you use the [skill name] skill?
```
It will quote the description back to you — and you'll see exactly what's missing.

## 🎉 What Just Happened

You just taught Claude a new capability. Skills use a 3-level progressive loading system: at startup, Claude only sees the skill name and description (~100 tokens each). When it recognizes your request matches a skill, it loads the full instructions. This means you can install dozens of skills without bloating your context window — they're lightweight until needed. Your skill folder can also include `scripts/` (executable code), `references/` (docs and schemas), and `assets/` (templates).

## Go Deeper

- **Share with your team:** Skills are just folders. Drop them in a shared repo and your whole team gets the same quality.
- **Iterate fast:** Most skills can be built and tested in 15-30 minutes using skill-creator
- **Three categories for PMs:**
  - **Document creation** — PRDs, release notes, status updates with consistent format
  - **Workflow automation** — Sprint planning, feedback analysis, competitive reviews
  - **MCP enhancement** — Add workflow guidance on top of tool access (e.g., teach Claude your Notion project setup process)
- **Skill library:** Browse community skills at [github.com/anthropics/skills](https://github.com/anthropics/skills)

## Share

Bring back: What's the one workflow you'd most want to automate? What's the trigger phrase you'd use?
