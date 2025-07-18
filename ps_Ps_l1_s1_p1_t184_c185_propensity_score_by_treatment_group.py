import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data from your specified path
file_path = '/Users/mizq7/Desktop/IDCR STUDY_JUNE 30, 2025/Remote Desktop_R Files and Folder/IDCRRR/output/cmOutput/Ps_l1_s1_p1_t184_c185.csv'
df = pd.read_csv(file_path)

plt.figure(figsize=(8, 6))
sns.histplot(data=df, x='propensityScore', hue='treatment', bins=30, stat='density', element='step', common_norm=False, palette='muted', alpha=0.6)
plt.title('Histogram of Propensity Scores by Treatment Group')
plt.xlabel('Propensity Score')
plt.ylabel('Density')
plt.legend(title='Treatment', labels=['Comparator (0)', 'Target (1)'])
plt.tight_layout()
plt.show()
