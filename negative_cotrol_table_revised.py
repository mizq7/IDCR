import pandas as pd

# --- EDIT THESE PATHS FOR YOUR LOCAL MACHINE ---
NEG_PATH = r"/Users/mizq7/Desktop/IDCR STUDY_JUNE 30, 2025/Remote Desktop_R Files and Folder/IDCRRR/output/shinyData_.rds & .xlsx version/negative_control_outcome_IDCRRR_DB.xlsx"
RES_PATH = r"/Users/mizq7/Desktop/IDCR STUDY_JUNE 30, 2025/Remote Desktop_R Files and Folder/IDCRRR/output/shinyData_.rds & .xlsx version/cohort_method_result_IDCRRR_DB.xlsx"

# Load
neg = pd.read_excel(NEG_PATH)      # expects columns: outcome_id, outcome_name
res = pd.read_excel(RES_PATH)      # CohortMethod results (primary + NC rows)

# Remove primary study outcome (ID 179) from NC join
res_nc = res[res['outcome_id'] != 179].copy()

# Merge names into results
nc = neg.merge(res_nc, on='outcome_id', how='left', suffixes=("", "_res"))

# Ensure numeric counts
for col in ['target_outcomes', 'comparator_outcomes']:
    if col not in nc.columns:
        nc[col] = 0
    nc[col] = nc[col].fillna(0).astype(int)

# Flags
nc['any_event'] = (nc['target_outcomes'] > 0) | (nc['comparator_outcomes'] > 0)
nc['estimable_both'] = (nc['target_outcomes'] > 0) & (nc['comparator_outcomes'] > 0)

# Save files
nc_cols = ['outcome_id','outcome_name','target_outcomes','comparator_outcomes','any_event','estimable_both']
nc_full = nc[nc_cols].sort_values('outcome_id')
nc_full.to_excel("NC_counts_summary.xlsx", sheet_name="AllNC", index=False)

# Subsets
nc_full[nc_full['any_event']].to_csv("NC_anyevent_counts.csv", index=False)
nc_full[nc_full['estimable_both']].to_csv("NC_estimable_counts.csv", index=False)
nc_full.to_csv("NC_full_counts.csv", index=False)

print(f"Total NC candidates: {len(nc_full)}")
print(f"NC with any events: {nc_full['any_event'].sum()}")
print(f"NC estimable in both groups: {nc_full['estimable_both'].sum()}")
