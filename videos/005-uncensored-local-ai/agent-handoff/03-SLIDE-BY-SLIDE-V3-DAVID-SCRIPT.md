# Slide-by-Slide — V3 (David-style script)

> Built: 2026-05-19 · **27 slides** · Layout: text left / visual right  
> **Deck:** https://docs.google.com/presentation/d/1H5EjsUaeSML9qS4qzKgfSF9LO5S4gsvtKuU0lJgIgvU/edit  
> **Previous deck (V2 / Dr. Abdillahi 36-click):** https://docs.google.com/presentation/d/1__1oytnNhw1BlGumJ0OwOmjwGjacoSmVkMgXh9hCF7Y/edit  
> **Reference bundle:** `06-ALL-IN-ONE.md`

Present mode: press **→** for each reveal (same progressive pattern as V2).

| # | Section | Title on slide |
|---|---------|----------------|
| 00 | Title | This Uncensored AI Model Is Insane |
| 01–03 | Intro | THE FORBIDDEN LLMs → USE IT LEGALLY |
| 04–05 | Why you need one | ONE AI FINE-TUNES YOU → OWN YOUR STACK |
| 06–08 | Mainstream | THE REFUSAL WALL → OVER-REFUSAL → WHO DECIDES SAFE? |
| 09–12 | Local solution | UNCENSORED label → Privacy → Cost+Offline → Tools simple |
| 13–16 | Ollama setup | Steps 1–4 (dolphin-llama3) |
| 17–19 | Demo | Fiction lock-pick → Political essay → Raw instruction-following |
| 20–22 | Dark side | Not unbiased → Real risks → Your responsibility |
| 23–26 | Outro | Insane empowerment → Recap → Subscribe → Who controls AI? |

## Cold open (no slide — B-roll before slide 00)

Split-screen: ChatGPT-style **refuses** lock-pick fiction vs dark UI **answers** in detail (~10s). Then host on camera → slide 00.

## Model command (on-camera)

```bash
ollama run dolphin-llama3
```

(Script source; say **ollama.com** not "olama".)

## Rebuild

```bash
cd 2.areas/content/videos/005-uncensored-local-ai
python3 rebuild-deck-v3-david-script.py          # new deck
python3 rebuild-deck-v3-david-script.py --replace  # overwrite V2 deck ID
```

## V2 vs V3 (what changed)

| V2 (06-ALL-IN-ONE) | V3 (this script) |
|--------------------|------------------|
| 37 slides, 36 clicks | 27 slides |
| `llama2-uncensored:7b`, 16GB Air focus | `dolphin-llama3`, general hardware |
| 8 use cases, surgery metaphor, cloud 5-gate | Shorter Ondrej-style arc: refusal → local benefits → setup → demo → ethics |
| Dr. Abdillahi prescription Rx | Subscribe + New Society CTA |
