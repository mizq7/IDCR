import pandas as pd
import matplotlib.pyplot as plt

file_path = '/Users/mizq7/Desktop/IDCR STUDY_JUNE 30, 2025/Remote Desktop_R Files and Folder/IDCRRR/output/cmOutput/Ps_l1_s1_p1_t184_c185_o179.csv'
df = pd.read_csv(file_path)

outcome_counts = df.groupby('treatment')['outcomeCount'].sum().reset_index()

plt.figure(figsize=(6,5))
plt.bar(['Comparator (0)', 'Target (1)'], outcome_counts['outcomeCount'])
plt.title('Total Outcome Count by Treatment Group')
plt.xlabel('Treatment')
plt.ylabel('Total Outcome Count')
plt.tight_layout()
plt.show()
