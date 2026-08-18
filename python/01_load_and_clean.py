import pandas as pd

# ============================================================
# 1. File paths
# ============================================================

INPUT_FILE = r"C:\Users\likit\OneDrive\Documents\Customer-Cohort-Retention-Analysis\data\Online Retail.xlsx"
OUTPUT_FILE = r"C:\Users\likit\OneDrive\Documents\Customer-Cohort-Retention-Analysis\data\cleaned_retail_data.csv"


# ============================================================
# 2. Load the dataset
# ============================================================

print("Loading dataset...")

df = pd.read_excel(INPUT_FILE)

print("\nOriginal dataset shape:")
print(df.shape)

print("\nColumn names:")
print(df.columns.tolist())


# ============================================================
# 3. Display first few records
# ============================================================

print("\nFirst 5 rows:")
print(df.head())


# ============================================================
# 4. Check missing values
# ============================================================

print("\nMissing values before cleaning:")
print(df.isnull().sum())


# ============================================================
# 5. Convert data types
# ============================================================

# Invoice number should be treated as text
df["InvoiceNo"] = df["InvoiceNo"].astype(str)

# Convert InvoiceDate to datetime
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])


# ============================================================
# 6. Remove records without CustomerID
# ============================================================

print("\nRemoving records with missing CustomerID...")

df = df.dropna(subset=["CustomerID"])


# ============================================================
# 7. Remove cancelled transactions
# ============================================================

# In this dataset, invoices beginning with "C"
# represent cancelled transactions.

print("Removing cancelled transactions...")

df = df[~df["InvoiceNo"].str.startswith("C")]


# ============================================================
# 8. Remove invalid quantities
# ============================================================

print("Removing invalid quantities...")

df = df[df["Quantity"] > 0]


# ============================================================
# 9. Remove invalid prices
# ============================================================

print("Removing invalid prices...")

df = df[df["UnitPrice"] > 0]


# ============================================================
# 10. Convert CustomerID to integer
# ============================================================

df["CustomerID"] = df["CustomerID"].astype(int)


# ============================================================
# 11. Create Revenue column
# ============================================================

df["Revenue"] = df["Quantity"] * df["UnitPrice"]


# ============================================================
# 12. Create Invoice Month
# ============================================================

df["InvoiceMonth"] = (
    df["InvoiceDate"]
    .dt.to_period("M")
    .astype(str)
)


# ============================================================
# 13. Check cleaned dataset
# ============================================================

print("\nCleaned dataset shape:")
print(df.shape)

print("\nCleaned dataset:")
print(df.head())

print("\nMissing values after cleaning:")
print(df.isnull().sum())


# ============================================================
# 14. Basic statistics
# ============================================================

print("\nTotal Revenue:")
print(f"£{df['Revenue'].sum():,.2f}")

print("\nUnique Customers:")
print(df["CustomerID"].nunique())

print("\nUnique Orders:")
print(df["InvoiceNo"].nunique())


# ============================================================
# 15. Save cleaned dataset
# ============================================================

df.to_csv(
    OUTPUT_FILE,
    index=False
)

print("\n========================================")
print("Data cleaning completed successfully!")
print("========================================")
print(f"Cleaned file saved to: {OUTPUT_FILE}")