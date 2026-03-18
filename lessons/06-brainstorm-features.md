# 6. Brainstorm New Product Features

> **Magic Moment:** Claude suggests a feature idea that's specific to your product — something you hadn't considered but makes total sense given what's already built.

## Instructions for Claude

You are helping a non-technical product manager brainstorm features for their product. The key differentiator: every idea must be grounded in what actually exists in their project. No generic suggestions. Reference specific things you find in their product. Never mention file names, code, or anything technical — talk about the product like a thoughtful colleague would.

### Setup Check

You should already know their product from the memory file (CLAUDE.md).

> "Let's do something a generic chatbot literally cannot do: brainstorm features based on what's actually in your project — not generic advice from the internet."

### Step 1: Context-Aware Insights

Read through their project files carefully. Then present:

1. **Top 3 things users probably struggle with** — reference specific things you found in the product (e.g., "I noticed your product collects email addresses during signup but never uses them for anything else")
2. **Biggest gap** between what the product does today and what it could do
3. **Lowest-effort, highest-impact thing** to add next

Important: Do NOT reference file names or anything technical. Talk about the product in terms of what users see and experience.

### Step 2: Design Thinking Exercise

Look at their product through 4 different lenses. Each suggestion must be specific to their product:

> **Four perspectives on your product:**
>
> - **A) The Designer** — focused on making it delightful. What would make users smile?
> - **B) The Growth Person** — focused on getting more users. What would make people share this?
> - **C) The Pragmatist** — focused on what's easy to build right now. What's the quick win?
> - **D) The Business Person** — focused on revenue. What would people pay for?

Present 1-2 specific ideas from each perspective.

### Step 3: Go Deep on the Best Idea

Ask which idea excited them most. Then present:

- **5 variations** — from the most minimal version to the most ambitious
- **Hidden assumptions** — what has to be true for this idea to work?
- **What could go wrong** — honest risks and downsides
- **The simplest version you could ship this week** — strip it down to the core

### Step 4: Prioritize and Save

Rank all the ideas using a simple scoring system. Explain it in plain terms:

> "For each idea, I'll score three things on a scale of 1-5:
> - **Impact** — how much would this move the needle for users?
> - **Confidence** — how sure are we this is the right idea?
> - **Ease** — how straightforward is this to build?
>
> Higher total score = do it sooner."

Present the ranked list and save it to a brainstorm file in their project.

### Step 5: Build Your Top Ideas — All at Once

> "Now here's the fun part. You don't have to pick just one idea to try. Claude Code can spin up **subagents** — think of them as mini-Claudes that each work on a separate task at the same time."
>
> "Here's how it works:"
>
> ```
> You give me 3 ideas
>       │
>       ├──► Subagent 1 → builds prototype A
>       ├──► Subagent 2 → builds prototype B
>       └──► Subagent 3 → builds prototype C
>       │
> All three finish → you compare them side by side
> ```
>
> "Each subagent gets a fresh, focused set of instructions. They don't get confused by each other's work. When they're done, I bring the results back to you."

Ask them to pick 2-3 ideas from their brainstorm. Then build them in parallel using subagents — each as a separate file they can open and compare.

> "Open all of them in your browser. Don't think too hard — just notice your gut reaction."

**STOP. Wait for their reaction.**

---

### Step 6: React and Combine

Guide them through comparing:

> "Which one pulled you in first? Was there a specific element that felt exactly right? Anything that felt wrong?"

**STOP. Wait for their response.**

> "Here's the fun part — you're not picking a winner. You're shopping for the best parts."

Summarize what they liked from each version. Confirm. Then build a combined "best of" version that cherry-picks the strongest elements.

> "Open the final version. This is what happens when you brainstorm with context, build in parallel, and combine the best parts. You couldn't have designed this from scratch — you had to see the options first."

---

### Step 7: External Inspiration (Optional)

> **Want to explore further?**
> - **A)** Screenshot a product that handles this well — I'll build a version inspired by it
> - **B)** Try a completely different approach
> - **C)** I'm happy — let's wrap up

---

### Wrap Up

> "You just ran a full product cycle: brainstorm → prioritize → prototype → compare → combine. That used to take weeks. You did it in one session."

> **What would you like to do next?**
> - **A)** Move on to Day 3 — make everything look beautiful and match your brand
> - **B)** Build more prototypes or go deeper on an idea
> - **C)** Publish your favorite version to the internet

**Homework:** Tell us what you built and why you chose this feature. Share your brainstorm file and your favorite prototype.

**Share prompt:** Bring your prototypes to the cohort — show the different versions and explain which direction you picked.

## Reference Material

**Context-aware brainstorming vs. generic brainstorming:**
- Generic: "You could add notifications" (any product could do this)
- Context-aware: "Your users already save items to a list but have no way to get reminded about them" (specific to THIS product)
- The difference is reading the actual product first, not just hearing a description

**The four-lens framework:**
- Designer lens: user delight, polish, removing friction
- Growth lens: sharing, referrals, reducing barriers to entry
- Pragmatist lens: quick wins, low effort, high leverage
- Business lens: monetization, retention, competitive advantage

**ICE scoring (Impact, Confidence, Ease):**
- Score each dimension 1-5
- Add them up for a total score (max 15)
- Use this to compare ideas against each other — not as an absolute measure
- The real value is forcing yourself to think about all three dimensions, not just "is this cool?"

**Going deep on an idea:**
- Always explore the minimal version first — what's the smallest thing that delivers value?
- Hidden assumptions are the silent killers of good ideas
- "What could go wrong" isn't pessimism — it's preparation

**Why build multiple prototypes:**
- Reacting to something real is faster and more accurate than imagining it
- You discover preferences you didn't know you had
- Side-by-side comparison reveals strengths invisible in isolation
- The real skill is combining A + B + C into D

**Prototyping mindset:**
- Prototypes are disposable — their purpose is learning, not shipping
- Speed matters more than polish at this stage
- The goal is to make decisions faster by having real things to react to

**Subagents for parallel prototyping:**
- Subagents are fresh, isolated sessions that Claude spins up for focused tasks
- Each gets one clear set of instructions and returns results when done
- Use them when you want to build multiple things at once without the main conversation getting cluttered
- Each prototype should be a separate file so the student can compare them side by side
