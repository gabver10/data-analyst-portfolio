-- Query 3: Seasonal Booking Trends
-- Analyzes pricing and availability patterns by month

SELECT 
    EXTRACT(MONTH FROM date) AS month,
    TO_CHAR(TO_DATE(EXTRACT(MONTH FROM date)::text, 'MM'), 'Month') AS month_name,
    COUNT(DISTINCT listing_id) AS active_listings,
    ROUND(AVG(price), 2) AS avg_price,
    ROUND(AVG(CASE WHEN available = TRUE THEN 1.0 ELSE 0.0 END) * 100, 2) AS availability_rate
FROM 
    calendar
WHERE 
    date BETWEEN CURRENT_DATE - INTERVAL '1 year' AND CURRENT_DATE + INTERVAL '3 months'
    AND price IS NOT NULL
GROUP BY 
    EXTRACT(MONTH FROM date),
    TO_CHAR(TO_DATE(EXTRACT(MONTH FROM date)::text, 'MM'), 'Month')
ORDER BY 
    month;