#install#pip install pandas
#install#pip install openpyxl

import pandas as pd
import sqlite3

# Load your Excel file
excel_file = "gunpla.xlsx"
sheet = "Sheet1"  # Change if your shee t has a different name

# Read the Excel file
df = pd.read_excel(excel_file, sheet_name=sheet)

# Clean the 'Recommend_Price' column (remove commas and convert to integers)
df["Recommend_Price"] = df["Recommend_Price"].astype(str).str.replace(",", "")
df["Recommend_Price"] = pd.to_numeric(df["Recommend_Price"], errors="coerce")

# Connect to SQLite database (or create it)
conn = sqlite3.connect("gundam_models.db")

# Save DataFrame to SQLite table named 'models'
df.to_sql("models", conn, if_exists="replace", index=False)

# Verify by printing a few rows
print("Sample rows inserted into database:")
for row in conn.execute("SELECT * FROM models LIMIT 5"):
    print(row)

# Close connection
conn.commit()
conn.close()
