/*
 * London Airbnb Neighborhood Analysis
 * This query analyzes performance metrics across all London neighborhoods
 * Author: Gabriele Vertullo
 */

-- NEIGHBORHOOD PERFORMANCE METRICS
SELECT 
    n.neighbourhood,
    COUNT(DISTINCT l.listing_id) AS num_listings,
    ROUND(AVG(l.price), 2) AS avg_listing_price,
    ROUND(AVG(c.price), 2) AS avg_calendar_price,
    ROUND(AVG(l.review_scores_rating), 2) AS avg_rating,
    COUNT(DISTINCT r.id) AS total_reviews,
    ROUND(AVG(LENGTH(r.comments)), 0) AS avg_review_length,
    ROUND(100.0 * SUM(CASE WHEN c.available = true THEN 1 ELSE 0 END) / COUNT(*), 2) AS availability_rate,
    ROUND(100.0 * COUNT(DISTINCT CASE WHEN l.host_is_superhost = true THEN l.host_id END) / 
          NULLIF(COUNT(DISTINCT l.host_id), 0), 2) AS superhost_percentage,
    ROUND(AVG(CASE 
        WHEN r.date > '2023-01-01' THEN l.review_scores_rating 
        ELSE NULL 
    END), 2) AS recent_avg_rating
FROM 
    listings l
JOIN 
    neighbourhoods n ON l.neighbourhood_cleansed = n.neighbourhood
LEFT JOIN 
    reviews r ON l.listing_id = r.listing_id
LEFT JOIN 
    calendar c ON l.listing_id = c.listing_id
            AND c.date BETWEEN CURRENT_DATE - INTERVAL '90 days' AND CURRENT_DATE + INTERVAL '90 days'
WHERE 
    l.review_scores_rating IS NOT NULL
GROUP BY 
    n.neighbourhood
ORDER BY 
    num_listings DESC;