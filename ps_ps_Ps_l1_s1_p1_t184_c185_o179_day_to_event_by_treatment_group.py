import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = '/Users/mizq7/Desktop/IDCR STUDY_JUNE 30, 2025/Remote Desktop_R Files and Folder/IDCRRR/output/cmOutput/Ps_l1_s1_p1_t184_c185_o179.csv'
df = pd.read_csv(file_path)

plt.figure(figsize=(8,6))
sns.boxplot(x='treatment', y='daysToEvent', data=df)
plt.title('Days to Event by Treatment Group')
plt.xlabel('Treatment (0=Comparator, 1=Target)')
plt.ylabel('Days to Event')
plt.tight_layout()
plt.show()
