
# Phase 1 – Remote Work & Urban Traffic Reduction (Group 20)

This project analyzes how **remote work adoption affects urban traffic congestion** across major Pakistani cities. The goal is to create a **clean, structured dataset** for further analysis and visualization in Phase 2.

---

## Project Details

* **Language:** Python  
* **Datasets:**
  * `traffic_raw.csv` – City-level traffic congestion (pre- and post-remote work)
  * `remotework_raw.csv` – Remote work share (%) and average commute time saved (minutes)
    
* **Goal:** To understand how remote work influences traffic reduction and productivity in urban cities.

---

## Dataset Overview

The datasets cover 2019–2023 for the following cities: Islamabad, Lahore, Karachi, Faisalabad, and Peshawar.

**Traffic Dataset (`traffic_raw.csv`):**

* `city` – City name  
* `year` – Year of observation  
* `pre_remote_congestion` – Traffic congestion index before remote work (%)  
* `post_remote_congestion` – Traffic congestion index after remote work (%)  
* `congestion_index` – Overall congestion measure  

**Remote Work Dataset (`remotework_raw.csv`):**

* `city` – City name  
* `year` – Year of observation  
* `remote_work_share` – Percentage of workforce working remotely  
* `avg_commute_time_saved` – Average commute time saved (minutes)  

*Note: Data is simulated realistically based on TomTom Traffic Index and national remote work surveys.*

---

## Workflow

### 1️⃣ Data Importing

* Used `pandas.read_csv()` to import both datasets.  
* Verified column types and first few rows with `head()` and `info()`.

### 2️⃣ Data Cleaning

* Checked for missing values and handled them:
  * Traffic data → replaced with **column mean**  
  * Remote work data → replaced with **0**  
* Removed duplicate rows.  
* Standardized city names.

### 3️⃣ Data Transformation

1. **Merged datasets** on `city` and `year`.  
2. **Traffic Reduction Percentage**:  

```python
traffic_reduction_percent = ((pre_remote_congestion - post_remote_congestion) / pre_remote_congestion) * 100
````

3. **Productivity Ratio**:

```python
productivity_ratio = remote_work_share * avg_commute_time_saved
```

4. **Comparison Index (Normalized 0–1 scale)**:

```python
comparison_index = (traffic_reduction_percent - traffic_reduction_percent.min()) / \
                   (traffic_reduction_percent.max() - traffic_reduction_percent.min())
```

5. Saved the cleaned dataset as `cleaned_dataset.csv`.

---

## Key Insights

* Cities with higher remote work adoption show **larger traffic reductions**.
* Productivity ratio captures **time saved due to remote work**, correlating with congestion reduction.
* Normalized comparison index enables **cross-city evaluation**.
* Dataset is now **clean, structured, and ready** for Phase 2 analysis.

---

## Folder Structure

```
Phase1_Group20/
├── data/
│   ├── traffic_raw.csv
│   ├── remotework_raw.csv
│   └── cleaned_dataset.csv
├── scripts/
│   └── codefile.py
└── README.md
```

---

## How to Run

1. Place raw datasets in the `data/` folder.
2. Run the script from the `scripts/` folder:

```bash
cd "C:\Users\Hp\Desktop\Phase1-Grp20\scripts"
python phase1_group20.py
```

3. `cleaned_dataset.csv` will be generated in the `data/` folder for Phase 2 analysis.

---




Do you want me to do that?
```
