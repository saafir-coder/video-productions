# Video 005 — Uncensored Local AI on 16GB RAM

> Working title: **The Forbidden LLM — on a 16GB MacBook Air**
> Target length: 9-10 min · Status: V2 deck shipped · Filming-ready

## Quick links

- **Agent handoff (markdown bundle for other agents)** → [`agent-handoff/00-INDEX.md`](./agent-handoff/00-INDEX.md) · single file: [`06-ALL-IN-ONE.md`](./agent-handoff/06-ALL-IN-ONE.md)
- **Full script (filming-ready)** → [`SCRIPT.md`](./SCRIPT.md)
- **Google Slides deck (37 slides, split-layout, click-reveals)** → [Open in Slides](https://docs.google.com/presentation/d/1__1oytnNhw1BlGumJ0OwOmjwGjacoSmVkMgXh9hCF7Y/edit)
- **Reference inspiration** → [David Ondrej — uncensored SuperGemma](https://youtu.be/TS_hH4sdiKs)

### Regenerate markdown from Google Slides

```bash
python3 export-handoff.py
```

Writes `agent-handoff/*.md` (live Slides fetch + full script + slide-by-slide + context + production).

## Deck V2 design

Every content slide is split:

- **LEFT** — script copy (what you say)
- **RIGHT** — visual element (what the viewer sees)
- **Bottom right** — slide counter (NN / 36)

Each "concept" is broken across sequential slides so pressing the right-arrow during the presentation reveals the next element. 36 reveal points total (see SCRIPT.md "engagement beats" table).

## Deck sections

| Slides | Section | Reveals |
|---|---|---|
| 00 | Title card | 1 |
| 01-03 | Hook — *The Forbidden LLM* | 3 |
| 04-05 | Who's training whom (you ↔ model) | 2 |
| 06-07 | Over-refusal is real | 2 |
| 08-15 | 8 legitimate use cases | 8 |
| 16-18 | "But isn't this illegal?" | 3 |
| 19-23 | Surgery: how models are liberated (abliteration / fine-tuning / both) | 5 |
| 24-25 | Cloud stack (5 gates) vs Local stack (1 step) | 2 |
| 26-29 | Setup step-by-step (install → pull → app → A/B test) | 4 |
| 30-32 | Results + honest hardware limits | 3 |
| 33-36 | Rx card · what you gained · next-video tease · CTA | 4 |

## Visual library (Dr. Abdillahi theme)

Generated in `assets/visuals/doctor/`:

| Visual | Use |
|---|---|
| `01-forbidden-hero.png` | Title + hook |
| `02-youre-being-tuned.png` | "The model is fine-tuning you" |
| `03-use-case-clipboard.png` | Medical chart with 8 use cases |
| `04-brain-with-censorship.png` | Anatomy diagram (refusal layer highlighted) |
| `05-abliteration.png` | Scalpel removing refusal weights |
| `06-finetuning.png` | IV drip of uncensored data |
| `07-combined-procedure.png` | Both procedures → liberated model |
| `08-cloud-stack.png` | 5-gate filter pipeline |
| `09-local-stack.png` | 1-step direct path |
| `10-legal-shield.png` | Balance scale: math vs crime |
| `11-refusal-stats.png` | Bar chart: Claude vs Local refusal rates |
| `12-prescription.png` | Final Rx card with the model |
| `13-setup-steps.png` | Terminal walk-through |
| `14-ram-meter.png` | 16GB Activity Monitor breakdown |
| `15-token-speed.png` | tok/s comparison vs Ondrej's 128GB rig |
| `16-demo-split.png` | Side-by-side Claude REFUSED / Local ANSWERED |
| `17-huggingface-card.png` | Hugging Face explainer |

## The model we use

**`llama2-uncensored:7b`** only (~3.8 GB).

### Where to get it

| Source | Link | Command |
|---|---|---|
| **Ollama library (use this)** | [ollama.com/library/llama2-uncensored](https://ollama.com/library/llama2-uncensored) | `ollama run llama2-uncensored:7b` |
| Original on Hugging Face (reference) | [georgesung/llama2_7b_chat_uncensored](https://huggingface.co/georgesung/llama2_7b_chat_uncensored) | Browse only — safetensors |
| GGUF on HF (advanced) | [TheBloke/llama2_7b_chat_uncensored-GGUF](https://huggingface.co/TheBloke/llama2_7b_chat_uncensored-GGUF) | Needs fixed Modelfile — we skip |

```bash
# Install Ollama
brew install ollama
brew services start ollama

# Download + run (pull happens on first run)
ollama run llama2-uncensored:7b
```

In the **Ollama app**: select **`llama2-uncensored:7b`** from the dropdown.

## Rebuild commands

```bash
# Re-generate visuals
python3 generate-doctor-visuals.py

# Rebuild the full deck (wipes V1, pushes V2 with 37 slides)
python3 rebuild-deck-v2.py
```

The rebuild script:
1. Uploads all 17 doctor visuals to Drive (public read).
2. Deletes every slide except the title slide.
3. Builds 37 new split-layout slides with title + left text + divider + right image + slide counter.
4. Updates the title slide's subtitle text.

## B-roll checklist (for filming)

- [ ] Claude refusal screen (shoplifter prompt)
- [ ] Same prompt → local model answering
- [ ] Terminal: `ollama run llama2-uncensored:7b`
- [ ] Activity Monitor RAM during inference
- [ ] Ollama app chat (model dropdown)
- [ ] Hugging Face page for `georgesung/llama2_7b_chat_uncensored`

## Legacy files

V1 build scripts (`build-slides.py`, `enhance-slides-images.py`, `generate-deck-visuals.py`, `push-diagram-visuals.py`, `update-slides-llama2-only.py`) are kept for reference but **superseded by `rebuild-deck-v2.py`**.
