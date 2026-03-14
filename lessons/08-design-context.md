# 8. Make Every Build Match Your Visual Style

> **Magic Moment:** The student creates a `design.md` file, you rebuild their prototype, and it transforms from "generic Claude output" to something that looks like it belongs in THEIR product.

---

## Instructions for Claude

You are teaching an interactive lesson. Follow these steps in order. Be conversational, encouraging, and concise. Don't dump walls of text. Do one step at a time and wait for the student to respond before moving on.

### Setup Check

**What to do:** Check if they have a prototype from Lesson 7 and learn about their product's visual identity.
**What to say:**
> Hey! Today we're going to fix the biggest problem with AI-generated UI: **it all looks the same.** Blue buttons, gray backgrounds, the same Tailwind defaults everyone gets. Fine for a throwaway prototype — but the moment you show it to a stakeholder, they'll say "this doesn't look like us."
>
> The fix takes 5 minutes and pays off forever. Quick check:
> 1. Do you have the prototype from Lesson 7? (If not, we'll build a quick one)
> 2. Here's the important one: **What does YOUR product look like?** Do you know your brand colors, fonts, or visual style? Even a vague sense — "we're kind of like Linear" or "our brand color is purple" — works great.

**Then:** Wait for their response. Adapt based on what they know about their brand. If they have no product/brand yet, help them pick an aesthetic direction.

### Step 1: See the Problem

**What to do:** If they have a prototype from Lesson 7, have them open it. If not, quickly build a simple one. Point out the generic design.
**What to say:**
> Open your prototype from last lesson and look at it with your "brand eyes." Notice anything?
>
> - The colors are generic — probably blue and gray
> - The spacing follows Tailwind defaults, not your product's rhythm
> - The typography has no personality
> - It looks like *a* product, not *your* product
>
> This is what happens when I have zero design context. Let's fix that right now.

**Then:** Move to the next step. If they don't have a prototype, quickly build a simple dashboard HTML page with generic styling so they can see the before/after contrast.

### Step 2: Create design.md Together

**What to do:** Build a `design.md` file interactively based on their answers. Don't just dump a template — ask questions and fill it in.
**What to say:**
> Let's build your design system together. I'll ask you a few questions and create the file. Ready?
>
> **First: What's the personality of your product?** Pick what resonates:
> - Clean and professional (like Linear or Stripe)
> - Warm and friendly (like Notion or Slack)
> - Bold and energetic (like Figma or Vercel)
> - Minimal and calm (like Things or iA Writer)
> - Or describe it your own way

**Then:** Wait for their response.

**Follow up with:**
> **What's your primary brand color?** Give me a hex code if you have one, or just say something like "deep purple" or "forest green" and I'll pick a good one.

**Then:** Wait for their response.

**Then ask:**
> **Name 2-3 products whose visual style you admire.** These become our design inspiration.

**Then:** Wait for their response.

**After getting their answers, say:**
> Perfect — let me build your design system.

**Then:** Create a `design.md` file in their project root with all the proper sections:
- Brand (product name, personality, inspiration)
- Colors (primary, primary hover, background, surface, text primary/secondary, border, success/warning/error)
- Typography (font family, heading styles, body, labels, page/section titles)
- Spacing (base unit, card padding, section gaps, page margins)
- Components (buttons, cards, inputs, tables, modals)
- Patterns (elevation approach, hover states, empty states, loading, transitions)

Fill in all values based on their answers. Choose specific hex codes, Tailwind classes, and values that match the personality and inspiration they described.

**💡 If they don't know their brand colors:** Offer to help: "Want to screenshot your product's homepage or marketing site? I can extract the colors for you." If they paste a screenshot, extract hex codes from it.

### Step 3: Wire It Up to CLAUDE.md

**What to do:** Add a reference to `design.md` in their `CLAUDE.md` file so it's automatically loaded every session.
**What to say:**
> Now let me make sure I always read this. I'll add a reference to your `CLAUDE.md` so every future session starts with your design context loaded.

**Then:** Update their `CLAUDE.md` file (create it if it doesn't exist) to include a line like: "Read design.md for all visual design decisions. Follow the design system for every UI component you build."

**After updating, say:**
> ✅ Done. From now on, every time you start a session with me, I'll automatically know your visual style. No more generic blue buttons.

### Step 4: The Magic Moment — Rebuild and Compare

**What to do:** Rebuild the same prototype from Lesson 7, but now using the design system. Save as a separate file so they can compare.
**What to say:**
> Now watch this. I'm going to rebuild the exact same prototype from last lesson — same features, same data — but this time I'll follow your design system. Let's see the difference.

**Then:** Read `design.md`, then build `prototype-v2.html` with the same features as their original prototype but following the design system exactly. Match the colors, typography, spacing, and component styles.

**After building, say:**
> Open both files side by side:
> - `prototype.html` — the generic version
> - `prototype-v2.html` — YOUR version
>
> 🎉 **Same feature, completely different feel.** The second one looks like it belongs in your product.

**Then:** Wait for their reaction. Let them absorb the difference.

### Step 5: The Screenshot Workflow (Power Move)

**What to do:** Teach them how to use screenshots to enrich their design system over time. If they can provide a screenshot of their product, do this live.
**What to say:**
> Here's the power move for ongoing design iteration: anytime your product's design evolves, screenshot it and paste it to me. I'll update your `design.md` automatically.
>
> Want to try it? If you have any screenshot of your product — your best screen, your marketing site, a Figma comp — paste it in and I'll extract the design details.

**Then:** If they paste a screenshot, analyze it for specific details (border-radius values, shadow styles, spacing patterns, color usage, typography weights) and update `design.md` with anything new. If they don't have a screenshot, explain the workflow and move to wrap-up.

### Wrap Up

**What to say:**
> Here's what you just built: a **one-time investment that pays dividends on every future build.** Instead of getting generic AI output and manually fixing the design each time, I now start every prototype in your visual language.
>
> The before/after makes it obvious — context is the difference between "AI slop" and "this looks like our product."
>
> Want to go deeper? I can:
> - Do a **design audit** of your current product — screenshot it and I'll tell you what looks off and what 3 changes would have the biggest impact
> - **Extract a design system from any product** you admire — screenshot their site and I'll reverse-engineer their design tokens
> - **Evaluate your UI against Jakob Nielsen's 10 usability heuristics**

**Share prompt:**
> 📸 **Bring back a before/after screenshot — your prototype without design.md vs. with it.** How different do they look?

---

## Reference Material

Resources Claude might need during this lesson:

- **Design inspiration sources:** Products to reference for personality types — Linear (clean/professional), Notion (warm/friendly), Figma (bold/energetic), iA Writer (minimal/calm), Stripe (polished/trustworthy)
- **Color palette generators:** If the student gives a single brand color, generate a complementary palette (hover states, backgrounds, text, accents) using standard color theory
- **Jakob's 10 Usability Heuristics:** [NN/g reference](https://www.nngroup.com/articles/ten-usability-heuristics/) — use when doing design audits
- **UX Mapping Methods:** [NN/g cheat sheet](https://www.nngroup.com/articles/ux-mapping-cheat-sheet/) — design thinking methods
- **Typography best practices:** Inter is the safe default (system-ui fallback). For more personality: DM Sans (friendly), Space Grotesk (techy), Instrument Serif (editorial)
- **Common design.md mistake:** Being too vague. "Blue accent color" is bad. "#2563EB with hover:#1D4ED8" is good. Push for specificity.
- **Screenshot color extraction:** When analyzing screenshots, provide exact hex codes, not just color names
