#!/usr/bin/env python3
"""Add Hugging Face + Ollama visuals to video deck via Slides createImage."""
import json
import subprocess
import sys

PRES_ID = "1__1oytnNhw1BlGumJ0OwOmjwGjacoSmVkMgXh9hCF7Y"

# Public image URLs for Slides createImage (must be stable PNG/JPEG, no auth)
# Uploaded via: gws drive +upload + permissions create (anyone reader)
def drive_url(file_id: str) -> str:
    return f"https://drive.google.com/uc?export=view&id={file_id}"


URLS = {
    "hf_title": drive_url("1GB09FTCELtLMKlrLYvMa3QhdKZOdLl3h"),
    "hf_icon": drive_url("1BcrDHM_S1TvcfLE6EOzL7O3KpLc0cM2y"),
    "ollama": drive_url("1NTx-fX3CR97JFNVSTrtJErwhiH3_gPDd"),
}

# EMU layout helpers (slide ~10" x 5.6")
def img(id_, url, page, x, y, w, h):
    return {
        "createImage": {
            "objectId": id_,
            "url": url,
            "elementProperties": {
                "pageObjectId": page,
                "size": {
                    "width": {"magnitude": w, "unit": "EMU"},
                    "height": {"magnitude": h, "unit": "EMU"},
                },
                "transform": {
                    "scaleX": 1,
                    "scaleY": 1,
                    "translateX": x,
                    "translateY": y,
                    "unit": "EMU",
                },
            },
        }
    }


def hf_slide_block(sid, stid, btid, insertion_index):
    """New slide: Hugging Face = GitHub for models."""
    title = "WHERE TO GET llama2-uncensored:7b"
    body = """Our model (use this in the video):

https://ollama.com/library/llama2-uncensored

ollama pull llama2-uncensored:7b
ollama run llama2-uncensored:7b

Optional reference on Hugging Face:
georgesung/llama2_7b_chat_uncensored
(same idea — open weights; Ollama packages it for you)

~3.8 GB — fits 16GB M3 Air"""

    reqs = [
        {
            "createSlide": {
                "objectId": sid,
                "insertionIndex": insertion_index,
                "slideLayoutReference": {"predefinedLayout": "TITLE_AND_BODY"},
                "placeholderIdMappings": [
                    {"layoutPlaceholder": {"type": "TITLE", "index": 0}, "objectId": stid},
                    {"layoutPlaceholder": {"type": "BODY", "index": 0}, "objectId": btid},
                ],
            }
        },
        {"insertText": {"objectId": stid, "text": title, "insertionIndex": 0}},
        {"insertText": {"objectId": btid, "text": body, "insertionIndex": 0}},
        img("hf_hub_logo", URLS["hf_title"], sid, 5200000, 1200000, 3600000, 950000),
        img("hf_hub_icon", URLS["hf_icon"], sid, 5200000, 2400000, 1200000, 1200000),
    ]
    return reqs


def main():
    reqs = []

    # Dedicated HF slide after Install (index 8 = after s_act1)
    reqs += hf_slide_block("s_hf_hub", "s_hf_hub_t", "s_hf_hub_b", 8)

    # Title slide — branding strip
    reqs.append(img("img_title_hf", URLS["hf_title"], "p", 200000, 3800000, 2800000, 750000))
    reqs.append(img("img_title_ollama", URLS["ollama"], "p", 3200000, 3850000, 700000, 990000))

    # Context — HF as source of truth for open weights
    reqs.append(img("img_ctx_hf", URLS["hf_icon"], "s_ctx", 6000000, 800000, 1100000, 1100000))

    # Install — Ollama
    reqs.append(img("img_act1_ollama", URLS["ollama"], "s_act1", 5800000, 600000, 900000, 1280000))

    # 16GB reality — HF quant picker callout
    reqs.append(img("img_act3_hf", URLS["hf_title"], "s_act3", 5000000, 500000, 3200000, 850000))

    # Payoff — both ecosystems
    reqs.append(img("img_pay_hf", URLS["hf_icon"], "s_payoff", 6200000, 700000, 900000, 900000))
    reqs.append(img("img_pay_ollama", URLS["ollama"], "s_payoff", 7100000, 700000, 650000, 920000))

    # Thumbnail concept — visual hint
    reqs.append(img("img_thumb_hf", URLS["hf_icon"], "s_thumb", 6000000, 1000000, 1000000, 1000000))

  # B-roll checklist — remind to film HF
    reqs.append(img("img_broll_hf", URLS["hf_title"], "s_broll", 4800000, 1400000, 3000000, 800000))

    payload = {"requests": reqs}
    cmd = [
        "npx", "gws", "slides", "presentations", "batchUpdate",
        "--params", json.dumps({"presentationId": PRES_ID}),
        "--json", json.dumps(payload),
    ]
    print(f"Applying {len(reqs)} visual requests...")
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print(r.stderr or r.stdout, file=sys.stderr)
        sys.exit(r.returncode)
    print(r.stdout[-500:] if len(r.stdout) > 500 else r.stdout)
    print(f"\nhttps://docs.google.com/presentation/d/{PRES_ID}/edit")


if __name__ == "__main__":
    main()
