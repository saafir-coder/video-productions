#!/usr/bin/env python3
"""Update Google Slides deck → single model: llama2-uncensored:7b via Ollama library."""
import json
import subprocess

PRES_ID = "1__1oytnNhw1BlGumJ0OwOmjwGjacoSmVkMgXh9hCF7Y"
CMD = "ollama run llama2-uncensored:7b"
PULL = "ollama pull llama2-uncensored:7b"

REPLACEMENTS = [
    ("ollama run hf.co/Centara/gemma-4-E4B-it-OBLITERATED-Q4_K_M-GGUF", CMD),
    ("hf.co/Centara/gemma-4-E4B-it-OBLITERATED-Q4_K_M-GGUF", "llama2-uncensored:7b"),
    ("ollama run hf.co/jeongsohn/SuperGemma-4-26B-uncensored-GGUF-v2", CMD),
    ("Gemma 4B obliterated Q4 on sixteen gigs", "llama2-uncensored 7B (~3.8 GB)"),
    ("Gemma 4B obliterated GGUF (from Hugging Face)", "llama2-uncensored 7B (Ollama library)"),
    ("pull from Hugging Face with hf.co", "pull with Ollama library"),
    ("Hugging Face → hf.co pull → local run", "Ollama library → llama2-uncensored:7b"),
    ("huggingface.co → hf.co → Ollama", "ollama.com/library → llama2-uncensored:7b"),
    ("16GB M3 Air | huggingface.co → hf.co → Ollama", "16GB M3 Air | llama2-uncensored:7b"),
    ("# Browse: huggingface.co/models → Files → .gguf\nollama run hf.co/Centara/gemma-4-E4B-it-OBLITERATED-Q4_K_M-GGUF\n\n# NOT hf.com — use hf.co | safetensors-only repos will fail",
     f"# Install Ollama from ollama.com\n{PULL}\n{CMD}\n\n# Or one step: {CMD}"),
    ("Step two: huggingface.co — find uncensored model with .gguf files. Not SuperGemma 26B on 16GB.",
     "Step two: ollama pull llama2-uncensored:7b — ~3.8 GB, fits 16GB RAM. (Viral 26B Gemma is optional pain-test only.)"),
    ("Tier 2: 4B obliterated Gemma (closest to viral topic)", "Tier 2 ✓: llama2-uncensored:7b (what we use)"),
    ("□ ollama run hf.co/Centara/gemma-4-E4B-it-OBLITERATED-Q4_K_M-GGUF works\n□ Repo has .gguf (not safetensors-only) — hf.co not hf.com",
     f"□ {PULL} completes\n□ {CMD} answers hi + A/B test prompt\n□ Film in Ollama app — model: llama2-uncensored:7b"),
    ("Description keywords: Ollama, Hugging Face, hf.co, uncensored, GGUF, 16GB RAM, self-hosted",
     "Description keywords: Ollama, llama2-uncensored, uncensored, local AI, 16GB RAM, self-hosted"),
]

HF_HUB_NEW = """WHERE TO GET IT (our model)

1. Ollama library (what we use):
   https://ollama.com/library/llama2-uncensored

   ollama pull llama2-uncensored:7b
   ollama run llama2-uncensored:7b

2. Original weights on Hugging Face (reference):
   huggingface.co/georgesung/llama2_7b_chat_uncensored

3. GGUF on HF (advanced — needs correct template):
   TheBloke/llama2_7b_chat_uncensored-GGUF

For this video: use Ollama library only — one command, works."""

def main():
    reqs = [{"replaceAllText": {"containsText": {"text": o, "matchCase": False}, "replaceText": n}}
            for o, n in REPLACEMENTS]
    # HF hub slide — replace common old blocks
    for old in [
        "Workflow:\n1. huggingface.co/models (browse)\n2. ollama run hf.co/USER/REPO:QUANT (pull + run)",
        "Workflow (memorize this):",
    ]:
        reqs.append({"replaceAllText": {"containsText": {"text": old, "matchCase": False},
                                        "replaceText": HF_HUB_NEW[:200] if len(old) < 30 else HF_HUB_NEW}})
    payload = {"requests": reqs}
    r = subprocess.run(
        ["npx", "gws", "slides", "presentations", "batchUpdate",
         "--params", json.dumps({"presentationId": PRES_ID}),
         "--json", json.dumps(payload)],
        capture_output=True, text=True,
    )
    if r.returncode != 0:
        print(r.stderr or r.stdout)
        raise SystemExit(1)
    print("Slides updated:", f"https://docs.google.com/presentation/d/{PRES_ID}/edit")

if __name__ == "__main__":
    main()
