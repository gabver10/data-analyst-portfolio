"""
This script runs all 10 SQL queries and saves results to CSV files.
"""

import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Load environment variables
load_dotenv(r"C:\temp\.env")

# Directories
SQL_DIR = r"C:\temp\sql"
RESULTS_DIR = r"C:\temp\results"

# Ensure results directory exists
os.makedirs(RESULTS_DIR, exist_ok=True)

# Get database credentials
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME")

# Create connection string
connection_string = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

# Connect to database
try:
    engine = create_engine(connection_string)
    print("Successfully connected to the database!")
except Exception as e:
    print(f"Error connecting to database: {e}")
    exit(1)

# List of query files
query_files = [
    ("analysis_queries.sql", "london_neighborhood_analysis.csv"),
    ("query2_property_type_analysis.sql", "property_type_analysis.csv"),
    ("query3_seasonal_trends.sql", "seasonal_trends.csv"),
    ("query4_review_sentiment.sql", "review_sentiment.csv"),
    ("query5_superhost_analysis.sql", "superhost_analysis.csv"),
    ("query6_availability_patterns.sql", "availability_patterns.csv"),
    ("query7_stay_duration.sql", "stay_duration.csv"),
    ("query8_price_rating_correlation.sql", "price_rating_correlation.csv"),
    ("query9_top_bottom_neighborhoods.sql", "top_bottom_neighborhoods.csv"),
    ("query10_host_portfolio.sql", "host_portfolio.csv")
]

# Run each query and save results
for sql_file, csv_file in query_files:
    print(f"\nProcessing {sql_file}...")
    
    # Load SQL query
    sql_path = os.path.join(SQL_DIR, sql_file)
    try:
        with open(sql_path, 'r') as file:
            query = file.read()
        print(f"Loaded query from {sql_path}")
    except Exception as e:
        print(f"Error reading SQL file {sql_path}: {e}")
        continue
    
    # Execute query and save results
    try:
        # Run query
        results = pd.read_sql_query(query, engine)
        print(f"Query executed successfully, retrieved {len(results)} rows")
        
        # Save to CSV
        csv_path = os.path.join(RESULTS_DIR, csv_file)
        results.to_csv(csv_path, index=False)
        print(f"Results saved to {csv_path}")
        
    except Exception as e:
        print(f"Error executing query: {e}")

print("\nAll queries completed!")