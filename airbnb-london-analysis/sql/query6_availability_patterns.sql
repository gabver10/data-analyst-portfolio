-- Query 6: Availability Patterns by Neighborhood
-- Analyzes which neighborhoods have highest/lowest availability

WITH availability_data AS (
    SELECT 
        l.neighbourhood_cleansed,
        c.listing_id,
        COUNT(c.date) AS total_dates,
        SUM(CASE WHEN c.available = TRUE THEN 1 ELSE 0 END) AS available_dates
    FROM 
        calendar c
    JOIN 
        listings l ON c.listing_id = l.listing_id
    WHERE 
        c.date BETWEEN CURRENT_DATE AND (CURRENT_DATE + INTERVAL '90 days')
    GROUP BY 
        l.neighbourhood_cleansed, c.listing_id
)
SELECT 
    neighbourhood_cleansed AS neighbourhood,
    COUNT(DISTINCT listing_id) AS num_listings,
    ROUND(AVG(available_dates), 2) AS avg_available_days,
    ROUND(AVG(available_dates * 100.0 / total_dates), 2) AS avg_availability_percent
FROM 
    availability_data
GROUP BY 
    neighbourhood_cleansed
ORDER BY 
    avg_availability_percent;