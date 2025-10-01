#!/usr/bin/node
// rectangle.js
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0 && Number.isInteger(w) && Number.isInteger(h)) {
      this.width = w;
      this.height = h;
    } else {
      // Create an empty object by not initializing width and height
    }
  }
}

module.exports = Rectangle;
