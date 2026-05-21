import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns
from scipy.stats import gaussian_kde
from mpl_toolkits.mplot3d import Axes3D

os.makedirs("images", exist_ok=True)
np.random.seed(42)

plt.rcParams.update({
    "figure.facecolor": "white",
    "axes.facecolor": "#f5f5f5",
    "axes.grid": True,
    "grid.alpha": 0.4,
    "font.family": "DejaVu Sans",
})

# ── 1. Line Chart ────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(7, 4))
months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
revenue = [42, 55, 48, 62, 78, 85, 92, 88, 95, 102, 98, 115]
net_income = [8, 12, 9, 15, 22, 26, 30, 27, 32, 38, 35, 44]
ax.plot(months, revenue, marker="o", color="#1565C0", lw=2, label="Revenue")
ax.plot(months, net_income, marker="s", color="#E53935", lw=2, label="Net Income")
ax.set_title("Line Chart — Revenue vs Net Income", fontweight="bold")
ax.set_ylabel("USD (thousands)")
ax.legend()
plt.tight_layout()
plt.savefig("images/line_chart.png", dpi=110, bbox_inches="tight")
plt.close()

# ── 2. Candlestick Chart ─────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(7, 4))
ax.set_facecolor("#1a1a2e")
fig.patch.set_facecolor("#1a1a2e")
opens  = [100,102, 98,105,103,107,110,108,112,109,115,112,118,116,120]
closes = [102, 98,105,103,107,110,108,112,109,115,112,118,116,120,123]
highs  = [104,103,107,106,109,112,111,114,113,117,116,120,119,122,125]
lows   = [ 99, 96, 97,101,102,106,107,107,108,108,110,111,115,115,119]
for i in range(len(opens)):
    color = "#26a69a" if closes[i] >= opens[i] else "#ef5350"
    ax.plot([i,i], [lows[i],highs[i]], color=color, lw=1.5)
    rect = plt.Rectangle((i-0.35, min(opens[i],closes[i])),
                          0.7, abs(closes[i]-opens[i]), color=color, zorder=3)
    ax.add_patch(rect)
ax.set_title("Candlestick Chart — Stock Price OHLC", fontweight="bold", color="white")
ax.set_xlabel("Trading Day", color="white")
ax.set_ylabel("Price (USD)", color="white")
ax.tick_params(colors="white")
for spine in ax.spines.values():
    spine.set_edgecolor("#444")
ax.set_facecolor("#1a1a2e")
ax.grid(color="#333", alpha=0.5)
plt.tight_layout()
plt.savefig("images/candlestick_chart.png", dpi=110, bbox_inches="tight")
plt.close()

# ── 3. Waterfall Chart ───────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(8, 4))
labels_wf = ["Revenue","COGS","Gross\nProfit","OpEx","EBIT"]
values_wf = [500, -200, None, -100, None]
bar_values = [500, 200, 300, 100, 200]
bottoms_wf = [0, 300, 0, 200, 0]
colors_wf  = ["#1565C0","#E53935","#2E7D32","#E53935","#2E7D32"]
for i,(lbl,val,bot,col) in enumerate(zip(labels_wf,bar_values,bottoms_wf,colors_wf)):
    ax.bar(i, val, bottom=bot, color=col, width=0.6, edgecolor="white", lw=1.2)
    ax.text(i, bot+val+3, f"${val}k", ha="center", fontsize=9, fontweight="bold")
    if i < 4:
        ax.plot([i+0.3, i+0.7],[bot+val, bot+val], color="#555", lw=1, ls="--")
ax.set_xticks(range(5))
ax.set_xticklabels(labels_wf)
ax.set_title("Waterfall Chart — P&L Bridge", fontweight="bold")
ax.set_ylabel("USD (thousands)")
ax.set_ylim(0, 560)
plt.tight_layout()
plt.savefig("images/waterfall_chart.png", dpi=110, bbox_inches="tight")
plt.close()

