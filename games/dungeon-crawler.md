# 1-alt. Build a Dungeon Crawler with Claude Code

> **Magic Moment:** You describe a game in plain English. Claude writes it, you play it in your terminal, then you keep adding features by just asking — combat, boss fights, save files — until you've built something genuinely fun.

## Why This Matters

The best way to learn a tool is to build something you actually want to use. Dashboards are fine. But a dungeon crawler you can play in your terminal? That's fun. And along the way you'll learn every core Claude Code skill — creating files, running code, iterating on features, and working with file I/O — without it ever feeling like homework.

## Before You Start

- Claude Code installed and authenticated (run `claude` in your terminal to confirm)
- A terminal window open
- 15-20 minutes — you're going to want to keep playing

## Do This Now

### Step 1: Create your project folder

**Paste this into Claude Code:**
```
Create a folder called dungeon-crawler and navigate into it
```

**What you should see:** Claude creates the folder and confirms it's navigated inside.

---

### Step 2: Build the base game with one prompt

This is the magic moment. One sentence → a playable game.

**Paste this into Claude Code:**
```
Build a terminal dungeon crawler game in Python. The dungeon should be a 5x5 grid of rooms displayed with ASCII art. The player starts in the top-left corner and needs to reach the exit in the bottom-right corner. Use WASD keys for movement. Show the map after each move with the player's position marked. Add some rooms that are locked or have simple text descriptions when you enter them. Make it fun.
```

**What you should see:** Claude creates a Python file (something like `dungeon.py`), writes the full game code — map rendering, player movement, room descriptions — and it's ready to run. This takes about 30 seconds.

💡 **What's happening under the hood:** Claude read your prompt, planned a file structure, created the file, and wrote working Python code. That's the **create + edit** abilities working together.

---

### Step 3: Play your game!

**Paste this into Claude Code:**
```
Run the dungeon game
```

**What you should see:** The game starts in your terminal! You'll see an ASCII map with your player position. Use WASD to move around, explore rooms, and find the exit.

Play for a minute. Explore. Find the exit. Then come back to Claude Code.

⚠️ **To quit the game**, press `Ctrl+C` or whatever exit key the game provides.

💡 **What you just learned:** Claude Code can **run commands** — it executed your Python script directly in the terminal. You didn't need to type `python dungeon.py` yourself.

---

### Step 4: Add a combat system — your first iteration

Now comes the powerful part. You don't need to touch the code. Just describe what you want.

**Paste this into Claude Code:**
```
Add a combat system to the dungeon game. Some rooms should have monsters with names and HP. Combat should be turn-based: the player can attack, defend, or run. Show HP bars with ASCII art for both the player and the monster. The player starts with 100 HP and 15 attack power. Add at least 3 different monster types with different stats.
```

**What you should see:** Claude reads your existing game file, understands the code structure, and adds a combat system — monsters, HP tracking, turn-based battles, ASCII health bars. It modifies the existing file rather than starting over.

Run it again:
```
Run the game again so I can test the combat
```

**What you should see:** The game now has monsters! Enter a room with a monster and you'll get a combat encounter with options to attack, defend, or run.

💡 **What you just learned:** This is **iteration** — Claude reads the existing code (👀 read), understands it, and modifies it (📝 edit). You didn't need to explain the existing code or point to specific files. Claude figured it out.

---

### Step 5: Add a boss fight and treasure

Let's get ambitious. More features, one prompt.

**Paste this into Claude Code:**
```
Make the game more interesting: Add a treasure system — gold drops from monsters, and some rooms have treasure chests. Add an inventory display. Put a boss monster guarding the exit room — it should have a unique name, way more HP, and a special attack. The player needs to defeat the boss to win. Add a victory screen with ASCII art when you beat the boss and show total gold collected.
```

**What you should see:** Claude adds treasure, an inventory, and a boss fight — all integrated with the existing combat and movement systems. Run it:

```
Run the game and let me fight the boss
```

Play through and try to beat the boss. If you die, that's part of the fun.

💡 **What you just learned:** Claude handles **complex, multi-feature requests**. It figured out how treasure interacts with combat, how the boss blocks the exit, and how the victory screen triggers. You described the product — Claude handled the implementation.

---

### Step 6: Add save and load — file I/O

Here's where it gets interesting from a skills perspective.

**Paste this into Claude Code:**
```
Add a save/load system to the dungeon game. When the player presses 'q', offer to save their progress to a JSON file. When the game starts, check if a save file exists and ask if they want to continue. Save the player's position, HP, gold, inventory, and which monsters have been defeated.
```

**What you should see:** Claude adds file I/O to the game — writing game state to a JSON file and reading it back on startup. Run it:

```
Run the game, explore a bit, then save and quit. Then run it again and load the save.
```

**What you should see:** The game saves your progress to a file like `save_game.json`. When you restart, it asks if you want to continue and drops you right where you left off.

💡 **What you just learned:** Claude creates and reads **data files**, not just code. This is the same skill you'll use for configs, exports, reports, and any project that needs persistent state. You can even ask Claude to read the save file:

```
Show me what the save file looks like
```

You'll see the JSON structure — your game state, saved as data.

---

### Step 7: Make it beautiful — polish and design

Time for the finishing touches.

**Paste this into Claude Code:**
```
Make the dungeon game look amazing. Add ANSI color codes — red for monsters, green for the player, yellow for gold/treasure, cyan for room descriptions. Add ASCII art for: the title screen, monster encounters (different art per monster type), the boss, and the victory screen. Add a HUD at the bottom showing HP, gold, and current room name. Make it feel polished and professional.
```

**What you should see:** Claude goes through the entire codebase and adds color, ASCII art, and a HUD. This is a big change — lots of edits across the file. Run it:

```
Run the final version of the game
```

**What you should see:** A colorful, polished terminal dungeon crawler with ASCII art, colored text, a HUD, and visual flair. This is a real game. You built it in 15 minutes.

## 🎉 What Just Happened

You just built a complete, playable terminal game through conversation. Let's count what Claude Code did:

| Step | Claude Code Skill | What It Did |
|------|------------------|-------------|
| 2 | 📄 Create + 📝 Edit | Built the base game from scratch |
| 3 | 🖥️ Run | Executed the Python script in your terminal |
| 4 | 👀 Read + 📝 Edit | Read existing code, added combat system |
| 5 | 📝 Edit | Added multiple features to existing code |
| 6 | 📄 Create + 👀 Read | Built save/load with JSON file I/O |
| 7 | 👀 Read + 📝 Edit | Polish pass — read everything, improved everything |

Every step used the same loop: **think → use tool → observe → think → use tool**. Claude reads your request, reads the existing code, plans changes, writes them, and sometimes runs the result. This is the **agent loop** — and it's how you'll build everything in this course.

You didn't learn "how to make a game." You learned how Claude Code creates files, edits code, runs programs, and reads context to iterate on complex projects. The game was just the fun wrapper.

## Go Deeper

Ready to keep pushing? Try these prompts:

- **"Add procedural level generation — random dungeon layouts each time"** — teaches Claude to write algorithms
- **"Add a multiplayer mode using websockets"** — teaches networking concepts
- **"Port this to a web version using HTML Canvas"** — teaches cross-platform thinking
- **"Add sound effects using the terminal bell or a sound library"** — teaches system integration
- **"Add a leaderboard that saves to a file"** — more file I/O practice

Each of these is one prompt away. That's the point.

## Share

**Bring back:** A screenshot of your dungeon crawler — either the map, a combat encounter, or your victory screen after beating the boss. Bonus points if you added a feature we didn't cover.
