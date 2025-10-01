#!/usr/bin/node
// square.js
const Rectangle = require('./4-rectangle'); // Assuming the previous rectangle.js is named 4-rectangle.js

class Square extends Rectangle {
  constructor (size) {
    // Call the constructor of Rectangle with both width and height as size
    super(size, size);
  }
}

module.exports = Square;
