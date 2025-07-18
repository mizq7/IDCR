import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set file path
file_path = '/Users/mizq7/Desktop/IDCR STUDY_JUNE 30, 2025/Remote Desktop_R Files and Folder/IDCRRR/output/shinyData_.rds & .xlsx version/preference_score_dist_t184_c185_IDCRRR_DB.xlsx'

# Load the data
df = pd.read_excel(file_path)

# Filter out rows with both densities <0.0001 for clarity
filtered = df[(df['target_density'] >= 0.0001) | (df['comparator_density'] >= 0.0001)]

fig, axes = plt.subplots(1, 2, figsize=(14, 5), sharey=True)

# Panel A: Target Group
sns.lineplot(ax=axes[0], data=filtered, x='preference_score', y='target_density', color='blue')
axes[0].set_title('A. Target Group (HSV-1)')
axes[0].set_xlabel('Preference Score')
axes[0].set_ylabel('Density')

# Panel B: Comparator Group
sns.lineplot(ax=axes[1], data=filtered, x='preference_score', y='comparator_density', color='orange')
axes[1].set_title('B. Comparator Group')
axes[1].set_xlabel('Preference Score')
axes[1].set_ylabel('')

plt.suptitle('Preference Score Density Distributions by Group', y=1.05)
plt.tight_layout()
plt.savefig('preference_score_density_panels.png', dpi=300)
plt.show()
