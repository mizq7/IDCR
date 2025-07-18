import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------------------------------------------------
# 1. Load Kaplan–Meier distribution data (full path supplied by user)
# -------------------------------------------------------------------------
FILE = (
    '/Users/mizq7/Desktop/IDCR STUDY_JUNE 30, 2025/Remote Desktop_R Files and '
    'Folder/IDCRRR/output/shinyData_.rds & .xlsx version/'
    'kaplan_meier_dist_t184_c185_IDCRRR_DB.xlsx'
)
df = pd.read_excel(FILE)

# -------------------------------------------------------------------------
# 2. Derive cumulative absolute risk difference: comparator − target
# -------------------------------------------------------------------------
df['risk_diff'] = df['comparator_survival'] - df['target_survival']

# -------------------------------------------------------------------------
# 3. Plot risk-difference curve
# -------------------------------------------------------------------------
plt.figure(figsize=(6, 3.5))
plt.step(df['time'], df['risk_diff'] * 100, where='post')       # % units
plt.axhline(0, linestyle='--', linewidth=0.8)
plt.xlabel('Days since cohort entry')
plt.ylabel('Absolute risk difference (%)')
plt.tight_layout()
plt.show()
