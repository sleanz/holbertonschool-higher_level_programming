-- Script to list all TV shows that have at least one genre linked
-- Usage: mysql hbtn_0d_tvshows < list_shows_with_genres.sql

SELECT tv_shows.title, tv_show_genres.genre_id 
FROM tv_shows 
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id 
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
