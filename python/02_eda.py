import pandas as pd
import matplotlib.pyplot as plt


# ============================================================
# 1. Load cleaned dataset
# ============================================================

INPUT_FILE = r"C:\Users\likit\OneDrive\Documents\Customer-Cohort-Retention-Analysis\data\cleaned_retail_data.csv"

print("Loading cleaned dataset...")

df = pd.read_csv(
    INPUT_FILE,
    parse_dates=["InvoiceDate"]
)

print("Dataset loaded successfully!")

print("\nDataset shape:")
print(df.shape)


# ============================================================
# 2. Basic Business KPIs
# ============================================================

# Total Revenue
total_revenue = df["Revenue"].sum()

# Total Customers
total_customers = df["CustomerID"].nunique()

# Total Orders
total_orders = df["InvoiceNo"].nunique()

# Total Products
total_products = df["StockCode"].nunique()

# Total Quantity Sold
total_quantity = df["Quantity"].sum()

# Average Order Value
average_order_value = total_revenue / total_orders


print("\n==========================================")
print("           BUSINESS KPIs")
print("==========================================")

print(f"Total Revenue       : £{total_revenue:,.2f}")
print(f"Total Customers     : {total_customers:,}")
print(f"Total Orders        : {total_orders:,}")
print(f"Total Products      : {total_products:,}")
print(f"Total Quantity Sold : {total_quantity:,}")
print(f"Average Order Value : £{average_order_value:,.2f}")


# ============================================================
# 3. Monthly Revenue Analysis
# ============================================================

print("\nCalculating monthly revenue...")

monthly_revenue = (
    df.groupby("InvoiceMonth")["Revenue"]
      .sum()
      .reset_index()
)


print("\n==========================================")
print("          MONTHLY REVENUE")
print("==========================================")

print(monthly_revenue)


# ============================================================
# 4. Monthly Orders
# ============================================================

monthly_orders = (
    df.groupby("InvoiceMonth")["InvoiceNo"]
      .nunique()
      .reset_index(name="Orders")
)


print("\n==========================================")
print("           MONTHLY ORDERS")
print("==========================================")

print(monthly_orders)


# ============================================================
# 5. Monthly Customers
# ============================================================

monthly_customers = (
    df.groupby("InvoiceMonth")["CustomerID"]
      .nunique()
      .reset_index(name="Customers")
)


print("\n==========================================")
print("          MONTHLY CUSTOMERS")
print("==========================================")

print(monthly_customers)


# ============================================================
# 6. Combine Monthly Metrics
# ============================================================

monthly_analysis = monthly_revenue.merge(
    monthly_orders,
    on="InvoiceMonth"
)

monthly_analysis = monthly_analysis.merge(
    monthly_customers,
    on="InvoiceMonth"
)


print("\n==========================================")
print("        MONTHLY BUSINESS ANALYSIS")
print("==========================================")

print(monthly_analysis)


# ============================================================
# 7. Save Monthly Analysis
# ============================================================

monthly_analysis.to_csv(
    "output/monthly_business_analysis.csv",
    index=False
)

print("\nMonthly analysis saved successfully!")


# ============================================================
# 8. Monthly Revenue Chart
# ============================================================

plt.figure(figsize=(12, 6))

plt.plot(
    monthly_analysis["InvoiceMonth"],
    monthly_analysis["Revenue"],
    marker="o"
)

plt.title("Monthly Revenue Trend")

plt.xlabel("Month")

plt.ylabel("Revenue (£)")

plt.xticks(rotation=45)

plt.grid(True, alpha=0.3)

plt.tight_layout()

plt.show()


# ============================================================
# 9. Monthly Customer Chart
# ============================================================

plt.figure(figsize=(12, 6))

plt.plot(
    monthly_analysis["InvoiceMonth"],
    monthly_analysis["Customers"],
    marker="o"
)

plt.title("Monthly Customer Trend")

plt.xlabel("Month")

plt.ylabel("Number of Customers")

plt.xticks(rotation=45)

plt.grid(True, alpha=0.3)

plt.tight_layout()

plt.show()


# ============================================================
# 10. Top 10 Products by Revenue
# ============================================================

top_products = (
    df.groupby("Description")["Revenue"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)


print("\n==========================================")
print("       TOP 10 PRODUCTS BY REVENUE")
print("==========================================")

print(top_products)


# ============================================================
# 11. Top 10 Countries by Revenue
# ============================================================

top_countries = (
    df.groupby("Country")["Revenue"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)


print("\n==========================================")
print("       TOP 10 COUNTRIES BY REVENUE")
print("==========================================")

print(top_countries)


# ============================================================
# 12. Final Message
# ============================================================

print("\n==========================================")
print("      EDA COMPLETED SUCCESSFULLY!")
print("==========================================")

print("Created:")
print("1. Monthly Revenue Analysis")
print("2. Monthly Customer Analysis")
print("3. Monthly Order Analysis")
print("4. Top Products Analysis")
print("5. Country Revenue Analysis")