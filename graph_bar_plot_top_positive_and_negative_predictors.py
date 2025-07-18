import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# File locations
model_file = '/Users/mizq7/Desktop/IDCR STUDY_JUNE 30, 2025/Remote Desktop_R Files and Folder/IDCRRR/output/shinyData_.rds & .xlsx version/propensity_model_IDCRRR_DB.xlsx'
covariate_file = '/Users/mizq7/Desktop/IDCR STUDY_JUNE 30, 2025/Remote Desktop_R Files and Folder/IDCRRR/output/shinyData_.rds & .xlsx version/covariate_IDCRRR_DB.xlsx'

# Load files (update sheet_name if needed)
model_df = pd.read_excel(model_file)
covariate_df = pd.read_excel(covariate_file)

# Print out available columns in each dataframe
print("Model file columns:", model_df.columns.tolist())
print("Covariate file columns:", covariate_df.columns.tolist())

# Merge using the covariate id (adjust column names if needed)
# Try typical variants if merge fails
possible_cov_id_cols = ['covariate_id', 'covariateId', 'CovariateId', 'Covariate_ID']
for col in possible_cov_id_cols:
    if col in model_df.columns and col in covariate_df.columns:
        merged = pd.merge(model_df, covariate_df, on=col, how='left')
        break
else:
    raise ValueError("Covariate ID column not found in both files. Please check the exact column name.")

print("Merged dataframe columns:", merged.columns.tolist())
print(merged.head())

# Identify domain/type column for coloring
domain_cols = ['domain_id', 'domain', 'type', 'covariate_type', 'domainId', 'CovariateType']
domain_col = None
for col in domain_cols:
    if col in merged.columns:
        domain_col = col
        print(f"Using '{col}' as the domain/type column for color-coding.")
        break

if domain_col is None:
    print("No domain/type column found. Please inspect columns and set domain_col manually.")
    print("Available columns:", merged.columns.tolist())
    # Optionally, set domain_col = 'the_correct_column_here'
    # exit()  # Stop if no domain column found

# Identify top 10 positive and negative coefficients
top_pos = merged.sort_values('coefficient', ascending=False).head(10)
top_neg = merged.sort_values('coefficient').head(10)
top_covariates = pd.concat([top_pos, top_neg])

# Plot
plt.figure(figsize=(10, 7))
if domain_col:
    sns.barplot(
        y='covariate_name',    # Adjust if your name column differs
        x='coefficient',
        hue=domain_col,
        data=top_covariates,
        dodge=False
    )
else:
    sns.barplot(
        y='covariate_name',
        x='coefficient',
        data=top_covariates,
        color='b'
    )
plt.title('Top Positive and Negative Predictors of HSV-1 Infection')
plt.xlabel('Coefficient (Log Odds)')
plt.ylabel('Covariate')
plt.axvline(0, color='gray', linestyle='--')
if domain_col:
    plt.legend(title='Domain', bbox_to_anchor=(1.02, 1), loc='upper left')
plt.tight_layout()
plt.show()
