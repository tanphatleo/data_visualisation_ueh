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
    border-left: 6px solid var(--orange-1);
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
    border-left: 5px solid var(--navy);
    background: var(--navy-4);
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
    background: var(--navy-4);
    border-top-color: var(--navy);
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
    background: var(--navy-2);
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

<!-- _class: title -->

# Data Visualisation
## Day 1 — From Data to Insight

---

**Course Introduction · Data Fundamentals · Tools · Data Types**

*9-week programme · Excel · Python*

---

## Agenda — Day 1

<div class="cols">

<div>

**Morning**
1. Our tools
2. Data → Information → Insight
3. Why visualisation matters
4. The visualisation workflow


</div>

<div>

**Afternoon**
5. Data types & why they matter
6. How to choose the right chart
7. How to make an effective chart
8. Hands-on exercise
9. Q & A + homework

</div>

</div>

<br>

> By end of day you will understand **what data is**, **what it becomes**, and **how we work with it** for the rest of this course.

---

<!-- _class: divider -->

<span class="part-no">01</span>

# Our Tools

## Excel · Python · *maybe* AI

---


## Three Tools, One Workflow

<div class="cols">

<div class="card">

### Microsoft Excel

- Business reports
- Quick prototypes
- PivotTables
- One-off analysis

<br>

Insert → **Charts wizard**

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
Line · Bar · Waterfall
Funnel · Stock (Candlestick) · Combo

</div>

<div>

![w:350px](images/ex01_table.png)

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

<!-- _class: divider -->

<span class="part-no">02</span>

# What Is Data?

## And Why Does It Matter?


---

## Data Is Everywhere

**Data is not just numbers in a spreadsheet.** Anything that is recorded — in any form — is data.

<div class="cols3">

<div class="card">

### 🧾 Transactions
Invoices, receipts, purchase orders, bank statements

</div>

<div class="card">

### 🎙️ Recordings
Audio calls, video footage, CCTV streams, meeting transcripts

</div>

<div class="card mid">

### 📋 Logs
Server logs, app events, user clicks, page views, error traces

</div>

<div class="card">

### 🌡️ Sensors
Temperature readings, GPS coordinates, heart rate, humidity

</div>

<div class="card">

### 👤 Interactions
Form submissions, survey responses, chat messages, search queries

</div>

<div class="card warm">

### 📷 Media
Photos, scans, X-rays, satellite imagery, documents

</div>

</div>


> as long as it is captured and stored in any form of information storage — it is data.

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

![w:340px](images/ex01_table.png)

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

**Without a chart**:

![w:350px](images/ex01_table.png)


</div>

<div style="height:100%; display:flex; flex-direction:column; justify-content:center;">

**What insight can you see from the data?**

</div>


---
## Why Visualisation Matters
<div>

**With a chart**:

<img src="images/Ex01_F05.png" style="max-width:100%; object-fit:contain;">

</div>

---

## The Same Numbers — Three Levels

| Level | What you see | What you can do |
|---|---|---|
| **Data** | `42, 55, 48, 62, 78, 85, 92, 88, 95, 102, 98, 115` | Nothing yet |
| **Information** | Monthly revenue Jan–Dec (USD thousands) | Begin comparing |
| **Insight** | Revenue grew 174% over the year; Q3 was the inflection point | Make a decision |

<br>


---


## The Visualisation Workflow

Every session in this course follows the same pipeline:

<br>

<div class="box-navy">

```
Raw Data  ▶  Clean & Structure  ▶  Presentation Table  ▶  Chart / Dashboard  ▶  Story + Decision                 
```

</div>

<br>

We cover **every step** — not just the chart at the end.
The table step is where most analysts lose quality.

---

## Ex01.01

<div class="box-navy" style="width: 100%;">

```
Raw Data ▶ Clean & Structure ▶ Presentation Table 
```
*Ronnykym. (2020). Online Store Sales Data [Data set]. Kaggle.*

Use Excel formulas or pivot table to report on sale by month of the year 2019 and 2020.

![w:200px](images/qr_ex01_raw.png)

</div>


---
## Ex01.01

![w:350px](images/ex01_table.png)
<!-- estimation 15 minute -->

---

<!-- _class: divider -->

<span class="part-no">03</span>

# Data Types

## An Important Concept in Visualisation

---

## Quantitative — Continuous vs Discrete

<div class="cols">

<div>

## Continuous

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

## Discrete

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

## Nominal

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
Bar · Donut · Treemap

</div>

<div>

## Ordinal

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

*We cover choropleth maps using `plotly` in the Tools section.*

