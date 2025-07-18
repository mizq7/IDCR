import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Read your Excel data
file_path = '/Users/mizq7/Desktop/IDCR STUDY_JUNE 30, 2025/Remote Desktop_R Files and Folder/IDCRRR/output/balance/bal_t184_c185_o179_a1.xlsx'
df = pd.read_excel(file_path)

# Ensure consistent string types for groupings
df['domainId'] = df['domainId'].astype(str)
df['covariateName'] = df['covariateName'].astype(str)

# 1. Scatterplot: SMD before vs. after matching (all covariates)
plt.figure(figsize=(8, 6))
sns.scatterplot(
    x='beforeMatchingStdDiff',
    y='afterMatchingStdDiff',
    hue='domainId',
    data=df,
    alpha=0.7,
    edgecolor=None
)
plt.axhline(0.1, color='gray', linestyle='--', lw=1)
plt.axhline(-0.1, color='gray', linestyle='--', lw=1)
plt.axvline(0.1, color='gray', linestyle='--', lw=1)
plt.axvline(-0.1, color='gray', linestyle='--', lw=1)
plt.plot([-3, 3], [-3, 3], color='black', lw=1, linestyle=':')  # y=x line
plt.title("Covariate Standardized Mean Differences: Before vs After Matching")
plt.xlabel("SMD Before Matching")
plt.ylabel("SMD After Matching")
plt.legend(title='Domain', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

# 2. Dumbbell Plot: SMD improvement for top 20 most imbalanced (absolute diff)
df['abs_diff'] = (df['beforeMatchingStdDiff'].abs() - df['afterMatchingStdDiff'].abs())
top20 = df.nlargest(20, 'abs_diff').copy()
top20 = top20.sort_values('abs_diff', ascending=False)

plt.figure(figsize=(8, 10))
for i, row in enumerate(top20.itertuples()):
    plt.plot([row.beforeMatchingStdDiff, row.afterMatchingStdDiff], [i, i], color='grey', lw=2)
    plt.plot(row.beforeMatchingStdDiff, i, 'o', color='blue', label='Before' if i == 0 else "")
    plt.plot(row.afterMatchingStdDiff, i, 'o', color='orange', label='After' if i == 0 else "")
plt.yticks(range(len(top20)), top20['covariateName'])
plt.xlabel("Standardized Mean Difference")
plt.title("Top 20 Covariates: SMD Before vs After Matching")
plt.legend()
plt.tight_layout()
plt.show()

# 3. Violin/Boxplot: Distribution of SMDs before and after matching
smd_melt = df.melt(
    value_vars=['beforeMatchingStdDiff', 'afterMatchingStdDiff'],
    var_name='Phase',
    value_name='SMD'
)
plt.figure(figsize=(8, 6))
sns.violinplot(x='Phase', y='SMD', data=smd_melt, inner='box', cut=0)
plt.axhline(0.1, color='gray', linestyle='--', lw=1)
plt.axhline(-0.1, color='gray', linestyle='--', lw=1)
plt.title("Distribution of Covariate SMDs Before and After Matching")
plt.ylabel("Standardized Mean Difference")
plt.tight_layout()
plt.show()

# 4. Bar Plot: Top 10 most imbalanced after matching
df['abs_after_smd'] = df['afterMatchingStdDiff'].abs()
top10_imbalanced = df.nlargest(10, 'abs_after_smd')

plt.figure(figsize=(10, 6))
sns.barplot(
    y='covariateName', x='abs_after_smd', data=top10_imbalanced,
    hue='domainId', dodge=False
)
plt.axvline(0.1, color='gray', linestyle='--', lw=1)
plt.title("Top 10 Most Imbalanced Covariates After Matching")
plt.xlabel("Absolute Standardized Mean Difference (After Matching)")
plt.ylabel("Covariate Name")
plt.tight_layout()
plt.show()

# 5. Box Plot: Domain-level SMD distribution before and after matching
smd_domain = df.melt(
    id_vars='domainId',
    value_vars=['beforeMatchingStdDiff', 'afterMatchingStdDiff'],
    var_name='Phase',
    value_name='SMD'
)
plt.figure(figsize=(12, 6))
sns.boxplot(x='domainId', y='SMD', hue='Phase', data=smd_domain, showfliers=False)
plt.axhline(0.1, color='gray', linestyle='--', lw=1)
plt.axhline(-0.1, color='gray', linestyle='--', lw=1)
plt.title("Covariate Balance by Domain (Boxplot of SMDs)")
plt.xlabel("Domain")
plt.ylabel("Standardized Mean Difference")
plt.legend(title='Matching Phase')
plt.tight_layout()
plt.show()

# 6. Scatterplot: Mean prevalence in target group before vs. after matching
plt.figure(figsize=(8, 6))
sns.scatterplot(
    x='beforeMatchingMeanTarget',
    y='afterMatchingMeanTarget',
    hue='domainId',
    data=df,
    alpha=0.6,
    edgecolor=None
)
plt.plot([0, 1], [0, 1], color='black', lw=1, linestyle=':')  # identity line
plt.title("Prevalence in Target Group: Before vs After Matching")
plt.xlabel("Mean Before Matching")
plt.ylabel("Mean After Matching")
plt.legend(title='Domain', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()
