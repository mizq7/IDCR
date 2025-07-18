import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid", font_scale=1.1)

file_path = '/Users/mizq7/Desktop/IDCR STUDY_JUNE 30, 2025/Remote Desktop_R Files and Folder/IDCRRR/output/cmOutput/Ps_l1_s1_p1_t184_c185_o179.csv'
df = pd.read_csv(file_path)

plt.figure(figsize=(8, 6))
sns.histplot(data=df, x='propensityScore', hue='treatment', bins=30, kde=True, element="step")
plt.title('Distribution of Propensity Scores by Treatment Group')
plt.xlabel('Propensity Score')
plt.ylabel('Count')
plt.tight_layout()
plt.show()