</div>

</div>

---

## Why Data Types Matter

**The data type determines the chart — not the other way around.**

| Data type | Examples | Suitable charts |
|---|---|---|
| **Continuous** | Revenue, temperature, height | Line, scatter, histogram |
| **Discrete** | Customers, units, page views | Bar, dot plot |
| **Nominal** | Country, product name, channel | Bar, treemap |
| **Ordinal** | Rating: Poor / Good / Excellent | Bar, heatmap |
| **Temporal** | Dates, timestamps | Line, area, candlestick |
| **Geospatial** | City, coordinates, country | Map, choropleth |

---

## Ex01.02

<div class="box-navy" style="width: 100%;">

**Identify the data type of each column in the Ex01 dataset.**

For each column, classify as: Continuous · Discrete · Nominal · Ordinal · Temporal · Geospatial

</div>

---

## Sample Data from Ex01
<img src="images/Ex0101_table.png" style="max-width:100%; object-fit:contain;">

---

## Data Dictionary and Types

| Column | Description | Data Type |
|---|---|---|
| **country** | Customer Origin Country | Categorical - Nominal |
| **order_value_EUR** | Order_value | Continuous |
| **cost** | Cost of goods sold | Continuous |
| **date** | date ordered | Temporal |
| **category** | Product Category | Categorical - Nominal |
| **customer_name** | Customer Name | Categorical - Nominal |
| **sales_manager** | Sale Manager Name | Categorical - Nominal |
| **sales_rep** | Sale Representative Name | Categorical - Nominal |
| **device_type** | The device type customer used to order - Nominal | Categorical - Nominal |
| **order_id** | unique order_id | Categorical - Nominal |

---

<!-- _class: divider -->

<span class="part-no">04</span>

# Deep Dive into Charts

## Bar/Column · Line · 

---

## Column Chart
<img src="images/chart_deep_dive/bar_charts.png" style="max-width:100%; max-height:530px; object-fit:contain;">

### Compare across categories
*inherently good for comparing totals.*


---

## Stacked Column Chart

<div class="cols">
<div>
<img src="images/chart_deep_dive/stacked_bar_charts.png" style="max-width:100%; max-height:530px; object-fit:contain;">
</div>
<div style="height:100%; display:flex; flex-direction:column; justify-content:center;">

### Compare across categories while showing components
**Total & Series A** - can easily be compared between categories
**Other Series** - can not be easily compared between categories

</div>
</div>

---

## Bar Chart

<img src="images/chart_deep_dive/bar_charts_h.png" style="max-width:100%; max-height:530px; object-fit:contain;">

### Compare across categories
*inherently good for Rankings.*

---

## 100 Stacked Bar Chart

<img src="images/chart_deep_dive/100_Stack_bar_chart.png" style="max-width:100%; max-height:530px; object-fit:contain;">

### Compositions of multiple categories
*inherently good for Rankings.*

---

## Pie Chart are evil


<div class="cols">
<div>
<img src="images/chart_deep_dive/pie_chart.png" style="max-width:100%; max-height:530px; object-fit:contain;">
</div>
<div style="height:100%; display:flex; flex-direction:column; justify-content:center;">

### Compositions - Part of a whole

**Human are bad at angles/arc** - can not easily be compared between categories

</div>
</div>

---

## Pie Chart are sometime (rarely)... not so evil


<div class="cols">
<div>
<img src="images/chart_deep_dive/pie_chart_not_evel.png" style="max-width:100%; max-height:530px; object-fit:contain;">
</div>
<div style="height:100%; display:flex; flex-direction:column; justify-content:center;">

### Compositions - highlight only ONE component

**Focus on ONE component** - assisted by callout

</div>
</div>

---

## Donut Chart


<div class="cols">
<div >
<img src="images/chart_deep_dive/donut.png" style="max-width:100%; max-height:530px; object-fit:contain;">
</div>
<div style="height:100%; display:flex; flex-direction:column; justify-content:center;">

### Compositions - highlight only ONE component
**Focus on ONE component** - assisted by callout


</div>
</div>

---


## Waffle Chart


<div class="cols">
<div style="padding-left:20px;">
<img src="images/chart_deep_dive/waffle_chart.png" style="max-width:100%; max-height:530px; object-fit:contain;">
</div>
<div style="height:100%; display:flex; flex-direction:column; justify-content:center;">

### Compositions - Parts of a whole
**Squares allow easy counting**


</div>
</div>

---


## Line Chart

<img src="images/chart_deep_dive/line_chart.png" style="max-width:100%; max-height:530px; object-fit:contain;">

