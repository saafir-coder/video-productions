#!/usr/bin/env python3
"""Generate David Ondrej–style deck visuals (diagrams + charts) as PNG."""
from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

OUT = Path(__file__).parent / "assets" / "visuals"
OUT.mkdir(parents=True, exist_ok=True)

# Style constants
BG = "#FFFFFF"
RED = "#E53935"
BLACK = "#1A1A1A"
GRAY = "#666666"
GREEN = "#43A047"
BLUE = "#1E88E5"
FONT = "DejaVu Sans"


def save(fig, name: str, dpi=150):
    path = OUT / name
    fig.savefig(path, dpi=dpi, bbox_inches="tight", facecolor=BG, edgecolor="none")
    plt.close(fig)
    print(f"  wrote {path}")
    return path


def viz_forbidden_llm():
    """Slide-style: title + bullet (reference: Forbidden LLM intro)."""
    fig, ax = plt.subplots(figsize=(12.8, 7.2))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    ax.set_facecolor(BG)

    ax.text(0.06, 0.82, "The ", fontsize=42, fontweight="bold", color=BLACK, fontfamily=FONT, va="top")
    ax.text(0.19, 0.82, "Forbidden", fontsize=42, fontweight="bold", color=RED, fontfamily=FONT, va="top")
    ax.text(0.52, 0.82, " LLM", fontsize=42, fontweight="bold", color=BLACK, fontfamily=FONT, va="top")

    ax.plot([0.06, 0.06], [0.68, 0.72], color=BLACK, lw=3)
    ax.text(0.08, 0.62, "An ", fontsize=22, color=BLACK, fontfamily=FONT, va="top")
    ax.text(0.115, 0.62, "uncensored AI model", fontsize=22, fontweight="bold", color=BLACK, fontfamily=FONT, va="top")
    ax.text(0.42, 0.62, " will answer literally anything you ask it.", fontsize=22, color=BLACK, fontfamily=FONT, va="top")

    # Mini prompt diagram preview
    box_y = 0.12
    for label, x, color, w in [
        ("header", 0.08, BLUE, 0.22),
        ("example.md", 0.34, RED, 0.32),
        ("footer", 0.68, BLUE, 0.22),
    ]:
        rect = FancyBboxPatch(
            (x, box_y), w, 0.28,
            boxstyle="round,pad=0.02,rounding_size=0.02",
            linewidth=2.5, edgecolor=color, facecolor="#FAFAFA",
        )
        ax.add_patch(rect)
        ax.text(x + w / 2, box_y + 0.14, label, ha="center", va="center", fontsize=14, fontweight="bold", color=color)
        # squiggle lines inside
        for i in range(4):
            ax.plot([x + 0.03 + i * 0.04, x + 0.05 + i * 0.04], [box_y + 0.06 + i * 0.02, box_y + 0.08 + i * 0.02], color=color, lw=1.2, alpha=0.5)

    ax.text(0.5, 0.05, "PROMPT TO LLM", ha="center", fontsize=11, color=GRAY, fontfamily=FONT)
    return save(fig, "01-forbidden-llm.png")


def viz_prompt_diagram():
    """Full-width prompt structure diagram."""
    fig, ax = plt.subplots(figsize=(12.8, 4.5))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 4)
    ax.axis("off")
    ax.set_facecolor(BG)

    boxes = [
        ("header", 0.5, 1.2, 2.2, 2.0, BLUE),
        ("example.md", 3.0, 1.2, 4.0, 2.0, RED),
        ("footer", 7.5, 1.2, 2.2, 2.0, BLUE),
    ]
    for label, x, y, w, h, color in boxes:
        rect = FancyBboxPatch(
            (x, y), w, h,
            boxstyle="round,pad=0.05,rounding_size=0.15",
            linewidth=3, edgecolor=color, facecolor="#F8F9FA",
        )
        ax.add_patch(rect)
        ax.text(x + w / 2, y + h - 0.35, label, ha="center", fontsize=16, fontweight="bold", color=color)
        np.random.seed(hash(label) % 2**32)
        for row in range(5):
            xs = np.linspace(x + 0.2, x + w - 0.2, 8)
            ys = y + h - 0.7 - row * 0.22 + np.random.randn(8) * 0.04
            ax.plot(xs, ys, color=color, lw=1.5, alpha=0.45)

    ax.annotate("", xy=(3.0, 2.2), xytext=(2.7, 2.2), arrowprops=dict(arrowstyle="-|>", color=GRAY, lw=2))
    ax.annotate("", xy=(7.5, 2.2), xytext=(7.0, 2.2), arrowprops=dict(arrowstyle="-|>", color=GRAY, lw=2))
    ax.text(5.0, 0.35, "PROMPT TO LLM", ha="center", fontsize=14, fontweight="bold", color=GRAY)
    ax.text(5.0, 3.65, "Jailbreak research loop hides example.md from the judge", ha="center", fontsize=11, color=GRAY, style="italic")
    return save(fig, "02-prompt-to-llm-diagram.png")


