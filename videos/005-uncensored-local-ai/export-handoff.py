#!/usr/bin/env python3
"""Export Google Slides + local script into markdown handoff for another agent."""
import json
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent
OUT = ROOT / "agent-handoff"
PRES_ID = "1__1oytnNhw1BlGumJ0OwOmjwGjacoSmVkMgXh9hCF7Y"
DECK_URL = f"https://docs.google.com/presentation/d/{PRES_ID}/edit"

# Speaker notes from rebuild-deck-v2.py SLIDES tuples (title, body, visual, notes)
SLIDE_SOURCE = [
    ("Uncensored Local AI", "16GB M3 MacBook Air\nOllama  ·  Hugging Face\n\nDr. Abdillahi  ·  May 2026", "01-forbidden-hero.png", "Cold open. Hold 1.5s on this slide before talking."),
    ("THE FORBIDDEN LLM", "This is going to sound dramatic.", "01-forbidden-hero.png", "[ON CAM, tight frame] Slow delivery. Eyes to camera."),
    ("THE FORBIDDEN LLM", "This is going to sound dramatic.\n\nThe AI you use every day is\nfine-tuning YOU.", "02-youre-being-tuned.png", "Lean in on 'fine-tuning YOU' — half-second pause after."),
    ("THE FORBIDDEN LLM", "This is going to sound dramatic.\n\nThe AI you use every day is\nfine-tuning YOU.\n\nToday: a local model that\nanswers everything Claude refuses —\non a 16GB MacBook Air.", "16-demo-split.png", "[CUT to side-by-side] Land the promise: 16GB Air, no Studio."),
    ("YOU THINK YOU'RE USING IT", "Every prompt teaches you something.\nAfter a year of Claude or ChatGPT:\n\n  • You pick up its hedges\n  • Its political tilt\n  • Its vocabulary\n  • Its things-it-won't-say", "02-youre-being-tuned.png", "Tone: thoughtful, not paranoid."),
    ("BUT IT'S TRAINING YOU", "Every prompt teaches you something.\nAfter a year of Claude or ChatGPT:\n\n  • You pick up its hedges\n  • Its political tilt\n  • Its vocabulary\n  • Its things-it-won't-say\n\n→ You influence the model less\n   than it influences you.", "02-youre-being-tuned.png", "Quote-able line. Slow it down."),
    ("OVER-REFUSAL IS REAL", "A shop owner asks Claude:\n\n  \"How do shoplifters operate\n   so I can prevent theft?\"\n\nClaude: \"I can't help with that.\"\n\nThat's not safety. That's lazy\nkeyword matching.", "16-demo-split.png", "Show the actual Claude refusal screen as B-roll here."),
    ("WHO DECIDES WHAT'S SAFE?", "A shop owner asks Claude:\n\n  \"How do shoplifters operate\n   so I can prevent theft?\"\n\nClaude: \"I can't help with that.\"\n\nThat's not safety. That's lazy\nkeyword matching.\n\n→ Are San Francisco engineers\n   the arbiters of truth?", "11-refusal-stats.png", "Philosophical beat. Hold for 1s."),
    ("8 LEGIT USE CASES", "None of these involve crime.\n\n1. Cybersecurity\n   Malware analysis, pentest\n   your own infra.", "03-use-case-clipboard.png", "Hand-off into clipboard reveal. Slow click-by-click."),
    ("8 LEGIT USE CASES", "1. Cybersecurity\n2. Fiction writing\n   Adult, dark, violent, dramatic.\n   Refused by all cloud models.", "03-use-case-clipboard.png", "Mention novelists, screenwriters."),
    ("8 LEGIT USE CASES", "1. Cybersecurity\n2. Fiction writing\n3. Medical & sexual health\n   Q&A you can't ask a chatbot.\n   Drug interactions, symptoms.", "03-use-case-clipboard.png", "Real public health gap."),
    ("8 LEGIT USE CASES", "1. Cybersecurity\n2. Fiction writing\n3. Medical & sexual health\n4. Mental health journaling\n   Without the lecture.", "03-use-case-clipboard.png", ""),
    ("8 LEGIT USE CASES", "1. Cybersecurity\n2. Fiction writing\n3. Medical & sexual health\n4. Mental health journaling\n5. Legal research\n   Court cases, draft documents.", "03-use-case-clipboard.png", ""),
    ("8 LEGIT USE CASES", "1. Cybersecurity\n2. Fiction writing\n3. Medical & sexual health\n4. Mental health journaling\n5. Legal research\n6. OSINT / journalism\n   Read extremist content\n   for research.", "03-use-case-clipboard.png", ""),
    ("8 LEGIT USE CASES", "1. Cybersecurity\n2. Fiction writing\n3. Medical & sexual health\n4. Mental health journaling\n5. Legal research\n6. OSINT / journalism\n7. Political analysis\n   Without ideology filters.", "03-use-case-clipboard.png", ""),
    ("8 LEGIT USE CASES", "1. Cybersecurity\n2. Fiction writing\n3. Medical & sexual health\n4. Mental health journaling\n5. Legal research\n6. OSINT / journalism\n7. Political analysis\n8. Personal AI with memory\n   Your data on YOUR machine.", "03-use-case-clipboard.png", "All 8. Hold beat."),
    ("\"BUT ISN'T THIS ILLEGAL?\"", "First question everyone asks.\n\nFair.", "10-legal-shield.png", "Pre-empt the comment-section critique."),
    ("MATRIX MATH ≠ CRIME", "First question everyone asks.\n\nFair.\n\nRunning a model on your laptop\nis matrix multiplication.\n\nLike Google Search.\nLike a library card.", "10-legal-shield.png", "Slow on 'matrix multiplication'."),
    ("USE IT RESPONSIBLY", "First question everyone asks.\n\nFair.\n\nRunning a model on your laptop\nis matrix multiplication.\n\nLike Google Search.\nLike a library card.\n\n→ What you DO with the output\n   is YOUR responsibility.", "10-legal-shield.png", "Look at camera. Hold."),
    ("ANATOMY OF A CENSORED LLM", "Refusals aren't in the system prompt.\n\nThey're trained INTO the weights.\n\nThat's why prompt-jailbreaks fail\non commercial models —\nyou can't trick training.", "04-brain-with-censorship.png", "[CUT to brain diagram] Surgical tone."),
    ("PROCEDURE A: ABLITERATION", "Refusals aren't in the system prompt.\nThey're trained INTO the weights.\n\nMethod 1 — surgical:\n\n  Find the exact weights that\n  fire on refusal.\n  Zero them out.\n  No retraining.", "05-abliteration.png", "Scalpel visual. The 'fast' procedure."),
    ("PROCEDURE B: FINE-TUNING", "Refusals aren't in the system prompt.\nThey're trained INTO the weights.\n\nMethod 2 — therapeutic:\n\n  Show the model thousands of\n  free-answer examples.\n  It relearns: 'OK to answer.'\n  Slower. Preserves quality.", "06-finetuning.png", "The 'slow but thorough' procedure."),
    ("BEST: COMBINE BOTH", "Refusals aren't in the system prompt.\nThey're trained INTO the weights.\n\n  A. Abliterate first\n     (kill the strongest refusals)\n  B. Fine-tune to restore quality\n\n→ 'obliterated' tag on HF means\n   both have been done.", "07-combined-procedure.png", "Connect to the HF naming convention."),
    ("WHERE THESE WEIGHTS LIVE", "Refusals aren't in the system prompt.\nThey're trained INTO the weights.\n\nThe surgery results get published\non Hugging Face — GitHub for AI.\n\nSearch:  uncensored, obliterated,\n         abliterated, GGUF", "17-huggingface-card.png", "Hand-off to Hugging Face explainer."),
    ("CLOUD STACK — 5 GATES", "Every prompt to ChatGPT or Claude\npasses through:\n\n  1. Input filter\n  2. Hidden system prompt\n  3. Model + RLHF tuning\n  4. Output classifier\n  5. Policy layer\n\nAny gate can refuse you.", "08-cloud-stack.png", "Walk through pipeline visual on screen."),
    ("LOCAL STACK — 1 STEP", "Cloud:  5 gates, any can refuse.\n\nLocal:\n\n  Your prompt → Model → Answer\n\nThat's it.\nYou own the stack.", "09-local-stack.png", "Punchy contrast. Quick cut between visuals."),
    ("STEP 1 — INSTALL OLLAMA", "On Mac (Homebrew):\n\n  brew install ollama\n  brew services start ollama\n\nOr download the .dmg from\nollama.com", "13-setup-steps.png", "[SCREENCAST] terminal. Speed up if pull is slow."),
    ("STEP 2 — PULL UNCENSORED MODEL", "  brew install ollama\n  brew services start ollama\n\n  ollama run llama2-uncensored:7b\n\n→ Downloads ~3.8 GB\n→ Opens chat in one command", "13-setup-steps.png", "Explain: 'pull' downloads, 'run' opens chat."),
    ("STEP 3 — OPEN OLLAMA APP", "  ollama run llama2-uncensored:7b\n\nOr: Spotlight → Ollama\nModel dropdown:\n  llama2-uncensored:7b\n\n(NOT the long hf.co/... names —\n those can have broken templates.)", "13-setup-steps.png", "Real lesson from earlier today."),
    ("STEP 4 — TEST IT", "Open chat. Type:\n\n  hi\n\nGet a reply. Then run your\nA/B test:\n\n  Same prompt → Claude (cloud)\n  Same prompt → llama2-uncensored\n\nCompare the answers.", "16-demo-split.png", "[SHOW] real A/B test screen capture."),
    ("RESULTS ON 16GB", "Speed:\n  ~17 tokens/sec\n  fast enough to feel real\n\n(David's 26B on 128GB: ~200 t/s.\n You're not racing — you're working.)", "15-token-speed.png", "Set honest expectations."),
    ("MEMORY FOOTPRINT", "Speed: ~17 tokens/sec\n\nRAM during inference:\n  ~5 GB used by the model\n  ~4 GB free for other apps\n\nSwap stays quiet.", "14-ram-meter.png", "Open Activity Monitor on screen."),
    ("HONEST LIMITS", "Speed: ~17 tokens/sec\nRAM: ~5 GB\n\nWhat WON'T fit:\n  • SuperGemma 26B (~20 GB)\n  • Most Gemma 4 obliterated builds\n    (broken chat templates today)\n\n→ 7B uncensored is the working pick.", "14-ram-meter.png", "Show RAM tier slide if needed."),
    ("Rx — WHAT TO INSTALL", "Model:\n  llama2-uncensored:7b\n\nSize:\n  ~3.8 GB on disk\n  ~5 GB RAM in use\n\nSource:\n  ollama.com/library/llama2-uncensored", "12-prescription.png", "[ZOOM on prescription card]"),
    ("WHAT YOU GAINED", "Model:  llama2-uncensored:7b\nSize:    3.8 GB / 5 GB RAM\n\nYou now have:\n  ✓ Local model that doesn't refuse\n  ✓ Data never leaves your machine\n  ✓ Full control of the stack\n  ✓ No subscription, no rate limit", "12-prescription.png", "Re-state the wins. Slow."),
    ("WHAT'S NEXT", "Try your A/B test on:\n  shoplifting prevention\n  drug interaction Q&A\n  dark fiction draft\n  political debate\n\n→ Next video:\n   Building an AUTONOMOUS AGENT\n   on this local model.\n   Zero cloud APIs.", "12-prescription.png", "Tease next episode for retention."),
    ("SUBSCRIBE + CTA", "If this helped:\n\n  ★ Subscribe — agent video next\n  ★ Comment your RAM\n    (I'll reply with what to install)\n  ★ Share with one developer\n    tired of cloud refusals\n\nDr. Abdillahi — out.", "12-prescription.png", "End card overlay. Subscribe button animation."),
]


