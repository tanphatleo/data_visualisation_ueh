"""
sankey_styles.py
Chart gallery — all 11 charts from the reference image plus Sankey styles.

Charts:
  01 – Bar          02 – Line         03 – Area
  04 – Slope        05 – Donut        06 – Waterfall
  07 – Candlestick  08 – Treemap      09 – Scatter + trend
  10 – Bubble       11 – Funnel
  36 – Sankey 2-column crossing
  37 – Sankey 4-layer funnel (20% remains)
  BP – Box plot
  BU – Bullet chart
  HM – Heatmap
  CM – Choropleth map
  GG – KPI Gauge
  CD – CDF chart
  HL – Histogram + KDE line
  PG – Pictogram (person icon grid)
  SA – Stacked Area
  SC – Stacked Column
  SA100 – 100% Stacked Area
  SC100 – 100% Stacked Column
  02b – Line dual (thick + thin)
  RD – Radar chart with hexagon boundary
  09b – Scatter orange (large points, no trend)
  10b – Bubble orange (large bubbles)
  HLb – Histogram orange
  BPb – Box plot orange

Requirements:
    pip install plotly kaleido numpy pandas
"""

import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import pandas as pd

# ── Colour palette ──────────────────────────────────────────────────────────────
NAVY    = "#0D1A63"
NAVY1   = "#253A95"
NAVY2   = "#5B73C4"
NAVY3   = "#A8B4DE"
NAVY4   = "#DDE2F2"
GRAY    = "#7e7e7e"
ORANGE  = "#F68048"
ORANGE1 = "#F89B72"
ORANGE2 = "#FAB69B"
ORANGE3 = "#FDD1C3"
ORANGE4 = "#FEEEE8"
BG      = "rgba(0,0,0,0)"
WHITE   = "#FFFFFF"

OUT = "day_1/images/chart_types"

def rgba(hex_color, alpha):
    h = hex_color.lstrip("#")
    r, g, b = int(h[0:2],16), int(h[2:4],16), int(h[4:6],16)
    return f"rgba({r},{g},{b},{alpha})"

def save(fig, name, w=500, h=500):
    fig.write_image(f"{OUT}/{name}.png", width=w, height=h, scale=2)
    print(f"Saved {name}.png")

def no_ax():
    return dict(visible=False, showgrid=False, zeroline=False,
                showticklabels=False, showline=False)

def L(**kw):
    """Base transparent layout."""
    d = dict(paper_bgcolor=BG, plot_bgcolor=BG,
             margin=dict(l=24, r=24, t=24, b=24),
             showlegend=False,
             font=dict(size=1, color="rgba(0,0,0,0)"))
    d.update(kw)
    return d


# ═══════════════════════════════════════════════════════════════════════════════
# 01 – Bar chart
# ═══════════════════════════════════════════════════════════════════════════════
fig = go.Figure(go.Bar(
    x=list(range(5)),
    y=[75, 90, 48, 28, 62],
    marker_color=NAVY,
    marker_line_width=0,
    width=0.88,
))
fig.update_layout(**L(xaxis=no_ax(), yaxis=no_ax()))
save(fig, "chart01_bar")


# ═══════════════════════════════════════════════════════════════════════════════
# 02 – Line chart (dots + lines)
# ═══════════════════════════════════════════════════════════════════════════════
fig = go.Figure(go.Scatter(
    x=[0, 1, 2, 3, 4, 5],
    y=[4.5, 2.8, 5.8, 3.2, 5.2, 3.0],
    mode='lines+markers',
    line=dict(color=NAVY, width=2.5),
    marker=dict(color=NAVY, size=11, line=dict(width=0)),
))
fig.update_layout(**L(xaxis=no_ax(), yaxis=dict(**no_ax(), range=[0, 6.4])))
save(fig, "chart02_line")


# ═══════════════════════════════════════════════════════════════════════════════
# 02b – Line dual (thick navy + thin orange)
# ═══════════════════════════════════════════════════════════════════════════════
fig = go.Figure()
fig.add_trace(go.Scatter(
    x=[0, 1, 2, 3, 4, 5],
    y=[4.5, 2.8, 5.8, 3.2, 5.2, 3.0],
    mode='lines',
    line=dict(color=NAVY, width=7),
))
fig.add_trace(go.Scatter(
    x=[0, 1, 2, 3, 4, 5],
    y=[2.0, 3.8, 2.5, 5.0, 2.8, 4.6],
    mode='lines',
    line=dict(color=ORANGE, width=1.5),
))
fig.update_layout(**L(xaxis=no_ax(), yaxis=dict(**no_ax(), range=[0, 6.4])))
save(fig, "chart02b_line_dual")


