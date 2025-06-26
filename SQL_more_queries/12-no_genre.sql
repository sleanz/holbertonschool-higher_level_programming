-- Script to list all TV shows without any genre linked
-- Usage: mysql hbtn_0d_tvshows < list_shows_no_genre.sql

SELECT tv_shows.title, tv_show_genres.genre_id 
FROM tv_shows 
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id 
WHERE tv_show_genres.genre_id IS NULL 
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
