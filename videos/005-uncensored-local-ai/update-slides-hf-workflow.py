#!/usr/bin/env python3
"""Patch existing Google Slides deck: HF + hf.co workflow (no llama2-uncensored library)."""
import json
import subprocess
import sys

PRES_ID = "1__1oytnNhw1BlGumJ0OwOmjwGjacoSmVkMgXh9hCF7Y"

# Primary model for 16GB — must be GGUF on Hugging Face
HF_MODEL = "Centara/gemma-4-E4B-it-OBLITERATED-Q4_K_M-GGUF"
OLLAMA_CMD = f"ollama run hf.co/{HF_MODEL}"

REPLACEMENTS = [
    ("llama2-uncensored 7B", "Gemma 4B obliterated GGUF (from Hugging Face)"),
    ("llama2-uncensored:7b", f"hf.co/{HF_MODEL}"),
    ("llama2-uncensored", "hugging face gguf + hf.co"),
    (
        '"Step two: pick a model that fits. Not SuperGemma 26B first — start with Gemma 4B obliterated GGUF (from Hugging Face). About four gigs."',
        '"Step two: on huggingface.co find a .gguf uncensored model (we use Gemma 4B obliterated). Must be GGUF — safetensors alone won\'t work with hf.co."',
    ),
    (
        "ollama pull llama2-uncensored:7b\nollama run llama2-uncensored:7b",
        f"# Browse: huggingface.co/models → Files → .gguf\n{OLLAMA_CMD}\n\n# NOT hf.com — use hf.co\n# Example alt: ollama run hf.co/TheBloke/llama2_7b_chat_uncensored-GGUF:Q4_K_M",
    ),
    ("ollama run hf.co/[model-path]", OLLAMA_CMD),
    (
        "What actually worked on my machine: Gemma 4B obliterated GGUF (from Hugging Face). Fast enough. Actually answers.",
        "What actually worked on my machine: pull from Hugging Face with hf.co — Gemma 4B obliterated Q4. Fast enough. Actually answers.",
    ),
    (
        "□ llama2-uncensored:7b pulled & responds",
        f"□ {OLLAMA_CMD} — pulls & responds\n□ Confirm repo has .gguf files (not safetensors only)",
    ),
    (
        "huggingface.co/models",
        "huggingface.co/models\n\nPull command:\n" + OLLAMA_CMD + "\n\n⚠ hf.co — NOT hf.com",
    ),
]

# Full body replace for HF hub slide (enhance-slides-images created s_hf_hub)
HF_HUB_OLD_SNIPPET = "In this video: find uncensored variants on HF → pull via Ollama → run locally."
HF_HUB_NEW = """Workflow (memorize this):
1. huggingface.co/models — search obliterated / uncensored + GGUF
2. Open Files — confirm .gguf exists (safetensors ≠ ollama hf.co)
3. Copy: ollama run hf.co/USER/REPO:QUANT

Our 16GB pick:
ollama run hf.co/Centara/gemma-4-E4B-it-OBLITERATED-Q4_K_M-GGUF

⚠ hf.co — NOT hf.com (manifest error)"""


def main():
    reqs = []
    for old, new in REPLACEMENTS:
        reqs.append({
            "replaceAllText": {
                "containsText": {"text": old, "matchCase": False},
                "replaceText": new,
                "pageObjectIds": [],  # all slides
            }
        })

    reqs.append({
        "replaceAllText": {
            "containsText": {"text": HF_HUB_OLD_SNIPPET, "matchCase": True},
            "replaceText": HF_HUB_NEW,
        }
    })

    # Title slide subtitle — add HF path
    reqs.append({
        "replaceAllText": {
            "containsText": {"text": "16GB M3 MacBook Air | Ollama", "matchCase": True},
            "replaceText": "16GB M3 Air | huggingface.co → hf.co → Ollama",
        }
    })

    payload = {"requests": reqs}
    print(f"Applying {len(reqs)} text replacements...")
    r = subprocess.run(
        [
            "npx", "gws", "slides", "presentations", "batchUpdate",
            "--params", json.dumps({"presentationId": PRES_ID}),
            "--json", json.dumps(payload),
        ],
        capture_output=True,
        text=True,
    )
    if r.returncode != 0:
        print(r.stderr or r.stdout, file=sys.stderr)
        sys.exit(r.returncode)
    print("Updated:", f"https://docs.google.com/presentation/d/{PRES_ID}/edit")


if __name__ == "__main__":
    main()