# ═══════════════════════════════════════════════════════════════════════════════
# 03 – Area chart (solid filled, angular silhouette)
# ═══════════════════════════════════════════════════════════════════════════════
fig = go.Figure(go.Scatter(
    x=[0, 1, 2, 3, 4, 5, 6],
    y=[0, 5, 9, 4, 2, 8, 7],
    fill='tozeroy',
    fillcolor=NAVY,
    mode='lines',
    line=dict(color=NAVY, width=0),
))
fig.update_layout(**L(xaxis=no_ax(), yaxis=no_ax()))
save(fig, "chart03_area")


# ═══════════════════════════════════════════════════════════════════════════════
# 04 – Slope chart (two-column, one orange line)
# ═══════════════════════════════════════════════════════════════════════════════
left_y  = [1.0, 2.2, 3.5, 4.8]
right_y = [3.8, 1.2, 4.2, 2.0]
fig = go.Figure()
for i, (lv, rv) in enumerate(zip(left_y, right_y)):
    col  = ORANGE if i == 2 else NAVY
    size = 9
    fig.add_trace(go.Scatter(
        x=[0, 1], y=[lv, rv],
        mode='lines+markers',
        line=dict(color=col, width=2.5),
        marker=dict(color=col, size=size, line=dict(width=0)),
    ))
fig.update_layout(**L(xaxis=no_ax(), yaxis=no_ax()))
save(fig, "chart04_slope")


# ═══════════════════════════════════════════════════════════════════════════════
# 05 – Donut chart
# ═══════════════════════════════════════════════════════════════════════════════
fig = go.Figure(go.Pie(
    values=[35, 22, 18, 14, 11],
    hole=0.55,
    marker=dict(
        colors=[NAVY, NAVY1, NAVY2, NAVY3, GRAY],
        line=dict(width=0),
    ),
    textinfo='none',
    hoverinfo='none',
    sort=False,
    direction='clockwise',
))
fig.update_layout(**L())
save(fig, "chart05_donut")


# ═══════════════════════════════════════════════════════════════════════════════
# 06 – Waterfall chart
# ═══════════════════════════════════════════════════════════════════════════════
# Waterfall using positioned Bar traces (go.Waterfall won't accept per-bar colors)
# Cumulative: 0 → 80 → 100 → 85 → 40
wf_bars = [
    dict(x=0, base=0,  h=30, color=NAVY),    # up:   0 → 30
    dict(x=1, base=18, h=12, color=ORANGE),  # down: 30 → 18
    dict(x=2, base=18, h=3,  color=NAVY),    # up:   18 → 21
    dict(x=3, base=14, h=7,  color=ORANGE),  # down: 21 → 14
    dict(x=4, base=0,  h=14, color=NAVY2),   # total: 14
]
fig = go.Figure()
for b in wf_bars:
    fig.add_trace(go.Bar(
        x=[b["x"]], y=[b["h"]], base=b["base"],
        marker_color=b["color"], marker_line_width=0,
        width=0.82, showlegend=False,
    ))
fig.update_layout(**L(xaxis=no_ax(), yaxis=no_ax()))
save(fig, "chart06_waterfall")


# ═══════════════════════════════════════════════════════════════════════════════
# 07 – Candlestick chart
# ═══════════════════════════════════════════════════════════════════════════════
rng = np.random.default_rng(7)
n = 10
dates = pd.date_range("2024-01-01", periods=n, freq="D")
close = np.cumsum(rng.normal(1.2, 1.5, n)) + 50
open_ = np.empty(n)
open_[0] = close[0] + rng.normal(0, 0.4)
for i in range(1, n):
    open_[i] = close[i - 1] + rng.normal(0, 0.3)
high  = np.maximum(open_, close) + abs(rng.normal(0, 0.6, n))
low   = np.minimum(open_, close) - abs(rng.normal(0, 0.6, n))

