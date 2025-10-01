#!/usr/bin/node

// Get arguments from the command line, excluding the first two elements (node and script path)
const args = process.argv.slice(2).map(Number); // Convert all arguments to integers

if (args.length <= 1) {
  console.log(0); // Print 0 if no arguments or only one argument
} else {
  // Sort in descending order and select the second biggest
  const secondBiggest = args.sort((a, b) => b - a)[1];
  console.log(secondBiggest);
}
