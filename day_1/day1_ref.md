---
marp: true
theme: default
paginate: true
html: true
style: |
  @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700;900&family=Roboto+Mono:wght@400;500&display=swap');

  :root {
    /* ── Navy palette (base → 4 lighter shades) ── */
    --navy:   #0D1A63;
    --navy-1: #253A95;
    --navy-2: #5B73C4;
    --navy-3: #A8B4DE;
    --navy-4: #DDE2F2;

    /* ── Orange palette (base → 4 lighter shades) ── */
    --orange:   #F68048;
    --orange-1: #F89B72;
    --orange-2: #FAB69B;
    --orange-3: #FDD1C3;
    --orange-4: #FEEEE8;

    /* ── Neutrals ── */
    --black: #111111;
    --white: #FFFFFF;
    --gray:  #7e7e7e;
    --line:  #E8E8EE;
  }

  /* ════════════════════════════════════
     BASE
  ════════════════════════════════════ */
  section {
    font-family: 'Roboto', 'Segoe UI', Arial, sans-serif;
    font-size: 21px;
    line-height: 1.7;
    color: var(--black);
    background: var(--white);
    padding: 56px 72px;
    box-sizing: border-box;
    text-align: justify;
  }

  /* ── Typography ── */
  h1 {
    font-family: 'Roboto', sans-serif;
    font-weight: 900;
    font-size: 2.1em;
    color: var(--navy);
    margin: 0 0 6px 0;
    line-height: 1.2;
  }

  h2 {
    font-family: 'Roboto', sans-serif;
    font-weight: 700;
    font-size: 1.45em;
    color: var(--navy);
    border-left: 6px solid var(--orange);
    padding-left: 14px;
    margin: 0 0 24px 0;
    line-height: 1.3;
  }

  h3 {
    font-family: 'Roboto', sans-serif;
    font-weight: 600;
    font-size: 1.05em;
    color: var(--navy-1);
    margin: 0 0 8px 0;
  }

  p { margin: 0 0 12px 0; }

  strong { color: var(--navy); font-weight: 700; }

  em { color: var(--navy-2); font-style: italic; }

  a { color: var(--orange); text-decoration: none; }

  /* ── Lists ── */
  ul, ol {
    margin: 4px 0 12px 0;
    padding-left: 1.5em;
  }
  li {
    margin-bottom: 6px;
    line-height: 1.6;
  }

  /* ── Code ── */
  code {
    font-family: 'Roboto Mono', monospace;
    font-size: 0.82em;
    background: var(--navy-4);
    color: var(--navy);
    padding: 2px 7px;
    border-radius: 4px;
  }

  pre {
    font-family: 'Roboto Mono', monospace;
    font-size: 0.75em;
    background: #14213D;
    color: #D0D8F0;
    border-radius: 10px;
    padding: 22px 26px;
    line-height: 1.6;
    margin: 12px 0;
    border-left: 4px solid var(--orange);
  }

  pre code {
    background: transparent;
    color: inherit;
    padding: 0;
    font-size: 1em;
  }

  /* ── Syntax highlight overrides ── */
  .hljs-string, .hljs-number { color: #F89B72; }
  .hljs-keyword             { color: #df0303; }
  .hljs-comment             { color: #7e7e7e; }
  .hljs-title, .hljs-built_in { color: #FAB69B; }

  /* ── Tables ── */
  table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.85em;
    margin: 12px 0;
  }
  th {
    background: var(--navy);
    color: var(--white);
    font-weight: 600;
    padding: 10px 14px;
    text-align: left;
    letter-spacing: 0.02em;
  }
  td {
    padding: 9px 14px;
    border-bottom: 1px solid var(--line);
    color: var(--black);
  }
  tr:nth-child(even) td { background: var(--navy-4); }
  tr:last-child td { border-bottom: none; }

  .small-table table { font-size: 0.65em; }
  .small-table th { padding: 6px 10px; }
  .small-table td { padding: 5px 10px; }

  /* ── Blockquote / callout ── */
  blockquote {
    border-left: 5px solid var(--orange);
    background: var(--orange-4);
    margin: 16px 0;
    padding: 12px 20px;
    border-radius: 0 8px 8px 0;
    font-style: normal;
    color: var(--black);
  }
  blockquote p { margin: 0; }

  /* ── Horizontal rule ── */
  hr {
    border: none;
    height: 3px;
    background: var(--orange);
    width: 64px;
    margin: 16px 0;
    border-radius: 2px;
  }

  /* ── Page number ── */
  section::after {
    font-family: 'Roboto', sans-serif;
    font-size: 0.72em;
    color: var(--navy-3);
    font-weight: 300;
  }

  /* ════════════════════════════════════
     LAYOUT HELPERS
  ════════════════════════════════════ */
  .cols  { display: grid; grid-template-columns: 1fr 1fr;       gap: 64px; }
  .cols-1-2  { display: grid; grid-template-columns: 1fr 2fr;       gap: 24px; }
  .cols-2-1  { display: grid; grid-template-columns: 2fr 1fr;       gap: 24px; }
  .cols3 { display: grid; grid-template-columns: 1fr 1fr 1fr;   gap: 24px; }
  .cols-3-2 { display: grid; grid-template-columns: 3fr 2fr;    gap: 36px; }

  /* ── Card ── */
  .card {
    background: var(--navy-4);
    border-radius: 10px;
    padding: 20px 22px;
    border-top: 5px solid var(--navy-1);
  }
  .card.warm {
    background: var(--orange-4);
    border-top-color: var(--orange);
  }
  .card.mid {
    background: var(--navy-4);
    border-top-color: var(--navy-2);
  }

  /* ── Highlight / callout box ── */
  .box {
    background: var(--orange-4);
    border-left: 5px solid var(--orange);
    border-radius: 0 8px 8px 0;
    padding: 14px 20px;
    margin: 12px 0;
  }
  .box-navy {
    background: var(--navy-4);
    border-left: 5px solid var(--navy-1);
    border-radius: 0 8px 8px 0;
    padding: 14px 20px;
    margin: 12px 0;
  }

  /* ── Badge / pill ── */
  .badge {
    display: inline-block;
    background: var(--orange);
    color: var(--white);
    font-size: 0.72em;
    font-weight: 700;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    padding: 4px 14px;
    border-radius: 20px;
  }
  .badge.navy {
    background: var(--navy);
  }
  .badge.outline {
    background: transparent;
    color: var(--navy-2);
    border: 1.5px solid var(--navy-3);
  }

  /* ════════════════════════════════════
     TITLE SLIDE
  ════════════════════════════════════ */
  section.title {
    background: var(--white);
    padding-left: 88px;
    border-left: 16px solid var(--orange);
    display: flex;
    flex-direction: column;
    justify-content: center;
  }
  section.title h1 {
    color: var(--navy);
    font-size: 2.8em;
    font-weight: 900;
    border: none;
    padding: 0;
    margin: 0 0 4px 0;
    line-height: 1.1;
  }
  section.title h2 {
    color: var(--navy-2);
    font-size: 1.35em;
    font-weight: 300;
    border: none;
    padding: 0;
    margin: 0 0 28px 0;
  }
  section.title hr {
    width: 48px;
    background: var(--orange);
    margin: 16px 0;
  }
  section.title p {
    color: var(--navy-3);
    font-size: 0.9em;
    font-weight: 300;
    margin: 0;
  }
  section.title strong {
    color: var(--navy-2);
    font-weight: 500;
  }

  /* ════════════════════════════════════
     SECTION DIVIDER
  ════════════════════════════════════ */
  section.divider {
    background: var(--white);
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;
    border-left: 16px solid var(--navy);
    padding-left: 88px;
  }
  section.divider .part-no {
    font-family: 'Roboto', sans-serif;
    font-size: 5em;
    font-weight: 900;
    color: var(--navy-4);
    line-height: 1;
    margin-bottom: -16px;
    display: block;
  }
  section.divider h1 {
    color: var(--navy);
    font-size: 2.4em;
    font-weight: 900;
    border: none;
    padding: 0;
    line-height: 1.1;
  }
  section.divider h2 {
    color: var(--navy-2);
    font-size: 1.1em;
    font-weight: 400;
    border: none;
    padding: 0;
    margin: 8px 0 0 0;
  }
  section.divider hr {
    background: var(--orange);
    margin: 14px 0;
  }

  /* ── Chart-type gallery ── */
  .chart-thumb { text-align: center; }
  .chart-thumb img { width: 100%; height: 260px; object-fit: contain; display: block; margin: 0 auto; }
  .chart-thumb p { font-size: 0.75em; font-weight: 700; color: var(--navy-1); margin: 8px 0 0 0; text-transform: uppercase; letter-spacing: 0.06em; }

  /* ── Purpose grid (4-col) ── */
  .cols4 { display: grid; grid-template-columns: 1fr 1fr 1fr 1fr; gap: 18px; }
  .cols4 h3 { text-align: center; border-bottom: 2px solid var(--orange); padding-bottom: 6px; margin-bottom: 10px; }
  .chart-thumb-sm { text-align: center; margin-bottom: 8px; }
  .chart-thumb-sm img { width: 100%; height: 110px; object-fit: contain; display: block; margin: 0 auto; }
  .chart-thumb-sm p { font-size: 0.6em; font-weight: 700; color: var(--navy); margin: 0 0 3px 0; text-transform: uppercase; letter-spacing: 0.05em; }
---

<!-- _class: divider -->

# Appendix

## FT Visual Vocabulary — Full Reference

---

## FT Visual Vocab - Deviation 

Emphasise variations (+/-) from a fixed reference point. Typically the reference point is zero but it can also be a target or a long-term average. Can also be used to show sentiment (positive/neutral/negative)

<div class="cols4">
<div class="chart-thumb-sm">
<p>bar-diverging</p>
<img src="ft_visual_vocab/deviation/Visual Vocabulary_files/bar-diverging.svg">
<div style="font-size: 0.6em; font-weight: normal; color: #444; text-transform: none; letter-spacing: normal; line-height: 1.4; margin: 8px auto 0; width: 75%; text-align: justify;">A simple standard bar chart that can handle both negative and positive magnitude values</div>
</div>
<div class="chart-thumb-sm">
<p>bar-diverging-stacked</p>
<img src="ft_visual_vocab/deviation/Visual Vocabulary_files/bar-diverging-stacked.svg">
<div style="font-size: 0.6em; font-weight: normal; color: #444; text-transform: none; letter-spacing: normal; line-height: 1.4; margin: 8px auto 0; width: 75%; text-align: justify;">Perfect for presenting survey results which involve sentiment (eg disagree, neutral, agreed</div>
</div>
<div class="chart-thumb-sm">
<p>spine-chart</p>
<img src="ft_visual_vocab/deviation/Visual Vocabulary_files/spine.svg">
<div style="font-size: 0.6em; font-weight: normal; color: #444; text-transform: none; letter-spacing: normal; line-height: 1.4; margin: 8px auto 0; width: 75%; text-align: justify;">Splits a single value into 2 contrasting components (eg Male/Female)</div>
</div>
<div class="chart-thumb-sm">
<p>line-surplus-deficit-filled</p>
<img src="ft_visual_vocab/deviation/Visual Vocabulary_files/line-surplur-defecit-fill.svg">
<div style="font-size: 0.6em; font-weight: normal; color: #444; text-transform: none; letter-spacing: normal; line-height: 1.4; margin: 8px auto 0; width: 75%; text-align: justify;">The shaded area of these charts allows a balance to be shown;  either against a baseline or between two serie</div>
</div>
</div>

<p style="font-size:0.45em; color:#7e7e7e; text-align:right; margin-top:16px;">Financial Times. (n.d.). <em>Visual vocabulary</em>. <a href="https://ft-interactive.github.io/visual-vocabulary/">https://ft-interactive.github.io/visual-vocabulary/</a></p>

---

## FT Visual Vocab - Correlation 

Show the relationship between two or more variables. Be mindful that, unless you tell them otherwise, many readers will assume the relationships you show them to be causal (i.e. one causes the other)

<div class="cols4">
<div class="chart-thumb-sm">
<p>scatterplot</p>
<img src="ft_visual_vocab/correlation/Visual Vocabulary_files/scatterplot.svg">
<div style="font-size: 0.6em; font-weight: normal; color: #444; text-transform: none; letter-spacing: normal; line-height: 1.4; margin: 8px auto 0; width: 75%; text-align: justify;">The standard way to show the relationship between two variables, each of which has its own axis</div>
</div>
<div class="chart-thumb-sm">
<p>line-column</p>
<img src="ft_visual_vocab/correlation/Visual Vocabulary_files/line-column.svg">
<div style="font-size: 0.6em; font-weight: normal; color: #444; text-transform: none; letter-spacing: normal; line-height: 1.4; margin: 8px auto 0; width: 75%; text-align: justify;">A good way of showing the relationship between an amount (columns) and a rate (line)</div>
</div>
<div class="chart-thumb-sm">
<p>scatterplot-connected</p>
<img src="ft_visual_vocab/correlation/Visual Vocabulary_files/scatterplot-connected.svg">
<div style="font-size: 0.6em; font-weight: normal; color: #444; text-transform: none; letter-spacing: normal; line-height: 1.4; margin: 8px auto 0; width: 75%; text-align: justify;">Usually used to show how the relationship between 2 variables has changed over time</div>
</div>

</div>

<p style="font-size:0.45em; color:#7e7e7e; text-align:right; margin-top:16px;">Financial Times. (n.d.). <em>Visual vocabulary</em>. <a href="https://ft-interactive.github.io/visual-vocabulary/">https://ft-interactive.github.io/visual-vocabulary/</a></p>

---

## FT Visual Vocab - Correlation (cont.)

<div class="cols4">
<div class="chart-thumb-sm">
<p>XY-heatmap</p>
<img src="ft_visual_vocab/correlation/Visual Vocabulary_files/XY-heatmap.svg">
<div style="font-size: 0.6em; font-weight: normal; color: #444; text-transform: none; letter-spacing: normal; line-height: 1.4; margin: 8px auto 0; width: 75%; text-align: justify;">A good way of showing the patterns between 2 categories of data, less good at showing fine differences in amounts</div>
</div>

<div class="chart-thumb-sm">
<p>Bubble</p>
<img src="ft_visual_vocab/correlation/Visual Vocabulary_files/bubble.svg">
<div style="font-size: 0.6em; font-weight: normal; color: #444; text-transform: none; letter-spacing: normal; line-height: 1.4; margin: 8px auto 0; width: 75%; text-align: justify;">Like a scatterplot, but adds additional detail by sizing the circles according to a third variable</div>
</div>

</div>

<p style="font-size:0.45em; color:#7e7e7e; text-align:right; margin-top:16px;">Financial Times. (n.d.). <em>Visual vocabulary</em>. <a href="https://ft-interactive.github.io/visual-vocabulary/">https://ft-interactive.github.io/visual-vocabulary/</a></p>

---

## FT Visual Vocab - Change V Time 

Give emphasis to changing trends. These can be short (intra-day) movements or extended series traversing decades or centuries: Choosing the correct time period is important to provide suitable context for the reader

<div class="cols4">
<div class="chart-thumb-sm">
<p>line</p>
<img src="ft_visual_vocab/change_v_time/Visual Vocabulary_files/line.svg">
<div style="font-size: 0.6em; font-weight: normal; color: #444; text-transform: none; letter-spacing: normal; line-height: 1.4; margin: 8px auto 0; width: 75%; text-align: justify;">The standard way to show a changing time series. If data are irregular, consider markers to represent data points</div>
</div>
<div class="chart-thumb-sm">
<p>column-timeline</p>
<img src="ft_visual_vocab/change_v_time/Visual Vocabulary_files/column-timeline.svg">
<div style="font-size: 0.6em; font-weight: normal; color: #444; text-transform: none; letter-spacing: normal; line-height: 1.4; margin: 8px auto 0; width: 75%; text-align: justify;">Columns work well for showing change over time - but usually best with only one series of data at a time</div>
</div>
<div class="chart-thumb-sm">
<p>column-line-timeline</p>
<img src="ft_visual_vocab/change_v_time/Visual Vocabulary_files/column-line-timeline.svg">
<div style="font-size: 0.6em; font-weight: normal; color: #444; text-transform: none; letter-spacing: normal; line-height: 1.4; margin: 8px auto 0; width: 75%; text-align: justify;">A good way of showing the relationship over time between an amount (columns) and a rate (line)</div>
</div>
<div class="chart-thumb-sm">
<p>stock-price</p>
<img src="ft_visual_vocab/change_v_time/Visual Vocabulary_files/stock-price.svg">
<div style="font-size: 0.6em; font-weight: normal; color: #444; text-transform: none; letter-spacing: normal; line-height: 1.4; margin: 8px auto 0; width: 75%; text-align: justify;">Usually focused on day-to-day activity, these charts show opening/closing and hi/low points of each day</div>
</div>
</div>

<p style="font-size:0.45em; color:#7e7e7e; text-align:right; margin-top:16px;">Financial Times. (n.d.). <em>Visual vocabulary</em>. <a href="https://ft-interactive.github.io/visual-vocabulary/">https://ft-interactive.github.io/visual-vocabulary/</a></p>

---

## FT Visual Vocab - Change V Time (cont.)

<div class="cols4">
<div class="chart-thumb-sm">
<p>slope</p>
<img src="ft_visual_vocab/change_v_time/Visual Vocabulary_files/slope-timeline.svg">
<div style="font-size: 0.6em; font-weight: normal; color: #444; text-transform: none; letter-spacing: normal; line-height: 1.4; margin: 8px auto 0; width: 75%; text-align: justify;">Good for showing changing data as long as the data can be simplified into 2 or 3 points without missing a key part of story</div>
</div>
<div class="chart-thumb-sm">
<p>area</p>
<img src="ft_visual_vocab/change_v_time/Visual Vocabulary_files/area.svg">
<div style="font-size: 0.6em; font-weight: normal; color: #444; text-transform: none; letter-spacing: normal; line-height: 1.4; margin: 8px auto 0; width: 75%; text-align: justify;">Use with care. These are good at showing changes to total, but seeing change in components can be very difficult.</div>
</div>
<div class="chart-thumb-sm">
<p>fan</p>
<img src="ft_visual_vocab/change_v_time/Visual Vocabulary_files/fan.svg">
<div style="font-size: 0.6em; font-weight: normal; color: #444; text-transform: none; letter-spacing: normal; line-height: 1.4; margin: 8px auto 0; width: 75%; text-align: justify;">Use to show the uncertainty in future projections - usually this grows the further forward to projection</div>
</div>
<div class="chart-thumb-sm">
<p>scatterplot-line-timeline</p>
<img src="ft_visual_vocab/change_v_time/Visual Vocabulary_files/scatterplot-line-timeline.svg">
<div style="font-size: 0.6em; font-weight: normal; color: #444; text-transform: none; letter-spacing: normal; line-height: 1.4; margin: 8px auto 0; width: 75%; text-align: justify;">A good way of showing changing data for two variables whenever there is a relatively clear pattern of progression. Connected scatterplot</div>
</div>
</div>

<p style="font-size:0.45em; color:#7e7e7e; text-align:right; margin-top:16px;">Financial Times. (n.d.). <em>Visual vocabulary</em>. <a href="https://ft-interactive.github.io/visual-vocabulary/">https://ft-interactive.github.io/visual-vocabulary/</a></p>

---

## FT Visual Vocab - Change V Time (cont.)

<div class="cols4">
<div class="chart-thumb-sm">
<p>calendar-heatmap</p>
<img src="ft_visual_vocab/change_v_time/Visual Vocabulary_files/calendar-heatmap.svg">
<div style="font-size: 0.6em; font-weight: normal; color: #444; text-transform: none; letter-spacing: normal; line-height: 1.4; margin: 8px auto 0; width: 75%; text-align: justify;">A great way of showing temporal patterns (daily, weekly, monthly), at the expense of showing precision in quantity</div>
</div>
<div class="chart-thumb-sm">
<p>priestley timeline</p>
<img src="ft_visual_vocab/change_v_time/Visual Vocabulary_files/priestley-timeline.svg">
<div style="font-size: 0.6em; font-weight: normal; color: #444; text-transform: none; letter-spacing: normal; line-height: 1.4; margin: 8px auto 0; width: 75%; text-align: justify;">Great when date and duration are key elements of the story in the data</div>
</div>
<div class="chart-thumb-sm">
<p>circles-timeline</p>
<img src="ft_visual_vocab/change_v_time/Visual Vocabulary_files/circle-timeline.svg">
<div style="font-size: 0.6em; font-weight: normal; color: #444; text-transform: none; letter-spacing: normal; line-height: 1.4; margin: 8px auto 0; width: 75%; text-align: justify;">Good for showing discrete values of varying size across multiple categories (eg earthquakes by contintent)</div>
</div>
<div class="chart-thumb-sm">
<p>seismogram</p>
<img src="ft_visual_vocab/change_v_time/Visual Vocabulary_files/seismogram.svg">
<div style="font-size: 0.6em; font-weight: normal; color: #444; text-transform: none; letter-spacing: normal; line-height: 1.4; margin: 8px auto 0; width: 75%; text-align: justify;">Another alternative to the circle timeline for showing series where there are big variations in the data</div>
</div>
</div>

<p style="font-size:0.45em; color:#7e7e7e; text-align:right; margin-top:16px;">Financial Times. (n.d.). <em>Visual vocabulary</em>. <a href="https://ft-interactive.github.io/visual-vocabulary/">https://ft-interactive.github.io/visual-vocabulary/</a></p>

---

## FT Visual Vocab - Ranking 

Use where an item's position in an ordered list is more important than its absolute or relative value. Don't be afraid to highlight the points of interest.

<div class="cols4">
<div class="chart-thumb-sm">
<p>bar-ordered</p>
<img src="ft_visual_vocab/ranking/Visual Vocabulary_files/bar-ordered.svg">
<div style="font-size: 0.6em; font-weight: normal; color: #444; text-transform: none; letter-spacing: normal; line-height: 1.4; margin: 8px auto 0; width: 75%; text-align: justify;">Standard bar charts display the ranks of values much more easily when sorted into order</div>
</div>
<div class="chart-thumb-sm">
<p>column-ordered</p>
<img src="ft_visual_vocab/ranking/Visual Vocabulary_files/column-ordered.svg">
<div style="font-size: 0.6em; font-weight: normal; color: #444; text-transform: none; letter-spacing: normal; line-height: 1.4; margin: 8px auto 0; width: 75%; text-align: justify;">Standard column charts display the ranks of values much more easily when sorted into order</div>
</div>
<div class="chart-thumb-sm">
<p>symbol-proportional-ordered</p>
<img src="ft_visual_vocab/ranking/Visual Vocabulary_files/symbol-proportional-ordered.svg">
<div style="font-size: 0.6em; font-weight: normal; color: #444; text-transform: none; letter-spacing: normal; line-height: 1.4; margin: 8px auto 0; width: 75%; text-align: justify;">Use when there are big variations between values and/or seeing fine differences between data is not so important.</div>
</div>
<div class="chart-thumb-sm">
<p>dot-plot-strip</p>
<img src="ft_visual_vocab/ranking/Visual Vocabulary_files/dot-plot-strip.svg">
<div style="font-size: 0.6em; font-weight: normal; color: #444; text-transform: none; letter-spacing: normal; line-height: 1.4; margin: 8px auto 0; width: 75%; text-align: justify;">Dots placed in order on a strip are a space-efficient method of laying out ranks across multiple categories.</div>
</div>
</div>

<p style="font-size:0.45em; color:#7e7e7e; text-align:right; margin-top:16px;">Financial Times. (n.d.). <em>Visual vocabulary</em>. <a href="https://ft-interactive.github.io/visual-vocabulary/">https://ft-interactive.github.io/visual-vocabulary/</a></p>

---

## FT Visual Vocab - Ranking (cont.)

<div class="cols4">
<div class="chart-thumb-sm">
<p>slope</p>
<img src="ft_visual_vocab/ranking/Visual Vocabulary_files/slope-ranking.svg">
<div style="font-size: 0.6em; font-weight: normal; color: #444; text-transform: none; letter-spacing: normal; line-height: 1.4; margin: 8px auto 0; width: 75%; text-align: justify;">Perfect for showing how ranks have changed over time or vary between categories.</div>
</div>
<div class="chart-thumb-sm">
<p>lollipop-h</p>
<img src="ft_visual_vocab/ranking/Visual Vocabulary_files/lollipop-h.svg">
<div style="font-size: 0.6em; font-weight: normal; color: #444; text-transform: none; letter-spacing: normal; line-height: 1.4; margin: 8px auto 0; width: 75%; text-align: justify;">Lollipop charts draw more attention to the data value than standard bar/column and can also show rank effectively</div>
</div>
<div class="chart-thumb-sm">
<p>lollipop-v</p>
<img src="ft_visual_vocab/ranking/Visual Vocabulary_files/lollipop-v.svg">
<div style="font-size: 0.6em; font-weight: normal; color: #444; text-transform: none; letter-spacing: normal; line-height: 1.4; margin: 8px auto 0; width: 75%; text-align: justify;">Lollipop charts draw more attention to the data value than standard bar/column and can also show rank effectively</div>
</div>
<div class="chart-thumb-sm">
<p>bump</p>
<img src="ft_visual_vocab/ranking/Visual Vocabulary_files/bump.svg">
<div style="font-size: 0.6em; font-weight: normal; color: #444; text-transform: none; letter-spacing: normal; line-height: 1.4; margin: 8px auto 0; width: 75%; text-align: justify;"></div>
</div>
</div>

<p style="font-size:0.45em; color:#7e7e7e; text-align:right; margin-top:16px;">Financial Times. (n.d.). <em>Visual vocabulary</em>. <a href="https://ft-interactive.github.io/visual-vocabulary/">https://ft-interactive.github.io/visual-vocabulary/</a></p>

---

## FT Visual Vocab - Distribution 

Show values in a dataset and how often they occur. The shape (or 'skew') of a distribution can be a memorable way of highlighting the lack of uniformity or equality in the data

<div class="cols4">
<div class="chart-thumb-sm">
<p>histogram</p>
<img src="ft_visual_vocab/distribution/Visual Vocabulary_files/histogram.svg">
<div style="font-size: 0.6em; font-weight: normal; color: #444; text-transform: none; letter-spacing: normal; line-height: 1.4; margin: 8px auto 0; width: 75%; text-align: justify;">The standard way to show a statistical distribution - keep the gaps between columns small to highlight the 'shape' of the data.</div>
</div>
<div class="chart-thumb-sm">
<p>boxplot</p>
<img src="ft_visual_vocab/distribution/Visual Vocabulary_files/boxplot.svg">
<div style="font-size: 0.6em; font-weight: normal; color: #444; text-transform: none; letter-spacing: normal; line-height: 1.4; margin: 8px auto 0; width: 75%; text-align: justify;">Summarise multiple distributions by showing the median (centre) and range of the data</div>
</div>
<div class="chart-thumb-sm">
<p>violin</p>
<img src="ft_visual_vocab/distribution/Visual Vocabulary_files/violin.svg">
<div style="font-size: 0.6em; font-weight: normal; color: #444; text-transform: none; letter-spacing: normal; line-height: 1.4; margin: 8px auto 0; width: 75%; text-align: justify;">Similar to a box plot but more effective with complex distributions (data that cannot be summarised with simple average).</div>
</div>
<div class="chart-thumb-sm">
<p>population-pyramis</p>
<img src="ft_visual_vocab/distribution/Visual Vocabulary_files/population-pyramis.svg">
<div style="font-size: 0.6em; font-weight: normal; color: #444; text-transform: none; letter-spacing: normal; line-height: 1.4; margin: 8px auto 0; width: 75%; text-align: justify;">A standard way for showing the age and sex breakdown of a population distribution; effectively, back to back histograms</div>
</div>
</div>

<p style="font-size:0.45em; color:#7e7e7e; text-align:right; margin-top:16px;">Financial Times. (n.d.). <em>Visual vocabulary</em>. <a href="https://ft-interactive.github.io/visual-vocabulary/">https://ft-interactive.github.io/visual-vocabulary/</a></p>

---

## FT Visual Vocab - Distribution (cont.)

<div class="cols4">
<div class="chart-thumb-sm">
<p>dot-plot-strip</p>
<img src="ft_visual_vocab/distribution/Visual Vocabulary_files/dot-plot-strip-distribution.svg">
<div style="font-size: 0.6em; font-weight: normal; color: #444; text-transform: none; letter-spacing: normal; line-height: 1.4; margin: 8px auto 0; width: 75%; text-align: justify;">Good for showing individual values in a distribution, can be a problem when too many dots have the same value</div>
</div>
<div class="chart-thumb-sm">
<p>dot-plot</p>
<img src="ft_visual_vocab/distribution/Visual Vocabulary_files/dot-plot.svg">
<div style="font-size: 0.6em; font-weight: normal; color: #444; text-transform: none; letter-spacing: normal; line-height: 1.4; margin: 8px auto 0; width: 75%; text-align: justify;">A simple way of showing the range (min/max) of data across multiple categories.</div>
</div>
<div class="chart-thumb-sm">
<p>barcode</p>
<img src="ft_visual_vocab/distribution/Visual Vocabulary_files/barcode.svg">
<div style="font-size: 0.6em; font-weight: normal; color: #444; text-transform: none; letter-spacing: normal; line-height: 1.4; margin: 8px auto 0; width: 75%; text-align: justify;">Like dot strip plots, good for displaying all the data in a table,they work best when highlighting individual values.</div>
</div>
<div class="chart-thumb-sm">
<p>cumulative-curve</p>
<img src="ft_visual_vocab/distribution/Visual Vocabulary_files/cumulative-curve.svg">
<div style="font-size: 0.6em; font-weight: normal; color: #444; text-transform: none; letter-spacing: normal; line-height: 1.4; margin: 8px auto 0; width: 75%; text-align: justify;">A good way of showing how unequal a distribution is: y axis is always cumulative frequency, x axis is always a measure.</div>
</div>
</div>

<p style="font-size:0.45em; color:#7e7e7e; text-align:right; margin-top:16px;">Financial Times. (n.d.). <em>Visual vocabulary</em>. <a href="https://ft-interactive.github.io/visual-vocabulary/">https://ft-interactive.github.io/visual-vocabulary/</a></p>

---

## FT Visual Vocab - Part Of Whole 

Show how a single entity can be broken down into its component elements. If the reader's interest is solely in the size of the components, consider a magnitude-type chart instead

<div class="cols4">
<div class="chart-thumb-sm">
<p>column-stacked</p>
<img src="ft_visual_vocab/part_of_whole/Visual Vocabulary_files/column-stacked.svg">
<div style="font-size: 0.6em; font-weight: normal; color: #444; text-transform: none; letter-spacing: normal; line-height: 1.4; margin: 8px auto 0; width: 75%; text-align: justify;">A simple way of showing part-to-whole relationships but can be difficult to read with more than a few components.</div>
</div>
<div class="chart-thumb-sm">
<p>bar-stacked-proportional</p>
<img src="ft_visual_vocab/part_of_whole/Visual Vocabulary_files/bar-stacked-proportional.svg">
<div style="font-size: 0.6em; font-weight: normal; color: #444; text-transform: none; letter-spacing: normal; line-height: 1.4; margin: 8px auto 0; width: 75%; text-align: justify;">A good way of showing the size and proportion of data at the same time, as long as the data are not too complicated.</div>
</div>

<div class="chart-thumb-sm">
<p>doughnut</p>
<img src="ft_visual_vocab/part_of_whole/Visual Vocabulary_files/doughnut.svg">
<div style="font-size: 0.6em; font-weight: normal; color: #444; text-transform: none; letter-spacing: normal; line-height: 1.4; margin: 8px auto 0; width: 75%; text-align: justify;">Similar to a pie chart - but the centre can be a good way of making space to include more information about the data (eg. total)</div>
</div>
</div>

<p style="font-size:0.45em; color:#7e7e7e; text-align:right; margin-top:16px;">Financial Times. (n.d.). <em>Visual vocabulary</em>. <a href="https://ft-interactive.github.io/visual-vocabulary/">https://ft-interactive.github.io/visual-vocabulary/</a></p>

---

## FT Visual Vocab - Part Of Whole (cont.)

<div class="cols4">
<div class="chart-thumb-sm">
<p>treemap</p>
<img src="ft_visual_vocab/part_of_whole/Visual Vocabulary_files/treemap.svg">
<div style="font-size: 0.6em; font-weight: normal; color: #444; text-transform: none; letter-spacing: normal; line-height: 1.4; margin: 8px auto 0; width: 75%; text-align: justify;">Use for hierarchical part-to-whole relationships; can be difficult to read when there are many small segments</div>
</div>
<div class="chart-thumb-sm">
<p>Voronoi</p>
<img src="ft_visual_vocab/part_of_whole/Visual Vocabulary_files/voronoi.svg">
<div style="font-size: 0.6em; font-weight: normal; color: #444; text-transform: none; letter-spacing: normal; line-height: 1.4; margin: 8px auto 0; width: 75%; text-align: justify;">A way of turning points into areas - any point within the area is closer to the central point than any other point</div>
</div>
<div class="chart-thumb-sm">
<p>sunburst</p>
<img src="ft_visual_vocab/part_of_whole/Visual Vocabulary_files/sunburst.svg">
<div style="font-size: 0.6em; font-weight: normal; color: #444; text-transform: none; letter-spacing: normal; line-height: 1.4; margin: 8px auto 0; width: 75%; text-align: justify;">Another way of visualisaing hierarchical part-to-whole relationships. Use sparingly (if at all) for obvious reasons.</div>
</div>
<div class="chart-thumb-sm">
<p>arc</p>
<img src="ft_visual_vocab/part_of_whole/Visual Vocabulary_files/arc.svg">
<div style="font-size: 0.6em; font-weight: normal; color: #444; text-transform: none; letter-spacing: normal; line-height: 1.4; margin: 8px auto 0; width: 75%; text-align: justify;">A hemicycle, often used for visualising political results.</div>
</div>
</div>

<p style="font-size:0.45em; color:#7e7e7e; text-align:right; margin-top:16px;">Financial Times. (n.d.). <em>Visual vocabulary</em>. <a href="https://ft-interactive.github.io/visual-vocabulary/">https://ft-interactive.github.io/visual-vocabulary/</a></p>

---

## FT Visual Vocab - Part Of Whole (cont.)

<div class="cols4">
<div class="chart-thumb-sm">
<p>gridplot</p>
<img src="ft_visual_vocab/part_of_whole/Visual Vocabulary_files/gridplot.svg">
<div style="font-size: 0.6em; font-weight: normal; color: #444; text-transform: none; letter-spacing: normal; line-height: 1.4; margin: 8px auto 0; width: 75%; text-align: justify;">Good for showing % information, they work best when used on whole numbers and work well in multiple layout form.</div>
</div>
<div class="chart-thumb-sm">
<p>Venn</p>
<img src="ft_visual_vocab/part_of_whole/Visual Vocabulary_files/venn.svg">
<div style="font-size: 0.6em; font-weight: normal; color: #444; text-transform: none; letter-spacing: normal; line-height: 1.4; margin: 8px auto 0; width: 75%; text-align: justify;">Generally only used for schematic representation</div>
</div>
<div class="chart-thumb-sm">
<p>Waterfall</p>
<img src="ft_visual_vocab/part_of_whole/Visual Vocabulary_files/waterfall.svg">
<div style="font-size: 0.6em; font-weight: normal; color: #444; text-transform: none; letter-spacing: normal; line-height: 1.4; margin: 8px auto 0; width: 75%; text-align: justify;">Can be useful for showing part-to-whole relationships where some of the components are negative.</div>
</div>
</div>

<p style="font-size:0.45em; color:#7e7e7e; text-align:right; margin-top:16px;">Financial Times. (n.d.). <em>Visual vocabulary</em>. <a href="https://ft-interactive.github.io/visual-vocabulary/">https://ft-interactive.github.io/visual-vocabulary/</a></p>

---

## FT Visual Vocab - Magnitude 

Show size comparisons. These can be relative (just being able to see larger/bigger) or absolute (need to see fine differences). Usually these show a 'counted' number (for example, barrels, dollars or people) rather than a calculated rate or per cent

<div class="cols4">
<div class="chart-thumb-sm">
<p>Column</p>
<img src="ft_visual_vocab/magnitude/Visual Vocabulary_files/column-magnitude.svg">
<div style="font-size: 0.6em; font-weight: normal; color: #444; text-transform: none; letter-spacing: normal; line-height: 1.4; margin: 8px auto 0; width: 75%; text-align: justify;">The standard way to compare the size of things. Must always start at 0 on the axis</div>
</div>
<div class="chart-thumb-sm">
<p>Bar</p>
<img src="ft_visual_vocab/magnitude/Visual Vocabulary_files/bar-magnitude.svg">
<div style="font-size: 0.6em; font-weight: normal; color: #444; text-transform: none; letter-spacing: normal; line-height: 1.4; margin: 8px auto 0; width: 75%; text-align: justify;">The standard way to compare the size of things. Must always start at 0 on the axis. Good when the data are not time series and labels have long category names</div>
</div>
<div class="chart-thumb-sm">
<p>column-grouped</p>
<img src="ft_visual_vocab/magnitude/Visual Vocabulary_files/column-grouped.svg">
<div style="font-size: 0.6em; font-weight: normal; color: #444; text-transform: none; letter-spacing: normal; line-height: 1.4; margin: 8px auto 0; width: 75%; text-align: justify;">As per standard column but allows for multiple series. Can become tricky to read with more than 2 series</div>
</div>
<div class="chart-thumb-sm">
<p>bar-grouped</p>
<img src="ft_visual_vocab/magnitude/Visual Vocabulary_files/bar-grouped-magnitude.svg">
<div style="font-size: 0.6em; font-weight: normal; color: #444; text-transform: none; letter-spacing: normal; line-height: 1.4; margin: 8px auto 0; width: 75%; text-align: justify;">As per standard bar but allows for multiple series. Can become tricky to read with more than 2 series</div>
</div>
</div>

<p style="font-size:0.45em; color:#7e7e7e; text-align:right; margin-top:16px;">Financial Times. (n.d.). <em>Visual vocabulary</em>. <a href="https://ft-interactive.github.io/visual-vocabulary/">https://ft-interactive.github.io/visual-vocabulary/</a></p>

---

## FT Visual Vocab - Magnitude (cont.)

<div class="cols4">
<div class="chart-thumb-sm">
<p>bar-stacked-proportional</p>
<img src="ft_visual_vocab/magnitude/Visual Vocabulary_files/bar-stacked-proportional-magnitude.svg">
<div style="font-size: 0.6em; font-weight: normal; color: #444; text-transform: none; letter-spacing: normal; line-height: 1.4; margin: 8px auto 0; width: 75%; text-align: justify;">A good way of showing the size and proportion of data at the same time - as long as the data are not too complicated</div>
</div>
<div class="chart-thumb-sm">
<p>symbol-proportional</p>
<img src="ft_visual_vocab/magnitude/Visual Vocabulary_files/symbol-proportional.svg">
<div style="font-size: 0.6em; font-weight: normal; color: #444; text-transform: none; letter-spacing: normal; line-height: 1.4; margin: 8px auto 0; width: 75%; text-align: justify;">Use when there are big variations between values and/or seeing fne differences between data is not so important</div>
</div>
<div class="chart-thumb-sm">
<p>isotope (pictogram)</p>
<img src="ft_visual_vocab/magnitude/Visual Vocabulary_files/isotope.svg">
<div style="font-size: 0.6em; font-weight: normal; color: #444; text-transform: none; letter-spacing: normal; line-height: 1.4; margin: 8px auto 0; width: 75%; text-align: justify;">Excellent solution in some instances - use only with whole numbers (do not slice off an arm to represent a decimal).</div>
</div>
<div class="chart-thumb-sm">
<p>lollipop-h</p>
<img src="ft_visual_vocab/magnitude/Visual Vocabulary_files/lollipop-h-magnitude.svg">
<div style="font-size: 0.6em; font-weight: normal; color: #444; text-transform: none; letter-spacing: normal; line-height: 1.4; margin: 8px auto 0; width: 75%; text-align: justify;">Lollipop charts draw more attention to the data value than standard bar/column and can also show rank effectively</div>
</div>
</div>

<p style="font-size:0.45em; color:#7e7e7e; text-align:right; margin-top:16px;">Financial Times. (n.d.). <em>Visual vocabulary</em>. <a href="https://ft-interactive.github.io/visual-vocabulary/">https://ft-interactive.github.io/visual-vocabulary/</a></p>

---

## FT Visual Vocab - Magnitude (cont.)

<div class="cols4">
<div class="chart-thumb-sm">
<p>lollipop-v</p>
<img src="ft_visual_vocab/magnitude/Visual Vocabulary_files/lollipop-v-magnitude.svg">
<div style="font-size: 0.6em; font-weight: normal; color: #444; text-transform: none; letter-spacing: normal; line-height: 1.4; margin: 8px auto 0; width: 75%; text-align: justify;">Lollipop charts draw more attention to the data value than standard bar/column and can also show rank effectively</div>
</div>
<div class="chart-thumb-sm">
<p>Radar</p>
<img src="ft_visual_vocab/magnitude/Visual Vocabulary_files/radar.svg">
<div style="font-size: 0.6em; font-weight: normal; color: #444; text-transform: none; letter-spacing: normal; line-height: 1.4; margin: 8px auto 0; width: 75%; text-align: justify;">A space-efficient way of showing value pf multiple variables -  but make sure they are organised in a way that makes sense to reader.</div>
</div>
<div class="chart-thumb-sm">
<p>Bullet</p>
<img src="ft_visual_vocab/magnitude/Visual Vocabulary_files/bullet.svg">
<div style="font-size: 0.6em; font-weight: normal; color: #444; text-transform: none; letter-spacing: normal; line-height: 1.4; margin: 8px auto 0; width: 75%; text-align: justify;"></div>
</div>
<div class="chart-thumb-sm">
<p>Parallel coordinates</p>
<img src="ft_visual_vocab/magnitude/Visual Vocabulary_files/parallel coordinates.svg">
<div style="font-size: 0.6em; font-weight: normal; color: #444; text-transform: none; letter-spacing: normal; line-height: 1.4; margin: 8px auto 0; width: 75%; text-align: justify;">An alternative to radar charts - again, the arrngement of the variables is important. Usually benefits from highlighting values</div>
</div>
</div>

<p style="font-size:0.45em; color:#7e7e7e; text-align:right; margin-top:16px;">Financial Times. (n.d.). <em>Visual vocabulary</em>. <a href="https://ft-interactive.github.io/visual-vocabulary/">https://ft-interactive.github.io/visual-vocabulary/</a></p>

---

## FT Visual Vocab - Spatial 

Used only when precise locations or geographical patterns in data are more important to the reader than anything else.

<div class="cols4">
<div class="chart-thumb-sm">
<p>basic-choropleth</p>
<img src="ft_visual_vocab/spatial/Visual Vocabulary_files/basic-choropleth.svg">
<div style="font-size: 0.6em; font-weight: normal; color: #444; text-transform: none; letter-spacing: normal; line-height: 1.4; margin: 8px auto 0; width: 75%; text-align: justify;">The standard approach for putting data on a map - should always be rates rather than totals and use a sensible base geography.</div>
</div>
<div class="chart-thumb-sm">
<p>proportional-symbol</p>
<img src="ft_visual_vocab/spatial/Visual Vocabulary_files/proportional-symbol.svg">
<div style="font-size: 0.6em; font-weight: normal; color: #444; text-transform: none; letter-spacing: normal; line-height: 1.4; margin: 8px auto 0; width: 75%; text-align: justify;">Use for totals rather than rates  - be wary that small differences in data will be hard to see.</div>
</div>
<div class="chart-thumb-sm">
<p>flow</p>
<img src="ft_visual_vocab/spatial/Visual Vocabulary_files/flow.svg">
<div style="font-size: 0.6em; font-weight: normal; color: #444; text-transform: none; letter-spacing: normal; line-height: 1.4; margin: 8px auto 0; width: 75%; text-align: justify;">For showing unambiguous movement across a map</div>
</div>
<div class="chart-thumb-sm">
<p>contour</p>
<img src="ft_visual_vocab/spatial/Visual Vocabulary_files/contour.svg">
<div style="font-size: 0.6em; font-weight: normal; color: #444; text-transform: none; letter-spacing: normal; line-height: 1.4; margin: 8px auto 0; width: 75%; text-align: justify;">For showing areas of equal value on a map. Can use deviation colour schemes for showing +/- values</div>
</div>
</div>

<p style="font-size:0.45em; color:#7e7e7e; text-align:right; margin-top:16px;">Financial Times. (n.d.). <em>Visual vocabulary</em>. <a href="https://ft-interactive.github.io/visual-vocabulary/">https://ft-interactive.github.io/visual-vocabulary/</a></p>

---

## FT Visual Vocab - Spatial (cont.)

<div class="cols4">
<div class="chart-thumb-sm">
<p>equalised-cartogram</p>
<img src="ft_visual_vocab/spatial/Visual Vocabulary_files/equalised-cartogram.svg">
<div style="font-size: 0.6em; font-weight: normal; color: #444; text-transform: none; letter-spacing: normal; line-height: 1.4; margin: 8px auto 0; width: 75%; text-align: justify;">Converting each unit on a map to a regular and equally-sized shape - good for representing voting regions with equal share.</div>
</div>
<div class="chart-thumb-sm">
<p>scaled-cartogram-value</p>
<img src="ft_visual_vocab/spatial/Visual Vocabulary_files/scaled-cartogram-value.svg">
<div style="font-size: 0.6em; font-weight: normal; color: #444; text-transform: none; letter-spacing: normal; line-height: 1.4; margin: 8px auto 0; width: 75%; text-align: justify;">Stretching and shrinking a map so that each area is sized according to a particular value.</div>
</div>
<div class="chart-thumb-sm">
<p>dot-density</p>
<img src="ft_visual_vocab/spatial/Visual Vocabulary_files/dot-density.svg">
<div style="font-size: 0.6em; font-weight: normal; color: #444; text-transform: none; letter-spacing: normal; line-height: 1.4; margin: 8px auto 0; width: 75%; text-align: justify;">Used to show the location of individual events/locations - make sure to annotate any patterns the reader should see.</div>
</div>
<div class="chart-thumb-sm">
<p>heat-map</p>
<img src="ft_visual_vocab/spatial/Visual Vocabulary_files/heat-map.svg">
<div style="font-size: 0.6em; font-weight: normal; color: #444; text-transform: none; letter-spacing: normal; line-height: 1.4; margin: 8px auto 0; width: 75%; text-align: justify;">Grid-based data values mapped with an intensity colour scale. As choropleth map - but not snapped to an admin/political unit.</div>
</div>
</div>

<p style="font-size:0.45em; color:#7e7e7e; text-align:right; margin-top:16px;">Financial Times. (n.d.). <em>Visual vocabulary</em>. <a href="https://ft-interactive.github.io/visual-vocabulary/">https://ft-interactive.github.io/visual-vocabulary/</a></p>

---

## FT Visual Vocab - Flow 

Show the reader volumes or intensity of movement between two or more states or conditions. These might be logical sequences or geographical locations

<div class="cols4">
<div class="chart-thumb-sm">
<p>sankey</p>
<img src="ft_visual_vocab/flow/Visual Vocabulary_files/sankey.svg">
<div style="font-size: 0.6em; font-weight: normal; color: #444; text-transform: none; letter-spacing: normal; line-height: 1.4; margin: 8px auto 0; width: 75%; text-align: justify;">Shows changes in flows from one condition to at least one other; good for tracing the eventual outcome of a complex process.</div>
</div>
<div class="chart-thumb-sm">
<p>waterfall</p>
<img src="ft_visual_vocab/flow/Visual Vocabulary_files/waterfall-flow.svg">
<div style="font-size: 0.6em; font-weight: normal; color: #444; text-transform: none; letter-spacing: normal; line-height: 1.4; margin: 8px auto 0; width: 75%; text-align: justify;">Designed to show the sequencing of data through a flow process, typically budgets. Can include +/- components</div>
</div>
<div class="chart-thumb-sm">
<p>chord</p>
<img src="ft_visual_vocab/flow/Visual Vocabulary_files/chord.svg">
<div style="font-size: 0.6em; font-weight: normal; color: #444; text-transform: none; letter-spacing: normal; line-height: 1.4; margin: 8px auto 0; width: 75%; text-align: justify;">A complex but powerful diagram which can illustrate 2-way flows (and net winner) in a matrix</div>
</div>
<div class="chart-thumb-sm">
<p>network</p>
<img src="ft_visual_vocab/flow/Visual Vocabulary_files/network.svg">
<div style="font-size: 0.6em; font-weight: normal; color: #444; text-transform: none; letter-spacing: normal; line-height: 1.4; margin: 8px auto 0; width: 75%; text-align: justify;">Used for showing the complexity and inter-connectdness of relationships of varying types.</div>
</div>
</div>

<p style="font-size:0.45em; color:#7e7e7e; text-align:right; margin-top:16px;">Financial Times. (n.d.). <em>Visual vocabulary</em>. <a href="https://ft-interactive.github.io/visual-vocabulary/">https://ft-interactive.github.io/visual-vocabulary/</a></p>
