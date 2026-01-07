import pandas as pd

# Load raw sales data
df = pd.read_csv("sales_data.csv")

# Remove duplicate records
df = df.drop_duplicates()

# Keep only valid rows needed for reporting
df = df.dropna(subset=["InvoiceNo", "Quantity", "UnitPrice", "Country", "InvoiceDate"])

# Convert data types
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"], errors="coerce")
df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
df["UnitPrice"] = pd.to_numeric(df["UnitPrice"], errors="coerce")

df = df.dropna(subset=["InvoiceDate", "Quantity", "UnitPrice"])

# Remove returns / invalid transactions
df = df[(df["Quantity"] > 0) & (df["UnitPrice"] > 0)]

# Create revenue column (used in Power BI)
df["Revenue"] = df["Quantity"] * df["UnitPrice"]

# Add time attributes for reporting
df["Year"] = df["InvoiceDate"].dt.year
df["Month"] = df["InvoiceDate"].dt.month

# Export cleaned dataset for SQL / Power BI
df.to_csv("cleaned_sales_data.csv", index=False)