**Compare over Time more many categories**


---



## Line Area Chart



<div class="cols">
<div style="padding-left:20px;">
<img src="images/chart_deep_dive/area_chart.png" style="max-width:100%; max-height:530px; object-fit:contain;">
</div>
<div style="height:100%; display:flex; flex-direction:column; justify-content:center;">

### Compare across categories while showing components



</div>
</div>


---


## Waterfall chart

<div class="cols">
<div style="padding-left:20px;">
<img src="images/chart_deep_dive/waterfall.png" style="max-width:100%; max-height:530px; object-fit:contain;">
</div>
<div style="height:100%; display:flex; flex-direction:column; justify-content:center;">

### Compositions with total line




---


## Scatter plot

<img src="images/chart_deep_dive/line_chart.png" style="max-width:100%; max-height:530px; object-fit:contain;">

**Compare over Time more many categories**


---


## Histogram

<img src="images/chart_deep_dive/line_chart.png" style="max-width:100%; max-height:530px; object-fit:contain;">

**Compare over Time more many categories**


---



<!-- _class: divider -->

<span class="part-no">05</span>

# How to Choose an Effective Chart

## Abela's Framework · FT Visual Vocabulary · Domain Examples

---

## Two (of many many) Frameworks for Chart Selection

*There are many different frameworks. These just serve as guides and are **not rules written in stone***

<div class="cols">

<div class="card">

### 🎯 Abela's Decision Tree
Start with **what you want to show** — Comparison, Distribution, Relationship, or Composition — then follow the branches to the right chart.

<br>

Developed by Andrew Abela (2006). Works best as a **quick first filter** when you already know your data type.


</div>

<div class="card warm">

### 📰 FT Visual Vocabulary
Organised by **analytical purpose** across 9 families — Deviation, Correlation, Change V Time, Ranking, Distribution, Part of Whole, Magnitude, Spatial, Flow.

<br>

Developed by the Financial Times visual journalism team. Covers **59 chart types** with real-world editorial context.


</div>

</div>

<br>

> Both frameworks start with the same question: **"What does your data need to say?"** — then map it to the right visual form.

---

## The Data-Type Decision Tree

<div style="display:flex; justify-content:center; align-items:center; margin-top:8px;">
<img src="images/chose_chart_diagram.png" style="max-width:100%; max-height:530px; object-fit:contain;">
</div>
<p style="font-size:0.45em; color:#7e7e7e; text-align:right; margin-top:6px;">Abela, A. V. (2015). The presentation: A story about communicating successfully with very few slides. CreateSpace Independent Publishing Platform</em> [Book].</p>

---

## Financial Times Visual Vocabulary

<div style="display:grid;grid-template-columns:repeat(9,1fr);gap:5px;margin-top:6px;">

<div style="text-align:center;">
<p style="font-size:0.45em;font-weight:800;color:var(--navy);text-transform:uppercase;letter-spacing:0.03em;border-bottom:2px solid var(--orange);padding-bottom:2px;margin:0 0 5px;">Deviation</p>
<img src="ft_visual_vocab/deviation/Visual Vocabulary_files/bar-diverging.svg" style="width:100%;height:52px;object-fit:contain;display:block;margin:0 auto 2px;">
<img src="ft_visual_vocab/deviation/Visual Vocabulary_files/bar-diverging-stacked.svg" style="width:100%;height:52px;object-fit:contain;display:block;margin:0 auto 2px;">
<img src="ft_visual_vocab/deviation/Visual Vocabulary_files/spine.svg" style="width:100%;height:52px;object-fit:contain;display:block;margin:0 auto 2px;">
<img src="ft_visual_vocab/deviation/Visual Vocabulary_files/line-surplur-defecit-fill.svg" style="width:100%;height:52px;object-fit:contain;display:block;margin:0 auto;">
</div>

<div style="text-align:center;">
<p style="font-size:0.45em;font-weight:800;color:var(--navy);text-transform:uppercase;letter-spacing:0.03em;border-bottom:2px solid var(--orange);padding-bottom:2px;margin:0 0 5px;">Correlation</p>
<img src="ft_visual_vocab/correlation/Visual Vocabulary_files/scatterplot.svg" style="width:100%;height:52px;object-fit:contain;display:block;margin:0 auto 2px;">
<img src="ft_visual_vocab/correlation/Visual Vocabulary_files/bubble.svg" style="width:100%;height:52px;object-fit:contain;display:block;margin:0 auto 2px;">
<img src="ft_visual_vocab/correlation/Visual Vocabulary_files/XY-heatmap.svg" style="width:100%;height:52px;object-fit:contain;display:block;margin:0 auto 2px;">
<img src="ft_visual_vocab/correlation/Visual Vocabulary_files/line-column.svg" style="width:100%;height:52px;object-fit:contain;display:block;margin:0 auto;">
</div>

