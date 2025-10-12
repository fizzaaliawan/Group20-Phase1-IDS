

# 🚦 Phase 1 – Remote Work & Urban Traffic Reduction (Group 20)

This project investigates how **remote work adoption impacts urban traffic congestion** in major Pakistani cities. The goal of Phase 1 is to create a **clean, structured dataset** for analysis and visualization in Phase 2.

---

## 📝 Project Details

| Attribute    | Description                                                                              |
| ------------ | ---------------------------------------------------------------------------------------- |
| **Language** | Python                                                                                   |
| **Datasets** | `traffic_raw.csv`, `remotework_raw.csv`                                                  |
| **Goal**     | Understand remote work’s influence on traffic reduction and productivity in urban cities |

*Data is simulated based on TomTom Traffic Index and national remote work surveys.*

---

## 🗃 Dataset Overview

**Traffic Dataset (`traffic_raw.csv`):**

| Column                 | Description                               |
| ---------------------- | ----------------------------------------- |
| city                   | City name                                 |
| year                   | Year of observation                       |
| pre_remote_congestion  | Traffic congestion before remote work (%) |
| post_remote_congestion | Traffic congestion after remote work (%)  |
| congestion_index       | Overall congestion measure                |

**Remote Work Dataset (`remotework_raw.csv`):**

| Column                 | Description                              |
| ---------------------- | ---------------------------------------- |
| city                   | City name                                |
| year                   | Year of observation                      |
| remote_work_share      | Percentage of workforce working remotely |
| avg_commute_time_saved | Average commute time saved (minutes)     |

---

## ⚙️ Workflow Steps

```
Raw Datasets
   │
   ▼
Data Importing (pandas.read_csv)
   │
   ▼
Data Cleaning
   • Handle missing values
   • Remove duplicates
   │
   ▼
Merge Datasets on city & year
   │
   ▼
Transformations
   • traffic_reduction_percent
   • productivity_ratio
   • comparison_index
   │
   ▼
Save Cleaned Dataset → cleaned_dataset.csv
```

---

## 🔢 Transformations

```python
# Traffic Reduction %
traffic_reduction_percent = ((pre_remote_congestion - post_remote_congestion) / pre_remote_congestion) * 100

# Productivity Ratio
productivity_ratio = remote_work_share * avg_commute_time_saved

# Comparison Index (0-1)
comparison_index = (traffic_reduction_percent - traffic_reduction_percent.min()) / \
                   (traffic_reduction_percent.max() - traffic_reduction_percent.min())
```

---

## 📊 Key Metrics

| Metric              | Min  | Max   |
| ------------------- | ---- | ----- |
| Traffic Reduction % | 5.0  | 31.25 |
| Productivity Ratio  | 0.02 | 6.3   |
| Comparison Index    | 0.0  | 1.0   |

**Insights:**

* Cities with higher remote work adoption show **larger traffic reductions**.
* Productivity ratio quantifies **time saved due to remote work**.
* Comparison index allows **cross-city evaluation**.

---

## 📂 Folder Structure

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

## ▶️ How to Run

1. Place raw datasets in the `data/` folder.
2. Navigate to the `scripts/` folder:

```bash
cd "C:\Users\Hp\Desktop\Phase1-Grp20\scripts"
python codefile.py
```

3. The **cleaned dataset** will be generated in `data/` for Phase 2 analysis.

