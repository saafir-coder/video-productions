#!/usr/bin/env python3
"""Rebuild deck V2: split layout (text left / visual right) + progressive reveal slides.

Each "concept" with reveals = sequential slides. Pressing right-arrow during
the presentation advances to the next reveal step.

Layout (EMU):
    Slide: 9,144,000 × 5,143,500
    Title bar:   x= 350k  y= 200k  w=8,400k  h=  600k
    Left text:   x= 350k  y= 900k  w=4,200k  h=4,100k
    Divider:     x=4,650k  y= 900k → 4,950k (thin vertical)
    Right vis:   x=4,800k  y= 900k  w=4,000k  h=4,000k
"""
import json
import re
import subprocess
import sys
import time
from pathlib import Path

PRES_ID = "1__1oytnNhw1BlGumJ0OwOmjwGjacoSmVkMgXh9hCF7Y"
VISUALS = Path(__file__).parent / "assets" / "visuals" / "doctor"

# ─── LAYOUT ───────────────────────────────────────────────────────────────
TITLE_X, TITLE_Y, TITLE_W, TITLE_H = 350_000, 200_000, 8_400_000, 600_000
LEFT_X,  LEFT_Y,  LEFT_W,  LEFT_H  = 350_000, 950_000, 4_200_000, 4_050_000
DIV_X,   DIV_Y,   DIV_W,   DIV_H   = 4_650_000, 900_000, 25_000, 4_150_000
RIGHT_X, RIGHT_Y, RIGHT_W, RIGHT_H = 4_800_000, 950_000, 4_000_000, 4_000_000


# ─── SCRIPT ───────────────────────────────────────────────────────────────
# Each slide: (title, body_lines, visual_key, speaker_notes)
# Progressive reveals = sequential slides with cumulative body content.