<div style="text-align:center;">
<p style="font-size:0.45em;font-weight:800;color:var(--navy);text-transform:uppercase;letter-spacing:0.03em;border-bottom:2px solid var(--orange);padding-bottom:2px;margin:0 0 5px;">Change V Time</p>
<img src="ft_visual_vocab/change_v_time/Visual Vocabulary_files/line.svg" style="width:100%;height:52px;object-fit:contain;display:block;margin:0 auto 2px;">
<img src="ft_visual_vocab/change_v_time/Visual Vocabulary_files/column-timeline.svg" style="width:100%;height:52px;object-fit:contain;display:block;margin:0 auto 2px;">
<img src="ft_visual_vocab/change_v_time/Visual Vocabulary_files/area.svg" style="width:100%;height:52px;object-fit:contain;display:block;margin:0 auto 2px;">
<img src="ft_visual_vocab/change_v_time/Visual Vocabulary_files/calendar-heatmap.svg" style="width:100%;height:52px;object-fit:contain;display:block;margin:0 auto;">
</div>

<div style="text-align:center;">
<p style="font-size:0.45em;font-weight:800;color:var(--navy);text-transform:uppercase;letter-spacing:0.03em;border-bottom:2px solid var(--orange);padding-bottom:2px;margin:0 0 5px;">Ranking</p>
<img src="ft_visual_vocab/ranking/Visual Vocabulary_files/bar-ordered.svg" style="width:100%;height:52px;object-fit:contain;display:block;margin:0 auto 2px;">
<img src="ft_visual_vocab/ranking/Visual Vocabulary_files/slope-ranking.svg" style="width:100%;height:52px;object-fit:contain;display:block;margin:0 auto 2px;">
<img src="ft_visual_vocab/ranking/Visual Vocabulary_files/lollipop-h.svg" style="width:100%;height:52px;object-fit:contain;display:block;margin:0 auto 2px;">
<img src="ft_visual_vocab/ranking/Visual Vocabulary_files/bump.svg" style="width:100%;height:52px;object-fit:contain;display:block;margin:0 auto;">
</div>

<div style="text-align:center;">
<p style="font-size:0.45em;font-weight:800;color:var(--navy);text-transform:uppercase;letter-spacing:0.03em;border-bottom:2px solid var(--orange);padding-bottom:2px;margin:0 0 5px;">Distribution</p>
<img src="ft_visual_vocab/distribution/Visual Vocabulary_files/histogram.svg" style="width:100%;height:52px;object-fit:contain;display:block;margin:0 auto 2px;">
<img src="ft_visual_vocab/distribution/Visual Vocabulary_files/boxplot.svg" style="width:100%;height:52px;object-fit:contain;display:block;margin:0 auto 2px;">
<img src="ft_visual_vocab/distribution/Visual Vocabulary_files/violin.svg" style="width:100%;height:52px;object-fit:contain;display:block;margin:0 auto 2px;">
<img src="ft_visual_vocab/distribution/Visual Vocabulary_files/cumulative-curve.svg" style="width:100%;height:52px;object-fit:contain;display:block;margin:0 auto;">
</div>

<div style="text-align:center;">
<p style="font-size:0.45em;font-weight:800;color:var(--navy);text-transform:uppercase;letter-spacing:0.03em;border-bottom:2px solid var(--orange);padding-bottom:2px;margin:0 0 5px;">Part of Whole</p>
<img src="ft_visual_vocab/part_of_whole/Visual Vocabulary_files/voronoi.svg" style="width:100%;height:52px;object-fit:contain;display:block;margin:0 auto 2px;">
<img src="ft_visual_vocab/part_of_whole/Visual Vocabulary_files/doughnut.svg" style="width:100%;height:52px;object-fit:contain;display:block;margin:0 auto 2px;">
<img src="ft_visual_vocab/part_of_whole/Visual Vocabulary_files/treemap.svg" style="width:100%;height:52px;object-fit:contain;display:block;margin:0 auto 2px;">
<img src="ft_visual_vocab/part_of_whole/Visual Vocabulary_files/column-stacked.svg" style="width:100%;height:52px;object-fit:contain;display:block;margin:0 auto;">
</div>

