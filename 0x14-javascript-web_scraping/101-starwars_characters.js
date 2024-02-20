#!/usr/bin/node
// A js script that prints every character
// of a star warks movie

const reqst = require('request');
const movieId = process.argv[2];
const movieUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

reqst.get(movieUrl, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const info = JSON.parse(body);
    const movieChars = info.characters;
    for (const chr of movieChars) {
      reqst.get(chr, function (error, response, body) {
        if (error) {
          console.log(error);
        } else {
          const n = JSON.parse(body);
          console.log(n.name);
        }
      });
    }
  }
});
