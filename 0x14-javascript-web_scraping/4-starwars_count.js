#!/usr/bin/node
// A js script that prints the number of
// movies where the character "Wedge Antilles"
// is present

const reqst = require('request');
let numOfMovies = 0;

reqst.get(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const info = JSON.parse(body);
    info.results.forEach(function (movie) {
      movie.characters.forEach(function (character) {
        if (character.includes(18)) {
          numOfMovies += 1;
        }
      });
    });
    console.log(numOfMovies);
  }
});
