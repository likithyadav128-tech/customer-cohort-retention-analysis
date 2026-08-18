import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load cleaned dataset

INPUT_FILE = r"C:\Users\likit\OneDrive\Documents\Customer-Cohort-Retention-Analysis\data\cleaned_retail_data.csv"

print("Loading cleaned dataset...")

df = pd.read_csv(
    INPUT_FILE,
    parse_dates=["InvoiceDate"]
)

print("Dataset loaded successfully!")
print("Rows:", len(df))


# 2. Create Invoice Month

df["InvoiceMonth"] = df["InvoiceDate"].dt.to_period("M")

print("\nInvoice month created successfully.")



# 3. Find First Purchase Month for Each Customer

customer_first_purchase = (
    df.groupby("CustomerID")["InvoiceMonth"]
      .min()
      .reset_index()
)

customer_first_purchase = customer_first_purchase.rename(
    columns={
        "InvoiceMonth": "CohortMonth"
    }
)

print("\n==========================================")
print("      CUSTOMER COHORT INFORMATION")
print("==========================================")

print(customer_first_purchase.head(10))


# ============================================================
# 4. Add Cohort Month to Original Dataset
# ============================================================

df = df.merge(
    customer_first_purchase,
    on="CustomerID",
    how="left"
)

print("\nCohort month added to transaction data.")


# ============================================================
# 5. Calculate Cohort Index
# ============================================================

df["CohortIndex"] = (
    (df["InvoiceMonth"].dt.year -
     df["CohortMonth"].dt.year) * 12

    +

    (df["InvoiceMonth"].dt.month -
     df["CohortMonth"].dt.month)

    + 1
)


print("\n==========================================")
print("          COHORT INDEX")
print("==========================================")

print(
    df[
        [
            "CustomerID",
            "InvoiceMonth",
            "CohortMonth",
            "CohortIndex"
        ]
    ].head(20)
)


# ============================================================
# 6. Count Unique Customers
# ============================================================

cohort_data = (
    df.groupby(
        [
            "CohortMonth",
            "CohortIndex"
        ]
    )["CustomerID"]
    .nunique()
    .reset_index()
)

cohort_data = cohort_data.rename(
    columns={
        "CustomerID": "Customers"
    }
)


print("\n==========================================")
print("       COHORT CUSTOMER COUNTS")
print("==========================================")

print(cohort_data.head(20))


# ============================================================
# 7. Create Cohort Pivot Table
# ============================================================

cohort_pivot = cohort_data.pivot(
    index="CohortMonth",
    columns="CohortIndex",
    values="Customers"
)


print("\n==========================================")
print("          COHORT PIVOT TABLE")
print("==========================================")

print(cohort_pivot)


# ============================================================
# 8. Calculate Retention Percentage
# ============================================================

retention_matrix = cohort_pivot.divide(
    cohort_pivot.iloc[:, 0],
    axis=0
) * 100


print("\n==========================================")
print("        CUSTOMER RETENTION (%)")
print("==========================================")

print(
    retention_matrix.round(2)
)


# ============================================================
# 9. Save Cohort Customer Counts
# ============================================================

cohort_pivot.to_csv(
    "output/cohort_customer_counts.csv"
)

print(
    "\nSaved: output/cohort_customer_counts.csv"
)


# ============================================================
# 10. Save Retention Matrix
# ============================================================

retention_matrix.to_csv(
    "output/cohort_retention.csv"
)

print(
    "Saved: output/cohort_retention.csv"
)


# ============================================================
# 11. Create Retention Heatmap
# ============================================================

plt.figure(
    figsize=(14, 8)
)

sns.heatmap(
    retention_matrix,
    annot=True,
    fmt=".1f",
    cmap="Blues",
    vmin=0,
    vmax=100
)

plt.title(
    "Customer Cohort Retention Rate (%)",
    fontsize=16
)

plt.xlabel(
    "Months Since First Purchase"
)

plt.ylabel(
    "Customer Cohort"
)

plt.tight_layout()


# ============================================================
# 12. Save Heatmap
# ============================================================

plt.savefig(
    "output/cohort_retention_heatmap.png",
    dpi=200,
    bbox_inches="tight"
)

print(
    "Saved: output/cohort_retention_heatmap.png"
)


# ============================================================
# 13. Display Heatmap
# ============================================================

plt.show()


# ============================================================
# 14. Final Message
# ============================================================

print("\n==========================================")
print("     COHORT ANALYSIS COMPLETED!")
print("==========================================")

print("""
Created files:

1. cohort_customer_counts.csv
2. cohort_retention.csv
3. cohort_retention_heatmap.png
""")