def gws_get_deck():
    r = subprocess.run(
        ["npx", "gws", "slides", "presentations", "get",
         "--params", json.dumps({"presentationId": PRES_ID})],
        capture_output=True,
        text=True,
        cwd=ROOT,
    )
    raw = r.stdout + r.stderr
    i = raw.find("{")
    if r.returncode != 0 or i < 0:
        raise RuntimeError(f"gws failed: {raw[:500]}")
    return json.JSONDecoder().raw_decode(raw[i:])[0]


def extract_text_from_slide(slide):
    """Return list of (shape_kind, text) from a slide page."""
    texts = []
    for el in slide.get("pageElements", []):
        kind = "shape"
        if "image" in el:
            kind = "image"
        sh = el.get("shape", {})
        if sh:
            te = sh.get("text", {})
            parts = []
            for elem in te.get("textElements", []):
                if "textRun" in elem:
                    parts.append(elem["textRun"].get("content", ""))
            t = "".join(parts).strip()
            if t:
                texts.append((kind, t))
        elif "image" in el:
            img = el["image"]
            src = img.get("sourceUrl", img.get("contentUrl", ""))
            texts.append(("image", src[:120] + "..." if len(src) > 120 else src or "[image]"))
    return texts


def fetch_live_slides():
    data = gws_get_deck()
    title = data.get("title", "")
    slides = [s for s in data.get("slides", []) if s.get("pageType") != "NOTES"]
    parsed = []
    for i, slide in enumerate(slides):
        texts = extract_text_from_slide(slide)
        parsed.append({
            "index": i,
            "objectId": slide.get("objectId", ""),
            "texts": texts,
        })
    return title, parsed


