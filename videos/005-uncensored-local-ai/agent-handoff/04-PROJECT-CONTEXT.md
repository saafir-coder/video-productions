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
