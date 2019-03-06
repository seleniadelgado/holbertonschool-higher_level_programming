-- list all genres and display number of Shows linked to each other
SELECT genre.name, 
COUNT(genre.id) AS number_of_shows
FROM tv_show_genres 
INNER JOIN genres
ON genre_id = genres.id
ORDER BY number_of_shows DESC;
