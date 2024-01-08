#!/usr/bin/node
const argv = process.argv;
const varOne = parseInt(argv[2], 10);
const varTwo = parseInt(argv[3], 10);
function add(a, b) {
  return (a + b);
}
console.log(add(varOne, varTwo));
