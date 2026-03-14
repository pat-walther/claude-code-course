# 11. Build Many Ideas at Once

> **Magic Moment:** You give Claude three different feature directions, it builds all three as separate prototypes, and you compare them side-by-side in your browser — making product decisions by reacting to real, working things instead of abstract discussions.

## Why This Matters

The old way: spend a week debating which direction to go, pick one, build it, realize it was wrong, start over. The new way: build all three in parallel, compare them, and pick the winner. When prototypes are cheap (minutes, not sprints), exploring multiple directions isn't wasteful — it's smart. This is creative selection: generate many options, react to them, combine the best parts.

## Before You Start

- [ ] Claude Code open in your project folder
- [ ] Your `design.md` and `CLAUDE.md` files set up (from Lessons 6 and 8)
- [ ] An open design question — something where you're genuinely unsure which direction to go

## Do This Now

### Step 1: Build three versions in one prompt

Pick a feature you're considering. Don't pick the "right" approach — that's the whole point. Let Claude build three genuinely different takes.

**Paste this into Claude Code:**
```
I want to explore 3 different approaches to [describe your feature — e.g., "an onboarding flow for new users" or "a settings page" or "a pricing comparison view"].

Build each as a separate HTML file (version-a.html, version-b.html, version-c.html).
Follow design.md for visual style.

Make them genuinely different from each other — not just color variations:
- Version A: Optimize for speed — fewest clicks, least friction, get users to the value fast
- Version B: Optimize for comprehension — more explanation, guided steps, nothing is confusing
- Version C: Optimize for delight — animations, personality, make it feel premium and polished

For each version, add a comment at the top of the file explaining the design philosophy and main tradeoff.
```

**What you should see:** Three separate HTML files, each taking a fundamentally different approach to the same problem. They'll share your design system (colors, typography) but differ in layout, flow, and priorities.

### Step 2: Compare them side-by-side

**Open all three in your browser.** Arrange them side by side (or use separate tabs and flip between them).

**What you should see:** 🎉 **This is the magic moment.** Three working prototypes of the same feature, each with a different philosophy. You're not comparing mockups or wireframes — you're clicking through real, interactive versions. Your gut reaction tells you more than any debate ever could.

Notice what happens: you'll probably like the flow from Version A, a visual element from Version C, and the copy from Version B. That's the whole point — you're not picking a winner, you're shopping for the best parts.

### Step 3: Combine the best parts

**Paste this into Claude Code (with screenshots if helpful):**
```
I've looked at all three versions. Here's what I want to combine:
- The overall layout and flow from Version A (it's the fastest)
- The explanation tooltips from Version B (they help new users without slowing down power users)
- The hover animations and card styling from Version C (they make it feel polished)

Build the combined version as version-final.html. Take the best of each — this should feel like the obvious right answer.
```

**What you should see:** A fourth prototype that cherry-picks the best elements from all three. This is creative selection in action — generate options, react, combine.

### Step 4: Run true parallel explorations

For even bigger design questions, you can run Claude Code sessions in parallel — truly simultaneous exploration.

**Open two or three separate terminal windows, each running Claude Code in your project folder. Give each a different brief:**

**Terminal 1:**
```
Read design.md and CLAUDE.md. Build a prototype for [your feature] optimized for first-time mobile users. Save as explore-mobile.html.
```

**Terminal 2:**
```
Read design.md and CLAUDE.md. Build a prototype for [your feature] optimized for power users who use this daily. Save as explore-power.html.
```

**Terminal 3:**
```
Read design.md and CLAUDE.md. Build a prototype for [your feature] that's radically simple — try to solve it with a single screen and no more than 3 interactive elements. Save as explore-minimal.html.
```

They run simultaneously. In 3-5 minutes, you have three fundamentally different explorations — each informed by your design system.

### Step 5: Steal from the best

One powerful variation: use external inspiration as context.

**Find a product you admire that solves a similar problem.** Screenshot their approach, then:

**Paste the screenshot into Claude Code:**
```
I love how [product name] handles this. Look at this screenshot. Build something inspired by this approach, adapted for my product. Follow my design.md for colors and typography, but borrow their layout and interaction patterns. Save as inspired-version.html.
```

**What you should see:** A prototype that combines your brand with another product's design patterns. This is how professional designers work — they reference what works and adapt it.

## 🎉 What Just Happened

You stopped treating prototyping as a linear process (design → debate → build → test → repeat) and started treating it as an exploration (build three → react → combine → build more). When prototypes take minutes instead of sprints, there's no reason to agonize over "the right direction" upfront. Build them all. React to real things. Combine what works.

The key insight: your gut reaction to a working prototype tells you more than any amount of planning. When you see Version C's animations, you either feel "yes, that's us" or "no, that's too much." That instinct is valid — and now you can test it in minutes.

## Go Deeper

- **The homework challenge:** Build 5 different prototypes in one sitting. Not 5 tweaks on one idea — 5 genuinely different features or approaches. Time yourself. Most people find they can do it in under 30 minutes.
- **A/B test your prototypes:** Share two versions with a colleague or friend: `"Which one would you click? Why?"` Their answer is more valuable than any framework.
- **Use external context:** Paste a blog post, product review, or Lenny's Newsletter excerpt into Claude and ask: `"Based on this article, give me 3 ideas on how to improve my app. Build a quick prototype of the best one."`
- **Different devices:** Ask Claude to build the same feature for desktop, tablet, and mobile as three separate prototypes. You'll spot responsive design problems immediately.
- **Copy a component you love:** See a beautiful card layout, pricing table, or navigation pattern on another site? Screenshot it and say: `"Recreate this component in my design system. Save it as a reusable HTML snippet I can paste into future prototypes."`

## Share

**Bring back:** Your 3 versions and which direction you chose. What made you choose it over the others?