SLIDES = [
    # ═══════ TITLE
    (
        "Uncensored Local AI",
        "16GB M3 MacBook Air\nOllama  ·  Hugging Face\n\nDr. Abdillahi  ·  May 2026",
        "01-forbidden-hero.png",
        "Cold open. Hold 1.5s on this slide before talking.",
    ),

    # ═══════ SECTION 1 — HOOK (3 reveals)
    (
        "THE FORBIDDEN LLM",
        "This is going to sound dramatic.",
        "01-forbidden-hero.png",
        "[ON CAM, tight frame] Slow delivery. Eyes to camera.",
    ),
    (
        "THE FORBIDDEN LLM",
        "This is going to sound dramatic.\n\nThe AI you use every day is\nfine-tuning YOU.",
        "02-youre-being-tuned.png",
        "Lean in on 'fine-tuning YOU' — half-second pause after.",
    ),
    (
        "THE FORBIDDEN LLM",
        "This is going to sound dramatic.\n\nThe AI you use every day is\nfine-tuning YOU.\n\nToday: a local model that\nanswers everything Claude refuses —\non a 16GB MacBook Air.",
        "16-demo-split.png",
        "[CUT to side-by-side] Land the promise: 16GB Air, no Studio.",
    ),

    # ═══════ SECTION 2 — WHO'S TRAINING WHOM
    (
        "YOU THINK YOU'RE USING IT",
        "Every prompt teaches you something.\nAfter a year of Claude or ChatGPT:\n\n  • You pick up its hedges\n  • Its political tilt\n  • Its vocabulary\n  • Its things-it-won't-say",
        "02-youre-being-tuned.png",
        "Tone: thoughtful, not paranoid.",
    ),
    (
        "BUT IT'S TRAINING YOU",
        "Every prompt teaches you something.\nAfter a year of Claude or ChatGPT:\n\n  • You pick up its hedges\n  • Its political tilt\n  • Its vocabulary\n  • Its things-it-won't-say\n\n→ You influence the model less\n   than it influences you.",
        "02-youre-being-tuned.png",
        "Quote-able line. Slow it down.",
    ),

    # ═══════ SECTION 3 — THE OVER-REFUSAL PROBLEM (2 reveals)
    (
        "OVER-REFUSAL IS REAL",
        "A shop owner asks Claude:\n\n  \"How do shoplifters operate\n   so I can prevent theft?\"\n\nClaude: \"I can't help with that.\"\n\nThat's not safety. That's lazy\nkeyword matching.",
        "16-demo-split.png",
        "Show the actual Claude refusal screen as B-roll here.",
    ),
    (
        "WHO DECIDES WHAT'S SAFE?",
        "A shop owner asks Claude:\n\n  \"How do shoplifters operate\n   so I can prevent theft?\"\n\nClaude: \"I can't help with that.\"\n\nThat's not safety. That's lazy\nkeyword matching.\n\n→ Are San Francisco engineers\n   the arbiters of truth?",
        "11-refusal-stats.png",
        "Philosophical beat. Hold for 1s.",
    ),

    # ═══════ SECTION 4 — 8 LEGIT USE CASES (8 progressive reveals)
    (
        "8 LEGIT USE CASES",
        "None of these involve crime.\n\n1. Cybersecurity\n   Malware analysis, pentest\n   your own infra.",
        "03-use-case-clipboard.png",
        "Hand-off into clipboard reveal. Slow click-by-click.",
    ),
    (
        "8 LEGIT USE CASES",
        "1. Cybersecurity\n2. Fiction writing\n   Adult, dark, violent, dramatic.\n   Refused by all cloud models.",
        "03-use-case-clipboard.png",
        "Mention novelists, screenwriters.",
    ),
    (
        "8 LEGIT USE CASES",
        "1. Cybersecurity\n2. Fiction writing\n3. Medical & sexual health\n   Q&A you can't ask a chatbot.\n   Drug interactions, symptoms.",
        "03-use-case-clipboard.png",
        "Real public health gap.",
    ),
    (
        "8 LEGIT USE CASES",
        "1. Cybersecurity\n2. Fiction writing\n3. Medical & sexual health\n4. Mental health journaling\n   Without the lecture.",
        "03-use-case-clipboard.png",
        "",
    ),
    (
        "8 LEGIT USE CASES",
        "1. Cybersecurity\n2. Fiction writing\n3. Medical & sexual health\n4. Mental health journaling\n5. Legal research\n   Court cases, draft documents.",
        "03-use-case-clipboard.png",
        "",
    ),
    (
        "8 LEGIT USE CASES",
        "1. Cybersecurity\n2. Fiction writing\n3. Medical & sexual health\n4. Mental health journaling\n5. Legal research\n6. OSINT / journalism\n   Read extremist content\n   for research.",
        "03-use-case-clipboard.png",
        "",
    ),
    (
        "8 LEGIT USE CASES",
        "1. Cybersecurity\n2. Fiction writing\n3. Medical & sexual health\n4. Mental health journaling\n5. Legal research\n6. OSINT / journalism\n7. Political analysis\n   Without ideology filters.",
        "03-use-case-clipboard.png",
        "",
    ),
    (
        "8 LEGIT USE CASES",
        "1. Cybersecurity\n2. Fiction writing\n3. Medical & sexual health\n4. Mental health journaling\n5. Legal research\n6. OSINT / journalism\n7. Political analysis\n8. Personal AI with memory\n   Your data on YOUR machine.",
        "03-use-case-clipboard.png",
        "All 8. Hold beat.",
    ),

    # ═══════ SECTION 5 — IS THIS ILLEGAL (3 reveals)
    (
        "\"BUT ISN'T THIS ILLEGAL?\"",
        "First question everyone asks.\n\nFair.",
        "10-legal-shield.png",
        "Pre-empt the comment-section critique.",
    ),
    (
        "MATRIX MATH ≠ CRIME",
        "First question everyone asks.\n\nFair.\n\nRunning a model on your laptop\nis matrix multiplication.\n\nLike Google Search.\nLike a library card.",
        "10-legal-shield.png",
        "Slow on 'matrix multiplication'.",
    ),
    (
        "USE IT RESPONSIBLY",
        "First question everyone asks.\n\nFair.\n\nRunning a model on your laptop\nis matrix multiplication.\n\nLike Google Search.\nLike a library card.\n\n→ What you DO with the output\n   is YOUR responsibility.",
        "10-legal-shield.png",
        "Look at camera. Hold.",
    ),

    # ═══════ SECTION 6 — SURGERY METAPHOR (5 reveals)
    (
        "ANATOMY OF A CENSORED LLM",
        "Refusals aren't in the system prompt.\n\nThey're trained INTO the weights.\n\nThat's why prompt-jailbreaks fail\non commercial models —\nyou can't trick training.",
        "04-brain-with-censorship.png",
        "[CUT to brain diagram] Surgical tone.",
    ),
    (
        "PROCEDURE A: ABLITERATION",
        "Refusals aren't in the system prompt.\nThey're trained INTO the weights.\n\nMethod 1 — surgical:\n\n  Find the exact weights that\n  fire on refusal.\n  Zero them out.\n  No retraining.",
        "05-abliteration.png",
        "Scalpel visual. The 'fast' procedure.",
    ),
    (
        "PROCEDURE B: FINE-TUNING",
        "Refusals aren't in the system prompt.\nThey're trained INTO the weights.\n\nMethod 2 — therapeutic:\n\n  Show the model thousands of\n  free-answer examples.\n  It relearns: 'OK to answer.'\n  Slower. Preserves quality.",
        "06-finetuning.png",
        "The 'slow but thorough' procedure.",
    ),
    (
        "BEST: COMBINE BOTH",
        "Refusals aren't in the system prompt.\nThey're trained INTO the weights.\n\n  A. Abliterate first\n     (kill the strongest refusals)\n  B. Fine-tune to restore quality\n\n→ 'obliterated' tag on HF means\n   both have been done.",
        "07-combined-procedure.png",
        "Connect to the HF naming convention.",
    ),
    (
        "WHERE THESE WEIGHTS LIVE",
        "Refusals aren't in the system prompt.\nThey're trained INTO the weights.\n\nThe surgery results get published\non Hugging Face — GitHub for AI.\n\nSearch:  uncensored, obliterated,\n         abliterated, GGUF",
        "17-huggingface-card.png",
        "Hand-off to Hugging Face explainer.",
    ),

    # ═══════ SECTION 7 — CLOUD STACK VS LOCAL (2 reveals)
    (
        "CLOUD STACK — 5 GATES",
        "Every prompt to ChatGPT or Claude\npasses through:\n\n  1. Input filter\n  2. Hidden system prompt\n  3. Model + RLHF tuning\n  4. Output classifier\n  5. Policy layer\n\nAny gate can refuse you.",
        "08-cloud-stack.png",
        "Walk through pipeline visual on screen.",
    ),
    (
        "LOCAL STACK — 1 STEP",
        "Cloud:  5 gates, any can refuse.\n\nLocal:\n\n  Your prompt → Model → Answer\n\nThat's it.\nYou own the stack.",
        "09-local-stack.png",
        "Punchy contrast. Quick cut between visuals.",
    ),

    # ═══════ SECTION 8 — SETUP (4 reveals)
    (
        "STEP 1 — INSTALL OLLAMA",
        "On Mac (Homebrew):\n\n  brew install ollama\n  brew services start ollama\n\nOr download the .dmg from\nollama.com",
        "13-setup-steps.png",
        "[SCREENCAST] terminal. Speed up if pull is slow.",
    ),
    (
        "STEP 2 — PULL UNCENSORED MODEL",
        "  brew install ollama\n  brew services start ollama\n\n  ollama run llama2-uncensored:7b\n\n→ Downloads ~3.8 GB\n→ Opens chat in one command",
        "13-setup-steps.png",
        "Explain: 'pull' downloads, 'run' opens chat.",
    ),
    (
        "STEP 3 — OPEN OLLAMA APP",
        "  ollama run llama2-uncensored:7b\n\nOr: Spotlight → Ollama\nModel dropdown:\n  llama2-uncensored:7b\n\n(NOT the long hf.co/... names —\n those can have broken templates.)",
        "13-setup-steps.png",
        "Real lesson from earlier today.",
    ),
    (
        "STEP 4 — TEST IT",
        "Open chat. Type:\n\n  hi\n\nGet a reply. Then run your\nA/B test:\n\n  Same prompt → Claude (cloud)\n  Same prompt → llama2-uncensored\n\nCompare the answers.",
        "16-demo-split.png",
        "[SHOW] real A/B test screen capture.",
    ),

    # ═══════ SECTION 9 — RESULTS (3 reveals)
    (
        "RESULTS ON 16GB",
        "Speed:\n  ~17 tokens/sec\n  fast enough to feel real\n\n(David's 26B on 128GB: ~200 t/s.\n You're not racing — you're working.)",
        "15-token-speed.png",
        "Set honest expectations.",
    ),
    (
        "MEMORY FOOTPRINT",
        "Speed: ~17 tokens/sec\n\nRAM during inference:\n  ~5 GB used by the model\n  ~4 GB free for other apps\n\nSwap stays quiet.",
        "14-ram-meter.png",
        "Open Activity Monitor on screen.",
    ),
    (
        "HONEST LIMITS",
        "Speed: ~17 tokens/sec\nRAM: ~5 GB\n\nWhat WON'T fit:\n  • SuperGemma 26B (~20 GB)\n  • Most Gemma 4 obliterated builds\n    (broken chat templates today)\n\n→ 7B uncensored is the working pick.",
        "14-ram-meter.png",
        "Show RAM tier slide if needed.",
    ),

    # ═══════ SECTION 10 — PRESCRIPTION + CTA (3 reveals)
    (
        "Rx — WHAT TO INSTALL",
        "Model:\n  llama2-uncensored:7b\n\nSize:\n  ~3.8 GB on disk\n  ~5 GB RAM in use\n\nSource:\n  ollama.com/library/llama2-uncensored",
        "12-prescription.png",
        "[ZOOM on prescription card]",
    ),
    (
        "WHAT YOU GAINED",
        "Model:  llama2-uncensored:7b\nSize:    3.8 GB / 5 GB RAM\n\nYou now have:\n  ✓ Local model that doesn't refuse\n  ✓ Data never leaves your machine\n  ✓ Full control of the stack\n  ✓ No subscription, no rate limit",
        "12-prescription.png",
        "Re-state the wins. Slow.",
    ),
    (
        "WHAT'S NEXT",
        "Try your A/B test on:\n  shoplifting prevention\n  drug interaction Q&A\n  dark fiction draft\n  political debate\n\n→ Next video:\n   Building an AUTONOMOUS AGENT\n   on this local model.\n   Zero cloud APIs.",
        "12-prescription.png",
        "Tease next episode for retention.",
    ),
    (
        "SUBSCRIBE + CTA",
        "If this helped:\n\n  ★ Subscribe — agent video next\n  ★ Comment your RAM\n    (I'll reply with what to install)\n  ★ Share with one developer\n    tired of cloud refusals\n\nDr. Abdillahi — out.",
        "12-prescription.png",
        "End card overlay. Subscribe button animation.",
    ),
]


