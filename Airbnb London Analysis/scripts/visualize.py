"""
This script generates visualizations from the SQL query results
for the London Airbnb neighborhood analysis.
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Fixed paths
RESULTS_FILE = r"C:\temp\results\london_neighborhood_analysis.csv"
VIZ_DIR = r"C:\temp\visualizations"

# Ensure visualizations directory exists
os.makedirs(VIZ_DIR, exist_ok=True)

# Load results from CSV
try:
    neighborhoods = pd.read_csv(RESULTS_FILE)
    print(f"Loaded data with {len(neighborhoods)} neighborhoods")
except Exception as e:
    print(f"Error loading CSV data: {e}")
    exit(1)

# Set styling for plots
sns.set_style("whitegrid")
plt.rcParams.update({'font.size': 12})

# Create visualizations

# 1. Top 10 neighborhoods by listing count
try:
    plt.figure(figsize=(12, 8))
    top_10 = neighborhoods.sort_values('num_listings', ascending=False).head(10)
    ax = sns.barplot(x='neighbourhood', y='num_listings', data=top_10)
    ax.set_title('Top 10 London Neighborhoods by Number of Airbnb Listings', fontsize=16)
    ax.set_xlabel('Neighborhood', fontsize=14)
    ax.set_ylabel('Number of Listings', fontsize=14)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    viz_path = os.path.join(VIZ_DIR, 'top_neighborhoods_by_listings.png')
    plt.savefig(viz_path)
    print(f"Created visualization: {viz_path}")
except Exception as e:
    print(f"Error creating listing count visualization: {e}")

# 2. Price vs. Rating scatterplot
try:
    plt.figure(figsize=(14, 10))
    scatter = sns.scatterplot(
        x='avg_listing_price', 
        y='avg_rating',
        size='num_listings',
        sizes=(50, 500),
        alpha=0.7,
        data=neighborhoods
    )
    
    # Add labels for each neighborhood
    for i, row in neighborhoods.iterrows():
        plt.text(row['avg_listing_price']+5, row['avg_rating'], row['neighbourhood'], 
                fontsize=9, alpha=0.8)
    
    plt.title('Price vs. Rating by London Neighborhood', fontsize=16)
    plt.xlabel('Average Listing Price (£)', fontsize=14)
    plt.ylabel('Average Rating', fontsize=14)
    plt.tight_layout()
    viz_path = os.path.join(VIZ_DIR, 'price_vs_rating.png')
    plt.savefig(viz_path)
    print(f"Created visualization: {viz_path}")
except Exception as e:
    print(f"Error creating price vs rating visualization: {e}")

# 3. Superhost percentage by neighborhood (top 10)
try:
    plt.figure(figsize=(12, 8))
    top_superhost = neighborhoods.sort_values('superhost_percentage', ascending=False).head(10)
    ax = sns.barplot(x='neighbourhood', y='superhost_percentage', data=top_superhost)
    ax.set_title('Top 10 London Neighborhoods by Superhost Percentage', fontsize=16)
    ax.set_xlabel('Neighborhood', fontsize=14)
    ax.set_ylabel('Superhost Percentage (%)', fontsize=14)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    viz_path = os.path.join(VIZ_DIR, 'top_neighborhoods_by_superhosts.png')
    plt.savefig(viz_path)
    print(f"Created visualization: {viz_path}")
except Exception as e:
    print(f"Error creating superhost visualization: {e}")

print("\nAll visualizations completed!")