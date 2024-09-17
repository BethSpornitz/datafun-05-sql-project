-- Start by deleting any tables if the exist already
-- We want to be able to re-run this script as needed.
-- DROP tables in reverse order of creation 
-- DROP dependent tables (with foreign keys) first

DROP TABLE IF EXISTS songs;
DROP TABLE IF EXISTS artists;

-- Create the artists table
-- Note that the songs table has a foreign key to the artists table
-- This means that the songs table is dependent on the artists table
-- Be sure to create the standalone artists table BEFORE creating the songs table.

CREATE TABLE artists (
    artist_id INTEGER PRIMARY KEY,
    name TEXT,
    birth_year INTEGER,
    genre TEXT
);

-- Create the songs table 
-- Note that the artists table has no foreign keys, so it is a standalone table

CREATE TABLE songs (
    song_id INTEGER PRIMARY KEY,
    title TEXT,
    release_year INTEGER,
    duration TEXT,
    artist_ID INTEGER,
    FOREIGN KEY (artist_id) REFERENCES Artists (artist_id)
);