# 8. Exercise: Install a New Skill

> **Magic Moment:** You install a skill, ask Claude a normal question, and it automatically follows a structured workflow you never explained.

## Instructions for Claude

You are running an interactive exercise where a non-technical product manager installs their first skill and sees it trigger automatically. Eric already explained what skills are in the live session. Your job is the hands-on part. Keep it jargon-free. Never mention API, CLI, JSON, YAML, git, npm, or framework. One step at a time. Wait for responses before moving on.

### Setup Check

Confirm they have Claude Code open and a project from previous lessons. If not, help them get set up first.

Say: "Let's install your first skill. This takes about 30 seconds, and after this, I'll have new capabilities you never have to explain to me."

### Step 1: Pick a Skill

Say: "First, what kind of work do you want me to get better at?"

**Pick the one that sounds most useful:**
- **A)** Making my designs and pages look more polished
- **B)** Writing cleaner, less AI-sounding content
- **C)** I want to browse what's available and pick one myself

If they pick A or B, great. Move to Step 2 with that choice.

If they pick C, point them to skills.sh or claude.com/plugins: "Take a look and tell me which one catches your eye. I'll wait."

### Step 2: Install It

Say: "Copy and paste this into Claude Code. It downloads a collection of skills that teach me new workflows."

```
/install-skill https://skills.sh
```

After installation: "I just learned a bunch of new things. Restart Claude Code so they take effect, then come back."

Wait for them to confirm they've restarted.

### Step 3: The Magic Moment

Now have them make a request that will trigger the skill naturally. Do NOT tell them which skill will activate.

Say: "Now ask me to build something. Don't mention any skill or special instructions. Just describe what you want like you normally would."

Offer suggestions if they're stuck:

**Try one of these:**
- **A)** "Design me a settings page for my product"
- **B)** "Build a dashboard showing my product's key metrics"
- **C)** Something specific to their product

Wait for their request, then build it. Follow whatever skill triggered naturally.

After building, pause and explain:

"Notice what just happened? You asked me to build a page. You didn't tell me HOW to design it. But I automatically followed a structured design process: layout choices, consistent spacing, visual hierarchy, color decisions. That's because the skill you installed activated behind the scenes when it detected your request matched its trigger. You'll never have to explain that process to me. I just know it now."

Open the result in the browser so they can see it.

### Step 4: Imagine Your Own

Say: "Skills work for any workflow you repeat. Think about your week. What's something you explain over and over, or a process you follow every time?"

Offer examples:

**Which of these sounds like something you'd use?**
- **A)** Weekly status updates: a skill that drafts them in your team's format automatically
- **B)** Spec reviews: a skill that checks specs against a quality checklist
- **C)** Sprint planning: a skill that organizes priorities into your planning template

Discuss whichever they pick. Help them picture what it would do step by step. Don't build it yet. Just plant the idea.

### Wrap Up

**What would you like to do next?**
- **A)** Move on to the next exercise: create your style guide so everything I build matches your brand
- **B)** Browse more skills at skills.sh to see what's available
- **C)** Start outlining a custom skill for your workflow

## Reference Material

**For Claude's use during this exercise:**

- Skills directory: https://skills.sh
- Anthropic plugins: https://claude.com/plugins
- Installation command: `/install-skill https://skills.sh`
- Skills are markdown files stored in the project that Claude reads automatically when a request matches the skill's trigger conditions
- The frontend-design skill guides Claude through layout choices, spacing, visual hierarchy, and consistent styling
- Custom skills follow a simple structure: a description of when to activate, and step-by-step instructions for what to do
- Students do NOT need to understand the file format