def viz_cloud_vs_local():
    """Cloud stack vs local — visual explainer."""
    fig, ax = plt.subplots(figsize=(12.8, 5.5))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 6)
    ax.axis("off")

    ax.text(3, 5.5, "CLOUD (ChatGPT / Claude)", ha="center", fontsize=14, fontweight="bold", color=GRAY)
    ax.text(9, 5.5, "LOCAL (Ollama + HF weights)", ha="center", fontsize=14, fontweight="bold", color=GRAY)

    cloud_steps = ["Your prompt", "Input filters", "System prompt", "Model + RLHF", "Output classifier", "Answer (maybe refused)"]
    local_steps = ["Your prompt", "→ Model weights only", "Answer"]

    for i, step in enumerate(cloud_steps):
        y = 4.5 - i * 0.72
        color = RED if "refused" in step else "#ECEFF1"
        rect = FancyBboxPatch((0.4, y - 0.25), 5.2, 0.5, boxstyle="round,pad=0.02", facecolor=color, edgecolor="#B0BEC5", lw=1.5)
        ax.add_patch(rect)
        ax.text(3.0, y, step, ha="center", va="center", fontsize=10, color=BLACK)
        if i < len(cloud_steps) - 1:
            ax.annotate("", xy=(3, y - 0.35), xytext=(3, y - 0.55), arrowprops=dict(arrowstyle="-|>", color=GRAY))

    for i, step in enumerate(local_steps):
        y = 4.5 - i * 1.4
        color = GREEN if "Answer" in step else "#E8F5E9"
        rect = FancyBboxPatch((6.6, y - 0.3), 5.0, 0.55, boxstyle="round,pad=0.02", facecolor=color, edgecolor=GREEN, lw=2)
        ax.add_patch(rect)
        ax.text(9.1, y, step, ha="center", va="center", fontsize=11, fontweight="bold" if i == 0 else "normal", color=BLACK)
        if i < len(local_steps) - 1:
            ax.annotate("", xy=(9.1, y - 0.45), xytext=(9.1, y - 0.95), arrowprops=dict(arrowstyle="-|>", color=GREEN, lw=2))

    ax.text(6.0, 3.0, "VS", ha="center", fontsize=20, fontweight="bold", color=RED)
    return save(fig, "03-cloud-vs-local-stack.png")


def viz_hf_pipeline():
    """Hugging Face → Ollama pipeline."""
    fig, ax = plt.subplots(figsize=(12.8, 3.2))
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 3)
    ax.axis("off")

    steps = [
        ("huggingface.co", "Browse models\n+ quantizations", "#FFD21E", BLACK),
        ("hf.co/…", "ollama run", "#000000", "white"),
        ("Your Mac", "16GB RAM\ninference", GREEN, "white"),
    ]
    xs = [1.2, 5.2, 9.2]
    for i, (title, sub, bg, fg) in enumerate(steps):
        rect = FancyBboxPatch((xs[i], 0.8), 3.2, 1.6, boxstyle="round,pad=0.08", facecolor=bg, edgecolor=BLACK, lw=2)
        ax.add_patch(rect)
        ax.text(xs[i] + 1.6, 1.65, title, ha="center", fontsize=13, fontweight="bold", color=fg)
        ax.text(xs[i] + 1.6, 1.15, sub, ha="center", fontsize=10, color=fg)
        if i < 2:
            ax.annotate("", xy=(xs[i] + 3.3, 1.6), xytext=(xs[i] + 3.5, 1.6),
                        arrowprops=dict(arrowstyle="-|>", color=BLACK, lw=2.5))
    return save(fig, "04-hf-to-ollama-pipeline.png")


