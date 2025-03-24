-- Query 4: Review Sentiment Analysis
-- Analyzes positive and negative keywords in reviews

WITH review_keywords AS (
    SELECT 
        l.neighbourhood_cleansed,
        COUNT(r.id) AS review_count,
        SUM(CASE WHEN r.comments ILIKE '%great%' THEN 1 ELSE 0 END) AS great_count,
        SUM(CASE WHEN r.comments ILIKE '%excellent%' THEN 1 ELSE 0 END) AS excellent_count,
        SUM(CASE WHEN r.comments ILIKE '%amazing%' THEN 1 ELSE 0 END) AS amazing_count,
        SUM(CASE WHEN r.comments ILIKE '%good%' THEN 1 ELSE 0 END) AS good_count,
        SUM(CASE WHEN r.comments ILIKE '%clean%' THEN 1 ELSE 0 END) AS clean_count,
        SUM(CASE WHEN r.comments ILIKE '%dirty%' THEN 1 ELSE 0 END) AS dirty_count,
        SUM(CASE WHEN r.comments ILIKE '%poor%' THEN 1 ELSE 0 END) AS poor_count,
        SUM(CASE WHEN r.comments ILIKE '%bad%' THEN 1 ELSE 0 END) AS bad_count,
        SUM(CASE WHEN r.comments ILIKE '%terrible%' THEN 1 ELSE 0 END) AS terrible_count
    FROM 
        listings l
    JOIN 
        reviews r ON l.listing_id = r.listing_id
    GROUP BY 
        l.neighbourhood_cleansed
)
SELECT 
    neighbourhood_cleansed AS neighbourhood,
    review_count,
    (great_count + excellent_count + amazing_count + good_count + clean_count) AS positive_mentions,
    (dirty_count + poor_count + bad_count + terrible_count) AS negative_mentions,
    ROUND(
        (great_count + excellent_count + amazing_count + good_count + clean_count)::NUMERIC /
        NULLIF((dirty_count + poor_count + bad_count + terrible_count), 0), 
        2
    ) AS positive_to_negative_ratio,
    ROUND(
        (great_count + excellent_count + amazing_count + good_count + clean_count)::NUMERIC * 100 /
        NULLIF(review_count, 0), 
        2
    ) AS positive_percent
FROM 
    review_keywords
WHERE 
    review_count > 100
ORDER BY 
    positive_to_negative_ratio DESC;