#!/usr/bin/node

const OrigSquare = require('./5-square');

class Square extends OrigSquare {
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
