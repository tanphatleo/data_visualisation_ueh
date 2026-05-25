"""
make_scripts_2.py
Generates a 3-panel bar chart comparison image:
  Single series | Two series | Multiple series
Output: images/chart_bar_variants.png
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# ── Colour palette ──────────────────────────────────────────────────────────
NAVY     = '#0D1A63'
NAVY_1   = '#253A95'
NAVY_2   = '#5B73C4'
NAVY_3   = '#A8B4DE'
NAVY_4   = '#DDE2F2'
ORANGE   = '#F68048'
BLACK    = '#111111'
WHITE    = '#FFFFFF'
GRAY     = '#7e7e7e'
LINE     = '#E8E8EE'

# ── Data ────────────────────────────────────────────────────────────────────
categories = ['Cat 1', 'Cat 2', 'Cat 3', 'Cat 4', 'Cat 5']
A = [4, 5, 3, 4, 7]
B = [6, 4, 5, 3, 6]
C = [5, 6, 4, 6, 4]
x = np.arange(len(categories))

# ── Shared axis styling ──────────────────────────────────────────────────────
def style_ax(ax):
    ax.set_ylim(0, 8)
    ax.set_yticks(range(0, 9))
    ax.set_xticks(x)
    ax.set_xticklabels(categories, fontsize=8.5, color=GRAY)
    ax.tick_params(axis='y', colors=GRAY, labelsize=8.5)
    ax.tick_params(axis='both', length=0)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color(LINE)
    ax.spines['bottom'].set_color(LINE)
    ax.yaxis.grid(True, color=LINE, linewidth=0.6, zorder=0)
    ax.set_axisbelow(True)
    ax.set_facecolor(WHITE)


def add_label(ax, bar, text, color):
    """Place a bold letter label just above a bar."""
    bx = bar.get_x() + bar.get_width() / 2
    by = bar.get_height()
    ax.text(bx, by + 0.25, text,
            ha='center', va='bottom',
            fontsize=9, fontweight='bold', color=color)


# ── Figure ───────────────────────────────────────────────────────────────────
fig, axes = plt.subplots(1, 3, figsize=(13, 4))
fig.patch.set_facecolor(WHITE)

# ── Panel 1: Single series ───────────────────────────────────────────────────
ax1 = axes[0]
ax1.bar(x, A, width=0.5, color=NAVY, zorder=3)
ax1.set_title('Single series', fontsize=11, fontweight='bold',
              color=BLACK, pad=10, loc='left')
style_ax(ax1)

# ── Panel 2: Two series ──────────────────────────────────────────────────────
ax2 = axes[1]
w2 = 0.35
bars_a2 = ax2.bar(x - w2 / 2, A, width=w2, color=NAVY,   zorder=3, label='Series A')
bars_b2 = ax2.bar(x + w2 / 2, B, width=w2, color=NAVY_2, zorder=3, label='Series B')
ax2.set_title('Two series', fontsize=11, fontweight='bold',
              color=BLACK, pad=10, loc='left')
style_ax(ax2)
# Callout labels on Cat 2 bars
add_label(ax2, bars_a2[1], 'A', NAVY)
add_label(ax2, bars_b2[1], 'B', NAVY_2)

# ── Panel 3: Multiple series ──────────────────────────────────────────────────
ax3 = axes[2]
w3 = 0.24
bars_a3 = ax3.bar(x - w3,   A, width=w3, color=NAVY,   zorder=3, label='Series A')
bars_b3 = ax3.bar(x,         B, width=w3, color=NAVY_2, zorder=3, label='Series B')
bars_c3 = ax3.bar(x + w3,   C, width=w3, color=NAVY_3, zorder=3, label='Series C')
ax3.set_title('Multiple series', fontsize=11, fontweight='bold',
              color=BLACK, pad=10, loc='left')
style_ax(ax3)
# Callout labels on Cat 2 bars
add_label(ax3, bars_a3[1], 'A', NAVY)
add_label(ax3, bars_b3[1], 'B', NAVY_2)

# ── Export ───────────────────────────────────────────────────────────────────
plt.tight_layout(w_pad=3)
out = 'images/chart_bar_variants.png'
plt.savefig(out, dpi=150, bbox_inches='tight', facecolor=WHITE)
print(f'Saved: {out}')
plt.show()
