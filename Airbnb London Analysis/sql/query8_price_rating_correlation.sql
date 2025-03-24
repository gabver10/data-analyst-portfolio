-- Query 8: Price-Rating Correlation Analysis
-- Analyzes relationship between price and different rating categories

SELECT 
    CASE
        WHEN price < 50 THEN 'Under £50'
        WHEN price BETWEEN 50 AND 99 THEN '£50-99'
        WHEN price BETWEEN 100 AND 149 THEN '£100-149'
        WHEN price BETWEEN 150 AND 199 THEN '£150-199'
        WHEN price BETWEEN 200 AND 299 THEN '£200-299'
        WHEN price >= 300 THEN '£300+'
    END AS price_category,
    COUNT(listing_id) AS num_listings,
    ROUND(AVG(review_scores_rating), 2) AS overall_rating,
    ROUND(AVG(review_scores_cleanliness), 2) AS cleanliness_rating,
    ROUND(AVG(review_scores_location), 2) AS location_rating,
    ROUND(AVG(review_scores_value), 2) AS value_rating,
    ROUND(AVG(number_of_reviews), 0) AS avg_reviews
FROM 
    listings
WHERE 
    price IS NOT NULL 
    AND price > 0 
    AND price < 1000
    AND review_scores_rating IS NOT NULL
GROUP BY 
    price_category
ORDER BY 
    MIN(price);