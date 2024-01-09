#!/usr/bin/node

const origSquare = require('./5-square');

class Square extends origSquare {
  charPrint (c) {
    c = c ? c : 'X';
    let x = 0;
    while (x < this.height) {
      console.log(c.repeat(this.width));
      x++;
    }
  }
}
module.exports = Square;
