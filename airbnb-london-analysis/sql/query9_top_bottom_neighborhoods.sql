-- Query 9: Top vs Bottom Neighborhoods
-- Compares top-rated and lowest-rated neighborhoods

WITH neighborhood_ratings AS (
    SELECT 
        neighbourhood_cleansed AS neighbourhood,
        COUNT(listing_id) AS num_listings,
        ROUND(AVG(review_scores_rating), 2) AS avg_rating,
        ROUND(AVG(price), 2) AS avg_price,
        RANK() OVER (ORDER BY AVG(review_scores_rating) DESC) AS top_rank,
        RANK() OVER (ORDER BY AVG(review_scores_rating) ASC) AS bottom_rank
    FROM 
        listings
    WHERE 
        review_scores_rating IS NOT NULL
        AND price IS NOT NULL
        AND price > 0
    GROUP BY 
        neighbourhood_cleansed
    HAVING 
        COUNT(listing_id) >= 20
)
SELECT 
    neighbourhood,
    num_listings,
    avg_rating,
    avg_price,
    CASE 
        WHEN top_rank <= 5 THEN 'Top 5'
        WHEN bottom_rank <= 5 THEN 'Bottom 5'
        ELSE 'Middle Tier'
    END AS rating_tier
FROM 
    neighborhood_ratings
WHERE 
    top_rank <= 5 OR bottom_rank <= 5
ORDER BY 
    avg_rating DESC;