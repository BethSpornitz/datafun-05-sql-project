-- query_group_by.sql

SELECT artist_id, COUNT(song_id) AS number_of_songs
FROM Songs
GROUP BY artist_id;