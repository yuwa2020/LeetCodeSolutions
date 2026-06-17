# Write your MySQL query statement below
WITH B AS (
SELECT player_id, MIN(event_date) AS event_date
FROM Activity
GROUP BY player_id
), A AS (
SELECT a.player_id, a.event_date
FROM Activity a
JOIN B as b
ON a.player_id = b.player_id
AND DATEDIFF(a.event_date, b.event_date) = 1
)

SELECT 
    ROUND((SELECT COUNT(*) FROM A) / (SELECT COUNT(*) FROM B ), 2) AS fraction