fig = go.Figure(go.Candlestick(
    x=dates,
    open=open_, high=high, low=low, close=close,
    increasing=dict(line=dict(color=NAVY, width=1.5), fillcolor=NAVY),
    decreasing=dict(line=dict(color=GRAY,  width=1.5), fillcolor=GRAY),
))
fig.update_layout(
    **L(xaxis=no_ax(), yaxis=no_ax()),
    xaxis_rangeslider_visible=False,
)
save(fig, "chart07_candlestick")


# ═══════════════════════════════════════════════════════════════════════════════
# 08 – Treemap
# ═══════════════════════════════════════════════════════════════════════════════
fig = go.Figure(go.Treemap(
    labels=["A", "B", "C", "D", "E"],
    parents=["", "", "", "", ""],
    values=[42, 22, 18, 12, 6],
    marker=dict(
        colors=[NAVY, NAVY2, NAVY3, NAVY3, GRAY],
        line=dict(width=0),
    ),
    textinfo="none",
    hoverinfo="none",
    tiling=dict(packing="squarify"),
))
fig.update_layout(**L())
save(fig, "chart08_treemap")


# ═══════════════════════════════════════════════════════════════════════════════
# 09 – Scatter plot + orange dashed trend line
# ═══════════════════════════════════════════════════════════════════════════════
rng2 = np.random.default_rng(42)
x_sc = rng2.uniform(1, 9, 13)
y_sc = 0.6 * x_sc + rng2.normal(0, 1.2, 13)
m, b = np.polyfit(x_sc, y_sc, 1)
x_ln = np.linspace(x_sc.min(), x_sc.max(), 80)

fig = go.Figure()
fig.add_trace(go.Scatter(
    x=x_sc, y=y_sc,
    mode='markers',
    marker=dict(color=NAVY2, size=9, line=dict(width=0)),
))
fig.add_trace(go.Scatter(
    x=x_ln, y=m * x_ln + b,
    mode='lines',
    line=dict(color=ORANGE, width=2.5, dash='dash'),
))
fig.update_layout(**L(xaxis=no_ax(), yaxis=no_ax()))
save(fig, "chart09_scatter")


# ═══════════════════════════════════════════════════════════════════════════════
# 10 – Bubble chart
# ═══════════════════════════════════════════════════════════════════════════════
bx = [2.0, 2.8, 3.5, 4.5, 5.5, 6.5, 3.2, 5.0, 4.0, 2.2]
by = [5.0, 6.5, 7.5, 6.0, 4.5, 3.5, 4.0, 7.0, 3.0, 7.5]
bs = [12,  18,  25,  50,  80, 100,  14,  30,  40,  10 ]

fig = go.Figure(go.Scatter(
    x=bx, y=by,
    mode='markers',
    marker=dict(
        color=NAVY2,
        size=bs,
        sizemode='area',
        sizeref=2. * max(bs) / (45**2),
        line=dict(width=0),
    ),
))
fig.update_layout(**L(xaxis=no_ax(), yaxis=no_ax()))
save(fig, "chart10_bubble")


# ═══════════════════════════════════════════════════════════════════════════════
# 11 – Funnel chart (centered horizontal bars)
# ═══════════════════════════════════════════════════════════════════════════════
# _fd = dict(
#     number=[1000, 620, 380, 190, 85, 34],
#     stage=["", "", "", "", "", ""],
# )
# fig = px.funnel(_fd, x="number", y="stage")
# fig.update_traces(
#     marker=dict(color=[NAVY, NAVY1, NAVY2, NAVY2, NAVY3, NAVY3], line=dict(width=0)),
#     textinfo="none",
#     connector=dict(visible=False),
# )
# fig.update_layout(**L(xaxis=no_ax(), yaxis=no_ax()))
# save(fig, "chart11_funnel", w=500, h=600)