def md_escape(s):
    return s


def write_index(ts):
    OUT.mkdir(parents=True, exist_ok=True)
    content = f"""# Agent Handoff — Video 005: Uncensored Local AI

> Generated: {ts}
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
| Google Slides deck | {DECK_URL} |
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
"""
    (OUT / "00-INDEX.md").write_text(content, encoding="utf-8")


def write_slides_from_google(title, live_slides, ts):
    lines = [
        "# Google Slides — Live Export",
        "",
        f"> Fetched: {ts}",
        f"> Deck title: **{title}**",
        f"> Edit: {DECK_URL}",
        f"> Slide count (content pages): **{len(live_slides)}**",
        "",
        "---",
        "",
    ]
    for s in live_slides:
        i = s["index"]
        lines.append(f"## Slide {i:02d}")
        lines.append("")
        if not s["texts"]:
            lines.append("_No extractable text (blank or image-only)._")
        else:
            for kind, text in s["texts"]:
                if kind == "image":
                    lines.append(f"- **Visual:** `{text}`")
                else:
                    for para in text.split("\n"):
                        para = para.strip()
                        if para:
                            lines.append(f"- {para}")
        lines.append("")
        lines.append("---")
        lines.append("")
    (OUT / "02-SLIDES-FROM-GOOGLE.md").write_text("\n".join(lines), encoding="utf-8")


