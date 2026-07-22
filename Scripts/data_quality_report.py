"""
data_quality_report.py

Purpose
-------
Validate the impact of imputing missing values in the `Amount` column.
The script compares the distribution of transaction amounts before and
after median imputation to ensure that commercial KPIs are not distorted.

Outputs
-------
visuals/Distribution_Amount_Before.png
visuals/Distribution_Amount_After.png
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# --------------------------------------------------
# Input and Output path
# --------------------------------------------------
base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
raw_input_path = os.path.join(base_path, "data","Amazon_Sales_Report.xlsx")
imputed_input_path = os.path.join(base_path, "results","cleaned_data.csv")

output_path = os.path.join(base_path, "visuals")
os.makedirs(os.path.dirname(output_path), exist_ok=True)

# --------------------------------------------------
# Load datasets
# --------------------------------------------------
raw_sales = pd.read_excel(raw_input_path)               # before imputation
imputed_sales = pd.read_csv(imputed_input_path)         # after imputation

# ========== GLOBAL STYLE ==========
sns.set_style("darkgrid")  
plt.rcParams.update({
    "font.family": "sans-serif",
    "font.size": 12,
    "axes.titlesize": 16,
    "axes.titleweight": "bold",
    "axes.labelsize": 14,
    "axes.labelweight": "bold",
    "xtick.labelsize": 12,
    "ytick.labelsize": 12
})

# ==================================================
# Distribution of Amount — Before Imputation
# ==================================================
plt.figure(figsize=(14,6))
ax = sns.histplot(raw_sales["Amount"], bins=50, kde=True, alpha=0.7)

plt.title("Distribution of Amount - Before Imputation")
plt.xlabel("Amount")
plt.ylabel("")

padding = (raw_sales["Amount"].max() - raw_sales["Amount"].min()) * 0.25
ymax = ax.get_ylim()[1]

plt.text(
    raw_sales["Amount"].max() - padding,
    ymax * 0.90,
    f"Mean = {int(raw_sales['Amount'].mean())}",
    fontsize=14,
    fontweight="bold"
)

plt.text(
    raw_sales["Amount"].max() - padding,
    ymax * 0.80,
    f"Median = {int(raw_sales['Amount'].median())}",
    fontsize=14,
    fontweight="bold"
)

plt.tight_layout()
plt.savefig(os.path.join(output_path, "Distribution_Amount_Before.png"), bbox_inches="tight")
plt.close()

# ==================================================
# Distribution of Amount — After Imputation
# ==================================================
plt.figure(figsize=(14,6))
ax = sns.histplot(imputed_sales["amount"], bins=50, kde=True, alpha=0.7)

plt.title("Distribution of Amount - After Imputation")
plt.xlabel("Amount")
plt.ylabel("")

padding = (imputed_sales["amount"].max() - imputed_sales["amount"].min()) * 0.25
ymax = ax.get_ylim()[1]

plt.text(
    imputed_sales["amount"].max() - padding,
    ymax * 0.90,
    f"Mean = {int(imputed_sales['amount'].mean())}",
    fontsize=14,
    fontweight="bold"
)

plt.text(
    imputed_sales["amount"].max() - padding,
    ymax * 0.80,
    f"Median = {int(imputed_sales['amount'].median())}",
    fontsize=14,
    fontweight="bold"
)

plt.tight_layout()
plt.savefig(os.path.join(output_path, "Distribution_Amount_After.png"), bbox_inches="tight")
plt.close()

# ==================================================
# Summary statistics comparison
# ==================================================
print("\nData Quality Validation — Amount Imputation\n")

print("Before Imputation")
print("-----------------")
print(f"Mean   : {int(raw_sales['Amount'].mean())}")
print(f"Median : {int(raw_sales['Amount'].median())}")

print("\nAfter Imputation")
print("----------------")
print(f"Mean   : {int(imputed_sales['amount'].mean())}")
print(f"Median : {int(imputed_sales['amount'].median())}")

print("\nConclusion:")
print("Median imputation preserves the central tendency of the data and")
print("prevents inflation of revenue-related KPIs.")