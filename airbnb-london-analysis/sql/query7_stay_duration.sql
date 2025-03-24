-- Query 7: Length of Stay Analysis
-- Analyzes minimum night requirements across neighborhoods

SELECT 
    neighbourhood_cleansed AS neighbourhood,
    COUNT(listing_id) AS num_listings,
    ROUND(AVG(minimum_nights), 2) AS avg_minimum_nights,
    ROUND(AVG(maximum_nights), 2) AS avg_maximum_nights,
    COUNT(CASE WHEN minimum_nights = 1 THEN 1 END) AS one_night_stays,
    COUNT(CASE WHEN minimum_nights BETWEEN 2 AND 3 THEN 1 END) AS short_stays,
    COUNT(CASE WHEN minimum_nights BETWEEN 4 AND 6 THEN 1 END) AS medium_stays,
    COUNT(CASE WHEN minimum_nights >= 7 THEN 1 END) AS weekly_plus_stays,
    ROUND(
        COUNT(CASE WHEN minimum_nights = 1 THEN 1 END)::NUMERIC * 100 / 
        COUNT(*),
        2
    ) AS one_night_percent
FROM 
    listings
GROUP BY 
    neighbourhood_cleansed
ORDER BY 
    avg_minimum_nights DESC;