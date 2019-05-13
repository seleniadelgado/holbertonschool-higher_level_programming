#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (isNaN(w) || isNaN(h) || w <= 0 || h <= 0) {
      let myobj = {};
    } else {
      this.width = w;
      this.height = h;
    }
  }
}
;
