#!/usr/bin/node

const myDict = require('./101-data').dict;
const dictionary = {};
const keys = Object.keys(myDict);
let x = 0;

while (x < keys.length) {
  const ky = keys[x];

  if (dictionary[myDict[ky]] === undefined) {
    dictionary[myDict[ky]] = [];
  }

  dictionary[myDict[ky]].push(ky);
  x++;
}
console.log(dictionary);
