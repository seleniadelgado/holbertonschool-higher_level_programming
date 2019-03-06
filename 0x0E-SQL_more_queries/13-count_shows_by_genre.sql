-- list all genres and display number of Shows linked to each other
SELECT genres.name, 
COUNT(genre.id) AS number_of_shows
FROM tv_show_genres 
INNER JOIN genres
ON genre_id = genres.id
GROUP BY genre.id
ORDER BY number_of_shows DESC;
