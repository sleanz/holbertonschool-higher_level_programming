-- Script to list all genres of the show Dexter
-- Usage: mysql hbtn_0d_tvshows < list_dexter_genres.sql

SELECT tv_genres.name 
FROM tv_genres 
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id 
JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id 
WHERE tv_shows.title = 'Dexter' 
ORDER BY tv_genres.name ASC;
