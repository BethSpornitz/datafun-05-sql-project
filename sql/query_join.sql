-- query_join.sql

SELECT Artists.name AS artist_name, Songs.title AS song_title
FROM Songs
INNER JOIN Artists ON Songs.artist_id = Artists.artist_id;