<div style="text-align:center;">
<p style="font-size:0.45em;font-weight:800;color:var(--navy);text-transform:uppercase;letter-spacing:0.03em;border-bottom:2px solid var(--orange);padding-bottom:2px;margin:0 0 5px;">Magnitude</p>
<img src="ft_visual_vocab/magnitude/Visual Vocabulary_files/column-magnitude.svg" style="width:100%;height:52px;object-fit:contain;display:block;margin:0 auto 2px;">
<img src="ft_visual_vocab/magnitude/Visual Vocabulary_files/bar-magnitude.svg" style="width:100%;height:52px;object-fit:contain;display:block;margin:0 auto 2px;">
<img src="ft_visual_vocab/magnitude/Visual Vocabulary_files/symbol-proportional.svg" style="width:100%;height:52px;object-fit:contain;display:block;margin:0 auto 2px;">
<img src="ft_visual_vocab/magnitude/Visual Vocabulary_files/radar.svg" style="width:100%;height:52px;object-fit:contain;display:block;margin:0 auto;">
</div>

<div style="text-align:center;">
<p style="font-size:0.45em;font-weight:800;color:var(--navy);text-transform:uppercase;letter-spacing:0.03em;border-bottom:2px solid var(--orange);padding-bottom:2px;margin:0 0 5px;">Spatial</p>
<img src="ft_visual_vocab/spatial/Visual Vocabulary_files/basic-choropleth.svg" style="width:100%;height:52px;object-fit:contain;display:block;margin:0 auto 2px;">
<img src="ft_visual_vocab/spatial/Visual Vocabulary_files/proportional-symbol.svg" style="width:100%;height:52px;object-fit:contain;display:block;margin:0 auto 2px;">
<img src="ft_visual_vocab/spatial/Visual Vocabulary_files/dot-density.svg" style="width:100%;height:52px;object-fit:contain;display:block;margin:0 auto 2px;">
<img src="ft_visual_vocab/spatial/Visual Vocabulary_files/flow.svg" style="width:100%;height:52px;object-fit:contain;display:block;margin:0 auto;">
</div>

<div style="text-align:center;">
<p style="font-size:0.45em;font-weight:800;color:var(--navy);text-transform:uppercase;letter-spacing:0.03em;border-bottom:2px solid var(--orange);padding-bottom:2px;margin:0 0 5px;">Flow</p>
<img src="ft_visual_vocab/flow/Visual Vocabulary_files/sankey.svg" style="width:100%;height:52px;object-fit:contain;display:block;margin:0 auto 2px;">
<img src="ft_visual_vocab/flow/Visual Vocabulary_files/chord.svg" style="width:100%;height:52px;object-fit:contain;display:block;margin:0 auto 2px;">
<img src="ft_visual_vocab/flow/Visual Vocabulary_files/network.svg" style="width:100%;height:52px;object-fit:contain;display:block;margin:0 auto 2px;">
<img src="ft_visual_vocab/flow/Visual Vocabulary_files/waterfall-flow.svg" style="width:100%;height:52px;object-fit:contain;display:block;margin:0 auto;">
</div>

</div>

<p style="font-size:0.45em; color:#7e7e7e; text-align:right; margin-top:8px;">Financial Times. (n.d.). <em>Visual vocabulary</em>. <a href="https://ft-interactive.github.io/visual-vocabulary/">https://ft-interactive.github.io/visual-vocabulary/</a></p>

---

## Chart Types — By Purpose

<div class="cols4">
<div>

### Comparison
<div class="chart-thumb-sm"><p>Bar</p><img src="images/chart_types/chart01_bar.png"></div>
<div class="chart-thumb-sm"><p>Line</p><img src="images/chart_types/chart02_line.png"></div>
<div class="chart-thumb-sm"><p>Slope</p><img src="images/chart_types/chart04_slope.png"></div>

</div>
<div>

### Composition
<div class="chart-thumb-sm"><p>Donut</p><img src="images/chart_types/chart05_donut.png"></div>
<div class="chart-thumb-sm"><p>Treemap</p><img src="images/chart_types/chart08_treemap.png"></div>
<div class="chart-thumb-sm"><p>Stacked Area</p><img src="images/chart_types/chart_stacked_area.png"></div>

</div>
<div>

### Relationship
<div class="chart-thumb-sm"><p>Scatter</p><img src="images/chart_types/chart09b_scatter_orange.png"></div>
<div class="chart-thumb-sm"><p>Bubble</p><img src="images/chart_types/chart10b_bubble_orange.png"></div>
<div class="chart-thumb-sm"><p>Heatmap</p><img src="images/chart_types/chart_heatmap.png"></div>

