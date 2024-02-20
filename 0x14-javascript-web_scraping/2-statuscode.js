#!/usr/bin/node
// A js script that displays the status code of GET
// Request

const reqst = require('request');
const reqsturl = process.argv[2];
reqst.get(reqsturl,
  function (error, response) {
    if (error) {
      console.log(error);
    } else {
      console.log(`code: ${response.statusCode}`);
    }
  });
