"""
analysis.py — KPI & Fulfilment Analysis for Amazon Marketplace Sales
--------------------------------------------------------------------

Business-focused analytics including:
- Core KPIs (Revenue, Orders, AOV, MOV)
- Order status mix (Delivered / Cancelled / Returned / In-Progress)
- Promotion efficiency & AOV uplift
- B2B vs Retail performance split
- Category concentration (Pareto risk)
- SKU catalogue efficiency (Low-rotation & Dead SKUs)
- Short-period trend KPIs (Monthly revenue & MoM growth)
- Fulfilment risk (Revenue stuck in Amazon flow)
- Managerial insights for commercial action

Output:
    → KPI & insight summary printed to console
    → KPI summary file: results/kpi_summary.csv
"""

import os
import pandas as pd


# ===== Input Validation =====
base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
input_path = os.path.join(base_path, "results", "cleaned_data.csv")
sales = pd.read_csv(input_path, parse_dates=["date"])

print("\n===== Amazon Marketplace — KPI Summary =====\n")
    
# ===== Date Range Check & Q2 Filter (Apr–Jun 2022) =====
print(f"Raw start date : {sales['date'].min().date()}")
print(f"Raw end date   : {sales['date'].max().date()}")

# Business scope: focus on Q2 2022 (Apr–Jun)
start_date = "2022-04-01"
end_date = "2022-06-30"

q2_data = (sales["date"] >= start_date) & (sales["date"] <= end_date)
sales = sales[q2_data].copy()

print(f"Filtered data range: {start_date} to {end_date}")
print(f"Rows after Q2 filter: {len(sales):,}")
print("-" * 50)

# === Analytical Assumptions ===
# These assumptions ensure KPI definitions remain business-valid:
#
# • Order Value KPIs (AOV, MOV):
#     - Revenue aggregated at order_id level (not item price)
#
# • Promotion Definition (Order-Level):
#     - Promo Order: an order where at least one item has promotion_ids
#       not null and not equal to "No Promotion".
#     - Non‑Promo Order: an order where none of the items have a promotion
#       (promotion_ids is null or equal to "No Promotion").
#
# • B2B Identification:
#     - Column `b2b` is boolean (True = B2B order, False = Retail order)
#
# • Fulfilment Mapping:
#     - "amazon" keywords → amazon fulfilment
#     - "merchant" keywords → merchant fulfilment
#     - otherwise → "unknown"
# Unrealized Revenue (Amazon Fulfilment)
# Definition:
#   Revenue from orders that have NOT been realized:
#       - "in_progress" → pending
#       - "cancelled"   → lost
#       - "returned"    → lost
#
# Data contract (guaranteed by cleaning.py)
# - promotion_ids contains no NaN
# - order_id maps to exactly one order_status
# - fulfilment contains only "Amazon"
#
# Business Impact:
#     These assumptions avoid misleading KPIs when data quality varies

# ======================
# Core KPIs
# ======================
Total_Revenue = float(sales["amount"].sum())
Total_Orders = int(sales["order_id"].nunique())
Total_Items = int(sales["qty"].sum())
AOV = Total_Revenue / Total_Orders if Total_Orders > 0 else 0
Median_Order_Value = sales.groupby("order_id")["amount"].sum().median()

print(f"Total Revenue = {Total_Revenue:,.0f} INR")
print("-" * 50)
print(f"Total Orders = {Total_Orders:,}")
print("-" * 50)
print(f"Total Items Sold = {Total_Items:,}")
print("-" * 50)
print(f"Average Order Value (AOV) = {AOV:,.2f} INR")
print("-" * 50)
print(f"Median Order Value = {Median_Order_Value:,.2f} INR")
print("-" * 50)

def order_pct(n):
    return round(n / Total_Orders * 100, 2) if Total_Orders > 0 else 0
def revenue_pct(n):
    return round(n / Total_Revenue * 100, 2) if Total_Revenue > 0 else 0

# ======================
# Order Status KPIs
# ======================
delivered_revenue = sales[sales['order_status'] == "delivered"]['amount'].sum()
cancelled_revenue = sales[sales['order_status'] == "cancelled"]['amount'].sum()
returned_revenue = sales[sales['order_status'] == "returned"]['amount'].sum()
in_progress_revenue = sales[sales['order_status'] == "in_progress"]['amount'].sum()

delivered_rate = revenue_pct(delivered_revenue)
cancellation_rate = revenue_pct(cancelled_revenue)
return_rate = revenue_pct(returned_revenue)
in_progress_rate = revenue_pct(in_progress_revenue)

print(f"Delivered Rate = {delivered_rate} %")
print(f"Cancellation Rate = {cancellation_rate} %")
print(f"Return Rate = {return_rate} %")
print(f"In-progress Rate = {in_progress_rate} %")
print("-" * 50)

# ======================
# Promotion Efficiency
# ======================
promo_order_ids = sales[sales["promotion_ids"] != "No Promotion"]["order_id"].unique()

