#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }

    Rectangle.prototype.print = function () {
      let i;
      for (i = 0; i < this.height; i++) { console.log('X'.repeat(this.width)); }
    };

    Rectangle.prototype.rotate = function () {
      let x = this.width;
      this.width = this.height;
      this.height = x;
    };
    Rectangle.prototype.double = function () {
      this.width = this.width * 2;
      this.height = this.height * 2;
    };
  }
};
