# Course Plan — Sub-Agent Reference

## Lesson Format (MANDATORY for every lesson file)

Every lesson MUST follow this exact structure:

```markdown
# [Lesson Number]. [Title]

> **Magic Moment:** [One sentence — what the student will experience that shifts their mental model]

## Why This Matters
[2-4 sentences. No theory dumps. Connect to their real work as a PM.]

## Before You Start
[Prerequisites — what they need open, installed, or ready]

## Do This Now

### Step 1: [Action verb]
[Clear instruction]

**Paste this into Claude Code:**
\```
[Copy-pasteable prompt]
\```

**What you should see:** [Expected output so they know it worked]

### Step 2: [Action verb]
[Next step...]

### Step 3: [Action verb]
[The magic moment step — this is where the "wow" happens]

## 🎉 What Just Happened
[Brief explanation of the mechanics — WHY it worked, what Claude did under the hood. 3-5 sentences max.]

## Go Deeper
[Optional: links, variations, advanced techniques, relevant YouTube videos]

## Share
[One prompt for the cohort: "Bring back: ___"]
```

## Tone & Style Rules
- Write like you're pair-programming with a friend, not lecturing
- Use emoji sparingly but effectively (🎉 for magic moments, ⚠️ for gotchas, 💡 for tips)
- Include "Expected output" after every prompt so students know they're on track
- If there are relevant YouTube videos or images from the Notion course, include URLs
- Make prompts progressively more impressive (build confidence → then blow their mind)
- No filler. Every sentence earns its spot.
- Address the reader as "you" — never "the student" or "users"

## Key Notion Page IDs (for reading source content)
Use NOTION_API_KEY from ~/.config/notion/api_key

### Root pages
- Claude Code for PMs: 303908c9-2c01-81e1-8c35-e0fe313d3976
- Claude Code for Stock Investing: 31a908c9-2c01-80d3-8ff5-fadd508cd79c

### Day 1 pages
- Course overview: 31f908c9-2c01-802f-a198-d807202c6ebf
- Setup Guide: 303908c9-2c01-814e-b650-c2c2154a89da
- Get comfortable: 303908c9-2c01-8157-92f1-e382a54eba97
- How do LLMs work: 303908c9-2c01-818f-ad47-f865153f8753
- How do coding agents work: 303908c9-2c01-8192-aa35-c9b617b9ecbb
- Skills overview: 31f908c9-2c01-8136-83cd-e37364cb698b
- Exercise Install skill: 31f908c9-2c01-81ad-9d35-f287bfd0fd5f

### Day 2 pages
- Introduce Claude to your product: 303908c9-2c01-81ed-833e-d364105136ba
- Brainstorm features: 303908c9-2c01-81d6-a66e-fa14a6f94582
- Download codebase: 303908c9-2c01-81d2-857d-e7094049b085
- Get product running: 303908c9-2c01-8180-9598-e8e557e75fd3
- Create project memory: 303908c9-2c01-81b6-86e8-c0bfe5786536
- Exercise brainstorm: 303908c9-2c01-8146-a9b6-c19e0bd25e1a

### Day 3 pages
- Build features that look great: 31f908c9-2c01-8191-9e0e-d2ed34f8be1d
- Read and improve design: 31f908c9-2c01-818e-9bc1-cefb35fd0dfa
- Start creating prototypes: 303908c9-2c01-81c5-b4e3-f81792d34d8f
- Get features right: 303908c9-2c01-81f8-9041-c7d00c605e23
- Apply design thinking: 303908c9-2c01-8123-be89-fae28eee4f01
- Architecture: 303908c9-2c01-814c-b011-eab3113296a7
- Build many prototypes: 303908c9-2c01-812d-853a-fb85631d4bdb
- Exercise first prototype: 303908c9-2c01-81f9-8fd4-d1a0e9616b50
- Exercise ambitious prototype: 303908c9-2c01-8158-a6e8-f9cc713e9cb1
- Exercise external context: 303908c9-2c01-81d2-8464-ff509c49acc2
- Exercise copy something: 303908c9-2c01-81e7-be5a-c8dad1ad1a18
- MCP servers: 303908c9-2c01-816a-8535-f0eb512a092f
- External documentation: 303908c9-2c01-81d2-9e56-fad227f2fdc9
- Keeping agent smart: 31f908c9-2c01-81ae-9ad2-ff1c713c7faf
- Context window: 303908c9-2c01-81b6-9f6b-e4c54786adc9

### Day 4 pages
- Re-create designs: 303908c9-2c01-815b-bd19-ffd37c29a7c5
- Exercise recreate UI: 303908c9-2c01-81bd-90c3-f697ba242efd
- Exercise map architecture: 303908c9-2c01-8191-a818-f1b4babfc04c
- design.md: 303908c9-2c01-8159-86d0-e032ab194344
- Improve design sense: 303908c9-2c01-8192-bf8b-f3cad115f8ce
- Shortcuts: 303908c9-2c01-816f-bf7f-dd3f5b6f4e02
- Plugins: 303908c9-2c01-8112-938d-dc363cd8d49b

### Day 5 pages
- Analyze onboarding: 303908c9-2c01-81be-a7cf-d2d4b2250712
- Customer feedback: 303908c9-2c01-8191-8f23-d676046361d7
- Release notes: 303908c9-2c01-818a-ba41-dc83847ff436
- Product guides: 303908c9-2c01-81ea-a840-e3f41603bf1b
- Backlog: 303908c9-2c01-81ab-9ac1-f8b13d3de7d6
- Usage analysis: 303908c9-2c01-8110-a8fc-fb3f037bc80e
- Competition: 303908c9-2c01-8179-a88a-cf6de0c39bae
- Pricing: 303908c9-2c01-8130-8997-eaa8d05c166a
- Storyboards: 303908c9-2c01-81dd-b04d-d91fa64d0840
- Stakeholder updates: 303908c9-2c01-81fe-a28f-cd86ea64dcb6
- Exercise onboarding: 31f908c9-2c01-81f6-911e-fb74eca63742
- Exercise PM task: 31f908c9-2c01-815b-858a-d37e2b611ee1
- Dogfood testing: 31f908c9-2c01-8180-89b3-f9cc8b6f6131

### Day 6 pages
- Deploying: 303908c9-2c01-81f7-bebb-ffa328451216
- Tests: 303908c9-2c01-81e1-bcbe-d42022b59f4c
- Code review: 303908c9-2c01-8197-b0bf-d326aefda4f2
- Personal OS: 303908c9-2c01-81f8-93e1-db14b9cb5f2f
- AI mindset: 303908c9-2c01-81a3-91ed-de3521fab736
- CI/CD concept: 303908c9-2c01-81fe-953b-f7510e4088ed
- Exercise CI/CD: 303908c9-2c01-8185-b81c-f479c1591023
- Tracing: 303908c9-2c01-8183-90a9-e8bb1c1ab1df
- OpenClaw: 31f908c9-2c01-81eb-b812-caa7ea4c3a62
