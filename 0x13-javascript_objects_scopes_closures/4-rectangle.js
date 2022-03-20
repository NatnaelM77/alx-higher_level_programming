#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print (char) {
    let rectangle = '';
    for (let row = 0; row < this.height; row++) {
      for (let col = 0; col < this.width; col++) {
        rectangle += (char ?? 'X');
      }
      console.log(rectangle);
      rectangle = '';
    }
  }

  rotate () {
    const height = this.height;
    this.height = this.width;
    this.width = height;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
