-- Script that lists all Comedy shows in the database hbtn_0d_tvshows
-- Each record displays: tv_shows.title
-- Results sorted in ascending order by the show title

SELECT tv_shows.title
FROM tv_shows, tv_show_genres, tv_genres
WHERE tv_shows.id = tv_show_genres.show_id
  AND tv_show_genres.genre_id = tv_genres.id
  AND tv_genres.name = 'Comedy'
ORDER BY tv_shows.title;
