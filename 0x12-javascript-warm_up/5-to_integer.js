#!/usr/bin/node

const argv = process.argv;
const input = parseInt(argv[2], 10);
if (!isNaN(input)) console.log('My number: ' + input);
else console.log('Not a number');
