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
