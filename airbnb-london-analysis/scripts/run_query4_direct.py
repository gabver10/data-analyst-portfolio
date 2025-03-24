"""
Direct PostgreSQL connection to run Query 4
"""

import os
import pandas as pd
import psycopg2
from dotenv import load_dotenv

# Load environment variables
load_dotenv(r"C:\temp\.env")

# File paths
SQL_FILE = r"C:\temp\sql\query4_review_sentiment.sql"
RESULTS_FILE = r"C:\temp\results\review_sentiment.csv"

# Ensure results directory exists
os.makedirs(os.path.dirname(RESULTS_FILE), exist_ok=True)

# Get database credentials
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME")

# Read the SQL query
with open(SQL_FILE, 'r') as file:
    query = file.read()
print(f"Successfully loaded query from {SQL_FILE}")

# Connect directly with psycopg2
try:
    # Create connection
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    print("Successfully connected to database")
    
    # Create a cursor
    cursor = conn.cursor()
    
    # Execute the query
    print("Executing query...")
    cursor.execute(query)
    
    # Fetch the results
    rows = cursor.fetchall()
    print(f"Query returned {len(rows)} rows")
    
    # Get column names
    column_names = [desc[0] for desc in cursor.description]
    print(f"Columns: {column_names}")
    
    # Create a DataFrame
    df = pd.DataFrame(rows, columns=column_names)
    
    # Save to CSV
    df.to_csv(RESULTS_FILE, index=False)
    print(f"Results saved to {RESULTS_FILE}")
    
    # Close cursor and connection
    cursor.close()
    conn.close()
    
except Exception as e:
    print(f"Error: {e}")