# ═══════════════════════════════════════════════════════════════════════════════
# 36 – Sankey 2-column (crossing flows)
# ═══════════════════════════════════════════════════════════════════════════════
fig36 = go.Figure(go.Sankey(
    arrangement="snap",
    node=dict(
        pad=12, thickness=26,
        line=dict(color=WHITE, width=0),
        label=[""] * 8,
        color=[NAVY1, NAVY, NAVY2, NAVY3,
               NAVY2, NAVY1, NAVY, NAVY2],
        x=[0.01, 0.01, 0.01, 0.01, 0.99, 0.99, 0.99, 0.99],
        y=[0.04, 0.26, 0.54, 0.80, 0.04, 0.26, 0.54, 0.80],
    ),
    link=dict(
        source=[0,  0,  1,  1,  2,  2,  3],
        target=[5,  6,  4,  6,  5,  7,  7],
        value= [20, 15, 25, 12, 18, 14, 10],
        color=[rgba(NAVY1,0.40), rgba(NAVY1,0.40),
               rgba(NAVY, 0.40), rgba(NAVY, 0.40),
               rgba(NAVY2,0.40), rgba(NAVY2,0.40),
               rgba(NAVY3,0.40)],
    ),
))
fig36.update_layout(**L())
save(fig36, "chart36_alluvial", w=640, h=560)


# ═══════════════════════════════════════════════════════════════════════════════
# 37 – Sankey 4-layer funnel (20% remains)
# ═══════════════════════════════════════════════════════════════════════════════
fig37 = go.Figure(go.Sankey(
    arrangement="snap",
    node=dict(
        pad=6, thickness=55,
        line=dict(color=WHITE, width=0),
        label=[""] * 7,
        color=[NAVY, NAVY1, NAVY2, NAVY3, NAVY4, NAVY4, NAVY4],
        x=[0.01, 0.34, 0.67, 0.99, 0.17,  0.50, 0.83],
        y=[0.15, 0.15, 0.15, 0.15, 0.88,  0.88, 0.88],
    ),
    link=dict(
        source=[0,  0,  1,  1,  2,  2],
        target=[1,  4,  2,  5,  3,  6],
        value= [65, 35, 40, 25, 20, 20],
        color=[rgba(NAVY, 0.45), rgba(NAVY4,0.35),
               rgba(NAVY1,0.45), rgba(NAVY4,0.35),
               rgba(NAVY2,0.45), rgba(NAVY4,0.35)],
    ),
))
fig37.update_layout(**L())
save(fig37, "chart37_sankey", w=900, h=500)


# ═══════════════════════════════════════════════════════════════════════════════
# BP – Box plot (3 categories)
# ═══════════════════════════════════════════════════════════════════════════════
rng3 = np.random.default_rng(42)
data = [
    rng3.normal(loc=50, scale=12, size=120),
    rng3.normal(loc=65, scale=9,  size=120),
    rng3.normal(loc=45, scale=16, size=120),
]
colors_bp    = [NAVY1, NAVY2, NAVY3]
fill_colors  = [rgba(NAVY1,0.55), rgba(NAVY2,0.55), rgba(NAVY3,0.55)]

fig_box = go.Figure()
for i, (d, fc, lc) in enumerate(zip(data, fill_colors, colors_bp)):
    fig_box.add_trace(go.Box(
        y=d, x=[i] * len(d),
        marker_color=lc, fillcolor=fc,
        line=dict(color=lc, width=2),
        boxpoints=False, showlegend=False,
        name=str(i), width=0.5,
    ))
fig_box.update_layout(**L(xaxis=no_ax(), yaxis=no_ax()))
save(fig_box, "chart_box_plot_navy", w=600, h=500)


# ═══════════════════════════════════════════════════════════════════════════════
# BU – Bullet chart  (bands: <70 poor, 70–95 ok, >95 good)
# ═══════════════════════════════════════════════════════════════════════════════
fig = go.Figure()
# Bands in axis coordinates so they span the full bar height
for x0, x1, col in [(0, 70, rgba(GRAY, 0.25)),
                     (70, 95, rgba(GRAY, 0.50)),
                     (95, 120, rgba(GRAY, 0.80))]:
    fig.add_shape(type="rect", x0=x0, x1=x1, y0=-1, y1=1,
                  xref="x", yref="y", fillcolor=col, line_width=0, layer="below")
# Measure bar — 90% the height of the bands (bands span 2 units → width=1.8)
fig.add_trace(go.Bar(
    x=[90], y=[0], orientation='h',
    marker_color=NAVY, marker_line_width=0, width=1.4,
))
# Target marker
fig.add_shape(type="line", x0=100, x1=100, y0=-1, y1=1,
              xref="x", yref="y", line=dict(color=ORANGE, width=4))
