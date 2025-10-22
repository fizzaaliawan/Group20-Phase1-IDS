import os
import requests
import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt

print("=" * 80)
print("PHASE 1 – Remote Work & Urban Traffic Reduction (Group 20) ")
print("=" * 80)

# -------------------------------------------------------------------
# STEP 1 – Fetch LIVE Traffic Data from TomTom API
# -------------------------------------------------------------------
print("\n🚦 STEP 1: Fetching Traffic Data via TomTom API")

TOMTOM_API_KEY = "1uXSX6JJHURuQW4cIKDWDgeReMQeE9Zx"
TOMTOM_FLOW_URL = "https://api.tomtom.com/traffic/services/4/flowSegmentData/relative0/10/json"

OUT_DIR = r"C:\Users\Hp\OneDrive\Desktop\SEM 6\SEM 6\Courses\Data Science\Phase1-Grp20\scripts\output_data"
os.makedirs(OUT_DIR, exist_ok=True)
TS = datetime.now().strftime("%Y%m%d_%H%M%S")

cities = {
    "Mumbai": (19.0760, 72.8777),
    "Delhi": (28.6139, 77.2090),
    "Singapore": (1.3521, 103.8198),
    "Dubai": (25.2048, 55.2708),
    "Kuala Lumpur": (3.1390, 101.6869),
    "Riyadh": (24.7136, 46.6753)
}

traffic_rows = []
for city, (lat, lon) in cities.items():
    url = f"{TOMTOM_FLOW_URL}?point={lat},{lon}&key={TOMTOM_API_KEY}"
    resp = requests.get(url)

    if resp.status_code == 200:
        seg = resp.json().get("flowSegmentData", {})
        traffic_rows.append({
            "city": city,
            "currentSpeed": seg.get("currentSpeed"),
            "freeFlowSpeed": seg.get("freeFlowSpeed"),
            "confidence": seg.get("confidence"),
            "timestamp": datetime.now().isoformat()
        })
        print(f"✅ Fetched traffic for {city}")
    else:
        print(f"❌ Error fetching {city}: {resp.status_code}")

traffic_data = pd.DataFrame(traffic_rows)
traffic_data.to_csv(f"{OUT_DIR}/traffic_raw_{TS}.csv", index=False)

print("\n📊 Traffic Data (Raw Preview):")
print(traffic_data.head())
print("-" * 80)

# 🧹 Clean Traffic Data
traffic_data.dropna(inplace=True)
traffic_data.reset_index(drop=True, inplace=True)

print("\n🚗 Traffic Data (Cleaned Preview):")
print(traffic_data.head())
print("-" * 80)

# -------------------------------------------------------------------
# STEP 2 – Load Remote Work Dataset (Local OECD File)
# -------------------------------------------------------------------
folder_path = r"C:\Users\Hp\OneDrive\Desktop\SEM 6\SEM 6\Courses\Data Science\Phase1-Grp20\data\OECD Going Digital Toolkit Indicator 55 (2025-10-21 9e389ee)"
all_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.xlsx')]

df_list = [pd.read_excel(file) for file in all_files]
oecd_data = pd.concat(df_list, ignore_index=True)

print("✅ All OECD Excel files merged successfully!")
print("📊 OECD Data Shape:", oecd_data.shape)
print(oecd_data.head())

rename_map = {
    "LOCATION": "country",
    "TIME": "year",
    "Value": "remote_work_share"
}
oecd_data.rename(columns=rename_map, inplace=True, errors="ignore")

if all(col in oecd_data.columns for col in ["country", "year", "remote_work_share"]):
    remote_data = oecd_data[["country", "year", "remote_work_share"]]
else:
    print("⚠️ Expected columns not found — check OECD dataset structure.")
    print(oecd_data.columns.tolist())
    remote_data = oecd_data.copy()

remote_data.dropna(inplace=True)
remote_data.reset_index(drop=True, inplace=True)

print("\n🖥️ OECD Remote Work Data (Cleaned Preview):")
print(remote_data.head())
print("-" * 80)

# -------------------------------------------------------------------
# STEP 3 – Final Cleaning & Save
# -------------------------------------------------------------------
print("\n💾 STEP 3: Final Cleaning & Saving Datasets")

traffic_data.rename(columns=lambda x: x.strip().lower().replace(" ", "_"), inplace=True)
remote_data.rename(columns=lambda x: x.strip().lower().replace(" ", "_"), inplace=True)

traffic_data.drop_duplicates(inplace=True)
remote_data.drop_duplicates(inplace=True)

# ✅ Future-proof numeric conversion
for col in traffic_data.columns:
    try:
        traffic_data[col] = pd.to_numeric(traffic_data[col])
    except Exception:
        pass

for col in remote_data.columns:
    try:
        remote_data[col] = pd.to_numeric(remote_data[col])
    except Exception:
        pass

traffic_data.to_csv(f"{OUT_DIR}/traffic_cleaned_{TS}.csv", index=False)
remote_data.to_csv(f"{OUT_DIR}/remote_cleaned_{TS}.csv", index=False)

print("✅ Datasets cleaned and saved!")
print("-" * 80)

# -------------------------------------------------------------------
# PHASE 2 – DATA TRANSFORMATION
# -------------------------------------------------------------------
print("\n" + "=" * 70)
print("⚙️ PHASE 2 – Data Transformation")
print("=" * 70)

