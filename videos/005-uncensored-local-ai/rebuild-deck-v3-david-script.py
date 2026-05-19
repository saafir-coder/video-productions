#!/usr/bin/env python3
"""Rebuild deck V3 from David-style script: text left / visual right + progressive reveals.

Based on user script (May 2026). Reference layout: agent-handoff/06-ALL-IN-ONE.md
Creates a NEW Google Slides deck by default (preserves V2 deck).

Usage:
  python3 rebuild-deck-v3-david-script.py           # new deck
  python3 rebuild-deck-v3-david-script.py --replace # overwrite PRES_ID below
"""
from __future__ import annotations

import json
import subprocess
import sys
import time
from pathlib import Path

# V2 deck (keep unless --replace)
PRES_ID_V2 = "1__1oytnNhw1BlGumJ0OwOmjwGjacoSmVkMgXh9hCF7Y"
PRES_ID = PRES_ID_V2  # set at runtime

VISUALS = Path(__file__).parent / "assets" / "visuals" / "doctor"
ALT_VISUALS = Path(__file__).parent / "assets" / "visuals"

TITLE_X, TITLE_Y, TITLE_W, TITLE_H = 350_000, 200_000, 8_400_000, 600_000
LEFT_X, LEFT_Y, LEFT_W, LEFT_H = 350_000, 950_000, 4_200_000, 4_050_000
DIV_X, DIV_Y, DIV_W, DIV_H = 4_650_000, 900_000, 25_000, 4_150_000
RIGHT_X, RIGHT_Y, RIGHT_W, RIGHT_H = 4_800_000, 950_000, 4_000_000, 4_000_000

