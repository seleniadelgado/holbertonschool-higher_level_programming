#!/usr/bin/node
const Rectangle = require('./4-rectangle');
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
  charPrint(c) {
    if (c !== null && c !== undefined) {
      c = 'C';
    } else {
      c = 'X';
    }
    let i;
    for (i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
};
