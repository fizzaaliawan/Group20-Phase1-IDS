
# Phase 1 – Remote Work & Urban Traffic Reduction (Group 20)

This project focuses on analyzing how **remote work adoption affects urban traffic congestion** across major Pakistani cities. The goal is to create a clean and structured dataset for **further analysis and visualization** in Phase 2.

---

## Project Details

* **Language:** R
* **Datasets:**

  * `traffic_raw.csv` – City-level traffic congestion (pre- and post-remote work)
  * `remotework_raw.csv` – Remote work share (%) and average commute time saved (minutes)
    
* **Goal:** To understand how remote work influences traffic reduction and productivity in urban cities.

---

## Dataset Overview

The datasets include traffic congestion and remote work data for 2019–2023. The cities covered are Islamabad, Lahore, Karachi, Faisalabad, and Peshawar.

**Traffic Dataset (`traffic_raw.csv`)**:

* `city` – City name
* `year` – Year of observation
* `pre_remote_congestion` – Traffic congestion index before remote work (%)
* `post_remote_congestion` – Traffic congestion index after remote work (%)
* `congestion_index` – Overall congestion measure

**Remote Work Dataset (`remotework_raw.csv`)**:

* `city` – City name
* `year` – Year of observation
* `remote_work_share` – Percentage of workforce working remotely
* `avg_commute_time_saved` – Average commute time saved (minutes)

*Note: Data is simulated realistically based on TomTom Traffic Index and national remote work surveys.*

---

## Analysis Breakdown

### Step 1: Data Importing

* Used `readr::read_csv()` to import both datasets into R.
* Checked column types and first few rows with `head()` and `str()`.

### Step 2: Data Cleaning

* Checked for missing values using `colSums(is.na())` and replaced them:

  * Missing traffic data → replaced with column mean
  * Missing remote work data → replaced with 0
* Removed duplicate rows (none found).
* Standardized city names and numeric formats.

### Step 3: Data Transformation

1. **Merged datasets** on `city` and `year` using `dplyr::inner_join()`.
2. **Traffic Reduction Percentage**:

```r
traffic_reduction_percent = ((pre_remote_congestion - post_remote_congestion) / pre_remote_congestion) * 100
```

3. **Productivity Ratio**:

```r
productivity_ratio = remote_work_share * avg_commute_time_saved
```

4. **Comparison Index (Normalized 0–1 scale)**:

```r
comparison_index = (traffic_reduction_percent - min(traffic_reduction_percent)) /
                   (max(traffic_reduction_percent) - min(traffic_reduction_percent))
```

5. Saved the cleaned and transformed dataset as `cleaned_dataset.csv`.

### Step 4: Data Verification

* Ensured that all merged rows matched the expected city-year combinations.
* Checked for negative or unrealistic values in computed metrics.

---

## Key Insights

* Cities with higher remote work adoption show a **larger reduction in traffic congestion**.
* Productivity ratio reflects **time saved due to remote work**, showing direct correlation with congestion reduction.
* Normalized comparison index enables **cross-city evaluation**.
* Dataset is now **clean, structured, and ready** for Phase 2 exploratory analysis and visualization.

---

## Folder Structure

```
Phase1_Group20/
├── data/
│   ├── traffic_raw.csv
│   ├── remotework_raw.csv
│   └── cleaned_dataset.csv
├── scripts/
│   └── phase1_group20.R
└── README.md
```

---

## How to Use

1. Place raw datasets in `data/`.
2. Run `phase1_group20.R` from `scripts/`.
3. `cleaned_dataset.csv` will be generated in `data/` for further analysis.

---

