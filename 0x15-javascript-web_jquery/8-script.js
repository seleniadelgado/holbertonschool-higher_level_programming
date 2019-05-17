$.get('https://swapi.co/api/films/?format=json', function (data) {
  for (let movie of data.results) { $('ul#list_movies').append('<li>' + movie.title + '</li>'); }
});
