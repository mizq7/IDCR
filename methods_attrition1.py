import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Path to your Excel file
file_path = '/Users/mizq7/Desktop/IDCR STUDY_JUNE 30, 2025/Remote Desktop_R Files and Folder/IDCRRR/output/shinyData/attrition_IDCRRR_DB.xlsx'
df = pd.read_excel(file_path)

# Filter for only target (184) and comparator (185) cohorts
df = df[df['exposure_id'].isin([184, 185])]

# Pivot so that each row is a step, and columns are 'Target' and 'Comparator'
pivot_df = df.pivot(index='description', columns='exposure_id', values='subjects').reset_index()
pivot_df.columns = ['Step', 'Target_n', 'Comparator_n']

# For attrition, steps should be in intended order. Optionally sort, or use sequence_number:
if 'sequence_number' in df.columns:
    order = df[df['exposure_id'] == 184].sort_values('sequence_number')['description'].tolist()
    pivot_df['Step'] = pd.Categorical(pivot_df['Step'], categories=order, ordered=True)
    pivot_df = pivot_df.sort_values('Step')

steps = pivot_df['Step'].tolist()
target_n = pivot_df['Target_n'].fillna(0).astype(int).tolist()
comparator_n = pivot_df['Comparator_n'].fillna(0).astype(int).tolist()

fig, ax = plt.subplots(figsize=(10, 7))
y_pos = list(reversed(range(len(steps))))
for i, label in enumerate(steps):
    text = f"{label}\nTarget: n = {target_n[i]:,}\nComparator: n = {comparator_n[i]:,}"
    rect = patches.FancyBboxPatch(
        (0.2, y_pos[i]), 3.8, 0.7,
        boxstyle="round,pad=0.05",
        linewidth=1.5,
        edgecolor='black',
        facecolor='#eeeeee'
    )
    ax.add_patch(rect)
    ax.text(
        2.1, y_pos[i]+0.35, text,
        ha='center', va='center',
        fontsize=11, fontweight='bold'
    )

for i in range(len(steps)-1):
    ax.annotate(
        '', (2.1, y_pos[i]-0.45), (2.1, y_pos[i]-0.15),
        arrowprops=dict(facecolor='black', arrowstyle='->', linewidth=1.5)
    )

ax.set_xlim(0, 4)
ax.set_ylim(-0.5, len(steps))
ax.axis('off')
plt.tight_layout()
plt.show()
