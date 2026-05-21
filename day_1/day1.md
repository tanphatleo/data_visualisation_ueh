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
  .cols  { display: grid; grid-template-columns: 1fr 1fr;       gap: 36px; }
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
---

<!-- _class: title -->

# Data Visualisation
## Day 1 — From Data to Insight

---

**Course Introduction · Data Fundamentals · Tools · Data Types**

*9-week programme · Excel · Google Sheets · Python*

---

## Agenda — Day 1

<div class="cols">

<div>

**Morning**
1. Data → Information → Insight
2. Why visualisation matters
3. The visualisation workflow
4. Our three tools

</div>

<div>

**Afternoon**
5. Data types — the full picture
6. Which data type → which chart?
7. Hands-on exercise
8. Q & A + homework

</div>

</div>

<br>

> By end of day you will understand **what data is**, **what it becomes**, and **how we work with it** for the rest of this course.

---

<!-- _class: divider -->

<span class="part-no">01</span>

# What Is Data?

## And Why Does It Matter?


---

## Data · Information · Insight

<div class="cols-1-2">
<div style="margin-right: px;">

A single transaction:
![w:300px](images/sample_imvoice.png)

</div>
<div>

Table record each transaction:

<div class="small-table">

| Date       | Invoice | Customer       | Product     | Qty | Unit Price | Total   |
|------------|---------|----------------|-------------|-----|------------|---------|
| 2024-01-03 | INV-001 | Alice Johnson  | Laptop X1   |   1 |     $899   |   $899  |
| 2024-02-14 | INV-002 | Bob Martinez   | Mouse Pro   |   3 |     $120   |   $360  |
| 2024-03-07 | INV-003 | Carol White    | Laptop X1   |   1 |     $899   |   $899  |
| 2024-01-22 | INV-004 | David Lee      | Keyboard K2 |   2 |     $150   |   $300  |
| 2024-04-11 | INV-005 | Emma Brown     | Monitor 27" |   1 |     $450   |   $450  |
| 2024-05-03 | INV-006 | Frank Wilson   | Mouse Pro   |   2 |     $120   |   $240  |
| 2024-02-28 | INV-007 | Grace Taylor   | Laptop X1   |   1 |     $899   |   $899  |
| 2024-06-15 | INV-008 | Henry Clark    | Monitor 27" |   2 |     $450   |   $900  |
| 2024-03-19 | INV-009 | Irene Scott    | Keyboard K2 |   1 |     $150   |   $150  |
| 2024-05-27 | INV-010 | James Rivera   | Mouse Pro   |   5 |     $120   |   $600  |
|...|

</div>

</div>

</div>


---

## Data · Information · Insight

<div class="cols-2-1">
<div>
Table record each transaction:
<div class="small-table">

| Date       | Invoice | Customer       | Product     | Qty | Unit Price | Total   |
|------------|---------|----------------|-------------|-----|------------|---------|
| 2024-01-03 | INV-001 | Alice Johnson  | Laptop X1   |   1 |     $899   |   $899  |
| 2024-02-14 | INV-002 | Bob Martinez   | Mouse Pro   |   3 |     $120   |   $360  |
| 2024-03-07 | INV-003 | Carol White    | Laptop X1   |   1 |     $899   |   $899  |
| 2024-01-22 | INV-004 | David Lee      | Keyboard K2 |   2 |     $150   |   $300  |
| 2024-04-11 | INV-005 | Emma Brown     | Monitor 27" |   1 |     $450   |   $450  |
| 2024-05-03 | INV-006 | Frank Wilson   | Mouse Pro   |   2 |     $120   |   $240  |
| 2024-02-28 | INV-007 | Grace Taylor   | Laptop X1   |   1 |     $899   |   $899  |
| 2024-06-15 | INV-008 | Henry Clark    | Monitor 27" |   2 |     $450   |   $900  |
| 2024-03-19 | INV-009 | Irene Scott    | Keyboard K2 |   1 |     $150   |   $150  |
| 2024-05-27 | INV-010 | James Rivera   | Mouse Pro   |   5 |     $120   |   $600  |
| ... |

</div>

</div>
  
<div>

Sum of transactions by month:

| Month | Revenue |
|---|---|
| Jan | 42 |
| Feb | 55 |
| Mar | 48 |
| Apr | 62 |
| May | 78 |
| Jun | 85 |

</div>
</div>

---

## Data · Information · Insight

<div class="cols3">

<div class="card">

