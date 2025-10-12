import pandas as pd

print("="*70)
print("Phase 1 – Remote Work & Urban Traffic Reduction")
print("Group 20 – Data Cleaning & Transformation")
print("="*70)

# Step 1: Import datasets
print("\nStep 1: Importing datasets")
traffic = pd.read_csv("../data/traffic_raw.csv")
remote = pd.read_csv("../data/remotework_raw.csv")
print("✅ Datasets imported successfully.")

# Step 2: Combined Missing & Duplicates table
def combined_summary(df, name):
    print(f"\nStep 2: {name} Summary (Missing Values & Duplicates)")
    print("-"*70)
    print(f"{'Column':30} {'Missing':>10} {'Duplicates':>10}")
    print("-"*70)
    total_duplicates = df.duplicated().sum()
    for col in df.columns:
        missing = df[col].isna().sum()
        print(f"{col:30} {missing:10} {total_duplicates:10}")
    print("-"*70)

combined_summary(traffic, "Traffic Dataset Before Cleaning")
combined_summary(remote, "Remote Work Dataset Before Cleaning")

# Step 3: Handle missing values
print("\nStep 3: Handling missing/null values")
traffic['pre_remote_congestion'] = traffic['pre_remote_congestion'].fillna(traffic['pre_remote_congestion'].mean())
traffic['post_remote_congestion'] = traffic['post_remote_congestion'].fillna(traffic['post_remote_congestion'].mean())
traffic['congestion_index'] = traffic['congestion_index'].fillna(traffic['congestion_index'].mean())
remote['remote_work_share'] = remote['remote_work_share'].fillna(0)
remote['avg_commute_time_saved'] = remote['avg_commute_time_saved'].fillna(0)
print("✅ Missing/null values handled.")

# Step 4: Remove duplicates
print("\nStep 4: Removing duplicate rows")
traffic.drop_duplicates(inplace=True)
remote.drop_duplicates(inplace=True)
print("✅ Duplicates removed (if any).")

# Step 5: Missing/Duplicates summary after cleaning
combined_summary(traffic, "Traffic Dataset After Cleaning")
combined_summary(remote, "Remote Work Dataset After Cleaning")

# Step 6: Merge datasets
print("\nStep 6: Merging datasets")
merged = pd.merge(traffic, remote, on=['city','year'], how='inner')
print("✅ Datasets merged successfully.")

# Step 7: Apply transformations
print("\nStep 7: Applying transformations")
merged['traffic_reduction_percent'] = ((merged['pre_remote_congestion'] - merged['post_remote_congestion']) / merged['pre_remote_congestion'] * 100).round(2)
merged['productivity_ratio'] = (merged['remote_work_share'] * merged['avg_commute_time_saved']).round(2)
merged['comparison_index'] = ((merged['traffic_reduction_percent'] - merged['traffic_reduction_percent'].min()) / 
                              (merged['traffic_reduction_percent'].max() - merged['traffic_reduction_percent'].min())).round(2)
print("✅ Transformations applied.")

# Step 8: Save cleaned dataset
print("\nStep 8: Saving cleaned dataset")
merged.to_csv("../data/cleaned_dataset.csv", index=False)
print("✅ 'cleaned_dataset.csv' created in data/ folder.")

# Step 9: Preview cleaned dataset compactly
print("\nStep 9: Preview of cleaned & transformed dataset (compact view)")
compact_cols = ['city', 'year', 'traffic_reduction_percent', 'productivity_ratio', 'comparison_index']
print(merged[compact_cols].to_string(index=False))

# Step 10: Summary metrics
print("\nStep 10: Summary of Key Metrics")
print("-"*70)
print(f"{'Metric':30} {'Min':>10} {'Max':>10}")
print("-"*70)
print(f"{'Traffic Reduction %':30} {merged['traffic_reduction_percent'].min():10} {merged['traffic_reduction_percent'].max():10}")
print(f"{'Productivity Ratio':30} {merged['productivity_ratio'].min():10} {merged['productivity_ratio'].max():10}")
print(f"{'Comparison Index':30} {merged['comparison_index'].min():10} {merged['comparison_index'].max():10}")
