import pandas as pd

# Load the dataset
df = pd.read_csv('property.csv')

# 1. Basic Info
info = {
    "rows": df.shape[0],
    "columns": df.shape[1],
    "column_names": df.columns.tolist()
}

# 2. Missing Values
missing_values = df.isnull().sum()
missing_values = missing_values[missing_values > 0].to_dict()

# 3. Statistical Summary
stats = df.describe().to_dict()

# Print the summary in a readable format
print("--- DATASET SUMMARY ---")
print(f"Total Rows: {info['rows']}")
print(f"Total Columns: {info['columns']}")
print("\n--- COLUMNS ---")
print(info['column_names'])
print("\n--- MISSING VALUES ---")
for col, count in missing_values.items():
    print(f"{col}: {count}")

print("\n--- BASIC STATISTICS (Numerical) ---")
print(df.describe())
