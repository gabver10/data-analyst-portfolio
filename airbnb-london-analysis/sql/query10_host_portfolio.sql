-- Query 10: Host Portfolio Size Analysis
-- Analyzes how host portfolio size relates to performance


WITH host_listings AS (
    SELECT 
        host_id,
        host_name,
        COUNT(listing_id) AS num_listings,
        CASE 
            WHEN COUNT(listing_id) = 1 THEN 'Single Listing'
            WHEN COUNT(listing_id) BETWEEN 2 AND 5 THEN '2-5 Listings'
            WHEN COUNT(listing_id) BETWEEN 6 AND 20 THEN '6-20 Listings'
            ELSE '20+ Listings'
        END AS host_category
    FROM listings
    GROUP BY host_id, host_name
),
superhost_status AS (
    SELECT DISTINCT host_id
    FROM listings
    WHERE host_is_superhost = TRUE
)
SELECT 
    h.host_category,
    COUNT(DISTINCT h.host_id) AS num_hosts,
    SUM(h.num_listings) AS total_listings,
    ROUND(AVG(h.num_listings), 2) AS avg_listings_per_host,
    ROUND(AVG(l.price), 2) AS avg_price,
    ROUND(AVG(l.review_scores_rating), 2) AS avg_rating,
    ROUND(
        COUNT(DISTINCT s.host_id)::NUMERIC * 100 / COUNT(DISTINCT h.host_id),
        2
    ) AS superhost_percent
FROM 
    host_listings h
JOIN 
    listings l ON h.host_id = l.host_id
LEFT JOIN 
    superhost_status s ON h.host_id = s.host_id
WHERE 
    l.review_scores_rating IS NOT NULL
    AND l.price IS NOT NULL
GROUP BY 
    h.host_category
ORDER BY 
    avg_listings_per_host;
