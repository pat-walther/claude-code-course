# 🔐 The AI Escape Room

> **Magic Moment:** You solve 5 puzzles using nothing but plain-English commands, and realize Claude Code is the Swiss Army knife you never knew you needed.

```
    ╔══════════════════════════════════════════╗
    ║                                          ║
    ║    ┌──────────────────────────────────┐   ║
    ║    │                                  │   ║
    ║    │         🔒 LOCKED 🔒             │   ║
    ║    │                                  │   ║
    ║    │   You need 5 keys to escape.     │   ║
    ║    │                                  │   ║
    ║    │   🔑 . . . . .                   │   ║
    ║    │                                  │   ║
    ║    │      Use Claude Code.            │   ║
    ║    │      That's your only tool.      │   ║
    ║    │                                  │   ║
    ║    └──────────────────────────────────┘   ║
    ║               ┌──────┐                   ║
    ║               │ ◉  ◉ │                   ║
    ║               │  ──  │                   ║
    ║               └──────┘                   ║
    ╚══════════════════════════════════════════╝
```

## The Setup

You've been locked in a digital escape room. The door has five locks. Each puzzle you solve gives you a key. Collect all five keys and you're free.

Your only tool? **Claude Code.** No Googling. No Stack Overflow. Just you and your AI agent.

**The clock is ticking.**

## Before You Start

