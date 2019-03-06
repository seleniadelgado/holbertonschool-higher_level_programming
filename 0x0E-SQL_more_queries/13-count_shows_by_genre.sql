-- list all genres and display number of Shows linked to each other

SELECT tv_show_genres.genre_id
FROM tv_show_genres
COUNT(*) AS number_of_shows
ON tv_show_genres.show_id = tv_shows.id
