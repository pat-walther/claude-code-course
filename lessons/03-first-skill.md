# 3. Install and Trigger Your First Skill

> **Magic Moment:** You install a skill, type a normal prompt without mentioning the skill at all, and Claude *automatically* loads it and follows a structured workflow you never explained.

## Why This Matters

Right now, every time you want Claude to follow a specific process, you have to explain it from scratch. Skills fix this. A skill is a reusable instruction set that Claude loads *automatically* when it detects a relevant request. Install a skill once, and it works forever — across every conversation. Think of it as teaching Claude a new workflow it never forgets.

## Before You Start

- Claude Code installed and working (Lesson 1 ✅)
- Access to [github.com/anthropics/skills](https://github.com/anthropics/skills)

## Do This Now

### Step 1: Understand what a skill is (30 seconds)

A skill is just a folder with a `SKILL.md` file. That file has:
- A **name** and **description** (how Claude decides when to use it)
- **Instructions** (what Claude should do when the skill triggers)
- Optionally: scripts, templates, and reference docs

The magic is in the **description field** — it tells Claude *when* to activate the skill. You never have to say "use this skill." Claude reads the description and decides on its own.

### Step 2: Install the `frontend-design` skill

**Paste this into your terminal (not Claude Code — quit Claude first with `Ctrl+C` if needed):**
```
cd ~/.claude/skills 2>/dev/null || mkdir -p ~/.claude/skills && cd ~/.claude/skills
git clone https://github.com/anthropics/skills.git anthropic-skills 2>/dev/null || (cd anthropic-skills && git pull)
```

**What you should see:** The skills repo downloads (or updates if you already have it). The `frontend-design` skill is now at `~/.claude/skills/anthropic-skills/frontend-design/`.

💡 **Alternative — Claude.ai web app:** Go to Claude.ai → Settings → Capabilities → Skills → Upload skill. Download the `frontend-design` folder from [github.com/anthropics/skills](https://github.com/anthropics/skills) and upload it there.

### Step 3: Launch Claude Code in your project

**Paste this into your terminal:**
```
cd ~/pm-playground && claude
```

**What you should see:** Claude Code launches in your project folder.

### Step 4: Trigger the skill WITHOUT mentioning it 🎉

This is the magic moment. Do NOT say "use the frontend-design skill." Just describe what you want as if you're talking to a designer.

**Paste this into Claude Code:**
```
Design a settings page for a mobile app. It should have sections for Account, Notifications, Privacy, and a logout button at the bottom. Make it look like a real iOS app — clean, native-feeling, with toggle switches.
```

**What you should see:** Claude detects that this is a frontend design task, **automatically loads the `frontend-design` skill**, and follows a structured design workflow:
1. It reads the skill instructions
2. It creates a polished HTML/CSS implementation
3. The output follows the skill's design methodology — not just random code

Look for the indicator that Claude loaded the skill — it may mention reading the skill file or you'll notice the output follows a more structured, opinionated design process than a generic response would.

### Step 5: Compare — ask the same thing without the skill

Open a new conversation (type `/clear` or restart Claude Code) and ask the exact same question. Notice the difference? With the skill, Claude follows a defined design system. Without it, you get generic code. That's the power of skills.

### Step 6: Verify the skill triggered

**Paste this into Claude Code:**
```
What skills do you have available? Which one did you just use?
```

**What you should see:** Claude lists the installed skills and confirms which one it loaded for your design request. If it didn't trigger automatically, try rephrasing your prompt to include words like "design", "UI", or "frontend" — these match the skill's description.

## 🎉 What Just Happened

You installed a pre-built skill that teaches Claude a specific design workflow. When you typed a prompt that matched the skill's description, Claude *automatically* loaded it — no explicit instruction needed. The skill's description field acts as a trigger: Claude scans all installed skills at the start of each conversation, and when your prompt matches, it pulls in the full instructions. You can install dozens of skills without slowing Claude down, because it only loads the full instructions when relevant (just ~100 tokens per skill at startup). This is how you scale your AI workflows — teach Claude once, benefit forever.

## Go Deeper

- Browse more skills at [github.com/anthropics/skills](https://github.com/anthropics/skills)
- Try building your own: ask Claude "Help me build a skill for writing weekly status updates"
- Read the `SKILL.md` file of any installed skill to see how the description triggers work

## Share

**Bring back:** What's one workflow you repeat every week that would make a great skill? What trigger phrase would you use? (Example: "Generate sprint retro notes" → triggers a retro-notes skill)
