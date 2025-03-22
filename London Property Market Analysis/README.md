# London Property Market Analysis (2024)

## Project Overview
This project analyzes the London property market using official 2024 transaction data from GOV.UK. The analysis explores price distributions, property types, borough comparisons, and statistical testing to identify significant patterns in London's dynamic real estate market.

## Data Source
- Data obtained from the UK Government's official property transaction database for 2024
- Original dataset filtered and cleaned to focus specifically on London properties
- Final dataset contains 44,584 property transactions after cleaning

## Dataset Features
The cleaned dataset includes the following key variables:
- `transaction_id`: Unique identifier for each property transaction
- `price`: Sale price in GBP
- `date_of_transfer`: Date when the property was sold
- `postcode`: Property postcode
- `property_type`: Type of property (Flat/Apartment, Terraced, Semi-Detached, Detached, Other)
- `duration`: Tenure type (Freehold/Leasehold)
- `district`: London borough/district
- `county`: Greater London
- Additional fields including street, town_city, old_new, paon, and category_type

## Tools & Technologies Used
- **Python**: Primary programming language for analysis
- **Pandas**: Data manipulation and cleaning
- **Matplotlib/Seaborn**: Data visualization
- **Jupyter Notebook**: Interactive development and presentation
- **Statistical testing**: ANOVA and Mann-Whitney U tests

## Key Findings

### Price Distribution
- **Average Price**: £775,687.04
- **Median Price**: £560,000.00
- **Price Range**: £10,000 to £10,000,000 (after cleaning outliers)
- **High-Value Properties**: 17.6% of properties (7,839) sold for over £1 million

### Property Types
- **Most Common**: Flat/Apartment (27,476 properties)
- **Distribution**: 
  - Flat/Apartment: 61.6%
  - Terraced: 25.9%
  - Semi-Detached: 7.1% 
  - Detached: 1.8%
  - Other: 4.2%
- **Statistical Significance**: ANOVA testing confirmed significant price differences between property types (F-statistic: 1359.80, p-value < 0.001)

### District Analysis
- **Most Expensive District**: Kensington and Chelsea
- **Least Expensive District**: Bexley
- **Statistical Significance**: Mann-Whitney U tests confirmed significant price differences between districts
  - Significant difference between Kensington and Chelsea vs. Bexley (p-value < 0.001)
  - Significant difference between districts with most properties: Wandsworth vs. Lambeth (p-value < 0.001)

### Notable Observations
- Extreme price variation in the London market, with properties ranging from £100 to £138,900,000 in the original dataset
- After outlier removal, the maximum price was capped at £10,000,000
- Flat/Apartment is overwhelmingly the dominant property type in London

## Repository Contents
- `London_Property_Analysis.ipynb`: Jupyter notebook containing all code, analysis, and visualizations
- `london_properties_cleaned.csv`: Cleaned dataset focused on London properties
- `README.md`: Project documentation

## Methodology
1. **Data Cleaning**:
   - Removed extreme price outliers
   - Standardized property types
   - Validated and processed date information
   
2. **Exploratory Analysis**:
   - Descriptive statistics for price distribution
   - Property type analysis
   - District/borough comparison

3. **Statistical Testing**:
   - ANOVA for property type price differences
   - Mann-Whitney U tests for district comparisons

## How to Use
1. Clone this repository
2. Ensure you have Jupyter Notebook installed along with required libraries (pandas, matplotlib, seaborn, scipy)
3. Open the `London_Property_Analysis.ipynb` file to view the complete analysis with all visualizations
4. The raw data is available in the CSV file if you wish to conduct your own analysis

## Future Work
- Incorporate historical data to analyze year-over-year trends
- Develop predictive models for property price forecasting
- Analyze the impact of transportation links on property values
- Investigate the relationship between property prices and socioeconomic indicators

---

*This project was completed as part of my data analyst portfolio, demonstrating skills in data cleaning, exploratory data analysis, statistical testing, and data visualization.*