### 📥 Data
Raw, unprocessed facts — no context, no meaning.

<br>

`42, 87, 13, 56`

`2024-01-03, North, 5000`

</div>

<div class="card mid">

### 📊 Information
Data **with context** — structured, labelled, comparable.

<br>

*"Monthly revenue Jan–Apr: 42k, 87k, 13k, 56k USD"*

</div>

<div class="card warm">

### 💡 Insight
Information that drives **action** — the "so what?" answer.

<br>

*"Revenue collapsed in March — investigate supply chain."*

</div>

</div>

<br>

> **Visualisation is the bridge** that turns information into insight at a glance.

---

## Why Visualisation Matters

<div class="cols">

<div>

**Without a chart** — find the biggest monthly jump:

| Month | Revenue |
|---|---|
| Jan | 42 |
| Feb | 55 |
| Mar | 48 |
| Apr | 62 |
| May | 78 |
| Jun | 85 |

*How long did that take?*

</div>

<div>

**With a line chart** — answer in under a second:

![w:600px](images/day_1_line.png)


```

*Apr → May (+16k) is the biggest jump.*

```

</div>

</div>
---

## The Same Numbers — Three Levels

| Level | What you see | What you can do |
|---|---|---|
| **Data** | `42, 55, 48, 62, 78, 85, 92, 88, 95, 102, 98, 115` | Nothing yet |
| **Information** | Monthly revenue Jan–Dec (USD thousands) | Begin comparing |
| **Insight** | Revenue grew 174% over the year; Q3 was the inflection point | Make a decision |

<br>

<div class="box">

**The analyst's job:** move every stakeholder from the left column to the right column — as fast as possible.

</div>

---


## The Visualisation Workflow

Every session in this course follows the same pipeline:

<br>

<div class="box-navy">

```
Raw Data  ──▶  Clean & Structure  ──▶  Presentation Table
                                               │
                                               ▼
                                     Chart / Dashboard
                                               │
                                               ▼
                                       Story + Decision
```

</div>

<br>

We cover **every step** — not just the chart at the end.
The table step is where most analysts lose quality.

---

<!-- _class: divider -->

<span class="part-no">Ex01</span>
<div class="box-navy" style="width: 100%;">

```
Raw Data  ── ▶  Clean & Structure  ── ▶  Presentation Table ── ▶ Chart / Dashboard
```
*Ronnykym. (2020). Online Store Sales Data [Data set]. Kaggle.*

Use excel formulae or pivot table to report on sale by month of the year 2019 and 2020.

</div>


---
## Ex01
---

<!-- _class: divider -->

<span class="part-no">02</span>

# Our Tools

## Excel · Google Sheets · Python

---

---

## Three Tools, One Workflow

<div class="cols3">

<div class="card">

### Microsoft Excel

- Business reports
- Quick prototypes
- PivotTables
- One-off analysis

<br>

Insert → **Charts wizard**

</div>

<div class="card">

### Google Sheets

- Shared dashboards
- Live data feeds
- Team collaboration
- Cloud access

<br>

Insert → **Chart panel**

</div>

<div class="card warm">

### Python 🐍

- Large datasets
- Automation & scripts
- Publication quality
- Reproducible analysis

`matplotlib` `seaborn` `plotly`

</div>

</div>

<br>

*Knowing **which tool to reach for** is itself a professional skill.*

---

## Excel — Core Skills We Will Cover

<div class="cols">

<div>

**Data work**
- PivotTable — group, aggregate, pivot
- VLOOKUP / XLOOKUP — merge tables
- Conditional formatting
- Data validation

<br>

**Charts**
Line · Bar · Pie · Waterfall
Funnel · Stock (Candlestick) · Combo

</div>

<div>

**First exercise preview**

```
Raw transaction log
────────────────────────
Date  | Region | Revenue
Jan 3 | North  | 5,000
Jan 5 | South  | 4,500
...

        ▼  PivotTable

Region | Q1    | Q2
North  | 42k   | 55k
South  | 38k   | 47k
```

</div>

</div>

---

## Google Sheets — When to Choose It

<div class="cols">

<div>

**Strengths over Excel**

- Real-time multi-user editing
- Built-in `QUERY()` — SQL-like filtering
- `IMPORTRANGE()` — live data from another sheet
- Free, browser-based, easy sharing
- Native connection to Google Data Studio

</div>

<div>

