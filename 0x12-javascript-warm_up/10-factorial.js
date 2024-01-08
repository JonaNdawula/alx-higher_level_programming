#!/usr/bin/node
const argv = process.argv;
const num = parseInt(argv[2], 10);
function fact (num) {
  if (num === 0 || num === 1) return 1;
  return num * fact(num - 1);
}
if (isNaN(num)) console.log(1);
else console.log(fact(num));
