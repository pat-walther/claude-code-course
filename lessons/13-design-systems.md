# 13. Component Libraries and Design Tokens

> **Magic Moment:** You point Claude at a design system and your generic-looking prototype transforms into something that looks like it has a real brand behind it — like having a designer on call.

## Why This Matters

Every PM has shipped something that "works" but looks like it was built by an engineer at 2am (no offense). The difference between a prototype people *use* and one people *dismiss* is often just visual consistency — matching colors, aligned spacing, coherent typography. A `DESIGN.md` file is your secret weapon: it teaches Claude your aesthetic preferences so every screen it builds looks intentional.

## Before You Start

- Claude Code open in your project directory
- Your project from previous lessons
- A browser open to browse design inspiration

## Do This Now

### Step 1: Browse design systems for inspiration

Open [designstyles.vercel.app](https://designstyles.vercel.app/) in your browser. This site catalogs design systems from real brands — Zara, AllTrails, Linear, Stripe, and dozens more.

Browse a few. Pick one that matches the *feeling* you want for your product:
- **Professional & clean?** Try Linear or Stripe
- **Bold & editorial?** Try Zara
- **Warm & adventurous?** Try AllTrails

Click into a brand and read its style guide. Notice how specific it is: exact hex codes, font families, border-radius values, shadow definitions.

**What you should see:** A complete design system with colors, typography, components, visual effects, and mood description.

### Step 2: Create your DESIGN.md

This is the file that will make every future prototype look consistent. You have two options:

**Option A: Start from a brand you admire**

Copy the style guide from designstyles.vercel.app, then:

**Paste this into Claude Code:**
```
I want to use this design aesthetic for my project. Save it as DESIGN.md in the project root and add a reference to it in CLAUDE.md so you always follow it:

[Paste the style guide here]

Adapt the brand name and mood to fit my product: [describe your product in one sentence].
```

**Option B: Create one from scratch based on your taste**

**Paste this into Claude Code:**
```
You are an expert UX designer. Create a DESIGN.md file for my project. My product is [describe it]. I want it to feel [pick 2-3 adjectives: trustworthy, playful, premium, minimal, bold, etc.].

Include these sections:
- Design philosophy (use Jakob's 10 usability heuristics)
- Color system (primary, secondary, accent, background, text — with hex codes)
- Typography (font families, weights, size hierarchy for h1, h2, body, UI)
- Component patterns (buttons, cards, inputs — with specific padding, border-radius, shadows)
- Spacing system (base unit, margins, section padding)
- Visual effects (shadows, transitions, hover states)
- Mood & audience description

Save it as DESIGN.md and add a reference in CLAUDE.md.
```

**What you should see:** A detailed design system file in your project root. Claude will also update CLAUDE.md to reference it, so every future session automatically follows your design guidelines.

### Step 3: Watch the transformation

Now rebuild a screen from your project using the new design system:

**Paste this into Claude Code:**
```
Read DESIGN.md, then redesign the main page of my app following every design token exactly. Use the correct colors, fonts, spacing, and component styles. Open it when done.
```

**What you should see:** 🎉 Your page looks *designed*. Same content, but now with intentional colors, proper typography hierarchy, consistent spacing, and components that feel cohesive. This is the difference between "prototype" and "product."

### Step 4: Convert your prototype to Figma (bonus)

Want to share your design with your team in Figma? Use [html.to.design](https://html.to.design/):

1. If your prototype is running locally, install the [Chrome extension](https://chromewebstore.google.com/detail/htmltodesign/ldnheaepmnmbjjjahokphckbpgciiaed)
2. If it's deployed to a public URL, use the Figma plugin directly
3. Enter your URL → it converts your HTML into editable Figma layers

💡 **If the page is on localhost**, you MUST use the Chrome extension. The Figma plugin can only access public URLs.

**What you should see:** Your prototype appears in Figma as editable layers — text, images, shapes all separated and editable. Your designer can now iterate on it directly.

### Step 5: Connect Figma MCP for the full loop

To close the design-to-code loop, connect the Figma MCP server so Claude can read your Figma designs directly:

**Run this in your terminal (outside Claude Code):**
```bash
claude mcp add --transport http figma https://mcp.figma.com/mcp
```

Then restart Claude Code and authenticate when prompted.

Now you can say:

**Paste this into Claude Code:**
```
Use the Figma MCP to read this design: [paste Figma URL]
Recreate it exactly, following DESIGN.md for any unspecified details.
Keep refining until no differences remain.
```

**What you should see:** Claude reads your Figma mock directly — no screenshots needed — and builds code that matches the design. It's still not perfect (Figma's MCP is evolving), but it's remarkably close.

## 🎉 What Just Happened

You created a personal design system that lives in your codebase. Every time Claude Code starts a session, it reads `CLAUDE.md`, finds the reference to `DESIGN.md`, and follows your design tokens. This means every new screen, every new component, every iteration automatically matches your brand. You also learned the html.to.design → Figma → Figma MCP loop, which lets you go from code to design to refined code seamlessly.

## Go Deeper

- [designstyles.vercel.app](https://designstyles.vercel.app/) — browse and copy brand design systems
- [html.to.design](https://html.to.design/) — convert any webpage to editable Figma designs
- [Figma MCP setup guide](https://code.claude.com/docs/en/mcp) — official MCP documentation
- [10 Usability Heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/) — Jakob Nielsen's foundational design principles
- [UX Mapping Methods Compared](https://www.nngroup.com/articles/ux-mapping-cheat-sheet/) — framework for customer journey mapping
- [Frontend Design Plugin](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/frontend-design) — Anthropic's official plugin for better design output

## Share

**Bring back:** Your before-and-after. Show the same screen without DESIGN.md (generic) vs. with DESIGN.md (branded). What brand style did you choose and why?
