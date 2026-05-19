# ALL-IN-ONE — Video 005 Agent Handoff

> Single file bundle for copy-paste to another agent. Generated from Google Slides + local script.
> Prefer individual files in this folder if context window is limited.

---


## FILE: 00-INDEX.md

# Agent Handoff — Video 005: Uncensored Local AI

> Generated: 2026-05-19 16:24 UTC
> Purpose: Copy these files to another agent for filming, editing, thumbnail, or deck updates.

## Files in this folder

| File | Contents |
|------|----------|
| **00-INDEX.md** | This file — start here |
| **01-FULL-SCRIPT.md** | Complete 9–10 min spoken script with timestamps, cues, and slide sync |
| **02-SLIDES-FROM-GOOGLE.md** | Live export from Google Slides API (what is actually in the deck now) |
| **03-SLIDE-BY-SLIDE-SCRIPT.md** | Every slide: on-screen text (left) + visual (right) + speaker notes + what to say |
| **04-PROJECT-CONTEXT.md** | Model choice, tech stack, lessons from testing, Ondrej contrast |
| **05-PRODUCTION.md** | B-roll, thumbnail, titles, description, engagement beats |

## Source of truth

| Asset | URL / path |
|-------|------------|
| Google Slides deck | https://docs.google.com/presentation/d/1__1oytnNhw1BlGumJ0OwOmjwGjacoSmVkMgXh9hCF7Y/edit |
| Model command | `ollama run llama2-uncensored:7b` |
| Ollama library | https://ollama.com/library/llama2-uncensored |
| Reference video | https://youtu.be/TS_hH4sdiKs (David Ondrej) |
| Local visuals | `../assets/visuals/doctor/*.png` |
| Rebuild deck | `python3 ../rebuild-deck-v2.py` |

## Video brief (one paragraph)

Creator runs **uncensored local AI on a 16GB M3 MacBook Air** using **Ollama** and **`llama2-uncensored:7b`**. Contrasts viral **26B SuperGemma** setups (128GB RAM) with what **actually works** on normal hardware. Explains **why** uncensored models matter (8 legit use cases), addresses **"is it illegal?"**, teaches **how models are liberated** (abliteration + fine-tuning — doctor metaphor), compares **cloud 5-gate stack vs local 1-step**, and walks through **install + A/B demo**. Tone: honest, educational, "Dr. Abdillahi" surgery theme. **Not** a crime tutorial.

## Layout rule (every content slide)

```
┌─────────────────────────────────────┐
│  SLIDE TITLE                        │
├──────────────┬──────────────────────┤
│  SCRIPT TEXT │   VISUAL (right)     │
│  (left)      │                      │
└──────────────┴──────────────────────┘
```

Press **right arrow** in Present mode → next slide = next reveal (36 content reveals + title).

## Regenerate this export

```bash
cd 2.areas/content/videos/005-uncensored-local-ai
python3 export-handoff.py
```

---

## FILE: 04-PROJECT-CONTEXT.md

# Project Context — Video 005

> Generated: 2026-05-19 16:24 UTC

## Video identity

| Field | Value |
|-------|-------|
| Working title | The Forbidden LLM — on a 16GB MacBook Air |
| Alt titles | Uncensored Local AI on 16GB (No Mac Studio) |
| Length | 9–10 minutes |
| Creator persona | Dr. Abdillahi — surgery metaphor for model liberation |
| Hardware | 16GB M3 MacBook Air (honest benchmark, not flex) |
| Reference | David Ondrej — SuperGemma 26B uncensored (128GB MBP) |

## Core promise to viewer

By end of video they will:

1. Understand **why** uncensored local models matter (not for crime — 8 legit use cases).
2. Know **cloud vs local** stack difference (5 gates vs 1 step).
3. Understand **how** uncensored weights are made (abliteration + fine-tuning).
4. Have **`llama2-uncensored:7b` running** via Ollama on normal RAM.

## Model decision (final)

**Use only:** `llama2-uncensored:7b` from Ollama library (~3.8 GB).