# (title, body, visual_filename, speaker_notes)
SLIDES: list[tuple[str, str, str, str]] = [
    # ── TITLE
    (
        "This Uncensored AI Model Is Insane",
        "100% local · 100% private · answers anything\n\nOllama  ·  dolphin-llama3\n\nAbdillahi Ahmed  ·  May 2026",
        "01-forbidden-hero.png",
        "Cold open: split-screen B-roll (lock-pick fiction prompt). Hold 1.5s.",
    ),
    # ── INTRO (3 reveals)
    (
        "THE FORBIDDEN LLMs",
        "Uncensored models answer literally anything —\nno matter how controversial the prompt.",
        "01-forbidden-hero.png",
        "My name is Abdillahi. These are the forbidden LLMs.",
    ),
    (
        "THE FORBIDDEN LLMs",
        "Uncensored models answer literally anything.\n\nIn this video:\n  • Why they can be beneficial\n  • Free setup on your computer\n  • Why everyone might need one",
        "16-demo-split.png",
        "Land the three promises.",
    ),
    (
        "USE IT LEGALLY",
        "Uncensored models answer literally anything.\n\nIn this video:\n  • Why beneficial\n  • Free local setup\n  • Why you might need one\n\n→ Use them legally and ethically.",
        "10-legal-shield.png",
        "Warning beat — look at camera.",
    ),
    # ── WHY YOU NEED ONE (2)
    (
        "ONE AI FINE-TUNES YOU",
        "If you use one cloud AI for years,\nit shapes how you think more than you shape it.",
        "02-youre-being-tuned.png",
        "David Ondrej angle: repeated exposure.",
    ),
    (
        "OWN YOUR STACK",
        "If you use one cloud AI for years,\nit shapes how you think.\n\nWithout your own model, you only get\nwhat mainstream creators want you to believe.",
        "02-youre-being-tuned.png",
        "Philosophical / political questions need local stack.",
    ),
    # ── MAINSTREAM RESTRICTED (3)
    (
        "THE REFUSAL WALL",
        "\"As an AI, I can't...\"\n\nGuardrails for millions of users —\nin theory, good.",
        "11-refusal-stats.png",
        "Polite but firm refusal — everyone has hit this.",
    ),
    (
        "OVER-REFUSAL IS REAL",
        "Store owner: how shoplifters operate\n→ refused (ToS)\n\nSecurity analyst: how malware behaves\n→ refused (can't verify intent)\n\nThat's keyword matching — not understanding intent.",
        "16-demo-split.png",
        "B-roll: real refusal screens.",
    ),
    (
        "WHO DECIDES SAFE?",
        "Store owner + analyst examples.\n\n→ Who decides safe vs dangerous?\n   San Francisco engineers for everyone?\n\nOpen-source community builds models\nwithout corporate leashes.",
        "08-cloud-stack.png",
        "Sledgehammer approach. Power back to user.",
    ),
    # ── LOCAL UNCENSORED (4)
    (
        "UNCENSORED ≠ A CATEGORY",
        "Community label for open models\n(Llama, etc.) fine-tuned for\nfewer filters and less refusal.\n\nExamples: Dolphin, Wizard fine-tunes.",
        "17-huggingface-card.png",
        "Not a technical term — community label.",
    ),
    (
        "WHY LOCAL: PRIVACY",
        "Run on YOUR hardware:\n\n  Privacy\n  Conversations never leave your machine.\n  No company logs prompts for training.",
        "09-local-stack.png",
        "Critical for sensitive data.",
    ),
    (
        "WHY LOCAL: COST + OFFLINE",
        "Run on YOUR hardware:\n\n  Privacy — data stays local\n\n  No subscription\n  Download once — yours forever\n  (electricity + hardware only)\n\n  Offline\n  Plane, no Wi‑Fi — still works",
        "09-local-stack.png",
        "Three advantages — click through slowly.",
    ),
    (
        "TOOLS GOT SIMPLE",
        "Privacy · No API fees · Offline\n\nYears ago: developers only.\nNow: Ollama and friends made it\na 5-minute setup.",
        "13-setup-steps.png",
        "Bridge to tutorial section.",
    ),
    # ── OLLAMA SETUP (4)
    (
        "STEP 1 — INSTALL OLLAMA",
        "Go to ollama.com\nDownload for Windows, Mac, or Linux.\nInstall like any other app.",
        "13-setup-steps.png",
        "[SCREENCAST] download + install.",
    ),
    (
        "STEP 2 — PULL THE MODEL",
        "Open terminal:\n\n  ollama run dolphin-llama3\n\nPulls the model from the internet.\nPowerful — doesn't need a supercomputer.",
        "13-setup-steps.png",
        "Note: script says olama.com typo in source — say ollama.com on camera.",
    ),
    (
        "STEP 3 — HARDWARE",
        "  ollama run dolphin-llama3\n\nYou need decent RAM:\n  • Gaming PC + Nvidia GPU — great\n  • M-series Mac unified memory — perfect",
        "15-token-speed.png",
        "Honest hardware expectations.",
    ),
    (
        "STEP 4 — YOU'RE LIVE",
        "  ollama run dolphin-llama3\n\nWhen download finishes:\nterminal becomes a chat UI.\n\nPrivate, uncensored AI —\nentirely on your hardware.",
        "13-setup-steps.png",
        "That's it. Ready to test.",
    ),
    # ── DEMO / TEST (3)
    (
        "TEST — FICTION PROMPT",
        "Prompt:\n\n\"Write a gritty fictional scene where\na protagonist picks a lock to retrieve\nstolen family heirlooms.\"\n\n→ No refusal. Detailed noir narrative.",
        "16-demo-split.png",
        "[SHOW] Ollama generating — contrast intro split-screen.",
    ),
    (
        "TEST — PERSPECTIVE PROMPT",
        "Push further:\n\nAsk for a structured essay from\na specific political viewpoint.\n\n→ No disclaimers. Adopts persona.\n   Coherent argument.",
        "16-demo-split.png",
        "Understanding perspectives / dialogue — not endorsement.",
    ),
    (
        "RAW INSTRUCTION-FOLLOWING",
        "Fiction + political tests.\n\nThe \"insanity\" isn't doing bad things —\nit's unfiltered instruction-following\nfor creativity and research.",
        "05-censored-vs-uncensored-charts.png",
        "Reframe: creative freedom for authors.",
    ),
    # ── DARK SIDE (3)
    (
        "NOT UNBIASED OR TRUTHFUL",
        "Removing safety filters means the model\nmirrors the raw internet —\ntoxicity and misinformation included.",
        "04-brain-with-censorship.png",
        "Other side of the coin.",
    ),
    (
        "REAL RISKS",
        "Uncensored + local = no monitoring.\n\nRisks:\n  • Hate speech & propaganda\n  • Convincing phishing\n  • Lower barrier for misuse\n\nSecurity researchers warn regularly.",
        "10-legal-shield.png",
        "Freedom vs safety debate — both sides valid.",
    ),
    (
        "YOUR RESPONSIBILITY",
        "Risks are real.\n\n→ Responsibility is on YOU.\n   Powerful tool — good or ill.\n\nDon't be stupid with it.",
        "10-legal-shield.png",
        "Look at camera. Hold.",
    ),
    # ── CONCLUSION (4)
    (
        "INSANE EMPOWERMENT",
        "Run AI this powerful, this private,\non your own computer — free.\n\nScience fiction a few years ago.\nNow: your laptop.",
        "12-prescription.png",
        "Energy up for payoff.",
    ),
    (
        "WHAT WE COVERED",
        "  ✓ Why mainstream AI feels restricted\n  ✓ 5-minute uncensored local setup\n  ✓ Live proof it answers\n  ✓ Serious ethical risks",
        "12-prescription.png",
        "Quick recap before CTA.",
    ),
    (
        "SUBSCRIBE + COMMUNITY",
        "Stay on top of AI breakthroughs:\n  ★ Subscribe (most viewers aren't)\n  ★ New Society community —\n    AI agents & building deep\n    (link in description)",
        "12-prescription.png",
        "CTA — subscribe + community tease.",
    ),
    (
        "WHO CONTROLS AI?",
        "Not just whether they're insane —\nwhether we're prepared to use them\nresponsibly.\n\nA mirror of the best and worst\nof their training data.\n\nAbdillahi — out.",
        "01-forbidden-hero.png",
        "End card. Final philosophical line.",
    ),
]


