#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let x = 0;
    while (x < this.height) {
      console.log('X'.repeat(this.width));
      x++;
    }
  }
}
module.exports = Rectangle;
