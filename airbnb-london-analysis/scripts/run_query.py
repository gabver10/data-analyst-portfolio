"""
This script securely connects to PostgreSQL and runs the neighborhood analysis query,
saving the results to a CSV file.
"""

import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Load environment variables from .env file (with credentials)
load_dotenv(r"C:\temp\.env")

# Fixed paths
SQL_FILE = r"C:\temp\sql\analysis_queries.sql"
RESULTS_FILE = r"C:\temp\results\london_neighborhood_analysis.csv"

# Ensure results directory exists
os.makedirs(r"C:\temp\results", exist_ok=True)

# Get database credentials from environment variables
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME")

# Create connection string
connection_string = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

# Create SQLAlchemy engine
try:
    engine = create_engine(connection_string)
    print("Successfully connected to the database!")
except Exception as e:
    print(f"Error connecting to database: {e}")
    exit(1)

# Load query from SQL file
try:
    with open(SQL_FILE, 'r') as file:
        query = file.read()
    print(f"Successfully loaded SQL query from {SQL_FILE}")
except Exception as e:
    print(f"Error reading SQL file: {e}")
    exit(1)

# Execute query and save results
try:
    # Run query
    london_neighborhoods = pd.read_sql_query(query, engine)
    print(f"Query executed successfully, retrieved {len(london_neighborhoods)} rows")
    
    # Save to CSV
    london_neighborhoods.to_csv(RESULTS_FILE, index=False)
    print(f"Results saved to {RESULTS_FILE}")
    
    # Display sample of results
    print("\nSample results:")
    print(london_neighborhoods.head())
    
except Exception as e:
    print(f"Error executing query: {e}")