promo_sales = sales[sales["order_id"].isin(promo_order_ids)]
nonpromo_sales = sales[~sales["order_id"].isin(promo_order_ids)]

promo_orders = promo_sales['order_id'].nunique()
nonpromo_orders = nonpromo_sales['order_id'].nunique()

promo_revenue = promo_sales['amount'].sum()
nonpromo_revenue = nonpromo_sales['amount'].sum()

promo_orders_pct = order_pct(promo_orders)
promo_revenue_pct = revenue_pct(promo_revenue) 
aov_promo = round(promo_revenue / promo_orders, 2) if promo_orders > 0 else 0
aov_nonpromo = round(nonpromo_revenue / nonpromo_orders, 2) if nonpromo_orders > 0 else 0
    
print(f"Orders from Promotions = {promo_orders_pct} %")
print(f"Revenue from Promotions = {promo_revenue_pct} %")
print(f"AOV with Promotions = {aov_promo:,.2f} INR")
print(f"AOV without Promotions = {aov_nonpromo:,.2f} INR")
print("-" * 50)

# ======================
# B2B vs Retail
# ======================
sales_b2b = sales[sales["b2b"]==True]
sales_retail = sales[sales["b2b"]==False]

b2b_orders = sales_b2b["order_id"].nunique()
retail_orders = sales_retail["order_id"].nunique()
b2b_aov = round(sales_b2b["amount"].sum() / b2b_orders,2) if b2b_orders > 0 else 0
retail_aov = round(sales_retail["amount"].sum() / retail_orders,2) if retail_orders > 0 else 0

b2b_revenue_pct = round(sales_b2b["amount"].sum()/Total_Revenue * 100,2)
retail_revenue_pct = round(sales_retail['amount'].sum() / Total_Revenue * 100, 2)

print(f"Revenue from B2B customers = {b2b_revenue_pct} %")
print(f"Revenue from Retail customers = {retail_revenue_pct} %")
print(f"Orders from B2B customers = {order_pct(b2b_orders)} %")
print(f"Orders from Retail customers = {order_pct(retail_orders)} %")
print(f"AOV for B2B Customers = {b2b_aov:,.2f} INR")
print(f"AOV for Retail Customers = {retail_aov:,.2f} INR")
print("-" * 50)

# ======================
# Category Performance
# ======================
cat_rev = sales.groupby("category")["amount"].sum().reset_index(name="Revenue")
cat_rev = cat_rev.sort_values("Revenue", ascending=False)

top_categories_share = round(cat_rev.head(2)["Revenue"].sum() / cat_rev["Revenue"].sum() * 100, 2)

print(f"Top 2 Categories Revenue Share = {top_categories_share} %")
print("Top Categories:")
print(cat_rev.head(5))
print("-" * 50)
print("Bottom Categories:")
print(cat_rev.tail(5))
print("-" * 50)

# ======================
# SKU Efficiency — Catalogue Waste
# ======================

# Aggregate revenue & orders per SKU
sku_rev = sales.groupby("sku")["amount"].sum().reset_index(name="rev")
sku_ord = sales.groupby("sku")["order_id"].nunique().reset_index(name="ord")
sku_perf = sku_rev.merge(sku_ord, on="sku")

# Rank calculations (Python = average rank)
sku_perf["rev_rank"] = sku_perf["rev"].rank(ascending=False)
sku_perf["ord_rank"] = sku_perf["ord"].rank(ascending=False)

# Thresholds (Top 50% by orders vs Bottom 50% by revenue)
threshold = len(sku_perf) * 0.5

# Low-rotation Flag
sku_perf["low_rotation_flag"] = (
    (sku_perf["ord_rank"] <= threshold) &
    (sku_perf["rev_rank"] > threshold)
).astype(int)

# Dead SKU Flag (no true zero-orders in dataset → use MOV profitability logic)
sku_perf["dead_flag"] = (
    (sku_perf["ord"] <= 1) &
    (sku_perf["rev"] < Median_Order_Value)   
).astype(int)

# KPI calculations
low_rotation = sku_perf[sku_perf["low_rotation_flag"] == 1]
dead_skus   = sku_perf[sku_perf["dead_flag"] == 1]

low_rotation_pct = round(len(low_rotation) / len(sku_perf) * 100, 2)
dead_skus_pct    = round(len(dead_skus) / len(sku_perf) * 100, 2)

# Export for BI tools (Tableau)
output_path = os.path.join(base_path, "results","sku_performance.csv")
os.makedirs(os.path.dirname(output_path), exist_ok=True)
sku_perf.round(2).to_csv(output_path, index=False)
print("✔ SKU performance exported → results/sku_performance.csv")
print("  Columns: sku, rev, ord, rev_rank, ord_rank, low_rotation_flag, dead_flag")

# Text summary in console
print(f"Low Rotation SKUs = {len(low_rotation)} ({low_rotation_pct}%)")
print(f"Dead SKUs         = {len(dead_skus)} ({dead_skus_pct}%)")
print("-" * 50)

