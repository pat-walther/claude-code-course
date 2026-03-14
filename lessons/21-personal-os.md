# 21. Build Your Personal OS

> **Magic Moment:** You create USER.md and SOUL.md, start a fresh Claude session, and it responds in your preferred style without being told — it already knows who you are and how you communicate.

## Why This Matters

Every Claude session starts from scratch. You re-explain who you are, what you're building, how you like to communicate. That's not just annoying — it's hours of wasted context per week. Two files fix this permanently. Write them once, and every future session starts with Claude already knowing you.

## Before You Start

- Claude Code open in your terminal
- A quiet 15 minutes to think about how you actually work (not how you think you should work)

## Do This Now

### Step 1: Clone the Personal OS template

There's a ready-made template that gives you the right file structure. Let Claude set it up for you.

**Paste this into Claude Code:**
```
Download this repo for me locally and get started with it: https://github.com/amanaiproduct/personal-os
```

**What you should see:** Claude clones the repo and walks you through the file structure — you'll see `GOALS.md`, a `knowledge/` folder, and the skeleton for your personal agent workspace.

### Step 2: Create your USER.md

This is the most important file. It tells Claude who you are so you never have to explain yourself again. Instead of writing it yourself, let Claude interview you.

**Paste this into Claude Code:**
```
Help me write my USER.md file. Ask me these questions one at a time:
1. What's your name and job title?
2. What product are you building and who is it for?
3. How do you like to communicate — terse and direct, or detailed and explanatory?
4. What are you working on right now?
5. What are your biggest recurring tasks?

Then compile my answers into a USER.md file I can save to my computer.
```

**What you should see:** Claude asks you questions one by one, then generates a clean USER.md with sections like `## About Me`, `## Current Work`, `## Communication Style`. Answer honestly — this is for you, not a job application.

💡 **Tip:** Include your timezone, your tech stack, and even pet peeves. "Don't say 'Great question!'" is a perfectly valid preference.

### Step 3: Create your SOUL.md

SOUL.md defines how Claude writes and thinks when it works with you. This is where you kill AI slop.

**Paste this into Claude Code:**
```
Now help me create a SOUL.md file. This defines your personality and writing style when working with me. Based on what you learned about me in USER.md, draft a SOUL.md that includes:

1. Writing style rules (e.g., "Be direct. No filler phrases. No 'Great question!'")
2. Response format preferences (e.g., "Use bullet points for lists, not paragraphs")
3. Things to never do (e.g., "Never apologize for not being able to do something — just explain what you can do instead")
4. Tone (e.g., "Casual but competent. Like a smart coworker, not a corporate chatbot.")

Show me what you've got, then I'll tweak it.
```

**What you should see:** A SOUL.md file that reads like instructions you'd give a new hire on day one. Edit it until it sounds right — this is the difference between AI slop and genuinely useful output.

### Step 4: Create your AGENTS.md

AGENTS.md tells Claude how to behave in your workspace — when to ask for approval, how to handle files, what to read at the start of every session.

**Paste this into Claude Code:**
```
Create an AGENTS.md file for my workspace. It should tell Claude to:

1. Read USER.md and SOUL.md at the start of every session
2. Keep responses concise unless I ask for detail
3. Ask before making changes to files outside the current project
4. Log important decisions and context to a memory/ folder
5. Never share personal info from USER.md in group contexts

Keep it under 50 lines. Practical, not philosophical.
```

**What you should see:** A clean, scannable AGENTS.md that acts as your workspace rulebook.

### Step 5: Test it — the magic moment

Now for the payoff. Start a completely fresh Claude session and see the difference.

**Close your current Claude Code session, then open a new one in the same directory. Paste this:**
```
What do you know about me and how I like to work?
```

**What you should see:** Claude references your name, your product, your communication style, your current projects — without you telling it anything. It already read USER.md, SOUL.md, and AGENTS.md. 🎉

Now try asking it to write something:
```
Draft a quick Slack message to my team about this week's priorities.
```

Notice the difference. No corporate speak. No "I hope this message finds you well." It writes like *you* told it to write.

## 🎉 What Just Happened

Claude Code automatically reads markdown files in your workspace at the start of every session. By creating USER.md (who you are), SOUL.md (how to communicate), and AGENTS.md (workspace rules), you gave Claude persistent memory of your preferences. These files are just text — you can version them, share them with your team, or evolve them over time. The more specific you are, the less you'll ever need to correct Claude again.

## Go Deeper

- **Add a knowledge/ folder:** Drop in PDFs, strategy docs, meeting notes, designs — anything Claude might need for open-ended work
- **Set up GOALS.md:** Define your quarterly objectives so Claude can help you prioritize
- **Template repo:** [github.com/amanaiproduct/personal-os](https://github.com/amanaiproduct/personal-os)
- **Iterate constantly:** Every time Claude does something you don't like, add a rule to SOUL.md. Within a week, it'll feel like a different tool.

## Share

Bring back: one line from your USER.md that you think will most change how Claude responds to you.
