# 10. Set Up the Right Project Structure

> **Magic Moment:** You ask Claude to diagram your project's architecture and it gives you a clear ASCII map of how everything fits together — frontend, backend, database, deployment — revealing complexity you didn't know was there (or simplicity you can take advantage of).

## Why This Matters

Most PMs avoid "architecture" conversations because they feel deeply technical. But architecture is really about tradeoffs — and tradeoffs are a PM's bread and butter. Should we build this as a single page or a multi-page app? Do we need a database, or can we store data locally? Is this feature easy or hard given our current setup? When you can see your project's architecture, you can make better product decisions. You stop proposing features that require rebuilding the foundation, and you start spotting opportunities that are "free" given what already exists.

## Before You Start

- [ ] Claude Code open in your project folder (ideally a real codebase, not just the prototype from earlier)
- [ ] If you're using a course sample project, that works too — you'll still learn the pattern

## Do This Now

### Step 1: Map what you have

This is the prompt that turns an intimidating codebase into a clear picture.

**Paste this into Claude Code:**
```
Diagram my architecture using ASCII. I want to know:
- Web and mobile frontend frameworks and libraries
- Backend libraries and frameworks
- Databases and data storage
- Background tasks or scheduled jobs
- Infrastructure and hosting providers
- How deployment works (manual, CI/CD, etc.)
- Test coverage (what's tested, what isn't)

Make the diagram show how data flows between these pieces. Label each connection.
```

**What you should see:** An ASCII diagram like this:

```
┌─────────────────┐          ┌──────────────────┐
│   Frontend      │   HTTP   │   Backend API    │
│   (React/Next)  │◄────────►│   (Node/Python)  │
│   Port 3000     │          │   Port 8000      │
└─────────────────┘          └────────┬─────────┘
                                       │
                                       │ SQL queries
                                       ▼
                              ┌──────────────────┐
                              │   PostgreSQL     │
                              │   Database       │
                              └──────────────────┘
```

Plus a written summary of each piece and its role. This is your architectural map.

### Step 2: Understand the complexity spectrum

Not every project needs the same architecture. Here's the mental model — ask Claude where your project falls.

**Paste this into Claude Code:**
```
Based on my project's current architecture, where does it fall on this spectrum?

SIMPLE → STANDARD → COMPLEX

Rate each layer:
- Frontend: (Simple = HTML files | Standard = React/Next/Vue | Complex = Micro-frontends)
- Backend: (Simple = No backend/serverless | Standard = Single API server | Complex = Microservices)
- Database: (Simple = Local storage/files | Standard = Single PostgreSQL | Complex = Multi-database + caching)
- Infrastructure: (Simple = Static hosting | Standard = PaaS like Render/Vercel | Complex = AWS/GCP with Kubernetes)

For each layer, tell me: should I move UP in complexity (and why), stay where I am, or simplify DOWN?
```

**What you should see:** 🎉 **This is the magic moment.** Claude doesn't just describe your architecture — it gives you actionable recommendations. Maybe your backend is more complex than it needs to be. Maybe your database is too simple for what you're trying to do. You're getting a tech lead's assessment in 30 seconds.

### Step 3: Test a feature against your architecture

Now use your architectural understanding to evaluate a product idea.

**Paste this into Claude Code:**
```
I want to add this feature: [describe a feature you're considering — e.g., "let users save their preferences and load them on their next visit" or "send a weekly email digest of activity"].

Given my current architecture:
1. How hard is this to build? (Easy/Medium/Hard and why)
2. What new pieces of infrastructure would I need?
3. What's the simplest possible implementation?
4. What's the "right" implementation if this becomes a core feature?
5. Show me a plan — don't build yet, just the plan.
```

**What you should see:** Claude evaluates your feature idea against your actual codebase — not in the abstract. It might say "this is easy because you already have a database with user accounts" or "this is hard because you'd need to add a background job runner, and you currently don't have one."

### Step 4: Set up a clean project structure

If you're starting a new prototype or project, get the foundation right from the start.

**Paste this into Claude Code:**
```
I'm starting a new prototype for [describe your idea]. Set up a clean project structure. I want:
- A clear folder organization with README explaining what goes where
- Frontend: simple HTML + Tailwind (keep it simple — no build step)
- Data: start with a JSON file, but structure the code so I can swap in a real database later
- A CLAUDE.md that describes the project and architecture decisions
- A design.md based on [your design style from Lesson 8]

Create the folder structure and all the config files. Don't build any features yet — just the skeleton.
```

**What you should see:** A well-organized project directory with clear separation of concerns, helpful README, and the memory files Claude needs to be effective. This is the foundation for everything you build next.

## 🎉 What Just Happened

You learned to see your project the way a technical lead sees it — as a set of connected layers with different complexity levels. The ASCII architecture diagram turns an intimidating codebase into something you can reason about. More importantly, you can now evaluate feature ideas against your architecture: "Is this easy or hard given what we have?" is a PM superpower.

The spectrum (Simple → Standard → Complex) is your decision framework. Start simple. Move up only when you have a clear reason. Claude helps you see when you're at the right level — and when you're overcomplicating things.

## Go Deeper

- **Architecture for your real product:** Run the architecture diagram prompt on your actual work codebase. Share the output with your engineering team — you'll either validate your understanding or learn something surprising.
- **The Tailwind starter:** For quick prototypes, HTML + Tailwind CSS via CDN is the sweet spot. No build step, no npm, just open the file in a browser. Ask Claude: `"Set up the simplest possible project structure for rapid prototyping — just HTML, Tailwind CDN, and Alpine.js for interactivity."`
- **Component libraries:** Speed up future builds by telling Claude which UI kit to use: `"Use shadcn/ui components throughout. Don't build custom components from scratch unless they don't exist in the library."`
- **Design systems gallery:** Browse [designsystems.surf](https://designsystems.surf/) or [component.gallery](https://component.gallery/components/) for inspiration on how other products structure their component libraries.

## Share

**Bring back:** Your architecture diagram. Were you surprised by anything Claude found? Was your project simpler or more complex than you expected?
