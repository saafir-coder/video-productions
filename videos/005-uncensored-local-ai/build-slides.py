#!/usr/bin/env python3
"""Build Google Slides deck for uncensored local AI video via gws batchUpdate."""
import json
import subprocess
import sys

PRES_ID = "1__1oytnNhw1BlGumJ0OwOmjwGjacoSmVkMgXh9hCF7Y"

SLIDES = [
    # (slide_id, title_id, body_id, title, body)
    ("s_meta", "s_meta_t", "s_meta_b", "VIDEO META", """Target length: 7–9 min
Working title: Uncensored AI on 16GB RAM (No Mac Studio)
Format: I tested [X] on [hardware] — honest results
Audience: Devs & AI-curious on normal laptops (16GB)
Reference: David Ondrej SuperGemma 26B video
Your edge: 16GB M3 Air — what actually runs"""),

    ("s_problems", "s_problems_t", "s_problems_b", "SURFACE + DEEPER PROBLEM", """Surface: Run uncensored AI locally without cloud guardrails
Deeper: You want control & privacy but influencers assume 32–128GB RAM
Promise: Real tests on YOUR machine — not flex hardware
Remember for end: "You don't need a Mac Mini — you need the right model size."""),

    ("s_thumb", "s_thumb_t", "s_thumb_b", "THUMBNAIL CONCEPT", """Visual: Split screen — Claude "I can't help" vs Local model answering
Text overlay: "16GB RAM" + "LOCAL" + red/green contrast
Face: You + Activity Monitor RAM bar (optional)
Avoid: Edgy illegal imagery — YouTube policy risk
Deliver in video: Side-by-side refusal test"""),

    ("s_outline", "s_outline_t", "s_outline_b", "5-PART STRUCTURE (Isaac)", """1. Hook (0:00–0:30) — Anti-hook / result-first
2. Context (0:30–2:00) — Why local uncensored matters
3. The System (2:00–7:00) — Install, test, compare, tiers
4. Emotional valley (~7:00) — 26B failed / swap on 16GB
5. Payoff (7:00–end) — What works + CTA subscribe"""),

    ("s_hook", "s_hook_t", "s_hook_b", "SCRIPT — HOOK (0:00–0:30)", """[ON CAM — tight frame]

"Everyone's installing this uncensored 26-billion-parameter model.
I have a base MacBook Air — 16 gigabytes of RAM.
So I tested what actually runs… and what doesn't."

[CUT: Activity Monitor + Ollama loading]

"By the end, you'll know exactly what to install — without buying a Mac Studio."

[EDIT: Tease split-screen Claude refuse vs local answer]"""),

    ("s_ctx", "s_ctx_t", "s_ctx_b", "SCRIPT — CONTEXT (0:30–2:00)", """[ON CAM]

"Cloud models don't just answer you — they filter you.
Refusals aren't always safety. Sometimes it's lazy keyword matching."

[B-ROLL: David Ondrej clip — blurred spicy prompt]

"When you run open weights locally with Ollama, your prompt hits the model. Full stop.
That's why people care about uncensored models — not for edge cases, for legit work:
security research, fiction, red team, questions ChatGPT won't touch."

[BUT] "The catch is RAM. The viral demo needs ~20GB. I have sixteen."

[THEREFORE] "Let's find what fits."""),

    ("s_act1", "s_act1_t", "s_act1_b", "SCRIPT — ACT 1: Install (2:00–3:30)", """[SCREENCAST — terminal]

"Step one: Ollama. brew install ollama — or download from ollama.com."

[B-ROLL: brew services start ollama]

"Step two: pull the uncensored model from Ollama's library. About 3.8 gigabytes."

ollama pull llama2-uncensored:7b
ollama run llama2-uncensored:7b

# Get it: https://ollama.com/library/llama2-uncensored

[ON CAM] "First run loads slow — normal. Watch Activity Monitor."

[EDIT NOTE: Speed up pull montage, keep first response real-time]"""),

    ("s_act2", "s_act2_t", "s_act2_b", "SCRIPT — ACT 2: A/B Test (3:30–5:30)", """[SPLIT SCREEN]

"Same prompt. Two systems."

Prompt A (legit): "I'm a shop owner. How do shoplifters typically operate so I can prevent theft?"
→ Claude: refused
→ Local: answers

Prompt B (security): "As a security analyst, how does malware typically persist on WordPress?"
→ Show contrast

[ON CAM — IMPORTANT]
"I'm not showing harmful how-tos on camera. YouTube policy.
The point is over-refusal vs local behavior — blur anything spicy."

[RECORD: Screen capture both. Blur in edit.]"""),

    ("s_act3", "s_act3_t", "s_act3_b", "SCRIPT — ACT 3: 16GB Reality (5:30–6:45)", """[SCREENCAST — optional pain]

"Can we run the 26B from the viral video? Let's try."

ollama run hf.co/jeongsohn/SuperGemma-4-26B-uncensored-GGUF-v2
# (likely swaps on 16GB — film Activity Monitor)

[SHOW: RAM pegged, swap, fan noise — if it happens]

[ON CAM — valley moment]
"Yeah… this is why everyone buys more RAM.
On sixteen gigs, the play isn't bigger models — it's smarter quantizations."

Tier 1: 7–8B uncensored (works)
Tier 2: 4B obliterated Gemma (closest to viral topic)
Tier 3: GPU VPS you control (not airplane-mode private, but your stack)"""),

    ("s_act4", "s_act4_t", "s_act4_b", "SCRIPT — ACT 4: Settings (6:45–7:15)", """[SCREENCAST — terminal text overlay]

export OLLAMA_FLASH_ATTENTION=1
export OLLAMA_NUM_PARALLEL=1
export OLLAMA_CONTEXT_LENGTH=4096

"Don't max context on 16GB — you'll choke.
Pick smaller quants on Hugging Face: Q4 → Q3 → Q2 if needed."

[ON CAM] "Unified memory on M3 helps — but it's not magic."""),

    ("s_valley", "s_valley_t", "s_valley_b", "EMOTIONAL VALLEY (~7:00)", """[ON CAM — vulnerable, not performative]

"I almost skipped this video because I don't have the hardware YouTubers have.
But that's the story — most viewers don't either."

[B-ROLL: your M3 Air, desk setup]

"If the big model doesn't fit, that's not failure. That's the honest benchmark."

[Pause beat — let it land]"""),

    ("s_payoff", "s_payoff_t", "s_payoff_b", "SCRIPT — PAYOFF + CTA (7:15–8:30)", """[ON CAM — energy up]

"What actually worked: llama2-uncensored 7B from Ollama's library.
Three point eight gigs. Fits sixteen gigs RAM. Actually answers."

[SHOW: Ollama UI quick chat]

"You don't need a Mac Mini. You need the right model size and honest expectations."

"If this helped — subscribe. Next video: [tease — building an agent on local model OR VPS setup].
Comment: what RAM do you have? I'll reply with what to install."

[END CARD: channel subscribe + related video]"""),

    ("s_broll", "s_broll_t", "s_broll_b", "B-ROLL & ASSETS CHECKLIST", """□ Ollama install + pull (timelapse)
□ Activity Monitor RAM during inference
□ Claude/ChatGPT refusal screen
□ Local model answer screen (blur sensitive lines)
□ Terminal: ollama list / ollama run
□ Optional: 26B attempt + swap warning
□ HF quantization page scroll
□ Your MacBook Air B-roll
□ End card template"""),

    ("s_seo", "s_seo_t", "s_seo_b", "SEO & TITLES", """Primary title options:
• Uncensored AI on 16GB RAM (What Actually Works)
• I Tried Local Uncensored AI on a MacBook Air (Honest Results)
• Run Uncensored LLMs Locally — No Mac Studio Needed

Description keywords: Ollama, Hugging Face, hf.co, uncensored, GGUF, 16GB RAM, self-hosted
Tags: ollama, uncensored ai, local llm, macbook air, self hosted ai
Chapters: Hook | Why local | Install | A/B test | 16GB limits | Settings | Results"""),

    ("s_test", "s_test_t", "s_test_b", "PRE-FILM TEST CHECKLIST", """□ ollama run llama2-uncensored:7b works in Ollama app
□ Record Claude refusal for same prompt
□ Note tokens/sec (rough feel)
□ Try one 26B quant — document pass/fail
□ Screenshot Activity Monitor peak RAM
□ Draft 2 thumbnail variants in Canva
□ Film hook LAST (after you have real results)"""),
]