| Situation | Choose |
|---|---|
| Colleagues editing simultaneously | **Sheets** |
| Data stays on your machine | **Excel** |
| Pulling live web / API data | **Sheets** |
| Complex macros / VBA | **Excel** |
| Sharing with non-Office users | **Sheets** |
| Large files (> 100MB) | **Excel** |

</div>

</div>

---

## Python — Three Libraries, Three Purposes

<div class="cols3">

<div class="card">

### matplotlib

The **foundation**. Full manual control over every element.

```python
import matplotlib.pyplot as plt

plt.plot(months, revenue,
         color='#0D1A63')
plt.title('Monthly Revenue')
plt.show()
```

</div>

<div class="card mid">

### seaborn

**Statistical charts** with minimal code. Built on matplotlib.

```python
import seaborn as sns

sns.boxplot(
  x='Group',
  y='Score',
  data=df
)
```

</div>

<div class="card warm">

### plotly

**Interactive** charts — hover, zoom, filter. Web & dashboards.

```python
import plotly.express as px

fig = px.bar(df,
  x='Month',
  y='Revenue')
fig.show()
```

</div>

</div>

---



# Data Types

## A Important Concept in Visualisation

---

---

## Why Data Types Matter

**The data type determines the chart — not the other way around.**

<div class="box">
Trying to draw a line chart on nominal categories, or a pie chart on continuous data, produces charts that are meaningless — or actively misleading.
</div>

<br>

| Data type | Examples | Suitable charts |
|---|---|---|
| **Continuous** | Revenue, temperature, height | Line, scatter, histogram |
| **Discrete** | Customers, units, page views | Bar, dot plot |
| **Nominal** | Country, product name, channel | Bar, pie, treemap |
| **Ordinal** | Rating: Poor / Good / Excellent | Bar, heatmap |
| **Temporal** | Dates, timestamps | Line, area, candlestick |
| **Geospatial** | City, coordinates, country | Map, choropleth |

---

## Quantitative — Continuous vs Discrete

<div class="cols">

<div>

### Continuous

Can take **any value** in a range — infinitely many possible values exist between two points.

<br>

**Examples**
- Revenue: $47,382.56
- Temperature: 36.8°C
- Height: 1.73 m
- Profit margin: 12.4%

<br>

**Key charts**
Line · Scatter · Histogram · Box Plot

</div>

<div>

### Discrete

**Countable whole numbers** only.
You cannot have 2.5 customers.

<br>

**Examples**
- Customers: 847
- Units sold: 1,200
- Page views: 54,321
- Support tickets: 7

<br>

**Key charts**
Bar · Column · Dot Plot

</div>

</div>

---

## Categorical — Nominal vs Ordinal

<div class="cols">

<div>

### Nominal

Categories with **no natural order**.
You cannot say North > South.

<br>

**Examples**
- Region: North / South / East / West
- Product: Widget A / Widget B
- Channel: Email / Social / Search
- Country: Vietnam / USA / UK

<br>

**Key charts**
Bar · Pie · Donut · Treemap

</div>

<div>

### Ordinal

Categories **with a meaningful order** — but the gap between levels may not be equal.

<br>

**Examples**
- Rating: Poor · Fair · Good · Excellent
- Education: High School · Bachelor's · Master's
- Priority: Low · Medium · High · Critical
- NPS: Detractor · Passive · Promoter

<br>

**Key charts**
Bar (sorted) · Heatmap · Stacked Bar

</div>

</div>

---

## Temporal — Time-based Data

Data recorded at **points in time** or over **time intervals**.

<div class="cols">

<div>

**Regular intervals**

Daily stock prices, monthly sales, hourly temperature readings.

The gap between points is constant — patterns like seasonality and trends become visible.

**Charts:** Line · Area · Candlestick · Calendar Heatmap

</div>

<div>

**Irregular intervals**

Customer purchase timestamps, server log events, support tickets.

Points are unevenly spaced — aggregation (hourly → daily → monthly) is needed first.

**Charts:** Line after aggregation · Event timeline

</div>

</div>

<br>

> **Golden rule:** Time always goes on the **X-axis**. The metric goes on the **Y-axis**.

---

## Geospatial Data

Data with a **location** component.

<div class="cols">

<div>

**Types of location data**

| Type | Example |
|---|---|
| Country name | "Vietnam", "USA" |
| Region / Province | "North", "HCMC" |
| Coordinates | lat 10.8°, lon 106.7° |
| Postal code | 70000 |
| Address | "123 Nguyen Hue St" |