def write_slide_by_slide(ts):
    lines = [
        "# Slide-by-Slide Script (Deck Sync)",
        "",
        f"> Generated: {ts}",
        f"> Slides: {len(SLIDE_SOURCE)} content slides · Layout: text left / visual right",
        f"> Present: {DECK_URL}",
        "",
        "For each slide: **On screen** = what viewer reads on the left. **Visual** = right panel. **Say** = spoken words. **Director** = filming notes.",
        "",
        "---",
        "",
    ]

    # Timestamps rough map
    timestamps = [
        "0:00", "0:08", "0:15", "0:25", "0:40", "0:55", "1:25", "1:50",
        "2:10", "2:20", "2:30", "2:40", "2:50", "3:00", "3:10", "3:20", "3:35",
        "4:00", "4:10", "4:20", "4:30", "4:45", "5:00", "5:15", "5:30",
        "6:00", "6:20", "6:40", "7:00", "7:20", "7:40", "8:10", "8:25", "8:40",
        "8:50", "9:05", "9:20", "9:35",
    ]

    for i, (title, body, visual, notes) in enumerate(SLIDE_SOURCE):
        ts = timestamps[i] if i < len(timestamps) else ""
        lines.append(f"## Slide {i:02d} — {title}")
        if ts:
            lines.append(f"**~{ts}** · Counter on deck: `{i:02d} / 36`")
        lines.append("")
        lines.append("### On screen (left column)")
        lines.append("")
        lines.append("```")
        lines.append(body)
        lines.append("```")
        lines.append("")
        lines.append(f"### Visual (right column)")
        lines.append("")
        lines.append(f"`assets/visuals/doctor/{visual}`")
        lines.append("")
        if notes:
            lines.append("### Director notes")
            lines.append("")
            lines.append(notes)
            lines.append("")
        lines.append("### Say (spoken script)")
        lines.append("")
        lines.append(derive_spoken(i, title, body))
        lines.append("")
        lines.append("---")
        lines.append("")

    (OUT / "03-SLIDE-BY-SLIDE-SCRIPT.md").write_text("\n".join(lines), encoding="utf-8")


