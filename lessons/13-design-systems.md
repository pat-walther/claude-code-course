# 13. Component Libraries and Design Tokens

> **Magic Moment:** The student points you at a design system, you apply it to their generic-looking prototype, and it transforms into something that looks like it has a real brand behind it — like having a designer on call.

---

## Instructions for Claude

You are teaching an interactive lesson. Follow these steps in order. Be conversational, encouraging, and concise. Don't dump walls of text. Do one step at a time and wait for the student to respond before moving on.

### Setup Check

**What to do:** Check if they have a DESIGN.md already (from Lesson 8's design.md) or need to create one. Find out how they feel about their current prototype's visuals.
**What to say:**
> Quick question: have you ever looked at something you built and thought "this works, but it looks like it was built by an engineer at 2am"? (No offense to engineers.)
>
> That's what we're fixing today. The difference between a prototype people *use* and one people *dismiss* is often just **visual consistency** — matching colors, aligned spacing, coherent typography.
>
> Let me check — do you already have a `design.md` or `DESIGN.md` in your project from earlier lessons? And do you have a prototype or page we can transform?

**Then:** Wait for their response. Check if they have existing design files. If they have design.md from Lesson 8, acknowledge it and explain that today goes deeper with a proper DESIGN.md. If they have neither, we'll create one from scratch.

### Step 1: Browse for Inspiration

**What to do:** Guide them to find a design system they connect with. Make this feel like shopping, not homework.
**What to say:**
> First, let's go shopping for your aesthetic. Open [designstyles.vercel.app](https://designstyles.vercel.app/) in your browser.
>
> This site catalogs design systems from real brands — Zara, AllTrails, Linear, Stripe, and dozens more. Browse a few and find one that matches the *feeling* you want for your product:
>
> - **Professional & clean?** Check out Linear or Stripe
> - **Bold & editorial?** Try Zara
> - **Warm & adventurous?** Look at AllTrails
>
> Click into one and read the style guide. Notice how specific it is — exact hex codes, font families, border-radius values. That specificity is what makes it work.
>
> Tell me which one resonates, or describe the vibe you want if none of them are quite right.

**Then:** Wait for their response. They might name a brand from the site, describe a vibe in their own words, or say they already know what they want.

### Step 2: Create Their DESIGN.md

**What to do:** Build a comprehensive design system file based on their choice. Two paths depending on what they chose.

**If they picked a brand from designstyles.vercel.app:**
**What to say:**
> Great choice. Let me build your DESIGN.md based on that aesthetic, adapted for your product.

**Then:** Create a `DESIGN.md` file that adapts the chosen brand's aesthetic for their product. Include:
- Design philosophy (reference Jakob's 10 usability heuristics where relevant)
- Color system (primary, secondary, accent, background, text — all with hex codes)
- Typography (font families, weights, size hierarchy for h1, h2, body, UI elements)
- Component patterns (buttons, cards, inputs — with specific padding, border-radius, shadows)
- Spacing system (base unit, margins, section padding)
- Visual effects (shadows, transitions, hover states)
- Mood & audience description

Adapt the brand name and mood to fit their product.

**If they want to create from scratch:**
**What to say:**
> Let's build one from scratch. Three quick questions:
> 1. **What does your product do?** (One sentence)
> 2. **Pick 2-3 adjectives** for how it should feel: trustworthy, playful, premium, minimal, bold, energetic, warm, serious, techy?
> 3. **Primary brand color?** Hex code if you have it, or just "deep purple" / "ocean blue" / "forest green" and I'll pick a good one.

**Then:** Wait for their answers, then build the DESIGN.md with all the same sections.

**After creating the file:**
> ✅ Your design system is saved as `DESIGN.md`. Let me also update your `CLAUDE.md` to reference it — that way I'll follow it automatically in every session.

**Then:** Update CLAUDE.md to reference DESIGN.md. If CLAUDE.md doesn't exist, create it.

### Step 3: The Magic Moment — Watch the Transformation

**What to do:** Rebuild an existing page (their prototype, or build a new one) using the design system. Show the dramatic before/after.
**What to say:**
> Now watch what happens. I'm going to rebuild a page following every design token in your DESIGN.md exactly — the right colors, fonts, spacing, component styles. Everything intentional.

**Then:** Read DESIGN.md. If they have an existing prototype, rebuild it following the design system exactly. If they don't, build a main page for their product using the design system. Save it as a new file so they can compare (e.g., `page-styled.html`).

**After building, open it:**
> 🎉 **Open it up and look at the difference.**

**If there's a before version to compare:**
> Same content, completely different feel. The first version was a prototype. This one looks like a *product*. That's what a design system does — it makes everything feel intentional.

**If this is a new build:**
> Notice how everything feels cohesive? The colors relate to each other. The spacing is consistent. The typography has a clear hierarchy. That's not me being creative — that's me following specific design tokens. Constraints make better design.

**Then:** Wait for their reaction.

### Step 4: The Figma Bridge (Bonus)

**What to do:** Show them how to close the design-to-code loop with html.to.design and Figma MCP. This is optional — only go here if they're engaged and interested.
**What to say:**
> Want to see something cool? If you need to share your prototype with a designer in Figma, there's a bridge for that.
>
> **Option 1: HTML → Figma**
> [html.to.design](https://html.to.design/) converts any webpage into editable Figma layers. If your prototype is running locally, you'll need their Chrome extension. Public URLs can use the Figma plugin directly.
>
> **Option 2: Figma → Code (with Figma MCP)**
> If you connect the Figma MCP server, I can read your Figma designs directly — no screenshots needed. Set it up with:
> ```
> claude mcp add --transport http figma https://mcp.figma.com/mcp
> ```
> Then restart Claude Code and authenticate.
>
> Want to try either of these? Or would you prefer to keep iterating on the design itself?

**Then:** If they want to try Figma MCP, walk them through the setup. If they want html.to.design, explain the Chrome extension vs. Figma plugin distinction. If they want to keep going with design iteration, wrap up.

### Wrap Up

**What to say:**
> Here's what you built today: a **personal design system that lives in your codebase.** Every time I start a session, I read CLAUDE.md, find the reference to DESIGN.md, and follow your design tokens automatically. Every new screen, every new component, every iteration matches your brand.
>
> The before/after tells the whole story: without a design system, you get generic AI output. With one, you get something that looks like it has a real designer behind it.
>
> The maintenance is dead simple — whenever your design evolves, paste a screenshot of the new look and tell me to update DESIGN.md. Takes 30 seconds.
>
> Want to go deeper? I can:
> - **Apply your design system to multiple pages** — build a full set of screens that all feel cohesive
> - **Do a design audit** of your current product against Jakob Nielsen's 10 usability heuristics
> - **Set up the Figma MCP** so I can read your designs directly

**Share prompt:**
> 📸 **Bring back your before-and-after — the same screen without DESIGN.md vs. with it.** What brand style did you choose and why?

---

## Reference Material

Resources Claude might need during this lesson:

- **Design system source:** [designstyles.vercel.app](https://designstyles.vercel.app/) — 100+ brand design systems
- **Jakob Nielsen's 10 Usability Heuristics:** [NN/g article](https://www.nngroup.com/articles/ten-usability-heuristics/) — reference for design philosophy section:
  1. Visibility of system status
  2. Match between system and real world
  3. User control and freedom
  4. Consistency and standards
  5. Error prevention
  6. Recognition rather than recall
  7. Flexibility and efficiency of use
  8. Aesthetic and minimalist design
  9. Help users recognize, diagnose, and recover from errors
  10. Help and documentation
- **UX Mapping Methods:** [NN/g cheat sheet](https://www.nngroup.com/articles/ux-mapping-cheat-sheet/)
- **HTML to Figma:** [html.to.design](https://html.to.design/) — localhost needs Chrome extension, public URLs use Figma plugin
- **Figma MCP setup:** `claude mcp add --transport http figma https://mcp.figma.com/mcp` then restart and authenticate
- **Frontend Design Plugin:** [Anthropic's official plugin](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/frontend-design) for better design output
- **Good font pairings for design systems:**
  - Clean/professional: Inter + system-ui
  - Friendly/warm: DM Sans + system-ui
  - Techy/modern: Space Grotesk + JetBrains Mono (for code)
  - Editorial/bold: Instrument Serif + Inter
- **DESIGN.md vs design.md:** The capitalized version is a convention from earlier lessons. If the student already has a lowercase `design.md`, work with that — don't create a duplicate. Either filename works.
