# 7. From Idea to Working App in One Prompt

> **Magic Moment:** You describe a feature in plain English, Claude builds it, and you open a fully interactive, visually polished prototype in your browser — in under two minutes.

## Why This Matters

Every PM has experienced this: you have a crystal-clear idea in your head, you describe it to your team, and three sprints later you get something that kind of resembles what you meant. The feedback loop from "idea" to "thing I can click on" used to take days or weeks. With Claude Code, it takes minutes. This lesson is the one that changes how you think about building.

## Before You Start

- [ ] Claude Code open in your project folder
- [ ] A web browser ready to open local files
- [ ] An idea for a feature (or just use the one below — it's a great one)

## Do This Now

### Step 1: Sketch your idea in ASCII first

Before we build anything real, get your idea out of your head and into text. This takes 30 seconds and gives Claude a visual target.

**Paste this into Claude Code:**
```
I want to build a customer feedback dashboard. Before writing any code, show me 3 different ASCII wireframe layouts for this page. It should include:
- A summary bar with key metrics (NPS score, total responses, sentiment trend)
- A filterable list of recent feedback entries
- A sentiment breakdown chart

Label what each layout prioritizes (e.g., "data-dense", "action-oriented", "visual-first").
```

**What you should see:** Three distinct ASCII layouts. They'll look like boxes and dashes — not pretty, but enough to react to. Pick the one that feels right, or tell Claude to combine elements from two of them.

### Step 2: Build the real thing

Now here's where it gets impressive. You're going to turn that wireframe into a working, interactive web app in a single prompt.

**Paste this into Claude Code:**
```
Build this as a single HTML file I can open in my browser. Use Tailwind CSS via CDN for styling and make it look polished and modern — think Linear or Notion quality.

Requirements:
- Use layout #[pick your favorite from Step 1]
- Generate realistic sample data (at least 15 feedback entries with names, dates, ratings, and comments)
- The NPS score gauge should be visually distinctive (use a colored arc or progress ring)
- Filters should actually work — let me filter by sentiment (positive/neutral/negative) and date range
- Clicking a feedback entry should expand it to show the full comment
- Add smooth transitions and hover states
- Use a clean color palette: slate backgrounds, blue accents, proper typography hierarchy
- Make it responsive — should look great on both desktop and mobile

Save it as prototype.html in my project root.
```

**What you should see:** Claude writes a complete HTML file with embedded CSS and JavaScript. It'll be several hundred lines — a fully functional mini-app.

### Step 3: Open it and see the magic

**Run this in your terminal (or paste into Claude Code):**
```
open prototype.html
```

**What you should see:** 🎉 **This is the magic moment.** A polished, interactive dashboard opens in your browser. The filters work. The cards expand. The metrics are formatted. The hover states are smooth. You described a feature in plain English two minutes ago, and now you're clicking through a working prototype.

Take a second to click around. Filter by sentiment. Expand a feedback entry. Resize the window to see the mobile layout.

### Step 4: Make it yours

Now iterate. This is where it gets fun — you're a PM giving feedback on a working prototype, not arguing about Figma mockups.

**Paste this into Claude Code:**
```
I opened the prototype. A few changes:
1. Add a search bar at the top that filters feedback by keyword in real-time
2. Add a "trends" section that shows a simple line chart of sentiment over the last 30 days (use Canvas or inline SVG, no external libraries)
3. Change the color scheme to [your product's primary color, e.g., "deep purple (#7C3AED) as the accent color"]
4. Add an export button that downloads the filtered feedback as CSV

Update prototype.html with these changes.
```

**What you should see:** Claude updates the file. Refresh your browser. New features are live. The whole cycle — feedback to working update — took about a minute.

## 🎉 What Just Happened

You just experienced the core superpower of Claude Code for PMs: **the gap between "I want this" and "I can click on this" collapsed to minutes.** Claude didn't just generate some HTML — it built interactive JavaScript, realistic data, responsive layouts, and polished styling. It interpreted your ASCII sketch, applied modern design patterns, and produced something you could put in front of a stakeholder right now.

The key insight: you didn't write requirements docs, create tickets, or wait for a sprint. You described what you wanted, reacted to what you got, and iterated in real time. This is the new prototyping loop.

## Go Deeper

- **Go ambitious:** Try building something wild — a Kanban board, a real-time chat interface, a pricing page calculator. The crazier the idea, the more impressive the result.
- **Use your real product:** Replace the feedback dashboard with your actual next feature. Describe it to Claude the way you'd describe it to a teammate.
- **Try multi-page prototypes:** Ask Claude to build a prototype with navigation between pages: `"Build a 3-page prototype: landing page, dashboard, and settings. Include a nav bar that links between them."`
- **Add real data:** Instead of sample data, paste in a CSV or JSON of real user data and ask Claude to build a dashboard around it.

## Share

**Bring back:** A screenshot of the prototype you built. What did you describe to Claude, and how close was v1 to what you imagined?
