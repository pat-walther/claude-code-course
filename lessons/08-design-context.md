# 8. Make Every Build Match Your Visual Style

> **Magic Moment:** You create a `design.md` file, rebuild the same prototype from Lesson 7, and it transforms from "generic Claude output" to something that looks like it belongs in YOUR product.

## Why This Matters

Here's the dirty secret of AI-generated UI: it all looks the same. Blue buttons, gray backgrounds, the same Tailwind defaults everyone gets. That's fine for a throwaway prototype — but the moment you show it to a stakeholder, they'll say "this doesn't look like us." The fix takes 5 minutes and pays off forever: tell Claude what "good" looks like for your product, once, and every build matches your visual language from the first prompt.

## Before You Start

- [ ] Claude Code open in your project folder
- [ ] The prototype from Lesson 7 (or any prototype you've built)
- [ ] Know your product's brand colors, fonts, and visual style (check your Figma, marketing site, or just your gut)

## Do This Now

### Step 1: See the problem

Open the prototype you built in Lesson 7. Look at it with your "brand eyes." Notice:
- The colors are generic (probably blue and gray)
- The spacing follows Tailwind defaults, not your product's rhythm
- The typography has no personality
- It looks like *a* product, not *your* product

This is what happens when Claude has zero design context. Let's fix that.

### Step 2: Create your design.md

This is the file that changes everything. It's a simple markdown file that describes your product's visual DNA. Claude reads it at the start of every session.

**Paste this into Claude Code:**
```
Create a file called design.md in my project root. Use this template and fill it in with sensible defaults for a modern SaaS product. I'll customize it after.

# Design System

## Brand
- Product name: [My Product]
- Personality: [e.g., "professional but approachable", "bold and playful", "minimal and calm"]
- Inspiration: [e.g., "Linear, Notion, Vercel" or "Stripe, Intercom"]

## Colors
- Primary: [main brand color]
- Primary hover: [darker shade]
- Background: [page background]
- Surface: [card/section background]
- Text primary: [main text]
- Text secondary: [muted/helper text]
- Border: [subtle borders]
- Success: [green shade]
- Warning: [amber shade]
- Error: [red shade]

## Typography
- Font family: Inter (fallback: system-ui, sans-serif)
- Headings: font-semibold, tracking-tight
- Body: text-sm (14px), leading-relaxed
- Labels: text-xs, uppercase, tracking-wide, text-secondary
- Page title: text-2xl font-bold
- Section title: text-lg font-semibold

## Spacing
- Base unit: 4px (Tailwind spacing scale)
- Card padding: p-4 (mobile), p-6 (desktop)
- Section gaps: space-y-6
- Inline element gaps: gap-2 or gap-3
- Page margins: px-4 (mobile), px-8 (desktop), max-w-6xl mx-auto

## Components
- Buttons: rounded-lg, font-medium, px-4 py-2
- Cards: bg-surface, rounded-xl, border, no drop shadows
- Inputs: rounded-lg, border, focus:ring-2 focus:ring-primary/20
- Tables: text-sm, divide-y, hover:bg-muted/50 on rows
- Modals: rounded-2xl, backdrop-blur-sm overlay

## Patterns
- Use border instead of shadow for elevation
- Hover states: subtle background change, not color change
- Empty states: centered illustration + helpful message + primary CTA
- Loading: skeleton shimmer, not spinners
- Transitions: duration-150 ease-in-out
```

**What you should see:** A clean `design.md` file in your project root. Now customize it.

### Step 3: Make it yours

**Edit the design.md to match YOUR product.** Here's the fast way:

**Paste this into Claude Code:**
```
Update design.md with these specifics for my product:
- Product name: [your product name]
- Primary color: [your hex code, e.g., "#7C3AED" for purple, "#059669" for green]
- Personality: [pick one: "clean and professional like Linear" / "warm and friendly like Notion" / "bold and energetic like Figma"]
- Inspiration products: [name 2-3 products whose visual style you admire]
```

💡 **Don't know your brand colors?** Screenshot your product's homepage or marketing site and paste it into Claude Code: `"What are the primary colors used in this screenshot? Give me hex codes."` Claude will extract them.

**What you should see:** Your `design.md` now reflects your actual product's visual identity.

### Step 4: Add design.md to CLAUDE.md

Make sure Claude reads your design system automatically on every session.

**Paste this into Claude Code:**
```
Add a reference to design.md in my CLAUDE.md file. Add a line that says:
"Read design.md for all visual design decisions. Follow the design system for every UI component you build."
```

### Step 5: Rebuild and see the difference

Now rebuild the exact same prototype from Lesson 7 — but this time Claude has your design context.

**Paste this into Claude Code:**
```
Read design.md first. Now rebuild prototype.html from scratch — same features (feedback dashboard with metrics, filterable list, expandable entries) but this time follow the design system exactly. Match the colors, typography, spacing, and component styles in design.md.

Save it as prototype-v2.html so I can compare with the original.
```

**What you should see:** 🎉 **This is the magic moment.** Open both files side by side:
- `prototype.html` — generic blue/gray, looks like every other AI prototype
- `prototype-v2.html` — YOUR colors, YOUR spacing, YOUR brand personality

Same feature, completely different feel. The second one looks like it belongs in your product.

### Step 6: The screenshot workflow

Here's the power move for ongoing design iteration: use screenshots as context.

**Take a screenshot of any part of your product that already looks right** (your best screen, your marketing site, a Figma comp). Then:

**Paste the screenshot into Claude Code with this prompt:**
```
This screenshot shows what our product currently looks like. Match this visual style exactly for all future prototypes. Note the specific:
- Button styles and border radius
- Card elevation (shadow vs border)
- Color usage and hierarchy
- Typography weight and spacing
- Overall density (compact vs spacious)

Update design.md with anything you notice that isn't already captured.
```

**What you should see:** Claude analyzes your screenshot and enriches your design.md with details you might have missed — specific border-radius values, shadow styles, or spacing patterns.

## 🎉 What Just Happened

You created a `design.md` file — a one-time investment that pays dividends on every future build. Instead of getting generic AI output and manually fixing the design each time, Claude now starts every prototype in your visual language. The before/after comparison makes it obvious: context is the difference between "AI slop" and "this looks like our product."

The screenshot workflow is the ongoing maintenance loop — whenever your design evolves, paste a screenshot and update design.md. It takes 30 seconds and keeps Claude current.

## Go Deeper

- **Design audit:** Paste a screenshot of your current product and ask: `"Review this screen as a design-conscious user. What looks off, inconsistent, or unfinished? What 3 changes would have the biggest visual impact?"`
- **Steal from the best:** Find a product whose design you admire. Screenshot it and say: `"Extract the design system from this screenshot. What colors, spacing, typography, and component patterns do they use? Write it as a design.md."`
- **Reference reading:** [UX Mapping Methods Compared](https://www.nngroup.com/articles/ux-mapping-cheat-sheet/) — NN/g's cheat sheet for design thinking methods
- **Jakob's 10 Usability Heuristics:** Have Claude evaluate your UI against these: `"Evaluate my prototype against Jakob Nielsen's 10 usability heuristics. Where am I strong? Where am I weakest?"`

## Share

**Bring back:** A before/after screenshot — your prototype without design.md vs. with it. How different do they look?
