import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Example DataFrame structure (fill with real counts/categories from your data)
df = pd.DataFrame({
    'ClinicalCategory': ['Dementia', 'Amnesia', 'Cognitive Deficit', 'Other', 'Dementia', 'Amnesia'],
    'ICDVersion': ['ICD-10-CM', 'ICD-10-CM', 'ICD-10-CM', 'ICD-9-CM', 'ICD-9-CM', 'ICD-9-CM'],
    'Count': [18, 4, 7, 21, 3, 6]
})

plt.figure(figsize=(8,6))
sns.barplot(data=df, x='ClinicalCategory', y='Count', hue='ICDVersion')
plt.title("Distribution of Codes by Clinical Category and ICD Version")
plt.ylabel("Number of Unique Codes")
plt.xlabel("Clinical Category")
plt.tight_layout()
plt.show()
