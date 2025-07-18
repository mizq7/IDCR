# ---------------------------------------------------------------
# Supplementary-Table S1 generator -- Covariate balance diagnostics
# ---------------------------------------------------------------
import pandas as pd
from pathlib import Path

# ---- 1.  File locations ----------------------------------------------------
root = Path("/Users/mizq7/Desktop/IDCR STUDY_JUNE 30, 2025/"
            "Remote Desktop_R Files and Folder/IDCRRR/output/"
            "shinyData_.rds & .xlsx version")

f_cov           = root / "covariate_IDCRRR_DB.xlsx"
f_cov_analysis  = root / "covariate_analysis_IDCRRR_DB.xlsx"
f_balance       = root / "covariate_balance_t184_c185_IDCRRR_DB.xlsx"

# ---- 2.  Load workbooks ----------------------------------------------------
cov           = pd.read_excel(f_cov)              # covariate_id → covariate_name
cov_analysis  = pd.read_excel(f_cov_analysis)     # covariate_analysis_id → domain
balance       = pd.read_excel(f_balance)          # SMDs & means

# ---- 3.  Merge to attach names & domains -----------------------------------
tbl = (balance
       .merge(cov[["covariate_id",
                   "covariate_name",
                   "covariate_analysis_id"]],
              on="covariate_id", how="left")
       .merge(cov_analysis[["covariate_analysis_id",
                            "covariate_analysis_name"]],
              on="covariate_analysis_id", how="left"))

# ---- 4.  Compute absolute SMD after weighting ------------------------------
tbl["abs_std_diff_after"] = tbl["std_diff_after"].abs()

# ---- 5.  Re-order & sort ----------------------------------------------------
cols_wanted = ["covariate_id",
               "covariate_name",
               "covariate_analysis_name",
               "target_mean_before",
               "comparator_mean_before",
               "std_diff_before",
               "target_mean_after",
               "comparator_mean_after",
               "std_diff_after",
               "abs_std_diff_after"]
tbl = tbl[cols_wanted].sort_values("abs_std_diff_after", ascending=False)

# ---- 6.  Write Supplementary Table S1 --------------------------------------
out_file = root / "Table_S1_Covariate_Balance.xlsx"
tbl.to_excel(out_file, index=False)
print(f"✓ Supplementary table created at: {out_file}")