# ── 4. Bar / Column Chart ────────────────────────────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(10, 4))
products = ["Product A","Product B","Product C","Product D","Product E"]
q1 = [120, 85, 200, 110, 160]
q2 = [150, 95, 220, 130, 180]
x = np.arange(5)
axes[0].bar(x-0.2, q1, 0.4, label="Q1", color="#1565C0", alpha=0.85)
axes[0].bar(x+0.2, q2, 0.4, label="Q2", color="#E53935", alpha=0.85)
axes[0].set_xticks(x); axes[0].set_xticklabels(products, rotation=15)
axes[0].set_title("Grouped Bar — Sales by Product", fontweight="bold")
axes[0].legend()
axes[1].bar(x, q1, 0.6, label="Q1", color="#1565C0", alpha=0.85)
axes[1].bar(x, q2, 0.6, bottom=q1, label="Q2", color="#E53935", alpha=0.85)
axes[1].set_xticks(x); axes[1].set_xticklabels(products, rotation=15)
axes[1].set_title("Stacked Bar — Sales by Product", fontweight="bold")
axes[1].legend()
plt.suptitle("Bar / Column Charts", fontweight="bold", fontsize=12)
plt.tight_layout()
plt.savefig("images/bar_chart.png", dpi=110, bbox_inches="tight")
plt.close()

# ── 5. Treemap ───────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(7, 4.5))
ax.set_facecolor("white")
rects = [
    (0,    0,    0.50, 0.58, "#1565C0", "Technology\n35%"),
    (0.50, 0,    0.50, 0.40, "#2E7D32", "Financials\n25%"),
    (0,    0.58, 0.34, 0.42, "#E65100", "Healthcare\n15%"),
    (0.34, 0.58, 0.30, 0.42, "#6A1B9A", "Energy\n12%"),
    (0.64, 0.40, 0.36, 0.60, "#00695C", "Consumer\n13%"),
]
for (x, y, w, h, c, lbl) in rects:
    ax.add_patch(mpatches.Rectangle((x+0.005,y+0.005), w-0.01, h-0.01,
                                     color=c, alpha=0.88))
    ax.text(x+w/2, y+h/2, lbl, ha="center", va="center",
            color="white", fontsize=10, fontweight="bold", linespacing=1.6)
ax.set_xlim(0,1); ax.set_ylim(0,1); ax.axis("off")
ax.set_title("Treemap — Portfolio Allocation by Sector", fontweight="bold")
plt.tight_layout()
plt.savefig("images/treemap.png", dpi=110, bbox_inches="tight")
plt.close()

# ── 6. Heatmap ───────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(6, 5))
metrics = ["Revenue","Cost","Margin","Volume","Price","Growth"]
corr = np.array([
    [ 1.00, -0.65,  0.80,  0.72,  0.45,  0.60],
    [-0.65,  1.00, -0.70, -0.55, -0.30, -0.50],
    [ 0.80, -0.70,  1.00,  0.60,  0.50,  0.65],
    [ 0.72, -0.55,  0.60,  1.00,  0.35,  0.55],
    [ 0.45, -0.30,  0.50,  0.35,  1.00,  0.40],
    [ 0.60, -0.50,  0.65,  0.55,  0.40,  1.00],
])
sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", center=0,
            xticklabels=metrics, yticklabels=metrics, ax=ax,
            linewidths=0.5, linecolor="white")
ax.set_title("Heatmap — Correlation Matrix", fontweight="bold")
plt.tight_layout()
plt.savefig("images/heatmap.png", dpi=110, bbox_inches="tight")
plt.close()

# ── 7. Bullet Chart ──────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(8, 2.8))
ax.set_facecolor("white")
ax.barh(0, 100, height=0.55, color="#FFCDD2", label="Poor (<50%)")
ax.barh(0, 75,  height=0.55, color="#FFECB3", label="Fair (50-75%)")
ax.barh(0, 50,  height=0.55, color="#C8E6C9", label="Good (≤50%)")
ax.barh(0, 68,  height=0.3,  color="#1565C0", label="Actual: 68%")
ax.plot([80,80], [-0.38, 0.38], color="#212121", lw=3.5, zorder=5)
ax.text(80, 0.45, "Target\n80%", ha="center", fontsize=8.5, fontweight="bold")
ax.text(68, -0.48, "Actual: 68%", ha="center", fontsize=8.5, color="#1565C0", fontweight="bold")
ax.set_xlim(0, 110); ax.set_yticks([])
ax.set_xlabel("Revenue (% of Plan)")
ax.set_title("Bullet Chart — Revenue vs Target", fontweight="bold")
ax.legend(loc="upper right", fontsize=8)
plt.tight_layout()
plt.savefig("images/bullet_chart.png", dpi=110, bbox_inches="tight")
plt.close()