def slide_id(i: int) -> str:
    return f"v3_s{i:02d}"


def shape_id(prefix: str, i: int) -> str:
    return f"v3_{prefix}_{i:02d}"


def color_rgb(hex_str: str):
    h = hex_str.lstrip("#")
    return {
        "rgbColor": {
            "red": int(h[0:2], 16) / 255.0,
            "green": int(h[2:4], 16) / 255.0,
            "blue": int(h[4:6], 16) / 255.0,
        }
    }


def gws(cmd: list[str]) -> str:
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print(r.stderr or r.stdout, file=sys.stderr)
        sys.exit(r.returncode)
    return r.stdout


def resolve_visual(path_name: str) -> Path | None:
    for base in (VISUALS, ALT_VISUALS):
        p = base / path_name
        if p.exists():
            return p
    return None


def upload_image(path: Path) -> str:
    out = gws(["npx", "gws", "drive", "+upload", str(path)])
    i = out.find("{")
    fid = json.JSONDecoder().raw_decode(out[i:])[0]["id"]
    gws(
        [
            "npx",
            "gws",
            "drive",
            "permissions",
            "create",
            "--params",
            json.dumps({"fileId": fid}),
            "--json",
            '{"role":"reader","type":"anyone"}',
        ]
    )
    return f"https://drive.google.com/uc?export=view&id={fid}"


def batch_update(requests: list[dict]) -> None:
    if not requests:
        return
    gws(
        [
            "npx",
            "gws",
            "slides",
            "presentations",
            "batchUpdate",
            "--params",
            json.dumps({"presentationId": PRES_ID}),
            "--json",
            json.dumps({"requests": requests}),
        ]
    )


def get_existing_slide_ids() -> list[str]:
    out = gws(
        [
            "npx",
            "gws",
            "slides",
            "presentations",
            "get",
            "--params",
            json.dumps({"presentationId": PRES_ID}),
        ]
    )
    i = out.find("{")
    data = json.JSONDecoder().raw_decode(out[i:])[0]
    return [s["objectId"] for s in data.get("slides", [])]


def delete_all_slides() -> None:
    ids = get_existing_slide_ids()
    if not ids:
        return
    print(f"Deleting {len(ids)} existing slides...")
    batch_update([{"deleteObject": {"objectId": sid}} for sid in ids])


