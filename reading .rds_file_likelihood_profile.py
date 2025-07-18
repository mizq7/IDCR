import pyreadr
import pandas as pd

# File paths
rds_path = '/Users/mizq7/Desktop/IDCR STUDY_JUNE 30, 2025/Remote Desktop_R Files and Folder/IDCRRR/output/shinyData/likelihood_profile_IDCRRR_DB.rds'
xlsx_path = '/Users/mizq7/Desktop/IDCR STUDY_JUNE 30, 2025/Remote Desktop_R Files and Folder/IDCRRR/output/shinyData/likelihood_profile_IDCRRR_DB.xlsx'

# Read .rds file
result = pyreadr.read_r(rds_path)

# If there are multiple objects in the .rds, choose the first DataFrame
# Most RDS files have a single DataFrame, use .items() to access it
for key, df in result.items():
    # Write to Excel file
    df.to_excel(xlsx_path, index=False)
    print(f"Converted '{key}' from .rds to Excel: {xlsx_path}")
    break  # Remove this break if you want to export all objects

# If you want to export all dataframes in the .rds file:
# for key, df in result.items():
#     df.to_excel(f"/path/to/output/{key}.xlsx", index=False)