# ── 8. Sankey Diagram (simplified arrow flow) ────────────────────────────────
fig, ax = plt.subplots(figsize=(8, 4.5))
ax.set_facecolor("white"); ax.axis("off")
flows = [
    (0.05, 0.5, 0.30, 0.7, 0.25, "#1565C0", "Revenue\n$500k"),
    (0.05, 0.5, 0.30, 0.3, 0.10, "#1565C0", ""),
    (0.35, 0.7, 0.60, 0.8, 0.15, "#E53935", "COGS\n$200k"),
    (0.35, 0.3, 0.60, 0.2, 0.10, "#FF9800", "OpEx\n$100k"),
    (0.65, 0.8, 0.90, 0.9, 0.08, "#E53935", ""),
    (0.65, 0.2, 0.90, 0.1, 0.07, "#FF9800", ""),
]
nodes = [
    (0.02, 0.35, 0.06, 0.30, "#1565C0", "Revenue\n$500k"),
    (0.32, 0.62, 0.06, 0.16, "#2E7D32", "Gross Profit\n$300k"),
    (0.62, 0.72, 0.06, 0.12, "#E53935", "COGS\n$200k"),
    (0.62, 0.12, 0.06, 0.10, "#FF9800", "OpEx\n$100k"),
    (0.88, 0.54, 0.06, 0.14, "#2E7D32", "EBIT\n$200k"),
]
arrow_data = [
    (0.08, 0.50, 0.32, 0.70, 0.22, "#1565C0"),
    (0.08, 0.50, 0.32, 0.30, 0.10, "#1565C0"),
    (0.38, 0.70, 0.62, 0.78, 0.12, "#E53935"),
    (0.38, 0.30, 0.62, 0.17, 0.10, "#FF9800"),
    (0.68, 0.78, 0.88, 0.61, 0.09, "#E53935"),
    (0.68, 0.17, 0.88, 0.54, 0.08, "#FF9800"),
]
for (x1,y1,x2,y2,h,c) in arrow_data:
    ax.annotate("", xy=(x2,y2), xytext=(x1,y1),
                arrowprops=dict(arrowstyle=f"->,head_width={h*1.5}",
                                color=c, lw=h*30, connectionstyle="arc3,rad=0.05"),
                xycoords="axes fraction", textcoords="axes fraction")
for (x,y,w,h,c,lbl) in nodes:
    ax.add_patch(mpatches.FancyBboxPatch((x,y),w,h, boxstyle="round,pad=0.01",
                                          color=c, alpha=0.85, transform=ax.transAxes,
                                          clip_on=False))
    ax.text(x+w/2, y+h/2, lbl, ha="center", va="center", color="white",
            fontsize=8, fontweight="bold", transform=ax.transAxes, clip_on=False)
ax.set_title("Sankey Diagram — Revenue Flow", fontweight="bold")
plt.tight_layout()
plt.savefig("images/sankey_diagram.png", dpi=110, bbox_inches="tight")
plt.close()

# ── 9. Radar / Spider Chart ──────────────────────────────────────────────────
cats = ["Liquidity","Profitability","Leverage","Efficiency","Growth","Solvency"]
N = len(cats)
angles = np.linspace(0, 2*np.pi, N, endpoint=False).tolist()
angles += angles[:1]
v1 = [0.8, 0.65, 0.4, 0.72, 0.88, 0.60]; v1 += v1[:1]
v2 = [0.5, 0.75, 0.65, 0.50, 0.42, 0.80]; v2 += v2[:1]
fig, ax = plt.subplots(figsize=(5.5, 5.5), subplot_kw=dict(polar=True))
ax.set_facecolor("#f5f5f5")
ax.plot(angles, v1, "o-", lw=2, color="#1565C0", label="Company A")
ax.fill(angles, v1, alpha=0.20, color="#1565C0")
ax.plot(angles, v2, "s-", lw=2, color="#E53935", label="Company B")
ax.fill(angles, v2, alpha=0.20, color="#E53935")
ax.set_xticks(angles[:-1]); ax.set_xticklabels(cats, fontsize=9)
ax.set_ylim(0, 1); ax.set_yticks([0.25,0.5,0.75,1.0])
ax.set_yticklabels(["25%","50%","75%","100%"], fontsize=7)
ax.set_title("Radar Chart — Financial KPI Comparison", fontweight="bold", pad=20)
ax.legend(loc="upper right", bbox_to_anchor=(1.35, 1.15))
plt.tight_layout()
plt.savefig("images/radar_chart.png", dpi=110, bbox_inches="tight")
plt.close()

