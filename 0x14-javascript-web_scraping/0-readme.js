#!/usr/bin/node
// Js script to read and print file content

const fs = require('fs');
fs.readFile(process.argv[2], 'utf-8',
  function (error, data) {
    if (error) {
      console.log(error);
      return;
    }
    else {
    console.log(data);
    }
  });    
