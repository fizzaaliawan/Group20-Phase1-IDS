

# 🚦 Remote Work & Urban Traffic Reduction – Phase 1

## 📘 Project Overview

This project explores the **relationship between remote work adoption and urban traffic congestion reduction**.
Using traffic and remote work datasets, we analyze how increasing remote work impacts congestion levels in major cities.

---

## 📂 Dataset Description

### 1️⃣ Traffic Dataset (TomTom Traffic Index)

Contains **city-level traffic congestion metrics** before and after remote work adoption.

| Column                   | Description                   |
| ------------------------ | ----------------------------- |
| `city`                   | City name                     |
| `year`                   | Year of observation           |
| `pre_remote_congestion`  | Congestion before remote work |
| `post_remote_congestion` | Congestion after remote work  |
| `congestion_index`       | Combined congestion index     |

---

### 2️⃣ Remote Work Dataset (National Remote Work Surveys)

Captures the **share of remote workers and commuting time saved** in each city.

| Column                   | Description                                |
| ------------------------ | ------------------------------------------ |
| `city`                   | City name                                  |
| `year`                   | Year of survey                             |
| `remote_work_share`      | Proportion of remote workers               |
| `avg_commute_time_saved` | Average daily commute time saved (minutes) |

Both datasets were merged on `city` and `year` for comparative analysis.

---

## ⚙️ Data Cleaning Steps

Performed using **Python (pandas)**.

1. Imported datasets using `pd.read_csv()`.
2. Replaced **missing values** with:

   * Mean (for traffic data)
   * Zero (for remote work data)
3. Removed duplicates using `drop_duplicates()`.
4. Standardized **city identifiers** and **year formats** for accurate merging.

---

## 🔄 Data Transformation Steps

Derived new variables for deeper insights:

| Derived Variable            | Formula                                                                          |
| --------------------------- | -------------------------------------------------------------------------------- |
| `traffic_reduction_percent` | ((pre_remote_congestion - post_remote_congestion) / pre_remote_congestion) × 100 |
| `productivity_ratio`        | remote_work_share × avg_commute_time_saved                                       |
| `comparison_index`          | Normalized value of traffic reduction percentage (0–1 scale)                     |

Final datasets were merged using **inner join** on `city` and `year` and saved as **`cleaned_dataset.csv`**.

---

## 📊 Output Summary

The final cleaned dataset includes:

| city     | year | traffic_reduction_percent | productivity_ratio | comparison_index |
| -------- | ---- | ------------------------- | ------------------ | ---------------- |
| London   | 2021 | 12.45                     | 23.6               | 0.74             |
| New York | 2021 | 9.80                      | 20.2               | 0.59             |

---


## 🧠 Key Takeaways

* Cleaning and transformation improved **data consistency and reliability**.
* Derived variables support meaningful analysis of the **remote work–traffic relationship**.
* The **cleaned dataset** will be used in **Phase 2 (EDA & Visualization)**.


---

Would you like me to make this in a downloadable **README.md** file (Markdown format)?