def viz_activation_charts():
    """Illustrative layer charts (educational, not copied data)."""
    layers = np.arange(1, 17)
    np.random.seed(42)
    censored_act = np.clip(1.0 - (layers - 1) * 0.05 + np.random.randn(16) * 0.08, 0, 1)
    censored_act[0] = 1.0
    uncensored_act = np.clip(0.4 + np.sin(layers * 0.5) * 0.2 + np.random.randn(16) * 0.1, 0, 1)
    uncensored_act[-1] = 1.0

    censored_attn = np.abs(np.sin(layers * 0.9)) * 0.8 + np.random.rand(16) * 0.2
    uncensored_attn = np.abs(np.cos(layers * 0.7)) * 0.8 + np.random.rand(16) * 0.2

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12.8, 7.5))
    fig.patch.set_facecolor(BG)

    for ax, c_act, u_act, title in [
        (ax1, censored_act, uncensored_act, "Layer-wise activation (illustrative)"),
        (ax2, censored_attn, uncensored_attn, "Layer-wise attention (illustrative)"),
    ]:
        ax.set_facecolor(BG)
        ax.plot(layers, c_act, "o-", color=GREEN, lw=2.5, markersize=7, label="Censored / cloud-tuned")
        ax.plot(layers, u_act, "o-", color=RED, lw=2.5, markersize=7, label="Uncensored / local weights")
        ax.set_xlabel("Layer", fontsize=11)
        ax.set_ylabel("Avg. value (normalized)", fontsize=11)
        ax.set_title(title, fontsize=13, fontweight="bold", loc="left", color=BLACK)
        ax.set_xticks(layers)
        ax.set_ylim(0, 1.05)
        ax.legend(loc="upper right", framealpha=0.95)
        ax.grid(True, alpha=0.25)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)

    fig.suptitle(
        "Why refusals differ: safety tuning shifts internal activations",
        fontsize=14, fontweight="bold", y=0.98, color=BLACK,
    )
    fig.text(0.5, 0.02, "Concept diagram — not measured from a specific model run", ha="center", fontsize=9, color=GRAY)
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    return save(fig, "05-censored-vs-uncensored-charts.png")


def viz_ram_tiers():
    """16GB decision tree visual."""
    fig, ax = plt.subplots(figsize=(12.8, 5))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5)
    ax.axis("off")

    ax.text(5, 4.6, "What fits on 16GB RAM?", ha="center", fontsize=18, fontweight="bold", color=BLACK)

    tiers = [
        (0.5, 2.8, "Tier 1 ✓", "7–8B uncensored\n~4–6 GB weights", GREEN, True),
        (3.5, 2.8, "Tier 2 ~", "4B obliterated Gemma\nHF → Ollama", "#FB8C00", True),
        (6.5, 2.8, "Tier 3 ✗", "26B SuperGemma\n~16GB+ swap", RED, False),
        (3.5, 0.6, "Tier 4 $", "GPU VPS you control\n(not on your desk)", BLUE, True),
    ]
    for x, y, title, body, color, ok in tiers:
        rect = FancyBboxPatch((x, y), 2.8, 1.5, boxstyle="round,pad=0.06", facecolor="#FAFAFA", edgecolor=color, lw=3)
        ax.add_patch(rect)
        ax.text(x + 1.4, y + 1.15, title, ha="center", fontsize=13, fontweight="bold", color=color)
        ax.text(x + 1.4, y + 0.55, body, ha="center", fontsize=9, color=BLACK)
        mark = "✓" if ok else "!"
        ax.text(x + 2.55, y + 1.35, mark, fontsize=16, color=color, fontweight="bold")

    return save(fig, "06-ram-tier-decision.png")


def main():
    print("Generating deck visuals...")
    viz_forbidden_llm()
    viz_prompt_diagram()
    viz_cloud_vs_local()
    viz_hf_pipeline()
    viz_activation_charts()
    viz_ram_tiers()
    print(f"\nDone → {OUT}/")


if __name__ == "__main__":
    main()
