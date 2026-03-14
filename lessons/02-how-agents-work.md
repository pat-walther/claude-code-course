# 2. How Agents Actually Work

> **Magic Moment:** You watch Claude's thinking process in real-time and realize it's not magic — it's a loop of "think → use tools → think again" that you can steer.

## Why This Matters

When Claude gives you a weird result, your instinct might be "AI is dumb." But 90% of the time, the problem is *context* — Claude didn't have the right information. Understanding the agent loop turns you from someone who gets frustrated at AI into someone who knows exactly which lever to pull. This mental model will save you hours over the rest of the course.

## Before You Start

- Claude Code installed and working (Lesson 1 ✅)
- Your `pm-playground` folder from the previous lesson

## Do This Now

### Step 1: Watch the agent loop in action

**Paste this into Claude Code:**
```
How many files are in this directory, what are their sizes, and which one was modified most recently?
```

**What you should see:** Claude doesn't just guess — watch carefully:
1. It **thinks** about what it needs to do
2. It **calls a tool** (runs `ls -la` or similar command in your terminal)
3. It **reads the result** from that tool
4. It **thinks again** and formulates its answer

This is the agent loop: **Think → Tool → Think → Respond**. Every single thing Claude does follows this pattern.

### Step 2: See the loop run multiple times

**Paste this into Claude Code:**
```
Read the index.html file, tell me how many lines of CSS vs JavaScript it contains, and suggest one improvement to the design
```

**What you should see:** Claude runs *multiple* loops:
- Loop 1: Read the file (tool: `read_file`)
- Loop 2: Analyze the contents (thinking)
- Loop 3: Respond with the counts and a suggestion

Notice how each tool call gives Claude new information that shapes its next step. It's not one giant brain dump — it's iterative.

### Step 3: See what happens with bad context

**Paste this into Claude Code:**
```
What does our API return for the /users endpoint?
```

**What you should see:** Claude will either admit it doesn't know, or try to look for API-related files in your project. It won't find any because this is a simple HTML project. This is the key insight: **Claude can only work with the context it has.** No API docs in the project = no useful answer about your API.

💡 **This is the #1 lesson:** Whenever Claude gives you a bad answer, ask yourself: "What context does my best engineer have that Claude doesn't?" Then give Claude that context.

## 🎉 What Just Happened

You just saw the inner workings of a coding agent. It's not one magical step — it's a loop: the LLM thinks, decides to use a tool (read a file, run a command, search the web), gets the result, and thinks again. This loop can run dozens of times for a single prompt. The quality of Claude's output depends on what goes *into* this loop — your prompt, the files it can see, and the tools it has access to. This is called **context engineering**, and it's the core skill of the entire course.

## Go Deeper

- [Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents) — Anthropic's own guide to the agent pattern
- [Effective Context Engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) — How to feed agents better information

## Share

**Bring back:** What's one thing you now understand about *why* Claude sometimes gives bad answers? One sentence.
