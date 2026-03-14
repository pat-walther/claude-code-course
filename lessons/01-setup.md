# 1. Install Claude Code and Get Your First Magic Moment

> **Magic Moment:** You type one sentence in plain English, and Claude writes a working app — files, code, and all — right in front of you.

## Why This Matters

You're about to install the tool that turns "I wish I could build that" into "I just built that." Claude Code is a terminal-based AI agent that reads files, writes code, runs commands, and browses the web — all from a single conversation. For a PM, this means you can go from product idea to working prototype without waiting for sprint planning.

## Before You Start

- A Mac or Windows computer
- 10 minutes of uninterrupted time
- A credit card for the Claude Pro subscription ($20/month — you'll need this for Claude Code access)

## Do This Now

### Step 1: Open your terminal

**On Mac:** Press `CMD + Space`, type "Terminal", hit Enter.
**On Windows:** Press `Win`, type "Command Prompt" or "PowerShell", hit Enter.

**What you should see:** A blank window with a blinking cursor. This is your command center for the rest of the course.

### Step 2: Install Claude Code

**Paste this into your terminal:**
```
npm install -g @anthropic-ai/claude-code
```

⚠️ **Don't have npm?** You'll need Node.js first. Go to [nodejs.org](https://nodejs.org), download the LTS version, install it, then re-run the command above.

**What you should see:** A bunch of text scrolling by, ending with something like `added X packages`. No red errors = you're good.

### Step 3: Launch Claude Code and sign in

**Paste this into your terminal:**
```
claude
```

**What you should see:** Claude Code starts up and asks you to authenticate. It will open a browser window — sign in with your Anthropic account (or create one). Select the **Pro plan** ($20/month, toggle to Monthly).

Once authenticated, you'll see the Claude Code prompt — a `>` waiting for your input. You're in.

💡 **Tip:** If the browser doesn't open automatically, copy the URL from the terminal and paste it into your browser. Click "Authorize" when prompted.

### Step 4: Create a project folder

**Paste this into Claude Code:**
```
Create a new folder called "pm-playground" and navigate into it
```

**What you should see:** Claude creates the folder and changes into it. It'll confirm something like "Created directory pm-playground and navigated into it."

### Step 5: Your first magic moment 🎉

**Paste this into Claude Code:**
```
Build me a personal dashboard webpage with my name, today's date, a motivational quote that changes on refresh, and a clean modern design. Use HTML, CSS, and JavaScript in a single file. Then open it in my browser.
```

**What you should see:** Claude thinks for a moment, then:
1. Creates an `index.html` file with all the code
2. Writes clean HTML, CSS, and JavaScript
3. Opens it in your default browser

You just built a working web app. Without writing a single line of code. Look at it in your browser — that's real, functioning software.

### Step 6: Verify it works

**Paste this into Claude Code:**
```
Show me the file you just created
```

**What you should see:** Claude displays the contents of `index.html`. Scroll through it — this is real, readable code. Refresh the page in your browser a few times and watch the quote change.

## 🎉 What Just Happened

Claude Code read your plain-English request, broke it down into a technical plan, wrote an entire HTML/CSS/JavaScript application, saved it as a file on your computer, and opened it in your browser. It didn't use a template — it generated that code from scratch based on your description. This is what "vibe coding" means: you steer with your product sense, Claude handles the implementation.

## Go Deeper

- Try modifying your dashboard: "Add a section that shows 3 fake tasks with checkboxes"
- Change the design: "Make it dark mode with a purple accent color"
- Get ambitious: "Add a countdown timer to 6pm today"

Each of these prompts will modify the existing file — Claude remembers what it already built.

## Share

**Bring back:** A screenshot of your personal dashboard. Bonus points if you customized it beyond the original prompt.
