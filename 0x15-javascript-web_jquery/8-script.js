// A JavaScript script that fetches and lists the 
// title for all movies by using this URL

let givenUrl = 'https://swapi-api.alx-tools.com/api/films/?format=json';
$.get(givenUrl, function (dt) {
  let movies = dt.results;
  for (let movie of movies) {
    $('ul#list_movies').append(`<li>${movie.title}</li>`);
  }
});
