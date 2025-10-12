

```markdown
# Phase 1 – Remote Work & Urban Traffic Reduction (Group 20)

## Project Overview
This project focuses on analyzing the impact of **remote work on urban traffic congestion** across major Pakistani cities. The aim is to prepare a clean and structured dataset for further exploratory data analysis (Phase 2) and visualization.  

The project is part of **Phase 1 of the Data Science Lifecycle** and covers **data importing, cleaning, and transformation**.

---

## Dataset Description
- **Traffic Dataset (`traffic_raw.csv`)**: Contains city-level traffic congestion data (pre- and post-remote work) for 2019–2023.  
- **Remote Work Dataset (`remotework_raw.csv`)**: Contains city-level remote work share (%) and average commute time saved (minutes) for the same period.  
- **Cities Covered**: Islamabad, Lahore, Karachi, Faisalabad, Peshawar  
- **Data Source**: Simulated realistic datasets based on TomTom Traffic Index and national remote work surveys.  

---

## Data Cleaning Steps
1. Checked for missing values and replaced them with **mean** (for congestion data) or **0** (for remote work data).  
2. Removed duplicates (none found).  
3. Standardized city names and numeric formats.  

---

## Data Transformation Steps
1. **Merged datasets** on `city` and `year`.  
2. **Traffic Reduction Percentage**:  
   \[
   \text{traffic_reduction_percent} = \frac{\text{pre_remote_congestion} - \text{post_remote_congestion}}{\text{pre_remote_congestion}} \times 100
   \]  
3. **Productivity Ratio**:  
   \[
   \text{productivity_ratio} = \text{remote_work_share} \times \text{avg_commute_time_saved}
   \]  
4. **Comparison Index**: Normalized traffic reduction (0–1 scale) for easy cross-city comparison.  
5. Saved the **cleaned and transformed dataset** as `cleaned_dataset.csv`.

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
1. Place the raw datasets (`traffic_raw.csv` and `remotework_raw.csv`) in the `data/` folder.  
2. Run the R script (`phase1_group20.R`) located in the `scripts/` folder.  
3. The script will produce the `cleaned_dataset.csv` file in the `data/` folder, ready for Phase 2 analysis.

---

## Notes
- This dataset is **simulated but realistic**, reflecting expected patterns of traffic reduction and remote work adoption.  
- Phase 2 will focus on **Exploratory Data Analysis (EDA)** and visualization using this cleaned dataset.
```

---


