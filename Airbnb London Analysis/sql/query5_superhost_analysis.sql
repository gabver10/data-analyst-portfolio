-- Query 5: Superhost Performance Analysis
-- Compares superhosts vs. regular hosts

SELECT 
    CASE 
        WHEN host_is_superhost = TRUE THEN 'Superhost'
        ELSE 'Regular Host'
    END AS host_type,
    COUNT(DISTINCT host_id) AS host_count,
    COUNT(listing_id) AS listing_count,
    ROUND(COUNT(listing_id)::NUMERIC / COUNT(DISTINCT host_id), 2) AS avg_listings_per_host,
    ROUND(AVG(price), 2) AS avg_price,
    ROUND(AVG(review_scores_rating), 2) AS avg_rating,
    ROUND(AVG(number_of_reviews), 2) AS avg_reviews,
    ROUND(AVG(reviews_per_month), 2) AS avg_reviews_per_month,
    ROUND(
        SUM(CASE WHEN instant_bookable = TRUE THEN 1 ELSE 0 END)::NUMERIC * 100 / 
        COUNT(listing_id), 
        2
    ) AS instant_bookable_percent
FROM 
    listings
WHERE 
    host_is_superhost IS NOT NULL
    AND review_scores_rating IS NOT NULL
GROUP BY 
    host_type
ORDER BY 
    host_type;