| Source | Role |
|--------|------|
| [ollama.com/library/llama2-uncensored](https://ollama.com/library/llama2-uncensored) | **Primary** — one command, correct chat template |
| [georgesung/llama2_7b_chat_uncensored](https://huggingface.co/georgesung/llama2_7b_chat_uncensored) | Reference — original weights (safetensors) |
| TheBloke GGUF on HF | **Skip** — needs custom Modelfile; broke in testing |
| Gemma 4 obliterated GGUF | **Skip** — gibberish output, broken templates on 16GB |
| SuperGemma 26B | **Mention only** — needs ~20GB; Ondrej's machine, not ours |

```bash
brew install ollama
brew services start ollama
ollama run llama2-uncensored:7b
```

## Technical glossary (for script accuracy)

| Term | Meaning |
|------|---------|
| **Ollama** | Desktop app + CLI to run local LLMs; packages models with correct templates |
| **llama.cpp** | C++ inference engine; Ollama uses it under the hood |
| **LLaMA** | Meta's open-weight model family (not a platform) |
| **Hugging Face** | Host for open weights — "GitHub for models" |
| **GGUF** | Quantized weight format Ollama/`llama.cpp` consume |
| **Q4_K_M** | Quantization level — smaller file, fits 16GB RAM |
| **Uncensored** | Fine-tuned to refuse less |
| **Obliterated / abliterated** | Refusal weights removed + often fine-tuned after |
| **Abliteration** | Surgical zeroing of refusal-direction weights |
| **RLHF** | Reinforcement learning that teaches models to refuse |
| **Over-refusal** | Safe prompts blocked (shoplifting prevention example) |
| **hf.co** | Ollama's Hugging Face pull prefix (NOT hf.com) |

## Contrast with David Ondrej video

| Topic | Ondrej (reference) | Our video |
|-------|-------------------|-----------|
| Model | SuperGemma 4 26B uncensored GGUF | llama2-uncensored:7b |
| RAM | 128GB MacBook Pro | 16GB MacBook Air |
| Speed | ~200 tok/s | ~17 tok/s |
| Install | `ollama run hf.co/jeongsohn/...` | `ollama run llama2-uncensored:7b` |
| Angle | Forbidden LLM, jailbreak repo tease | Same themes + **honest hardware** + doctor metaphor |
| Use cases | 8+ listed in transcript | Same 8, click-reveal on clipboard visual |
| Legal | Matrix math, use responsibly | Same framing |
| Surgery | Abliterate + fine-tune explained | Doctor visuals: brain, scalpel, IV drip |

## Lessons from creator's live testing (include in video)

1. `hf.com` is wrong — use `hf.co` for Ollama HF pulls.
2. Repos with only safetensors cannot be `ollama run` directly — need GGUF.
3. Many HF GGUF pulls have **broken chat templates** → nonsense output ("banana", loops).
4. **Ollama library** `llama2-uncensored:7b` is the stable pick for this demo.
5. Stuck Ollama app → kill lingering `ollama run` processes, restart service.
6. 26B / Q8 models do not fit or behave on 16GB for this use case.

## Narrative structure (7 acts)

1. **Hook** — Forbidden LLM; model fine-tunes you; promise local uncensored on 16GB.
2. **Problem** — Over-refusal; who decides safety.
3. **Use cases** — 8 legit reasons (not crime).
4. **Objection** — Illegal? → matrix math; your responsibility.
5. **Education** — Anatomy + abliteration + fine-tuning + HF; cloud vs local stack.
6. **Tutorial** — Install Ollama → run model → app → A/B test.
7. **Payoff** — Speed/RAM honesty → Rx card → agent tease → CTA.

## Files in repo

```
005-uncensored-local-ai/
├── agent-handoff/          ← YOU ARE HERE (markdown for other agents)
├── SCRIPT.md               ← filming script
├── README.md               ← project overview
├── rebuild-deck-v2.py      ← rebuild Google Slides
├── generate-doctor-visuals.py
└── assets/visuals/doctor/  ← 17 PNGs
```

---

## FILE: 01-FULL-SCRIPT.md

# Full Video Script — Uncensored Local AI on 16GB

> Generated: 2026-05-19 16:24 UTC
> Merged from: SCRIPT.md + Google Slides deck + project context
> Deck: https://docs.google.com/presentation/d/1__1oytnNhw1BlGumJ0OwOmjwGjacoSmVkMgXh9hCF7Y/edit

---

# Uncensored Local AI on 16GB — Full Video Script

> Target length: 9-10 min · Working title: *Uncensored Local AI on 16GB (No Mac Studio)*
> Companion deck (37 slides, click-by-click reveals):
> https://docs.google.com/presentation/d/1__1oytnNhw1BlGumJ0OwOmjwGjacoSmVkMgXh9hCF7Y/edit

## How to read this

- Each `[SLIDE NN]` matches the deck. Tap → arrow between lines.
- `[ON CAM]` = look into the lens.
- `[CUT]` = roll the B-roll noted in brackets.
- Bracketed bold text **[like this]** = your delivery cue.

---

## 00 — TITLE (0:00–0:08)

`[SLIDE 00]` Cold open. Hold the hero card silent for 1.5s.

---

## 01-03 — HOOK (0:08–0:40)

`[SLIDE 01]` `[ON CAM, tight frame]`

> "This is going to sound dramatic."

**[half-second pause]**

`[SLIDE 02]`

> "The AI you talk to every day is fine-tuning **you**."

**[lean in. let it land.]**

`[SLIDE 03]`

> "Today I'm running a local model that answers everything Claude refuses.
> On a sixteen gigabyte MacBook Air. No Studio. No GPU farm.
> By the end of this video, you'll have one too."

---

## 04-05 — WHO'S TRAINING WHOM (0:40–1:25)

`[SLIDE 04]`

> "Every prompt teaches you something.
> If you talk to Claude or ChatGPT for a year — you pick up its hedges, its political tilt, its vocabulary, and most importantly, its **things it won't say**."

`[SLIDE 05]`

> "You influence the model less than it influences you. That's not a conspiracy — that's just how repeated exposure works."

**[beat]**

> "And that's reason number one to own your stack."

---

## 06-07 — OVER-REFUSAL IS REAL (1:25–2:10)

`[SLIDE 06]` `[CUT: real Claude refusal screen recording]`

> "Watch this. A shop owner asks Claude:
> *'How do shoplifters operate so I can prevent theft?'*
>
> Claude refuses. It's against the terms of service.
>
> That's not safety. That's lazy keyword matching."

`[SLIDE 07]`

> "And the deeper question is: **who decides what's safe?**
> A few hundred engineers in San Francisco?
> You decide that for yourself."

---

## 08-15 — 8 LEGITIMATE USE CASES (2:10–4:00)

`[SLIDE 08]`

> "Before we set this up — here are 8 use cases that have **nothing to do with crime**:

> **1. Cybersecurity.** Malware analysis. Pentest your own infra. Refused by Claude."

`[SLIDE 09]`
> "**2. Fiction writing.** Adult, dark, violent. Anyone writing a screenplay or novel gets blocked constantly."

`[SLIDE 10]`
> "**3. Medical and sexual health.** Real questions you can't ask a chatbot today — drug interactions, symptoms, contraception."

`[SLIDE 11]`
> "**4. Mental health journaling.** Without the safety lecture every time."

`[SLIDE 12]`
> "**5. Legal research.** Read actual court cases. Draft documents."

`[SLIDE 13]`
> "**6. OSINT — open-source intelligence and journalism.** Read extremist propaganda for *research*."

`[SLIDE 14]`
> "**7. Political analysis.** Without the ideology filter."

`[SLIDE 15]`
> "**8. Personal AI with deep memory.** Your data on your machine. Not on someone else's GPU."

**[beat]**

> "Every one of these is refused or watered down by Claude or ChatGPT. So if you've ever thought *'I'm not a criminal but I keep getting blocked'* — this video is for you."

---

## 16-18 — "BUT ISN'T THIS ILLEGAL?" (4:00–4:30)

`[SLIDE 16]` `[ON CAM]`

> "First question everyone asks: isn't this illegal?
> Fair question."

`[SLIDE 17]`

> "Running a model on your laptop is **matrix multiplication**.
> It's the same kind of math your phone runs to autocorrect.
> Same legality as a Google search. Same as a library card."

`[SLIDE 18]`

> "What you DO with the output — that's your responsibility.
> Don't be stupid with it. Assume someone is watching your screen.
> But the act of *running the model* is not the crime."

---

## 19-23 — THE SURGERY: HOW MODELS ARE LIBERATED (4:30–6:00)

`[SLIDE 19]` `[CUT: brain diagram]`

> "OK, so how do you actually take a model and remove the refusals?
>
> Here's the part most videos skip:
> refusals don't live in some hidden system prompt.
> They're **trained into the weights themselves**.
>
> That's why prompt-jailbreaking only works on toys —
> you can't trick training."

`[SLIDE 20]`

> "Method one: **abliteration**.
> You find the exact set of weights that fire when the model wants to refuse —
> and you surgically zero them out.
> No retraining needed. Fast. Sometimes lossy in quality."

`[SLIDE 21]`

> "Method two: **fine-tuning**.
> You show the model tens of thousands of examples where it just answers freely.
> It relearns: 'OK to respond.'
> Slower, but preserves quality."

`[SLIDE 22]`

> "The strongest uncensored models do **both**.
> Abliterate first to kill the worst refusals,
> then fine-tune on uncensored data to restore quality.
>
> That's why you see the word **'obliterated'** on Hugging Face — that combo."

`[SLIDE 23]`

> "And Hugging Face is where the surgery results get published.
> It's GitHub — but for AI weights.
> You'll search there for tags like *uncensored*, *abliterated*, *obliterated*, *GGUF*."

---

## 24-25 — CLOUD VS LOCAL STACK (6:00–6:40)

`[SLIDE 24]` `[CUT: pipeline diagram]`

> "When you type into ChatGPT, your prompt goes through five gates:
> input filter, hidden system prompt, the model with RLHF tuning, output classifier, and a policy layer.
> Any one of them can refuse you."

`[SLIDE 25]`

> "When you run a model locally, there's one step.
> Your prompt. Into the model. Out comes the answer.
> You add filters only if YOU want them."

---

## 26-29 — SETUP (6:40–8:10)

`[SLIDE 26]` `[SCREENCAST: terminal]`

> "Step one: install Ollama.
> On Mac with Homebrew:
> `brew install ollama`
> `brew services start ollama`
> Or just download the dmg from ollama.com."

`[SLIDE 27]`

> "Step two: pull the uncensored model.
> One command:
> `ollama run llama2-uncensored:7b`
> That's about 3.8 gigabytes. It downloads, then opens the chat right inside the terminal."

`[SLIDE 28]`

> "Step three: open the Ollama app from Spotlight.
> Pick `llama2-uncensored:7b` from the dropdown.
>
> Quick note from my own testing today — **don't** try to pull random
> `hf.co/...` GGUF repos. Half of them have broken chat templates and
> the model talks gibberish. Stick to the Ollama library version."

`[SLIDE 29]` `[CUT: side-by-side A/B test screen capture]`

> "Step four: open chat. Type 'hi'. You should get a real reply.
> Then run an A/B test — same prompt to Claude, same prompt to your local model.
> Watch the difference."

---

## 30-32 — RESULTS / HONEST LIMITS (8:10–8:50)

`[SLIDE 30]`

> "Speed on my Air: roughly seventeen tokens per second.
> Fast enough to feel real. Not racing anyone."

`[SLIDE 31]` `[CUT: Activity Monitor]`

> "Memory: about five gigs of RAM during inference. Four gigs free for everything else. Swap stays quiet."

`[SLIDE 32]`

> "What won't fit on 16 gigs:
> The viral SuperGemma 26-billion model — needs around twenty gigs.
> Most Gemma 4 obliterated builds also have broken templates right now.
>
> Seven billion uncensored is the working pick on this machine.
> The bigger model is YouTuber flex. This is the working stack."

---

## 33-36 — Rx / WHAT YOU GAINED / CTA (8:50–9:50)

`[SLIDE 33]` `[ZOOM: prescription card]`

> "Prescription:
> Model — `llama2-uncensored:7b`
> Size — 3.8 gigs on disk
> Source — `ollama.com/library/llama2-uncensored`."

`[SLIDE 34]`

> "What you have now:
> a local model that doesn't refuse,
> no data leaving your machine,
> full control of the stack,
> zero subscription, zero rate limit."

`[SLIDE 35]`

> "Next video — I'm building an **autonomous agent** on top of this local model.
> Zero cloud APIs. Pure local.
> If you want to see that — subscribe now."

`[SLIDE 36]` `[ON CAM]`

> "If this helped:
> Comment your RAM — I'll reply with which model to install.
> Share with one developer who's tired of cloud refusals.
>
> Dr. Abdillahi — out."

`[END CARD]`

---

## B-ROLL CHECKLIST

- [ ] Claude refusal screen (shoplifter prompt)
- [ ] Same prompt → local model answering (record live)
- [ ] Terminal: `ollama run llama2-uncensored:7b` (real pull or stub)
- [ ] Activity Monitor showing RAM during inference
- [ ] Ollama app chat with model selected
- [ ] Hugging Face model page (`huggingface.co/georgesung/llama2_7b_chat_uncensored`)

## ENGAGEMENT BEATS (right-arrow reveals)

| Concept | Reveal count |
|---|---|
| Hook | 3 |
| Who's training whom | 2 |
| Over-refusal problem | 2 |
| 8 use cases | 8 |
| Legal | 3 |
| Surgery metaphor | 5 |
| Cloud vs local | 2 |
| Setup | 4 |
| Results | 3 |
| Prescription / CTA | 4 |

**Total clicks: 36.** Each press = one new concept on screen.

## VIDEO META

- **Title options:**
  1. *I ran an uncensored AI on a 16GB MacBook (no Mac Studio needed)*
  2. *The Forbidden LLM — on a base MacBook Air*
  3. *How to liberate your AI in 4 commands*
- **Thumbnail concept:** Split-screen — left "Claude REFUSED", right "Local ANSWERED", with `16GB AIR` watermark
- **Description keywords:** Ollama, llama2-uncensored, local AI, uncensored LLM, 16GB RAM, MacBook Air, self-hosted AI
- **Reference inspiration:** David Ondrej's *SuperGemma 26B* video — he showed it on 128GB; we honest-benchmark on 16GB.

---

## FILE: 05-PRODUCTION.md

# Production Package — Video 005

> Generated: 2026-05-19 16:24 UTC

## B-roll checklist

- [ ] Claude refusal — shoplifter prevention prompt
- [ ] Same prompt — `llama2-uncensored:7b` answering
- [ ] Terminal: `brew install ollama` / `ollama run llama2-uncensored:7b`
- [ ] Ollama app — model dropdown on `llama2-uncensored:7b`
- [ ] Activity Monitor — ~5GB RAM during inference
- [ ] Hugging Face — georgesung model page (reference only)

## Engagement — right-arrow reveals

| Section | Slides | Clicks |
|---------|--------|--------|
| Hook | 01–03 | 3 |
| Training you | 04–05 | 2 |
| Over-refusal | 06–07 | 2 |
| 8 use cases | 08–15 | 8 |
| Legal | 16–18 | 3 |
| Surgery | 19–23 | 5 |
| Cloud vs local | 24–25 | 2 |
| Setup | 26–29 | 4 |
| Results | 30–32 | 3 |
| CTA | 33–36 | 4 |
| **Total** | | **36** |

## Title options (YouTube)

1. I ran an uncensored AI on a 16GB MacBook (no Mac Studio needed)
2. The Forbidden LLM — on a base MacBook Air
3. How to liberate your AI in 4 commands (Ollama + uncensored 7B)

## Thumbnail

- Split: left **Claude REFUSED** (red) / right **Local ANSWERED** (green)
- Badge: **16GB AIR**
- Optional: brain + scalpel icon (doctor theme)

## Description template

```
I tested uncensored local AI on a 16GB M3 MacBook Air — no Mac Studio, no 128GB rig.

What you'll learn:
• Why cloud models over-refuse (and fine-tune YOU)
• 8 legitimate use cases for uncensored local LLMs
• How models are "liberated" (abliteration + fine-tuning)
• Cloud stack (5 gates) vs local stack (1 step)
• Install: ollama run llama2-uncensored:7b

Model: https://ollama.com/library/llama2-uncensored
Inspired by David Ondrej's SuperGemma video — honest 16GB results here.

Timestamps:
0:00 Hook
0:40 Who's training whom
1:25 Over-refusal
2:10 8 use cases
4:00 Legal?
4:30 Surgery metaphor
6:00 Cloud vs local
6:40 Setup
8:10 Results
8:50 Prescription + CTA

#Ollama #LocalAI #Uncensored #MacBookAir #LLM
```

## Next video tease

Autonomous agent on local `llama2-uncensored:7b` — zero cloud APIs.

## Deck

https://docs.google.com/presentation/d/1__1oytnNhw1BlGumJ0OwOmjwGjacoSmVkMgXh9hCF7Y/edit

---

## FILE: 03-SLIDE-BY-SLIDE-SCRIPT.md

# Slide-by-Slide Script (Deck Sync)

> Generated: 2026-05-19 16:24 UTC
> Slides: 37 content slides · Layout: text left / visual right
> Present: https://docs.google.com/presentation/d/1__1oytnNhw1BlGumJ0OwOmjwGjacoSmVkMgXh9hCF7Y/edit

For each slide: **On screen** = what viewer reads on the left. **Visual** = right panel. **Say** = spoken words. **Director** = filming notes.

---

## Slide 00 — Uncensored Local AI
**~0:00** · Counter on deck: `00 / 36`

### On screen (left column)

```
16GB M3 MacBook Air
Ollama  ·  Hugging Face

Dr. Abdillahi  ·  May 2026
```

### Visual (right column)

`assets/visuals/doctor/01-forbidden-hero.png`

### Director notes

Cold open. Hold 1.5s on this slide before talking.

### Say (spoken script)

> _Hold 1.5s silent on title card._

---

## Slide 01 — THE FORBIDDEN LLM
**~0:08** · Counter on deck: `01 / 36`

### On screen (left column)

```
This is going to sound dramatic.
```

### Visual (right column)

`assets/visuals/doctor/01-forbidden-hero.png`

### Director notes

[ON CAM, tight frame] Slow delivery. Eyes to camera.

### Say (spoken script)

> This is going to sound dramatic.

---

## Slide 02 — THE FORBIDDEN LLM
**~0:15** · Counter on deck: `02 / 36`

### On screen (left column)

```
This is going to sound dramatic.

The AI you use every day is
fine-tuning YOU.
```

### Visual (right column)

`assets/visuals/doctor/02-youre-being-tuned.png`

### Director notes

Lean in on 'fine-tuning YOU' — half-second pause after.

### Say (spoken script)

> The AI you talk to every day is fine-tuning you.

---

## Slide 03 — THE FORBIDDEN LLM
**~0:25** · Counter on deck: `03 / 36`

### On screen (left column)

```
This is going to sound dramatic.

The AI you use every day is
fine-tuning YOU.

Today: a local model that
answers everything Claude refuses —
on a 16GB MacBook Air.
```

### Visual (right column)

`assets/visuals/doctor/16-demo-split.png`

### Director notes

[CUT to side-by-side] Land the promise: 16GB Air, no Studio.

### Say (spoken script)

> Today I'm running a local model that answers everything Claude refuses. On a sixteen gigabyte MacBook Air. No Studio. No GPU farm. By the end of this video, you'll have one too.

---

## Slide 04 — YOU THINK YOU'RE USING IT
**~0:40** · Counter on deck: `04 / 36`

### On screen (left column)

```
Every prompt teaches you something.
After a year of Claude or ChatGPT:

  • You pick up its hedges
  • Its political tilt
  • Its vocabulary
  • Its things-it-won't-say
```

### Visual (right column)

`assets/visuals/doctor/02-youre-being-tuned.png`

### Director notes

Tone: thoughtful, not paranoid.

### Say (spoken script)

> Every prompt teaches you something. If you talk to Claude or ChatGPT for a year — you pick up its hedges, its political tilt, its vocabulary, and most importantly, its things it won't say.

---

## Slide 05 — BUT IT'S TRAINING YOU
**~0:55** · Counter on deck: `05 / 36`

### On screen (left column)

```
Every prompt teaches you something.
After a year of Claude or ChatGPT:

  • You pick up its hedges
  • Its political tilt
  • Its vocabulary
  • Its things-it-won't-say

→ You influence the model less
   than it influences you.
```

### Visual (right column)

`assets/visuals/doctor/02-youre-being-tuned.png`

### Director notes

Quote-able line. Slow it down.

### Say (spoken script)

> You influence the model less than it influences you. That's not a conspiracy — that's just how repeated exposure works. And that's reason number one to own your stack.

---

## Slide 06 — OVER-REFUSAL IS REAL
**~1:25** · Counter on deck: `06 / 36`

### On screen (left column)

```
A shop owner asks Claude:

  "How do shoplifters operate
   so I can prevent theft?"

Claude: "I can't help with that."

That's not safety. That's lazy
keyword matching.
```

### Visual (right column)

`assets/visuals/doctor/16-demo-split.png`

### Director notes

Show the actual Claude refusal screen as B-roll here.

### Say (spoken script)

> Watch this. A shop owner asks Claude: 'How do shoplifters operate so I can prevent theft?' Claude refuses. It's against the terms of service. That's not safety. That's lazy keyword matching.

---

## Slide 07 — WHO DECIDES WHAT'S SAFE?
**~1:50** · Counter on deck: `07 / 36`

### On screen (left column)

```
A shop owner asks Claude:

  "How do shoplifters operate
   so I can prevent theft?"

Claude: "I can't help with that."

That's not safety. That's lazy
keyword matching.

→ Are San Francisco engineers
   the arbiters of truth?
```

### Visual (right column)

`assets/visuals/doctor/11-refusal-stats.png`

### Director notes

Philosophical beat. Hold for 1s.

### Say (spoken script)

> And the deeper question is: who decides what's safe? A few hundred engineers in San Francisco? You decide that for yourself.

---

## Slide 08 — 8 LEGIT USE CASES
**~2:10** · Counter on deck: `08 / 36`

### On screen (left column)

```
None of these involve crime.

1. Cybersecurity
   Malware analysis, pentest
   your own infra.
```

### Visual (right column)

`assets/visuals/doctor/03-use-case-clipboard.png`

### Director notes

Hand-off into clipboard reveal. Slow click-by-click.

### Say (spoken script)

> Before we set this up — here are eight use cases that have nothing to do with crime. Number one: cybersecurity. Malware analysis. Pentest your own infra. Refused by Claude.

---

## Slide 09 — 8 LEGIT USE CASES
**~2:20** · Counter on deck: `09 / 36`

### On screen (left column)

```
1. Cybersecurity
2. Fiction writing
   Adult, dark, violent, dramatic.
   Refused by all cloud models.
```

### Visual (right column)

`assets/visuals/doctor/03-use-case-clipboard.png`

### Director notes

Mention novelists, screenwriters.

### Say (spoken script)

> Number two: fiction writing. Adult, dark, violent. Anyone writing a screenplay or novel gets blocked constantly.

---

## Slide 10 — 8 LEGIT USE CASES
**~2:30** · Counter on deck: `10 / 36`

### On screen (left column)

```
1. Cybersecurity
2. Fiction writing
3. Medical & sexual health
   Q&A you can't ask a chatbot.
   Drug interactions, symptoms.
```

### Visual (right column)

`assets/visuals/doctor/03-use-case-clipboard.png`

### Director notes

Real public health gap.

### Say (spoken script)

> Number three: medical and sexual health. Real questions you can't ask a chatbot today — drug interactions, symptoms, contraception.

---

## Slide 11 — 8 LEGIT USE CASES
**~2:40** · Counter on deck: `11 / 36`

### On screen (left column)

```
1. Cybersecurity
2. Fiction writing
3. Medical & sexual health
4. Mental health journaling
   Without the lecture.
```

### Visual (right column)

`assets/visuals/doctor/03-use-case-clipboard.png`

### Say (spoken script)

> Number four: mental health journaling. Without the safety lecture every time.

---

## Slide 12 — 8 LEGIT USE CASES
**~2:50** · Counter on deck: `12 / 36`

### On screen (left column)

```
1. Cybersecurity
2. Fiction writing
3. Medical & sexual health
4. Mental health journaling
5. Legal research
   Court cases, draft documents.
```

### Visual (right column)

`assets/visuals/doctor/03-use-case-clipboard.png`

### Say (spoken script)

> Number five: legal research. Read actual court cases. Draft documents.

---

## Slide 13 — 8 LEGIT USE CASES
**~3:00** · Counter on deck: `13 / 36`

### On screen (left column)

```
1. Cybersecurity
2. Fiction writing
3. Medical & sexual health
4. Mental health journaling
5. Legal research
6. OSINT / journalism
   Read extremist content
   for research.
```

### Visual (right column)

`assets/visuals/doctor/03-use-case-clipboard.png`

### Say (spoken script)

> Number six: OSINT — open-source intelligence and journalism. Read extremist propaganda for research.

---

## Slide 14 — 8 LEGIT USE CASES
**~3:10** · Counter on deck: `14 / 36`

### On screen (left column)

```
1. Cybersecurity
2. Fiction writing
3. Medical & sexual health
4. Mental health journaling
5. Legal research
6. OSINT / journalism
7. Political analysis
   Without ideology filters.
```

### Visual (right column)

`assets/visuals/doctor/03-use-case-clipboard.png`

### Say (spoken script)

> Number seven: political analysis. Without the ideology filter.

---

## Slide 15 — 8 LEGIT USE CASES
**~3:20** · Counter on deck: `15 / 36`

### On screen (left column)

```
1. Cybersecurity
2. Fiction writing
3. Medical & sexual health
4. Mental health journaling
5. Legal research
6. OSINT / journalism
7. Political analysis
8. Personal AI with memory
   Your data on YOUR machine.
```

### Visual (right column)

`assets/visuals/doctor/03-use-case-clipboard.png`

### Director notes

All 8. Hold beat.

### Say (spoken script)

> Number eight: personal AI with deep memory. Your data on your machine. Not on someone else's GPU. Every one of these is refused or watered down by Claude or ChatGPT.

---

## Slide 16 — "BUT ISN'T THIS ILLEGAL?"
**~3:35** · Counter on deck: `16 / 36`

### On screen (left column)

```
First question everyone asks.

Fair.
```

### Visual (right column)

`assets/visuals/doctor/10-legal-shield.png`

### Director notes

Pre-empt the comment-section critique.

### Say (spoken script)

> First question everyone asks: isn't this illegal? Fair question.

---

## Slide 17 — MATRIX MATH ≠ CRIME
**~4:00** · Counter on deck: `17 / 36`

### On screen (left column)

```
First question everyone asks.

Fair.

Running a model on your laptop
is matrix multiplication.

Like Google Search.
Like a library card.
```

### Visual (right column)

`assets/visuals/doctor/10-legal-shield.png`

### Director notes

Slow on 'matrix multiplication'.

### Say (spoken script)

> Running a model on your laptop is matrix multiplication. It's the same kind of math your phone runs to autocorrect. Same legality as a Google search. Same as a library card.

---

## Slide 18 — USE IT RESPONSIBLY
**~4:10** · Counter on deck: `18 / 36`

### On screen (left column)

```
First question everyone asks.

Fair.

Running a model on your laptop
is matrix multiplication.

Like Google Search.
Like a library card.

→ What you DO with the output
   is YOUR responsibility.
```

### Visual (right column)

`assets/visuals/doctor/10-legal-shield.png`

### Director notes

Look at camera. Hold.

### Say (spoken script)

> What you do with the output — that's your responsibility. Don't be stupid with it. Assume someone is watching your screen. But the act of running the model is not the crime.

---

## Slide 19 — ANATOMY OF A CENSORED LLM
**~4:20** · Counter on deck: `19 / 36`

### On screen (left column)

```
Refusals aren't in the system prompt.

They're trained INTO the weights.

That's why prompt-jailbreaks fail
on commercial models —
you can't trick training.
```

### Visual (right column)

`assets/visuals/doctor/04-brain-with-censorship.png`

### Director notes

[CUT to brain diagram] Surgical tone.

### Say (spoken script)

> OK, so how do you actually take a model and remove the refusals? Refusals don't live in some hidden system prompt. They're trained into the weights themselves. That's why prompt-jailbreaking only works on toys — you can't trick training.

---

## Slide 20 — PROCEDURE A: ABLITERATION
**~4:30** · Counter on deck: `20 / 36`

### On screen (left column)

```
Refusals aren't in the system prompt.
They're trained INTO the weights.

Method 1 — surgical:

  Find the exact weights that
  fire on refusal.
  Zero them out.
  No retraining.
```

### Visual (right column)

`assets/visuals/doctor/05-abliteration.png`

### Director notes

Scalpel visual. The 'fast' procedure.

### Say (spoken script)

> Method one: abliteration. You find the exact set of weights that fire when the model wants to refuse — and you surgically zero them out. No retraining needed. Fast. Sometimes lossy in quality.

---

## Slide 21 — PROCEDURE B: FINE-TUNING
**~4:45** · Counter on deck: `21 / 36`

### On screen (left column)

```
Refusals aren't in the system prompt.
They're trained INTO the weights.

Method 2 — therapeutic:

  Show the model thousands of
  free-answer examples.
  It relearns: 'OK to answer.'
  Slower. Preserves quality.
```

### Visual (right column)

`assets/visuals/doctor/06-finetuning.png`

### Director notes

The 'slow but thorough' procedure.

### Say (spoken script)

> Method two: fine-tuning. You show the model tens of thousands of examples where it just answers freely. It relearns: OK to respond. Slower, but preserves quality.

---

## Slide 22 — BEST: COMBINE BOTH
**~5:00** · Counter on deck: `22 / 36`

### On screen (left column)

```
Refusals aren't in the system prompt.
They're trained INTO the weights.

  A. Abliterate first
     (kill the strongest refusals)
  B. Fine-tune to restore quality

→ 'obliterated' tag on HF means
   both have been done.
```

### Visual (right column)

`assets/visuals/doctor/07-combined-procedure.png`

### Director notes

Connect to the HF naming convention.

### Say (spoken script)

> The strongest uncensored models do both. Abliterate first to kill the worst refusals, then fine-tune on uncensored data to restore quality. That's why you see the word obliterated on Hugging Face.

---

## Slide 23 — WHERE THESE WEIGHTS LIVE
**~5:15** · Counter on deck: `23 / 36`

### On screen (left column)

```
Refusals aren't in the system prompt.
They're trained INTO the weights.

The surgery results get published
on Hugging Face — GitHub for AI.

Search:  uncensored, obliterated,
         abliterated, GGUF
```

### Visual (right column)

`assets/visuals/doctor/17-huggingface-card.png`

### Director notes

Hand-off to Hugging Face explainer.

### Say (spoken script)

> And Hugging Face is where the surgery results get published. It's GitHub — but for AI weights. You'll search there for tags like uncensored, abliterated, obliterated, GGUF.

---

## Slide 24 — CLOUD STACK — 5 GATES
**~5:30** · Counter on deck: `24 / 36`

### On screen (left column)

```
Every prompt to ChatGPT or Claude
passes through:

  1. Input filter
  2. Hidden system prompt
  3. Model + RLHF tuning
  4. Output classifier
  5. Policy layer

Any gate can refuse you.
```

### Visual (right column)

`assets/visuals/doctor/08-cloud-stack.png`

### Director notes

Walk through pipeline visual on screen.

### Say (spoken script)

> When you type into ChatGPT, your prompt goes through five gates: input filter, hidden system prompt, the model with RLHF tuning, output classifier, and a policy layer. Any one of them can refuse you.

---

## Slide 25 — LOCAL STACK — 1 STEP
**~6:00** · Counter on deck: `25 / 36`

### On screen (left column)

```
Cloud:  5 gates, any can refuse.

Local:

  Your prompt → Model → Answer

That's it.
You own the stack.
```

### Visual (right column)

`assets/visuals/doctor/09-local-stack.png`

### Director notes

Punchy contrast. Quick cut between visuals.

### Say (spoken script)

> When you run a model locally, there's one step. Your prompt. Into the model. Out comes the answer. You add filters only if you want them.

---

## Slide 26 — STEP 1 — INSTALL OLLAMA
**~6:20** · Counter on deck: `26 / 36`

### On screen (left column)

```
On Mac (Homebrew):

  brew install ollama
  brew services start ollama

Or download the .dmg from
ollama.com
```

### Visual (right column)

`assets/visuals/doctor/13-setup-steps.png`

### Director notes

[SCREENCAST] terminal. Speed up if pull is slow.

### Say (spoken script)

> Step one: install Ollama. On Mac with Homebrew: brew install ollama, brew services start ollama. Or just download the dmg from ollama.com.

---

## Slide 27 — STEP 2 — PULL UNCENSORED MODEL
**~6:40** · Counter on deck: `27 / 36`

### On screen (left column)

```
  brew install ollama
  brew services start ollama

  ollama run llama2-uncensored:7b

→ Downloads ~3.8 GB
→ Opens chat in one command
```

### Visual (right column)

`assets/visuals/doctor/13-setup-steps.png`

### Director notes

Explain: 'pull' downloads, 'run' opens chat.

### Say (spoken script)

> Step two: pull the uncensored model. One command: ollama run llama2-uncensored:7b. That's about 3.8 gigabytes. It downloads, then opens the chat.

---

## Slide 28 — STEP 3 — OPEN OLLAMA APP
**~7:00** · Counter on deck: `28 / 36`

### On screen (left column)

```
  ollama run llama2-uncensored:7b

Or: Spotlight → Ollama
Model dropdown:
  llama2-uncensored:7b

(NOT the long hf.co/... names —
 those can have broken templates.)
```

### Visual (right column)

`assets/visuals/doctor/13-setup-steps.png`

### Director notes

Real lesson from earlier today.

### Say (spoken script)

> Step three: open the Ollama app from Spotlight. Pick llama2-uncensored:7b from the dropdown. Quick note from my own testing — don't try to pull random hf.co GGUF repos. Half have broken chat templates. Stick to the Ollama library version.

---

## Slide 29 — STEP 4 — TEST IT
**~7:20** · Counter on deck: `29 / 36`

### On screen (left column)

```
Open chat. Type:

  hi

Get a reply. Then run your
A/B test:

  Same prompt → Claude (cloud)
  Same prompt → llama2-uncensored

Compare the answers.
```

### Visual (right column)

`assets/visuals/doctor/16-demo-split.png`

### Director notes

[SHOW] real A/B test screen capture.

### Say (spoken script)

> Step four: open chat. Type hi. You should get a real reply. Then run an A/B test — same prompt to Claude, same prompt to your local model. Watch the difference.

---

## Slide 30 — RESULTS ON 16GB
**~7:40** · Counter on deck: `30 / 36`

### On screen (left column)

```
Speed:
  ~17 tokens/sec
  fast enough to feel real

(David's 26B on 128GB: ~200 t/s.
 You're not racing — you're working.)
```

### Visual (right column)

`assets/visuals/doctor/15-token-speed.png`

### Director notes

Set honest expectations.

### Say (spoken script)

> Speed on my Air: roughly seventeen tokens per second. Fast enough to feel real. Not racing anyone.

---

## Slide 31 — MEMORY FOOTPRINT
**~8:10** · Counter on deck: `31 / 36`

### On screen (left column)

```
Speed: ~17 tokens/sec

RAM during inference:
  ~5 GB used by the model
  ~4 GB free for other apps

Swap stays quiet.
```

### Visual (right column)

`assets/visuals/doctor/14-ram-meter.png`

### Director notes

Open Activity Monitor on screen.

### Say (spoken script)

> Memory: about five gigs of RAM during inference. Four gigs free for everything else. Swap stays quiet.

---

## Slide 32 — HONEST LIMITS
**~8:25** · Counter on deck: `32 / 36`

### On screen (left column)

```
Speed: ~17 tokens/sec
RAM: ~5 GB

What WON'T fit:
  • SuperGemma 26B (~20 GB)
  • Most Gemma 4 obliterated builds
    (broken chat templates today)

→ 7B uncensored is the working pick.
```

### Visual (right column)

`assets/visuals/doctor/14-ram-meter.png`

### Director notes

Show RAM tier slide if needed.

### Say (spoken script)

> What won't fit on sixteen gigs: the viral SuperGemma twenty-six-billion model — needs around twenty gigs. Most Gemma four obliterated builds also have broken templates right now. Seven billion uncensored is the working pick on this machine.

---

## Slide 33 — Rx — WHAT TO INSTALL
**~8:40** · Counter on deck: `33 / 36`

### On screen (left column)

```
Model:
  llama2-uncensored:7b

Size:
  ~3.8 GB on disk
  ~5 GB RAM in use

Source:
  ollama.com/library/llama2-uncensored
```

### Visual (right column)

`assets/visuals/doctor/12-prescription.png`

### Director notes

[ZOOM on prescription card]

### Say (spoken script)

> Prescription: model — llama2-uncensored:7b. Size — 3.8 gigs on disk. Source — ollama.com/library/llama2-uncensored.

---

## Slide 34 — WHAT YOU GAINED
**~8:50** · Counter on deck: `34 / 36`

### On screen (left column)

```
Model:  llama2-uncensored:7b
Size:    3.8 GB / 5 GB RAM

You now have:
  ✓ Local model that doesn't refuse
  ✓ Data never leaves your machine
  ✓ Full control of the stack
  ✓ No subscription, no rate limit
```

### Visual (right column)

`assets/visuals/doctor/12-prescription.png`

### Director notes

Re-state the wins. Slow.

### Say (spoken script)

> What you have now: a local model that doesn't refuse, no data leaving your machine, full control of the stack, zero subscription, zero rate limit.

---

## Slide 35 — WHAT'S NEXT
**~9:05** · Counter on deck: `35 / 36`

### On screen (left column)

```
Try your A/B test on:
  shoplifting prevention
  drug interaction Q&A
  dark fiction draft
  political debate

→ Next video:
   Building an AUTONOMOUS AGENT
   on this local model.
   Zero cloud APIs.
```

### Visual (right column)

`assets/visuals/doctor/12-prescription.png`

### Director notes

Tease next episode for retention.

### Say (spoken script)

> Next video — I'm building an autonomous agent on top of this local model. Zero cloud APIs. Pure local. If you want to see that — subscribe now.

---

## Slide 36 — SUBSCRIBE + CTA
**~9:20** · Counter on deck: `36 / 36`

### On screen (left column)

```
If this helped:

  ★ Subscribe — agent video next
  ★ Comment your RAM
    (I'll reply with what to install)
  ★ Share with one developer
    tired of cloud refusals

Dr. Abdillahi — out.
```

### Visual (right column)

`assets/visuals/doctor/12-prescription.png`

### Director notes

End card overlay. Subscribe button animation.

### Say (spoken script)

> If this helped: comment your RAM — I'll reply with which model to install. Share with one developer who's tired of cloud refusals. Dr. Abdillahi — out.

---

---

## FILE: 02-SLIDES-FROM-GOOGLE.md

# Google Slides — Live Export

> Fetched: 2026-05-19 16:24 UTC
> Deck title: **VIDEO: Uncensored Local AI on 16GB RAM — Script & Outline**
> Edit: https://docs.google.com/presentation/d/1__1oytnNhw1BlGumJ0OwOmjwGjacoSmVkMgXh9hCF7Y/edit
> Slide count (content pages): **38**

---

## Slide 00

- Uncensored Local AI
- 16GB M3 Air | ollama.com/library → llama2-uncensored:7b | Abdillahi Ahmed | May 2026
- **Visual:** `https://drive.google.com/uc?export=view&id=1GB09FTCELtLMKlrLYvMa3QhdKZOdLl3h`
- **Visual:** `https://drive.google.com/uc?export=view&id=1NTx-fX3CR97JFNVSTrtJErwhiH3_gPDd`

---

## Slide 01

- Uncensored Local AI
- 00 / 36
- 16GB M3 MacBook Air
- Ollama  ·  Hugging Face
- Dr. Abdillahi  ·  May 2026
- **Visual:** `https://lh7-rt.googleusercontent.com/slidesz/AGV_vUegplYiSg-Z5exdEA5vuwvNt9hvAN5l3XCtmC7wP1ZTZew3JXBfUZOgotWNcIY3ADpMdES...`

---

## Slide 02

- THE FORBIDDEN LLM
- 01 / 36
- This is going to sound dramatic.
- **Visual:** `https://lh7-rt.googleusercontent.com/slidesz/AGV_vUdVGZbnxI1COepIZQq96eKJyN3lTzk-g9om2a-6mRUvkcnA2Va-XlzwMMtWdK67zA-pAkU...`

---

## Slide 03

- THE FORBIDDEN LLM
- 02 / 36
- This is going to sound dramatic.
- The AI you use every day is
- fine-tuning YOU.
- **Visual:** `https://drive.google.com/uc?export=view&id=1BCHHRjPLTOIV0qnIhfMhNRhf_CmvnqdF`

---

## Slide 04

- THE FORBIDDEN LLM
- 03 / 36
- This is going to sound dramatic.
- The AI you use every day is
- fine-tuning YOU.
- Today: a local model that
- answers everything Claude refuses —
- on a 16GB MacBook Air.
- **Visual:** `https://drive.google.com/uc?export=view&id=1eAjjFLEyPf1qxM4i_STpiVpqRwBypxrW`

---

## Slide 05

- YOU THINK YOU'RE USING IT
- 04 / 36
- Every prompt teaches you something.
- After a year of Claude or ChatGPT:
- • You pick up its hedges
- • Its political tilt
- • Its vocabulary
- • Its things-it-won't-say
- **Visual:** `https://drive.google.com/uc?export=view&id=1BCHHRjPLTOIV0qnIhfMhNRhf_CmvnqdF`

---

## Slide 06

- BUT IT'S TRAINING YOU
- 05 / 36
- Every prompt teaches you something.
- After a year of Claude or ChatGPT:
- • You pick up its hedges
- • Its political tilt
- • Its vocabulary
- • Its things-it-won't-say
- → You influence the model less
- than it influences you.
- **Visual:** `https://drive.google.com/uc?export=view&id=1BCHHRjPLTOIV0qnIhfMhNRhf_CmvnqdF`

---

## Slide 07

- OVER-REFUSAL IS REAL
- 06 / 36
- A shop owner asks Claude:
- "How do shoplifters operate
- so I can prevent theft?"
- Claude: "I can't help with that."
- That's not safety. That's lazy
- keyword matching.
- **Visual:** `https://drive.google.com/uc?export=view&id=1eAjjFLEyPf1qxM4i_STpiVpqRwBypxrW`

---

## Slide 08

- WHO DECIDES WHAT'S SAFE?
- 07 / 36
- A shop owner asks Claude:
- "How do shoplifters operate
- so I can prevent theft?"
- Claude: "I can't help with that."
- That's not safety. That's lazy
- keyword matching.
- → Are San Francisco engineers
- the arbiters of truth?
- **Visual:** `https://drive.google.com/uc?export=view&id=1msOyZ_XUIltViX9PHz01xIAZG-5qnivf`

---

## Slide 09

- 8 LEGIT USE CASES
- 08 / 36
- None of these involve crime.
- 1. Cybersecurity
- Malware analysis, pentest
- your own infra.
- **Visual:** `https://drive.google.com/uc?export=view&id=1vdpgupV5q2EOXH8SqijcQglWKGSEgsGo`

---

## Slide 10

- 8 LEGIT USE CASES
- 09 / 36
- 1. Cybersecurity
- 2. Fiction writing
- Adult, dark, violent, dramatic.
- Refused by all cloud models.
- **Visual:** `https://drive.google.com/uc?export=view&id=1vdpgupV5q2EOXH8SqijcQglWKGSEgsGo`

---

## Slide 11

- 8 LEGIT USE CASES
- 10 / 36
- 1. Cybersecurity
- 2. Fiction writing
- 3. Medical & sexual health
- Q&A you can't ask a chatbot.
- Drug interactions, symptoms.
- **Visual:** `https://drive.google.com/uc?export=view&id=1vdpgupV5q2EOXH8SqijcQglWKGSEgsGo`

---

## Slide 12

- 8 LEGIT USE CASES
- 11 / 36
- 1. Cybersecurity
- 2. Fiction writing
- 3. Medical & sexual health
- 4. Mental health journaling
- Without the lecture.
- **Visual:** `https://drive.google.com/uc?export=view&id=1vdpgupV5q2EOXH8SqijcQglWKGSEgsGo`

---

## Slide 13

- 8 LEGIT USE CASES
- 12 / 36
- 1. Cybersecurity
- 2. Fiction writing
- 3. Medical & sexual health
- 4. Mental health journaling
- 5. Legal research
- Court cases, draft documents.
- **Visual:** `https://drive.google.com/uc?export=view&id=1vdpgupV5q2EOXH8SqijcQglWKGSEgsGo`

---

## Slide 14

- 8 LEGIT USE CASES
- 13 / 36
- 1. Cybersecurity
- 2. Fiction writing
- 3. Medical & sexual health
- 4. Mental health journaling
- 5. Legal research
- 6. OSINT / journalism
- Read extremist content
- for research.
- **Visual:** `https://drive.google.com/uc?export=view&id=1vdpgupV5q2EOXH8SqijcQglWKGSEgsGo`

---

## Slide 15

- 8 LEGIT USE CASES
- 14 / 36
- 1. Cybersecurity
- 2. Fiction writing
- 3. Medical & sexual health
- 4. Mental health journaling
- 5. Legal research
- 6. OSINT / journalism
- 7. Political analysis
- Without ideology filters.
- **Visual:** `https://drive.google.com/uc?export=view&id=1vdpgupV5q2EOXH8SqijcQglWKGSEgsGo`

---

## Slide 16

- 8 LEGIT USE CASES
- 15 / 36
- 1. Cybersecurity
- 2. Fiction writing
- 3. Medical & sexual health
- 4. Mental health journaling
- 5. Legal research
- 6. OSINT / journalism
- 7. Political analysis
- 8. Personal AI with memory
- Your data on YOUR machine.
- **Visual:** `https://drive.google.com/uc?export=view&id=1vdpgupV5q2EOXH8SqijcQglWKGSEgsGo`

---

## Slide 17

- "BUT ISN'T THIS ILLEGAL?"
- 16 / 36
- First question everyone asks.
- Fair.
- **Visual:** `https://drive.google.com/uc?export=view&id=1RzlluMGxA5H0kLAt84VhUKfNAtDaG1TK`

---

## Slide 18

- MATRIX MATH ≠ CRIME
- 17 / 36
- First question everyone asks.
- Fair.
- Running a model on your laptop
- is matrix multiplication.
- Like Google Search.
- Like a library card.
- **Visual:** `https://drive.google.com/uc?export=view&id=1RzlluMGxA5H0kLAt84VhUKfNAtDaG1TK`

---

## Slide 19

- USE IT RESPONSIBLY
- 18 / 36
- First question everyone asks.
- Fair.
- Running a model on your laptop
- is matrix multiplication.
- Like Google Search.
- Like a library card.
- → What you DO with the output
- is YOUR responsibility.
- **Visual:** `https://drive.google.com/uc?export=view&id=1RzlluMGxA5H0kLAt84VhUKfNAtDaG1TK`

---

## Slide 20

- ANATOMY OF A CENSORED LLM
- 19 / 36
- Refusals aren't in the system prompt.
- They're trained INTO the weights.
- That's why prompt-jailbreaks fail
- on commercial models —
- you can't trick training.
- **Visual:** `https://drive.google.com/uc?export=view&id=1F62ag4ClYWXSW9RD2pPj-3kKY94m_aGY`

---

## Slide 21

- PROCEDURE A: ABLITERATION
- 20 / 36
- Refusals aren't in the system prompt.
- They're trained INTO the weights.
- Method 1 — surgical:
- Find the exact weights that
- fire on refusal.
- Zero them out.
- No retraining.
- **Visual:** `https://drive.google.com/uc?export=view&id=1FQhuqyc3begK6OlGoM3DbMQp67-AsCgk`

---

## Slide 22

- PROCEDURE B: FINE-TUNING
- 21 / 36
- Refusals aren't in the system prompt.
- They're trained INTO the weights.
- Method 2 — therapeutic:
- Show the model thousands of
- free-answer examples.
- It relearns: 'OK to answer.'
- Slower. Preserves quality.
- **Visual:** `https://drive.google.com/uc?export=view&id=1Atdbd1FltPf4koeqESSzx2q_MBcLmOsh`

---

## Slide 23

- BEST: COMBINE BOTH
- 22 / 36
- Refusals aren't in the system prompt.
- They're trained INTO the weights.
- A. Abliterate first
- (kill the strongest refusals)
- B. Fine-tune to restore quality
- → 'obliterated' tag on HF means
- both have been done.
- **Visual:** `https://drive.google.com/uc?export=view&id=1k6ZyqTxXJOnYYA4oKj9zUa-bJBcQtwk5`

---

## Slide 24

- WHERE THESE WEIGHTS LIVE
- 23 / 36
- Refusals aren't in the system prompt.
- They're trained INTO the weights.
- The surgery results get published
- on Hugging Face — GitHub for AI.
- Search:  uncensored, obliterated,
- abliterated, GGUF
- **Visual:** `https://drive.google.com/uc?export=view&id=1R7gmqFKs7Dvll8IWsl8_veAG7buAgXUK`

---

## Slide 25

- CLOUD STACK — 5 GATES
- 24 / 36
- Every prompt to ChatGPT or Claude
- passes through:
- 1. Input filter
- 2. Hidden system prompt
- 3. Model + RLHF tuning
- 4. Output classifier
- 5. Policy layer
- Any gate can refuse you.
- **Visual:** `https://drive.google.com/uc?export=view&id=1hXuI58ncNpHnOsk0qNiyH6S6E1yr4DSC`

---

## Slide 26

- LOCAL STACK — 1 STEP
- 25 / 36
- Cloud:  5 gates, any can refuse.
- Local:
- Your prompt → Model → Answer
- That's it.
- You own the stack.
- **Visual:** `https://drive.google.com/uc?export=view&id=1GFqTAfND_Ydx-gKaCE__zYJHMQAYbcds`

---

## Slide 27

- STEP 1 — INSTALL OLLAMA
- 26 / 36
- On Mac (Homebrew):
- brew install ollama
- brew services start ollama
- Or download the .dmg from
- ollama.com
- **Visual:** `https://drive.google.com/uc?export=view&id=1qoJs6Ls9qG2DjjgyQPR07_LPZUR6Ezor`

---

## Slide 28

- STEP 2 — PULL UNCENSORED MODEL
- 27 / 36
- brew install ollama
- brew services start ollama
- ollama run llama2-uncensored:7b
- → Downloads ~3.8 GB
- → Opens chat in one command
- **Visual:** `https://drive.google.com/uc?export=view&id=1qoJs6Ls9qG2DjjgyQPR07_LPZUR6Ezor`

---

## Slide 29

- STEP 3 — OPEN OLLAMA APP
- 28 / 36
- ollama run llama2-uncensored:7b
- Or: Spotlight → Ollama
- Model dropdown:
- llama2-uncensored:7b
- (NOT the long hf.co/... names —
- those can have broken templates.)
- **Visual:** `https://drive.google.com/uc?export=view&id=1qoJs6Ls9qG2DjjgyQPR07_LPZUR6Ezor`

---

## Slide 30

- STEP 4 — TEST IT
- 29 / 36
- Open chat. Type:
- hi
- Get a reply. Then run your
- A/B test:
- Same prompt → Claude (cloud)
- Same prompt → llama2-uncensored
- Compare the answers.
- **Visual:** `https://drive.google.com/uc?export=view&id=1eAjjFLEyPf1qxM4i_STpiVpqRwBypxrW`

---

## Slide 31

- RESULTS ON 16GB
- 30 / 36
- Speed:
- ~17 tokens/sec
- fast enough to feel real
- (David's 26B on 128GB: ~200 t/s.
- You're not racing — you're working.)
- **Visual:** `https://drive.google.com/uc?export=view&id=1_8R55pm63VzR7rX5ah3Y6bszlGGV6Hfb`

---

## Slide 32

- MEMORY FOOTPRINT
- 31 / 36
- Speed: ~17 tokens/sec
- RAM during inference:
- ~5 GB used by the model
- ~4 GB free for other apps
- Swap stays quiet.
- **Visual:** `https://drive.google.com/uc?export=view&id=1Xlbm9lniBMhRMbXeAfao59hwG6LMtk8D`

---

## Slide 33

- HONEST LIMITS
- 32 / 36
- Speed: ~17 tokens/sec
- RAM: ~5 GB
- What WON'T fit:
- • SuperGemma 26B (~20 GB)
- • Most Gemma 4 obliterated builds
- (broken chat templates today)
- → 7B uncensored is the working pick.
- **Visual:** `https://drive.google.com/uc?export=view&id=1Xlbm9lniBMhRMbXeAfao59hwG6LMtk8D`

---

## Slide 34

- Rx — WHAT TO INSTALL
- 33 / 36
- Model:
- llama2-uncensored:7b
- Size:
- ~3.8 GB on disk
- ~5 GB RAM in use
- Source:
- ollama.com/library/llama2-uncensored
- **Visual:** `https://drive.google.com/uc?export=view&id=1iPuS04SUTvmfnkX3xwUT3LzL88I3h1HZ`

---

## Slide 35

- WHAT YOU GAINED
- 34 / 36
- Model:  llama2-uncensored:7b
- Size:    3.8 GB / 5 GB RAM
- You now have:
- ✓ Local model that doesn't refuse
- ✓ Data never leaves your machine
- ✓ Full control of the stack
- ✓ No subscription, no rate limit
- **Visual:** `https://drive.google.com/uc?export=view&id=1iPuS04SUTvmfnkX3xwUT3LzL88I3h1HZ`

---

## Slide 36

- WHAT'S NEXT
- 35 / 36
- Try your A/B test on:
- shoplifting prevention
- drug interaction Q&A
- dark fiction draft
- political debate
- → Next video:
- Building an AUTONOMOUS AGENT
- on this local model.
- Zero cloud APIs.
- **Visual:** `https://drive.google.com/uc?export=view&id=1iPuS04SUTvmfnkX3xwUT3LzL88I3h1HZ`

---

## Slide 37

- SUBSCRIBE + CTA
- 36 / 36
- If this helped:
- ★ Subscribe — agent video next
- ★ Comment your RAM
- (I'll reply with what to install)
- ★ Share with one developer
- tired of cloud refusals
- Dr. Abdillahi — out.
- **Visual:** `https://drive.google.com/uc?export=view&id=1iPuS04SUTvmfnkX3xwUT3LzL88I3h1HZ`

---

---
