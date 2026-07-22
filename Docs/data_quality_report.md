
# 📊 Data Quality Report — Amount Imputation Validation

The `amount` field is **highly right‑skewed** due to a small number of high‑value orders.  
This means average‑based methods (mean imputation) would **inflate commercial KPIs**.

---

### ✔ Imputation Strategy
**Global Median Imputation**

Why median?  
- It resists extreme outliers  
- It preserves **business reality** of most orders  
- It avoids distortion in revenue metrics (AOV, Total Revenue)

---

## Distribution Comparison

### 🔹 Before Imputation
*(Insert image: `Visuals/Distribution_Amount_Before.png`)*

### 🔹 After Imputation
*(Insert image: `Visuals/Distribution_Amount_After.png`)*

Even after imputation, the distribution remains right‑skewed → **we did not artificially add “fake revenue”** to the data.

---

## Summary Statistics Impact

<div align = "center">

| Metric      | Before    | After    | Interpretation                             |
|-------------|-----------|----------|--------------------------------------------|
| **Mean**    | 648       | 645      | Negligible shift → KPIs remain trustworthy |
| **Median**  | 605       | 605      | Central tendency fully preserved           |
| **Skewness**| High      | High     | Market reality unchanged                   |

</div>

---

### Final Business Message
By imputing missing amounts with **overall median**,  
we **balanced two priorities**:

📌 *Data completeness (no missing KPIs)*  
📌 *No distortion of commercial insights*

This ensures that **financial KPIs presented to stakeholders represent real business patterns** — not artifacts of cleaning.

---