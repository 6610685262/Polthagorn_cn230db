import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect('gundam_models.db')

print("0 : GunplaKits per grade.")
print("1 : Each grade's average price.")
print("2 : GunplaKits per year.")
print("3 : Top 10 Media with most Gunpla Product.")
print("4 : ALL.")
print("Any other key : End Program.")
command = input("Please Select mode: ")

if (command == "0") or (command == "4"):
    query = """
    SELECT Grade, COUNT(*) as Kit_per_grade
    FROM models
    GROUP BY Grade
    ORDER BY Kit_per_grade DESC;
    """
    df = pd.read_sql_query(query, conn)
    print(df)

if (command == "1") or (command == "4"):
    query = """
    SELECT Grade, ROUND(AVG(Recommend_Price), 0) AS avg_price
    FROM models
    GROUP BY Grade
    ORDER BY avg_price DESC;
    """
    df = pd.read_sql_query(query, conn)
    print(df)
    print("""Price currency is "Yen" and no 10% tax included. """)

if (command == "2") or (command == "4"):
    query = """
    SELECT Release_Year,
    COUNT(*)                AS kits_released
    FROM models
    GROUP BY Release_Year
    ORDER BY kits_released DESC;
    """
    df = pd.read_sql_query(query, conn)
    print(df)

if (command == "3") or (command == "4"):
    query = """
    SELECT Media,
    COUNT(*) AS count_by_series
    FROM models
    GROUP BY Media
    ORDER BY count_by_series DESC
    LIMIT 10;
    """
    df = pd.read_sql_query(query, conn)
    print(df)

print("Program Ended.")