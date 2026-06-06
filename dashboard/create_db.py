import pandas as pd
import sqlite3
import os

os.makedirs("database", exist_ok=True)

df = pd.read_csv("data/sales_data.csv")

conn = sqlite3.connect("database/sales.db")

df.to_sql("sales", conn, if_exists="replace", index=False)

conn.close()

print("Database Created Successfully!")