</div>
<div>

### Distribution
<div class="chart-thumb-sm"><p>Histogram</p><img src="images/chart_types/chart_histogram_orange.png"></div>
<div class="chart-thumb-sm"><p>Box Plot</p><img src="images/chart_types/chart_box_plot_orange.png"></div>
<div class="chart-thumb-sm"><p>CDF</p><img src="images/chart_types/chart_cdf.png"></div>

</div>
</div>

---

## Finance Charts

<div class="cols4">
<div class="chart-thumb-sm"><p>Bar</p><img src="images/chart_types/chart01_bar.png"></div>
<div class="chart-thumb-sm"><p>Line</p><img src="images/chart_types/chart02b_line_dual.png"></div>
<div class="chart-thumb-sm"><p>Stacked Column</p><img src="images/chart_types/chart_stacked_column.png"></div>
<div class="chart-thumb-sm"><p>100% Stacked Column</p><img src="images/chart_types/chart_stacked_column_100.png"></div>
<div class="chart-thumb-sm"><p>Stacked Area</p><img src="images/chart_types/chart_stacked_area.png"></div>
<div class="chart-thumb-sm"><p>100% Stacked Area</p><img src="images/chart_types/chart_stacked_area_100.png"></div>
<div class="chart-thumb-sm"><p>Area</p><img src="images/chart_types/chart03_area.png"></div>
<div class="chart-thumb-sm"><p>Waterfall</p><img src="images/chart_types/chart06_waterfall.png"></div>
<div class="chart-thumb-sm"><p>Candlestick</p><img src="images/chart_types/chart07_candlestick.png"></div>

<div class="chart-thumb-sm"><p>Gauge</p><img src="images/chart_types/chart_gauge.png"></div>
<div class="chart-thumb-sm"><p>Treemap</p><img src="images/chart_types/chart08_treemap.png"></div>
<div class="chart-thumb-sm"><p>Donut</p><img src="images/chart_types/chart05_donut.png"></div>
</div>

---

## Sales & Marketing Charts

<div class="cols4">
<div class="chart-thumb-sm"><p>Bar</p><img src="images/chart_types/chart01_bar.png"></div>
<div class="chart-thumb-sm"><p>Line</p><img src="images/chart_types/chart02b_line_dual.png"></div>
<div class="chart-thumb-sm"><p>Slope</p><img src="images/chart_types/chart04_slope.png"></div>
<div class="chart-thumb-sm"><p>Area</p><img src="images/chart_types/chart03_area.png"></div>
<div class="chart-thumb-sm"><p>Stacked Column</p><img src="images/chart_types/chart_stacked_column.png"></div>
<div class="chart-thumb-sm"><p>Stacked Area</p><img src="images/chart_types/chart_stacked_area.png"></div>
<div class="chart-thumb-sm"><p>Donut</p><img src="images/chart_types/chart05_donut.png"></div>
<div class="chart-thumb-sm"><p>Radar</p><img src="images/chart_types/chart_radar.png"></div>
<div class="chart-thumb-sm"><p>Funnel</p><img src="images/chart_types/chart11_funnel.png"></div>
<div class="chart-thumb-sm"><p>Alluvial</p><img src="images/chart_types/chart36_alluvial.png"></div>
<div class="chart-thumb-sm"><p>Sankey</p><img src="images/chart_types/chart37_sankey.png"></div>
<div class="chart-thumb-sm"><p>Pictogram</p><img src="images/chart_types/chart_pictogram.png"></div>
</div>

---

## Science & Research Charts

<div class="cols4">
<div class="chart-thumb-sm"><p>Scatter</p><img src="images/chart_types/chart09b_scatter_orange.png"></div>
<div class="chart-thumb-sm"><p>Bubble</p><img src="images/chart_types/chart10b_bubble_orange.png"></div>
<div class="chart-thumb-sm"><p>Radar</p><img src="images/chart_types/chart_radar.png"></div>
<div class="chart-thumb-sm"><p>Heatmap</p><img src="images/chart_types/chart_heatmap.png"></div>
<div class="chart-thumb-sm"><p>Choropleth</p><img src="images/chart_types/chart_choropleth.png"></div>
<div class="chart-thumb-sm"><p>Line</p><img src="images/chart_types/chart02b_line_dual.png"></div>
<div class="chart-thumb-sm"><p>Histogram</p><img src="images/chart_types/chart_histogram_orange.png"></div>
<div class="chart-thumb-sm"><p>Histogram + KDE</p><img src="images/chart_types/chart_histogram_line.png"></div>
<div class="chart-thumb-sm"><p>CDF</p><img src="images/chart_types/chart_cdf.png"></div>
<div class="chart-thumb-sm"><p>Box Plot</p><img src="images/chart_types/chart_box_plot_orange.png"></div>
</div>

