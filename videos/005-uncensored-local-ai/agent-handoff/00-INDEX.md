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
| **06-ALL-IN-ONE.md** | Everything above in one file (for single copy-paste) |
| **07-DECK-V3-LINK.md** | V3 deck URL (David-style script, 27 slides) |
| **03-SLIDE-BY-SLIDE-V3-DAVID-SCRIPT.md** | V3 filming sync + comparison to V2 |

## Source of truth

| Asset | URL / path |
|-------|------------|
| Google Slides deck (V2) | https://docs.google.com/presentation/d/1__1oytnNhw1BlGumJ0OwOmjwGjacoSmVkMgXh9hCF7Y/edit |
| Google Slides deck (V3 — **current script**) | https://docs.google.com/presentation/d/1H5EjsUaeSML9qS4qzKgfSF9LO5S4gsvtKuU0lJgIgvU/edit |
| Model command (V3 script) | `ollama run dolphin-llama3` |
| Model command (V2 deck) | `ollama run llama2-uncensored:7b` |
| Ollama library | https://ollama.com/library/llama2-uncensored |
| Reference video | https://youtu.be/TS_hH4sdiKs (David Ondrej) |
| Local visuals | `../assets/visuals/doctor/*.png` |
| Rebuild deck V2 | `python3 ../rebuild-deck-v2.py` |
| Rebuild deck V3 | `python3 ../rebuild-deck-v3-david-script.py` |

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
