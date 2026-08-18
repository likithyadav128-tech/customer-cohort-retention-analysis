import pandas as pd


# ============================================================
# 1. Load all processed datasets
# ============================================================

print("Loading processed datasets...")

transactions = pd.read_csv(
    "output/cleaned_retail_data.csv"
)

customer_metrics = pd.read_csv(
    "output/customer_metrics.csv"
)

rfm_customers = pd.read_csv(
    "output/rfm_customers.csv"
)

cohort_retention = pd.read_csv(
    "output/cohort_retention.csv"
)

cohort_counts = pd.read_csv(
    "output/cohort_customer_counts.csv"
)


print("All datasets loaded successfully!")


# ============================================================
# 2. Prepare Transaction Data
# ============================================================

print("\nPreparing transaction data...")

transactions.to_csv(
    "output/PowerBI_Transactions.csv",
    index=False
)


# ============================================================
# 3. Prepare Customer Metrics
# ============================================================

print("Preparing customer metrics...")

customer_metrics.to_csv(
    "output/PowerBI_CustomerMetrics.csv",
    index=False
)


# ============================================================
# 4. Prepare RFM Customer Data
# ============================================================

print("Preparing RFM customer data...")

rfm_customers.to_csv(
    "output/PowerBI_RFMCustomers.csv",
    index=False
)


# ============================================================
# 5. Prepare Cohort Retention Data
# ============================================================

print("Preparing cohort retention data...")

cohort_retention.to_csv(
    "output/PowerBI_CohortRetention.csv",
    index=False
)


# ============================================================
# 6. Prepare Cohort Customer Counts
# ============================================================

print("Preparing cohort customer counts...")

cohort_counts.to_csv(
    "output/PowerBI_CohortCustomerCounts.csv",
    index=False
)


# ============================================================
# 7. Display Dataset Sizes
# ============================================================

print("\n==========================================")
print("        POWER BI DATASET SIZES")
print("==========================================")

print(
    "Transactions:",
    transactions.shape
)

print(
    "Customer Metrics:",
    customer_metrics.shape
)

print(
    "RFM Customers:",
    rfm_customers.shape
)

print(
    "Cohort Retention:",
    cohort_retention.shape
)

print(
    "Cohort Customer Counts:",
    cohort_counts.shape
)


# ============================================================
# 8. Final Message
# ============================================================

print("\n==========================================")
print("      POWER BI EXPORT COMPLETED!")
print("==========================================")

print("""
The following files are ready for Power BI:

1. PowerBI_Transactions.csv
2. PowerBI_CustomerMetrics.csv
3. PowerBI_RFMCustomers.csv
4. PowerBI_CohortRetention.csv
5. PowerBI_CohortCustomerCounts.csv
""")