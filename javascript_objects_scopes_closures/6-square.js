#!/usr/bin/node
// 6-square.js
const Square = require('./5-square'); // Assuming 5-square.js is the previous version

class SquareExtended extends Square {
  charPrint (c) {
    // Use 'X' if c is not defined
    const charToPrint = c === undefined ? 'X' : c;

    // Print the square by iterating over the size of the square
    for (let i = 0; i < this.height; i++) {
      console.log(charToPrint.repeat(this.width));
    }
  }
}

module.exports = SquareExtended;
