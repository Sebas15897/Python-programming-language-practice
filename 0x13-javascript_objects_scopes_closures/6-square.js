#!/usr/bin/node
const S = require('./5-square');

class Square extends S {
  charPrint (c) {
    if (!c) {
      c = 'X';
    }
    for (let j = this.height; j; j--) {
      console.log(c.repeat(this.width));
    }
  }
}
module.exports = Square;