# ── 10. Pie / Donut Chart ────────────────────────────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(9, 4))
labels_p = ["Organic\nSearch","Paid Search","Direct","Social","Email"]
sizes_p  = [32, 25, 20, 15, 8]
colors_p = ["#1565C0","#E53935","#2E7D32","#FF9800","#6A1B9A"]
axes[0].pie(sizes_p, labels=labels_p, colors=colors_p, autopct="%1.0f%%",
            startangle=140, pctdistance=0.75,
            wedgeprops=dict(edgecolor="white", linewidth=1.5))
axes[0].set_title("Pie Chart — Traffic Sources", fontweight="bold")
axes[1].pie(sizes_p, colors=colors_p, autopct="%1.0f%%", startangle=140,
            pctdistance=0.82, wedgeprops=dict(width=0.52, edgecolor="white", linewidth=1.5))
axes[1].text(0, 0, "Traffic\nSources", ha="center", va="center", fontsize=10, fontweight="bold")
axes[1].set_title("Donut Chart — Traffic Sources", fontweight="bold")
plt.tight_layout()
plt.savefig("images/pie_donut_chart.png", dpi=110, bbox_inches="tight")
plt.close()

# ── 11. Funnel Chart ─────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(6, 5.5))
stages  = ["Leads","Qualified","Proposals","Negotiations","Closed Won"]
counts  = [1000, 620, 310, 155, 82]
colors_f = ["#1565C0","#1976D2","#2196F3","#42A5F5","#90CAF9"]
max_c = counts[0]
for i,(s,c,col) in enumerate(zip(stages,counts,colors_f)):
    w = c / max_c
    left = (1-w)/2
    ax.barh(len(stages)-1-i, w, left=left, height=0.72, color=col, edgecolor="white", lw=1.5)
    ax.text(0.5, len(stages)-1-i, f"{s}\n{c:,}", ha="center", va="center",
            color="white", fontweight="bold", fontsize=9.5)
    if i < len(stages)-1:
        conv = counts[i+1]/counts[i]*100
        ax.text(1.01, len(stages)-1-i-0.5, f"↓ {conv:.0f}%", va="center", fontsize=8, color="#666")
ax.set_xlim(0, 1.15); ax.set_ylim(-0.5, len(stages)-0.5)
ax.axis("off")
ax.set_title("Funnel Chart — Sales Pipeline", fontweight="bold")
plt.tight_layout()
plt.savefig("images/funnel_chart.png", dpi=110, bbox_inches="tight")
plt.close()

# ── 12. Scatter Plot ─────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(6, 4.5))
spend   = np.random.uniform(500, 5000, 80)
conv    = 0.04*spend + np.random.normal(0, 40, 80)
channel = np.random.choice(["Search","Social","Display"], 80)
colors_sc = {"Search":"#1565C0","Social":"#E53935","Display":"#2E7D32"}
for ch, col in colors_sc.items():
    mask = channel == ch
    ax.scatter(spend[mask], conv[mask], c=col, alpha=0.75, s=60,
               edgecolors="white", lw=0.5, label=ch)
m,b = np.polyfit(spend, conv, 1)
xs = np.linspace(spend.min(), spend.max(), 100)
ax.plot(xs, m*xs+b, color="#FF9800", lw=2.2, ls="--", label="Trend line")
ax.set_title("Scatter Plot — Ad Spend vs Conversions", fontweight="bold")
ax.set_xlabel("Ad Spend (USD)"); ax.set_ylabel("Conversions")
ax.legend()
plt.tight_layout()
plt.savefig("images/scatter_plot.png", dpi=110, bbox_inches="tight")
plt.close()

