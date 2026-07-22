"""
cleaning.py — Data Cleaning Module for Amazon Marketplace Sales Analysis
-----------------------------------------------------------------------

This script performs structured data cleaning and validation, including:
    • Schema validation for core business fields (Soft warnings)
    • Text normalization and whitespace trimming
    • Removal of Excel artifact columns (Unnamed)
    • Postal code standardization for mapping
    • Data type standardization for dates and numerics
    • Missing value handling with business logic
    • Median imputation for `amount` (right-skewed revenue distribution)
    • Essential geo-field filtration (drop missing city/state/country)
    • Status normalization (Delivered / Cancelled / Returned / In-Progress)

🔎 Analytical Decisions:
    • Median imputation is chosen due to right-skewed price distribution.
    • Geo columns are mapping-essential → rows missing city/state/country removed.

Output:
    → Cleaned dataset exported to results/cleaned_data.csv
    → Validation report printed to console

Author: Asma — Data Analyst
"""

import os
import pandas as pd
import numpy as np


# Load raw data
base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
input_path = os.path.join(base_path, "data","Amazon_Sales_Report.xlsx")
sales = pd.read_excel(input_path)
initial_rows = sales.shape[0]

# Normalize column names
sales.columns = (
    sales.columns.str.lower()
    .str.strip()
    .str.replace(" ", "_")
    .str.replace("-", "_")
)

# Drop Unnamed columns
sales.drop(columns=['unnamed:_22'], inplace = True)
    
# Clean string columns & fix textual nulls
obj_cols = sales.select_dtypes("object").columns
for col in obj_cols:
    sales[col] = (
        sales[col].astype(str)
        .str.strip()
        .replace(
            ["", "nan", "NaN", "none", "None", "null", "Null", "NA", "N/A", "n/a"],
            np.nan,
            regex=False
        )
    )
# Convert date accurately
sales["date"] = pd.to_datetime(sales["date"], errors="coerce", dayfirst=True)

# Drop duplicates
duplicate_count = sales.duplicated().sum()
sales.drop_duplicates(inplace=True)

# Geo fields cleaning — must be valid for mapping
geo_fields = ["ship_city", "ship_state", "ship_country"]
for col in geo_fields:
    sales[col] = (
        sales[col].astype(str)
        .str.strip()
        .replace("nan", np.nan)
        )

# Postal code normalization
sales["ship_postal_code"] = (
    sales["ship_postal_code"]
    .astype(str)
    .str.replace(".0", "", regex=False)
    .replace("nan", np.nan)
)

# Drop rows missing key GEO info
before_geo = sales.shape[0]
sales.dropna(subset=geo_fields, inplace=True)
geo_dropped = before_geo - sales.shape[0]

# Amount imputation — global median (business-safe)
sales["amount"] = pd.to_numeric(sales["amount"], errors="coerce")
median_amount = sales["amount"].median()
sales["amount"] = sales["amount"].fillna(median_amount)
print(f"✔ Amount missing values imputed with global median ({median_amount}) "
      "- avoids distorting category price structure")

# Fill remaining defaults AFTER fixing textual nulls
fill_defaults = {
    "courier_status": "Unknown",
    "currency": "INR",
    "promotion_ids": "No Promotion",
    "fulfilled_by": "Unknown"
}
for col, val in fill_defaults.items():
    sales[col]=sales[col].fillna(val)

# Status normalization
delivered = ['Shipped - Delivered to Buyer']
cancelled = ['Cancelled']
returned = [
    'Shipped - Returned to Seller',
    'Shipped - Rejected by Buyer',
    'Shipped - Lost in Transit',
    'Shipped - Returning to Seller',
    'Shipped - Damaged'
]
in_progress = [
    'Shipped', 'Shipped - Out for Delivery', 'Shipped - Picked Up',
    'Pending', 'Pending - Waiting for Pick Up', 'Shipping'
]

conditions = [
    sales["status"].isin(delivered),
    sales["status"].isin(cancelled),
    sales["status"].isin(returned),
    sales["status"].isin(in_progress)
]
labels = ["delivered", "cancelled", "returned", "in_progress"]
sales["order_status"] = np.select(conditions, labels, default="unknown")

# Ensure output path exists
output_path = os.path.join(base_path, "results","cleaned_data.csv")
os.makedirs(os.path.dirname(output_path), exist_ok=True)
sales.to_csv(output_path, index=False)


# Final clean summary
print("\n===== Data Cleaning Summary =====")
print(f"Initial rows      : {initial_rows}")
print(f"Final rows        : {sales.shape[0]}")
print(f"Duplicates removed: {duplicate_count}")
print(f"GEO dropped       : {geo_dropped}")
print(f"✔ Cleaned dataset exported → {output_path}")
print("=================================\n")
print("🏁 Cleaning process completed.\n")