fig.update_layout(**L(
    xaxis=dict(**no_ax(), range=[0, 120]),
    yaxis=dict(**no_ax(), range=[-1, 1]),
))
save(fig, "chart_bullet", w=640, h=220)


# ═══════════════════════════════════════════════════════════════════════════════
# HM – Heatmap
# ═══════════════════════════════════════════════════════════════════════════════
rng_h = np.random.default_rng(5)
z_heat = rng_h.uniform(0, 1, (7, 7))
fig = go.Figure(go.Heatmap(
    z=z_heat,
    colorscale=[[0, NAVY4], [0.5, NAVY2], [1, NAVY]],
    showscale=False,
    xgap=3, ygap=3,
))
fig.update_layout(**L(xaxis=no_ax(), yaxis=no_ax()))
save(fig, "chart_heatmap")


# ═══════════════════════════════════════════════════════════════════════════════
# CM – Choropleth map (France metropolitan regions)
# ═══════════════════════════════════════════════════════════════════════════════
import urllib.request as _urlreq, json as _json

_geo_url = "https://raw.githubusercontent.com/gregoiredavid/france-geojson/master/regions-version-simplifiee.geojson"
with _urlreq.urlopen(_geo_url) as _resp:
    _france_geo = _json.loads(_resp.read())

# Keep only the 13 metropolitan regions (2-digit codes ≥ 11)
_METRO = {"11","24","27","28","32","44","52","53","75","76","84","93","94"}
_france_geo["features"] = [f for f in _france_geo["features"]
                            if f["properties"]["code"] in _METRO]
_codes   = [f["properties"]["code"] for f in _france_geo["features"]]
_rng_fr  = np.random.default_rng(9)
_fr_vals = _rng_fr.integers(20, 100, len(_codes)).tolist()

fig = px.choropleth(
    geojson=_france_geo,
    locations=_codes,
    color=_fr_vals,
    featureidkey="properties.code",
    color_continuous_scale=[[0, NAVY4], [0.5, NAVY2], [1, NAVY]],
    basemap_visible=False,
)
fig.update_traces(marker_line_width=1.5, marker_line_color=WHITE)
fig.update_coloraxes(showscale=False)
fig.update_layout(
    **L(margin=dict(l=0, r=0, t=0, b=0)),
    geo=dict(
        bgcolor="rgba(0,0,0,0)",
        showframe=False,
        showcoastlines=False,
        showland=False,
        lataxis_range=[41.2, 51.5],
        lonaxis_range=[-5.5, 9.8],
    ),
)
save(fig, "chart_choropleth", w=560, h=620)


# ═══════════════════════════════════════════════════════════════════════════════
# GG – KPI Gauge
# ═══════════════════════════════════════════════════════════════════════════════
fig = go.Figure(go.Indicator(
    mode="gauge",
    value=72,
    gauge=dict(
        axis=dict(visible=False, range=[0, 100]),
        bar=dict(color=NAVY, thickness=0.65),
        bgcolor="rgba(0,0,0,0)",
        borderwidth=0,
        steps=[
            dict(range=[0,  40], color=NAVY4),
            dict(range=[40, 70], color=NAVY3),
            dict(range=[70, 100], color=NAVY2),
        ],
        threshold=dict(
            line=dict(color=ORANGE, width=4),
            thickness=0.8,
            value=85,
        ),
    ),
    domain=dict(x=[0, 1], y=[0, 1]),
))
fig.update_layout(**L())
save(fig, "chart_gauge", w=500, h=350)


# ═══════════════════════════════════════════════════════════════════════════════
# CD – CDF (Cumulative Distribution Function)
# ═══════════════════════════════════════════════════════════════════════════════
rng_cdf = np.random.default_rng(15)
cdf_data = np.sort(rng_cdf.normal(50, 15, 300))
cdf_y = np.arange(1, len(cdf_data) + 1) / len(cdf_data)

fig = go.Figure()
fig.add_trace(go.Scatter(
    x=cdf_data, y=cdf_y,
    mode='lines',
    line=dict(color=NAVY, width=2.5),
    fill='tozeroy',
    fillcolor=rgba(NAVY2, 0.18),
))
fig.update_layout(**L(
    xaxis=no_ax(),
    yaxis=dict(**no_ax(), range=[0, 1.05]),
))
save(fig, "chart_cdf")


