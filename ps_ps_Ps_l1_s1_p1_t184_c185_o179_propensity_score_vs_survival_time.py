import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = '/Users/mizq7/Desktop/IDCR STUDY_JUNE 30, 2025/Remote Desktop_R Files and Folder/IDCRRR/output/cmOutput/Ps_l1_s1_p1_t184_c185_o179.csv'
df = pd.read_csv(file_path)

plt.figure(figsize=(8,6))
sns.scatterplot(x='propensityScore', y='survivalTime', hue='treatment', data=df, alpha=0.7)
plt.title('Propensity Score vs. Survival Time')
plt.xlabel('Propensity Score')
plt.ylabel('Survival Time (days)')
plt.legend(title='Treatment', labels=['Comparator (0)', 'Target (1)'])
plt.tight_layout()
plt.show()
