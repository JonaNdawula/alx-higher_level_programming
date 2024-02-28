// A JavaScript script that fetches the character name from this 
// URL: https://swapi-api.alx-tools.com/api/people/5/?format=json

let givenUrl = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
$.get(givenUrl, function (dt, st) {
  $('div#character').text(dt.name);
});
