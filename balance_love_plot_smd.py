#!/usr/bin/env python3
# ---------------------------------------------------------------------------
#  DOMAIN-STRATIFIED LOVE PLOT  (|SMD| before vs after PS weighting)
#  Generates:  Figure_LovePlot_CovariateBalance.png   at same folder level
# ---------------------------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
from pathlib import Path

# ========== 1.  FILE LOCATIONS =============================================
ROOT = Path("/Users/mizq7/Desktop/IDCR STUDY_JUNE 30, 2025/"
            "Remote Desktop_R Files and Folder/IDCRRR/output/"
            "shinyData_.rds & .xlsx version")

BALANCE_XLSX      = ROOT / "covariate_balance_t184_c185_IDCRRR_DB.xlsx"
COVAR_XLSX        = ROOT / "covariate_IDCRRR_DB.xlsx"
COVAR_ANALYSIS_XL = ROOT / "covariate_analysis_IDCRRR_DB.xlsx"
OUT_PNG           = ROOT / "Figure_LovePlot_CovariateBalance.png"

# ========== 2.  LOAD AND MERGE =============================================
print("Reading Excel files …")
bal  = pd.read_excel(BALANCE_XLSX)
cov  = pd.read_excel(COVAR_XLSX)          # covariate_id → covariate_name, covariate_analysis_id
anal = pd.read_excel(COVAR_ANALYSIS_XL)   # covariate_analysis_id → covariate_analysis_name

df = (bal
      .merge(cov[["covariate_id", "covariate_name", "covariate_analysis_id"]],
             on="covariate_id", how="left")
      .merge(anal[["covariate_analysis_id", "covariate_analysis_name"]],
             on="covariate_analysis_id", how="left"))

# ========== 3.  CREATE DOMAIN VARIABLE =====================================
def classify_domain(txt: str) -> str:
    """Collapse detailed analysis names into 3 broad OMOP domains."""
    if isinstance(txt, str):
        if "Demographics" in txt:
            return "Demographics"
        if "Procedure" in txt or "Condition" in txt:
            return "Condition/Procedure"
        if "Measurement" in txt:
            return "Measurement"
    return "Other"

df["domain"] = df["covariate_analysis_name"].apply(classify_domain)

# ========== 4.  COMPUTE |SMD| AND ORDER ====================================
df["abs_before"] = df["std_diff_before"].abs()
df["abs_after"]  = df["std_diff_after"].abs()
df = df.sort_values("abs_after", ascending=False).reset_index(drop=True)
df["rank"] = df.index + 1          # 1 = worst residual imbalance

# ========== 5.  COLOUR MAP =================================================
PALETTE = {           # Colour-blind friendly
    "Demographics"        : "#0072B5",  # royal-blue
    "Condition/Procedure" : "#E69F00",  # orange
    "Measurement"         : "#009E73",  # bluish-green
    "Other"               : "#9E9E9E"   # light grey
}
df["colour"] = df["domain"].map(PALETTE)

# ========== 6.  PLOT =======================================================
plt.figure(figsize=(7, 10))

# Hollow grey dots  = BEFORE weighting
plt.scatter(df["abs_before"], df["rank"],
            facecolors='none', edgecolors='#C0C0C0',
            s=20, alpha=0.6)

# Solid coloured dots = AFTER weighting
plt.scatter(df["abs_after"], df["rank"],
            c=df["colour"], s=20)

# Threshold
plt.axvline(0.10, color="black", linestyle="--", lw=1)

# Label top 25 residual imbalances
for _, row in df.head(25).iterrows():
    plt.text(row["abs_after"] + 0.005, row["rank"],
             row["covariate_name"][:40], fontsize=6, va='center')

# Axes & styling
plt.gca().invert_yaxis()
plt.yticks([])
plt.xlabel("|Standardised Mean Difference|", fontsize=10)
plt.title("Domain-stratified Love Plot of Covariate Balance", fontsize=12)

# Legend
legend_handles = [
    mlines.Line2D([], [], marker='o', linestyle='', markersize=5,
                  markerfacecolor='none', markeredgecolor='#C0C0C0',
                  label='Before PS weighting'),
    mlines.Line2D([], [], marker='o', linestyle='', markersize=5,
                  markerfacecolor='#4D4D4D', markeredgecolor='#4D4D4D',
                  label='After PS weighting')
]
for dom, col in PALETTE.items():
    if dom != "Other":   # include or omit 'Other' as desired
        legend_handles.append(
            mlines.Line2D([], [], marker='o', linestyle='',
                          markersize=5, markerfacecolor=col, markeredgecolor=col,
                          label=dom)
        )
plt.legend(handles=legend_handles, frameon=False, fontsize=7, loc='upper right')
plt.tight_layout()

# ========== 7.  SAVE ========================================================
plt.savefig(OUT_PNG, dpi=300)
plt.close()
print(f"✓ Love plot saved to: {OUT_PNG}")
