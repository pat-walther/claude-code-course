# 24. Deploy and Ship — Tests, CI/CD, and Going Live

> **Magic Moment:** Claude sets up your entire deployment pipeline — tests, linters, CI, hosting — and you push code that automatically tests and deploys to a live URL. You built it AND shipped it.

## Why This Matters

Building a prototype is great. Shipping it to a URL that anyone can visit? That's a product. This lesson closes the loop on everything you've learned. By the end, you'll have automated tests catching bugs, a CI pipeline running on every change, and a live deployment that updates automatically. This is how real products work — and Claude sets it all up for you.

## Before You Start

- A project with code (your prototype from earlier lessons works perfectly)
- A GitHub account (free)
- Claude Code open in your project directory
- 20-30 minutes

## Do This Now

### Step 1: Set up tests and linting

Tests verify your code works. Linters catch syntax errors. Together, they give your AI coding agent debugging tools that human developers use — so it gets implementations right the first time.

**Paste this into Claude Code:**
```
Please setup tests in this repo, and make a plan to write several unit tests for my application, and a way to measure test coverage. Tell me what key test cases you are covering based on my user persona and product workflows.
```

**What you should see:** Claude analyzes your codebase, picks the right testing framework (Jest, pytest, etc.), creates test files, and explains which user workflows each test covers. It might create 5-15 tests depending on your app's complexity.

Now add linting:

**Paste this into Claude Code:**
```
Please setup linters for both the backend and frontend, and add a makefile command to run everything.
```

**What you should see:** Linters configured (ESLint, Ruff, etc.) and a simple `make lint` + `make test` command you can run anytime.

### Step 2: Push to GitHub

Your code needs to live on GitHub for everything else to work.

**Paste this into Claude Code:**
```
Create a new GitHub repository for this project and push my code to it. Include a proper .gitignore file.
```

**What you should see:** Claude initializes git, creates a `.gitignore`, creates a GitHub repo, and pushes your code. You'll get a URL like `github.com/your-username/your-project`.

### Step 3: Set up CI with GitHub Actions

CI (Continuous Integration) means your tests run automatically on every pull request. No more "it works on my machine."

**Paste this into Claude Code:**
```
Setup a ci.yml file as a GitHub Action to run the linter and tests on every PR. Also add instructions to CLAUDE.md telling future coding agents to use the linter, write any missing tests, and make sure tests pass before creating a PR.
```

**What you should see:** A `.github/workflows/ci.yml` file that triggers on every pull request. Claude also updates your project's CLAUDE.md so that any future AI session knows to run tests before committing.

### Step 4: Deploy to a live URL

Time to put your project on the internet. You have options — we'll use the simplest path.

**Option A — Vercel (best for frontend/Next.js apps):**
```
Deploy this project to Vercel. Set it up so every push to main auto-deploys.
```

**Option B — Netlify (best for static sites):**
```
Deploy this project to Netlify with automatic deployments on push to main.
```

**Option C — Render (best for full-stack apps with a backend):**
```
Create a service for this site and deploy it to Render. Set it up so every merge to main triggers a new deployment.
```

**What you should see:** Claude configures the deployment service, pushes your code, and gives you a live URL. Your project is now on the internet. 🎉

### Step 5: Set up code review (bonus)

LLMs are better critics than creators. Use this to your advantage — set up automated code review on every PR.

**Paste this into Claude Code:**
```
Set up automated code review for this repository. I want an AI reviewer that comments on every pull request with:
1. Potential bugs or edge cases
2. Code quality suggestions
3. Security concerns

Use Claude Code's GitHub Actions integration or Cursor's bugbot — whichever is easier to set up.
```

**What you should see:** A GitHub Action or bot configuration that automatically reviews every PR. When you (or Claude) open a PR, it gets AI-reviewed before you merge.

### Step 6: Test the full pipeline

Now let's prove it all works end-to-end.

**Paste this into Claude Code:**
```
Make a small visible change to the app (like updating the page title or adding a footer), create a new branch, commit the changes, and open a pull request.
```

**What you should see:**
1. Claude makes the change on a new branch
2. It pushes and opens a PR
3. GitHub Actions runs your linter and tests automatically ✅
4. The code review bot comments on the PR 🔍
5. After you merge, it auto-deploys to your live URL 🚀

Visit your deployment URL after merging — you should see the change live.

## 🎉 What Just Happened

You just set up a professional deployment pipeline — the same kind used by real engineering teams. Here's what's now automated:

- **Tests** run on every PR to catch bugs before they ship
- **Linters** catch syntax and style issues automatically
- **CI (GitHub Actions)** orchestrates all checks without you lifting a finger
- **Code review** gives you AI-powered feedback on every change
- **Auto-deployment** pushes tested, reviewed code to production on merge

This is the full loop: build → test → review → deploy. You can now ship features with confidence, even as a non-engineer PM.

## Go Deeper

- **Error tracking:** Set up [Sentry](https://sentry.io) to monitor production errors. Install the Sentry MCP so Claude can fix bugs by just pasting an error URL: `mcp.sentry.dev`
- **PR previews:** If using Render, enable PR Previews (Settings → PR Previews) to get a unique URL for every pull request — perfect for sharing work-in-progress with stakeholders
- **Stably.ai:** Set up AI-powered QA tests that run against your live app on every change
- **The PM superpower:** You can now say "I want feature X" → Claude builds it → tests run → it deploys → users see it. That's a one-person product team.

## Share

Bring back: your live deployment URL. Show the cohort what you shipped this week.
