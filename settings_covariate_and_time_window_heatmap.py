import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Example covariate/time window data
data = {
    'Covariate': [
        'Age Group', 'Gender', 'Ethnicity', 'Drug Group Era (Short)', 'Drug Group Era (Long)',
        'Measurement (Short)', 'Measurement (Long)', 'Condition Group Era (Short)', 'Condition Group Era (Long)'
    ],
    'Short-Term': [1, 1, 1, 1, 0, 1, 0, 1, 0],
    'Medium-Term': [0, 0, 0, 0, 0, 0, 0, 0, 0],
    'Long-Term': [0, 0, 0, 0, 1, 0, 1, 0, 1]
}
df = pd.DataFrame(data)
df.set_index('Covariate', inplace=True)

plt.figure(figsize=(8, 5))
sns.heatmap(df, annot=True, cbar=False, cmap='Greys', linewidths=0.5, linecolor='black')
plt.title('Covariate Inclusion by Time Window')
plt.ylabel('Covariate')
plt.xlabel('Time Window')
plt.tight_layout()
plt.show()
