-- Script to list all TV shows with their genre IDs (including shows without genres)
-- Usage: mysql hbtn_0d_tvshows < list_all_shows.sql

SELECT tv_shows.title, tv_show_genres.genre_id 
FROM tv_shows 
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id 
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