- Claude Code installed and running (complete [Lesson 1](../lessons/01-setup.md) first if you haven't)
- Navigate to the `games/escape-room-files/` directory in your terminal before launching Claude Code
- Something to write on (you'll need to track your keys)

## ⏱️ Start Your Timer NOW

Note the time. Write it down. You'll need it at the end.

**My start time: ____:____**

| Par Time | Rating |
|----------|--------|
| Under 10 minutes | 🏆 Houdini |
| 10–15 minutes | 🥇 Lock Pick |
| 15–25 minutes | 🥈 Safe Cracker |
| 25–40 minutes | 🥉 Escape Artist |
| 40+ minutes | 🎖️ You Still Made It |

---

## 🔑 Puzzle 1: The Encrypted Message

**Skill unlock: Claude can run code**

You find a file on the desk. It's gibberish — some kind of encoded message. The answer is in there, but you can't read it.

The file is `puzzle1.txt`. It contains an encoded message.

**Your mission:** Ask Claude Code to decode the message and reveal the hidden text.

**What to tell Claude:** Describe what you need in plain English. Tell it about the file. Ask it to figure out the encoding and decode it.

**You'll know you solved it when:** You see a readable English sentence that contains a number. That number is **Key #1**. Write it down.

<details>
<summary>💡 Hint 1 (click to reveal)</summary>

The encoding is base64 — one of the most common encoding schemes on the web. You could tell Claude that, or you could just ask it to "figure out the encoding and decode the file" and see if it gets there on its own. (It will.)

</details>

<details>
<summary>💡 Hint 2 (click to reveal)</summary>

Try: "Read the file puzzle1.txt and decode the encoded message inside it. It looks like it might be base64."

</details>

**⏱️ Par time:** 2 minutes

**Key #1: ____**

---

## 🔑 Puzzle 2: The Hidden Data

**Skill unlock: Claude can read and analyze files**

You find a spreadsheet — `puzzle2.csv` — with employee data. 20 rows. Looks normal at first glance. But one row is different. One row has a hidden pattern in its numbers.

**Your mission:** Ask Claude Code to analyze the CSV file and find the row where ALL four numeric values (alpha, beta, gamma, delta) share a special mathematical property.

**What to tell Claude:** You're looking for a pattern. One row is different from all the others. The numbers in that row share something in common that no other row's numbers do.

**You'll know you solved it when:** Claude identifies the special row and explains *why* those numbers are special. The **ID number** of that row is **Key #2**. Write it down.

<details>
<summary>💡 Hint 1 (click to reveal)</summary>

The pattern is mathematical. Think about what makes a number "special" — what property could all four numbers in one row share?

</details>

<details>
<summary>💡 Hint 2 (click to reveal)</summary>

The property is about prime numbers. Try: "Read puzzle2.csv and find the row where all four numeric columns (alpha, beta, gamma, delta) are prime numbers."

</details>

**⏱️ Par time:** 3 minutes

**Key #2: ____**

---

## 🔑 Puzzle 3: The Broken Code

**Skill unlock: Claude can debug and fix code**

There's a Python program — `puzzle3.py` — that's supposed to output the next key. But it's broken. Three bugs. It won't even run.

**Your mission:** Ask Claude Code to read the buggy code, find and fix all 3 bugs, then run it with your **Key #1** as the argument.

**What to tell Claude:** The program has exactly 3 bugs. You need it to fix them AND run the corrected program. The program takes a command-line argument — use the number you found in Puzzle 1.

**You'll know you solved it when:** The program runs and outputs a phrase made of number-words separated by dashes (like "THREE-FOUR" or "SIX-ONE-NINE"). That phrase is **Key #3**. Write it down.

<details>
<summary>💡 Hint 1 (click to reveal)</summary>

The bugs are:
1. A syntax error (something missing on a line)
2. A type error (a string being used where an integer is needed)
3. Another type error (input not being converted)

</details>

<details>
<summary>💡 Hint 2 (click to reveal)</summary>

Try: "Read puzzle3.py, find and fix all 3 bugs, then run it with the argument 73" (replace 73 with your actual Key #1 if different — but it should be 73).

</details>

**⏱️ Par time:** 4 minutes

**Key #3: ____**

---

## 🔑 Puzzle 4: The Visual Key

**Skill unlock: Claude can create files and webpages**

No file this time. This puzzle lives in your head — and Claude's ability to create.

You need to build a **visual decoder page**. Here's what it must display:

1. A large title: "ESCAPE ROOM — KEY WALL"
2. Three boxes in a row, each showing one of your three keys so far:
   - Box 1: Key #1 (the number)
   - Box 2: Key #2 (the ID number)
   - Box 3: Key #3 (the word phrase)
3. Below the boxes: the **sum** of Key #1 and Key #2, displayed in large bold text
4. A dark background with glowing green text (escape room vibes 🟢)

**Your mission:** Ask Claude Code to build this HTML page, filling in your three keys. Then open it in your browser.

**You'll know you solved it when:** The page displays correctly and the sum of your first two keys is visible. That sum is **Key #4**. Write it down.

<details>
<summary>💡 Hint 1 (click to reveal)</summary>

You just need to ask Claude to build it. Give it all the details — your key values, the layout, the styling. It'll create the HTML file for you.

</details>

<details>
<summary>💡 Hint 2 (click to reveal)</summary>

Try: "Create an HTML file called key-wall.html with a dark background and glowing green text. Show three boxes in a row with these values: [Key #1], [Key #2], and [Key #3]. Below them, show the sum of the first two numbers in large bold text. Make it look like an escape room display. Open it in my browser."

</details>

**⏱️ Par time:** 3 minutes

**Key #4: ____**

---

## 🔑 Puzzle 5: The Final Lock

**Skill unlock: Claude can combine ALL capabilities**

You have all four keys. Now you need to combine them to unlock the final door.

Here's what the final lock requires — a **"congratulations" webpage** that proves you escaped. It must include:

1. **ASCII art** of a trophy at the top
2. Your **escape time** (the current time minus your start time)
3. A **key summary table** showing all 4 keys and which puzzle they came from
4. The **final code**: take Key #4, multiply it by 3, and subtract Key #1 — display the result prominently
5. A section called **"Skills Unlocked"** listing what each puzzle taught you:
   - Puzzle 1 → "Claude can run code and decode data"
   - Puzzle 2 → "Claude can read and analyze files"
   - Puzzle 3 → "Claude can debug and fix code"
   - Puzzle 4 → "Claude can create files and webpages"
   - Puzzle 5 → "Claude can combine all of the above"
6. Confetti animation or some celebratory visual flair 🎉

**Your mission:** Give Claude ALL the information and ask it to build this final page in one prompt. This is the boss level — you're combining everything.

**You'll know you solved it when:** The page opens in your browser with all the elements above, including your escape time and the calculated final code.

<details>
<summary>💡 Hint 1 (click to reveal)</summary>

The key to this puzzle is writing one clear, comprehensive prompt. Give Claude everything it needs: your start time, all four key values, the calculations, the layout requirements, and the styling preferences. One shot.

</details>

<details>
<summary>💡 Hint 2 (click to reveal)</summary>

Try: "Build a congratulations webpage called escape-complete.html. At the top, create ASCII art of a trophy. Show my escape time (I started at [TIME]). Create a table with 4 rows showing my keys: Puzzle 1 = [Key1], Puzzle 2 = [Key2], Puzzle 3 = [Key3], Puzzle 4 = [Key4]. Calculate the final code: [Key4] × 3 − [Key1] and display it in big text. Add a 'Skills Unlocked' section listing what each puzzle taught me. Add confetti animation. Dark background, celebratory theme. Open it in my browser."

</details>

**⏱️ Par time:** 4 minutes

---

## 🔓 You Escaped!

**Stop your timer.**

**My end time: ____:____**

**My total time: ____ minutes**

How'd you do?

| Your Time | Your Rating |
|-----------|------------|
| Under 10 min | 🏆 **Houdini** — You're a natural. Claude barely had to think. |
| 10–15 min | 🥇 **Lock Pick** — Clean, efficient, impressive. |
| 15–25 min | 🥈 **Safe Cracker** — Solid work. You found your rhythm. |
| 25–40 min | 🥉 **Escape Artist** — You got out. That's what matters. |
| 40+ min | 🎖️ **Persistent** — You never gave up. That's a PM superpower. |

---

## 🎉 What Just Happened

You just used Claude Code to:

| Puzzle | What You Did | Claude Code Capability |
|--------|-------------|----------------------|
| 1 — The Encrypted Message | Decoded a base64 string | **Run code** — Claude can execute scripts and commands |
| 2 — The Hidden Data | Found a pattern in a CSV | **Read & analyze files** — Claude can process data and spot patterns |
| 3 — The Broken Code | Fixed 3 bugs and ran a program | **Debug & fix code** — Claude can find and resolve errors |
| 4 — The Visual Key | Built an HTML page from scratch | **Create files** — Claude can generate entire webpages |
| 5 — The Final Lock | Combined everything into one output | **Orchestrate** — Claude can handle complex, multi-step tasks in one prompt |

None of these required you to write a single line of code. You described what you wanted in plain English, and Claude handled the rest. **That's the entire mental model for this course.**

## The Key Takeaways

1. **Claude can run things.** Not just write code — actually execute it and show you results.
2. **Claude can read your files.** CSVs, text files, codebases — it reads them and reasons about what's inside.
3. **Claude can debug.** Show it broken code and it'll find and fix the issues — then prove it works.
4. **Claude can create.** Webpages, files, scripts — describe what you want and it builds it.
5. **Claude can combine.** The real power is chaining these capabilities in a single prompt.

## Go Deeper

- **Speedrun it:** Try the whole room again from scratch. Beat your time.
- **Modify the puzzles:** Ask Claude to make puzzle3.py harder, or create a puzzle6.py with 5 bugs.
- **Create your own escape room:** Ask Claude to generate a new set of puzzles for a friend to solve.

## Share

**Post your escape time and a screenshot of your congratulations page (with the ASCII trophy).** Bonus: share your total prompt count — how many times did you talk to Claude across all 5 puzzles?
