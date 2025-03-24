-- Query 2: Property Type Analysis
-- Analyzes price, ratings, and review counts by property type

SELECT 
    property_type,
    COUNT(listing_id) AS num_listings,
    ROUND(AVG(price), 2) AS avg_price,
    ROUND(AVG(review_scores_rating), 2) AS avg_rating,
    SUM(number_of_reviews) AS total_reviews,
    ROUND(AVG(CASE WHEN host_is_superhost = TRUE THEN 1.0 ELSE 0.0 END) * 100, 2) AS superhost_percent
FROM 
    listings
WHERE 
    price IS NOT NULL 
    AND review_scores_rating IS NOT NULL
GROUP BY 
    property_type
HAVING 
    COUNT(listing_id) > 10
ORDER BY 
    num_listings DESC;