# ── 13. Choropleth / Geographic Map (schematic) ──────────────────────────────
fig, ax = plt.subplots(figsize=(8, 4.5))
ax.set_facecolor("#d0e8f1")
regions = {
    "West\n$2.1M":      ([-125,-115,-115,-125,-125],[25,25,49,49,25], "#1565C0"),
    "Midwest\n$1.5M":   ([-115,-90,-90,-115,-115], [25,25,49,49,25],  "#42A5F5"),
    "South\n$3.2M":     ([-100,-75,-75,-100,-100], [25,25,37,37,25],  "#0D47A1"),
    "Northeast\n$1.8M": ([-80,-65,-65,-80,-80],    [37,37,47,47,37],  "#1976D2"),
    "Central\n$1.0M":   ([-90,-80,-80,-90,-90],    [37,37,45,45,37],  "#90CAF9"),
}
for lbl,(xs,ys,col) in regions.items():
    ax.fill(xs, ys, color=col, alpha=0.85, edgecolor="white", lw=2)
    ax.text(np.mean(xs[:-1]), np.mean(ys[:-1]), lbl,
            ha="center", va="center", color="white", fontsize=8.5, fontweight="bold")
ax.set_xlim(-130,-60); ax.set_ylim(22,52)
ax.set_title("Choropleth Map — Sales Revenue by Region (USA)", fontweight="bold")
ax.set_xlabel("Longitude"); ax.set_ylabel("Latitude")
sm = plt.cm.ScalarMappable(cmap="Blues", norm=plt.Normalize(1.0, 3.2))
sm.set_array([])
plt.colorbar(sm, ax=ax, label="Revenue (USD M)", fraction=0.03, pad=0.02)
plt.tight_layout()
plt.savefig("images/choropleth_map.png", dpi=110, bbox_inches="tight")
plt.close()

# ── 14. Gauge / KPI Chart ────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(5.5, 3.8), subplot_kw=dict(polar=True))
ax.set_facecolor("white"); fig.patch.set_facecolor("white")
theta = np.linspace(np.pi, 0, 300)
poor_end = int(300*0.40); fair_end = int(300*0.75)
ax.fill_between(theta[:poor_end], 0.7, 1.0, color="#E53935", alpha=0.75)
ax.fill_between(theta[poor_end:fair_end], 0.7, 1.0, color="#FF9800", alpha=0.75)
ax.fill_between(theta[fair_end:], 0.7, 1.0, color="#2E7D32", alpha=0.75)
value_pct = 0.72
needle_angle = np.pi * (1 - value_pct)
ax.annotate("", xy=(needle_angle, 0.68), xytext=(needle_angle, 0.0),
            arrowprops=dict(arrowstyle="->,head_width=0.06,head_length=0.05",
                            color="#212121", lw=2.5))
ax.scatter([needle_angle], [0], s=80, color="#212121", zorder=5)
ax.set_ylim(0, 1.2)
ax.set_theta_zero_location("W"); ax.set_theta_direction(-1)
ax.set_axis_off()
ax.text(np.pi/2, -0.35, "72%", ha="center", va="center",
        fontsize=22, fontweight="bold", color="#212121", transform=ax.transData)
ax.text(np.pi/2, -0.58, "Conversion Rate", ha="center", va="center",
        fontsize=9, color="#666", transform=ax.transData)
ax.text(np.pi, 0.78, "Poor", ha="left",  va="center", color="white", fontsize=8, transform=ax.transData)
ax.text(np.pi*0.62, 0.95, "Fair", ha="center",  va="center", color="white", fontsize=8, transform=ax.transData)
ax.text(np.pi*0.2, 0.78, "Good", ha="right", va="center", color="white", fontsize=8, transform=ax.transData)
ax.set_title("Gauge Chart — KPI vs Target", fontweight="bold", pad=10)
plt.tight_layout()
plt.savefig("images/gauge_chart.png", dpi=110, bbox_inches="tight")
plt.close()

# ── 15. Area Chart ───────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(7, 4))
mo = np.arange(12)
organic = [20,22,25,28,35,38,42,40,45,50,48,55]
paid    = [15,18,20,22,25,28,30,32,35,38,40,42]
direct  = [10,12,11,14,16,15,17,18,20,22,21,25]
mlabels = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
ax.stackplot(mo, organic, paid, direct,
             labels=["Organic","Paid","Direct"],
             colors=["#1565C0","#43A047","#FF9800"], alpha=0.80)
