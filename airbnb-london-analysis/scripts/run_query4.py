"""
Script to run only Query 4 (Review Sentiment Analysis) and save results
"""

import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Set up logging
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

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

# Create connection string
connection_string = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

# Print connection details (without password)
logger.info(f"Connecting to: postgresql://{DB_USER}:***@{DB_HOST}:{DB_PORT}/{DB_NAME}")

# Read the SQL query
try:
    with open(SQL_FILE, 'r') as file:
        query = file.read()
    logger.info(f"Successfully loaded query from {SQL_FILE}")
    logger.info(f"Query length: {len(query)} characters")
except Exception as e:
    logger.error(f"Error reading SQL file: {e}")
    exit(1)

# Connect to database
try:
    engine = create_engine(connection_string)
    logger.info("Successfully connected to database")
    
    # Test connection
    with engine.connect() as conn:
        logger.info("Connection test successful")
except Exception as e:
    logger.error(f"Error connecting to database: {e}")
    exit(1)

# Execute query and save results
try:
    # First check what data we're working with - how many neighborhoods have reviews
    check_query = """
    SELECT COUNT(DISTINCT l.neighbourhood_cleansed) 
    FROM listings l
    JOIN reviews r ON l.listing_id = r.listing_id
    """
    
    neighborhoods_count = pd.read_sql_query(check_query, engine).iloc[0, 0]
    logger.info(f"Number of neighborhoods with reviews: {neighborhoods_count}")
    
    # Check review counts by neighborhood
    review_counts_query = """
    SELECT 
        l.neighbourhood_cleansed,
        COUNT(r.id) AS review_count
    FROM 
        listings l
    JOIN 
        reviews r ON l.listing_id = r.listing_id
    GROUP BY 
        l.neighbourhood_cleansed
    ORDER BY 
        review_count DESC
    LIMIT 10
    """
    
    review_counts = pd.read_sql_query(review_counts_query, engine)
    logger.info(f"Top neighborhoods by review count:")
    for _, row in review_counts.iterrows():
        logger.info(f"  {row['neighbourhood_cleansed']}: {row['review_count']} reviews")
    
    # Now execute the actual query
    logger.info("Executing main query...")
    results = pd.read_sql_query(query, engine)
    
    # Check results
    row_count = len(results)
    logger.info(f"Query executed successfully, retrieved {row_count} rows")
    
    if row_count > 0:
        logger.info("Sample of first row:")
        logger.info(results.iloc[0])
        
        # Save to CSV
        results.to_csv(RESULTS_FILE, index=False)
        logger.info(f"Results saved to {RESULTS_FILE}")
    else:
        logger.warning("Query returned 0 rows!")
        
        # Let's modify the query to lower the threshold and see if that helps
        modified_query = query.replace("WHERE \n    review_count > 100", "WHERE \n    review_count > 0")
        logger.info("Trying modified query with lower threshold...")
        
        modified_results = pd.read_sql_query(modified_query, engine)
        mod_row_count = len(modified_results)
        logger.info(f"Modified query returned {mod_row_count} rows")
        
        if mod_row_count > 0:
            logger.info("First row from modified query:")
            logger.info(modified_results.iloc[0])
            
            # Save modified results
            modified_file = RESULTS_FILE.replace('.csv', '_modified.csv')
            modified_results.to_csv(modified_file, index=False)
            logger.info(f"Modified results saved to {modified_file}")
            
            # Now let's save the original file too, even if empty
            results.to_csv(RESULTS_FILE, index=False)
            logger.info(f"Empty original results saved to {RESULTS_FILE}")
    
except Exception as e:
    logger.error(f"Error executing query: {e}")
    # Print the actual query for debugging
    logger.error(f"Query that failed:\n{query[:500]}...")  # First 500 chars