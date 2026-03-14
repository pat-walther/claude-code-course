# 14. MCP Servers, Docs, and External Context

> **Magic Moment:** You connect an MCP server and Claude suddenly has capabilities it didn't have before — reading your Figma designs, querying live documentation, or pulling data from your tools — without leaving the terminal.

## Why This Matters

Claude Code is powerful out of the box, but it's limited to what's in your project folder and what it already knows. MCP (Model Context Protocol) servers are like giving Claude new superpowers: connect Figma and it can read your designs. Connect Notion and it can pull from your wiki. Connect a docs server and it always uses the latest API documentation. For PMs, this is the difference between Claude being a clever assistant and Claude being a *connected* team member.

## Before You Start

- Claude Code open in your project directory
- Terminal access for running `claude mcp add` commands
- Accounts for any tools you want to connect (Figma, Notion, etc.)

## Do This Now

### Step 1: Understand what MCP is (30-second version)

MCP stands for **Model Context Protocol**. Here's the simple explanation:

- **Without MCP:** Claude can only work with files on your computer and its training knowledge
- **With MCP:** Claude can reach out to external tools — Figma, Notion, Sentry, databases — and use them directly

Think of MCP servers as *adapters*. Each one teaches Claude how to talk to a specific tool. You install them once, and Claude can use them in every session.

💡 **Start here:** Check [claude.ai/directory](https://claude.ai/directory) first. Many tools can be connected with one click using OAuth — no command-line setup needed. Only use the manual setup below if your tool isn't in the directory.

### Step 2: Install your first MCP server — Figma

Figma MCP gives Claude the ability to read your designs, extract structured layout data, and pull screenshots of specific frames. This is game-changing for PMs who work with designers.

**Run this in your terminal (outside Claude Code):**
```bash
claude mcp add --transport http figma https://mcp.figma.com/mcp
```

Now restart Claude Code (`Ctrl + C`, then `claude` to relaunch).

**Paste this into Claude Code:**
```
/mcp
```

**What you should see:** Claude Code shows your installed MCP servers. Click **Connect** next to Figma and authenticate with your Figma account. Once connected, you'll see Figma listed as active.

Now test it:

**Paste this into Claude Code:**
```
Use the Figma MCP to read this design: [paste any Figma URL here]
Describe what you see — the layout, colors, and components.
```

**What you should see:** 🎉 Claude describes your Figma design in detail — without you taking a single screenshot. It can see the layers, read the text, identify colors and spacing.

### Step 3: Add Context7 for live documentation

Context7 is an MCP server that gives Claude access to up-to-date documentation for popular libraries and frameworks. No more Claude using outdated API methods.

**Run this in your terminal:**
```bash
claude mcp add --transport http context7 https://mcp.context7.com/mcp
```

Restart Claude Code, then test it:

**Paste this into Claude Code:**
```
Use Context7 to look up the latest Tailwind CSS documentation for their color utilities. Then use those exact utilities to style a card component.
```

**What you should see:** Claude fetches *current* documentation instead of relying on its training data. This matters when libraries update frequently — you get working code, not deprecated patterns.

### Step 4: Add one more server for your workflow

Pick the MCP server most relevant to your work:

**For Notion users (access your wiki and docs):**
```bash
claude mcp add --scope user --transport http notion https://mcp.notion.com/mcp
```

**For Playwright (automated browser testing and iteration):**
```bash
claude mcp add --scope user playwright npx '@playwright/mcp@latest'
```

**For Sentry (error monitoring):**
```bash
claude mcp add --scope user --transport http sentry https://mcp.sentry.dev/mcp
```

After installing, always restart Claude Code and run `/mcp` to authenticate.

**Verify everything's connected:**
```bash
claude mcp list
```

**What you should see:** A list of all your installed MCP servers and their connection status.

### Step 5: Keep Claude smart across long sessions

Now that Claude has access to external tools, it's doing more work per session — which fills up its context window faster. Here are three techniques to keep it sharp:

**Compact at ~60% context usage:**

When Claude starts contradicting itself or producing worse output, it's time to compact:

**Paste this into Claude Code:**
```
Write everything we've done so far to progress.md. Include: the end goal, the approach we're taking, what we've completed, and the current problem we're working on. Be specific.
```

Then start a new session and open with: *"Read progress.md and continue where we left off."*

**Use subagents for research:**

Instead of letting research clutter your main session:

**Paste this into Claude Code:**
```
Before we start building, spin up a subagent to explore how [feature X] currently works in the codebase. Have it return a summary of the relevant files and how they connect — then we'll use that to plan the work.
```

**Follow the research → plan → build workflow:**

1. **Research:** "Explore the codebase and summarize how [X] works. Write to research.md." → You review and correct
2. **Plan:** "Based on research.md, write a step-by-step plan to build [feature]." → You review the approach
3. **Build:** "Follow plan.md, phase by phase. Check in after each phase." → Claude builds, you verify

⚠️ **The key insight:** Errors amplify upstream. A wrong assumption in research leads to a wrong plan, which leads to dozens of wrong lines of code. Review the research and the plan — not the final output. That's where your PM judgment has the highest leverage.

## 🎉 What Just Happened

You gave Claude Code external capabilities by connecting MCP servers. Figma MCP lets it read designs directly. Context7 gives it access to current documentation. And you learned context management techniques — compacting, subagents, and the research-plan-build workflow — that keep Claude performing at its best across long sessions. These aren't just Claude Code skills; they're the foundation of working effectively with any AI coding agent.

## Go Deeper

- [claude.ai/directory](https://claude.ai/directory) — one-click OAuth connections for popular tools
- [Claude Code MCP Docs](https://code.claude.com/docs/en/mcp) — official setup guide for manual MCP configuration
- [Effective Context Engineering for AI Agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) — Anthropic's deep dive on context management
- [Equipping Agents with Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills) — how Anthropic thinks about agent capabilities
- [Advanced Context Engineering](https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/ace-fca.md) — community guide to keeping agents smart
- 📺 [YouTube: Context Management for Coding Agents](https://www.youtube.com/watch?v=rmvDxxNubIg) — video walkthrough

## Share

**Bring back:** Which MCP server did you connect, and what's the first thing you used it for? Bonus: share a screenshot of your `/mcp` output showing your connected servers.