ax.set_xticks(mo); ax.set_xticklabels(mlabels, rotation=30)
ax.set_title("Area Chart — Monthly Traffic by Channel", fontweight="bold")
ax.set_ylabel("Sessions (thousands)")
ax.legend(loc="upper left")
plt.tight_layout()
plt.savefig("images/area_chart.png", dpi=110, bbox_inches="tight")
plt.close()

# ── 16. Bubble Chart ─────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(7, 5))
msize  = np.array([100,200,150,300, 80,250])
growth = np.array([ 15,  8, 20,  5, 25, 12])
share  = np.array([ 30, 45, 20, 60, 15, 40])
plbls  = ["A","B","C","D","E","F"]
cols_b = ["#1565C0","#2E7D32","#FF9800","#E53935","#6A1B9A","#00695C"]
sc = ax.scatter(msize, growth, s=share*40, c=cols_b, alpha=0.75,
                edgecolors="white", lw=1.5, zorder=3)
for i,lbl in enumerate(plbls):
    ax.annotate(lbl, (msize[i],growth[i]), ha="center", va="center",
                color="white", fontweight="bold", fontsize=10, zorder=4)
ax.set_title("Bubble Chart — Market Analysis (BCG-style)", fontweight="bold")
ax.set_xlabel("Market Size (USD M)"); ax.set_ylabel("Growth Rate (%)")
ax.text(0.98,0.98,"Bubble size = Market Share %",
        transform=ax.transAxes, ha="right", va="top", fontsize=8, color="#888")
ax.axhline(np.mean(growth), color="#aaa", ls="--", lw=1)
ax.axvline(np.mean(msize),  color="#aaa", ls="--", lw=1)
ax.text(np.mean(msize)+5,  max(growth)-1, "Stars",        fontsize=8, color="#888")
ax.text(5,                  max(growth)-1, "Question Marks",fontsize=8, color="#888")
ax.text(np.mean(msize)+5,  3,             "Cash Cows",    fontsize=8, color="#888")
ax.text(5,                  3,             "Dogs",         fontsize=8, color="#888")
plt.tight_layout()
plt.savefig("images/bubble_chart.png", dpi=110, bbox_inches="tight")
plt.close()

# ── 17. Histogram ────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(6, 4))
data_h = np.concatenate([np.random.normal(62, 9, 200), np.random.normal(84, 7, 100)])
ax.hist(data_h, bins=28, color="#1565C0", edgecolor="white", alpha=0.80, density=True)
kde = gaussian_kde(data_h, bw_method=0.3)
xr  = np.linspace(data_h.min(), data_h.max(), 300)
ax.plot(xr, kde(xr), color="#E53935", lw=2.5, label="KDE")
ax.axvline(np.mean(data_h), color="#FF9800", ls="--", lw=1.8, label=f"Mean={np.mean(data_h):.1f}")
ax.set_title("Histogram — Test Score Distribution + KDE", fontweight="bold")
ax.set_xlabel("Score"); ax.set_ylabel("Density")
ax.legend()
plt.tight_layout()
plt.savefig("images/histogram.png", dpi=110, bbox_inches="tight")
plt.close()

# ── 18. Box Plot ─────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(7, 4.5))
grps = ["Control","Treatment A","Treatment B","Treatment C"]
data_bx = [np.random.normal(m, s, 80) for m,s in [(58,10),(72,12),(66,9),(81,14)]]
bp = ax.boxplot(data_bx, patch_artist=True, notch=False,
                medianprops=dict(color="#E53935", lw=2.2),
                whiskerprops=dict(lw=1.5), capprops=dict(lw=1.8),
                flierprops=dict(marker="o", markerfacecolor="#aaa", markersize=4, alpha=0.5))
colors_bp = ["#BBDEFB","#C8E6C9","#FFE0B2","#F8BBD0"]
for patch, col in zip(bp["boxes"], colors_bp):
    patch.set_facecolor(col)
ax.set_xticklabels(grps)
ax.set_title("Box Plot — Response Score by Experimental Group", fontweight="bold")
ax.set_ylabel("Response Score")
plt.tight_layout()
plt.savefig("images/box_plot.png", dpi=110, bbox_inches="tight")
plt.close()

