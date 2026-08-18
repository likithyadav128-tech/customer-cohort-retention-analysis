import pandas as pd


# ============================================================
# 1. Load Customer Metrics
# ============================================================

INPUT_FILE = r"C:\Users\likit\OneDrive\Documents\Customer-Cohort-Retention-Analysis\data\cleaned_retail_data.csv"
print("Loading cleaned dataset...")

print("Loading customer metrics...")

df = pd.read_csv(INPUT_FILE)

print("Dataset loaded successfully!")

print("\nNumber of customers:", len(df))


# ============================================================
# 2. Check Customer Metrics
# ============================================================

print("\n==========================================")
print("       CUSTOMER METRICS")
print("==========================================")

print(
    df[[
            "CustomerID",
            "Recency",
            "Frequency",
            "Monetary"
        ]
    ].head(10)
)


# ============================================================
# 3. Calculate RFM Scores
# ============================================================

# R = Recency
# Lower recency is better.
#
# F = Frequency
# Higher frequency is better.
#
# M = Monetary
# Higher spending is better.


# -------------------------
# Recency Score
# -------------------------

df["R_Score"] = pd.qcut(
    df["Recency"].rank(method="first"),
    4,
    labels=[4, 3, 2, 1]
).astype(int)


# -------------------------
# Frequency Score
# -------------------------

df["F_Score"] = pd.qcut(
    df["Frequency"].rank(method="first"),
    4,
    labels=[1, 2, 3, 4]
).astype(int)


# -------------------------
# Monetary Score
# -------------------------

df["M_Score"] = pd.qcut(
    df["Monetary"].rank(method="first"),
    4,
    labels=[1, 2, 3, 4]
).astype(int)


# ============================================================
# 4. Create RFM Score
# ============================================================

df["RFM_Score"] = (
    df["R_Score"].astype(str)
    + df["F_Score"].astype(str)
    + df["M_Score"].astype(str)
)


# ============================================================
# 5. Create Customer Segments
# ============================================================

def customer_segment(row):

    r = row["R_Score"]
    f = row["F_Score"]
    m = row["M_Score"]

    # High recency + high frequency + high monetary
    if r >= 3 and f >= 3 and m >= 3:
        return "Champions"

    # Recent and frequent customers
    elif r >= 3 and f >= 2:
        return "Loyal Customers"

    # Recent customers
    elif r >= 3:
        return "Potential Loyalists"

    # Older customers but high frequency
    elif r <= 2 and f >= 3:
        return "At Risk"

    # Low engagement customers
    else:
        return "Lost Customers"


df["Segment"] = df.apply(
    customer_segment,
    axis=1
)


# ============================================================
# 6. Display RFM Results
# ============================================================

print("\n==========================================")
print("             RFM RESULTS")
print("==========================================")

print(
    df[
        [
            "CustomerID",
            "Recency",
            "Frequency",
            "Monetary",
            "R_Score",
            "F_Score",
            "M_Score",
            "RFM_Score",
            "Segment"
        ]
    ].head(20)
)


# ============================================================
# 7. Count Customers by Segment
# ============================================================

segment_counts = (
    df["Segment"]
    .value_counts()
)


print("\n==========================================")
print("       CUSTOMERS BY SEGMENT")
print("==========================================")

print(segment_counts)


# ============================================================
# 8. Revenue by Segment
# ============================================================

segment_revenue = (
    df.groupby("Segment")["Revenue"]
      .sum()
      .sort_values(
          ascending=False
      )
)


print("\n==========================================")
print("          REVENUE BY SEGMENT")
print("==========================================")

print(segment_revenue)


# ============================================================
# 9. Average Revenue by Segment
# ============================================================

average_revenue = (
    df.groupby("Segment")["Revenue"]
      .mean()
      .sort_values(
          ascending=False
      )
)


print("\n==========================================")
print("       AVERAGE REVENUE BY SEGMENT")
print("==========================================")

print(
    average_revenue
)


# ============================================================
# 10. Save RFM Dataset
# ============================================================

OUTPUT_FILE = (
    "output/rfm_customers.csv"
)

df.to_csv(
    OUTPUT_FILE,
    index=False
)


print("\n==========================================")
print("       RFM ANALYSIS COMPLETED")
print("==========================================")

print(
    f"Saved file: {OUTPUT_FILE}"
)