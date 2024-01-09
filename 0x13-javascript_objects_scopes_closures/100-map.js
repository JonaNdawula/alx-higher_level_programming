#!/usr/bin/node

const ls = require('./100-data').list;
const map = ls.map((a, b) => a * b);
console.log(ls);
console.log(map);