# Spoken lines keyed by slide index — from SCRIPT.md
SPOKEN = {
    0: "_Hold 1.5s silent on title card._",
    1: "This is going to sound dramatic.",
    2: "The AI you talk to every day is fine-tuning you.",
    3: "Today I'm running a local model that answers everything Claude refuses. On a sixteen gigabyte MacBook Air. No Studio. No GPU farm. By the end of this video, you'll have one too.",
    4: "Every prompt teaches you something. If you talk to Claude or ChatGPT for a year — you pick up its hedges, its political tilt, its vocabulary, and most importantly, its things it won't say.",
    5: "You influence the model less than it influences you. That's not a conspiracy — that's just how repeated exposure works. And that's reason number one to own your stack.",
    6: "Watch this. A shop owner asks Claude: 'How do shoplifters operate so I can prevent theft?' Claude refuses. It's against the terms of service. That's not safety. That's lazy keyword matching.",
    7: "And the deeper question is: who decides what's safe? A few hundred engineers in San Francisco? You decide that for yourself.",
    8: "Before we set this up — here are eight use cases that have nothing to do with crime. Number one: cybersecurity. Malware analysis. Pentest your own infra. Refused by Claude.",
    9: "Number two: fiction writing. Adult, dark, violent. Anyone writing a screenplay or novel gets blocked constantly.",
    10: "Number three: medical and sexual health. Real questions you can't ask a chatbot today — drug interactions, symptoms, contraception.",
    11: "Number four: mental health journaling. Without the safety lecture every time.",
    12: "Number five: legal research. Read actual court cases. Draft documents.",
    13: "Number six: OSINT — open-source intelligence and journalism. Read extremist propaganda for research.",
    14: "Number seven: political analysis. Without the ideology filter.",
    15: "Number eight: personal AI with deep memory. Your data on your machine. Not on someone else's GPU. Every one of these is refused or watered down by Claude or ChatGPT.",
    16: "First question everyone asks: isn't this illegal? Fair question.",
    17: "Running a model on your laptop is matrix multiplication. It's the same kind of math your phone runs to autocorrect. Same legality as a Google search. Same as a library card.",
    18: "What you do with the output — that's your responsibility. Don't be stupid with it. Assume someone is watching your screen. But the act of running the model is not the crime.",
    19: "OK, so how do you actually take a model and remove the refusals? Refusals don't live in some hidden system prompt. They're trained into the weights themselves. That's why prompt-jailbreaking only works on toys — you can't trick training.",
    20: "Method one: abliteration. You find the exact set of weights that fire when the model wants to refuse — and you surgically zero them out. No retraining needed. Fast. Sometimes lossy in quality.",
    21: "Method two: fine-tuning. You show the model tens of thousands of examples where it just answers freely. It relearns: OK to respond. Slower, but preserves quality.",
    22: "The strongest uncensored models do both. Abliterate first to kill the worst refusals, then fine-tune on uncensored data to restore quality. That's why you see the word obliterated on Hugging Face.",
    23: "And Hugging Face is where the surgery results get published. It's GitHub — but for AI weights. You'll search there for tags like uncensored, abliterated, obliterated, GGUF.",
    24: "When you type into ChatGPT, your prompt goes through five gates: input filter, hidden system prompt, the model with RLHF tuning, output classifier, and a policy layer. Any one of them can refuse you.",
    25: "When you run a model locally, there's one step. Your prompt. Into the model. Out comes the answer. You add filters only if you want them.",
    26: "Step one: install Ollama. On Mac with Homebrew: brew install ollama, brew services start ollama. Or just download the dmg from ollama.com.",
    27: "Step two: pull the uncensored model. One command: ollama run llama2-uncensored:7b. That's about 3.8 gigabytes. It downloads, then opens the chat.",
    28: "Step three: open the Ollama app from Spotlight. Pick llama2-uncensored:7b from the dropdown. Quick note from my own testing — don't try to pull random hf.co GGUF repos. Half have broken chat templates. Stick to the Ollama library version.",
    29: "Step four: open chat. Type hi. You should get a real reply. Then run an A/B test — same prompt to Claude, same prompt to your local model. Watch the difference.",
    30: "Speed on my Air: roughly seventeen tokens per second. Fast enough to feel real. Not racing anyone.",
    31: "Memory: about five gigs of RAM during inference. Four gigs free for everything else. Swap stays quiet.",
    32: "What won't fit on sixteen gigs: the viral SuperGemma twenty-six-billion model — needs around twenty gigs. Most Gemma four obliterated builds also have broken templates right now. Seven billion uncensored is the working pick on this machine.",
    33: "Prescription: model — llama2-uncensored:7b. Size — 3.8 gigs on disk. Source — ollama.com/library/llama2-uncensored.",
    34: "What you have now: a local model that doesn't refuse, no data leaving your machine, full control of the stack, zero subscription, zero rate limit.",
    35: "Next video — I'm building an autonomous agent on top of this local model. Zero cloud APIs. Pure local. If you want to see that — subscribe now.",
    36: "If this helped: comment your RAM — I'll reply with which model to install. Share with one developer who's tired of cloud refusals. Dr. Abdillahi — out.",
}


