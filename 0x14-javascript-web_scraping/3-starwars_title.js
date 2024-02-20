#!/usr/bin/node
// Js script that prints title of a star wars movie

const reqst = require('request');
const reqstUrl = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

reqst.get(reqstUrl,
  function (error, response, body) {
    if (error) {
      console.log(error);
    } else {
      const info = JSON.parse(body);
      console.log(info.title);
    }
  });
