import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set file path
file_path = '/Users/mizq7/Desktop/IDCR STUDY_JUNE 30, 2025/Remote Desktop_R Files and Folder/IDCRRR/output/shinyData_.rds & .xlsx version/preference_score_dist_t184_c185_IDCRRR_DB.xlsx'

# Load the data
df = pd.read_excel(file_path)

# Filter out rows with both densities <0.0001 for clarity
filtered = df[(df['target_density'] >= 0.0001) | (df['comparator_density'] >= 0.0001)]

plt.figure(figsize=(8, 5))
sns.lineplot(data=filtered, x='preference_score', y='target_density', label='Target Group (HSV-1)', color='blue')
sns.lineplot(data=filtered, x='preference_score', y='comparator_density', label='Comparator Group', color='orange')

plt.xlabel('Preference Score')
plt.ylabel('Density')
plt.title('Preference Score Density by Group')
plt.legend()
plt.tight_layout()
plt.savefig('preference_score_density_combined.png', dpi=300)
plt.show()
