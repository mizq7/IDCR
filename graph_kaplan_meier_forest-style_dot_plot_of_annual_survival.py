import pandas as pd
import numpy as np
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
# 2. Extract the last record observed within each whole year (0‒10 years)
# -------------------------------------------------------------------------
df['year'] = (df['time'] // 365).astype(int)          # floor to integer year
annual = (
    df[df['year'] <= 10]                              # restrict to first 10 y
      .sort_values('time')
      .groupby('year', as_index=False)
      .tail(1)                                        # pick final row per year
      .reset_index(drop=True)
)

# -------------------------------------------------------------------------
# 3. Forest-style dot plot
# -------------------------------------------------------------------------
y_pos = np.arange(len(annual))[::-1]                  # invert order for plotting

plt.figure(figsize=(6, 4.5))

# Comparator cohort (non-HSV-1)
plt.errorbar(
    annual['comparator_survival'] * 100,
    y_pos + 0.15,
    xerr=[
        (annual['comparator_survival'] - annual['comparator_survival_lb']) * 100,
        (annual['comparator_survival_ub'] - annual['comparator_survival']) * 100
    ],
    fmt='o',
    label='Non-HSV-1 cohort'
)

# HSV-1 cohort
plt.errorbar(
    annual['target_survival'] * 100,
    y_pos - 0.15,
    xerr=[
        (annual['target_survival'] - annual['target_survival_lb']) * 100,
        (annual['target_survival_ub'] - annual['target_survival']) * 100
    ],
    fmt='o',
    label='HSV-1 cohort'
)

plt.yticks(y_pos, [f'{yr} yr' for yr in annual['year']])
plt.xlabel('Survival probability (%)')
plt.legend()
plt.tight_layout()
plt.show()
