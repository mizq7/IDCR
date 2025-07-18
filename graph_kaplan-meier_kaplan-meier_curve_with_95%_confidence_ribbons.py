import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------------------------------------------------
# 1. Load Kaplan–Meier distribution data (user-supplied filesystem path)
# -------------------------------------------------------------------------
FILE = (
    '/Users/mizq7/Desktop/IDCR STUDY_JUNE 30, 2025/Remote Desktop_R Files and '
    'Folder/IDCRRR/output/shinyData_.rds & .xlsx version/'
    'kaplan_meier_dist_t184_c185_IDCRRR_DB.xlsx'
)
df = pd.read_excel(FILE)

# -------------------------------------------------------------------------
# 2. Plot Kaplan–Meier survival curves with 95 % confidence ribbons
# -------------------------------------------------------------------------
plt.figure(figsize=(6, 4))

# HSV-1 cohort
plt.step(df['time'], df['target_survival'],
         where='post', label='HSV-1 cohort')
plt.fill_between(
    df['time'],
    df['target_survival_lb'],
    df['target_survival_ub'],
    step='post', alpha=0.2
)

# Comparator cohort
plt.step(df['time'], df['comparator_survival'],
         where='post', label='Non-HSV-1 cohort')
plt.fill_between(
    df['time'],
    df['comparator_survival_lb'],
    df['comparator_survival_ub'],
    step='post', alpha=0.2
)

plt.xlabel('Days since cohort entry')
plt.ylabel('Survival probability')
plt.ylim(0.7, 1.01)
plt.legend()
plt.tight_layout()
plt.show()
