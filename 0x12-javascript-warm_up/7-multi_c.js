#!/usr/bin/node

const argv = process.argv;
let i = parseInt(argv[2], 10);

if (typeof i === 'number') {
  for (; i > 0; i--) {
  console.log('C is fun');	  
  }
} 
else {
  console.log('Missing number of occurances');
}
