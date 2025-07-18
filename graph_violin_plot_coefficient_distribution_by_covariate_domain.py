import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# File locations
model_file = '/Users/mizq7/Desktop/IDCR STUDY_JUNE 30, 2025/Remote Desktop_R Files and Folder/IDCRRR/output/shinyData_.rds & .xlsx version/propensity_model_IDCRRR_DB.xlsx'
covariate_file = '/Users/mizq7/Desktop/IDCR STUDY_JUNE 30, 2025/Remote Desktop_R Files and Folder/IDCRRR/output/shinyData_.rds & .xlsx version/covariate_IDCRRR_DB.xlsx'

# Load Excel files
model_df = pd.read_excel(model_file)
covariate_df = pd.read_excel(covariate_file)

# Print column options for inspection
print("Model file columns:", model_df.columns.tolist())
print("Covariate file columns:", covariate_df.columns.tolist())

# Merge on available covariate ID column
possible_cov_id_cols = ['covariate_id', 'covariateId', 'CovariateId', 'Covariate_ID']
for col in possible_cov_id_cols:
    if col in model_df.columns and col in covariate_df.columns:
        merged = pd.merge(model_df, covariate_df, on=col, how='left')
        break
else:
    raise ValueError("Covariate ID column not found in both files. Please check column names.")

print("Merged dataframe columns:", merged.columns.tolist())
print(merged.head())

# Identify the domain column
domain_cols = ['domain_id', 'domain', 'type', 'covariate_type', 'domainId', 'CovariateType']
domain_col = None
for col in domain_cols:
    if col in merged.columns:
        domain_col = col
        print(f"Using '{col}' as the domain/type column for violin plot color-coding.")
        break

if domain_col is None:
    print("No domain/type column found. Please inspect columns and set domain_col manually.")
    print("Available columns:", merged.columns.tolist())
    # Optionally: domain_col = 'set_column_name_here'
    # exit()

# Violin plot
plt.figure(figsize=(12, 7))
if domain_col:
    sns.violinplot(
        x=domain_col,
        y='coefficient',
        data=merged,
        palette='Set2',
        cut=0
    )
else:
    sns.violinplot(
        y='coefficient',
        data=merged,
        color='skyblue'
    )
plt.title('Distribution of Propensity Model Coefficients by Covariate Domain')
plt.xlabel('Covariate Domain')
plt.ylabel('Coefficient (Log Odds)')
plt.axhline(0, color='gray', linestyle='--')
plt.tight_layout()
plt.show()