---

## Ex01.03 — Formulating Questions

<div class="box-navy" style="width: 100%;">

**Activity: What can we ask the data?**
Take a moment to look at the dataset structure and data types.
What are some analytical questions we can answer using this data? 
![w:200px](images/qr_ex01_raw.png)
</div>

---

## 20 Analytical Questions for Ex01.03

With our dataset mapped out, what can we ask it? Here are 20 questions we can answer using visualization:

<div style="font-size: 1em; column-count: 2; column-gap: 40px;">

1. What is the total overall revenue and total cost?
2. Which **country** generated the highest total revenue?
3. What is the average order value across all transactions?
4. How do sales trend over time (**date**) on a monthly basis?
5. Which product **category** yields the highest total profit?
6. Who are the top 5 customers (**customer_name**) by total volume?
7. Which **sales_manager** has the highest-performing team?
8. Which **sales_rep** closed the highest number of orders?
9. Are there noticeable seasonal spikes throughout the year?
10. What is the most frequently used **device_type** for ordering?
</div>

--- 

## 20 Analytical Questions (cont.)

<div style="font-size: 1em; column-count: 2; column-gap: 40px;">

11. Is there a correlation between device and average order value?
12. Which country has the lowest average profit margin per order?
13. How does the product mix (**category**) differ by country?
14. Which customer has the highest single order value?
15. What percentage of revenue comes from the top category?
16. Does the time of year influence category popularity?
17. Do specific reps specialize in high-value vs. volume orders?
18. How does total cost vary relative to revenue across countries?
19. Which device and country combo yields the highest order value?
20. What is the distribution of order values (small vs large)?

</div>

---

## Ex01.04 — Chart Selection Activity

<div class="box-navy" style="width: 100%;">

**Activity: Choose the Right Chart**

1. One student selects a question from the 20 analytical questions.
2. The class discusses and decides **what chart type** is best to answer it.
3. Justify your choice based on the data types and the message you want to convey.

</div>

---

##
<!-- _class: divider -->

<span class="part-no">05</span>

# Chart Journey

## From Table to Insight — A Practical Walkthrough

---

## Step 0 — The Presentation Table

<div class="cols">

<div style="margin-right:100px;">

Before drawing any chart, you need a **clean presentation table** — aggregated, labelled, and ready to visualise.

<br>

This is the output of **Ex01.01**: monthly sales by year, condensed from thousands of raw transactions into 24 numbers.

<br>


</div>

<div>

<img src="images/ex01_table.png" style="margin-right:100px;width:350PX;  object-fit:contain;">

</div>

</div>

---

## Step 1 — Insert the Chart

<div class="cols-1-2">

<div>

Pick the chart type that matches your data and question.

*Two series · Monthly time axis → **Grouped Bar Chart***

<br>

<div class="box">

**Raw first attempt — problems to fix:**
- Y-axis shows raw numbers (`10,000,000`)
- Title gives no analytical signal
- Colours are default, no visual hierarchy

</div>

</div>

<div>

<img src="images/Ex01_F01.png" style="max-width:100%; object-fit:contain;">

</div>

</div>

---

## Step 2 — Format for Readability

<div class="cols-1-2">

<div>

Clean up anything that **slows the reader down**.

<br>

<div class="box-navy">

**What changed:**
- Y-axis: `10,000,000` → `10M` (shorthand)
- Title: year labels **bolded** and **colour-coded** to match the bars
- Gridlines thinned; chart area decluttered

</div>

<br>


</div>

<div>

<img src="images/Ex01_F02.png" style="max-width:100%; object-fit:contain;">

</div>

</div>

---

## Step 3 — Focus on the Story

<div class="cols-1-2">

<div>

Decide what you want the reader to **notice first** — then make that visually obvious.

<br>

<div class="box">

**What changed:**
- All non-December bars **greyed out**
- December data labels added: `8.7M` / `5.9M`
- Callout annotation states the insight in plain language

</div>

<br>



</div>

<div>

<img src="images/Ex01_F03.png" style="max-width:100%; object-fit:contain;">

</div>

</div>

---

## Step 4 — Add Context

<div class="cols-1-2">

<div>

Layer in a second data series to show **why** the story matters.

<br>

<div class="box-navy">

**What changed:**
- Net accumulated revenue difference added as an **overlaid line chart** (combo chart)
- December's sharp dip **confirms** the annotation