if 'city' in traffic_data.columns and 'currentspeed' in traffic_data.columns:
    traffic_selected = traffic_data[['city', 'currentspeed', 'freeflowspeed']].copy()
else:
    traffic_selected = traffic_data.copy()

if 'country' in remote_data.columns and 'remote_work_share' in remote_data.columns:
    remote_selected = remote_data[['country', 'year', 'remote_work_share']].copy()
else:
    remote_selected = remote_data.copy()

traffic_summary = traffic_selected.groupby('city', as_index=False).mean(numeric_only=True)
remote_summary = remote_selected.groupby('year', as_index=False)['remote_work_share'].mean()

merged_data = pd.DataFrame({
    'year': remote_summary['year'],
    'avg_remote_work_share': remote_summary['remote_work_share'],
    'avg_speed': traffic_summary['currentspeed'].mean()
})

# -------------------------------------------------------------------
# STEP 4 – Key Metrics Calculation
# -------------------------------------------------------------------
print("\n📊 STEP 4: Calculating Key Metrics")

try:
    if not traffic_data.empty and not remote_data.empty:
        pre_remote_congestion = traffic_data["freeflowspeed"].mean()
        post_remote_congestion = traffic_data["currentspeed"].mean()
        traffic_reduction = ((pre_remote_congestion - post_remote_congestion) / pre_remote_congestion) * 100

        remote_work_share = remote_data["remote_work_share"].mean()
        avg_commute_time_saved = 1.2
        productivity_ratio = remote_work_share * avg_commute_time_saved

        comparison_index = np.clip(traffic_reduction / 100, 0, 1)

        print(f"🚦 Traffic Reduction Percentage: {traffic_reduction:.2f}%")
        print(f"💼 Productivity Ratio: {productivity_ratio:.2f}")
        print(f"📈 Comparison Index (0–1 scale): {comparison_index:.2f}")

        metrics = pd.DataFrame({
            "Traffic_Reduction_Percentage": [traffic_reduction],
            "Productivity_Ratio": [productivity_ratio],
            "Comparison_Index": [comparison_index]
        })
        metrics_file = f"{OUT_DIR}/final_metrics_{TS}.csv"
        metrics.to_csv(metrics_file, index=False)
        print(f"💾 Metrics saved successfully to: {metrics_file}")

    else:
        print("⚠️ Not enough data to calculate metrics.")

except Exception as e:
    print("❌ Error calculating metrics:", e)

# -------------------------------------------------------------------
# STEP 5 – Visualization (Authentic Charts)
# -------------------------------------------------------------------
import seaborn as sns

print("\n📈 STEP 5: Generating Authentic Charts")

sns.set_style("whitegrid")

# ============================================
# CHART 1 – Average Traffic Speed per City
# ============================================
plt.figure(figsize=(12, 7))

x = np.arange(len(traffic_summary['city']))
width = 0.35

plt.bar(x - width/2, traffic_summary['freeflowspeed'], width,
        label='Free Flow Speed', color='#1f77b4')
plt.bar(x + width/2, traffic_summary['currentspeed'], width,
        label='Current Speed', color='#ff7f0e')

plt.title("Average Traffic Speed per City (Free Flow vs Current)", fontsize=16, weight='bold')
plt.xlabel("City", fontsize=14)
plt.ylabel("Speed (km/h)", fontsize=14)
plt.xticks(x, traffic_summary['city'], rotation=30)
plt.legend(fontsize=12)
plt.tight_layout()
plt.savefig(f"{OUT_DIR}/traffic_speed_chart_{TS}.png", dpi=300)
plt.show()

print("✅ Chart 1 saved successfully!")

# ============================================
# CHART 2 – Trend of Remote Work Share Over Years
# ============================================
plt.figure(figsize=(10, 6))

plt.plot(remote_summary['year'], remote_summary['remote_work_share'],
         marker='o', color='#2ca02c', linewidth=2)

# Annotate each point with its value
for x_val, y_val in zip(remote_summary['year'], remote_summary['remote_work_share']):
    plt.text(x_val, y_val + 0.3, f"{y_val:.1f}%", ha='center', fontsize=10)

plt.title("Trend in Remote Work Share Over Years", fontsize=16, weight='bold')
plt.xlabel("Year", fontsize=14)
plt.ylabel("Remote Work Share (%)", fontsize=14)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig(f"{OUT_DIR}/remote_work_chart_{TS}.png", dpi=300)
plt.show()

print("✅ Chart 2 saved successfully!")

# ============================================
# CHART 3 – Correlation Between Remote Work & Traffic Speed
# ============================================
plt.figure(figsize=(8, 6))

# Use scatter plot to show relationship
plt.scatter(remote_summary['remote_work_share'],
            [traffic_summary['currentspeed'].mean()] * len(remote_summary),
            color='#9467bd', s=100, alpha=0.7)

plt.title("Correlation Between Remote Work Share & Avg Traffic Speed", fontsize=16, weight='bold')
plt.xlabel("Remote Work Share (%)", fontsize=14)
plt.ylabel("Average Traffic Speed (km/h)", fontsize=14)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig(f"{OUT_DIR}/correlation_chart_{TS}.png", dpi=300)
plt.show()

print("✅ Chart 3 saved successfully!")
print(f"✅ All charts saved to: {OUT_DIR}")
print("=" * 80)
