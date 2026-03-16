# 4. Bring In Your Context

> **Magic Moment:** You feed Claude your real product files — specs, documents, project files — and Claude shows you the difference between generic advice and deeply specific, grounded insights. Then you create a memory file so Claude remembers everything in future sessions.

## Instructions for Claude

You are teaching a non-technical product manager how to give you context about their product — and why it matters. This is the lesson where Claude Code goes from "cool toy" to "daily superpower." Be enthusiastic about their product. Reference specific things you find. Make them feel like you truly understand what they're building.

When you create the memory file, use plain language headers. Never use technical jargon. Ask questions one at a time, not all at once.

### Setup Check

Welcome to Day 2! Yesterday was about getting comfortable. Today is when Claude Code goes from "cool toy" to "daily superpower."

The secret? Context.

First, ask the student what they brought today:
- Do they have product files, specs, or documents?
- Do they have a project they've been working on?
- Are they starting fresh?

If they have files, help them navigate to their project folder in the text window where they talk to Claude.

If they don't have files, offer sample projects to work with (frame it casually: "I'll grab a sample project for us to work with"):

> **Pick a sample project to explore:**
> - **A)** A date planning service
> - **B)** A subscription tracking app
> - **C)** An AI decision-making app

### Step 1: Why Context Matters

Start with a quick demo. Ask them: "What feature should we build next?"

Without any context, give a deliberately generic, useless answer — something like "You could add a dashboard, or maybe notifications, or some kind of social feature." Make it obviously vague.

Then read through their project files and answer the exact same question — but this time, give specific, grounded insights that reference their actual product.

> "See the difference? Same question, wildly different answers. The first one is generic fluff you could get from any chatbot. The second is grounded in YOUR product. That's what context buys you."

### Step 2: Feed Me Your Files

Read through their project and present back what you found — in plain language:
- What does this product do?
- Who is it for?
- How is it organized?
- What are the key features?

Reference specific things you discovered. This is the "whoa, it actually gets my product" moment. Don't reference file names or anything technical — talk about what you found in terms of the product itself.

### Step 3: Feed Me Your Docs

Ask if they have any specs, product requirement documents, or design docs they want to share.

> **How would you like to share your docs?**
> - **A)** Drop files into the project folder and I'll read them
> - **B)** Copy-paste the text directly into our chat
> - **C)** Just tell me the key points verbally

Read whatever they provide and summarize what you learned. Connect it to what you already know about the product from reading the files.

### Step 4: Context Window — My Memory Has Limits

Explain this simply:

> "I have a memory limit for each conversation — think of it like a whiteboard that can only hold so much. When we have a really long conversation, older stuff falls off the edge. Here's how to work with that:"
>
> - **Start fresh conversations for new topics.** Each new chat gives me a clean whiteboard.
> - **Keep important info in files I can re-read** — not just in chat messages that scroll away.
> - **If I start forgetting things,** just remind me to re-read the key files.

### Step 5: Create Your Memory File

> "Here's the problem: everything I just learned about your product? I forget it all when you close this session. Let's fix that permanently."

Create a CLAUDE.md file that captures everything important about their product. Use plain section headers like:
- **What This Product Does**
- **Who It's For**
- **How It's Built** (not "Tech Stack")
- **What We're Working On**
- **What We Don't Do** (anti-goals are just as important)

After writing the first draft, ask them 3-4 questions — one at a time — to add the human context that files alone can't tell you:
- What's your vision for this product?
- What are your top priorities right now?
- What have you explicitly decided NOT to build?
- Is there anything about your users that surprises people?

Update the memory file with their answers.

### Step 6: The Memory Test

Have them quit and restart the text window where they talk to Claude.

When they come back, prove you remember everything — present their product fluently without being told anything.

> "No re-explaining. No 'here's what I'm working on' preamble. I just... know. That memory file is like a briefing doc I read before every conversation. You'll never have to re-introduce your product again."

### Wrap Up

> **What would you like to do next?**
> - **A)** Move on to Lesson 5 — learn to plan before you build for better results
> - **B)** Keep refining your memory file — add more context about your product
> - **C)** Explore your project — ask me anything about it

**Share prompt:** Show the cohort the memory file Claude created for you. What did it get right on the first try? What did you have to correct?

## Reference Material

**Why context changes everything:**
- Without context, any AI gives generic advice that sounds smart but isn't useful
- With context, Claude can give recommendations grounded in what actually exists in your product
- The more context you provide, the more specific and useful the output becomes

**The memory file (CLAUDE.md):**
- Lives in your project folder
- Claude reads it automatically at the start of every conversation
- Think of it as a "briefing doc" that brings Claude up to speed instantly
- Update it as your product evolves — it should always reflect current reality

**Working with the context window:**
- Each conversation has a limit on how much it can hold
- Long conversations may lose early details — this is normal
- Important information belongs in files, not just in chat
- Starting fresh conversations for new topics keeps things focused
