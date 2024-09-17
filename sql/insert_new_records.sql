-- insert_new_records.sql
-- Insert new records into the artists table
INSERT INTO artists (artist_id, name, birth_year, genre) VALUES
(6, 'Queen', 1970, 'Rock'),
(7, 'Nirvana', 1987, 'Grunge'),
(8, 'Taylor Swift', 1989, 'Pop'),
(9, 'The Rolling Stones', 1962, 'Rock'),
(10, 'Billie Eilish', 2001, 'Pop'),
(11, 'Kanye West', 1977, 'Hip Hop'),
(12, 'Ariana Grande', 1993, 'Pop'),
(13, 'The Who', 1964, 'Rock'),
(14, 'Bruno Mars', 1985, 'Pop'),
(15, 'Rihanna', 1988, 'Pop');

-- Insert new records into the songs table
INSERT INTO songs (song_id, title, release_year, duration, artist_id) VALUES
(11, 'Bohemian Rhapsody', 1975, '5:55', 6),
(12, 'Smells Like Teen Spirit', 1991, '5:01', 7),
(13, 'Love Story', 2008, '3:55', 8),
(14, 'Paint It Black', 1966, '3:22', 9),
(15, 'Bad Guy', 2019, '3:14', 10),
(16, 'Stronger', 2007, '5:11', 11),
(17, '7 Rings', 2019, '2:59', 12),
(18, 'Baba O\Riley', 1971, '5:00', 13),
(19, 'Uptown Funk', 2014, '4:30', 14),
(20, 'Umbrella', 2007, '4:36', 15);