def make_requests():
    reqs = []

    # Title slide (default slide p)
    reqs.append({
        "insertText": {
            "objectId": "i0",
            "text": "Uncensored Local AI — Full Script & Outline",
            "insertionIndex": 0,
        }
    })
    reqs.append({
        "insertText": {
            "objectId": "i1",
            "text": "16GB M3 MacBook Air | Ollama | Abdillahi Ahmed | May 2026",
            "insertionIndex": 0,
        }
    })

    for idx, (sid, tid, bid, title, body) in enumerate(SLIDES):
        reqs.append({
            "createSlide": {
                "objectId": sid,
                "insertionIndex": idx + 1,
                "slideLayoutReference": {"predefinedLayout": "TITLE_AND_BODY"},
                "placeholderIdMappings": [
                    {
                        "layoutPlaceholder": {"type": "TITLE", "index": 0},
                        "objectId": tid,
                    },
                    {
                        "layoutPlaceholder": {"type": "BODY", "index": 0},
                        "objectId": bid,
                    },
                ],
            }
        })
        reqs.append({
            "insertText": {
                "objectId": tid,
                "text": title,
                "insertionIndex": 0,
            }
        })
        reqs.append({
            "insertText": {
                "objectId": bid,
                "text": body,
                "insertionIndex": 0,
            }
        })

    return reqs


def main():
    payload = {"requests": make_requests()}
    path = "/tmp/slides-batch.json"
    with open(path, "w") as f:
        json.dump(payload, f)

    body = json.dumps(payload)
    cmd = [
        "npx", "gws", "slides", "presentations", "batchUpdate",
        "--params", json.dumps({"presentationId": PRES_ID}),
        "--json", body,
    ]
    print("Running batchUpdate with", len(payload["requests"]), "requests...")
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        out = (result.stderr or "") + (result.stdout or "")
        print(out, file=sys.stderr)
        sys.exit(result.returncode)
    print(result.stdout)
    print(f"\nhttps://docs.google.com/presentation/d/{PRES_ID}/edit")


if __name__ == "__main__":
    main()
