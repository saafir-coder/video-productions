#!/usr/bin/env python3
"""Upload diagram PNGs to Drive and insert as full-width visual slides."""
import json
import subprocess
import sys
from pathlib import Path

PRES_ID = "1__1oytnNhw1BlGumJ0OwOmjwGjacoSmVkMgXh9hCF7Y"
VISUALS = Path(__file__).parent / "assets" / "visuals"

# (file, slide_id, insertion_index, image_object_id)
# Insert visual-first BLANK slides before script sections for filming
SLIDE_PLAN = [
    ("01-forbidden-llm.png", "s_viz_forbidden", 6, "viz_img_forbidden"),
    ("03-cloud-vs-local-stack.png", "s_viz_cloud", 8, "viz_img_cloud"),
    ("04-hf-to-ollama-pipeline.png", "s_viz_hf", 10, "viz_img_hf"),
    ("02-prompt-to-llm-diagram.png", "s_viz_prompt", 12, "viz_img_prompt"),
    ("05-censored-vs-uncensored-charts.png", "s_viz_charts", 14, "viz_img_charts"),
    ("06-ram-tier-decision.png", "s_viz_ram", 16, "viz_img_ram"),
]

# Full-bleed-ish placement on 16:9 slide (EMU)
IMG_X, IMG_Y = 200000, 150000
IMG_W, IMG_H = 8700000, 4800000


def drive_url(file_id: str) -> str:
    return f"https://drive.google.com/uc?export=view&id={file_id}"


def upload_and_share(path: Path) -> str:
    r = subprocess.run(
        ["npx", "gws", "drive", "+upload", str(path)],
        capture_output=True,
        text=True,
    )
    raw = r.stdout + r.stderr
    i = raw.find("{")
    if r.returncode != 0 or i < 0:
        raise RuntimeError(f"Upload failed for {path}: {raw}")
    # gws may print prefix lines before JSON
    decoder = json.JSONDecoder()
    data, _ = decoder.raw_decode(raw[i:])
    fid = data["id"]
    subprocess.run(
        [
            "npx", "gws", "drive", "permissions", "create",
            "--params", json.dumps({"fileId": fid}),
            "--json", '{"role": "reader", "type": "anyone"}',
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    return drive_url(fid)


def img_req(oid, url, page):
    return {
        "createImage": {
            "objectId": oid,
            "url": url,
            "elementProperties": {
                "pageObjectId": page,
                "size": {
                    "width": {"magnitude": IMG_W, "unit": "EMU"},
                    "height": {"magnitude": IMG_H, "unit": "EMU"},
                },
                "transform": {
                    "scaleX": 1,
                    "scaleY": 1,
                    "translateX": IMG_X,
                    "translateY": IMG_Y,
                    "unit": "EMU",
                },
            },
        }
    }


def main():
    reqs = []
    urls = {}

    print("Uploading visuals to Drive...")
    for fname, sid, _, ioid in SLIDE_PLAN:
        path = VISUALS / fname
        if not path.exists():
            print(f"  skip missing {path}", file=sys.stderr)
            continue
        urls[fname] = upload_and_share(path)
        print(f"  {fname} → {urls[fname][:60]}...")

    for fname, sid, idx, ioid in SLIDE_PLAN:
        if fname not in urls:
            continue
        reqs.append({
            "createSlide": {
                "objectId": sid,
                "insertionIndex": idx,
                "slideLayoutReference": {"predefinedLayout": "BLANK"},
            }
        })
        reqs.append(img_req(ioid, urls[fname], sid))

    # Also overlay key diagrams on existing script slides (right column)
    overlays = [
        ("01-forbidden-llm.png", "s_hook", "ov_hook", 4800000, 400000, 4000000, 2200000),
        ("05-censored-vs-uncensored-charts.png", "s_act2", "ov_act2", 3500000, 300000, 5200000, 3000000),
        ("06-ram-tier-decision.png", "s_act3", "ov_act3", 3800000, 400000, 5000000, 2800000),
    ]
    for fname, page, oid, x, y, w, h in overlays:
        if fname not in urls:
            continue
        reqs.append({
            "createImage": {
                "objectId": oid,
                "url": urls[fname],
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
        })

    if not reqs:
        sys.exit("No requests built")

    payload = {"requests": reqs}
    print(f"\nPushing {len(reqs)} Slides API requests...")
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
    print(f"Done: https://docs.google.com/presentation/d/{PRES_ID}/edit")


if __name__ == "__main__":
    main()