# ═══════════════════════════════════════════════════════════════════════════════
# HL – Histogram + KDE line
# ═══════════════════════════════════════════════════════════════════════════════
rng_hl = np.random.default_rng(20)
hl_data = rng_hl.normal(50, 15, 400)

counts, edges = np.histogram(hl_data, bins=20)
bin_w = edges[1] - edges[0]
bin_centers = (edges[:-1] + edges[1:]) / 2

# Silverman bandwidth KDE (vectorised)
bw = 1.06 * hl_data.std() * len(hl_data) ** (-0.2)
x_kde = np.linspace(edges[0], edges[-1], 300)
kde = np.exp(-0.5 * ((x_kde[:, None] - hl_data[None, :]) / bw) ** 2).sum(axis=1)
kde /= len(hl_data) * bw * np.sqrt(2 * np.pi)
kde_scaled = kde * len(hl_data) * bin_w   # scale to match bar counts

fig = go.Figure()
fig.add_trace(go.Bar(
    x=bin_centers,
    y=counts,
    width=bin_w * 0.92,
    marker_color=rgba(NAVY2, 0.65),
    marker_line_width=0,
))
fig.add_trace(go.Scatter(
    x=x_kde, y=kde_scaled,
    mode='lines',
    line=dict(color=ORANGE, width=2.5),
))
fig.update_layout(**L(xaxis=no_ax(), yaxis=no_ax()))
save(fig, "chart_histogram_line")


# ═══════════════════════════════════════════════════════════════════════════════
# PG – Pictogram (person icon grid, 8 × 3 = 24 units, 16 filled = 67%)
# ═══════════════════════════════════════════════════════════════════════════════
pg_cols, pg_rows = 8, 3
pg_filled = 16
y_gap = 1.9

xs_bf, ys_bf, xs_hf, ys_hf = [], [], [], []  # filled
xs_be, ys_be, xs_he, ys_he = [], [], [], []  # empty

for r in range(pg_rows):
    for c in range(pg_cols):
        idx = r * pg_cols + c
        xp = c
        yp = (pg_rows - 1 - r) * y_gap
        if idx < pg_filled:
            xs_bf.append(xp); ys_bf.append(yp)
            xs_hf.append(xp); ys_hf.append(yp + 0.76)
        else:
            xs_be.append(xp); ys_be.append(yp)
            xs_he.append(xp); ys_he.append(yp + 0.76)

fig = go.Figure()
for xs_b, ys_b, xs_h, ys_h, col in [
    (xs_bf, ys_bf, xs_hf, ys_hf, NAVY),
    (xs_be, ys_be, xs_he, ys_he, NAVY3),
]:
    fig.add_trace(go.Scatter(
        x=xs_b, y=ys_b, mode='markers',
        marker=dict(symbol='circle', size=36, color=col, line=dict(width=0)),
    ))
    fig.add_trace(go.Scatter(
        x=xs_h, y=ys_h, mode='markers',
        marker=dict(symbol='circle', size=16, color=col, line=dict(width=0)),
    ))
fig.update_layout(**L(
    xaxis=dict(**no_ax(), range=[-0.65, pg_cols - 0.35]),
    yaxis=dict(**no_ax(), range=[-0.85, (pg_rows - 1) * y_gap + 1.55]),
))
save(fig, "chart_pictogram", w=600, h=310)


# ═══════════════════════════════════════════════════════════════════════════════
# SA – Stacked Area chart
# ═══════════════════════════════════════════════════════════════════════════════
x_sa = list(range(7))
sa_series = [
    dict(y=[10, 14, 12, 16, 13, 18, 15], color=NAVY),
    dict(y=[6,  8,  9,  7,  10, 8,  11], color=NAVY2),
    dict(y=[4,  5,  6,  5,  7,  6,  8],  color=NAVY3),
]
fig = go.Figure()
for s in sa_series:
    fig.add_trace(go.Scatter(
        x=x_sa, y=s["y"],
        mode='lines',
        stackgroup='one',
        line=dict(width=0),
        fillcolor=s["color"],
    ))
fig.update_layout(**L(xaxis=no_ax(), yaxis=no_ax()))
save(fig, "chart_stacked_area")


