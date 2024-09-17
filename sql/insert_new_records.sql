-- insert_new_records.sql
-- Insert new records into the artists table
INSERT INTO artists (name, birth_year, genre) VALUES
('Queen', 1970, 'Rock'),
('Nirvana', 1987, 'Grunge'),
('Taylor Swift', 1989, 'Pop'),
('The Rolling Stones', 1962, 'Rock'),
('Billie Eilish', 2001, 'Pop'),
('Kanye West', 1977, 'Hip Hop'),
('Ariana Grande', 1993, 'Pop'),
('The Who', 1964, 'Rock'),
('Bruno Mars', 1985, 'Pop'),
('Rihanna', 1988, 'Pop');

-- Insert new records into the songs table
INSERT INTO songs (title, release_year, duration, artist_id) VALUES
('Bohemian Rhapsody', 1975, '5:55', 1),
('Smells Like Teen Spirit', 1991, '5:01', 2),
('Love Story', 2008, '3:55', 3),
('Paint It Black', 1966, '3:22', 4),
('Bad Guy', 2019, '3:14', 5),
('Stronger', 2007, '5:11', 6),
('7 Rings', 2019, '2:59', 7),
('Baba O\Riley', 1971, '5:00', 8),
('Uptown Funk', 2014, '4:30', 9),
('Umbrella', 2007, '4:36', 10);