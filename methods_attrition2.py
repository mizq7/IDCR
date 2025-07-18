import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# File path to your Excel file
file_path = '/Users/mizq7/Desktop/IDCR STUDY_JUNE 30, 2025/Remote Desktop_R Files and Folder/IDCRRR/output/shinyData/attrition_IDCRRR_DB.xlsx'
df = pd.read_excel(file_path)

# Filter to keep only cohort attrition steps (not negative controls or other outputs)
# exposure_id 184 = Target, 185 = Comparator
df = df[df['exposure_id'].isin([184, 185])]

# Pivot so each step (description) is one row, columns are Target and Comparator subject counts
pivot_df = df.pivot(index='description', columns='exposure_id', values='subjects').reset_index()
pivot_df.columns = ['Step', 'Target_n', 'Comparator_n']

# Optional: Order the steps according to sequence_number
if 'sequence_number' in df.columns:
    step_order = df[df['exposure_id'] == 184].sort_values('sequence_number')['description'].tolist()
    pivot_df['Step'] = pd.Categorical(pivot_df['Step'], categories=step_order, ordered=True)
    pivot_df = pivot_df.sort_values('Step')

# Extract the labels and counts
step_labels = pivot_df['Step'].tolist()
target_n = pivot_df['Target_n'].fillna(0).astype(int).tolist()
comparator_n = pivot_df['Comparator_n'].fillna(0).astype(int).tolist()

# Bar plot
x = np.arange(len(step_labels))
width = 0.35

fig, ax = plt.subplots(figsize=(10, 6))
rects1 = ax.bar(x - width/2, target_n, width, label='Target (HSV-1)', color="#336699")
rects2 = ax.bar(x + width/2, comparator_n, width, label='Comparator', color="#cc9966")

ax.set_ylabel('Number of Patients')
ax.set_title('Cohort Attrition at Each Step')
ax.set_xticks(x)
ax.set_xticklabels(step_labels, rotation=30, ha='right', fontsize=10)
ax.legend()
plt.tight_layout()
plt.show()
