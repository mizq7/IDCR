import pandas as pd
import matplotlib.pyplot as plt

# Path to your file
file_path = '/Users/mizq7/Desktop/IDCR STUDY_JUNE 30, 2025/Remote Desktop_R Files and Folder/IDCRRR/output/shinyData/attrition_IDCRRR_DB.xlsx'
df = pd.read_excel(file_path)

# Keep only exposure_id 184 (target) and 185 (comparator)
df = df[df['exposure_id'].isin([184, 185])]

# Pivot the table: each row is a description (attrition step), columns are Target/Comparator subject counts
pivot_df = df.pivot(index='description', columns='exposure_id', values='subjects').reset_index()
pivot_df.columns = ['Step', 'Target_n', 'Comparator_n']

# Order the steps according to sequence_number (if available)
if 'sequence_number' in df.columns:
    order = df[df['exposure_id'] == 184].sort_values('sequence_number')['description'].tolist()
    pivot_df['Step'] = pd.Categorical(pivot_df['Step'], categories=order, ordered=True)
    pivot_df = pivot_df.sort_values('Step')

# Get the steps and numbers as lists
steps = pivot_df['Step'].tolist()
target_n = pivot_df['Target_n'].fillna(0).astype(int).tolist()
comparator_n = pivot_df['Comparator_n'].fillna(0).astype(int).tolist()

# Plot
plt.figure(figsize=(10,6))
plt.step(steps, target_n, where='mid', label='Target (HSV-1)', linewidth=2, marker='o')
plt.step(steps, comparator_n, where='mid', label='Comparator', linewidth=2, marker='s')
plt.xlabel('Attrition Step')
plt.ylabel('Number of Patients')
plt.title('Stepwise Attrition Curve')
plt.legend()
plt.xticks(rotation=30, ha='right', fontsize=10)
plt.tight_layout()
plt.show()
