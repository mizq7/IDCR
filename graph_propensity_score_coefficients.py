import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load files
model_df = pd.read_excel('/Users/mizq7/Desktop/IDCR STUDY_JUNE 30, 2025/Remote Desktop_R Files and Folder/IDCRRR/output/shinyData_.rds & .xlsx version/propensity_model_IDCRRR_DB.xlsx')
covariate_df = pd.read_excel('/Users/mizq7/Desktop/IDCR STUDY_JUNE 30, 2025/Remote Desktop_R Files and Folder/IDCRRR/output/shinyData_.rds & .xlsx version/covariate_IDCRRR_DB.xlsx')

# Merge on covariate_id
merged = pd.merge(model_df, covariate_df, left_on='covariate_id', right_on='covariate_id', how='left')

# Density plot of coefficients
plt.figure(figsize=(8,5))
sns.histplot(merged['coefficient'], bins=40, kde=True, color='skyblue')
plt.title('Distribution of Fitted Propensity Score Coefficients')
plt.xlabel('Coefficient Value')
plt.ylabel('Number of Covariates')
plt.tight_layout()
plt.show()
