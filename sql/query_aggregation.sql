-- query_aggregation.sql

SELECT artist_id, COUNT(*) AS number_of_songs
FROM Songs
GROUP BY artist_id;