# ═══════════════════════════════════════════════════════════════════════════════
# SC – Stacked Column chart
# ═══════════════════════════════════════════════════════════════════════════════
x_sc2 = list(range(5))
sc_series = [
    dict(y=[30, 35, 28, 42, 38], color=NAVY),
    dict(y=[20, 22, 25, 18, 24], color=NAVY2),
    dict(y=[15, 12, 18, 14, 16], color=NAVY3),
]
fig = go.Figure()
for s in sc_series:
    fig.add_trace(go.Bar(
        x=x_sc2, y=s["y"],
        marker_color=s["color"],
        marker_line_width=0,
        width=0.85,
    ))
fig.update_layout(**L(
    xaxis=no_ax(), yaxis=no_ax(),
    barmode='stack',
))
save(fig, "chart_stacked_column")


# ═══════════════════════════════════════════════════════════════════════════════
# SA100 – 100% Stacked Area
# ═══════════════════════════════════════════════════════════════════════════════
x_sa100 = list(range(7))
sa100_series = [
    dict(y=[10, 14, 12, 16, 13, 18, 15], color=NAVY),
    dict(y=[6,  8,  9,  7,  10, 8,  11], color=NAVY2),
    dict(y=[4,  5,  6,  5,  7,  6,  8],  color=NAVY3),
]
fig = go.Figure()
for s in sa100_series:
    fig.add_trace(go.Scatter(
        x=x_sa100, y=s["y"],
        mode='lines',
        stackgroup='pct',
        groupnorm='percent',
        line=dict(width=0),
        fillcolor=s["color"],
    ))
fig.update_layout(**L(xaxis=no_ax(), yaxis=no_ax()))
save(fig, "chart_stacked_area_100")


# ═══════════════════════════════════════════════════════════════════════════════
# SC100 – 100% Stacked Column
# ═══════════════════════════════════════════════════════════════════════════════
x_sc100 = list(range(5))
sc100_series = [
    dict(y=[30, 35, 28, 42, 38], color=NAVY),
    dict(y=[20, 22, 25, 18, 24], color=NAVY2),
    dict(y=[15, 12, 18, 14, 16], color=NAVY3),
]
fig = go.Figure()
for s in sc100_series:
    fig.add_trace(go.Bar(
        x=x_sc100, y=s["y"],
        marker_color=s["color"],
        marker_line_width=0,
        width=0.85,
    ))
fig.update_layout(**L(
    xaxis=no_ax(), yaxis=no_ax(),
    barmode='stack',
    barnorm='percent',
))
save(fig, "chart_stacked_column_100")


# ═══════════════════════════════════════════════════════════════════════════════
# RD – Radar (Spider) chart
# ═══════════════════════════════════════════════════════════════════════════════
categories = ["A", "B", "C", "D", "E", "F"]
rd_series = [
    dict(r=[80, 65, 90, 55, 75, 70], color=NAVY),
    dict(r=[50, 80, 60, 85, 45, 65], color=ORANGE),
]
fig = go.Figure()
# Outer hexagon boundary
fig.add_trace(go.Scatterpolar(
    r=[100] * 6 + [100],
    theta=categories + [categories[0]],
    mode='lines',
    line=dict(color=NAVY3, width=2),
    fill='none',
))
for s in rd_series:
    r_closed = s["r"] + [s["r"][0]]
    theta_closed = categories + [categories[0]]
    fig.add_trace(go.Scatterpolar(
        r=r_closed,
        theta=theta_closed,
        fill='toself',
        fillcolor=rgba(s["color"], 0.20),
        line=dict(color=s["color"], width=2.5),
    ))
fig.update_layout(**L(
    polar=dict(
        bgcolor="rgba(0,0,0,0)",
        radialaxis=dict(visible=False, range=[0, 100]),
        angularaxis=dict(visible=False),
    ),
))
save(fig, "chart_radar")


# ═══════════════════════════════════════════════════════════════════════════════
# 09b – Scatter orange (large points, navy trend line)
# ═══════════════════════════════════════════════════════════════════════════════
rng2b = np.random.default_rng(7)
x_sc2b = rng2b.uniform(1, 9, 18)
y_sc2b = x_sc2b + rng2b.normal(0, 0.9, 18)
_m2b, _b2b = np.polyfit(x_sc2b, y_sc2b, 1)
_tx2b = np.array([x_sc2b.min(), x_sc2b.max()])

