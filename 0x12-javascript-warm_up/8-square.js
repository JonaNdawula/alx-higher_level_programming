#!/usr/bin/node 

const argv = process.argv;
let i = 0;
const n = parseInt(argv[2], 10);
if (!isNaN(n)) {
  while (i < n) {
    console.log('X'.repeat(n));
    i++;
  }
} else console.log('Missing size');