</div>

<div>

**Key charts**

**Choropleth map** — colour regions by value (sales by country)

**Dot / bubble map** — sized dots at coordinates (store locations)

**Geo heatmap** — density of events (customer clusters)

*We cover choropleth maps using `plotly` in Part 2.*

</div>

</div>

---

## The Data-Type Decision Tree

```
What is your data type?
│
├── Numeric + time axis?             ──▶  Line / Area / Candlestick
│
├── Numeric, comparing groups?       ──▶  Bar / Box Plot / Violin
│
├── Numeric, one variable only?      ──▶  Histogram
│
├── Two numeric variables?           ──▶  Scatter Plot
│
├── Categorical, part of a whole?    ──▶  Pie / Donut / Treemap
│
├── Categorical, comparing values?   ──▶  Bar Chart (sorted)
│
└── Location?                        ──▶  Map / Choropleth
```

---

## Common Mistakes with Data Types

<div class="cols">

<div>

❌ **Line chart on nominal data**

Connecting "North → South → East" with a line implies a trend or order that does not exist.

*Fix: use a bar chart.*

<br>

❌ **Pie chart with too many categories**

A 12-slice pie chart is unreadable.

*Fix: use a sorted bar chart or treemap.*

</div>

<div>

❌ **Averaging ordinal data**

*"Average satisfaction: 2.7"* — implies equal spacing between ratings that may not exist.

*Fix: use frequency percentages.*

<br>

✅ **Match chart to data type**

The chart type is not a style choice — it is a statement about the **structure of your data**.

</div>

</div>

---

<!-- _class: divider -->

<span class="part-no">04</span>

# Hands-On

## Identify Data Types in a Real Dataset

---

---

## Exercise — Label Every Column

Look at this dataset. Working in pairs, label each column with its data type.

| Date | Salesperson | Region | Product | Units Sold | Unit Price | Revenue |
|---|---|---|---|---|---|---|
| Jan 03 | Alice | North | Widget A | 50 | 100 | 5,000 |
| Jan 05 | Bob | South | Widget B | 30 | 150 | 4,500 |
| Jan 12 | Carol | East | Widget A | 40 | 100 | 4,000 |

<br>

**Discuss for 3 minutes:**
- Which columns are numerical? Continuous or discrete?
- Which are categorical? Nominal or ordinal?
- Which is temporal?
- What charts could we build from this data?

---

## Exercise — Answers

| Column | Data Type | Reason |
|---|---|---|
| **Date** | Temporal | Ordered time series — trend charts possible |
| **Salesperson** | Nominal | Names, no natural rank order |
| **Region** | Nominal | Locations, no natural rank order |
| **Product** | Nominal | Category labels, no order |
| **Units Sold** | Discrete | Whole numbers only, countable |
| **Unit Price** | Continuous | Can be any decimal value |
| **Revenue** | Continuous | Derived from Units × Price, any decimal |

<br>

**Charts we can build:**
Revenue over time (line) · Revenue by region (bar) · Product mix (pie) · Units vs Price (scatter)

---

## Day 1 — Key Takeaways

<div class="cols">

<div>

**Core concepts**

- **Data** = raw facts, no meaning alone
- **Information** = data with context
- **Insight** = information that drives action
- Visualisation accelerates the journey

<hr>

**Data types**
Continuous · Discrete · Nominal · Ordinal · Temporal · Geospatial

*Data type determines chart — not personal preference.*

</div>

<div>

**Tools**
- **Excel** — fast, offline, business standard
- **Sheets** — collaborative, cloud, live data
- **Python** — powerful, automated, reproducible
  - `matplotlib` foundations
  - `seaborn` statistics
  - `plotly` interactive

<hr>

**Workflow**

Raw Data → Clean Table → Chart → Insight

</div>

</div>

---

## Homework Before Day 2

<br>

**1. Data types in the wild**
Find any report, news article, or dashboard. Label every column or axis label with its data type and write two sentences explaining your choices.

<br>

**2. Environment check**
Activate the `venv` and run:
```python
import matplotlib; print(matplotlib.__version__)
```

<br>

**3. Optional reading**
*Storytelling with Data* — Chapter 1: "The importance of context"

---

<!-- _class: title -->

# See You on Day 2

## Finance Visualisation

---

**Next session covers:**
Trial Balance · P&L Statement · Balance Sheet · Waterfall Chart · Candlestick Chart

<br>

*Questions before Day 2? Reach out anytime.*
