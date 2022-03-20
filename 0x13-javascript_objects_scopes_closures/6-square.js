#!/usr/bin/node

const square = require('./5-square');

module.exports = class Square extends square {
  charPrint (c) {
    if (c) {
      this.print(c);
    } else {
      this.print();
    }
  }
};