# ── 19. Violin Plot ──────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(7, 4.5))
grps = ["Control","Treatment A","Treatment B","Treatment C"]
rows = []
for g,(m,s) in zip(grps, [(58,10),(72,12),(66,9),(81,14)]):
    vals = np.random.normal(m, s, 120)
    rows.extend({"Group":g,"Score":v} for v in vals)
df_v = pd.DataFrame(rows)
sns.violinplot(x="Group", y="Score", data=df_v, ax=ax, inner="box",
               palette=["#BBDEFB","#C8E6C9","#FFE0B2","#F8BBD0"])
ax.set_title("Violin Plot — Score Distribution by Group", fontweight="bold")
plt.tight_layout()
plt.savefig("images/violin_plot.png", dpi=110, bbox_inches="tight")
plt.close()

# ── 20. Error Bar Chart ──────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(6, 4))
groups_e = ["Control","Low Dose","Mid Dose","High Dose"]
means_e  = [44, 53, 65, 74]
errors_e = [5.2, 6.1, 4.8, 7.5]
cols_e   = ["#90CAF9","#64B5F6","#1976D2","#0D47A1"]
ax.bar(groups_e, means_e, yerr=errors_e, color=cols_e, alpha=0.88,
       capsize=9, error_kw={"lw":2, "capthick":2}, edgecolor="white", lw=1.2)
for i,(g,m,e) in enumerate(zip(groups_e,means_e,errors_e)):
    ax.text(i, m+e+1.5, f"{m}", ha="center", fontsize=9, fontweight="bold")
ax.set_title("Error Bar Chart — Mean Response ± SD by Dose", fontweight="bold")
ax.set_ylabel("Response Score (Mean ± SD)")
ax.set_ylim(0, 90)
plt.tight_layout()
plt.savefig("images/error_bar_chart.png", dpi=110, bbox_inches="tight")
plt.close()

# ── 21. Scatter Matrix (Pair Plot) ───────────────────────────────────────────
np.random.seed(0)
iris = pd.DataFrame({
    "Sepal Length": np.r_[np.random.normal(5.0,0.35,50),np.random.normal(5.9,0.5,50),np.random.normal(6.6,0.6,50)],
    "Sepal Width":  np.r_[np.random.normal(3.4,0.38,50),np.random.normal(2.8,0.31,50),np.random.normal(3.0,0.32,50)],
    "Petal Length": np.r_[np.random.normal(1.5,0.17,50),np.random.normal(4.3,0.47,50),np.random.normal(5.5,0.55,50)],
    "Petal Width":  np.r_[np.random.normal(0.25,0.1,50),np.random.normal(1.35,0.2,50),np.random.normal(2.0,0.25,50)],
    "Species": ["Setosa"]*50+["Versicolor"]*50+["Virginica"]*50,
})
g = sns.pairplot(iris, hue="Species", height=1.7, plot_kws={"alpha":0.55,"s":25},
                 palette=["#1565C0","#E53935","#2E7D32"])
g.figure.suptitle("Scatter Matrix (Pair Plot) — Iris Dataset", fontweight="bold", y=1.02)
plt.savefig("images/scatter_matrix.png", dpi=100, bbox_inches="tight")
plt.close()

# ── 22. Rose / Polar Chart ───────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(5.5, 5.5), subplot_kw=dict(polar=True))
ax.set_facecolor("#f5f5f5")
N_dirs = 16
dirs = np.linspace(0, 2*np.pi, N_dirs, endpoint=False)
freqs = np.array([0.4,0.55,0.9,0.75,0.6,0.45,0.3,0.35,0.5,0.65,0.8,0.7,0.55,0.42,0.35,0.38])
wid = 2*np.pi/N_dirs
bars = ax.bar(dirs, freqs, width=wid*0.9, bottom=0.08,
              color=plt.cm.cool(freqs), alpha=0.85, edgecolor="white", lw=0.8)
dir_labels = ["N","NNE","NE","ENE","E","ESE","SE","SSE","S","SSW","SW","WSW","W","WNW","NW","NNW"]
ax.set_xticks(dirs); ax.set_xticklabels(dir_labels, fontsize=8)
ax.set_theta_zero_location("N"); ax.set_theta_direction(-1)
ax.set_title("Rose Chart — Wind Direction & Frequency", fontweight="bold", pad=20)
plt.tight_layout()
plt.savefig("images/rose_chart.png", dpi=110, bbox_inches="tight")
plt.close()

