#!/usr/bin/node
// A js script that gets contents
// of a webpage and stores them in a file

const reqst = require('request');
const fs = require('fs');

reqst.get(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(process.argv[3], body, 'utf-8', function (error) {
      if (error) {
        console.log(error);
      }
    });
  }
});