</div>


</div>

<div>

<img src="images/Ex01_F04.png" style="max-width:100%; object-fit:contain;">

</div>

</div>

---

## Step 5 — The Finished Chart




<img src="images/Ex01_F05.png" style="max-width:100%; object-fit:contain;">

<br>
<br>
<br>

Final refinement: make sure the **spotlight lands exactly where the story is**.

---

## What if 2 Insights?


<img src="images/Ex01_F06.png" style="max-width:100%; object-fit:contain;">
<br>
<br>

A chart can carry **more than one story** — as long as each spotlight is clearly labelled and the two stories are directly connected.

---

## Alternative Presentation

<img src="images/Ex01_F09.png" style="max-width:100%; object-fit:contain;">
<br>
<br>

**Plot the difference directly**

---

## Alternative Presentation 2




<img src="images/Ex01_F11.png" style="max-width:100%; object-fit:contain;">


**How about line chart?**

---

## Alternative Presentation 3 — ❌ Don't Do This

<div class="cols-1-2">

<div style="">

The same data — but this layout **breaks a fundamental rule**.


<div class="box" style="border-left-color: #CC3300; background: #FFF0ED;">

**What is wrong:**
- Our eyes read horizontal flow as time sequence — left to right
- A vertical time axis hides trends and makes the chart feel like a ranking, not a timeline

</div>

</div>

<div style="margin-left:100px;">

<img src="images/Ex01_F10.png" style="max-height:65%; object-fit:contain;">

</div>

</div>

---

<!-- _class: divider -->

<span class="part-no">Ref</span>

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

**How to choose a chart**
- Abela's tree — start with your message
- FT Visual Vocabulary — 9 purpose families
- Domain context — Finance, Sales, Science each have common patterns

<hr>

**Tools**
- **Excel** — fast, offline, business standard
- **Python** — powerful, automated, reproducible

</div>

</div>

---

<!-- _class: title -->

# See You on Day 2

## Finance Visualisation

---

**Next session covers:**
Trial Balance · P&L Statement · Balance Sheet · Waterfall Chart · Candlestick Chart

<br>

*Questions before Day 2? Reach out anytime.*

---

## References

<div style="font-size: 0.72em; line-height: 1.8; color: var(--black);">

Avila, S. (2025, November 19). Financial data visualization: Types, tools, & why use it in 2025. *Julius AI*. https://julius.ai/articles/financial-data-visualization-guide

CleanChart. (n.d.). Financial data visualization. *CleanChart Blog*. https://www.cleanchart.app/blog/financial-data-visualization

Dattani, S. (2025). Saloni's guide to data visualization: Why data visualization matters, and how to make charts more effective, clear, transparent, and sometimes, beautiful. *Scientific Discovery*. https://www.scientificdiscovery.dev/p/salonis-guide-to-data-visualization

HubSpot. (2025, December 3). 18 best types of charts and graphs for data visualization [+ how to choose]. *HubSpot Blog*. https://blog.hubspot.com/marketing/types-of-graphs-for-data-visualization

SR Analytics. (2025, November 6). Data visualization techniques guide: Charts that drive ROI 2026. *SR Analytics Blog*. https://sranalytics.io/blog/data-visualization-techniques/

Yale University Library. (2024, August). Data visualization: Common types of data visualizations. *Yale University Library Guides*. https://guides.library.yale.edu/datavisualization/types

</div>

use the data in A1:D13 to create a chart, series 2019 and 2020 should be column, and Net Acc Diff should be a line, 
use color A6A6A6 for the columns of 2019, and F68048 for columns of 2020. 
set series overlap to 60% , gap width should be 50%. 

format vertical axis text to show M instead of whole number, also format the data label, the axis should have no decimal

Net Acc Diff should be a line, and the color should be 0D1A63, the line should be smooth. Net Acc Diff should be on the same vertical axis not the second one. 

only show label for the month Dec.  also format the data label to use M but with 1 decimal place

delete all grid lines

set title to "Monthly Sales 2019 vs 2020 (EUR)" format the 2019 in the title to bold and color A6A6A6 and 2020 to bold and color F68048 

delete the legend for the series


    
Day 1	Introduction	
Day 2	Data processing + charts in excel	Finance
Day 3	Data processing + charts in excel	Finance
Day 4	Data processing + charts in python	Marketing
Day 5	Capston 1	Finance
Day 6	Data processing + charts in python	Marketing
Day 7	Data processing + charts in python	Science
Day 8	Data processing + charts in python	Science
Day 9	Capston 2	Free Subject
