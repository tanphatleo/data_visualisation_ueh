# Sales Dataset — Full Analytical Report
**Dataset:** `Ex01_Raw.xlsx`
**Period covered:** January 2019 – December 2020
**Date of analysis:** 2026-05-26
**Analyst:** Claude (AI-assisted analysis)

---

## Table of Contents

1. [Dataset Overview](#1-dataset-overview)
2. [Overall KPIs — Two-Year Summary](#2-overall-kpis--two-year-summary)
3. [2020 Annual Performance Review](#3-2020-annual-performance-review)
4. [Tablet Channel Collapse Investigation](#4-tablet-channel-collapse-investigation)
5. [Deep Investigation — Why 2020 Revenue Did Not Grow](#5-deep-investigation--why-2020-revenue-did-not-grow)
6. [Sales Manager Efficiency Review](#6-sales-manager-efficiency-review)
7. [Composite Score Methodology](#7-composite-score-methodology)
8. [Customer × Sales Rep Overlap Analysis](#8-customer--sales-rep-overlap-analysis)
9. [Manager Imbalance & Consolidation Strategy](#9-manager-imbalance--consolidation-strategy)
10. [Master Recommendations](#10-master-recommendations)

---

## 1. Dataset Overview

### Structure

| Attribute | Value |
|-----------|-------|
| Total Records | 1,000 orders |
| Columns | 10 |
| Date Range | 2 January 2019 → 30 December 2020 |
| Missing Values | None |

### Columns & Data Types

| Column | Type | Description |
|--------|------|-------------|
| `country` | string | Customer's country |
| `order_value_EUR` | float | Order revenue in EUR |
| `cost` | float | Cost of goods for the order |
| `date` | datetime | Order date |
| `category` | string | Product category (10 unique) |
| `customer_name` | string | Customer company name |
| `sales_manager` | string | Managing sales manager |
| `sales_rep` | string | Sales representative who placed the order |
| `device_type` | string | Device used to place order (PC / Mobile / Tablet) |
| `order_id` | string | Unique order identifier |

### Dimension Cardinality

| Dimension | Unique Values |
|-----------|--------------|
| Countries | 15 |
| Product Categories | 10 |
| Customers | 75 |
| Sales Managers | 15 |
| Sales Reps | 35 |
| Device Types | 3 (PC, Mobile, Tablet) |

### Derived Fields (calculated during analysis)

```
profit        = order_value_EUR − cost
margin_pct    = profit / order_value_EUR × 100
year          = date.year
month         = date.month
quarter       = date.quarter
year_month    = date.to_period('M')
size_bucket   = order_value_EUR binned into <50K / 50-100K / 100-150K / 150-200K / 200-300K / 300K+
```

---

## 2. Overall KPIs — Two-Year Summary

### Top-Line Metrics

| Metric | Value |
|--------|-------|
| **Total Revenue** | EUR 113,361,739 |
| **Total Cost** | EUR 94,369,311 |
| **Total Profit** | EUR 18,992,428 |
| **Average Profit Margin** | 16.75% |
| **Total Orders** | 1,000 |
| **Average Order Value** | EUR 113,362 |
| **Orders per Year** | ~500 |

### Statistical Summary (per order)

| Metric | Revenue | Cost | Profit | Margin% |
|--------|---------|------|--------|---------|
| Mean | 113,362 | 94,369 | 18,992 | 16.75% |
| Std Dev | 61,775 | 51,540 | 10,918 | 2.67% |
| Min | 15,101 | 12,114 | 2,074 | 12.00% |
| 25th Pct | 65,311 | 54,248 | 10,746 | 14.34% |
| Median | 105,419 | 87,095 | 17,332 | 16.98% |
| 75th Pct | 151,193 | 125,571 | 25,205 | 19.04% |
| Max | 383,997 | 304,701 | 79,295 | 21.00% |

> **Margins are exceptionally stable** (std dev = 2.67 percentage points), ranging from 12% to 21% — suggesting formula-based pricing or strong cost controls. There are no significant margin outliers by category, country, or rep.

### Revenue by Category

| Category | Orders | Revenue (EUR) | Share | Avg Margin |
|----------|--------|--------------|-------|-----------|
| Clothing | 155 | 17,661,682 | 15.6% | 16.56% |
| Games | 139 | 15,321,623 | 13.5% | 16.68% |
| Appliances | 131 | 15,139,669 | 13.4% | 16.90% |
| Electronics | 134 | 14,482,078 | 12.8% | 16.71% |
| Books | 117 | 13,179,979 | 11.6% | 16.75% |
| Beauty | 115 | 12,569,064 | 11.1% | 16.88% |
| Smartphones | 95 | 11,101,655 | 9.8% | 16.42% |
| Outdoors | 50 | 5,939,075 | 5.2% | **17.57%** |
| Accessories | 35 | 4,703,931 | 4.1% | 16.82% |
| Other | 29 | 3,262,983 | 2.9% | 16.46% |

> **Outdoors** has the highest margin (17.57%) but only 5.2% revenue share — a high-value niche worth expanding. **Smartphones** has the lowest margin (16.42%) — possibly reflecting competitive pricing pressure.

### Revenue by Country

| Country | Orders | Revenue (EUR) | Share | Avg Margin |
|---------|--------|--------------|-------|-----------|
| Portugal | 239 | 27,796,362 | 24.5% | 16.73% |
| France | 232 | 25,900,678 | 22.8% | 16.80% |
| Sweden | 182 | 19,637,204 | 17.3% | 16.72% |
| UK | 101 | 12,115,617 | 10.7% | 16.94% |
| Finland | 44 | 5,548,035 | 4.9% | 16.35% |
| Ireland | 43 | 4,952,285 | 4.4% | 16.58% |
| Bulgaria | 30 | 3,482,145 | 3.1% | 17.07% |
| Netherlands | 28 | 3,224,665 | 2.8% | 16.53% |
| Luxembourg | 22 | 2,913,550 | 2.6% | 16.88% |
| Germany | 24 | 2,794,049 | 2.5% | 16.82% |
| Spain | 26 | 2,499,240 | 2.2% | 16.44% |
| Italy | 10 | 935,569 | 0.8% | 16.34% |
| Denmark | 11 | 763,204 | 0.7% | 17.54% |
| Belgium | 6 | 608,970 | 0.5% | 15.36% |
| Austria | 2 | 190,166 | 0.2% | 19.25% |

> **Top 3 countries (Portugal, France, Sweden) generate 64.6% of total revenue.** The bottom 10 markets combined account for only ~12%.

### Revenue by Device Type

| Device | Orders | Revenue (EUR) | Share | Avg Margin |
|--------|--------|--------------|-------|-----------|
| PC | 785 | 89,647,284 | 79.1% | 16.77% |
| Mobile | 142 | 15,447,394 | 13.6% | 16.67% |
| Tablet | 73 | 8,267,061 | 7.3% | 16.58% |

> **PC dominates at 79.1%** — consistent with B2B buyer profiles. High order values on PC (median EUR 111,537) vs Tablet (median EUR 82,116) support this interpretation.

### Top 10 Customers by Revenue (2-year total)

| Customer | Orders | Revenue (EUR) | Share |
|----------|--------|--------------|-------|
| **Johns and Sons** | 142 | 16,360,257 | **14.4%** |
| Hessel-Stiedemann | 55 | 6,512,064 | 5.7% |
| Dickinson, Hyatt and Berge | 24 | 2,706,730 | 2.4% |
| Larkin-Collier | 21 | 2,566,550 | 2.3% |
| Altenwerth-Konopelski | 20 | 2,524,208 | 2.2% |
| Swaniawski, Runolfsson and Green | 25 | 2,506,135 | 2.2% |
| Romaguera-Dietrich | 20 | 2,426,708 | 2.1% |
| Rowe, Hermiston and Kessler | 22 | 2,312,525 | 2.0% |
| Wisoky Inc | 21 | 2,277,714 | 2.0% |
| Labadie and Sons | 19 | 2,165,265 | 1.9% |

> **Johns and Sons is a critical concentration risk** — one customer equals 14.4% of total revenue.

---

## 3. 2020 Annual Performance Review

### Top-Line KPIs: 2019 vs 2020

| Metric | 2019 | 2020 | YoY Change |
|--------|------|------|-----------|
| Total Revenue | EUR 56,617,524 | EUR 56,744,214 | **+0.2%** |
| Total Profit | EUR 9,487,278 | EUR 9,505,150 | **+0.2%** |
| Avg Margin | 16.79% | 16.70% | −0.09pp |
| Total Orders | 490 | 510 | **+4.1%** |
| Avg Order Value | EUR 115,546 | EUR 111,263 | **−3.7%** |

> **Headline story: flat revenue.** The business processed 4% more orders but each was worth 3.7% less — volume growth was entirely cancelled out by deal size decline.

### Quarterly Performance

| Quarter | Revenue 2020 | Revenue 2019 | YoY |
|---------|-------------|-------------|-----|
| Q1 | EUR 10,755,057 | EUR 9,934,007 | **+8.3%** |
| Q2 | EUR 16,765,179 | EUR 15,690,154 | **+6.9%** |
| Q3 | EUR 13,735,223 | EUR 14,946,120 | **−8.1%** |
| Q4 | EUR 15,488,755 | EUR 16,047,244 | **−3.5%** |

> **2020 started strong but reversed in H2.** H1 grew +7.4%, H2 fell −5.7%. The business lost momentum precisely at mid-year.

### Monthly Revenue Highlights

| Month | 2020 Revenue | YoY | Signal |
|-------|-------------|-----|--------|
| November | EUR 4,734,730 | **+59.9%** | Best YoY month |
| May | EUR 5,537,944 | **+44.8%** | Strong |
| March | EUR 3,579,944 | **+42.0%** | Strong |
| August | EUR 4,714,525 | **+37.2%** | Solid |
| February | EUR 1,959,413 | **−32.3%** | Weakest month |
| December | EUR 5,884,298 | **−32.5%** | Missed holiday peak |
| July | EUR 5,242,556 | **−21.0%** | Summer slump |
| September | EUR 3,778,141 | **−22.4%** | Soft |

> **December 2020 is the most alarming signal** — typically the strongest month, it fell −32.5% vs 2019 (EUR 5.9M vs EUR 8.7M). This represents EUR 2.83M of missing revenue from a single month.

### Category Performance (2019 vs 2020)

| Category | 2020 Revenue | YoY | Margin 2020 |
|----------|-------------|-----|------------|
| Other | EUR 2,061,873 | **+71.7%** | 16.2% |
| Outdoors | EUR 3,636,725 | **+58.0%** | **17.5%** |
| Books | EUR 7,764,174 | **+43.4%** | 16.4% |
| Appliances | EUR 8,027,083 | **+12.9%** | 16.7% |
| Electronics | EUR 7,623,298 | **+11.1%** | 16.2% |
| Accessories | EUR 2,471,114 | **+10.7%** | 16.7% |
| Smartphones | EUR 5,140,870 | **−13.8%** | 16.5% |
| Games | EUR 7,197,501 | **−11.4%** | 17.2% |
| Beauty | EUR 5,354,534 | **−25.8%** | 17.3% |
| Clothing | EUR 7,467,044 | **−26.8%** | 16.5% |

> **Clothing** lost EUR 2.7M vs 2019 — the single largest category decline. The category lost both 15 orders AND its average price fell 11% — a simultaneous volume and price compression. **Outdoors** grew +58% with the highest margin in the portfolio (17.5%) — standout performer.

### Country Performance (2019 vs 2020)

| Country | 2020 Revenue | YoY | Key Driver |
|---------|-------------|-----|-----------|
| Netherlands | EUR 2,208,785 | **+117.4%** | Explosive growth — single rep Nero Harbisher |
| Portugal | EUR 16,073,409 | **+37.1%** | Top market growing — Celine Tumasian team |
| Denmark | EUR 426,743 | **+26.8%** | Small but growing |
| France | EUR 11,177,584 | **−24.1%** | Lost EUR 3.5M — critical decline |
| Luxembourg | EUR 1,241,235 | **−25.8%** | Declining |
| Spain | EUR 1,009,574 | **−32.2%** | Significant drop |

### Device Type YoY

| Device | 2020 Revenue | YoY |
|--------|-------------|-----|
| PC | EUR 46,607,181 | **+8.3%** |
| Mobile | EUR 7,230,452 | **−12.0%** |
| Tablet | EUR 2,906,581 | **−45.8%** |

> **Tablet revenue nearly halved.** This was flagged for deep investigation (see Section 4).

---

## 4. Tablet Channel Collapse Investigation

### Overall Tablet Snapshot

| Metric | 2019 | 2020 | YoY |
|--------|------|------|-----|
| Orders | 38 | 35 | −7.9% |
| Revenue | EUR 5,360,480 | EUR 2,906,581 | **−45.8%** |
| **Avg Order Value** | **EUR 141,065** | **EUR 83,045** | **−41.1%** |
| Avg Margin | 16.96% | 16.17% | −0.79pp |
| Revenue Share of Total | 9.5% | 5.1% | −4.4pp |

> **Critical insight: the order count barely changed (38 → 35). The entire −45.8% revenue collapse is driven by average order value shrinking from EUR 141K to EUR 83K** — customers did not leave the tablet channel, they placed smaller orders on it.

### Root Cause: Category Collapse on Tablet

| Category | 2019 Tablet Rev | 2020 Tablet Rev | YoY |
|----------|----------------|----------------|-----|
| **Clothing** | EUR 1,375,995 | EUR 120,332 | **−91.3%** |
| **Appliances** | EUR 998,330 | EUR 257,676 | **−74.2%** |
| Smartphones | EUR 885,751 | EUR 378,957 | −57.2% |
| Beauty | EUR 952,973 | EUR 513,356 | −46.1% |
| Electronics | EUR 380,080 | EUR 503,730 | **+32.5%** |
| Books | EUR 37,074 | EUR 178,510 | **+381.5%** |

> **Clothing on Tablet essentially vanished (−91.3%)**, falling from EUR 1.38M to EUR 120K. Combined with Appliances (−74%), these two categories account for approximately EUR 2M of the EUR 2.45M revenue loss on tablet.

### Country Breakdown on Tablet

| Country | 2019 | 2020 | YoY |
|---------|------|------|-----|
| Luxembourg | EUR 569,532 | EUR 0 | **−100%** |
| Ireland | EUR 114,233 | EUR 0 | **−100%** |
| Bulgaria | EUR 37,074 | EUR 0 | **−100%** |
| Sweden | EUR 962,507 | EUR 381,158 | −60.4% |
| UK | EUR 458,446 | EUR 148,850 | −67.5% |
| Portugal | EUR 992,515 | EUR 1,086,869 | **+9.5%** |

> **3 countries went completely to zero on tablet.** Portugal is the only major market holding its tablet share.

### Quarterly Tablet Pattern

| Quarter | 2019 Revenue | 2020 Revenue | YoY |
|---------|-------------|-------------|-----|
| Q1 | EUR 464,299 | EUR 793,467 | **+70.9%** |
| Q2 | EUR 2,026,086 | EUR 591,439 | **−70.8%** |
| Q3 | EUR 882,023 | EUR 1,025,344 | **+16.2%** |
| Q4 | EUR 1,988,071 | EUR 496,331 | **−75.0%** |

> Q2 and Q4 of 2019 contained massive one-off tablet orders (June 2019: EUR 1.24M; December 2019: EUR 1.33M) that were not repeated in 2020. These outlier spikes distorted the baseline.

### Customer Migration — The Key Finding

**16 customers stopped buying on Tablet in 2020. Every single one remained active — they migrated to PC.**

| Customer Lost from Tablet | 2019 Tablet Revenue | 2020 Channel (PC/Mobile) |
|---------------------------|--------------------|-----------------------|
| Walter LLC | EUR 178,615 | → PC: EUR 1,075,629 |
| Friesen-Rath | EUR 163,968 | → PC: EUR 992,278 |
| Farrell, Swaniawski and Crist | EUR 194,531 | → PC: EUR 880,623 + Mobile |
| Hilll-Vandervort | EUR 155,827 | → PC: EUR 759,217 + Mobile |
| Kihn Inc | EUR 154,951 | → PC: EUR 690,276 + Mobile |
| Corwin and Sons | EUR 321,757 | → PC: EUR 608,416 + Mobile |
| McClure Inc | EUR 214,983 | → PC: EUR 589,170 |
| O'Connell-Mitchell | EUR 256,604 | → PC: EUR 492,513 + Mobile |
| Morissette Group | EUR 172,202 | → PC: EUR 474,821 |

> **Zero customers fully churned from the business.** Every customer who left the Tablet channel spent more on PC/Mobile in 2020 than they had spent on Tablet in 2019.

### Order Size Gap Explains the Revenue Drop

| Channel | Median Order (2020) | Mean Order (2020) |
|---------|-------------------|-----------------|
| PC | EUR 111,537 | EUR 116,518 |
| Mobile | EUR 87,513 | EUR 96,406 |
| **Tablet** | EUR 82,116 | EUR 83,045 |

> Tablet orders are structurally **28% smaller** than PC orders. When customers migrated their large orders to PC, tablet revenue collapsed even though some orders continued.

### Root Cause Summary for Tablet Collapse

| # | Finding |
|---|---------|
| 1 | **Not churn — channel migration.** All 16 customers who left tablet stayed active via PC |
| 2 | **Clothing on Tablet collapsed −91%** — the single biggest category driver |
| 3 | **June & December 2019 were outlier spikes** — not structural; 2020 is the true baseline |
| 4 | **3 markets (Luxembourg, Ireland, Bulgaria) went to zero** on tablet purchasing |
| 5 | **PC average order is 40% larger** — natural gravitational pull for larger transactions |
| 6 | **16 new tablet customers acquired in 2020**, all placing small single orders (EUR 27K–141K) |

---

## 5. Deep Investigation — Why 2020 Revenue Did Not Grow

### The Revenue Bridge

The EUR +126,690 net change (virtually zero growth) decomposes into three nearly-cancelling forces:

| Component | EUR | Detail |
|-----------|-----|--------|
| Retained customers (71) — net change | **−224,320** | Existing customers collectively spent less |
| Lost customers (2 churned) | **−153,082** | Littel-Blick & Lind, Mueller |
| New customers (2 added) | **+504,092** | Stehr-Bogan & one other |
| **NET** | **+126,690** | Essentially flat |

> Only **2 customers fully churned** (tiny accounts, EUR 153K combined). The story is in the 71 retained customers: **41 grew** (total uplift EUR +12.49M), **34 declined** (total drag EUR −12.36M). The two sides cancelled each other out almost perfectly.

### Order Frequency vs Deal Size Decomposition

**Revenue = Number of Orders × Average Order Value**

| Component | 2019 | 2020 | Change |
|-----------|------|------|--------|
| Number of Orders | 490 | 510 | **+20 (+4.1%)** |
| Avg Order Value (EUR) | 115,546 | 111,263 | **−4,283 (−3.7%)** |
| Revenue (EUR) | 56,617,524 | 56,744,214 | +126,690 (+0.2%) |

**Decomposed effect:**
- **Volume effect** (+20 orders × 2019 avg price): EUR **+2,310,919**
- **Mix/Price effect** (510 orders × lower avg value): EUR **−2,184,229**
- Net: EUR +126,690

> **The volume gain (+EUR 2.31M) was almost perfectly offset by the AOV decline (−EUR 2.18M).** The business grew its order count but shifted to structurally smaller deals.

### Order Size Bucket Analysis — The Big Deal Problem

| Bucket | Orders 2019 | Orders 2020 | Revenue Δ |
|--------|------------|------------|---------|
| < EUR 50K | 73 | 75 | +EUR 197K |
| EUR 50–100K | 155 | 170 | **+EUR 1.49M** |
| EUR 100–150K | 126 | 146 | **+EUR 2.83M** |
| EUR 150–200K | 85 | 81 | −EUR 1.08M |
| **EUR 200–300K** | **46** | **35** | **−EUR 2.60M** |
| **EUR 300K+** | **5** | **3** | **−EUR 715K** |

> **The large-deal pipeline dried up.** 2019 had 51 orders above EUR 150K; 2020 had only 38. The disappearance of big-ticket orders (>EUR 200K) cost EUR 3.3M that smaller orders could not replace.

### Category Mix Shift — Dual Problem: Volume AND Price

| Category | Orders Δ | AOV 2019 | AOV 2020 | AOV Δ | Revenue Δ |
|----------|---------|---------|---------|------|---------|
| **Clothing** | −15 orders | EUR 119,937 | EUR 106,672 | **−EUR 13,265** | **−EUR 2,727,595** |
| **Beauty** | −7 orders | EUR 118,271 | EUR 99,158 | **−EUR 19,113** | **−EUR 1,859,996** |
| Smartphones | +1 order | EUR 126,825 | EUR 107,101 | −EUR 19,724 | −EUR 819,915 |
| **Outdoors** | +8 orders | EUR 109,636 | EUR 125,404 | **+EUR 15,769** | **+EUR 1,334,374** |
| **Electronics** | −2 orders | EUR 100,864 | EUR 115,505 | **+EUR 14,641** | **+EUR 764,518** |
| **Books** | **+25 orders** | EUR 117,735 | EUR 109,355 | −EUR 8,380 | **+EUR 2,348,370** |

> Clothing lost 15 orders AND its average price fell 11% simultaneously — the worst combination possible. Meanwhile Books gained 25 orders but at a lower AOV — volume compensated but compressed the deal quality. **Category mix is shifting toward lower-value, higher-volume products.**

### Country Analysis — Portugal's Win Was Cancelled

| Country | Revenue Δ | Driver |
|---------|---------|--------|
| **Portugal** | **+EUR 4,350,456** | +33 orders, AOV also up — all metrics positive |
| **Netherlands** | **+EUR 1,192,906** | +6 orders, AOV +EUR 38K — quality growth |
| **France** | **−EUR 3,545,510** | −24 orders AND AOV fell EUR 7,547 — double failure |
| **Sweden** | **−EUR 1,169,225** | −6 orders, AOV also down |
| **UK** | **−EUR 683,950** | Steady decline |

> **Portugal grew EUR 4.35M — but France declined EUR 3.55M and Sweden EUR 1.17M simultaneously.** These are markets #1, #2, and #3 by revenue. When two of the top three decline together, aggregate growth is structurally impossible regardless of what smaller markets do.

### H1 vs H2 — Where Momentum Died

| Period | Orders Δ | AOV Δ | Revenue Δ |
|--------|---------|-------|---------|
| **H1 (Jan–Jun)** | +17 | **+EUR 575** | **+EUR 1,896,076 (+7.4%)** |
| **H2 (Jul–Dec)** | +3 | **−EUR 8,876** | **−EUR 1,769,387 (−5.7%)** |

> **H1 looked like a genuine growth year (+7.4%). H2 reversed it entirely.** The average order value in H2 collapsed by EUR 8,876 per order. This is the core narrative arc of 2020: strong start, structural second-half weakness.

### Month-by-Month Loss vs Gain

| Losing Months | Revenue Lost | Gaining Months | Revenue Gained |
|--------------|------------|----------------|---------------|
| December | −EUR 2,829,478 | November | +EUR 1,773,412 |
| July | −EUR 1,396,053 | May | +EUR 1,712,262 |
| September | −EUR 1,091,919 | August | +EUR 1,277,075 |
| February | −EUR 936,151 | March | +EUR 1,058,116 |
| June | −EUR 534,097 | January | +EUR 699,085 |
| April | −EUR 103,139 | October | +EUR 497,577 |
| **TOTAL** | **−EUR 6,890,837** | **TOTAL** | **+EUR 7,017,527** |

> Six months gained EUR 7.0M; six months lost EUR 6.9M. **The entire year's net growth (EUR +126K) came from a EUR 127K margin between two equally matched halves.** There was no underlying growth trend — only random monthly variation.

### Johns & Sons — The Elephant in the Room

| Metric | 2019 | 2020 | Δ |
|--------|------|------|---|
| Revenue | EUR 9,344,592 | EUR 7,015,665 | **−EUR 2,328,926 (−24.9%)** |
| Orders | 80 | 62 | **−18 orders** |
| Avg Order Value | EUR 116,807 | EUR 113,156 | −EUR 3,652 |
| Revenue share | 16.5% | 12.4% | −4.1pp |

**Where Johns & Sons pulled back:**

| Category | 2019 | 2020 | Δ |
|----------|------|------|---|
| Books | EUR 1,581,886 | EUR 776,898 | −EUR 804,987 |
| Outdoors | EUR 835,492 | EUR 124,235 | −EUR 711,257 |
| Games | EUR 1,129,569 | EUR 671,141 | −EUR 458,428 |
| Clothing | EUR 1,390,859 | EUR 973,536 | −EUR 417,323 |

> **Johns & Sons alone subtracted EUR 2.33M from 2020** — nearly 18× the total net revenue change. Without this single account's decline, 2020 would have grown +4.3%. All other 74 customers combined delivered +EUR 2.46M of growth, which Johns & Sons almost entirely absorbed.

### Sales Rep-Level Contributors

**Biggest gainers:**

| Rep | Revenue Δ |
|----|---------|
| Brynn Dempster | **+EUR 2,148,931 (+165%)** |
| Nero Harbisher | +EUR 1,192,906 (+117%) |
| Aurelie Wren | +EUR 1,117,897 (+51%) |

**Biggest losers:**

| Rep | Revenue Δ |
|----|---------|
| Maighdiln Upcraft | **−EUR 1,610,013 (−56%)** |
| Alyosha Meah | −EUR 1,516,715 (−50%) |
| Amelina Piscopiello | −EUR 1,468,884 (−36%) |

> The three underperforming reps collectively cost **−EUR 4.6M** in 2020 vs their own 2019 output. None left the company. This suggests performance management gaps at the manager level.

### Quantified Root Causes — Ranked by Impact

| # | Root Cause | Revenue Impact | Recommended Action |
|---|-----------|---------------|-------------------|
| 1 | Johns & Sons pulled back 18 orders | −EUR 2.33M | Dedicated key account manager; investigate why spend fell −25% |
| 2 | France territory declined (Othello Bowes) | −EUR 3.55M | Urgent territory review; fewer and smaller deals is a strategic red flag |
| 3 | Large deal pipeline dried up (>EUR 200K: 51→38 orders) | −EUR 3.3M | Pipeline health review; diagnose why big deals are not closing |
| 4 | Clothing category collapsed (orders AND price fell) | −EUR 2.73M | Product-market fit investigation; customer feedback analysis |
| 5 | 3 reps underperforming vs 2019 by −50% each | −EUR 4.6M | Performance improvement plans; coaching from top performers |

---

## 6. Sales Manager Efficiency Review

### Efficiency Scorecard (2020)

Key metrics defined:
- **Rev/Rep** = Total revenue ÷ number of reps managed
- **Orders/Rep** = Total orders ÷ number of reps managed
- **Rev/Cust** = Total revenue ÷ number of unique customers

| Manager | Revenue | Rev/Rep | Ord/Rep | AOV | Margin | Rev/Cust | Overall Rank |
|---------|---------|---------|--------|-----|--------|---------|-------------|
| **Celine Tumasian** | EUR 16.1M | **EUR 3,215K** | **27.2** | EUR 118K | 16.93% | **EUR 292K** | **#1** |
| Othello Bowes | EUR 11.2M | EUR 2,236K | 20.8 | EUR 107K | 16.58% | EUR 248K | #2 |
| Maxie Marrow | EUR 9.2M | EUR 1,847K | 17.6 | EUR 105K | 16.92% | EUR 201K | #4 |
| Jessamine Apark | EUR 5.7M | EUR 1,905K | 16.0 | EUR 119K | 16.77% | EUR 204K | #3 |
| Hube Corey | EUR 3.0M | EUR 1,505K | 11.0 | EUR 137K | 15.29% | EUR 177K | #6 |
| Denice Amberg | EUR 2.2M | EUR 2,209K | 17.0 | EUR 130K | 16.24% | EUR 138K | #5 |
| Ilsa Kob | EUR 1.2M | EUR 1,241K | 9.0 | EUR 138K | 16.94% | EUR 138K | #7 |
| Emalia Dinse | EUR 1.0M | EUR 337K | 3.7 | EUR 92K | 17.03% | EUR 112K | #11 |
| Modestia Byfford | EUR 0.4M | EUR 213K | 3.5 | EUR 61K | 17.47% | EUR 61K | #14 |

### Efficiency Tier Classification (Z-Score Composite)

> Managers are scored across 5 dimensions (Revenue, AOV, Margin, Rev/Rep, Rev/Cust) using Z-scores then averaged. See Section 7 for full methodology.

| Manager | Composite Z-Score | YoY Revenue | Tier |
|---------|------------------|------------|------|
| **Celine Tumasian** | **+1.55** | +37.1% | 🌟 **STAR** |
| Othello Bowes | +0.82 | −24.1% | ⚠️ **WATCH** |
| Maxie Marrow | +0.54 | −11.2% | ⚠️ **WATCH** |
| Jessamine Apark | +0.53 | −10.7% | ⚠️ **WATCH** |
| Ilsa Kob | +0.20 | −25.8% | ⚠️ **WATCH** |
| Denice Amberg | +0.25 | +117.4% | ✅ **SOLID** |
| Hube Corey | +0.14 | +18.6% | ✅ **SOLID** |
| Rickard Doogood | −0.07 | −1.8% | 🔴 **AT RISK** |
| Charil Alpe | −0.19 | −17.6% | 🔴 **AT RISK** |
| Emalia Dinse | −0.52 | −32.2% | 🔴 **AT RISK** |
| Glenine Suttaby | −0.41 | +14.5% | 📈 **DEVELOPING** |
| Piggy Roscrigg | −0.65 | +3.6% | 📈 **DEVELOPING** |
| Modestia Byfford | −0.94 | +26.8% | 📈 **DEVELOPING** |
| Lambert Norheny | −1.04 | +66.4% | 📈 **DEVELOPING** |
| Orsa Geekin | −0.21 | NEW | 📈 **DEVELOPING** |

**Tier definitions:**
- **STAR** = high composite efficiency score AND positive YoY growth
- **SOLID** = average or above composite AND growing
- **WATCH** = above-average composite but declining — efficient but losing ground
- **AT RISK** = below-average composite AND declining
- **DEVELOPING** = growing but below-average efficiency — scale not yet reached

### Individual Manager Deep-Dives

#### 🌟 Celine Tumasian — STAR (Portugal)

Best performer on every single metric simultaneously.

| Metric | Value | Rank vs Group |
|--------|-------|--------------|
| Revenue 2020 | EUR 16.07M | #1 |
| YoY Growth | +37.1% (+EUR 4.35M) | #1 |
| Rev/Rep | EUR 3,215K | #1 — 44% above #2 |
| Orders/Rep | 27.2 | #1 |
| Customer Retention | 80% | Best in top-4 |
| New Customers | 20 | Highest of all managers |

Her 5-rep team breakdown:

| Rep | Revenue 2020 | YoY | Status |
|----|-------------|-----|--------|
| Corene Shirer | EUR 3.91M | +30.8% | Star |
| Brynn Dempster | EUR 3.45M | **+164.7%** | Breakout |
| Aurelie Wren | EUR 3.30M | +51.2% | Rising |
| Smitty Culverhouse | EUR 2.48M | +23.0% | Solid |
| Hortense Gerring | EUR 2.93M | −9.3% | Slight dip |

> 4 of 5 reps grew. This is a well-led, high-performing team — the company's model team.

---

#### ⚠️ Othello Bowes — WATCH (France)

High absolute efficiency but all metrics moving in the wrong direction.

| Metric | 2019 | 2020 | YoY |
|--------|------|------|-----|
| Revenue | EUR 14.7M | EUR 11.2M | **−24.1%** |
| AOV | EUR 115K | EUR 107K | −6.6% |
| Rev/Customer | EUR 289K | EUR 248K | −14.0% |
| Customer Retention | 51 customers | 45 customers | Lost 14, gained 8 (73% retention) |

His 5-rep team breakdown (2020):

| Rep | Revenue 2020 | YoY | Issue |
|----|-------------|-----|-------|
| Avrit Chanders | EUR 2.67M | **+31.1%** | Only grower |
| Amelina Piscopiello | EUR 2.59M | **−36.2%** | Lost EUR 1.47M |
| Ora Grennan | EUR 2.37M | −17.4% | Declining |
| Crysta Halls | EUR 2.28M | −20.9% | Declining |
| Maighdiln Upcraft | EUR 1.26M | **−56.0%** | Lost EUR 1.61M |

> Root cause: Maighdiln Upcraft (−EUR 1.61M) and Amelina Piscopiello (−EUR 1.47M) together lost EUR 3.08M — this alone explains most of the team's total decline. The manager has not arrested the fall of two key reps.

---

#### ⚠️ Maxie Marrow — WATCH (Sweden)

| Metric | 2019 | 2020 | YoY |
|--------|------|------|-----|
| Revenue | EUR 10.4M | EUR 9.2M | −11.2% |
| Orders | 94 | 88 | −6.4% |
| AOV | EUR 110.7K | EUR 104.9K | −5.2% |

His 5-rep team — 2 growing, 3 declining:

| Rep | Revenue 2020 | YoY |
|----|-------------|-----|
| Madelon Bront | EUR 2.29M | **+37.5%** |
| Caro Morfield | EUR 1.63M | **+22.8%** |
| Anita Woakes | EUR 1.82M | +1.7% (flat) |
| Tarrah Castelletti | EUR 1.98M | −23.5% |
| **Alyosha Meah** | EUR 1.51M | **−50.0%** |

> Alyosha Meah alone lost EUR 1.52M — a −50% personal collapse from the team's previous top earner.

---

#### ⚠️ Jessamine Apark — WATCH (UK)

| Metric | 2019 | 2020 | YoY |
|--------|------|------|-----|
| Revenue | EUR 6.4M | EUR 5.7M | −10.7% |
| Customer Retention | 29 customers | 28 customers | **52% retention** (lost 14, gained 13) |

Her 3-rep team — 1 growing, 2 declining:

| Rep | Revenue 2020 | YoY |
|----|-------------|-----|
| Winny Agnolo | EUR 2.65M | **+30.9%** |
| Genevra Charrisson | EUR 1.90M | −22.2% |
| Jay Morefield | EUR 1.17M | **−39.7%** |

> The 52% customer retention rate (worst of the top-4 managers) signals a systematic relationship problem, not just deal-closure difficulties.

---

#### ✅ Denice Amberg — SOLID (Netherlands) — Standout for expansion

| Metric | 2019 | 2020 | YoY |
|--------|------|------|-----|
| Revenue | EUR 1.02M | EUR 2.21M | **+117.4%** |
| AOV | EUR 92K | **EUR 130K** | **+40.7%** |
| Profit/Order | EUR 15,654 | EUR 20,787 | **+32.8%** |
| Customers | 9 | 16 | +78% |

> One manager, one rep (Nero Harbisher) — doubled the business in a year while increasing both deal quality AND profitability. This team needs additional resources to scale. It is the highest-growth unit in the portfolio on a percentage basis.

---

#### 🔴 Emalia Dinse — AT RISK (Spain)

Three reps with divergent performance — manager has not cross-pollinated the success:

| Rep | Revenue 2020 | YoY |
|----|-------------|-----|
| Manuel Goudie | EUR 337K | **+390.4%** |
| Perri Aldersley | EUR 353K | **−47.7%** |
| Bertha Walbrook | EUR 320K | **−57.1%** |

> One rep is exploding, two are collapsing. The manager has not transferred Goudie's approach to the others. **Revenue/Rep of EUR 337K is the lowest among all multi-rep teams.**

### Quarterly Consistency (Coefficient of Variation, 2020)

CV% = StdDev of quarterly revenue / Average quarterly revenue × 100. **Lower = more consistent.**

| Manager | CV% | Assessment |
|---------|-----|-----------|
| Othello Bowes | 24% | Most consistent pipeline |
| Maxie Marrow | 26% | Smooth and reliable |
| Celine Tumasian | 35% | Q2 spike — growth is lumpy but present |
| Jessamine Apark | 35% | Reasonable |
| Ilsa Kob | 75% | Q3 spike, Q2 near-zero — very erratic |
| Denice Amberg | 63% | Q3 nearly zero — pipeline gap |
| Emalia Dinse | 65% | Unpredictable |
| Modestia Byfford | 85% | Almost all revenue in Q2 |
| Orsa Geekin | 138% | Only Q1 and Q4 — significant mid-year gap |

### Customer Retention by Manager (2020)

| Manager | 2019 Custs | Retained | Lost | New | Retention% |
|---------|-----------|---------|------|-----|-----------|
| **Celine Tumasian** | 44 | 35 | 9 | 20 | **80%** |
| Othello Bowes | 51 | 37 | 14 | 8 | 73% |
| Maxie Marrow | 50 | 35 | 15 | 11 | 70% |
| Glenine Suttaby | 8 | 5 | 3 | 17 | 62% |
| Jessamine Apark | 29 | 15 | 14 | 13 | 52% |
| Denice Amberg | 9 | 4 | 5 | 12 | 44% |
| Hube Corey | 15 | 4 | 11 | 13 | 27% |
| Emalia Dinse | 11 | 3 | 8 | 6 | 27% |
| **Charil Alpe** | 13 | 2 | 11 | 11 | **15%** |
| **Rickard Doogood** | 9 | 1 | 8 | 10 | **11%** |
| **Ilsa Kob** | 9 | 1 | 8 | 8 | **11%** |

> Charil Alpe, Rickard Doogood, and Ilsa Kob have retention rates of 11–15% — essentially replacing their entire customer base annually. This means no compounding relationship value and constant cold-start cost of sale for every order.

---

## 7. Composite Score Methodology

### Overview

The composite score assesses each manager's **relative efficiency** compared to the peer group using Z-score normalisation across 5 dimensions. It is a descriptive benchmarking tool, not an absolute performance rating.

### Step 1 — Five Dimensions Selected

| Dimension | Column | Business Rationale |
|-----------|--------|-------------------|
| Revenue | `revenue` | Primary output measure |
| AOV | `aov` | Deal quality — are they selling large tickets? |
| Margin % | `avg_margin` | Profit discipline |
| Revenue per Rep | `rev_per_rep` | Team productivity efficiency |
| Revenue per Customer | `rev_per_cust` | Account depth and relationship value |

### Step 2 — Z-Score Normalisation

For each dimension, each manager's raw value is standardised:

```
Z = (manager_value − group_mean) / group_standard_deviation
```

**Interpretation:**
- Z = 0 → exactly at the group average
- Z = +1.0 → 1 standard deviation above average
- Z = −1.0 → 1 standard deviation below average
- All dimensions are now on a comparable scale regardless of units

### Step 3 — Simple Average

```
Composite = (Z_revenue + Z_aov + Z_margin + Z_rev_per_rep + Z_rev_per_cust) / 5
```

### Worked Example — Celine Tumasian (score: +1.55)

| Dimension | Her Value | Group Mean | Group Std | Z-Score |
|-----------|-----------|-----------|-----------|---------|
| Revenue | EUR 16.07M | EUR 3.72M | EUR 4.76M | +2.59 |
| AOV | EUR 118K | EUR 103K | EUR 24K | +0.60 |
| Margin % | 16.93% | 16.74% | 1.21% | +0.15 |
| Rev/Rep | EUR 3,215K | EUR 1,203K | EUR 932K | +2.16 |
| Rev/Cust | EUR 292K | EUR 133K | EUR 71K | +2.23 |
| **Composite** | | | | **(2.59+0.60+0.15+2.16+2.23) / 5 = +1.55** |

### Known Limitations

| Limitation | Impact |
|-----------|--------|
| **Equal weighting** | Revenue and Margin are treated as equally important |
| **Revenue double-counted** | Revenue, Rev/Rep, and Rev/Cust all derive from revenue — slight revenue bias |
| **No growth dimension** | YoY% is reported separately but not in the composite score |
| **Scale sensitivity** | Solo managers (1 rep, few customers) produce extreme Z-scores |
| **No volume adjustment** | A 1-rep manager vs a 5-rep manager face structurally different constraints |

### Recommended Alternative — Weighted Composite

| Dimension | Suggested Weight | Rationale |
|-----------|-----------------|-----------|
| Revenue | 30% | Primary output |
| YoY Growth | 25% | Direction matters as much as level |
| Rev/Rep | 20% | Team efficiency |
| Margin % | 15% | Profit quality |
| Customer Retention | 10% | Relationship sustainability |

---

## 8. Customer × Sales Rep Overlap Analysis

### Scale of the Multi-Rep Phenomenon

| Metric | Value |
|--------|-------|
| Total customers | 75 |
| Customers served by **only 1 rep ever** | **4 (5.3%)** |
| Customers served by **2+ reps** | **71 (94.7%)** |
| Customer–Country combos with 2+ reps in same country | **162** |
| Cross-manager account conflicts (same customer, same country, different managers) | **0** |

> **94.7% of customers have been served by more than one sales rep.** This is not an exception — it is the structural norm of the business. Importantly, all multi-rep situations occur **within the same manager's team** — no cross-manager territorial conflicts exist.

### Rep Overlap by Country

| Country | Customers | Multi-Rep % | Active Reps | Assessment |
|---------|-----------|------------|-------------|-----------|
| **France** | 59 | **81%** | 5 | Saturated — no effective account ownership |
| **Portugal** | 64 | **70%** | 5 | Saturated |
| **Sweden** | 61 | **59%** | 5 | Heavy overlap |
| **UK** | 42 | 36% | 3 | Moderate overlap |
| Spain | 17 | 24% | 3 | Some overlap |
| Finland / Ireland | 28 / 25 | ~25% | 2 each | Manageable — 2-rep territories |
| Germany / Netherlands / Luxembourg / Austria | — | **0%** | 1 each | Clean — single-rep territories |

### Three Structural Scenarios

#### Scenario A — Sequential Handoff (~18% of cases) ✅

The customer was served by Rep X, then the account was transferred to Rep Y. Their active periods do not overlap in time.

**Cause:** Territory restructure, rep departure, or planned account reassignment.
**Risk:** Low — normal sales management. Main risk is knowledge-transfer gaps during handoff.
**Example:** Schowalter, Lesch and Beahan | Portugal — served by different reps across 2019 vs 2020 with no date overlap.

#### Scenario B — Concurrent Overlap (~40% of cases) ⚠️

Multiple reps are actively serving the **same customer simultaneously** — their active periods overlap in the calendar.

**Cause:** No sub-territory or account ownership rules within the manager's country. All reps in a territory are free to approach any customer.
**Risk:** High — internal price competition, commission disputes, confused customer contact, no single relationship owner.

**Most severe example — Johns & Sons | France (33 orders, EUR 3.77M):**

| Rep | Active Window | Orders |
|-----|--------------|--------|
| Amelina Piscopiello | Jan 2019 → Dec 2020 | 9 |
| Avrit Chanders | Jan 2019 → Sep 2020 | 3 |
| Crysta Halls | Feb 2019 → Jun 2019 | 3 |
| Maighdiln Upcraft | Sep 2019 → Nov 2020 | 5 |
| Ora Grennan | Mar 2019 → Dec 2020 | 13 |

All 5 reps simultaneously active on the same account for nearly 2 years. On some dates, two different reps placed orders for the same customer within days of each other.

**Same pattern confirmed in:** Johns & Sons | Portugal (5 reps), Johns & Sons | Sweden (4 reps), Johns & Sons | UK (3 reps).

#### Scenario C — Product / Department Split (~42% of cases) ✅ if managed

Different reps serve the same customer but in **different product categories**, with non-overlapping date windows.

**Cause:** Large enterprise customers have separate buying departments (e.g., IT buys Electronics, Procurement buys Appliances). Each rep owns their product line for that customer.
**Risk:** Low if intentional and coordinated. Risk emerges if reps are unaware of each other's activity.

**Examples:**
- Bashirian, Okuneva and Bechtelar | Portugal: Aurelie Wren → Books & Clothing; Smitty Culverhouse → Electronics & Appliances
- Walter LLC | Sweden: Anita Woakes → Outdoors; Tarrah Castelletti → Beauty & Accessories

### Johns & Sons — The Most Complex Account in the Business

| Metric | Value |
|--------|-------|
| Total orders (2 years) | 142 |
| Total revenue | EUR 16,360,257 |
| Countries active in | 14 |
| Unique sales reps ever | **31** |
| Unique managers touched | 9 |

**Every country in this account has multiple reps — all confirmed CONCURRENT (Scenario B).**

> A buyer at Johns & Sons in France, for example, may receive calls from 5 different "account managers" from the same company. With 31 reps touching this account, consistent pricing, messaging, and relationship management are essentially impossible.

### Why This Happens — Structural Root Cause

Territory is defined at the **manager level** (one manager = one country), but there are **no sub-territory or account ownership rules at the rep level within that country**.

```
Manager Celine Tumasian  =  Portugal territory
  └── ALL 5 of her reps can call on ANY customer in Portugal
        → No named account list per rep exists
        → First rep to reach the customer wins the order
        → Customer interacts with whichever rep calls them
```

Single-rep markets (Germany, Netherlands, Luxembourg, Austria) have zero overlap simply because there is no second rep who could create it.

### Business Risks of Concurrent Overlap

| Risk | Description |
|------|------------|
| **Internal price competition** | Two reps from the same team may offer different discounts to win the same deal |
| **No account ownership** | When revenue declines (like Johns & Sons −25%), no single person is clearly accountable |
| **Commission disputes** | Who receives credit for a relationship they jointly touched? |
| **Customer confusion** | The buyer receives calls from multiple "account managers" — erodes professional image |
| **Knowledge fragmentation** | No rep knows the full account history — context is split across many people |
| **Churn blindspot** | If 3 of 5 reps quietly stop calling, no one notices the relationship is weakening |

### Recommended Solutions

| Action | Detail |
|--------|--------|
| **Assign named account owners** | For every customer in France, Portugal, Sweden: one primary rep owns the relationship |
| **Start with top accounts** | Johns & Sons, Hessel-Stiedemann, Larkin-Collier are highest-value concurrent cases |
| **Formalise Category C splits** | Where product/department splits are intentional, document them formally |
| **Keep Scenario A handoffs** | Sequential transitions are acceptable — just enforce structured 30-day overlap knowledge transfer |
| **Redesign sub-territories** | With 5 reps per major market, divide customers into 5 named account lists — eliminates overlap |
| **Link commission to ownership** | Revenue credit flows to the named account owner, not whoever placed the last order |

---

## 9. Manager Imbalance & Consolidation Strategy

### The Scale of the Imbalance

Every manager today owns exactly one country. Territory size — not business volume — determines workload, yet territories are wildly unequal:

| Metric | Smallest Manager | Largest Manager | Ratio |
|--------|-----------------|----------------|-------|
| **Revenue** | EUR 190,166 (Orsa Geekin) | EUR 27,796,362 (Celine Tumasian) | **146×** |
| **Customers** | 2 (Orsa Geekin) | 64 (Celine Tumasian) | **32×** |
| **Orders** | 2 (Orsa Geekin) | 239 (Celine Tumasian) | **120×** |
| **Reps** | 1 | 5 | 5× |

### Current Territory Map (15 Managers)

| Manager | Country | Customers | Reps | Revenue | Rev Share |
|---------|---------|-----------|------|---------|----------|
| Celine Tumasian | Portugal | 64 | 5 | EUR 27.8M | 24.5% |
| Othello Bowes | France | 59 | 5 | EUR 25.9M | 22.8% |
| Maxie Marrow | Sweden | 61 | 5 | EUR 19.6M | 17.3% |
| Jessamine Apark | UK | 42 | 3 | EUR 12.1M | 10.7% |
| Hube Corey | Finland | 28 | 2 | EUR 5.5M | 4.9% |
| Glenine Suttaby | Ireland | 25 | 2 | EUR 5.0M | 4.4% |
| Charil Alpe | Bulgaria | 24 | 2 | EUR 3.5M | 3.1% |
| Denice Amberg | Netherlands | 21 | 1 | EUR 3.2M | 2.8% |
| Ilsa Kob | Luxembourg | 17 | 1 | EUR 2.9M | 2.6% |
| Rickard Doogood | Germany | 19 | 1 | EUR 2.8M | 2.5% |
| Emalia Dinse | Spain | 17 | 3 | EUR 2.5M | 2.2% |
| Piggy Roscrigg | Italy | 10 | 1 | EUR 0.9M | 0.8% |
| Modestia Byfford | Denmark | 11 | 2 | EUR 0.8M | 0.7% |
| Lambert Norheny | Belgium | 6 | 1 | EUR 0.6M | 0.5% |
| **Orsa Geekin** | Austria | 2 | 1 | EUR 0.2M | 0.2% |

> **The bottom 4 managers combined** (Piggy Roscrigg, Modestia Byfford, Lambert Norheny, Orsa Geekin) generate **EUR 2.5M = 2.2% of total revenue** — less than what Celine Tumasian's team generates in a single average month.

### Country Complexity Score

*(Revenue weight 50% + Customer count weight 50%, normalised to 100 based on Portugal as maximum)*

| Country | Manager | Complexity | Verdict |
|---------|---------|-----------|---------|
| Portugal | Celine Tumasian | **100.0 / 100** | Requires full-time dedicated manager |
| France | Othello Bowes | **92.7 / 100** | Requires full-time dedicated manager |
| Sweden | Maxie Marrow | **83.0 / 100** | Requires full-time dedicated manager |
| UK | Jessamine Apark | **54.6 / 100** | Requires full-time dedicated manager |
| Finland | Hube Corey | **31.9 / 100** | Borderline — manageable with one add-on |
| Ireland | Glenine Suttaby | **28.4 / 100** | Can pair with Portugal cluster |
| Netherlands | Denice Amberg | **23.1 / 100** | Can anchor a DACH/small-market cluster |
| Bulgaria | Charil Alpe | **20.1 / 100** | Can pair with Italy |
| Germany | Rickard Doogood | **18.1 / 100** | Natural DACH cluster (Ger + Lux + Aus) |
| Luxembourg | Ilsa Kob | **16.5 / 100** | Absorb into DACH cluster |
| Spain | Emalia Dinse | **17.8 / 100** | Borderline — keep standalone for now |
| Italy | Piggy Roscrigg | **7.0 / 100** | Absorb immediately |
| Denmark | Modestia Byfford | **10.0 / 100** | Natural pair with Sweden |
| Belgium | Lambert Norheny | **5.6 / 100** | Natural pair with France (French-speaking) |
| Austria | Orsa Geekin | **2.7 / 100** | Absorb immediately — 2 customers, 2 orders |

### Proposed New Structure — 15 Managers → 8 Managers

**Guiding principles for pairing:**
1. Geographic proximity (neighbouring countries)
2. Cultural / language affinity (e.g. French-speaking Belgium with France; Scandinavian Denmark with Sweden; DACH cluster)
3. Combined complexity score ≤ 130/100 (no manager overburdened)
4. Every manager maintains minimum EUR 5M combined revenue
5. Absorbing manager must have demonstrated capacity (growth trend, efficient Rep/Rev ratio)

| # | Manager | Countries | Customers | Reps | Revenue | Complexity |
|---|---------|-----------|-----------|------|---------|-----------|
| 1 | **Celine Tumasian** | Portugal + Ireland | 67 | 7 | **EUR 32.7M** | 128.4 |
| 2 | **Othello Bowes** | France + Belgium | 59 | 6 | **EUR 26.5M** | 98.5 |
| 3 | **Maxie Marrow** | Sweden + Denmark | 62 | 7 | **EUR 20.4M** | 93.0 |
| 4 | **Jessamine Apark** | UK + Netherlands | 48 | 4 | **EUR 15.3M** | 76.8 |
| 5 | **Hube Corey** | Finland (standalone) | 28 | 2 | **EUR 5.5M** | 31.9 |
| 6 | **Denice Amberg** | Germany + Luxembourg + Austria | 29 | 3 | **EUR 5.9M** | 40.3 |
| 7 | **Charil Alpe** | Bulgaria + Italy | 30 | 3 | **EUR 4.4M** | 34.5 |
| 8 | **Emalia Dinse** | Spain (standalone) | 17 | 3 | **EUR 2.5M** | 17.8 |

**Total revenue covered: EUR 113,361,739 = 100% of total.**

### Pairing Rationale

| Pair | Rationale |
|------|-----------|
| **Portugal + Ireland** | Both Atlantic-facing, Celine's growth engine absorbs a smaller market also showing growth (+14.5%). Her team gains 2 Irish reps. |
| **France + Belgium** | French-speaking Belgium pairs naturally with France. Othello's network extends without cultural shift. Lambert Norheny's 1 rep slots into Othello's team. |
| **Sweden + Denmark** | Classic Scandinavian cluster — shared business culture, geographic proximity. Modestia's 2 reps fold into Maxie's team, which gains capacity. |
| **UK + Netherlands** | Both English-language markets; Jessamine gains Nero Harbisher (+117% YoY) from Denice's team, adding growth potential. |
| **Germany + Luxembourg + Austria** | Standard DACH cluster used across European sales organisations. Denice Amberg (+117% YoY) is the ideal candidate — proven ability to grow small markets, high AOV improvement. |
| **Bulgaria + Italy** | Both smaller, lower-complexity markets. Combined complexity 34.5 — comfortably within single-manager capacity. |

### 7 Managers Proposed for Elimination

| Manager | Current Revenue | Absorbed By | Key Rationale |
|---------|----------------|-------------|--------------|
| **Orsa Geekin** | EUR 190,166 | → Denice Amberg | Austria: 2 customers, 2 orders — a sub-territory, not a real country operation. Absorb immediately. |
| **Lambert Norheny** | EUR 608,970 | → Othello Bowes | Belgium is French-speaking and geographically adjacent. One rep (Collin Mackness) folds into Othello's team. |
| **Modestia Byfford** | EUR 763,204 | → Maxie Marrow | Denmark is Scandinavian — natural extension of Sweden territory. 2 reps join Maxie's team. |
| **Piggy Roscrigg** | EUR 935,569 | → Charil Alpe | Italy pairs with Bulgaria as an emerging/smaller market cluster. |
| **Rickard Doogood** | EUR 2,794,049 | → Denice Amberg | Germany + Luxembourg + Austria = standard DACH cluster. 1 rep (Casie MacBain) joins Denice. |
| **Ilsa Kob** | EUR 2,913,550 | → Denice Amberg | Luxembourg already in DACH cluster. 1 rep (Jocelyn Laurentino) joins Denice. Retention issue (11%) suggests no lost momentum. |
| **Glenine Suttaby** *(conditional)* | EUR 4,952,285 | → Celine Tumasian | Ireland growing +14.5%. **Conditional: review H1 2021. Only absorb if growth plateaus. If growth continues, Glenine stays.** |

### Cost Saving Estimate

| Scenario | Basis | Annual Saving |
|----------|-------|--------------|
| Conservative | 7 managers × EUR 80K (salary only) | **EUR 560,000** |
| Mid | 7 managers × EUR 100K (salary + benefits + overhead) | **EUR 700,000** |
| Full | 7 managers × EUR 120K (including travel, tools, office) | **EUR 840,000** |
| **As % of total profit** | EUR 700K / EUR 18.99M | **3.69%** |
| **As % of total revenue** | EUR 700K / EUR 113.4M | **0.62%** |

> Even the conservative estimate (EUR 560K) is more than **3× the combined revenue** of Orsa Geekin + Lambert Norheny (EUR 799K combined). The cost of managing these territories exceeds their incremental revenue contribution.

### Decision Framework — Phased Elimination

**Phase 1 — Eliminate immediately (clear ROI, minimal customer relationship risk):**
- ✅ Orsa Geekin — 2 customers, brand new territory, no entrenched relationships
- ✅ Lambert Norheny — Belgium absorbs into France (same language, adjacent)
- ✅ Modestia Byfford — Denmark into Sweden (Scandinavian cluster, natural)
- ✅ Piggy Roscrigg — Italy into Bulgaria cluster (similar scale and complexity)

**Phase 2 — Eliminate with 60-day structured transition:**
- ✅ Rickard Doogood — Germany is established; structured knowledge transfer to Denice Amberg required
- ✅ Ilsa Kob — Luxembourg similarly established; low retention rate (11%) means customer relationships are already weak — limited downside

**Phase 3 — Conditional (review H1 2021 data before deciding):**
- ⚠️ Glenine Suttaby — Ireland +14.5% growth in 2020; if growth continues in H1 2021, retain. If flat, absorb into Celine Tumasian's team.

### Risks & Mitigations

| Risk | Probability | Mitigation |
|------|------------|-----------|
| Customer relationship disruption during handover | Medium | 90-day parallel period; departing manager introduces successor to each key account personally |
| Celine Tumasian overload (complexity 128.4 with Ireland) | Medium | Complexity is within the target ceiling of 130; gains 2 additional reps from Ireland |
| Denice Amberg's DACH cluster is all low-volume markets | Low | Combined EUR 5.9M with her +117% YoY track record; she has demonstrated the ability to grow small markets |
| Ireland momentum lost if Glenine absorbed | High | Explicitly conditional — do not absorb until growth plateaus; Glenine's 2 reps remain regardless |
| Emalia Dinse remaining sub-scale (EUR 2.5M) | High | If Spain does not grow in 2021, fold into a Southern Europe cluster with Italy/Bulgaria |
| Rep confusion during transition | Low | Only the manager layer changes; all reps remain in current territories and account relationships |

---

## 10. Master Recommendations

### Immediate Actions (0–30 days)

| Priority | Action | Expected Impact |
|----------|--------|----------------|
| 🔴 1 | **Assign a dedicated key account manager to Johns & Sons** — one named person across all countries | Stabilise the EUR 16.4M account that declined −25% in 2020 |
| 🔴 2 | **Performance review for Maighdiln Upcraft (−56%), Alyosha Meah (−50%), Amelina Piscopiello (−36%)** | These 3 reps cost EUR 4.6M in 2020; intervention or territory change needed |
| 🔴 3 | **Eliminate Orsa Geekin and Lambert Norheny territories** (absorb into existing teams) | EUR 160K+ immediate saving; 0 revenue at risk |
| 🟡 4 | **Assign named account owners in France, Portugal, Sweden** — end concurrent rep overlap | Fix 162 customer–country combos where multiple reps compete for the same account |

### Short-Term Actions (30–90 days)

| Priority | Action | Expected Impact |
|----------|--------|----------------|
| 🟡 5 | **Eliminate Modestia Byfford and Piggy Roscrigg** with structured 60-day transition | EUR 240K saving; reps retained and merged into adjacent teams |
| 🟡 6 | **Eliminate Rickard Doogood and Ilsa Kob** with structured 60-day transition | EUR 560K saving; DACH cluster under Denice Amberg |
| 🟡 7 | **Investigate Clothing category collapse** — price AND volume fell simultaneously | EUR 2.73M drag that needs product/market root-cause analysis |
| 🟡 8 | **Scale Denice Amberg's team** — add 1 additional rep to Netherlands | The portfolio's highest-growth unit (EUR +1.19M, +117%) needs headcount to sustain momentum |
| 🟡 9 | **Investigate the tablet + Clothing intersection** — Clothing on tablet fell −91% | This specific combination almost certainly has a UX or product discovery problem on the tablet channel |

### Medium-Term Structural Changes (90 days – 6 months)

| Priority | Action | Expected Impact |
|----------|--------|----------------|
| 🟢 10 | **Review Glenine Suttaby / Ireland after H1 2021** — absorb or retain based on growth | EUR 100K saving + EUR 5M territory decisions |
| 🟢 11 | **Review Emalia Dinse / Spain after 2021** — fold into Southern Europe cluster if stagnant | Resolve the only manager still below minimum viable territory scale after consolidation |
| 🟢 12 | **Study Celine Tumasian's management approach** — document and replicate playbook | Her team has 4/5 reps growing; her coaching methods should be the company template |
| 🟢 13 | **Redesign rep-level commission structure** to reward named account ownership | Eliminate incentive for reps to compete for the same customer's orders |
| 🟢 14 | **Introduce account-level revenue reporting** — track Johns & Sons monthly | A 14.4% customer should have a dedicated dashboard, not blend into aggregate reports |

---

*End of report. All figures derived from `Ex01_Raw.xlsx` using Python (pandas). Analysis conducted in session dated 2026-05-26.*
