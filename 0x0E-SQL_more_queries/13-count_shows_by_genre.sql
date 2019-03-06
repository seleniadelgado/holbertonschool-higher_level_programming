-- list all genres and display number of Shows linked to each other
SELECT tv_genres.name AS genre, 
COUNT(genre_id) AS number_of_shows
FROM tv_show_genres 
INNER JOIN tv_genres
ON genre_id = tv_genres.id
GROUP BY tv_genres.name
ORDER BY COUNT(genre_id) DESC;
