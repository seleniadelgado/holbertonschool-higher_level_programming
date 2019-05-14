#!/usr/bin/node
const Square1 = require('./5-square');
module.exports = class Square extends Square1 {
  constructor (size) {
    super(size, size);
  }
  charPrint (c) {
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