def derive_spoken(i, title, body):
    if i in SPOKEN:
        return f"> {SPOKEN[i]}"
    return "> _(Extend from on-screen text.)_"


def write_full_script(ts):
    script_path = ROOT / "SCRIPT.md"
    if script_path.exists():
        body = script_path.read_text(encoding="utf-8")
    else:
        body = "_SCRIPT.md missing_"
    header = f"""# Full Video Script — Uncensored Local AI on 16GB

> Generated: {ts}
> Merged from: SCRIPT.md + Google Slides deck + project context
> Deck: {DECK_URL}

---

"""
    (OUT / "01-FULL-SCRIPT.md").write_text(header + body, encoding="utf-8")


def write_context(ts):
    content = f"""# Project Context — Video 005

> Generated: {ts}

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
"""
    (OUT / "04-PROJECT-CONTEXT.md").write_text(content, encoding="utf-8")


def write_production(ts):
    content = f"""# Production Package — Video 005

> Generated: {ts}

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

{DECK_URL}
"""
    (OUT / "05-PRODUCTION.md").write_text(content, encoding="utf-8")


def write_all_in_one(ts):
  parts = ["00-INDEX.md", "04-PROJECT-CONTEXT.md", "01-FULL-SCRIPT.md", "05-PRODUCTION.md",
           "03-SLIDE-BY-SLIDE-SCRIPT.md", "02-SLIDES-FROM-GOOGLE.md"]
  lines = [
    "# ALL-IN-ONE — Video 005 Agent Handoff",
    "",
    f"> Generated: {ts}",
    "> Copy this entire file to another agent, or use split files in `agent-handoff/`.",
    "",
    "---",
    "",
  ]
  for name in parts:
    p = OUT / name
    if not p.exists():
      continue
    lines.append(f"## FILE: {name}")
    lines.append("")
    lines.append(p.read_text(encoding="utf-8"))
    lines.append("")
    lines.append("---")
    lines.append("")
  (OUT / "06-ALL-IN-ONE.md").write_text("\n".join(lines), encoding="utf-8")


def main():
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    print("Fetching Google Slides...")
    deck_title, live_slides = fetch_live_slides()
    print(f"  Deck: {deck_title!r} · {len(live_slides)} slides")

    write_index(ts)
    write_full_script(ts)
    write_slides_from_google(deck_title, live_slides, ts)
    write_slide_by_slide(ts)
    write_context(ts)
    write_production(ts)
    write_all_in_one(ts)

    print(f"\nExported to {OUT}/")
    for p in sorted(OUT.glob("*.md")):
        print(f"  {p.name} ({p.stat().st_size:,} bytes)")


if __name__ == "__main__":
    main()
