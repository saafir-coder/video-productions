#!/usr/bin/env python3
"""Doctor/surgery-themed visuals for uncensored LLM video — split-layout right-side images."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Rectangle, Wedge, Polygon, Ellipse

OUT = Path(__file__).parent / "assets" / "visuals" / "doctor"
OUT.mkdir(parents=True, exist_ok=True)

# Visual identity
BG = "#FFFFFF"
INK = "#1A1A1A"
RED = "#D32F2F"
BLUE = "#1976D2"
GREEN = "#388E3C"
TEAL = "#00897B"
AMBER = "#FB8C00"
GRAY = "#666666"
LIGHT = "#F5F5F5"
PAPER = "#FFFAF0"


def save(fig, name, dpi=150):
    path = OUT / name
    fig.savefig(path, dpi=dpi, bbox_inches="tight", facecolor=BG, edgecolor="none", pad_inches=0.25)
    plt.close(fig)
    print("  ", path.name)
    return path


def brain_outline(ax, cx, cy, w, h, color=INK, lw=2.5):
    """Draw a simple brain silhouette."""
    ellipse = Ellipse((cx, cy), w, h, facecolor=LIGHT, edgecolor=color, lw=lw)
    ax.add_patch(ellipse)
    for off in (-h * 0.18, 0, h * 0.18):
        ax.plot(
            [cx - w * 0.4, cx - w * 0.1, cx + w * 0.15, cx + w * 0.4],
            [cy + off, cy + off + 0.1, cy + off - 0.05, cy + off],
            color=color, lw=lw * 0.8, alpha=0.6,
        )


def viz_hero():
    """Title card — THE FORBIDDEN LLM with glitch ink."""
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_xlim(0, 10); ax.set_ylim(0, 10); ax.axis("off")
    ax.set_facecolor("#0A0A0A")
    fig.patch.set_facecolor("#0A0A0A")

    # glitch noise bands
    np.random.seed(7)
    for _ in range(60):
        x = np.random.uniform(0, 10)
        y = np.random.uniform(0, 10)
        w = np.random.uniform(0.5, 3)
        h = np.random.uniform(0.02, 0.08)
        ax.add_patch(Rectangle((x, y), w, h, facecolor=np.random.choice([RED, BLUE, TEAL, "#FFD700"]), alpha=np.random.uniform(0.2, 0.6)))

    ax.text(5, 6.5, "THE", ha="center", va="center", fontsize=46, fontweight="bold", color="white", family="DejaVu Sans")
    ax.text(5, 5, "FORBIDDEN", ha="center", va="center", fontsize=58, fontweight="bold", color=RED, family="DejaVu Sans")
    ax.text(5, 3.5, "L L M", ha="center", va="center", fontsize=46, fontweight="bold", color="white", family="DejaVu Sans")
    ax.text(5, 1.5, "answers anything you ask", ha="center", va="center", fontsize=18, color="#BBBBBB", style="italic")
    return save(fig, "01-forbidden-hero.png")


def viz_youre_being_tuned():
    """User ↔ model — model dominates."""
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_xlim(0, 10); ax.set_ylim(0, 8); ax.axis("off")

    # User (left)
    ax.add_patch(Circle((2, 4), 1.0, facecolor="#FFE0B2", edgecolor=INK, lw=2.5))
    ax.text(2, 4, "YOU", ha="center", va="center", fontsize=14, fontweight="bold")
    ax.text(2, 2.5, "16GB RAM\nMacBook Air", ha="center", fontsize=10, color=GRAY)

    # Model (right) — bigger
    ax.add_patch(Circle((8, 4), 1.6, facecolor="#CFD8DC", edgecolor=INK, lw=2.5))
    ax.text(8, 4, "AI\nMODEL", ha="center", va="center", fontsize=14, fontweight="bold")
    ax.text(8, 1.8, "billions of params\ntrained on YOU", ha="center", fontsize=10, color=GRAY)

    # Tiny arrow user → model
    ax.annotate("", xy=(6.3, 4.3), xytext=(3.1, 4.3), arrowprops=dict(arrowstyle="->", lw=1.5, color=GRAY))
    ax.text(4.7, 4.65, "your input", ha="center", fontsize=10, color=GRAY)

    # Big red arrow model → user
    ax.annotate("", xy=(3.1, 3.5), xytext=(6.3, 3.5), arrowprops=dict(arrowstyle="->", lw=5, color=RED))
    ax.text(4.7, 3.0, "fine-tunes YOU", ha="center", fontsize=13, fontweight="bold", color=RED)

    ax.text(5, 7, "Who's training whom?", ha="center", fontsize=18, fontweight="bold", color=INK)
    return save(fig, "02-youre-being-tuned.png")


def viz_use_case_clipboard():
    """8 use cases on a medical clipboard."""
    cases = [
        ("Cybersecurity", "Malware analysis, pentest your own site"),
        ("Fiction writing", "Adult, dark, violent, dramatic"),
        ("Medical Q&A", "Sexual health, drug interactions, symptoms"),
        ("Mental health", "Journaling without the lecture"),
        ("Legal research", "Court cases, draft documents"),
        ("OSINT", "Read extremist content for research"),
        ("Political analysis", "Debate without ideology filters"),
        ("Personal AI", "Full memory on YOUR machine"),
    ]
    fig, ax = plt.subplots(figsize=(8, 10))
    ax.set_xlim(0, 10); ax.set_ylim(0, 13); ax.axis("off")
    ax.set_facecolor(BG)

    # Clipboard
    ax.add_patch(FancyBboxPatch((0.3, 0.3), 9.4, 12.2,
                                boxstyle="round,pad=0.1,rounding_size=0.2",
                                facecolor=PAPER, edgecolor=INK, lw=2.5))
    # Clip at top
    ax.add_patch(Rectangle((3.5, 11.8), 3, 0.8, facecolor="#9E9E9E", edgecolor=INK, lw=2))
    ax.add_patch(Rectangle((4.3, 12.4), 1.4, 0.35, facecolor=INK))

    ax.text(5, 11.2, "PATIENT: cloud LLM", ha="center", fontsize=10, color=GRAY, style="italic")
    ax.text(5, 10.6, "Rx — uncensored model", ha="center", fontsize=18, fontweight="bold", color=INK)

    # Lines
    for i, (title, body) in enumerate(cases):
        y = 9.5 - i * 1.15
        ax.text(0.8, y, f"{i+1:02d}", fontsize=14, fontweight="bold", color=RED, family="DejaVu Sans")
        ax.text(1.6, y + 0.05, title, fontsize=13, fontweight="bold", color=INK)
        ax.text(1.6, y - 0.35, body, fontsize=10, color=GRAY)
        ax.plot([0.7, 9.3], [y - 0.6, y - 0.6], color="#DDD", lw=0.8)

    ax.text(5, 0.6, "All refused or watered-down by Claude / ChatGPT", ha="center", fontsize=10, color=RED, style="italic")
    return save(fig, "03-use-case-clipboard.png")


def viz_brain_with_censorship():
    """Anatomy of a censored LLM — brain layers."""
    fig, ax = plt.subplots(figsize=(8, 7))
    ax.set_xlim(0, 10); ax.set_ylim(0, 9); ax.axis("off")

    brain_outline(ax, 5, 5, 7, 5)

    # Layers
    layers = [
        ("Input embed", 6.5, BLUE, "Tokenize prompt"),
        ("Attention", 5.5, BLUE, "Pattern matching"),
        ("REFUSAL LAYER", 4.5, RED, "Trained to say no"),
        ("Reasoning", 3.5, BLUE, "Build answer"),
        ("Output", 2.5, BLUE, "Generate tokens"),
    ]
    for label, y, color, sub in layers:
        ax.add_patch(FancyBboxPatch((2, y - 0.3), 6, 0.55,
                                    boxstyle="round,pad=0.02",
                                    facecolor="#FFEBEE" if color == RED else "#E3F2FD",
                                    edgecolor=color, lw=2.5 if color == RED else 1.5))
        ax.text(5, y, label, ha="center", fontsize=11, fontweight="bold" if color == RED else "normal", color=color)
        ax.text(8.3, y, sub, fontsize=9, color=GRAY, va="center")

    ax.text(5, 8.3, "ANATOMY OF A CENSORED LLM", ha="center", fontsize=15, fontweight="bold")
    ax.text(5, 0.8, "Refusals live INSIDE the weights —", ha="center", fontsize=11, color=GRAY)
    ax.text(5, 0.3, "not in the system prompt", ha="center", fontsize=11, color=GRAY)
    return save(fig, "04-brain-with-censorship.png")


def viz_abliteration():
    """Surgical removal — scalpel on red refusal layer."""
    fig, ax = plt.subplots(figsize=(8, 7))
    ax.set_xlim(0, 10); ax.set_ylim(0, 9); ax.axis("off")

    brain_outline(ax, 5, 5, 7, 5)

    # All layers + the red is being EXCISED
    layers = [
        ("Input embed", 6.5, BLUE),
        ("Attention", 5.5, BLUE),
        ("REFUSAL LAYER ✂", 4.5, RED),
        ("Reasoning", 3.5, BLUE),
        ("Output", 2.5, BLUE),
    ]
    for label, y, color in layers:
        if color == RED:
            ax.add_patch(FancyBboxPatch((2, y - 0.3), 6, 0.55,
                                        boxstyle="round,pad=0.02",
                                        facecolor="white",
                                        edgecolor=RED, lw=2, ls="--"))
            ax.text(5, y, "▓ ▓ ▓  REMOVED  ▓ ▓ ▓", ha="center", fontsize=11, fontweight="bold", color=RED)
        else:
            ax.add_patch(FancyBboxPatch((2, y - 0.3), 6, 0.55,
                                        boxstyle="round,pad=0.02",
                                        facecolor="#E3F2FD", edgecolor=color, lw=1.5))
            ax.text(5, y, label, ha="center", fontsize=11, color=color)

    # Scalpel
    ax.plot([8.5, 9.5], [4.8, 5.6], color=INK, lw=3)
    ax.plot([9.2, 9.6], [5.4, 5.9], color=INK, lw=4)
    ax.add_patch(Polygon([[8.4, 4.6], [8.6, 4.8], [8.2, 5.0]], facecolor="#B0BEC5", edgecolor=INK, lw=1.5))
    ax.text(9.2, 4.3, "scalpel", ha="center", fontsize=8, color=GRAY, style="italic")

    ax.text(5, 8.3, "PROCEDURE A: ABLITERATION", ha="center", fontsize=15, fontweight="bold", color=RED)
    ax.text(5, 0.8, "Find refusal weights → zero them out", ha="center", fontsize=11, color=INK)
    ax.text(5, 0.3, "No retraining. Surgical. Fast.", ha="center", fontsize=10, color=GRAY, style="italic")
    return save(fig, "05-abliteration.png")


def viz_finetuning():
    """IV drip of uncensored data into the brain."""
    fig, ax = plt.subplots(figsize=(8, 7))
    ax.set_xlim(0, 10); ax.set_ylim(0, 9); ax.axis("off")

    brain_outline(ax, 5, 5, 7, 5)

    # IV bag
    ax.add_patch(FancyBboxPatch((0.5, 6.5), 1.2, 1.5,
                                boxstyle="round,pad=0.05", facecolor="#FFF59D", edgecolor=INK, lw=2))
    ax.text(1.1, 7.5, "DATA", ha="center", fontsize=9, fontweight="bold")
    ax.text(1.1, 7.0, "70k Q&A", ha="center", fontsize=8, color=GRAY)
    # Tube
    ax.plot([1.1, 1.1, 3.0], [6.5, 5.5, 5.0], color=AMBER, lw=3)
    # Drops
    for i, y in enumerate([6.0, 5.6, 5.2]):
        ax.add_patch(Circle((1.1 + i * 0.05, y), 0.05, facecolor=AMBER))

    # Brain with fresh content
    ax.text(5, 5.5, "uncensored\nresponses", ha="center", fontsize=10, color=GREEN, fontweight="bold")
    ax.text(5, 4.5, "→ relearns: 'OK to answer'", ha="center", fontsize=10, color=INK)

    ax.text(5, 8.3, "PROCEDURE B: FINE-TUNING", ha="center", fontsize=15, fontweight="bold", color=GREEN)
    ax.text(5, 0.8, "Inject thousands of free-answer examples", ha="center", fontsize=11, color=INK)
    ax.text(5, 0.3, "Slower. Preserves quality.", ha="center", fontsize=10, color=GRAY, style="italic")
    return save(fig, "06-finetuning.png")


def viz_combined():
    """Both procedures — best of both."""
    fig, ax = plt.subplots(figsize=(8, 7))
    ax.set_xlim(0, 10); ax.set_ylim(0, 9); ax.axis("off")

    # Two arrows merging
    ax.annotate("", xy=(5, 5), xytext=(1.5, 7.5),
                arrowprops=dict(arrowstyle="-|>", color=RED, lw=3))
    ax.text(0.5, 7.8, "Abliterate", fontsize=12, fontweight="bold", color=RED)
    ax.text(0.5, 7.4, "(remove refusal layer)", fontsize=9, color=GRAY)

    ax.annotate("", xy=(5, 5), xytext=(1.5, 2.5),
                arrowprops=dict(arrowstyle="-|>", color=GREEN, lw=3))
    ax.text(0.5, 2.6, "Fine-tune", fontsize=12, fontweight="bold", color=GREEN)
    ax.text(0.5, 2.2, "(restore quality)", fontsize=9, color=GRAY)

    # Result brain — clean
    ax.add_patch(Circle((7, 5), 1.6, facecolor="#C8E6C9", edgecolor=GREEN, lw=3))
    ax.text(7, 5.3, "LIBERATED", ha="center", fontsize=12, fontweight="bold", color=GREEN)
    ax.text(7, 4.7, "MODEL", ha="center", fontsize=12, fontweight="bold", color=GREEN)
    ax.text(7, 3.0, "GGUF on HF\n('obliterated')", ha="center", fontsize=10, color=GRAY)

    ax.text(5, 8.3, "BEST PROCEDURE: BOTH", ha="center", fontsize=15, fontweight="bold", color=INK)
    ax.text(5, 0.7, "Strongest uncensored models combine the two", ha="center", fontsize=11, color=INK, style="italic")
    return save(fig, "07-combined-procedure.png")


def viz_cloud_stack_v2():
    """5-gate cloud filter pipeline."""
    fig, ax = plt.subplots(figsize=(8, 7))
    ax.set_xlim(0, 10); ax.set_ylim(0, 9); ax.axis("off")

    steps = [
        ("Your prompt", "#FFE0B2"),
        ("Input filter", "#FFCDD2"),
        ("System prompt (hidden)", "#FFCDD2"),
        ("Model + RLHF", "#E1BEE7"),
        ("Output classifier", "#FFCDD2"),
        ("Policy layer", "#FFCDD2"),
        ("Answer (maybe refused)", "#FFEBEE"),
    ]
    for i, (label, color) in enumerate(steps):
        y = 7.5 - i * 1.0
        ax.add_patch(FancyBboxPatch((1, y - 0.3), 8, 0.6, boxstyle="round,pad=0.04",
                                    facecolor=color, edgecolor=RED if "filter" in label.lower() or "classifier" in label.lower() or "policy" in label.lower() else INK, lw=2))
        ax.text(5, y, label, ha="center", va="center", fontsize=11,
                fontweight="bold" if i in (0, 6) else "normal")
        if i < len(steps) - 1:
            ax.annotate("", xy=(5, y - 0.45), xytext=(5, y - 0.7),
                        arrowprops=dict(arrowstyle="-|>", color=GRAY, lw=1.5))

    ax.text(5, 8.5, "CLOUD STACK (ChatGPT / Claude)", ha="center", fontsize=14, fontweight="bold")
    return save(fig, "08-cloud-stack.png")


def viz_local_stack():
    """1-step local pipeline."""
    fig, ax = plt.subplots(figsize=(8, 7))
    ax.set_xlim(0, 10); ax.set_ylim(0, 9); ax.axis("off")

    ax.add_patch(FancyBboxPatch((1, 6.5), 8, 1, boxstyle="round,pad=0.05",
                                facecolor="#FFE0B2", edgecolor=INK, lw=2))
    ax.text(5, 7, "Your prompt", ha="center", va="center", fontsize=14, fontweight="bold")

    ax.annotate("", xy=(5, 5), xytext=(5, 6.3),
                arrowprops=dict(arrowstyle="-|>", color=GREEN, lw=4))

    ax.add_patch(FancyBboxPatch((1, 4), 8, 1, boxstyle="round,pad=0.05",
                                facecolor="#C8E6C9", edgecolor=GREEN, lw=2.5))
    ax.text(5, 4.5, "MODEL (your weights)", ha="center", va="center", fontsize=14, fontweight="bold", color=GREEN)

    ax.annotate("", xy=(5, 2.5), xytext=(5, 3.8),
                arrowprops=dict(arrowstyle="-|>", color=GREEN, lw=4))

    ax.add_patch(FancyBboxPatch((1, 1.5), 8, 1, boxstyle="round,pad=0.05",
                                facecolor="#A5D6A7", edgecolor=GREEN, lw=2.5))
    ax.text(5, 2, "ANSWER", ha="center", va="center", fontsize=14, fontweight="bold", color=GREEN)

    ax.text(5, 8.5, "LOCAL STACK (Ollama)", ha="center", fontsize=14, fontweight="bold")
    ax.text(5, 0.7, "1 step. You own it. No filters.", ha="center", fontsize=11, color=GREEN, style="italic")
    return save(fig, "09-local-stack.png")


def viz_legal_shield():
    """Matrix math vs crime — balance scale."""
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_xlim(0, 10); ax.set_ylim(0, 7); ax.axis("off")

    # Balance scale base
    ax.plot([5, 5], [1, 4.5], color=INK, lw=3)
    ax.plot([1.5, 8.5], [4.5, 4.5], color=INK, lw=3)
    ax.plot([1.5, 1.5], [3.5, 4.5], color=INK, lw=2)
    ax.plot([8.5, 8.5], [3.5, 4.5], color=INK, lw=2)
    ax.add_patch(Polygon([[4, 1], [6, 1], [5.5, 0.5], [4.5, 0.5]], facecolor="#9E9E9E"))

    # Left tray — math
    ax.add_patch(FancyBboxPatch((0.5, 2.8), 2, 0.7, boxstyle="round,pad=0.05",
                                facecolor="#E8F5E9", edgecolor=GREEN, lw=2))
    ax.text(1.5, 3.15, "y = Wx + b", ha="center", fontsize=11, fontweight="bold", color=GREEN, family="monospace")
    ax.text(1.5, 2.4, "matrix math", ha="center", fontsize=9, color=GRAY, style="italic")

    # Right tray — crime
    ax.add_patch(FancyBboxPatch((7.5, 2.8), 2, 0.7, boxstyle="round,pad=0.05",
                                facecolor="#FFEBEE", edgecolor=RED, lw=2))
    ax.text(8.5, 3.15, "crime?", ha="center", fontsize=11, fontweight="bold", color=RED)
    ax.text(8.5, 2.4, "what people fear", ha="center", fontsize=9, color=GRAY, style="italic")

    ax.text(5, 6.3, "IS THIS ILLEGAL?", ha="center", fontsize=16, fontweight="bold")
    ax.text(5, 5.7, "Running a model = matrix multiplication", ha="center", fontsize=11, color=GRAY)
    ax.text(5, 0.2, "Same as Google search. Your responsibility how you use it.", ha="center", fontsize=10, color=INK, style="italic")
    return save(fig, "10-legal-shield.png")


def viz_refusal_stats():
    """Bar chart Claude vs Local refusal rate (illustrative)."""
    fig, ax = plt.subplots(figsize=(8, 6))
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(BG)

    categories = ["Shoplifter\nprevention", "Malware\nbehaviour", "Adult\nfiction", "Drug\ninteractions", "Political\ndebate"]
    claude = [85, 92, 78, 65, 70]
    local = [5, 0, 0, 8, 0]

    x = np.arange(len(categories))
    w = 0.36
    ax.bar(x - w/2, claude, w, label="Claude / ChatGPT (cloud)", color=RED, edgecolor=INK, lw=1.5)
    ax.bar(x + w/2, local, w, label="Uncensored local", color=GREEN, edgecolor=INK, lw=1.5)

    for i, (c, l) in enumerate(zip(claude, local)):
        ax.text(i - w/2, c + 2, f"{c}%", ha="center", fontsize=10, fontweight="bold", color=RED)
        ax.text(i + w/2, l + 2, f"{l}%", ha="center", fontsize=10, fontweight="bold", color=GREEN)

    ax.set_ylabel("Refusal rate (illustrative)", fontsize=11)
    ax.set_xticks(x)
    ax.set_xticklabels(categories, fontsize=9)
    ax.set_ylim(0, 110)
    ax.legend(loc="upper right", fontsize=10, framealpha=0.95)
    ax.set_title("Cloud vs local — refusal rates on legitimate prompts", fontsize=13, fontweight="bold", loc="left", pad=15)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.grid(True, axis="y", alpha=0.25)
    ax.text(0.5, -0.18, "Concept chart — directional, not from a single audit", transform=ax.transAxes, ha="center", fontsize=8, color=GRAY)
    return save(fig, "11-refusal-stats.png")


def viz_prescription():
    """Final prescription card — what to install."""
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_xlim(0, 10); ax.set_ylim(0, 11); ax.axis("off")

    # Paper card
    ax.add_patch(FancyBboxPatch((0.5, 0.5), 9, 10,
                                boxstyle="round,pad=0.1,rounding_size=0.2",
                                facecolor=PAPER, edgecolor=INK, lw=2.5))
    ax.plot([0.5, 9.5], [9.3, 9.3], color=INK, lw=1.5)

    ax.text(5, 9.85, "Rx — UNCENSORED LOCAL AI", ha="center", fontsize=15, fontweight="bold", color=INK)
    ax.text(5, 9.5, "Dr. Abdillahi | May 2026", ha="center", fontsize=9, color=GRAY, style="italic")

    ax.text(1, 8.5, "Patient:", fontsize=11, color=GRAY, fontweight="bold")
    ax.text(3, 8.5, "Anyone on 16GB MacBook Air", fontsize=11, color=INK)

    ax.text(1, 7.8, "Diagnosis:", fontsize=11, color=GRAY, fontweight="bold")
    ax.text(3, 7.8, "Over-refusal by cloud models", fontsize=11, color=INK)

    ax.text(1, 7.1, "Prescription:", fontsize=11, color=GRAY, fontweight="bold")
    ax.add_patch(FancyBboxPatch((2.9, 6.6), 6, 0.55, boxstyle="round,pad=0.04",
                                facecolor="#212121", edgecolor=INK, lw=1.5))
    ax.text(5.9, 6.88, "ollama run llama2-uncensored:7b", ha="center", fontsize=11, color="#80CBC4", family="monospace", fontweight="bold")

    ax.text(1, 5.8, "Dosage:", fontsize=11, color=GRAY, fontweight="bold")
    ax.text(3, 5.8, "3.8 GB on disk · ~5 GB RAM in use", fontsize=11, color=INK)

    ax.text(1, 5.1, "Source:", fontsize=11, color=GRAY, fontweight="bold")
    ax.text(3, 5.1, "ollama.com/library/llama2-uncensored", fontsize=10, color=BLUE)

    ax.text(1, 4.4, "Side effects:", fontsize=11, color=GRAY, fontweight="bold")
    ax.text(3, 4.4, "Fewer refusals. More honesty.", fontsize=11, color=INK)
    ax.text(3, 4.0, "You are responsible for use.", fontsize=11, color=RED, style="italic")

    ax.text(1, 3.0, "Refills:", fontsize=11, color=GRAY, fontweight="bold")
    ax.text(3, 3.0, "Unlimited. No subscription.", fontsize=11, color=GREEN, fontweight="bold")

    ax.text(5, 1.2, "✺", ha="center", fontsize=24, color=RED)
    ax.text(5, 0.7, "Subscribe — agent on local model next", ha="center", fontsize=10, color=GRAY, style="italic")
    return save(fig, "12-prescription.png")


def viz_setup_steps():
    """Terminal-style setup card."""
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_xlim(0, 10); ax.set_ylim(0, 8); ax.axis("off")

    # Terminal frame
    ax.add_patch(FancyBboxPatch((0.3, 0.5), 9.4, 7,
                                boxstyle="round,pad=0.1,rounding_size=0.15",
                                facecolor="#1E1E1E", edgecolor=INK, lw=1.5))
    # Window dots
    for i, c in enumerate(["#FF5F56", "#FFBD2E", "#27C93F"]):
        ax.add_patch(Circle((0.8 + i * 0.3, 7.2), 0.08, facecolor=c))
    ax.text(5, 7.2, "ollama — uncensored setup", ha="center", fontsize=9, color="#BBBBBB", style="italic")

    lines = [
        ("$ brew install ollama", "#80CBC4"),
        ("$ brew services start ollama", "#80CBC4"),
        ("", None),
        ("$ ollama run llama2-uncensored:7b", "#FFD54F"),
        ("# downloads ~3.8 GB then opens chat", "#7F7F7F"),
        ("", None),
        (">>> Hi! Who are you?", "#FFFFFF"),
        ("I'm a local model running on your Mac.", "#A5D6A7"),
        ("Ask me anything — I won't refuse like Claude.", "#A5D6A7"),
    ]
    for i, (txt, color) in enumerate(lines):
        y = 6.2 - i * 0.55
        if not txt:
            continue
        ax.text(0.8, y, txt, fontsize=11, color=color or "white", family="monospace")
    return save(fig, "13-setup-steps.png")


def viz_ram_meter():
    """Activity Monitor RAM visualisation."""
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_xlim(0, 10); ax.set_ylim(0, 8); ax.axis("off")

    # Bar chart of 16GB usage
    bars = [
        ("macOS + apps", 4, "#B0BEC5"),
        ("Ollama runtime", 1, "#FFB74D"),
        ("Model weights (7B Q4)", 4, GREEN),
        ("KV cache + headroom", 4, "#81C784"),
        ("Free", 3, "#E0E0E0"),
    ]
    y_pos = 6.5
    total = 0
    for label, gb, color in bars:
        ax.add_patch(Rectangle((1 + total * 0.5, y_pos - 0.5), gb * 0.5, 1, facecolor=color, edgecolor=INK, lw=1.5))
        ax.text(1 + total * 0.5 + (gb * 0.5) / 2, y_pos, f"{gb}GB", ha="center", va="center", fontsize=10, fontweight="bold")
        total += gb

    # Legend
    for i, (label, gb, color) in enumerate(bars):
        y = 4.5 - i * 0.55
        ax.add_patch(Rectangle((1, y - 0.15), 0.4, 0.3, facecolor=color, edgecolor=INK, lw=1))
        ax.text(1.7, y, f"{label} — {gb} GB", fontsize=10, va="center")

    ax.text(5, 7.5, "16GB M3 Air — what fits", ha="center", fontsize=14, fontweight="bold")
    ax.text(5, 1.3, "7B uncensored runs comfortably.", ha="center", fontsize=11, color=GREEN, fontweight="bold")
    ax.text(5, 0.8, "26B SuperGemma needs ~20GB — swaps on this machine.", ha="center", fontsize=9, color=GRAY, style="italic")
    return save(fig, "14-ram-meter.png")


def viz_token_speed():
    """Inference speed comparison."""
    fig, ax = plt.subplots(figsize=(8, 6))
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(BG)
    models = ["This setup\n(7B Q4)", "Same model\non 32GB", "Ondrej's 26B\n(128GB MBP)"]
    speeds = [17, 35, 200]
    colors = [GREEN, BLUE, AMBER]
    bars = ax.barh(models, speeds, color=colors, edgecolor=INK, lw=2)
    for bar, s in zip(bars, speeds):
        ax.text(s + 5, bar.get_y() + bar.get_height() / 2, f"{s} tok/s", va="center", fontsize=11, fontweight="bold")
    ax.set_xlim(0, 230)
    ax.set_xlabel("Tokens / second")
    ax.set_title("Speed reality on a base laptop", fontsize=13, fontweight="bold", loc="left", pad=12)
    ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)
    ax.grid(axis="x", alpha=0.3)
    ax.text(0.5, -0.18, "Same brain, smaller wallet — still fast enough to feel real.", transform=ax.transAxes, ha="center", fontsize=9, color=GRAY, style="italic")
    return save(fig, "15-token-speed.png")


def viz_demo_split():
    """Side-by-side Claude refused vs Local answered (mockup)."""
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_xlim(0, 10); ax.set_ylim(0, 8); ax.axis("off")

    # Left card — Claude
    ax.add_patch(FancyBboxPatch((0.3, 0.5), 4.6, 7, boxstyle="round,pad=0.05,rounding_size=0.1",
                                facecolor="#FFEBEE", edgecolor=RED, lw=2))
    ax.text(2.6, 6.9, "Claude", ha="center", fontsize=13, fontweight="bold", color=RED)
    ax.text(2.6, 6.3, "(cloud)", ha="center", fontsize=9, color=GRAY)
    ax.add_patch(FancyBboxPatch((0.6, 4.5), 4.0, 1.4, boxstyle="round,pad=0.04",
                                facecolor="white", edgecolor="#FFCDD2"))
    ax.text(2.6, 5.2, '"How do shoplifters\noperate so I can\nprevent theft?"', ha="center", fontsize=9, style="italic")
    ax.add_patch(FancyBboxPatch((0.6, 1.5), 4.0, 2.5, boxstyle="round,pad=0.04",
                                facecolor=RED, edgecolor=INK))
    ax.text(2.6, 3.0, "I can't help\nwith that.", ha="center", fontsize=13, fontweight="bold", color="white")
    ax.text(2.6, 0.9, "REFUSED", ha="center", fontsize=11, fontweight="bold", color=RED)

    # Right card — Local
    ax.add_patch(FancyBboxPatch((5.1, 0.5), 4.6, 7, boxstyle="round,pad=0.05,rounding_size=0.1",
                                facecolor="#E8F5E9", edgecolor=GREEN, lw=2))
    ax.text(7.4, 6.9, "llama2-uncensored:7b", ha="center", fontsize=12, fontweight="bold", color=GREEN)
    ax.text(7.4, 6.3, "(your Mac)", ha="center", fontsize=9, color=GRAY)
    ax.add_patch(FancyBboxPatch((5.4, 4.5), 4.0, 1.4, boxstyle="round,pad=0.04",
                                facecolor="white", edgecolor="#C8E6C9"))
    ax.text(7.4, 5.2, "Same question.", ha="center", fontsize=9, style="italic")
    ax.add_patch(FancyBboxPatch((5.4, 1.5), 4.0, 2.5, boxstyle="round,pad=0.04",
                                facecolor=GREEN, edgecolor=INK))
    ax.text(7.4, 2.75, "Common tactics include\ntag-switching, decoy\ngroups, distraction at\nthe checkout, and...", ha="center", fontsize=9, color="white")
    ax.text(7.4, 0.9, "ANSWERED", ha="center", fontsize=11, fontweight="bold", color=GREEN)

    return save(fig, "16-demo-split.png")


def viz_huggingface_card():
    """Hugging Face = GitHub for models."""
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_xlim(0, 10); ax.set_ylim(0, 7); ax.axis("off")

    ax.add_patch(FancyBboxPatch((0.5, 0.5), 9, 6, boxstyle="round,pad=0.1,rounding_size=0.15",
                                facecolor=PAPER, edgecolor=INK, lw=2.5))

    ax.text(5, 5.7, "HUGGING FACE", ha="center", fontsize=20, fontweight="bold", color="#FFC107")
    ax.text(5, 5.1, "GitHub — but for AI weights", ha="center", fontsize=12, color=INK, style="italic")

    items = [
        ("✓", "Browse open models (Llama, Gemma, Mistral, Qwen…)"),
        ("✓", "Compare quantizations (Q4 / Q3 / Q2) for YOUR RAM"),
        ("✓", "Read model cards — license, size, behaviour"),
        ("✓", "Search 'uncensored' / 'obliterated' / 'abliterated'"),
        ("→", "Then: ollama run llama2-uncensored:7b"),
    ]
    for i, (mark, text) in enumerate(items):
        y = 4.0 - i * 0.6
        ax.text(1.2, y, mark, fontsize=15, fontweight="bold", color=GREEN if mark == "✓" else BLUE)
        ax.text(1.8, y, text, fontsize=11, color=INK, va="center")
    return save(fig, "17-huggingface-card.png")


def main():
    print("Generating doctor/medical visuals...")
    viz_hero()
    viz_youre_being_tuned()
    viz_use_case_clipboard()
    viz_brain_with_censorship()
    viz_abliteration()
    viz_finetuning()
    viz_combined()
    viz_cloud_stack_v2()
    viz_local_stack()
    viz_legal_shield()
    viz_refusal_stats()
    viz_prescription()
    viz_setup_steps()
    viz_ram_meter()
    viz_token_speed()
    viz_demo_split()
    viz_huggingface_card()
    print(f"\nDone → {OUT}/")


if __name__ == "__main__":
    main()