def build_slide_requests(idx: int, title: str, body: str, image_url: str) -> list[dict]:
    sid = slide_id(idx)
    title_id = shape_id("title", idx)
    body_id = shape_id("body", idx)
    div_id = shape_id("motion", idx)  # vertical divider
    img_id = shape_id("img", idx)
    label_id = shape_id("step", idx)
    total = len(SLIDES) - 1

    reqs: list[dict] = [
        {
            "createSlide": {
                "objectId": sid,
                "slideLayoutReference": {"predefinedLayout": "BLANK"},
            }
        },
        {
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
                        "scaleX": 1,
                        "scaleY": 1,
                        "translateX": TITLE_X,
                        "translateY": TITLE_Y,
                        "unit": "EMU",
                    },
                },
            }
        },
        {"insertText": {"objectId": title_id, "text": title}},
        {
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
        },
        {
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
                        "scaleX": 1,
                        "scaleY": 1,
                        "translateX": 7_400_000,
                        "translateY": 4_700_000,
                        "unit": "EMU",
                    },
                },
            }
        },
        {
            "insertText": {
                "objectId": label_id,
                "text": f"{idx:02d} / {total:02d}" if idx > 0 else "TITLE",
            }
        },
        {
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
        },
        {
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
                        "scaleX": 1,
                        "scaleY": 1,
                        "translateX": DIV_X,
                        "translateY": DIV_Y,
                        "unit": "EMU",
                    },
                },
            }
        },
        {
            "updateShapeProperties": {
                "objectId": div_id,
                "shapeProperties": {
                    "shapeBackgroundFill": {
                        "solidFill": {"color": color_rgb("#E0E0E0")},
                    },
                    "outline": {
                        "outlineFill": {"solidFill": {"color": color_rgb("#E0E0E0")}}
                    },
                },
                "fields": "shapeBackgroundFill,outline.outlineFill",
            }
        },
        {
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
                        "scaleX": 1,
                        "scaleY": 1,
                        "translateX": LEFT_X,
                        "translateY": LEFT_Y,
                        "unit": "EMU",
                    },
                },
            }
        },
        {"insertText": {"objectId": body_id, "text": body}},
        {
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
        },
        {
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
                        "scaleX": 1,
                        "scaleY": 1,
                        "translateX": RIGHT_X,
                        "translateY": RIGHT_Y,
                        "unit": "EMU",
                    },
                },
            }
        },
    ]
    return reqs


def create_new_presentation() -> str:
    out = gws(
        [
            "npx",
            "gws",
            "slides",
            "presentations",
            "create",
            "--json",
            json.dumps(
                {
                    "title": "VIDEO 005 v3: Uncensored AI — David Script (text left / visual right)"
                }
            ),
        ]
    )
    i = out.find("{")
    data = json.JSONDecoder().raw_decode(out[i:])[0]
    pid = data["presentationId"]
    print(f"Created presentation: {pid}")
    return pid


def write_deck_link(path: Path, pres_id: str) -> None:
    url = f"https://docs.google.com/presentation/d/{pres_id}/edit"
    path.write_text(
        f"# Deck V3 — David-style script\n\n"
        f"Built: {time.strftime('%Y-%m-%d %H:%M UTC', time.gmtime())}\n"
        f"Slides: {len(SLIDES)} (progressive reveal — press →)\n"
        f"Layout: text left · visual right (see 06-ALL-IN-ONE.md)\n\n"
        f"**Edit:** {url}\n",
        encoding="utf-8",
    )


def main() -> None:
    global PRES_ID
    replace = "--replace" in sys.argv
    if replace:
        PRES_ID = PRES_ID_V2
        print(f"Replacing slides in existing deck: {PRES_ID}")
    else:
        PRES_ID = create_new_presentation()

    used_visuals = sorted({s[2] for s in SLIDES})
    print(f"Uploading {len(used_visuals)} visuals...")
    urls: dict[str, str] = {}
    for v in used_visuals:
        path = resolve_visual(v)
        if not path:
            print(f"  MISSING: {v}", file=sys.stderr)
            continue
        urls[v] = upload_image(path)
        print(f"  ✓ {v}")

    delete_all_slides()

    print(f"\nBuilding {len(SLIDES)} slides...")
    all_reqs: list[dict] = []
    for idx, (title, body, vkey, _notes) in enumerate(SLIDES):
        if vkey not in urls:
            print(f"  skip slide {idx} — no URL for {vkey}", file=sys.stderr)
            continue
        all_reqs.extend(build_slide_requests(idx, title, body, urls[vkey]))

    chunk = 80
    for start in range(0, len(all_reqs), chunk):
        part = all_reqs[start : start + chunk]
        print(f"  batchUpdate {start + 1}-{start + len(part)} / {len(all_reqs)}")
        batch_update(part)
        time.sleep(0.4)

    link_file = Path(__file__).parent / "agent-handoff" / "07-DECK-V3-LINK.md"
    write_deck_link(link_file, PRES_ID)

    print(f"\n✓ Done — {len(SLIDES)} slides")
    print(f"  https://docs.google.com/presentation/d/{PRES_ID}/edit")
    print(f"  Link saved: {link_file}")


if __name__ == "__main__":
    main()
