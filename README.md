

# 🚦 Phase 1 – Remote Work & Urban Traffic Reduction (Group 20)

This project analyzes the impact of remote work on urban traffic congestion using live data from the TomTom Traffic API and OECD Remote Work datasets.
It demonstrates real-world data cleaning, transformation, and visualization techniques in Python.


---

📁 Project Overview

The purpose of this project is to explore how increased remote work trends contribute to reduced city traffic congestion.
The project integrates live traffic data and OECD remote work statistics to:

Fetch real-time traffic flow data from TomTom API

Clean, merge, and transform multiple datasets

Calculate key comparative metrics

Visualize traffic and remote work trends



---

🧩 Technologies Used

Library	Purpose

os	File and directory handling
requests	Fetching live data from APIs
pandas	Data cleaning, transformation, and CSV handling
numpy	Numerical operations and metric calculations
datetime	Handling timestamps for logs and saved files
matplotlib.pyplot	Data visualization and chart generation



---

🧠 Steps Performed

STEP 1 – Fetch LIVE Traffic Data from TomTom API

API used:
https://api.tomtom.com/traffic/services/4/flowSegmentData/relative0/10/json

Fetches traffic data for six cities: Mumbai, Delhi, Singapore, Dubai, Kuala Lumpur, Riyadh

Extracts attributes like:

currentSpeed

freeFlowSpeed

confidence

timestamp


Saves results in a CSV file
→ traffic_raw_<timestamp>.csv



---

STEP 2 – Load Remote Work Dataset (OECD)

Loads all .xlsx files from the OECD dataset folder.

Merges them into a single DataFrame.

Renames columns:

LOCATION → country

TIME → year

Value → remote_work_share


Cleans and saves the dataset as
→ remote_cleaned_<timestamp>.csv



---

STEP 3 – Final Cleaning

Converts numeric columns for consistency.

Removes duplicates and null values.

Ensures clean column names (lowercase and underscores).

Stores cleaned versions of both datasets.



---

PHASE 2 – Data Transformation

Aggregates average current speed and free flow speed by city.

Computes average remote work share per year.

Merges transformed summaries into a single dataset for comparison.



---

STEP 4 – Key Metrics Calculation

Calculates three key indicators:

Metric	Description

Traffic Reduction Percentage	% decrease in average speed due to congestion
Productivity Ratio	Estimated increase in productivity from remote work
Comparison Index	Scaled indicator comparing both effects (0–1 scale)


Output file:
→ final_metrics_<timestamp>.csv


---

STEP 5 – Visualization

Two visualizations are generated and saved:

1. Bar Chart: Average Traffic Speed per City

Compares currentSpeed vs freeFlowSpeed



2. Line Graph: Remote Work Share Over Years

Shows remote work growth trend




Output images:

traffic_speed_chart_<timestamp>.png

remote_work_chart_<timestamp>.png



---

💡 Key Insights

Cities with higher remote work adoption show less traffic congestion.

Average productivity correlates positively with remote work share.

The Comparison Index helps visualize balance between reduced congestion and increased work efficiency.



---