# ======================
# Trend KPIs
# ======================
sales["month"] = sales["date"].dt.month_name().str[:3]
month_order = ["Apr", "May", "Jun"]
sales["month"] = pd.Categorical(sales["month"], categories=month_order, ordered=True)
    
rev_month = sales.groupby("month", observed = True)["amount"].sum().reset_index(name="Revenue")
rev_month["MoM_Growth_%"] = round(rev_month["Revenue"].pct_change() * 100,2)
    
print("Monthly Revenue & MoM Growth:")
print(rev_month)
print("-" * 50)

# ======================
# Unrealized Revenue 
# (Amazon Fulfilment)
# =====================
amazon_sales = sales[sales["fulfilment"].str.lower() =="amazon"]
unrealized_statuses = ["in_progress", "cancelled", "returned"]
unrealized_revenue = amazon_sales[
    amazon_sales["order_status"].str.lower().isin(unrealized_statuses)]["amount"].sum()

print(f"⚠ Total Unrealized Revenue = {unrealized_revenue:,.0f} INR")
print("-" * 50)
    
# ======================
# Export KPI Table
# ======================
KPI_names = [
    "Total Revenue (INR)", "Total Orders", "Total Items Sold",
    "AOV (INR)", "Median Order Value (INR)",
    "Delivered Rate (%)", "Cancellation Rate (%)",
    "Return Rate (%)", "In-Progress Rate (%)",
    "Orders with Promotions (%)", "Revenue from Promotions (%)",
    "AOV with Promotions (INR)", "AOV without Promotions (INR)",
    "Revenue from B2B (%)", "Revenue from Retail (%)",
    "Low Rotation SKUs (%)", "Dead SKUs (%)",
    "Top 2 Category Revenue Share (%)",
    "Unrealized Revenue (INR)"
]

KPI_values = [
    Total_Revenue, Total_Orders, Total_Items,
    AOV, Median_Order_Value,
    delivered_rate, cancellation_rate,
    return_rate, in_progress_rate,
    promo_orders_pct, promo_revenue_pct,
    aov_promo, aov_nonpromo,
    b2b_revenue_pct, retail_revenue_pct,
    low_rotation_pct, dead_skus_pct,
    top_categories_share, unrealized_revenue
]

output_path = os.path.join(base_path, "results","kpi_summary.csv")
os.makedirs(os.path.dirname(output_path), exist_ok=True)
pd.DataFrame({"KPI": KPI_names, "Value": KPI_values}).round(2).to_csv(output_path, index=False)

print("✔ KPI summary exported")
print("=============================================")

# Compute unrealized revenue share for insights
share_risk = round(unrealized_revenue / Total_Revenue * 100, 2)

# ======================
# Scenario Analysis
# Impact of reducing cancellation rate
# ======================
revenue_cancelled = sales[sales["order_status"] == "cancelled"]["amount"].sum()

scenarios = [0.05, 0.10, 0.15]

for r in scenarios:
    recovered = r * revenue_cancelled
    impact_pct = (recovered / Total_Revenue) * 100

    print(f"Recovery Scenario {int(r*100)}%:")
    print(f"Additional Revenue: {recovered:,.0f} INR")
    print(f"Impact on Total Revenue: {impact_pct:.2f}%\n")

max_scenario = max(scenarios)
best_case_recovered = max_scenario * revenue_cancelled
best_case_pct = (best_case_recovered / Total_Revenue) * 100
cancel_share = (revenue_cancelled / Total_Revenue) * 100

# ======================
# Managerial Insights
# ======================
print("\n🧠 Managerial Insights")

print(f"• Amazon Fulfilment-related revenue exposure accounts for {share_risk}% of total revenue.")
print("  → This includes cancelled, returned, and in-progress orders; therefore it represents operational risk exposure rather than realized financial loss.")

print(f"• Cancelled orders represent {cancel_share:.2f}% of total revenue.")
print(f"  → A conservative 15% reduction could recover ~{best_case_pct:.2f}% incremental revenue without new customer acquisition.")

print("• Revenue structure suggests operational bottlenecks in fulfilment flow rather than pure demand weakness.")
print("  → However, this conclusion is directional and should be validated with category-level demand signals.")

print(f"• SKU inefficiency is material: {dead_skus_pct:.2f}% dead SKUs and {low_rotation_pct:.2f}% low-rotation SKUs.")
print("  → Indicates inefficient capital allocation in long-tail inventory.")

print(f"• Revenue concentration is high: top 2 categories contribute {top_categories_share}% of total revenue.")
print("  → This creates dependency risk on a small subset of demand drivers.")

print("\n• PRIORITY ORDER (impact × effort logic):")
print("  1. Fulfilment optimization (high impact, system-wide cash-flow effect)")
print("  2. Cancellation reduction (high impact, low effort, fast ROI)")
print("  3. Catalogue optimization (medium impact, medium effort)")
print("  4. Promotion refocus (strategic, long-term)")

print("\n✔ Analysis complete!")
print("=========================================================\n")