fig = go.Figure([
    go.Scatter(x=x_sc2b, y=y_sc2b, mode='markers',
               marker=dict(color=ORANGE, size=40, line=dict(width=0))),
    go.Scatter(x=_tx2b, y=_m2b * _tx2b + _b2b, mode='lines',
               line=dict(color=NAVY, width=4.5)),
])
fig.update_layout(**L(xaxis=no_ax(), yaxis=no_ax()))
save(fig, "chart09b_scatter_orange")


# ═══════════════════════════════════════════════════════════════════════════════
# 10b – Bubble orange (large bubbles)
# ═══════════════════════════════════════════════════════════════════════════════
bx2 = [2.0, 3.2, 4.5, 5.8, 6.5, 3.8, 5.0, 2.6, 4.2, 6.0]
by2 = [6.0, 4.5, 7.2, 5.0, 3.2, 6.8, 3.8, 5.5, 4.0, 6.5]
bs2 = [18,  35,  60,  90, 120,  25,  50,  14,  42,  70 ]

fig = go.Figure(go.Scatter(
    x=bx2, y=by2,
    mode='markers',
    marker=dict(
        color=[rgba(ORANGE, 0.75)] * len(bs2),
        size=bs2,
        sizemode='area',
        sizeref=2. * max(bs2) / (50**2) / 5,
        line=dict(width=0),
    ),
))
fig.update_layout(**L(xaxis=no_ax(), yaxis=no_ax()))
save(fig, "chart10b_bubble_orange")


# ═══════════════════════════════════════════════════════════════════════════════
# HLb – Histogram orange + navy KDE line
# ═══════════════════════════════════════════════════════════════════════════════
rng_hlb = np.random.default_rng(21)
hlb_data = rng_hlb.normal(50, 15, 400)

counts_b, edges_b = np.histogram(hlb_data, bins=20)
bin_w_b = edges_b[1] - edges_b[0]
bin_centers_b = (edges_b[:-1] + edges_b[1:]) / 2

bw_b = 1.06 * hlb_data.std() * len(hlb_data) ** (-0.2)
x_kde_b = np.linspace(edges_b[0], edges_b[-1], 300)
kde_b = np.exp(-0.5 * ((x_kde_b[:, None] - hlb_data[None, :]) / bw_b) ** 2).sum(axis=1)
kde_b /= len(hlb_data) * bw_b * np.sqrt(2 * np.pi)
kde_scaled_b = kde_b * len(hlb_data) * bin_w_b

fig = go.Figure()
fig.add_trace(go.Bar(
    x=bin_centers_b, y=counts_b,
    width=bin_w_b * 0.92,
    marker_color=rgba(ORANGE, 0.65),
    marker_line_width=0,
))
fig.add_trace(go.Scatter(
    x=x_kde_b, y=kde_scaled_b,
    mode='lines',
    line=dict(color=NAVY, width=2.5),
))
fig.update_layout(**L(xaxis=no_ax(), yaxis=no_ax()))
save(fig, "chart_histogram_orange")


# ═══════════════════════════════════════════════════════════════════════════════
# BPb – Box plot orange (3 categories)
# ═══════════════════════════════════════════════════════════════════════════════
rng_bpb = np.random.default_rng(43)
data_b = [
    rng_bpb.normal(loc=50, scale=12, size=120),
    rng_bpb.normal(loc=65, scale=9,  size=120),
    rng_bpb.normal(loc=45, scale=16, size=120),
]
colors_bpb   = [ORANGE, ORANGE1, ORANGE2]
fill_bpb     = [rgba(ORANGE, 0.55), rgba(ORANGE1, 0.55), rgba(ORANGE2, 0.55)]

fig_boxb = go.Figure()
for i, (d, fc, lc) in enumerate(zip(data_b, fill_bpb, colors_bpb)):
    fig_boxb.add_trace(go.Box(
        y=d, x=[i] * len(d),
        marker_color=lc, fillcolor=fc,
        line=dict(color=lc, width=2),
        boxpoints=False, showlegend=False,
        name=str(i), width=0.5,
    ))
fig_boxb.update_layout(**L(xaxis=no_ax(), yaxis=no_ax()))
save(fig_boxb, "chart_box_plot_orange", w=600, h=500)