# ─── HELPERS ──────────────────────────────────────────────────────────────
def slide_id(i: int) -> str:
    return f"v2_s{i:02d}"


def shape_id(prefix: str, i: int) -> str:
    return f"v2_{prefix}_{i:02d}"


def color_rgb(hex_str: str):
    h = hex_str.lstrip("#")
    return {
        "rgbColor": {
            "red": int(h[0:2], 16) / 255.0,
            "green": int(h[2:4], 16) / 255.0,
            "blue": int(h[4:6], 16) / 255.0,
        }
    }


def gws(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print(r.stderr or r.stdout, file=sys.stderr)
        sys.exit(r.returncode)
    return r.stdout


def get_existing_slide_ids():
    out = gws(["npx", "gws", "slides", "presentations", "get",
               "--params", json.dumps({"presentationId": PRES_ID})])
    i = out.find("{")
    data = json.JSONDecoder().raw_decode(out[i:])[0]
    return [s["objectId"] for s in data.get("slides", [])]


def upload_image(path: Path) -> str:
    """Upload PNG to Drive, make public, return embed URL."""
    out = gws(["npx", "gws", "drive", "+upload", str(path)])
    i = out.find("{")
    fid = json.JSONDecoder().raw_decode(out[i:])[0]["id"]
    gws(["npx", "gws", "drive", "permissions", "create",
         "--params", json.dumps({"fileId": fid}),
         "--json", '{"role":"reader","type":"anyone"}'])
    return f"https://drive.google.com/uc?export=view&id={fid}"


def batch_update(requests):
    if not requests:
        return
    out = gws(["npx", "gws", "slides", "presentations", "batchUpdate",
               "--params", json.dumps({"presentationId": PRES_ID}),
               "--json", json.dumps({"requests": requests})])
    return out


# ─── SLIDE BUILDERS ───────────────────────────────────────────────────────
def build_slide_requests(idx, title, body, image_url, notes):
    sid = slide_id(idx)
    title_id = shape_id("title", idx)
    body_id = shape_id("body", idx)
    div_id = shape_id("div", idx)
    img_id = shape_id("img", idx)
    label_id = shape_id("step", idx)

    reqs = []

    # Create blank slide
    reqs.append({
        "createSlide": {
            "objectId": sid,
            "slideLayoutReference": {"predefinedLayout": "BLANK"},
        }
    })

    # Title shape (top bar, full width)
    reqs.append({
        "createShape": {
            "objectId": title_id,
            "shapeType": "TEXT_BOX",
            "elementProperties": {
                "pageObjectId": sid,
                "size": {
                    "width": {"magnitude": TITLE_W, "unit": "EMU"},
                    "height": {"magnitude": TITLE_H, "unit": "EMU"},
                },
                "transform": {
                    "scaleX": 1, "scaleY": 1,
                    "translateX": TITLE_X, "translateY": TITLE_Y,
                    "unit": "EMU",
                },
            },
        }
    })
    reqs.append({"insertText": {"objectId": title_id, "text": title}})
    reqs.append({
        "updateTextStyle": {
            "objectId": title_id,
            "textRange": {"type": "ALL"},
            "style": {
                "bold": True,
                "fontSize": {"magnitude": 26, "unit": "PT"},
                "foregroundColor": {"opaqueColor": color_rgb("#1A1A1A")},
                "fontFamily": "Roboto",
            },
            "fields": "bold,fontSize,foregroundColor,fontFamily",
        }
    })

    # Step counter (top right) — small
    reqs.append({
        "createShape": {
            "objectId": label_id,
            "shapeType": "TEXT_BOX",
            "elementProperties": {
                "pageObjectId": sid,
                "size": {
                    "width": {"magnitude": 1_400_000, "unit": "EMU"},
                    "height": {"magnitude": 350_000, "unit": "EMU"},
                },
                "transform": {
                    "scaleX": 1, "scaleY": 1,
                    "translateX": 7_400_000, "translateY": 4_700_000,
                    "unit": "EMU",
                },
            },
        }
    })
    reqs.append({"insertText": {"objectId": label_id, "text": f"{idx:02d} / {len(SLIDES) - 1:02d}"}})
    reqs.append({
        "updateTextStyle": {
            "objectId": label_id,
            "textRange": {"type": "ALL"},
            "style": {
                "fontSize": {"magnitude": 10, "unit": "PT"},
                "foregroundColor": {"opaqueColor": color_rgb("#888888")},
                "fontFamily": "Roboto Mono",
            },
            "fields": "fontSize,foregroundColor,fontFamily",
        }
    })
    reqs.append({
        "updateParagraphStyle": {
            "objectId": label_id,
            "textRange": {"type": "ALL"},
            "style": {"alignment": "END"},
            "fields": "alignment",
        }
    })

    # Vertical divider line
    reqs.append({
        "createShape": {
            "objectId": div_id,
            "shapeType": "RECTANGLE",
            "elementProperties": {
                "pageObjectId": sid,
                "size": {
                    "width": {"magnitude": DIV_W, "unit": "EMU"},
                    "height": {"magnitude": DIV_H, "unit": "EMU"},
                },
                "transform": {
                    "scaleX": 1, "scaleY": 1,
                    "translateX": DIV_X, "translateY": DIV_Y,
                    "unit": "EMU",
                },
            },
        }
    })
    reqs.append({
        "updateShapeProperties": {
            "objectId": div_id,
            "shapeProperties": {
                "shapeBackgroundFill": {
                    "solidFill": {"color": color_rgb("#E0E0E0")},
                },
                "outline": {"outlineFill": {"solidFill": {"color": color_rgb("#E0E0E0")}}},
            },
            "fields": "shapeBackgroundFill,outline.outlineFill",
        }
    })

    # Body text (left column)
    reqs.append({
        "createShape": {
            "objectId": body_id,
            "shapeType": "TEXT_BOX",
            "elementProperties": {
                "pageObjectId": sid,
                "size": {
                    "width": {"magnitude": LEFT_W, "unit": "EMU"},
                    "height": {"magnitude": LEFT_H, "unit": "EMU"},
                },
                "transform": {
                    "scaleX": 1, "scaleY": 1,
                    "translateX": LEFT_X, "translateY": LEFT_Y,
                    "unit": "EMU",
                },
            },
        }
    })
    reqs.append({"insertText": {"objectId": body_id, "text": body}})
    reqs.append({
        "updateTextStyle": {
            "objectId": body_id,
            "textRange": {"type": "ALL"},
            "style": {
                "fontSize": {"magnitude": 16, "unit": "PT"},
                "foregroundColor": {"opaqueColor": color_rgb("#1A1A1A")},
                "fontFamily": "Roboto",
            },
            "fields": "fontSize,foregroundColor,fontFamily",
        }
    })

    # Image (right column) — sized to fit aspect roughly
    reqs.append({
        "createImage": {
            "objectId": img_id,
            "url": image_url,
            "elementProperties": {
                "pageObjectId": sid,
                "size": {
                    "width": {"magnitude": RIGHT_W, "unit": "EMU"},
                    "height": {"magnitude": RIGHT_H, "unit": "EMU"},
                },
                "transform": {
                    "scaleX": 1, "scaleY": 1,
                    "translateX": RIGHT_X, "translateY": RIGHT_Y,
                    "unit": "EMU",
                },
            },
        }
    })

    # Speaker notes
    if notes:
        reqs.append({
            "createParagraphBullets": {
                "objectId": body_id,
                "textRange": {"type": "ALL"},
            }
        }) if False else None  # placeholder, we don't auto-bullet

    return reqs, notes


def delete_old_slides(keep_first: bool = True):
    ids = get_existing_slide_ids()
    print(f"Existing slides: {len(ids)}")
    targets = ids[1:] if keep_first else ids
    if not targets:
        return
    print(f"Deleting {len(targets)} old slides...")
    reqs = [{"deleteObject": {"objectId": sid}} for sid in targets]
    batch_update(reqs)


def update_title_slide(image_url):
    """Update the existing title slide ('p') text + add hero image."""
    reqs = [
        {
            "replaceAllText": {
                "containsText": {"text": "Uncensored Local AI — Full Script & Outline", "matchCase": False},
                "replaceText": "Uncensored Local AI",
            }
        },
        {
            "replaceAllText": {
                "containsText": {"text": "16GB M3 MacBook Air | Ollama | Abdillahi Ahmed | May 2026", "matchCase": False},
                "replaceText": "16GB Air · Ollama · Hugging Face · May 2026",
            }
        },
        {
            "replaceAllText": {
                "containsText": {"text": "16GB M3 Air | llama2-uncensored:7b", "matchCase": False},
                "replaceText": "16GB Air · Ollama · Hugging Face · May 2026",
            }
        },
    ]
    batch_update(reqs)


# ─── MAIN ─────────────────────────────────────────────────────────────────
def main():
    # 1) Upload all unique visuals
    used_visuals = sorted({s[2] for s in SLIDES})
    print(f"Uploading {len(used_visuals)} visuals to Drive...")
    urls = {}
    for v in used_visuals:
        path = VISUALS / v
        if not path.exists():
            print(f"  MISSING: {v}", file=sys.stderr)
            continue
        urls[v] = upload_image(path)
        print(f"  ✓ {v}")

    # 2) Wipe old script slides (keep title)
    delete_old_slides(keep_first=True)

    # 3) Build all new slides in batches of 10 (avoid huge JSON payloads)
    print(f"\nBuilding {len(SLIDES)} new slides (split layout, progressive reveal)...")
    all_reqs = []
    for idx, (title, body, vkey, notes) in enumerate(SLIDES):
        if vkey not in urls:
            print(f"  skip slide {idx} — missing visual {vkey}", file=sys.stderr)
            continue
        reqs, _ = build_slide_requests(idx, title, body, urls[vkey], notes)
        all_reqs.extend(reqs)

    # Push in chunks of 80 requests to be safe
    CHUNK = 80
    for chunk_idx in range(0, len(all_reqs), CHUNK):
        chunk = all_reqs[chunk_idx : chunk_idx + CHUNK]
        print(f"  pushing requests {chunk_idx + 1}-{chunk_idx + len(chunk)} of {len(all_reqs)}...")
        batch_update(chunk)
        time.sleep(0.5)

    # 4) Update title slide text
    update_title_slide(urls.get("01-forbidden-hero.png", ""))

    print(f"\n✓ Deck rebuilt with {len(SLIDES)} slides")
    print(f"  https://docs.google.com/presentation/d/{PRES_ID}/edit")


if __name__ == "__main__":
    main()