# ── 23. 3D Surface Plot ──────────────────────────────────────────────────────
fig = plt.figure(figsize=(7, 5))
fig.patch.set_facecolor("white")
ax = fig.add_subplot(111, projection="3d")
ax.set_facecolor("white")
x3 = np.linspace(-3, 3, 60)
y3 = np.linspace(-3, 3, 60)
X3, Y3 = np.meshgrid(x3, y3)
Z3 = np.sin(np.sqrt(X3**2 + Y3**2)) * np.exp(-0.15*(X3**2+Y3**2))
surf = ax.plot_surface(X3, Y3, Z3, cmap="plasma", alpha=0.92, linewidth=0, antialiased=True)
fig.colorbar(surf, ax=ax, shrink=0.45, aspect=10, label="Z value")
ax.set_title("3D Surface Plot — Response Surface", fontweight="bold")
ax.set_xlabel("Variable X"); ax.set_ylabel("Variable Y"); ax.set_zlabel("Response Z")
plt.tight_layout()
plt.savefig("images/surface_3d.png", dpi=110, bbox_inches="tight")
plt.close()

# ── 24. Network / Graph Diagram ──────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(6, 5))
ax.set_facecolor("white")
np.random.seed(7)
n = 12
pos = {i: (np.random.uniform(0.1,0.9), np.random.uniform(0.1,0.9)) for i in range(n)}
edges_n = [(0,1),(0,3),(1,2),(1,4),(2,5),(3,4),(3,6),(4,5),(4,7),(5,8),(6,7),(7,8),(7,9),(8,10),(9,10),(9,11),(10,11)]
for (u,v) in edges_n:
    ax.plot([pos[u][0],pos[v][0]],[pos[u][1],pos[v][1]],
            color="#90A4AE", lw=1.5, alpha=0.7, zorder=1)
node_sizes = [500,400,350,450,600,380,320,550,420,380,340,360]
for i,(x,y) in pos.items():
    ax.scatter(x, y, s=node_sizes[i], c="#1565C0", zorder=3,
               edgecolors="white", lw=1.8, alpha=0.90)
    ax.text(x, y, str(i+1), ha="center", va="center",
            color="white", fontweight="bold", fontsize=8, zorder=4)
ax.set_title("Network Diagram — Protein Interaction Graph", fontweight="bold")
ax.axis("off")
plt.tight_layout()
plt.savefig("images/network_diagram.png", dpi=110, bbox_inches="tight")
plt.close()

# ── 25. Regression & Residual Plots ─────────────────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(9, 4))
xr = np.random.uniform(10, 100, 90)
yr = 2.8*xr + 30 + np.random.normal(0, 18, 90)
m_r, b_r = np.polyfit(xr, yr, 1)
y_pred_r  = m_r*xr + b_r
residuals_r = yr - y_pred_r
axes[0].scatter(xr, yr, color="#1565C0", alpha=0.65, edgecolors="white", s=50)
xs_r = np.linspace(xr.min(), xr.max(), 200)
axes[0].plot(xs_r, m_r*xs_r+b_r, color="#E53935", lw=2.2)
axes[0].fill_between(xs_r, m_r*xs_r+b_r-25, m_r*xs_r+b_r+25, alpha=0.15, color="#E53935")
axes[0].set_title("Regression Fit + 95% CI Band", fontweight="bold")
axes[0].set_xlabel("X"); axes[0].set_ylabel("Y")
axes[1].scatter(y_pred_r, residuals_r, color="#2E7D32", alpha=0.65, edgecolors="white", s=50)
axes[1].axhline(0, color="#E53935", lw=2, ls="--")
axes[1].set_title("Residual Plot", fontweight="bold")
axes[1].set_xlabel("Fitted Values"); axes[1].set_ylabel("Residuals")
plt.suptitle("Regression / Residual Plots", fontweight="bold")
plt.tight_layout()
plt.savefig("images/residual_plot.png", dpi=110, bbox_inches="tight")
plt.close()

print("All 25 chart images generated successfully!")
