"""
This script generates visualizations for all query results.
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Set paths
RESULTS_DIR = r"C:\temp\results"
VIZ_DIR = r"C:\temp\visualizations"

# Ensure visualizations directory exists
os.makedirs(VIZ_DIR, exist_ok=True)

# Set styling for all plots
sns.set_style("whitegrid")
plt.rcParams.update({'font.size': 12})

def save_plot(filename):
    """Helper function to save plot with consistent formatting"""
    path = os.path.join(VIZ_DIR, filename)
    plt.tight_layout()
    plt.savefig(path, dpi=300)
    plt.close()
    print(f"Created visualization: {path}")

# 1. Neighborhood Analysis (already done in previous script)

# 2. Property Type Analysis
try:
    df = pd.read_csv(os.path.join(RESULTS_DIR, "property_type_analysis.csv"))
    
    # Get top 10 property types by listing count
    top_properties = df.sort_values('num_listings', ascending=False).head(10)
    
    plt.figure(figsize=(14, 8))
    ax = sns.barplot(x='property_type', y='avg_price', data=top_properties)
    
    # Add listing count as text on each bar
    for i, p in enumerate(ax.patches):
        ax.annotate(f"n={top_properties.iloc[i]['num_listings']}",
                   (p.get_x() + p.get_width() / 2., p.get_height() + 5),
                   ha='center', va='bottom', fontsize=10)
    
    plt.title('Average Price by Property Type (Top 10)', fontsize=16)
    plt.xlabel('Property Type', fontsize=14)
    plt.ylabel('Average Price (£)', fontsize=14)
    plt.xticks(rotation=45, ha='right')
    save_plot('property_type_analysis.png')
except Exception as e:
    print(f"Error creating property type visualization: {e}")

# 3. Seasonal Trends
try:
    df = pd.read_csv(os.path.join(RESULTS_DIR, "seasonal_trends.csv"))
    
    # Sort by month number
    df['month'] = pd.to_numeric(df['month'])
    df = df.sort_values('month')
    
    fig, ax1 = plt.figure(figsize=(14, 8)), plt.gca()
    
    # Plot average price
    ax1.set_xlabel('Month', fontsize=14)
    ax1.set_ylabel('Average Price (£)', fontsize=14, color='tab:blue')
    ax1.plot(df['month_name'], df['avg_price'], marker='o', color='tab:blue', linewidth=3)
    ax1.tick_params(axis='y', labelcolor='tab:blue')
    
    # Create second y-axis for availability
    ax2 = ax1.twinx()
    ax2.set_ylabel('Availability Rate (%)', fontsize=14, color='tab:red')
    ax2.plot(df['month_name'], df['availability_rate'], marker='s', color='tab:red', linewidth=3)
    ax2.tick_params(axis='y', labelcolor='tab:red')
    
    plt.title('Seasonal Pricing and Availability Trends', fontsize=16)
    plt.xticks(rotation=45)
    save_plot('seasonal_trends.png')
except Exception as e:
    print(f"Error creating seasonal trends visualization: {e}")

# 4. Review Sentiment Analysis
try:
    df = pd.read_csv(os.path.join(RESULTS_DIR, "review_sentiment.csv"))
    
    # Get top 15 neighborhoods by positive-to-negative ratio
    top_neighborhoods = df.sort_values('positive_to_negative_ratio', ascending=False).head(15)
    
    plt.figure(figsize=(14, 8))
    
    # Create a horizontal bar chart
    bars = plt.barh(y=top_neighborhoods['neighbourhood'], 
              width=top_neighborhoods['positive_to_negative_ratio'],
              color=sns.color_palette("viridis", 15))
    
    # Add count on bars
    for bar in bars:
        width = bar.get_width()
        plt.text(width + 0.3, bar.get_y() + bar.get_height()/2, 
                f'{width:.1f}x', ha='left', va='center')
    
    plt.title('Top 15 Neighborhoods by Positive-to-Negative Review Ratio', fontsize=16)
    plt.xlabel('Ratio of Positive to Negative Mentions', fontsize=14)
    plt.ylabel('Neighborhood', fontsize=14)
    save_plot('review_sentiment.png')
except Exception as e:
    print(f"Error creating review sentiment visualization: {e}")

# 5. Superhost Analysis
try:
    df = pd.read_csv(os.path.join(RESULTS_DIR, "superhost_analysis.csv"))
    
    # Create metrics to compare
    metrics = ['avg_price', 'avg_rating', 'avg_reviews_per_month', 'instant_bookable_percent']
    metric_names = ['Average Price (£)', 'Average Rating', 'Monthly Reviews', 'Instant Booking (%)']
    
    plt.figure(figsize=(14, 10))
    
    # Create a 2x2 subplot
    for i, (metric, name) in enumerate(zip(metrics, metric_names)):
        plt.subplot(2, 2, i+1)
        sns.barplot(x='host_type', y=metric, data=df)
        plt.title(name, fontsize=14)
        plt.xlabel('')
        plt.ylabel(name, fontsize=12)
    
    plt.suptitle('Superhost vs Regular Host Performance', fontsize=16)
    save_plot('superhost_analysis.png')
except Exception as e:
    print(f"Error creating superhost analysis visualization: {e}")

# 6. Availability Patterns
try:
    df = pd.read_csv(os.path.join(RESULTS_DIR, "availability_patterns.csv"))
    
    # Get top 10 most and least available neighborhoods
    most_available = df.nlargest(10, 'avg_availability_percent')
    least_available = df.nsmallest(10, 'avg_availability_percent')
    
    # Combine them with a label column
    most_available['availability_group'] = 'Most Available'
    least_available['availability_group'] = 'Least Available'
    plot_df = pd.concat([most_available, least_available])
    
    plt.figure(figsize=(14, 10))
    sns.barplot(x='neighbourhood', y='avg_availability_percent', 
                hue='availability_group', data=plot_df, palette=['#5cb85c', '#d9534f'])
    
    plt.title('Neighborhoods with Highest and Lowest Availability (Next 90 Days)', fontsize=16)
    plt.xlabel('Neighborhood', fontsize=14)
    plt.ylabel('Average Availability (%)', fontsize=14)
    plt.xticks(rotation=90)
    plt.legend(title='')
    save_plot('availability_patterns.png')
except Exception as e:
    print(f"Error creating availability patterns visualization: {e}")

# 7. Stay Duration Analysis
try:
    df = pd.read_csv(os.path.join(RESULTS_DIR, "stay_duration.csv"))
    
    # Get top 15 neighborhoods by one-night percentage
    top_one_night = df.nlargest(15, 'one_night_percent')
    
    plt.figure(figsize=(14, 8))
    
    # Create stacked bar chart of stay types
    stay_types = ['one_night_stays', 'short_stays', 'medium_stays', 'weekly_plus_stays']
    labels = ['1 Night', '2-3 Nights', '4-6 Nights', '7+ Nights']
    
    # Convert to percentages
    for col in stay_types:
        top_one_night[f'{col}_pct'] = top_one_night[col] / top_one_night['num_listings'] * 100
    
    # Create a stacked bar chart
    ax = top_one_night.plot.barh(x='neighbourhood', 
                          y=[f'{col}_pct' for col in stay_types],
                          stacked=True, figsize=(14, 10), 
                          color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'])
    
    plt.title('Stay Duration Distribution in Top One-Night Stay Neighborhoods', fontsize=16)
    plt.xlabel('Percentage of Listings', fontsize=14)
    plt.ylabel('Neighborhood', fontsize=14)
    plt.legend(labels, title='Minimum Stay')
    
    # Add the average minimum nights as text
    for i, row in enumerate(top_one_night.itertuples()):
        plt.text(101, i, f'Avg Min: {row.avg_minimum_nights:.1f} nights', 
                 ha='left', va='center', fontsize=10)
    
    plt.xlim(0, 130)  # Make room for the text
    save_plot('stay_duration.png')
except Exception as e:
    print(f"Error creating stay duration visualization: {e}")

# 8. Price Rating Correlation
try:
    df = pd.read_csv(os.path.join(RESULTS_DIR, "price_rating_correlation.csv"))
    
    plt.figure(figsize=(14, 8))
    
    # Melt the dataframe to get all rating types in one column
    rating_cols = ['overall_rating', 'cleanliness_rating', 'location_rating', 'value_rating']
    rating_names = ['Overall', 'Cleanliness', 'Location', 'Value']
    
    melted = pd.melt(df, id_vars=['price_category', 'num_listings'], 
                     value_vars=rating_cols, 
                     var_name='rating_type', value_name='rating')
    
    # Map rating type to readable names
    mapping = dict(zip(rating_cols, rating_names))
    melted['rating_type'] = melted['rating_type'].map(mapping)
    
    # Sort by price category (maintaining original price order)
    price_order = df['price_category'].tolist()
    melted['price_category'] = pd.Categorical(melted['price_category'], categories=price_order, ordered=True)
    melted = melted.sort_values('price_category')
    
    # Create line plot
    sns.lineplot(x='price_category', y='rating', hue='rating_type', 
                 data=melted, marker='o', markersize=10)
    # Fix the x-axis labels by replacing 'Â£' with '£'
    current_labels = plt.gca().get_xticklabels()
    new_labels = [label.get_text().replace('Â£', '£') for label in current_labels]
    plt.gca().set_xticklabels(new_labels)
    
    plt.title('Ratings by Price Category', fontsize=16)
    plt.xlabel('Price Category', fontsize=14)
    plt.ylabel('Average Rating', fontsize=14)
    plt.ylim(4.3, 5.0)  # Zoom in to see differences
    plt.legend(title='Rating Type')
    save_plot('price_rating_correlation.png')
except Exception as e:
    print(f"Error creating price-rating correlation visualization: {e}")

# 9. Top vs Bottom Neighborhoods
try:
    df = pd.read_csv(os.path.join(RESULTS_DIR, "top_bottom_neighborhoods.csv"))
    
    plt.figure(figsize=(14, 8))
    
    # Set color palette based on rating tier
    palette = {'Top 5': '#5cb85c', 'Bottom 5': '#d9534f'}
    
    # Create scatter plot
    ax = sns.scatterplot(x='avg_price', y='avg_rating', 
                     hue='rating_tier', size='num_listings',
                     sizes=(100, 500), alpha=0.7, palette=palette,
                     data=df)
    
    # Add neighborhood labels
    for _, row in df.iterrows():
        plt.text(row['avg_price']+5, row['avg_rating'], row['neighbourhood'], 
                 fontsize=11, alpha=0.8)
    
    plt.title('Top 5 vs Bottom 5 Rated Neighborhoods', fontsize=16)
    plt.xlabel('Average Price (£)', fontsize=14)
    plt.ylabel('Average Rating', fontsize=14)
    plt.legend(title='Rating Tier')
    save_plot('top_bottom_neighborhoods.png')
except Exception as e:
    print(f"Error creating top vs bottom neighborhoods visualization: {e}")

# 10. Host Portfolio Analysis
try:
    df = pd.read_csv(os.path.join(RESULTS_DIR, "host_portfolio.csv"))
    
    plt.figure(figsize=(12, 10))
    
    # Create a figure with 4 subplots
    fig, axs = plt.subplots(2, 2, figsize=(14, 10))
    
    # Plot 1: Host distribution
    axs[0, 0].pie(df['num_hosts'], labels=df['host_category'], autopct='%1.1f%%',
                  colors=sns.color_palette("viridis", len(df)))
    axs[0, 0].set_title('Distribution of Hosts by Portfolio Size')
    
    # Plot 2: Listings distribution
    axs[0, 1].pie(df['total_listings'], labels=df['host_category'], autopct='%1.1f%%',
                  colors=sns.color_palette("viridis", len(df)))
    axs[0, 1].set_title('Distribution of Listings by Host Portfolio Size')
    
    # Plot 3: Average price by portfolio size
    sns.barplot(x='host_category', y='avg_price', data=df, ax=axs[1, 0],
                palette=sns.color_palette("viridis", len(df)))
    axs[1, 0].set_title('Average Price by Host Portfolio Size')
    axs[1, 0].set_xlabel('Host Portfolio Size')
    axs[1, 0].set_ylabel('Average Price (£)')
    
    # Plot 4: Superhost percentage by portfolio size
    sns.barplot(x='host_category', y='superhost_percent', data=df, ax=axs[1, 1],
                palette=sns.color_palette("viridis", len(df)))
    axs[1, 1].set_title('Superhost Percentage by Portfolio Size')
    axs[1, 1].set_xlabel('Host Portfolio Size')
    axs[1, 1].set_ylabel('Superhost Percentage (%)')
    
    plt.suptitle('Host Portfolio Size Analysis', fontsize=16)
    plt.tight_layout()
    save_plot('host_portfolio.png')
except Exception as e:
    print(f"Error creating host portfolio visualization: {e}")

print("\nAll visualizations completed!")