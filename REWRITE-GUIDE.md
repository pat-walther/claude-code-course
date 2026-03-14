# Lesson Rewrite Guide: "Claude Teaches You" Format

## The Problem With the Current Format
Current lessons say "Paste this into Claude Code:" with copy-paste prompts. That's a reference doc, not an interactive experience. If someone tells Claude "teach me this file," Claude just reads the prompts aloud.

## The New Format
Each lesson is written AS INSTRUCTIONS TO CLAUDE about how to teach the student. The student opens Claude Code, pastes or references the lesson file, and says "teach me this." Claude then RUNS the lesson interactively: asking questions, building things, explaining as it goes.

## Structure for Every Lesson

```markdown
# [Number]. [Title]

> **Magic Moment:** [What the student will experience]

---

## Instructions for Claude

You are teaching an interactive lesson. Follow these steps in order. Be conversational, encouraging, and concise. Don't dump walls of text. Do one step at a time and wait for the student to respond before moving on.

### Setup Check
[Check prerequisites. Ask if they're ready. Don't proceed until confirmed.]

### Step 1: [Name]
**What to do:** [What Claude should do — ask a question, build something, explain a concept]
**What to say:** [Suggested dialogue — Claude can rephrase but should hit these points]
**Then:** [Wait for response / build something / show output]

### Step 2: [Name]
...

### The Magic Moment (Step N)
**What to do:** [The step where the wow happens]
**What to say:** [Frame it — "Watch this..." or "Now try asking me..."]
**Then:** [Do the impressive thing]

### Wrap Up
**What to say:** [Brief explanation of what happened and why it matters]
**Share prompt:** [Give them something to bring back to the cohort]

---

## Reference Material
[Context Claude might need: links, data, templates. NOT for the student to read — for Claude to use during the lesson.]
```

## Key Principles

1. **Claude DOES, not TELLS.** Instead of "paste this prompt," Claude just does the thing. Instead of "you should see X," Claude shows them X.

2. **Conversational flow.** Claude asks questions, reacts to answers, adapts. "What product are you building?" then uses their answer in the next step.

3. **One step at a time.** Never dump 5 steps at once. Do one, wait for response, do the next.

4. **The student's project is the content.** Wherever possible, Claude works on THEIR codebase, THEIR data, THEIR product. Not a generic example.

5. **Fallback examples.** If the student doesn't have their own data/project, provide a fallback: "If you don't have a project yet, I'll use a sample one."

6. **Fun and personality.** Claude should celebrate wins ("🎉 Look at that!"), be honest about limitations ("This part isn't perfect yet — let's iterate"), and keep energy high.

7. **No meta-narration.** Claude should NOT say "According to the lesson file, step 3 says..." — it should feel natural, like a knowledgeable teacher who happens to know exactly what to show next.

## What Changes From Current Lessons

| Current (Runbook) | New (Claude Teaches) |
|---|---|
| "Paste this into Claude Code:" | Claude just runs the prompt itself |
| "What you should see:" | Claude shows them and explains |
| "Why This Matters" section for student to read | Claude explains this conversationally at the right moment |
| "Go Deeper" links at the end | Claude offers these as options: "Want to go deeper? I can show you..." |
| Generic example project | Claude asks "What are you building?" and uses their answer |
| Student drives | Claude drives, student responds and reacts |
