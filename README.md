

# 🚦 Phase 1 – Remote Work & Urban Traffic Reduction (Group 20)

### 👩‍💻Data Cleaning, Transformation & Visualization

This project explores the **relationship between remote work and urban traffic reduction**, using live and open data sources.
It demonstrates data cleaning, transformation, and visualization processes in Python.

---

## 📁 Project Overview

The goal of this project is to analyze how **remote work adoption** impacts **urban traffic congestion**.
The project combines **real-time traffic data** and **remote work statistics** to provide meaningful insights through data-driven analysis.

---

## 🧩 Technologies Used

| Library               | Purpose                                         |
| --------------------- | ----------------------------------------------- |
| **os**                | File and directory handling                     |
| **requests**          | Fetching live data from APIs                    |
| **pandas**            | Data cleaning, transformation, and CSV handling |
| **numpy**             | Numerical and statistical operations            |
| **datetime**          | Managing timestamps and file logs               |
| **matplotlib.pyplot** | Visualizing data and generating charts          |

---

## 🧠 Steps Performed

### **STEP 1 – Live Traffic Data from TomTom API**

* API used:
  `https://api.tomtom.com/traffic/services/4/flowSegmentData/relative0/10/json`
* Real-time traffic data was fetched for the following cities:
  **Mumbai, Delhi, Singapore, Dubai, Kuala Lumpur, and Riyadh**
* Extracted attributes:

  * `currentSpeed`
  * `freeFlowSpeed`
  * `confidence`
  * `timestamp`
* Data saved as CSV for further analysis.

---

### **STEP 2 – Remote Work Dataset**

* In the given assignment, the **National Remote Work Surveys** was mentioned as the second data source.
* However, since **its API was not available**, the group used an **alternative website providing public datasets and APIs**.
* The **OECD “Going Digital Toolkit” dataset** was selected as it includes global data on **remote work trends**.
* The dataset was merged, cleaned, and standardized for analysis.

---

### **STEP 3 – Data Cleaning & Transformation**

* Removed missing and duplicate records.
* Renamed columns for consistency.
* Converted numeric fields for proper calculations.
* Created summarized datasets for:

  * Average **traffic speed** per city
  * Average **remote work share** per year

---

### **STEP 4 – Key Metrics**

| Metric                           | Description                                          |
| -------------------------------- | ---------------------------------------------------- |
| **Traffic Reduction Percentage** | Measures decrease in congestion levels               |
| **Productivity Ratio**           | Estimates productivity linked with remote work share |
| **Comparison Index**             | A normalized index combining both factors            |

---

### **STEP 5 – Visualization**

Two visualizations were generated:

1. **Bar Chart:** Average Traffic Speed per City (Current vs Free Flow Speed)
2. **Line Chart:** Average Remote Work Share Over the Years

---

## 💡 Key Insights

* Cities with higher **remote work adoption** showed **lower traffic congestion levels**.
* The **Comparison Index** reflects how remote work positively influences both **productivity** and **urban mobility**.
* When a dataset’s API is unavailable, using **public open data sources** like **OECD** ensures accessibility and reliability.

---

