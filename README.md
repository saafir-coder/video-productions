# video-productions

Inner-Sizze video production hub: scripts, Google Slides decks, agent handoffs, and rebuild tooling.

**Org:** [saafir-coder](https://github.com/saafir-coder)

## What lives here

| Area | Purpose |
|------|---------|
| `videos/NNN-topic/` | One folder per video (script, slides, assets, handoff) |
| `agent-handoff/` | Filming exports: slide-by-slide sync, production notes |
| `scripts/` | Deck rebuild (`gws` + Google Slides API), visual generation |

## Layout (per video)

```
videos/005-example/
├── README.md
├── SCRIPT.md
├── rebuild-deck-*.py      # text left · visual right
├── assets/visuals/
└── agent-handoff/
    ├── 00-INDEX.md
    ├── 03-SLIDE-BY-SLIDE-*.md
    └── 07-DECK-LINK.md
```

## Slide deck format

Every content slide:

- **Left:** on-screen script text (progressive reveal — press → in Present)
- **Right:** diagram / screenshot / brand visual

Built with [Google Workspace CLI (`gws`)](https://github.com/googleworkspace/cli) → Slides `batchUpdate` + Drive-hosted PNGs.

## Active projects

| Video | Deck | Model (demo) |
|-------|------|----------------|
| 005 — Uncensored local AI (V3) | [Google Slides](https://docs.google.com/presentation/d/1H5EjsUaeSML9qS4qzKgfSF9LO5S4gsvtKuU0lJgIgvU/edit) | `ollama run dolphin-llama3` |

Workspace source (local): `Claude-skills-Work-space-rebuilt/2.areas/content/videos/005-uncensored-local-ai/`

## Prerequisites

- `npx gws` authenticated to Google Workspace (Slides + Drive)
- Python 3.10+
- Ollama (for local-AI tutorial videos)

## License

Private / Inner-Sizze — all rights reserved unless noted otherwise.
